# MVP: open-source AI workspace (chat + auto model routing)

```
Browser -> LibreChat -> LiteLLM (auto router, costs) -> open models (OpenRouter for the MVP, EU hosts later)
```

The user never picks a model. Two choices only: **Asistente** (the software picks) and **Pensar más** (always the strongest model).

## Run it
1. `cp .env.example .env` and fill in the secrets and your OpenRouter key.
2. Model IDs are already set for OpenRouter. To change host later, edit `litellm/config.yaml`.
3. `docker compose up -d`, then open http://localhost:3080.

## Not built yet (next steps)
- Deep research service (planner, cheap page readers, writer).
- Per-reply cost display for the user (LiteLLM already returns the cost in the `x-litellm-response-cost` header).
- File export (PDF/Excel/Word/PPT) and memory.

## Status
Tested live (LiteLLM v1.110.1 in Docker + OpenRouter): the auto-router sends greetings, emails and summaries to DeepSeek Flash, long reports to GLM-5.3 and step-by-step analysis to Kimi K3.1 Pro. Cost per reply comes back in the `x-litellm-response-cost` header. LibreChat has not been run yet. Test: `python3 -I tests/route_test.py`.
