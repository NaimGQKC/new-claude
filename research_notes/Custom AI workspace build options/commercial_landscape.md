# Commercial landscape for a self-hosted / BYO-API-key AI workspace sold to SMBs (US and EU, as of 2026-11-18)

Method notes: Research used web search (which returns synthesized summaries) plus direct page fetches. Where a primary page could not be fetched (OpenAI and Hetzner help pages returned 403/404; Anthropic's pricing page not reached), figures come from third-party pages and are flagged "secondary". Many price aggregators (costbench, zemith, eesel, dupple, etc.) disagree with each other; they are used only where noted and should be re-verified on vendor pages before any pricing decision. Nothing here is legal advice.

---

## 1. Competitors and adjacent products with BYO-key or usage-based pricing

### Takeaway
The market is crowded at the $20-30/seat/month point (Onyx, Dust, Langdock, Mistral, Abacus, Microsoft/Google bundles), and the BYO-key niche is already served by TypingMind (flat team fee plus API passthrough), AnythingLLM, Msty, Cherry Studio, and OpenRouter (credits-plus-fee). A BYO-key product therefore competes on usage transparency and cheap routing, not on being the only option; evidence of traction for any BYO-key vendor is thin or absent in what I found.

### Cited Findings
- **TypingMind Custom/Teams**: flat fee starting at $99/month including 5 users, API usage billed separately via the customer's own keys; vendor claims this is cost-effective versus Claude Team (vendor marketing, self-published comparison). [TypingMind docs](https://docs.typingmind.com/typingmind-team/getting-started/typingmind-team-vs-claude-team). The same page compares against Claude Team at "$30/month per user, 5 minimum", which is outdated (see section 2).
- **TypingMind individual licences**: one-time purchase, Standard $39, Extended $79, Premium $99 (listed "50% off" from $198), Bulk licence $395 for up to 10 users; API costs excluded; keys stored in the browser; self-host version is a compiled static app with no source and no modification/redistribution rights; Teams (custom-branded workspace) has no listed price and uses subscription pricing. [TypingMind buy page](https://www.typingmind.com/buy). Conflict: a third-party summary also cites extra seats at $8/user/month; not confirmed on the primary page.
- **Langdock** (German, EU-hosted): per-seat, euros excl. VAT. Core Standard seat €23.20/month annual or €29 monthly; Work Standard €31.20 annual / €39 monthly; "Max" seats (5x usage) €99-109; volume bands down to €12.80 (Core, 551+ seats). API product billed per token (e.g. Sonnet 4.6 €3/€15 per 1M tokens, EU-hosted). Workflows add-on €449/month per workspace. Enterprise custom for 1,000+ users. FAQ says bringing your own model keys lowers seat price and removes usage limits, but no reduced price is shown. [Langdock pricing](https://www.langdock.com/pricing).
- **Onyx**: Business $20/user/month billed annually (free trial), Enterprise custom with on-prem and region-specific deployment; Community Edition free to self-host. [Onyx pricing](https://onyx.app/pricing); secondary source gives $25 monthly [GoSearch](https://www.gosearch.ai/faqs/onyx-ai-pricing-the-real-open-source-tco-in-2026/) (vendor-adjacent, treat as weak).
- **Dust**: Pro seat reported at $30/month or $24 annual, Max seat $150/$120, credit-based; Enterprise quote-only with ~100-user minimum reported. Secondary sources only, inconsistent across listings. [Orb pricing atlas](https://www.withorb.com/pricing-atlas/dust), [AutomationAtlas](https://automationatlas.io/answers/dust-pricing-explained-2026/).
- **Glean**: no public pricing; third-party estimates $50-75/user/month with ~100-seat minimums, which Glean has not confirmed. Weak evidence. [Activepieces blog](https://www.activepieces.com/blog/glean-pricing-in-2026-cost-seats-and-minimums), [GoSearch](https://www.gosearch.ai/blog/glean-pricing-explained). Not an SMB product in practice.
- **Mistral Le Chat Team** (reportedly renamed "Vibe" on 28 May 2026, single source): $24.99/user/month monthly, $19.99 annual; Enterprise custom with self-hosting. Secondary sources. [Wise guide](https://wise.com/gb/blog/mistral-ai-pricing), [Zemith](https://www.zemith.com/en/learn/mistral-le-chat-pricing).
- **Abacus.AI ChatLLM Teams**: $10/user/month (monthly billing, $7 first month promotion), Pro tier $20, credit-based; billed per invited user with no stated user cap. Official pages. [Abacus ChatLLM Teams](https://chatllm.abacus.ai/), [Abacus billing FAQ](https://abacus.ai/help/chatllm-ai-super-assistant/faqs/billing). This is the closest "cheap multi-model per-seat" price anchor.
- **T3 Chat**: $8/month Pro with a 4-hour resetting usage meter; no official user or revenue numbers found; "traction" claims come from competitor blogs. [Zemith](https://www.zemith.com/en/learn/t3chat-pricing), [Autumn blog on T3's pricing](https://www.useautumn.com/blog/working-with-t3-chat-on-a-new-way-of-pricing).
- **Poe**: compute-point pools; reported tiers $4.99 / $19.99 / $49.99 / $99.99 / $249.99 per month, ~$30 per million points flat; no clear team plan. Aggregator sources disagree on tier names and free allowance. [Activepieces](https://www.activepieces.com/blog/poe-subscription-pricing-2026-plans-and-point-costs.md), [UsagePricing](https://usagepricing.com/blueprint/activity/poe-2026-03-30-packaging).
- **OpenRouter** (the "credits + fee" model): fee on credit purchases 5.5% (Standard) or 8% (Business); token prices equal provider list prices; BYOK has no OpenRouter fee up to $25,000/month list-price inference, 5% above. Enterprise via contract. Primary source. [OpenRouter pricing](https://openrouter.ai/pricing). Third-party pieces citing 1M-request BYOK allowances conflict with this and appear outdated.
- **AnythingLLM Cloud**: reported $50/month (Basic) and $99/month (Pro), BYO LLM key; secondary blog only, unverified. **Msty Studio**: free desktop, paid Aurum reported $149/user/year or $349 lifetime (unverified), Enterprise priced by seat count and deployment; [Msty Enterprise announcement](https://msty.ai/blog/msty-studio-enterprise-plan-announcement), [secondary pricing summary](https://toolradar.com/tools/msty/pricing). **Cherry Studio**: AGPL-3.0 code, enterprise tiers via sales, no published price found. [AIToolsAtlas](https://aitoolsatlas.ai/tools/cherry-studio/pricing).
- **LibreChat**: MIT core; no documented official managed SaaS or commercial tier; one source says ClickHouse acquired LibreChat in November 2025 and says it stays MIT (single secondary source). [TrueFoundry comparison](https://www.truefoundry.com/blog/librechat-vs-open-webui), [dev.co](https://dev.co/ai/mcp/librechat).
- **Open WebUI Enterprise**: pricing by quote only (no public price found); see section 5 for licence.
- **Cohere**: not researched in sufficient depth; no sourced finding.

### Inferences
- Seat-priced competitors cluster at $20-30/seat/month (monthly) with ~20% annual discounts; Abacus ($10) and T3 ($8) show a cheaper end. Any flat fee above roughly $10/seat equivalent has to be justified by something other than "access to many models".
- TypingMind's $99/5-users flat model is the nearest existing analogue to "BYO key plus platform fee"; there is no independent evidence of its customer count or revenue.
- Dust, Langdock and Onyx are the more direct SMB/mid-market competitors for a hosted, governed workspace; they bundle model access so customers do not manage keys.

### Gaps
- No verified traction (users, ARR) for TypingMind, T3 Chat, Msty, Cherry Studio, Abacus ChatLLM, or Open WebUI Enterprise.
- Open WebUI Enterprise, Cherry Studio, Cohere, and Glean price points not published or not found.
- Could not fetch AnythingLLM's own pricing page or Poe's; figures are secondary.

---

## 2. What SMBs pay for ChatGPT/Claude/Gemini/Copilot; SMB adoption, spend, pain points

### Takeaway
Big-vendor list prices for small teams are now low and have no real seat minimum: roughly $20-25/seat for ChatGPT Business and Claude Team (2-seat minimum), about $21 for Copilot Business, and Gemini bundled into Google Workspace from about $14/user. SMB surveys put data privacy/security as the top barrier, and a large share of SMB owners spend nothing on AI tools; shadow AI via personal accounts is widespread but mostly documented in enterprise samples.

### Cited Findings
- **ChatGPT Business**: standard seat $25/user/month monthly or $20 annual (annual price cut by $5 on 2 April 2026 per OpenAI help text as relayed); 2-seat minimum; Premium seat $125 monthly / $100 annual (launched around August 2026); cap of 200 paid seats per Business subscription from 24 Aug 2026. Source is a search synthesis citing OpenAI's help centre (help pages themselves returned 403 to my fetch); one source conflict on whether Premium exists. [OpenAI help: manage billing](https://help.openai.com/en/articles/8792536-manage-billing-on-chatgpt-team), [AI Business](https://aibusiness.com/generative-ai/new-premium-tier-for-chatgpt-business). ChatGPT Enterprise pricing is unpublished; $45-75/seat is an unofficial estimate [Coworker.ai](https://coworker.ai/blog/chatgpt-enterprise-pricing).
- **Claude Team**: announced 28 January 2026: Standard $20/seat annual or $25 monthly; Premium $100 annual / $125 monthly (5x usage). [Anthropic: Updates to Claude Team](https://claude.com/resources/articles/claude-team-updates). Minimum seats cut from 5 to 2 and a 150-seat cap per third-party coverage (page itself does not state it; older pages still say 5). [Pillitteri](https://pasqualepillitteri.it/en/news/8545/claude-team-2-seats-small-teams), [Krater](https://krater.ai/blog/claude-team-plan-pricing).
- **Microsoft 365 Copilot Business**: launched 1 December 2025 at $21/user/month for organizations up to 300 users, no seat minimum (down from $30); promotions and bundles changed during 2026 and sources conflict on bundle prices. [Office Watch](https://office-watch.com/2025/microsoft-365-copilot-business-ai-add-on/), [SoftwareOne](https://www.softwareone.com/en/channel-partner/articles/2026/05/26/lower-copilot-prices-bigger-partner-opportunity).
- **Gemini in Google Workspace**: bundled; Business Standard reported $14/user/month annual, $16.80 monthly (third-party October 2026 reviews, no Google page fetched); Gemini was a $20 add-on before January 2025. [Dupple](https://dupple.com/learn/google-workspace-pricing), [eesel](https://www.eesel.ai/blog/gemini-workspace-pricing).
- **Adoption (EU)**: Eurostat 2025: 20% of EU enterprises (10+ employees) used AI, up from 13.5% in 2024; small enterprises 17%, medium 30.4%, large 55.0%. [Eurostat Statistics Explained](https://ec.europa.eu/eurostat/statistics-explained/index.php/Use_of_artificial_intelligence_in_enterprises), [Eurostat news](https://ec.europa.eu/eurostat/web/products-eurostat-news/w/ddn-20251211-2).
- **Adoption/spend/barriers (US)**: Bluevine (April 2026, n=942 US small-business owners): 33% spend nothing on AI tools, data security/privacy the top single barrier at 33% (up from 23%). Upwork Q1 2026 (n=195 SMB leaders, 10-99 employees): privacy/security 49% (multi-select). Techaisle/AWS: cybersecurity 53% top barrier. All vendor-sponsored; figures not comparable across surveys. [Bluevine](https://www.bluevine.com/blog/small-business-ai-trends-report-2026), [Upwork](https://www.upwork.com/resources/state-of-ai-in-smbs), [US Chamber report (not read in detail)](https://www.uschamber.com/assets/documents/Empowering-Small-Business-The-Impact-of-Technology-on-U.S.-Small-Business-Small-Business-Report-2026.pdf).
- **Shadow AI**: Netskope reports ~47% of workplace gen-AI users use personal accounts; Verizon 2026 DBIR reports 67% of AI access on corporate devices via personal accounts; Gartner Q1 2026 survey reports 88% of employees with an employer AI tool also use a personal one. These come via secondary summaries and are mostly enterprise samples, not SMB-specific; one aggregator was caught mis-citing. [Infosecurity Magazine](https://www.infosecurity-magazine.com/news/personal-llm-accounts-drive-shadow), [StationX](https://app.stationx.net/articles/shadow-ai-statistics).

### Inferences
- At $20/seat/month annual and 2-seat minimums, a 10-person firm pays about $2,400/year to OpenAI or Anthropic. A BYO-key workspace must beat that on total cost to win on price; for light users, API spend is often well below $20/seat, but heavy users can exceed it (see section 3).
- Pain point supported by evidence: data control and security. Cost as a barrier is weakly supported (survey wording varies; GTIA found security ahead of cost). The "pay for what you use" pitch is therefore better aimed at light/uneven users and at firms wanting control, not at "ChatGPT is too expensive".

### Gaps
- No SMB-specific survey found on willingness to pay for usage transparency, or on discounting of ChatGPT/Claude/Copilot for small teams.
- No clean 2026 US figure for share of SMBs using gen-AI.
- Google pricing page and Anthropic pricing page were not fetched directly.

---

## 3. Pricing-model analysis: BYO key + fee vs per-seat vs markup vs flat

### Takeaway
Market evidence favours (a) per-seat bundles at $20-30 for mainstream SMBs, (b) flat team fees with API passthrough (TypingMind) for the technical niche, and (c) low single-digit-percent fees on credits/BYOK for pure routers (OpenRouter). The one clear failure signal found is usage-based surprise billing (Cursor 2025), which supports transparency and spend caps as a feature, but I found no direct evidence of customers paying a premium for transparency alone.

### Cited Findings
- **Credits + percent fee**: OpenRouter charges 5.5% (Standard) or 8% (Business) on credit purchases, and BYOK is free up to $25k/month list-price usage then 5%. [OpenRouter pricing](https://openrouter.ai/pricing). Third-party coverage says OpenRouter signalled a future move from the BYOK percentage to a fixed monthly subscription (weak, single secondary source). [Dupple](https://dupple.com/learn/openrouter-pricing)
- **Flat platform fee + passthrough**: TypingMind Teams from $99/month for 5 users, keys and usage billed directly by provider. [TypingMind docs](https://docs.typingmind.com/typingmind-team/getting-started/typingmind-team-vs-claude-team)
- **Seat + usage hybrid**: Langdock (seats plus API tokens plus workflows add-on), Dust (seats plus credits), Abacus (seat plus credits), Poe (points). [Langdock](https://www.langdock.com/pricing), [Abacus](https://abacus.ai/help/chatllm-ai-super-assistant/faqs/billing)
- **Vendor-side price changes in token supply**: DeepSeek raised V4 API prices from 13 August 2026 (V4 Pro now $0.66/$1.98 per M tokens off-peak, $1.32/$3.96 peak, up from $0.435/$0.87; Flash $0.22/$0.66 off-peak vs $0.14/$0.28), citing demand outpacing compute; analysts quoted say Anthropic raised prices in April for a similar reason. [InfoWorld](https://www.infoworld.com/article/4209439/deepseek-raises-some-v4-prices-by-more-than-10x-as-ai-demand-strains-capacity.html). Another secondary source cites V4.1 Flash at $0.30/$1.20 peak since 10 September 2026. [Puter](https://developer.puter.com/tutorials/deepseek-api-pricing/) (conflicts with InfoWorld's Flash figures; could not verify on DeepSeek's own page).
- **Usage-pricing backlash**: Cursor's June 2025 shift from request limits to a $20 credit pool caused surprise charges, an apology and refunds; users could later set spending limits. Backlash was mainly about unclear communication. [Yahoo Finance/AP-style report](https://finance.yahoo.com/news/cursor-apologizes-unclear-pricing-changes-225709399.html), [SaaStr](https://www.saastr.com/cursor-our-users-love-per-seat-pricing-its-just-the-cost-side-makes-it-harder). SaaStr's headline claims users love per-seat pricing and the pain is on the vendor's cost side (commentary, not data). Tessl notes AI vendors converge on hybrid subscription+usage. [Tessl](https://tessl.io/blog/cursor-new-pricing-structure-explained)
- **Poe** shows buying points gives no per-point discount (~$30/M points across tiers), i.e. a pure pass-through-ish margin model. [Activepieces](https://www.activepieces.com/blog/poe-subscription-pricing-2026-plans-and-point-costs.md) (secondary)

### Inferences
- Token markup (5-8%) is defensible only for a router with bulk credits; for a self-hosted/BYO-key product it is hard to apply because the customer pays the provider directly. The user's "customers pay API cost directly" model therefore pushes monetisation to a flat workspace/platform fee or per-seat fee, which matches TypingMind's structure.
- Cheaper models (DeepSeek, GLM, Kimi) are being repriced upward (DeepSeek Aug 2026), so a "cheap Chinese model" cost advantage may narrow; cost-per-task routing should be re-measured, not assumed.
- Always-visible cost plus spend caps directly address the documented Cursor failure mode, which is a plausible differentiator, but its monetisable value is unproven.

### Gaps
- No evidence found of SMBs paying a premium specifically for token-cost transparency; no published churn or conversion data for any BYO-key product.
- Replit and other 2026 usage-pricing outcomes only touched in passing.

---

## 4. Data, security and compliance for Chinese-hosted APIs (US and EU)

### Takeaway
Private-sector use of Chinese APIs is not illegal in the US or EU, but the risk surface is real and growing: federal procurement bans now reach contractors, EU regulators call DeepSeek's China transfers unlawful for the consumer app, and DeepSeek's policy states PRC storage with training allowed unless opted out and no published retention or zero-retention option. The user's belief that "SMBs don't mind" is plausible for low-sensitivity SMBs but wrong for regulated, public-sector-adjacent, and EU-personal-data segments.

### Cited Findings
- **DeepSeek privacy policy**: states "we directly collect, process and store your Personal Data in People's Republic of China"; model training listed as a purpose with an opt-out right (via email, no in-app mechanism described); no fixed retention period; no separate API/Open Platform retention or training terms stated. [DeepSeek privacy policy](https://cdn.deepseek.com/policies/en-US/deepseek-privacy-policy.html). Third-party sources disagree on whether the paid API trains on inputs; none cite a primary API term. [Meetily summary](https://meetily.ai/llm-privacy/deepseek)
- **US federal**: FY2026 NDAA (enacted 18 Dec 2025) required DoD to issue an exclusion order for DeepSeek; DHS Exclusion and Removal Order #2026-01 (dated 24 July 2026, Federal Register 20 Oct 2026) bars DeepSeek, affiliates and covered third-party products from civilian procurement and removal from systems; extends to contractors and firms dealing with primes (flow-down via FAR 52.204-30 per law-firm alerts); DoD order 8 Sept 2026. Private-sector use is not restricted. [CRS In Focus IF13336](https://www.everycrsreport.com/reports/IF13336.html), [Wiley alert](https://www.wiley.law/alert-DeepSeek-Ban-Creates-New-Compliance-and-Reporting-Obligations-for-Contractors), [Akin Gump](https://www.akingump.com/en/insights/ai-law-and-regulation-tracker/dhs-orders-exclusion-and-removal-of-deepseek-products-from-federal-civilian-agency-systems). Commentators flag uncertainty about AI gateways that route to DeepSeek models. (CRS page has internal date inconsistencies; dates should be verified against the Federal Register.)
- **US states**: at least 17 states have some government-device ban per a BGR tally (Texas first, 31 Jan 2025). [BGR](https://bgr.com/2014815/deepseek-illegal-us-states), [TechCrunch](https://techcrunch.com/2025/02/03/deepseek-the-countries-and-agencies-that-have-banned-the-ai-companys-tech)
- **EU/Italy/Germany**: Italy's Garante imposed an immediate processing limitation on 30 Jan 2025; Berlin's DPA asked Apple/Google in June 2025 to remove the app, saying the transfer to China breaches GDPR Art. 46(1) because no adequacy decision exists and safeguards weren't shown, citing Chinese government access powers. These concern the consumer app; regulator positions, not court rulings, and legal theory is contested. [Heise](https://heise.de/-10462419), [Silicon UK](https://www.silicon.co.uk/mobility/mobile-apps/deepseek-faces-app-store-ban-in-germany-after-data-transfer-criticism-619998), [Euroconsumers](https://www.euroconsumers.org/?p=6707), [Jan 2026 retrospective PDF](https://ai-regulation.com/wp-content/uploads/2026/01/DeepSeek-One-Year-Later.pdf)
- **Security evaluations**: NIST CAISI (Sept 2025) found DeepSeek models lag US models and are more susceptible to hijacking and CCP-narrative echoing; May 2026 evaluation of V4 Pro says it lags the frontier by ~8 months; critics say the methodology was selectively framed. [TechRepublic](https://www.techrepublic.com/article/news-deepseek-security-gaps-caisi-study/), [Decrypt](https://decrypt.co/366685/bitcoin-ethereum-metaverse-tokens-sink-further-after-holiday-crypto-rally?amp=1) (secondary; the NIST primary page was not read).
- **Corporate sentiment**: hundreds of companies blocked DeepSeek within days in Jan 2025; Fox Rothschild blocked it for attorneys. Experts quoted by SCMP expect the federal ban to deter wider US business adoption (opinion). [TechCrunch](https://techcrunch.com/2025/01/31/hundreds-of-companies-are-blocking-deepseek-over-china-data-risks), [Bloomberg Law](https://news.bloomberglaw.com/legal-ethics/fox-rothschild-blocks-deepseeks-ai-model-for-attorney-use), [SCMP](https://www.scmp.com/tech/big-tech/article/3371649/washingtons-deepseek-ban-may-deter-us-firms-adopting-chinese-ai-models-experts)
- **US-hosted open-weight alternatives**: Together AI lists roughly Kimi K2.6 $1.20/$4.50, GLM-5.x $1.40/$4.40, DeepSeek V4 Pro $1.74/$3.48 per M tokens (aggregator; sources disagree; US-only hosting not confirmed). [AIPricing.guru](https://www.aipricing.guru/together-pricing/), [Together pricing](https://www.together.ai/pricing-capacity). Compare to DeepSeek's own V4 Pro at $0.66-$1.32 input / $1.98-$3.96 output after August 2026 ([InfoWorld](https://www.infoworld.com/article/4209439/deepseek-raises-some-v4-prices-by-more-than-10x-as-ai-demand-strains-capacity.html)). Langdock sells EU-hosted access to mainstream models at near-list prices (Sonnet 4.6 €3/€15). [Langdock](https://www.langdock.com/pricing)

### Inferences
- The same open weights (DeepSeek, Kimi, GLM) run on US/EU hosts like Together/Fireworks avoid the China-storage issue; based on the aggregator numbers the price premium over DeepSeek's own API now looks modest (roughly 1-3x on input depending on tier and peak/off-peak), though this is not verified and varies by model. This would let the product offer "Chinese-lab models, Western hosting" as a default and gate first-party Chinese APIs behind an explicit admin toggle.
- Segments likely to object: law (client confidentiality), health (HIPAA-adjacent), finance, defense/federal contractors (direct FAR/NDAA exposure), anyone processing EU personal data (Chapter V transfer). Segments likely fine: marketing, e-commerce, agencies, dev shops with non-sensitive content.
- A reseller that routes customer data to a Chinese provider on its own default could inherit processor liability; making routing a customer-controlled, per-workspace policy shifts that responsibility.

### Gaps
- No primary DeepSeek/Moonshot/Z.ai/Alibaba API terms (retention, training on API data) retrieved beyond the DeepSeek privacy policy; Moonshot, Z.ai and Alibaba policies not checked.
- No authoritative guidance found on EU API customers (controller) sending personal data to DeepSeek; only consumer-app enforcement.
- No finance/health-sector regulator guidance on Chinese LLM APIs found; no SMB survey on Chinese-API sentiment (user's belief is untested).
- Kimi/GLM-specific government actions not found in this research.

---

## 5. Open-source licence implications for resale; liability; deployment models

### Takeaway
MIT (LibreChat) permits commercial resale and hosted SaaS with only notice retention. Open WebUI (v0.6.6+) allows charging for access but forbids removing its branding above 50 users without a paid enterprise licence, so white-labelling it is not free. AGPL components (Cherry Studio; reportedly the LibreChat admin panel) require source disclosure for network-served modifications. Writing a proprietary workspace from scratch avoids these constraints.

### Cited Findings
- **Open WebUI**: licence since v0.6.6 (April 2025) is BSD-3 plus branding restriction; not OSI-approved; branding must stay unless: 50 or fewer users in a 30-day period, written permission for substantive contributors, or a paid enterprise licence. "You MUST get an enterprise or proprietary license before removing our branding for mass redistribution or resale"; charging for access is allowed if branding kept; co-branding prohibited; paid SaaS forks must carry a "not affiliated" disclosure. Code through v0.6.5 remains BSD-3. [Open WebUI licence page](https://docs.openwebui.com/license/). Third-party sources vary on the user threshold wording (50 vs 51); official page says 50 or fewer is exempt. [WZ-IT analysis](https://wz-it.com/en/blog/open-webui-license-branding-business/)
- **LibreChat**: core MIT; commercial deployment, modification and resale allowed with notice retention; one comparison says the Admin Panel is AGPL-3.0 and the code interpreter Apache-2.0, conflicting with "pure MIT" claims elsewhere, so repository licence files must be checked. [WZ-IT comparison](https://wz-it.com/en/blog/open-webui-vs-librechat-comparison/), [dev.co](https://dev.co/ai/mcp/librechat)
- **Cherry Studio**: AGPL-3.0 code. [AIToolsAtlas](https://aitoolsatlas.ai/tools/cherry-studio/pricing) (secondary)
- **TypingMind**: closed source; self-host build licensed for use only, no modification or redistribution. [TypingMind buy](https://www.typingmind.com/buy)
- **Deployment models in market**: Onyx offers managed cloud plus free self-host plus on-prem enterprise; Langdock offers EU-hosted SaaS with dedicated deployment for enterprise; TypingMind Teams is vendor-hosted custom-branded workspace; Msty Enterprise advertises isolated infrastructure. [Onyx](https://onyx.app/pricing), [Langdock](https://www.langdock.com/pricing), [Msty](https://msty.ai/blog/msty-studio-enterprise-plan-announcement)

### Inferences
- If the user's workspace is their own code, there is no upstream licence constraint; if it forks Open WebUI they need an enterprise licence (price unpublished) to rebrand once any customer exceeds 50 users.
- Customer-own-cloud deployment (customer holds data and keys) minimises the user's liability (no hosted customer data, no key custody) but raises support cost and weakens recurring revenue; vendor-hosted raises GDPR processor obligations (DPA, subprocessor list, breach notification), SOC 2/ISO-type questionnaires from SMB buyers, and the Chinese-routing issue above. A hybrid (vendor-hosted control plane, keys stored client-side as TypingMind does) is a precedent.

### Gaps
- No legal analysis found specific to reselling AGPL/MIT software with BYO keys, or to processor liability for AI workspaces; no sourced SaaS liability/insurance cost. Primary LICENSE files not read.

---

## 6. Unit economics sketch

### Takeaway
Infrastructure per customer is tiny (single-digit to low-double-digit euros per month); the real cost is the founder's support and compliance time. At plausible fees ($99-300/month per customer account), break-even for a part-time income is in the tens of customers, but the market anchors (TypingMind $99/5 users, Onyx $20/seat) cap what can be charged. All arithmetic below is my own and uses stated assumptions.

### Cited Findings (inputs)
- **Hosting prices (EU, excl. VAT, volatile)**: Hetzner raised cloud prices on 1 April 2026 and again for CPX/CCX lines from 15 June 2026; reported CX22 €3.29 to €4.49 and CPX11 €3.85 to €5.49 in April; CX23 reported €2.99 at launch, €5.49 by June and sometimes unavailable; IPv4 €0.50/month extra; some larger lines up sharply. Hetzner's cloud page shows entry shared plans from €5.49-€5.99/month and dedicated-vCPU from €36.99/month. Secondary figures conflict. [Hetzner cloud page](https://www.hetzner.com/cloud/), [Cloudron forum](https://forum.cloudron.io/topic/15111/hetzner-price-increases-by-20-30-other-hosting-providers-soon-to-follow/26), [Bitdoze](https://www.bitdoze.com/hetzner-cloud-cost-optimized-plans/), [WZ-IT on June increase](https://wz-it.com/en/blog/hetzner-price-increase-june-2026-cpx-ccx-alternatives/), [Findstack](https://findstack.com/resources/hetzner-price-increase-2026)
- **Competitor fee benchmarks**: TypingMind Teams $99/5 users; Onyx $20/user; Langdock €23.20/user; Abacus $10/user; ChatGPT Business/Claude Team $20/user annual (all cited above).
- **Payment/overhead**: not researched (Stripe fees, accounting, insurance, SOC 2 costs not sourced).

### Inferences (my arithmetic, assumptions stated)
- Hosting: one 4-8 GB VM (roughly €10-40/month based on the shared-plan range above) can plausibly host several small tenants of a lightweight app (database, app server, no GPU since inference is API-based), so infra is about €2-15 per tenant per month, under 5% of a $99+ fee. Assumption: ~10 active users per tenant, light usage. Not benchmarked.
- Support/ops: if each SMB consumes ~1-2 hours/month of founder time (onboarding, key issues, outages), at a notional $50/hour that is $50-100/month, which dominates hosting. This is an assumption with no source.
- Fee scenarios (illustrative):
  - Flat $99/month per workspace (TypingMind-like, 5 users included): gross margin roughly $80-90 after infra/payments; to net $5,000/month before support time needs about 55-60 customers.
  - $12/seat/month, average 10 seats = $120/month: about 45 customers for $5,000/month.
  - $20/seat (Onyx price) at 10 seats = $200/month: about 25-28 customers, but you then compete head-on with Onyx, ChatGPT Business and Claude Team at the same price while adding key-management work for the customer.
  - Token markup of 5% on a $60/month average API bill = $3/month per customer, immaterial; markup alone cannot fund the business unless you bundle credits at scale (OpenRouter's model relies on large volume; no volume benchmark found).
- Customer acquisition cost, churn and support-load assumptions are unsourced; real break-even is longer if SMBs churn when the novelty fades or ask for SSO/SOC 2.

### Gaps
- No sourced SMB SaaS CAC/churn benchmarks, support-time data, payment fees, insurance, or compliance (SOC 2/ISO 27001) costs gathered.
- Hetzner's current exact price list could not be retrieved (docs page 404; cloud page lacked specs); AWS/Azure/other EU provider prices not collected.

---

## Cross-cutting assessment (for the report writer)

### Takeaway
Commercialisation looks feasible as a niche product (technical or privacy-conscious micro-SMBs, agencies, dev shops, EU firms wanting control) at a modest flat or per-seat fee, but weakly supported as a mass-market ChatGPT replacement. The "Chinese APIs are fine" assumption should be replaced by a customer-controlled routing policy with Western-hosted open-weight defaults.

### Inferences
- A subscription/fee is justifiable if it buys things customers cannot get from BYO key alone: hosting and updates, shared prompts/agents, admin spend caps and per-user usage analytics, governed routing, and an audit trail. The TypingMind comparison page lists exactly these (role-based access, token usage analytics, SSO, per-user limits) as differentiators versus Claude Team (vendor claim).
- Main risks: competition from bundled big-vendor seats at $20-25 with no minimums; DeepSeek and other cheap-API price rises; regulatory exposure when routing to Chinese hosts; unverified demand for BYO-key; support burden of key management for non-technical SMB users; Open WebUI licensing if forked.

### Gaps
- No primary evidence of paying SMB demand for BYO-key tools beyond TypingMind's continued existence; recommend customer-discovery interviews and a pricing test as the next step.
