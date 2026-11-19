"""Tiny OpenAI-compatible server so the chat app can offer "Investigación profunda" as a model.
It streams progress lines while the research runs, then the final report with sources and cost."""
import json, os, threading, queue, time, urllib.parse
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import re, unicodedata, urllib.error, urllib.request
import research, documents, usage

GATEWAY, KEY = usage.GATEWAY, usage.KEY
VERB = r"(haz(me)?|crea(me)?|genera(me)?|prepara(me)?|redacta(me)?|monta(me)?|necesito|quiero|dame|make|create|generate|draft|prepare)"
NOUN = r"(excel|hoja de calculo|spreadsheet|word|\.docx|pdf|presentacion|powerpoint|ppt|diapositivas|slides|plantilla|documento|contrato|presupuesto|factura)"

def wants_document(msgs):
    """Free keyword check, so the user never has to pick 'create a file' from a menu."""
    if re.search(r"title for the conversation|5-word|5 words or less|memory", last_user(msgs).lower()):
        return False  # background jobs (conversation titles, memory) must never create files
    last = "".join(c for c in unicodedata.normalize("NFD", last_user(msgs).lower()) if unicodedata.category(c) != "Mn")
    prev = [m for m in msgs if m.get("role") == "assistant"]
    if prev and "Tu documento:" in text_of(prev[-1]["content"]) and len(last) < 300:
        return True   # follow-up edit of the file we just made ("hazlo más corto")
    return bool(re.search(VERB + r".{0,60}" + NOUN, last))

FILES_DIR = documents.FILES_DIR
FLOWS = {  # model name -> function(conversation_messages, progress, cost) -> final markdown
    "deep-research": lambda msgs, progress, cost: "\n---\n\n" + research.render(*research.run(last_user(msgs), progress=progress, cost=cost), cost),
    "crear-documento": lambda msgs, progress, cost: "\n---\n\n" + documents.create(transcript(msgs), progress, cost),
}

def text_of(c):
    return " ".join(p.get("text", "") for p in c if isinstance(p, dict)) if isinstance(c, list) else (c or "")

def last_user(msgs):
    u = [m for m in msgs if m.get("role") == "user"]
    return text_of(u[-1]["content"]) if u else ""

def transcript(msgs):
    return "\n\n".join(f"{m['role'].upper()}: {text_of(m['content'])[:6000]}" for m in msgs if m.get("role") in ("user", "assistant"))[-20000:]

class H(BaseHTTPRequestHandler):
    def _json(self, code, obj):
        b = json.dumps(obj).encode()
        self.send_response(code); self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(b))); self.end_headers(); self.wfile.write(b)

    def do_GET(self):
        if self.path.rstrip("/").endswith("/models"):
            return self._json(200, {"object": "list", "data": [{"id": m, "object": "model", "owned_by": "local"} for m in ["asistente", *FLOWS]]})
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

    def passthrough(self, req, model):
        req = dict(req, model=model)
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
        while chunk := resp.read1(8192) if hasattr(resp, "read1") else resp.read(8192):
            self.wfile.write(chunk); self.wfile.flush()

    def do_POST(self):
        if not self.path.endswith("/chat/completions"):
            return self._json(404, {"error": "not found"})
        req = json.loads(self.rfile.read(int(self.headers.get("Content-Length", 0))) or b"{}")
        msgs = req.get("messages", [])
        model = req.get("model")
        if model == "asistente":   # front door for normal chat: files go to our tools, the rest to the model router
            if not wants_document(msgs):
                return self.passthrough(req, "auto")
            model = "crear-documento"
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

        def chunk(text, finish=None):
            return "data: " + json.dumps({"id": "dr-1", "object": "chat.completion.chunk", "created": int(time.time()),
                "model": "deep-research", "choices": [{"index": 0, "delta": {"content": text} if text else {}, "finish_reason": finish}]}) + "\n\n"

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
