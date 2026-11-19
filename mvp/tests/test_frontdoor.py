"""Free tests for the front door (no models, no network). Run: python3 tests/test_frontdoor.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "tools"))
import frontdoor

def u(t): return [{"role": "user", "content": t}]
CASES = [
    # (messages, expected action, expected model or None, expected packs)
    (u("Hola, ¿qué tal?"), "chat", "auto", []),
    (u("Escribe un email para confirmar una cita"), "chat", "auto", []),
    (u("Hazme una hoja de cálculo de gastos"), "document", None, []),
    (u("Prepárame una presentación sobre ventas"), "document", None, []),
    (u("Crea una imagen para un post de Instagram con una cafetería"), "image", None, ["hosteleria"]),
    (u("Diséñame un logo para mi tienda"), "image", None, ["comercio"]),
    (u("Crea una imagen para la presentación"), "image", None, []),
    (u("Hazme una presentación con imágenes de casas"), "document", None, []),
    (u("Soy agente inmobiliario, escríbeme un anuncio para un piso de 3 habitaciones"), "chat", "auto", ["inmobiliaria"]),
    (u("Asunto: Factura pendiente\nHola, aún no hemos recibido el pago. Un saludo"), "chat", "auto", ["email"]),
    (u("Provide a concise, 5-word-or-less title for the conversation: hazme un logo"), "chat", "auto", []),
    ([{"role": "user", "content": "hazme un pdf"}, {"role": "assistant", "content": "**Listo. Tu documento:** [a](http://x)"},
      {"role": "user", "content": "hazlo más corto"}], "document", None, []),
    ([{"role": "user", "content": "crea una imagen de un perro"}, {"role": "assistant", "content": "**Tu imagen:** [d](http://x)"},
      {"role": "user", "content": "más colorida"}], "image", None, []),
    # long attached document -> cheap long-context model, stronger only when the question needs it
    (u("Resume este documento:\n" + "texto del contrato " * 2500), "chat", "fast", []),
    (u("Analiza los riesgos de este contrato:\n" + "cláusula de pago " * 2500), "chat", "strong", []),
    (u("Compara las conclusiones del informe:\n" + "datos " * 5000), "chat", "balanced", []),
    # memory text in a system message switches the pack on too
    ([{"role": "system", "content": "Memoria: el usuario trabaja en una clínica de fisioterapia"}, {"role": "user", "content": "Redacta un recordatorio para mañana"}], "chat", "auto", ["fisioterapia"]),
]
bad = 0
for msgs, act, model, pks in CASES:
    d = frontdoor.decide(msgs)
    ok = d["action"] == act and (model is None or d["model"] == model) and d["packs"] == pks
    bad += not ok
    print(("PASS" if ok else "FAIL"), "|", frontdoor.last_user(msgs)[:55].replace("\n", " "), "->", d["action"], d["model"], d["packs"], "|", d["reason"])
print(f"\n{len(CASES) - bad}/{len(CASES)} passed"); sys.exit(1 if bad else 0)
