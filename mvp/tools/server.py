"""Tiny OpenAI-compatible server so the chat app can offer "Investigación profunda" as a model.
It streams progress lines while the research runs, then the final report with sources and cost."""
import json, os, threading, queue, time, urllib.parse
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import re, unicodedata, urllib.error, urllib.request
import research, documents, images, usage, frontdoor
from frontdoor import last_user, transcript

GATEWAY, KEY = usage.GATEWAY, usage.KEY
CAP_EUR = float(os.environ.get("MONTHLY_CAP_EUR", "0"))      # 0 = no cap

def cap_status():
    """('over'|'near'|'ok', spent). Never blocks when the spend log can't be read."""
    spent = usage.spent_eur() if CAP_EUR > 0 else None
    if spent is None: return "ok", spent
    return ("over" if spent >= CAP_EUR else "near" if spent >= 0.8 * CAP_EUR else "ok"), spent
FILES_DIR = documents.FILES_DIR
FLOWS = {  # model name -> function(conversation_messages, progress, cost) -> final markdown
    "deep-research": lambda msgs, progress, cost: "\n---\n\n" + research.render(*research.run(last_user(msgs), depth=research.choose_depth(last_user(msgs)), progress=progress, cost=cost), cost),
    "crear-documento": lambda msgs, progress, cost: "\n---\n\n" + documents.create(transcript(msgs), progress, cost),
    "crear-imagen": lambda msgs, progress, cost: "\n---\n\n" + images.create(transcript(msgs), progress, cost),
}

text_of_system = lambda m: frontdoor.text_of(m.get("content"))

def sse_chunk(text, finish=None, model="asistente"):
    return "data: " + json.dumps({"id": "dr-1", "object": "chat.completion.chunk", "created": int(time.time()), "model": model,
        "choices": [{"index": 0, "delta": {"content": text} if text else {}, "finish_reason": finish}]}) + "\n\n"

class H(BaseHTTPRequestHandler):
    def _json(self, code, obj):
        b = json.dumps(obj).encode()
        self.send_response(code); self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(b))); self.end_headers(); self.wfile.write(b)

    def do_GET(self):
        if self.path.rstrip("/").endswith("/models"):
            return self._json(200, {"object": "list", "data": [{"id": m, "object": "model", "owned_by": "local"} for m in ["asistente", "pensar-mas", *FLOWS]]})
        if self.path.startswith("/gasto"):
            b = usage.render().encode()
            self.send_response(200); self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(b))); self.end_headers(); return self.wfile.write(b)
        if self.path.startswith("/files/"):
            p = os.path.realpath(os.path.join(FILES_DIR, urllib.parse.unquote(self.path[len("/files/"):])))
            if p.startswith(os.path.realpath(FILES_DIR) + os.sep) and os.path.isfile(p):
                b = open(p, "rb").read()
                self.send_response(200); self.send_header("Content-Type", "application/octet-stream")
                self.send_header("Content-Disposition", 'attachment; filename="%s"' % os.path.basename(p))
                self.send_header("Content-Length", str(len(b))); self.end_headers(); return self.wfile.write(b)
            return self._json(404, {"error": "not found"})
        self._json(200, {"status": "ok"})

    def canned(self, req, text):
        """Reply with fixed text (no model call, no cost)."""
        if req.get("stream"):
            self.send_response(200); self.send_header("Content-Type", "text/event-stream"); self.end_headers()
            self.wfile.write((sse_chunk(text) + sse_chunk("", "stop") + "data: [DONE]\n\n").encode()); return
        self._json(200, {"id": "c-1", "object": "chat.completion", "model": "asistente", "choices": [
            {"index": 0, "message": {"role": "assistant", "content": text}, "finish_reason": "stop"}]})

    def passthrough(self, req, model, system="", notice=""):
        req = dict(req, model=model)
        if system:   # industry pack instructions go first
            msgs = list(req.get("messages", []))
            if msgs and msgs[0].get("role") == "system":
                msgs[0] = dict(msgs[0], content=text_of_system(msgs[0]) + "\n\n" + system)
            else:
                msgs.insert(0, {"role": "system", "content": system})
            req["messages"] = msgs
        r = urllib.request.Request(GATEWAY + "/v1/chat/completions", json.dumps(req).encode(),
                                   {"Content-Type": "application/json", "Authorization": "Bearer " + KEY})
        try:
            resp = urllib.request.urlopen(r, timeout=600)
        except urllib.error.HTTPError as e:
            return self._json(e.code, json.loads(e.read() or b"{}"))
        except Exception as e:
            return self._json(502, {"error": {"message": f"No se pudo contactar con el modelo: {e}"}})
        self.send_response(200); self.send_header("Content-Type", resp.headers.get("Content-Type", "application/json"))
        self.send_header("Cache-Control", "no-cache"); self.end_headers()
        if notice and req.get("stream"):
            self.wfile.write(sse_chunk(notice).encode()); self.wfile.flush()
        while chunk := resp.read1(8192) if hasattr(resp, "read1") else resp.read(8192):
            self.wfile.write(chunk); self.wfile.flush()

    def do_POST(self):
        if not self.path.endswith("/chat/completions"):
            return self._json(404, {"error": "not found"})
        req = json.loads(self.rfile.read(int(self.headers.get("Content-Length", 0))) or b"{}")
        msgs = req.get("messages", [])
        model = req.get("model")
        if model in ("asistente", "pensar-mas", "deep-research", "crear-documento", "crear-imagen"):
            cap, spent = cap_status()
            if cap == "over":
                return self.canned(req, f"Este mes has llegado al límite de gasto que fijaste ({frontdoor.fmt(CAP_EUR)}). "
                                        "Para seguir, pide a la persona que administra la cuenta que lo amplíe. Tus conversaciones y archivos siguen aquí.")
        if model in ("asistente", "pensar-mas"):   # front door: files and images go to our tools, the rest to the cheapest fitting model
            msgs, state = frontdoor.resolve_confirmation(msgs)
            if state == "declined":
                return self.canned(req, "De acuerdo, no lo hago. Si quieres, dime qué parte te interesa y lo hago más pequeño y barato.")
            req = dict(req, messages=msgs)
            d = frontdoor.decide(msgs, confirmed=(state == "confirmed"))
            frontdoor.log(d)
            if d["action"] == "ask":
                return self.canned(req, d["ask"])
            if d["action"] == "chat":
                if model == "pensar-mas":
                    d["model"] = "auto-think"
                if cap == "near":
                    d["notice"] += f"_Ojo: llevas {frontdoor.fmt(spent)} de tu límite mensual de {frontdoor.fmt(CAP_EUR)}._\n\n"
                return self.passthrough(req, d["model"], d["system"], d["notice"])
            model = "crear-documento" if d["action"] == "document" else "crear-imagen"
        elif model not in FLOWS:
            model = "deep-research"
        stream = bool(req.get("stream"))
        q = queue.Queue()
        result = {}

        def work():
            cost = {}
            try:
                result["text"] = FLOWS[model](msgs, lambda m: q.put(f"_{m}_\n\n"), cost)
            except Exception as e:
                result["text"] = f"\n\nError durante la investigación: {e}"
            q.put(None)
        threading.Thread(target=work, daemon=True).start()

        chunk = sse_chunk

        if stream:
            self.send_response(200); self.send_header("Content-Type", "text/event-stream")
            self.send_header("Cache-Control", "no-cache"); self.end_headers()
            while (m := q.get()) is not None:
                self.wfile.write(chunk(m).encode()); self.wfile.flush()
            self.wfile.write(chunk(result["text"]).encode()); self.wfile.write(chunk("", "stop").encode())
            self.wfile.write(b"data: [DONE]\n\n"); self.wfile.flush()
        else:
            parts = []
            while (m := q.get()) is not None:
                parts.append(m)
            self._json(200, {"id": "dr-1", "object": "chat.completion", "model": model, "choices": [
                {"index": 0, "message": {"role": "assistant", "content": "".join(parts) + result["text"]}, "finish_reason": "stop"}]})

    def log_message(self, *a):
        pass

if __name__ == "__main__":
    ThreadingHTTPServer(("0.0.0.0", int(os.environ.get("PORT", "8000"))), H).serve_forever()
