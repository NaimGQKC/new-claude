"""Industry packs: small, human-readable JSON files (prompt only, no code, no tool access).
A pack switches on by itself when the user says (or memory says) what they do. Drop more files in packs/ to add more."""
import glob, json, os, re, unicodedata

DIR = os.environ.get("PACKS_DIR", os.path.join(os.path.dirname(__file__), "packs"))

def norm(s):
    return "".join(c for c in unicodedata.normalize("NFD", (s or "").lower()) if unicodedata.category(c) != "Mn")

def load():
    out = []
    for f in sorted(glob.glob(os.path.join(DIR, "*.json"))):
        try:
            p = json.load(open(f, encoding="utf-8"))
            p["triggers"] = [norm(t) for t in p.get("triggers", [])]
            out.append(p)
        except Exception:
            pass   # a broken community file must never break chat
    return out

PACKS = load()

def active(texts):
    """texts: all message texts (system + user). Returns up to 2 matching packs."""
    blob = norm(" \n ".join(texts))[-12000:]
    return [p for p in PACKS if any(t in blob for t in p["triggers"])][:2]

def system_text(packs):
    return "\n\n".join(p["prompt"] for p in packs)

def notice(packs, history_text):
    """One-time friendly line when a pack switches on (skipped if already shown in this chat or silent)."""
    lines = []
    for p in packs:
        if p.get("silent") or f"Modo {p['name']} activado" in history_text:
            continue
        helps = "; ".join(p.get("can_help", []))
        lines.append(f"_💡 Modo {p['name']} activado.{' Puedo ayudarte, por ejemplo, con: ' + helps + '.' if helps else ''}_\n\n")
    return "".join(lines)
