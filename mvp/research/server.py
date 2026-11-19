"""Tiny OpenAI-compatible server so the chat app can offer "Investigación profunda" as a model.
It streams progress lines while the research runs, then the final report with sources and cost."""
import json, os, threading, queue, time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import research

MODEL = "deep-research"

class H(BaseHTTPRequestHandler):
    def _json(self, code, obj):
        b = json.dumps(obj).encode()
        self.send_response(code); self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(b))); self.end_headers(); self.wfile.write(b)

    def do_GET(self):
        if self.path.rstrip("/").endswith("/models"):
            return self._json(200, {"object": "list", "data": [{"id": MODEL, "object": "model", "owned_by": "local"}]})
        self._json(200, {"status": "ok"})

    def do_POST(self):
        if not self.path.endswith("/chat/completions"):
            return self._json(404, {"error": "not found"})
        req = json.loads(self.rfile.read(int(self.headers.get("Content-Length", 0))) or b"{}")
        msgs = [m for m in req.get("messages", []) if m.get("role") == "user"]
        question = msgs[-1]["content"] if msgs else ""
        if isinstance(question, list):  # content parts
            question = " ".join(p.get("text", "") for p in question if isinstance(p, dict))
        stream = bool(req.get("stream"))
        q = queue.Queue()
        result = {}

        def work():
            cost = {}
            try:
                r, s, i = research.run(question, progress=lambda m: q.put(f"_{m}_\n\n"), cost=cost)
                result["text"] = "\n---\n\n" + research.render(r, s, i, cost)
            except Exception as e:
                result["text"] = f"\n\nError durante la investigación: {e}"
            q.put(None)
        threading.Thread(target=work, daemon=True).start()

        def chunk(text, finish=None):
            return "data: " + json.dumps({"id": "dr-1", "object": "chat.completion.chunk", "created": int(time.time()),
                "model": MODEL, "choices": [{"index": 0, "delta": {"content": text} if text else {}, "finish_reason": finish}]}) + "\n\n"

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
            self._json(200, {"id": "dr-1", "object": "chat.completion", "model": MODEL, "choices": [
                {"index": 0, "message": {"role": "assistant", "content": "".join(parts) + result["text"]}, "finish_reason": "stop"}]})

    def log_message(self, *a):
        pass

if __name__ == "__main__":
    ThreadingHTTPServer(("0.0.0.0", int(os.environ.get("PORT", "8000"))), H).serve_forever()
