"""Free test for the admin spend page (no models, no network). Run: python3 tests/test_usage.py"""
import os, sys, tempfile
os.environ["STATE_DIR"] = tempfile.mkdtemp()
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "tools"))
import usage

rows = [  # shape of LiteLLM /spend/logs?summarize=false
    {"spend": 0.10, "startTime": "2026-11-02T10:00:00", "end_user": "ana@example.com", "user": "default_user_id"},
    {"spend": 0.05, "startTime": "2026-11-02T11:00:00", "end_user": "luis@example.com", "user": "default_user_id"},
    {"spend": 0.20, "startTime": "2026-11-03T09:00:00", "end_user": "ana@example.com", "user": "default_user_id"},
    {"spend": 0.00, "startTime": "2026-11-03T09:05:00", "end_user": None, "user": "default_user_id"},
]
total, n, days, people = usage.summarize(rows)
ok = [
    ("total", abs(total - 0.35) < 1e-9 and n == 4),
    ("per person", abs(people["ana@example.com"] - 0.30) < 1e-9 and abs(people["luis@example.com"] - 0.05) < 1e-9),
    ("unidentified bucket", "(sin identificar)" in people),
    ("cap default 0", usage.get_cap() == 0),
]
usage.set_cap("12,5".replace(",", "."))
ok.append(("cap saved", usage.get_cap() == 12.5))
html = usage.page(rows)
ok += [("page shows euros", "€" in html and "ana@example.com" in html), ("page has cap form", 'name="cap"' in html and 'name="token"' in html),
       ("page never shows messages", "messages" not in html.lower() or "contenido" in html.lower())]
for name, v in ok: print("PASS" if v else "FAIL", "|", name)
print(f"\n{sum(v for _, v in ok)}/{len(ok)} passed"); sys.exit(0 if all(v for _, v in ok) else 1)
