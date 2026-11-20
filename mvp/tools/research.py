"""Deep research pipeline (MVP). Plan -> search -> read pages -> write -> check. Prints cost per stage.

Every model call goes through the LiteLLM gateway (model names: fast / balanced / writer / strong).
  python research.py "your question"                 # real run (needs the gateway running)
  python research.py --dry "question" --urls URL...  # NO model calls: fake models, real page fetching
Search providers: ddgs (free, best effort) or brave (set BRAVE_API_KEY; ~$5 per 1,000 searches).
Needs: pip install ddgs trafilatura
"""
import argparse, concurrent.futures as cf, json, os, re, sys, time, urllib.parse, urllib.request

GATEWAY = os.environ.get("GATEWAY_URL", "http://localhost:4000")
KEY = os.environ.get("GATEWAY_KEY", "sk-test")
class Cost(dict):
    """stage -> USD, plus .user = who asked (sent to the gateway so spend is attributed per person)."""
    user = None

DRY = bool(os.environ.get("RESEARCH_DRY"))   # fake models, no spend

# ---------- model calls -------------------------------------------------------------------
def llm(cost, stage, model, system, user, max_tokens=6000):
    if DRY:
        return MOCK[stage](user)
    payload = {"model": model, "max_tokens": max_tokens,
               "messages": [{"role": "system", "content": system}, {"role": "user", "content": user}]}
    if getattr(cost, "user", None):
        payload["user"] = cost.user
    body = json.dumps(payload).encode()
    req = urllib.request.Request(GATEWAY + "/v1/chat/completions", body,
                                 {"Content-Type": "application/json", "Authorization": "Bearer " + KEY})
    with urllib.request.urlopen(req, timeout=300) as r:
        data, hdr = json.load(r), r.headers
    cost[stage] = cost.get(stage, 0.0) + float(hdr.get("x-litellm-response-cost") or 0)
    return data["choices"][0]["message"].get("content") or ""

def parse_json(text, default):
    m = re.search(r"(\{.*\}|\[.*\])", text, re.S)
    try:
        return json.loads(m.group(1)) if m else default
    except Exception:
        return default

MOCK = {  # fake answers so the plumbing can be tested for free
    "plan": lambda u: json.dumps({"queries": ["fake query one", "fake query two"]}),
    "read": lambda u: json.dumps([{"claim": "Fake claim from page", "quote": u.split("PAGE:\n", 1)[-1][200:260]}]),
    "write": lambda u: "Informe de prueba (modelo falso). Dato de ejemplo [1].",
    "check": lambda u: "[]",
    "image_prompt": lambda u: "A clean modern marketing photo of a cozy living room, soft light, space for text",
    "document": lambda u: json.dumps({"type": "docx", "title": "Documento de prueba", "blocks": [
        {"t": "h", "text": "Resumen", "level": 1}, {"t": "p", "text": "Texto de ejemplo."}, {"t": "ul", "items": ["Uno", "Dos"]},
        {"t": "table", "header": ["Concepto", "Importe"], "rows": [["A", "10"], ["B", "20"]]}]}),
}

# ---------- search + fetch ----------------------------------------------------------------
SEARCH_USD = 0.008   # measured: one OpenRouter web search call, 5 results

def search_openrouter(query, n, cost):
    """Built-in default: OpenRouter's web plugin, called through our gateway (no extra account or key)."""
    payload = {"model": "fast", "max_tokens": 1, "messages": [{"role": "user", "content": query}],
               "extra_body": {"plugins": [{"id": "web", "max_results": n}], "reasoning": {"enabled": False}}}
    if getattr(cost, "user", None):
        payload["user"] = cost.user
    body = json.dumps(payload).encode()
    req = urllib.request.Request(GATEWAY + "/v1/chat/completions", body, {"Content-Type": "application/json", "Authorization": "Bearer " + KEY})
    data = json.load(urllib.request.urlopen(req, timeout=120))
    cost["search"] = cost.get("search", 0.0) + SEARCH_USD
    ann = data["choices"][0]["message"].get("annotations") or []
    return [{"title": a["url_citation"].get("title") or a["url_citation"]["url"], "url": a["url_citation"]["url"]}
            for a in ann if a.get("url_citation", {}).get("url")]

def search(query, n=4, cost=None):
    cost = {} if cost is None else cost
    if DRY:
        return [{"title": "Wikipedia: Physical therapy", "url": "https://en.wikipedia.org/wiki/Physical_therapy"}]
    if os.environ.get("BRAVE_API_KEY"):
        url = "https://api.search.brave.com/res/v1/web/search?" + urllib.parse.urlencode({"q": query, "count": n})
        req = urllib.request.Request(url, headers={"X-Subscription-Token": os.environ["BRAVE_API_KEY"], "Accept": "application/json"})
        res = json.load(urllib.request.urlopen(req, timeout=30)).get("web", {}).get("results", [])
        return [{"title": r["title"], "url": r["url"]} for r in res]
    try:
        res = search_openrouter(query, n, cost)
        if res:
            return res
    except Exception as e:
        print(f"  gateway search failed for {query!r}: {e}", file=sys.stderr)
    try:   # last resort: free scraping search (unreliable)
        from ddgs import DDGS
        return [{"title": r["title"], "url": r["href"]} for r in DDGS().text(query, max_results=n)]
    except Exception as e:
        print(f"  search failed for {query!r}: {e}", file=sys.stderr)
        return []

def fetch(url, limit=15000):
    import trafilatura
    try:
        html = trafilatura.fetch_url(url)
        text = trafilatura.extract(html) if html else None
    except Exception:
        text = None
    return (text or "")[:limit]

def norm(s):
    return re.sub(r"\s+", " ", s).strip().lower()

# ---------- pipeline ----------------------------------------------------------------------
# depth -> (searches, results per search, max pages read, rough USD: ~$0.008 per search + ~$0.0015 per page read + writer)
DEPTHS = {"rapida": (4, 5, 8, 0.12), "normal": (8, 6, 30, 0.30), "profunda": (15, 8, 100, 0.75)}

def choose_depth(question):
    q = re.sub(r"\s+", " ", question.lower())
    if re.search(r"a fondo|exhaustiv|profund|muy detallad|todas las fuentes|in depth|thorough", q): return "profunda"
    if re.search(r"rapid|breve|por encima|quick", q): return "rapida"
    return "normal"

def run(question, urls=None, depth="normal", planner="strong", reader="fast", writer="strong", checker="fast",
        progress=print, cost=None):
    cost = Cost() if cost is None else cost
    n_queries, per_query, max_pages, usd = DEPTHS[depth]
    t0 = time.time()
    progress(f"Investigación {depth}: hasta {max_pages} páginas. Coste estimado: unos {usd*1.3*0.92:.2f} €".replace(".", ",", 1) + ".")
    # 1. plan
    if urls:
        queries = []
    else:
        out = llm(cost, "plan", planner,
                  "You plan web research. Reply ONLY with JSON: {\"queries\": [..]} containing %d short, different web search queries "
                  "(in the language best suited to find good sources) that together answer the question." % n_queries, question, 2000)
        queries = parse_json(out, {}).get("queries", [question])[:n_queries]
    progress(f"1/5 Planificando: {len(queries)} búsquedas")

    # 2. search
    found = [{"url": u, "title": u} for u in (urls or [])]
    for q in queries:
        found += search(q, per_query, cost=cost)
    seen, hits = set(), []
    for h in found:
        if h["url"] not in seen:
            seen.add(h["url"]); hits.append(h)
    hits = hits[:max_pages]
    progress(f"2/5 Buscando: {len(hits)} páginas candidatas")

    # 3. fetch + read (cheap model, in parallel); a claim is kept only if its quote really is on the page
    def read_page(h):
        text = fetch(h["url"])
        if len(text) < 500:
            return h, []
        out = llm(cost, "read", reader,
                  "Extract facts that help answer the question, using ONLY the page text. Reply ONLY with a JSON list "
                  "[{\"claim\": \"...\", \"quote\": \"exact sentence copied from the page\"}], max 5 items; [] if nothing useful.",
                  f"QUESTION: {question}\n\nPAGE:\n{text}", 3000)
        facts = [f for f in parse_json(out, []) if isinstance(f, dict) and f.get("quote") and norm(f["quote"]) in norm(text)]
        return h, facts
    with cf.ThreadPoolExecutor(10) as ex:
        results = list(ex.map(read_page, hits))
    notes, sources = [], []
    for h, facts in results:
        if facts:
            sources.append(h)
            notes += [{"n": len(sources), "claim": f["claim"], "quote": f["quote"]} for f in facts]
    progress(f"3/5 Leyendo: {len(sources)} páginas útiles, {len(notes)} datos con cita verificada")
    if not notes:
        return "No se encontraron fuentes utilizables.", sources, []

    # 4. write
    notes_txt = "\n".join(f"[{n['n']}] {n['claim']}  (quote: \"{n['quote']}\")" for n in notes)
    report = llm(cost, "write", writer,
                 "Write a clear, well-structured research report answering the question. Use ONLY the numbered notes. "
                 "Cite every factual sentence like [1]. If the notes don't cover something, say it is unknown. "
                 "Answer in the language of the question. No invented numbers.",
                 f"QUESTION: {question}\n\nNOTES:\n{notes_txt}", 8000)
    progress("4/5 Redactando el informe: listo")

    # 5. check
    out = llm(cost, "check", checker,
              "Compare the REPORT with the NOTES. Reply ONLY with a JSON list of sentences from the report that state facts "
              "not supported by the notes (empty list if all supported).",
              f"NOTES:\n{notes_txt}\n\nREPORT:\n{report}", 2000)
    issues = parse_json(out, [])
    progress(f"5/5 Comprobando: {len(issues)} frase(s) sin respaldo [{time.time()-t0:.0f}s]")
    return report, sources, issues

def render(report, sources, issues, cost):
    md = report + "\n\n## Fuentes\n" + "\n".join(f"[{i}] {s['title']} - {s['url']}" for i, s in enumerate(sources, 1))
    if issues:
        md += "\n\n## Avisos (frases no respaldadas por las fuentes)\n" + "\n".join(f"- {i}" for i in issues)
    md += "\n\n## Coste\n" + "\n".join(f"- {k}: ${v:.4f}" for k, v in cost.items()) + f"\n- TOTAL: ${sum(cost.values()):.4f}\n"
    return md

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("question")
    ap.add_argument("--dry", action="store_true", help="fake models, no spend")
    ap.add_argument("--urls", nargs="*", help="skip search, read these pages")
    ap.add_argument("--writer", default="strong")
    ap.add_argument("--depth", choices=list(DEPTHS), default=None)
    ap.add_argument("--out", default="report.md")
    a = ap.parse_args()
    DRY = a.dry or DRY
    cost = {}
    report, sources, issues = run(a.question, a.urls, depth=a.depth or choose_depth(a.question), writer=a.writer, cost=cost)
    open(a.out, "w").write(render(report, sources, issues, cost))
    print(f"saved {a.out}; cost ${sum(cost.values()):.4f}")
