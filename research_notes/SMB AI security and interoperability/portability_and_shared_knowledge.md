# Portability and shared knowledge across AI platforms (Claude, ChatGPT, Gemini, Copilot, LibreChat/Open WebUI), as of 2026-11-20

Source-quality note: Official help centers/vendor posts are marked "(official)"; blogs, news and community write-ups are marked "(secondary)". Several 2026 items (Claude Code AGENTS.md fallback, Agent Plugins, A2A transfer to AAIF, Open Memory Protocol) were found only via news/secondary sources or a search summary and could not be verified on the primary page; flagged inline. OpenAI help-center pages returned HTTP 403 to fetch, so OpenAI help-center claims below come from search-result snippets or secondary sources and are labelled. No Gemini/Workspace admin-level and no Microsoft self-service chat-export docs were verified.

## 1. Data export formats and what is in them

### Takeaway
All four vendors offer a self-service or admin export, but none exports "projects + memory + instructions" as a complete, re-importable bundle. Chat history is the only reliably portable item (ChatGPT `conversations*.json` and Claude `conversations.json` import into LibreChat; Open WebUI auto-detects ChatGPT; Gemini imports ChatGPT/Claude ZIPs for personal accounts outside EEA/UK/CH). Projects, custom GPTs, Gems and Copilot agents have no portable export format.

### Cited Findings
**ChatGPT**
- Export is requested at Settings > Data controls > Export data, or via the OpenAI Privacy Portal. The ZIP contains conversations in JSON plus other data in CSV or other formats; it can take up to 7 days; the download link expires 24 hours after receipt; deleted chats cannot be restored (official, via search snippet) — [OpenAI help 7260999](https://help.openai.com/en/articles/7260999-exporting-your-chatgpt-history-and-data)
- Self-service export is not available for ChatGPT Business, Enterprise or Healthcare workspaces (requests go to the workspace owner); Edu depends on admin settings and role (official, via search snippet) — [OpenAI help 7260999](https://help.openai.com/en/articles/7260999-exporting-your-chatgpt-history-and-data). Versions of the article differ on whether the file is chat.html or JSON, and on whether Go is listed.
- Community reverse-engineered layout (secondary): partitioned `conversations-NNN.json` (array of conversation objects with title, timestamps, model slug, flags); a `mapping` dictionary of nodes forming a DAG (edits/regenerations create branches), a current-node pointer, and a root node with no message; `export_manifest.json`, `user.json`, `user_settings.json`, `message_feedback.json`, `chat.html` (often >100 MB), uploaded files named `file-<ID>-<name>`, per-conversation image folders, `dalle-generations/`, and canvas/project workspace folders — [chatgpt-to-markdown docs](https://difegam.github.io/chatgpt-to-markdown/explanation/export-format). Another secondary guide says the tree must be walked to linearize a conversation — [Level Up Coding](https://levelup.gitconnected.com/your-chatgpt-history-is-a-tree-not-a-transcript-2026-5660ceb301d4)
- Memory and custom instructions "are included" per one secondary guide, but no official OpenAI source confirming this was found — [ai-chat-importer](https://ai-chat-importer.com/guides/chatgpt-export-format-explained). Treat as unverified.
- Reported incomplete exports exist (a user reported nothing before 2024-10-28) (secondary, community forum) — [OpenAI community](https://community.openai.com/t/incomplete-data-export-with-conversations-json/1019950)

**Claude**
- Individuals on Free/Pro/Max/Ultra export from Settings > Privacy on web or Claude Desktop (not mobile). Export contains conversation data, account user data and shared voice recordings; it excludes original uploaded files; the help page does not mention Projects or Memory and does not state the file format. Download link expires after 24 hours and may work once. Team/Enterprise members can export their own chats only if an owner enables "Allow members to export their own data"; Primary Owners export org-wide data from Organization settings > Data and privacy (official) — [Claude help: export your data](https://support.claude.com/en/articles/9450526-how-to-export-your-claude-data)
- Official page also says exported data cannot be imported into another personal Claude account (personal-account migration not supported) — same source.
- Third-party guides list `conversations.json`, `user_profile.json`, `usage.json` and say Projects and memory are not in the standard export (secondary) — [takeoutday.org](https://takeoutday.org/guides/how-to-export-claude-data). File names conflict with other sources (LibreChat docs refer to `conversations.json` inside the Claude archive) — [LibreChat docs](https://www.librechat.ai/docs/features/import_convos). Verify against a real export.

**Gemini / Google**
- Google Takeout: tick "Gemini" for Gems data and "My Activity > Gemini Apps" for chats, generated media and uploads; delivery by email link (7 days), Drive, Dropbox, OneDrive or Box; `.zip` or `.tgz`; one-off or recurring; takes hours to days. The page does not mention memory and does not address Workspace accounts (official) — [Google: Download your Gemini Apps data](https://support.google.com/gemini/answer/16920332)
- Activity records default to HTML; JSON is selectable (secondary; guides disagree on default) — [takeoutday.org Gemini guide](https://takeoutday.org/guides/gemini-data-export)

**Microsoft**
- No self-service per-user chat export was found. Microsoft's route is admin-driven: Copilot prompts and responses are stored in the user's mailbox and discovered/exported via Purview eDiscovery; GDPR DSR guidance describes portability as a machine-readable electronic copy (official) — [Microsoft Learn GDPR DSR](https://learn.microsoft.com/en-us/compliance/regulatory/gdpr-dsr-office365). A May 2026 Microsoft community blog says Copilot produces prompts, responses, memories and Pages, and full-text search of .page files is not available in eDiscovery review sets (secondary/vendor blog) — [Tech Community](https://techcommunity.microsoft.com/t5/microsoft-security-community/collecting-microsoft-365-copilot-data-with-microsoft-purview/ba-p/4516489)

**LibreChat / Open WebUI**
- LibreChat imports ChatGPT, Claude, ChatbotUI v1 and LibreChat JSON; users unzip the archive and upload `conversations.json` at Settings > Data & Privacy; format is auto-detected from content; default max file 250 MiB (admin env `CONVERSATION_IMPORT_MAX_FILE_SIZE_BYTES`); a single conversation or message is limited to about 16 MB; rate limited per user/IP (official) — [LibreChat docs](https://www.librechat.ai/docs/features/import_convos). Verified: yes, ChatGPT and Claude imports are documented; a secondary search summary says Claude "thinking blocks" are imported.
- LibreChat export, one conversation at a time (no bulk): Markdown (default), Text, JSON (re-importable), CSV, Screenshot PNG; "export all branches" for JSON/CSV only; PDF is not listed (official) — [LibreChat docs](https://www.librechat.ai/docs/features/import_convos)
- Open WebUI imports its own JSON, ChatGPT exports (auto-detected via `mapping` key) and custom JSON that follows its schema; no built-in converter for Claude or Gemini; export is all chats as one JSON; docs do not mention PDF/TXT, admin export, or export of models/prompts/knowledge (official) — [Open WebUI docs](https://docs.openwebui.com/features/chat-conversations/data-controls/import-export.md)

### Inferences
- A one-click "chat history" mover is feasible for ChatGPT -> LibreChat/Open WebUI/Gemini today; the other direction (into ChatGPT) is not supported by anything found.
- The ChatGPT tree (`mapping`/`current_node`) is the stable, documented-by-community structure that importers already depend on (LibreChat, Open WebUI); Claude's file names are less certain.
- Workspace/Business/Enterprise tiers are the weakest for self-service export (OpenAI Business/Enterprise: owner-only; Claude Team: owner must enable; Microsoft: eDiscovery admin).

### Gaps
- No official OpenAI page found stating whether memory, projects, custom GPTs are in the export ZIP (help pages 403 on fetch).
- No official schema from OpenAI or Anthropic for the JSON; all schema knowledge is reverse-engineered.
- Microsoft: no per-user export doc found; Copilot memory export path unconfirmed.
- Gemini: whether memory is included in Takeout and Workspace-account behaviour unconfirmed.

## 2. Memory portability

### Takeaway
Memory portability is currently a copy/paste of a text summary generated by a prompt, not a file format. Claude and Gemini both ship "import memory from another AI" flows; neither is lossless. Open memory formats/servers exist (OpenMemory MCP, MacPaw Portable Memory proposal) but are not adopted by the big vendors.

### Cited Findings
- Claude memory import: available on Free, Pro, Max, Ultra, Team and Enterprise, on web and Claude Desktop. Flow: Settings > Your Claude (or Settings > Memory) > "Start import"; copy Anthropic's prompt, run it in the other AI to list stored memories in a code block (with dates), paste back and "Add to memory". Claude extracts entries; work-focused design may drop unrelated personal details; labelled experimental; legacy Team/Enterprise experience uses "memory edits" that can take up to 24 hours (official) — [Claude help 12123587](https://support.claude.com/en/articles/12123587-importing-and-exporting-your-memory-from-chatgpt-and-other-ai-providers)
- Claude memory export: Settings > Your Claude > Manage next to "Your memory", or ask Claude in chat to write memories verbatim, then save locally or paste into another service (official) — same source.
- Gemini import (memory + chat history): personal Google Accounts only (not work/school/supervised); 18+; memory via a copy-prompt flow; chat history via `.zip` up to 5 GB, up to 5 zips/day, processing up to a day; NOT available in EEA, Switzerland or UK; imported chats are saved in Activity and may be used to improve Google services including training generative AI; re-uploading overwrites previously imported conversations (official) — [Google: Import from other AI platforms](https://support.google.com/gemini/answer/16868299?hl=en)
- ChatGPT: no standalone "import memory" or official memory-export feature found. Only a search-derived statement that no article confirms a standalone memory export; separate-by-design memory vs training controls (official snippet) — [OpenAI data controls](https://help.openai.com/articles/7730893-data-controls-in-chatgpt). The paste-prompt method (ask ChatGPT to list all memories) is what Claude's flow relies on.
- Shared ChatGPT projects have project-only memory, described by OpenAI Academy as available on Enterprise/Business when workspace memory is enabled (official-ish, via search summary) — [OpenAI Academy](https://academy.openai.com/en/public/clubs/work-users-ynjqu/resources/projects). A Business user reports that sharing a project forces memory to project-only, disables File Library and Work Mode (secondary, unverified community post) — [OpenAI community](https://community.openai.com/t/business-shared-projects-should-support-work-mode-shared-memory-and-shared-file-library/1388787)
- Open memory servers/formats: Mem0's OpenMemory MCP is a local memory server shared by MCP-compatible tools; its cloud MCP server is a different product that stores data in Mem0's cloud (vendor blog/secondary) — [Mem0](https://mem0.ai/blog/introducing-openmemory-mcp). MacPaw "Portable Memory" (July 2026 preprint) proposes a `.mem` bundle with canonical serialization, tombstones and optional Ed25519 signing; a proposal, not adopted — [MacPaw Research](https://research.macpaw.com/publications/portable-memory). A June 2026 article describes an "Open Memory Protocol" with early adapter gaps (secondary news; not verified) — [WinBuzzer](https://winbuzzer.com/2026/06/30/open-memory-protocol-gives-compatible-ai-tools-one-memory-st-xcxwbn/)
- Microsoft Copilot memories exist as Copilot-generated data discoverable in Purview (secondary) — see section 1.

### Inferences
- A "memory" mover should treat memory as a human-reviewable Markdown file the user approves, not a sync. Each platform re-summarises on import (Claude keeps mainly work content), so round-tripping loses fidelity.
- Gemini's import is consumer-only and EEA/UK/CH-excluded, so it cannot serve an EU workspace.
- For team context, a shared Markdown "context" file in the shared knowledge store is more reliable than personal memory import.

### Gaps
- No confirmed ChatGPT official memory export page; no Microsoft Copilot memory export page.
- No evidence that any big vendor reads an open memory format (OpenMemory, `.mem`, Open Memory Protocol) natively.

## 3. Project and instruction portability

### Takeaway
Product objects (Claude Projects, ChatGPT Projects/Custom GPTs, Gemini Gems, Copilot declarative agents) are not exportable to each other. What travels is plain files: Markdown instructions, knowledge documents, SKILL.md skill folders (open standard, widely adopted), AGENTS.md (coding-agent oriented), and MCP servers/Agent Plugins bundles.

### Cited Findings
- Claude Projects: Team/Enterprise members can share projects with individuals, email lists or the whole org; "Can view" vs "Can edit" levels; owners can turn off sharing (Enterprise: per role); project knowledge uses RAG mode to expand capacity as it nears context limits; a new projects beta is rolling out (official) — [Claude help: projects](https://support.claude.com/en/articles/9517075-what-are-projects)
- Claude's Google Drive connector can be added to Files only in private projects; the option is disabled for shared projects (official, via search summary) — [Claude help 9519177](https://support.claude.com/en/articles/9519177-add-content-to-projects)
- ChatGPT Projects: sharing available in Business, Enterprise, Edu and (per help center) Free/Go/Plus/Pro; chat access vs edit access; up to 100 collaborators; up to 40 files in Business/Enterprise/Edu projects; deleting a file removes it for everyone; Enterprise/Edu admin controls default off (OpenAI launch post / help center via search summary) — [OpenAI](https://openai.com/index/more-ways-to-work-with-your-team), [OpenAI Academy](https://academy.openai.com/en/public/clubs/work-users-ynjqu/resources/projects)
- Gemini Gems: sharing uses Drive-style sharing and can be disabled by admins; Gems are only shareable when custom knowledge is device uploads or Drive files; NotebookLM sources reportedly cannot be shared via a Gem (official for Drive-based sharing, secondary for the NotebookLM limit) — [Workspace Updates](https://workspaceupdates.googleblog.com/2025/09/gem-sharing-gemini-app-workspace.html)
- Microsoft: a Copilot agent equals a declarative agent; builders can use SharePoint sites/folders/files, web and Copilot connectors as knowledge; access follows the user's SharePoint/OneDrive permissions; Copilot Studio supports MCP servers (GA per Microsoft FAQ) and A2A (public preview per FAQ; conflicting conference deck says "announced, rolling out") (official/secondary mix) — [Microsoft Learn: knowledge sources](https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/knowledge-sources), [Copilot Studio FAQ](https://adoption.microsoft.com/files/copilot-studio/Microsoft-Copilot-Studio_FAQ.pdf)
- Agent Skills (SKILL.md folders): published as open standard Dec 2025; Anthropic announced on 2026-10-22 it is donating the spec, name/logo, GitHub org and agentskills.io to the Agentic AI Foundation (AAIF, Linux Foundation); Anthropic says more than 70 agent platforms (incl. ChatGPT, Cursor, GitHub Copilot, VS Code) integrate it, ~1 million skills published, nearly 280 million installed (vendor-reported, unaudited); maintainers include engineers from Anthropic, Google, OpenAI (official) — [Anthropic](https://www.anthropic.com/news/donating-agent-skills-to-the-agentic-ai-foundation)
- ChatGPT skills: OpenAI docs say standalone skills are in the ChatGPT desktop app, Codex CLI and IDE extension, and plugin-bundled skills in ChatGPT web/desktop/mobile (via search summary of OpenAI docs) — [OpenAI skills docs](https://learn.chatgpt.com/docs/build-skills). Install paths differ (`.claude/skills/` vs `.agents/skills/`) and host-specific front-matter fields are not portable (secondary) — [Cross-agent compatibility guide](https://serhiismetanskyi.github.io/digital-garden/ai-skills/06-cross-agent-compatibility/)
- Agent Plugins (published 2026-08-06): a `plugin.json` folder bundling MCP servers and Agent Skills; shaped by Amazon, Cursor, GitHub, Microsoft, OpenAI, Vercel; steering committee Amazon, Cursor, Microsoft, OpenAI, Vercel; ChatGPT, Codex, Cursor, GitHub Copilot, Kiro and VS Code support it at launch; marketplaces, install, permissions and trust are left to each client; critics call it thin (secondary: The Next Web; Anthropic not listed among members) — [TNW](https://thenextweb.com/news/openai-agent-plugins-open-standard-skills-mcp). A different outlet's summary treats Agent Plugins' relationship to Skills as unclear.
- AGENTS.md: contributed by OpenAI to AAIF in Dec 2025; AAIF self-reports >60,000 open-source projects (unaudited). Claude Code reportedly added an AGENTS.md fallback (when no CLAUDE.md) in v2.1.277 on 2026-09-18, behind feature flags, not on Bedrock/Vertex/Foundry (secondary: AI Weekly, InfoWorld, DevOps.com via search summary; not verified on Anthropic's own docs) — [AI Weekly](https://aiweekly.co/alerts/anthropic-adopts-openais-agentsmd-spec-in-claude-code-21277-falls-back-to-it), [InfoWorld](https://infoworld.com/article/4224410/claude-code-now-also-accepts-instructions-in-openais-agents-md-format.html). AGENTS.md/CLAUDE.md are repo-file conventions for coding agents, not read by the chat apps' Projects.

### Inferences
- "What can be synced": instruction text (copy/paste), knowledge files (same files uploaded or, better, referenced via connectors), SKILL.md folders, MCP server URLs. "What cannot": project object itself, project memory, Custom GPT Actions config, Gems, Copilot agent manifests, chat-project association, sharing ACLs.
- Because Claude's Drive connector is disabled in shared projects and ChatGPT shared projects have file/memory quirks, project-level knowledge is least portable exactly when a team uses it; connectors at account level are the portable layer.
- Skills are the most credible basis for a portable "instructions + procedure" unit; AGENTS.md matters only for repo-based/coding tools.

### Gaps
- No official, citable export for ChatGPT Custom GPT instructions/Actions or Gems; no Copilot agent export (beyond Copilot Studio solutions) was researched.
- Anthropic's own docs not checked for AGENTS.md; the claim rests on secondary sources.
- ChatGPT help-center project limits not fetched directly (403).

## 4. Shared knowledge as common ground (Drive, SharePoint, Notion, Confluence, Git/Markdown)

### Takeaway
All major tools have official connectors that run with the user's own permissions for Google Drive and SharePoint/Microsoft 365; Notion and Confluence support is uneven. Pattern: keep one source of truth in Drive or SharePoint (or a Git/Markdown repo mirrored to one), let each AI read it through connectors, and let non-technical users edit in Docs/Word/Notion normally.

### Cited Findings
- ChatGPT connectors respect existing user permissions for Drive and SharePoint; Enterprise/Edu connectors default off with group-level admin control; "synced" connectors for Drive (Team/Enterprise/Edu) and SharePoint (Pro/Business/Enterprise/Edu) pre-index content; Microsoft connectors require Entra permissions; employees can get different answers because of different access (secondary: Varonis, CData; official OpenAI SharePoint help snippet) — [OpenAI SharePoint connector help](https://help.openai.com/en/articles/12143177-sharepoint-connectors-in-chatgpt), [Varonis](https://www.varonis.com/blog/chatgpt-enterprise-connectors). Official OpenAI evidence for Notion/Confluence not found.
- Claude Microsoft 365 connector: Team/Enterprise only; Owner/Primary Owner plus Entra Global Admin setup; work/school accounts only; access is delegated (Claude can only access what the user already can); newly uploaded docs may need indexing time (official) — [Claude help 10166901](https://support.claude.com/en/articles/10166901-using-the-microsoft-365-connector), [Claude docs](https://claude.com/docs/connectors/microsoft/365.md)
- Claude Google Drive connector: each user signs in with their own Google account, so access is limited to what that account can open; Google Docs added to chats/projects sync from Drive (official) — [Claude Drive connector docs](https://claude.com/docs/connectors/google/drive). Claude's connector guidance recommends GitHub connector with Projects for persistent codebase context — [Claude connector getting started](https://claude.com/docs/connectors/getting-started.md)
- Gemini: Gems can use Drive files as knowledge; Gemini Enterprise lists Confluence Cloud and Notion among third-party connectors (Notion connector can create/update pages and databases); NotebookLM notebooks can be added as a source in Gemini for Workspace users (official Google FAQ/release notes via search summary) — [Gemini Enterprise FAQ](https://cloud.google.com/gemini-enterprise/faq), [Workspace Updates Jan 2026](https://workspaceupdates.googleblog.com/2026/01/take-notebooks-further-notebooklm-gemini.html)
- Microsoft 365 Copilot agents ground on SharePoint/OneDrive content the user can access, plus Copilot connectors (official) — [Microsoft Learn](https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/knowledge-sources)
- Connector permission inheritance has a data-exposure side: over-shared SharePoint/Drive content becomes searchable through AI (vendor security blog) — [Varonis](https://www.varonis.com/blog/chatgpt-enterprise-connectors)

### "Shared project folder" pattern (inference, built on the above)
- One folder (Drive "Team AI Context" or SharePoint library) holding: `context.md` (what/why/glossary), `instructions.md` (tone, rules), `decisions.md`, source documents. Non-technical users edit in Docs/Word; nothing needs to be re-uploaded. Power users connect Claude (Drive/M365 connector) and ChatGPT (Drive/SharePoint connector); each tool's project instruction just says "read folder X first".
- Sharing ACL on the folder is the single permission model; connectors inherit it per user. Use group-based sharing so access changes in one place.
- Optionally mirror a Git/Markdown repo (read-only for non-technical users) into the folder; the repo hosts SKILL.md/AGENTS.md for coding agents.

### Inferences
- What breaks: (a) Claude's Drive connector is private-project only; (b) NotebookLM and some Drive-linked knowledge cannot be shared through Gems; (c) ChatGPT project files are capped (40) and shared-project memory/file-library behaviour reported to differ; (d) Gems, ChatGPT and Claude each index separately, so freshness varies (sync vs live); (e) tools may return different answers for different users because of permission inheritance; (f) Notion/Confluence connector support differs per vendor and plan.
- Direct, live connectors beat uploaded copies because upload copies go stale and are not permission-aware.

### Gaps
- No official source confirming Notion/Confluence connectors for ChatGPT or Claude; not researched for Copilot beyond generic Copilot connectors.
- Admin-level details for Gemini connectors to Drive in Gemini Enterprise vs Workspace Gemini not fully verified.
- Git repo as knowledge source: only the Claude GitHub connector mention found.

## 5. Identity federation and shadow AI

### Takeaway
SSO plus domain verification gives a single login and kills the personal-account path on the corporate domain, but does not stop employees using a personal Gmail account on a consumer AI; that needs network/browser-level discovery or controls.

### Cited Findings
- ChatGPT: SAML SSO per workspace; "Enforce SSO" blocks password and social login for verified-domain users; OpenAI advises against automatic account creation when using SCIM (official, via search snippet) — [OpenAI SSO overview](https://help.openai.com/en/articles/10468051-sso-overview)
- Claude with Entra: domain verification, SSO, "Require SSO", "Restrict organization creation" to prevent personal Claude accounts on the verified domain; SCIM on Enterprise only (Entra P1/P2); Team uses group assignment and JIT (secondary how-to, not Anthropic docs) — [T-Minus 365 guide](https://tminus365.com/how-to-set-up-claude-sso-with-microsoft-entra-id-10-minute-guide/)
- Domain capture only catches accounts created with company email, not personal gmail.com logins (practitioner blog) — [LastPass](https://blog.lastpass.com/posts/shadow-ai-is-an-identity-problem); a Microsoft Q&A report says users choosing "Continue with Google" on chatgpt.com can bypass Conditional Access (user report, unverified) — [Microsoft Q&A](https://learn.microsoft.com/en-us/answers/questions/5793514/how-to-prevent-users-from-logging-into-personal-ch)
- Microsoft Entra Global Secure Access has a network-based "shadow AI discovery" feature identifying traffic to AI services (official) — [Microsoft Learn](https://learn.microsoft.com/en-sg/Entra/global-secure-access/concept-shadow-ai-discovery)

### Inferences
- Pick one IdP (Google Workspace or Entra) as the source; enforce SAML/OIDC on every paid AI workspace, verify the domain, and disable personal-account creation where the vendor supports it. SSO reduces shadow AI because unmanaged signups on the corporate email are blocked and admins can see/offboard users; residual risk is personal accounts and unmanaged browsers.
- Connector permission inheritance is only as good as the IdP groups behind it, so identity federation is also what makes the shared-folder pattern safe.

### Gaps
- Google Workspace-as-IdP setup for Claude/ChatGPT and Gemini-specific enforcement were not found.
- Anthropic's own SSO documentation not fetched.

## 6. Open agent/interoperability standards beyond MCP

### Takeaway
MCP, Agent Skills and AGENTS.md now live under the Linux Foundation's Agentic AI Foundation; A2A reached v1.0 and is reportedly joining AAIF. Real adoption: MCP and Skills are widely used by end tools; A2A is enterprise/cloud-platform centered; Apps SDK is ChatGPT-centric but built on MCP.

### Cited Findings
- A2A: launched by Linux Foundation June 2025 (AWS, Cisco, Google, Microsoft, Salesforce, SAP, ServiceNow); v1.0 first stable spec announced 2026-04-09 with signed Agent Cards, multi-tenancy, migration path; >150 supporting organizations (from >50), >22,000 GitHub stars; Microsoft integrated into Azure AI Foundry and Copilot Studio, AWS via Bedrock AgentCore Runtime; five SDK languages (Python, JS, Java, Go, .NET); "active production deployments" but none named (official LF release) — [Linux Foundation](https://www.linuxfoundation.org/press/a2a-protocol-surpasses-150-organizations-lands-in-major-cloud-platforms-and-sees-enterprise-production-use-in-first-year)
- A2A to AAIF: Axios (2026-08-17) reports A2A getting a new home in AAIF; Enterprise DNA says the transfer happened 2026-08-20 and AAIF membership exceeds 250 (secondary; dates conflict; Axios reads as announced plan) — [Axios](https://axios.com/2026/08/17/a2a-agentic-ai-foundation-open-ai-standards), [Enterprise DNA](https://enterprisedna.co/resources/news/google-a2a-aaif-agent-protocol-open-standard-august-2026)
- Copilot Studio A2A: "public preview" per Microsoft FAQ vs "announced, rolling out" per conference deck; MCP GA — [Copilot Studio FAQ](https://adoption.microsoft.com/files/copilot-studio/Microsoft-Copilot-Studio_FAQ.pdf)
- OpenAI Apps SDK: introduced Oct 2025 (preview) built on MCP; developer submissions and in-ChatGPT directory opened 2025-12-17; Apps SDK changelog lists MCP Apps compatibility (Feb 2026), host style variables (May 2026), distribution of approved integrations as Codex plugins (Mar 2026), per-app preferences and admin defaults for Business/Enterprise (Jun 2026) (official changelog/launch posts via search summary) — [OpenAI Apps SDK changelog](https://developers.openai.com/apps-sdk/changelog), [OpenAI](https://openai.com/index/introducing-apps-in-chatgpt/). No 2026 app counts found. No evidence of an independent standards body for "MCP Apps".
- AAIF: co-founded by Anthropic, Block and OpenAI (Dec 2025); hosts MCP (donated by Anthropic), AGENTS.md, and now Agent Skills (official) — [Anthropic](https://www.anthropic.com/news/donating-agent-skills-to-the-agentic-ai-foundation)
- OpenAPI tools: not specifically researched in this pass.

### Inferences
- For a non-technical team, none of these are user-facing; they matter because tools can share one MCP server and one Skills folder. A2A is relevant mostly to Copilot Studio/Foundry/Google agent builders, not to chat-app users.
- "Vendor says X million installs/60,000 projects" figures are self-reported.

### Gaps
- OpenAPI-based tool definitions (GPT Actions, Copilot API plugins) adoption not researched.
- A2A support in Claude and ChatGPT not found; A2A real-world usage evidence thin (no named production adopters).
- Verify AAIF governance of A2A on LF/AAIF primary page.

## Key question A: Realistic low-effort way for a non-technical user and a power user to work on the same project today (and what breaks)

### Takeaway
Use a shared Drive/SharePoint folder as the project's single source of truth, with SSO and group permissions. The non-technical user works in the workspace's own AI (or whatever the company standardises on); the power user connects Claude/ChatGPT to the same folder via official connectors. Chats and memory do not sync; only files and instructions do.

### Cited Findings
- See section 4 for connector facts: Drive/SharePoint connectors in ChatGPT, Claude (M365 Team/Enterprise only; Drive connector private-project only) and Gemini/Copilot honour user permissions.
- ChatGPT and Claude project sharing are within their own vendor tenancy only (section 3).

### Inferences
- Minimal recipe: (1) shared folder with `context.md` + `instructions.md` + source docs; (2) each person's AI project instruction points to it; (3) conclusions/decisions written back to `decisions.md` by a human; (4) skills/AGENTS.md live in Git for power users only.
- What breaks: no shared chat history across vendors; memory differs per tool; Claude Drive connector not available in shared projects; indexing delays; different answers per permission; ChatGPT project file cap; import tools lossy. Humans must paste outcomes back into the folder.

### Gaps
- No empirical test of this recipe in the research; it is a design inference.

## Key question B: Which formats are stable enough to build a one-click "move my project to/from Claude/ChatGPT" feature on

### Takeaway
Stable enough: Markdown/plain text instructions, uploaded source files, SKILL.md folders (AAIF-governed), MCP server configs, and ChatGPT-style `conversations.json` for read-only history import (LibreChat/Open WebUI already do). Not stable: any project/GPT/Gem/agent object, memory, and Claude's export file layout.

### Cited Findings
- See sections 1-3: LibreChat and Open WebUI parse ChatGPT `mapping` trees; Agent Skills is an AAIF-governed spec; Agent Plugins `plugin.json` is new (Aug 2026) and called thin; vendors expose no project API in the sources found.

### Inferences
- A "move" feature should be a wizard that (a) exports user-owned Markdown (instructions, memory summary), (b) re-uploads files or connects the shared folder, (c) installs SKILL.md folders, (d) optionally imports chat history into a self-hosted app. Direct vendor-to-vendor project transfer has no official API in anything found.
- Treat vendor UIs (memory import prompts, Settings paths) as unstable: they moved names between articles (e.g., Settings > Memory vs Your Claude; Data Controls vs Data & Privacy).

### Gaps
- No evidence on public APIs for Claude Projects or ChatGPT Projects CRUD; not searched.

## Key question C: Where vendors limit portability; legal rights

### Takeaway
Portability is limited by plan (Business/Enterprise owner-only export; Gemini import consumer-only and blocked in EEA/UK/CH; Claude personal export cannot be re-imported; Claude memory import filters to work content), by missing objects (no project/memory in standard exports), and by short link expiries. GDPR Art. 20 and the EU Data Act help but are narrower than people expect.

### Cited Findings
- Limits listed above: ChatGPT self-service export unavailable on Business/Enterprise/Healthcare; 24 h link expiry for ChatGPT and Claude; Claude personal-account migration unsupported; Gemini import excludes EEA/UK/CH and Workspace accounts; imported Gemini chats may train Google models (official, sections 1-2). Gemini import being unavailable in the EEA means the import right exists commercially only elsewhere.
- GDPR Art. 20 per WP29/EDPB guidelines WP242 rev.01: covers data "provided by" the data subject, interpreted broadly to include observed data from use of a service; delivery in structured, commonly used, machine-readable format; critics (and the Commission per IAPP) found the observed-data reading too broad (official guidelines + secondary) — [EDPB WP242](https://www.edpb.europa.eu/documents/guideline/guidelines-on-the-right-to-data-portability-under-regulation-2016679-wp242_es), [IAPP](https://iapp.org/news/a/european-commission-experts-uneasy-over-wp29-data-portability-interpretation-1). Inferred/derived data exclusion rests on a secondary blog only; not verified in the guideline text.
- EU Data Act cloud switching (Chapter VI, applying since 2025-09-12): switching barriers must be removed; exportable structured machine-readable data with functional equivalence; switching/data-extraction charges only at cost until 2027-01-12 then generally banned; commentators read it as covering SaaS; the boundary for customer data vs vendor metadata/models/logs is contested; business customers cannot sue directly, enforcement by national authorities (secondary law-firm summaries) — [Greenberg Traurig](https://gtlaw.com/en/insights/2025/9/cloud-switching-under-the-eu-data-act), [DLA Piper](https://www.dlapiper.com/en/insights/publications/law-in-tech/2026/cloud-exit-under-the-eu-data-act), [Taylor Wessing](https://www.taylorwessing.com/de/global-data-hub/2025/eu-data-act---understanding-the-issues/gdh---aeu-data-act-cloud-switching-provisions)
- Microsoft's DSR guidance treats portability as a machine-readable copy (official) — section 1.

### Inferences
- Art. 20 applies to individuals' personal data (not the company's own project knowledge) and only where processing is by consent or contract and automated; it does not oblige vendors to produce importable "projects" or memories. For a business account, the employer is controller; employees' rights run via the employer. Direct vendor-to-vendor transmission "where technically feasible" is not something any of the vendors offer for chats in the sources found.
- Data Act is the stronger lever for a company switching AI SaaS vendors, but applicability to AI chat products and the scope of exportable "exportable data" are untested.
- Legal conclusions here are not legal advice and need counsel confirmation.

### Gaps
- GDPR Art. 20 primary text and the guideline paragraph on inferred data were not read directly; no regulator or court decision on AI chatbot portability found.
- Whether Data Act switching covers OpenAI/Anthropic/Google consumer vs business AI products is not established.
- Plan-limit specifics for Claude/ChatGPT project and file quotas not fully verified.
