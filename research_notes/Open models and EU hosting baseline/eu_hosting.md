# Open-weight LLM hosting on European servers: providers, prices, data handling, sovereignty (as of 2026-11-18)

Notes on method:
- I fetched every page and API below on **2026-11-18**. Prices are per 1M tokens unless noted, in the currency the provider publishes. I did not convert currencies; EUR and USD are shown as given.
- "Official" means the provider's own pricing page, docs or public `/v1/models` API. "Aggregator" means OpenRouter's public API (`https://openrouter.ai/api/v1/models/<model>/endpoints`) or Artificial Analysis. Aggregator numbers are flagged **[AGG]**.
- VAT: I state VAT treatment only where the page says it. Otherwise it is listed under Gaps.
- Model names: OpenRouter's catalogue confirms that all the candidate models exist under these IDs: `deepseek/deepseek-v4.1-flash`, `deepseek/deepseek-v4-pro`, `moonshotai/kimi-k3.1-pro`, `z-ai/glm-5.3`, `z-ai/glm-5.3-flash`, `qwen/qwen3.8-27b`, `minimax/minimax-m3.1-flash`, `mistralai/mistral-large-4-0`, `mistralai/mistral-small-2603` (Small 4), `openai/gpt-oss-120b/20b`. "Qwen4" exists only as `qwen/qwen4-max`, which is served solely by Alibaba, and I found no evidence that it is open-weight. ([OpenRouter models API](https://openrouter.ai/api/v1/models))

---

## Q1. Which candidate models each EU option offers, and official per-1M-token prices (input / cached input / output); prompt caching

### Takeaway
No single EU-owned host carries every candidate model.
- **Broadest EU-owned catalogues:** T-Systems AI Foundation Services, Scaleway and OVHcloud. Between them they cover DeepSeek V4.1 Flash, GLM-5.3 / GLM-5.3-Flash, Qwen3.8-27B, gpt-oss and Mistral Small.
- **Kimi K3.1 Pro:** only two EU-owned hosts publish a price for it: Berget AI (Sweden) and Verda (Finland).
- **No EU-owned serverless host found:** DeepSeek V4 Pro and MiniMax M3.1-Flash.
- **Mistral Large 4:** only on Mistral's own platform.
- **Prompt-caching discounts** are published by Mistral (10% of input), T-Systems (15% of input), Scaleway (20% of input on two models), Berget (30% on Kimi), Verda, Nebius and Cloudflare. OVH, IONOS, STACKIT, Regolo and Infomaniak publish no cached-input price.

### Cited Findings

**Master price table (candidate models; official unless flagged)**

| Model | Provider (owner country) | Input | Cached input | Output | Currency | Source |
|---|---|---|---|---|---|---|
| DeepSeek V4.1 Flash (1017) | OVHcloud AI Endpoints (FR) | 0.27 | n/p | 1.08 | EUR | [OVH catalog (en-ie, EUR)](https://www.ovhcloud.com/en-ie/public-cloud/ai-endpoints/catalog/) |
| DeepSeek V4.1 Flash (1017) | Scaleway Generative APIs, Paris (FR) | 0.60 | 0.12 | 1.80 | EUR | [Scaleway Generative APIs](https://www.scaleway.com/en/generative-apis/) |
| DeepSeek V4.1 Flash | T-Systems AIFS, T Cloud Germany (DE) | 0.30 | 0.045 | 1.20 | EUR | [T-Systems LLM Hub models](https://docs.llmhub.t-systems.net/models/) |
| DeepSeek V4.1 Flash 1017 | Mistral La Plateforme (FR), global | 0.30 | 0.007 | 1.20 | USD (per OpenRouter; doc page has a USD/EUR toggle) | [Mistral pricing docs](https://docs.mistral.ai/inference/pricing) |
| DeepSeek V4.1 Flash 1017 | Verda Inference (preview) | 0.15 | 0.006 | 0.60 | USD | [Verda pricing](https://verda.com/pricing) |
| DeepSeek V4.1 Flash | Nebius Token Factory | 0.30 | 0.01 | 1.20 | USD **[AGG]** | [OpenRouter endpoints](https://openrouter.ai/api/v1/models/deepseek/deepseek-v4.1-flash/endpoints) |
| DeepSeek V4.1 Flash 1017 | Cloudflare Workers AI (US) | 0.300 | 0.006 | 1.200 | USD | [Cloudflare Workers AI pricing](https://developers.cloudflare.com/workers-ai/platform/pricing/) |
| DeepSeek V4.1 Flash | Regolo.ai (IT) | listed in API (`deepseek-v4.1-flash`, usage multiplier 3.0); **no price on pricing page** | – | – | EUR | [Regolo models API](https://api.regolo.ai/v1/models), [Regolo pricing](https://regolo.ai/pricing/) |
| DeepSeek V4 Pro (0813) | Cloudflare Workers AI (US) | 1.320 | 0.044 | 3.960 | USD | [Cloudflare pricing](https://developers.cloudflare.com/workers-ai/platform/pricing/) |
| DeepSeek V4 Pro (0813) | DeepInfra (US) | 1.30 | 0.10 | 2.60 | USD | [DeepInfra pricing](https://deepinfra.com/pricing) |
| DeepSeek V4 Pro | **No EU-owned host found** (not on Scaleway, OVH, T-Systems, Mistral, IONOS, STACKIT, Berget, Regolo; no Nebius endpoint on OpenRouter) | – | – | – | – | [OpenRouter endpoints](https://openrouter.ai/api/v1/models/deepseek/deepseek-v4-pro/endpoints) |
| Kimi K3.1 Pro | Berget AI (SE) | 3.00 | 0.90 | 10.00 | EUR | [Berget models API](https://api.berget.ai/v1/models) |
| Kimi K3.1 Pro | Verda Inference (preview) | 2.00 | 0.20 | 10.00 | USD | [Verda pricing](https://verda.com/pricing) |
| Kimi K3.1 Pro | Nebius Token Factory (fp4) | 2.00 | 0.20 | 10.00 | USD **[AGG]** | [OpenRouter endpoints](https://openrouter.ai/api/v1/models/moonshotai/kimi-k3.1-pro/endpoints) |
| Kimi K3.1 Pro | Together / Fireworks / DeepInfra (US) | 2.00 / 2.00 / 2.00 (DeepInfra promo 1.90) | 0.20 | 10.00 (DeepInfra promo 9.50) | USD | [Together](https://www.together.ai/pricing), [Fireworks](https://fireworks.ai/pricing), [DeepInfra](https://deepinfra.com/pricing) |
| GLM-5.3 | Scaleway, Paris | 1.80 | n/p | 5.50 | EUR | [Scaleway Generative APIs](https://www.scaleway.com/en/generative-apis/) |
| GLM-5.3 | T-Systems AIFS, Germany | 1.40 | 0.21 | 4.40 | EUR | [T-Systems models](https://docs.llmhub.t-systems.net/models/) |
| GLM-5.3 | Mistral, global / EU region | 1.40 / 1.54 | 0.14 / 0.154 | 4.40 / 4.84 | USD (EU = 1.1×) | [Mistral pricing](https://docs.mistral.ai/inference/pricing); EU figure confirmed **[AGG]** by `mistral/nvfp4/eu` on [OpenRouter](https://openrouter.ai/api/v1/models/z-ai/glm-5.3/endpoints) |
| GLM-5.3 | Nebius (fp4) | 1.40 | 0.26 | 4.40 | USD **[AGG]** | [OpenRouter](https://openrouter.ai/api/v1/models/z-ai/glm-5.3/endpoints) |
| GLM-5.3 | Cloudflare Workers AI (US) | 1.400 | 0.260 | 4.400 | USD | [Cloudflare](https://developers.cloudflare.com/workers-ai/platform/pricing/) |
| GLM-5.3 | Regolo (IT) | only **glm5.2** offered: 2.30 / – / 6.90 | – | – | EUR | [Regolo pricing](https://regolo.ai/pricing/) |
| GLM-5.3-Flash | Berget AI (SE), FP8 | 0.25 | n/p | 0.50 | EUR | [Berget models API](https://api.berget.ai/v1/models) |
| GLM-5.3-Flash | T-Systems AIFS | 0.20 | 0.03 | 0.60 | EUR | [T-Systems models](https://docs.llmhub.t-systems.net/models/) |
| GLM-5.3-Flash | Mistral, global (EU = 1.1×) | 0.15 | 0.03 | 0.50 | USD | [Mistral pricing](https://docs.mistral.ai/inference/pricing) |
| GLM-5.3-Flash | Nebius (fp4) | 0.15 | 0.03 | 0.50 | USD **[AGG]** | [OpenRouter](https://openrouter.ai/api/v1/models/z-ai/glm-5.3-flash/endpoints) |
| GLM-5.3-Flash | Cloudflare (US) | 0.150 | 0.030 | 0.500 | USD | [Cloudflare](https://developers.cloudflare.com/workers-ai/platform/pricing/) |
| Qwen3.8-27B | OVHcloud (fp8) | 0.40 | n/p | 2.70 | EUR | [OVH catalog](https://www.ovhcloud.com/en-ie/public-cloud/ai-endpoints/catalog/) |
| Qwen3.8-27B | Scaleway | 0.60 | 0.12 | 3.30 | EUR | [Scaleway](https://www.scaleway.com/en/generative-apis/) |
| Qwen3.8-27B | IONOS AI Model Hub (DE) | 0.40 | n/p | 2.70 | EUR (ES site) | [IONOS ES](https://cloud.ionos.es/managed/ai-model-hub) |
| Qwen3.8-27B | STACKIT AI Model Serving, EU01 (DE) | 0.45 | n/p | 0.65 | EUR | [STACKIT](https://stackit.com/en/products/data-ai/stackit-ai-model-serving) |
| Qwen 3.8 27B FP8 | T-Systems AIFS | 0.50 | 0.075 | 2.50 | EUR | [T-Systems models](https://docs.llmhub.t-systems.net/models/) |
| qwen3.8-27b | Regolo (IT) | 0.50 | n/p | 3.40 | EUR | [Regolo pricing](https://regolo.ai/pricing/) |
| Qwen3.8-27B-FP8 | Infomaniak (CH) | 0.40 | n/p | 3.00 | CHF | [Infomaniak AI prices](https://www.infomaniak.com/en/hosting/ai-services/prices) |
| Qwen3.8-27B | Nebius (fp4) | 0.45 | 0.10 | 3.00 | USD **[AGG]** | [OpenRouter](https://openrouter.ai/api/v1/models/qwen/qwen3.8-27b/endpoints) |
| MiniMax M3.1-Flash | Nebius (fp4) | 0.15 | 0.015 | 0.60 | USD **[AGG]** | [OpenRouter](https://openrouter.ai/api/v1/models/minimax/minimax-m3.1-flash/endpoints) |
| MiniMax M3.1-Flash | Together (US) | 0.15 | 0.015 | 0.60 | USD | [Together](https://www.together.ai/pricing) |
| MiniMax M3.1-Flash | **No EU-owned host found** (Scaleway's docs list only the older MiniMax-M2.5) | – | – | – | – | [Scaleway supported models](https://www.scaleway.com/en/docs/generative-apis/reference-content/supported-models/) |
| Mistral Large 4 | Mistral, global / EU | 0.70 / 0.77 | 0.07 / 0.077 | 2.10 / 2.31 | USD | [Mistral pricing](https://docs.mistral.ai/inference/pricing); EU price **[AGG]** [OpenRouter](https://openrouter.ai/api/v1/models/mistralai/mistral-large-4-0/endpoints) |
| Mistral Small 4 | Mistral, global / EU | 0.15 / 0.165 | 0.015 / 0.0165 | 0.60 / 0.66 | USD | [Mistral pricing](https://docs.mistral.ai/inference/pricing); [OpenRouter](https://openrouter.ai/api/v1/models/mistralai/mistral-small-2603/endpoints) |
| Mistral Small 4 | T-Systems AIFS | 0.60 | 0.09 | 1.20 | EUR | [T-Systems](https://docs.llmhub.t-systems.net/models/) |
| mistral-small-4-119b | Regolo | 0.20 | n/p | 0.70 | EUR | [Regolo](https://regolo.ai/pricing/) |
| Mistral-Small-4-119B-2603 | Infomaniak | 0.20 | n/p | 0.75 | CHF | [Infomaniak](https://www.infomaniak.com/en/hosting/ai-services/prices) |
| Mistral Small 3.2 24B | OVH 0.09/0.28 · Scaleway 0.15/0.35 · IONOS 0.10/0.30 · Berget 0.30/0.30 | – | n/p | – | EUR | [OVH](https://www.ovhcloud.com/en-ie/public-cloud/ai-endpoints/catalog/), [Scaleway](https://www.scaleway.com/en/generative-apis/), [IONOS ES](https://cloud.ionos.es/managed/ai-model-hub), [Berget API](https://api.berget.ai/v1/models) |
| gpt-oss-120b | OVH 0.08/0.40 · Scaleway 0.15/0.60 · IONOS 0.15/0.65 · STACKIT 0.45/0.65 · T-Systems 0.20/(0.03 cached)/0.65 · Regolo 0.20/0.70 | – | T-Systems 0.03 only | – | EUR | pages above; [T-Systems](https://docs.llmhub.t-systems.net/models/) |
| gpt-oss-120b | AWS Bedrock eu-west-1 | 0.15 | – | 0.60 | USD **[AGG]** | [OpenRouter](https://openrouter.ai/api/v1/models/openai/gpt-oss-120b/endpoints) |
| gpt-oss-20b | OVH 0.04/0.15 · STACKIT 0.15/0.25 · Regolo 0.10/0.20 · Bedrock eu-west-1 0.07/0.15 USD **[AGG]** | – | – | – | EUR/USD | [OVH](https://www.ovhcloud.com/en-ie/public-cloud/ai-endpoints/catalog/), [STACKIT](https://stackit.com/en/products/data-ai/stackit-ai-model-serving), [Regolo](https://regolo.ai/pricing/), [OpenRouter](https://openrouter.ai/api/v1/models/openai/gpt-oss-20b/endpoints) |

(n/p = no cached-input price published on the page.)

**Other candidate-adjacent models seen on EU hosts:**
- **Scaleway:** qwen3.5-397b-a17b €0.60/€3.60; qwen3.6-35b-a3b €0.25/€1.50; gemma-4-26b-a4b €0.25/€0.50; mistral-medium-3.5-128b €1.50/€7.50; deepseek-v4-flash-0731 €0.40 / €0.08 cached / €0.80. ([Scaleway](https://www.scaleway.com/en/generative-apis/))
- **OVH:** Qwen3.5-397B €0.60/€3.60; qwen3.6-35b-a3b €0.17/€1.15; gemma-4-26b-a4b €0.09/€0.35; nemotron3-nano-30b €0.05/€0.20. ([OVH](https://www.ovhcloud.com/en-ie/public-cloud/ai-endpoints/catalog/))
- **Infomaniak:** Kimi K2.6 (not K3.1) at CHF 0.60/3.00. ([Infomaniak](https://www.infomaniak.com/en/hosting/ai-services/prices))
- **STACKIT:** Qwen3 VL 235B €1.50/€1.75. ([STACKIT](https://stackit.com/en/products/data-ai/stackit-ai-model-serving))

**Helper models (embeddings / rerankers / OCR), official:**
- **OVHcloud:** bge-m3 €0.01/M; Qwen3-Embedding-8B €0.10/M; bge-multilingual-gemma2 €0.01 (being retired 21 Jan 2027); Qwen3Guard-Gen-8B/0.6B free (beta); whisper-large-v3-turbo €0.04601/h. ([OVH catalog](https://www.ovhcloud.com/en-ie/public-cloud/ai-endpoints/catalog/))
- **IONOS (EUR, ES site):** bge-m3 €0.02/M; Qwen3-VL-Embedding-8B €0.10/M; Qwen3-VL-Reranker-8B €0.04/M; LightOnOCR 2 €0.15 in / €0.30 out; Whisper large-v3 €0.0025/min. Embeddings bill input tokens only. ([IONOS ES](https://cloud.ionos.es/managed/ai-model-hub), [IONOS US page](https://cloud.ionos.com/managed/ai-model-hub))
- **T-Systems:** BGE-M3 €0.05/M; Qwen3 Embedding 8B €0.10/M; Jina Embeddings v2 Base DE €0.05/M; Nemotron 3.5 Embedding 8B €0.15/M; Qwen3-Reranker-4B €0.05/M; LightOnOCR-3-4B €0.20/€0.03/€0.60; PaddleOCR-VL-1.6 €0.10/€0.015/€0.40. ([T-Systems models](https://docs.llmhub.t-systems.net/models/))
- **Scaleway:** qwen3-embedding-8b €0.10/M; bge-multilingual-gemma2 €0.10/M; lightonocr-3-0.8b €2.20/M input, output free; whisper-large-v3 €0.003/audio min. ([Scaleway](https://www.scaleway.com/en/generative-apis/))
- **Berget:** BAAI/bge-reranker-v2-m3 €0.10/M; multilingual-e5-large €0.03/M; multilingual-e5-large-instruct €0.03/M. ([Berget models API](https://api.berget.ai/v1/models))
- **Infomaniak:** bge-reranker-v2-m3 CHF 0.01/M; Qwen3-Reranker-0.6B CHF 0.009/M; Qwen3-Embedding-8B CHF 0.07/M; bge-multilingual-gemma2 CHF 0.065/M; All-MiniLM-L12-v2 free. ([Infomaniak](https://www.infomaniak.com/en/hosting/ai-services/prices))
- **Regolo:** Qwen3-Embedding-8B €0.001/request; Qwen3-Reranker-4B €0.01/query; deepseek-ocr-2 €0.02/request; faster-whisper-large-v3 €0.00015/s. ([Regolo](https://regolo.ai/pricing/))
- **STACKIT:** e5-mistral-7b €0.02/M; Qwen3 VL Embedding 8B €0.08/M. ([STACKIT](https://stackit.com/en/products/data-ai/stackit-ai-model-serving))
- **Mistral:** Mistral Embed $0.10 (cached $0.01); OCR 4.1 $4 per 1,000 pages; OCR 3 $2 per 1,000 pages. ([Mistral pricing](https://docs.mistral.ai/inference/pricing))
- **Cloudflare (US):** bge-m3 $0.012/M; qwen3-embedding-0.6b $0.012/M; bge-reranker-base $0.003/M. ([Cloudflare](https://developers.cloudflare.com/workers-ai/platform/pricing/))
- **NLI models:** none of the hosts above lists one. I searched the catalogues fetched and found none.

**Prompt caching: mechanics and billing**
- **Mistral:** "Cached prompt tokens are billed at 10% of the standard input token price."
  - Opt-in by sending the same `prompt_cache_key`, which "increases the chance of a cache hit, but it doesn't guarantee one".
  - 64-token blocks; prompts under 64 tokens never hit. No write cost and no TTL stated.
  - ([Mistral prompt caching](https://docs.mistral.ai/inference/conversations/advanced/prompt-caching))
- **Mistral regional (EU) inference** is "billed at 1.1× standard list pricing" for input, output, cached reads and cache writes. Agents, Batch and Files are not available on regional endpoints. ([Mistral regional inference](https://docs.mistral.ai/inference/regional-inference))
- **Nebius:**
  - Caching is automatic ("you don't need to change your requests, set cache keys, or opt in") and best-effort, with no guaranteed TTL; "an unused prefix may be removed after a few minutes".
  - On serverless the cache "is shared within a model across organizations"; dedicated endpoints get an isolated cache.
  - Caching works the same under ZDR.
  - ([Nebius cached tokens](https://docs.tokenfactory.nebius.com/cached-tokens))
- **T-Systems AIFS:** cached input is billed at 15% of the normal input price, for T-Cloud-hosted models only (per the LLM Hub docs as summarised by search). ([T-Systems plans](https://docs.llmhub.t-systems.net/plans/))
  - Consistent with the per-model table: GLM-5.3 €1.40 → €0.21 and DeepSeek V4.1 Flash €0.30 → €0.045 are both 15%. ([T-Systems models](https://docs.llmhub.t-systems.net/models/))
- **Berget:** "For models with cached-input pricing… prefix-cache hits are billed at a reduced rate. Other models bill cached tokens at the regular input rate." Only Kimi K3.1 Pro has a cached price (€0.90 vs €3.00, i.e. 30%). ([Berget pricing](https://berget.ai/en/pricing), [Berget models API](https://api.berget.ai/v1/models))
- **Scaleway:** cached prices are listed for deepseek-v4.1-flash-1017 (€0.12, 20% of input), qwen3.8-27b (€0.12, 20%) and deepseek-v4-flash-0731 (€0.08, 20%). The mechanics and TTL could not be read because Scaleway's docs returned HTTP 403. ([Scaleway](https://www.scaleway.com/en/generative-apis/))
- **Verda:** "Cache read applies to input tokens that match a recently processed prompt prefix." Kimi K3.1 Pro cache read is $0.20 (10%); DeepSeek 4.1 Flash is $0.006 (4%). ([Verda pricing](https://verda.com/pricing))
- **OVH, IONOS, STACKIT, Regolo, Infomaniak:** no cached-input price on their pricing pages (pages above).

**Billing models and VAT**
- **Berget:**
  - Prepaid plans only after the €5 trial: "an active plan (from €25 / month in prepaid credits) is required… we don't offer pure pay-as-you-go without a plan."
  - "All listed prices exclude VAT"; EU businesses with a VAT ID are reverse-charged.
  - ([Berget pricing](https://berget.ai/en/pricing))
- **Regolo:** "*Prices exclude VAT, applied only in Italy". PAYG has a €0 monthly fee; subscriptions run €39–€319/month with daily token allowances weighted by a per-model multiplier. ([Regolo pricing](https://regolo.ai/pricing/))
- **Infomaniak:** "Prices do not include VAT". Prices are in CHF; 1M free credits. ([Infomaniak](https://www.infomaniak.com/en/hosting/ai-services/prices))
- **Hetzner:** all prices shown "excl. VAT". ([Hetzner GPU](https://www.hetzner.com/dedicated-rootserver/matrix-gpu/))
- **Scaleway:** first 1,000,000 tokens free; a Batches API discount is mentioned but not quantified on the page. ([Scaleway](https://www.scaleway.com/en/generative-apis/))
- **T-Systems:** "Shared plans use a monthly token revenue commitment. Usage above it is billed at list prices." Plans are Essential, Professional and Agentic; Enterprise is custom. ([T-Systems plans](https://docs.llmhub.t-systems.net/plans/))
- **Mistral:** batch processing "reduces the price by 50%", and "cached input tokens reduce input cost by up to 90%". ([Mistral pricing page](https://mistral.ai/pricing))

**US providers with EU options (official)**
- **Together AI:** "EU data centers available for customers who need their inference and storage to remain within the European Union". Creating dedicated endpoints in targeted (EU) data centers requires a Scale or Enterprise plan, and pricing comes from sales. The article does not say whether EU serverless is available. ([Together support](https://support.together.ai/articles/8079447813-eu-data-centers-and-dedicated-model-deployment))
- **Fireworks:**
  - "Region-restricted deployments are priced at 1.5x" for GPU deployments.
  - "Fireworks Sovereign" (inference on GPUs in the customer's own cloud or data center) is "Private preview for Enterprise", priced by contract.
  - Serverless GLM 5.3 costs $1.40 / $0.26 / $4.40; DeepSeek V4.1 Flash $0.30 / $0.006 / $1.20.
  - ([Fireworks pricing](https://fireworks.ai/pricing))
- **AWS Bedrock (from the official model–region table):**
  - gpt-oss-120b: **In-Region** in eu-central-1 (Frankfurt), eu-north-1, eu-south-1, eu-west-1 and eu-west-2.
  - Qwen3 235B A22B 2507: In-Region in Frankfurt, Stockholm, Milan and London.
  - DeepSeek V3.2: In-Region only in Stockholm and London.
  - **Kimi K3 / Kimi K3.1 Pro Highspeed / GLM 5.3** in EU regions are "not-supported" In-Region and Geo, and supported **only via Global** cross-region inference, which is not EU-bound.
  - No DeepSeek V4.x or MiniMax M3.1 entries.
  - ([AWS Bedrock model region compatibility](https://docs.aws.amazon.com/bedrock/latest/userguide/models-region-compatibility.html))
- **Azure AI Foundry:** Fireworks' Microsoft partner page reportedly says EU Data Zone PayGo for Fireworks-served models (DeepSeek, Kimi) is "Not today… EU coverage is on the roadmap". Microsoft's own pricing pages showed placeholders. **Unverified; search-summary only.** ([Fireworks × Microsoft](https://fireworks.ai/partners/microsoft), [Azure Foundry Fireworks pricing](https://azure.microsoft.com/pricing/details/ai-foundry-models/fireworks/))
- **Google Vertex AI:**
  - Google's open-models deprecation page reportedly lists DeepSeek-V3.1/V3.2, GLM 4.7/5 and Kimi K2 Thinking MaaS for retirement on 21 Oct 2026, recommending self-deployment instead.
  - Data at rest is stored in the selected region, but "regionalization of data processing may vary".
  - **Search-summary only; I did not fetch the page.**
  - ([Vertex open-model deprecations](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/deprecations/open-models), [Vertex MaaS open models](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/maas/use-open-models))
- **Cloudflare Workers AI:** prices are listed above; DeepSeek V4.x, GLM-5.3 and Kimi K2.6 need a paid plan. ([Cloudflare](https://developers.cloudflare.com/workers-ai/platform/pricing/))
  - I found no official doc for an EU jurisdiction setting on Workers AI. Cloudflare's Jurisdiction Restrictions apply to Durable Objects, and the Data Localization Suite is an Enterprise add-on. (Search summary.) ([Cloudflare Data Localization Suite](https://www.cloudflare.com/data-localization))

### Inferences
- **Cheapest official EU-owned prices per tier:**
  - **DeepSeek V4.1 Flash:** OVH at €0.27/€1.08 has the cheapest list price but no cache discount. T-Systems at €0.30 / €0.045 cached / €1.20 will be cheaper for chat apps with long, repeated system prompts and history, where cache hits dominate input.
  - **GLM-5.3:** T-Systems at €1.40 / €0.21 / €4.40 beats Scaleway (€1.80/€5.50, no cache) and is roughly equal to Mistral EU ($1.54 / $0.154 / $4.84).
  - **GLM-5.3-Flash:** T-Systems (€0.20 / €0.03 / €0.60) or Mistral EU ($0.165 / $0.033 / $0.55).
  - **Qwen3.8-27B:** STACKIT's €0.65 output is an outlier, about 4× cheaper than OVH/IONOS (€2.70). Worth confirming with STACKIT that it is not a placeholder.
  - **gpt-oss-120b:** OVH €0.08/€0.40.
- Mistral's EU region is effectively a 10% surcharge. OpenRouter's `mistral/eu` endpoints show exactly 1.1× the global price ($0.77 vs $0.70 for Large 4), which corroborates the docs.
- Mistral now hosts third-party open models (GLM-5.3, GLM-5.3-Flash, DeepSeek V4.1 Flash). That makes it a single EU-owned vendor for both "Mistral" and "Chinese open-weight" tiers, but Kimi K3.1 Pro is absent.
- For a LibreChat + LiteLLM gateway, a realistic EU-owned stack needs 3–4 provider accounts: T-Systems or Mistral EU, OVH/Scaleway, Berget or Verda for Kimi, and one helper-model host.

### Gaps
- **Nebius:** the official price page (`tokenfactory.nebius.com/organization/prices`) returned HTTP 403 (login-walled) and `nebius.com/prices-ai-studio` returned 404. All Nebius prices here are aggregator (OpenRouter) figures.
- **Scaleway:** the `/en/pricing/model-as-a-service/` page and the data-privacy and rate-limit docs returned HTTP 403. Prices come from the official `/en/generative-apis/` product page (Paris region selector).
- **Mistral:** the docs pricing page does not label currency explicitly. USD is inferred from OpenRouter matching.
- **Mistral Large 4 / Medium 3.5 licensing:** whether these are open-weight (Apache-2.0) could not be confirmed. Mistral's pricing FAQ says open-weight commercial deployments "require a Mistral license with separate terms" for some models. ([Mistral pricing](https://mistral.ai/pricing))
- **No cached price or VAT statement:** OVH, IONOS, STACKIT (cached); OVH, IONOS, STACKIT, Scaleway, T-Systems, Mistral (VAT).
- **Not found:**
  - Gcore Everywhere Inference: no per-token price; API docs show only per-hour deployment pricing examples.
  - Nscale: no per-token price found (the official serverless page did not render numbers; aggregators conflict).
  - Exoscale: no per-token or GPU price extracted.
  - Genesis Cloud and Cudo: not researched (call budget).
  - Baseten EU and DeepInfra EU: no EU-region confirmation found.
- **Qwen:** "Qwen3.8" open flagship (`qwen3.8-2.4t-a95b`) appears only on Alibaba, Novita, SiliconFlow and Venice (non-EU) per OpenRouter. Its open-weight status is unconfirmed.

---

## Q2. Data handling: retention, logging, training, DPA, EU-only processing, sub-processors, certifications

### Takeaway
- **Strongest written guarantees:**
  - **IONOS:** prompts are never logged or persisted, processing happens in German data centers only, there are no third-party sub-processors, and the service is in BSI C5 scope.
  - **Regolo:** zero data retention by design.
  - **Mistral EU and T-Systems:** explicit EU processing.
- **Nebius:**
  - Retains prompts and outputs by default (for speculative decoding) unless ZDR is toggled on.
  - **Its public serverless endpoints are "Global"**, with no fixed processing region.
  - It is therefore not EU-pinned unless you use dedicated endpoints.
- **Mistral:** ZDR is a separate, request-based control. The default reportedly keeps API data for 30 days for abuse monitoring.

### Cited Findings
- **Nebius Token Factory:**
  - Retention is on by default: inputs and outputs are kept for speculative decoding, which "is enabled by default for best performance". Retained data "are stored in Finland (EU)".
  - ZDR is a per-organization toggle: "your inputs (prompts) and outputs (responses) are not stored on our systems after each request is processed". It may reduce inference speed.
  - Training: "We do not use your content to train, fine-tune or improve any AI models".
  - **Public endpoints show region "Global"**: processing location is decided dynamically and can change without notice. Dedicated endpoints process data "within the region you selected".
  - DPA is part of the ToS. Sub-processors get 15 days' prior notice. Certifications: "ISO 27001, ISO 27701 and SOC 2 Type II".
  - Transfers outside the EU rely on SCCs and EU-US DPF certification. Parent company: Nebius Group N.V. (NASDAQ: NBIS).
  - ([Nebius legal quick guide](https://docs.tokenfactory.nebius.com/legal/legal-quick-guide))
- **IONOS AI Model Hub:**
  - Data centers in Germany; "your prompts and the generated outputs are processed there and nowhere else".
  - Prompt and output content "is never logged and is never accessed by personnel… not written to any log or to persistent storage; it is not used to train…".
  - Only metadata (timestamp, model, token counts) is recorded.
  - "No third-party sub-processors are engaged for AI Model Hub."
  - "AI Model Hub falls within the scope of BSI C5." It is covered by the general DPA as a platform service.
  - ([IONOS data handling](https://docs.ionos.com/cloud/ai/ai-model-hub/governance-and-compliance/data-handling))
- **Regolo.ai:** "We do not retain, log, or reuse any input or output data processed through our models"; "No use of data for training, fine-tuning, or any other secondary purpose". The page refers to independent certification of the ZDR policy. ([Regolo zero data retention](https://regolo.ai/zero-data-retention/))
- **OVHcloud AI Endpoints:**
  - "hosted and run in the European Union. Your data is never used to train our models, and we only keep what is strictly necessary for billing" (product page, via search summary). ([OVH AI Endpoints](https://www.ovhcloud.com/en/public-cloud/ai-endpoints))
  - **SecNumCloud:** OVH's SecNumCloud-qualified products are Private Cloud and Bare Metal Pod. Extending the qualification to AI solutions is stated as a plan, not a fact. ([OVH SecNumCloud](https://www.ovhcloud.com/en/compliance/secnumcloud/), [OVH SecNumCloud news](https://corporate.ovhcloud.com/en/newsroom/news/secnumcloud-strategy-acceleration/))
- **Scaleway Generative APIs:** "We do not collect, read, reuse, or analyse the content of your inputs, prompts or outputs generated by the APIs". The tagline reads "Towards a sovereign AI where your data remains yours, and only in Europe." The region selector shows Paris only. ([Scaleway Generative APIs](https://www.scaleway.com/en/generative-apis/))
- **Mistral:**
  - The EU regional endpoint (`api.eu.mistral.ai`) runs on "Multiple data centers in EU and EFTA countries".
  - "Regional inference does not provide regional storage for all control-plane data"; if a workload uses an unsupported feature, "the regional processing guarantees for that workload do not apply".
  - ZDR is a separate control from regional inference. ([Mistral regional inference](https://docs.mistral.ai/inference/regional-inference))
  - ZDR applies to supported stateless API calls on paid plans and is requested via support. Training opt-out is separate ("You do not need ZDR to opt out of model training"). ([Mistral ZDR docs](https://docs.mistral.ai/admin/monitor-comply/zero-data-retention))
  - Secondary sources describe a default 30-day rolling retention for abuse monitoring. ([ConductAtlas summary of Mistral privacy policy](https://conductatlas.com/platform/mistral-ai/mistral-ai-privacy-policy/data-retention-api-inputoutput-30-day-rolling-window/))
  - The Vibe/Le Chat pricing page shows "Model training: Opt-out" on all plans. ([Mistral pricing](https://mistral.ai/pricing))
- **STACKIT:** describes itself as "data-sovereign STACKIT Cloud", region EU01 (Germany). The claims of no data storage and no training come only from partner material (innFactory), and C5 coverage of this specific product is unconfirmed. ([STACKIT product](https://stackit.com/en/products/data-ai/stackit-ai-model-serving), [innFactory review](https://innfactory.ai/en/blog/stackit-ai-model-serving-tested-fully-sovereign-ai-solutions-for-enterprises/))
- **T-Systems AIFS:** open models are hosted on "T Cloud Germany (EU)". In the same catalogue, proprietary models run on Azure Sweden/France and GCP Europe/Worldwide, so it is a mixed sovereign/hyperscaler hub. ([T-Systems models](https://docs.llmhub.t-systems.net/models/))
- **Berget AI:** "Founded in Sweden in 2024, Berget AI offers inference and AI infrastructure for private and public sector organisations." Its managed Kubernetes includes an isolated VLAN option. ([Berget pricing](https://berget.ai/en/pricing))
- **Verda:** "SOC 2 and GDPR compliant". ([Verda pricing](https://verda.com/pricing))
- **Hetzner GPU:** "GDPR-compliant", location eu-central. ([Hetzner GPU](https://www.hetzner.com/dedicated-rootserver/matrix-gpu/))
- **ENS (Spain):** I found no evidence of ENS category ALTA certificates for OVHcloud, Scaleway, IONOS or STACKIT. ENS ALTA certificates exist for Spanish providers such as Telefónica, Claranet and Gigas. One consultancy says AWS and Azure hold ENS Alta. (Search summary.) ([Telefónica ENS ALTA](https://www.telefonica.es/es/wp-content/uploads/sites/10/2025/05/esquema-nacional-seguridad-ALTA-TCCT.pdf), [Gigas ENS Alto](https://www.estrategiasdeinversion.com/actualidad/noticias/empresas/gigas-obtiene-el-ens-alto-y-consolida-su-estrategia-n-892225), [Google Cloud ENS](https://cloud.google.com/security/compliance/ens?hl=es))

### Inferences
- **Nebius is not "EU-sovereign" by default.** Even though retained data sits in Finland, serverless processing is "Global". For a sovereignty-sensitive product, Nebius is usable only via EU-region dedicated endpoints with ZDR on, or not at all.
- **Mistral EU covers chat completions and function calling only.** Agents, Batch and Files are excluded from regional guarantees, so LibreChat file uploads and RAG must not use Mistral's Files API if EU-only processing is required.
- **The cleanest paper trail for a GDPR DPIA:** IONOS (explicit no-log, no sub-processors, C5) and Regolo (ZDR by design). Both have narrower model catalogues; neither has Kimi K3.1 Pro or GLM-5.3.

### Gaps
- Scaleway's data-privacy and rate-limit docs returned HTTP 403. Certifications (ISO 27001 / HDS) are not verified here.
- OVH AI Endpoints ISO 27001 / SOC 2 / HDS scope is claimed only in marketing copy (search summary).
- Berget, Verda and Regolo ISO 27001 certificates were not verified. Infomaniak data policy was not fetched.
- Mistral's default API retention (30 days) comes from a secondary source.
- No provider-level ENS status was confirmed for any EU-owned AI inference service.

---

## Q3. Ownership, CLOUD Act exposure, and what "sovereign" legally means

### Takeaway
- EU data-centre location does not remove US legal reach when the operator is a US company. Microsoft France's legal director testified under oath that he could not guarantee EU data would not be handed to US authorities.
- The Commission's operational definition of sovereignty is now the Cloud Sovereignty Framework, which uses SEAL levels. In its April 2026 tender, OVHcloud (in a consortium), STACKIT and Scaleway reached **SEAL-3**, while a Google-tech-based offering (S3NS) reached only SEAL-2.
- EUCS "High" with sovereignty requirements is still not adopted.

### Cited Findings
- **CLOUD Act reach (reporting):** the CLOUD Act lets US authorities compel data "even if it is physically stored outside the USA, as long as it is controlled by a US company". ([heise](https://heise.de/-10494789))
  - Statutory basis: 18 U.S.C. § 2713 requires providers to disclose data "regardless of whether such communication, record, or other information is located within or outside of the United States". ([18 U.S.C. § 2713, Cornell LII](https://www.law.cornell.edu/uscode/text/18/2713))
- **Microsoft France testimony:** Anton Carniaux, legal director of Microsoft France, was asked by the French Senate whether French citizens' data would never go to US authorities without French consent. He answered: "No, I cannot guarantee that." Reporting notes the same framework applies to AWS and Google. ([heise](https://heise.de/-10494789), [it-daily](https://www.it-daily.net/shortnews-en/microsoft-eu-data-not-protected-from-us-access))
- **EU Cloud Sovereignty Framework tender (April 2026):** the Commission "awarded its Sovereign Cloud call for tender", worth up to EUR 180 million over 6 years.
  - SEAL-3 ("Digital Resilience level… immune from supply chain disruption by non-EU third parties"): Post Telecom-led partnership with OVHcloud and CleverCloud; STACKIT (Schwarz Group); Scaleway (Iliad Group).
  - SEAL-2 ("Data Sovereignty level"): Proximus-led partnership using S3NS, Clarence and Mistral. S3NS runs Google Cloud technology "exclusively operated by EU companies".
  - SEAL-4 "requires a full EU supply chain, from chips to software". Minimum to be eligible: SEAL-2.
  - ([European Commission news, 2026-04-17](https://commission.europa.eu/news-and-media/news/commission-advances-cloud-sovereignty-through-strategic-procurement-2026-04-17_en))
- **SEAL levels and the CLOUD Act:** the framework (v1.2.1, Oct 2025) ranks offers with a Sovereignty Score and minimum SEAL levels. Secondary summaries map its "legal exposure" objective to exposure to foreign authority, such as the CLOUD Act or FISA. ([Cloud Sovereignty Framework PDF (mirror)](https://ppc.land/content/files/2025/11/Cloud-Sovereignty-Framework.pdf), [arc42 summary](https://quality.arc42.org/standards/eu-cloud-sovereignty-framework))
- **EUCS:** still not adopted. Sovereignty requirements for the "High" level (data localisation, primacy of EU law) were the main sticking point and were opposed as trade barriers. A Feb 2026 legal analysis says a final version is pending.
  - The Commission's June 2026 sovereignty package introduced a Cloud and AI Development Act (CADA). Sources disagree on whether CADA supersedes or complements EUCS. (Secondary / think-tank sources; no primary ENISA doc found.)
  - ([Cullen International on CSA2](https://www.cullen-international.com/news/2026/02/Revised-Cybersecurity-Act--CSA2----Changes-to-the-EU-cybersecurity-certification-framework.html), [EUISS brief](https://iss.europa.eu/publications/briefs/technical-political-when-cloud-certification-scheme-divides-europe), [CSA labs](https://labs.cloudsecurityalliance.org/research/eu-tech-sovereignty-cloud-ai-enterprise-risk-v1-0-csa-styled/))
- **SecNumCloud (France):** OVH holds SecNumCloud 3.2 qualifications in three data centers (Roubaix, Gravelines, Strasbourg) for Private Cloud and Bare Metal Pod, not for AI Endpoints. ([OVH SecNumCloud news](https://corporate.ovhcloud.com/en/newsroom/news/secnumcloud-strategy-acceleration/))
- **Ownership, per provider sources:**
  - STACKIT: "European hyperscaler from Schwarz Digits". ([STACKIT](https://stackit.com/en/products/data-ai/stackit-ai-model-serving))
  - Scaleway: Iliad Group. ([EC](https://commission.europa.eu/news-and-media/news/commission-advances-cloud-sovereignty-through-strategic-procurement-2026-04-17_en))
  - Berget: founded in Sweden. ([Berget](https://berget.ai/en/pricing))
  - Nebius: parent Nebius Group N.V., listed on NASDAQ. ([Nebius legal](https://docs.tokenfactory.nebius.com/legal/legal-quick-guide))
  - T-Systems (Deutsche Telekom): open models on T Cloud Germany. ([T-Systems](https://docs.llmhub.t-systems.net/models/))
  - Together: US company; "a US provider can offer EU residency but not EU sovereignty" (competitor-sourced commentary). ([lyceum](https://lyceum.technology/magazine/together-ai-alternatives-for-eu-data-residency/))
- **AWS European Sovereign Cloud** is a separate partition from eu-central-1. Its first GA open-weight family is Gemma 4, so none of the candidate models are there. (Search summary.) ([AWS Security Blog](https://aws.amazon.com/blogs/security/run-open-weight-models-on-aws-bedrock-in-aws-european-sovereign-cloud/))

### Inferences
- **EU-owned and EU-operated (lowest CLOUD Act exposure):** OVHcloud, Scaleway, STACKIT, IONOS, T-Systems (Telekom), Mistral, Berget, Regolo/Seeweb, Infomaniak (Swiss; Switzerland has an EU adequacy decision), Hetzner. Probably Verda too: its Finnish ownership was not verified here.
- **US-owned, CLOUD-Act-exposed even in EU regions:** AWS, Azure, Google, Cloudflare, Together, Fireworks, DeepInfra, Baseten.
- **Nebius is a grey zone:** a Dutch-domiciled parent, but it operates US data centers and subsidiaries. Its serverless routing is "Global" and it relies on EU-US DPF for transfers. Treat it as "EU-headquartered but not EU-only" and verify which entity you contract with.
- Using OpenRouter (a US company) as the router would itself break the sovereignty story. LiteLLM should call EU providers directly.
- For marketing claims, "EU-hosted, EU-owned provider, no US parent" is defensible for the EU-owned set. "Sovereign" in the EC sense (SEAL-3) is evidenced only for OVHcloud, STACKIT and Scaleway.

### Gaps
- I did not obtain the primary EDPB/EDPS 2019 joint response on the CLOUD Act (the URL I tried returned 404).
- I did not obtain a primary French Senate transcript.
- I did not determine whether Mistral, IONOS or T-Systems have SEAL ratings, or whether CADA has entered into force.

---

## Q4. Performance: speed, TTFT, uptime, rate limits

### Takeaway
Public performance data for EU hosts is thin.
- **Artificial Analysis:** covers Scaleway and Nebius for GLM-5.3 (they sit mid-pack on time per task) but has no EU-host data for DeepSeek V4.1 Flash.
- **OpenRouter one-day uptime** for EU-relevant endpoints is mostly ≥99%: Nebius 100%, Mistral EU 99.0–100%.
- **Rate limits:** OVH publishes 400 requests/min per project per model.

### Cited Findings
- **Artificial Analysis, GLM-5.3** (time per Intelligence Index task / time to first answer token; TTFAT includes reasoning, so it is not raw TTFT):
  - Scaleway: 12.1 min / 33.93 s (max blended price $2.52/M)
  - Nebius FP4: 14.9 min / 48.78 s
  - Together: 12.6 min / 41.32 s
  - Fireworks: 17.2 min / 51.20 s; Fireworks FAST: 8.2 min / 25.93 s
  - Baseten: 16.5 min / 47.13 s; Baseten FAST: 8.1 min / 25.79 s
  - DeepInfra: 22.7 min / 78.65 s
  - Z.ai: 23.1 min / 67.58 s
  - Mistral, OVH, Bedrock and Cloudflare are not listed.
  - [AGG] ([Artificial Analysis GLM-5.3 providers](https://artificialanalysis.ai/models/glm-5-3/providers))
- **Artificial Analysis, DeepSeek V4.1 Flash:** no output-speed data. TTFAT ranges from Baseten FAST 6.66 s and Together 18.62 s to DeepInfra 49.11 s. No EU-owned host (Nebius, Mistral, Scaleway, OVH, Verda) is listed. [AGG] ([AA DeepSeek V4.1 Flash providers](https://artificialanalysis.ai/models/deepseek-v4-1-flash/providers))
- **OpenRouter one-day uptime** [AGG], snapshot taken 2026-11-18:
  - Nebius: 100% for DeepSeek V4.1 Flash, GLM-5.3, GLM-5.3-Flash, Kimi K3.1 Pro, Qwen3.8-27B, MiniMax M3.1-Flash and gpt-oss-120b.
  - Mistral `eu`: 99.02% (Large 4), 100% (Small 4, GLM-5.3 EU).
  - Mistral `zdr`: 99.24% (Large 4).
  - Cloudflare: 99.43% (DeepSeek V4.1 Flash), 99.92% (GLM-5.3), 86.67% (Qwen3.8-27B).
  - DeepInfra flex: 76.6% (V4.1 Flash).
  - Amazon Bedrock us-east: 73.8% (Kimi K3.1 Pro).
  - Bedrock eu-west-1: 99.76% (gpt-oss-120b).
  - ([OpenRouter endpoints API](https://openrouter.ai/api/v1/models/z-ai/glm-5.3/endpoints))
- **Berget status, self-reported** in its public models API: Kimi-K3.1-Pro latency 1,111 ms and 81.3 tokens/s; GLM-5.3-Flash latency 1,104 ms. ([Berget models API](https://api.berget.ai/v1/models))
- **OVH rate limits:** "400 requests per minute, per Public Cloud project and per model"; anonymous access is "2 requests per minute, per IP and per model". ([OVH AI Endpoints capabilities](https://help.ovhcloud.com/csm/en-public-cloud-ai-endpoints-capabilities?id=kb_article_view&sysparm_article=KB0065424))
- **Scaleway:** "End-users in Europe will benefit from response time below 200ms to get the first tokens streamed" (marketing claim). ([Scaleway](https://www.scaleway.com/en/generative-apis/))
- **T-Systems:** RPM and TPM ceilings depend on plan tier and are "best-effort". ([T-Systems plans](https://docs.llmhub.t-systems.net/plans/))
- **Berget:** Kimi K3 is rate-limited in Berget Code once 50% of quota is used, and serverless rate limits are "shared per seat". ([Berget pricing](https://berget.ai/en/pricing))
- **Nebius:** a ZDR account loses speculative decoding, which "may impact the level of service provided (e.g., inference speed)". ([Nebius legal](https://docs.tokenfactory.nebius.com/legal/legal-quick-guide))

### Inferences
- **Scaleway's GLM-5.3** is competitive on speed: the fastest non-"FAST" endpoint measured by Artificial Analysis.
- **Nebius benchmarks** are probably measured with speculative decoding on. Expect slower results with ZDR enabled.
- Build LiteLLM fallbacks: uptime snapshots vary from 73% to 100% across providers on the same day.

### Gaps
- No tokens/s or TTFT data for OVH, IONOS, STACKIT, T-Systems, Regolo, Mistral EU or Verda.
- No published rate limits for Scaleway (docs 403), IONOS, STACKIT, Regolo or Mistral (tier-based; not fetched).
- No published SLA/uptime figures from EU-owned providers were retrieved.

---

## Q5. Self-hosting comparison: EU GPU rental costs and break-even; CPU helper models on a VPS

### Takeaway
- **EU GPU rental, on-demand:**
  - Verda (Finland): H100 $5.40/h, H200 $6.90/h, B200 $9.80/h, B300 $12.79/h.
  - Hetzner (Germany): RTX PRO 6000 96 GB servers from €999/month (1× GPU) to €3,599/month (4× GPU).
- **Big MoE models:** at current per-token prices, self-hosting a large MoE (DeepSeek V4.1 Flash is 748B parameters) only pays at tens of billions of tokens per month.
- **Mid-size dense models:** a Qwen3.8-27B-class model on one Hetzner GPU breaks even at roughly 1.5–3B tokens/month.
- **Helper models** (embeddings, rerankers) are so cheap via API (bge-m3 €0.01/M on OVH) that CPU self-hosting is justified by privacy or latency, not cost.

### Cited Findings
- **Verda on-demand GPU prices (spot in brackets), USD:**
  - 1× GB300 288 GB: $14.71/h ($7.354)
  - 1× B300 268 GB: $12.79/h ($6.395)
  - 1× B200 180 GB: $9.796/h ($4.898)
  - 1× H200 141 GB: $6.904/h ($3.452)
  - 1× H100 80 GB: $5.399/h ($2.700)
  - 1× A100 80 GB: $2.422/h ($1.211)
  - ([Verda pricing](https://verda.com/pricing))
- **Hetzner GEX GPU servers** (excl. VAT, location eu-central):
  - GEX45 (RTX PRO 4000 Blackwell 24 GB): €214/month or €0.3429/h, +€209 setup
  - GEX63 (1× RTX PRO 6000 Blackwell Max-Q 96 GB): €999/month or €1.6009/h, +€999 setup
  - GEX131 (RTX PRO 6000 96 GB, Xeon Gold 5412U, from 256 GB RAM): from €1,499/month or €2.4022/h, +€1,499 setup
  - GEX430 (4× RTX PRO 6000 96 GB): €3,599/month or €5.7676/h, +€3,599 setup
  - No H100/H200/B200 listed.
  - ([Hetzner GPU](https://www.hetzner.com/dedicated-rootserver/matrix-gpu/))
- **Hetzner Cloud VPS** (excl. VAT): shared "Regular Performance" from €5.49/month; "Cost-Optimized" from €5.99/month (currently not available); dedicated-vCPU "General Purpose" from €36.99/month. ([Hetzner Cloud](https://www.hetzner.com/cloud/))
- **Scaleway's dedicated-vs-serverless calculator:**
  - Example: mistral-small-3.2 at 10,000 input + 1,000 output tokens per request; 2× H100 needed.
  - "Dedicated Deployment… €1,655 Usage time only… €4,964 At maximum size (24/7)" versus serverless at €2,775/month.
  - This implies about €3.40 per H100-hour on Scaleway dedicated (€4,964 / 730 h / 2).
  - ([Scaleway](https://www.scaleway.com/en/generative-apis/))
- **Fireworks:** region-restricted GPU deployments cost 1.5× standard GPU rates. ([Fireworks](https://fireworks.ai/pricing))
- **Model sizes, from OVH catalog metadata:** DeepSeek-V4.1-Flash-1017 "748B" (fp4, 1000K context); Qwen3.8-27B "27B" (fp8); bge-m3 "0.567B"; Qwen3-Embedding-8B "7.6B". ([OVH catalog](https://www.ovhcloud.com/en-ie/public-cloud/ai-endpoints/catalog/))

### Inferences (my calculations; not from sources)
- **Break-even, large MoE (DeepSeek V4.1 Flash, 748B fp4):**
  - Serving needs roughly a full 8-GPU H200/B200 node. On Verda that is 8 × $6.904 = **$55.2/h ≈ $40.3k/month** on-demand.
  - The T-Systems API at €0.30 in / €1.20 out averages about €0.525/M for a 3:1 input:output mix.
  - Break-even is about 75B tokens/month (about 29k tokens/s sustained, 24/7). Self-hosting this tier is not rational for an early-stage product.
- **Break-even, Qwen3.8-27B:**
  - One Hetzner GEX131 costs €1,499/month (plus €1,499 setup).
  - Versus OVH/IONOS (€0.40/€2.70, about €0.975/M at 3:1), break-even is about 1.5B tokens/month (about 590 tokens/s average).
  - Versus STACKIT (€0.45/€0.65, about €0.50/M), break-even is about 3B tokens/month.
  - Whether one RTX PRO 6000 can sustain that aggregate throughput with vLLM batching is unverified.
- **Kimi K3.1 Pro:** OpenRouter metadata shows model_size 2,800 (B) in Berget's API, which needs multi-node B200/GB300 capacity. Self-hosting is out of reach; use Berget or Verda.
- **CPU helpers:** bge-m3 (568M), multilingual-e5-large, bge-reranker-v2-m3 and Qwen3-Reranker-0.6B, plus a small NLI cross-encoder, fit comfortably in RAM. They can run on a Hetzner dedicated-vCPU instance (from €36.99/month) or even a shared €5.49–€15 VPS for low volume.
  - But OVH charges €0.01 per 1M embedding tokens, so 1B embedding tokens cost about €10 via API.
  - Self-host helpers only for latency, offline operation, NLI (which no host offers), or to keep document text on your own box.

### Gaps
- MI300X EU pricing was not found. I did not fetch H100/H200 prices for Nebius, Scaleway, OVH GPU, Genesis Cloud, Cudo, Nscale or Gcore.
- No measured CPU throughput figures (tokens/s for bge-m3 or rerankers on Hetzner vCPUs) were retrieved.
- Real vLLM throughput for the candidate models on RTX PRO 6000 or H200 was not retrieved.

---

## Q6. Recommended primary + backup EU host per tier

### Takeaway
- **Fast tier:** GLM-5.3-Flash or DeepSeek V4.1 Flash on T-Systems (primary) with Mistral EU (backup).
- **Balanced tier:** Qwen3.8-27B or gpt-oss-120b on OVH or STACKIT, with Scaleway as backup.
- **Strong tier:** GLM-5.3 on T-Systems or Mistral EU, with Scaleway as backup. Kimi K3.1 Pro on Berget, with Verda as backup.
- **Helpers:** OVH or IONOS embeddings and rerankers, plus self-hosted NLI on a Hetzner CPU box.
- **Avoid as "sovereign":** US hyperscalers and Nebius serverless.

### Cited Findings (basis for the recommendation)
- **T-Systems:** the only EU-owned host found with published cached-input pricing on all of DeepSeek V4.1 Flash, GLM-5.3, GLM-5.3-Flash and Qwen3.8-27B, at 15% of input; hosted on T Cloud Germany. ([T-Systems models](https://docs.llmhub.t-systems.net/models/))
- **Mistral EU:** carries GLM-5.3, GLM-5.3-Flash, DeepSeek V4.1 Flash, Large 4 and Small 4, with a 10% cached rate and a 1.1× EU uplift. ([Mistral pricing](https://docs.mistral.ai/inference/pricing), [Mistral regional](https://docs.mistral.ai/inference/regional-inference))
- **Kimi K3.1 Pro EU-owned options:** Berget (€3 / €0.90 / €10) and Verda ($2 / $0.20 / $10). ([Berget API](https://api.berget.ai/v1/models), [Verda](https://verda.com/pricing))
- **Scaleway:** SEAL-3; GLM-5.3 €1.80/€5.50; DeepSeek V4.1 Flash €0.60/€0.12/€1.80. ([EC](https://commission.europa.eu/news-and-media/news/commission-advances-cloud-sovereignty-through-strategic-procurement-2026-04-17_en), [Scaleway](https://www.scaleway.com/en/generative-apis/))
- **OVH:** SEAL-3 (consortium); lowest list prices on DeepSeek V4.1 Flash (€0.27/€1.08) and gpt-oss-120b (€0.08/€0.40); 400 RPM per model. ([OVH catalog](https://www.ovhcloud.com/en-ie/public-cloud/ai-endpoints/catalog/), [OVH limits](https://help.ovhcloud.com/csm/en-public-cloud-ai-endpoints-capabilities?id=kb_article_view&sysparm_article=KB0065424))

### Inferences (recommendation)

| Tier | Model | Primary | Backup | Why |
|---|---|---|---|---|
| Fast / cheap | GLM-5.3-Flash | T-Systems (€0.20 / €0.03 / €0.60) | Mistral EU ($0.165 / $0.033 / $0.55); Berget (€0.25/€0.50) as third | EU-owned, German hosting, cache discount; Mistral adds a second French legal entity |
| Fast / cheap | DeepSeek V4.1 Flash | T-Systems (€0.30 / €0.045 / €1.20) | OVH (€0.27 / – / €1.08), with Scaleway or Mistral EU as alternates | T-Systems cache makes chat history cheap; OVH has the cheapest list price and SEAL-3 |
| Balanced | Qwen3.8-27B | STACKIT (€0.45/€0.65, pending confirmation of the outlier price) or OVH/IONOS (€0.40/€2.70) | T-Systems (€0.50 / €0.075 / €2.50) or Scaleway (€0.60 / €0.12 / €3.30) | Multiple EU-owned hosts, so easy failover |
| Balanced | gpt-oss-120b | OVH (€0.08/€0.40) | Scaleway (€0.15/€0.60) or IONOS (€0.15/€0.65) | Cheapest EU-owned; widely hosted |
| Balanced (EU-native brand) | Mistral Small 4 / Large 4 | Mistral EU endpoint | Regolo or Infomaniak for Small 4; none found for Large 4 | Large 4 is only available from Mistral |
| Strong | GLM-5.3 | T-Systems (€1.40 / €0.21 / €4.40) or Mistral EU ($1.54 / $0.154 / $4.84) | Scaleway (€1.80/€5.50; fast on AA) | Three EU-owned hosts |
| Strong (frontier) | Kimi K3.1 Pro | Berget (Sweden; €3 / €0.90 / €10; ex-VAT, prepaid plan) | Verda ($2 / $0.20 / $10, preview); Nebius dedicated EU endpoint + ZDR only if contracted | Only EU-owned options found |
| Strong | DeepSeek V4 Pro, MiniMax M3.1-Flash | No EU-owned serverless host; drop from launch lineup, or self-host V4 Pro on dedicated EU GPUs only at high volume | – | Only US/Chinese hosts or Nebius-global |
| Helpers | Embeddings / rerank / OCR | OVH bge-m3 (€0.01/M) + IONOS Qwen3-VL-Reranker-8B (€0.04/M) or Infomaniak bge-reranker-v2-m3 (CHF 0.01/M) | T-Systems BGE-M3 / Qwen3-Reranker-4B (€0.05/M); T-Systems PaddleOCR-VL (€0.10/€0.40) | Cheap, EU-owned |
| Helpers | NLI / guard | Self-host on Hetzner dedicated-vCPU (from €36.99/month); OVH Qwen3Guard free (beta) | – | No hosted NLI found |

- Configure LiteLLM with per-model fallback lists drawn from the table, and with ZDR or no-log providers first.
- Avoid routing through OpenRouter, US hyperscaler EU regions and Nebius serverless if the product promise is "EU-owned and EU-only".
- Price caveat: mixing EUR and USD providers adds FX exposure. EUR-billed options are T-Systems, OVH, Scaleway, IONOS, STACKIT, Berget and Regolo. Mistral, Verda and Nebius are USD on the pages seen.

### Gaps
- No SLA comparison is available. All prices should be re-checked at contract time.
- Specifically needs confirmation: STACKIT Qwen3.8-27B output price, the Scaleway price page (403), the Nebius login-walled price list, and T-Systems minimum monthly commitments per plan.
