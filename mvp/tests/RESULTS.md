# Real-model test results (2026-11-19)

Setup: LiteLLM v1.110.1 (Docker) + tools service, real models through OpenRouter. Total spend for everything below: about **$0.18**.
Samples of every output are in `mvp/samples/`.

| # | Test | Result | Time | Cost |
|---|---|---|---|---|
| 1-3 | Greeting, short email, 3-point summary | Correct, short, plain Spanish. Routed to the fast model | 1-2 s | < $0.001 each |
| 4 | "Soy agente inmobiliario..." real-estate ad | Pack switched on by itself, one-time "Modo Inmobiliaria" line, good ad. | 4 s | ~$0.002 |
| 5 | Pasted email | Summary, what is asked, draft reply signed as the user | 2 s | ~$0.001 |
| 6 | "Pensar más" clinic margin problem | Correct maths (660 sessions, 12.400 EUR, break-even 350) | 8 s | ~$0.02 |
| 7 | Excel expenses sheet | Opens, 2 sheets, headers, categories, totals sheet. Sample data (dates are made-up) | 15 s | ~$0.003 |
| 8 | PowerPoint, 5 slides, physio clinic | Opens, 6 slides with sensible titles | 9 s | ~$0.003 |
| 9 | Formal letter (Word), unpaid invoice | Opens, 22 paragraphs, placeholders for unknown facts | 6 s | ~$0.003 |
| 10 | Instagram image with the text "Menú del día" | 1024x1024 cafe photo, Spanish text with accent rendered correctly | 5 s | ~$0.04 (est.) |
| 11 | Summary of a ~15K-token document | Routed to the fast model, good 5-point summary | 2 s | ~$0.005 |
| 12 | Analysis of the same document | Worked, but was sent to the strong model because of a keyword bug (fixed: now balanced) | 41 s | ~$0.04 |
| 13 | Deep research on fixed pages | 10 quote-verified facts, cited report, admits what sources do not say | 51 s | $0.056 |
| 14 | Deep research with search ("precio de una sesión de fisioterapia en España") | 4 searches, 8 pages, 5 useful, 30 verified facts, cited table, notes that sources disagree | 95 s | $0.119 |
| 15 | Deep research at the new default depth ("normal": up to 30 pages) | 8 searches, 30 pages found, 19 useful, 89 quote-verified facts; the checker flagged 3 sentences as unsupported | 171 s | $0.204 (about 0,24 EUR with markup) |

Depth levels: `rapida` (8 pages, ~$0.12), `normal` (30 pages, ~$0.20-0.30), `profunda` (100 pages, ~$0.75 estimated, not yet run).
The user gets `profunda` by writing "a fondo" in the question. Reading pages is cheap (~$0.0012 per page); the writer and searches are what cost.

## Bugs found and fixed during testing
- Image saved as `.png` although the model returns JPEG: now detects the real type.
- The word "riesgo" matched both lists in the model chooser, sending ordinary document analysis to the expensive model.
- Free DuckDuckGo search is blocked from many networks: default search is now OpenRouter's web search (about $0.008 per search), with Brave Search or DuckDuckGo as options.

## Still not tested
- LibreChat end to end with real models in a browser (memory, conversation titles, file upload text extraction).
- OCR of scanned PDFs and photos.
- Any user other than us; any quality comparison against Claude or Perplexity (needs your judgement).
- Windows install on your PC.
- Cost figures of OpenRouter lag; the image price is an estimate.
