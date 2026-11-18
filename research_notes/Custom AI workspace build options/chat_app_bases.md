# Open-source / source-available self-hosted AI chat workspaces as a base for a Claude-style product (as of 18 Nov 2026)

Method note: GitHub's API was blocked in this session, so stars/licenses/releases come from fetching the repo pages, LICENSE files and release pages through a summarizing fetch tool. Where the Releases section rendered empty on a repo's front page, I fetched the /releases page instead; release dates there show day+month only (no year), and I treat them as 2026 because the pages' own context/ footers and today's date indicate so. Star counts are snapshots from the fetch. Many comparison blogs surfaced by search are vendor/affiliate content and are flagged as such.

## 1. License, stars, release cadence, backing, acquisitions (per candidate)

### Takeaway
LibreChat (MIT) and Onyx CE (MIT) are the only strong chat-workspace candidates with fully permissive licenses; Open WebUI (branding-locked custom license), LobeHub (Apache-based but derivative-distribution needs a commercial license) and Dify (no multi-tenant SaaS without written permission) all carry commercialization-relevant restrictions. LibreChat has been owned by ClickHouse since Nov 2025, with the founder and team employed there.

### Cited Findings

#### LibreChat
- License MIT; 47.3k stars, 9.7k forks; repo now shown under the LibreChat-AI org; README highlights v0.8.9 — [GitHub repo](https://github.com/danny-avila/LibreChat)
- Releases: v0.8.9 (17 Nov, pre-release), v0.8.9-rc1 (26 Oct), v0.8.8 (01 Oct, flagged pre-release), rc1–rc4 of v0.8.8 (14 Aug–23 Sep), v0.8.7 (24 Jun, the last release not flagged as pre-release) — roughly one minor every 1.5–3 months with multiple RCs — [Releases](https://github.com/danny-avila/LibreChat/releases)
- ClickHouse acquired LibreChat on 4 Nov 2025; price undisclosed; founder Danny Avila and team joined ClickHouse; ClickHouse plans a native LibreChat experience in ClickHouse Cloud, visualization, enterprise security/governance and a semantic layer — [Business Wire](https://www.businesswire.com/news/home/20251104505230/en/ClickHouse-Acquires-LibreChat-to-Democratize-AI-Driven-Analytics-Through-the-Open-Source-Agentic-Data-Stack) (page returned 403 to me; details taken from search summary), [ClickHouse blog](https://clickhouse.com/blog/clickhouse-acquires-librechat) (says operations continue unchanged with ongoing investment; does not mention MIT; its metadata shows a conflicting date 2026-07-28 vs dateline 4 Nov 2025)
- HN thread: ClickHouse staff said the MIT license stays and focus is analytics features not SSO gating; commenters were skeptical ("beginning of the end", fear of enterprise tier/"SSO tax"), and noted the assurances are non-binding — [HN mirror](https://hn.jakechampion.name/item/45877770)
- Code Interpreter is powered by ClickHouse/code-interpreter (Apache 2.0, self-hosted) — [Search summary of LibreChat docs](https://www.librechat.ai/docs/features/code_interpreter), [repo](https://github.com/danny-avila/LibreChat)

#### Open WebUI
- 159.0k stars, 23.1k forks; README: "includes code under the Open WebUI License, which requires preserving the Open WebUI branding" — [GitHub repo](https://github.com/open-webui/open-webui)
- LICENSE: prohibits altering/removing/obscuring/replacing "Open WebUI" branding, except (i) deployments with <=50 end users in any rolling 30-day period, (ii) prior written permission from the copyright holder, or (iii) an executed enterprise license; violation is "material breach" — [LICENSE](https://github.com/open-webui/open-webui/blob/main/LICENSE)
- License is BSD-style plus branding clause since v0.6.6 (April 2025); its own docs say it is not OSI-approved (secondary/blog source, unverified by me) — [Community Impact blog (vendor-style)](https://sales.communityimpact.com/open-webui-vs-librechat-2026-best-self-hosted-ai-chat-interface.html)
- Releases: v0.13.4 (17 Nov), v0.13.3/.2/.1 (8 Nov), v0.13.0 (3 Nov), v0.12.5 (29 Oct), v0.12.4 (25 Oct), v0.12.3 (16 Oct) — very fast cadence (8 releases in ~5 weeks) — [Releases](https://github.com/open-webui/open-webui/releases)
- Company-backed with an Enterprise offering (enterprise docs, "Terminals (Enterprise)") — [GitHub repo](https://github.com/open-webui/open-webui)

#### LobeChat / LobeHub
- 85.8k stars, 16.4k forks; repo front page says "LobeHub Community License" while a README badge says Apache 2.0 (conflict on the page) — [GitHub repo](https://github.com/lobehub/lobe-chat)
- LICENSE: "LobeHub Community License, based on Apache License 2.0 with additional conditions": commercial use allowed incl. as a frontend/backend service without modifying source; "a commercial license must be obtained from the producer if you want to develop and distribute a derivative work"; producer may tighten the license later — [LICENSE](https://github.com/lobehub/lobe-chat/blob/canary/LICENSE)
- Releases: Desktop v2.3.4 "Latest" and v2.3.5-canary.1 both 18 Nov; frequent nightly PR builds — [Releases](https://github.com/lobehub/lobe-chat/releases)

#### Onyx
- Community Edition MIT; Enterprise Edition adds org features; 33.5k stars, 4.8k forks — [GitHub repo](https://github.com/onyx-dot-app/onyx)
- Latest v5.1.3 (16 Nov) plus helm chart releases up to 18 Nov — [Releases](https://github.com/onyx-dot-app/onyx/releases)

#### Dify
- 161k stars, 25.5k forks; "Dify Open Source License" = Apache 2.0 + conditions — [GitHub repo](https://github.com/langgenius/dify)
- Conditions: no operating a multi-tenant environment with the source without written authorization (one tenant = one workspace); may not remove/modify LOGO or copyright in the console/apps when using the `web/` frontend — [LICENSE](https://github.com/langgenius/dify/blob/main/LICENSE)

#### AnythingLLM
- MIT; 68.4k stars, 7.7k forks; latest version referenced v1.11.2 (release page not checked) — [GitHub repo](https://github.com/Mintplex-Labs/anything-llm)

#### Jan
- Apache 2.0; 45.8k stars; Tauri/Rust desktop app — [GitHub repo](https://github.com/janhq/jan)

#### Cherry Studio
- AGPL-3.0 (Community Edition); separate commercial license available by contacting vendor; Enterprise Edition adds private deployment, centralized model mgmt; 53.6k stars — [GitHub repo](https://github.com/CherryHQ/cherry-studio)

#### Big-AGI
- MIT; 7.2k stars; latest release listed "Open 2.1.3" (date not shown; 2.0 was 31 Oct 2025); hosted Pro at $10.99/mo; independent, non-VC — [GitHub repo](https://github.com/enricoros/big-AGI)

#### NextChat
- MIT; 89.0k stars, 58.5k forks; latest version named v2.15.8 (no date; last-commit date not shown — cannot confirm active) — [GitHub repo](https://github.com/ChatGPTNextWeb/NextChat)

#### Hugging Face chat-ui
- Apache-2.0; ~11.0k stars; SvelteKit + MongoDB; OpenAI-compatible endpoints only — [GitHub repo](https://github.com/huggingface/chat-ui)

#### Open Canvas (LangChain)
- MIT; 5.5k stars; ARCHIVED (read-only) by owner on 26 Feb 2026 — [GitHub repo](https://github.com/langchain-ai/open-canvas)

#### Goose
- Apache-2.0; 56.8k stars; part of the Agentic AI Foundation (Linux Foundation); Rust desktop/CLI agent — [GitHub repo](https://github.com/aaif-goose/goose)

#### OpenHands
- MIT per repo page (enterprise-folder license not confirmed by my fetch); 93.8k stars; now a self-hosted "Agent Canvas" control center for coding agents — [GitHub repo](https://github.com/OpenHands/OpenHands)

#### Dyad
- Apache 2.0 outside `src/pro`; `src/pro` is FSL 1.1 (fair-source); 22.3k stars; an app builder rather than a chat workspace — [GitHub repo](https://github.com/dyad-sh/dyad)

#### Chatbot UI (McKay Wrigley)
- MIT; the README points users to a hosted chatbotui.com; I found no 2026 activity evidence either way — [SourcePulse](https://www.sourcepulse.org/projects/743610)

#### Claude-style "artifacts"/design clones
- 13point5/open-artifacts archived 6 Oct 2024; open-codesign (MIT Electron, "Claude Design" clone, ~5.6k stars per a May 2026 roundup); open-design (Apache-2.0, local-first canvas, 20+ coding agents) — these are third-party roundups, not verified on repos — [Search results incl. pasqualepillitteri.it roundup](https://pasqualepillitteri.it/en/news/1518/open-source-claude-design-clones), [open-artifacts](https://github.com/13point5/open-artifacts)

### Inferences
- For later SMB commercialization, license risk ranking (best to worst): MIT (LibreChat, Onyx CE, AnythingLLM, Big-AGI, NextChat) > Apache (Jan, HF chat-ui, Goose) > custom (LobeHub: derivative distribution needs license; Open WebUI: cannot rebrand beyond 50 users without enterprise license; Dify: no multi-tenant SaaS) > AGPL (Cherry Studio; also copyleft network clause for SaaS).
- ClickHouse ownership gives LibreChat funding and stability but a strategic pivot risk toward analytics; MIT means the code can always be forked.
- Open WebUI's growth and cadence are the highest of the chat-first projects, but the license is the largest barrier to a white-label SMB product.

### Gaps
- Exact release dates with year, and current "latest stable" per repo for AnythingLLM, Jan, Cherry Studio, NextChat, Big-AGI, HF chat-ui; GitHub API was blocked.
- Whether LibreChat's v0.8.8/v0.8.9 "pre-release" tags indicate a deliberate stable-channel practice; I only saw the label.
- Open WebUI LICENSE_HISTORY and CLA implications (contributor assignment) not reviewed.

## 2. Stack, extensibility, MCP

### Takeaway
LibreChat is Node/TypeScript + MongoDB (+Redis/Meilisearch optional); Open WebUI is Python (FastAPI) + Svelte with an in-app Functions/Pipes plugin system; LobeHub is a Next.js/Vite + Postgres monorepo; Onyx is Python + Postgres/Vespa-style index and heavy multi-service. All of the chat-first candidates support MCP.

### Cited Findings
- LibreChat: JavaScript/TypeScript, Node, Bun, Turborepo; Docker/Helm; Redis config; OpenTelemetry/Langfuse; MongoDB inferred from compose files (page does not state it); MCP integration; agent Skills (SKILL.md), subagents, agent management API — [GitHub repo](https://github.com/danny-avila/LibreChat)
- Open WebUI: Python 3.12 backend, Svelte/TypeScript/Vite/Tailwind frontend, Docker image variants (:main, :slim, :cuda, :ollama); MCP via Streamable HTTP; Functions that can filter/transform/route messages — [GitHub repo](https://github.com/open-webui/open-webui), [Features docs](https://docs.openwebui.com/features/)
- LobeHub: Next.js + Vite SPA, Bun/pnpm workspaces, PostgreSQL (Drizzle ORM), Redis, RustFS, SearXNG, Better Auth; MCP marketplace — [GitHub repo](https://github.com/lobehub/lobe-chat)
- Onyx: vector+keyword index, background connector workers, model inference servers, Redis, MinIO; Lite mode <1GB without indexing; Docker/K8s — [GitHub repo](https://github.com/onyx-dot-app/onyx)
- Dify: Python API + Next.js web; Docker Compose with several services; MCP in agents; visual workflow canvas — [GitHub repo](https://github.com/langgenius/dify)
- AnythingLLM: Vite/React frontend, Node Express server + collector; MCP listed — [GitHub repo](https://github.com/Mintplex-Labs/anything-llm)
- Cherry Studio: Electron/TypeScript desktop; MCP client; no web/server version described — [GitHub repo](https://github.com/CherryHQ/cherry-studio)
- Jan: Tauri (Rust) desktop with extensions, MCP, local server at :1337 — [GitHub repo](https://github.com/janhq/jan)
- HF chat-ui: SvelteKit + MongoDB, MCP servers, router "Omni" needing a JSON policy — [GitHub repo](https://github.com/huggingface/chat-ui)
- Open Canvas: Next.js-style web + LangGraph agents, Supabase auth (archived) — [GitHub repo](https://github.com/langchain-ai/open-canvas)

### Inferences
- A solo developer forking for deep customization (system-controlled routing, cost bar) will find a single-language TypeScript monorepo (LibreChat) or Python+Svelte (Open WebUI) tractable; Onyx and Dify are multi-service systems with more surface area than needed.
- Open WebUI's Functions system lets some routing/cost logic be added without forking; LibreChat requires code changes or a proxy (e.g., LiteLLM) in front.

### Gaps
- Real-world forkability/code-quality assessments (test coverage, architectural cleanliness) were not found in independent sources.
- LibreChat's DB (MongoDB) is only inferred from compose-file names in the page I read; docs not fetched to confirm.

## 3. Native features vs requirements

### Takeaway
LibreChat has the closest native match to a Claude-style feature list (artifacts, agents, subagents, memory, projects, code interpreter with file output, skills, MCP). Open WebUI is stronger on built-in admin/analytics, RBAC/SSO, tabbed workspace, terminals/sandboxes, but its docs did not list artifacts, projects or deep research. None of them natively offer system-controlled per-task model routing or Claude-like automatic context management with always-visible cost.

### Cited Findings
- LibreChat features: agents (no-code, marketplace), Skills, Subagents, MCP, code interpreter (sandboxed, file upload/download), Artifacts (React/HTML/Mermaid), web search with scraping/reranking, image gen, presets, branching/forking, import/export, OAuth2/LDAP, admin panel, resumable streams; context compaction mentioned; persistent memory not found on the repo front page — [GitHub repo](https://github.com/danny-avila/LibreChat)
- LibreChat docs: Memory (saved facts added to conversations), Artifacts (React, HTML, SVG, Markdown, Mermaid), Code Interpreter, Agents, Projects (chats grouped with instructions + reference files); token usage tracked in Admin Insights dashboard; docs page did not cover file generation (docx/xlsx/pptx), deep research, compaction, reasoning effort — [LibreChat features docs](https://www.librechat.ai/docs/features)
- LibreChat release notes: v0.8.8 agent-managed memory with per-agent isolation; v0.8.7 skills authoring + GitHub sync; v0.8.8 interrupt/steer/queue controls and background task cards; v0.8.9 Chat Projects with shared instructions/files, resumable background subagent streams, experimental SDK-backed agents, Agent Channels (Slack, beta) — [Releases](https://github.com/danny-avila/LibreChat/releases)
- LibreChat balance system: `balance:` config in librechat.yaml, token credits, start balance, auto-refill, reservation of in-flight spend, display as credits/currency/percent — [Balance docs](https://www.librechat.ai/docs/configuration/librechat_yaml/object_structure/balance); (whether a per-message cost display exists was not confirmed)
- LibreChat file generation: code interpreter returns generated files persisted across turns; stateful sessions; docs confirm xlsx/csv inputs but no confirmation of docx/pptx/xlsx output — would depend on sandbox libraries or a Skill — [Search summary of docs](https://www.librechat.ai/docs/features/code_interpreter)
- Open WebUI v0.13.x: tabbed workspace (Desktop/Browser tabs, notes, channels, calendar), Git side panel, side chats, MCP Apps in chat, on-demand sandboxed terminals, "Tether" for local models/tools/MCP over stdio, coding agents (Codex, Claude Code, Copilot) selectable as chat models, built-in visualization and video generation tools (off by default), automations with agents — [Releases](https://github.com/open-webui/open-webui/releases)
- Open WebUI docs: code execution (Python in browser/Open Terminal), memory, web search with citations, "thinking effort" presets, MCP Streamable HTTP, RBAC/groups/SSO/OIDC/LDAP/SCIM 2.0, analytics dashboard (messages, tokens, cost); artifacts, projects, deep research, file generation not listed on that page (absence on one page, not proof of absence in product) — [Features docs](https://docs.openwebui.com/features/)
- Open WebUI Analytics: per-user token attribution built in; dollar cost is estimated manually from provider pricing per docs snippet; community functions/pipes (e.g., live cost tracker, token-tracking library) and LiteLLM add budgets — [Analytics docs](https://docs.openwebui.com/features/administration/analytics/), [Search results](https://docs.litellm.ai/docs/tutorials/openweb_ui.md)
- LobeHub: agents + Agent Teams (sequential/parallel/iterative/debate), memory (reviewable/editable), Resource Library, "Pages" documents, scheduled tasks, 40+ providers, channel bots (Discord, Slack, Telegram; DingTalk and WeCom added in v2.3.4), SSO; artifacts not mentioned — [GitHub repo](https://github.com/lobehub/lobe-chat), [Releases](https://github.com/lobehub/lobe-chat/releases)
- Onyx: deep research (multi-step), custom agents, artifacts for generated documents/downloadable files, secure sandbox for code, SSO (OIDC/SAML), SCIM, RBAC, usage analytics (appears under Enterprise heading; edition mapping not stated); projects and memory not mentioned on front page; v5.1.3 passes Word/PowerPoint/Excel files attached to Agents/Projects to Code Interpreter in original form; "Craft" sandbox — [GitHub repo](https://github.com/onyx-dot-app/onyx), [Releases](https://github.com/onyx-dot-app/onyx/releases)
- Dify: workflow canvas, RAG pipeline, agents with sandbox, observability integrations, BaaS API; not a Claude-style chat UI — [GitHub repo](https://github.com/langgenius/dify)
- AnythingLLM: workspaces, built-in agents/no-code agent builder, scheduled tasks, automatic memories, dynamic model routing, multi-user only in Docker — [GitHub repo](https://github.com/Mintplex-Labs/anything-llm)
- Cherry Studio: agents with workspaces/tool permissions, Skills + MCP, knowledge base, scheduled tasks, multi-model comparison; desktop only; artifacts not mentioned — [GitHub repo](https://github.com/CherryHQ/cherry-studio)
- Big-AGI: Beam multi-model, personas, chat cost estimation (since 1.16.0), reasoning-model support; no artifacts — [GitHub repo](https://github.com/enricoros/big-AGI)
- NextChat: history compression, optional MCP, plugins, Artifacts; browser-local storage — [GitHub repo](https://github.com/ChatGPTNextWeb/NextChat)
- HF chat-ui: LLM Router "Omni" (image -> multimodal route, MCP-enabled -> agentic route, else default) via user-supplied JSON policy — [GitHub repo](https://github.com/huggingface/chat-ui)
- Open Canvas: memory/reflections, artifact versioning, quick actions (archived) — [GitHub repo](https://github.com/langchain-ai/open-canvas)
- Goose: local general-purpose agent, 15+ providers, 70+ MCP extensions, desktop/CLI; not a chat workspace — [GitHub repo](https://github.com/aaif-goose/goose)
- OpenHands: self-hosted control center for coding agents with per-conversation Docker sandboxes — [GitHub repo](https://github.com/OpenHands/OpenHands)
- Dyad: local app builder, not a chat workspace — [GitHub repo](https://github.com/dyad-sh/dyad)
- Jan: local-first desktop, custom assistants, MCP — [GitHub repo](https://github.com/janhq/jan)

### Inferences
- Closest to the user's list: LibreChat (artifacts + projects + memory + agents/subagents + code interpreter + skills) with Onyx as the strongest on deep research/enterprise search but heavier and less chat-UX oriented.
- Per-task, system-controlled model routing and "smart context/token management" are not shipped as a policy engine by any candidate; this is where custom code (or a LiteLLM/OpenRouter-style gateway) is needed regardless of base. HF chat-ui's Omni router is the closest example of a routing concept but is minimal.
- Office-file generation (PDF/Excel/Word/PPT) likely must be built as skills/tools on a sandbox (code interpreter) in any base.
- Deep research is native only in Onyx among the verified candidates; LibreChat/Open WebUI would need an agent/MCP implementation.

### Gaps
- No verification that LibreChat Artifacts/Open WebUI artifacts handle PDF/Office previews; not found.
- Whether Open WebUI has artifacts/projects in 2026 is unverified (Open WebUI had HTML artifact rendering historically; my docs fetch did not list it).
- Whether LibreChat shows per-message token/cost live in the UI: not confirmed.
- Per-agent model assignment: LibreChat agents are "built on any model" (docs); depth of subagent model selection not verified.
- Onyx memory/projects: front page silent, but v5.1.3 notes reference Projects; treat as present but unverified in detail.

## 4. Chinese-model / custom-endpoint support and reasoning_content handling

### Takeaway
LibreChat has documented first-class Moonshot/Kimi support and explicit customParams knobs for reasoning_content replay; this is the best-documented handling found. For the others, evidence is thin.

### Cited Findings
- LibreChat supports OpenAI-compatible custom endpoints — [GitHub repo](https://github.com/danny-avila/LibreChat)
- Moonshot doc: for kimi-k2.5 / kimi-k2-thinking, the custom endpoint name must be "Moonshot" (case-insensitive) for interleaved reasoning with tool calls to work; otherwise error "thinking is enabled but reasoning_content is missing in assistant tool call message" — [LibreChat Moonshot docs](https://www.librechat.ai/docs/configuration/librechat_yaml/ai_endpoints/moonshot)
- LibreChat customParams supports `reasoningFormat`, `reasoningKey`, `includeReasoningContent`, `includeReasoningHistory` for gateways that need reasoning replayed — [LibreChat custom_params docs](https://www.librechat.ai/ja/docs/configuration/librechat_yaml/object_structure/custom_params)
- The same missing-reasoning_content failure occurs in other clients (Cursor BYOK with Kimi/DeepSeek) when reasoning is dropped from history after tool calls — a generic class of bug, not LibreChat-specific — [Cursor forum](https://forum.cursor.com/t/kimi-2-6-custom-model-provider-returned-error-error-message-thinking-is-enabled-but-reasoning-content-is-missing/159625/5)
- Open WebUI: connects to Ollama and OpenAI-compatible APIs; "thinking effort" presets — [GitHub repo](https://github.com/open-webui/open-webui), [Features docs](https://docs.openwebui.com/features/)
- LobeHub: 40+ providers; DingTalk/WeCom bots (China ecosystem) — [GitHub repo](https://github.com/lobehub/lobe-chat), [Releases](https://github.com/lobehub/lobe-chat/releases)
- NextChat lists DeepSeek and Baidu among providers — [GitHub repo](https://github.com/ChatGPTNextWeb/NextChat)
- Dify topics mention DeepSeek; Jan lists MiniMax among cloud providers; Cherry Studio is a China-origin product with local-model support — [Dify](https://github.com/langgenius/dify), [Jan](https://github.com/janhq/jan), [Cherry Studio](https://github.com/CherryHQ/cherry-studio)

### Inferences
- Because the user wants system-controlled routing across any provider, putting a gateway (LiteLLM/OpenRouter-style, or custom) between the UI and providers normalizes reasoning_content handling in one place, regardless of base. This is my inference, not a sourced recommendation.

### Gaps
- No evidence gathered on Open WebUI, LobeHub or Onyx handling of DeepSeek/Kimi reasoning_content in multi-turn tool calling.
- GLM (Z.ai), Qwen, MiniMax-specific behaviors not researched.

## 5. Known problems: security, performance, maintenance, UX

### Takeaway
Both leading candidates have had frequent serious CVEs in 2026, concentrated around MCP, code-execution, file handling and OAuth; a self-hosted internet-facing deployment needs patch discipline. LibreChat's problems are mostly MCP/agents plumbing; Open WebUI's include cross-user RCE reports.

### Cited Findings
- LibreChat: CVE-2026-22252 (critical, CVSS 9.1; MCP stdio command injection, fixed v0.8.2-rc2); CVE-2026-32625 (critical per one aggregator; MCP URL placeholder secret exfiltration, <=0.8.3); CVE-2026-34371 (arbitrary file write via execute_code, fixed 0.8.4); CVE-2026-54030 (OAuth token theft, CVSS 9.3, details not found); CVE-2026-44653 (shared MCP view leaks admin secrets); March 2026 SSRF, IDOR in SSE stream and MCP OAuth callback token theft — [Search results via SentinelOne/NVD/aggregators](https://nvd.nist.gov/vuln/detail/CVE-2026-32625), [SentinelOne](https://www.sentinelone.com/vulnerability-database/cve-2026-22252/); sources disagree on some scores (aggregators; I did not open the GitHub advisories)
- Open WebUI: CVE-2026-56400 (critical, CVSS 9.6; CORS misconfiguration -> RCE, per Wiz), CVE-2026-87016 (OAuth/SQLite auth bypass, High 8.1, fixed 0.11.1), CVE-2026-28788 (file overwrite, fixed 0.8.6), CVE-2026-54009 (cross-user file disclosure), a July 2026 write-up on cross-user code-interpreter RCE via Socket.IO session ID (v0.9.6), and Tenable advisory TRA-2026-39; some CVEs against it were disputed/rejected (CVE-2026-0767) — [Wiz](https://www.wiz.io/vulnerability-database/cve/cve-2026-56400), [Open WebUI vendor disposition](https://docs.openwebui.com/security/vendor-dispositions/cve-2026-0767/), [Tenable](https://it.tenable.com/security/research/tra-2026-39), [aicybr blog](https://aicybr.com/blog/open-webui-cve-2026-87016-oauth-sqlite-auth-bypass), [CraftedSignal](https://feed.craftedsignal.io/briefs/2026-07-open-webui-cross-user-rce/); third-party trackers disagree, verify against GitHub advisories
- LibreChat performance: MeiliSearch indexing latency on very large histories (10k+ messages) — [toolhalla review (affiliate-style)](https://toolhalla.ai/blog/librechat-review-open-source-chatgpt-alternative-2026)
- Open WebUI gotcha: after update to 0.12.5 without WEBUI_SECRET_KEY, old sessions return 401 — [Search summary of a tutorial](https://lumadock.com/tutorials/openwebui-vs-librechat)
- LibreChat v0.8.9 notes require a migration for deployments with durable MCP name reservations — [Releases](https://github.com/danny-avila/LibreChat/releases)
- Open WebUI v0.13.x shipped 3 patch releases in one day (8 Nov) including fixes for plain HTTP chat loading — signals fast but churny releases — [Releases](https://github.com/open-webui/open-webui/releases)
- UX: a vendor-style comparison rated LobeChat UI polish "Excellent" vs "Good" for Open WebUI/LibreChat — treat as opinion — [Elest.io blog](https://blog.elest.io/librechat-vs-openwebui-vs-lobe-chat-which-to-self-host-in-2026/), [search summary]

### Inferences
- Any base needs sandboxing for code execution and strict MCP controls; the CVE pattern (MCP, code interpreter, file/object authorization) is exactly the feature area the user wants (agents, file generation, browser agent), so security design should be a first-order requirement.

### Gaps
- Could not find first-hand Reddit/HN experience reports of using these as a Claude replacement; the searches returned only vendor/affiliate comparison blogs. GitHub issue health (open-issue counts) obtained only partly: AnythingLLM 321 open issues, Jan 402, Goose 364, HF chat-ui 210 ([repos above](https://github.com/Mintplex-Labs/anything-llm)); none for LibreChat/Open WebUI.
- No CVE data collected for LobeHub, Onyx, Dify, AnythingLLM, Cherry Studio.

## 6. Community reviews and real-user experiences

### Takeaway
Independent first-hand reviews are scarce in what I could access; consensus among (mostly vendor/affiliate) comparisons is Open WebUI = local/Ollama + RAG, LibreChat = multi-provider/commercial APIs, LobeChat = polish.

### Cited Findings
- Consensus positioning and caveat that these sources are vendor/affiliate and have no benchmarks — [Search summary: elest.io, sliplane, requesty, onyx.app comparisons](https://blog.elest.io/librechat-vs-openwebui-vs-lobe-chat-which-to-self-host-in-2026/), [Onyx insights (Onyx is a competitor, biased)](https://onyx.app/insights/openwebui-vs-librechat-vs-onyx)
- HN reaction to ClickHouse deal described above; some users call LibreChat their favorite open-source LLM frontend — [HN mirror](https://hn.jakechampion.name/item/45877770)
- Star counts in some blogs are stale (e.g., 36,840 LibreChat / 136,533 Open WebUI) vs fetched 47.3k / 159.0k — [Community Impact blog](https://sales.communityimpact.com/open-webui-vs-librechat-2026-best-self-hosted-ai-chat-interface.html)

### Inferences
- Treat star count differences as adoption signal only (Open WebUI > LibreChat by about 3x); for forking, code quality and license matter more.

### Gaps
- Reddit r/selfhosted, r/OpenWebUI, r/LocalLLaMA threads and GitHub Discussions were not retrieved.

## 7. Fit for commercialization and recommendation (comparison matrix)

### Takeaway
Top 3: (1) LibreChat as the fork base (MIT, closest feature match, TypeScript, MCP/agents/artifacts/memory/projects), accepting ClickHouse-ownership and MCP-security risk; (2) Onyx CE (MIT) if deep research / enterprise search / SMB knowledge is central, accepting heavier infrastructure; (3) Open WebUI as the fastest-moving option for personal single-user use only, not as a commercial white-label base (branding clause) — or build a thin custom app on a gateway if LibreChat's structure fights the system-controlled routing design.

### Cited Findings
Matrix (Y = verified in sources above, ~ = partial/unverified, N = not found/absent; license column is the commercialization gate):

| Candidate | License | Stars | Cadence (Nov 2026) | Artifacts | File/Doc gen | Code interp. | Projects | Memory | Deep research | Agents/subagents | Per-task routing | Cost/usage | Multi-user/SSO | MCP | Fit as base |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LibreChat | MIT | 47.3k | ~1.5–3 mo minors + RCs | Y | ~ (code interp. files) | Y | Y (v0.8.9) | Y | N | Y (subagents, skills) | N (agent-level model only) | ~ (balance/credits, admin insights) | Y | Y | Best |
| Open WebUI | Custom, branding lock (<=50 users free) | 159.0k | Multiple/wk | ~ | ~ | Y | ~ | Y | N | ~ (automations, coding agents) | N (Functions could route) | Y analytics tokens/cost; $ manual | Y strong | Y | Good personally; poor for white-label |
| LobeHub | Apache+conditions (derivative distro needs license) | 85.8k | Multiple/wk | N (Pages) | N | ~ | ~ | Y | N | Y (teams) | N | ~ | Y | Y | Polished UX; license + heavy stack risk |
| Onyx CE | MIT (+EE) | 33.5k | ~weekly | Y | Y | Y (sandbox) | ~ | ~ | Y | Y | ~ | ~ (EE analytics) | Y (SSO mostly EE) | ~ | Best for deep research/SMB knowledge |
| Dify | Apache+multi-tenant/logo conditions | 161k | n/a | N | N | ~ | N | N | ~ | Y workflows | ~ | Y (LLMOps) | Y | Y | Workflow builder, not chat UX; SaaS barred |
| AnythingLLM | MIT | 68.4k | n/a | N | N | N | ~ (workspaces) | Y | N | Y | ~ (dynamic routing) | N | Docker only | Y | Simple RAG; not Claude-like |
| Cherry Studio | AGPL-3.0 | 53.6k | n/a | N | N | N | N | N | N | Y | N | N | N (desktop) | Y | Desktop power-user; AGPL |
| Jan | Apache-2.0 | 45.8k | n/a | N | N | N | N | N | N | ~ | N | N | N | Y | Local desktop; no |
| Big-AGI | MIT | 7.2k | n/a | N | N | N | N | N | N | N | N | Y cost est. | Paid hosted | ~ | Small, good BYOK UI |
| NextChat | MIT | 89.0k | unknown/stale? | Y | N | N | N | N | N | N | N | N | N | ~ | Lightweight; weak |
| HF chat-ui | Apache-2.0 | ~11.0k | unknown | N | N | N | N | N | N | ~ | ~ (Omni router) | N | ~ | Y | Minimal, router idea only |
| Open Canvas | MIT | 5.5k | Archived Feb 2026 | Y | N | N | N | Y | N | ~ | N | N | Supabase | N | Do not use |
| Goose | Apache-2.0 | 56.8k | n/a | N | N | Y (agent) | N | N | ~ | Y | N | N | N | Y | Agent runtime; possible component for browser/desktop agent |
| OpenHands | MIT (per page) | 93.8k | v1.42.0 referenced | N | N | Y | N | N | N | Y | N | N | ~ | ~ | Coding agent runtime, not chat workspace |
| Dyad | Apache + FSL pro folder | 22.3k | n/a | N | N | N | N | N | N | ~ | N | N | N | ~ | App builder; wrong category |
| Chatbot UI | MIT | n/a | unclear, hosted shift | N | N | N | N | N | N | N | N | N | Supabase | N | Skip |

Sources for all matrix rows: the per-candidate repo/doc links listed in sections 1-5. "n/a" means the release page was not fetched.

- Commercial angle for LibreChat: MIT permits rebranding and SaaS; risk is ClickHouse's strategic direction, with promised continued OSS investment — [ClickHouse blog](https://clickhouse.com/blog/clickhouse-acquires-librechat), [HN](https://hn.jakechampion.name/item/45877770)
- Commercial angle for Open WebUI: rebranding allowed only <=50 users or with permission/enterprise license — [LICENSE](https://github.com/open-webui/open-webui/blob/main/LICENSE)
- Commercial angle for LobeHub: derivative works distribution needs commercial license — [LICENSE](https://github.com/lobehub/lobe-chat/blob/canary/LICENSE)
- Commercial angle for Dify: no multi-tenant operation without authorization — [LICENSE](https://github.com/langgenius/dify/blob/main/LICENSE)
- Commercial angle for Cherry Studio: AGPL-3.0 with commercial license available — [GitHub repo](https://github.com/CherryHQ/cherry-studio)

### Inferences
- Honest ranking for this user's requirements:
  1. LibreChat (fork or run + extend via agents/MCP/skills and a gateway). Pros: MIT, native artifacts/projects/memory/subagents/skills/code interpreter, MCP, balance system, multi-user. Cons: no native per-task system routing, cost bar may need custom UI, MongoDB, repeated MCP/execution CVEs, ownership by a database company, "pre-release" labeling of latest builds.
  2. Onyx CE (if deep research and SMB knowledge/connectors dominate). Pros: MIT CE, native deep research, agents, artifacts, sandbox. Cons: heavy multi-service stack, many valuable org features in EE, less proven as a general Claude-style chat UX (unverified), memory/projects unconfirmed.
  3. Open WebUI (single-user phase only) or build-from-scratch around a gateway. Open WebUI has the best momentum and admin/analytics, but branding lock blocks SMB white-label commercialization; building from scratch gives full control over routing/context/cost but costs months to reach parity on artifacts, memory, projects and file generation.
- Not recommended as base: Cherry Studio (AGPL desktop), Jan (local-first desktop), Chatbot UI, NextChat, Open Canvas (archived), Dyad, OpenHands/Goose (agent runtimes — but consider Goose/OpenHands as components for the later browser/computer agent).
- Architectural suggestion (inference): regardless of base, put a LiteLLM-like gateway or custom router service in the middle so routing, reasoning_content normalization, token/cost metering and Chinese-provider quirks are system-owned, which also keeps the UI swappable.

### Gaps
- No quantified comparison of effort to fork versus build from scratch; the estimate is judgment, not sourced.
- Onyx memory/projects/UX quality and real-world reviews not verified; Onyx's own blog comparisons are competitor content.
- I did not verify Msty (proprietary desktop; search returned nothing on its license), Kimi/Z.ai open apps, LibreChat forks, or 2026 "Claude clones" beyond the third-party roundup of Artifact/Design clones (open-codesign, open-design), whose stars and activity are unverified.
- Releases pages show no year; fetch tool summaries could miss details (release pages truncated at 100,000 characters).
