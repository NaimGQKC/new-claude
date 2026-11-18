# 01 – Analysis (research findings)

Date: 2026-11-18. Goal: a self-hosted, Claude-style app. It should have per-task model routing, smart context and token handling, and deep research as the main use case. The base is LibreChat, and it should accept Chinese and other LLMs.

Evidence labels: **[verified]** read from the project's own docs. **[secondary]** blogs or aggregators, so double-check. **[assumption]** my estimate or prior knowledge, to be tested in a spike.

---

## 1. Base: LibreChat (decision: yes, with a *thin* fork)

| Need | Status in LibreChat | Notes |
|---|---|---|
| License | MIT [verified] | Commercial use and rebranding are fine. |
| Any LLM | Custom OpenAI-compatible endpoints via `librechat.yaml`: `baseURL`, `apiKey`, `models`, `addParams`, `dropParams`, `headers` [verified] | DeepSeek, Kimi, Qwen and GLM all expose OpenAI-style APIs [assumption, confirm in spike]. OpenRouter is a one-key fallback. |
| Reasoning models | `customParams`: `reasoningFormat` (`reasoning_effort`, `reasoning_object`, `disabled`), `reasoningKey` (`reasoning_content`), replay of reasoning history [verified] | Chinese thinking models return `reasoning_content`, which is covered. |
| Effort slider (Claude-style) | Not confirmed as a first-class UI control | Likely a small custom feature that maps the slider to thinking on/off, effort or budget per model. |
| Per-task models | Already partly there [verified]: each agent has its own model; **subagents** run in their own context with their own model, tools and memory; `summarization.provider/model`; `titleModel`; the memory agent has its own model; model specs / presets | Most of the "right model for each job" idea is config, not code. |
| Artifacts | React, HTML and Mermaid, with fullscreen preview [verified] | |
| Context management | `summarization` block [verified]: triggers (`token_ratio`, `remaining_tokens`, `messages_to_refine`), `retainRecent`, `maxSummaryTokens`, `contextPruning` of old tool output, manual "Compact context". Context-usage gauge plus optional cost display (v0.8.7). | Strong base. We tune it for caching (section 4). |
| Memory | Key/value facts, a `set_memory` / `delete_memory` tool, optional background memory agent, a Memories panel [verified]. It is **off until configured**. | Whole store is sent each turn, so it is for short facts only. No search over history. Fine for now (memory is your last priority). |
| Projects | Shared instructions plus reference files (v0.8.9) [verified] | |
| Export | Markdown, text, JSON, CSV and screenshot [secondary/verified docs]. **No PDF.** | Only JSON and CSV include all branches. You said markdown or text is enough, so the PDF priority is dropped. |
| MCP tools | Supported, with `deferred_tools` so tools don't all load into context [verified] | This is how we plug in deep research and browser tools. |
| Auth / multi-user | OAuth2, LDAP, email, passkeys [verified] | You are the only user, but this matters for the commercial case. |
| Stack | Node/React, MongoDB, Meilisearch, optional Redis, Docker Compose [secondary] | About 47k stars, fast releases (v0.8.5 to v0.8.9 in months). |

**Fork strategy.** LibreChat ships fast, so a heavy fork means constant merge pain. Rules:
1. Do as much as possible in `librechat.yaml` (endpoints, specs, summarization, memory).
2. Put new capabilities in **separate services behind MCP** (deep research, browser agent).
3. Fork only for UI and logic that can't live elsewhere (effort slider, task routing, usage dashboard). Keep patches small and rebase on each release.

**Rejected bases.** Open WebUI uses a non-OSI license with a branding clause, so it's a problem for commercial use [secondary]. LobeChat's license is unclear. Onyx is MIT and has built-in deep research, but it is a company-search product rather than a personal Claude clone.

## 2. Deep research (main use case)

| Option | License | What it is | Verdict |
|---|---|---|---|
| **GPT Researcher** | Apache-2.0, about 31k stars [verified] | Planner plus workers, cited reports, custom OpenAI-compatible endpoint via `OPENAI_BASE_URL`, MCP client, a separate `gptr-mcp` MCP server, runs as FastAPI/Docker | **Phase-1 pick.** Fastest way to get deep research into LibreChat as an MCP tool. Whether it supports separate fast/smart/strategic models is not confirmed here (I believe it does, via env vars [assumption]). |
| **LibreChat-native** (agent + subagents + search + MCP) | MIT | A smart planner agent that spawns cheap reader subagents | **Phase-2 candidate.** Gives us full control of context and cost, and the best UX (inline in chat). More work. |
| LangChain `open_deep_research` | MIT [verified] | Supervisor plus researchers, per-stage models, MCP | **Archived 2026-08-21.** Good reference design only. Do not build on it. |
| Tongyi DeepResearch (Alibaba) | Apache-2.0 [verified] | 30B/3B-active model *trained* for research. Needs Serper (search), Jina (page reading), a Python sandbox, and a summarizer API. Hosted on OpenRouter and Alibaba Bailian. | Possible "research brain" later via hosted API. 128K context. |
| MiroThinker | Apache-2.0 (likely) [secondary] | Open research models. v1.7 about 74% BrowseComp. | Same idea. Evaluate later. |
| Onyx | MIT community edition | Whole platform with deep research | Reference, not a base. |

Search and reading layer (needed by any option):
- DeepSeek's API offers Search and Fetch at **$0.75 per 1,000 requests** [verified], so about $0.075 for a 100-call run.
- Alternatives: Tavily, Brave, Exa, self-hosted SearXNG, Jina Reader [secondary].
- Plug-in point for GPT Researcher is unverified. Test in a spike.

Benchmarks are noisy. Scores depend on the judge model and the setup, and the sources disagree on who leads [secondary]. **We should build our own small test set (10 to 20 of your real research questions) and compare models on it**, rather than trust leaderboards.

Key insight: deep research cost and quality depend mostly on **which model does the reading and which does the reasoning**. A cheap model reads and summarizes pages, and a smart model plans and writes. That is the per-task routing you described.

## 3. Models (the "per-task" map)

Prices per 1M tokens (official DeepSeek page [verified]; others [secondary], confirm before budgeting):

| Model | Input (cache miss) | Cache hit | Output | Notes |
|---|---|---|---|---|
| DeepSeek V4.1 Flash | $0.30 peak / $0.15 off-peak | $0.006 / $0.003 | $1.20 / $0.60 | 1M context, thinking on/off, vision |
| DeepSeek V4 Pro | $1.32 / $0.66 | $0.044 / $0.022 | $3.96 / $1.98 | 1M context, no vision |
| Qwen3.5 Plus | $0.40 | n/a | $2.40 | [secondary] |
| Kimi K2 | $0.60 | n/a | $2.50 | [secondary] |
| GLM-5 | $1.00 | n/a | $3.20 | [secondary] |

DeepSeek peak hours are 01:00–04:00 and 06:00–10:00 UTC on weekdays; everything else is half price. Heavy jobs like deep research can be **scheduled or queued off-peak**.

Proposed task slots for the design phase:

| Slot | Needs | Starting candidate |
|---|---|---|
| Everyday chat | Fast, cheap | DeepSeek Flash |
| Hard reasoning / "high effort" | Smart | DeepSeek V4 Pro, Kimi, or GLM-5 |
| Deep-research planner and writer | Smart, reliable tool use | V4 Pro or Kimi (test on your questions) |
| Deep-research reader / page summarizer | Cheapest, huge volume | Flash or Qwen Flash |
| Titles, summaries, memory extraction | Cheapest | Flash |
| Vision (images, screenshots, browser) | Multimodal | Flash (has vision) or Qwen-VL [assumption] |
| Browser agent | Strong tool use plus vision | To test |

Do we need LiteLLM? **Not at first.** LibreChat already talks to many OpenAI-style endpoints directly. LiteLLM (MIT) is a "switchboard" that sits in front of all providers. It adds automatic fallbacks if a provider is down, central API keys, and spend tracking [secondary]. Add it later if we need those, especially for the commercial version.

## 4. Smart context and tokens (what we add on top)

LibreChat gives us summarization, pruning and a usage gauge. The design should add:

1. **Cache-friendly prompts.** DeepSeek cache hits cost about **50x less** than misses ($0.006 vs $0.30) [verified]. Keep the system prompt and history prefix stable and append-only. Every edit or reshuffle of old messages breaks the cache.
2. **Compact late and in big steps.** With 1M-token windows, summarizing at about 80% fullness is fine, and each summary rewrites the prefix and breaks the cache once. Avoid frequent small summaries.
3. **Prune tool output first.** Old search and page dumps are the biggest waste. LibreChat's `contextPruning` does this, and we tune it.
4. **Cheap model for summaries.** Set `summarization.model` to Flash.
5. **Deep research context isolation.** Readers work in their own context and return short notes, so the main chat never sees raw pages (the subagent pattern).
6. **Visible budget.** Per-conversation cost, a daily cap, and a warning before a deep research run ("estimated about $1").
7. **Effort slider.** Low, medium and high map to model choice plus thinking on/off.

## 5. Browser agent (last)

| Option | Notes |
|---|---|
| Nanobrowser | Chrome extension, closest to Claude in Chrome [secondary] |
| browser-use | Python agent framework on Playwright, very popular [secondary] |
| Playwright MCP | Browser tools for any agent, no planning of its own [secondary] |
| Stagehand | TypeScript, Playwright plus AI actions [secondary] |

For your use cases:
- **Gmail:** use the API or an MCP server, not browser clicking. Safer and more reliable.
- **LinkedIn / Instagram:** browser-session automation is against LinkedIn's terms and gets accounts restricted, mostly when volume is high and messages look the same [secondary, vendor-written]. Instagram's official API only covers business accounts and a 24-hour reply window [secondary].
- **Safer pattern:** the agent drafts and **you approve each send**, at human-like volume, using your own logged-in browser.
- **Prompt injection:** an agent reading DMs or emails can be tricked by text inside them. Needs confirmation prompts and limited permissions.

## 6. Cost: self-hosted vs ChatGPT Enterprise

### Competitor prices (weak evidence; Enterprise is not published)
- ChatGPT Business: about **$20–25/user/mo**, 2-seat minimum [secondary].
- ChatGPT Enterprise: reported **$45–75/user/mo, 150-seat minimum**, about $108k/year entry; the often-quoted $60 traces back to a 2023 post [secondary].
- Claude Team about $25–30; Claude Enterprise reports conflict ($20–35) [secondary].

### Our assumptions [assumption, all changeable]
- Chat turn: 8k tokens in (80% cache hit), 600 out.
- Deep research run: 1.5M tokens in (50% cache hit), 60k out, plus about $0.10 of search.
- Prices are DeepSeek peak (worst case). Fixed hosting about $60/mo (25 users), $150 (150 users), $400 (500 users).

| User type | Chat turns/mo | Deep research runs/mo | API cost/user/mo (Flash chat + Pro research) |
|---|---|---|---|
| Light | 100 | 2 | **$2.85** |
| Typical | 400 | 10 | **$14.10** |
| Heavy | 1,000 | 30 | **$42.06** |

Per deep research run: about **$1.36 on V4 Pro**, about **$0.40 on Flash only**. Deep research is about 95% of the cost.

### Company comparison (typical users)

| Seats | Self-hosted (API + hosting) | ChatGPT Business @ $25 | ChatGPT Enterprise @ $45–60 |
|---|---|---|---|
| 25 | **$413/mo** ($16.50/user) | $625 | n/a (150 minimum, so $6,750–9,000) |
| 150 | **$2,265/mo** ($15.10/user) | $3,750 | **$6,750–9,000** |
| 500 | **$7,451/mo** ($14.90/user) | $12,500 | **$22,500–30,000** |

### Personal-use check (added after review)
The "Light / Typical / Heavy" table above is **per month**. If you do roughly 100 chats and 2 deep research runs **per day**, multiply by 30:

| Per-run cost assumption | 2 runs/day, per month | 1 run/day, per month | Break-even vs a $20 plan |
|---|---|---|---|
| V4 Pro, my guess (1.5M in / 60k out) | **$85** | $45 | 12 runs/mo |
| Flash, my guess | **$28** | $16 | 41 runs/mo |
| V4 Pro, lean (500k in / 30k out) | $34 | $19 | 32 runs/mo |
| Flash, lean | $13 | $9 | 100 runs/mo |

- Chat is almost free (about $3.70/mo for 100 chats a day). **Deep research is the whole bill.**
- A $20 ChatGPT plan is flat, but deep research on it is capped. The most-cited cap is about 25 runs/month (about 250 on Pro) [secondary, not on OpenAI's pricing page; check the in-app counter].
- Tokens per deep research run are **my guess**, not measured. This is the biggest uncertainty and needs a real test run.
- On cost alone, for one person, this is **not clearly better than a $20 plan**. The case for building rests on control, model choice, context handling and no caps, or on the commercial angle.

### Is it commercializable?
**Cheaper on raw cost, but price alone is a weak pitch.**
- At 150+ seats, raw cost is about 3–4x below ChatGPT Enterprise. That leaves room for a good margin even at $25–30/seat.
- At 25 seats, we are barely under ChatGPT Business ($16.50 vs $25), and that excludes our time. A small company will just buy Business.
- The numbers exclude engineering, support, security work and compliance (SOC 2, SSO, audit logs, data-loss controls), which is where an enterprise product's real cost sits.
- **The biggest commercial problem is data residency.** Many companies won't send documents to Chinese-hosted APIs. Fix: serve open-weight models (DeepSeek, Qwen, Kimi, GLM) from US/EU hosts or the customer's own GPUs. That changes prices, and I haven't priced it. Needs its own research.
- Heavy users are expensive. Flat-price competitors win on them, so a commercial version needs usage caps, off-peak scheduling for deep research, or usage-based pricing.
- Real selling points: model choice, data control or self-hosting, per-task optimization, no vendor lock-in, and lower cost at scale.
- The space is crowded (LibreChat, Open WebUI, Onyx, LobeChat, and others [secondary]).

## 7. Open questions / spikes before design is final
1. Confirm that LibreChat works against DeepSeek, Kimi, Qwen and GLM endpoints, with thinking models and tool calling. Chinese models vary in tool-call quality.
2. Test GPT Researcher through `gptr-mcp` in LibreChat, using a Chinese model for the LLM and a search API for retrieval.
3. Decide how the effort slider maps onto each provider's thinking parameters.
4. Build the 10–20 question deep research test set and compare candidate models.
5. Confirm the memory and `summarization` config on a running instance.
6. Verify official prices for Qwen, Kimi and GLM, and check cache-hit pricing.

## Sources
- [LibreChat repo](https://github.com/danny-avila/LibreChat), [custom endpoints](https://www.librechat.ai/docs/configuration/librechat_yaml/object_structure/custom_endpoint), [memory](https://www.librechat.ai/docs/features/memory), [summarization](https://www.librechat.ai/docs/configuration/librechat_yaml/object_structure/summarization), [v0.8.5 changelog](https://www.librechat.ai/changelog/v0.8.5), [subagents](https://www.librechat.ai/docs/features/subagents), [export docs](https://www.librechat.ai/docs/features/import_convos)
- [Open WebUI vs LibreChat (license)](https://docs.openwebui.com/alternatives/librechat.md), [Onyx comparison](https://onyx.app/insights/openwebui-alternatives)
- [GPT Researcher](https://github.com/assafelovic/gpt-researcher), [gptr MCP docs](https://docs.gptr.dev/docs/gpt-researcher/retrievers/mcp-configs), [LangChain open_deep_research (archived)](https://github.com/langchain-ai/open_deep_research), [Tongyi DeepResearch](https://github.com/Alibaba-NLP/DeepResearch), [MiroThinker](https://github.com/MiroMindAI/MiroThinker), [DeepResearch Bench paper](https://proceedings.iclr.cc/paper_files/paper/2026/file/465f22be10e07b301c6ed58f0472f704-Paper-Conference.pdf)
- [DeepSeek pricing (official)](https://api-docs.deepseek.com/quick_start/pricing), [Qwen pricing](https://benchlm.ai/alibaba/api-pricing), [GLM-5 vs Qwen3.5 pricing](https://anotherwrapper.com/tools/llm-pricing/qwen3.5-397b-a17b/glm-5), [China AI pricing](https://capitalandcompute.net/md/china-ai-pricing.md)
- [ChatGPT Enterprise pricing](https://redresscompliance.com/openai-enterprise-pricing-2026-per-user-analysis.html), [ChatGPT for Work pricing](https://www.eesel.ai/blog/chatgpt-work-pricing), [Enterprise AI price index](https://coworker.ai/blog/enterprise-ai-price-index)
- [Browser agents compared](https://dev.to/agdex_ai/ai-native-browser-automation-in-2026-browser-use-stagehand-steel-and-playwright-mcp-compared-160n), [LinkedIn automation risk](https://cotera.co/articles/linkedin-automation-ai-agents), [Instagram API limits](https://instantdm.com/guides/instagram-ai-agent-rate-limits-safety)
- [LiteLLM docs](https://docs.litellm.ai/docs)
