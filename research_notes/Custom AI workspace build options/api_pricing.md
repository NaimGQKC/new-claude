# API pricing for a self-hosted AI workspace (as of 2026-11-18)

Conventions: all prices are USD. "/1M" means per 1,000,000 tokens (not per token). "/day" and "/30d" are per day and per 30-day month. Fetch date for every page: 2026-11-18. Official pages mostly show no "last updated" date; where a page showed none, it is noted. Prices below were read through a page-to-text fetcher, so a few pages were truncated or rendered empty (flagged in Gaps).

## 1. Official per-1M-token prices, context window, peak/off-peak, batch, tiers

### Takeaway
Cheapest tier (about $0.10-0.30 in / $0.50-1.20 out per 1M) is DeepSeek V4.1 Flash, GLM-5.3-Flash, Qwen3.8-Flash, MiniMax M3.1-Flash, GPT-6-luna and Claude Haiku 5.5. Mid-tier ($1.3-2.5 in / $4-10 out per 1M) is DeepSeek V4 Pro, GLM-5.3, Kimi K3.1 Pro, Qwen3.7-Max, GPT-6.2-sol, Claude Sonnet 5.5, Gemini 4 Carbon/Argon. Frontier tier ($4-8 in / $20-40 out per 1M) is Opus 5.5, Fable 5.2, GPT-6.2-astra. Note model names in this table are exactly as the pages list them.

### Cited Findings

**DeepSeek (first party), per 1M tokens** — [DeepSeek pricing](https://api-docs.deepseek.com/quick_start/pricing) (no last-updated date on page; mentions changes effective 2026-11-18)
- `deepseek-flash` (V4.1-Flash-1017): context 1M, max output 384K. Cache hit $0.003 off-peak / $0.006 peak; cache miss $0.15 / $0.30; output $0.60 / $1.20.
- `deepseek-v4-pro` (V4-Pro-0813): context 1M, max output 384K (page lists context/output once for both; fetcher assumed it applies to both). Cache hit $0.022 / $0.044; cache miss $0.66 / $1.32; output $1.98 / $3.96. No vision on Pro; Flash has vision.
- Off-peak is half of peak. Peak = 01:00-04:00 and 06:00-10:00 UTC Mon-Fri excluding Chinese public holidays; everything else (weekends, holidays) is off-peak.
- No batch discount or context tiers listed on this page. Legacy names `deepseek-v4-flash` still accepted and billed at Flash prices.
- Search and Fetch APIs $0.75 per 1,000 successful requests each; server-side search/fetch triggered during model calls is NOT billed from 12:00 Beijing time on 2026-11-18 (token usage only). File parsing/OCR $0.225 per 1,000 pages.

**Z.ai GLM, per 1M tokens** — [Z.ai pricing](https://docs.z.ai/guides/overview/pricing) (no date, no context window listed)
- GLM-5.3: in $1.4, cached in $0.26, out $4.4. GLM-5.2 and 5.1: same. GLM-5: $1 / $0.2 / $3.2.
- GLM-5.3-Flash: $0.15 / $0.03 / $0.50. GLM-5.3-FlashX: $0.37 / $0.075 / $1.25. GLM-4.7-FlashX $0.07/$0.01/$0.4. GLM-4.7-Flash and GLM-4.5-Flash are free. GLM-4.5-Air $0.2/$0.03/$1.1.
- Cached-input storage is "limited-time free". Web Search built-in tool: $0.01 per use.

**Moonshot Kimi** — [Kimi pricing docs](https://platform.kimi.ai/docs/pricing/chat) (price table rendered EMPTY in fetch; text only)
- Context: K3 series 1,048,576 tokens; K2 series 262,144. K2 closed to new users 2026-10-31, retirement planned end of Dec 2026. Batch for kimi-k3.1-pro and kimi-k3 is 60% of standard price.
- Per-token numbers could only be cross-checked: Moonshot AI endpoint at $2 in / $10 out per 1M for K3.1 Pro (and a "highspeed" $4 / $20) via [OpenRouter K3.1 Pro providers](https://openrouter.ai/moonshotai/kimi-k3.1-pro/providers); Together lists K3.1 Pro $2.00 in / $0.20 cached / $10.00 out and K3 $3.00 / $0.30 / $15.00 on [Together pricing](https://www.together.ai/pricing). A search summary of aggregators gives cache write $2 (5-min) / $4 (1-hour) — unverified secondary, see [search result](https://developer.puter.com/tutorials/kimi-api-pricing/). Treat $2 / $0.20 / $10 as consistent across three sources but NOT read from the Kimi table.

**Alibaba Qwen via Model Studio, Singapore/international, per 1M** — [Model Studio pricing](https://www.alibabacloud.com/help/en/model-studio/model-pricing) (first 100k chars read of ~156k; page says these are list prices; some rows flagged "limited-time 20% off")
- Max: qwen4-max $1.5 in / $4.5 out (≤1M); qwen3.8-max $2 / $6; qwen3.7-max $2.5 / $7.5; qwen-max $1.6 / $6.4.
- Plus: qwen3.7-plus ≤256K $0.4 / $1.6, 256K-1M $1.2 / $4.8 (carries a "20% off for a limited time" label; listed numbers are originals); qwen3.6-plus $0.5/$3 (≤256K), $2/$6 (256K-1M); qwen3.5-plus $0.4/$2.4 and $0.5/$3.
- Flash: qwen3.8-flash $0.15 / $0.47 (0-1M); qwen3.7-flash tiered $0.03/$0.13 (≤32K), $0.10/$0.40 (32-256K), $0.20/$0.80 (256K-1M); qwen3.5-flash $0.1/$0.4.
- Batch: "half price" for qwen-max and qwen3.7/3.6/3.5-flash and qwen-flash; no batch discount listed for Plus. Context window not stated explicitly; tiers go to 1M.

**MiniMax, per 1M** — [MiniMax pay-as-you-go](https://platform.minimax.io/docs/guides/pricing-paygo) (no date; context window not listed)
- M3.1-Flash: in $0.15, out $0.60, cache read $0.015.
- M3 standard: ≤512k input tokens $0.30 / $1.20, cache read $0.06; >512k $0.60 / $2.40, cache read $0.12 ("permanent 50% off", previously double). Priority tier 1.5x standard. Cache write price not listed.

**OpenAI, per 1M** — [OpenAI API pricing](https://developers.openai.com/api/docs/pricing) (openai.com/api/pricing returned 403; no date). Short context ≤272K input; long >272K roughly 2x input, 1.5x output.
- gpt-6.2-astra $8.00 in / $0.40 cached / $40.00 out (long: $16/$0.80/$60). gpt-6.2-sol $2.00 / $0.10 / $10.00 (long $4/$0.20/$15). gpt-6.1-terra $1.00/$0.05/$5.00. gpt-6-luna (listed as mini/nano tier) $0.10 / $0.01 / $0.50 (long $0.20/$0.02/$0.75). gpt-5.6-luna $0.20/$0.02/$1.20. gpt-5.4-mini $0.75/$0.075/$4.50; gpt-5.4-nano $0.20/$0.02/$1.25. gpt-5.5 $5/$0.50/$30.
- Batch = 50% (e.g. gpt-6.2-sol $1.00/$0.05/$5.00; gpt-6-luna $0.05/$0.005/$0.25). Flex same as batch on most models. "Fast" (formerly Priority) = 2x-4x (gpt-6.2-sol $4/$0.20/$20).

**Anthropic, per MTok (= per 1M)** — [Anthropic pricing](https://platform.claude.com/docs/en/about-claude/pricing) (no date)
- Claude Fable 5.2: $8 in / $10 5m-write / $16 1h-write / $0.20 cache read / $40 out. Opus 5.5: $4 / $5 / $8 / $0.20 / $20. Sonnet 5.5: $2 / $2.50 / $4 / $0.10 / $10. Haiku 5.5: $0.10 / $0.125 / $0.20 / $0.01 / $0.50 for prompts ≤100K tokens; $0.50 / $0.625 / $1 / $0.05 / $2.50 for prompts >100K. Haiku 4.5 $1/$5.
- Opus 5 / 4.x: $5 in, $25 out. Sonnet 5: $2/$10 (introductory price made permanent; the planned Sept 1 rise to $3/$15 "will not occur").
- Batch API = 50% off input and output (Sonnet 5.5 $1/$5; Opus 5.5 $2/$10; Haiku 5.5 $0.05/$0.25 ≤100K). Full 1M context at standard price for 4.6+ models except Haiku 5.5. US-only inference (`inference_geo: "us"`) = 1.1x on everything. Fast mode (Opus 5.5 $8/$40; Fable 5.2 $16/$80), not combinable with batch.
- Tokenizer note: Claude 4.7 and later produce about 30% more tokens for the same text than earlier models, so per-token price comparisons with older Claude or other vendors understate real cost.

**Google Gemini, per 1M, paid tier** — [Gemini pricing](https://aistudio.google.com/docs/pricing) (301 redirect from ai.google.dev; 116k chars, first 100k read plus tool section; no date)
- Gemini 4 Carbon and Argon: $2.00 in / $0.10 cached / $10 out, rising to $4.00 / $0.20 / $20 on 2026-12-01. Gemini 4 Neon $3 / $0.15 / $15. Gemini 4 Hydrogen $1.50 / $0.075 / $7.50.
- Gemini 3.8 Flash and 3.6 Flash: $0.75 / $0.075 / $3.75, rising to $1.50 / $0.15 / $7.50 on 2027-01-01 (cache storage $0.50 -> $1.00 per 1M per hour). Gemini 3.5 Flash-Lite $0.30 / $0.03 / $2.50. Gemini 3.1 Pro Preview $2 (≤200k) / $4 (>200k) in, out $12/$18.
- Batch and Flex = 50% of standard for most models (Carbon/Argon $1.00 in / $5.00 out now). Priority tier ~1.8x. Gemini 2.5 Pro/Flash being deprecated and re-routed 2026-12-01.
- Free tier exists for Hydrogen, 3.8/3.6 Flash and others (input/output tokens free), not for Carbon/Argon/Neon.

### Inferences
- Source conflicts to flag: older web mirrors quote DeepSeek V4 Pro at $0.435 / $0.87 (a launch-period 75% discount to 2026-05-31) — stale relative to the current official $0.66/$1.98 off-peak. See [OpenRouter V4 Pro search results](https://openrouter.ai/models/deepseek/deepseek-v4-pro).
- Gemini 4 Carbon price doubles in 12 days (Dec 1) and Gemini 3.8 Flash doubles on Jan 1, so any cost model built today should use the post-change prices for planning.
- Haiku 5.5 is by far the cheapest Anthropic option, but its price quintuples for prompts >100K, which matters for deep-research agent loops whose context grows past 100K.

### Gaps
- Kimi official per-token table did not render in fetch (two attempts incl. .md). Moonshot first-party web-search tool pricing not found.
- Qwen web-search / code-interpreter prices and implicit-cache percentages for Singapore were not found on the pricing page (remaining 56k chars of page unread for those items; second fetch of the offset returned nothing relevant).
- MiniMax and Z.ai context windows not listed on their price pages.
- Anthropic "Fable/Mythos" are the pages' names for the top tier; Mythos is limited-access. Not verified from any second source.

## 2. Prompt caching mechanics per provider

### Takeaway
All providers cache automatically on prefix match; Anthropic is the only one that requires (or recommends) explicit `cache_control` and charges a write surcharge (1.25x for 5 min, 2x for 1 hour). OpenAI GPT-5.6+ also now charges a write premium. Read discounts range from 90% (typical) to 95-97.5% (newest Anthropic/OpenAI/DeepSeek models).

### Cited Findings
- DeepSeek: automatic, on by default, no code change; no fixed TTL, unused caches cleared "within a few hours to a few days"; no write surcharge mentioned; hit/miss tokens reported as `prompt_cache_hit_tokens` / `prompt_cache_miss_tokens`; best-effort, not guaranteed 100% — [DeepSeek KV cache guide](https://api-docs.deepseek.com/guides/kv_cache). Flash hit = 2% of miss price; Pro hit = 3.3% of miss price (from [pricing](https://api-docs.deepseek.com/quick_start/pricing)).
- Anthropic: two modes — automatic (single top-level `cache_control`) or explicit breakpoints. 5-minute write 1.25x, 1-hour write 2x, read 0.1x on most models; 0.05x on Opus 5.5 and Sonnet 5.5; 0.025x on Fable/Mythos 5.1/5.2. Break-even after 1 read (5m) or 2 reads (1h). Multipliers stack with batch and data-residency — [Anthropic pricing: prompt caching](https://platform.claude.com/docs/en/about-claude/pricing).
- OpenAI: automatic by default; min 1,024 tokens; GPT-5.6+ can use explicit breakpoints. On GPT-5.6+: write 1.25x for default 30-minute lifetime or 2.5x for 12-hour (Responses API); read 0.1x typical, 0.05x on GPT-6.2 Astra/Sol and GPT-6.1 Sol/Terra. Earlier models: no write charge, in-memory 5-10 min (up to 1 hour), optional 24h retention — [OpenAI prompt caching guide](https://developers.openai.com/api/docs/guides/prompt-caching).
- Google: implicit caching on by default for Gemini 2.5+; min 4,096 tokens for Gemini 4 / 3.8 / 3.6 / 3.1 Pro (2,048 for 2.5); explicit caching NOT supported on Gemini 4 models (still on Gemini 3 / 2.5 via generateContent); on Gemini 4 a multi-turn request caches the prior request in full only if the new request adds ≥2,050 tokens. Storage fee for explicit caches $0.50-$4.50 per 1M tokens per hour depending on model — [Gemini caching](https://aistudio.google.com/docs/caching), [Gemini pricing](https://aistudio.google.com/docs/pricing). Page did not state TTL or the implicit-hit discount percentage; the price table implies 10% of input (Carbon $0.10 vs $2.00).
- Z.ai: implicit, automatic; no TTL stated ("reasonable time limits"); `usage.prompt_tokens_details.cached_tokens`; page text says cache-hit tokens are billed "usually 50%" — [Z.ai cache guide](https://docs.z.ai/guides/capabilities/cache). CONFLICT: price table gives cached $0.26 vs $1.4 input (18.6%) — [Z.ai pricing](https://docs.z.ai/guides/overview/pricing), and Alibaba's doc says GLM hit billing is ~18.57-25% — [Alibaba context cache](https://www.alibabacloud.com/help/en/model-studio/context-cache). Use the price table.
- Kimi: automatic context caching on repeated prefixes, default TTL 5 minutes; for K3 series, cache writes are billed by TTL (5 min or 1 hour), and cached input billed only at the hit price — [Kimi pricing docs](https://platform.kimi.ai/docs/pricing/chat).
- Alibaba Qwen: implicit cache hits typically 20% of input price, creation 100% (no surcharge), min 1,024 tokens (512 for Zhipu-deployed GLM), TTL not fixed; explicit cache creation typically 125%, hits 10%, 5-minute TTL refreshed on each hit; qwen4-max explicit: create $1.875 (5m) / $3 (1h), hit $0.075; DeepSeek V4 Pro 0813 and Flash implicit hits listed at 10% — [Alibaba context cache](https://www.alibabacloud.com/help/en/model-studio/context-cache). Note: this 10% for DeepSeek on Alibaba differs from DeepSeek first-party (3.3%/2%).
- MiniMax: cache read price listed ($0.015 Flash, $0.06 M3); mechanism and write price not documented on the price page — [MiniMax pricing](https://platform.minimax.io/docs/guides/pricing-paygo).

### Inferences
- For a workspace that re-sends an ever-growing conversation, DeepSeek, Anthropic (5m TTL with automatic caching), Qwen and Kimi all reward keeping the prompt prefix byte-stable. Two chat turns more than 5 minutes apart will usually miss a 5-minute cache (Anthropic default, Kimi default, Qwen explicit) — so for ~100 turns/day spread across the day, the realistic hit rate is lower than the 90% assumed below unless 1-hour TTL is used (Anthropic 2x write).
- Gemini 4's 4,096-token minimum and 2,050-token increment rule means short chats may get little cache benefit.

### Gaps
- Gemini implicit-cache TTL; MiniMax cache TTL and write price; DeepSeek/Z.ai/Kimi minimum cacheable size (DeepSeek and Z.ai docs state none).

## 3. Third-party hosts for open-weight models, prices, and US/EU hosting

### Takeaway
The OpenRouter provider tables show most mainstream US inference hosts (Together, Fireworks, Baseten, Nebius, Parasail, DigitalOcean, Cloudflare, etc.) charging identical-to-first-party list price for GLM-5.3 ($1.40/$4.40) and Kimi K3.1 Pro ($2/$10), and 2x the off-peak DeepSeek V4 Pro price (= parity with DeepSeek's peak price, $1.32/$3.96). Geo-pinned US options carry a 25-50% premium. OpenRouter does not state provider locations.

### Cited Findings
- DeepSeek V4 Pro 0813 on OpenRouter (per 1M in/out): DeepSeek and Alibaba Int. and StreamLake $0.66 / $1.98 (DeepSeek and Alibaba lines labelled as time-of-day UTC window rate); NovitaAI $0.99 / $2.97; DeepInfra $1.04 / $2.08 (other DeepInfra listings $1.30-1.95); Together, Baseten, Nebius, Parasail, DigitalOcean, SiliconFlow, Cloudflare, AtlasCloud $1.32 / $3.96; CoreWeave $1.31 / $3.96. Outliers: Relace $0.0999 / $8.00, Wafer $0.111 / $4.44. "Not currently available through EU in-region routing." No locations given — [OpenRouter V4 Pro 0813 providers](https://openrouter.ai/deepseek/deepseek-v4-pro-0813/providers).
- GLM-5.3 on OpenRouter: Z.ai, Together, Fireworks, Nebius, Parasail, Crusoe, SambaNova, Baseten (fp4) all $1.40 / $4.40; DeepInfra $0.45 / $2.00 (and a second listing $0.5625 / $2.50); NovitaAI $0.63 / $1.98; SiliconFlow $0.70 / $1.90; Cloudflare $0.70 / $2.20; Bedrock $1.68 / $5.28. Europe (EU in-region routing): Inceptron $1.05 / $4.20 and Mistral $1.54 / $4.84 (Mistral also lists $1.40 / $4.40 non-EU) — [OpenRouter GLM-5.3 providers](https://openrouter.ai/z-ai/glm-5.3/providers). Fireworks "Spot" $0.98 / $3.08.
- Kimi K3.1 Pro on OpenRouter: Moonshot AI $2 / $10 (and $4 / $20 highspeed); Fireworks, Together, Nebius, DigitalOcean, Parasail, Alibaba Int., Modal $2 / $10; DeepInfra $1.90 / $9.50; Bedrock $4 / $20 (and $4.40 / $22); not available through EU in-region routing — [OpenRouter K3.1 Pro providers](https://openrouter.ai/moonshotai/kimi-k3.1-pro/providers). OpenRouter says pay-as-you-go with no markup on provider price.
- Together official serverless (per 1M in / cached / out): DeepSeek V4.1 Flash $0.30 / $0.006 / $1.20; V4 Pro 0813 $1.32 / $0.13 / $3.96; GLM-5.3 $1.40 / $0.26 / $4.40; GLM-5.3-Flash $0.15 / $0.03 / $0.50; Kimi K3.1 Pro $2 / $0.20 / $10; Qwen3.7-Max $2.50 / $0.50 / $7.50; MiniMax M3.1 Flash $0.15 / $0.015 / $0.60. A separate "US geo-pinned" table lists V4 Pro $1.65 / $0.1625 / $4.95 (+25%), V4.1 Flash $0.375 / $0.0075 / $1.50 (+25%), GLM-5.3 $1.75 / $0.325 / $5.50 (+25%), Kimi K3 $3.75 / $0.375 / $18.75 (+25%) — [Together pricing](https://www.together.ai/pricing). The page does not describe residency policy itself.
- Secondary (aggregator/blog, Oct-Nov 2026): Fireworks, Together, Baseten quote same list price for GLM-5.3 ($1.40/$4.40) and Kimi K3 ($3/$15); Fireworks US-hosted Kimi K3 and GLM-5.3 reportedly 50% more than default endpoints — [agentpedia, Nov 11 2026](https://agentpedia.codes/blog/best-ai-inference-providers-2026), [andrew.ooo, Oct 2026](https://andrew.ooo/answers/leading-serverless-inference-providers-2026/). Not verified on Fireworks' own page.
- Groq: only Kimi K2 found ($1.00 in / $3.00 out, cached $0.50) per [Layer3 Labs guide, updated Aug 6 2026](https://www.layer3labs.io/guides/groq-pricing) (secondary). Cerebras: GLM 4.7 at $2.25/M (secondary, [search results](https://computeprices.com/compare/cerebras-vs-fireworks-ai)). No current Groq/Cerebras price for GLM-5.3, Kimi K3.x or DeepSeek V4 found.

### Inferences
- Premium vs first party: DeepSeek V4 Pro on US hosts is 0% above DeepSeek's peak rate but +100% above off-peak ($1.32 vs $0.66 in; $3.96 vs $1.98 out); GLM-5.3 and Kimi K3.1 Pro on US hosts are ~0% premium (parity), and a US geo-pinned option is +25% (Together). The real premium of EU/US hosting is the cache discount differences: Together DeepSeek V4 Pro cached $0.13 vs DeepSeek first party $0.022-0.044 (3-6x higher).
- Cheap outliers (Relace, Wafer, AkashML, inference.net at $0.07-0.25 input) likely reflect different input/output skew, quantization, or caching assumptions; their locations are not stated, and I did not verify them. Don't use without checking.
- EU hosting for these models is thin: only Mistral and Inceptron appear on GLM-5.3 with EU routing; DeepSeek V4 Pro and Kimi K3.1 Pro show none on OpenRouter.

### Gaps
- Fireworks, DeepInfra, Novita, Groq, Cerebras official pages not fetched directly; location/data-center country per host not stated on OpenRouter pages; OpenRouter pages are listing snapshots with no date.

## 4. Search, fetch, and tool pricing

### Takeaway
Native web search costs $10 per 1,000 calls at Anthropic and OpenAI, $14 per 1,000 at Google (after 5,000 free per month), $0.01 per use ($10 per 1,000) at Z.ai, and is free at DeepSeek from 2026-11-18 (previously $0.75 per 1,000). Code execution is free or cheap everywhere.

### Cited Findings
- Anthropic: web search $10 per 1,000 searches plus tokens for search results; web fetch no extra charge beyond tokens; code execution free when used with web search/fetch (`_20260209` tool versions), otherwise 1,550 free hours/month then $0.05 per container-hour (min 5-minute execution); Managed Agents session runtime $0.08 per session-hour plus tokens — [Anthropic pricing](https://platform.claude.com/docs/en/about-claude/pricing). Tool-use system prompt adds ~286 tokens (Sonnet/Opus/Haiku 5.5).
- OpenAI: web search $10 per 1K calls plus search content tokens at model rates; "web search preview" $25 per 1K; Code Interpreter/hosted shell $0.03 (1 GB) to $1.92 (64 GB) per 20-minute session; file search $2.50 per 1K calls, storage $0.10/GB/day (1 GB free) — [OpenAI pricing](https://developers.openai.com/api/docs/pricing).
- Google: Search grounding for Gemini 3+ = 5,000 free per month (shared), then $14 per 1,000 requests (Gemini 2.5: 1,500 RPD free then $35 per 1,000); code execution and URL context free as tools (tokens only); Maps grounding 5,000/mo free then $14 per 1,000 (Gemini 3+); Gemini Deep Research billed at standard token list rates incl. thinking tokens, tool fees separate — [Gemini pricing](https://aistudio.google.com/docs/pricing).
- DeepSeek: Search API and Fetch API $0.75 per 1,000 successful requests each; server-side search/fetch during model calls not billed from 2026-11-18 12:00 Beijing time — [DeepSeek pricing](https://api-docs.deepseek.com/quick_start/pricing).
- Z.ai: Web Search $0.01 per use — [Z.ai pricing](https://docs.z.ai/guides/overview/pricing).

### Inferences
- For 2 deep-research runs/day at ~40 searches each (assumption, not sourced) = 80 searches/day = 2,400/month: Anthropic/OpenAI about $24/month ($0.80/day), Z.ai $24/month, Google $0 (inside the 5,000 free/month, if chat doesn't also use grounding), DeepSeek $0. Search tool fees matter only for the cheapest models (more than the token bill for DeepSeek Flash).
- A self-hosted workspace can swap in a cheaper search backend (not researched here).

### Gaps
- Kimi, Qwen, MiniMax search/code-interpreter pricing not found.

## 5. Published token consumption for chat turns and deep-research runs

### Takeaway
Measured deep-research input volumes vary by 20x depending on harness: from about 45k (OpenAI o3 Deep Research) to 315k (Gemini Deep Research) to 670-780k (Claude Opus + web search and Perplexity) input tokens per task, with output only 6k-25k. This supports the user's 500k-3M scenarios as the plausible upper range; 500k is closer to measured data. No authoritative figure exists for typical chat turn tokens.

### Cited Findings
- DRACO benchmark (Perplexity; arXiv 2602.11685, submitted 12 Feb 2026) — the paper abstract itself reports no token counts ([arXiv](https://arxiv.org/abs/2602.11685)). Average input / output tokens per task as listed on a secondary aggregator, flagged "self-reported" and attributed to DRACO: Perplexity Deep Research (Opus 4.6) 778,711 / 8,807; Claude Opus 4.6 with web search + code execution 691,338 / 8,143; Claude Opus 4.5 same tools 669,389 / 6,174; Gemini Deep Research 315,548 / 22,066; OpenAI Deep Research (o3) 44,587 / 24,944; o4-mini 40,891 / 12,615 — [benchmarklist DRACO](https://benchmarklist.com/benchmarks/draco/). The aggregator does not state units; it is secondary, so verify in the paper before quoting.
- Anthropic engineering: agents use ~4x more tokens than chat; multi-agent systems ~15x more tokens than chat; token usage alone explains 80% of BrowseComp performance variance; lead agent launches 3-5 parallel subagents; complex research can use >10 subagents — [Anthropic multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system).
- GAIA per-task averages (Memento paper, 10-task sample, from search summary): Level 1 about 26k in / 4.7k out; Level 2 about 48k / 6.9k; Level 3 about 121k / 9.8k — [Memento arXiv 2508.16153](https://arxiv.org/pdf/2508.16153). Not deep research per se.
- Harness comparison (DRIFT paper, from search summary): average total tokens per trajectory differ by harness, e.g. bare 5.6k, Codex 12.5k, Claude Code 28.1k — [search result](https://arxiv.org/pdf/2606.02060). Not verified against the paper.
- Chat turn: real-world assistant responses fluctuate about 480-810 tokens per turn; most WildChat/LMSYS conversations are <1k tokens in total (ThoughtTrace study, from search summary) — [ThoughtTrace arXiv 2605.20087](https://arxiv.org/pdf/2605.20087). Re-sending history makes cumulative input grow roughly quadratically; a 20-turn session of ~1,000 new tokens per turn gives about 210,000 cumulative input tokens — [tianpan.co, 2026-05-17](https://tianpan.co/blog/2026/05/17/quadratic-cost-conversation-ai-chat-spend) (blog, illustrative arithmetic, not a measurement).

### Inferences
- Output tokens per research run: 6k-25k measured in DRACO; the 30k assumed in the cost model below is on the high side (conservative) for the report plus intermediate reasoning, but reasoning models with long thinking could exceed it.
- The user's assumed 8k input / 600 output per chat turn is within the plausible range (600 output matches the ~480-810 measured), but an 8k prompt implies system prompt + moderate history.

### Gaps
- No vendor-published per-turn token average; most numbers come from a secondary aggregator or search-engine summaries of papers that I did not read in full. DeepSeek/GLM/Kimi-driven research harnesses (e.g. open-source deep-research agents) have no token figures found.

## 6. Worked cost model

### Takeaway
At 100 chat turns/day plus 2 deep-research runs/day (1.5M input, 85% cached, 30k output per run), monthly token cost ranges from about $4-7 (cheap-tier: DeepSeek V4.1 Flash, GPT-6-luna, Haiku 5.5, MiniMax Flash, Qwen3.8-Flash, GLM-5.3-Flash) through about $15-40 (DeepSeek V4 Pro, MiniMax M3, Qwen3.7-Plus, Gemini 3.8 Flash) to $75-90 (GPT-6.2-sol, Sonnet 5.5, Kimi K3.1 Pro, Gemini 4 Carbon now, GLM-5.3, Qwen3.7-Max up to $116) and $170-320 for Opus 5.5 / Fable 5.2 / GPT-6.2-astra. Research runs dominate the bill on every model except the cheap tier.

### Assumptions (all per the stated user usage; mine unless marked)
- Chat: 100 turns/day; each turn 8,000 input tokens (user-stated), of which I assume 90% cache hit and 10% cache miss (assumption; a 5-minute TTL may lower real hit rate); 600 output tokens (user-stated). Thinking tokens not added.
- Research: 2 runs/day (user-stated); the "input tokens" figure is the cumulative billed input across all LLM calls in a run (500k / 1.5M / 3M, user-stated scenarios); I assume 85% of input is a cache hit (growing context re-sent each step; assumption) and 15% cache miss; 30,000 output tokens per run (assumption; DRACO measured 6k-25k).
- Cache write surcharge applied only to Anthropic on the miss portion (1.25x, 5-minute write); OpenAI GPT-5.6+ also lists a 1.25x write premium, which I did not apply (it would add under 3% to chat cost). Gemini 4 Carbon shown at both the current and the Dec 1 price. DeepSeek shown at both peak and off-peak (peak = 01:00-04:00 and 06:00-10:00 UTC weekdays, about 7 of 24 hours on weekdays, so real blended cost is closer to the off-peak figure plus ~25-35% for a daytime-heavy user). Qwen cache hit price is ASSUMED at 20% of input (documented as typical implicit-cache hit rate, not read per model). Kimi prices cross-checked (not read from the official table). Batch not used (interactive).
- Tool fees (search) are excluded; see section 4 (about $24/month at 40 searches per run for Anthropic/OpenAI/Z.ai, $0 for DeepSeek and Google within free quota).
- Calculation script output is reproducible: cost = (input x hit% x cache-hit price + input x miss% x miss price x write multiplier + output x output price) / 1,000,000. Per-request price tiers (Haiku 5.5 >100K, GPT >272K, Qwen >256K, Gemini 3.1 Pro >200K) were NOT applied: this assumes each individual API call stays under the tier threshold, plausible when 1.5M total is spread over ~40+ calls, but not guaranteed.

### Chat only: 100 turns/day (8k in, 90% cached, 600 out) — USD
| Model | per turn | per day | per 30 days |
|---|---|---|---|
| GPT-6-luna | 0.00045 | 0.045 | 1.36 |
| DeepSeek V4.1 Flash off-peak / peak | 0.00050 / 0.00100 | 0.05 / 0.10 | 1.50 / 3.01 |
| Claude Haiku 5.5 (≤100K prompt) | 0.00047 | 0.047 | 1.42 |
| MiniMax M3.1-Flash | 0.00059 | 0.059 | 1.76 |
| Qwen3.8-Flash (cache 20% assumed) | 0.00062 | 0.062 | 1.85 |
| GLM-5.3-Flash | 0.00064 | 0.064 | 1.91 |
| MiniMax M3 | 0.00139 | 0.139 | 4.18 |
| DeepSeek V4 Pro off-peak / peak | 0.00187 / 0.00375 | 0.19 / 0.38 | 5.62 / 11.25 |
| Qwen3.7-Plus (cache 20% assumed) | 0.00186 | 0.186 | 5.57 |
| Gemini 3.5 Flash-Lite | 0.00196 | 0.196 | 5.87 |
| Gemini 3.8 Flash (current price) | 0.00339 | 0.339 | 10.17 |
| GLM-5.3 | 0.00563 | 0.563 | 16.90 |
| Gemini 4 Hydrogen | 0.00624 | 0.624 | 18.72 |
| GPT-6.2-sol | 0.00832 | 0.832 | 24.96 |
| Gemini 4 Carbon (now) / from Dec 1 | 0.00832 / 0.01664 | 0.83 / 1.66 | 24.96 / 49.92 |
| Claude Sonnet 5.5 | 0.00872 | 0.872 | 26.16 |
| Kimi K3.1 Pro | 0.00904 | 0.904 | 27.12 |
| Qwen3.7-Max | 0.01010 | 1.010 | 30.30 |
| Claude Opus 5.5 | 0.01744 | 1.744 | 52.32 |
| GPT-6.2-astra | 0.03328 | 3.328 | 99.84 |
| Claude Fable 5.2 | 0.03344 | 3.344 | 100.32 |

### Deep research: 2 runs/day, 30k out each, 85% cached — USD per run, per day (2 runs), per 30 days (60 runs)
Columns show 500k / 1.5M / 3M cumulative input tokens per run.
| Model | per run | per day (2 runs) | per 30 days |
|---|---|---|---|
| GPT-6-luna | 0.027 / 0.050 / 0.086 | 0.05 / 0.10 / 0.17 | 1.6 / 3.0 / 5.1 |
| Claude Haiku 5.5 (≤100K prompt per call) | 0.029 / 0.056 / 0.097 | 0.06 / 0.11 / 0.19 | 1.7 / 3.4 / 5.8 |
| DeepSeek V4.1 Flash off-peak | 0.031 / 0.056 / 0.093 | 0.06 / 0.11 / 0.19 | 1.8 / 3.3 / 5.6 |
| DeepSeek V4.1 Flash peak | 0.061 / 0.111 / 0.186 | 0.12 / 0.22 / 0.37 | 3.7 / 6.7 / 11.2 |
| MiniMax M3.1-Flash | 0.036 / 0.071 / 0.124 | 0.07 / 0.14 / 0.25 | 2.1 / 4.3 / 7.4 |
| Qwen3.8-Flash (cache 20% assumed) | 0.038 / 0.086 / 0.158 | 0.08 / 0.17 / 0.32 | 2.3 / 5.2 / 9.5 |
| GLM-5.3-Flash | 0.039 / 0.087 / 0.159 | 0.08 / 0.17 / 0.32 | 2.3 / 5.2 / 9.5 |
| MiniMax M3 (≤512k) | 0.084 / 0.180 / 0.324 | 0.17 / 0.36 / 0.65 | 5.0 / 10.8 / 19.4 |
| Qwen3.7-Plus (cache 20% assumed) | 0.112 / 0.240 / 0.432 | 0.22 / 0.48 / 0.86 | 6.7 / 14.4 / 25.9 |
| DeepSeek V4 Pro off-peak | 0.118 / 0.236 / 0.413 | 0.24 / 0.47 / 0.83 | 7.1 / 14.2 / 24.8 |
| DeepSeek V4 Pro peak | 0.237 / 0.472 / 0.825 | 0.47 / 0.94 / 1.65 | 14.2 / 28.3 / 49.5 |
| Gemini 3.5 Flash-Lite | 0.110 / 0.181 / 0.286 | 0.22 / 0.36 / 0.57 | 6.6 / 10.8 / 17.2 |
| Gemini 3.8 Flash (current) | 0.201 / 0.377 / 0.641 | 0.40 / 0.75 / 1.28 | 12.0 / 22.6 / 38.5 |
| GLM-5.3 | 0.347 / 0.778 / 1.425 | 0.69 / 1.56 / 2.85 | 20.8 / 46.7 / 85.5 |
| Gemini 4 Hydrogen | 0.369 / 0.658 / 1.091 | 0.74 / 1.32 / 2.18 | 22.2 / 39.5 / 65.5 |
| GPT-6.2-sol and Gemini 4 Carbon (now; same prices) | 0.492 / 0.877 / 1.455 | 0.98 / 1.75 / 2.91 | 29.6 / 52.6 / 87.3 |
| Claude Sonnet 5.5 | 0.530 / 0.990 / 1.680 | 1.06 / 1.98 / 3.36 | 31.8 / 59.4 / 100.8 |
| Kimi K3.1 Pro | 0.535 / 1.005 / 1.710 | 1.07 / 2.01 / 3.42 | 32.1 / 60.3 / 102.6 |
| Qwen3.7-Max | 0.625 / 1.425 / 2.625 | 1.25 / 2.85 / 5.25 | 37.5 / 85.5 / 157.5 |
| Gemini 4 Carbon (from Dec 1) | 0.985 / 1.755 / 2.910 | 1.97 / 3.51 / 5.82 | 59.1 / 105.3 / 174.6 |
| Claude Opus 5.5 | 1.060 / 1.980 / 3.360 | 2.12 / 3.96 / 6.72 | 63.6 / 118.8 / 201.6 |
| GPT-6.2-astra | 1.970 / 3.510 / 5.820 | 3.94 / 7.02 / 11.64 | 118.2 / 210.6 / 349.2 |
| Claude Fable 5.2 | 2.035 / 3.705 / 6.210 | 4.07 / 7.41 / 12.42 | 122.1 / 222.3 / 372.6 |

### Combined monthly total (chat + research), per 30 days, at 500k / 1.5M / 3M input per research run
| Model | 500k | 1.5M | 3M |
|---|---|---|---|
| GPT-6-luna | $3.0 | $4.4 | $6.5 |
| Claude Haiku 5.5 | $3.1 | $4.8 | $7.2 |
| DeepSeek V4.1 Flash off-peak / peak | $3.3 / $6.7 | $4.8 / $9.7 | $7.1 / $14.2 |
| MiniMax M3.1-Flash | $3.9 | $6.0 | $9.2 |
| Qwen3.8-Flash | $4.1 | $7.0 | $11.3 |
| GLM-5.3-Flash | $4.2 | $7.1 | $11.4 |
| MiniMax M3 | $9.2 | $15.0 | $23.6 |
| Qwen3.7-Plus | $12.3 | $20.0 | $31.5 |
| DeepSeek V4 Pro off-peak / peak | $12.7 / $25.4 | $19.8 / $39.6 | $30.4 / $60.7 |
| Gemini 3.5 Flash-Lite | $12.5 | $16.7 | $23.1 |
| Gemini 3.8 Flash | $22.2 | $32.8 | $48.6 |
| GLM-5.3 | $37.7 | $63.6 | $102.4 |
| Gemini 4 Hydrogen | $40.9 | $58.2 | $84.2 |
| GPT-6.2-sol / Gemini 4 Carbon (now) | $54.5 | $77.6 | $112.3 |
| Claude Sonnet 5.5 | $58.0 | $85.6 | $127.0 |
| Kimi K3.1 Pro | $59.2 | $87.4 | $129.7 |
| Qwen3.7-Max | $67.8 | $115.8 | $187.8 |
| Gemini 4 Carbon (from Dec 1) | $109.0 | $155.2 | $224.5 |
| Claude Opus 5.5 | $115.9 | $171.1 | $253.9 |
| GPT-6.2-astra | $218.0 | $310.4 | $449.0 |
| Claude Fable 5.2 | $222.4 | $322.6 | $472.9 |

### Cache-hit sensitivity (research runs, 1.5M input, 30k out, per DAY for 2 runs; hit rate 0% / 50% / 85% / 95%)
- DeepSeek V4 Pro (peak): $4.20 / $2.28 / $0.94 / $0.56
- Claude Sonnet 5.5: $8.10 / $4.50 / $1.98 / $1.26 (includes 1.25x write on misses)
- GPT-6.2-sol: $6.60 / $3.75 / $1.75 / $1.19
- Kimi K3.1 Pro: $6.60 / $3.90 / $2.01 / $1.47

### Inferences
- Caching is worth more than model choice among mid-tier models: dropping from 85% to 0% hit roughly 4x-4.5x's the research bill.
- Research dominates: at 1.5M tokens per run, 2 runs/day costs 5-10x as much as 100 chat turns/day on mid-tier models; on the cheapest models they are similar.
- Using a cheap model for chat (Flash/luna/Haiku, under $4/month) and a mid-tier model for research ($14-60/month) is cheaper than any one frontier model for both ($170-320/month).
- Chat on a 600-token output model barely moves with price of output; input cache-miss price dominates chat cost.
- Haiku 5.5's >100K prompt tier ($0.50 in / $2.50 out) would multiply its research cost about 5x if calls exceed 100K tokens each; with 3M input tokens in a single long-context agent this could happen.
- Gemini and OpenAI numbers use list prices; Gemini 4 Carbon doubles Dec 1 and Gemini 3.8 Flash doubles Jan 1.

### Gaps
- Real cache hit rate not measurable without usage; Qwen implicit-cache rate unverified per model; chat/Kimi cache write costs (5m/1h) not included; no thinking-token estimate (reasoning models can multiply output tokens); no search/fetch tool fees in the totals.
