"""Create Word / Excel / PowerPoint / PDF files. The model writes a small JSON spec, templates render it
(so the layout is always clean and the cheap model only has to produce content)."""
import json, os, re, uuid
import research

FILES_DIR = os.environ.get("FILES_DIR", "/data/files")
PUBLIC_URL = os.environ.get("PUBLIC_URL", "http://localhost").rstrip("/")

SYSTEM = """You create business documents. Reply ONLY with one JSON object, no other text.
Pick the file type that fits the request: "docx" (letters, reports, contracts, notes: the default), "xlsx" (tables, budgets,
lists, anything with numbers), "pptx" (presentations, slides), "pdf" (only if a PDF is asked for). Write in the language of the request.
Schemas:
 docx and pdf: {"type":"docx","title":"...","blocks":[{"t":"h","text":"...","level":1},{"t":"p","text":"..."},
   {"t":"ul","items":["..."]},{"t":"table","header":["..."],"rows":[["..."]]}]}
 xlsx: {"type":"xlsx","title":"...","sheets":[{"name":"...","header":["..."],"rows":[["text",12.5,"=B2*2"]]}]}  (formulas start with "=")
 pptx: {"type":"pptx","title":"...","slides":[{"title":"...","bullets":["..."],"notes":"..."}]}
Make it complete and realistic, ready to use. Use placeholders like [Nombre] only for facts you cannot know."""

def make_spec(conversation, cost, model="balanced"):
    for _ in range(2):  # one retry if the JSON is broken
        out = research.llm(cost, "document", model, SYSTEM, conversation, 8000)
        spec = research.parse_json(out, None)
        if isinstance(spec, dict) and spec.get("type") in ("docx", "xlsx", "pptx", "pdf"):
            return spec
    raise ValueError("No se pudo preparar el documento")

def _num(v):
    if isinstance(v, str) and re.fullmatch(r"-?\d+([.,]\d+)?", v.strip()):
        return float(v.replace(",", "."))
    return v

def render_docx(spec, path):
    from docx import Document
    d = Document()
    d.add_heading(spec.get("title", ""), 0)
    for b in spec.get("blocks", []):
        t = b.get("t")
        if t == "h": d.add_heading(b.get("text", ""), min(int(b.get("level", 1)), 4))
        elif t == "p": d.add_paragraph(b.get("text", ""))
        elif t == "ul":
            for i in b.get("items", []): d.add_paragraph(str(i), style="List Bullet")
        elif t == "table" and b.get("header"):
            tb = d.add_table(rows=1, cols=len(b["header"])); tb.style = "Light Grid Accent 1"
            for c, h in enumerate(b["header"]): tb.rows[0].cells[c].text = str(h)
            for r in b.get("rows", []):
                cells = tb.add_row().cells
                for c, v in enumerate(r[:len(cells)]): cells[c].text = str(v)
    d.save(path)

def render_xlsx(spec, path):
    from openpyxl import Workbook
    from openpyxl.styles import Font, PatternFill
    wb = Workbook(); wb.remove(wb.active)
    for s in spec.get("sheets", []) or [{"name": "Hoja1", "header": [], "rows": []}]:
        ws = wb.create_sheet(re.sub(r"[\[\]:*?/\\]", "", str(s.get("name", "Hoja")))[:31] or "Hoja")
        if s.get("header"):
            ws.append(s["header"])
            for c in ws[1]:
                c.font = Font(bold=True, color="FFFFFF"); c.fill = PatternFill("solid", fgColor="2F5597")
        for r in s.get("rows", []): ws.append([_num(v) for v in r])
        for col in ws.columns:
            ws.column_dimensions[col[0].column_letter].width = min(50, max(10, max(len(str(c.value or "")) for c in col) + 2))
        ws.freeze_panes = "A2"
    wb.save(path)

def render_pptx(spec, path):
    from pptx import Presentation
    p = Presentation(); p.slide_width, p.slide_height = 12192000, 6858000
    s = p.slides.add_slide(p.slide_layouts[0]); s.shapes.title.text = spec.get("title", "")
    for sl in spec.get("slides", []):
        s = p.slides.add_slide(p.slide_layouts[1]); s.shapes.title.text = sl.get("title", "")
        tf = s.placeholders[1].text_frame; tf.clear()
        for i, b in enumerate(sl.get("bullets", [])):
            (tf.paragraphs[0] if i == 0 else tf.add_paragraph()).text = str(b)
        if sl.get("notes"): s.notes_slide.notes_text_frame.text = str(sl["notes"])
    p.save(path)

def render_pdf(spec, path):
    from xml.sax.saxutils import escape
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import getSampleStyleSheet
    from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle, ListFlowable, ListItem
    st = getSampleStyleSheet(); out = [Paragraph(escape(spec.get("title", "")), st["Title"])]
    for b in spec.get("blocks", []):
        t = b.get("t")
        if t == "h": out.append(Paragraph(escape(b.get("text", "")), st["Heading%d" % min(int(b.get("level", 1)), 3)]))
        elif t == "p": out += [Paragraph(escape(b.get("text", "")), st["BodyText"]), Spacer(1, 6)]
        elif t == "ul": out.append(ListFlowable([ListItem(Paragraph(escape(str(i)), st["BodyText"])) for i in b.get("items", [])], bulletType="bullet"))
        elif t == "table" and b.get("header"):
            data = [[Paragraph(escape(str(c)), st["BodyText"]) for c in row] for row in [b["header"]] + b.get("rows", [])]
            tb = Table(data, repeatRows=1)
            tb.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#DDE6F5")), ("GRID", (0, 0), (-1, -1), 0.5, colors.grey)]))
            out += [tb, Spacer(1, 8)]
    SimpleDocTemplate(path, pagesize=A4).build(out)

RENDER = {"docx": render_docx, "xlsx": render_xlsx, "pptx": render_pptx, "pdf": render_pdf}

def create(conversation, progress, cost):
    progress("Preparando el contenido del documento…")
    spec = make_spec(conversation, cost)
    progress("Dando formato al archivo…")
    kind = spec["type"]
    name = (re.sub(r"[^\w\- ]", "", spec.get("title", "documento"))[:60].strip().replace(" ", "_") or "documento") + "." + kind
    folder = os.path.join(FILES_DIR, uuid.uuid4().hex[:12]); os.makedirs(folder, exist_ok=True)
    RENDER[kind](spec, os.path.join(folder, name))
    url = f"{PUBLIC_URL}/files/{os.path.basename(folder)}/{name}"
    return f"**Listo. Tu documento:** [{name}]({url})\n\nSi quieres cambios, dímelo (por ejemplo: «hazlo más corto» o «añade una columna de totales»).\n"
