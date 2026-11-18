# Open-weight LLM quality for general assistant work (as of 2026-11-18)

Scope note for the report writer. All pages were fetched on 2026-11-18 unless stated otherwise. Rules used throughout:
- "AA" means Artificial Analysis. Every AA Intelligence Index number below is **v5.0.1**, the only version shown on the pages fetched. No v4 numbers are mixed into the tables. Where a secondary source quotes a different AA number, it is flagged as a conflict.
- "Vals" means the Vals Index **v2.2**, last updated 2026-11-18.
- "EQ-Bench CW" means EQ-Bench **Creative Writing v3** (Elo), read from the leaderboard's data file.
- **INDEPENDENT** means a third-party evaluator (AA, Vals, EQ-Bench). **VENDOR** means the model maker's own model card. **SECONDARY** means blogs or aggregators.
- Closed models (Claude, GPT, Gemini) appear only as a reference bar. They are not candidates.

Main sources:
- AA open-weights page: https://artificialanalysis.ai/models/open-source
- AA leaderboard: https://artificialanalysis.ai/leaderboards/models
- AA methodology: https://artificialanalysis.ai/methodology/intelligence-benchmarking
- AA model pages: https://artificialanalysis.ai/models/kimi-k3-1-pro, https://artificialanalysis.ai/models/deepseek-v4-1-flash, https://artificialanalysis.ai/models/glm-5-3
- Vals Index: https://www.vals.ai/benchmarks/vals_index
- EQ-Bench CW v3: page https://eqbench.com/creative_writing.html, data https://eqbench.com/creative_writing.js
- Hugging Face model API (license tags and creation dates), e.g. https://huggingface.co/api/models/deepseek-ai/DeepSeek-V4.1-Flash
- Kimi model card (vendor): https://huggingface.co/moonshotai/Kimi-K3.1-Pro
- Wavect open-weight comparison (secondary, updated 2026-11-11): https://wavect.io/blog/open-weight-llm-comparison-2026/

---

## Q1. Independent scores per model (AA Intelligence Index v5.0.1, Vals Index v2.2, sub-evals, others)

### Takeaway
Two independent indexes agree on the order at the top. **Kimi K3.1 Pro** is the strongest open-weight model (AA v5 46, Vals 62.52%). Next comes a tight group of **DeepSeek V4.1 Flash 1017** (AA 33, Vals 61.26%), **GLM-5.3** (AA 32, Vals 59.85%), **Inkling 2 Small** (31 / 56.08%), **MiniMax-M3.1-Flash** (29 / 53.78%), **GLM-5.3-Flash** (28 / 50.86%) and **Mistral Large 4** (26 / 56.53%). The best closed models score AA 55–65 and Vals 66–71%. AA v5 is heavily agentic, and older or small models (gpt-oss-120b, Gemma 4, Mistral Small 4 / Medium 3.5) score near its floor (4–5). It therefore separates weak models poorly on simple assistant tasks.

### Cited Findings

**What AA v5.0.1 measures (important for interpreting the numbers)**
- AA Intelligence Index v5.0.1 has 9 evals in four categories of 25% each. **Knowledge Work**: AA-Briefcase v1.1 15%, AutomationBench-AA 5%, GDP.pdf 5%. **Coding**: FrontierCode-AA 2.0 15%, Terminal-Bench 4.0 10%. **Science**: Terminal-Bench-Science 0.1 15%, CritPt v2 Hard Subset 10%. **General**: AA-Omniscience v1.1 15%, HLE-Diamond 10%. — [AA methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)
- GDPval-AA "was removed from the Intelligence Index in v5.0, having been a constituent up to and including v4.3.2." The page does not say whether v4 and v5 scores are comparable. AA-Omniscience v1.1 is "not directly comparable with v1." — [AA methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)
- AA model pages for Kimi K3.1 Pro, DeepSeek V4.1 Flash and GLM-5.3 name the sub-evals but show **no per-eval scores** in fetchable text. Sub-evals the founder asked about (GPQA, IFBench, AA-LCR, tau2, SciCode) are not shown there. — [AA Kimi page](https://artificialanalysis.ai/models/kimi-k3-1-pro), [AA GLM-5.3 page](https://artificialanalysis.ai/models/glm-5-3)

**AA Intelligence Index v5.0.1, open-weight models (INDEPENDENT, fetched 2026-11-18)** — [AA leaderboard](https://artificialanalysis.ai/leaderboards/models), [AA open-weights page](https://artificialanalysis.ai/models/open-source)

| Open-weight model (AA variant) | AA v5.0.1 | Cost/Index task | Time/task | Context |
|---|---|---|---|---|
| Kimi K3.1 Pro | 46 | $3.68 | 39.3 min | 1M |
| Tencent Hy4 (preview weights are Apache 2.0 per Wavect; open status of the final weights unconfirmed) | 35 | $1.03 | 13.7 min | 1M |
| DeepSeek V4.1 Flash 1017 (Max) | 33 | $0.60 | 13.5 min | 1M |
| GLM-5.3 (Max) | 32 | $5.01 | 23.1 min | 1M |
| Inkling 2 Small | 31 | $1.18 | 21.4 min | 1M |
| MiMo-V2.6-Pro | 30 | $0.26 | 35.6 min | 1M |
| Ling 3.1 Flash 1019 | 30 | $3.19 | n/a | 1M |
| MiniMax-M3.1-Flash | 29 | $0.49 | 17.5 min | 1M |
| Qwen3.8-Flash-Next | 29 | $0.57 | 30.8 min | 256k |
| GLM-5.3-Flash | 28 | $0.58 | 39.3 min | 1M |
| MiMo-V2.6-Flash | 27 | $0.13 | 53.9 min | 1M |
| Mistral Large 4 (High) | 26 | $2.06 | 20.6 min | 1M |
| Muse Spark Open (Xhigh) | 25 | $2.02 | 6.1 min | 1M |
| GLM-5.3 (Low effort) | 23 | n/a | 12.8 min | 1M |
| DeepSeek V4 Pro 0813 (Max) | 23 | $1.77 | 17.6 min | 1M |
| Qwen3.8 27B (Xhigh) | 20 | $3.53 | 38.6 min | 256k |
| MiniMax-M3 | 19 | $1.29 | 15.3 min | 1M |
| K2 Horizon 375B A23B | 18 | $0.00 | 4.5 min | 524k |
| Nemotron 3.5 Super VL | 14 | $0.48 | 4.4 min | 1M |
| Nemotron 3 Ultra 550B A55B Reasoning | 12 | $2.21 | 4.4 min | 262k |
| Nemotron 3.5 Lightning | 6 | $0.31 | 3.9 min | 1M |
| Mistral Medium 3.5 | 5 | $1.04 | 4.6 min | 256k |
| Gemma 4 E4B Reasoning | 5 | $0.0083 | 4.3 min | 128k |
| Gemma 4 31B Reasoning | 4 | n/a | n/a | 256k |
| Mistral Small 4 Reasoning | 4 | $0.0399 | 1.7 min | 256k |
| gpt-oss-120b (High) | 4 | $0.35 | 6.5 min | 131k |

The GLM-5.3 Low row comes from the [AA GLM-5.3 page](https://artificialanalysis.ai/models/glm-5-3). All other rows come from the [AA leaderboard](https://artificialanalysis.ai/leaderboards/models).

- Several models appear on the AA leaderboard with **no Index score**: Qwen3.8 2.4T A95B (the open flagship), Kimi K2.7 Code, Llama 4 Maverick and Scout, Qwen3.5 397B, gpt-oss-20b, Gemma 4 12B non-reasoning, Ministral 3 and Magistral. — [AA leaderboard](https://artificialanalysis.ai/leaderboards/models)
- The AA "open-weights" page showed only 11 of 396 models with its default filter. It did **not** list GLM-5.3-Flash, MiniMax-M3.1-Flash, DeepSeek V4 Pro or Qwen3.8-Flash-Next, even though Hugging Face hosts weights for most of them. — [AA open-weights page](https://artificialanalysis.ai/models/open-source); HF API, e.g. [GLM-5.3-Flash](https://huggingface.co/api/models/zai-org/GLM-5.3-Flash)
- The original DeepSeek V4.1 Flash page (September 2026 checkpoint) is marked deprecated. Its Index is "N/A", and it points to V4.1 Flash 1017 (33) as the recommended newer release. — [AA DeepSeek V4.1 Flash page](https://artificialanalysis.ai/models/deepseek-v4-1-flash)

**AA v5.0.1 closed-model reference bar** — [AA leaderboard](https://artificialanalysis.ai/leaderboards/models)

| Closed model | AA v5.0.1 |
|---|---|
| Claude Fable 5.2 Max | 65 |
| GPT-6.2 Astra Max | 62 |
| Gemini 4 Neon Xhigh | 61 |
| Claude Opus 5.5 Max | 59 |
| GPT-6.2 Sol Max | 57 |
| Claude Sonnet 5.5 Max | 55 |
| Gemini 4 Argon High | 50 |
| Claude Haiku 5.5 Max | 36 |
| GPT-6 Luna Max | 28 |
| Gemini 3.5 Flash-Lite | 12 |

**Vals Index v2.2 (INDEPENDENT; GDP-weighted finance, coding, legal and tax agent tasks; updated 2026-11-18)** — [Vals Index](https://www.vals.ai/benchmarks/vals_index)
- Formula: (8.0×Finance + 5.6×Coding + 1.2×Legal + 0.5×Tax)/15.3. Finance = Finance Agent v2.1 + Excel Modeling v1.1. Coding = Terminal-Bench 4.0, Vibe Code Bench v1.1, Code Migration v1.1. Legal = Legal Research Bench, HLAB-Vals-1.1. Tax = Tax Agent Bench. — [Vals Index](https://www.vals.ai/benchmarks/vals_index)

Open-weight families:

| Rank | Model | Score | Cost/test | Duration/test |
|---|---|---|---|---|
| 14 | Qwen 4 Max (probably not open-weight, see Gaps) | 63.20% | $9.33 | 1h05m |
| 15 | Kimi K3.1 Pro | 62.52% | $6.44 | 1h04m |
| 16 | DeepSeek V4.1 Flash 1017 | 61.26% | $0.66 | 39m55s |
| 19 | GLM 5.3 | 59.85% | $8.52 | 1h04m |
| 21 | Qwen 3.8 Max 0902 | 59.05% | $8.73 | 1h46m |
| 25 | Mistral Large 4 | 56.53% | $3.72 | 47m48s |
| 26 | Inkling 2 Small | 56.08% | $3.51 | 50m35s |
| 30 | MiniMax-M3.1-Flash | 53.78% | $0.66 | 43m18s |
| 32 | DeepSeek V4 Pro 0813 | 52.97% | $2.50 | 58m03s |
| 33 | Kimi K3 | 52.95% | $7.17 | 1h15m |
| 35 | GLM 5.3 Flash | 50.86% | $2.05 | 1h04m |
| 41 | Inkling (v1) | 28.96% | $1.85 | 17m13s |
| 42 | Inkling Small (v1) | 27.59% | $0.40 | 16m26s |

gpt-oss is not on the Vals leaderboard. — [Vals Index](https://www.vals.ai/benchmarks/vals_index)

Closed reference on Vals v2.2:

| Model | Score |
|---|---|
| Claude Fable 5.2 | 71.31% |
| Gemini 4 Neon | 70.87% |
| Claude Sonnet 5.5 | 70.85% |
| Claude Opus 5.5 | 70.14% |
| GPT-6.2 Astra | 67.66% |
| GPT-6.2 Sol | 66.06% |
| Claude Haiku 5.5 | 58.73% |
| Gemini 3.8 Flash | 55.95% |

— [Vals Index](https://www.vals.ai/benchmarks/vals_index)

**Vendor-reported scores (VENDOR; Kimi model card; Kimi's own harness at reasoning_effort=max)** — [Kimi K3.1 Pro HF card](https://huggingface.co/moonshotai/Kimi-K3.1-Pro)

| Benchmark | Kimi K3.1 Pro | Claude Fable 5.1 | GPT-6 Astra | Claude Opus 5.5 | DeepSeek V4.1 Flash 1017 | GLM-5.3 |
|---|---|---|---|---|---|---|
| GPQA-Diamond | 94.2 | 93.7 | 96.1 | 93.9 | 92.2 | 91.7 |
| HLE-Full | 51.1 | 57.6 | 53.6 | 59.8 | 42.6 | 43.0* |
| HLE-Diamond | 39.4 | 55.1 | 65.8 | 60.9 | 21.6 | 25.1* |
| GDP.pdf | 34.6 | 27.6 | 34.2 | 30.6 | 17.2 | 11.2 |
| MMMU-Pro | 84.1 | 86.3 | 86.9 | 87.7 | 80.6 | — |
| Kimi Hallu Bench, no tools (lower is better) | 5.4 | 11.4 | 4.2 | 6.8 | 13.1 | 14.8 |

\* GLM-5.3 HLE is on the text-only subset. The card has no MMLU-Pro, IFEval/IFBench, multilingual or long-context scores.

**Conflicting secondary numbers (flag; do not use)**
- A search summary of secondary blogs (e.g. [morphllm](https://www.morphllm.com/kimi-k3-1), [kingy.ai](https://kingy.ai/blog/kimi-k3-1-pro/)) said "Kimi K3.1 Pro at 55 on the AA Index, GLM-5.3 (max) at 45, Qwen3.8 2.4T A95B at 40." These do **not** match AA's live v5.0.1 figures (46 / 32 / no score). They are probably from an older index version or a different date. The same summary gave GLM 5.3 a Vals score of 59.73% against 59.85% live, a small drift from re-runs.

### Inferences
- Within the same AA v5.0.1 version, the open-weight frontier (Kimi 46) sits about 9–19 points below the closed frontier (55–65) and about 10 points above Claude Haiku 5.5 (36). DeepSeek V4.1 Flash (33) is roughly at Haiku 5.5 level on AA. On Vals it is above Haiku 5.5 (61.26% vs 58.73%).
- The **Vals** gap is smaller than the AA gap. Kimi is about 8–9 points behind Claude Opus/Sonnet 5.5 on Vals. The cluster of DeepSeek Flash, GLM-5.3, Mistral Large 4 and Inkling 2 Small spans only about 5 points (56–61%).
- DeepSeek V4 Pro 0813 is now **dominated** by the newer V4.1 Flash 1017 on both indexes: AA 23 vs 33, Vals 52.97% vs 61.26%. It is no longer a reason to pay "Pro" costs.
- Kimi K3 (Vals 52.95%) is superseded by K3.1 Pro (62.52%). K2.x matters now only on writing benchmarks (see Q2).
- Both indexes are agentic, coding and science heavy. Neither directly measures "write a polite email in Spanish." For the fast tier, writing and speed data (Q2, Q3) matter more than AA v5 ranks.

### Gaps
- No per-sub-eval AA scores could be extracted for any model, so no AA GPQA, HLE, IFBench, AA-LCR, Omniscience or long-context numbers per model. The pages render them in charts without readable values.
- LMArena (now arena.ai) returned HTTP 403 to automated fetches (https://arena.ai/leaderboard/text). No Arena text, creative-writing or language-category scores were obtained.
- No LiveBench, SimpleBench, RULER or Fiction.LiveBench numbers were collected (not reached within the tool budget).
- Qwen3.8 2.4T A95B, the open Qwen flagship, has no AA v5 score. It is unclear whether Vals' "Qwen 3.8 Max 0902" is the same weights as the open 2.4T-A95B release.

---

## Q2. Writing quality (emails, reports, creative writing, tone) and multilingual quality

### Takeaway
On independent creative-writing Elo (EQ-Bench CW v3), the top open models are at or above the closed bar. Kimi K3.1 Pro (2172.6) is essentially tied with GPT-6 Astra (2176.9) and above Claude Fable 5.1 (2155.3). GLM-5.3 (2076.4) is above Claude Opus 5.5 (2050.9). Qwen3.8-27B (1670.5) writes about as well as Claude Sonnet 4.5 (1677.1), which is notable for a 27B Apache model. DeepSeek V4.x Flash/Pro sit around 1540–1560, roughly Claude Opus 4 level. No usable Spanish, Catalan, French or German benchmark numbers were found for these models.

### Cited Findings

**EQ-Bench Creative Writing v3 (INDEPENDENT; columns: elo_score, creative_writing_score (rubric), avg_length, vocab_complexity, slop_score, repetition_score; no date shown on the page)** — [EQ-Bench CW v3 data](https://eqbench.com/creative_writing.js), [page](https://eqbench.com/creative_writing.html)

Open-weight models:

| Model | Elo | Rubric | Avg length | Slop | Repetition |
|---|---|---|---|---|---|
| Kimi K3.1 Pro | 2172.6 | 16.63 | 5825 | 9.64 | 3.68 |
| Kimi K3 | 2083.3 | 16.35 | 5488 | 9.70 | 3.73 |
| GLM-5.3 | 2076.4 | 16.44 | 5913 | 8.42 | 3.23 |
| Qwen3.8-2.4T-A95B | 1843.8 | 15.29 | 6046 | 12.26 | 3.50 |
| GLM-5.2 | 1759.2 | 15.32 | — | 13.11 | — |
| Kimi K2.6 | 1721.0 | 14.93 | 8333 | 13.30 | 3.77 |
| Nemotron 3 Ultra 550B A55B | 1691.7 | 14.69 | 10536 | 18.42 | 3.23 |
| Qwen3.8-27B | 1670.5 | 12.96 | 5400 | 12.12 | 4.19 |
| Kimi K2 Instruct | 1665.5 | — | — | — | — |
| Kimi K2 Thinking | 1630.6 | — | — | — | — |
| Inkling (v1) | 1609.1 | 14.18 | 8378 | 15.02 | 4.22 |
| GLM-5 | 1600.7 | — | — | — | — |
| GLM-5.1 | 1593.9 | — | — | — | — |
| Kimi K2.5 | 1578.8 | — | — | — | — |
| DeepSeek V4 Flash | 1559.4 | 13.95 | 6031 | 20.92 | 4.30 |
| DeepSeek V4 Pro | 1552.6 | 14.99 | 7444 | 19.66 | 3.21 |
| DeepSeek V4.1 Flash | 1539.9 | 14.05 | 6121 | 22.42 | 5.21 |
| DeepSeek V3.2 | 1514.9 | — | — | — | — |
| MiMo-V2.5-Pro | 1493.1 | — | — | — | — |
| Inkling Small (v1) | 1491.4 | 11.78 | 8589 | 14.67 | 3.78 |
| Qwen3.5-397B-A17B | 1478.3 | — | — | — | — |
| Mistral Large 3 (675B, 2512) | 1412.6 | 12.46 | 6269 | 28.17 | 5.96 |
| Gemma 4 31B-it | 1368.6 | 13.60 | 5884 | 29.69 | 5.67 |
| MiniMax M2.5 | 1361.6 | — | — | 26.78 | — |
| Gemma 4 26B-A4B | 1305.1 | — | — | — | — |
| Gemma 4 12B | 1289.5 | — | — | — | — |
| Nemotron 3.5 Lightning 30B-A3B | 1280.9 | — | — | — | — |
| Mistral Small 3.2 24B | 1256.2 | 11.44 | 4696 | 32.82 | 6.97 |
| GLM-4.7-Flash | 1138.6 | — | — | — | — |
| gpt-oss-120b | 956.0 | 9.57 | 10270 | 31.35 | 4.03 |
| Llama 4 Maverick | 858.1 | — | — | — | — |
| Llama 4 Scout | 781.1 | — | — | — | — |

Muse Glimmer-30B (1804.3) is also on the list. Wavect lists it as Apache 2.0 open weights. — [EQ-Bench data](https://eqbench.com/creative_writing.js), [Wavect](https://wavect.io/blog/open-weight-llm-comparison-2026/)

Closed reference on the same leaderboard:

| Model | Elo |
|---|---|
| GPT-6 Astra | 2176.9 |
| Claude Fable 5.1 | 2155.3 |
| Claude Opus 5 | 2135.0 |
| GPT-6 Sol | 2126.0 |
| Claude Opus 5.5 | 2050.9 |
| Claude Fable 5 | 1943.6 |
| Claude Sonnet 5 | 1797.9 |
| Gemini 4 Argon | 1757.8 |
| Claude Sonnet 4.5 | 1677.1 |
| Claude Sonnet 4 | 1482.6 |
| GPT-4o (chatgpt-4o-latest 2025-03-27) | 1500.9 |

— [EQ-Bench data](https://eqbench.com/creative_writing.js)

- **Not on EQ-Bench CW v3**: Mistral Large 4, Mistral Medium 3.5, Mistral Small 4, MiniMax M3/M3.1-Flash, GLM-5.3-Flash, Inkling 2 Small, MiMo-V2.6. The closest proxies are their predecessors: Mistral Large 3 at 1412.6, Mistral Medium 3.1 at 1475.5 (API) and Inkling Small v1 at 1491.4. — [EQ-Bench data](https://eqbench.com/creative_writing.js)
- **GDPval-AA** (AA's realistic knowledge-work deliverable eval) is no longer part of AA Index v5. No per-model GDPval-AA scores were retrieved. — [AA methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)
- GDP.pdf, a document-deliverable eval in the AA v5 Knowledge Work category, has **vendor** numbers on Kimi's card: Kimi K3.1 Pro 34.6, GPT-6 Astra 34.2, Opus 5.5 30.6, DeepSeek V4.1 Flash 1017 17.2, GLM-5.3 11.2. — [Kimi HF card (VENDOR)](https://huggingface.co/moonshotai/Kimi-K3.1-Pro)
- Hallucination, relevant to "trustworthy office answers". Vendor Kimi Hallu Bench (lower is better): Kimi K3.1 Pro 5.4, Opus 5.5 6.8, DeepSeek V4.1 Flash 13.1, GLM-5.3 14.8. This is **vendor-reported on the vendor's own benchmark** and needs independent confirmation, e.g. AA-Omniscience. — [Kimi HF card](https://huggingface.co/moonshotai/Kimi-K3.1-Pro)

**Multilingual**
- MMLU-ProX covers 29 languages in the paper (the project site lists 13, including Spanish). No results for Qwen3.8, GLM-5.3, DeepSeek V4.1 or Mistral Large 4 were found. The most recent aggregate leaderboard found (BenchLM) lists Qwen3.7 Max at 87%, Claude Opus 4.5 at 85.7%, Qwen3.7 Plus at 85.4% and GLM-5 at 83.1%. These are older generations and all-language averages, not Spanish splits. — [MMLU-ProX paper](https://arxiv.org/pdf/2503.10497), [mmluprox.github.io](https://mmluprox.github.io), [BenchLM MMLU-ProX](https://benchlm.ai/benchmarks/mmluprox)

### Inferences
- For a writing-centric workspace, **GLM-5.3** is the standout value. Its writing Elo is at Claude Opus 5.5 level, it has the lowest slop (8.42) and repetition (3.23) among top open models, and its AA/Vals scores are mid-pack. **Kimi K3.1 Pro** writes best but is slow (Q3).
- **DeepSeek V4.1 Flash** is strong on agentic indexes but only mid on prose (Elo 1539.9, slop 22.42, repetition 5.21, the worst among the top open models). It suits structured tasks better than tone-sensitive writing.
- **Qwen3.8-27B** (Apache 2.0, 27B dense) beats much larger DeepSeek models on creative writing (1670.5 vs about 1540–1560). This makes it a candidate for a self-hosted cheap writing tier.
- Mistral (the EU vendor) has no current-generation writing score. Its last measured open model (Large 3, 1412.6) trails every Chinese frontier open model by 150–760 Elo. Large 4 must be tested in-house before it is assumed to match.
- EQ-Bench CW measures creative fiction, not business emails. Ranking similarity for emails and reports is plausible but unproven.

### Gaps
- No independent Spanish, Catalan, French or German scores for any current model: no Arena language categories (403), no MMLU-ProX splits, no Global-MMLU. **This is the largest gap for a Spain-based product.** Recommend an in-house Spanish/Catalan eval.
- No Arena creative-writing category (403).
- EQ-Bench judge methodology and date were not captured from the page.
- No instruction-following (IFEval/IFBench) numbers per model.

---

## Q3. Speed, latency and verbosity (tokens spent per task)

### Takeaway
In max-reasoning modes, all strong open models have very long **time-to-first-answer-token** (TTFT) on AA: 40–160 s, because thinking happens first. For a non-technical user that is unacceptable for simple tasks. The fast tier must run **non-reasoning or low effort**. Examples: DeepSeek V4.1 Flash non-reasoning has 0.89 s TTFT and about 225 tok/s; GLM-5.3 Low has 9.54 s TTFT and half the tokens of Max. Kimi K3.1 Pro is the slowest strong model (31 tok/s, 158.74 s TTFT on Kimi's API).

### Cited Findings
AA defines TTFT as "time to first answer token", which includes the reasoning time. Speeds are medians across providers unless noted.

| Model / mode | Output tok/s | TTFT (first answer token) | Output tokens to run AA Index | Price in/out per 1M (blended 7:2:1) | Source |
|---|---|---|---|---|---|
| Kimi K3.1 Pro | 31 | 158.74 s (Kimi API) | 113M | $2.00 / $10.00 (blended $1.54) | [AA Kimi](https://artificialanalysis.ai/models/kimi-k3-1-pro) |
| DeepSeek V4.1 Flash 1017 (Max) | 172 | 41.57 s | n/a | blended $0.18 | [AA open-weights page](https://artificialanalysis.ai/models/open-source), [AA leaderboard](https://artificialanalysis.ai/leaderboards/models) |
| DeepSeek V4.1 Flash (Sept checkpoint), Max | 222 | 36.67 s | n/a | $0.30 / $1.20 (blended $0.18) | [AA V4.1 Flash](https://artificialanalysis.ai/models/deepseek-v4-1-flash) |
| DeepSeek V4.1 Flash (Sept checkpoint), Non-reasoning | 225 | 0.89 s | n/a | same as above | [AA V4.1 Flash](https://artificialanalysis.ai/models/deepseek-v4-1-flash) |
| GLM-5.3 (Max) | 86 | 67.58 s | 135M | $1.40 / $4.40 (blended $0.90) | [AA GLM-5.3](https://artificialanalysis.ai/models/glm-5-3) |
| GLM-5.3 (Low) | 68 | 9.54 s | 63.3M | n/a | [AA GLM-5.3](https://artificialanalysis.ai/models/glm-5-3) |
| Inkling 2 Small | 117 | 40.01 s | n/a | blended $0.18 | [AA open-weights page](https://artificialanalysis.ai/models/open-source), [AA leaderboard](https://artificialanalysis.ai/leaderboards/models) |
| MiMo-V2.6-Pro | 57 | 42.18 s | n/a | blended $0.18 | same as above |
| Mistral Large 4 (High) | 66 | 73.31 s | n/a | blended $0.40 | same as above |
| Qwen3.8 27B (Xhigh) | 47 | 129.08 s | n/a | blended $0.47 | same as above |
| MiniMax-M3.1-Flash | n/a | 49.36 s | n/a | n/a | [AA leaderboard](https://artificialanalysis.ai/leaderboards/models) |
| GLM-5.3-Flash | n/a | 85.70 s | n/a | n/a | same |
| K2 Horizon 375B A23B | 238 | 17.03 s | n/a | n/a | same as above |
| Nemotron 3.5 Super VL | 307 | 12.29 s | n/a | blended $0.11 | same as above |

- Reference medians for open-weight models of similar size: 101M output tokens to run the Index, 18.60 s TTFT, 13.8 min per task, $0.43 in / $1.59 out. — [AA Kimi page](https://artificialanalysis.ai/models/kimi-k3-1-pro), [AA GLM-5.3 page](https://artificialanalysis.ai/models/glm-5-3)
- Non-reasoning open models with low TTFT on AA: Qwen3 Next 80B A3B Instruct 1.19 s, Llama 4 Maverick 1.29 s, Llama 4 Scout 1.13 s, gpt-oss-20b Low 1.82 s, Ministral 3 14B 2.37 s, Ministral 3 8B 1.92 s, Qwen3.6 35B A3B Non-reasoning 3.22 s, Qwen3.5 122B A10B Non-reasoning 4.51 s. Closed reference: GPT-5.5 Instant 1.76 s. — [AA leaderboard](https://artificialanalysis.ai/leaderboards/models)
- Closed reference TTFT in max modes: Claude Opus 5.5 Max 359.20 s, GPT-6.2 Sol Max 75.06 s, Claude Haiku 5.5 Max 182.61 s. — [AA leaderboard](https://artificialanalysis.ai/leaderboards/models)
- Cost per AA Index task, which captures verbosity times price:

| Model | Cost/Index task |
|---|---|
| DeepSeek V4.1 Flash 1017 | $0.60 |
| MiniMax-M3.1-Flash | $0.49 |
| GLM-5.3-Flash | $0.58 |
| Inkling 2 Small | $1.18 |
| Mistral Large 4 | $2.06 |
| Kimi K3.1 Pro | $3.68 |
| GLM-5.3 Max | $5.01 |
| Qwen3.8 27B Xhigh | $3.53 |
| Claude Opus 5.5 (reference) | $10.04 |
| Claude Haiku 5.5 (reference) | $0.41 |

— [AA leaderboard](https://artificialanalysis.ai/leaderboards/models)

### Inferences
- Verbosity changes the economics. GLM-5.3 Max costs $5.01 per task despite a $0.90 blended price, because it uses 135M tokens. That is more than Kimi ($3.68) and 8x DeepSeek V4.1 Flash ($0.60) for about the same AA score as DeepSeek (32 vs 33).
- Qwen3.8 27B at Xhigh is a poor deal on AA: 20 points, $3.53 per task, 129 s TTFT, which signals heavy overthinking. Its value is in non-thinking or low-effort writing, which AA did not test.
- For EU self-hosting, AA tok/s figures come from vendors' and providers' own GPUs. EU hosts will differ. Benchmark your own deployment.

### Gaps
- No AA output-token counts were extracted for DeepSeek V4.1 Flash 1017, Inkling 2 Small, MiniMax, Mistral or Qwen; the chart values were not readable.
- No non-reasoning TTFT or tok/s for Kimi K3.1 Pro (low effort), Mistral Large 4 non-reasoning, or GLM-5.3-Flash non-reasoning.

---

## Q4. Thinking / reasoning modes and the quality change between modes

### Takeaway
Most current open frontier models ship reasoning effort controls. **Kimi K3.1 Pro** offers low, high and max (default max). **DeepSeek V4.1 Flash** offers Max and Non-reasoning. **GLM-5.3** offers Max and Low. Mistral Large 4, Qwen3.8 and gpt-oss expose effort labels (High, Xhigh, Low/High). The only measured same-model quality delta is GLM-5.3: AA v5 drops from 32 (Max) to 23 (Low) while tokens halve and TTFT falls from 67.6 s to 9.5 s.

### Cited Findings
- Kimi K3.1 Pro: `reasoning_effort` "supports `"low"`, `"high"`, and `"max"` (default `"max"`)". Benchmark results use max. AA lists only one variant. — [Kimi HF card (VENDOR)](https://huggingface.co/moonshotai/Kimi-K3.1-Pro), [AA Kimi page](https://artificialanalysis.ai/models/kimi-k3-1-pro)
- DeepSeek V4.1 Flash: AA lists "(Max)" (reasoning) and "(Non-reasoning)" variants. Non-reasoning TTFT is 0.89 s vs 36.67 s for Max. No index score is shown for non-reasoning. — [AA V4.1 Flash](https://artificialanalysis.ai/models/deepseek-v4-1-flash)
- GLM-5.3: Max 32 / Low 23 (AA v5.0.1). Output tokens 135M vs 63.3M. TTFT 67.58 s vs 9.54 s. Time per task 23.1 vs 12.8 min. No non-reasoning variant is listed. — [AA GLM-5.3](https://artificialanalysis.ai/models/glm-5-3)
- Effort labels on the AA leaderboard: Mistral Large 4 "High", Qwen3.8 27B "Xhigh", gpt-oss-120b "High", gpt-oss-20b "Low", Mistral Small 4 "Reasoning", Gemma 4 31B and E4B "Reasoning" vs Gemma 4 12B "Non-reasoning", Nemotron 3 Ultra "Reasoning", Muse Spark Open "Xhigh". — [AA leaderboard](https://artificialanalysis.ai/leaderboards/models)
- AA runs reasoning models with the maximum output tokens their creators disclose, at temperature 0.6 unless the lab recommends otherwise. — [AA methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)
- EQ-Bench CW tested Kimi K2 Instruct (1665.5) and K2 Thinking (1630.6) separately. The thinking variant scored **lower** on creative writing. — [EQ-Bench data](https://eqbench.com/creative_writing.js)

### Inferences
- For a router, effort level is a second knob alongside model choice. "GLM-5.3 Low" or "DeepSeek V4.1 Flash non-reasoning" can serve the balanced and fast tiers from the same deployed weights as the strong tier. That reduces the number of models to host in the EU.
- The Kimi K2 Instruct vs Thinking result suggests that thinking does not help prose, and may hurt it. Route writing tasks to non-thinking or low effort. This is one data point; validate it.

### Gaps
- No AA score for Kimi K3.1 Pro at low or high effort, DeepSeek V4.1 Flash non-reasoning, or Mistral Large 4 non-reasoning. The quality loss from turning thinking off is unmeasured for most candidates.

---

## Q5. Licenses (commercial restrictions)

### Takeaway
The cleanest licenses are **MIT**: DeepSeek V4.1 Flash, DeepSeek V4 Pro, GLM-5.3-Flash and MiMo-V2.6. **Apache 2.0** covers Qwen3.8-27B, Inkling 2 Small, Mistral Small 4, Gemma 4 31B, gpt-oss-120b and Muse Glimmer-30B. Custom licenses that need legal review cover **Kimi K3.1 Pro**, **GLM-5.3**, **Qwen3.8-2.4T-A95B**, **MiniMax M3/M3.1-Flash**, **Mistral Large 4** and **Medium 3.5**, Nemotron 3.5 and Llama 4. Two of them reportedly have conditions aimed at large model-as-a-service or "AI work-assistant" businesses, which is exactly this product.

### Cited Findings
| Model | HF license tag | Notes | Source |
|---|---|---|---|
| DeepSeek V4.1 Flash (HF created 2026-09-10) | MIT | — | [HF API](https://huggingface.co/api/models/deepseek-ai/DeepSeek-V4.1-Flash); AA page also says MIT, [AA](https://artificialanalysis.ai/models/deepseek-v4-1-flash) |
| DeepSeek V4 Pro (created 2026-04-22) | MIT | — | [HF API](https://huggingface.co/api/models/deepseek-ai/DeepSeek-V4-Pro) |
| GLM-5.3 (created 2026-08-25) | other: "glm-5.3" | AA FAQ: "Commercial use is allowed with restrictions." Wavect: "permissive, not labelled MIT." Possible conflict; read the file. | [HF API](https://huggingface.co/api/models/zai-org/GLM-5.3), [AA GLM-5.3](https://artificialanalysis.ai/models/glm-5-3), [Wavect](https://wavect.io/blog/open-weight-llm-comparison-2026/) |
| GLM-5.3-Flash (created 2026-08-25; 320B total / 18B active per Wavect) | MIT | — | [HF API](https://huggingface.co/api/models/zai-org/GLM-5.3-Flash), [Wavect](https://wavect.io/blog/open-weight-llm-comparison-2026/) |
| Kimi K3.1 Pro (HF repo created 2026-11-02; AA FAQ release 2026-10-23) | other: "kimi-k3.1-pro" | Wavect: "extra conditions for large model-as-a-service businesses and very large commercial products", with exemptions for qualifying internal use. Secondary search summary: "modified MIT… conditions for large hosted services and products over 100M monthly users" (unverified against the LICENSE file). | [HF API](https://huggingface.co/api/models/moonshotai/Kimi-K3.1-Pro), [Wavect](https://wavect.io/blog/open-weight-llm-comparison-2026/), [orcarouter](https://www.orcarouter.ai/blog/kimi-k3-1-pro-open-weights) |
| Qwen3.8-27B (created 2026-08-05) | Apache 2.0 | — | [HF API](https://huggingface.co/api/models/Qwen/Qwen3.8-27B) |
| Qwen3.8-2.4T-A95B | Qwen3.8-Max License | "Conditions for very large products and large MaaS or AI work-assistant businesses" | [Wavect](https://wavect.io/blog/open-weight-llm-comparison-2026/) |
| Qwen3.8-Flash-Next | Qwen Community License 1.0 per Wavect | Third-party quantized repos on HF are tagged apache-2.0, a conflict; check the official repo | [Wavect](https://wavect.io/blog/open-weight-llm-comparison-2026/), [HF search](https://huggingface.co/api/models?search=Qwen3.8) |
| Inkling 2 Small (created 2026-11-04) | Apache 2.0 | — | [HF API](https://huggingface.co/api/models/thinkingmachines/Inkling-2-Small) |
| MiniMax-M3 (created 2026-06-02) | other: "minimax-community" | — | [HF API](https://huggingface.co/api/models/MiniMaxAI/MiniMax-M3) |
| MiniMax-M3.1-Flash (created 2026-10-17) | other | — | [HF search](https://huggingface.co/api/models?search=MiniMax-M3.1) |
| Mistral Large 4 1T-A52B (created 2026-09-30) | other | — | [HF search](https://huggingface.co/api/models?search=Mistral-Large-4) |
| Mistral Medium 3.5 128B (created 2026-03-31) | other | — | [HF search](https://huggingface.co/api/models?search=Mistral-Medium-3.5) |
| Mistral Small 4 119B 2603 (created 2026-01-23) | Apache 2.0 | — | [HF search](https://huggingface.co/api/models?search=Mistral-Small-4) |
| Gemma 4 31B-it | Apache 2.0 | — | [HF search](https://huggingface.co/api/models?search=gemma-4-31B) |
| gpt-oss-120b | Apache 2.0 | — | [HF search](https://huggingface.co/api/models?search=gpt-oss-120b) |
| Nemotron 3.5 Super VL 120B-A12B (created 2026-10-12) | other | — | [HF search](https://huggingface.co/api/models?search=Nemotron-3.5-Super) |
| MiMo-V2.6 Pro/Flash (created 2026-09-21) | MIT | — | [HF search](https://huggingface.co/api/models?search=MiMo-V2.6) |
| Llama 4 Scout/Maverick | Llama 4 Community License | The use policy "withholds the multimodal grant from EU-domiciled individuals and companies, with an end-user exception" | [Wavect](https://wavect.io/blog/open-weight-llm-comparison-2026/) |
| Muse Glimmer-30B | Apache 2.0 | — | [Wavect](https://wavect.io/blog/open-weight-llm-comparison-2026/) |
| Muse Spark Open | Gated Muse Model License | "Attribution, use-policy and model-as-a-service conditions" | [Wavect](https://wavect.io/blog/open-weight-llm-comparison-2026/) |
| Tencent Hy4 preview | Apache 2.0 for the preview weights | Final terms "to be confirmed" | [Wavect](https://wavect.io/blog/open-weight-llm-comparison-2026/) |

- No official open-weight **Qwen4** repo was found on Hugging Face. A search for "Qwen4" returned only unrelated community repos. "Qwen 4 Max" appears on AA (43) and Vals (63.20%). — [HF search](https://huggingface.co/api/models?search=Qwen4), [AA leaderboard](https://artificialanalysis.ai/leaderboards/models), [Vals](https://www.vals.ai/benchmarks/vals_index)

### Inferences
- A hosted workspace sold to businesses is plausibly "model-as-a-service" or an "AI work-assistant business" under the Kimi, Qwen3.8-Max and Muse Spark licenses. Legal must read those LICENSE files before Kimi K3.1 Pro is chosen for the strong tier.
- If legal review blocks Kimi K3.1 Pro, the next-best license-safe strong option is DeepSeek V4.1 Flash 1017 at max effort (MIT, AA 33, Vals 61.26%).
- Qwen 4 Max should be treated as **closed/API-only** until weights appear. It is not a candidate.

### Gaps
- The LICENSE texts for Kimi K3.1 Pro, GLM-5.3, MiniMax, Mistral Large 4 / Medium 3.5 and Nemotron were not read verbatim. Exact MAU or revenue thresholds and attribution clauses are unconfirmed.

---

## Q6. Comparison to the ChatGPT/Claude quality bar, task by task

### Takeaway
- **Prose and creative writing:** top open models (Kimi K3.1 Pro, GLM-5.3) already match or beat current Claude and GPT.
- **Hard agentic analysis** (finance, legal, multi-step work products): open models trail by about 8–10 Vals points and 9–19 AA v5 points. Kimi K3.1 Pro is roughly a "Gemini 4 Argon / below Claude Sonnet 5.5" level model.
- **Cheap tier:** DeepSeek V4.1 Flash is at or above Claude Haiku 5.5 on Vals, and close to it on AA.
- **Speed and responsiveness:** the strong open models are much slower than what users expect from ChatGPT.

### Cited Findings
- Hard analysis and agentic work (Vals v2.2): Claude Opus 5.5 70.14%, Sonnet 5.5 70.85%, GPT-6.2 Sol 66.06%, Kimi K3.1 Pro 62.52%, DeepSeek V4.1 Flash 61.26%, GLM-5.3 59.85%, Claude Haiku 5.5 58.73%. — [Vals](https://www.vals.ai/benchmarks/vals_index)
- General intelligence (AA v5.0.1): Opus 5.5 59, Sonnet 5.5 55, Gemini 4 Argon 50, Kimi K3.1 Pro 46, Haiku 5.5 36, DeepSeek V4.1 Flash 33, GLM-5.3 32, GPT-6 Luna 28. — [AA leaderboard](https://artificialanalysis.ai/leaderboards/models)
- Creative writing (EQ-Bench CW v3): GPT-6 Astra 2176.9, Kimi K3.1 Pro 2172.6, Claude Fable 5.1 2155.3, GLM-5.3 2076.4, Claude Opus 5.5 2050.9, Claude Sonnet 5 1797.9, Qwen3.8-27B 1670.5, DeepSeek V4.1 Flash 1539.9. — [EQ-Bench data](https://eqbench.com/creative_writing.js)
- Science and knowledge, vendor-reported on the Kimi card: GPQA-Diamond is near parity (Kimi 94.2 vs Opus 5.5 93.9 vs GPT-6 Astra 96.1). HLE-Full shows a gap (Kimi 51.1 vs Opus 5.5 59.8). — [Kimi HF card (VENDOR)](https://huggingface.co/moonshotai/Kimi-K3.1-Pro)
- Responsiveness: GPT-5.5 Instant TTFT is 1.76 s, against Kimi K3.1 Pro at 158.74 s and DeepSeek V4.1 Flash non-reasoning at 0.89 s. — [AA leaderboard](https://artificialanalysis.ai/leaderboards/models), [AA V4.1 Flash](https://artificialanalysis.ai/models/deepseek-v4-1-flash)

### Inferences
| Task | Best open option | Gap vs the ChatGPT/Claude bar |
|---|---|---|
| Emails, short rewrites, summaries | DeepSeek V4.1 Flash non-reasoning, GLM-5.3 Low, Qwen3.8-27B | Likely at parity for 50-year-old office users, provided latency is low. Not directly benchmarked; Spanish quality unverified. |
| Long reports and polished prose | GLM-5.3, Kimi K3.1 Pro | At parity or better (EQ-Bench). |
| Hard multi-step analysis (spreadsheets, finance, legal) | Kimi K3.1 Pro | Noticeable gap: about 8 Vals points below Opus/Sonnet 5.5, 13 AA points below Opus 5.5. |
| Factual Q&A without tools | — | Unverified independently. Vendor data says Kimi hallucinates less than Opus 5.5, but DeepSeek and GLM hallucinate about 2x more (vendor). |

### Gaps
- No independent head-to-head on business emails or summaries (Arena was blocked). There is no Spanish-language comparison against ChatGPT or Claude.

---

## Q7. Recommended tier mapping (fast/cheap, balanced, strong) for general assistant tasks

### Takeaway
Suggested router (all candidates have weights on Hugging Face):
- **Fast/cheap:** DeepSeek V4.1 Flash 1017 in non-reasoning mode (MIT). Alternates: Qwen3.8-27B non-thinking (Apache) for small self-hosting, or Mistral Small 4 (Apache, EU vendor).
- **Balanced:** DeepSeek V4.1 Flash 1017 at max/reasoning (MIT). For writing-heavy tasks, GLM-5.3 at Low effort (custom license).
- **Strong:** Kimi K3.1 Pro at high or max effort (custom license; legal check required). License-safe fallback: DeepSeek V4.1 Flash Max.
- **Writing specialist:** GLM-5.3 (or Kimi K3.1 Pro at low effort).

### Cited Findings (justification, consistent numbers: AA v5.0.1 / Vals v2.2 / EQ-Bench CW v3 Elo)

| Tier | Model and mode | AA v5 | Vals v2.2 | EQ-CW Elo | Speed / TTFT | License |
|---|---|---|---|---|---|---|
| Fast | DeepSeek V4.1 Flash, non-reasoning | n/a (Max = 33) | 61.26% (1017) | 1539.9 | 225 tok/s, 0.89 s (Sept checkpoint) | MIT |
| Fast, self-host alternate | Qwen3.8-27B | 20 at Xhigh | n/a | 1670.5 | 47 tok/s at Xhigh | Apache 2.0 |
| Balanced | DeepSeek V4.1 Flash 1017 Max | 33 | 61.26% | 1539.9 | 172 tok/s, 41.57 s; $0.60/task | MIT |
| Balanced, writing | GLM-5.3 Low | 23 (Max = 32) | 59.85% (default) | 2076.4 | 68 tok/s, 9.54 s | GLM-5.3 custom |
| Strong | Kimi K3.1 Pro | 46 | 62.52% | 2172.6 | 31 tok/s, 158.74 s; $3.68/task | Kimi custom |
| Strong, license-safe | DeepSeek V4.1 Flash 1017 Max | 33 | 61.26% | 1539.9 | as above | MIT |
| Considered, not first choice | Inkling 2 Small | 31 | 56.08% | n/a (v1 Small 1491.4) | 117 tok/s, 40.01 s | Apache 2.0 |
| Considered, not first choice | Mistral Large 4 High | 26 | 56.53% | n/a (Large 3 1412.6) | 66 tok/s, 73.31 s | other |
| Considered, not first choice | MiniMax-M3.1-Flash | 29 | 53.78% | n/a | 49.36 s | other |
| Considered, not first choice | GLM-5.3-Flash | 28 | 50.86% | n/a | 85.70 s | MIT |
| Considered, not first choice | DeepSeek V4 Pro 0813 | 23 | 52.97% | 1552.6 | 54.42 s | MIT |
| Dropped | gpt-oss-120b, Gemma 4 31B, Mistral Small 4, Mistral Medium 3.5, Llama 4 | 4–5, or not scored | — | 956 / 1368.6 / — / — / 858.1 (Maverick) | — | — |

Sources: [AA leaderboard](https://artificialanalysis.ai/leaderboards/models), [AA open-weights page](https://artificialanalysis.ai/models/open-source), [AA V4.1 Flash](https://artificialanalysis.ai/models/deepseek-v4-1-flash), [AA GLM-5.3](https://artificialanalysis.ai/models/glm-5-3), [AA Kimi](https://artificialanalysis.ai/models/kimi-k3-1-pro), [Vals](https://www.vals.ai/benchmarks/vals_index), [EQ-Bench data](https://eqbench.com/creative_writing.js), HF API license tags (Q5).

### Inferences
- **Why DeepSeek V4.1 Flash is the backbone.** It has the best quality per euro among open models: AA 33 at $0.60 per task vs GLM-5.3 at 32 for $5.01. It is at or above Claude Haiku 5.5 on Vals and has an MIT license. Its non-reasoning mode gives sub-second TTFT. One set of weights can serve both the fast and balanced tiers, which simplifies EU hosting. The 552B/16B-active figures come from the AA page; Wavect counts 763B from safetensors (conflict noted).
- **Why Kimi K3.1 Pro is strong-tier only.** It leads every independent open-model measure: AA 46, Vals 62.52%, EQ 2172.6. But 31 tok/s, 158.74 s TTFT and a 2.8T-parameter footprint make it slow and expensive to self-host. It should be invoked only for explicitly hard tasks, with a "thinking…" UX, and at low or high effort where possible. Its license must be cleared for a MaaS or work-assistant business.
- **Why GLM-5.3 for writing.** Its EQ-Bench Elo (2076.4) is above Claude Opus 5.5, with the lowest slop among the top open models. Low effort keeps TTFT at about 10 s and halves tokens. Avoid Max for routine work because of the 135M-token verbosity ($5.01 per task).
- **EU-vendor option.** Mistral Large 4 (AA 26, Vals 56.53%) and Mistral Small 4 (Apache) are below the Chinese leaders on every independent measure found. They are worth keeping only if "EU-origin model" is itself a selling point. Large 4 writing and Spanish quality are unmeasured.
- **Must-do before launch:** an in-house Spanish/Catalan/French/German eval on emails, summaries and reports for the 4–5 shortlisted models; TTFT/tok/s benchmarks on the actual EU hosting stack; and legal review of the Kimi, GLM-5.3 and MiniMax licenses.

### Gaps
- Tier assignments rest on agentic indexes and creative-writing Elo. No independent data covers business-email quality, Spanish/Catalan fluency, instruction following or long-context recall (AA-LCR, RULER, Fiction.LiveBench) for these models. LMArena was inaccessible (HTTP 403), and LiveBench and SimpleBench were not collected.
