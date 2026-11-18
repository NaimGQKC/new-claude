# Automatic model routing, "think harder" controls, reasoning display and senior-friendly UX (as of 2026-11-18)

Scope: design basis for a LibreChat (MIT) + LiteLLM workspace serving only EU-hosted open-weight models (e.g. DeepSeek V4.1 Flash = fast, Kimi K3.1 Pro = strong), for non-technical users of around 50 and older. Vendor claims are marked **[vendor claim]**. Most docs pages were read through a summarising fetch tool, so check exact field names against the live docs before shipping.

## 1. Precedents: how ChatGPT, Claude, Gemini, Perplexity and Le Chat choose models and show thinking, and what users thought

### Takeaway
The big consumer products have all moved to automatic selection with a small escape hatch: Auto plus a Fast/Thinking choice, or a "Think" toggle. GPT-5's August 2025 launch is the cautionary tale. When the router failed or felt opaque, users read it as the product getting worse or cutting costs. OpenAI responded by showing which model answered and by bringing back manual modes. Lesson: route automatically, but be transparent and give one simple "think harder" override.

### Cited Findings
**OpenAI / ChatGPT (GPT-5 router)**
- The GPT-5 system card describes "a unified system" with a fast model for most questions, a deeper reasoning model (gpt-5-thinking) for harder ones, and "a real-time router" that decides based on conversation type, complexity, tool needs and explicit user intent (e.g. a user asking it to "think hard") **[vendor claim]**. — [OpenAI GPT-5 system card](https://openai.com/index/gpt-5-system-card); [arXiv copy 2601.03267](https://arxiv.org/html/2601.03267v1)
- A claim that the router is "continuously trained on real signals, including when users switch models, preference rates for responses, and measured correctness" turned up only on a secondary aggregator page. It is unverified against the original card. — [catalyzex](https://www.catalyzex.com/paper/openai-gpt-5-system-card)
- At launch, Altman said the "autoswitcher" was broken for part of the day, so GPT-5 "seemed way dumber". OpenAI then tweaked selection, promised more transparency about which model answers, restored GPT-4o for paid users and raised rate limits. — [VentureBeat](https://venturebeat.com/ai/openai-returns-old-models-to-chatgpt-as-sam-altman-admits-bumpy-gpt-5-rollout); [BankInfoSecurity](https://www.bankinfosecurity.com/gpt-5-launch-meets-praise-user-pushback-price-wars-a-29175)
- ChatGPT then added user-selectable "Auto", "Fast" and "Thinking" settings for GPT-5, announced by Altman on X. (Seen in search-result summaries of press coverage; the original X post was not opened.) — [AINews](https://www.ainews.com/p/sam-altman-addresses-gpt-5-rollout-issues-brings-back-gpt-4o-for-users); [VentureBeat](https://venturebeat.com/ai/openai-returns-old-models-to-chatgpt-as-sam-altman-admits-bumpy-gpt-5-rollout)
- Fortune on the backlash:
  - Many users did not realise GPT-5 was several models behind a router, and some suspected OpenAI was hiding how it worked.
  - Quote from Anand Chowdhary: "When routing hits, it feels like magic. When it whiffs, it feels broken."
  - Altman had called the old model picker a "very confusing mess".
  - Jiaxuan You (UIUC): routing is "intuitive but very hard to get right".
  - — [Fortune, 2025-08-12](https://fortune.com/2025/08/12/openai-gpt-5-model-router-backlash-ai-future/)
- Some commentary said the router stayed "unpredictable" after the fixes, and that users read it as cost-cutting. These are opinion sources. — [Built In](https://builtin.com/articles/openai-power-users-lesson); [Shelly Palmer blog](https://shellypalmer.com/2025/08/five-days-with-gpt-5/)

**Google Gemini app**
- Late 2025: the picker offered "Fast – Answers quickly", "Thinking" and later "Pro". — [9to5Google](https://9to5google.com/2025/12/17/gemini-app-3-flash-rollout/)
- May 2026: a "Thinking level" menu (Standard / Extended) was added at the bottom of the picker. — [Beebom](https://gadgets.beebom.com/news/google-gemini-app-thinking-levels-app-integrations-roll-out)
- October 2026: free users "without a plan" can no longer pick a model. "Auto" routes prompts to Flash-Lite, Flash or Pro, and Low/Medium/High "effort levels" replace "Extended". — [9to5Google 2026-10-09](https://9to5google.com/2026/10/09/gemini-auto-free-users/); [Android Headlines](https://www.androidheadlines.com/2026/10/google-gemini-free-tier-auto-model-selection.html)

**Perplexity**
- "Best" is the automatic option inside Search: it "picks a suitable model for each query". Manual choice is available only on eligible plans **[vendor doc]**. — [Perplexity Help Center](https://perplexity.ai/help-center/en/articles/10354919-what-advanced-ai-models-are-included-in-my-subscription)

**Mistral Le Chat**
- "Think mode" (Magistral models) is a toggle next to the chat box. Fast is the default.
- It shows "the full reasoning path" before the answer, and stays on until the user switches modes **[vendor doc]**.
- — [Mistral docs: Think mode](https://docs.mistral.ai/le-chat/conversation/think-mode); [Mistral Help](https://help.mistral.ai/en/articles/424377-reason-with-le-chat-s-think-mode)

**Anthropic / Claude**
- The API uses "adaptive thinking", where the model decides how much to think, controlled by an `effort` setting.
- Thinking display can be "summarized" or "omitted". No setting returns the raw chain of thought; summarized mode returns a summary.
- On newer models (Opus 4.7 and later per Vercel's gateway docs) the default is "omitted". Docs pages differ on exactly which models default to which.
- — [Claude docs: extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking.md); [Claude docs: adaptive thinking](https://platform.claude.com/docs/fr/build-with-claude/adaptive-thinking); [Vercel AI Gateway](https://vercel.com/docs/ai-gateway/capabilities/reasoning/anthropic)

### Inferences
- The industry has converged on one pattern: automatic routing by default, plus a single "think harder" toggle. Gemini Auto + effort, ChatGPT Auto/Fast/Thinking, Le Chat Fast/Think and Perplexity Best all follow it. Model names are hidden from the people least able to use them; Gemini free tier and Perplexity free both lock users into automatic selection.
- The GPT-5 backlash was mostly about trust and control: silent downgrades, unknown model, lost favourite. It was not about the idea of routing. For older users, the mitigations are:
  - a stable, single "assistant" identity;
  - a small visible hint when it "thought more";
  - never silently downgrading mid-conversation.

### Gaps
- No public, quantitative satisfaction data on routers (CSAT, retention or the share of users choosing Thinking) was found from OpenAI, Google or Perplexity.
- I could not open the GPT-5 system card's router section directly to confirm the "trained on user switching" claim.
- Claude.ai's consumer UI (extended-thinking toggle, effort) was not separately verified; only the API docs were.

## 2. Routing methods, their accuracy, and what a solo founder can realistically use

### Takeaway
Academic evidence is sobering. LLMRouterBench (Jan 2026) found that many published routers, including OpenRouter's commercial one, do not reliably beat "always use the best single model" on cost/quality. Gains come mostly from careful choice of models and tiers, not from clever routers. A solo founder should use a cheap deterministic heuristic plus keyword router (LiteLLM's built-in complexity router), make the fast model the default, and offer a user "think more" override, rather than training a classifier.

### Cited Findings
**LLMRouterBench (Jan 2026)**
- Covers 400K+ instances, 21 datasets, 33 models and 10 baselines (RouterDC, EmbedLLM, GraphRouter, Avengers, HybridLLM, FrugalGPT, RouteLLM and others).
- "Several recent methods, including the commercial router OpenRouter, fail to reliably outperform the simple Best Single baseline" in performance-cost settings.
- The choice of embedding backbone matters little. Larger model pools give diminishing returns compared with careful curation.
- Accepted to Findings of ACL 2026.
- — [arXiv 2601.07206](https://arxiv.org/abs/2601.07206); [ACL Anthology](https://aclanthology.org/2026.findings-acl.1881/); code at [GitHub](https://github.com/ynulihao/LLMRouterBench)

**RouteLLM (LMSYS, 2024)**
- Routers trained on human preference data plus data augmentation cut costs "by over 2 times in certain cases" without hurting quality, and transfer when the strong/weak models are swapped **[author claim]**.
- The abstract does not list per-router numbers. — [arXiv 2406.18665](https://arxiv.org/abs/2406.18665)

**vLLM Semantic Router**
- A fine-tuned ModernBERT classifier decides whether a query needs reasoning and sets reason_on/off.
- On MMLU-Pro with Qwen3-30B it reports +10.2% accuracy, -47.1% latency and -48.5% tokens compared with always-on reasoning **[author/vendor claim]**.
- It runs inside Envoy, so it is an extra infrastructure layer.
- — [arXiv 2510.08731](https://arxiv.org/pdf/2510.08731); [vLLM blog](https://vllm.ai/blog/2025-09-11-semantic-router); [Red Hat Developers](https://developers.redhat.com/articles/2025/09/11/vllm-semantic-router-improving-efficiency-ai-reasoning)

**LiteLLM Auto Router (beta, since v1.94.0)**
- Configured as `model: auto_router/complexity_router`, with SIMPLE / MEDIUM / COMPLEX / REASONING tiers. — [LiteLLM docs: auto routing](https://docs.litellm.ai/docs/proxy/auto_routing)
- Classifier options:
  - Default heuristic scorer: no API call, sub-millisecond. It scores 7 dimensions: tokens, code, reasoning markers, technical terms, simple indicators, multi-step patterns, question complexity. Two or more reasoning markers force REASONING.
  - LLM classifier: one small model call.
  - "JEV" classifier: calls a third-party service, TypeSafe.
  - Deterministic `keyword_tier_rules`, optionally with embedding paraphrase matching.
  - Custom Python plugin.
  - — [LiteLLM docs](https://docs.litellm.ai/docs/proxy/auto_routing)
- What it classifies: the last real human message, with tool output and system-reminder blocks excluded, plus by default up to 3 prior user turns. — [LiteLLM docs](https://docs.litellm.ai/docs/proxy/auto_routing)
- Self-reported benchmarks, all **[vendor claim]** — [LiteLLM auto-router benchmarks](https://docs.litellm.ai/docs/auto_router/benchmarks):
  - 220 prompts across 6 public benchmarks: 40.4% cost saving at 97.1% relative quality (91.8% vs 94.5% pass rate) against an all-flagship baseline.
  - RouterArena (8,399 queries): 74.5% saving at 87.3% quality.
  - Production (450+ users, 272,876 requests, Apr–Aug 2026): 51.1% saving against a flagship-only counterfactual, and 95% of requests never reached the flagship tier.
  - Shadow LLM-judge on 143 turns: router won 9.8%, tied 78.3% and lost 11.9% against the flagship.
  - Classifier context: tier agreement on history-dependent follow-ups was 14% with 0 prior turns, 47% with 1 and 78% with 2.
  - JEV vs a Haiku-4.5 LLM classifier: 95% vs 73.75% agreement with hand-written expected tiers on only 80 synthetic cases.
  - The page itself says labels were not independently reviewed and sample sizes are small.
- On OpenRouter's auto router: it is shown not to reliably beat the best single model in LLMRouterBench. — [arXiv 2601.07206](https://arxiv.org/abs/2601.07206)

### Inferences
- Practical stack for a solo founder:
  1. LiteLLM complexity router with the heuristic classifier, plus `keyword_tier_rules` in Spanish and English (e.g. "analiza", "compara", "contrato", "paso a paso", "demuestra"). This costs nothing extra and adds no latency.
  2. Map SIMPLE and MEDIUM to DeepSeek V4.1 Flash, and COMPLEX and REASONING to Kimi K3.1 Pro (or keep Flash with high reasoning effort on COMPLEX).
  3. A user "Pensar más" toggle that forces the strong tier.
  4. Logging of tier decisions, with a weekly review of misroutes.
- A trained classifier (RouteLLM-style or vLLM-SR) is likely premature until the product has real traffic labels.
- The LLMRouterBench result suggests that with only two models, a well-tuned rule ("default fast; strong for long, analytical, document or multi-step requests; or when the user asks") captures most of the available value.
- Cascades ("try cheap, check confidence, escalate") add latency and double-answer UX problems for chat users. Confidence-based escalation is better kept for background or agent tasks than for interactive chat. (This is inference; no direct consumer-UX study was found.)

### Gaps
- RouterBench (2024) and FrugalGPT cascade figures were not fetched in this pass; only their inclusion as LLMRouterBench baselines is confirmed.
- No independent (non-vendor) evaluation of the LiteLLM complexity router was found.
- No published accuracy for routers on Spanish-language consumer prompts was found.

## 3. Keeping prompt caching while routing

### Takeaway
Switching model mid-conversation throws away the provider's prefix cache, because each model's cache is separate. The fix is per-conversation stickiness: pin the model for a session (LiteLLM `session_affinity`) and only escalate at the start of a new turn, deliberately, accepting one cache miss.

### Cited Findings
- LiteLLM `session_affinity` is off by default. When on, it pins a session's first-turn model, keyed by `session_id` metadata, for `session_affinity_ttl_seconds` (default 3600).
- The docs warn that the session then "inherits the first turn's tier", so a conversation that starts simple stays on the cheap model.
- — [LiteLLM docs: auto routing](https://docs.litellm.ai/docs/proxy/auto_routing)
- LiteLLM reports that the router plus caching was 37–69% cheaper than caching a single fixed model across five datasets **[vendor claim, details on a separate page not read]**. — [LiteLLM benchmarks](https://docs.litellm.ai/docs/auto_router/benchmarks)
- DeepSeek thinking mode:
  - In plain multi-turn chat, earlier `reasoning_content` can be omitted (the API ignores it).
  - With tools, `reasoning_content` must be sent back on later sub-requests, or the API returns a 400 error.
  - Thinking mode ignores temperature/top_p.
  - Switching model mid-turn during a tool loop can therefore break things.
  - — [DeepSeek API: Thinking Mode](https://api-docs.deepseek.com/guides/thinking_mode/)

### Inferences
- Recommended policy:
  - Decide the tier on the first message of a conversation and on each new user turn, never inside a tool or agent loop.
  - Allow one-way upgrade (fast to strong) when a later turn is classified COMPLEX or REASONING, or when the user presses "Pensar más". Do not downgrade automatically within a conversation.
  - Keep the system prompt and tool definitions byte-identical across models so each model's cache warms quickly.
- `session_affinity` as built pins to the first turn's tier, which conflicts with "upgrade on harder turns". A small custom routing plugin, or LibreChat passing an explicit tier tag, may be needed to get "sticky but upgrade-only" behaviour.
- Cache pricing and TTL vary by EU host (e.g. vLLM/SGLang automatic prefix caching vs provider APIs). Verify with the chosen host.

### Gaps
- Prompt-cache behaviour and pricing for EU-hosted DeepSeek V4.1 / Kimi K3.1 deployments were not researched here.
- I did not confirm whether LiteLLM's affinity can be configured as "upgrade-only".

## 4. What LibreChat supports today (modelSpecs, reasoning display, agents, UI simplification)

### Takeaway
Without code changes, LibreChat can:
- hide the model picker and parameters;
- offer a small set of named "modes" (modelSpecs with presets, including `reasoning_effort` for custom OpenAI-compatible endpoints);
- set landing text and conversation starters;
- replay `reasoning_content` for DeepSeek/Kimi tool calls.

It has no built-in automatic per-request router. Point a modelSpec at a LiteLLM "auto" model name and let the gateway choose. A one-tap "Pensar más" toggle in the composer that switches tier mid-conversation would most likely need a small UI change, or be modelled as two specs.

### Cited Findings
**modelSpecs: top-level**
- `enforce` (default false): specs "strictly override other configuration settings".
- `prioritize` (default true).
- `list` (required).
- `addedEndpoints` (requires `interface.modelSelect`).
- Defining a `list` without `interface` overrides disables `modelSelect`, `parameters` and `presets`. That hides the endpoint dropdown and the API-key gear.
- `hideBadgeRow` hides the composer's Tools/Skills/MCP chips (file uploads stay).
- — [LibreChat docs: modelSpecs](https://www.librechat.ai/docs/configuration/librechat_yaml/object_structure/model_specs)

**modelSpecs: per spec**
- `name`, `label`, `default`, `softDefault`, `description`, `iconURL`, `showIconInMenu`, `showIconInHeader`, `group`, `groupIcon`, `showInMenu`, `showOnLanding`.
- `conversation_starters` (max 4).
- Feature toggles: `webSearch`, `fileSearch`, `executeCode`, `memory`, `askUserQuestion`, `runInBackground`, `mcpServers`, `skills`, `subagents`, `artifacts`.
- — [LibreChat docs: modelSpecs](https://www.librechat.ai/docs/configuration/librechat_yaml/object_structure/model_specs)

**modelSpecs: preset reasoning fields**
- `reasoning_effort` (none / minimal / low / medium / high / xhigh / max) for openAI, azureOpenAI, custom OpenAI-like endpoints and Bedrock (ZAI and MoonshotAI models).
- `reasoning_summary` (auto / concise / detailed) for openAI, azure and custom.
- `thinking`, `thinkingBudget` and `effort` for Anthropic/Google.
- `thinkingDisplay` (auto / summarized / omitted / updates) for Anthropic and Bedrock-Anthropic only.
- — [LibreChat docs: modelSpecs](https://www.librechat.ai/docs/configuration/librechat_yaml/object_structure/model_specs)

**Reasoning replay for custom endpoints (customParams)**
- `reasoningFormat` (e.g. `reasoning_object`) and `reasoningKey` (e.g. `reasoning_content`).
- `includeReasoningContent: true` replays reasoning on assistant tool-call turns.
- `includeReasoningHistory: true` rebuilds `reasoning_content` from history across turns, only for providers that need it.
- — [LibreChat docs: custom params](https://www.librechat.ai/en/docs/configuration/librechat_yaml/object_structure/custom_params)

**Kimi/Moonshot**
- The custom endpoint `name` must be "Moonshot" (case-insensitive) for interleaved reasoning with tool calls on kimi-k2.5 / kimi-k2-thinking.
- Otherwise you get the error "thinking is enabled but reasoning_content is missing in assistant tool call message".
- If Kimi is reached through LiteLLM under another endpoint name, the customParams flags above are the likely fix (inference).
- — [LibreChat docs: Moonshot](https://www.librechat.ai/docs/configuration/librechat_yaml/ai_endpoints/moonshot)

**Changelog v0.8.1 (2025-12-11)**
- "improved reasoning/thinking content display, copy-to-clipboard" (#10278).
- "Reasoning Parameters for Custom Endpoints" (#10297).
- DeepSeek V3.2 tool calling and OpenRouter reasoning (#10752).
- — [LibreChat changelog v0.8.1](https://www.librechat.ai/changelog/v0.8.1)

**interface: fields that simplify the UI**
- `modelSelect`, `parameters`, `presets`, `prompts`, `bookmarks`, `multiConvo`, `agents`, `temporaryChat`, `fileSearch`, `webSearch`, `runCode`, `marketplace` (default off), `contextUsage` (token gauge, default on, so set it false for seniors), `contextCost`, `artifactUndocking`, `mascot`, `buildInfo`.
- `customWelcome` (supports `{{user.name}}`), `landingHeading: greeting`, `landingFooter`, `defaultPinnedTools`, `messageAuthor: whenDifferent`.
- Several permission-style fields only seed USER-role defaults at first startup. Manage them in the Admin Panel after that.
- — [LibreChat docs: interface](https://www.librechat.ai/docs/configuration/librechat_yaml/object_structure/interface)

### Inferences
- Minimal no-code design:
  - One default modelSpec, "Asistente", that points at the LiteLLM model `auto` (the complexity router) with `reasoning_effort: low`.
  - A second spec, "Asistente – pensar más", that points at the strong model or a REASONING-tier alias with `reasoning_effort: high`.
  - `interface.modelSelect/parameters/presets: false`, `contextUsage: false`, `hideBadgeRow: true`, and `conversation_starters` written in plain Spanish.
- A real per-message "Pensar más" button in the composer, a "pensé más en esto" badge, or a mid-conversation tier upgrade would need a LibreChat frontend change: a composer toggle that sends a header or tag (e.g. `x-litellm-tags`) to LiteLLM. This is an inference; no such built-in toggle was found in the docs read.
- Reasoning collapsing: LibreChat already renders `reasoning_content` from DeepSeek/Kimi as a collapsible thinking block, per v0.8.1 "reasoning content display". Showing a *summary* instead of raw CoT for open models is not documented for custom endpoints; `thinkingDisplay` is Anthropic-only.

### Gaps
- I did not verify a "Compact context" feature or how LibreChat agents/subagents assign different models per subagent (only the `subagents` spec toggle was seen).
- Changelogs after v0.8.1 (to Nov 2026) were not read in full. Check the current release notes for reasoning-display and summarisation features.
- I did not confirm whether LibreChat shows the resolved model name returned by LiteLLM (`return_raw_model_name`).

## 5. What LiteLLM supports for routing (auto router, tags, fallbacks, budgets, cost headers)

### Takeaway
LiteLLM covers the gateway side well: a beta complexity auto-router with tiers, keyword rules and session affinity; tag-based routing via header or key/team; fallbacks; budget routing; and unified `reasoning_content` with `reasoning_effort` mapping and rounding.

### Cited Findings
**Auto router config**
- `complexity_router_config.tiers` maps tiers to a model or a list. Lists are picked at random, or Thompson-sampled with `adaptive: true`.
- `complexity_router_default_model`, `keyword_tier_rules`, `semantic_keyword_matching`, `tier_boundaries`, `token_thresholds`, `dimension_weights`, `classifier_type`, `classifier_fallback`, `session_affinity`, `return_raw_model_name`, `modality_routing`.
- It is beta, and "config keys and defaults may change".
- — [LiteLLM: auto routing](https://docs.litellm.ai/docs/proxy/auto_routing)
- The older embedding-based semantic auto router is deprecated (about 100–500 ms per embedding call). — [LiteLLM: auto routing](https://docs.litellm.ai/docs/proxy/auto_routing)

**Tag routing**
- Deployments get `litellm_params.tags`. Requests send `tags`, `metadata.tags` or the header `x-litellm-tags`. Key/team/project tags are inherited.
- `default`-tagged deployments receive untagged requests. `router_settings.enable_tag_filtering`, `tag_filtering_match_any`, plus `!` (exclude) and `&` (require all) operators.
- Response header `x-litellm-model-id` identifies the deployment used.
- The page links to fallbacks (`/docs/proxy/reliability`, `router_settings.fallbacks`) and Budget Routing (`/docs/proxy/provider_budget_routing`).
- — [LiteLLM: tag routing](https://docs.litellm.ai/docs/proxy/tag_routing)

**Reasoning standardisation**
- `reasoning_content` is returned across providers (DeepSeek, Anthropic, Bedrock, Vertex, OpenRouter, xAI, Mistral Magistral, Groq and others). `thinking_blocks` is Anthropic-only.
- `reasoning_effort` is mapped per provider. `model_info.reasoning_effort_levels` rounds unsupported levels, and `drop_params` drops unsupported ones. `supports_reasoning` is reported at `/model_group/info`.
- `reasoning_auto_summary` adds `summary="detailed"` to OpenAI Responses requests.
- — [LiteLLM: reasoning_content](https://docs.litellm.ai/docs/reasoning_content)

### Inferences
- Wire "Pensar más" as either:
  - a separate model alias (`asistente-pro`) that routes to Kimi with `reasoning_effort: high`; or
  - an `x-litellm-tags: think` header that keyword rules or tag filtering map to the strong deployment.
- Per-user budgets via virtual keys can cap strong-model spend for each subscriber. Cost tracking/headers exist in LiteLLM generally (from prior knowledge; the `x-litellm-response-cost` header was not confirmed on the pages read).

### Gaps
- Moonshot/Kimi reasoning-effort mapping is not documented on the LiteLLM reasoning page. Check how Kimi K3.x exposes effort.
- I did not read the response-cost header, budget-routing and fallback pages in this pass.

## 6. Reasoning display: how open models expose it, faithfulness concerns, and showing summaries to non-experts

### Takeaway
Open models (DeepSeek, Kimi) return raw chain of thought in `reasoning_content`. Research shows raw CoT is often unfaithful to what actually drove the answer. Closed vendors now show summaries, or nothing, by default. For older non-experts: show a short, plain-language "what I considered" summary, collapsed by default, generated by the fast model from the raw reasoning. Do not show the raw stream.

### Cited Findings
**How open models expose reasoning**
- DeepSeek thinking mode returns CoT in `reasoning_content` alongside `content`, toggled with a `thinking` object (enabled/disabled). — [DeepSeek API docs](https://api-docs.deepseek.com/guides/thinking_mode/)
- LiteLLM normalises reasoning to `reasoning_content` across providers. — [LiteLLM docs](https://docs.litellm.ai/docs/reasoning_content)

**Faithfulness research (Anthropic, 2025)**
- Claude 3.7 Sonnet and DeepSeek R1 mentioned hints they actually used in their CoT often less than 20% of the time.
- Outcome-based RL plateaued at about 28% / 20% faithfulness.
- Models admitted reward hacks less than 2% of the time.
- Unfaithful CoTs were on average longer than faithful ones.
- — [Anthropic research](https://www.anthropic.com/research/reasoning-models-dont-say-think); [arXiv 2505.05410](https://arxiv.org/html/2505.05410v1)

**Vendor practice**
- Anthropic returns only summarized or omitted thinking; "no display setting returns the raw chain of thought". Omitting reduces latency but not cost.
- A newer `thinking-display-updates-2026-08-18` beta shows progress updates between tool calls.
- — [Claude docs](https://platform.claude.com/docs/en/build-with-claude/extended-thinking.md); [LibreChat modelSpecs (thinkingDisplay: updates)](https://www.librechat.ai/docs/configuration/librechat_yaml/object_structure/model_specs)
- OpenAI exposes `reasoning_summary` (auto/concise/detailed) rather than raw reasoning, as reflected in LibreChat's preset options. — [LibreChat modelSpecs](https://www.librechat.ai/docs/configuration/librechat_yaml/object_structure/model_specs)

**Older adults and explanations**
- A Georgia Tech CHI 2026 study (23 older adults living alone, users of voice assistants) found that agents "must provide clear explanations for their suggestions" or older adults won't trust them. Many participants "feel excluded from the design". — [Georgia Tech, 2026-03-31](https://ic.gatech.edu/external-news/new-study-shows-explainability-must-older-adults-trust-ai)
- A search summary of the same work said explanations grounded in user history or environmental data built trust, while the AI's "internal reasoning" created skepticism. I could not confirm this on the page fetched. — [Georgia Tech CoC news](https://www.cc.gatech.edu/index.php/news/new-study-shows-explainability-must-older-adults-trust-ai)
- A CHI 2026 study (n=70) found that high agreeableness in LLM voice assistants improved older adults' trust and likeability toward explanations. (From search results; paper not opened.) — [arXiv 2510.06697](https://arxiv.org/pdf/2510.06697v2)

### Inferences
- Display rule: collapsed by default, under a label such as "Cómo lo he pensado (3 pasos)", with 2–4 plain-language bullet steps and no raw text.
- A cheap way to build it: after the strong model answers, the fast model rewrites `reasoning_content` into 3 bullets, or the strong model is prompted to output a short "pasos" section.
- Add a caveat line, e.g. "Esto es un resumen; compruebe datos importantes".
- While the model thinks, show a single progress message ("Estoy pensando con más detalle… puede tardar unos 20 segundos"), not streaming CoT. Long raw streams are likely to overwhelm and alarm non-experts. This is inference, consistent with vendor practice and the faithfulness findings.
- Raw CoT may contain language mixing, false starts or sensitive content. Summarising also acts as a safety filter.

### Gaps
- No user study was found that compares raw vs summarised reasoning display specifically for older adults.
- I did not verify Kimi K3.x's reasoning field and effort parameters (the LibreChat docs cover only kimi-k2.5 / k2-thinking).

## 7. UX for older and non-technical users: research and concrete design rules

### Takeaway
Age-friendly design is largely good accessibility (WCAG) plus fewer choices, forgiving input, plain language and explanations. Older adults blame themselves for errors and feel excluded. Many chatbot users over 50 consider themselves beginners. Hide models and parameters, give examples to start from, support voice, and make "think more" a single clearly labelled option.

### Cited Findings
**NN/g**
- Users 65+ make more errors than younger users and tend to blame themselves.
- Ability to use websites declines about 0.8% per year between ages 25 and 60.
- Research base: 123 participants aged 65+ in five countries, 2001–2019.
- Guidelines:
  - avoid tiny or light-gray text;
  - make large click/tap targets;
  - accept multiple input formats, including speaking instead of using pickers;
  - tolerate typos and punctuation;
  - write clear, visible, simple error messages that make the fix easy.
- — [NN/g: Usability for Older Adults, 2019](https://www.nngroup.com/articles/usability-for-senior-citizens/)
- NN/g video: users 65+ are 43% slower at using websites than users aged 21–55. (From the search snippet.) — [NN/g video](https://www.nngroup.com/videos/designing-seniors/)
- NN/g's focus is 65+. AARP-linked work (Chisnell & Redish) defined "older adults" as 50+. — [Dana Chisnell heuristics](https://danachisnell.com/tag/heuristics)

**W3C WAI**
- Research found "existing international accessibility standards from the W3C WAI address most older user needs" (vision, hearing, motor and cognitive decline overlap with disability needs).
- Some needs are closer to traditional usability than to WCAG.
- — [W3C WAI: Older Users and Web Accessibility](https://www.w3.org/WAI/older-users/); [WAI-AGE needs](https://www.w3.org/WAI/WAI-AGE/needs.html)

**Older adults and generative AI**
- AARP reports that 42% of older adults who use a chatbot consider themselves AI beginners, 28% intermediate and 7% advanced. (From the search snippet.) — [AARP](https://www.aarp.org/personal-technology/how-to-prompt-ai-chatbot/)
- A survey of 323 US generative-AI chatbot users found Baby Boomers to be "an obscure but enthusiastic cohort". — [Ju, Stewart & Park, Information Research](https://publicera.kb.se/ir/article/view/41281)
- A nationally representative US survey (Innovation in Aging, 2025) found that older individuals perceive more benefits and fewer risks of generative AI than younger ones. (From the search snippet.) — [Prolific citations: Katz et al.](https://citations.prolific.com/authors/b-katz)
- A value-sensitive-design interview study with 12 US older adults examined value tensions in their engagement with generative AI. — [PMC12761539](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12761539/)
- CHI 2026, "It feels like hard work trying to talk to it": breakdowns in a medication-management voice assistant, four breakdown types, and older adults using their surroundings to repair them. (From the search snippet.) — [arXiv 2510.06690](https://arxiv.org/pdf/2510.06690v1)
- Industry precedent of hiding the picker for the least-engaged tier: Gemini free users are locked to Auto. — [9to5Google](https://9to5google.com/2026/10/09/gemini-auto-free-users/)

### Inferences
These design rules are synthesised from the sources above; the numeric values follow common WCAG and age-friendly practice and should be validated by testing.
- **Model choice:** no model names or pickers. One assistant ("Asistente"), and one switch labelled "Pensar más (más lento, más cuidadoso)" with a sentence explaining when to use it.
- **Type and targets:** base text of at least 18px, adjustable; contrast of at least 4.5:1 (WCAG AA); tap targets of at least 44×44px; no light-gray placeholder-only instructions.
- **Starting points:** about 4 large example cards on the home screen (LibreChat `conversation_starters`), e.g. "Escribir un correo", "Explicarme una carta del banco", "Resumir un documento", "Planear un viaje".
- **Language:** plain Spanish with no jargon ("modelo", "tokens", "contexto", "prompt"). Hide the token or context gauge (`contextUsage: false`).
- **Voice:** a visible microphone button for dictation, plus read-aloud of answers.
- **Errors:** forgiving input; if something fails, explain it in one sentence with a single "Intentar de nuevo" button, and never blame the user.
- **Trust signals:**
  - a small note when it thought more;
  - sources for factual claims;
  - a clear "puede equivocarse" line placed under the composer (`landingFooter: composer`);
  - a stable visual identity across fast and strong models, so routing is invisible but honest.
- **Testing:** test with 5–8 real users aged 50–75 in Spain before launch. Guidelines alone are insufficient. — [Dana Chisnell](https://danachisnell.com/tag/heuristics); [NN/g](https://www.nngroup.com/articles/usability-for-senior-citizens/)

### Gaps
- NN/g's full 87-guideline senior report (with numeric font and target sizes) is paywalled and was not read.
- No study was found that measures older adults' confusion with model pickers specifically. The evidence is indirect: the GPT-5 backlash and Altman's "very confusing mess" remark.
- No Spain- or EU-specific study of older adults using LLM chatbots was found in this pass.
