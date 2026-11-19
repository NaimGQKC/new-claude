"""'Mi gasto' page: what the team has spent this month, in plain words. Reads LiteLLM's spend log."""
import json, os, time, urllib.request
from collections import defaultdict
from html import escape

GATEWAY = os.environ.get("GATEWAY_URL", "http://localhost:4000")
KEY = os.environ.get("GATEWAY_KEY", "sk-test")
MARKUP = float(os.environ.get("MARKUP", "0.30"))          # our fee on top of the real model cost
EUR_PER_USD = float(os.environ.get("EUR_PER_USD", "0.92"))

def month_logs():
    start = time.strftime("%Y-%m-01")
    req = urllib.request.Request(f"{GATEWAY}/spend/logs?start_date={start}&end_date={time.strftime('%Y-%m-%d', time.gmtime(time.time()+86400))}",
                                 headers={"Authorization": "Bearer " + KEY})
    return json.load(urllib.request.urlopen(req, timeout=20))

def summarize(logs):
    days, total, n = defaultdict(float), 0.0, 0
    for r in logs:
        c = float(r.get("spend") or 0)
        total += c; n += 1; days[str(r.get("startTime", ""))[:10]] += c
    return total, n, days

def page(logs=None, error=None):
    total, n, days = summarize(logs or [])
    price = total * (1 + MARKUP) * EUR_PER_USD
    rows = "".join(f"<tr><td>{escape(d)}</td><td>{v*(1+MARKUP)*EUR_PER_USD:.2f} €</td></tr>" for d, v in sorted(days.items(), reverse=True)[:31])
    note = f"<p class='err'>No se pudo leer el gasto: {escape(error)}</p>" if error else ""
    return f"""<!doctype html><html lang="es"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Mi gasto</title><style>
body{{font:20px/1.5 system-ui,sans-serif;max-width:720px;margin:2rem auto;padding:0 16px;color:#1d1d1f;background:#fff}}
.big{{font-size:56px;font-weight:700;margin:.2em 0}}.card{{border:2px solid #d0d7e2;border-radius:16px;padding:20px;margin:16px 0}}
table{{width:100%;border-collapse:collapse}}td{{padding:10px;border-bottom:1px solid #e5e8ee}}a{{color:#1a56c4}}.err{{color:#b00020}}
@media (prefers-color-scheme:dark){{body{{background:#111;color:#eee}}.card{{border-color:#333}}td{{border-color:#333}}a{{color:#8ab4ff}}}}
</style><h1>Mi gasto este mes</h1>{note}
<div class="card"><div>Hasta hoy llevas</div><div class="big">{price:.2f} €</div>
<div>en {n} respuestas. Pagas solo lo que usas, sin cuota por persona.</div></div>
<h2>Día a día</h2><table>{rows or '<tr><td>Todavía no hay uso este mes.</td></tr>'}</table>
<p><a href="/">← Volver al asistente</a></p></html>"""

def render():
    try:
        return page(month_logs())
    except Exception as e:
        return page([], str(e))


_cache = {"t": 0, "eur": None}
def spent_eur():
    """This month's spend in euros (what the customer pays). None if the spend log can't be read."""
    if time.time() - _cache["t"] > 60:
        try:
            total = summarize(month_logs())[0]
            _cache.update(t=time.time(), eur=total * (1 + MARKUP) * EUR_PER_USD)
        except Exception:
            _cache.update(t=time.time(), eur=None)
    return _cache["eur"]
