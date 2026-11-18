# Subscription plans vs raw API pricing (as of 18 Nov 2026)

Scope note: Official OpenAI pages (openai.com/chatgpt/pricing, help.openai.com, openai.com/api/pricing) returned HTTP 403 to my fetcher, so OpenAI plan and API facts below come from (a) OpenAI's own docs page learn.chatgpt.com/docs/pricing, which I could fetch, and (b) third-party trackers. Those are labelled. Anthropic's API pricing page and claude.com/pricing were fetched directly. Perplexity and Google figures are secondary sources only. All dollar worked examples in the break-even section are my own arithmetic on stated assumptions, not sourced facts.

## 1. Current plans and prices (ChatGPT, Claude, Gemini, Perplexity)

### Takeaway
The consumer entry tier is about $20/month everywhere (ChatGPT Plus, Claude Pro, Google AI Pro, Perplexity Pro). Above it, tiers are $100 and $200 (ChatGPT Pro has $100/$200/$500; Claude Max $100/$200; Google AI Ultra $99.99/$199.99; Perplexity Max $200). Team and business seats are about $20-25 per user with 2-seat minimums.

### Cited Findings
**ChatGPT (OpenAI)**
- Free $0; Go $8/month; Plus $20/month; Pro "from $100/month" with plans at $100, $200 or $500; Business $20/user/month billed annually, $25/user/month billed monthly, "2+ users"; Enterprise & Edu are contact-sales; API is pay-per-use. This is OpenAI's own pricing docs page. — [learn.chatgpt.com/docs/pricing](https://learn.chatgpt.com/docs/pricing)
- Third-party tracker (checked 12 Nov 2026) agrees on Go $8 and Plus $20, and says Pro $100/$200/$500 and Business $25 monthly / $20 annual ($240/yr). It says Enterprise is quote-based. — [CostBench](https://www.costbench.com/software/ai-chatbots/chatgpt/)
- Pro tier history per a third-party timeline: $100 Pro introduced 9 Apr 2026; Pro 500 introduced 29 Sep 2026; the Pro 100 and Pro 500 allowances doubled on 29 Oct 2026. The same article says OpenAI's Go help article states Go, Plus and Pro have no annual billing or prepaid multi-month option (not verified against the help page, which I could not open). — [tech-insider.org](https://tech-insider.org/chatgpt-go-vs-plus-vs-pro-100-200-500-2026/)
- Models by tier (third-party summary of OpenAI release notes): Free and Go use GPT-6 Luna; Plus gets GPT-6 Sol, GPT-6.1 Sol and GPT-6 Astra in Work and Codex; Pro adds GPT-6 Pro (powered by GPT-6 Astra); Pro 500 adds "Ultrafast" variants. GPT-5.5 was retired from ChatGPT on 14 Oct 2026. — [tech-insider.org](https://tech-insider.org/chatgpt-go-vs-plus-vs-pro-100-200-500-2026/)
- Business and Enterprise: Business has SAML SSO, MFA and no training on business data by default; Enterprise adds SCIM, EKM, RBAC, Compliance API, data residency. — [learn.chatgpt.com/docs/pricing](https://learn.chatgpt.com/docs/pricing)

**Claude (Anthropic)** (from claude.com/pricing as read by my fetch tool; the page says prices and plans may change)
- Free $0. Pro $17/month billed annually ($200 upfront) or $20/month billed monthly. — [claude.com/pricing](https://claude.com/pricing)
- Max $100/month listed as 5x Pro usage, including $100/month in API credits; a $200/month tier labelled "Ultra" listed as 10x weekly usage with no 5-hour limit for verified accounts and $200/month in API credits. Note this differs from the older "Max 5x $100 / Max 20x $200" naming, so verify on the live page. — [claude.com/pricing](https://claude.com/pricing)
- Team standard seat $20/seat/month annual or $25 monthly, 2 to 150 seats; Team premium seat $100/seat annual or $125 monthly, 5x standard usage. Enterprise $20/seat/month annual with a 20-seat minimum plus usage billed at API rates. — [claude.com/pricing](https://claude.com/pricing)
- Models: Pro includes Opus, Sonnet, Haiku, with Fable (the top model) via usage credits; Max and Ultra get Fable up to 50% of weekly limits. — [claude.com/pricing](https://claude.com/pricing)

**Google (Gemini)**
- Announced at I/O on 19 May 2026: AI Plus $7.99/month (2x limits), AI Pro $19.99/month (4x limits, 5 TB storage), AI Ultra from $99.99/month (up to 20x), top Ultra tier $200/month (cut from $250). — [The Decoder](https://the-decoder.com/google-overhauls-its-ai-subscriptions-at-i-o-2026-with-three-tiers-starting-at-10-a-month/)
- Google moved from daily prompt limits to a "compute-used" model: quotas reset every five hours with a weekly cap, and users who run out are moved to smaller models. — [The Decoder](https://the-decoder.com/google-overhauls-its-ai-subscriptions-at-i-o-2026-with-three-tiers-starting-at-10-a-month/)

**Perplexity** (April 2026 secondary source; no official page read)
- Pro $20/month or $200/year; Max $200/month or $2,000/year; Enterprise Pro $40/seat/month ($400/yr); Enterprise Max $325/seat/month ($3,250/yr). — [Finout](https://www.finout.io/blog/perplexity-pricing-in-2026)
- Perplexity says unlimited usage on Pro and Max applies only to the chat interface, not the API. — [Finout](https://www.finout.io/blog/perplexity-pricing-in-2026)

### Inferences
- Annual discounts are small or absent for consumer plans: Claude Pro saves $3/month (15%); ChatGPT consumer plans reportedly have no annual option; Perplexity Pro annual $200 vs $240 monthly-equivalent is about 17% off.
- Seat minimums: ChatGPT Business and Claude Team are 2 seats; Claude Enterprise 20 seats. A solo user cannot use Business/Team cheaper than the $20 individual plan, and Business monthly ($25) is more expensive than Plus.

### Gaps
- I could not open openai.com/chatgpt/pricing or help.openai.com (403); the Pro tier $500 and Go no-annual claims rest on OpenAI's docs page and one third-party article.
- Google's and Perplexity's official pages were not read; Perplexity figures are as of April 2026.
- CostBench lists a Business "premium seat" at $125/$100, which looks borrowed from Claude Team and is unconfirmed; ignore it unless verified.

## 2. Usage limits per plan (messages, deep research, agents, context)

### Takeaway
Limits are mostly undisclosed or expressed as ranges. ChatGPT Plus deep research is not officially stated as a number on the pricing page (third parties say about 25 per month, roughly 10 full plus 15 lightweight in some sources); Claude publishes no research quota at all, only shared 5-hour and weekly usage bars; Gemini and Perplexity quotas have changed in 2026 and sources conflict.

### Cited Findings
**ChatGPT**
- OpenAI's docs list Plus and standard Business "local messages per five-hour period" (for Codex-style usage) as ranges, for example GPT-6.2 Sol 17-180, GPT-6 Astra 5-45, GPT-6 Luna 350-3,000. These are "estimates, not fixed limits"; Pro plans "currently have no five-hour limit"; weekly limits may also apply. The page does not mention deep research quotas. — [learn.chatgpt.com/docs/pricing](https://learn.chatgpt.com/docs/pricing)
- Credits: Plus and Pro can buy extra credits after reaching limits; example rates are credits per 1M tokens, GPT-6.2 Sol 50 input / 2.5 cached / 250 output, GPT-6 Luna 2.5 / 0.25 / 12.5. A typical GPT-5.6 Sol task may use 2-15 credits. — [learn.chatgpt.com/docs/pricing](https://learn.chatgpt.com/docs/pricing)
- Deep research on Plus: one search summary reports OpenAI's pricing page describes deep research only as Limited (Free), Expanded (Plus), Maximum (Pro) with no run count (October 2026 article). — [search summary citing ai.zenken.co.jp](https://ai.zenken.co.jp/en/post/chatgpt-usage/)
- Third-party tracker (limits last verified 29 Jul 2026, cross-checked because OpenAI's help center blocks bots): Free about 10 flagship messages per 5 hours and 5 lightweight deep research per month; Plus 160 flagship messages per 3 hours, 25 deep research per month (mix of full and lightweight), 80 file uploads per 3 hours, up to 3,000 "Thinking" messages per week; Pro "effectively unmetered", deep research 125 full + 125 lightweight per month. Pro deep research and context figures were last verified 15 Jan 2026 (before the 2026 tier changes) so treat as dated. — [AI Plan Finder](https://aiplanfinder.com/chatgpt-usage-limits)
- Historical: Plus started at 10 deep research queries/month (Feb 2025), reportedly raised to 25 in April 2025. — [Dataconomy](https://dataconomy.com/2025/02/26/chatgpt-plus-subscribers-now-enjoy-deep-research-feature/) (Feb 2025 launch figure); the 25 figure is from the search summary above and not independently confirmed.
- Context windows (October 2026 third-party summary of OpenAI help): Go and Plus 256K reasoning / 54K instant; Pro 400K reasoning / 128K instant. Scheduled tasks: Go 3, Plus 5, Pro 15. Conflicts with the older 32K Plus figure at AI Plan Finder (Jan 2026). — [tech-insider.org](https://tech-insider.org/chatgpt-go-vs-plus-vs-pro-100-200-500-2026/)
- The same article says new Pro 200 subscribers after late September 2026 get a lower allowance than earlier ones (per CostBench), and SemiAnalysis says OpenAI cut its $200 plan limits in half. — [CostBench](https://www.costbench.com/software/ai-chatbots/chatgpt/); [SemiAnalysis](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x)

**Claude**
- Pro limits depend on conversation length, number of messages, model and feature; there is a five-hour session limit plus a weekly limit across models, and Research and web search count against usage. Pro, Max, Team users can view progress bars under Settings > Usage. — [support.claude.com Pro usage](https://support.claude.com/en/articles/8324991-about-claude-s-pro-plan-usage) (as summarised in a search result; page not fetched)
- User anecdote (May 2026): on Pro, "at most 1 successful research mode question per session"; one Sonnet 4.6 research run that completed used 56% of the limit (236 sources) and another failed at the limit. One person's report, not an official quota. — [William Angel](https://www.williamangel.net/blog/2026/05/20/ClaudeAI-Pro-Plan-Gives-Single-Deep-Research.html)
- Anthropic introduced weekly rate limits effective 28 Aug 2025 for Pro and Max to curb continuous background Claude Code use. — [TechCrunch](https://techcrunch.com/2025/07/28/anthropic-unveils-new-rate-limits-to-curb-claude-code-power-users/)
- Max/Ultra tiers: 5x and 10x Pro weekly usage as listed on the pricing page; no absolute message counts. — [claude.com/pricing](https://claude.com/pricing)

**Google**
- Older (Feb 2026) listing: AI Pro Deep Research 20 reports/day; Ultra $99.99 75/day; top Ultra 200/day (9to5Google, via search summary). The May 2026 overhaul replaced daily prompt counts with compute-based quotas and the article does not state deep research quotas, so the older per-day numbers may be superseded. — [9to5Google](https://9to5google.com/2026/02/21/google-ai-pro-ultra-features/) and [The Decoder](https://the-decoder.com/google-overhauls-its-ai-subscriptions-at-i-o-2026-with-three-tiers-starting-at-10-a-month/)

**Perplexity**
- Pro: unlimited Pro Search, 20 Research queries per day, 50 Labs queries per month, $5/month API credits; Max: unlimited Labs and Research. (April 2026.) — [Finout](https://www.finout.io/blog/perplexity-pricing-in-2026)
- Conflict: another source says Pro Deep Research dropped to 20/month in early 2026 and unclear whether Max is capped. — search summary of [suprmind.ai](https://suprmind.ai/hub/perplexity/pricing/) (not fetched); I could not resolve this.

### Inferences
- Every vendor deliberately avoids publishing a hard monthly deep research count at the $20 tier (except through third-party scrapes), consistent with limits being tuned dynamically to capacity.
- Backing out the credit rates: GPT-6 Sol at 50 credits per 1M input tokens vs API $2/M implies 1 credit is roughly $0.04 if credits track API prices (my arithmetic; credit dollar price not found).

### Gaps
- No official, current number found for ChatGPT Plus deep research runs, agent-mode messages, or Claude Research runs.
- Agent/browser task limits for any plan not found in verifiable sources.
- File-generation limits not found.
- Gemini and Perplexity current deep research quotas unverified post-May 2026.

## 3. Evidence on subsidy / cost to serve heavy subscribers

### Takeaway
There is credible but mostly third-party evidence that the top-end $100-$500 coding-heavy tiers can deliver thousands of dollars of API-equivalent tokens, but those are "at list API price" ceilings; the same analysts assume API gross margins of 75-92%, so real cost-to-serve is far lower. For $20 chat users, there is no public evidence of a large subsidy, and the only on-record executive admission of losses (Altman, Jan 2025) concerned the $200 Pro plan.

### Cited Findings
- Sam Altman posted on X in early Jan 2025 that OpenAI was "losing money on OpenAI pro subscriptions" because "people use it much more than we expected"; he said he chose the price personally and expected it to make money. Strong evidence (named executive), but only for the $200 tier and now 22 months old. — [Fortune](https://fortune.com/2025/01/07/sam-altman-openai-chatgpt-pro-subscription-losing-money-tech/)
- SemiAnalysis (Patel et al., 5 Oct 2026) says subscriptions are about 10% of Anthropic's revenue but can take over 40% of its inference compute; on a baseline of 100% utilization and 92% API gross margins, maxing out Opus 5.5 on the plan implies about -369% gross margin and maxing Fable 5.1 about 1%; at a more realistic 20% average utilization, margins are 6% (Opus 5.5) and 80% (Fable 5.1). It also says Anthropic offers about 5x the API-equivalent value of OpenAI across mid-tier models, OpenAI halved its $200 plan limits, and $200 OpenAI plan is exhausted after $2,897 of GPT-6 Astra usage while the $200 Claude plan would have 50% left after $2,485 of Fable 5.1. — [SemiAnalysis](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) (primary but partly paywalled; I read a summary of its text)
- SemiAnalysis thread of 10 Jun 2026: a fully utilized $200 ChatGPT Pro plan is worth up to about $14,000 at API rates versus about $8,000 for Claude Max 20x; methodology was subscribing to each and running coding workloads until the weekly cap, then pricing tokens at API rates; margins assume 75% API gross margin. Criticised as ambiguous in price calculation. — [GIGAZINE](http://gigazine.net/news/20260612-anthropic-openai-subscription-margin/)
- Secondary reports of the same thread cite -1,650% (ChatGPT Pro 20x) and -900% (Claude Max 20x) margin at full utilization under the 75% assumption. — search summary of [FourWeekMBA](https://fourweekmba.com/subsidized-agi-economy-ai-subscription-margin-harness-theory/) (not fetched; low confidence)
- Counterview: one analysis argues API-equivalent comparisons overstate the loss because retail API prices carry a markup over serving cost, and there is no public evidence the average Max subscriber costs more than they pay. — search summary of [ClaudeFolio](https://claudefolio.com/blog/is-anthropic-really-losing-money-on-your-200-max-plan) (page returned 403; summary only)
- Anthropic's response to heavy use was rate limits, not repricing: weekly caps from 28 Aug 2025 aimed at users running Claude Code "continuously in the background, 24/7". — [TechCrunch](https://techcrunch.com/2025/07/28/anthropic-unveils-new-rate-limits-to-curb-claude-code-power-users/)
- A search turned up no on-record Anthropic executive saying Max loses money; the "far more than the fee" claims (e.g. one user consuming $51,291 in a month) are unverified blog claims. — search results via [implicator.ai](https://www.implicator.ai/claude-gets-expensive-anthropic-launches-premium-100-200-subscription-tiers/) (not read); treat as low reliability.

### Inferences
- Because the "-369%" and "-1,650%" numbers divide API-priced tokens by an assumed 75-92% API margin, they say as much about API margins as about subscription subsidy. If API list prices are 4-12x serving cost, a $20 plan used at 20% utilization is plausibly profitable, which reconciles the user's intuition ("it can't subsidize so much") with the evidence: subsidy appears concentrated in maxed-out agentic coding on the $100-$500 tiers.
- The plan limit structure (5-hour windows, weekly caps, model fallback) is the mechanism that caps loss; it is the "averaging of light and heavy users" the user asked about.

### Gaps
- No OpenAI or Anthropic disclosure of per-subscriber cost; The Information, Bloomberg and Reuters pieces on subscription gross margin were not found in this pass.
- SemiAnalysis's $20 and $100 plan API-equivalent values are only in paywalled charts.

## 4. Why subscription is cheap versus API (mechanisms)

### Takeaway
The flat plan is cheaper for moderate users because (1) caps and rolling windows bound consumption, (2) overflow falls back to cheaper models, (3) most subscribers use well under the cap, and (4) vendors' API prices include a large margin relative to cost.

### Cited Findings
- Rolling five-hour windows plus weekly caps (ChatGPT Plus/Business, Claude, Google), and "estimates, not fixed limits" ranges — [learn.chatgpt.com/docs/pricing](https://learn.chatgpt.com/docs/pricing); [Claude usage help](https://support.claude.com/en/articles/8324991-about-claude-s-pro-plan-usage)
- Model downgrade at cap: Google moves users who exhaust quota to smaller models — [The Decoder](https://the-decoder.com/google-overhauls-its-ai-subscriptions-at-i-o-2026-with-three-tiers-starting-at-10-a-month/); ChatGPT Pro 200 falls back from GPT-6 Pro to GPT-5.6 Thinking at Medium at the weekly limit — [tech-insider.org](https://tech-insider.org/chatgpt-go-vs-plus-vs-pro-100-200-500-2026/); Plus flagship overflow to a lighter model — [AI Plan Finder](https://aiplanfinder.com/chatgpt-usage-limits)
- Utilization averaging: SemiAnalysis models 20% average utilization versus 100% to show margin swing from -369% to 6% — [SemiAnalysis](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x)
- API margin assumption 75-92% by SemiAnalysis — [SemiAnalysis](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x); [GIGAZINE](http://gigazine.net/news/20260612-anthropic-openai-subscription-margin/) (assumptions, not disclosed margins)
- Cheaper models in the free/low tiers: Free and Go run GPT-6 Luna, which costs $0.10/$0.50 per M tokens via API. — [tech-insider.org](https://tech-insider.org/chatgpt-go-vs-plus-vs-pro-100-200-500-2026/); [BenchLM](https://benchlm.ai/openai/api-pricing)
- Consumer-app token budgets: the ChatGPT consumer context is 54K (instant) / 256K (reasoning) on Plus vs 1.05M API context, so app conversations carry smaller prompts than a raw-API workspace would send. — [tech-insider.org](https://tech-insider.org/chatgpt-go-vs-plus-vs-pro-100-200-500-2026/); [BenchLM](https://benchlm.ai/openai/api-pricing)

### Inferences
- The user's skepticism is partly right: a $20 plan is not obviously a big subsidy for typical chat use; its cheapness comes from model choice, caps and averaging. Heavy deep-research users are the ones exposed to cap hits.
- Enterprise pricing (Claude Enterprise: seat price plus usage at API rates) shows the vendors treat flat pricing as a consumer/small-team construct and bill heavy usage at API rates once usage is metered. — [claude.com/pricing](https://claude.com/pricing)

### Gaps
- No quantified per-turn token budget for consumer apps from OpenAI or Anthropic; hidden system prompt/caching effects unknown.

## 5. API prices for frontier and cheap models (Nov 2026)

### Takeaway
Frontier API models cost about $4-8 per M input and $20-40 per M output; mid-tier $2/$10; cheap tier $0.10/$0.50. Web search adds about $10 per 1,000 searches (Anthropic's rate), which dominates cheap deep research.

### Cited Findings
- Anthropic (official docs): Fable 5.2 $8 in / $40 out per MTok (cache hits $0.20); Fable 5.1 $10/$50; Opus 5.5 $4/$20; Opus 5 $5/$25; Sonnet 5.5 $2/$10; Haiku 5.5 $0.10/$0.50 (prompts up to 100K; $0.50/$2.50 above); Batch API 50% off; web search $10 per 1,000 searches; Claude 4.7 and later models use a tokenizer producing about 30% more tokens for the same text. 1M context at standard pricing for 4.6+ models except Haiku 5.5. — [Anthropic pricing docs](https://platform.claude.com/docs/en/about-claude/pricing)
- OpenAI API (third-party tracker updated 18 Nov 2026; OpenAI's own page was blocked): GPT-6.2 Astra $8/$40 (cached $0.40); GPT-6 Astra $10/$50; GPT-6.2/6.1 Sol $2/$10 (cached $0.10); GPT-6.1 Terra $1/$5; GPT-6 Luna $0.10/$0.50; GPT-5.6 Sol $4/$20; 1.05M context. — [BenchLM](https://benchlm.ai/openai/api-pricing)
- o3-deep-research listed at $10 input / $40 output per M tokens, but OpenAI's model page (Traditional Chinese version) reportedly says it stopped service on 23 Jul 2026. — [OpenAI model page](https://developers.openai.com/zh-Hant/api/docs/models/o3-deep-research) (via search summary; not fetched)
- Perplexity Sonar Deep Research API: $2/$8 base tokens, $2 per M citation tokens, $3 per M reasoning tokens, $5 per 1,000 searches; a full query "can run to $0.41 or more". — [Finout](https://www.finout.io/blog/perplexity-pricing-in-2026)
- Observed deep research costs: roughly $0.40 to $5 per query in the sources I found (search fees and reasoning tokens dominate); one calculator puts o4-mini deep research near $0.41; a worked example of 48 searches and about 95K reasoning tokens cost about $0.53 (older models); a developer forum report of about $2.50 per Gemini deep research call is unverified. — search summary of [Simon Willison](https://simonwillison.net/2025/May/28/claude-calculator/), [APICostCalc](https://apicostcalc.com/deep-research-api-cost-calculator.html), [Gemini forum](https://discuss.ai.google.dev/t/google-gemini-deep-research-costs/112804) (not fetched individually)

### Inferences
- OpenAI offers no first-party "deep research" API model anymore (o3-deep-research retired), so a DIY deep research agent must be built from a general model plus search tool; cost is model tokens plus search fees.

### Gaps
- OpenAI's web search tool price for 2026 not verified; I assume $10/1,000 (Anthropic's published rate) for all models.
- Anthropic, OpenAI do not publish deep-research-per-run token counts.

## 6. Break-even analysis (my arithmetic, assumptions stated)

### Takeaway
At 100 chat turns/day plus 2 deep research runs/day (3,000 turns and 60 runs per month), an all-frontier API bill is about $130-$880/month; mid-tier models about $70-$250; cheap models about $15-$50. A flat $20 plan only loses to the API if you use cheap models and moderate research depth; $200 plans beat the frontier API in almost every scenario here.

### Assumptions (mine, not sourced)
- Chat turn A (light): 2,000 input + 600 output tokens. Chat turn B (heavy, long threads, no caching): 8,000 input + 1,000 output.
- Deep research run, light: 150K input + 20K output tokens + 20 searches ($0.20 at $10/1,000). Heavy: 800K input + 60K output + 60 searches ($0.60). No prompt caching or batch discount (would cut input costs; batch is 50% off but not interactive).
- Month = 30 days. $20/month = $0.67/day; $200/month = $6.67/day.
- Price tiers use the API prices in section 5. Frontier = GPT-6.2 Astra / Fable 5.2 ($8/$40) and Opus 5.5 ($4/$20); mid = Sonnet 5.5 / GPT-6 Sol ($2/$10); cheap = Haiku 5.5 / GPT-6 Luna ($0.10/$0.50). Anthropic's newer tokenizer (about +30% tokens) is ignored.

### Per-unit costs
| Tier | Chat turn A | Chat turn B | Deep research light | Deep research heavy |
|---|---|---|---|---|
| Frontier $8/$40 | $0.040 | $0.104 | $2.20 | $9.40 |
| Frontier $4/$20 (Opus 5.5) | $0.020 | $0.052 | $1.20 | $5.00 |
| Mid $2/$10 | $0.010 | $0.026 | $0.70 | $2.80 |
| Cheap $0.10/$0.50 | $0.0005 | $0.0013 | $0.23 | $0.71 |

### Monthly cost: 3,000 chat turns + 60 deep research runs
| Tier | Chat only (A to B) | Research only (light to heavy) | Total/month | Total/day |
|---|---|---|---|---|
| Frontier $8/$40 | $120 to $312 | $132 to $564 | $252 to $876 | $8.4 to $29 |
| Frontier $4/$20 | $60 to $156 | $72 to $300 | $132 to $456 | $4.4 to $15 |
| Mid $2/$10 | $30 to $78 | $42 to $168 | $72 to $246 | $2.4 to $8.2 |
| Cheap $0.10/$0.50 | $1.5 to $3.9 | $13.5 to $42.6 | $15 to $47 | $0.50 to $1.55 |
| Hybrid: cheap chat + mid research | $1.5 to $3.9 | $42 to $168 | $44 to $172 | $1.5 to $5.7 |

### How many deep research runs $20 buys on the API
| Tier | Light runs per $20 | Heavy runs per $20 |
|---|---|---|
| Frontier $8/$40 | about 9 | about 2 |
| Frontier $4/$20 | about 17 | 4 |
| Mid $2/$10 | about 29 | about 7 |
| Cheap $0.10/$0.50 | about 89 | about 28 |
Observed costs in sources ($0.41 Sonar-type, $0.53 example) imply about 38-49 runs per $20 for cheap-search-heavy pipelines. — [Finout](https://www.finout.io/blog/perplexity-pricing-in-2026)

### Break-even logic
- Budget per turn at 100 turns/day: $20 plan = $0.0067 per turn; $200 plan = $0.067 per turn (chat only). Only cheap models (about $0.0005-0.0013) beat $20; Opus 5.5 even with light turns ($0.020) loses to the $20 plan; frontier $8/$40 loses to $200 plan only on heavy turns ($0.104 > $0.067).
- Research only, 2 runs/day: $20 plan = $0.33 per run; $200 plan = $3.33 per run. Only cheap light ($0.23) beats the $20 plan; mid-tier and frontier runs all cost more than $0.33. Against the $200 plan ($3.33 per run), the light runs at all tiers ($0.23-$2.20), mid heavy ($2.80) and cheap heavy ($0.71) are cheaper on the API, while heavy runs on frontier models ($5.00 Opus 5.5, $9.40 at $8/$40) cost more, so the $200 plan wins there.
- Combined: all-frontier API is above $4.4/day in every case here, i.e. $130+/month, worse than $20 and mostly worse than $200 (except the lightest Opus 5.5 case, $132/month). All-cheap API at light research ($15/month) beats $20 plans narrowly; at heavy research ($47/month) it does not.

### Does the plan cover about 3,000 turns and 60 runs per month?
- ChatGPT Plus: 100 turns/day is well inside a 160-messages-per-3-hours flagship cap (third-party figure, Jul 2026) and Go/Free-level Luna usage; 60 deep research runs exceeds the third-party Plus figure of about 25/month (and the 10 full + 15 light figure), so Plus likely does not cover 60; Pro's reported 125 full + 125 light would, but that figure is from Jan 2026 and Pro tiers changed afterward. — [AI Plan Finder](https://aiplanfinder.com/chatgpt-usage-limits)
- Claude Pro: no published research quota; a May 2026 user report of about one research run per five-hour session makes 2 per day borderline and 60 per month risky; the $100 Max tier (5x Pro) is the plausible fit. — [William Angel](https://www.williamangel.net/blog/2026/05/20/ClaudeAI-Pro-Plan-Gives-Single-Deep-Research.html); [claude.com/pricing](https://claude.com/pricing)
- Google AI Pro: older listing of 20 Deep Research/day would cover 60/month easily, but quotas were reworked in May 2026 and are unconfirmed. — [9to5Google](https://9to5google.com/2026/02/21/google-ai-pro-ultra-features/)
- Perplexity Pro: 20 Research queries/day (April 2026) would cover 2/day easily, but a conflicting source says 20/month. — [Finout](https://www.finout.io/blog/perplexity-pricing-in-2026)

### Inferences
- Combined recommendation logic: a hybrid (cheap model for chat; one subscription such as Perplexity Pro or Google AI Pro for deep research quotas) can cost about $20-40/month, beating a fully DIY API workspace; building on APIs only pays off if you route chat to cheap models, cap research depth, or need features subscriptions lack (own data, model choice, no caps).
- The cheap-model chat cost is negligible (about $2-4/month for 3,000 turns), so the dominant API cost is deep research, driven by input tokens re-read across many tool turns and search fees. Prompt caching (cache reads at 10% of input) can cut the input portion substantially, so heavy-case numbers above are upper bounds for a well-built agent.

### Gaps
- No measured token counts for vendor deep research runs; my two run profiles are guesses and should be replaced with a measured run on the user's own prompts.
- Tokenizer variance (+30% for newer Anthropic models) and tool-call overhead not modelled.
- The Information, Bloomberg or Reuters reporting on subscriber economics (e.g. OpenAI considering lowering token prices, mentioned in GIGAZINE citing WSJ) was not verified.
