# Deep-research systems and search/fetch infrastructure (as of 2026-11-18)

Conventions: "MEASURED" = number reported by a benchmark run or the vendor's own metered data. "VENDOR-STATED" = vendor claim or list price. "ESTIMATE" = my arithmetic from stated assumptions. Many pages were read through a summarising fetch tool, and several GitHub pages did not show release dates; those are listed under Gaps. Aggregator sites often disagree with first-party pages; where they do, I say so.

## 1. Open-source deep-research projects (license, stars, architecture, model roles, MCP, outputs)

### Takeaway
No single project is clearly the best fit. GPT Researcher (Apache-2.0, ~30.8k stars) and Local Deep Research (MIT, ~9.6k stars) are the most directly usable for self-hosting with cheap OpenAI-compatible models and an MCP server. LangChain open_deep_research is MIT, benchmarked with token and cost data, but archived on 2026-08-21. Tongyi DeepResearch and MiroThinker are trained research models with agent harnesses, not complete "report writer" products, and they need their own tool stack (Serper, Jina, a summariser LLM, a sandbox).

### Cited Findings
- **GPT Researcher**: Apache-2.0, 30.8k stars. Planner generates research questions and execution agents gather information, followed by a publisher step. Works with any OpenAI-compatible endpoint via `OPENAI_BASE_URL`. MCP client (`RETRIEVER=tavily,mcp`) and a separate MCP server repo (gptr-mcp). Exports PDF/Word/Markdown. Its README claims "Deep Research" costs about $0.4 per run using o3-mini at high reasoning effort, about 5 minutes. Context-filter cost per report in its README: $0.115 to $0.192 depending on filter. The release page showed no releases in the fetched snapshot. — [GitHub](https://github.com/assafelovic/gpt-researcher)
- **GPT Researcher FAQ** states about $0.01 per run for GPT-4 era usage; this is dated. — [GPT Researcher FAQ via search result](https://docs.gptr.dev/docs/faq)
- **LangChain open_deep_research**: MIT, 12.7k stars, archived (read-only) on Aug 21, 2026. LangGraph server; models loaded via `init_chat_model()`. Four separately configurable roles (summarization, research, compression, final report), defaults gpt-4.1-mini / gpt-4.1 / gpt-4.1 / gpt-4.1. Requires structured outputs and tool calling. Has `mcp_config`. Default search Tavily. — [GitHub](https://github.com/langchain-ai/open_deep_research)
- **Tongyi DeepResearch (Alibaba-NLP)**: Apache-2.0, 20.2k stars. Model is Tongyi-DeepResearch-30B-A3B (30.5B total, 3.3B active, 128K context), released 2025-09-17. ReAct mode and an IterResearch "Heavy" mode. Tools: Serper (search and Scholar), Jina (page "visit"), an OpenAI-compatible LLM for page summarisation, DashScope for file parsing, SandboxFusion for Python. Available on OpenRouter. — [GitHub](https://github.com/Alibaba-NLP/DeepResearch)
- **MiroThinker**: Apache-2.0, 8.5k stars. Latest announced MiroThinker-1.7 (235B) and 1.7-mini (30B) on 2026-03-11. Single agent, 256K context, "keep5" retains only the 5 latest tool results, up to 300 tool calls per task. Tools via MCP-style servers: E2B Python sandbox, Serper search, Jina scrape plus LLM summary; README suggests a small summariser such as Qwen3-14B or GPT-5-Nano. Self-reported BrowseComp 74.0% (the README also contains an inconsistent 88.2% claim). — [GitHub](https://github.com/MiroMindAI/MiroThinker)
- **Local Deep Research (LearningCircuit)**: MIT, 9.6k stars. Default mode is a LangGraph agent. Supports Ollama, LM Studio, llama.cpp, OpenAI, Anthropic, Gemini, OpenRouter, and any OpenAI- or Anthropic-compatible endpoint. Search: SearXNG recommended, plus arXiv, PubMed, Semantic Scholar, Wikipedia, Tavily, Brave, SerpAPI, local docs. Markdown and PDF export. MCP server over STDIO (`ldr-mcp`, tools including `quick_research`, `detailed_research`, `generate_report`; local only, no auth), authenticated HTTP REST API, Python API. Self-reported SimpleQA 95.7% with Qwen3.6-27B (Serper), xbench-DeepSearch 77% (77/100). No BrowseComp or DeepResearch Bench result reported. — [GitHub](https://github.com/LearningCircuit/local-deep-research)
- **Onyx**: MIT Community Edition, 33.5k stars. "Multi-step research flow" deep research feature; supports Ollama/LiteLLM/vLLM and major hosted providers; MCP client and MCP server. Architecture and per-role model assignment not described on the repo page. — [GitHub](https://github.com/onyx-dot-app/onyx)
- **dzhng/deep-research**: MIT, 19.9k stars. Recursive breadth x depth loop (defaults breadth 4, depth 2): generates SERP queries, extracts learnings and follow-up directions, recurses, then writes a markdown report. Default LLM o3-mini; `FIREWORKS_KEY` switches to DeepSeek R1; custom endpoint supported. Uses Firecrawl for search and scraping. Aims to stay under 500 lines. One model slot, no per-role assignment. — [GitHub](https://github.com/dzhng/deep-research)
- **Jina node-DeepResearch**: Apache-2.0, 5.2k stars. Loop of search / visit / reflect / answer until a token budget is exceeded, then "Beast Mode" forces a final answer. Answers need references to be accepted. Exposes an OpenAI-compatible `/v1/chat/completions` endpoint (model name `jina-deepsearch-v1`), streaming reasoning in `<think>` tags and `[^1]` footnote citations. Requires Jina API key; Gemini recommended, OpenAI-compatible and local LLMs supported. — [GitHub](https://github.com/jina-ai/node-DeepResearch)
- **Stanford STORM / Co-STORM**: MIT, 31.9k stars. Four stages (research with simulated expert conversations, outline, article, polish). Separately configurable LMs per stage (conversation simulator, question asker, outline, article, polish); README suggests cheaper models early and stronger for article generation. Retrievers include Serper, Brave, SearXNG, Tavily, DuckDuckGo, You, Bing. Latest cited news item is `knowledge-storm` v1.1.0 in 2025/01. — [GitHub](https://github.com/stanford-oval/storm)
- **WebThinker** (RUC-NLPIR): open code; paper reports WebThinker-32B at 15.8% on HLE; a later paper says WebThinker and WebSailor show limited performance on BrowseComp. License and star count not retrieved. — [arXiv](https://arxiv.org/pdf/2504.21776); [arXiv 2509.13309](https://arxiv.org/html/2509.13309v2)
- **Kimi-Researcher**: no evidence it is open source; papers cite it as proprietary. — [arXiv 2511.11793](https://arxiv.org/html/2511.11793v1)
- **Ubicloud "Dewey.py"** (reference build, open models): search (DuckDuckGo or Tavily), per-source LLM summary, reasoning model drafts and proposes 3 sub-queries per iteration (about 3 iterations), outline, writer, PDF export plus resumable JSON state. Used Mistral Small 24B for summarising/writing and DeepSeek-R1-Distill-Qwen-32B for reasoning. Reports 5 to 10 minutes and "less than 10 cents" per run (no token counts; no quality evaluation vs commercial). Lesson stated: a naive search-and-write version looked polished but hallucinated. — [Ubicloud blog](https://www.ubicloud.com/blog/rebuilding-deep-research-with-open-models)
- **Other 2026 claimants** (self-reported, I did not verify openness): DuMate-DeepResearch claims 58.03% on DeepResearch Bench; NVIDIA AI-Q blueprint reports 55.95 and 54.50 on DeepResearch Bench and Bench II. — [search summary of arXiv 2605.11732 and related](https://arxiv.org/pdf/2605.11732)

### Inferences
- Only open_deep_research (4 roles), STORM (5 stages), and GPT Researcher (fast/smart/strategic style slots per its docs, not confirmed on the repo page) give meaningful per-role model assignment. dzhng and node-DeepResearch are single-model loops.
- The archived status of open_deep_research means no upstream fixes; it is still a useful reference design (supervisor, parallel researchers, compression, final-report writer) to copy rather than depend on.
- Tongyi and MiroThinker are only attractive if you host a 30B model or use it via OpenRouter; the research harness around them (Serper plus Jina plus summariser) is the same stack you would build natively.

### Gaps
- Release dates and recent commit dates for most repos were not shown in the fetched pages. Verify with `gh api repos/OWNER/REPO/releases`.
- WebThinker license/stars; Onyx internals and per-role model settings; GPT Researcher exact model-slot variable names.
- Whether any 2026 open-source project beats GPT Researcher / open_deep_research on independent benchmarks: not found.

## 2. Quality evidence (benchmarks, independent leaderboards, commercial vs open)

### Takeaway
Independent, current numbers are thin. The only clean commercial-vs-commercial RACE table I could read is the original June 2025 paper (Gemini DR 48.88 > OpenAI DR 46.98 > Perplexity 42.25), judged by Gemini-2.5-Pro. The leaderboard now uses a GPT-5.5 judge, so old and new scores are not comparable, and I could not read the live Hugging Face leaderboard. Open systems built on strong models (open_deep_research with GPT-5) have reached about 50 RACE, which is in the same range as commercial products. I found no DeepSeek V4, GLM-5 or Kimi K2.x entries on DeepResearch Bench.

### Cited Findings
- **DeepResearch Bench** (100 PhD-level tasks, 22 fields). RACE scores reports on comprehensiveness, insight/depth, instruction following, readability; FACT checks citation grounding. Original paper (arXiv 2506.11763, authors Du et al.), RACE judge Gemini-2.5-Pro, FACT judge Gemini-2.5-Flash: Gemini-2.5-Pro Deep Research 48.88 (C.Acc 81.44%, 111.21 effective citations); OpenAI Deep Research 46.98 (77.96%, 40.79); Claude-3.7-Sonnet w/ Search 40.67 (93.68%, 32.48); Perplexity Deep Research 42.25 (90.24%, 31.26); Grok Deeper Search 40.24 (83.59%, 8.15). — [arXiv 2506.11763 (HTML)](https://arxiv.org/html/2506.11763)
- Benchmark repo: RACE judge switched to GPT-5.5 on 11 May 2026; legacy Gemini-2.5-Pro submissions accepted only until 31 May 2026; RACE cleaning model GPT-5.6 Luna since 22 Sep 2026; FACT judge GPT-5.4-mini. Live leaderboard is a Hugging Face Space (did not render in my fetch). — [GitHub README](https://raw.githubusercontent.com/Ayanami0730/deep_research_bench/main/README.md); [HF Space](https://huggingface.co/spaces/muset-ai/DeepResearch-Bench-Leaderboard)
- April 2026 changelog entries (search summary of the repo): Xiaoyi DeepResearch 57.00 (#1, 16 Apr), Cellcog Max 56.67, Grep Deep Research 56.23. These are proprietary agents, under the old judge. — [repo summary via docsearch](https://docsearch.algolia.com/mcp/docs/repo/ayanami0730/deep_research_bench)
- open_deep_research on DeepResearch Bench, 100 tasks, run by LangChain (not independent): GPT-5 config RACE 0.4943; gpt-4.1 defaults 0.4309; Claude Sonnet 4 0.4401; submission config 0.4344, ranked #6 at the time (Aug 2). Another summary cites 50.60 with GPT-5, above Gemini-2.5-Pro Deep Research. — [GitHub](https://github.com/langchain-ai/open_deep_research); [search summary](https://arxiv.org/pdf/2506.11763)
- **DeepResearch Bench II** (132 tasks, rubrics from expert reports; Jan 2026 preprint): even the best systems satisfy under 50% of rubrics. Secondary-aggregator totals: OpenAI o3 Deep Research 45.40, Gemini-3-Pro Deep Research 44.60, Gemini-2.5-Pro DR 41.98, Doubao 40.99, Qwen3-Max DR 39.25, Grok 39.23, Perplexity Research 38.58, Tongyi DeepResearch 29.89. — [Emergent Mind summary](https://www.emergentmind.com/topics/deep-research-bench-ii); [arXiv 2601.08536](https://arxiv.org/html/2601.08536v1)
- **FutureSearch Deep Research Bench** (independent, FutureSearch): top is Claude 4.6 Opus (high) at 55% accuracy and $0.55/task (~6 min); Opus low 53.1% at $0.24 (~130 s); Gemini 3 Flash (low) about $0.05/task. "Most models cluster well under a dollar." Published Feb 12, updated Mar 30, 2026. — [FutureSearch](https://futuresearch.ai/blog/cost-of-deep-research)
- **BrowseComp-Plus** (830 queries, fixed corpus; vendor-run by Sail, April 22 2026): Sail (GLM-5.1 orchestrator plus gpt-oss-120b reader swarm, Qwen3-Embed-8B/BM25 retriever) 90.72% accuracy at $0.15/query; prior best open-source 68%; off-the-shelf open baseline 57%; closed solutions 90.48%. Vendor claim, not independent. — [Sail Research](https://www.sailresearch.com/news/browsecomp-plus)
- **BrowseComp aggregates (BenchLM, mixed self-reported)**: June 2 snapshot GPT-5.5 Pro 90.1%; Oct 29 snapshot top 92.5%, with Kimi K3.1 Pro 92.1%; GLM-5.1 68.0 on BrowseComp but 33.9 on LiveBrowseComp. The source warns entries mix bare models, models with browsing, and full agents, and that the benchmark is near saturation. I could not verify several of the model names. — [BenchLM](https://www.benchlm.ai/benchmarks/browsecomp)
- MiroThinker-1.7 BrowseComp 74.0% (self-reported). — [GitHub](https://github.com/MiroMindAI/MiroThinker)
- Anthropic's own research eval: Opus 4 lead with Sonnet 4 subagents beat single-agent Opus 4 by 90.2%; token usage explained 80% of BrowseComp performance variance. — [Anthropic engineering](https://www.anthropic.com/engineering/multi-agent-research-system)
- Search-API quality matters for FACT-type scores: AIMultiple (via Parallel's own article, so vendor-filtered) reports Parallel Advanced 93.5% of excerpts supported vs Tavily Advanced 64.0%. — [Parallel](https://parallel.ai/articles/tavily-alternatives.md)

### Inferences
- A well-built open pipeline on a mid-tier-plus model is plausibly within a few RACE points of ChatGPT/Gemini Deep Research (GPT-5 on open_deep_research ~50 vs Gemini-2.5 DR 48.88 under the old judge), but this was shown with GPT-5, not with DeepSeek/GLM/Kimi. Treat "close to commercial with cheap models" as a hypothesis to test on your own tasks, not a published fact.
- The Sail result suggests orchestrator-plus-cheap-reader-swarm is the cost-efficient pattern, but it ran on a fixed corpus, so web-fetch noise and paywalls are not represented.
- RACE rewards long, comprehensive reports; FACT rewards correctly attributed citations. Prioritise a separate citation-verification step if citations matter to you.

### Gaps
- Current live leaderboard (GPT-5.5 judge) values: not readable via fetch. Someone should open the HF Space.
- No published RACE/FACT for DeepSeek V4, GLM-5.x, Kimi K2.x, Qwen3.6 inside GPT Researcher / open_deep_research.
- Independent Claude Research and Perplexity Deep Research 2026 scores: not found. DRACO and LiveResearchBench results: not found.

## 3. Cost per run (measured, vendor-stated, and my estimates)

### Takeaway
Measured data show open pipelines range from about $0.10 to about $2 per task on frontier-class models, and commercial APIs from about $1 to $7 (and anecdotally $50 for the old o3-deep-research API). On DeepSeek V4.1 Flash, my estimate is $0.10 to $0.55 per run (about $0.05 to $0.28 off-peak). On a 2 runs/day schedule that is roughly $3 to $33 per month for Flash and $11 to $135 per month for Pro, before search costs.

### Cited Findings (measured or published)
- open_deep_research, 100 DeepResearch Bench tasks (LangChain-run): defaults gpt-4.1: $45.98 total, 58.0M tokens, so about $0.46 and 580k tokens per task. Claude Sonnet 4: $187.09, 138.9M tokens, so about $1.87 and 1.39M tokens per task. GPT-5: 204.6M tokens, so about 2.05M tokens per task (cost not listed). Submission config: $87.83, 207M tokens, so about $0.88 and 2.07M tokens per task. (Per-task figures are my division by 100.) — [GitHub](https://github.com/langchain-ai/open_deep_research)
- Anthropic: agents use about 4x chat tokens, multi-agent about 15x. Effort rules: simple fact-finding 1 agent with 3-10 tool calls; comparisons 2-4 subagents with 10-15 calls each; complex research 10+ subagents. — [Anthropic engineering](https://www.anthropic.com/engineering/multi-agent-research-system)
- Gemini Deep Research (Google's own estimates, not measured): standard about 250k input and 60k output tokens, about 80 searches, $1-3 per task; Max about 900k input, 80k output, about 160 searches, $3-7. Computed with Gemini 3.1 Pro at $2/$12 per M (<=200K prompts), search grounding $14 per 1,000 queries, 60% cache hit. — [tokencost.app](https://tokencost.app/blog/gemini-deep-research-agent-cost)
- Gemini Deep Research and Max launched 2026-04-21 on Gemini 3.1 Pro, async, preview. — [Google blog](https://blog.google/innovation-and-ai/models-and-research/gemini-models/next-Generation-gemini-deep-research/); [Phil Schmid](https://www.philschmid.de/deep-research-update)
- ADRA-Bank paper (search snippet, not fully read): per-task cost OpenAI $1.76, Perplexity $0.68, Grok $0.36; Gemini via web UI so no cost. — [arXiv 2512.00986](https://arxiv.org/pdf/2512.00986)
- OpenAI o3-deep-research API list price $10 input, $2.50 cached, $40 output per M plus per-call tool fees; one forum user reported about 1M input and 1M output tokens per question (anecdote, implies about $50). A Korean OpenAI page marks the dated snapshot discontinued; status unconfirmed. — [OpenAI docs](https://developers.openai.com/api/docs/models/o3-deep-research); [OpenAI forum](https://community.openai.com/t/deep-research-in-the-api-webhooks-and-web-search-with-o3/1299919)
- NVIDIA AI-Q profiling: in one Deep Research Bench run, search calls were about 30% of total cost. — [NVIDIA docs](https://docs.nvidia.com/aiq-blueprint/2.1.0/profiling/index.html)
- Sail BrowseComp-Plus cost per query on the same token workload: $0.15 (Sail), $0.97 OpenRouter, $0.98 Baseten, $1.40 Fireworks, $1.44 Together, $2.11 OpenAI GPT-5.4/Nano, $5.39 Z AI first party (GLM-5.1/GLM-4.7). Note: bar-chart labels in the source were misaligned; I used the table. — [Sail Research](https://www.sailresearch.com/news/browsecomp-plus)
- Practitioner claims (unverified): Ubicloud under $0.10 per run with 24B-32B open models; a services-firm guide $0.10-$2 per report for an n8n build; DeepSeek-API tutorial says under two cents of tool fees per run at list price. — [Ubicloud](https://www.ubicloud.com/blog/rebuilding-deep-research-with-open-models); [search summary of tech-insider tutorial](https://tech-insider.org/au/?p=2934)
- Page-text token cost can exceed the search fee by 6x-20x in a full-page-read agent (article's own model: 3 searches x 10 results per question, ~5,000 tokens per page, $2/M input). — [beri.net](https://www.beri.net/article/tavily-vs-exa-vs-brave-vs-perplexity-search-api-agent-cost-2026)

### Official per-token prices used (per 1M tokens, USD)
- **DeepSeek (official page, fetched today)**: deepseek-flash (V4.1-Flash-1017): cache hit $0.006 peak / $0.003 off-peak; cache miss $0.30 / $0.15; output $1.20 / $0.60. deepseek-v4-pro (V4-Pro-0813): cache hit $0.044 / $0.022; miss $1.32 / $0.66; output $3.96 / $1.98. 1M context, 384K max output. Off-peak is half price; peak is 01:00-04:00 and 06:00-10:00 UTC Mon-Fri excluding Chinese public holidays; all other times (including weekends) off-peak. — [DeepSeek pricing](https://api-docs.deepseek.com/quick_start/pricing)
  - Conflict: InfoWorld (Aug 2026) reported different Flash numbers ($0.22 in / $0.66 out off-peak) from the Aug 16 change; the official page now shows V4.1-Flash lower, so the official page appears to supersede it. — [InfoWorld](https://www.infoworld.com/article/4209439/deepseek-raises-some-v4-prices-by-more-than-10x-as-ai-demand-strains-capacity.html)
- **GLM (official docs)**: GLM-5 $1.00 in / $0.20 cached / $3.20 out; GLM-5.1 and GLM-5.3 $1.40 / $0.26 / $4.40; GLM-5.3-Flash $0.15 / $0.03 / $0.50; GLM-5.3-FlashX $0.37 / $0.075 / $1.25. Built-in web search $0.01 per use. — [Z.ai pricing](https://docs.z.ai/guides/overview/pricing)
- **Kimi K2.6**: first-party page shows ¥1.10 cache hit, ¥6.50 miss, ¥27.00 output per M, 262,144 context. A kimi.ai mirror (via search) gives $0.16 / $0.95 / $4.00; I use these USD figures. The page also lists K3.1 Pro, K3, K2.7 Code, K2.5 without prices. — [Kimi pricing (CNY)](https://www.kimi.com/resources/kimi-k2-6-pricing); [USD mirror via search](https://www.kimi.ai/resources/kimi-k2-6-pricing)
- **Qwen3.6-Flash (Alibaba Model Studio, official)**: Global (US/Germany/Japan/HK) and Beijing <=256K input tier $0.165 in / $0.99 out, explicit cache read $0.017; Singapore $0.25 / $1.50. 256K-1M tier $0.66 / $3.961. Beijing batch about half. — [Alibaba Cloud](https://www.alibabacloud.com/help/en/model-studio/qwen3-6-flash.md)
  - Qwen3.6-Plus is listed at $0.50 / $3 by one source and $0.325 / $1.95 by another; a Sept 2026 guide lists Qwen3.8 Max $2/$6 and Qwen3.8 Flash $0.14/$0.42 that I could not corroborate. I exclude these from the tables. — [search results](https://developer.puter.com/tutorials/qwen-api-pricing/)

### Inferences: ESTIMATES (my arithmetic)

Assumptions (not measured; anchored on measured 0.6M-2.1M tokens per task from open_deep_research and Google's 250k-900k input estimate): total input tokens per run (cumulative over all LLM calls) and output tokens, 60% of input tokens served from cache (Google quotes 50-70% implicit cache hit; agent loops re-send long prefixes), model-per-call context under 256K.

| Scenario | Input tokens | Output tokens | Description |
|---|---|---|---|
| Low | 400k | 40k | Quick question, ~15 searches, ~15 pages, short report |
| Medium | 1.2M | 80k | Typical multi-section report, ~50 searches, ~60 pages |
| High | 3.0M | 150k | Exhaustive report, ~120 searches, ~150 pages, extra verification pass |

Cost per run, LLM only (single model plays all roles), USD:

| Model | Low | Medium | High |
|---|---|---|---|
| DeepSeek V4.1 Flash, peak | 0.10 | 0.24 | 0.55 |
| DeepSeek V4.1 Flash, off-peak | 0.05 | 0.12 | 0.28 |
| DeepSeek V4 Pro, peak | 0.38 | 0.98 | 2.26 |
| DeepSeek V4 Pro, off-peak | 0.19 | 0.49 | 1.13 |
| GLM-5 | 0.34 | 0.88 | 2.04 |
| GLM-5.3-Flash | 0.05 | 0.13 | 0.31 |
| Kimi K2.6 (USD mirror prices) | 0.35 | 0.89 | 2.03 |
| Qwen3.6-Flash (Global, <=256K) | 0.07 | 0.17 | 0.38 |

Per day (2 runs) and per month (60 runs), LLM only:

| Model | Low /day | Low /month | Medium /day | Medium /month | High /day | High /month |
|---|---|---|---|---|---|---|
| DeepSeek Flash, peak | 0.19 | 5.8 | 0.49 | 14.6 | 1.10 | 33.1 |
| DeepSeek Flash, off-peak | 0.10 | 2.9 | 0.24 | 7.3 | 0.55 | 16.5 |
| DeepSeek Pro, peak | 0.76 | 22.8 | 1.96 | 58.9 | 4.51 | 135 |
| DeepSeek Pro, off-peak | 0.38 | 11.4 | 0.98 | 29.5 | 2.26 | 67.7 |
| GLM-5 | 0.67 | 20.2 | 1.76 | 52.8 | 4.08 | 122 |
| GLM-5.3-Flash | 0.10 | 3.1 | 0.27 | 8.0 | 0.62 | 18.5 |
| Kimi K2.6 | 0.70 | 21.0 | 1.78 | 53.5 | 4.06 | 122 |
| Qwen3.6-Flash | 0.14 | 4.2 | 0.34 | 10.3 | 0.75 | 22.6 |

Formula: cost = in x (0.4 x miss price + 0.6 x hit price) + out x output price. Example, Flash peak medium: 1.2 x (0.4x0.30 + 0.6x0.006) + 0.08 x 1.20 = 0.148 + 0.096 = $0.244.

Search/fetch add-on per medium run (50 searches + 60 page fetches), list prices from section 4: Tavily PAYG about $0.40 plus extract about $0.10; Exa about $0.35 (contents for 10 results included); Brave about $0.25; Serper about $0.05 at $1/1k; DeepSeek Search/Fetch about $0.04 + $0.05 (at $0.75/1k each); Firecrawl scrape about $0.06 (Standard plan); SearXNG $0 in fees. So search can equal or exceed Flash LLM cost; it is a major lever.

Other estimate observations:
- Mixed-role design (Pro or GLM-5 for planner/writer, Flash for readers): if about 15% of tokens go to the strong model and 85% to Flash, the medium run is roughly $0.35 to $0.45 peak. This is illustrative arithmetic only.
- These estimates would be a lot lower than commercial APIs ($1-7 per run) and about equal to open_deep_research's measured gpt-4.1 $0.46 per run, but with a 5-10x cheaper per-token model.

### Gaps
- No measured tokens-per-run for any DeepSeek V4, GLM-5, Kimi K2.x or Qwen3.6 research pipeline. My three scenarios are unvalidated; the first action should be to instrument a pilot (log usage per role).
- Official Anthropic/OpenAI deep-research per-run cost for ChatGPT/Claude subscription features: not published.
- Kimi K2.6 official USD price and any batch/cache terms not confirmed from the first-party USD page.
- Perplexity Sonar Deep Research per-token rate card: not retrieved (page lacked it).

## 4. Search and fetch infrastructure (prices, free tiers, limits, quality)

### Takeaway
List prices span roughly $0.75 (DeepSeek Search) and $1 (Serper, Perplexity Fast) to $5-8 per 1,000 for Tavily/Brave/Exa-class APIs. The largest cost is not the search call but the page text fed to the LLM. DeepSeek's own Search/Fetch API ($0.75/1k each) is attractive for a DeepSeek-centred stack, and its docs say server-side tool calls become unbilled from 12:00 Beijing time today. Self-hosted SearXNG removes per-query fees but is the least reliable.

### Cited Findings
- **DeepSeek Search API and Fetch API**: $0.75 per 1,000 successful requests each; file parsing/OCR $0.225 per 1,000 pages. The official pricing page says that from 12:00 Beijing time on November 18, 2026, server-side search and fetch triggered by model calls are no longer billed (only tokens). Search API opened 2026-10-17 (endpoints `POST /v1/tools/search` and `/v1/tools/fetch`). Secondary sources describe an earlier free window ending Nov 1, so the pricing page is the more current source; whether directly-called (non-model-triggered) requests stay billed is not clear from what I read. — [DeepSeek pricing](https://api-docs.deepseek.com/quick_start/pricing); [ppc.land](https://ppc.land/deepseek-prices-web-search-for-ai-agents-at-0-75-per-1-000-calls/); [DeepSeek search guide](https://api-docs.deepseek.com/guides/search)
- **Tavily** (official docs): search 1 credit basic / 2 advanced; extract 1 credit per 5 URLs basic (2 advanced); research endpoint 15-250 credits (pro) or 4-110 (mini). Free 1,000 credits/month, no card. Pay-as-you-go $0.008/credit ($8 per 1,000 basic searches); Growth plan $500 for 100k credits ($0.005). — [Tavily docs](https://docs.tavily.com/documentation/api-credits)
- **Exa**: official pricing page lists search with contents at $7 per 1,000 (10 results, text/highlights included, $1 per 1,000 extra results), Deep $12, Deep (Reasoning) $15; contents endpoint $1 per 1,000 pages; summaries $1 per 1,000. A third-party list also shows an "instant"/Lite tier at $4 and free credits ($10/month); unconfirmed on the official page. — [Exa pricing changelog](https://exa.ai/docs/changelog/pricing-update.md); [Exa pricing](https://exa.ai/docs/reference/pricing); [Parallel comparison](https://parallel.ai/articles/tavily-alternatives.md)
- **Brave Search API**: $5 per 1,000 (Search), $5 monthly free credits but card required, Answers $4 per 1,000 plus $5/M tokens (third-party, Nov 14, 2026); official page fetch returned no plan details. Brave returns snippets, not full pages. — [Parallel comparison](https://parallel.ai/articles/tavily-alternatives.md); [beri.net](https://www.beri.net/article/tavily-vs-exa-vs-brave-vs-perplexity-search-api-agent-cost-2026)
- **Perplexity Search API**: $5 per 1,000 requests, $1 with Fast Search; one request may contain up to five queries; no token charges; failed/rate-limited requests not billed. Agent API `web_search` tool $2.50 per 1,000 ($1 fast). — [Perplexity docs](https://docs.perplexity.ai/docs/getting-started/pricing)
- **Serper**: 2,500 free queries, no card (official page). Third-party: about $1 per 1,000 base, falling to about $0.30 at volume; returns snippets/links only. — [Serper](https://serper.dev); [search summary](https://fastcrw.com/alternatives/cheapest-search-api)
- **Firecrawl** (official): Free 1,000 credits (2 concurrent, 10 scrape/min); Hobby $19 for 5k; Standard $99 for 100k credits (25 concurrent, 500/min); Growth $399 for 500k; Scale $749 for 1M. Scrape 1 credit/page; JSON format +4 credits; PDF parsing 1 credit per PDF page; search 2 credits per 10 results; failed pages with 403/404 still cost 1 credit; empty results not charged. Standard plan effective about $0.99 per 1,000 pages. — [Firecrawl pricing](https://www.firecrawl.dev/pricing)
- **Jina Reader/Search**: Reader free without a key (20 RPM); free key gives 500 RPM Reader / 100 RPM Search; premium 5,000/1,000 RPM; every new key has 10M free tokens; Search is a fixed 10,000 tokens per request minimum; Reader bills by output tokens; native PDF support, `jina-ocr-v1` costs 40x more tokens. Models are CC-BY-NC 4.0, commercial use needs an Elastic license (Elastic now sells Jina commercial licenses from Aug 10, 2026). Average latency about 7.9 s Reader, 2.5 s Search. — [Jina Reader](https://jina.ai/reader)
- **Parallel** (vendor): $1 per 1,000 (Turbo/Fast), $5 (Basic/Advanced); free credits at signup; free MCP server. **You.com**: not covered by sources read. — [Parallel](https://parallel.ai/articles/tavily-alternatives.md)
- **Z.ai built-in web search**: $0.01 per use. — [Z.ai pricing](https://docs.z.ai/guides/overview/pricing)
- **SearXNG**: failure modes are upstream engines blocking the bot (silently missing results), the instance's own limiter returning 429, and JSON output not enabled by default (must enable it; failed JSON calls often return HTML). Check the `unresponsive_engines` field. No independent measured reliability data found; the You.com guide critiquing it is from a competitor. — [You.com guide](https://you.com/resources/searxng-alternatives); [SSD Nodes](https://www.ssdnodes.com/learn/searxng-rate-limits-and-429-errors); [LiteLLM docs](https://docs.litellm.ai/docs/search/searxng)

### Inferences
- With DeepSeek models, DeepSeek Search/Fetch looks cheapest for a hosted option ($0.75/1k, possibly free for model-triggered calls), but I could not verify its result quality, rate limits or paywall behaviour. Serper plus a Reader (Jina free key, or Firecrawl) is the cheap mature combination used by Tongyi and MiroThinker.
- A hybrid is sensible: SearXNG or Serper for discovery, a paid reader/extractor only for pages that fail a plain HTTP fetch.
- Paywalls: none of the vendors' pages I read promise paywall bypass; treat paywalled pages as unavailable and rely on abstracts/PDF mirrors.

### Gaps
- You.com, SerpAPI current pricing; Brave official plan table; DeepSeek Search/Fetch rate limits, quality and paywall/PDF behaviour; independent measurements of Firecrawl/Jina scraping success rates on paywalled and JS-heavy sites; Tavily rate limits.
- Independent search-quality benchmark other than the Parallel-filtered AIMultiple result.

## 5. Design patterns that cut cost

### Takeaway
Spend tokens where evidence says they matter (Anthropic: token budget explains most BrowseComp variance) but route them to cheap models: parallel cheap readers/summarisers, a stronger model only for planning and final writing, and strong caching. Effort levels with explicit budgets prevent runaway cost.

### Cited Findings
- Orchestrator-worker with parallel subagents: lead starts 3-5 subagents in parallel, each uses 3+ tools in parallel, cutting research time by up to 90%; effort-scaling rules embedded in prompts; a CitationAgent attributes claims after the loop; resumable state/checkpointing for long runs. — [Anthropic engineering](https://www.anthropic.com/engineering/multi-agent-research-system)
- Per-role models: open_deep_research uses separate summarization/research/compression/final-report models; its "bench submission" used gpt-4.1-nano for summarization. STORM suggests cheap early-stage LMs. — [open_deep_research](https://github.com/langchain-ai/open_deep_research); [STORM](https://github.com/stanford-oval/storm)
- Cheap reader model for page summaries: MiroThinker suggests Qwen3-14B or GPT-5-Nano as the summariser; Sail used gpt-oss-120b as a reader swarm under a GLM-5.1 orchestrator at $0.15/query. — [MiroThinker](https://github.com/MiroMindAI/MiroThinker); [Sail](https://www.sailresearch.com/news/browsecomp-plus)
- Context management: MiroThinker "keep5" keeps only 5 latest tool results. — [MiroThinker](https://github.com/MiroMindAI/MiroThinker)
- Token budget plus forced answer: node-DeepResearch stops at a token budget then "Beast Mode" answers. — [node-DeepResearch](https://github.com/jina-ai/node-DeepResearch)
- Breadth/depth knobs: dzhng defaults breadth 4, depth 2 (recommended 3-10 and 1-5). — [dzhng](https://github.com/dzhng/deep-research)
- GPT Researcher: skipping the context filter costs 65% more per report ($0.192 vs about $0.115). — [GPT Researcher](https://github.com/assafelovic/gpt-researcher)
- Caching: DeepSeek cache-hit input is about 2% of the miss price (e.g. $0.006 vs $0.30 peak for Flash); Google assumes 50-70% implicit cache hit; Qwen explicit cache read is about 10% of input. — [DeepSeek pricing](https://api-docs.deepseek.com/quick_start/pricing); [tokencost.app](https://tokencost.app/blog/gemini-deep-research-agent-cost); [Alibaba](https://www.alibabacloud.com/help/en/model-studio/qwen3-6-flash.md)
- Off-peak scheduling: DeepSeek charges half price outside 01:00-04:00 and 06:00-10:00 UTC on weekdays, and all weekend. — [DeepSeek pricing](https://api-docs.deepseek.com/quick_start/pricing)
- A simple search-and-write pipeline looked polished but hallucinated and lacked depth; iterative self-review and full-page/PDF extraction improved quality. — [Ubicloud](https://www.ubicloud.com/blog/rebuilding-deep-research-with-open-models)

### Inferences
- A caching layer for fetched pages (URL-keyed, with TTL) is a design recommendation from the cost structure (page text is the main token cost, per the beri.net model); no source measured its savings.
- Because DeepSeek cache-hit pricing is about 50x cheaper than a miss, keep the agent's prompt prefix stable (system prompt, plan, notes first; new evidence appended) to maximise hits.
- Run scheduled (non-urgent) jobs at off-peak times to halve Flash/Pro cost; with 2 runs/day this saves about $2-4 per month on Flash and $20-60 on Pro medium-to-high scenarios (from my table).
- Reranking before reading (embedding or small cross-encoder, as in Sail's Qwen3-Embed-8B/BM25) cuts pages read; savings unmeasured.

### Gaps
- No source quantified savings from reranking, early stopping, or page caching in deep research. A pilot should A/B these.

## 6. Exposing deep research in a chat UI (MCP, background jobs, streaming)

### Takeaway
Everyone converges on the same shape: asynchronous job, a plan or clarifying step, streamed progress/thought summaries, resumable state, and a cited report at the end. For a self-hosted chat UI, the lowest-friction options are an MCP tool that starts a job and returns an ID, or an OpenAI-compatible endpoint that streams progress.

### Cited Findings
- **Gemini**: Deep Research and Deep Research Max are async via the Interactions API (`background=True`; poll an interaction ID); streaming needs `background=True` and `stream=True`, and live thought summaries need `thinking_summaries="auto"`; "collaborative planning" lets you review and refine a plan before approving; one practitioner advises resuming streams by interaction ID after drops (community advice). — [Google Cloud docs](https://docs.cloud.google.com/gemini-enterprise-agent-platform/agents/use-deep-research); [Phil Schmid](https://www.philschmid.de/deep-research-update)
- **Claude Research**: lead agent plus parallel subagents plus citation agent; synchronous subagent execution identified as a bottleneck; resumable from failure; rainbow deployments to avoid breaking running agents. — [Anthropic engineering](https://www.anthropic.com/engineering/multi-agent-research-system)
- **ChatGPT deep research UI**: I could not retrieve OpenAI's page (HTTP 403). The o3-deep-research API supports background mode and webhooks per the OpenAI forum thread title, and one user reported a failed run when `max_output_tokens` was too low. — [OpenAI forum](https://community.openai.com/t/deep-research-in-the-api-webhooks-and-web-search-with-o3/1299919)
- **MCP/API options in open projects**: GPT Researcher (MCP client and gptr-mcp server), Local Deep Research (`ldr-mcp` STDIO plus REST), Onyx (MCP client and server), node-DeepResearch (OpenAI-compatible streaming endpoint with `<think>` blocks and footnote citations), open_deep_research (`mcp_config`, LangGraph server). — [GPT Researcher](https://github.com/assafelovic/gpt-researcher); [LDR](https://github.com/LearningCircuit/local-deep-research); [Onyx](https://github.com/onyx-dot-app/onyx); [node-DeepResearch](https://github.com/jina-ai/node-DeepResearch); [open_deep_research](https://github.com/langchain-ai/open_deep_research)
- Tavily and Perplexity expose their own research/agent endpoints (Tavily research endpoint 4-250 credits). — [Tavily docs](https://docs.tavily.com/documentation/api-credits)
- Ubicloud saved full state as JSON so research can be resumed. — [Ubicloud](https://www.ubicloud.com/blog/rebuilding-deep-research-with-open-models)

### Inferences
- Recommended UX pattern for a self-hosted workspace: (1) a `start_research(question, effort)` tool that returns a job ID after an optional plan-approval step; (2) a `get_research_status(job_id)` tool streaming phase and counters (queries run, pages read, tokens and dollars spent); (3) the final report stored as markdown with a source list. MCP clients usually have tool timeouts, so a long job should not block a single tool call. This is a design inference from the Gemini/Claude patterns, not a published standard.
- Showing live dollar and token spend per job gives the "transparent cost" the user wants and is easy because every call goes through your own gateway.

### Gaps
- Exact ChatGPT and Claude consumer-UI behaviour (progress sidebar, notifications, durations) not retrieved. MCP-spec support for long-running tasks/progress notifications not researched.

## 7. Recommended architecture (my synthesis; ESTIMATES and opinion)

### Takeaway
Build a native, small pipeline, borrowing the open_deep_research / Anthropic orchestrator-worker design, rather than adopting a whole project. Use DeepSeek V4.1 Flash for reading and drafting, a stronger model (DeepSeek V4 Pro or GLM-5) only for planning, synthesis and the verifier, and route everything through one LLM gateway that logs tokens and cost per role. Start from GPT Researcher or open_deep_research code as a reference or fallback if you want a working baseline in a day.

### Inferences
- **Pipeline**: clarify and plan (strong model, 1 call) -> N parallel researcher workers (Flash) each doing search -> rerank -> fetch -> compress to notes -> a gap-check/reflect step by the planner (max 1-2 rounds) -> writer (strong model, long-output) -> citation/claim-check pass (Flash) that verifies each cited claim against stored page text.
- **Search/fetch**: DeepSeek Search/Fetch API or Serper for search; a fetch cascade of plain HTTP + readability, then Jina Reader or Firecrawl for JS-heavy pages and PDFs; SearXNG only as a free fallback. Cache every fetched page and its summary by URL.
- **Budgets**: effort levels (quick/standard/deep) setting a max number of searches, pages and token spend, with a hard stop and "answer with what you have" like node-DeepResearch's Beast Mode.
- **Scheduling**: allow "run later at off-peak" for non-urgent jobs (half price on DeepSeek).
- **Expected cost**: about $0.15-$0.50 per standard report (about $9-30 per month at 2 runs/day) including search, based on the medium-scenario estimates above; not measured.
- **Validation plan**: run 10 representative questions against ChatGPT/Gemini deep research and your pipeline, score blind with a rubric (or a RACE-style LLM judge plus a manual citation spot-check), and record tokens per role to replace my scenario assumptions.

### Gaps
- No evidence that the DeepSeek/GLM/Kimi/Qwen stack reaches commercial-level report quality; this is the main unvalidated risk and the pilot should test it first.
