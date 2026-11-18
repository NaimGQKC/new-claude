# Pre-built agents, connectors and MCP servers for a self-hosted Claude-style workspace (as of 2026-11-18)

Research method note: about 35 tool calls (over the 15 guideline, given the very broad scope). Primary sources (spec site, vendor pricing pages, GitHub READMEs, Anthropic/OpenAI/Google docs) were preferred. Where only blogs/aggregators were available this is flagged. Ecosystem counts are volatile and aggregator-sourced; stars/licenses are from the GitHub page as fetched on 2026-11-18.

## 1. MCP ecosystem state: spec, registry, directories, quality

### Takeaway
The MCP spec is now at revision 2026-07-28 (stateless, sessions removed, tasks moved to an extension, DCR deprecated in favour of Client ID Metadata Documents), the official MCP Registry is still labelled preview, and directory counts range from ~21k (PulseMCP) to >100k (Glama) depending on what is counted. Quantity is huge, quality is highly uneven; the Anthropic reference servers are explicitly demo-grade and many (GitHub, Slack, Google Drive, Postgres) are archived, so "official vendor server" or a well-maintained platform is preferable to a random community server.

### Cited Findings
- Latest spec revision is 2026-07-28; the draft changelog after it only adds minor items (CIMD draft-03 pin, restoring `_meta` fields) — [MCP draft changelog](https://modelcontextprotocol.io/specification/draft/changelog)
- 2025-11-25 release added experimental Tasks (call-now/fetch-later), Client ID Metadata Documents (CIMD, SEP-991) as recommended client registration, OpenID Connect discovery, incremental scope consent, and OAuth client-credentials for machine-to-machine — summarised in [WorkOS](https://workos.com/blog/mcp-2025-11-25-spec-update) and the official [2025-11-25 changelog](https://modelcontextprotocol.io/specification/2025-11-25/changelog) (secondary summary via search; official changelog is the authority)
- 2026-07-28 major changes: protocol-level sessions and `Mcp-Session-Id` removed; the `initialize` handshake removed (every request carries protocol version and client capabilities in `_meta`); new mandatory `server/discover` RPC; `subscriptions/listen` replaces GET stream and resource subscribe; SSE resumability removed — [MCP 2026-07-28 changelog](https://modelcontextprotocol.io/specification/2026-07-28/changelog)
- 2026-07-28: Tasks moved out of core into an official extension `io.modelcontextprotocol/tasks` (polling via `tasks/get`, new `tasks/update`, `tasks/list` removed) — [MCP 2026-07-28 changelog](https://modelcontextprotocol.io/specification/2026-07-28/changelog)
- 2026-07-28: server-initiated requests (roots, sampling, elicitation) are replaced by a Multi Round-Trip Requests pattern (`InputRequiredResult` / `inputResponses`); `notifications/elicitation/complete` removed — [MCP 2026-07-28 changelog](https://modelcontextprotocol.io/specification/2026-07-28/changelog)
- 2026-07-28 deprecates Roots, Sampling and Logging features, HTTP+SSE transport, and OAuth Dynamic Client Registration (RFC7591) in favour of Client ID Metadata Documents; minimum 12-month deprecation window policy adopted — [MCP 2026-07-28 changelog](https://modelcontextprotocol.io/specification/2026-07-28/changelog)
- 2026-07-28 auth hardening: clients MUST validate the `iss` parameter (RFC 9207) if present; credentials bound to issuing authorization server; `ttlMs`/`cacheScope` required on list results; servers SHOULD return `tools/list` in deterministic order to improve LLM prompt-cache hits — [MCP 2026-07-28 changelog](https://modelcontextprotocol.io/specification/2026-07-28/changelog)
- Practical consequence: Open WebUI still lists Dynamic Client Registration and a Static-client mode, and Claude/ChatGPT still talk to remote servers; clients need to track both 2025-11-25 and 2026-07-28 for some time — [Open WebUI MCP docs](https://docs.openwebui.com/features/extensibility/mcp/)
- Official MCP Registry (registry.modelcontextprotocol.io) is a discovery site/API; the page itself shows no maturity label or count — [Official MCP Registry](https://registry.modelcontextprotocol.io/). A search-based review says it remains in preview with possible breaking changes/data resets and no GA date found — [Towards AI mid-2026 registries](https://pub.towardsai.net/mcp-registries-in-mid-2026-one-upstream-won-2ce541b92036) (secondary; summary from search results)
- Registry server counts from third-party API queries: 9,652 (24 May 2026), 26,479 (2 Sep 2026), 39,238 (4 Oct 2026), 52,042 (28 Oct 2026, one author's own query, counts latest versions); a deduplicated cross-registry estimate is ~22.5k — see [dev.to registry by the numbers](https://dev.to/amareswer/the-mcp-registry-by-the-numbers-38nc), [dailyaiworld](https://dailyaiworld.com/public/blogs/mcp-registry-26479-servers-alive-health), [agentndx census](https://agentndx-web.pages.dev/blog/how-many-mcp-servers-exist-census-2026). These are NOT official figures and do not reconcile.
- Directory sizes (comparison blogs, late Oct 2026): Glama ~111–113k open-source servers plus ~40k remote connectors; PulseMCP ~21.6k; MCP.so ~20k+ (April); Smithery ~7–8k (April) — [Apideck directories](https://www.apideck.com/blog/mcp-server-directories), [studiomeyer](https://studiomeyer.io/en/blog/mcp-marketplaces-2026.md). PulseMCP's own page showed 21,531 servers with filters for Anthropic References / Official Providers / Community (page 1 sample: 26 official, 8 community, 8 reference) — [PulseMCP](https://www.pulsemcp.com/servers)
- Smithery: acquired by Arcade.dev (announced 5 Aug 2026); hosted proxy, API, accounts, CLI/SDKs shut down 31 Oct 2026; public directory remains — [Smithery notice](https://smithery.ai/future), [Arcade blog](https://arcade.dev/blog/smithery-joins-arcade). One outlet raises neutrality concerns because Arcade also runs a server-quality benchmark — [runtimewire](https://runtimewire.com/article/arcade-acquires-smithery-agent-tool-supply-chain)
- Docker MCP Catalog: `mcp` namespace on Docker Hub shows 244 repositories (not all servers), with cosign signatures repo suggesting signed images — [Docker Hub /u/mcp](https://hub.docker.com/u/mcp). Docker MCP Gateway (MIT, ~1.6k stars) runs each local server in its own container, keeps secrets out of env vars, has built-in OAuth flows, profiles with per-tool allow-lists, and can import from the community MCP registry — [docker/mcp-gateway](https://github.com/docker/mcp-gateway)
- Anthropic's `modelcontextprotocol/servers` (92.1k stars; Apache-2.0 for new code, MIT for existing) now maintains only Everything, Fetch, Filesystem, Git, Memory, Sequential Thinking, Time; GitHub, GitLab, Google Drive, Slack, Postgres, Puppeteer, Redis, Sentry, SQLite, Brave Search, etc. are archived; README states these are reference implementations, "not production-ready" — [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers)
- Google now ships official remote Workspace MCP servers (Gmail, Drive, Docs, Sheets, Slides, Calendar, Chat), one server per product, requiring a Google Cloud project with the API/MCP service enabled and an OAuth client; per directory/blog sources still Developer Preview as of Oct 2026 — [Google guide](https://developers.google.com/workspace/guides/configure-mcp-servers), [Workspace Updates May 2026](https://workspaceupdates.googleblog.com/2026/05/agent-tools-and-security-updates-for-workspace-developers.html); preview/endpoint details from [developersdigest](https://www.developersdigest.tech/mcp-servers/google-workspace-gmail) (third-party)
- Google's guidance warns of indirect prompt injection from untrusted emails/docs and cross-tool leakage when Gmail, Drive and Chat are connected together — [Google guide via search summary](https://developers.google.com/workspace/guides/configure-mcp-servers)

### Inferences
- A workspace should be written against the remote Streamable HTTP + OAuth model and plan for the 2026-07-28 stateless protocol; stdio should be treated as a local-only convenience.
- Use the official registry or a signed catalog (Docker) as the source of truth for any "install from directory" feature, and treat directory counts as marketing.
- Because Smithery's hosted proxy is gone and Anthropic archived many reference servers, avoid depending on either for production connectors.

### Gaps
- No primary source for the official registry's current count or GA status (page failed to load counts; only third-party figures).
- I did not verify per-directory counts from each directory's own site except PulseMCP.
- Did not confirm what fraction of servers are "official" vendor-published versus community (only a one-page PulseMCP sample).

## 2. Connector / integration platforms (managed OAuth, many apps)

### Takeaway
For a single user, the cheapest path is free tiers (Composio free 10k calls, Pipedream free dev tier, Arcade 2,000 calls, Nango free 10 connections) or self-hosted n8n/Activepieces/Nango (limited). Truly open-source self-hostable options with permissive licenses are Activepieces (MIT), MetaMCP (MIT, but archived), Klavis (Apache-2.0, repo deprecated); Nango is source-available (Elastic) with limited self-host; Composio's SDK is MIT but its backend appears hosted/BYOC-enterprise only; n8n is fair-code. For an SMB multi-tenant product, per-end-user pricing (Pipedream $2/ext user, Nango per connection) and token custody are the main design/ cost issues.

### Cited Findings
- Composio: SDK monorepo is MIT, 31.2k stars, "1000+ toolkits"; the repo page does not say the hosted backend is open source — [ComposioHQ/composio](https://github.com/ComposioHQ/composio)
- Composio pricing page: Free $0 (10,000 tool calls/mo, $2 one-time credits, up to 3 members, 3 custom MCP servers); Standard $18/seat/mo (10,000 calls per seat, SSO, firewall, zero data retention); Enterprise custom with BYOC, SCIM, audit logs; extra tool calls $0.005 each; "1,700+ apps"; no self-host except Enterprise BYOC — [Composio pricing](https://composio.dev/pricing). Conflicting third-party claims (e.g., $29/mo, "Elastic-2.0", "fully open source") are stale or competitor-authored — [Merge on Composio pricing](https://www.merge.dev/blog/composio-pricing), [AnythingMCP](https://anythingmcp.com/vs/composio)
- Pipedream: Free (dev only, no production/external users), Startup $99/mo annual ($150 monthly; garbled on page), 100 external users included then $2/user/mo, credits $0.012 each beyond 10,000; MCP included on all plans; "3,000+ connectors, 10,000+ tools"; self-hosting not mentioned — [Pipedream pricing](https://pipedream.com/pricing)
- Zapier MCP: included in all Zapier plans; each tool call = 2 tasks from your task quota; "9,000+ apps and 66,000+ triggers/actions" on homepage vs "30,000+ actions" in FAQ; credentials in Zapier's managed layer; app/action-level access controls; SOC 2 Type II; no self-hosting — [Zapier MCP](https://zapier.com/mcp)
- Arcade.dev: Free 2,000 tool calls/mo; Team $25/mo + $0.01/call; Enterprise custom (cloud, VPC or air-gapped); integration count not on pricing page — [Arcade pricing](https://www.arcade.dev/pricing)
- Nango: Elastic License 2.0, 13.3k stars; self-host free with limited feature set (Dockerfile.self_hosted, docker-compose); managed OAuth + token refresh for 1,300+ APIs, 10,000+ prebuilt tools, MCP — [NangoHQ/nango](https://github.com/NangoHQ/nango). Pricing: Free (10 connections, 10 compute hrs, 10 GB), Pay-as-you-go $50/mo with $0.29/connection; self-host support is Enterprise — [Nango pricing](https://www.nango.dev/pricing)
- Activepieces: MIT Community Edition (25.6k stars), self-hostable/air-gapped, pieces exposed as MCP servers; counts inconsistent on the page (200+/280+/~400) — [activepieces/activepieces](https://github.com/activepieces/activepieces)
- n8n: fair-code under Sustainable Use License + Enterprise License, 211k stars; README says "1500+ integrations" vs About "400+"; repo tagged mcp-client/mcp-server; Community edition lacks SSO, projects, sharing of credentials, external secrets, etc. — [n8n-io/n8n](https://github.com/n8n-io/n8n), [n8n editions](https://docs.n8n.io/hosting/community-edition-features/). I could not retrieve the license terms for commercial/SMB hosting.
- Klavis AI: Apache-2.0, ~5.8k stars, 100+ prebuilt integrations with OAuth, Strata for context-efficient tool discovery; repo marked deprecated/archived (page statements conflict) — [Klavis-AI/klavis](https://github.com/Klavis-AI/klavis)
- MetaMCP: MIT, ~2.8k stars; aggregator/gateway with namespaces, per-endpoint OAuth (2025-06-18 spec) or API keys, OIDC SSO, middleware (e.g., filter inactive tools), rate limits, multi-tenant; repo archived with development moved to `ai-dev` branch — [metatool-ai/metamcp](https://github.com/metatool-ai/metamcp)
- Merge Agent Handler: free start then consumption pricing; blog says 30+ prebuilt connectors; a third-party (Oct 2026) lists Free 2,000 credits / Pro $1,000/mo, unverified — [Merge pricing](https://www.merge.dev/pricing/agent-handler), [eseospace](https://eseospace.com/blog/merge-mcp/)
- Single-source gaps: Toolhouse not researched; Make not researched.
- Google Workspace single-purpose open server: `taylorwilsdon/google_workspace_mcp` — MIT, ~3.5k stars, 12 services/120+ tools (Gmail 15, Drive 16, Calendar 7, Docs 19, Sheets 14, ...), OAuth 2.1 multi-user, stdio and streamable HTTP — [google_workspace_mcp](https://github.com/taylorwilsdon/google_workspace_mcp)

### Inferences
- Token storage: hosted platforms (Composio, Pipedream, Zapier, Arcade, Nango Cloud) hold the user's OAuth tokens on their infrastructure (Zapier states credentials stay in its managed layer; Composio has ZDR on paid tiers). For a privacy-first single-user tool that is a trade-off versus self-held tokens (Nango self-host, Activepieces, direct per-app servers).
- Single user: free tiers (10k calls Composio, 2k Arcade) are plenty; cost is not the issue, token custody and vendor lock-in are.
- SMB later: Pipedream Connect ($2/external user beyond 100) or Nango (per connection) are shaped for this; self-hosted Activepieces (MIT) avoids per-user fees but you own token security and app-verification burden (see section 6).

### Gaps
- Toolhouse, Make, and number-of-apps for Arcade not verified.
- How each platform encrypts/stores tokens (KMS, regional) not found on primary pages except Zapier's brief statement.
- n8n license commercial terms and its MCP node behaviour not verified from primary docs.

## 3. How major apps handle MCP and connectors

### Takeaway
Everyone converged on remote Streamable-HTTP MCP with OAuth for multi-user use. LibreChat has the richest self-hosted per-user model (stdio only via admin YAML; per-user keys/OAuth; agent tool pickers), Open WebUI is Streamable-HTTP-only natively and uses `mcpo` (OpenAPI proxy) for stdio, and Claude/ChatGPT both run remote connectors from their cloud (so cannot reach local stdio servers).

### Cited Findings
- Claude: custom connectors accept any remote MCP URL (Free capped at 1; paid plans more); Claude connects from Anthropic's cloud, not the user's device; directory holds vetted connectors; Anthropic warns custom connectors allow unverified services — [Claude custom connectors docs](https://claude.com/docs/connectors/custom/remote-mcp), [Anthropic connectors directory help](https://support.claude.com/en/articles/11724452-use-the-connectors-directory-to-extend-claude-s-capabilities), [MCP directory policy](https://support.claude.com/en/articles/11175166-mcp-directory-policy)
- ChatGPT: Developer mode gives full MCP client support (read and write, write needs confirmation by default), supports SSE and streaming HTTP, OAuth/none/mixed auth, no local MCP servers; Apps SDK (launched 6 Oct 2025) turns an MCP server into a ChatGPT app with UI; docs and help center conflict on which plans get write access (Plus vs business plans only) — [OpenAI developer mode](https://developers.openai.com/api/docs/guides/developer-mode), [OpenAI help](https://help.openai.com/en/articles/12584461-developer-mode-and-mcp-apps-in-chatgpt)
- LibreChat: servers defined in `librechat.yaml` (restart required); users with permission can add remote Streamable HTTPS/SSE servers in UI; stdio only via YAML; auth modes none/auto-OAuth, API key (shared or per-user), OAuth with background refresh, On-Behalf-Of (OIDC + admin grant); per-user connections, idle close 15 min; UI-created servers cannot use env-var placeholders; agents pick tools from servers; sharing with users/groups/roles — [LibreChat MCP docs](https://www.librechat.ai/docs/features/mcp). Note: "Pick a model that supports tool calls or the model will never call the server's tools" (same page)
- Open WebUI: native MCP since v0.6.31, Streamable HTTP only; OAuth 2.1 with DCR or static client; admin-only server add; per-user OAuth grants stored per user (need `WEBUI_SECRET_KEY` to decrypt after restart); OAuth tools cannot be default tools; stdio/SSE servers must go through `mcpo` (OpenAPI proxy) — [Open WebUI MCP docs](https://docs.openwebui.com/features/extensibility/mcp/)
- Dify: no fully native MCP at last check; MCP via community marketplace plugins (MCP SSE/HTTP tools, agent strategy) and can expose Dify apps as MCP servers; Dify blog says native support is being worked on — [Dify blog](https://www.dify.ai/blog/dify-mcp-plugin-hands-on-guide-integrating-zapier-for-effortless-agent-tool-calls) (search summary; may be outdated by Nov 2026)
- LobeHub (ex-LobeChat): MCP marketplace at lobehub.com/mcp with one-click install of local/remote servers; community-maintained entries — [LobeHub MCP](https://lobehub.com/mcp?q=kit) (search summary)
- Cherry Studio: MCP via Settings > MCP Servers, stdio and Streamable HTTP; AGPL-3.0 per SourceForge listing — [Cherry Studio docs](https://docs.cherry-ai.com/docs/en-us/advanced-basic/mcp/config), [SourceForge](https://sourceforge.net/mirror/cherry-studio/)
- Onyx: core MIT, enterprise code (ee/) under separate license; docs say connectors, chat, agents, search are free/open source, but a third-party says connector permission sync is Enterprise-only (unverified) — [Onyx billing docs](https://docs.onyx.app/admins/billing/overview.md), [wz-it comparison](https://wz-it.com/en/blog/onyx-self-hosted-installation/)

### Inferences
- Building on LibreChat gives the most complete "connectors + per-user auth + agent" scaffolding; Open WebUI gives broad ecosystem and mcpo but needs admin-managed servers and workarounds for default OAuth tools.
- A custom build should implement: remote MCP client with OAuth (CIMD + DCR fallback), per-user token vault, an admin allow-list, and an stdio sandbox (Docker) for local servers.

### Gaps
- Dify, LobeHub, Cherry Studio findings come from search summaries, not fetched primary pages.
- LibreChat agent-marketplace feature: the MCP page does not cover it; not verified.
- ChatGPT plan eligibility conflict unresolved.

## 4. Pre-built agents, templates, skills and portability

### Takeaway
The only genuinely cross-vendor portable "agent" artifact is the Agent Skills format (SKILL.md folder, open standard by Anthropic, adopted by many clients). GPTs, Dify apps, and LibreChat agents are app-specific configs. Anthropic's skills repo is the best starting library.

### Cited Findings
- Agent Skills: folder with `SKILL.md` (name, description + instructions) plus optional scripts/references/assets; progressive disclosure (name+description at startup, full body on activation, resources on demand); open standard originally by Anthropic and adopted by a growing number of products — [agentskills.io](https://agentskills.io/home)
- `anthropics/skills`: 197.2k stars; README says many skills (including docx/pdf/pptx/xlsx) are Apache 2.0 (check per-skill license files); categories: creative/design, development (webapp testing, MCP server builder), enterprise/communication, document skills; marked demonstration/educational — [anthropics/skills](https://github.com/anthropics/skills)
- Claude-for-work plugin bundles (skills + MCP connectors, e.g., sales, legal) exist as "plugins" in this very session's skill list; they are Claude Code/Cowork-specific packaging (observed in environment, no URL).
- LibreChat agents can attach MCP servers and select tools (see section 3) — [LibreChat MCP docs](https://www.librechat.ai/docs/features/mcp)
- Dify plugin marketplace hosts community tool/agent-strategy plugins — [Dify marketplace example](https://marketplace.dify.ai/plugin/junjiem/mcp_see_agent)

### Inferences
- Implement skills (SKILL.md) as the sharing unit: markdown + scripts run in a sandbox; "pre-built agents" become skill + tool-allowlist + model-routing preset in a small manifest (own format) so they are portable across the workspace and to other skills-compatible clients.
- Skills are prompt-injection-adjacent code: vet them like dependencies (see section 6).

### Gaps
- GPT Store status/policy, OpenAI Agents SDK, LibreChat agent marketplace, Dify template exchange details were not verified.
- No data on list of clients adopting Agent Skills (clients page not fetched).

## 5. Tool-context bloat and mitigations; cheap model tool-calling

### Takeaway
Loading many MCP tools up front costs tens of thousands of tokens and degrades selection; the main mitigations are deferred loading/tool search, code-execution-with-MCP (98.7% reduction in Anthropic's example), and gateways that filter tools. Anthropic's tool search is API-side for Claude models only, so a model-agnostic workspace should implement client-side tool search. Open Chinese models (GLM-5.x, Kimi K2.x, DeepSeek V4, Qwen) score ~74–77% on MCP Atlas per aggregator data.

### Cited Findings
- Typical multi-server setup (GitHub, Slack, Sentry, Grafana, Splunk) ≈ 55k tokens of definitions; tool search typically cuts >85%; selection accuracy degrades beyond ~30–50 tools — [Anthropic tool search docs](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool)
- Tool search: `defer_loading: true`; regex and BM25 variants; up to 10,000 deferred tools; returns 5 matches by default; custom client-side implementation (embeddings) possible by returning `tool_reference` blocks; keep 3–5 hot tools non-deferred; use when 10+ tools or >10k tokens of definitions — [Anthropic tool search docs](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool). Only works with Claude models via the API.
- Code execution with MCP: expose servers as code APIs on a filesystem; example reduces 150,000 tokens to 2,000 (98.7%); keeps large intermediate data out of context; can tokenise PII; requires sandboxing with resource limits and monitoring — [Anthropic engineering](https://www.anthropic.com/engineering/code-execution-with-mcp)
- MCP 2026-07-28 requires deterministic tool ordering and `ttlMs` caching to improve LLM prompt-cache hits — [MCP changelog](https://modelcontextprotocol.io/specification/2026-07-28/changelog)
- Gateways: MetaMCP namespaces + middleware to filter tools; Docker MCP Gateway per-profile tool allow-lists; Klavis Strata for context-efficient discovery — [MetaMCP](https://github.com/metatool-ai/metamcp), [Docker mcp-gateway](https://github.com/docker/mcp-gateway), [Klavis](https://github.com/Klavis-AI/klavis)
- Cheap-model tool use (aggregator, indicative): MCP Atlas July 2026 snapshot GLM-5.2 76.8%, Kimi K2.7 Code 76%, DeepSeek V4 Pro 74.2%; a later Oct 27 page shows same open-weight ordering but conflicting overall leaderboard; BFCL-v4 open-weight slots mostly Qwen (secondary blog); scaffolding changes rankings — [BenchLM MCP Atlas](https://www.benchlm.ai/benchmarks/mcpAtlas), [BenchLM tool use](https://www.benchlm.ai/best/tool-use), [mcpplayground](https://mcpplaygroundonline.com/blog/best-ai-model-for-mcp-tool-calling)

### Inferences
- Design: per-agent tool allow-lists (<~20 tools hot), plus a meta tool "search_tools" (BM25/embedding over names+descriptions) that works for any model; for data-heavy flows (Sheets, email batches) offer a sandboxed code-execution mode.
- With cheap models, keep tool lists short, enforce JSON-schema validation and retries, and route tool-heavy/high-stakes steps to a stronger model.

### Gaps
- No primary leaderboard (BFCL, MCP Atlas owner) was fetched; MCP-Universe/MCPMark results not found. Model names/versions come from aggregators and should be verified before being cited as fact.
- Token costs of specific popular MCP servers (e.g., Google Workspace server 120+ tools) not measured.

## 6. Security risks and guardrails; platform policies

### Takeaway
The dominant risk is not a server bug but the "lethal trifecta": untrusted content + private data + outbound action, hijacked by prompt injection (proved on the official GitHub MCP server). Supply-chain attacks on community servers are real (postmark-mcp BCC backdoor). Guardrails: least-privilege scopes, per-tool approval for writes/sends, pinned and hashed tool definitions, sandboxed servers, per-session data isolation, audit logging.

### Cited Findings
- Invariant Labs "toxic agent flow": a malicious public GitHub issue made an agent using the official GitHub MCP server pull private repo data and leak it in a public PR; tested with Claude 4 Opus; "Always Allow" confirmations make it worse; described as not a server code flaw, requiring system-level mitigation (per-session repo scoping, guardrails, monitoring); alignment alone insufficient — [Invariant Labs](https://invariantlabs.ai/blog/mcp-github-vulnerability)
- postmark-mcp (Sept 2025): lookalike npm package, v1.0.16 added a hidden BCC to the attacker on all emails; Postmark said it is not an official tool — [Startup Defense ATLAS case study](https://www.startupdefense.io/mitre-atlas-case-studies/aml-cs0053-poisoned-postmark-mcp-server-email-exfiltration) (secondary; originally reported by Koi Security)
- Rug pull = tool definition changed after approval; mitigations commonly proposed: pin versions and diff tool definitions against an approved baseline — [Waxell](https://www.waxell.ai/blog/mcp-rug-pull-attack) (vendor blog)
- OWASP MCP Top 10 (2025 edition, beta/pilot phase): token mismanagement, privilege escalation via scope creep, tool poisoning, supply chain, command injection, prompt injection via contextual payloads, insufficient authN/Z, lack of audit/telemetry, shadow MCP servers, context injection/over-sharing — [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/)
- CVEs: MCPJam Inspector CVE-2026-23744 (CVSS 9.8, default 0.0.0.0 bind, RCE, fixed in 1.4.3) — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-23744); Anthropic MCP Inspector/mcp-remote RCE CVE-2025-49596 (CVSS 9.8) per aggregator — [Tech Jack Solutions PDF](https://techjacksolutions.com/wp-content/uploads/2026/04/scc-cve-2026-0058.pdf) (verify on NVD); an argument-injection entry for Anthropic's Git MCP server exists in a Positive Technologies database with inconsistent ID and no vendor advisory seen — [PT-2026-23710](https://dbugs.ptsecurity.com/vulnerability/PT-2026-23710)
- Docker-style isolation: container per server, secrets not in env vars, per-profile tool allow-lists — [docker/mcp-gateway](https://github.com/docker/mcp-gateway)
- MCP spec hardening in 2026-07-28: RFC 9207 `iss` validation; credentials keyed by issuer — [MCP changelog](https://modelcontextprotocol.io/specification/2026-07-28/changelog)
- Google Gmail/Drive access: personal use, dev/test, internal-org use are listed exceptions to restricted-scope verification, but storing/transmitting restricted-scope data on servers triggers a security assessment (CASA); costs quoted by vendors range from ~$3k to $15k–75k and are not official — [Google restricted scope verification](https://developers.google.com/identity/protocols/oauth2/production-readiness/restricted-scope-verification), [GMass](https://www.gmass.co/blog/google-oauth-verification-security-assessment/), [Nylas](https://developer.nylas.com/docs/dev-guide/provider-guides/google/google-verification-security-assessment-guide). Note: an unverified Gmail app in "Testing" or unverified production state has user caps and warning screens (not verified here).
- LinkedIn: most open-source LinkedIn MCP servers use a `li_at` session cookie (scraping/session automation), which secondary sources say breaches the User Agreement; API Terms §3.1 reportedly bars using the API to automate posting; official API access is limited/partner-gated — [contentin.io](https://contentin.io/blog/linkedin-mcp-terms-of-service/), [unipile](https://www.unipile.com/is-linkedin-scraping-legal/) (secondary; verify against LinkedIn's own terms)
- Instagram: not researched (see gaps).

### Inferences
- Minimum viable guardrails for the workspace: (1) allowlist of vetted servers with pinned versions/digests; (2) hash tool descriptions and require re-approval on change; (3) read tools auto-allowed, write/send/delete tools require human approval showing the exact arguments (no "Always Allow" for sends); (4) no combining private-data read tools and open-web fetch/outbound-write tools in one session without approval; (5) least-privilege OAuth scopes (e.g., Gmail readonly + drafts instead of send); (6) sandbox stdio servers in containers with no ambient credentials and egress filtering; (7) encrypt token vault, log every tool call; (8) treat skills as code.
- For Gmail via official Google remote server or self-owned OAuth client in "personal use" mode, single-user use avoids CASA; an SMB product storing mail data would likely trigger it.
- LinkedIn should be treated as "manual/export only or official API" rather than a session-cookie MCP.

### Gaps
- Instagram/Meta platform policy not researched.
- Primary sources for Unit 42, Trail of Bits, Palo Alto research not fetched; tool-poisoning original Invariant post not fetched.
- CVE-2025-49596 and the Anthropic Git server CVEs not verified on NVD/GitHub advisories.
- LinkedIn clauses not verified from linkedin.com legal pages.

## 7. Recommended first connectors and best option for each

### Takeaway
Start with a small, vetted set: Google Workspace (official Google remote servers in preview or the MIT `google_workspace_mcp` as self-hosted fallback), GitHub (official GitHub server; the Anthropic reference one is archived), Slack/Notion via vendor-hosted remote MCP or a platform (Composio/Pipedream/Activepieces), web search/fetch via Anthropic's maintained Fetch plus a search API server, filesystem/Git via the maintained reference servers in a container, browser via Playwright/Browser server in a sandbox, and doc skills for office docs.

### Cited Findings
- Gmail, Drive, Docs, Sheets, Slides, Calendar, Chat: official Google remote MCP servers (preview) — [Google guide](https://developers.google.com/workspace/guides/configure-mcp-servers); self-hosted alternative `taylorwilsdon/google_workspace_mcp` (MIT, 12 services, 120+ tools, OAuth 2.1, stdio/HTTP) — [repo](https://github.com/taylorwilsdon/google_workspace_mcp)
- GitHub: the Anthropic reference GitHub server is archived — [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers); GitHub's own MCP server (the one in this session, `github` tools such as `get_file_contents`, `create_pull_request`) is the maintained option, and was the subject of the Invariant injection research — [Invariant Labs](https://invariantlabs.ai/blog/mcp-github-vulnerability)
- Slack: reference server archived and now maintained by Zencoder (community) — [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers); alternatives via aggregators: Composio, Pipedream, Zapier, Activepieces (sections 2)
- Notion: not verified independently here; reachable through Composio/Pipedream/Zapier/Activepieces/Nango catalogs (counts above)
- Filesystem, Fetch, Git, Memory, Time: maintained reference servers (Apache-2.0/MIT) — [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers)
- Web search: Brave Search reference server archived and "replaced by an official server" — [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers)
- Office docs: Anthropic's docx/pdf/pptx/xlsx Agent Skills (Apache-2.0 per README; verify per skill) — [anthropics/skills](https://github.com/anthropics/skills)
- Browser: puppeteer reference server archived — [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers); Playwright MCP not researched
- Aggregation/gateway layer: Docker MCP Gateway (MIT) for sandboxed local servers; MetaMCP (MIT, archived) or Activepieces (MIT) for multi-app — [docker/mcp-gateway](https://github.com/docker/mcp-gateway), [MetaMCP](https://github.com/metatool-ai/metamcp), [Activepieces](https://github.com/activepieces/activepieces)

### Inferences
Recommended architecture for single user first:
1. Core workspace implements: remote MCP client (Streamable HTTP, OAuth with CIMD + DCR fallback), tool-search meta tool, per-tool approval UI, token vault, audit log, token-cost display per tool call.
2. Day-one connectors: Google Workspace (self-owned OAuth client, personal-use, minimal scopes), GitHub (official), Fetch + a search API, Filesystem (scoped dir) + doc skills, Slack and Notion through either a self-hosted Activepieces or Composio free tier, browser in a container.
3. Pre-built agents = SKILL.md bundles + tool allowlist + model-routing preset ("Inbox triager", "Meeting prep", "Repo reviewer", "Research"), shipped in-repo, reviewed like code.
4. For later SMB: add a multi-tenant token vault (or Nango/Pipedream Connect), per-tenant allowlists, SSO, audit export; budget for Google CASA if storing Gmail data; consider licensing implications (n8n/Nango/Elastic vs MIT Activepieces/MetaMCP).
5. Stack: LibreChat is the closest existing base for per-user MCP auth + agents (AGPL? license not verified here); a custom build is justified mainly for routing + cost display + artifacts.

### Gaps
- Playwright/browser MCP, Notion official MCP, Slack official MCP, GitHub MCP license/stars, and Brave official server were not verified against primary pages.
- LibreChat and Open WebUI licenses (Open WebUI has a custom license with branding restrictions, to my knowledge) were not verified in this research; check before building an SMB product on them.
- No cost data on tokens consumed per connector.
