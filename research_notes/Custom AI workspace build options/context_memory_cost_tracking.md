# Context management, token efficiency, memory and cost tracking for a self-hosted LLM workspace (as of 2026-11-18)

Evidence labels used below: [VENDOR] = provider/vendor's own docs or blog (authoritative for facts about their product, not for performance claims); [PEER/PAPER] = arXiv/academic; [3P] = third-party blog/secondary; [SELF-REPORTED] = benchmark run by the party selling the thing. Model names (Opus 5.5, GPT-5.6, DeepSeek V4.1, Qwen 3.8, GLM-5.3, Kimi K3) are as shown on the vendors' pages fetched on 2026-11-18; prices change often and must be re-checked.

---

## 1. Prompt caching per provider (automatic vs explicit, TTL, minimum, discount) and how to structure prompts

### Takeaway
Chinese/open providers (DeepSeek, Moonshot, Z.ai, Qwen implicit) cache automatically with no code changes and no write fee. Anthropic and OpenAI (5.6+) add optional explicit breakpoints with write surcharges. Everything is prefix-based, so the design rule is: stable prefix, append-only history, deterministic serialization, no timestamps or per-request content early in the prompt. Anything that rewrites earlier context (summarization, tool list edits, model switching) resets the cache.

### Cited Findings

**DeepSeek**
- Caching is on by default, automatic, disk-based. A hit requires matching a stored "cache prefix unit"; units are stored at end of user input, end of model output, common prefixes detected across requests, and fixed token intervals in long inputs. TTL not fixed: cleared "usually within a few hours to a few days". "Best-effort", no guaranteed hit rate; construction takes seconds. Usage fields `prompt_cache_hit_tokens` / `prompt_cache_miss_tokens`. No minimum prefix stated on the page. [VENDOR] — [DeepSeek KV cache docs](https://api-docs.deepseek.com/guides/kv_cache)
- Current pricing page (fetched 2026-11-18): `deepseek-flash` (V4.1-Flash-1017, 1M context, 384K max output) cache hit $0.003 off-peak / $0.006 peak per 1M, cache miss $0.15 / $0.30, output $0.60 / $1.20. `deepseek-v4-pro` (V4-Pro-0813, 1M ctx) cache hit $0.022 / $0.044, miss $0.66 / $1.32, output $1.98 / $3.96. Peak = 01:00-04:00 and 06:00-10:00 UTC Mon-Fri excl. Chinese holidays. Hit price is ~1/50 of miss price on Flash (0.003 vs 0.15) and ~1/30 on Pro. From 2026-11-18 12:00 Beijing time, server-side search/web-fetch calls are no longer billed separately, only tokens. [VENDOR] — [DeepSeek pricing](https://api-docs.deepseek.com/quick_start/pricing)
- Note for cost code: DeepSeek has time-of-day (peak/off-peak) pricing, so a cost tracker needs time-aware price tables. LiteLLM's cost docs list "off-peak pricing" among custom-pricing features. [VENDOR] — [LiteLLM cost tracking](https://docs.litellm.ai/docs/proxy/cost_tracking)

**Z.ai (GLM)**
- Automatic (implicit) context caching, no manual config; no numeric TTL ("reasonable time limits"); no minimum stated; cache hit billed at a discount, "usually 50%" per the caching page; usage field `usage.prompt_tokens_details.cached_tokens`. [VENDOR] — [Z.ai cache guide](https://docs.z.ai/guides/capabilities/cache)
- Pricing page: GLM-5.3 input $1.40, cached $0.26, output $4.40; GLM-5.3-Flash $0.15 / cached $0.03 / $0.50; GLM-5.3-FlashX $0.37 / $0.075 / $1.25 per 1M; cached-input storage "limited-time free". The effective hit discount (~81-80%) is larger than the "usually 50%" figure on the caching guide — the two Z.ai pages are inconsistent; trust the price table. [VENDOR] — [Z.ai pricing](https://docs.z.ai/guides/overview/pricing)
- OpenRouter summarizes Z.ai as automatic, writes free, reads about 0.2x input. [VENDOR/aggregator] — [OpenRouter prompt caching](https://openrouter.ai/docs/guides/best-practices/prompt-caching)

**Moonshot / Kimi**
- Kimi API automatically enables context caching billing for repeated request prefixes; default TTL 5 minutes; K3 series (kimi-k3, kimi-k3.1-pro) 1,048,576-token context, K2 series 262,144; K3 batch is 60% of standard price. The page text was ambiguous on whether K3 cache writes are billed by TTL (5 min / 1 h) — unclear. Per-1M prices were not captured (tables empty in the fetch). [VENDOR] — [Kimi pricing](https://platform.kimi.ai/docs/pricing/chat)
- OpenRouter summary: Moonshot automatic, writes free, reads 0.25x input. [VENDOR/aggregator] — [OpenRouter prompt caching](https://openrouter.ai/docs/guides/best-practices/prompt-caching)

**Alibaba Qwen (Model Studio)**
- Two mutually exclusive modes. Explicit: manual `cache_control: {"type":"ephemeral"}`, min 1,024 tokens, creation ~125% of input price, hit ~10%, TTL 5 min reset on each hit, deterministic within TTL, up to 4 markers, 20-block lookback. Implicit: automatic, cannot be disabled, min 1,024 tokens (512 for Zhipu-deployed GLM), creation 100%, hit typically 20%, TTL indeterminate, not guaranteed. Several newer models (qwen4-max, qwen3.8-max, qwen3.8-flash...) deviate from these ratios; deepseek-v4-pro-0813 hosted on Model Studio uses 10% implicit. Usage fields: `prompt_tokens_details.cached_tokens` and `cache_creation_input_tokens` (OpenAI-compatible; cached tokens included in `prompt_tokens`); Anthropic-compatible endpoint reports `cache_read_input_tokens` separately from `input_tokens`. [VENDOR] — [Alibaba Model Studio context cache](https://www.alibabacloud.com/help/en/model-studio/context-cache)

**OpenAI**
- Automatic caching on by default. Older models: minimum depends on request settings (about 1,024 visible tokens classically); `prompt_cache_key` helps route (aim ~15 req/min per key; more traffic should be partitioned); retention `in_memory` (~5-10 min idle, up to 1 h) or `24h`. GPT-5.6+: 1,024 visible input tokens minimum; optional explicit breakpoints (`prompt_cache_options.mode: "explicit"`); TTL `30m` default or `12h` (Responses API only); cache reads 0.1x input (0.05x some models); writes 1.25x (30 min) or 2.5x (12 h); usage fields `input_tokens_details.cached_tokens`, `cache_write_tokens`. Docs say "discounted up to 95%"; cache-hit rates in examples (70%, >90%) are illustrative. Prefix guidance: static instructions and reference first, dynamic content (timestamps, user data) last; append, don't rewrite; keep tool definitions identical (use `tool_choice: none`/`allowed_tools` instead of removing tools); "summarization, compaction, or truncation can reset reuse". [VENDOR] — [OpenAI prompt caching](https://developers.openai.com/api/docs/guides/prompt-caching)
- OpenRouter lists reads as 0.25x or 0.5x for pre-5.6 models and writes free pre-5.6. [VENDOR/aggregator] — [OpenRouter prompt caching](https://openrouter.ai/docs/guides/best-practices/prompt-caching)

**Anthropic**
- Two modes: automatic (single top-level `cache_control`, breakpoint moves forward as conversation grows; not supported on Bedrock) and explicit (up to 4 block-level breakpoints). TTL 5 min default (refreshed free on each hit; clock starts when request begins) or 1 h (`ttl: "1h"`; 1 h entries must precede 5 min entries). Multipliers: 5 min write 1.25x, 1 h write 2x, read 0.1x (0.05x for Opus 5.5 and Sonnet 5.5; 0.025x for Fable/Mythos 5.x). Minimum cacheable length 512 tokens (Opus 5.5, Opus 5, Sonnet 5.5, Fable 5, Haiku 5.5), 1,024 (Sonnet 5, 4.6, 4.5, Opus 4.8), 2,048 (Opus 4.7), 4,096 (Opus 4.6/4.5, Haiku 4.5); shorter prompts silently uncached. Hierarchy tools -> system -> messages; changing a level invalidates it and everything after. Changing tool definitions invalidates all; toggling web search/citations, speed setting, `tool_choice`, adding/removing images, and thinking/effort config invalidate parts. Reads look back up to 20 blocks. Usage: `total_input = cache_read_input_tokens + cache_creation_input_tokens + input_tokens` (three disjoint buckets). A timestamp or per-request message inside the prefix means "every request pays a write without getting a read". Entries only become available after the first response starts (do not fire parallel requests expecting a hit). `max_tokens: 0` pre-warms. [VENDOR] — [Anthropic prompt caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)

**Google Gemini**
- Implicit caching on by default for Gemini 2.5 and newer; explicit cache objects only on generateContent for Gemini 3/2.5 (not Gemini 4, not Interactions API). Min tokens for implicit: 4,096 for Gemini 4 and 3.x models listed, 2,048 for 2.5 Flash/Pro. Gemini 4 multi-turn: full prior request is cached only if the new request adds at least 2,050 tokens, otherwise last 2,050 tokens are reprocessed at full price. Hits reported in `usage.total_cached_tokens`. Discount/storage/TTL not on that page. [VENDOR] — [Google AI Studio caching docs](https://aistudio.google.com/docs/caching)
- OpenRouter: Gemini implicit has no write/storage fee, reads 0.25x; implicit TTL about 3-5 min; explicit writes fixed 5 min TTL; minimums 1,024 (2.5 Flash) / 4,096 (2.5 Pro) per that page (conflicts with Google's page above on the minimums — newer Google page wins). [VENDOR/aggregator] — [OpenRouter prompt caching](https://openrouter.ai/docs/guides/best-practices/prompt-caching)

**Prompt-structure rules (from Manus, with vendor corroboration)**
- Manus: KV-cache hit rate is "the single most important metric" for a production agent; ~100:1 input-to-output token ratio; cached vs uncached Claude Sonnet input $0.30 vs $3 per MTok. Rules: stable prefix (a precise timestamp at the start of the system prompt is a classic mistake), append-only context (never modify earlier actions/observations), deterministic serialization (JSON key order can silently break caching), explicit breakpoints where needed (at least end of system prompt). Don't add/remove tools mid-task (invalidates cache and confuses the model about earlier turns); instead mask logits / restrict via consistent tool-name prefixes. [VENDOR/practitioner, not independent] — [Manus context engineering blog](https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus)
- OpenAI says the same: keep tool definitions consistent, append don't rewrite, compaction/summarization/truncation can reset reuse. [VENDOR] — [OpenAI prompt caching](https://developers.openai.com/api/docs/guides/prompt-caching)

**Routing / session affinity**
- OpenRouter sticky routing: after a cached request, follow-ups for the same model route to the same provider while the cache read is cheaper than regular input; keyed by hash of first system/developer message + first non-system message by default, or by `session_id` / `x-session-id` header (up to 256 chars); expires after 60 min inactivity; skipped when `provider.order` is set. For Z.ai OpenRouter sends a session affinity key derived from `session_id`. Usage fields: `prompt_tokens_details.cached_tokens`, `cache_write_tokens`, `cache_discount`. [VENDOR] — [OpenRouter prompt caching](https://openrouter.ai/docs/guides/best-practices/prompt-caching)

### Inferences
- With DeepSeek Flash, a prefix-stable 100k-token chat turn costs about $0.0003 (cache hit, off-peak) vs $0.015 (miss), so cache discipline matters more than any summarization trick for cheap models; ~50x swing per prompt. (Arithmetic from DeepSeek's price table.)
- Summarization/compaction is not "free savings" under caching: it rewrites the prefix and forces a full-price miss on the next turn (OpenAI and Manus both warn about this). Compaction should therefore happen rarely, in big steps (e.g., at 60-80% of window), and ideally be re-cached immediately; per-turn tool-result masking should be done in a way that only edits tail-end content or a pre-planned boundary.
- Cache hit-rate and TTL behaviors differ a lot: DeepSeek (hours-days, best effort) and Kimi (5 min default) vs Anthropic (5 min/1 h). A workspace used by one human with pauses > 5 min between turns will lose Anthropic/Qwen-explicit/Kimi caches unless 1 h TTL or re-warming is used; DeepSeek's long TTL is much friendlier to single-user "come back later" sessions.
- Model switching mid-conversation resets the cache because caches are per-provider/per-model (no source states otherwise); a workspace should treat model switch as a cost event and warn the user.
- A cost tracker must treat three usage conventions: OpenAI-style (cached tokens included in prompt_tokens), Anthropic-style (three disjoint buckets), and Langfuse's exclusive buckets (see section 6).

### Gaps
- Exact minimum prefix for DeepSeek, Z.ai, Kimi not stated on their pages (DeepSeek: "not specified" on the KV-cache page; community commonly cites 64-token granularity but I did not verify).
- Kimi per-1M prices (hit/miss/output) not captured; Z.ai TTL not numeric; Gemini discount percentages/TTL not on Google page fetched.
- No independent measurement of real-world cache hit rates on DeepSeek/GLM/Kimi found.

---

## 2. Compaction, summarization, observation masking, context editing, sub-agents, retrieval

### Takeaway
Best-supported cheap technique: mask/clear old tool results while keeping the agent's reasoning and actions (JetBrains/TUM: about half the cost, solve rate equal to or better than LLM summarization). Anthropic ships this as "context editing" and reports vendor-measured gains. LLM-summary compaction works but is costlier, can elongate trajectories, and breaks caches. Sub-agent isolation trades ~15x tokens for quality on research tasks. Context rot is real and measured independently (Chroma), which is the reason to keep context small even when the window is 1M.

### Cited Findings

**Context rot / lost in the middle (the problem)**
- Chroma "Context Rot" (July 2025): 18 LLMs (Claude, GPT-4.1/o3, Gemini 2.5, Qwen3) all got worse as input length grew even on simple tasks; one distractor hurt, four hurt more; shuffled haystacks beat coherent ones; on LongMemEval, ~113k-token full prompts vs ~300-token focused prompts: all models did significantly better with focused prompts; needle position had no notable effect in their NIAH tests. Chroma sells a vector DB (potential bias toward retrieval), but methodology is public. [3P/independent-ish] — [Chroma context rot](https://www.trychroma.com/research/context-rot)
- Liu et al. "Lost in the Middle": accuracy is U-shaped in position of relevant info; highest at start or end, drops in the middle, even for long-context models. Note the 2023-era models; Chroma's finding of no position effect on simple NIAH suggests the effect varies by task/model. [PEER/PAPER] — [arXiv 2307.03172](https://arxiv.org/abs/2307.03172)
- Anthropic: context rot — recall decreases as context grows, gradual, across models; context is a finite "attention budget"; aim for the smallest set of high-signal tokens. [VENDOR] — [Anthropic effective context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)

**Observation masking vs summarization (independent evidence)**
- "The Complexity Trap" (JetBrains Research + TUM; NeurIPS 2025 workshop; arXiv 2508.21433), SWE-agent on SWE-bench Verified: simple observation masking (hide old tool outputs with placeholder, keep reasoning/actions) was about half the cost of the raw agent (e.g., Qwen3-Coder 480B ~52% cheaper, solve rate +2.6%); LLM summarization could not consistently or significantly outperform masking across configurations; masking saved ~$0.03/instance (~$15 per 500) vs summarization; a hybrid cut cost a further 7% vs masking and 11% vs summarization. Caveats: heuristic triggers; one scaffold/benchmark (initial evidence on OpenHands). I could not fetch the JetBrains blog (403); figures are from a search summary of the arXiv paper — verify exact numbers in the arXiv v3 before quoting. [PEER/PAPER] — [arXiv 2508.21433](https://arxiv.org/pdf/2508.21433)
- Manus: compression should be reversible — drop page content but keep URL, drop document but keep path; use the file system as unlimited external memory; keep failed actions in context so the model updates beliefs; maintain a todo.md "recitation" to keep objectives near the end of context (typical task ~50 tool calls); add controlled variation to avoid few-shot ruts. [VENDOR/practitioner] — [Manus blog](https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus)

**ACON (learned compression guidelines)**
- ACON (Microsoft; arXiv 2510.00615; listed at ICML 2026 PMLR 306, venue not verified): optimizes natural-language compression guidelines for observations and histories using failure analysis; reports 26-54% peak-token reduction on AppWorld, OfficeBench, multi-objective QA while mostly keeping performance; compressor distillable into smaller models keeping >95% accuracy; code at github.com/microsoft/acon. [PEER/PAPER, authors' numbers] — [arXiv 2510.00615](https://arxiv.org/abs/2510.00615v2) (via search summary; paper not read in full)

**Anthropic context editing / memory tool / compaction / sub-agents**
- Context editing automatically clears stale tool calls/results near token limits, keeping conversation flow; memory tool is a client-side file-based store (create/read/update/delete files in a memory directory); internal agentic-search eval: memory tool + context editing +39% vs baseline, context editing alone +29%; in a 100-turn web-search eval, context editing cut token consumption 84% and let workflows finish that otherwise failed on context exhaustion. Setup details not published → vendor claim, treat as directional. [VENDOR] — [Anthropic context management announcement](https://claude.com/blog/context-management)
- Anthropic guidance: compaction = summarize near-full context and restart (Claude Code keeps the summary plus the five most recently accessed files); tool-result clearing is "one of the safest lightest touch forms of compaction"; structured note-taking to external memory; sub-agents use tens of thousands of tokens but return ~1,000-2,000-token summaries; just-in-time retrieval (keep paths/links, load on demand; Claude Code loads CLAUDE.md up front and uses glob/grep for the rest); hybrid retrieval for less dynamic domains. [VENDOR] — [Anthropic effective context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- Anthropic multi-agent research: agents use ~4x the tokens of chat, multi-agent ~15x; token usage alone explains 80% of performance variance in their browsing eval; orchestrator-worker (Opus 4 lead + Sonnet 4 subagents) beat single-agent Opus 4 by 90.2% on their internal research eval. The "$1 chat becomes $15" dollar illustration is from a third-party write-up, not Anthropic. [VENDOR for ratios; 3P for dollar example] — [Anthropic multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system), [search summary listing](https://www.anthropic.com/news/multi-agent-research-system)
- Claude Code auto-compact trigger: third-party and issue-tracker sources conflict (64-75%, ~80%/160k, ~83.5%, ~967K on 1M model, and a reported ~420K on Opus 1M); manual `/compact` accepts focus instructions, auto-compact does not; CLAUDE.md survives compaction; `/context` shows "context left until auto-compact"; a community env var `CLAUDE_CODE_AUTO_COMPACT_WINDOW` is mentioned. All unverified against official docs. [3P, unverified] — [GitHub issue 40757 listing](https://claudeissues.com/issue/40757-auto-compact-triggers-at-420k-tokens-despite-opus-having-1m-context-window-thres), [Context compaction deep dive](https://codex.danielvaughan.com/2026/04/14/context-compaction-deep-dive-codex-cli-claude-code-opencode/)

### Inferences
- Recommended escalation ladder for the workspace (cheap to expensive): (1) stable-prefix + append-only; (2) mask/clear old tool outputs and large attachments with reversible stubs (path/URL/message-id) — evidence-backed and cheap; (3) only then checkpoint compaction (LLM summary) at a high threshold, producing a new stable prefix; (4) offload to memory/files and retrieval. Reasoning from JetBrains + Anthropic + Manus + OpenAI cache warnings.
- Because DeepSeek-class cache hits cost ~2% of misses, aggressive early compaction can cost more than it saves on cheap cached models; compaction pays off mainly for quality (context rot), the window limit, or for frontier models with expensive reads. This is my inference; no source measured compaction ROI under cache pricing.
- Show the user "what is about to be dropped" before compaction and let them pin items — consistent with Anthropic's "tune for recall first" advice, but this UI pattern is my suggestion.

### Gaps
- No independent, controlled study of observation masking on chat (non-coding) workloads; JetBrains is SWE-agent only.
- Could not fetch JetBrains blog (HTTP 403); exact figures taken from search summary of arXiv paper.
- No source quantifying cache-hit loss from compaction/masking.
- LibreChat's own compaction/summarization implementation not verified in this pass.

---

## 3. Long context vs RAG with 1M-token models at cheap prices

### Takeaway
Long context often wins on raw accuracy for small/medium corpora but costs far more per query even with caching; RAG is 5-26x cheaper per query in the studies found; consensus is hybrid/routed. With DeepSeek-style ~$0.003-0.006/M cache hits, stuffing a stable 200k project into a cached prefix is economically viable, but cache TTL/miss risk and context rot remain.

### Cited Findings
- "The Token Tax of Epistemic Accuracy" (arXiv 2606.20898, June 2026): 972 answers, manufacturing-safety domain, two small LLMs: long-context prompting 73.1% correctness vs 65.4% semantic RAG, but ~26x cost per query (~$0.118 vs ~$0.0045). Small, narrow study. [PEER/PAPER] — [arXiv 2606.20898](https://arxiv.org/pdf/2606.20898)
- Secondary analysis (Oct 2026, Preview-model prices, provisional): with caching, a 400K-token long-context answer on Claude Sonnet 5.5 cost $0.085 vs $0.017 for RAG (5x). [3P] — [beri.net](https://www.beri.net/article/long-context-vs-rag-cost-prompt-caching-crossover-2026)
- Search summary: Google's "Self-Route" (route between RAG and long context) cut computation cost while keeping most of long-context accuracy; consensus of 2026 commentary favors hybrid. [3P] — [intuitionlabs](https://intuitionlabs.ai/articles/long-context-ai-vs-retrieval-rag)
- Context rot evidence above (Chroma; Anthropic) argues against filling the window even when it is available.
- Memory-vs-full-context (conversational): LongMemEval full-context vs fact-memory — long-context GPT-5-mini had higher recall on LongMemEval and LoCoMo; memory is cheaper after ~10 interaction turns at 100k context (break-even falls as context grows). [PEER/PAPER, Mem0-framework-based] — [arXiv 2603.04814](https://arxiv.org/abs/2603.04814)

### Inferences
- For a single-user workspace: put the stable project instructions + small files fully in the cached prefix; for large file sets use retrieval (top-k chunks appended late in the prompt so they don't break the prefix), with an "expand to full document" option. Routing heuristic by corpus size is my inference, based on the 5-26x cost ratios.
- RAG chunks injected mid-prefix change per query and destroy caching of everything after them; place retrieved chunks at the end of the prompt (after stable history) or as a tool result — inference from the prefix rules in section 1.

### Gaps
- No independent 2026 benchmark of 1M-context cheap Chinese models (DeepSeek V4, Kimi K3) on long-context accuracy at 500k-1M found.
- Cost ratios come from small studies with other models; not reproduced with DeepSeek cache pricing.

---

## 4. Memory systems (Mem0, Letta, Zep/Graphiti, Cognee, LangMem, Supermemory, LibreChat, ChatGPT/Claude)

### Takeaway
Memory benchmarks (LoCoMo, LongMemEval) are heavily self-reported and disputed; full-context baselines are often as good or better on accuracy, with memory winning mainly on cost/latency over many turns. For a single user, a small curated key/value or markdown-file memory (LibreChat/Claude style) plus agentic search over files is the pragmatic option; graph/temporal systems (Graphiti) are only worth it when facts change over time and you accept a graph DB and structured-output LLM requirements.

### Cited Findings

**Systems: license, self-hosting, claims**
- Mem0: Apache-2.0; Docker self-host (`make bootstrap` in `server`), auth on by default; defaults to OpenAI gpt-5-mini + text-embedding-3-small (other LLMs supported); optional spaCy NLP extra for BM25/entity extraction. README claims (April 2026 algorithm, from Mem0's managed platform "with proprietary optimizations"; OSS "similar but not identical"): LoCoMo 92.5 (from 71.4), LongMemEval 94.4 (from 67.8), BEAM 1M 64.1, ~7K tokens per query, p50 ~0.9-1.1s. [VENDOR, SELF-REPORTED] — [mem0 GitHub](https://github.com/mem0ai/mem0)
- Zep/Graphiti: Graphiti Apache-2.0; temporal knowledge graph (facts have validity windows, superseded not deleted; episodes with provenance; hybrid semantic+BM25+graph retrieval); needs Neo4j 5.26, FalkorDB 1.1.2 or Neptune; defaults to OpenAI; "works best with LLM services that support structured output"; smaller/local models may cause schema-mismatch ingestion failures. [VENDOR] — [Graphiti GitHub](https://github.com/getzep/graphiti)
- Letta: Apache-2.0; self-host via `letta server`; page fetched did not describe memory architecture (core blocks/archival/sleep-time) — not verified here. [VENDOR] — [Letta GitHub](https://github.com/letta-ai/letta)
- Letta's filesystem experiment: LoCoMo conversation stored in one file, agent with grep/search_files/open/close tools on GPT-4o mini scored 74.0% vs Mem0's reported 68.5% (graph variant); Letta attributes it to agents' skill at tool use, and cautions LoCoMo may be a weak memory measure. Letta is a competitor; Mem0 has since rewritten its pipeline (92.5% claim), and Letta has not rerun. [SELF-REPORTED, competitor] — [Letta blog](https://www.letta.com/blog/benchmarking-ai-agent-memory); critique via [search summary / Aktagon](https://signals.aktagon.com/articles/2026/02/benchmarking-ai-agent-memory-is-a-filesystem-all-you-need/)
- Cognee: described as open-source graph-native memory; license not clearly stated in sources found; its headline benchmark (Jan 2026) ran Cognee tuned vs competitors on defaults (uneven). LangMem: library tied to LangGraph storage, one source says MIT (ambiguous). Supermemory: sources disagree — core closed source with MIT dev tooling vs MIT with self-host on top tier. All via competitor/aggregator posts. [3P, weak] — [Cognee guide](https://www.cognee.ai/blog/guides/open-source-memory-frameworks-llm-agents), [vectorize.io Mem0 vs Supermemory](https://vectorize.io/articles/mem0-vs-supermemory)
- LibreChat memory: key/value facts injected into every new message (not search over chat history); model gets `set_memory`/`delete_memory` tools; Memories side panel for user edits; config keys `tokenLimit` (total per user, default none), `charLimit` (per entry, default 10000), `messageWindowSize` (default 5, for the optional background agent), `validKeys`, optional `agent` with own provider/model; background agent runs alongside the chat request, gets until main response ends plus up to 3 s, late results are dropped. [VENDOR] — [LibreChat memory](https://www.librechat.ai/docs/features/memory), [LibreChat memory config](https://www.librechat.ai/docs/configuration/librechat_yaml/object_structure/memory)

**Benchmark disputes and independent evidence**
- Zep vs Mem0 LoCoMo dispute: Zep says Mem0 misimplemented Zep and that corrected Zep scores 75.14% (+/-0.17), about 10 points above Mem0; Mem0 says Zep included the adversarial category (non-standard; standard practice is categories 1-4) and re-scored Zep at 58.44%; Zep's original claim was 84%. Unresolved; both parties are vendors. [SELF-REPORTED both sides] — [Zep rebuttal](https://blog.getzep.com/lies-damn-lies-statistics-is-mem0-really-sota-in-agent-memory/) (as summarized by search; page not fetched)
- EngramaBench (Apr 2026): GPT-4o full-context highest composite (0.6186); only a graph-structured memory beat it, and only on cross-space reasoning; Mem0 was cheapest but clearly weaker. [PEER/PAPER, per search summary] — [alphaxiv 2604.21229](https://www.alphaxiv.org/abs/2604.21229.md)
- MemDelta (Jul 2026): verbatim RAG ~ full-context GPT-4o-mini (47.2% vs 49.8%, p=0.34); ranking reverses across models. [PEER/PAPER, per search summary] — [benchmarklist MemDelta](https://benchmarklist.com/benchmarks/memdelta/)
- A June 2026 independent-researcher paper reports retrieval-based memory 83.6% vs full-context 73.2% on LongMemEval_S with ~8x fewer tokens (hybrid read path required; single self-reported run). [PEER/PAPER, self-reported] — [alphaxiv 2606.09900](https://www.alphaxiv.org/abs/2606.09900v1)
- Mem0-framework paper (arXiv 2603.04814): long-context GPT-5-mini > fact-memory on LongMemEval/LoCoMo recall; memory cheaper after ~10 turns at 100k. A review flagged a ~45-point gap between Mem0's self-report and an independent replication of its older algorithm (attributed to that arXiv paper; I could not verify the 45-point figure directly). [PEER/PAPER; criticism via 3P] — [arXiv 2603.04814](https://arxiv.org/abs/2603.04814)
- LongMemEval itself: Chroma's run showed focused ~300-token prompts beating ~113k full prompts on all 18 models — i.e., good retrieval > stuffing. [3P] — [Chroma](https://www.trychroma.com/research/context-rot)
- Critique that LoCoMo does not score knowledge updates and that the benchmark's adversarial category handling makes numbers non-comparable. [3P] — [Aktagon summary](https://signals.aktagon.com/articles/2026/02/benchmarking-ai-agent-memory-is-a-filesystem-all-you-need/), [DEV: benchmark forbids "I don't know"](https://dev.to/gde03/the-ai-memory-benchmark-everyone-quotes-forbids-saying-i-dont-know-o1n)

**Anthropic memory tool**
- Client-side file-based memory directory the model reads/writes via tool calls; developer controls storage. [VENDOR] — [Anthropic context management](https://claude.com/blog/context-management)

### Inferences
- Practical single-user design (lower priority per the brief): (a) small always-injected "core memory" of curated facts (LibreChat-style key/value with a hard token cap; place at the end of the system block or in a stable block that changes rarely to protect the cache); (b) per-project/notes as files searchable by an agentic grep/vector tool (Letta/Anthropic memory-tool pattern); (c) optional nightly/background extraction job rather than per-turn extraction, to keep cost and cache impact low. Reasoning from the evidence above; no source tested this exact combo.
- Per-turn memory edits to the system prompt invalidate the cache on every change; batch memory updates between sessions or inject memory as a late message instead.
- Avoid Graphiti unless you need temporal reasoning: needs a graph DB plus a structured-output-capable LLM for ingestion; small cheap local models can fail ingestion (Graphiti README). Cheap Chinese models with JSON-schema support may work but I found no test.
- Don't pick on benchmark numbers: every headline number is vendor self-reported and methodologies conflict.

### Gaps
- Did not verify Letta's core/archival memory blocks and sleep-time compute docs, nor Cognee/LangMem/Supermemory licenses from primary repos.
- Zep rebuttal and Mem0 GitHub Issue #5 not read directly; ChatGPT/Claude consumer-memory design (e.g., summaries vs retrieval) not researched in this pass.
- No independent test of these memory frameworks with DeepSeek/Qwen/GLM as the extraction LLM.

---

## 5. Projects (persistent instructions + files): RAG, vector stores, embeddings

### Takeaway
Evidence gathered here is thin for vector-store comparisons; embedding-model guidance is mostly vendor/blog-level. BGE-M3 (MIT, hybrid dense+sparse+multi-vector, ~4 GB VRAM) and Qwen3-Embedding (0.6B small / 8B top open model) are the common self-hosted picks; verify with your own retrieval eval, particularly for Chinese/multilingual.

### Cited Findings
- Qwen3-Embedding-8B reported as leading open-weights on multilingual MTEB (70.58; vendor claim repeated across blogs), needs ~16.4 GB VRAM at FP16; Qwen3-Embedding-0.6B scores 64.33 on a MTEB-v2 average at ~1.4 GB VRAM; BGE-M3 MIT-licensed, outputs dense, sparse and ColBERT-style vectors in one pass, runs on ~4 GB VRAM, scores vary by source (63.0 vs 59.84); nomic-embed-text-v1.5 suggested for CPU-only. Sources advise running your own retrieval eval; English MTEB rank can mislead for non-English retrieval. [3P] — [premai embedding ranking](https://blog.premai.io/best-embedding-models-for-rag-2026-ranked-by-mteb-score-cost-and-self-hosting), [fast.io](https://fast.io/resources/best-embedding-models-for-rag-agents/)
- Mem0's README recommends a Qwen ~600M embedding model (or comparable) for best hybrid search. [VENDOR] — [mem0 GitHub](https://github.com/mem0ai/mem0)
- Anthropic's pattern for projects/code: load small instruction files up front (CLAUDE.md), retrieve everything else just-in-time via lightweight identifiers. [VENDOR] — [Anthropic context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)

### Inferences
- Pattern: project = (stable system instructions + pinned small files in the cached prefix) + (indexed larger files retrievable via a tool call). Use hybrid (BM25 + dense) retrieval; BM25 gets you far with zero embedding cost. Source for hybrid benefit: Graphiti/Mem0 both ship hybrid retrieval; I did not find an independent study of hybrid vs dense for personal project corpora.
- For a single user, SQLite/pgvector or LanceDB (embedded) are likely sufficient; no sources on scale limits were found, so this is an inference.

### Gaps
- No credible comparison of pgvector vs Qdrant vs LanceDB vs Chroma found (search returned only embedding-model articles).
- No hosted-embedding price table captured (e.g., OpenAI text-embedding-3-small, Qwen/DashScope text-embedding) — need a separate fetch.
- Chunking/reranking evidence not gathered.

---

## 6. Cost tracking and display (Claude, ChatGPT, OpenRouter, TypingMind, LibreChat; LiteLLM, Langfuse, Helicone, OpenLIT, tokencost; cache-aware cost, budgets, pre-run estimates)

### Takeaway
LibreChat already has the key UI pieces (context-usage gauge, optional cost display, transactions, balances). LiteLLM proxy gives per-key/user/team/tag spend, per-response cost header and budgets; Langfuse stores usage buckets and prices them per usage type (cache read/write separate). The hard part is cache-aware arithmetic: normalize each provider's usage convention and price with a versioned price table that includes time-of-day tiers.

### Cited Findings

**LibreChat (open-source UI)**
- Newer releases: a context gauge (prompt/context usage vs model window, hover summary, click-through breakdown of prompt, completion, cached tokens, branch and conversation totals) controlled by `contextUsage`; `contextCost` (default false) shows cost values; token transactions stored in a Transactions collection (`transactions.enabled`), separate from balance enforcement; `balance` object in librechat.yaml enforces credits (1000 credits = $0.001); per-model rates for custom endpoints via `endpoints.custom[].tokenConfig` with context windows and per-million rates; `currency` static multiplier. An older `balance.tokenCosts` per-1K example only appears on a third-party mirror — don't trust. [VENDOR docs, per search results] — [LibreChat token usage](https://librechat.ai/docs/configuration/token_usage), [transactions config](https://www.librechat.ai/zh/docs/configuration/librechat_yaml/object_structure/transactions), [balance config](https://www.librechat.ai/tr/docs/configuration/librechat_yaml/object_structure/balance)

**LiteLLM**
- Tracks spend per key, user, team and tags (`metadata`, `x-litellm-tags` header); `x-litellm-response-cost` header per call; `max_budget` + `budget_duration` per key/team, `model_max_budget`; custom pricing, fee margins, provider discounts, off-peak pricing; spend logs in `LiteLLM_SpendLogs`, reports via `/global/spend/report`; zero-cost anomaly counter; warns fallback routes may not share one budget cleanly. The cost page doesn't cover cache-aware cost or alerting. [VENDOR] — [LiteLLM cost tracking](https://docs.litellm.ai/docs/proxy/cost_tracking)
- Prompt-caching page: normalizes to OpenAI-style usage where `prompt_tokens` includes cache-hit and miss, `prompt_tokens_details.cached_tokens` = hits, `cache_creation_input_tokens` Anthropic-only; `completion_cost()` prices cache reads/writes (incl. 12 h OpenAI tier via `cache_creation_input_token_cost_above_12hr`); caching silently skipped below provider minimum so check creation tokens; DeepSeek listed as working "same as OpenAI" with no DeepSeek-specific cost details; OpenRouter not mentioned there. [VENDOR] — [LiteLLM prompt caching](https://docs.litellm.ai/docs/completion/prompt_caching)

**Langfuse**
- Usage and cost can be ingested (ingested cost has priority) or inferred from usage + model definition (regex `match_pattern`, per-usage-type prices; tiers by usage/params/metadata); usage buckets must be disjoint (e.g., `input`, `input_cached_tokens`/`cache_read_input_tokens`, `output`); OpenAI-style inclusive counts must be converted to exclusive; costs computed at ingestion so later price changes don't rewrite history; Langfuse "no longer estimates token counts" from text — no usage, no cost. License not confirmed on that page. [VENDOR] — [Langfuse model usage and cost](https://langfuse.com/docs/model-usage-and-cost)

**tokencost**
- MIT Python lib, 400+ models, client-side counting (tiktoken; Anthropic token-count API for some Claude models; cl100k approximation for older Claude); page shows only prompt/completion prices — no cache pricing mentioned; ~2k stars. [VENDOR] — [tokencost GitHub](https://github.com/AgentOps-AI/tokencost)

**OpenRouter**
- Per-response usage with `cached_tokens`, `cache_write_tokens`, `cache_discount` (negative for Anthropic writes, positive for reads); viewable in Activity page and `/api/v1/generation`. [VENDOR] — [OpenRouter prompt caching](https://openrouter.ai/docs/guides/best-practices/prompt-caching)

**Deep-research cost estimation**
- Anthropic: agents ~4x, multi-agent ~15x chat tokens; token usage explains 80% of performance variance. Use as a multiplier prior for pre-run estimates, not a budget. [VENDOR] — [Anthropic multi-agent research](https://www.anthropic.com/engineering/multi-agent-research-system)

### Inferences
- Cache-aware cost formula to implement per call: `cost = miss_tokens*P_in + hit_tokens*P_hit + write_tokens*P_write + out_tokens*P_out`, with miss = prompt_tokens - cached (OpenAI/DeepSeek/Qwen-OpenAI convention) or `input_tokens` (Anthropic convention, disjoint buckets); price rows keyed by (provider, model, effective-from, peak/off-peak, cache TTL tier). Derived from the usage conventions documented above.
- Always use provider-returned usage for billing display; use local tokenizers only for pre-send estimates (see section 7). Langfuse's choice to stop estimating supports this.
- Pre-run estimator for deep research: estimate = (planned steps x average context size x (1-expected hit rate) x P_in) + hit portion + output tokens, then show a range using the 4x/15x priors plus a hard cap (LiteLLM `max_budget` per key/tag/session, plus a workspace-level kill switch). Design suggestion; no source validated an estimator's accuracy.
- Display recommendation: per-message "cost = $X (Y% cached, saved $Z)" with a running conversation total and a context gauge — mirrors LibreChat's click-through breakdown (prompt/completion/cached).

### Gaps
- Helicone and OpenLIT docs not fetched; TypingMind, ChatGPT-with-API, and Claude's own cost/usage UI behavior not verified (a `/cost` command exists in Claude Code but I could not verify details).
- Alerting configuration (LiteLLM, Langfuse) not read.
- LiteLLM's handling of DeepSeek peak/off-peak and of Qwen/GLM implicit-cache price ratios not verified — likely needs custom price overrides.

---

## 7. Token counting accuracy across Chinese-model tokenizers

### Takeaway
Don't use tiktoken as a proxy for DeepSeek/Qwen/GLM/Kimi: counts for Chinese text differ materially by tokenizer, and some vendors have no official client-side tokenizer. Use each model's Hugging Face tokenizer for pre-send estimates and always reconcile with the API's returned usage for billing.

### Cited Findings
- A Chinese-language benchmark table (labeled approximate): same Chinese passage ~165 tokens in cl100k_base vs ~92 for Qwen-2/3 and ~98 for DeepSeek-V3. [3P, weak] — [CSDN tokenizer article](https://adg.csdn.net/6a311f5810ee7a33f27df251.html)
- A dev.to test of billed input tokens on three aligned passages: Kimi K2.5 leanest on Chinese, DeepSeek-v4 and GLM-5.2 close behind; includes billing overhead so it doesn't isolate tokenizers. [3P] — [dev.to tokenizer cost test](https://dev.to/synthorai/which-llm-is-cheapest-for-your-language-tokenizer-costs-measured-1k5m)
- One counter tool states no official browser-side tokenizer exists for Anthropic, Google, DeepSeek, Qwen, Kimi, GLM or Llama (counts are estimates); DeepSeek token-counter guide says tiktoken estimates cause large discrepancies on multilingual text; guidance is to load the published HF tokenizer (`transformers`, `trust_remote_code=True` for DeepSeek). Alibaba's own Qwen token-counting doc sample loads `o200k_base` rather than a Qwen vocabulary — treat as approximate. [3P, weak] — [fast.io DeepSeek token counter](https://fast.io/resources/deepseek-token-counter/), [OpenReplay counter](https://openreplay.com/tools/llm-token-counter/), [Qwen token counting docs](https://docs.platform.qianwenai.com/developer-guides/run-and-scale/token-counting)
- tokencost uses tiktoken for strings and chat messages; the page doesn't say how non-OpenAI providers are counted. [VENDOR] — [tokencost](https://github.com/AgentOps-AI/tokencost)
- Anthropic and OpenAI usage fields are authoritative for cache accounting (see section 1); Langfuse refuses to infer tokens from text. [VENDOR] — [Langfuse](https://langfuse.com/docs/model-usage-and-cost)

### Inferences
- Pre-send estimator: per-model HF tokenizer (cached locally), with a +-10-15% band displayed as "~" until the response returns real usage; fall back to chars/3 style heuristics for unknown models (heuristic—no source validated the band). After response, replace with the provider usage numbers.
- Tool/system-prompt overhead, chat templates and hidden reasoning tokens are not in the visible text count; this explains estimate-vs-bill gaps (inference).

### Gaps
- No authoritative, reproducible benchmark of tokens-per-character for Chinese vs English across DeepSeek V4, Qwen 3.x, GLM-5.x, Kimi K3 tokenizers; all numbers above are from low-quality sources.
- Whether providers expose token-count endpoints (as Anthropic does) was not verified for DeepSeek/Z.ai/Moonshot.

---

## Usable open-source components (shortlist from findings)

| Need | Component | License / note | Source |
|---|---|---|---|
| Chat UI with context gauge, cost display, transactions, balances, memory | LibreChat | memory, `contextUsage`/`contextCost`, transactions/balance config documented (license not checked) | [LibreChat docs](https://librechat.ai/docs/configuration/token_usage) |
| Spend tracking, budgets, per-key/user/team/tag, cost header | LiteLLM proxy | docs verified; license not checked in this pass | [LiteLLM](https://docs.litellm.ai/docs/proxy/cost_tracking) |
| Observability with cache-aware usage buckets and price tables | Langfuse | self-hostable; license not confirmed on fetched page | [Langfuse](https://langfuse.com/docs/model-usage-and-cost) |
| Client-side cost estimation | tokencost | MIT; no cache pricing; tiktoken-based | [tokencost](https://github.com/AgentOps-AI/tokencost) |
| Fact memory layer | Mem0 | Apache-2.0, Docker self-host | [mem0](https://github.com/mem0ai/mem0) |
| Temporal knowledge-graph memory | Graphiti | Apache-2.0; needs Neo4j/FalkorDB/Neptune | [Graphiti](https://github.com/getzep/graphiti) |
| Stateful agents with memory | Letta | Apache-2.0 | [Letta](https://github.com/letta-ai/letta) |
| Learned context compression research code | ACON | Microsoft repo (license not checked) | [arXiv 2510.00615](https://arxiv.org/abs/2510.00615v2) |
| Embeddings (self-hosted) | BGE-M3 (MIT), Qwen3-Embedding 0.6B/8B | per 3P roundups | [premai](https://blog.premai.io/best-embedding-models-for-rag-2026-ranked-by-mteb-score-cost-and-self-hosting) |

Not covered (no data gathered): Helicone, OpenLIT, TypingMind, Open WebUI, Supermemory/Cognee/LangMem primary repos, vector DB benchmarks.
