# Build-your-own Claude-style workspace (frameworks, SDKs, gateways) and open-source browser agents, as of Nov 2026

Method note: stars/licenses were read from each GitHub repo page via WebFetch on 2026-11-18 (the GitHub REST API was blocked in this session). Star counts are approximate snapshots. The GitHub "Releases" sections came back empty in the fetched text, so I could NOT verify latest release versions or dates for any repo; that is a gap throughout. Page-summarizer output can mis-state licenses; where a page did not name a license I say so.

## 1. Frontend / UI kits for a chat workspace

### Takeaway
The live, healthy options are Vercel AI SDK (+ shadcn-hosted AI Elements), assistant-ui (MIT) and CopilotKit (MIT). Two popular reference UIs are now archived (LangChain Agent Chat UI, Open Canvas) and Chainlit's repo shows as archived, so none of those should be a foundation. AI Elements is mid-migration into shadcn/ui, so new work should use the shadcn version. No kit ships a complete "Claude.ai-style" artifacts panel plus branching plus cost bar out of the box; that glue is yours.

### Cited Findings
- Vercel AI SDK: ~28.1k stars; README shows `ToolLoopAgent`, `createAgentUIStreamResponse` (streams an agent to Next.js) and the `useChat` hook in `@ai-sdk/react`. The page did not name the license or list OpenAI-compatible/Chinese providers. — [vercel/ai](https://github.com/vercel/ai)
- AI Elements (Vercel): ~2.5k stars, built on shadcn/ui, needs Next.js + AI SDK + Tailwind CSS-variables mode. The repo warns it "is moving to shadcn/ui and will be deprecated at the end of November 2026"; new projects should use the shadcn/ui version. — [vercel/ai-elements](https://github.com/vercel/ai-elements)
- Confirmed by search: the shadcn/ui version is copied into your project (no package), has migration prompts for coding agents, and renames some components (e.g. agent.tsx becomes Subagent, commit.tsx becomes Trace). InfoQ says existing users need not rewrite anything. — [shadcn AI Elements changelog](https://ui.shadcn.com/docs/changelog/2026-10-ai-elements), [shadcn AI Elements docs](https://ui.shadcn.com/docs/ai-elements), [InfoQ](https://infoq.com/news/2026/08/shadcn-conversational-primitives)
- I could not confirm from the repo page that AI Elements has dedicated Artifact/Branch/Tool components (the README text only named conversation, message, code block, reasoning). — [vercel/ai-elements](https://github.com/vercel/ai-elements)
- assistant-ui: ~13.3k stars, MIT. Has branch-picker primitive, tool-call UI (`makeAssistantToolUI`), inline human approvals, attachments. Runtimes for Vercel AI SDK, LangGraph/LangChain, AG-UI, A2A, Google ADK and OpenCode, or custom backends. Optional paid "Assistant Cloud" for thread persistence. — [assistant-ui/assistant-ui](https://github.com/assistant-ui/assistant-ui)
- CopilotKit: ~38.8k stars, MIT. Built on the AG-UI protocol; generative UI (controlled, declarative, open-ended), shared agent/UI state, human-in-the-loop. Supports LangGraph, Deep Agents, CrewAI, Mastra, Google ADK, PydanticAI, Microsoft Agent Framework, AWS Strands, Claude Agent SDK, LlamaIndex, Agno, AG2. React/Next.js GA; Angular, Vue, React Native also listed. — [CopilotKit/CopilotKit](https://github.com/CopilotKit/CopilotKit)
- LangChain Agent Chat UI: ~3.3k stars, MIT, ARCHIVED on Nov 3 2026 (read-only). Requires a LangGraph server; has an artifacts side panel via `thread.meta.artifact`; README warns the passthrough API does not authenticate callers. — [langchain-ai/agent-chat-ui](https://github.com/langchain-ai/agent-chat-ui)
- Open Canvas (LangChain): ~5.5k stars, MIT, ARCHIVED Feb 26 2026. Had versioned code/markdown artifacts, a memory/reflection agent, quick actions. Useful only as a design reference. — [langchain-ai/open-canvas](https://github.com/langchain-ai/open-canvas)
- Chainlit: ~12.5k stars, Apache-2.0. Original team stepped back May 1 2025 (community maintained); the fetched page also says the repo was archived Oct 15 2026, which conflicts with "community maintained" and should be re-checked. — [Chainlit/chainlit](https://github.com/Chainlit/chainlit)

### Inferences
- A pragmatic stack is Next.js + AI SDK `useChat` (or assistant-ui) + shadcn-hosted AI Elements for rendering, with your own artifact panel (iframe sandbox) and cost bar. assistant-ui is the stronger fit if you want branching and a pluggable backend; CopilotKit if you want an agent-protocol (AG-UI) boundary between a Python agent backend and the React UI.
- Because AI Elements is being folded into shadcn/ui, pinning to the old `ai-elements` package would be a dead end; start on the shadcn version.
- Choosing a framework whose UI layer is not coupled to one agent framework (assistant-ui, CopilotKit via AG-UI) lets you swap the agent harness later.

### Gaps
- No verified release dates/versions for any of these (Releases section empty in fetched text).
- Did not verify AI SDK license or its list of OpenAI-compatible providers (DeepSeek/Qwen/Moonshot/Zhipu) from primary docs.
- Whether assistant-ui/AI Elements provide Claude-style artifact side panels natively was not confirmed.

## 2. Agent frameworks / SDKs / harnesses (Chinese models, subagents, compaction, MCP, sandboxing)

### Takeaway
For model-agnostic routing the best-supported options are OpenAI Agents SDK (Chat Completions/LiteLLM adapters), Pydantic AI, Mastra, LangGraph/Deep Agents, smolagents and opencode. Claude Agent SDK is attractive (hooks, subagents, MCP, sessions, Claude Code's context management) but Anthropic explicitly says it does not support routing Claude Code to non-Claude models through any gateway, so using it with DeepSeek/Qwen/Kimi is technically possible but unsupported.

### Cited Findings
- Claude Agent SDK: Python repo ~8.6k stars, MIT per repo link, but docs say use is governed by Anthropic's Commercial Terms. Capabilities: built-in tools, hooks, subagents, MCP, permissions, sessions, skills/plugins; "the same tools, agent loop, and context management that power Claude Code". — [claude-agent-sdk-python](https://github.com/anthropics/claude-agent-sdk-python), [Agent SDK overview](https://code.claude.com/docs/en/agent-sdk/overview)
- Agent SDK terms: third parties may not offer claude.ai login or rate limits for products built on the SDK without approval (use API keys); branding rules forbid "Claude Code" naming/ASCII art in your product. — [Agent SDK overview](https://code.claude.com/docs/en/agent-sdk/overview)
- Gateway/base URL: Claude Code docs say any gateway exposing a supported API format works, but "Anthropic doesn't endorse, maintain, or audit third-party gateway products, and doesn't support routing Claude Code to non-Claude models through any gateway." — [Other LLM gateways](https://code.claude.com/docs/en/llm-gateway)
- LiteLLM documents using the Agent SDK/Claude Code with any provider through its `/v1/messages` endpoint with `ANTHROPIC_BASE_URL` pointing at the proxy; a closed Feb 2026 issue reported the SDK rejecting non-`sk-ant-` LiteLLM keys (status of fix not fully verified); third-party gateway vendors note Claude-specific server tools may not work with other models. — [LiteLLM Agent SDK tutorial](https://docs.litellm.ai/docs/tutorials/claude_agent_sdk), [LiteLLM non-Anthropic models](https://docs.litellm.ai/docs/tutorials/claude_non_anthropic_models), [issue (JP)](https://claudeissues.com/issue/22760-claude-agent-sdk-litellm-anthropic-api); search summary sourced from [Maxim gateway article](https://www.getmaxim.ai/articles/best-ai-gateways-for-the-claude-agent-sdk-in-2026/)
- Claude Code Router (musistudio): ~38.2k stars, MIT; local gateway at 127.0.0.1:3456 for Claude Code/Codex/Kimi CLI with routing rules, retries, ordered fallbacks, credential pools, request logs and cost estimates; providers include OpenAI, Anthropic, Gemini, OpenRouter, DeepSeek, SiliconFlow, Moonshot, Kimi Code, Mistral, Z.AI, Bailian. — [claude-code-router](https://github.com/musistudio/claude-code-router)
- OpenAI Agents SDK: non-OpenAI models via `AsyncOpenAI(base_url=...)` + `OpenAIChatCompletionsModel`, per-agent or per-run `ModelProvider`, plus beta `any-llm` and `LiteLLM` adapters. Caveats: many providers lack the Responses API; Responses-only features (e.g. tool search, `previous_response_id`) are rejected or silently dropped on Chat Completions; some providers lack JSON-schema structured outputs; disable tracing (or set a trace key) or you get 401s. — [OpenAI Agents SDK models](https://openai.github.io/openai-agents-python/models/)
- LangGraph: ~45.1k stars, MIT; durable execution, human-in-the-loop, short/long-term memory; "Deep Agents" is a higher-level package on LangGraph for planning, subagents, filesystem. — [langgraph](https://github.com/langchain-ai/langgraph)
- Mastra (TypeScript): ~29.6k stars; Apache-2.0 core with `ee/` directories under a Mastra Enterprise License (production use needs a license); agents, graph workflows with suspend/resume, "Observational Memory", MCP server authoring, model router "40+ providers". — [mastra-ai/mastra](https://github.com/mastra-ai/mastra)
- Pydantic AI: ~21.3k stars, MIT; MCP, 9 durable-execution engines (Temporal, DBOS, Prefect, Restate...), AG-UI and Vercel AI event streams, "context management"/"compaction" listed under Pydantic AI Harness. DeepSeek/Moonshot not named on the page (provider list says "dozens more"). — [pydantic/pydantic-ai](https://github.com/pydantic/pydantic-ai)
- Agno: ~43.2k stars, Apache-2.0; AgentOS runtime with auth/RBAC, approvals, scheduling, durable execution, memory, teams, MCP, UI at os.agno.com. — [agno-agi/agno](https://github.com/agno-agi/agno)
- smolagents (Hugging Face): ~30.4k stars, Apache-2.0; CodeAgent writes actions as Python; sandboxes via E2B, Blaxel, Modal, Docker (local executor "must not be used as a security boundary"); LiteLLM "100+ LLMs", OpenAI-compatible endpoints, MCP tools. — [huggingface/smolagents](https://github.com/huggingface/smolagents)
- OpenHands: ~93.8k stars, MIT link; Python SDK + Agent Server in `OpenHands/software-agent-sdk`; Docker sandbox options (none / single / per-conversation container); "use with any LLM"; can host Claude Code, Codex, Gemini CLI, OpenCode via ACP. Condenser/compaction not confirmed from page. — [OpenHands/OpenHands](https://github.com/OpenHands/OpenHands)
- opencode: ~227.8k stars, MIT; built-in `build` and `plan` agents and a `general` subagent. Provider list/SDK/compaction not confirmed on the page fetched. — [anomalyco/opencode](https://github.com/anomalyco/opencode)
- Goose: ~56.8k stars, Apache-2.0, under the Linux Foundation's Agentic AI Foundation; 15+ providers, 70+ MCP extensions; subagents/context management not described on the page. — [aaif-goose/goose](https://github.com/block/goose)
- Kimi CLI (MoonshotAI): ~11.4k stars, Apache-2.0, ARCHIVED and no longer maintained; README points to "Kimi Code CLI" (github.com/MoonshotAI/kimi-code); supports ACP and MCP. — [MoonshotAI/kimi-cli](https://github.com/MoonshotAI/kimi-cli)
- Not researched: CrewAI, Google ADK (only named as supported by CopilotKit/assistant-ui), Zhipu/GLM-specific handling in any framework.

### Inferences
- "System-controlled per-task routing" is easiest if every framework talks to ONE OpenAI-compatible (or Anthropic-compatible) gateway (LiteLLM/CCR) so the routing policy lives outside the agent framework. Then the harness choice matters less.
- Claude Agent SDK is best when the main model is Claude; mixing in cheap Chinese models via a gateway works in practice but is explicitly unsupported and may break Claude-specific tools (inference from the Anthropic doc plus vendor notes). For a product to SMBs, the Commercial Terms and no-claude.ai-login rule apply.
- For a provider-agnostic harness with compaction and subagents already built, opencode (MIT), Pydantic AI, LangGraph + Deep Agents and OpenAI Agents SDK are the cleaner candidates; sandboxed code execution is best delegated to a separate sandbox (E2B/Docker/OpenHands runtime) rather than built into the framework.

### Gaps
- No primary-source benchmark of how well each framework handles DeepSeek/Qwen/Kimi/GLM tool-calling; not found.
- Compaction behavior was not verified for opencode, Goose, OpenHands, Mastra from primary docs.
- Release dates/versions unverified; CrewAI and Google ADK not assessed.

## 3. Gateways / observability with cost tracking

### Takeaway
LiteLLM (gateway, spend tracking, routing) plus Langfuse (tracing, cost dashboards, self-host) is the obvious open-source pairing; both are widely adopted. Helicone, OpenLIT, Portkey and OpenRouter were not verified in this pass.

### Cited Findings
- LiteLLM: ~63.5k stars; virtual keys, spend tracking, guardrails, load balancing, multi-tenant cost tracking per project/user; Auto Router that picks a model per prompt; providers include DeepSeek, Moonshot, Qwen variants; `/messages` (Anthropic format) supported. The page did not name the license; enterprise features are under a "LiteLLM Commercial License". — [BerriAI/litellm](https://github.com/BerriAI/litellm)
- Langfuse: ~37.6k stars; MIT except `ee` folders; part of ClickHouse since January 2026; Docker Compose, Helm/Kubernetes, Terraform self-hosting; usage/cost tracking, dashboards, metrics API; an "AI Gateway (beta)" tracks spend per user/key/model; telemetry on by default (disable with `TELEMETRY_ENABLED=false`). — [langfuse/langfuse](https://github.com/langfuse/langfuse)
- Claude Code Router also provides request logs and cost estimates (see section 2). — [claude-code-router](https://github.com/musistudio/claude-code-router)
- OpenAI Agents SDK traces export to OpenAI by default and must be disabled or redirected when using other providers. — [OpenAI Agents SDK models](https://openai.github.io/openai-agents-python/models/)

### Inferences
- Always-visible cost tracking in the UI can be driven from the gateway's per-key/per-request spend (LiteLLM) rather than computed client-side, which also covers all agent frameworks uniformly.

### Gaps
- Helicone, OpenLIT, Portkey (open-source gateway), OpenRouter: not fetched; licenses/stars/features unverified.
- LiteLLM license text and recent security/stability record not verified.

## 4. Existing "Claude-like" open-source projects that already combine these (fork-vs-build)

### Takeaway
Self-hosted all-in-one chat apps exist but have licence caveats: Open WebUI carries a branding-preservation licence and LobeHub a custom community licence, which matter if you later sell to SMBs. LibreChat (user's current option) was not re-verified here.

### Cited Findings
- Open WebUI: ~159k stars; the repo says it includes code under the "Open WebUI License, which requires preserving the Open WebUI branding". Artifacts/deep research/code interpreter were not shown on the fetched page. — [open-webui/open-webui](https://github.com/open-webui/open-webui)
- LobeHub (formerly LobeChat): ~85.8k stars; README says "LobeHub Community License" while showing an Apache-2.0 badge (unclear, check LICENSE); MCP marketplace, agent teams, resource library, Docker Compose self-hosting. Open WebUI's own comparison page says LobeHub is source-available rather than OSI open source. — [lobehub/lobehub](https://github.com/lobehub/lobehub), [Open WebUI vs LobeHub](https://docs.openwebui.com/alternatives/lobehub)
- Third-party comparisons say LibreChat has HTML/code artifacts in a side panel, Open WebUI is weaker on built-in deep research, and Onyx/Khoj are the deep-research-oriented options (blog-level sources, low reliability). — [Pinggy](https://pinggy.io/blog/best_open_source_alternatives_to_chatgpt/), [Open WebUI vs LobeHub](https://docs.openwebui.com/alternatives/lobehub)
- OpenHands and goose are agent-first and could back a chat UI via ACP/server APIs. — [OpenHands](https://github.com/OpenHands/OpenHands), [goose](https://github.com/block/goose)

### Inferences
- If the SMB product ambition is real, Open WebUI's branding clause and LobeHub's licence are reasons to prefer an MIT/Apache base (assistant-ui, CopilotKit, opencode, LiteLLM, Langfuse) or LibreChat (licence unverified here).

### Gaps
- LibreChat license/features, Onyx, Khoj not fetched in this pass.
- Per-feature comparison against the user's list (artifacts, deep research, per-task routing) from primary docs not done.

## 5. Effort estimate: build from components vs fork

### Takeaway
No credible published estimate was found; the figures below are my own judgement, not sourced. Roughly: forking a mature chat app gets a usable single-user v1 in about 1-3 weeks of one developer, but the custom routing/cost/context features fight the app's architecture; assembling components is about 5-9 weeks for a comparable v1 with AI coding help.

### Cited Findings
- Nothing citable on person-weeks was found.

### Inferences (unsourced, labelled as estimates)
- Component build for one developer using Claude Code-style help: chat UI + streaming + persistence (1-1.5 wk); gateway (LiteLLM) with per-task routing rules and cost bar (1 wk); agent harness with tools, MCP, subagents and context compaction (1.5-2.5 wk); artifacts panel with sandboxed iframe and file generation (1-1.5 wk); deep research workflow (1-2 wk); auth/hardening (0.5-1 wk). Total approx 6-9 weeks to a polished v1; 3-4 weeks for a rough one.
- Fork: 1-3 weeks to deploy and configure, then ongoing merge cost for each custom feature; the build path wins when routing, cost UX and context management are core differentiators or when licence freedom for an SMB product matters.
- The browser agent should be a separate service/extension later, not coupled to the chat UI.

### Gaps
- No real-world case studies of time-to-v1 for either path.

## 6. Browser agents (Nov 2026): licence, stars, models, reliability

### Takeaway
Open-source choices: browser-use (MIT, ~121k stars), Stagehand (MIT, ~26k), Playwright MCP (Apache-2.0, ~40k, has an extension mode that reuses your logged-in Chrome), Skyvern (AGPL-3.0, ~23k), Nanobrowser (Apache-2.0, ~14k Chrome extension). Reliability claims are mostly vendor self-reports; independent evaluation (Online-Mind2Web) shows far lower success than WebVoyager claims. Per-task cost data was not found.

### Cited Findings
- browser-use: ~121.4k stars, MIT; default model on its own gateway `bu-4.0` (mini/pro variants); built-in ChatOpenAI/ChatAnthropic/ChatGoogle; any Pydantic AI model string; OpenAI-compatible `base_url` (e.g. Ollama); cloud browsers $0.06/browser-hour; repo page shows own Browser Use Benchmark v2 chart (numbers not in text). — [browser-use/browser-use](https://github.com/browser-use/browser-use)
- browser-use claims 89.1% on WebVoyager (586 tasks, GPT-4o) after modifying the harness, removing 55 "impossible" tasks, shifting dates, and manually reviewing failures; steps per site averaged 8.5-36.2; no cost reported. Notte's open evaluation measured 77.3% self-reported and 60.2% LLM-verified for browser-use v0.1.40 with GPT-4o. — [Browser Use SOTA report](https://browser-use.com/posts/sota-technical-report), [Notte evals via search](https://dev.to/andreanotte/opensource-web-agent-outclasses-browser-use-ne1)
- Browser Use blog also claims 97% on Online-Mind2Web and says Browser Use Cloud scores 78%, 16 points ahead of the best open-source model (company claims, unverified). — [Browser Use blog](https://browser-use.com/posts)
- Online-Mind2Web (300 tasks, 136 live sites): authors found most frontier agents complete only ~30% under human evaluation versus much higher self-reported WebVoyager scores; proposes WebJudge (~85% agreement with humans). A third-party summary gives 30-61% for frontier agents. — [arXiv 2504.01382](https://arxiv.org/abs/2504.01382), [AlphaXiv](https://alphaxiv.org/benchmarks/uc-berkeley/online-mind2web)
- Stagehand: ~26.1k stars, MIT; TypeScript, Python, Go; `act`, `observe`, `extract`, caching (`cache: true` on Browserbase), accessibility-tree trimming to cut tokens; example uses `openai/gpt-5.4-mini`; Browserbase model gateway. No price figures. — [browserbase/stagehand](https://github.com/browserbase/stagehand)
- Playwright MCP: ~39.9k stars, Apache-2.0; default uses the accessibility tree (no vision required), optional `--caps=vision` coordinate tools; `--extension` mode connects to a running Chrome/Edge with the Playwright Extension and reuses logged-in sessions; states it is "not a security boundary"; `browser_run_code_unsafe` is "RCE-equivalent". — [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp)
- Skyvern: ~23.4k stars, AGPL-3.0 (anti-bot measures only in managed cloud); supports OpenAI GPT-5.x, Claude 4.x, Gemini 3.x, Azure, Bedrock, Ollama/OpenRouter/OpenAI-compatible via LiteLLM; reports 64.4% on WebBench; a report URL mentions 85.8% WebVoyager (not stated on page); self-host via pip or Docker Compose; telemetry on by default. — [Skyvern-AI/skyvern](https://github.com/Skyvern-AI/skyvern)
- Nanobrowser: ~14.3k stars, Apache-2.0 Chrome extension; providers include Anthropic, OpenAI, Gemini, Bedrock, OpenRouter, Grok, DeepSeek, Mistral, any OpenAI-compatible endpoint, Ollama/LM Studio (models must support tool calling; recommends Qwen3.8 27B with 16k+ context); vision optional. — [nanobrowser/nanobrowser](https://github.com/nanobrowser/nanobrowser)
- Claude in Chrome (Anthropic's own, closed) is the reference product; it generally launched with autonomous browser actions per one news summary. — [aiunderstanding.org](https://aiunderstanding.org/news/anthropic-makes-claude-in-chrome-generally-available-with-autonomous-browser-actio)

### Inferences
- Text/accessibility-tree agents (Playwright MCP default, Nanobrowser) can work with cheap non-vision Chinese models that have good tool calling; vision-dependent flows (Skyvern, screenshot modes) need a VL-capable model.
- Expect real-world success well below vendor benchmark numbers (Online-Mind2Web evidence), so design for supervised, short, reversible tasks.
- Playwright MCP extension mode or Nanobrowser are the closest open equivalents to "Claude in Chrome" for acting inside your own logged-in sessions; Skyvern's AGPL matters for an SMB product.

### Gaps
- Cost per task: no reliable primary figure found for any agent.
- Open-source Qwen-VL/UI-TARS/GLM-V computer-use models: search returned nothing; not assessed.
- Latest release dates, current Online-Mind2Web leaderboard rows and Skyvern's 85.8% WebVoyager claim unverified.

## 7. Gmail / LinkedIn / Instagram: APIs vs browser automation, ToS, ban risk, injection, HITL

### Takeaway
Gmail has an official path (OAuth API; a Google-run Gmail MCP server in developer preview, reportedly draft-only). LinkedIn forbids bots, automation and browser extensions in its User Agreement, so browser-agent automation of LinkedIn risks restriction. Instagram's official API covers only professional accounts and Meta requires written permission for automated data collection, so browser automation of Instagram is contrary to its terms. Prompt injection against browser agents is a demonstrated, unsolved problem.

### Cited Findings
- LinkedIn User Agreement 8.2 prohibits using "software, devices, scripts, robots or any other means" (naming crawlers, browser plugins and add-ons) to harvest data, and prohibits "bots or other unauthorized automated methods to access the Services". — [LinkedIn User Agreement](https://www.linkedin.com/legal/user-agreement)
- LinkedIn help pages say it does not permit third-party tools that scrape or automate activity and that accounts can be restricted; see [Prohibited software and extensions](https://www.linkedin.com/help/linkedin/answer/a1341387) and [Automated activity on LinkedIn](https://www.linkedin.com/help/linkedin/answer/90586) (seen only as search listings, text not fetched). Restriction-rate statistics in vendor blogs are unverifiable and LinkedIn publishes no thresholds. — [search results summary](https://www.datablist.com/how-to/linkedin-account-restriction)
- Meta Automated Data Collection Terms (effective Oct 7 2024): "You will not engage in Automated Data Collection without first obtaining Meta's express written permission"; accepting the terms is not permission. The page's product definition references Facebook; Instagram coverage appears only via links, so applicability to Instagram is indirect from that page. — [Meta ADC terms](https://www.facebook.com/legal/automated_data_collection_terms)
- Instagram's own Terms of Use text could not be fetched (page returned only a header). Secondary sources quote it as forbidding collecting data by automated means without prior permission; wording unverified. — [search results](https://help.instagram.com/740480200552298)
- Instagram Platform: messaging and publishing APIs are for professional (business/creator) accounts only; personal accounts cannot use them; 30-day limit on Requests folder messages; Advanced Access/App Review for apps serving accounts you do not own. — [Instagram Platform overview](https://developers.facebook.com/documentation/instagram-platform/overview), [Messaging API](https://developers.facebook.com/docs/instagram-platform/instagram-api-with-instagram-login/messaging-api)
- Gmail: Google reportedly runs a remote Gmail MCP (gmailmcp.googleapis.com) in Developer Preview with `gmail.readonly` and `gmail.compose` scopes and create_draft but no send tool (sources conflict on send; launch date also conflicts April vs "preview as of October 2026"). A community server adds an immediate `send_email` tool. — [DragApp Gmail MCP](https://www.dragapp.com/blog/gmail-mcp-server/), [Google Workspace updates blog](https://workspaceupdates.googleblog.com/2026/05/agent-tools-and-security-updates-for-workspace-developers.html)
- Gmail restricted scopes trigger OAuth verification and, for apps handling data on servers, a CASA security assessment renewed yearly; third-party vendor docs say personal-use (<100 users) or "Testing"-status apps are exempt, but Google's own page in the results did not show this. — [Nylas guide](https://developer.nylas.com/docs/dev-guide/provider-guides/google/google-verification-security-assessment-guide), [Google restricted scope verification](https://developers.google.com/identity/protocols/oauth2/production-readiness/restricted-scope-verification)
- Anthropic Claude for Chrome pilot (Aug 2025): 123 test cases/29 scenarios; attack success 23.6% without mitigations, 11.2% with; browser-specific challenge set 35.7% to 0%; later Nov 2025 data (Best-of-N adaptive attacker) e.g. Sonnet 4: 13.8% model-only to 2.0% with improved safeguards; Anthropic says even 1% is meaningful risk; Simon Willison called 11.2% "catastrophic". — [Anthropic: Claude for Chrome](https://www.anthropic.com/news/claude-for-chrome), [Anthropic: prompt injection defenses](https://www.anthropic.com/research/prompt-injection-defenses), [Simon Willison](https://simonwillison.net/2025/Aug/26/piloting-claude-for-chrome/)
- Brave showed indirect prompt injection in Perplexity Comet: hidden Reddit spoiler text led the agent to read the user's email, trigger an OTP, read it from Gmail and post both to Reddit; a second post showed "unseeable" injections hidden as faint text in screenshots; Brave calls it a systemic issue for AI browsers. — [Brave Comet post](https://brave.com/blog/comet-prompt-injection/), [Brave unseeable injections](https://brave.com/blog/unseeable-prompt-injections/)
- Playwright MCP itself warns it is not a security boundary and that origin allow/block lists are not security controls. — [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp)

### Inferences
- Safest design: use official APIs where they exist (Gmail via OAuth/MCP with draft-only scope, human clicks send; Instagram Graph API only for your own professional account; LinkedIn has no general consumer API, so keep LinkedIn read-only/manual or use a human-in-the-loop copilot that prepares text but does not click).
- Browser agent guardrails: run in a separate Chrome profile with only the needed accounts, per-domain allowlists enforced outside the model, no autonomous send/post/connect/DM actions (explicit approval for every irreversible step), strip/flag untrusted page text, never put email content and browsing in the same context without taint tracking, rate-limit and log every action.
- For the SMB product, LinkedIn/Instagram automation would expose customers to account restrictions; that is a product-liability decision, not just a technical one.

### Gaps
- Instagram Terms of Use clause and LinkedIn help-page text not read directly (fetch returned only headers/search snippets).
- Gmail MCP details (send capability, GA status) from Google's own docs not verified.
- No independent 2026 benchmarks of prompt-injection success for open-source browser agents; not found.
- Unverified aggregator claim of 0-0.3% attack success for newer Claude models was seen and deliberately excluded.
