# Measured token usage per task type: a cost baseline for an open-weight, EU-hosted AI workspace (as of 2026-11-18)

Reference usage: about 100 chat turns per day and about 2 deep-research runs per day. Each number is labeled one of three ways:
- **MEASURED**: from logged traffic or an instrumented run.
- **VENDOR-MEASURED**: measured by a party selling the product being measured.
- **ESTIMATE/INFERENCE**: my own derivation, or a blog guess.

Tokenizers differ between sources (LMSYS and WildChat use the Llama-2 tokenizer; PolicyLayer uses o200k), so treat cross-source comparisons as approximate (±10–20%).

## Typical chat: measured input/output tokens per turn and per conversation

### Takeaway
Measured consumer chat is short. Conversations average 2.0–2.5 turns. User messages average 70–300 tokens and visible responses 215–440 tokens. Per-request API prompts are much larger (average >6K tokens by late 2025), because they carry the system prompt, the tools and the history. In a Claude-like workspace, the *input* per turn is set by fixed overhead (system prompt + tool schemas + memory) plus history, not by what the user types.

### Cited Findings
- **MEASURED (LMSYS-Chat-1M, 1M conversations, collected Apr–Aug 2023):** average 2.0 turns per conversation, user prompts averaging 69.5 tokens, model responses averaging 214.5 tokens. The ICLR version table gives 2.02 turns / 69.83 / 215.71. — [LMSYS-Chat-1M paper, arXiv 2309.11998](https://arxiv.org/html/2309.11998v4)
- **MEASURED (WildChat, 1M ChatGPT conversations, 2023–2024):** 2.52 turns per conversation on average (2.54 in a later table). About 41% of conversations are multi-turn and 3.7% exceed 10 turns. User tokens average 295.58 ± 1609.18 and chatbot response tokens 441.34 ± 410.91, so prompt length is heavily right-skewed by pasted documents and code. — [WildChat paper, arXiv 2405.01470](https://arxiv.org/pdf/2405.01470)
- **MEASURED (compiled table):** WildChat has about 4x the prompt length and about 2x the response length of LMSYS-Chat-1M (2.5 / 295.6 / 441.3 vs 2.0 / 69.5 / 214.5). — [Network and Systems Performance Characterization of MCP-Enabled LLM Agents, arXiv 2511.07426](https://arxiv.org/pdf/2511.07426)
- **MEASURED (OpenRouter, 100-trillion-token study, Dec 2025 / arXiv Jan 2026):**
  - Average prompt tokens per request grew "roughly fourfold from around 1.5K to over 6K" since early 2024.
  - Average completion tokens per request "nearly tripled from about 150 to 400".
  - Average total sequence length was under 2,000 in late 2023 and over 5,400 by late 2025.
  - Programming requests "routinely exceed 20K input tokens" and average 3–4x the length of general prompts.

  [State of AI: An Empirical 100 Trillion Token Study with OpenRouter, arXiv 2601.10088](https://arxiv.org/html/2601.10088v1); primary report at [openrouter.ai/state-of-ai](https://openrouter.ai/state-of-ai)
- **MEASURED (OpenRouter):** the share of all tokens routed through reasoning-optimized models went from a "negligible slice" in Q1 2025 to "exceeds fifty percent" by late 2025. — [arXiv 2601.10088](https://arxiv.org/html/2601.10088v1)

### Inferences
- Visible output per chat turn of about 215–440 tokens is a well-measured range (2023–24 consumer chat). OpenRouter's average of about 400 completion tokens (late 2025, including some reasoning output) agrees with it. A central value for visible answers is **about 450 tokens**.
- User-typed input of about 70–300 tokens per turn is negligible next to the fixed prefix. The cost driver is **system prompt + tool schemas + memory + conversation history**.
- With about 2.5 turns per conversation, the average turn carries only about 0.75 prior exchanges of history, about 560 tokens at 300 in + 450 out per exchange (inference). A founder who is a power user (long project threads, pasted files) will run longer. WildChat's 3.7% of conversations above 10 turns and the ±1609 standard deviation on prompts show the tail.

### Gaps
- I found no 2026 public dataset of consumer-chat turn lengths. LMSYS and WildChat are from 2023–24, when system prompts were short and tools were rare. OpenRouter's figures are API traffic, not consumer chat.
- I did not research Microsoft Copilot usage reports for turn-length data.
- The OpenAI NBER study gives no tokens per message.

## Task mix: share of writing, information seeking, analysis, coding, and file creation

### Takeaway
In consumer chat, about 80% of conversations are practical guidance, information seeking or writing, and programming is only about 4% of ChatGPT messages. On Claude, coding-type tasks are about 35% of Claude.ai conversations, and coding dominates API token volume (>50% of OpenRouter tokens). For a general-purpose workspace, most *turns* can go to a cheap, fast, non-thinking model. Most *tokens*, though, come from the coding, agentic and long-context minority.

### Cited Findings
- **MEASURED (OpenAI/NBER w34255, Sept 2025; data from Nov 2022 to Jul 2025):**
  - "Practical Guidance," "Seeking Information," and "Writing" "collectively account for nearly 80% of all conversations".
  - Non-work messages grew from 53% to more than 70% of usage.
  - "Writing" dominates work tasks.

  [NBER w34255](https://www.nber.org/papers/w34255)
- **MEASURED, via secondary coverage:** "Computer Programming" is 4.2% of all messages. Writing is 40% of work-related messages (June 2025). Intent splits about 49% "Asking" and 40% "Doing". — [Gizmodo coverage](https://gizmodo.com/openai-how-people-use-chatgpt-2000658906); [OpenAI summary](https://openai.com/index/how-people-are-using-chatgpt/)
- **Secondary, not verified against the PDF:** Practical Guidance 29%, Seeking Information 24%, Writing 24%. — [Search Atlas](https://searchatlas.com/news/how-people-actually-use-chatgpt/)
- **MEASURED (Anthropic Economic Index, March 2026 report, Feb 2026 data):**
  - Tasks tied to Computer & Mathematical occupations (the coding proxy) are 35% of Claude.ai conversations.
  - Coding is migrating to the API and Claude Code, where top-10-task concentration rose from 28% to 33%.
  - The January 2026 report (Nov 2025 data) found Claude.ai conversations 52% augmentative and 45% automated.

  [Anthropic Economic Index, March 2026](https://anthropic.com/research/economic-index-march-2026-report); [January 2026 report](https://www.anthropic.com/research/anthropic-economic-index-january-2026-report)
- **MEASURED (OpenRouter, token-weighted):**
  - Programming went from about 11% of tokens in early 2025 to over 50% in late 2025.
  - On open-weight models, roleplay is over 50% of tokens and programming about 15–20%.
  - Open-weight models reached about one-third of usage by late 2025.

  [arXiv 2601.10088](https://arxiv.org/html/2601.10088v1)

### Inferences
- A founder-style workspace mixes ChatGPT-like use (writing and info-seeking) with Claude-like use (coding and analysis). A defensible routing split is (ESTIMATE): **about 60–70% of turns to a cheap non-thinking model** (emails, rewrites, quick Q&A, summaries), **about 20–30% to a mid or thinking model** (analysis, multi-step reasoning, file generation), and **about 10% to a strong coding/agentic model**.
  - The 4.2% programming share in ChatGPT is a lower bound. The 35% coding share on Claude.ai is an upper bound for a technical founder.
- Token-weighted, coding and agentic turns can be 3–4x the average prompt size (OpenRouter), so a 10% share of turns can carry 30–50% of input tokens (inference).

### Gaps
- No study gives a measured share for "file creation" (PDF/Excel/Word/PPT) as a task type.
- I did not retrieve Microsoft Copilot task-mix data.
- The exact NBER per-topic percentages were not verified against the PDF.

## Reasoning/thinking token overhead (open models, thinking vs non-thinking)

### Takeaway
Measured thinking overhead on current open models is highly skewed. On DeepSeek V4.1 Flash at max effort in agentic-coding turns, the **median was only 36–54 reasoning tokens per turn, but the mean was 403–1,033**, because a few turns think for more than 5K tokens. Independent work finds open-weight reasoning models use 1.5–4x more completion tokens than closed models, and up to 10x on simple knowledge questions. Routing simple questions to non-thinking mode therefore matters.

### Cited Findings
- **VENDOR-MEASURED (Keln gateway benchmark, 20–21 Oct 2026):** DeepSeek V4.1 Flash, reasoning effort max on every turn, 3,360 agentic Claude-Code-replay turns per gateway. Reasoning tokens per turn:

  | Gateway | Mean | Median | Turns over 5,000 tokens |
  |---|---|---|---|
  | Keln | 856 | 40 | 152 |
  | OpenRouter | 1,033 | 42 | 212 |
  | Vercel | 403 | 54 | 36 |
  | Ramp | 420 | 36 | 43 |

  The same model gave different reasoning volumes on different gateways, so the provider matters. — [Keln blog](https://keln.ai/blog/ai-gateway-benchmark-deepseek-v4-1-flash)
- **VENDOR-MEASURED (Keln inference benchmark, 3–4 Nov 2026, DeepSeek V4.1 Flash and GLM-5.3 Flash):** providers returned "broadly similar amounts of reasoning tokens". Exact values appear only in an image. — [dev.to / Keln](https://dev.to/kris_holy/ai-inference-benchmark-keln-vs-fireworks-together-ai-baseten-modal-deepinfra-zai-4n5b)
- **MEASURED (Nous Research, Aug 2025, 19 models):**
  - Open-weight models use about 1.5–4x more completion tokens than closed models, and up to 10x on simple knowledge questions that are answerable in one sentence.
  - gpt-oss-120b and llama-3.3-nemotron-super-49b were the most token-efficient open models.

  [Nous Research](https://nousresearch.com/measuring-thinking-efficiency-in-reasoning-models-the-missing-benchmark); [VentureBeat](https://venturebeat.com/ai/that-cheap-open-source-ai-model-is-actually-burning-through-your-compute-budget/)
- **MEASURED (UCSD, DeepResearch Bench subset, Oct 2025):** GPT-5 used 1,818–2,241 reasoning tokens per deep-research task and o3-deep-research 3,450–4,135. — [Qi, Abhyankar, Zhang, NeurIPS 2025 Efficient Reasoning workshop](https://escholarship.org/uc/item/36h5r7z4)
- **Artificial Analysis:** reports "output tokens per Intelligence Index task" and splits reasoning and answer token prices in cost to run. On the pages I fetched, though, the token figures for open models (for example Kimi K2.5 reasoning vs non-reasoning) rendered as "N/A" or no data. Time to first answer token for Kimi K2.5 was 39.41 s with reasoning vs 3.02 s without, which indirectly shows a large thinking overhead. AA's blended price assumes a **7:2:1 cache-hit : input : output** token ratio, which is an assumption, not a measurement. — [Artificial Analysis Kimi K2.5 comparison](https://artificialanalysis.ai/models/comparisons/kimi-k2-5-non-reasoning-vs-kimi-k2-5)

### Inferences
- For chat turns routed to thinking mode, a reasonable expected overhead is **about 500–1,000 reasoning tokens per turn (mean)**, with a high case of 2,000–5,000 on hard turns. For non-thinking turns it is about 0.
- If about 30% of turns use thinking, the **blended reasoning overhead is about 150–300 tokens per average turn** (expected), with a high of about 1,000 if thinking is always on, given the Nous 1.5–10x verbosity of open models (inference).

### Gaps
- I could not extract Artificial Analysis per-model token totals (the pages are JS-rendered). Re-check AA's "Output Tokens Used to Run Intelligence Index" chart for the specific open models chosen (DeepSeek V4.x, GLM-5.x, Qwen, Kimi).
- I found no measured reasoning tokens for *plain chat* turns on open models. The Keln data is agentic-coding turns with about 40K prompts.

## Deep research: tokens and tool calls per run, split by role

### Takeaway
An instrumented open-source deep-research agent (LangChain open_deep_research on GPT-4.1) **ingests about 0.1–2.5M tokens of web page content per run** but **outputs only about 4–6K tokens** (about 2–3.5K intermediate, about 2.1–2.3K for the final report). Measured cost was $0.26–$0.57 per run at OpenAI prices. Input-side reader tokens dominate the cost. These are mostly fresh web content and therefore largely uncacheable.

### Cited Findings
- **MEASURED (UCSD instrumented study, 10 DeepResearch Bench tasks, 3 trials each; Oct 2025):**

  | System | Task set | Intermediate ("reasoning") output | Final-answer output | Cost | Latency |
  |---|---|---|---|---|---|
  | LangChain-DR (GPT-4.1 base) | long | 3,527 ± 2,692 | 2,147 ± 783 | $0.57 ± 0.60 | 18.57 ± 7.72 min |
  | LangChain-DR (GPT-4.1 base) | short | 1,966 ± 1,061 | 2,327 ± 414 | $0.26 ± 0.17 | 4.62 ± 0.83 min |
  | o3-deep-research | long | 4,135 reasoning | 15,249 output | $1.27 | 10.52 min |
  | GPT-5 | long | 2,241 reasoning | 9,127 output | $0.28 | 5.52 min |

  - For LangChain-DR, **web page content tokens per task ranged from 500K to over 2.5M on long tasks and 100K to 1.25M on short tasks**.
  - Web search took 73% of wall-clock time on GPT-5 and 50% on LangChain-DR.
  - "Final answer generation consumes the majority of completion tokens."

  [escholarship.org/uc/item/36h5r7z4](https://escholarship.org/uc/item/36h5r7z4)
- **MEASURED (open_deep_research README):** the GPT-5 configuration's evaluation row on Deep Research Bench (100 PhD-level tasks) totals **204,640,896 tokens**, RACE 0.4943. If that is the full 100-task run, it is about 2.05M tokens per task (INFERENCE; the table does not state the scope explicitly). — [langchain-ai/open_deep_research](https://github.com/langchain-ai/open_deep_research)
- **MEASURED (Anthropic multi-agent research system, June 2025):**
  - Agents use about 4x more tokens than chat, and multi-agent systems about 15x more.
  - Token usage alone explains 80% of BrowseComp performance variance; tokens, tool calls and model choice together explain 95%.
  - Effort-scaling rules: simple fact-finding uses "1 agent with 3-10 tool calls"; direct comparisons use "2-4 subagents with 10-15 calls each"; complex research uses "more than 10 subagents". The lead spawns 3–5 subagents in parallel, and each subagent uses 3+ tools in parallel.
  - No lead-vs-subagent token split is given.

  [Anthropic Engineering](https://www.anthropic.com/engineering/multi-agent-research-system)
- **MEASURED (FutureSearch Deep Research Bench cost/accuracy, Feb–Mar 2026):** cost per task was Gemini 3 Flash (low) $0.05, Claude 4.6 Opus (low) $0.24 at about 130 s, and Claude 4.6 Opus (high) $0.55 at about 6 min. Most agents "cluster well under a dollar". No token counts are given. — [FutureSearch](https://futuresearch.ai/cost-of-deep-research)
- **ESTIMATE (blogs, not measured):** 150K–400K tokens per thorough research question; a full 100-task ODR benchmark run costs $20–$100. — [digitalapplied guide, Aug 2026](https://www.digitalapplied.com/blog/open-source-deep-research-agents-2026-guide); [rentierdigital](https://rentierdigital.xyz/blog/langgraph-deep-research)

### Inferences
Role split, built from the measured totals above (ESTIMATE):

| Role | Input tokens | Output tokens |
|---|---|---|
| Planner/supervisor | 20–60K cumulative (repeated small calls over a growing plan) | about 1–2K |
| Readers/researchers (search + fetch + summarize pages) | 100K / 600K / 2.5M (low / expected / high) | about 2–3.5K |
| Writer | 15–50K (compressed notes) | about 2–3K (LangChain); up to 9–15K for long OpenAI-style reports |

- Readers carry about 90% of input tokens. The measured web-content ranges set the input; the output figure is measured LangChain intermediate output.
- Searches and page fetches per run (ESTIMATE, anchored on Anthropic's effort rules): low 5–10 calls, expected 20–40, high 60–150 for complex runs with more than 10 subagents.
- Cacheability: page content is unique per run. Only the agent system prompt and tool prefix (a few thousand tokens per call) and the growing supervisor context cache, so the cached share for deep research is likely **only about 10–30%** of input (inference).

### Gaps
- I found no public measured per-role token split (planner vs readers vs writer) for any system.
- I found no measured count of searches and fetches per run for LangChain ODR, Gemini or OpenAI deep research. DRACO and BrowseComp-Plus cost reports were not retrieved within the tool budget.

## File generation (PDF/Excel/Word/PPT) and code-interpreter tasks

### Takeaway
I found no public measured token counts per file-generation or code-interpreter task. The closest measured proxy is agentic tool loops. In those loops, cost is driven by the number of steps times the re-sent context, and caching dominates.

### Cited Findings
- **MEASURED (agentic coding proxy):** one mini-swe-agent run of a DeepSWE task made **155 API calls, with 19.5M prompt tokens total (about 126K per call on average) and about 60K output tokens**. With good caching it cost $0.13–$0.40 on the best DeepSeek V4 Flash providers; poorly caching providers cost up to $2.30. — [olafdsouza.com, Sept 2026](https://olafdsouza.com/blog/your-inference-provider-sucks-at-caching)
- **VENDOR-MEASURED:** the median agentic turn in a replayed Claude Code corpus was about 40.7K prompt tokens (DeepSeek) and 38.6K (GLM-5.3 Flash). — [Keln blog](https://keln.ai/blog/ai-gateway-benchmark-deepseek-v4-1-flash); [dev.to / Keln](https://dev.to/kris_holy/ai-inference-benchmark-keln-vs-fireworks-together-ai-baseten-modal-deepinfra-zai-4n5b)

### Inferences
- A file-generation task in a sandbox (write a python-docx/openpyxl/pptx script, run it, fix errors, return the file) is typically 3–10 tool steps. At 8–20K context per step (system + tools + skill instructions + growing history), that is **about 50–150K input tokens (70–90% cacheable within the loop) and 3–10K output tokens per file** (ESTIMATE; no measured source).
- Treat this as a separate line item, sized somewhere between a chat turn and a deep-research run.

### Gaps
- There is no published measurement for document, spreadsheet or slide generation token usage in ChatGPT, Claude or open-source agents.

## Prompt-cache hit rates in real workloads, including idle pauses

### Takeaway
On agentic, steady-pacing workloads, good open-model providers cache **94–99% of prompt tokens** (theoretical ceiling about 98.8%). Hit rates fall sharply after idle pauses, because most providers evict within 1–15 minutes. Mixed real-world traffic shows much lower gateway-level hit rates (36–77%). Chat with human think-time sits between those two cases.

### Cited Findings
- **VENDOR-MEASURED (Keln gateway benchmark, 20–21 Oct 2026, DeepSeek V4.1 Flash, 3,360 turns per gateway, median prompt 40.7K, 5% of turns paused 1–20 min):** overall hit rate was Keln 93.9%, OpenRouter 88.5%, Vercel 86.7%, Ramp 62.6%. Hit rate by pause before the turn:

  | Pause before turn | Keln | OpenRouter | Vercel | Ramp |
  |---|---|---|---|---|
  | Under 10 s | 94% | 87% | 85% | 58% |
  | 1–5 min | 93% | 83% | 78% | 50% |
  | 5–10 min | 80% | 89% | 64% | 44% |
  | Over 10 min | 75% | 52% | 25% | 23% |

  [Keln blog](https://keln.ai/blog/ai-gateway-benchmark-deepseek-v4-1-flash); also [dev.to](https://dev.to/kris_holy/ai-gateway-benchmark-openrouter-vercel-ramp-keln-comparing-cache-hit-rate-speed-reasoning-3afi)
- **VENDOR-MEASURED (Keln inference benchmark, 3–4 Nov 2026):**
  - DeepSeek V4.1 Flash: Keln 94.3%, best direct provider about 95%.
  - GLM-5.3 Flash: Keln 90.5%.
  - After a 15–20 min break on GLM-5.3 Flash, the share still cached was Keln 63.0%, DeepInfra 38.4%, Z.ai 16.5%, and Baseten, Modal and Fireworks 0%.
  - Cost on DeepSeek was $2.09 per 1,000 turns at Keln list prices of $0.30 input, $0.01 cached and $1.20 output per million tokens.

  [dev.to / Keln](https://dev.to/kris_holy/ai-inference-benchmark-keln-vs-fireworks-together-ai-baseten-modal-deepinfra-zai-4n5b)
- **MEASURED (independent, 18 DeepSeek V4 Flash providers, Aug–Sept 2026, byte-identical replay of a 155-call agent session, median pause 6 s):**
  - Ceiling 98.8%. Hit rates were DeepSeek 98.8%, Fireworks 97.9%, DeepInfra 97.2%, GMICloud 94.5%, Cloudflare 86.7%, Parasail 60.6%, OpenInference 7.7%.
  - Cost per task spread 17.7x ($0.13–$2.30).
  - TTL tests (30K prefix): most providers evicted within 1–15 min. DeepSeek was still warm after 45 min; Fireworks and Sail lasted 15–45 min; DeepInfra and Cloudflare 5–15 min; several only 1–5 min.
  - Providers' published hit rates correlated only 0.27–0.62 with measured ones.

  [olafdsouza.com](https://olafdsouza.com/blog/your-inference-provider-sucks-at-caching)
- **MEASURED (gateway snapshot, April 2026, mixed customer traffic; seen in search snippet only, page not opened):** Anthropic-direct 77%, OpenAI 36%, DeepSeek 48%. — [Requesty](https://www.requesty.ai/data/cache-hit-rate-by-provider-april-2026)
- **Practitioner report:** the same prompt saw 0% to 91% hit rates in production depending on provider and setup (not opened). — [dev.to](https://dev.to/sm1ck/we-measured-llm-prompt-caching-in-production-same-prompt-0-to-91-hit-rates-oio)

### Inferences
- Within a chat conversation, human gaps are usually seconds to a few minutes, so 80–93% of the prefix stays cached. The **first turn of each conversation** often comes after more than 10 minutes idle, when only 0–75% is cached depending on provider. Fresh user text, retrieved files and web results never cache.
- Expected cached share of chat input is about **60–70%** (low 25%, high 90%) (inference from the tables above).
- For EU hosting, choose a provider whose TTL is at least 15 minutes. That one choice moves the chat cached share by about 30 percentage points.

### Gaps
- The Keln figures are vendor self-benchmarks, and I found no independent replication.
- I found no measured cache hit rates for *human-paced chat* (all measured runs are agentic replays).
- DeepSeek's, Anthropic's and OpenAI's own published platform-wide hit-rate figures were not retrieved.

## System prompt and tool-definition overhead (and memory/project files)

### Takeaway
Fixed prompt overhead is the largest controllable input cost in chat. Consumer assistants ship 15–30K-token system prompts, according to leaks. MCP tool schemas cost about 80–600 tokens per tool, and a 20–70-tool surface costs 3–13K tokens on every turn unless tools are deferred.

### Cited Findings
- **Secondary (leaks, not official):** the Claude 3.7-era Claude.ai system prompt with tools was about 24,000 tokens; Claude 4.6 was about 15,000 tokens; a 2026 prompt was reported at 27–30K tokens. — [Towards AI](https://pub.towardsai.net/tokens-wasted-on-empty-words-claudes-leaked-24k-system-prompt-is-shockingly-inefficient-5e188a2792a8); [Adversa AI](https://adversa.ai/blog/revealing-claude-4-6-system-prompt-using-a-chain-of-partial-to-full-prompt-leak-attack); [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks)
- **VENDOR-MEASURED (PolicyLayer, o200k tokenizer):**
  - Per-server averages run from 78 to 193 tokens per tool. A 19-tool server costs 3,213 tokens and a 67-tool server 12,920 tokens.
  - Allow-listing 3 of 11 tools cut the cost about 73%.

  [PolicyLayer token-cost index](https://policylayer.com/token-cost?add=jina)
- **Other blog figures:**
  - Typical tool schemas are 250–600 tokens. A 30K-token tool surface is re-sent on every turn of a 20-turn session. — [Unblocked](https://getunblocked.com/blog/mcp-tool-overload/)
  - Measured Codex CLI total prompt overhead was 25,450 tokens vs an expected 8,500. Claude Code defers MCP schemas behind tool search, while Cursor, Windsurf and Gemini CLI load everything upfront. — [Daniel Vaughan, Apr 2026](https://codex.danielvaughan.com/2026/04/23/mcp-schema-bloat-system-prompt-tax-tool-definition-performance/)

### Inferences
- For the founder's own workspace (ESTIMATE): a lean system prompt of 1.5–3K, 10–15 core tools at about 150 tokens each (1.5–2.5K), and memory/profile of 0.5–2K come to **about 4–7K tokens of static prefix per turn**. A Claude.ai-scale prompt would be 15–30K.
- Project files or knowledge attached in context add their full size on each turn, cacheable only if they stay byte-stable at the front of the prompt.
- The prefix is identical across turns, so it is the most cacheable part. The prefix should be ordered as system prompt, then tools, then memory, then project files, then history, so the stable parts lead.

### Gaps
- There is no official token count for any vendor's production system prompt.
- PolicyLayer's counts use the o200k tokenizer, so open-model tokenizers will differ.

## Recommended baseline (for one cost computation)

### Takeaway
Use the expected-value per-unit figures below. Each one cites a measured anchor where one exists, and estimates are labeled.

### Cited Findings
Baseline per unit:

| Unit | Low | Expected | High | Anchor (measured unless marked) |
|---|---|---|---|---|
| User message tokens | 70 | 300 | 1,600+ | [LMSYS](https://arxiv.org/html/2309.11998v4) 69.5; [WildChat](https://arxiv.org/pdf/2405.01470) 295.6 ± 1609 |
| Static prefix: system + tools + memory | 2,000 | 5,000 | 25,000 | ESTIMATE; [PolicyLayer](https://policylayer.com/token-cost?add=jina) per-tool; [leaks](https://adversa.ai/blog/revealing-claude-4-6-system-prompt-using-a-chain-of-partial-to-full-prompt-leak-attack) 15–30K |
| History per turn | 0 | 1,500 | 10,000 | INFERENCE from 2.0–2.5 turns per conversation, power-user skew |
| **Input tokens per chat turn** | **2,000** | **7,000** | **35,000** | Cross-check: [OpenRouter](https://arxiv.org/html/2601.10088v1) average prompt about 6K (late 2025); coding requests >20K |
| Visible output per turn | 215 | 450 | 1,000 | [LMSYS](https://arxiv.org/html/2309.11998v4); [WildChat](https://arxiv.org/pdf/2405.01470); [OpenRouter](https://arxiv.org/html/2601.10088v1) about 400 |
| Reasoning tokens per turn, blended over routing mix | 0 | 250 | 1,000 | [Keln](https://keln.ai/blog/ai-gateway-benchmark-deepseek-v4-1-flash) mean 403–1,033 and median 36–54 when always on; [Nous](https://nousresearch.com/measuring-thinking-efficiency-in-reasoning-models-the-missing-benchmark) 1.5–10x |
| **Output tokens per chat turn** | **215** | **700** | **2,000** | sum of the two rows above |
| Cached share of chat input | 25% | 65% | 90% | [Keln](https://keln.ai/blog/ai-gateway-benchmark-deepseek-v4-1-flash) by idle bucket; [olafdsouza](https://olafdsouza.com/blog/your-inference-provider-sucks-at-caching) TTL; [Requesty](https://www.requesty.ai/data/cache-hit-rate-by-provider-april-2026) 36–77% |
| Deep research, reader input | 100K | 600K | 2.5M | [UCSD](https://escholarship.org/uc/item/36h5r7z4) web content per task 0.1–2.5M |
| Deep research, planner/supervisor input | 20K | 40K | 100K | ESTIMATE |
| Deep research, writer input | 15K | 30K | 60K | ESTIMATE |
| **Deep research input per run (all roles)** | **150K** | **~700K** | **2.6M** | [UCSD](https://escholarship.org/uc/item/36h5r7z4); [ODR README](https://github.com/langchain-ai/open_deep_research) about 2.05M per task (inference) |
| Deep research output per run, intermediate (planner + readers) | 2K | 3.5K | 6K | [UCSD](https://escholarship.org/uc/item/36h5r7z4) LangChain-DR 1,966–3,527 mean |
| Deep research output per run, writer | 2K | 3K | 15K | [UCSD](https://escholarship.org/uc/item/36h5r7z4) LangChain 2.1–2.3K; o3-DR 15.2K |
| Deep research output per run, reasoning if thinking models are used | 0 | 2K | 4K | [UCSD](https://escholarship.org/uc/item/36h5r7z4) GPT-5 1.8–2.2K; o3-DR 3.5–4.1K |
| Cached share of deep-research input | 5% | 20% | 40% | INFERENCE: web content is unique per run |
| Searches + fetches per run | 6–10 | 25–40 | 100–150 | [Anthropic](https://www.anthropic.com/engineering/multi-agent-research-system) effort rules (ESTIMATE from them) |
| Deep research multiplier vs a chat turn | 4x | 15x | — | [Anthropic](https://www.anthropic.com/engineering/multi-agent-research-system) (agents 4x, multi-agent 15x) |
| Measured cost per deep-research run, frontier APIs | $0.05 | $0.26–$0.57 | $1.27 | [FutureSearch](https://futuresearch.ai/cost-of-deep-research); [UCSD](https://escholarship.org/uc/item/36h5r7z4) |

### Inferences
Daily volume at the reference usage of 100 turns and 2 runs, using expected values:
- **Chat:** about 700K input tokens per day (about 455K cached, about 245K uncached) and about 70K output tokens per day.
- **Deep research:** about 1.4M input tokens per day (about 1.1M uncached) and about 17K output tokens per day.
- Deep research is therefore about two-thirds of daily input tokens, and the majority of uncached input, from only 2% of interactions. Its reader stage is where a cheap long-context model gives the biggest savings.
- One cross-check (ESTIMATE): at Keln's DeepSeek V4.1 Flash list prices ($0.30 input, $0.01 cached, $1.20 output per million tokens), the expected day costs about $0.16 for chat ($0.074 uncached input + $0.005 cached + $0.084 output) and about $0.36 for deep research ($0.34 uncached input + $0.02 output), before routing to stronger models. The report writer should recompute with the chosen EU provider's prices.

### Gaps
- The deep-research role split, the search counts and the file-generation figures are estimates, because no public source measures them.
- The cache-hit figures come mainly from vendor benchmarks (Keln) and one independent replay. None measures human-paced chat.
- Consumer turn-length data predates 2025.
