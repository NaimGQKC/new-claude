# Vendor plans, security, privacy and admin: Google Gemini (Workspace), Microsoft 365 Copilot / Copilot Chat, Mistral Le Chat (Team/Enterprise) for EU SMBs, as of 20 Nov 2026

Source-quality legend: [P] = primary vendor page fetched directly; [S] = secondary (press / researcher / aggregator); [SS] = a search-tool summary of a vendor page that I could not fetch directly (treat as lower confidence). Pages marked "dated" show the date on the page. Naming note: Microsoft's Learn docs now call the product "Microsoft Copilot" (pages updated Oct-Nov 2026) and mention a "Microsoft 365 E7" SKU; one aggregator says Mistral renamed Le Chat to "Vibe" in May 2026 (unconfirmed by Mistral's own pages I read, which still use "Le Chat").

## 1. What is the cheapest EU SMB-suitable tier of each (SSO + DPA + no training) and what does it cost per user/month? Add-on vs bundled? Minimum seats?

### Takeaway
Google is cheapest-in-effect because Gemini is bundled into every Workspace Business edition (Business Starter EUR 6.80/user/month annual, EUR 8.10 flexible; Standard EUR 13.60 annual / EUR 16.20 flexible), with no separate AI add-on. Microsoft sells Copilot Business as an add-on (EUR 15.60/user/month, paid yearly, ex VAT, per Microsoft's Irish storefront) on top of an eligible Business plan, capped at 300 users; Copilot Chat is free with Entra-based M365 plans. Mistral Team is USD 24.99/user/month monthly (USD 19.99 annual per third-party sources) but SAML SSO is Enterprise-only (quote-based), so the cheapest Mistral tier that meets "SSO" is Enterprise.

### Cited Findings
**Google Gemini / Workspace**
- Official Google table (EUR/USD per user per month): Business Starter EUR 8.10 flexible / EUR 6.80 annual ($8.40 / $7.00); Business Standard EUR 16.20 / EUR 13.60 ($16.80 / $14.00); Business Plus EUR 25.30 / EUR 21.10 ($26.40 / $22.00). Nonprofit discounts continue. [P] — [Google: AI features and pricing updates for Workspace Business editions](https://knowledge.workspace.google.com/admin/billing/ai-features-and-pricing-updates-for-google-workspace-business-editions) (also [support.google.com/a/answer/15400543](https://support.google.com/a/answer/15400543))
- The standalone "Gemini for Workspace" add-on is no longer sold or renewed; add-on charges ended 31 Jan 2025; new pricing for existing subscriptions with more than 10 licences from 17 Mar 2025 and for 1-10 licences from 7 Jul 2025 or at renewal. [P] — same Google page above
- Business Starter, Standard and Plus all list Gemini features across Gmail, Calendar, Chat, Meet, Docs, Sheets, Slides, Vids, Forms and Drive; the Gemini app has "Standard" vs "Pro" access tiers (Pro: 1M-token context vs 32K for Standard). Some features differ by edition (the page's table was hard to map row by row). [P] — same Google page
- Google states Gemini app submissions "aren't reviewed by humans or otherwise used to train models"; interactions in Workspace apps stay within the organization; prompts/outputs are stored with Workspace content; existing data-region policies and DLP apply automatically. [P] — same Google page
- No minimum seat count is stated on Google's page (it only uses a 1-10 licence threshold for price-change timing). Annual/fixed-term plans need a 1-year commitment and cannot be reduced until renewal; flexible plans allow adding/removing users any time. [P] — same Google page
- Conflict on Starter: one search summary of Google's pricing page said Starter has Gemini in Gmail only and Standard has Gemini across Gmail/Docs/Meet [SS]; the fetched Google knowledge page lists AI features across all apps for Starter, Standard and Plus (with some feature-level differences). Verify edition feature matrix in the Admin console. — [SS search result](https://workspace.google.com/pricing?hl=en-GB_uk) vs [P](https://knowledge.workspace.google.com/admin/billing/ai-features-and-pricing-updates-for-google-workspace-business-editions)
- Separate paid product "Gemini Enterprise" (formerly Agentspace-line): Standard/Plus listed from USD 30/seat/month; a "Business" edition for small teams reported at USD 21/seat/month annual (TechCrunch, Oct 2025); one Google support page figure set says Business $24 monthly / $20 annual and Enterprise $36 monthly / $30 annual. Figures conflict; not verified as of Nov 2026. [S/SS] — [TechCrunch, 9 Oct 2025](https://techcrunch.com/2025/10/09/google-ramps-up-its-ai-in-the-workplace-ambitions-with-gemini-enterprise); [support.google.com/a/answer/14700766](https://support.google.com/a/answer/14700766?hl=en)

**Microsoft 365 Copilot / Copilot Chat**
- Microsoft Copilot Business: add-on for organisations with up to 300 users that hold an eligible M365 Business licence (Business Premium, Standard, Basic, Apps for Business, Teams Essentials); annual commitment; max 300 licensed users per tenant; larger orgs use enterprise Copilot licensing. Docs updated 4 Nov 2026. [P] — [Microsoft Learn: License options for Microsoft Copilot](https://learn.microsoft.com/microsoft-365/copilot/copilot-business-faq) (fetched content canonicalised to learn.microsoft.com/en-us/copilot/plan/copilot-license-options)
- Irish Microsoft storefront: Copilot Business "originally from EUR 18.20, now from EUR 15.60 user/month, paid yearly" (ex VAT); bundles: Business Standard + Copilot EUR 20.36; Business Premium + Copilot EUR 27.73 (per user/month, yearly). [SS: search summary of Microsoft page; direct fetch returned HTTP 503] — [Microsoft IE business add-ons page](https://www.microsoft.com/en-ie/microsoft-365/business/additional-services-plans-and-pricing)
- Conflict on EUR price: a Microsoft partner source said a 1 Dec 2025 - 30 Jun 2026 campaign priced Copilot Business at EUR 16.24 after a 15% discount; USD list price is USD 21/user/month and Microsoft said Copilot Business stays at USD 21 after the 1 July (2026) M365 price increases. [S/SS] — [Primend](https://www.primend.com/blog/important-changes-to-microsoft-licences-and-prices-in-2026/); [Microsoft 365 blog, 2 Dec 2025](https://www.microsoft.com/en-us/microsoft-365/blog/2025/12/02/microsoft-365-copilot-business-the-future-of-work-for-small-businesses/). A May 2026 partner article (SoftwareOne) claims lower Copilot prices but flags its own figures as unverified; not used. [SS] — [SoftwareOne](https://www.softwareone.com/en/channel-partner/articles/2026/05/26/lower-copilot-prices-bigger-partner-opportunity)
- Microsoft 365 Copilot Chat (web-grounded chat) is described by Microsoft as available at no additional cost with eligible M365 plans (signed in with Entra ID). [SS] — [Microsoft Learn Copilot overview](https://learn.microsoft.com/sv-se/copilot/overview)
- Copilot Business is the only listed prerequisite path for Business plans; the prerequisite M365 Business Basic/Standard/Premium base licence cost is additional (not researched in EUR here).
- Prompts, responses and data accessed through Microsoft Graph are not used to train foundation LLMs; Copilot complies with GDPR and EU Data Boundary commitments. Learn page dated 9 Jul 2026 (updated 4 Nov 2026). [P] — [Microsoft Learn: Data, privacy and security for Microsoft Copilot](https://learn.microsoft.com/en-us/copilot/microsoft-365/microsoft-365-copilot-privacy)
- Copilot Business FAQ says it follows the data policies set for the organisation's M365 business tenant. [SS] — [Copilot Business FAQ](https://learn.microsoft.com/microsoft/365/copilot/copilot-business-faq)

**Mistral Le Chat**
- Mistral pricing page (fetched; shown in USD even with currency=eur param): Free; Pro USD 14.99/month; Team USD 24.99 per user/month ex taxes (page also shows "$50/mo" for users, which may imply a 2-seat minimum — my inference, unconfirmed); Enterprise custom/quote. [P] — [mistral.ai/fr/pricing](https://mistral.ai/fr/pricing/?currency=eur)
- Third-party guides give Team USD 19.99 per user/month on annual billing (Wise guide) and speculate Enterprise at "USD 20K+/month" (an aggregator estimate, unofficial). [S] — [Wise: Mistral pricing guide](https://wise.com/gb/blog/mistral-ai-pricing)
- Features listed under Team/Enterprise on pricing page: domain verification, data export, up to 30 GB storage per user, knowledge connectors, admin API, audit logs, SAML SSO (cells were unclear about which plan has which). [P, partially legible]
- Mistral docs state: "You need an Enterprise plan to configure SAML SSO"; Team gets domain verification only; SAML 2.0 only, OIDC not supported; SCIM provisioning is in "private preview"; automatic Team seat assignment on first SSO sign-in is possible. [P] — [Mistral docs: SSO](https://docs.mistral.ai/admin/security-access/sso)
- Mistral says Le Chat Enterprise includes an admin interface with RBAC and SCIM user provisioning (official feature list surfaced via search; the help article itself returned 404 on direct fetch). Conflict with docs page labelling SCIM "private preview". [SS] — [help.mistral.ai Enterprise features](https://help.mistral.ai/en/articles/347544-what-features-are-included-in-le-chat-enterprise) vs [P] [Mistral SSO docs](https://docs.mistral.ai/admin/security-access/sso)
- No-training default for Team/Enterprise: the pricing page has a "model training" row but the values did not extract; not verified. See Gaps.

### Inferences
- Cheapest "SSO + DPA + no training" paths: (a) Google Workspace Business Starter at EUR 6.80/user annual (Workspace has Google SSO natively; Gemini bundled; the Gemini app no-training statement applies) — no separate AI line item; (b) Microsoft: base M365 Business Basic/Standard (with Entra ID SSO) plus Copilot Business EUR 15.60 for the paid M365 Copilot, or EUR 0 extra for Copilot Chat; (c) Mistral: Enterprise only for SAML (price undisclosed), though Team at USD ~20-25 offers a no-SSO-but-Google/Microsoft-login team space.
- Effective AI premium for a 20-person Spanish SMB: Google about EUR 0 above existing Workspace; Microsoft about EUR 15.60 x N, plus Business Standard/Premium base; Mistral about USD 20-25 x N on top of whatever suite they already pay for.

### Gaps
- Official EUR prices for Mistral Team/Enterprise not found (page renders USD). Minimum seat counts for Mistral Team not confirmed. No VAT-inclusive Spain-specific pricing sources checked.
- Microsoft EUR figures came via search summary because the page fetch failed (503); recheck the live Microsoft IE/ES page.
- Gemini Enterprise (separate product) current price conflicts; not resolved.
- Whether Mistral Team plan explicitly opts out of training by default: not confirmed from official sources in this pass (note Mistral's consumer plans may differ).

## 2. Security / admin feature matrix: no-training, retention, SSO/SCIM, RBAC, audit logs, data residency, certifications, DPA/GDPR, DLP/labels

### Takeaway
Microsoft and Google both inherit tenant-level identity, DLP, labels, retention and audit tooling from the underlying suite; Microsoft has the most mature, explicit documentation (Purview retention/eCDiscovery for Copilot interactions, EU Data Boundary, ISO 42001). Google added Gemini app data-region support in June 2026 (EU/US per OU). Mistral offers EU-headquartered hosting and SOC 2 Type II + ISO 27001/27701, but SAML SSO is Enterprise-only and SCIM was still labelled private preview in its docs.

### Cited Findings
**Microsoft Copilot**
- Copilot only surfaces data the user already has at least view permission to; honours Purview sensitivity-label encryption/usage rights; semantic index respects user identity boundary. [P] — [Microsoft Learn privacy page](https://learn.microsoft.com/en-us/copilot/microsoft-365/microsoft-365-copilot-privacy)
- Retention/audit: prompts and responses stored with other M365 content ("Copilot activity history"), encrypted at rest, managed through Content Search/Purview retention policies; users can delete their history via My Account; admins can export Teams Copilot chats via Teams Export APIs. [P] — same Microsoft page
- EU: "EU traffic stays within the EU Data Boundary while worldwide traffic can be sent to the EU and other countries for LLM processing"; Copilot added to data-residency commitments 1 Mar 2024 (Advanced Data Residency / Multi-Geo). Models from Anthropic used as a subprocessor are currently excluded from the EU Data Boundary — admins can choose whether to enable third-party models. [P] — same Microsoft page
- Web grounding (Bing) is an optional connected experience and is outside EUDB commitments (from a Microsoft documentation quote on Q&A). [SS] — [Microsoft Q&A thread](https://learn.microsoft.com/en-us/answers/questions/1664962/is-copilot-for-m365-chat-(graph-and-web-grounding))
- Certifications named for Copilot: GDPR, ISO 27001, HIPAA, ISO 42001 (AI management); ISO 27018 referenced; commitment to EU AI Act compliance. [P] — Microsoft Learn privacy page. SOC 2, C5, ENS not named on that page (not searched separately; known to be held for M365 broadly but not verified in this pass).
- Microsoft says Copilot services opted out of Azure OpenAI abuse monitoring (no human review). Prompt-injection protection includes jailbreak and cross-prompt injection (XPIA) classifiers, "may not be available in all scenarios". [P] — same page
- Admin governance of agents: "Integrated apps" in M365 admin center shows permissions/terms; admins choose which agents are allowed. [P] — same page
- SharePoint Advanced Management (SAM) features, including Restricted Content Discovery (RCD), become available to SharePoint admins once at least one Copilot licence is assigned; RCD limits discovery in tenant-wide search and Copilot but does not change permissions. Licensing details differ between Microsoft pages and a community comment. [SS] — [Microsoft Learn: SAM features with Copilot licence](https://learn.microsoft.com/sharepoint/sharepoint-advanced-management-features-copilot-license); [RCD](https://learn.microsoft.com/sharepoint/restricted-content-discovery)

**Google Gemini (Workspace)**
- Gemini app now adheres to Workspace data-region requirements as of 29 Jun 2026: admins can pick EU storage and processing, US, or both, per organisational unit. [P: Google Workspace Updates blog via search result] — [Workspace Updates, June 2026](https://workspaceupdates.googleblog.com/2026/06/gemini-app-data-regions-support.html)
- Gemini in Workspace apps: interactions stay within the org; DLP and data regions apply automatically; customer content not used for training outside the domain without permission. [P] — [Google knowledge page](https://knowledge.workspace.google.com/admin/billing/ai-features-and-pricing-updates-for-google-workspace-business-editions)
- Certifications, Gemini Enterprise (separate product): one Google compliance page lists ISO 27001/27017/27018/27701 and BSI C5:2020; another version lists ISO family and SOC reports with no C5; a third says the Standard/Plus editions "will be included in future audits". Conflict; C5 status for Gemini Enterprise unconfirmed; no source found that confirms certification coverage for the Gemini app in Workspace specifically. [SS] — [Gemini Enterprise compliance security controls](https://docs.cloud.google.com/gemini/enterprise/docs/compliance-security-controls?authuser=1)
- Custom Workspace editions such as Enterprise Essentials (Data Region Edition) and Deskless do not include generative AI features. [P] — Google knowledge page above

**Mistral**
- Mistral help centre (dated 12 Aug 2026): "Mistral complies with both SOC 2 Type II and ISO 27001/27701 frameworks"; reports via trust.mistral.ai. [P] — [help.mistral.ai article 323772](https://help.mistral.ai/en/articles/323772-do-you-have-soc2-or-iso27001-certification)
- Enterprise data processed in the EU by default with US processing via explicit opt-in endpoint; self-hosting / private cloud / on-prem options. [S: third-party tracker (June 2026 WAIMAKERS summary)]; Mistral's own launch post says Le Chat can be self-hosted, in a public/private cloud, or Mistral-cloud hosted. [SS] — [WAIMAKERS GDPR overview](https://www.waimakers.com/en/resources/gdpr-compliance/mistral-ai); [Mistral Le Chat Enterprise announcement](https://mistral.ai/fr/news/le-chat-enterprise)
- SAML SSO Enterprise-only; SCIM private preview; auto seat assignment; Entra, Google, Okta named as IdPs. [P] — [Mistral SSO docs](https://docs.mistral.ai/admin/security-access/sso)
- RBAC admin interface and SCIM listed in Enterprise features; audit logs and SAML on pricing page under Team/Enterprise. [SS/P partial]

### Inferences
- For Spanish SMBs, Microsoft has the clearest documented chain from identity to labels to retention to eDiscovery; Google's equivalent (Drive labels, DLP, Vault, data regions) is native to Workspace but I did not fetch Google's Gemini admin/audit documentation, so my comparison on audit logs for Gemini is thinner.
- The Microsoft EU Data Boundary statement has two caveats worth flagging to an EU buyer: worldwide-traffic wording and the exclusion of Anthropic models (and Bing web grounding).

### Gaps
- ENS (Esquema Nacional de Seguridad) certification status: no source found for any of the three in this pass. Likely only relevant for Spanish public sector suppliers; not verified.
- SOC 2 / C5 for M365 Copilot and for Gemini app: not verified from primary pages here.
- Google Gemini: audit-log/Admin console coverage of Gemini app activity, retention defaults (Gemini app activity), and SSO/SCIM specifics were not researched in this pass.
- Mistral: audit-log depth, data retention defaults, and DPA terms not read; official Mistral data-residency page not found.
- Copilot Chat (free tier) specific controls (e.g., Purview DLP for Copilot Chat prompts) not verified.

## 3. What makes Copilot/Gemini "enterprise secure" in practice for an SMB, and where do SMBs misconfigure (oversharing)?

### Takeaway
Both assistants are "secure" mainly because they only retrieve what the signed-in user can already access and run inside the tenant's compliance boundary — which means the SMB's existing permissions hygiene (SharePoint/OneDrive/Drive sharing, labels) is the real control, and oversharing is the main failure mode.

### Cited Findings
- Microsoft: "Microsoft Copilot only surfaces organizational data to which individual users have at least view permissions. It's important that you're using the permission models... such as SharePoint, to help ensure the right users or groups have the right access", including permissions granted via shared channels with external tenants. [P] — [Microsoft Learn privacy page](https://learn.microsoft.com/en-us/copilot/microsoft-365/microsoft-365-copilot-privacy)
- Microsoft tooling to mitigate oversharing: Restricted Content Discovery and other SAM features included when at least one Copilot licence exists; Microsoft publishes an oversharing mitigation blog and SharePoint-Copilot best-practices docs. [SS] — [Microsoft Learn SAM/Copilot licence](https://learn.microsoft.com/sharepoint/sharepoint-advanced-management-features-copilot-license); [Tech Community: Mitigate oversharing](https://techcommunity.microsoft.com/blog/microsoft365copilotblog/mitigate-oversharing-to-govern-microsoft-365-copilot-and-agents/4448744)
- Microsoft encryption with sensitivity labels can exclude programmatic (agent) access, limiting agents from reading labelled content. [P] — Microsoft Learn privacy page
- Google: Gemini honours existing Workspace permissions, DLP and data-region policies, per Google's page; interactions stay in the org. [P] — [Google knowledge page](https://knowledge.workspace.google.com/admin/billing/ai-features-and-pricing-updates-for-google-workspace-business-editions)
- Reported failure of the labels control: bug CW1226324 let Microsoft 365 Copilot Chat summarise emails in Sent Items and Drafts despite confidential sensitivity labels and DLP policies; detected 21 Jan 2026; reported publicly ~18 Feb 2026; attributed by Microsoft to a code error; sources differ on whether the fix is complete. [S] — [The Register, 18 Feb 2026](https://www.theregister.com/2026/02/18/microsoft_copilot_data_loss_prevention/); [TechRadar](https://www.techradar.com/pro/security/microsoft-admits-an-office-bug-exposed-confidential-user-emails-to-copilot); [Petri](https://petri.com/microsoft-365-copilot-bug-confidential-emails/)

### Inferences
- Common SMB misconfigurations that follow from the vendors' own statements (not individually cited): "Everyone except external users" or org-wide links on SharePoint sites and "anyone in the organization with the link" in Drive; unlabelled sensitive data; legacy sites with broad membership; guest access via Teams shared channels; third-party agents/connectors turned on by default (Google's Workspace MCP connectors are ON by default per Sept 2026 post, see Q6).
- SMBs without Purview/labels licensing (Business Basic/Standard) have fewer label/DLP controls; Business Premium bundles Purview basics and Entra P1 (general knowledge; not verified in this pass).

### Gaps
- No quantitative data on how often SMBs misconfigure sharing; no survey source found. Google-specific guidance on Drive oversharing before Gemini rollout not searched.
- Licence-tier mapping of Purview/DLP/labels features to Business Standard vs Premium and Google Business Standard vs Plus not verified.

## 4. Is Mistral Le Chat a credible EU-native competitor on security (hosting, certifications, price, features)?

### Takeaway
Credible for EU hosting/sovereignty and baseline certs (SOC 2 Type II, ISO 27001/27701, EU default processing for Enterprise, self-host option), but weaker than the incumbents on SMB-grade admin maturity: SAML SSO only on Enterprise (quote-based), SCIM in private preview, OIDC unsupported, and no suite-level DLP/labels/eDiscovery. Price is higher per seat than Google's bundled Gemini and comparable to Copilot Business.

### Cited Findings
- SOC 2 Type II and ISO 27001/27701 compliance claimed on Mistral's help centre (12 Aug 2026), reports via trust centre. [P] — [help.mistral.ai](https://help.mistral.ai/en/articles/323772-do-you-have-soc2-or-iso27001-certification)
- Deployment options include self-hosting, private/public cloud, or Mistral-hosted (launch announcement). [SS] — [Mistral](https://mistral.ai/fr/news/le-chat-enterprise)
- EU-by-default processing for Enterprise with US endpoint opt-in (third-party). [S] — [WAIMAKERS](https://www.waimakers.com/en/resources/gdpr-compliance/mistral-ai)
- SAML 2.0 SSO Enterprise only; SCIM private preview; no OIDC; domain verification from Team. [P] — [Mistral SSO docs](https://docs.mistral.ai/admin/security-access/sso)
- Team price USD 24.99/user/month; Enterprise custom. [P] — [Mistral pricing](https://mistral.ai/fr/pricing/?currency=eur)
- Admin controls for MCP connectors: connectors must be configured by an organisation admin before use; custom MCP connectors need admin. [SS] — [Mistral help: introduction to connectors](https://help.mistral.ai/en/articles/393507-introduction-to-connectors); [MCP connectors docs](https://docs.mistral.ai/le-chat/knowledge-integrations/connectors/mcp-connectors)

### Inferences
- Mistral is a good fit for firms prioritising EU legal-entity/sovereignty (French company, EU processing) or wanting a second, non-hyperscaler assistant; it is not a drop-in replacement for suite-integrated assistants because it lacks native access to Drive/SharePoint permissions model except via connectors.
- Because Spain-specific certifications (ENS) were not found, public-sector-adjacent SMBs should ask Mistral directly.

### Gaps
- Mistral audit log depth, retention, DPA text, sub-processor list (e.g., cloud hosts), and whether any non-EU sub-processors touch Le Chat data: not retrieved.
- Mistral incidents/vulnerability disclosures: not searched.
- Mistral C5/ENS: no source found.

## 5. Known weaknesses and incidents (2025-2026)

### Takeaway
All major assistants have had indirect-prompt-injection / exfiltration findings; Microsoft's EchoLeak (CVE-2025-32711, CVSS 9.3) and the 2026 CW1226324 label/DLP bypass, and Google's GeminiJack (Dec 2025) and calendar-invite injection (Jan 2026) were all fixed server-side by the vendors, with no confirmed in-the-wild exploitation found in the sources read. The recurring pattern: untrusted content (email, calendar invite, document) plus broad retrieval plus an outbound channel (links/images).

### Cited Findings
- EchoLeak (CVE-2025-32711): zero-click M365 Copilot flaw disclosed by Aim Security in June 2025; Microsoft rated it critical (CVSS 9.3); fixed server-side, no customer action; it bypassed XPIA classifiers and link-redaction. [S] — [Dark Reading](https://www.darkreading.com/application-security/researchers-detail-zero-click-copilot-exploit-echoleak); [arXiv 2509.10540](https://arxiv.org/abs/2509.10540v1); [The Hacker News, Jun 2025](https://thehackernews.com/2025/06/zero-click-ai-vulnerability-exposes.html)
- CW1226324 (Copilot Chat summarised Sent Items/Drafts despite labels and DLP), detected 21 Jan 2026. [S] — [The Register](https://www.theregister.com/2026/02/18/microsoft_copilot_data_loss_prevention/)
- Reprompt (Varonis Threat Labs): one-click attack hijacking Copilot Personal sessions and exfiltrating data, patched Jan 2026; Varonis states M365 enterprise Copilot customers were not affected. A June 2026 Varonis follow-up reportedly found a similar chain in Copilot Enterprise Search ("SearchLeak"), more dangerous for orgs (detail not read). [S] — [Varonis: Reprompt](https://varonis.com/blog/reprompt); [SecurityWeek](https://www.securityweek.com/new-reprompt-attack-silently-siphons-microsoft-copilot-data/amp/)
- GeminiJack (Noma Labs, Dec 2025): zero-click flaw in Gemini Enterprise / Vertex AI Search — a poisoned Doc, Calendar event or email made Gemini search for sensitive terms and exfiltrate them via an attacker-controlled image URL; fixed by Google. [S] — [SecurityWeek](https://www.securityweek.com/google-patches-gemini-enterprise-vulnerability-exposing-corporate-data/amp/); [Infosecurity Magazine](https://www.infosecurity-magazine.com/news/google-fixes-gemini-enterprise-flaw)
- Miggo Security (Jan 2026): calendar-invite indirect prompt injection that made Gemini write private calendar details into a new event visible to the attacker; mitigated. Earlier SafeBreach (Aug 2025) calendar-invite technique and HiddenLayer indirect-injection demos in Gmail/Slides/Drive. [S] — [The Hacker News, Jan 2026](https://thehackernews.com/2026/01/google-gemini-prompt-injection-flaw.html); [BleepingComputer](https://www.bleepingcomputer.com/news/security/gemini-ai-assistant-tricked-into-leaking-google-calendar-data/amp/); [SecurityWeek (HiddenLayer)](https://www.securityweek.com/ai-security-firm-shows-how-threat-actors-could-abuse-google-gemini-for-workspace/amp/)
- Microsoft itself states prompt-injection classifiers "may not be available in all Microsoft Copilot scenarios". [P] — Microsoft Learn privacy page

### Inferences
- Server-side fixes mean SMBs cannot patch themselves; their mitigation is limiting what Copilot/Gemini can read (least privilege, labels), restricting external email/calendar-invite auto-processing, and keeping third-party connectors/agents off unless needed.
- Mistral had no incident found, but I did not search for it; absence is not evidence of safety, and Le Chat's lower market share means less researcher scrutiny (inference).

### Gaps
- Copilot Studio agent prompt-injection findings in 2026: none found. Mistral Le Chat security research: not searched. SearchLeak details unread.

## 6. MCP client/connector mechanisms for power users

### Takeaway
All three now expose an MCP-style mechanism with admin gating, but maturity differs: Mistral Le Chat has custom MCP connectors (admin-configured, marked beta on the pricing page); Google added MCP-based third-party connectors to Gemini in Workspace (Sept 2026, ON by default for eligible users) and BYO custom MCP servers in Gemini Enterprise (public preview, July 2026); Microsoft exposes MCP via Copilot Studio / Agent 365 tooling servers and Work IQ servers that generally need a full Microsoft 365 Copilot licence, with BYO MCP servers in preview.

### Cited Findings
- Google (Sept 2026): Gemini in Workspace can connect via MCP to Asana, Atlassian Rovo, HubSpot, Mailchimp, QuickBooks, Monday, Salesforce in Sheets, Gmail, Drive, Docs, Chat; ON by default for users with Gemini access; admins can manage at domain/OU/group level and choose which connectors are enabled via Apps > Google Workspace Marketplace apps; applies to Business Standard/Plus (and listed Business edition set) and Enterprise editions; Rapid/Scheduled Release domains; post dated 15 Sep 2026, click path corrected 30 Sep 2026. [P] — [Workspace Updates, 15 Sep 2026](https://workspaceupdates.googleblog.com/2026/09/connect-to-more-tools-with-gemini-in-Google-Workspace.html)
- Gemini Enterprise: custom MCP server connection in Public Preview (release notes dated 29 Jul 2026); custom MCP data stores blocked by default via an org policy constraint that admins must override; Google hosts a Workspace MCP endpoint (Gmail, Drive, Docs, Sheets, Slides, Calendar, Chat, People). [SS] — [Gemini Enterprise release notes](https://support.google.com/g/answer/16719009?hl=en); [Google codelab](https://codelabs.developers.google.com/google-workspace-ge)
- Microsoft: Agent 365 tooling servers (Copilot Search, SharePoint/OneDrive, Outlook, Word) usable in Copilot Studio agents; Work IQ MCP servers need a Microsoft 365 Copilot licence; admins allow/block servers in the M365 admin center "Tools" page; BYO remote MCP servers in preview routed through an Agent 365 Tooling Gateway; Purview/Defender observability. Licensing statement dated 19 Nov 2025 — may have changed. [SS] — [Microsoft 365 Dev blog, 19 Nov 2025](https://devblogs.microsoft.com/microsoft365dev/microsoft-agent-365-interoperability-for-smart-secure-productivity/); [Manage tools for agents](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/manage-tools-for-agent)
- Microsoft Copilot agents/Graph connectors: admins select which agents are allowed in Integrated apps; third-party agent data handling follows the agent's own terms. [P] — Microsoft Learn privacy page
- Mistral: Le Chat has custom MCP connectors; connectors must be configured by an organisation admin before use; pricing page lists "Connecteurs MCP personnalisés (bêta)". [SS/P] — [Mistral MCP connectors docs](https://docs.mistral.ai/le-chat/knowledge-integrations/connectors/mcp-connectors); [Mistral pricing](https://mistral.ai/fr/pricing/?currency=eur)

### Inferences
- Governance risk: Google's default-ON third-party MCP connectors mean an SMB admin should review the Marketplace/Apps settings before rolling out, since each connector widens the data an injected prompt could reach.
- For a power user needing arbitrary MCP servers, Mistral (admin-added) and Gemini Enterprise (preview, policy override) are the most direct; Microsoft's path is via Copilot Studio/Agent 365 and more licence-gated.

### Gaps
- Whether Copilot Chat (free) or Copilot Business users can use custom MCP in Copilot Studio without the full licence as of Nov 2026: not confirmed.
- Whether Gemini in Workspace connectors (Sept 2026) and Gemini Enterprise BYO-MCP share the same admin surface: unclear.

## 7. Likely default / power-user tools in a Spanish SMB already on Google Workspace or Microsoft 365, and bundling/pricing

### Takeaway
By bundling, the default assistant is whichever the SMB's suite vendor ships: Gemini (included in all Workspace Business editions at no extra charge since Jan 2025) for Google shops, and Copilot Chat (free with Entra-based M365) for Microsoft shops, with paid Microsoft 365 Copilot Business (EUR 15.60/user, up to 300 users) as the power-user upgrade. Mistral would typically be an add-on chosen for EU sovereignty rather than a suite default.

### Cited Findings
- Gemini folded into Workspace Business/Enterprise plans with price rises; Gemini add-on dropped. [P] — [Google knowledge page](https://knowledge.workspace.google.com/admin/billing/ai-features-and-pricing-updates-for-google-workspace-business-editions); [ITPro](https://www.itpro.com/software/workspace/google-workspace-is-getting-a-gemini-makeover-but-prices-are-going-to-increase)
- Copilot Business is the SMB add-on (<=300 users) on Business Basic/Standard/Premium, annual commitment; Copilot Chat included at no extra cost. [P/SS] — [Microsoft Learn license options](https://learn.microsoft.com/microsoft-365/copilot/copilot-business-faq); [Microsoft Learn overview](https://learn.microsoft.com/sv-se/copilot/overview)
- Mistral Team USD 24.99/user/month; SSO requires Enterprise. [P] — [Mistral pricing](https://mistral.ai/fr/pricing/?currency=eur)

### Inferences
- Because of bundling, Google-Workspace SMBs get Gemini "by default" and a pricing advantage; Microsoft SMBs get Copilot Chat by default and must pay EUR 15.60 more per user for in-app M365 Copilot and Graph grounding. A mixed estate is common: free/bundled assistant for everyone, paid Copilot or Mistral for a few power users.

### Gaps
- No Spain-specific market-share or adoption data found for Google Workspace vs Microsoft 365 vs Mistral among Spanish SMBs; the "likely default" claim is an inference from bundling only.
- Spanish-language/ES storefront prices (EUR incl./excl. IVA) not checked; the Irish storefront figures are used as a proxy.
