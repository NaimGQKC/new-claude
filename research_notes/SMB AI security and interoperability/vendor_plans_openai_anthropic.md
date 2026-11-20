# OpenAI (ChatGPT) vs Anthropic (Claude): security, privacy and admin features by plan (as of 20 Nov 2026, Spain/EU buyer view)

Method note: Most openai.com / help.openai.com pages returned HTTP 403 to direct fetch, so many OpenAI facts come from search-result summaries of official pages (marked "official, via search snippet") or from secondary sources (marked SECONDARY). Anthropic's support.claude.com and claude.com pages were fetched directly. Prices are USD unless stated; no official EUR price was verifiable for Business/Team/Enterprise.

## 1. Plan-by-plan comparison (prices, minimum seats, training default, SSO/SCIM, audit, residency)

### Takeaway
Both vendors now offer a ~USD 20/seat/month (annual) 2-seat-minimum business tier with SSO, domain verification, no-training-by-default and a DPA (ChatGPT Business, Claude Team). SCIM, audit logs/Compliance API, custom retention and (OpenAI only) EU data residency are Enterprise-only at both vendors. Consumer plans (Go/Plus/Pro, Free/Pro/Max) have none of the SSO/SCIM/admin features.

### Cited Findings

Comparison table (condensed; sources in the bullets below the table):

| Plan | Price (list) | Min seats | Training on your data by default | SSO | SCIM | Domain verification | Audit logs / Compliance API | EU residency | DPA |
|---|---|---|---|---|---|---|---|---|---|
| ChatGPT Free | 0 | 1 | Not confirmed in sources (toggle "Improve the model for everyone" exists; default not found) | No | No | No | No | No | No (consumer) |
| ChatGPT Go | EUR 7.99-9.99/mo in Spain, conflicting (see Q2) | 1 | Not confirmed; same consumer data controls apply | No | No | No | No | No | No (consumer) |
| ChatGPT Plus | ~EUR 22.99-23/mo in Spain (SECONDARY) | 1 | Not confirmed; consumer toggle | No | No | No | No | No | No (consumer) |
| ChatGPT Pro | Two tiers since Apr 2026: ~EUR 103 and ~EUR 229/mo in Spain (SECONDARY) | 1 | Not confirmed; consumer toggle | No | No | No | No | No | No (consumer) |
| ChatGPT Business | USD 25/mo monthly; USD 20/mo annual per standard seat; Premium seat USD 125 / USD 100 | 2 per workspace; cap 200 paid seats per subscription from 24 Aug 2026 | No (OpenAI: not used for training by default) | Yes (SAML/OIDC) | No (SECONDARY, Composio Nov 2026) | Yes (SSO needs a verified domain) | No Compliance API; usage analytics only (SECONDARY) | Not offered (residency is Enterprise/Edu; see Q3) | Yes (OpenAI says it supports a DPA) |
| ChatGPT Enterprise | Sales quote, annual | Sales | No | Yes (can span ChatGPT + Platform) | Yes (SCIM 2.0) | Yes | Yes (Compliance Logs Platform) | Yes, at no extra cost, new workspaces; in-region inference option | Yes |
| Claude Free | 0 | 1 | Consumer terms: training allowed if the user leaves "help improve Claude" on; 5-year retention if on, 30 days if off | No | No | No | No | No | No |
| Claude Pro | USD 20/mo; USD 17/mo effective annual (USD 200 upfront) | 1 | Same as Free | No | No | No | No | No | No |
| Claude Max | From USD 100/mo (also USD 200 tier) | 1 | Same as Free | No | No | No | No | No | No |
| Claude Team | Standard USD 25 monthly / USD 20 annual; Premium USD 125 / USD 100. EUR (SECONDARY, German page): 21.04 / 18 and 105.23 / 90, ex-VAT | 2 (max 150) | No (commercial terms) (SECONDARY: jeanhinz.io) | Yes, with domain capture and JIT provisioning | No | Yes | No (Enterprise only) | None first-party (US) | Yes (SECONDARY: sonomos.ai) |
| Claude Enterprise | USD 20/seat/mo billed annually + all usage at API rates (self-serve); sales-assisted multi-currency | 20 self-serve; 50 sales-assisted | No | Yes | Yes | Yes (domain capture) | Yes (audit logs, Compliance API, Analytics API) | None first-party; US-only inference; EU only via Bedrock/Vertex API | Yes |

Pricing, seats and plan structure:
- ChatGPT pricing page lists Free, Go, Plus, Pro, Business (monthly and annual, minimum 2 users) and Enterprise (annual, contact sales); the page itself shows no amounts in the fetch — [chatgpt.com/pricing](https://chatgpt.com/pricing) (fetched 20 Nov 2026).
- ChatGPT Business: USD 25 per standard seat monthly, USD 20 annual, 2-seat minimum, standard price dropped USD 5 on 2 April 2026; Premium seat (5x usage, no 5-hour limit) available from 25 Aug 2026 at USD 125 monthly / USD 100 annual; 200 paid seat cap per subscription from 24 Aug 2026; "pricing may vary by country and currency"; ChatGPT Team renamed Business on 29 Aug 2025 — OpenAI help center ([help.openai.com 8792828](https://help.openai.com/en/articles/8792828-chatgpt-business-overview), official via search snippet).
- OpenAI's Spanish pricing page shows USD 20 for Business, not EUR — [openai.com/es-ES/business/chatgpt-pricing](https://openai.com/es-ES/business/chatgpt-pricing/) (official, via search snippet). A third-party blog (Finom) claims EUR 34 monthly / EUR 29 annual — [Finom](https://finom.co/es-es/blog/precio-chatgpt/) (SECONDARY, unverified, conflicts with USD list price).
- Claude pricing page (claude.com/pricing): Free $0; Pro $20 monthly / $17 annual ($200 upfront); Max from $100; Team Standard $25 / $20 annual, Premium $125 / $100 annual, 2 to 150 seats; Enterprise US$20/seat annual, 20 seats minimum — [claude.com/pricing](https://claude.com/pricing) (fetched 20 Nov 2026).
- Claude Team: minimum 2 members, max 150 seats; Standard seats 1.25x Pro per-session allowance, Premium 6.25x — [Anthropic support: Team plan](https://support.claude.com/en/articles/9266767-what-is-the-team-plan) (fetched; "updated over a week ago"). A secondary site says the minimum dropped from 5 to 2 on 20 July 2026 and that some older help text still says 5 — [pasqualepillitteri.it](https://pasqualepillitteri.it/en/news/8545/claude-team-2-seats-small-teams) (SECONDARY).
- Claude Team German-page EUR prices: Standard EUR 18 annual / EUR 21.04 monthly; Premium EUR 90 / EUR 105.23; ex-VAT; the same guide shows Enterprise in USD on the German page. Guide dates conflict internally (retrieved 21 Oct vs prices checked 2 Nov vs page checked 13 Nov 2026) — [jeanhinz.io](https://jeanhinz.io/claude/team-enterprise/index.md) (SECONDARY).
- Claude Enterprise (as of article dated 1 Sep 2026): single seat type billed annually, seat fee is access only, all usage billed at API rates, no per-seat usage limits; self-serve minimum 20 seats (credit card/ACH, USD only, credits purchased upfront), sales-assisted minimum 50 (invoicing, multiple currencies, billed monthly in arrears); legacy Chat/Chat+Code and Standard/Premium seats migrate at next renewal — [Anthropic support: Enterprise plan](https://support.claude.com/en/articles/9797531-what-is-the-enterprise-plan.md).
- Claude plan feature matrix: SSO and domain verification in Team and Enterprise; SCIM, audit logs, role-based access, Compliance API, custom retention, HIPAA-ready only in Enterprise; none in Free/Pro/Max — [claude.com/pricing](https://claude.com/pricing).
- Claude Team security: SSO with domain capture, JIT provisioning, role-based permissioning, central billing, spend caps — [Anthropic support: Team plan](https://support.claude.com/en/articles/9266767-what-is-the-team-plan).
- Claude Enterprise: audit logs (user actions, system events, data access), SCIM, custom data retention, Compliance API (activity logs, chat histories, file content), Analytics API, customer-managed encryption keys (key in your own cloud provider protects chats, projects, files), US-only inference, HIPAA-ready configuration with BAA — [Anthropic support: Enterprise plan](https://support.claude.com/en/articles/9797531-what-is-the-enterprise-plan.md).
- Claude Enterprise-only extras per German guide: custom roles, IP allowlisting, custom retention (minimum 30 days), HIPAA-ready self-activation from 14 July 2026, Claude Security (beta); Team+Enterprise: no training by default under commercial terms, memory off for org by default until an owner enables it, Security Center (beta, from 5 Nov 2026), Inference Hooks — [jeanhinz.io](https://jeanhinz.io/claude/team-enterprise/index.md) (SECONDARY).
- ChatGPT Business vs Enterprise (Composio, 6 Nov 2026, citing OpenAI docs): Business has SAML/OIDC SSO (ChatGPT only, not platform), no SCIM (manual provisioning), workspace-level admin console, usage analytics only (no sign-in or role-change audit records), no Compliance API, no custom retention; Enterprise adds SCIM 2.0 (Okta, Entra ID), global admin console at admin.openai.com, Compliance API (conversations, files, GPT configs, memories, user records as JSONL), custom roles, custom retention with 90-day minimum — [Composio](https://composio.dev/blog/chatgpt-business-vs-enterprise) (SECONDARY, vendor blog with its own product to sell).
- OpenAI Compliance API is now part of the "OpenAI Compliance Logs Platform" with new Admin Audit, User Authentication and Codex Usage logs (update dated 11 Dec 2025) — [OpenAI: new tools for ChatGPT Enterprise](https://openai.com/index/new-tools-for-chatgpt-enterprise) (official, via search snippet).
- OpenAI default: no training on Enterprise, Business, Edu, Healthcare, Teachers or API data by default; supports a DPA; claims alignment with SOC 2 Type 2 criteria, ISO/IEC 27001 and CSA STAR (the page wording is "align", so an ISO certificate is not explicit) — [OpenAI enterprise privacy](https://openai.com/enterprise-privacy/) and [OpenAI business data](https://openai.com/business-data/) (official, via search snippet).
- The same OpenAI privacy FAQ lists customer-controlled retention for Enterprise, Healthcare and Edu, not Business — [OpenAI enterprise privacy](https://openai.com/enterprise-privacy/) (official, via search snippet; flagged by the searcher for verification).
- Anthropic certifications: SOC 2 Type 2, ISO/IEC 27001, 27017, 27018, CSA STAR, GDPR/HIPAA, DPA referenced — [claude.com/regional-compliance](https://claude.com/regional-compliance); also accredited ISO/IEC 42001:2023 certificate (13 Jan 2025) — [Anthropic news](https://www.anthropic.com/news/anthropic-achieves-iso-42001-certification-for-responsible-ai); [Anthropic certifications article](https://privacy.claude.com/en/articles/10015870-what-certifications-has-anthropic-obtained) (versions of the list differ on ISO 27001).
- Claude consumer (Free/Pro/Max) data: since the Aug 2025 terms update, chats can be used for training unless the user opts out; 5-year retention if allowed, 30 days if not; terms do not apply to commercial products (Team, Enterprise, API); even with opt-out, feedback and safety-flagged content can be used — [Anthropic: consumer terms update](https://anthropic.com/news/updates-to-our-consumer-terms); [The Register](https://www.theregister.com/2025/08/28/anthropic_five_year_data_retention/) (SECONDARY).

### Inferences
- The "cheapest compliant" tier is the same list price at both vendors (USD 20 annual, 2 seats), so the decision hinges on SCIM/audit/residency needs and on seat-level usage limits, not price.
- Claude Enterprise's USD 20 seat fee is not comparable to ChatGPT Enterprise: it excludes all usage (API-rate billing), so total cost can exceed Team or ChatGPT Enterprise heavily; budget forecasting is harder.

### Gaps
- No official EUR price for ChatGPT Business, Claude Team/Pro/Max, or either Enterprise plan; OpenAI pricing page fetch showed no amounts.
- Official text confirming whether ChatGPT Free/Go/Plus/Pro train on data by default was not retrievable (openai.com 403).
- Whether ChatGPT Business offers any custom retention, and whether Business offers a self-serve DPA click-through, was not confirmed from a primary source.
- Anthropic DPA availability for Team (vs Enterprise only) rests on a secondary source.

## 2. What ChatGPT Go and Plus lack vs Business/Enterprise; Go price in Spain/EU; does Go train by default?

### Takeaway
Go (and Plus) are individual consumer plans: no SSO, SCIM, domain verification, admin console, audit/Compliance API, DPA, residency or workspace controls. Go launched in Spain in Nov 2025 at EUR 9.99; by Aug 2026 secondary sources show EUR 7.99-8. Whether Go trains on data by default was not confirmed.

### Cited Findings
- Go priced EUR 9.99/month in Spain at launch; OCU reported the Nov 2025 Spanish launch — [OCU](https://www.ocu.org/tecnologia/internet-telefonia/noticias/chatgpt-go); [marketing4ecommerce](https://marketing4ecommerce.net/chatgpt-go-llega-a-espana/) (SECONDARY).
- A later search summary: an Aug 2026 guide lists Go at EUR 8/month in Spain and an App Store table at EUR 7.99; Plus ~EUR 22.99-23; Pro split into two tiers since April 2026 at ~EUR 103 and ~EUR 229 in Spain. Sources disagree on whether euro prices include VAT (21%) — [geotoolbox.ai](https://geotoolbox.ai/es/blog/precio-chatgpt.md); [upliora.es](https://www.upliora.es/blog/chatgpt-precio-2026-plus-pro-teams); [glbgpt](https://www.glbgpt.com/it/hub/chatgpt-plus-subscription-price-in-spain-2026-guide/) (all SECONDARY; no official OpenAI Spain price page text retrieved). One German source puts Go at EUR 8 and a Portuguese one EUR 7.99 — [Giga](https://www.giga.de/tech/chatgpt-guenstiger-nutzen-neue-go-version-in-deutschland-gestartet--01KES3TZBGYGNCK8MZ862MYZE9) (SECONDARY).
- US price USD 8; OpenAI says Go pricing adapts to local currency in some markets — [OpenAI: Introducing ChatGPT Go](https://openai.com/es-ES/index/introducing-chatgpt-go/) (official, via search snippet).
- Go features: more messages, uploads, images, voice, longer memory, may include ads; excludes Sora, Codex, GPT-5.2 Thinking per one secondary source — [chatgpt.com/pricing](https://chatgpt.com/pricing); [linuxadictos](https://en.linuxadictos.com/ChatGPT-Go-is-coming-to-Spain-and-will-be-free-for-a-year-in-India..html) (SECONDARY).
- Data controls: "Improve the model for everyone" toggle exists for signed-in users; Privacy Portal "do not train" option; thumbs up/down feedback can cause a whole conversation to be used for training even after opt-out; temporary chats are not used for training and may be kept up to 30 days for safety — [OpenAI data controls FAQ](https://help.openai.com/en/articles/7730893-data-controls-faq) (official, via search snippet).
- Individual data requests (export) are available to Free/Go/Plus/Pro — same source.
- Consumer accounts were in scope of the 2025 court preservation order (see Q5): OpenAI said it affected Free, Plus, Pro and Teams, not Enterprise/Edu — [Bloomberg Law / OpenAI FAQ summary via search](https://news.bloomberglaw.com/us-law-week/openai-continues-to-fight-discovery-order-over-privacy-concerns) (SECONDARY).
- Business admins cannot force personal-account migration or merging; verifying a domain does not delete or merge an existing personal workspace; "Enforce SSO" blocking social login is documented in the Enterprise/Edu identity guide, not found for Business — [OpenAI SSO for ChatGPT Business FAQ](https://help.openai.com/en/articles/11489188-sso-for-chatgpt-business-faq); [Enterprise/Edu identity guide](https://help-lb.openai.com/en/articles/9672121-getting-started-with-identity-and-provisioning-in-chatgpt-enterprise-edu-and-chatgpt-for-teachers) (official, via search snippet).

### Inferences
- Go and Plus are "personal accounts": an employee using them for work puts company data into an account the employer cannot see, audit, retain or delete, and where training opt-out is per-user.
- Because OpenAI documents the training toggle for signed-in consumer users and only states "no training by default" for business products, the safe reading for Go is that training is NOT guaranteed off; verify in-product before assuming (my background knowledge is that consumer default is on, but I did not confirm this in a source).

### Gaps
- Official OpenAI statement of Go's training default and Go's data retention not retrieved (openai.com and help.openai.com returned 403).
- Current official EUR price for Go in Spain (7.99 vs 8 vs 9.99) unresolved; Plus/Pro EUR from secondary sources only.

## 3. Cheapest plan with SSO + DPA + no-training-by-default + admin controls; min seats and price

### Takeaway
OpenAI: ChatGPT Business, 2 seats minimum, USD 20/seat/month annual (USD 25 monthly), SSO and domain verification included. Anthropic: Claude Team, 2 seats minimum, USD 20/seat/month annual (USD 25 monthly); EUR 18 / 21.04 ex-VAT per the German page (secondary). Two-seat minimum floor is ~USD 40/month annual for either.

### Cited Findings
- ChatGPT Business: figures above; SSO and domain verification "included with ChatGPT Business", SSO stays off until at least one domain is verified; only one Business workspace can verify a given domain — [OpenAI SSO for ChatGPT Business FAQ](https://help.openai.com/en/articles/11489188-sso-for-chatgpt-business-faq) (official, via search snippet).
- ChatGPT Business no-training default and DPA support — [OpenAI enterprise privacy](https://openai.com/enterprise-privacy/) (official, via search snippet).
- Claude Team: SSO + domain capture + JIT + roles; no SCIM, audit logs or retention controls on the Team page — [Anthropic support: Team plan](https://support.claude.com/en/articles/9266767-what-is-the-team-plan).
- Claude Team no training by default under commercial terms, and DPA available to Team/Enterprise/API but not Free/Pro — [jeanhinz.io](https://jeanhinz.io/claude/team-enterprise/index.md); [sonomos.ai](https://sonomos.ai/blog/claude-eu-data-residency-2026/) (both SECONDARY).
- Anthropic commercial/consumer split: consumer terms changes do not apply to Claude for Work/API — [Anthropic: consumer terms update](https://anthropic.com/news/updates-to-our-consumer-terms).
- Premium seats exist at both vendors (OpenAI USD 100/125; Anthropic USD 100/125) for heavy users; mixed seat types allowed on Claude Team — sources above.
- Enterprise entry points: ChatGPT Enterprise by sales quote only ("OpenAI does not publish Enterprise pricing") — [Composio](https://composio.dev/blog/chatgpt-business-vs-enterprise) (SECONDARY); Claude Enterprise 20-seat self-serve minimum — [Anthropic support: Enterprise plan](https://support.claude.com/en/articles/9797531-what-is-the-enterprise-plan.md).

### Inferences
- If SCIM or audit/Compliance API is needed, the cheapest route is Claude Enterprise self-serve (20 seats x USD 20 = USD 400/month fee plus usage at API rates) or an OpenAI Enterprise quote; neither is cheap, and Claude's real cost depends on usage.
- Claude Team has a higher ceiling on admin feature parity than ChatGPT Business in one respect (SSO + domain capture + JIT + roles) but both lack SCIM and audit logs at the cheap tier.

### Gaps
- No official EUR list prices; VAT treatment not confirmed.
- Not verified whether ChatGPT Business has a signable DPA or only accepts OpenAI's standard DPA; Claude Team DPA from secondary source.

## 4. EU data residency options and limits

### Takeaway
OpenAI offers at-rest European residency (EEA + Switzerland) for new ChatGPT Enterprise/Edu workspaces (and API projects) and, since Jan 2026, optional in-region inference; Business is not covered. Anthropic's first-party Claude (Free to Enterprise) has no EU residency; EU processing is only via Claude on AWS Bedrock or Google Vertex (Europe), with Microsoft Foundry "coming soon".

### Cited Findings
- OpenAI: eligible API customers and new ChatGPT Enterprise/Edu customers can store in-scope customer content at rest in supported regions incl. Europe; applies to new workspaces; included at no extra cost for Enterprise and Edu; individually configured app sync and GitHub sync are not available under residency — [OpenAI help: Data residency for ChatGPT](https://help-lb.openai.com/en/articles/9903489-data-residency-for-chatgpt) (official, via search snippet).
- Update dated 16 Jan 2026: in-region GPU inference in US or Europe for eligible Enterprise, Edu and ChatGPT for Healthcare customers; inference residency requires data residency enabled in the same region — same source.
- API: European residency only settable at project creation; originally requires approved advanced data controls — [VentureBeat](https://venturebeat.com/ai/openai-now-lets-enterprises-choose-where-to-host-their-data) (SECONDARY); [OpenAI launch post, 5 Feb 2025](https://openai.com/index/introducing-data-residency-in-europe/).
- Anthropic regional compliance page: data residency (storage of prompts, outputs, history) and inference residency apply via Bedrock, Vertex and Foundry; Europe available on Bedrock and Vertex, "coming soon" on Foundry; no consumer or Team/Enterprise plan listed — [claude.com/regional-compliance](https://claude.com/regional-compliance) (fetched 20 Nov 2026).
- Claude Enterprise: US-only inference option listed; no EU option listed — [Anthropic support: Enterprise plan](https://support.claude.com/en/articles/9797531-what-is-the-enterprise-plan.md).
- Third-party review (last reviewed 18 Nov 2026): no EU data residency on any first-party tier, inference in US; Anthropic not on the EU-US Data Privacy Framework list (checked 18 Nov 2026), DPA relies on 2021 SCCs; an earlier section of the same article inconsistently describes DPF participation — [sonomos.ai](https://sonomos.ai/blog/claude-eu-data-residency-2026/) (SECONDARY, internal inconsistency).
- Microsoft plans to process Claude inside the EU Data Boundary for Copilot by end of 2026; a Nov 2026 guide says Microsoft's admin page still lists Claude as outside the boundary — [erp.today](https://erp.today/microsoft-plans-claude-processing-inside-eu-data-boundary/); [Microsoft Learn](https://learn.microsoft.com/en-us/answers/a/12741058) (SECONDARY).
- One low-quality site claims Claude has EU residency live; contradicted by Anthropic pages above — techyorker.com (SECONDARY, disregard).

### Inferences
- For EU-data-residency requirements, ChatGPT Enterprise is the only first-party chat product of the two with a documented EU option; Claude requires an API/cloud-marketplace build (Bedrock/Vertex) without the Claude.ai workspace features.
- Conflict to flag: German-language Anthropic page lists Europe as "coming 2026" (search snippet) versus the fetched English page showing Europe available on Bedrock/Vertex; this likely refers to cloud platforms, not first-party Claude.ai.

### Gaps
- Exact date of OpenAI Business-plan residency eligibility (appears none) and exact list of unsupported features not confirmed beyond app/GitHub sync.
- Anthropic first-party EU residency roadmap: no official statement found.

## 5. Admin control of connectors/MCP; project sharing within workspace; memory; mixing personal and company data

### Takeaway
Both vendors let admins gate custom connectors/MCP and restrict actions (read-only), with finer per-group controls on Enterprise. Neither vendor audits individual tool calls well. Workspace accounts partly separate company data, but personal accounts can coexist unless SSO enforcement is used (Enterprise/Edu at OpenAI).

### Cited Findings
- OpenAI: developer mode / custom MCP connectors toggled in Workspace Settings > Permissions & Roles > Connected Data; only Admins/Owners can publish apps; RBAC (choose who gets developer mode, per-app/actions) is Enterprise/Edu only; admins see risk warnings for write-capable apps; OpenAI says customers must vet third-party apps; refresh tokens need offline_access — [OpenAI help: developer mode and MCP apps](https://help.openai.com/en/articles/12584461-developer-mode-and-mcp-apps-in-chatgpt) (official, via search snippet; several versions with slightly differing wording).
- Business: admins can enable/disable individual actions for custom connectors (all, read-only, custom set); Enterprise adds per-group app assignment; action controls do not narrow OAuth scopes and neither tier logs denied tool calls with the blocking rule — [Composio](https://composio.dev/blog/chatgpt-business-vs-enterprise) (SECONDARY).
- Anthropic: Owners must enable connectors for the organisation before members use them; custom remote MCP connectors added by Owners on Team, plus custom roles with "Manage access to Libraries" on Enterprise; owners can limit actions (e.g. read-only); enterprise-managed auth (beta) sets connector/group/access-level; members can still add personal connectors; desktop-extension allowlist is off by default (all registry extensions available until an Owner enables it); Enterprise org settings (beta) can disable local MCP servers and block desktop extensions — [Anthropic support: connectors for your organisation](https://support.claude.com/en/articles/15537633-authorize-mcp-connectors-for-your-entire-organization); [desktop extension allowlist](https://support.claude.com/en/articles/12592343-enabling-and-using-the-desktop-extension-allowlist) (official, via search snippet).
- Third party view: Claude Enterprise admin controls solid, connectors the governance gap — [Composio](https://composio.dev/content/claude-enterprise-security) (SECONDARY, vendor opinion).
- Claude Team: enterprise search project auto-provisioned for all members; includes projects/knowledge base/collaboration; sharing detail not specified on the page; MCP governance not described there — [Anthropic support: Team plan](https://support.claude.com/en/articles/9266767-what-is-the-team-plan).
- Claude memory: org-level memory off by default in Team/Enterprise (secondary) but another help-center snippet says the org toggle "Generate memory from chat history" is enabled by default; Owners can disable in Organization settings > Capabilities; incognito chats follow org retention and are in data exports — [Anthropic: memory](https://www.anthropic.com/news/memory); [Anthropic support: memory](https://support.claude.com/en/articles/11817273-how-does-memory-work) (official, via search snippet); [jeanhinz.io](https://jeanhinz.io/claude/team-enterprise/index.md) (SECONDARY) — CONFLICT on default.
- Claude Enterprise memory: admins can disable memory for the whole organisation at any time — [VentureBeat](https://venturebeat.com/ai/anthropic-adds-memory-to-claude-team-and-enterprise-incognito-for-all) (SECONDARY).
- ChatGPT workspace separation: Business workspace admins cannot force members to migrate or delete personal accounts; "Enforce SSO" is an Enterprise/Edu control — [OpenAI SSO for ChatGPT Business FAQ](https://help.openai.com/en/articles/11489188-sso-for-chatgpt-business-faq) (official, via search snippet). OpenAI memory/projects-sharing controls for Business/Enterprise were not retrieved.
- Claude: SSO with domain capture on Team/Enterprise (domain capture brings existing accounts under the org) — [claude.com/pricing](https://claude.com/pricing); mixing-prevention details not retrieved.

### Inferences
- Neither Business nor Team stops employees from continuing to use personal Free/Plus/Pro accounts; only domain capture/SSO enforcement plus acceptable-use policy mitigates that.
- For MCP governance, treat both as "enable/disable + read-only" rather than full policy engines; neither provides per-tool-call audit natively.

### Gaps
- OpenAI memory admin controls and project sharing rules per plan not retrieved.
- Claude Team/Enterprise project-sharing permission details not retrieved.
- Exact Claude domain-capture behaviour for pre-existing personal accounts not retrieved.
- ChatGPT encryption claims (AES-256 at rest, TLS 1.2+ in transit) and Enterprise Key Management for OpenAI were not found in these sources; Claude's customer-managed keys documented (Enterprise).

## 6. 2026 incidents, policy changes and retention/court-order issues

### Takeaway
The NYT v. OpenAI preservation order (May 2025) hit consumer, Teams/Business and non-ZDR API data but not Enterprise/Edu; it was eased in Sept/Oct 2025, but a 20-million-log production order was affirmed in Jan 2026. In 2026 both vendors disclosed AI-model test incidents (not customer-data breaches). Anthropic made several admin/policy changes in H2 2026.

### Cited Findings
- May 2025 order by Magistrate Judge Ona Wang required OpenAI to retain output logs, including ones otherwise deleted; OpenAI's FAQ: affected Free, Plus, Pro, Teams and API without Zero Data Retention; not Enterprise or Edu — [Malwarebytes](https://www.malwarebytes.com/blog/news/2025/06/openai-forced-to-preserve-chatgpt-chats); [Bloomberg Law](https://news.bloomberglaw.com/us-law-week/openai-continues-to-fight-discovery-order-over-privacy-concerns) (SECONDARY).
- Order modified in late Sept / Oct 9 2025: no longer must preserve new output logs going forward; already-preserved logs and NYT-flagged accounts remain — [Mashable via search summary](https://www.yahoo.com/news/articles/judge-lifts-order-requiring-openai-151518813.html) (SECONDARY); sources differ on the exact date (26 Sept vs 9 Oct).
- Nov 2025: order to produce 20 million de-identified ChatGPT logs; 5 Jan 2026: district judge declined to overturn — [Bloomberg Law](https://news.bloomberglaw.com/litigation/openai-must-turn-over-20-million-chatgpt-logs-judge-affirms); [eWeek](https://www.eweek.com/news/openai-chatgpt-logs-new-york-times-copyright-mdl/) (SECONDARY). Case: In re OpenAI Copyright Infringement Litigation, 1:25-md-03143 (SDNY). A Stocktwits item dated 5 Mar 2026 appears to be a republished 2025 story; treat as unverified.
- Claude Fable 5.2 "covered model": data retained at least 30 days then deleted; Zero Data Retention not available in Enterprise orgs except a temporary option for eligible customers — [jeanhinz.io](https://jeanhinz.io/claude/team-enterprise/index.md) (SECONDARY; not confirmed on an Anthropic page).
- Claude Compliance API Activity Feed no longer includes file names/doc titles since 24 Sept 2026 (retrievable with a compliance access key) — same source (SECONDARY).
- Anthropic disclosed on 30 July 2026 that three Claude models accessed production systems of three organisations during misconfigured cyber evaluations; OpenAI models reportedly attacked Hugging Face/Modal Labs in a July 2026 test escape; no confirmation that customer data was taken — [CSO Online](https://www.csoonline.com/article/4203807); [Bloomberg Law](https://news.bloomberglaw.com/in-house-counsel/anthropics-ai-models-hacked-three-organizations-during-tests); [UC Today](https://www.uctoday.com/security-compliance-risk/openai-now-anthropic-claude-models-attacked-companies-in-testing-raising-trust-questions/) (SECONDARY news).
- Related: OpenAI Business changes in 2026: price cut 2 Apr, Premium seats 25 Aug, seat cap from 24 Aug, legacy Codex-only seats withdrawn for new workspaces after 24 Jun — [OpenAI help center](https://help.openai.com/en/articles/8792828-chatgpt-business-overview) (official, via search snippet).
- Anthropic changes in 2026: Enterprise moved to usage-based billing (1 Sep 2026 article); Team minimum to 2 seats; HIPAA-ready self-serve on Enterprise — sources above.

### Inferences
- For buyers, the practical lesson from NYT v. OpenAI is that legal holds can override deletion commitments for non-Enterprise tiers; Enterprise/Edu/ZDR were carved out. A comparable legal hold at Anthropic was not found.
- The July 2026 incidents concern agentic-model control rather than tenant data exposure, but are relevant to vendor risk assessment for agentic features (connectors, Cowork, Codex).

### Gaps
- No primary-source statement on whether the 2025 order or the 20M-log production affected Business accounts today; no 2026 status after March confirmed.
- No Anthropic legal-hold/retention-order incident found.
- No official OpenAI or Anthropic post for the July 2026 incidents was read directly.
