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
    req = urllib.request.Request(f"{GATEWAY}/spend/logs?summarize=false&start_date={start}&end_date={time.strftime('%Y-%m-%d', time.gmtime(time.time()+86400))}",
                                 headers={"Authorization": "Bearer " + KEY})
    return json.load(urllib.request.urlopen(req, timeout=20))

STATE_DIR = os.environ.get("STATE_DIR", "/data/state")
SETTINGS = os.path.join(STATE_DIR, "settings.json")
_tokens = set()          # one-time tokens for the admin form (simple CSRF protection)

def load_settings():
    try:
        return json.load(open(SETTINGS))
    except Exception:
        return {}

def get_cap():
    """Monthly limit in euros set by the admin on the spend page; falls back to MONTHLY_CAP_EUR. 0 = no limit."""
    s = load_settings()
    return float(s["cap_eur"]) if "cap_eur" in s else float(os.environ.get("MONTHLY_CAP_EUR", "0"))

def set_cap(value):
    os.makedirs(STATE_DIR, exist_ok=True)
    s = load_settings(); s["cap_eur"] = max(0.0, float(value))
    json.dump(s, open(SETTINGS, "w")); _cache["t"] = 0

def summarize(logs):
    days, people, total, n = defaultdict(float), defaultdict(float), 0.0, 0
    for r in logs:
        c = float(r.get("spend") or 0)
        who = r.get("end_user") or r.get("user") or "(sin identificar)"
        if who in ("default_user_id", "None", ""): who = "(sin identificar)"
        total += c; n += 1; days[str(r.get("startTime", ""))[:10]] += c; people[who] += c
    return total, n, days, people

def _eur(usd):
    return usd * (1 + MARKUP) * EUR_PER_USD

STYLE = """<style>
body{font:20px/1.5 system-ui,sans-serif;max-width:760px;margin:2rem auto;padding:0 16px;color:#1d1d1f;background:#fff}
.big{font-size:56px;font-weight:700;margin:.2em 0}.card{border:2px solid #d0d7e2;border-radius:16px;padding:20px;margin:16px 0}
table{width:100%;border-collapse:collapse}td,th{padding:10px;border-bottom:1px solid #e5e8ee;text-align:left}a{color:#1a56c4}.err{color:#b00020}
input{font:inherit;padding:8px;width:7em}button{font:inherit;padding:10px 18px;border-radius:10px;border:0;background:#1a56c4;color:#fff;cursor:pointer}
@media (prefers-color-scheme:dark){body{background:#111;color:#eee}.card{border-color:#333}td,th{border-color:#333}a{color:#8ab4ff}}
</style>"""

def page(logs=None, error=None, saved=False):
    import secrets
    total, n, days, people = summarize(logs or [])
    price = _eur(total)
    cap = get_cap()
    token = secrets.token_hex(8); _tokens.add(token)
    p_rows = "".join(f"<tr><td>{escape(w)}</td><td>{_eur(v):.2f} €</td></tr>" for w, v in sorted(people.items(), key=lambda x: -x[1]))
    d_rows = "".join(f"<tr><td>{escape(d)}</td><td>{_eur(v):.2f} €</td></tr>" for d, v in sorted(days.items(), reverse=True)[:31])
    note = f"<p class='err'>No se pudo leer el gasto: {escape(error)}</p>" if error else ""
    ok = "<p>✔ Límite guardado.</p>" if saved else ""
    pct = f" ({price / cap * 100:.0f}% del límite)" if cap > 0 else ""
    return f"""<!doctype html><html lang="es"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Gasto del equipo</title>{STYLE}<h1>Gasto del equipo este mes</h1>{note}{ok}
<div class="card"><div>Hasta hoy el equipo lleva</div><div class="big">{price:.2f} €</div>
<div>en {n} respuestas{pct}. Solo se paga lo que se usa, sin cuota por persona. Aquí no se ve el contenido de ninguna conversación.</div></div>
<div class="card"><form method="post" action="/gasto/cap"><b>Límite mensual</b> (0 = sin límite)<br>
<input name="cap" value="{cap:g}" inputmode="decimal"> € <input type="hidden" name="token" value="{token}"> <button>Guardar</button></form>
<small>Al 80% se avisa a los usuarios; al 100% el asistente se detiene hasta el mes siguiente o hasta que subas el límite.</small></div>
<h2>Por persona</h2><table>{p_rows or '<tr><td>Todavía no hay uso este mes.</td></tr>'}</table>
<h2>Día a día</h2><table>{d_rows or '<tr><td>Todavía no hay uso este mes.</td></tr>'}</table>
<p><a href="/">← Volver al asistente</a></p></html>"""

def render(saved=False):
    try:
        return page(month_logs(), saved=saved)
    except Exception as e:
        return page([], str(e), saved)

def privacy_page():
    mode = os.environ.get("HOSTING_MODE", "test")
    days = os.environ.get("RETENTION_DAYS", "90")
    hosts = escape(os.environ.get("MODEL_HOSTS", "proveedores de IA con servidores en la Unión Europea"))
    if mode == "eu":
        banner = ""
        models = (f"<p>Tus mensajes se envían a modelos de IA alojados por: <b>{hosts}</b>. Tenemos acuerdo con ellos para que "
                  "<b>no guarden tus mensajes ni los usen para entrenar modelos</b>. Los creadores de los modelos (por ejemplo, empresas de China) "
                  "<b>nunca reciben tus datos</b>: solo publican el modelo, que funciona en servidores europeos.</p>")
    else:
        banner = "<div class='card'><b>Versión de prueba.</b> Los mensajes pasan por un servicio que no garantiza que los datos se queden en la UE. <b>No escribas datos reales de clientes.</b></div>"
        models = "<p>Mientras dure la prueba, los mensajes se envían a modelos de IA a través de OpenRouter.</p>"
    return f"""<!doctype html><html lang="es"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Privacidad</title>{STYLE}<h1>Tus datos, explicado fácil</h1>{banner}
<h2>Qué guardamos</h2><p>Tus conversaciones y archivos, en el servidor de tu empresa. Se <b>borran solos a los {escape(days)} días</b>. Tú puedes borrarlos antes cuando quieras.</p>
<h2>A dónde van tus mensajes</h2>{models}
<h2>Quién puede ver qué</h2><ul><li>El administrador de tu empresa ve <b>cuánto se gasta por persona</b>, no lo que escribes.</li>
<li>No leemos tus conversaciones.</li><li>Tus datos no se venden ni se usan para anunciarte nada.</li></ul>
<h2>Copias de seguridad</h2><p>Se guardan cifradas.</p>
<p><small>Texto de ayuda para clientes. Debe revisarlo un abogado antes de usarse con clientes reales.</small></p>
<p><a href="/">← Volver al asistente</a></p></html>"""

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
