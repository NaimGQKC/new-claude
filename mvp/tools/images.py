"""Marketing-grade simple images. A cheap model writes a good image prompt from the chat (+ business context),
then the image model draws it. The picture is saved and shown inline."""
import base64, json, os, re, urllib.request, uuid
import research, documents

PROMPT_SYS = """You write prompts for an AI image generator. From the conversation, write ONE detailed prompt in English for the
image the user wants: subject, style, composition, colors, lighting, mood. Use the business context if given. Marketing style:
clean, modern, professional, uncluttered, plenty of empty space. If words must appear in the image, keep them to at most 5 words,
written exactly as the user wants them. If the user asks for changes to a previous image, rewrite the previous description with
those changes. Reply ONLY with the prompt."""

_PNG = base64.b64decode("iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==")

def generate(prompt, cost, model="image"):
    """Returns PNG bytes. Goes through the gateway so the cost lands in 'Mi gasto'."""
    if research.DRY:
        return _PNG
    payload = {"model": model, "modalities": ["image", "text"], "messages": [{"role": "user", "content": prompt}]}
    if getattr(cost, "user", None):
        payload["user"] = cost.user
    body = json.dumps(payload).encode()
    req = urllib.request.Request(research.GATEWAY + "/v1/chat/completions", body,
                                 {"Content-Type": "application/json", "Authorization": "Bearer " + research.KEY})
    with urllib.request.urlopen(req, timeout=300) as r:
        data, hdr = json.load(r), r.headers
    cost["image"] = cost.get("image", 0.0) + float(hdr.get("x-litellm-response-cost") or 0)
    msg = data["choices"][0]["message"]
    urls = [i.get("image_url", {}).get("url", "") for i in (msg.get("images") or [])]
    if isinstance(msg.get("content"), list):
        urls += [p.get("image_url", {}).get("url", "") for p in msg["content"] if isinstance(p, dict) and p.get("type") == "image_url"]
    for u in urls:
        m = re.match(r"data:image/\w+;base64,(.+)", u or "", re.S)
        if m:
            return base64.b64decode(m.group(1))
    raise ValueError("El modelo no devolvió ninguna imagen. Prueba a describirla de otra forma.")

def create(conversation, progress, cost):
    progress("Pensando cómo debe ser la imagen…")
    prompt = research.llm(cost, "image_prompt", "fast", PROMPT_SYS, conversation, 700).strip()
    progress("Creando la imagen… (puede tardar medio minuto)")
    png = generate(prompt, cost)
    folder = os.path.join(documents.FILES_DIR, uuid.uuid4().hex[:12]); os.makedirs(folder, exist_ok=True)
    ext = "jpg" if png[:3] == b"\xff\xd8\xff" else "webp" if png[8:12] == b"WEBP" else "png"   # the model may return JPEG
    name = f"imagen.{ext}"
    open(os.path.join(folder, name), "wb").write(png)
    url = f"{documents.PUBLIC_URL}/files/{os.path.basename(folder)}/{name}"
    return (f"![Imagen]({url})\n\n**Tu imagen:** [descargar]({url})\n\n"
            f"Si quieres cambios, dímelo (por ejemplo: «más colorida» o «con el texto Ofertas de otoño»).\n\n"
            f"<sub>Descripción usada: {prompt[:600]}</sub>\n")
