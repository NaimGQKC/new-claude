"""Send sample prompts through the gateway and print: which model answered, tokens, cost, time.
Usage: python3 -I route_test.py [base_url] [key]"""
import json, sys, time, urllib.request

BASE = sys.argv[1] if len(sys.argv) > 1 else "http://localhost:4000"
KEY = sys.argv[2] if len(sys.argv) > 2 else "sk-test"

PROMPTS = [
    ("auto", "Hola, ¿qué tal?"),
    ("auto", "Escribe un email corto a un cliente para confirmar su cita del jueves a las 10:00."),
    ("auto", "Resume en 3 puntos: Las tarifas planas por usuario obligan a las empresas a pagar lo mismo por empleados que casi no usan la herramienta, mientras que el pago por uso ajusta el coste al consumo real."),
    ("auto", "Redacta un informe de una página sobre los pros y contras de pasar de tarifas por usuario a pago por uso en una clínica de fisioterapia de 8 personas."),
    ("auto", "Analiza paso a paso: una clínica cobra 40€ por sesión, tiene 6 fisios con 5 sesiones al día, 22 días al mes. Los costes fijos son 14.000€/mes. ¿Cuál es el margen y cuántas sesiones menos soporta antes de perder dinero?"),
    ("auto-think", "Una clínica cobra 40€ por sesión, tiene 6 fisios con 5 sesiones al día, 22 días al mes. Costes fijos 14.000€/mes. ¿Cuál es el margen y cuántas sesiones menos soporta antes de perder dinero?"),
]

def call(model, text):
    body = json.dumps({"model": model, "messages": [{"role": "user", "content": text}], "max_tokens": 4000}).encode()
    req = urllib.request.Request(BASE + "/v1/chat/completions", body,
        {"Content-Type": "application/json", "Authorization": "Bearer " + KEY})
    t = time.time()
    with urllib.request.urlopen(req, timeout=180) as r:
        data = json.load(r); hdr = r.headers
    return data, hdr, time.time() - t

for model, text in PROMPTS:
    try:
        d, h, secs = call(model, text)
        u = d.get("usage", {})
        print(f"[{model}] {text[:55]!r}\n   -> routed={h.get('x-litellm-model-name')}  in={u.get('prompt_tokens')} out={u.get('completion_tokens')}"
              f"  cost=${h.get('x-litellm-response-cost')}  {secs:.1f}s")
        print("   ", (d['choices'][0]['message'].get('content') or '').replace("\n", " ")[:160])
    except Exception as e:
        print(f"[{model}] {text[:55]!r}\n   -> ERROR {e}")
