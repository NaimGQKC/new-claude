# MVP: open-source AI workspace (chat + auto model routing)

```
Browser -> LibreChat -> LiteLLM (auto router, costs) -> EU-hosted open models
```

The user never picks a model. Two choices only: **Asistente** (the software picks) and **Pensar más** (always the strongest model).

## Run it
1. `cp .env.example .env` and fill in the secrets and your EU host's URL and key.
2. Edit the model IDs in `litellm/config.yaml` to the names your host uses.
3. `docker compose up -d`, then open http://localhost:3080.

## Not built yet (next steps)
- Deep research service (planner, cheap page readers, writer).
- Per-reply cost display for the user (LiteLLM already returns the cost in the `x-litellm-response-cost` header).
- File export (PDF/Excel/Word/PPT) and memory.

## Status
Config files are written from the LibreChat and LiteLLM docs. They are not yet tested against a live provider.
