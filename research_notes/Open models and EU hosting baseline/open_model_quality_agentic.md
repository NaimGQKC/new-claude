# Open-weight LLM quality for agentic work, deep research, tool calling, factual reliability, vision and file/code generation (as of 2026-11-18)

Notes on method and conventions (read first):
- "Independent" = measured by a third party (Artificial Analysis, Vectara, LLM-AggreFact maintainers, benchmark owners). "Vendor" = numbers in the model maker's own model card/blog. Vendor tables routinely use different harnesses (Claude Code, Codex, mini-SWE-agent, in-house), effort settings ("max") and benchmark versions, so cross-vendor tables are NOT like-for-like.
- All Artificial Analysis (AA) numbers below were extracted on 2026-11-18 from the data embedded in AA's own model pages (https://artificialanalysis.ai/models/inkling-2-small, https://artificialanalysis.ai/models/gpt-oss-120b, https://artificialanalysis.ai/models/claude-opus-5-5). They are AA Intelligence Index **v5.0.1** values. AA's v5.0.1 index comprises 9 evals: AA-Briefcase v1.1, AutomationBench-AA, Terminal-Bench 4.0, FrontierCode-AA 2.0, AA-Omniscience v1.1, GDP.pdf, HLE-Diamond, CritPt v2 (Hard), Terminal-Bench-Science 0.1 — [AA model page](https://artificialanalysis.ai/models/inkling-2-small). Older blog posts quote v4.x scores (e.g. "GLM-5.3 = 60", "Kimi K3.1 Pro = 55"); those are a different scale and must not be mixed with v5.0.1 numbers (Kimi K3.1 Pro: 55 on v4.3.2 vs 46 on v5.0.1 per [local-ai-zone Nov 2026 summary](https://local-ai-zone.github.io/blog/November_2026_AI_Model_Updates.html), aggregator).
- Many benchmarks named in the brief (tau2-bench, BFCL, SWE-bench Verified, OSWorld v1) have largely been superseded in Nov-2026 vendor cards by newer versions (Terminal-Bench 2.1/3.0/4.0, DeepSWE v1.1, Toolathlon Verified, tau3-Banking, OSWorld 2.0/2.1). Where only the older benchmark exists for a model, it is noted.

### Master table A — Independent Artificial Analysis data (retrieved 2026-11-18, AA Intelligence Index v5.0.1)
Source for every row: data embedded in [AA Inkling 2 Small page](https://artificialanalysis.ai/models/inkling-2-small) (open models), [AA gpt-oss-120b page](https://artificialanalysis.ai/models/gpt-oss-120b) and [AA Claude Opus 5.5 page](https://artificialanalysis.ai/models/claude-opus-5-5) (closed reference rows). Decimals are AA's raw values rounded to 1 dp. "Omni" = AA-Omniscience v1.1. TB4 = Terminal-Bench 4.0 as run by AA. "—" = AA shows null.

| Model (AA name) | Release (AA) | License (AA) | Params total/active (B) | AA Index v5.0.1 | TB4 (AA) | Omni Index (−100..100) | Omni accuracy | Omni hallucination rate | GDPval-AA v2.1 (Elo) | GDP.pdf all-pass | MMMU-Pro | AA-LCR | tau3-Banking | EnterpriseOps-Gym | Price $/1M in/out |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kimi K3.1 Pro | 2026-10-23 | Kimi K3.1-Pro Licence (custom) | 2800 / 104 | 46.5 | 67.2% | 29.9 | 48.9% | 37.3% | 1860.6 | 31.4% | 83.9% | 86.3% | — | — | 2.00 / 10.00 |
| DeepSeek V4.1 Flash 1017 | 2026-10-17 | MIT | 552 / 16 | 32.6 | 33.8% | 0.9 | 39.6% | 64.1% | 1745.8 | 17.2% | 80.6% | 82.7% | — | — | 0.30 / 1.20 |
| GLM-5.3 | 2026-08-18 | GLM-5.3 License (custom) | 753 / 40 | 31.7 | 41.9% | 6.0 | 32.3% | 38.9% | 1654.8 | 11.2% | — (text-only) | 79.7% | 50.3% | 36.4% | 1.40 / 4.40 |
| Inkling 2 Small (Thinking Machines) | 2026-11-05 | Apache 2.0 | 594 / 17 | 30.6 | 13.1% | 16.1 | 33.8% | 26.7% | 1630.2 | 25.2% | 81.6% | 83.3% | 40.4% | 46.8% | 0.30 / 1.00 |
| MiMo-V2.6-Pro (Xiaomi) | 2026-09-21 | MIT | 1020 / 42 | 29.9 | 34.8% | −4.5 | 34.8% | 60.2% | 1692.1 | 19.2% | — | 86.3% | — | — | 0.435 / 0.87 |
| Ling 3.1 Flash 1019 | 2026-10-22 | MIT | 560 / 25 | 29.6 | 32.8% | −0.1 | 26.5% | 36.3% | 1655.0 | 12.6% | — | 82.3% | — | — | 0.30 / 0.90 |
| MiniMax-M3.1-Flash | 2026-10-19 | MiniMax Community License | 428 / 23 | 29.1 | 25.8% | −6.4 | 45.1% | 93.7% | 1465.3 | 20.8% | 79.1% | 79.7% | — | — | 0.15 / 0.60 |
| Qwen3.8-Flash-Next | 2026-08-26 | Qwen Community License 1.0 | 180 / 6 | 28.6 | 25.3% | −12.2 | 23.5% | 46.8% | 1636.8 | 15.6% | 78.6% | 79.7% | 45.4% | — | 0.15 / 0.47 |
| Step 5 Preview (StepFun) | 2026-09-18 | StepFun Model License 1.0 | 600 / 27 | 28.5 | 33.3% | 16.4 | 36.4% | 31.3% | 1590.7 | 14.8% | 76.4% | 88.3% | — | 47.2% | 1.00 / 2.70 |
| GLM-5.3-Flash | 2026-08-26 | MIT | 320 / 18 | 27.8 | 32.8% | 0.7 | 28.2% | 38.3% | 1648.3 | 15.4% | — | 80.0% | 47.2% | 33.2% | 0.15 / 0.50 |
| Mistral Large 4 | 2026-10-29 | Mistral Ecosystem Open-Weight License | 1050 / 52 | 26.1 | 24.7% | 5.1 | 26.0% | 28.2% | — | 17.6% | — | — | — | — | 0.70 / 2.10 |
| Muse Spark Open | 2026-10-15 | Muse Model License | 816 / 42 | 24.9 | 8.1% | 25.8 | 42.0% | 28.0% | 1401.1 | 18.6% | 80.9% | 78.3% | — | — | 1.25 / 4.25 |
| DeepSeek V4 Pro 0813 | 2026-08-13 | MIT | 1600 / 49 | 23.1 | 14.1% | −6.4 | 45.2% | 94.1% | 1455.6 | 11.4% | — | 80.3% | 39.6% | 49.6% | 1.32 / 3.96 |
| MiniMax-M3 | 2026-06-01 | MiniMax Community License | 428 / 23 | 18.9 | 2.0% | −5.5 | 44.9% | 91.4% | 1249.7 | 9.8% | 78.6% | 83.0% | 15.3% (tau2: 88.9%) | 32.1% | 0.30 / 1.20 |
| Nemotron 3 Ultra 550B A55B | 2026-06-04 | OpenMDW | 550 / 55 | 11.8 | 0.5% | 3.4 | 21.2% | 22.6% | 1020.0 | 5.0% | — | 79.3% | 14.2% (tau2: 83.3%) | 28.9% | 0.60 / 2.40 |
| gpt-oss-120b | 2025-08-05 | Apache 2.0 | — | 3.8 | 0.0% | −46.4 | 21.7% | 86.9% | 615.3 | 4.2% | — | 52.0% | 12.8% (tau2: 65.8%) | — | — |
| *Closed reference:* Claude Fable 5.2 | 2026-11-09 | closed | — | 64.6 | 59.6% | 66.8 | 79.1% | 59.3% | 1831.1 | 24.2% | — | 83.3% | — | — | — |
| *Closed:* GPT-6.2 Astra | 2026-11-17 | closed | — | 62.1 | 64.1% | 50.0 | 68.6% | 59.1% | — | 29.8% | 89.5% | — | — | — | — |
| *Closed:* Gemini 4 Neon | 2026-11-18 | closed | — | 61.4 | 63.6% | 54.8 | 60.5% | 14.4% | — | 28.0% | — | — | — | — | — |
| *Closed:* Gemini 4 Carbon | 2026-10-28 | closed | — | 60.0 | 65.2% | 53.5 | 58.3% | 11.4% | 1732.7 | 28.4% | — | 79.3% | — | — | — |
| *Closed:* Claude Opus 5.5 | 2026-09-22 | closed | — | 59.1 | 59.6% | 48.1 | 65.5% | 50.3% | 1866.3 | 26.2% | 87.7% | 84.7% | — | — | — |
| *Closed:* Claude Sonnet 5.5 | 2026-09-28 | closed | — | 54.5 | 63.6% | 30.5 | 51.5% | 43.3% | 1837.8 | 25.8% | — | 82.7% | — | — | — |

(AA's own leaderboard FAQ confirms: "Kimi K3.1 Pro is the highest-ranked open weights model with an Intelligence Index score of 46", 53 of 124 tracked models are open weights; DeepSeek V4.1 Flash 1017 Max = 33, GLM-5.3 Max = 32 — [AA leaderboard](https://artificialanalysis.ai/leaderboards/models), retrieved 2026-11-18.)

---

## 1. Which of the requested models actually exist as open weights on 2026-11-18, and under what licenses?

### Takeaway
Of the requested names, Kimi K3.1 Pro, DeepSeek V4.1 Flash (and -1017), DeepSeek V4 Pro, GLM-5.3, GLM-5.3-Flash, MiniMax M3 and M3.1-Flash, Mistral Large 4, Inkling 2 Small, Qwen3.8 (27B, Flash-Next, 2.4T-A95B) and gpt-oss all have public weights; Qwen 4 does NOT yet (API-only Qwen4-Max). Only DeepSeek (MIT), GLM-5.3-Flash (MIT), Inkling 2 Small (Apache 2.0), Qwen3.8-27B (Apache 2.0) and gpt-oss (Apache 2.0) carry standard permissive licenses; Kimi, GLM-5.3, MiniMax, Mistral Large 4 and the larger Qwen3.8 models use custom licenses that need legal review for a hosted SaaS.

### Cited Findings
- Kimi K3.1 Pro: 2.8T total / 104B active MoE, 1M context, native image input (MoonViT-V2), MXFP4 weights via QAT; license field "other / kimi-k3.1-pro" (custom "Kimi K3.1 Pro License") — [HF model card](https://huggingface.co/moonshotai/Kimi-K3.1-Pro). AA lists release 2026-10-23 and license "Kimi K3.1-Pro Licence" — [AA](https://artificialanalysis.ai/models/inkling-2-small). Some blogs claim Apache 2.0 and a Nov 4/5 weights date ([local-ai-zone](https://local-ai-zone.github.io/blog/November_2026_AI_Model_Updates.html)); this conflicts with the primary HF card, which shows a custom license.
- DeepSeek V4.1 Flash: 552B backbone, 8B active in prefill / 16B in decode, 1M context, natively multimodal (image+text), reasoning effort integer 1–100, MIT license — [HF card](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash). DeepSeek-V4.1-Flash-1017 is a "minor update" with gains on reasoning/coding/agentic/visual tasks, MIT — [HF card](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017). DeepSeek V4 Pro (1.6T total / 49B active base) MIT — [HF card](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro) and [V4.1 Flash card base-model table](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash).
- GLM-5.3: same base as GLM-5.2, post-training only; pipeline "text-generation" (text-only); license "other / glm-5.3" — [HF card](https://huggingface.co/zai-org/GLM-5.3). AA: 753B/40B, released 2026-08-18, "GLM-5.3 License" — [AA](https://artificialanalysis.ai/models/inkling-2-small).
- GLM-5.3-Flash: 320B total / 18B active, "first natively multimodal model in the GLM-5 series", hybrid sparse+linear attention, MIT license — [HF card](https://huggingface.co/zai-org/GLM-5.3-Flash).
- MiniMax-M3: ~428B / ~23B active, native text/image/video, 1M context, "minimax-community" license — [HF card](https://huggingface.co/MiniMaxAI/MiniMax-M3). MiniMax-M3.1-Flash: same size, sparse attention throughout, QAT, DSpark speculative decoding, same community license — [HF card](https://huggingface.co/MiniMaxAI/MiniMax-M3.1-Flash).
- Mistral Large 4: HF repo mistralai/Mistral-Large-4-1T-A52B, license tag "other", repo created 2026-09-30 — [HF API](https://huggingface.co/api/models/mistralai/Mistral-Large-4-1T-A52B); AA: 1050B/52B, released 2026-10-29, "Mistral Ecosystem Open-Weight License" — [AA](https://artificialanalysis.ai/models/inkling-2-small). Secondary reporting says it is a modified MIT that requires a separate commercial license for businesses operating a Model-as-a-Service offering — [technology.org, 2026-11-03](https://www.technology.org/2026/11/03/mistral-large-4-open-weights-hugging-face-modified-mit/) and [Mistral announcement](https://mistral.ai/news/mistral-large-4-oss/) (Mistral page not fetched; clause wording should be verified). This clause is directly relevant to a hosted AI workspace.
- Inkling 2 Small (Thinking Machines): Apache 2.0, HF repo created 2026-11-04 — [HF API](https://huggingface.co/api/models/thinkingmachines/Inkling-2-Small); AA: 594B total / 17B active, released 2026-11-05 — [AA](https://artificialanalysis.ai/models/inkling-2-small).
- Qwen3.8 open models on HF: Qwen3.8-27B (created 2026-08-05, Apache 2.0, image-text-to-text), Qwen3.8-Flash-Next (2026-08-24, license "other"), Qwen3.8-2.4T-A95B (2026-08-08, license "other", text-generation) — [HF API Qwen search](https://huggingface.co/api/models?author=Qwen&search=Qwen3.8). AA lists Qwen3.8-Flash-Next as 180B/6B, "Qwen Community License 1.0" — [AA](https://artificialanalysis.ai/models/inkling-2-small).
- Qwen 4: Qwen4-Max launched 2026-11-16 API-only (reported 2.4T/71B active, $1.50/$4.50 per 1M); no Qwen 4 repository on HF as of 18 Nov; smaller open Qwen4 models promised without sizes/dates/license — [felloai](https://felloai.com/qwen-4/), [cellcog](https://cellcog.ai/blog/qwen-4-release-date/) (aggregators); a Manifold market priced 78% for HF weights by Nov 25 — [Manifold](https://manifold.markets/Terminator2/will-alibaba-publish-open-weights-f). One aggregator says Qwen 4 scored 58 on the AA index with Apache 2.0 weights promised for Dec 20 — [local-ai-zone](https://local-ai-zone.github.io/blog/November_2026_AI_Model_Updates.html) (unverified).
- gpt-oss-120b: Apache 2.0, released 2025-08-05 — [AA](https://artificialanalysis.ai/models/gpt-oss-120b).
- Research specialists: Tongyi DeepResearch 30B-A3B, Apache 2.0 — [HF card](https://huggingface.co/Alibaba-NLP/Tongyi-DeepResearch-30B-A3B). MiroThinker-1.7 (235B) and 1.7-mini (30B), Apache 2.0, created 2026-03-09 — [HF API](https://huggingface.co/api/models/miromind-ai/MiroThinker-1.7), [GitHub README](https://github.com/MiroMindAI/MiroThinker); MiroThinker-H1 (88.2 BrowseComp) is proprietary — [GitHub README](https://github.com/MiroMindAI/MiroThinker).

### Inferences
- For an EU-hosted commercial SaaS, the license-clean core set is DeepSeek V4.x (MIT), GLM-5.3-Flash (MIT), Inkling 2 Small (Apache 2.0), Qwen3.8-27B (Apache 2.0), gpt-oss (Apache 2.0), MiroThinker-1.7 / Tongyi DeepResearch (Apache 2.0). Kimi K3.1 Pro, GLM-5.3, MiniMax M3/M3.1, Mistral Large 4 and Qwen3.8 Flash-Next/2.4T need their license texts reviewed (the Mistral MaaS clause in particular looks like it targets exactly this business model).
- Kimi K3.1 Pro (2.8T params) is extremely heavy to self-host; DeepSeek V4.1 Flash (16B active) and Inkling 2 Small (17B active) are far cheaper to run per token.

### Gaps
- Full license texts (Kimi K3.1 Pro, GLM-5.3, MiniMax Community, Mistral Ecosystem, Qwen Community 1.0) were not read in this session; the restrictions on hosted/MaaS use are unverified except via secondary reporting for Mistral.
- Qwen3.8-2.4T-A95B and Qwen3.8-27B are not in the AA open-model dataset extracted here (only Flash-Next is), so no independent scores for them were found.

---

## 2. Independent vs vendor results on agentic and tool-use benchmarks (tau2/tau3, Terminal-Bench, BFCL, MCP-Atlas, Toolathlon, SWE-bench/DeepSWE)

### Takeaway
On independent AA measurement Kimi K3.1 Pro is the clear open leader for agentic work (AA index 46.5; Terminal-Bench 4.0 67.2%, above Claude Opus 5.5's 59.6%), followed by a tight cluster at ~28–33 (DeepSeek V4.1 Flash 1017, GLM-5.3, Inkling 2 Small, MiMo, MiniMax M3.1-Flash, Qwen3.8-Flash-Next, GLM-5.3-Flash). Vendor Terminal-Bench numbers for several open models are much higher than AA's reproductions (e.g. Mistral Large 4: 41% vendor vs 24.7% AA; MiniMax M3.1-Flash: 38.1 vendor vs 25.8% AA), so vendor tables should be discounted. BFCL and tau2 no longer appear in current vendor cards; AA now reports tau3-Banking, where GLM-5.3 (50.3%) leads the open models measured.

### Cited Findings
Independent (AA, retrieved 2026-11-18, see Master table A for sources):
- Terminal-Bench 4.0 (AA): Kimi K3.1 Pro 67.2%; GLM-5.3 41.9%; MiMo-V2.6-Pro 34.8%; DeepSeek V4.1 Flash 1017 33.8%; Step 5 Preview 33.3%; GLM-5.3-Flash 32.8%; Ling 3.1 Flash 32.8%; MiniMax M3.1-Flash 25.8%; Qwen3.8-Flash-Next 25.3%; Mistral Large 4 24.7%; DeepSeek V4 Pro 0813 14.1%; Inkling 2 Small 13.1%; MiniMax-M3 2.0%; gpt-oss-120b 0.0%. Closed: Gemini 4 Carbon 65.2%, GPT-6.2 Astra 64.1%, Claude Opus 5.5 59.6% — [AA](https://artificialanalysis.ai/models/inkling-2-small), [AA Opus 5.5 page](https://artificialanalysis.ai/models/claude-opus-5-5).
- tau3-Banking (AA): GLM-5.3 50.3%; GLM-5.3-Flash 47.2%; Qwen3.8-Flash-Next 45.4%; Inkling 2 Small 40.4%; DeepSeek V4 Pro 0813 39.6%; MiniMax-M3 15.3%; Nemotron 3 Ultra 14.2%; gpt-oss-120b 12.8% (Kimi K3.1 Pro, DeepSeek V4.1 Flash, MiniMax M3.1 not reported) — [AA](https://artificialanalysis.ai/models/inkling-2-small), [AA gpt-oss page](https://artificialanalysis.ai/models/gpt-oss-120b).
- tau2-bench (AA, only for older entries): MiniMax-M3 88.9%; Nemotron 3 Ultra 83.3%; gpt-oss-120b 65.8% — same sources. (tau2 appears saturated; AA no longer reports it for new models.)
- EnterpriseOps-Gym (AA): DeepSeek V4 Pro 0813 49.6%; Step 5 Preview 47.2%; Inkling 2 Small 46.8%; GLM-5.3 36.4%; GLM-5.3-Flash 33.2%; MiniMax-M3 32.1% — [AA](https://artificialanalysis.ai/models/inkling-2-small).
- AutomationBench-AA (AA-measured, cited inside the Kimi card): Kimi K3.1 Pro 73.3; Claude Opus 5.5 69.5; GPT-6 Astra 68.5; DeepSeek V4.1 Flash 1017 66.6; GLM-5.3 62.2 — [Kimi K3.1 Pro card](https://huggingface.co/moonshotai/Kimi-K3.1-Pro).
- GDPval-AA v2.1 (AA Elo, real knowledge-work deliverables): Kimi K3.1 Pro 1860.6 vs Claude Opus 5.5 1866.3; DeepSeek V4.1 Flash 1017 1745.8; MiMo 1692.1; GLM-5.3 1654.8; Inkling 2 Small 1630.2; MiniMax M3.1-Flash 1465.3 — [AA](https://artificialanalysis.ai/models/inkling-2-small). (The Kimi card quotes 1846 for itself, an earlier AA snapshot — [Kimi card](https://huggingface.co/moonshotai/Kimi-K3.1-Pro).)

Vendor-reported (each from its own card; harness noted):
- Kimi K3.1 Pro (max effort, Claude Code harness): Terminal-Bench 4.0 65.7 (Opus 5.5 66.4, GPT-6 Astra 58.2); DeepSWE v1.1 75.5 (Opus 5.5 74.2); SWE Marathon v1.1 51.7; HLE-Full w/ tools 70.0; APEX-Agents 69.4 (Opus 5.5 73.5) — [HF card](https://huggingface.co/moonshotai/Kimi-K3.1-Pro).
- DeepSeek V4.1 Flash 1017: Terminal-Bench 4.0 42.3 (Claude Code harness), DeepSWE v1.1 77.0 (mini-SWE), AutomationBench v1.0.6 60.5, Agents' Last Exam 35.4 — [HF card](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017). DeepSeek V4.1 Flash (original): Terminal-Bench 2.1 90.6, TB 4.0 31.2, DeepSWE 74.2, AutomationBench 54.8, HLE w/ tools 63.9 — [HF card](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash). Same card shows harness sensitivity: DeepSWE v1.1 ranges 65.5 (OpenCode) to 74.2 (mini-SWE) for the same model.
- DeepSeek V4 Pro (April-2026 preview card, Max effort): SWE-bench Verified 80.6, SWE-bench Pro 55.4, Terminal Bench 2.0 67.9, MCPAtlas Public 73.6 (Opus-4.6 Max 73.8), Toolathlon 51.8 (GPT-5.4 xHigh 54.6), BrowseComp 83.4. V4-Flash Max: SWE Verified 79.0, MCPAtlas 69.0, Toolathlon 47.8 — [HF card](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro).
- GLM-5.3 (Z.ai): Toolathlon Verified 73.0 (Kimi K3 76.5, DeepSeek-V4 Pro-0813 74.1, Qwen3.8-Max 72.5, Opus 4.8 76.2); Terminal Bench 2.1 88.2; Terminal Bench 3.0 28.3; DeepSWE v1.1 66.9; AutomationBench v1.0.6 48.2; HLE w/ tools 62.5 — [HF card](https://huggingface.co/zai-org/GLM-5.3). GLM-5.3-Flash Toolathlon Verified 78.4 and Terminal-Bench 2.1 84.3 are reported only by aggregators citing Z.ai's launch post — [BenchLM](https://benchlm.ai/models/glm-5-3-flash), [DataCamp](https://www.datacamp.com/blog/glm-5-3-flash); the HF card's numbers are in an image not verified here.
- MiniMax M3.1-Flash: AutomationBench v1.0.6 62.8; BankerToolBench 76.2; Terminal Bench 4.0 38.1 (Codex harness); DeepSWE v1.1 73.7; Agents' Last Exam 29.6 — [HF card](https://huggingface.co/MiniMaxAI/MiniMax-M3.1-Flash).
- Qwen3.8-27B (dense, Apache 2.0): Terminal Bench 2.1 (Terminus) 73.0; SWE-bench Pro 61.7 (Claude Code harness; Opus 4.6 Max 53.4); DeepSWE 1.1 42.2 — [HF card](https://huggingface.co/Qwen/Qwen3.8-27B).
- Mistral Large 4: Terminal-Bench 4.0 41% (vendor) per secondary reporting; "no one has replicated" — [gattyworks](https://gattyworks.com/news/mistral-large-4-open-weights-license) (aggregator).
- Inkling 2 Small: vendor DeepSWE v1.1 72.1, EnterpriseOps-Gym 46.8 — [VentureBeat](https://venturebeat.com/technology/thinking-machines-launches-inkling-2-small-with-near-frontier-performance-on-enterprise-benchmarks), [MindStudio](https://www.mindstudio.ai/blog/inkling-2-small-thinking-machines) (secondary; EnterpriseOps-Gym 46.8% matches AA's independent figure).

Vendor-vs-vendor and vendor-vs-independent inconsistencies (same model, same benchmark):
- GLM-5.3 Terminal-Bench 4.0: 41.8 in Kimi's card vs 37.9 in DeepSeek's and MiniMax's cards vs 41.9% measured by AA — [Kimi card](https://huggingface.co/moonshotai/Kimi-K3.1-Pro), [DeepSeek 1017 card](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017), [AA](https://artificialanalysis.ai/models/inkling-2-small).
- DeepSeek V4.1 Flash 1017 Terminal-Bench 4.0: 42.3 (DeepSeek) vs 33.8% (AA).
- GLM-5.3 AutomationBench v1.0.6: 48.2 (Z.ai) vs 48.8 (DeepSeek and MiniMax cards).
- DeepSeek V4.1 Flash NL2Repo-Bench: 64.0 in the model card vs 65.4 in DeepSeek's changelog / the 1017 card — [V4.1 Flash card](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash), [1017 card](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017).
- Kimi K3 Terminal-Bench 4.0 shown as 12.6 by DeepSeek/MiniMax — [DeepSeek card](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017).

### Inferences
- For multi-step tool use, the only open model that independently matches closed frontier models is Kimi K3.1 Pro. The second tier (GLM-5.3, DeepSeek V4.1 Flash 1017) sits at roughly 55–70% of frontier on AA's agentic evals.
- GLM-5.3/GLM-5.3-Flash look relatively strong on customer-service-style tool calling (tau3-Banking leaders among the open models measured) and on Toolathlon; DeepSeek V4.x is strong on SWE/terminal tasks.
- Inkling 2 Small is weak at terminal/coding agents (13.1% TB4) but strong on enterprise-ops, low hallucination, and vision. That profile suits connector/MCP workflows more than coding.
- Expect 5–15 point drops from vendor numbers when you run a model in your own harness. Run your own MCP eval before committing.

### Gaps
- No current BFCL (v3/v4) scores were found for any of the Nov-2026 open models; the leaderboard (gorilla.cs.berkeley.edu) was not fetched.
- No independent MCP-Atlas, MCP-Universe or MCPMark numbers were found for Kimi K3.1 Pro, GLM-5.3, DeepSeek V4.1 Flash, MiniMax M3.x, Mistral Large 4 or Inkling 2 Small; the only MCP-Atlas figures are DeepSeek's April-2026 vendor numbers for V4.
- The official Toolathlon and tau-bench leaderboards were not fetched; the Toolathlon "Verified" numbers above come from Z.ai's card ("via the official evaluation service").
- Vals AI pages were not fetched directly. The Inkling Terminal-Bench 4.0 figure of 12.6% "per Vals AI" was relayed by OpenRouter/MindStudio (aggregators).

---

## 3. Deep research (BrowseComp, BrowseComp-Plus, GAIA, xbench-DeepSearch, DeepResearch Bench, FutureSearch): best planner/writer vs cheap page reader

### Takeaway
On vendor BrowseComp, Kimi K3.1 Pro (92.1) matches or beats the closed frontier (GPT-6 Astra 91.5, Opus 5.5 90.8 in Kimi's table). It is also the only open model with independent evidence of frontier-level long-context reasoning (AA-LCR 86.3%) and agentic knowledge work (GDPval-AA ≈ Opus 5.5). That makes it the best open research planner/writer. For cheap page reading and summarization, DeepSeek V4.1 Flash has the best published grounded-summarization faithfulness of any current open frontier model (Vectara 4.2% hallucination). It also has very low active parameters and AA-LCR 82.7%. Its closed-book hallucination rate is high, though (AA 64.1%), so it should be kept strictly grounded. No primary DeepResearch Bench scores for these open models were found.

### Cited Findings
- Kimi K3.1 Pro BrowseComp 92.1 (context compaction at 200K, 500-step max, temp 1.0) vs GPT-6 Astra 91.5 and Claude Opus 5.5 90.8 in the same vendor table; HLE-Full w/ tools 70.0 vs Opus 5.5 67.7 — [Kimi HF card](https://huggingface.co/moonshotai/Kimi-K3.1-Pro).
- DeepSeek V4 Pro (April preview) BrowseComp 83.4 (Max), 80.4 (High); V4-Flash 73.2 (Max), 53.5 (High) — [DeepSeek V4 Pro card](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro). No BrowseComp figure is given in the V4.1 Flash or 1017 cards — [V4.1 Flash card](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash).
- Kimi K3 BrowseComp is reported as 91.2 or 90.4 depending on the aggregator — [buildfastwithai](https://buildfastwithai.com/blogs/deepseek-v4-vs-kimi-k3-vs-glm-5-2-coding), [Onyx](https://onyx.app/insights/best-open-source-llms-2026) (aggregators, conflicting).
- Inkling 2 Small: BrowseComp 90.2% "self-reported in the model card" per [BenchLM](https://benchlm.ai/models/inkling-2-small) (aggregator; the primary card was not read).
- MiroThinker-1.7 (235B, Apache 2.0): BrowseComp 74.0, BrowseComp-ZH 75.3, GAIA-Val-165 82.7, HLE-Text 42.9; 256K context, max 300 tool calls; the reference config uses Serper (Google search) plus Jina scraping with a separate "summary LLM" for page extraction — [MiroThinker GitHub README](https://github.com/MiroMindAI/MiroThinker). MiroThinker v1.5-30B (Jan 2026): BrowseComp 69.8, GAIA-Val-165 80.8 — same source.
- Tongyi DeepResearch 30B-A3B (2025, Apache 2.0): claims SOTA on HLE, BrowseComp, BrowseComp-ZH, WebWalkerQA, GAIA, xbench-DeepSearch, FRAMES, with ReAct and "Heavy" (IterResearch) modes — [HF card](https://huggingface.co/Alibaba-NLP/Tongyi-DeepResearch-30B-A3B). BrowseComp-Plus 36.9% per one aggregator, as of 8 Nov 2026 — [BenchLM BrowseComp-Plus](https://benchlm.ai/benchmarks/browsecomp-plus) / [benchleader](https://www.benchleader.com/benchmarks/browsecomp_plus) (aggregator, not verified against the official leaderboard).
- DeepResearch Bench judge change (primary): on 11 May 2026 the official RACE evaluator switched from Gemini-2.5-Pro to GPT-5.5 (FACT pipeline to GPT-5.4-mini), after testing on 200 human-annotated articles (human inter-annotator agreement 68.78%; GPT-5.5 best on Overall/PAR/FAS). Dual leaderboards ran until 31 May; from 1 June only the GPT-5.5 leaderboard is maintained. On 22 Sep 2026 the article-cleaning model changed to GPT-5.6 Luna, with judges unchanged — [deep_research_bench GitHub README](https://github.com/Ayanami0730/deep_research_bench). The live leaderboard is a HF Space ([link](https://huggingface.co/spaces/muset-ai/DeepResearch-Bench-Leaderboard)), not retrievable as text here.
- LongCat-DeepResearch (Meituan, arXiv 28 Sep 2026): 55.25 on DeepResearchBench, 51.35 on DeepResearch Bench II, 79.83 on ResearchRubrics; the abstract does not state the judge version or open-weight status — [arXiv 2609.36071](https://arxiv.org/abs/2609.36071).
- Long-context reading (AA-LCR, independent): Step 5 Preview 88.3%; Kimi K3.1 Pro 86.3%; MiMo-V2.6-Pro 86.3%; Inkling 2 Small 83.3%; MiniMax-M3 83.0%; DeepSeek V4.1 Flash 1017 82.7%; GLM-5.3 79.7%; Qwen3.8-Flash-Next 79.7%; gpt-oss-120b 52.0%; Claude Opus 5.5 84.7% — [AA](https://artificialanalysis.ai/models/inkling-2-small), [AA Opus page](https://artificialanalysis.ai/models/claude-opus-5-5).
- Grounded summarization (Vectara HHEM, updated 2026-10-22): DeepSeek-V4.1-Flash 4.2% hallucination, 99.9% answer rate, 108-word average summary — [Vectara leaderboard](https://github.com/vectara/hallucination-leaderboard) (details in Q4).

### Inferences
- Research planner/writer: Kimi K3.1 Pro. It leads open models on BrowseComp (vendor), HLE w/ tools (vendor), AA index, AA-LCR, GDPval-AA, and has the lowest closed-book hallucination rate of the top-tier open models (37.3%). Confidence: medium-high on capability. Its price ($2/$10 per 1M on AA), 2.8T size and custom license are the main costs.
- Cheaper planner alternatives: GLM-5.3 (vendor HLE w/ tools 62.5, AA hallucination 38.9%, but text-only and a custom license) or DeepSeek V4.1 Flash 1017 (MIT, $0.30/$1.20). The latter's 64.1% Omniscience hallucination rate means it should not be trusted to write unsourced facts.
- Page reader/summarizer: DeepSeek V4.1 Flash. It has the best Vectara score among current open frontier models (4.2%), only 8B active parameters in prefill (input-heavy workloads), 1M context, MIT, and vision for screenshots and PDFs. Inkling 2 Small is a credible second (Apache 2.0, AA-LCR 83.3%, lowest Omniscience hallucination of the group at 26.7%), but it has no Vectara entry yet. Confidence: medium.
- Research-specialized small models (MiroThinker-1.7-mini 30B, Tongyi DeepResearch 30B-A3B) are far below Kimi K3.1 Pro on BrowseComp (74.0 vs 92.1 for the 235B MiroThinker). They are mainly useful as cheap sub-agents for search loops, not as report writers.

### Gaps
- No primary DeepResearch Bench (GPT-5.5 judge) scores were found for any open model or open-model pipeline; the leaderboard Space was not readable.
- No independent BrowseComp, BrowseComp-Plus, GAIA, xbench-DeepSearch or FutureSearch/FutureX results were found for Kimi K3.1 Pro, GLM-5.3, DeepSeek V4.1, MiniMax M3.x, Mistral Large 4 or Inkling 2 Small. All BrowseComp numbers above are vendor-reported.
- BrowseComp setups differ (context compaction, step limits, search provider), so vendor numbers are not comparable across labs.

---

## 4. Factual reliability: closed-book hallucination (AA-Omniscience) vs grounded summarization faithfulness (Vectara HHEM, FACTS Grounding)

### Takeaway
These two kinds of measurement disagree sharply. DeepSeek V4.1 Flash is the most faithful current open frontier model when summarizing a provided document (Vectara 4.2%). Yet it hallucinates in 64.1% of the closed-book cases where it does not answer correctly (AA-Omniscience). DeepSeek V4 Pro and the MiniMax M3 family have closed-book hallucination rates above 90%. Among capable open models, Inkling 2 Small (26.7%), Mistral Large 4 (28.2%), Kimi K3.1 Pro (37.3%) and GLM-5.3 (38.9%) are the least prone to confabulating. For a deep-research product, force all factual claims through retrieved sources and a verifier. Never let the model answer from memory.

### Cited Findings
AA-Omniscience v1.1 (independent; 3,000 questions across 6 domains, down from 6,000 in v1. The Omniscience Index runs from −100 to 100, "jointly penalizes hallucinations and rewards abstention", and 0 means as many correct answers as incorrect — [AA-Omniscience page](https://artificialanalysis.ai/evaluations/omniscience), paper [arXiv 2511.13029](https://arxiv.org/abs/2511.13029)). Values retrieved 2026-11-18 from [AA](https://artificialanalysis.ai/models/inkling-2-small):
- Hallucination rate (lower is better): Nemotron 3 Ultra 22.6%; Inkling 2 Small 26.7%; Muse Spark Open 28.0%; Mistral Large 4 28.2%; Step 5 Preview 31.3%; Ling 3.1 Flash 36.3%; Kimi K3.1 Pro 37.3%; GLM-5.3-Flash 38.3%; GLM-5.3 38.9%; Qwen3.8-Flash-Next 46.8%; MiMo-V2.6-Pro 60.2%; DeepSeek V4.1 Flash 1017 64.1%; gpt-oss-120b 86.9%; MiniMax-M3 91.4%; MiniMax-M3.1-Flash 93.7%; DeepSeek V4 Pro 0813 94.1%.
- Accuracy: Kimi K3.1 Pro 48.9%; DeepSeek V4 Pro 45.2%; MiniMax M3.1-Flash 45.1%; Muse Spark Open 42.0%; DeepSeek V4.1 Flash 1017 39.6%; Inkling 2 Small 33.8%; GLM-5.3 32.3%; Mistral Large 4 26.0%; gpt-oss-120b 21.7%.
- Omniscience Index (net): Kimi K3.1 Pro 29.9; Muse Spark Open 25.8; Step 5 Preview 16.4; Inkling 2 Small 16.1; GLM-5.3 6.0; Mistral Large 4 5.1; DeepSeek V4.1 Flash 1017 0.9; GLM-5.3-Flash 0.7; MiniMax M3.1-Flash −6.4; DeepSeek V4 Pro −6.4; Qwen3.8-Flash-Next −12.2; gpt-oss-120b −46.4.
- Closed reference: Claude Opus 5.5 hallucination 50.3%, accuracy 65.5%, index 48.1; Claude Fable 5.2 59.3% / 79.1% / 66.8; GPT-6.2 Astra 59.1% / 68.6% / 50.0; Gemini 4 Carbon 11.4% / 58.3% / 53.5; Gemini 4 Neon 14.4% / 60.5% / 54.8 — [AA Opus page](https://artificialanalysis.ai/models/claude-opus-5-5). The AA evaluation page says the lowest hallucination rate belongs to "Gemini 4 Carbon (Medium) … 4%" — [AA-Omniscience](https://artificialanalysis.ai/evaluations/omniscience). That is a different effort variant from the 11.4% (default) row above.

Vectara HHEM hallucination leaderboard (independent; HHEM-scored summaries of provided documents, temperature 0, prompt forbids outside knowledge; **last updated 22 Oct 2026**; this is the newer dataset, the older one is archived on the branch hhem-2.3-old-dataset) — [vectara/hallucination-leaderboard README](https://github.com/vectara/hallucination-leaderboard):
- Open models (hallucination rate / answer rate / average words): Llama-3.3-70B-Instruct 4.1% / 99.5% / 64.6; **DeepSeek-V4.1-Flash 4.2% / 99.9% / 108.2**; Gemma-3-12B 4.4%; Mistral-Large-2411 4.5%; Qwen3-8B 4.8%; Mistral-Small-2501 5.1%; Granite-4.0-H-Small 5.2%; Gemma-4-26B-A4B 5.2%; DeepSeek-V3.2-Exp 5.3%; DeepSeek-V3.1 5.5%; Qwen3-32B 5.9%; DeepSeek-V3.2 6.3%; Gemma-4-31B 7.4%; Llama-4-Maverick 8.2%; **DeepSeek-V4-Pro 8.6% / 97.2%**; MiniMax-M2.5 9.1%; Qwen3-235B-A22B 9.3%; GLM-4.7-Flash 9.3%; Nemotron-3-Nano-30B-A3B 9.6%; **GLM-5 10.1%**; Qwen3.5-Flash 10.5%; Qwen3.5-35B-A3B 10.5%; **Kimi-K2.6 10.8%**; DeepSeek-R1 11.3%; MiniMax-M2.7 12.9%; Kimi-K2.5 14.2%; **gpt-oss-120b 14.2%**; **Mistral-3-Large-2512 14.5%**; Kimi-K2-Instruct-0905 17.9%.
- Closed reference on the same board: GPT-5.4-nano 3.1%; GPT-6 Sol 6.5%; GPT-5.4 7.0%; Claude Haiku 4.5 9.8%; **Claude Opus 5.5 9.9%**; Gemini 3.1 Pro preview 10.4%; Claude Sonnet 4.6 10.6%; Gemini 4 Argon 12.1%; Claude Opus 4.7 12.0% — same source.
- Top entry overall: antgroup/finix_s1_32b 1.8% — same source.
- Not yet on Vectara (as of 22 Oct 2026): Kimi K3 / K3.1 Pro, GLM-5.1/5.2/5.3/5.3-Flash, MiniMax M3 / M3.1-Flash, Mistral Large 4, Inkling 2 Small, Qwen3.8 — same source (absence verified by grep of the README table).
- An aggregator lists "DeepSeek V4 Pro 8.6%, GLM-5 10.1%, Kimi K2.6 10.8%" from a May 2026 snapshot — [CodingFleet](https://codingfleet.com/blog/ai-model-hallucination-rates-2026/). These match the current primary values.

Vendor-internal factuality:
- Kimi Hallu Bench (Moonshot-internal, claim-level hallucination judged by fact-checking agents; lower is better): with tools, Kimi K3.1 Pro 8.3, GPT-6 Astra 5.5, Claude Opus 5.5 15.0, DeepSeek V4.1 Flash 1017 23.3, GLM-5.3 22.6; without tools, Kimi K3.1 Pro 5.4, DeepSeek 1017 13.1, GLM-5.3 14.8 — [Kimi card](https://huggingface.co/moonshotai/Kimi-K3.1-Pro).
- SimpleQA-Verified (DeepSeek-reported): V4-Pro Max 57.9, V4-Flash Max 34.1 — [DeepSeek V4 Pro card](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro). V4.1-Flash base model 42.3 (25-shot) — [V4.1 Flash card](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash).

FACTS Grounding:
- The official leaderboard is on Kaggle ([FACTS Grounding](https://www.kaggle.com/benchmarks/google/facts-grounding), [FACTS suite](https://www.kaggle.com/benchmarks/google/facts)). The page is JavaScript-rendered and its scores could not be retrieved in this session. Search snippets show Qwen 3.8 Max and Gemma 4 26B A4B listed, without scores. Aggregator numbers (e.g. BenchLM, Suprmind) include unverifiable entries and are not reported here.

### Inferences
- Grounded faithfulness and closed-book honesty are different properties and must be selected separately. DeepSeek V4.1 Flash is excellent at the first and poor at the second. Kimi K3.1 Pro and Inkling 2 Small are relatively good at the second; their grounded faithfulness is unmeasured on Vectara.
- In the open-model space, a high AA-Omniscience accuracy often comes with a very high hallucination rate (DeepSeek V4 Pro: 45.2% accuracy, 94.1% hallucination). Such models almost never abstain. Research prompts should explicitly allow "not found in sources" answers, and the pipeline should verify claims.
- The closed frontier is not much better at closed-book honesty (Opus 5.5 50.3%, GPT-6.2 Astra 59.1%), except Gemini 4 (11–14%). Users' "Claude-like" expectations come from retrieval plus citation, not from model memory.

### Gaps
- No primary FACTS Grounding scores for any Nov-2026 open model.
- No Vectara entries for Kimi K3.1 Pro, GLM-5.3(-Flash), MiniMax M3.x, Mistral Large 4, Inkling 2 Small or Qwen3.8. The Vectara row "DeepSeek-V4.1-Flash" does not say whether it is the original or the -1017 update.
- The exact AA hallucination-rate formula (understood to be the share of non-correct responses that were confidently wrong rather than abstentions) was not re-read from AA's methodology page in this session.
- Vectara HHEM is English-only per its README; Spanish-language faithfulness is unmeasured.

---

## 5. Tool-calling reliability in practice (DSML tags, parsers, reasoning_content echo, structured output, parallel calls)

### Takeaway
The main practical risks are serving-side parsers, not the models. DeepSeek V4/V4.1 have a well-documented series of vLLM bugs where DSML tool-call markup leaks into user-visible content: under streaming with `tool_choice=auto`, at long context (~95K+ tokens), and with spelling variants in V4.1. Kimi K3.1 Pro and GLM-5.3 require the full assistant turn (including reasoning) to be passed back between tool calls. DeepSeek V4.1 ships no Jinja chat template at all. Budget engineering time for a tested parser and template layer per model.

### Cited Findings
- vLLM #40800/#40801: DeepSeek V4 intermittently leaks DSML fragments in auto + streaming mode; reporters say `tool_choice=required` or `stream=false` reduces or removes it; a prefix buffer was proposed — [vLLM #40800](https://github.com/vllm-project/vllm/issues/40800), [#40801](https://github.com/vllm-project/vllm/issues/40801).
- vLLM #48931: at roughly 95K+ tokens DeepSeek-V4-Flash sometimes omits the `<｜DSML｜tool_calls>` opener, so a complete invoke block is emitted as plain text; PR #55954 parses wrapper-less invokes, but it also drops trailing text after a tool block, which changes V3.2 behavior — [#48931](https://github.com/vllm-project/vllm/issues/48931), [PR #55954](https://github.com/vllm-project/vllm/pull/55954).
- vLLM #51914: DeepSeek-V4-Flash-0731 intermittently emits a malformed DSML start wrapper on v0.27.1 + DSpark — [#51914](https://github.com/vllm-project/vllm/issues/51914).
- PR #54686: after a tool-call section closes, the parser does not re-enter tool parsing for a second invoke (relevant to sequential or parallel calls) — [PR #54686](https://github.com/vllm-project/vllm/pull/54686).
- PR #62517: the `deepseek_v41` parser did not accept the V4.1 opener spelling `<｜DSML｜ tool_calls>`; a fully V4-spelled block still comes through as text — [PR #62517](https://github.com/vllm-project/vllm/pull/62517).
- vllm-ascend PR #18457: streaming DSML markers arriving as plain text on the MTP path were demoted to content; the fix may cause prose mentions of the marker to parse as tool calls — [PR #18457](https://github.com/vllm-project/vllm-ascend/pull/18457).
- Downstream reports: Cline sees DSML markup leaking into content on its hosted path — [cline #13348](https://github.com/cline/cline/issues/13348); a non-canonical wrapper spelling from NVIDIA NIM escapes leak cleaners — [oh-my-pi #14576](https://github.com/can1357/oh-my-pi/issues/14576).
- (The merge status of each issue and PR above was not checked.)
- DeepSeek V4.1 Flash / 1017 ship no Jinja chat template. DeepSeek instead provides `encoding.py` (multi-turn, tool calling, thinking mode, numeric reasoning effort, mid-conversation system messages, interleaved images) and a Rust/Python `deepseek-recipe` library that converts Messages, Chat Completions and Responses API requests and parses streamed tool calls — [V4.1 Flash card](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash), [1017 card](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017). NVIDIA's NVFP4 build enables tool calling in vLLM with the `deepseek_v41` parser — [nvidia/DeepSeek-V4.1-Flash-1017-NVFP4](https://huggingface.co/nvidia/DeepSeek-V4.1-Flash-1017-NVFP4) (per search snippet).
- Kimi K3.1 Pro: "For multi-turn conversations and tool calls, Kimi K3.1 Pro requires the complete assistant message returned by the API to be passed back to `messages` as-is — including `reasoning_content` and `tool_calls`". `reasoning_effort` accepts low/high/max, default max. The Moonshot API documents structured output, partial mode, tool choice and dynamic tool loading — [Kimi card](https://huggingface.co/moonshotai/Kimi-K3.1-Pro).
- GLM-5.3 / GLM-5.3-Flash: `reasoning_effort` low/high/max (default max); the chat template's `clear_thinking` defaults to false and should be set to true for chat scenarios — [GLM-5.3 card](https://huggingface.co/zai-org/GLM-5.3), [GLM-5.3-Flash card](https://huggingface.co/zai-org/GLM-5.3-Flash).
- MiniMax M3: `thinking` modes enabled/adaptive/disabled — [M3 card](https://huggingface.co/MiniMaxAI/MiniMax-M3). M3.1-Flash: `reasoning_effort` low…max in the chat template; Transformers support is "in progress" — [M3.1-Flash card](https://huggingface.co/MiniMaxAI/MiniMax-M3.1-Flash).
- An arXiv validity audit of tool-calling benchmarks exists — [arXiv 2607.02577](https://arxiv.org/pdf/2607.02577) (not read).

### Inferences
- Default model settings are "max" reasoning effort (Kimi, GLM, DeepSeek benchmarks). This drives latency: AA measured 39.3 min per Intelligence-Index task and 158.7 s to first answer token for Kimi K3.1 Pro, vs 13.5 min / 41.6 s for DeepSeek V4.1 Flash 1017 — [AA leaderboard](https://artificialanalysis.ai/leaderboards/models). A per-task router should set effort explicitly.
- For DeepSeek in production: use DeepSeek's own `deepseek-recipe` parser, or a pinned vLLM version with the V4.1 parser fixes. Add a server-side DSML leak scrubber and regression tests at >100K context and in streaming mode.
- Preserving `reasoning_content` across tool turns (Kimi) raises context and cost in long research loops. Context compaction (as Kimi uses for BrowseComp) will be needed.

### Gaps
- No systematic, independent study was found comparing parallel tool-call support, JSON-schema/structured-output adherence, or tool-call error rates across these open models (BFCL-style).
- Equivalent GitHub issue sweeps were not done for the Kimi K3.1, GLM-5.3 or MiniMax M3.x parsers.

---

## 6. File and code generation (Office documents, SWE-bench, Aider, LiveCodeBench)

### Takeaway
Independent office and file evidence is thin. On AA's agentic knowledge-work evals, Kimi K3.1 Pro is near the closed frontier: GDPval-AA 1860.6 vs Opus 5.5 1866.3, and GDP.pdf all-pass 31.4% vs Opus 5.5 26.2%. DeepSeek V4.1 Flash 1017 is the cost-efficient second (GDPval-AA 1745.8). Academic office-suite benchmarks from mid-2026 show all open models (GLM-5.2, Kimi K2.6, DeepSeek V4 Pro, MiniMax M3) well below human level, at 13.8–17.9 vs a human 27.79 on OmegaUse-OfficeVal. For code, DeepSeek V4.1 Flash 1017 leads vendor DeepSWE v1.1 at 77.0. Kimi K3.1 Pro leads the independent Terminal-Bench 4.0 at 67.2%.

### Cited Findings
- AA GDPval-AA v2.1 Elo: Kimi K3.1 Pro 1860.6; DeepSeek V4.1 Flash 1017 1745.8; MiMo 1692.1; Ling 3.1 Flash 1655.0; GLM-5.3 1654.8; GLM-5.3-Flash 1648.3; Qwen3.8-Flash-Next 1636.8; Inkling 2 Small 1630.2; MiniMax M3.1-Flash 1465.3; DeepSeek V4 Pro 0813 1455.6; gpt-oss-120b 615.3. Closed: Claude Opus 5.5 1866.3, Claude Sonnet 5.5 1837.8 — [AA](https://artificialanalysis.ai/models/inkling-2-small), [AA Opus page](https://artificialanalysis.ai/models/claude-opus-5-5).
- AA GDP.pdf all-pass: Kimi K3.1 Pro 31.4%; Inkling 2 Small 25.2%; MiniMax M3.1-Flash 20.8%; MiMo 19.2%; Muse Spark Open 18.6%; Mistral Large 4 17.6%; DeepSeek V4.1 Flash 1017 17.2%; GLM-5.3 11.2%. Closed: GPT-6.2 Astra 29.8%, Opus 5.5 26.2% — same sources.
- AA-Briefcase v1.1 (AA Elo, cited in Kimi card): Kimi K3.1 Pro 1678 vs Claude Opus 5.5 1803, GPT-6 Astra 1569, DeepSeek 1017 1570, GLM-5.3 1507 — [Kimi card](https://huggingface.co/moonshotai/Kimi-K3.1-Pro).
- Vendor office numbers (Kimi card, Claude Code harness for non-Kimi models): OfficeQA Pro v2: Kimi K3.1 Pro 64.4, Opus 5.5 62.2, DeepSeek 1017 40.4, GLM-5.3 31.1. DECK-Arena (internal, presentation generation via python-pptx/pptxjs/Kimi DSL, Elo): Kimi 1456, GPT-6 Astra 1423, Opus 5.5 1253, DeepSeek 1017 1231, GLM-5.3 1119 — [Kimi card](https://huggingface.co/moonshotai/Kimi-K3.1-Pro).
- OmegaUse-OfficeVal (arXiv 2607.27155 v2, 18 Aug 2026; long-horizon office-suite tasks, fixed scaffold): human best 27.79; GLM-5.2 17.91; Qwen3.7-Plus 17.51; Kimi K2.6 17.00; DeepSeek-V4-Pro 14.48; MiniMax M3 13.82 — [arXiv HTML](https://arxiv.org/html/2607.27155). The authors report better performance on Word/Excel than on PPT and mixed-file tasks (per search snippet).
- OfficeEval ("Mind the Gap", arXiv 2606.10956): 200 NCRE tasks with 7,118 machine-gradable Word/Excel/PowerPoint criteria; open-weight Qwen3.5-397B-A17B scored roughly 2.3–11.1% pass rates across categories — [arXiv 2606.10956](https://arxiv.org/html/2606.10956v1) (search snippet only; full table not read).
- PPT-Eval (computer-use on PowerPoint): best open-weight model OpenCUA-VL-32B at 28% success — [arXiv 2606.31154](https://arxiv.org/html/2606.31154) (search snippet).
- Code, vendor: DeepSWE v1.1: DeepSeek V4.1 Flash 1017 77.0; Kimi K3.1 Pro 75.5; DeepSeek V4.1 Flash 74.2; MiniMax M3.1-Flash 73.7; Inkling 2 Small 72.1 (secondary); GLM-5.3 66.9; Qwen3.8-27B 42.2; Opus 5.5 74.2 — [DeepSeek 1017](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017), [Kimi](https://huggingface.co/moonshotai/Kimi-K3.1-Pro), [MiniMax](https://huggingface.co/MiniMaxAI/MiniMax-M3.1-Flash), [GLM-5.3](https://huggingface.co/zai-org/GLM-5.3), [Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B). SWE-bench Verified (older): DeepSeek V4-Pro Max 80.6, V4-Flash Max 79.0 — [V4 Pro card](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro). SWE-bench Pro: Qwen3.8-27B 61.7 (Claude Code, refined task set) — [Qwen3.8-27B card](https://huggingface.co/Qwen/Qwen3.8-27B).
- Code, independent: AA FrontierCode-AA 2.0: DeepSeek V4.1 Flash 1017 28.5%; Qwen3.8-Flash-Next 27.1%; Kimi K3.1 Pro 25.5%; Inkling 2 Small 25.4%; MiMo 24.0%; MiniMax-M3 21.9%; GLM-5.3 21.6%; MiniMax M3.1-Flash 20.8%; GLM-5.3-Flash 17.6%; Mistral Large 4 15.0% — [AA](https://artificialanalysis.ai/models/inkling-2-small) (field `frontierCode20`).

### Inferences
- For document generation (PDF/DOCX/XLSX/PPTX via code, e.g. python-docx/openpyxl/python-pptx in a sandbox), Kimi K3.1 Pro is the open quality leader; DeepSeek V4.1 Flash 1017 is the value pick (MIT, roughly 1/7 Kimi's output price on AA). Confidence: medium. Evidence is mostly AA GDPval/GDP.pdf plus vendor office benchmarks, not a dedicated docx/xlsx/pptx fidelity benchmark.
- Office benchmarks show all open models (and closed ones) far from reliable on long-horizon office tasks. The product should use deterministic templates and code libraries for file rendering, with the LLM producing content and structure, rather than free-form agentic file editing.

### Gaps
- No Aider Polyglot or LiveCodeBench results were found for the Nov-2026 open models (the AA dataset has a `livecodebench` field, but it was not populated or extracted for these models).
- Full per-model tables for OfficeEval and OmegaUse-OfficeVal (Word/Excel/PPT breakdowns, newer models such as GLM-5.3 or Kimi K3.x) were not obtained.

---

## 7. Vision, screenshots and computer/browser use (OSWorld, ScreenSpot-Pro, MMMU, WebVoyager, Online-Mind2Web)

### Takeaway
Among the general open models, natively multimodal options are Kimi K3.1 Pro, DeepSeek V4.1 Flash, GLM-5.3-Flash, MiniMax M3/M3.1-Flash, Inkling 2 Small and Qwen3.8-27B/Flash-Next. GLM-5.3 itself is text-only. On independent MMMU-Pro (AA), Kimi K3.1 Pro leads the open models at 83.9% (Opus 5.5 87.7%), with Inkling 2 Small at 81.6% and DeepSeek V4.1 Flash 1017 at 80.6%. Computer-use numbers are vendor-only. Kimi K3.1 Pro reports OSWorld V2.1 79.6 (Opus 5.5 81.8). The small dense Apache-2.0 Qwen3.8-27B claims OSWorld-Verified 84.3 and WebArena-Verified 64.8, which would make it the most attractive self-hostable browser-agent candidate if independently confirmed.

### Cited Findings
- MMMU-Pro (AA, independent): Kimi K3.1 Pro 83.9%; Inkling 2 Small 81.6%; Muse Spark Open 80.9%; DeepSeek V4.1 Flash 1017 80.6%; MiniMax M3.1-Flash 79.1%; Qwen3.8-Flash-Next 78.6%; MiniMax-M3 78.6%; Step 5 Preview 76.4%; GLM-5.3 not applicable (text-only). Closed: GPT-6.2 Astra 89.5%, Opus 5.5 87.7% — [AA](https://artificialanalysis.ai/models/inkling-2-small), [AA Opus page](https://artificialanalysis.ai/models/claude-opus-5-5).
- Kimi K3.1 Pro (vendor): OSWorld V2.1 79.6 (Kimi Agent harness in the official OSWorld v2 repo) vs Opus 5.5 81.8, Fable 5.1 80.7, GPT-6 Astra 75.8, DeepSeek 1017 69.3; MMMU-Pro 84.1; CharXiv (RQ) 89.0; MMMU-Pro w/ python 90.0 — [Kimi card](https://huggingface.co/moonshotai/Kimi-K3.1-Pro).
- MiniMax M3.1-Flash (vendor): OSWorld 2.0 (0808 Full release) 61.7 vs Kimi K3 58.3, DeepSeek V4.1 Flash 54.3 (MiniMax in-house reproduction), GPT-5.6 Sol 65.7, Opus 5 70.6; CharXiv RQ 82.5 — [MiniMax M3.1-Flash card](https://huggingface.co/MiniMaxAI/MiniMax-M3.1-Flash). (OSWorld 2.0 and V2.1 are different versions and not comparable.)
- DeepSeek V4.1 Flash (vendor): base-model DocVQA 95.6, MMMU-Pro (4-shot base) 56.5, RefCOCO-avg 86.0; instruct Chartography w/ tools 78.9, BabyVision w/ tools 89.6; 1017: 83.0 / 92.5 — [V4.1 Flash card](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash), [1017 card](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017).
- Qwen3.8-27B (vendor, Apache 2.0, dense, native image and video): OSWorld-Verified 84.3 (vs Qwen3.6-27B 63.9, Qwen3.7-Plus 73.3, Opus 4.6 Max 72.7); WebArena-Verified 64.8 (official grader, OSWorld scaffold); Vision2Web 62.9; MathVision 90.0 (94.6 with code interpreter); 262K native context, extensible to 1M — [Qwen3.8-27B card](https://huggingface.co/Qwen/Qwen3.8-27B).
- GUI specialists: GUI-Owl-1.5 (Qwen3-VL-based, Mobile-Agent-v3.5, Feb 2026): OSWorld 56.5; ScreenSpot-Pro 80.3 with crop refinement, 72.9 without — [arXiv 2602.16855](https://arxiv.org/pdf/2602.16855) (via search snippet). Qwen-UI-Agent (arXiv, 30 Jul 2026): OSWorld-Verified 79.5%, ScreenSpot-Pro 81.5% (with zoom-in), WebArena 73.6%, OSWorld-v2 40.0% partial-progress; the abstract gives no weight license or HF link — [arXiv 2607.28227](https://arxiv.org/abs/2607.28227). A third-party paper reports UI-Venus-1.5 at the top of ScreenSpot-Pro among native-grounding open models, and EvoCUA first among open agents on OSWorld at that time — [arXiv 2604.07831](https://arxiv.org/pdf/2604.07831). The UI-TARS public repo's headline numbers are still from UI-TARS-1.5 (Apr 2025) — [bytedance/UI-TARS](https://github.com/bytedance/ui-tars) (per search snippet).
- Inkling 2 Small: MathVision 92.8% (self-reported, via [BenchLM](https://benchlm.ai/models/inkling-2-small), aggregator).

### Inferences
- Browser agent (later phase): shortlist Qwen3.8-27B (Apache 2.0, 27B dense, cheap to host in the EU, strongest vendor OSWorld/WebArena claims) and Kimi K3.1 Pro (strongest general model with independent MMMU-Pro lead, but very heavy). Use a grounding specialist (GUI-Owl-1.5 / UI-Venus class) only if pixel-level click accuracy is a bottleneck. Confidence: low-medium, since all computer-use numbers are vendor-reported and use different OSWorld versions.
- Screenshot and PDF understanding inside research: DeepSeek V4.1 Flash (MIT, DocVQA 95.6 base) or Inkling 2 Small (Apache 2.0, MMMU-Pro 81.6%) are cost-effective readers.

### Gaps
- No independent OSWorld-Verified/OSWorld 2.x, ScreenSpot-Pro, WebVoyager or Online-Mind2Web results were found for any Nov-2026 open general model. The OSWorld site now redirects to an archived v1 page (osworld-v1.xlang.ai), and the v2 leaderboard was not located.
- No 2026 results were found for Holo (H Company), GLM-V (GLM-5V-class) or UI-TARS-2 open checkpoints. Whether Qwen-UI-Agent has open weights is unconfirmed.

---

## 8. Small claim-checking / NLI verifier models (MiniCheck, FactCG, HHEM-2.1-Open, Granite Guardian, Bespoke-MiniCheck): licenses and LLM-AggreFact scores

### Takeaway
On the LLM-AggreFact leaderboard (average balanced accuracy, zero-shot), Bespoke-MiniCheck-7B scores 77.4, but it is CC BY-NC 4.0 (non-commercial; a commercial license from Bespoke is needed). The best commercially usable small verifiers are Granite Guardian 3.3 8B (76.5, Apache 2.0), FactCG-DeBERTa-v3-Large (0.4B, 75.6, MIT) and MiniCheck-Flan-T5-Large (0.8B, 75.0, MIT). HHEM-2.1-Open (Apache 2.0) is not shown on the default LLM-AggreFact view. The newest leaders (nimble-v4-max 79.5, Clef 79.0) are 27B models whose licenses were not checked.

### Cited Findings
- LLM-AggreFact leaderboard (default view shows 19 of 47 models; average score; retrieved 2026-11-18): nimble-v4-max (27B) 79.5; Clef (27B) 79.0; Decider v1.2 (27B) 78.7; Jev 1.13.0 78.7; d1-ultra 78.5; nimble-v4 (9B) 77.8; **Bespoke-MiniCheck-7B 77.4**; Claude-3.5 Sonnet 77.2; Clef Flash (9B) 76.6; Drex v1.5 (9B) 76.5; **Granite Guardian 3.3 (8B) 76.5**; Mistral-Large 2 (123B) 76.5; gpt-4o-2024-05-13 75.9; **FactCG-DeBERTa-L (0.4B) 75.6**; Qwen2.5-72B-Instruct 75.6; **MiniCheck-Flan-T5-L (0.8B) 75.0**; Llama-3.3-70B 74.5; Llama-3.1-405B 74.4; QwQ-32B-Preview 71.8 — [LLM-AggreFact](https://llm-aggrefact.github.io/). The page shows no last-updated date in the fetched text. Bespoke's docs describe the metric as average balanced accuracy — [Bespoke MiniCheck docs](https://docs.bespokelabs.ai/minicheck/overview).
- Licenses (primary HF): Bespoke-MiniCheck-7B "licensed under CC BY-NC 4.0 … For commercial licensing, please contact company@bespokelabs.ai" — [HF card](https://huggingface.co/bespokelabs/Bespoke-MiniCheck-7B); MiniCheck-Flan-T5-Large MIT — [HF](https://huggingface.co/lytang/MiniCheck-Flan-T5-Large); FactCG-DeBERTa-v3-Large MIT — [HF](https://huggingface.co/yaxili96/FactCG-DeBERTa-v3-Large); HHEM (vectara/hallucination_evaluation_model) Apache 2.0, last modified 2026-10-06 — [HF](https://huggingface.co/vectara/hallucination_evaluation_model); Granite Guardian 3.3 8B Apache 2.0 — [HF](https://huggingface.co/ibm-granite/granite-guardian-3.3-8b).
- Caveat: a Snowflake study reports Bespoke-MiniCheck-7B F1 0.7771 on an LLM-AggreFact holdout (a different metric) — [Snowflake blog](https://www.snowflake.com/en/engineering-blog/benchmarking-LLM-as-a-judge-RAG-triad-metrics/); "Verify with Caution" warns about imperfect factuality metrics — [arXiv 2501.14883](https://arxiv.org/pdf/2501.14883).

### Inferences
- For a commercial EU product, the citation verifier could be Granite Guardian 3.3 8B (best permissive score, 76.5) as the main checker, with FactCG-DeBERTa-L (0.4B) or MiniCheck-Flan-T5-L (0.8B) as a very cheap first pass on every claim. Bespoke-MiniCheck-7B would need a paid license. HHEM-2.1-Open is the same model family Vectara uses for its leaderboard, which makes it convenient for regression-testing summarizer faithfulness. Confidence: medium. Scores differ by only ~2 points, and all of these models are trained and evaluated mostly on English.

### Gaps
- No HHEM-2.1-Open score on LLM-AggreFact was found in the default view.
- Licenses for nimble-v4/Clef/Decider/Drex were not checked.
- No multilingual (Spanish) verifier benchmark was found.

---

## 9. Recommended open-weight model per agentic job (with justification and confidence)

### Takeaway
A router built on four or five open models covers the product: Kimi K3.1 Pro for research planning and report writing (and hard agentic tasks), DeepSeek V4.1 Flash 1017 for page reading, summarization, cheap tool loops and code/files, GLM-5.3-Flash or Inkling 2 Small as permissive mid-cost tool/MCP workers, Qwen3.8-27B as the browser/GUI candidate, and a small NLI verifier (Granite Guardian 3.3 / FactCG) for citation checking. The biggest risks are the custom licenses (Kimi, GLM-5.3, MiniMax, Mistral), DeepSeek parser bugs, and the lack of independent deep-research and computer-use evaluations.

### Cited Findings
(Justifications reuse numbers already cited above; sources repeated for traceability.)
- (a) Deep-research planner and report writer: **Kimi K3.1 Pro**. It has the highest open AA index (46.5), TB4 67.2%, GDPval-AA 1860.6 (≈ Opus 5.5 1866.3), AA-LCR 86.3%, and the best open Omniscience Index (29.9) with a 37.3% hallucination rate. Vendor figures: BrowseComp 92.1 and HLE w/ tools 70.0 — [AA](https://artificialanalysis.ai/models/inkling-2-small), [Kimi card](https://huggingface.co/moonshotai/Kimi-K3.1-Pro). Confidence: medium-high on quality, with a license caveat (custom). Fallback with an MIT license: DeepSeek V4.1 Flash 1017 (AA 32.6, GDPval 1745.8), used strictly grounded. A text-only, lower-hallucination fallback: GLM-5.3 (Omni hallucination 38.9%, vendor HLE w/ tools 62.5), with a custom license — [GLM card](https://huggingface.co/zai-org/GLM-5.3).
- (b) Reading and summarizing web pages: **DeepSeek V4.1 Flash (1017)**. Vectara hallucination 4.2% (best current open frontier model), 99.9% answer rate, 8B/16B active, 1M context, vision, MIT, $0.30/$1.20 — [Vectara](https://github.com/vectara/hallucination-leaderboard), [DeepSeek card](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash), [AA](https://artificialanalysis.ai/models/inkling-2-small). Confidence: medium. Caveats: the Vectara row may be the pre-1017 version, and closed-book hallucination is 64.1%, so prompts must forbid outside knowledge. Alternate: Inkling 2 Small (Apache 2.0, AA-LCR 83.3%, Omni hallucination 26.7%, no Vectara entry).
- (c) Tool calling / MCP / connectors: **GLM-5.3-Flash** (MIT, 18B active, AA tau3-Banking 47.2%, TB4 32.8%, $0.15/$0.50) or **Inkling 2 Small** (Apache 2.0, EnterpriseOps-Gym 46.8%, tau3-Banking 40.4%). Escalate hard multi-tool tasks to Kimi K3.1 Pro (AutomationBench-AA 73.3 vs Opus 5.5 69.5) — [AA](https://artificialanalysis.ai/models/inkling-2-small), [Kimi card](https://huggingface.co/moonshotai/Kimi-K3.1-Pro). GLM-5.3 (full) has the best open tau3-Banking at 50.3% and vendor Toolathlon Verified 73.0 — [GLM card](https://huggingface.co/zai-org/GLM-5.3). Confidence: low-medium. There is no independent BFCL/MCP-Atlas data for these models.
- (d) File and code generation (PDF/Excel/Word/PowerPoint via code): **DeepSeek V4.1 Flash 1017** as default (vendor DeepSWE 77.0, AA FrontierCode 28.5%, GDPval 1745.8, MIT, cheap); **Kimi K3.1 Pro** for high-stakes decks and reports (AA GDP.pdf 31.4%, vendor OfficeQA Pro v2 64.4 and DECK-Arena lead) — [DeepSeek 1017](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017), [AA](https://artificialanalysis.ai/models/inkling-2-small), [Kimi card](https://huggingface.co/moonshotai/Kimi-K3.1-Pro). Confidence: medium.
- (e) Vision, screenshots and browser control: **Qwen3.8-27B** (Apache 2.0, vendor OSWorld-Verified 84.3, WebArena-Verified 64.8) as the self-hostable browser-agent candidate; **Kimi K3.1 Pro** as the strongest general multimodal model (AA MMMU-Pro 83.9%, vendor OSWorld V2.1 79.6) — [Qwen3.8-27B card](https://huggingface.co/Qwen/Qwen3.8-27B), [AA](https://artificialanalysis.ai/models/inkling-2-small), [Kimi card](https://huggingface.co/moonshotai/Kimi-K3.1-Pro). For screenshot and PDF reading inside research: DeepSeek V4.1 Flash or Inkling 2 Small (MMMU-Pro 80.6% / 81.6%). Confidence: low-medium (vendor-only computer-use evidence).
- Claim verification: **Granite Guardian 3.3 8B** (76.5, Apache 2.0) plus **FactCG-DeBERTa-L** (75.6, MIT, 0.4B) — [LLM-AggreFact](https://llm-aggrefact.github.io/), [HF](https://huggingface.co/ibm-granite/granite-guardian-3.3-8b). Confidence: medium.
- Models not recommended for core jobs: gpt-oss-120b (AA index 3.8, TB4 0%, Omni hallucination 86.9%, Vectara 14.2%) — [AA](https://artificialanalysis.ai/models/gpt-oss-120b), [Vectara](https://github.com/vectara/hallucination-leaderboard). MiniMax M3/M3.1-Flash and DeepSeek V4 Pro 0813 for any unsupervised factual writing (Omni hallucination 91–94%). Mistral Large 4: middling agentic scores (AA 26.1, TB4 24.7% vs a 41% vendor claim), plus the reported MaaS license restriction — [AA](https://artificialanalysis.ai/models/inkling-2-small), [technology.org](https://www.technology.org/2026/11/03/mistral-large-4-open-weights-hugging-face-modified-mit/).
- Quality bar: the best open model (Kimi K3.1 Pro, AA 46.5) trails the closed frontier by 13–18 index points (Claude Fable 5.2 64.6, GPT-6.2 Astra 62.1, Gemini 4 Neon 61.4, Claude Opus 5.5 59.1). On specific agentic tasks (TB4, GDPval-AA, BrowseComp) it is at parity — [AA](https://artificialanalysis.ai/models/claude-opus-5-5).

### Inferences
- A Mistral-free stack is likely for an EU founder, despite Mistral being European, because of AA quality and the MaaS license clause. A "European model" marketing angle would come at a quality cost. This is an inference; the Mistral license text should be read first.
- If the Kimi license turns out to be incompatible with hosted resale, the planner/writer slot falls to DeepSeek V4.1 Flash 1017 (MIT) with heavier verification. That is a large quality step down (AA 32.6 vs 46.5).
- Qwen 4 open weights (promised, not released as of 2026-11-18) could change the picture within weeks; re-check in December.

### Gaps
- The ranking rests on AA's index plus vendor cards. No head-to-head independent evaluation of open models inside a full deep-research pipeline (planner + reader + writer + verifier) was found.
- No Spanish-language evaluation for any of these jobs was found, which matters for a Spain-based product.
- EU hosting availability per model (which EU providers serve Kimi K3.1 Pro, GLM-5.3, DeepSeek V4.1 etc.) is outside this note's scope and was not researched here.
