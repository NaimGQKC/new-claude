"""The 'front door' decides, for every message, what to do. No AI is used for this decision (it is free and instant):
  1) is a file wanted?  2) is an image wanted?  3) which industry pack applies?  4) which model fits (document size, topic)?"""
import json, os, re, sys, time, unicodedata
import packs

VERB = (r"(haz(me)?|crea(me)?|genera(me)?|prepara(me)?|redacta(me)?|monta(me)?|dibuja(me)?|disena(me)?|necesito|quiero|dame|"
        r"make|create|generate|draft|prepare|draw|design)")
FILE_NOUN = (r"(excel|hoja de calculo|spreadsheet|word|\.docx|pdf|presentacion|powerpoint|ppt|diapositivas|slides|plantilla|"
             r"documento|contrato|presupuesto|factura)")
IMAGE_NOUN = (r"(imagen|imagenes|foto|fotografia|logo|logotipo|cartel|banner|ilustracion|dibujo|poster|flyer|portada|"
              r"image|picture|illustration|publicacion para|post para)")
BACKGROUND = r"title for the conversation|5-word|5 words or less|memory"   # titles / memory jobs must never create files

def norm(s):
    return "".join(c for c in unicodedata.normalize("NFD", (s or "").lower()) if unicodedata.category(c) != "Mn")

def text_of(c):
    return " ".join(p.get("text", "") for p in c if isinstance(p, dict)) if isinstance(c, list) else (c or "")

def last_user(msgs):
    u = [m for m in msgs if m.get("role") == "user"]
    return text_of(u[-1]["content"]) if u else ""

def transcript(msgs):
    return "\n\n".join(f"{m['role'].upper()}: {text_of(m['content'])[:6000]}" for m in msgs
                       if m.get("role") in ("user", "assistant") or (m.get("role") == "system"))[-20000:]

def _file_or_image(msgs):
    raw = last_user(msgs)
    if re.search(BACKGROUND, raw.lower()):
        return None
    last = norm(raw)
    prev = [m for m in msgs if m.get("role") == "assistant"]
    if prev and len(last) < 300:     # short follow-up ("hazlo más corto") continues the last thing we made
        p = text_of(prev[-1]["content"])
        if "Tu documento:" in p: return "document"
        if "Tu imagen:" in p: return "image"
    d = re.search(VERB + r".{0,60}?" + FILE_NOUN, last)
    i = re.search(VERB + r".{0,60}?" + IMAGE_NOUN, last)
    if d and i:   # both words present: the noun that comes first is the thing wanted
        return "document" if d.end() <= i.end() else "image"
    return "document" if d else "image" if i else None

LEGAL_FIN = r"(clausula|riesgo|contrato|legal|fiscal|impuesto|balance|auditor|demanda|norma|rgpd|laboral|sancion)"
ANALYSIS = r"(analiza|revisa|compara|conclusion|riesgo|clausula|por que|que implica|incongruencia|contradic)"

def pick_model(msgs):
    """Cheapest model that is good enough for the job. Long input = a document was attached."""
    users = [text_of(m["content"]) for m in msgs if m.get("role") == "user"]
    est_tokens = sum(len(t) for t in users) // 4
    last = norm(last_user(msgs))
    if est_tokens >= 6000:
        if re.search(LEGAL_FIN, last) and re.search(ANALYSIS, last):
            return "strong", f"document (~{est_tokens} tokens): legal/financial analysis"
        if re.search(ANALYSIS, last):
            return "balanced", f"document (~{est_tokens} tokens): analysis"
        return "fast", f"document (~{est_tokens} tokens): summary or extraction"
    return "auto", f"router (~{est_tokens} tokens)"

def decide(msgs, confirmed=False):
    kind = _file_or_image(msgs)
    texts = [text_of(m["content"]) for m in msgs if m.get("role") in ("system", "user")]
    ps = packs.active(texts)
    if kind:
        d = {"action": kind, "model": None, "reason": f"{kind} request", "estimate_eur": estimate_fixed("image" if kind == "image" else "document")}
    else:
        model, reason = pick_model(msgs)
        d = {"action": "chat", "model": model, "reason": reason}
        est_tokens = sum(len(text_of(m["content"])) for m in msgs if m.get("role") == "user") // 4
        d["estimate_eur"] = estimate_chat(model, est_tokens)
        if d["estimate_eur"] > CONFIRM_EUR and not confirmed:
            d["action"] = "ask"; d["ask"] = ask_text(d["estimate_eur"])
    d["packs"] = [p["id"] for p in ps]
    d["system"] = packs.system_text(ps)
    d["notice"] = packs.notice(ps, " ".join(text_of(m["content"]) for m in msgs if m.get("role") == "assistant"))
    if d["action"] == "chat" and d.get("estimate_eur", 0) >= SHOW_EUR:
        d["notice"] += f"_Documento grande: coste aproximado {fmt(d['estimate_eur'])}._\n\n"
    return d

def log(d):
    print(json.dumps({"t": int(time.time()), "est_eur": round(d.get("estimate_eur", 0), 4), **{k: d[k] for k in ("action", "model", "reason", "packs")}}), file=sys.stderr, flush=True)


# ---------- cost estimates (what the USER pays: model cost + markup, in euros) -------------------------------------
MARKUP = float(os.environ.get("MARKUP", "0.30"))
EUR_PER_USD = float(os.environ.get("EUR_PER_USD", "0.92"))
CONFIRM_EUR = float(os.environ.get("CONFIRM_EUR", "1.0"))     # ask before spending more than this
SHOW_EUR = float(os.environ.get("SHOW_EUR", "0.10"))          # mention the estimate above this
# USD per 1M tokens (input, output) and a typical answer length in tokens (thinking models write more)
PRICE = {"fast": (0.30, 1.20, 800), "balanced": (0.30, 1.20, 2500), "writer": (1.40, 4.40, 2000),
         "strong": (3.00, 15.00, 4000), "auto": (0.30, 1.20, 1500)}
FIXED_EUR = {"deep-research": 0.54, "image": 0.04, "document": 0.01}   # USD-based estimates measured/derived earlier
CONFIRM_MARK = "¿Quieres que continúe?"

def eur(usd):
    return usd * (1 + MARKUP) * EUR_PER_USD

def fmt(x):
    return f"{x:.2f}".replace(".", ",") + " €"

def estimate_chat(model, est_tokens):
    pin, pout, out_tok = PRICE.get(model, PRICE["auto"])
    return eur((est_tokens * pin + out_tok * pout) / 1e6)

def estimate_fixed(kind):
    return eur(FIXED_EUR[kind])

def resolve_confirmation(msgs):
    """Stateless yes/no handling. Returns (messages_to_use, state) with state in None | 'confirmed' | 'declined'."""
    if len(msgs) >= 3 and msgs[-1].get("role") == "user" and msgs[-2].get("role") == "assistant" \
            and CONFIRM_MARK in text_of(msgs[-2]["content"]):
        ans = norm(last_user(msgs)).strip(" .!¡¿?")
        if re.fullmatch(r"(si|sii+|vale|ok|adelante|continua|continuar|claro|de acuerdo|yes|go)", ans):
            return msgs[:-2], "confirmed"
        return msgs, "declined"
    return msgs, None

def ask_text(amount):
    return (f"Esto va a costar unos **{fmt(amount)}** (es una estimación; el documento es muy grande). "
            f"{CONFIRM_MARK} Responde **sí** o **no**.")
