# Enterprise security controls and trust path for a self-hosted LibreChat + LiteLLM + MongoDB + PostgreSQL + Caddy stack (as of 2026-11-20)

Version context: LibreChat v0.8.9 released 2026-11-17 (v0.8.8 on 2026-09-30) per the [LibreChat changelog](https://www.librechat.ai/changelog). LiteLLM docs consulted are the live docs.litellm.ai pages (no single version stamped); the March 2026 incident affected PyPI 1.82.7/1.82.8. Research was capped at roughly 20 tool calls; items I could not verify are listed under Gaps in each section. Many cost figures come from vendor/aggregator sites with a commercial interest and are flagged as such.

---

## Q1. Control-by-control: what the stack provides natively, with configuration, with custom code, from a third party, or not feasible

### Takeaway
SSO (OIDC/SAML), local-signup disabling, domain allow-lists, 2FA for local users, retention TTLs, per-key budgets/rate limits, Presidio PII masking, spend-log retention and image-pinning are all achievable in open-source form with configuration. The gaps that cost money or code are: LiteLLM's enterprise-gated items (audit logs, SCIM, JWT auth, secret-manager integrations, guardrails per key/team, tag budgets, RBAC beyond basics), LibreChat SCIM (no evidence found), a per-user "who asked what / which files and connectors" audit trail (must be assembled from Mongo + LiteLLM logs), and MongoDB encryption at rest (Enterprise-only natively, so use disk/volume encryption instead).

### Cited Findings

**SSO / identity (LibreChat)**
- LibreChat supports OpenID Connect/OAuth2, SAML, LDAP/AD, email login and passkeys (passkeys off by default, `ALLOW_PASSKEY_LOGIN=true`) — [LibreChat auth docs](https://www.librechat.ai/docs/configuration/authentication)
- `ALLOW_REGISTRATION` toggles email sign-up; with it off an admin can still add users with the create-user script. The docs state OpenID and SAML "don't support disabling registration alone" (i.e., any user who authenticates at the IdP can be auto-created unless restricted by domain/role) — [LibreChat auth docs](https://www.librechat.ai/docs/configuration/authentication)
- `ALLOW_EMAIL_LOGIN=false` hides the local login form and rejects local/LDAP credential logins while OIDC/SAML keep working; `ALLOW_EMAIL_LOGIN_OVERRIDE` permits credential login for controlled API integrations and each use is logged — [LibreChat auth docs](https://www.librechat.ai/docs/configuration/authentication)
- Allowed email domains are set in the `registration` block of `librechat.yaml` (domain restriction) — [LibreChat auth docs](https://www.librechat.ai/docs/configuration/authentication)
- The first account in a single-tenant deployment becomes ADMIN, so create it with local email/password first — [LibreChat auth docs](https://www.librechat.ai/docs/configuration/authentication)
- Entra ID: OIDC via app registration; role/group gating with `OPENID_REQUIRED_ROLE` (comma-separated), `OPENID_REQUIRED_ROLE_PARAMETER_PATH`, `OPENID_REQUIRED_ROLE_TOKEN_KIND`; a groups claim must be added under Token configuration; Graph group search needs `GroupMember.Read.All` (usually admin consent) and `OPENID_REUSE_TOKENS=true` — [LibreChat Entra guide](https://www.librechat.ai/docs/configuration/authentication/OAuth2-OIDC/azure)
- Google: OAuth client with `GOOGLE_CLIENT_ID/SECRET`; the Google page does NOT document a Workspace hosted-domain (`hd`) restriction, only that the admin-panel refresh re-checks "allowed domain" — [LibreChat Google guide](https://www.librechat.ai/docs/configuration/authentication/OAuth2-OIDC/google). Domain restriction therefore relies on the `registration` allowed-domains list.
- `OPENID_ADMIN_ROLE` grants ADMIN from an IdP role/group (admin-panel docs); official Keycloak page says token-kind values are `id`/`access`, while a Mintlify mirror shows `access_token` — docs conflict, test against your version — [Admin panel docs](https://www.librechat.ai/docs/configuration/admin_panel); [search summary of Keycloak page vs mirror](https://www.librechat.ai/llms.mdx/docs/configuration/authentication/OAuth2-OIDC/keycloak)
- SAML: supports cert, NameID binding (stable NameID, not email), claim mapping; Single Logout (SLO) NOT supported; SAML and OIDC are mutually exclusive (OIDC wins if both set); the SAML page documents no role/group mapping — [LibreChat SAML docs](https://www.librechat.ai/docs/configuration/authentication/SAML)
- Session settings: access token 15 min, refresh 7 days defaults (`SESSION_EXPIRY`, `REFRESH_TOKEN_EXPIRY`); with `OPENID_REUSE_TOKENS=true` the IdP's token lifetime/revocation governs the session — [LibreChat auth docs](https://www.librechat.ai/docs/configuration/authentication)
- SCIM: a search for LibreChat SCIM support found nothing LibreChat-specific (results were OpenAI, Okta, Open WebUI). Open WebUI does document SCIM 2.0 — [Open WebUI SCIM](https://docs.openwebui.com/features/authentication-access/auth/scim.txt). LiteLLM lists SCIM as Enterprise — [LiteLLM enterprise](https://docs.litellm.ai/docs/enterprise)

**MFA/2FA**
- Local/LDAP users can enable TOTP-style 2FA; `ENFORCE_TWO_FACTOR_AUTHENTICATION=true` forces enrollment; OIDC/SAML users cannot (the IdP must enforce MFA); enforcement is process-wide env, not per tenant — [LibreChat auth docs](https://www.librechat.ai/docs/configuration/authentication)

**RBAC / admin**
- Admin panel is a separate service requiring LibreChat v0.8.5+, talking to `/api/admin` endpoints; admins need ADMIN role or `access:admin` capability; capabilities such as `read:configs`, `manage:configs`, section-scoped `manage:configs:<section>`; custom roles, groups, system grants; grant audit log (list, CSV export, integrity check; needs `read:audit_log`; no write endpoints); SSO via the same OIDC or Google; `ADMIN_SSO_ONLY` hides password form; bundled in official Docker Compose; Helm option — [Admin panel docs](https://www.librechat.ai/docs/configuration/admin_panel)
- The admin-panel docs page states no license; the repo ClickHouse/librechat-admin-panel is AGPL-3.0, has 114 commits, no releases/packages listed, 26 open issues — [GitHub repo](https://github.com/ClickHouse/librechat-admin-panel). The v0.8.8 release candidate notes said it was bundled into default compose files — [search result summary, LibreChat changelog](https://www.librechat.ai/changelog)
- Outside the panel, LibreChat's permission model is ADMIN/USER system roles plus ACLs on shared agents/prompts (from a third-party mirror, lower reliability) — [Mintlify mirror](https://www.mintlify.com/danny-avila/LibreChat/user-management/permissions)
- MCP access can be controlled via interface `use`/`create`/`share` flags — [LibreChat MCP settings](https://www.librechat.ai/v0.8.7/docs/configuration/librechat_yaml/object_structure/mcp_settings)

**Audit logging**
- LiteLLM "Audit logs" (admin actions, key-level changes, retention policies) are Enterprise — [LiteLLM enterprise](https://docs.litellm.ai/docs/enterprise)
- LiteLLM open-source includes spend tracking, request/response logging, Prometheus metrics (pricing page) — [LiteLLM pricing](https://www.litellm.ai/pricing). Spend logs are stored in Postgres; `store_prompts_in_spend_logs` adds prompt/response bodies to DB (off by default; the prod docs advise keeping it off for sensitive workloads) — [LiteLLM prod guide](https://docs.litellm.ai/docs/proxy/prod)
- Enterprise adds team-based logging, per-team logging opt-out, log export to GCS/Azure Blob — [LiteLLM enterprise](https://docs.litellm.ai/docs/enterprise)
- LibreChat's own admin "grant audit log" covers permission grants, not user prompts — [Admin panel docs](https://www.librechat.ai/docs/configuration/admin_panel). No source found for a built-in LibreChat "who asked what" export or file/connector-use audit trail.

**Retention and deletion**
- LibreChat `interface.retentionMode`: `temporary` (default; only user-marked temporary chats expire), `all` (every chat expires, still visible until then), `ephemeral` (all chats temporary, toggle locked). `temporaryChatRetention` hours default 720, range 1–8760; `generalChatRetention` for `all`; `retainAgentFiles` — [LibreChat data retention](https://www.librechat.ai/docs/configuration/data_retention)
- Conversations/messages/shared links deleted by MongoDB TTL index on `expiredAt` (about a minute after deadline); files via periodic sweep; saving a conversation extends its deadline; memories never expire; mode changes are not retroactive — [LibreChat data retention](https://www.librechat.ai/docs/configuration/data_retention)
- LiteLLM spend-log retention is open source: `maximum_spend_logs_retention_period` (e.g. "7d"), interval, cron, size-based caps, partitioning; with none set nothing is deleted — [LiteLLM spend log deletion](https://docs.litellm.ai/docs/proxy/spend_logs_deletion)
- Set `disable_error_logs: True` (default writes LLM exceptions to DB) — [LiteLLM prod guide](https://docs.litellm.ai/docs/proxy/prod)

**Budgets and rate limits**
- Open source: virtual keys, users and teams, spend tracking, budgets and rate limits — [LiteLLM pricing](https://www.litellm.ai/pricing); [LiteLLM enterprise](https://docs.litellm.ai/docs/enterprise)
- Enterprise-gated: tag-based budgets, per-key per-model budgets, temporary budget increases, soft-budget email alerts, spend report generation, IP allow-lists, key rotation — [LiteLLM enterprise](https://docs.litellm.ai/docs/enterprise)

**Guardrails / PII**
- Open source: guardrails framework with custom guardrails and Presidio PII masking — [LiteLLM enterprise](https://docs.litellm.ai/docs/enterprise)
- Presidio needs separate Analyzer and Anonymizer containers (`PRESIDIO_ANALYZER_API_BASE`, `PRESIDIO_ANONYMIZER_API_BASE`); modes `pre_call`, `post_call`, `logging_only` (masks only what goes to logging callbacks, only `/chat/completions` success logging), `pre_mcp_call`; per-entity MASK or BLOCK — [LiteLLM Presidio docs](https://docs.litellm.ai/docs/proxy/guardrails/pii_masking_v2)
- Enterprise-gated: per-key/team guardrails; built-in `hide_secrets`, LLM Guard, LlamaGuard, OpenAI/Google moderation, Lakera and Aporia prompt-injection guardrails — [LiteLLM enterprise](https://docs.litellm.ai/docs/enterprise)

**Encryption**
- MongoDB native encryption at rest is Enterprise-only (WiredTiger); Community can use client-side field-level encryption — [MongoDB docs](https://www.mongodb.com/docs/current/core/security-encryption-at-rest/); [MongoDB forum](https://www.mongodb.com/community/forums/t/wiredtiger-storage-engine-to-use-apis-to-encrypt-decrypt-data-at-rest/185818)
- Caddy terminates TLS; no source fetched on Caddy automatic HTTPS (known from general knowledge; unverified here).

**Secrets management**
- LiteLLM master key must start `sk-`, store in a secret manager; `LITELLM_SALT_KEY` must be set before adding models and never changed (credentials become unreadable); `LITELLM_MODE="PRODUCTION"` disables `load_dotenv`; set `trusted_proxy_ranges` to the LB CIDR — [LiteLLM prod guide](https://docs.litellm.ai/docs/proxy/prod)
- LiteLLM integration with AWS/Azure/GCP/Vault secret managers is Enterprise — [LiteLLM enterprise](https://docs.litellm.ai/docs/enterprise)
- LibreChat requires persistent `JWT_SECRET`/`JWT_REFRESH_SECRET` (32+ bytes) — [LibreChat auth docs](https://www.librechat.ai/docs/configuration/authentication)

**Tenant isolation (LibreChat)**
- LibreChat now has tenant-related env options: `TENANT_ISOLATION_STRICT=true` (403 `TENANT_CONTEXT_REQUIRED` when tenant missing), `TRUST_TENANT_HEADER` (accept `X-Tenant-Id` pre-auth; disabled by default; only behind a reverse proxy that strips client values) — [LibreChat upgrade docs](https://www.librechat.ai/docs/configuration/upgrade); [dotenv ref](https://librechat.ai/docs/configuration/dotenv). Admin-panel docs say tenant-scoped callers cannot reach other tenants and admins are provisioned per tenant — [Admin panel docs](https://www.librechat.ai/docs/configuration/admin_panel). A third-party index claims FerretDB-backed database-per-org isolation; unverified — [docsearch index](https://docsearch.algolia.com/mcp/docs/repo/danny-avila/librechat).

**MCP connectors / prompt injection / egress**
- MCP SSRF: when `allowedDomains` is not configured, SSRF-prone (private) targets are blocked by default; `allowedDomains` is a strict whitelist (listing a private IP also blocks unlisted public destinations); `allowedAddresses` for private services; only list hostnames whose DNS you control — [LibreChat MCP settings (v0.8.7)](https://www.librechat.ai/v0.8.7/docs/configuration/librechat_yaml/object_structure/mcp_settings)
- CVE-2026-31951: user-created MCP servers could set arbitrary headers with credential placeholder substitution, enabling OpenID access-token theft; affects 0.8.2-rc1 to 0.8.3-rc1, fixed in 0.8.3-rc2 — [NVD](https://nvd.nist.gov/vuln/detail/cve-2026-31951); [Tenable](https://www.tenable.com/cve/CVE-2026-31951)
- CVE-2026-32625 (critical, 9.6): LibreChat exfiltrates server secrets via MCP server URL injection; I did not retrieve details or affected range — [Rapid7](https://www.rapid7.com/db/vulnerabilities/cve-2026-32625/)
- Nothing found in docs on prompt injection through MCP tool output; LiteLLM prompt-injection guardrails (Lakera/Aporia) are Enterprise per above.

**Supply chain**
- 2026-03-24: LiteLLM PyPI 1.82.7 and 1.82.8 backdoored (TeamPCP); safe ≤1.82.6; 1.82.8 used a `.pth` file executing on any Python start; credentials exfiltrated (SSH keys, cloud creds, k8s secrets, env vars); publishing token stolen via compromised Trivy action in CI; same actor hit Trivy (Mar 19) and Checkmarx KICS (Mar 23). Exposure window reported variously as ~10:39–16:00 UTC (Heise) vs quarantine ~13:38 UTC (Snyk) — sources differ — [Heise](https://heise.de/-11224139); [Snyk](https://snyk.io/articles/poisoned-security-scanner-backdooring-litellm); [JFrog](https://research.jfrog.com/post/litellm-compromised-teampcp/); [GitHub issue #24518](https://github.com/BerriAI/litellm/issues/24518)
- LiteLLM response ("CI/CD v2", 2026-03-30): isolated scan/test environments, separate validation and release repos, PyPI Trusted Publishing, immutable Docker tags (GHCR support planned), Cosign-signed GHCR images starting with `v1.83.0-nightly`; recommends verifying by commit hash, with pinned versions like `v1.83.0-stable` — [LiteLLM CI/CD v2](https://docs.litellm.ai/blog/ci-cd-v2-improvements)
- Practical note from the incident coverage: Docker image users of the official proxy image were reported differently across write-ups; I did not verify whether the Docker image (vs PyPI) was affected. See Gaps.

**Logging without storing chat content**
- Keep `store_prompts_in_spend_logs` off and set spend-log retention — [LiteLLM prod guide](https://docs.litellm.ai/docs/proxy/prod); Presidio `logging_only` masks before logging callbacks — [LiteLLM Presidio docs](https://docs.litellm.ai/docs/proxy/guardrails/pii_masking_v2); per-team logging opt-out is Enterprise — [LiteLLM enterprise](https://docs.litellm.ai/docs/enterprise). LibreChat stores chat content in MongoDB by design; `ephemeral` retention mode with short TTL is the closest to "not storing" — [LibreChat data retention](https://www.librechat.ai/docs/configuration/data_retention)

### Inferences
Suggested assessment matrix (my synthesis from the cited facts above):

| Control | Rating | Notes |
|---|---|---|
| OIDC SSO Google/Entra | Needs configuration | Native in LibreChat; test group-overage in Entra (many groups) |
| SAML | Needs configuration | Works but no SLO, no documented role mapping, exclusive with OIDC |
| Domain restriction, disable local signup | Needs configuration | `registration` allowed domains + `ALLOW_EMAIL_LOGIN=false`; note OIDC/SAML cannot disable auto-registration alone so use domain/required-role gating |
| Group-to-role mapping | Needs configuration (OIDC only) | `OPENID_REQUIRED_ROLE`/`OPENID_ADMIN_ROLE`; fine-grained per-group app roles via admin panel; SAML path unclear |
| SCIM | Needs custom code or third party | No LibreChat SCIM found; LiteLLM SCIM is Enterprise. Substitute: IdP-gated login + required group + offboarding runbook + periodic deactivation sync script |
| MFA | Delegate to IdP | Enforce in Google/Entra conditional access; local 2FA only for break-glass admin |
| RBAC/admin | Needs configuration | Admin panel is functional but young; AGPL-3.0 implication below |
| Audit log (who asked what) | Needs custom code | Mongo messages + LiteLLM spend logs with user/key attribution; ship to append-only store; LiteLLM audit log of admin actions needs Enterprise |
| Retention/deletion | Needs configuration | Strong native TTL; memories and backups are outside it; document backup retention |
| Budgets/rate limits | Needs configuration (native in LiteLLM OSS) | Tag budgets/temp increases need Enterprise |
| PII redaction | Needs configuration + extra containers | Presidio is OSS; per-team policies and Lakera-style injection detection are Enterprise |
| Encryption in transit | Needs configuration | Caddy TLS; internal Docker network, enable Mongo/Postgres TLS if on separate hosts |
| Encryption at rest | Needs configuration (disk) | Use LUKS/provider volume encryption; Mongo native is Enterprise |
| Secrets management | Needs configuration / third party | Docker secrets/SOPS/Vault OSS; LiteLLM's native secret-manager integration is Enterprise |
| Backups/DR | Needs configuration | Encrypted off-site dumps, restore tests; no source fetched, standard practice |
| Tenant isolation | Needs configuration (single-tenant) / immature (multi-tenant) | See Q3 |
| MCP egress control | Needs configuration + host firewall | Use `allowedDomains`, plus container egress proxy/firewall; prompt injection cannot be fully mitigated, only reduced by least privilege, read-only connectors, human confirmation |
| Vuln/supply chain | Needs configuration | Pin image digests, verify Cosign, Dependabot/Renovate, Trivy (note Trivy itself was compromised in March 2026, so pin its action by commit SHA), SBOM via Syft |
| Logging without content | Needs configuration | Feasible for LiteLLM; LibreChat content in Mongo remains unless `ephemeral` |
| Admin panel AGPL-3.0 | Legal consideration | AGPL-3.0 network-use clause: if you modify the panel and let users interact with it over a network, you must offer the modified source to those users. Running it unmodified internally imposes little obligation; keep it a separate service and avoid embedding its code in proprietary code. Get a lawyer check; this is general knowledge, not from a fetched source. The main LibreChat repo's license was not confirmed in this research (commonly cited as MIT; unverified here). |

### Gaps
- LibreChat SCIM: no evidence either way; check GitHub issues/discussions directly.
- Whether the official LiteLLM Docker image (not just PyPI) shipped the compromised versions; not verified.
- Official LibreChat page on group-to-role mapping beyond `OPENID_REQUIRED_ROLE`/`OPENID_ADMIN_ROLE`; Google `hd` enforcement not documented; Entra group-overage handling not documented.
- LibreChat main repo license and any file-use/tool-use audit logging features; LibreChat v0.8.9 "account protection" details were not retrievable.
- Details of CVE-2026-32625 (affected versions, fix) not retrieved; review the GitHub security advisories list for LibreChat and LiteLLM before pinning.
- PostgreSQL native encryption (no TDE in core) not verified from a source.
- Caddy specifics (automatic HTTPS, rate limiting, access logs) not researched.
- The LiteLLM audit-logs anchor page returned 404; details come from the enterprise overview only.

---

## Q2. Minimum credible "enterprise-grade" feature set for an SMB, and what is cheap vs expensive

### Takeaway
An SMB buyer typically needs: SSO with their IdP and enforced MFA, role separation, encryption, retention/deletion controls, EU data residency, a DPA with sub-processor list, and evidence of a vulnerability process. Most of that is cheap configuration; the expensive parts are audit trail with attribution, SCIM, formal attestation and (if LiteLLM Enterprise is required) license cost.

### Cited Findings
- LiteLLM positions its Enterprise tier toward teams with 100+ users or 10+ production AI use cases, trial 30 days — [LiteLLM enterprise](https://docs.litellm.ai/docs/enterprise). A tiny deployment is therefore below its target segment.
- LiteLLM SSO for the Admin UI is free for up to 5 users, a license is required above that — [LiteLLM enterprise](https://docs.litellm.ai/docs/enterprise). Note this concerns who logs into the LiteLLM admin UI, not end-user chat logins (those go through LibreChat).
- Vanta's EU bundle (ISO 27001 + GDPR) priced at $8k per a Vanta page cited in an EU-alternatives search — [Vanta EU bundle](https://www.vanta.com/products/expansion/eu-bundle)

### Inferences
- Cheap (days of work, no license): OIDC SSO via Google/Entra, disable local signup, domain restriction, IdP-enforced MFA, TTL retention, LiteLLM budgets/rate limits, Presidio, pinned image digests, disk encryption, Caddy TLS, security.txt, DPA template, sub-processor list.
- Moderate (weeks): attribution-grade audit log pipeline, restore-tested backups, egress allow-listing for MCP, SBOM/Trivy in CI, access-review process, incident-response and vendor-management policies.
- Expensive: SOC 2/ISO/ENS attestation (Q4), LiteLLM Enterprise license (price undisclosed), SCIM, 24/7 support, third-party pen-testing every year.
- Because LiteLLM admin-UI users are few (the two founders), the 5-user free SSO allowance probably covers the need. LiteLLM end users are LibreChat's service identity, so per-user budgets need LibreChat to pass user identity to LiteLLM (a custom-code or configuration step I did not verify from docs).

### Gaps
- No primary-source survey of what SMB buyers' security questionnaires require; the list above is my synthesis.
- Pricing for the minimum feature set has no verified single source.

---

## Q3. Single-tenant per customer vs multi-tenant: which is better for security claims, cost and data sovereignty

### Takeaway
For a two-person team, one stack per customer (or per small customer group) gives the cleanest isolation story and sovereignty claim, but costs operational overhead; LibreChat's multi-tenancy exists (strict isolation flag, tenant-scoped admins) but appears new and has little third-party validation, so a "shared tenant" claim would be harder to defend.

### Cited Findings
- LibreChat tenant isolation settings exist (`TENANT_ISOLATION_STRICT`, `TRUST_TENANT_HEADER`, `X-Tenant-Id` header handling) — [LibreChat upgrade docs](https://www.librechat.ai/docs/configuration/upgrade)
- Some LibreChat settings are process-wide and not per tenant, e.g., `ENFORCE_TWO_FACTOR_AUTHENTICATION` — [LibreChat auth docs](https://www.librechat.ai/docs/configuration/authentication)
- The first-account-becomes-admin behavior is described for single-tenant deployments — [LibreChat auth docs](https://www.librechat.ai/docs/configuration/authentication)
- LiteLLM Enterprise lists organizations/teams RBAC and team-based logging, per-team logging opt-out — [LiteLLM enterprise](https://docs.litellm.ai/docs/enterprise)
- The LiteLLM compromise stole environment variables and credentials from hosts — [JFrog](https://research.jfrog.com/post/litellm-compromised-teampcp/). Shared multi-tenant deployments concentrate every customer's provider keys in one blast radius.

### Inferences
- Per-customer stack (separate compose project, DBs, LiteLLM keys, provider API keys or per-customer virtual keys, separate encryption keys, separate region/VM): strongest blast-radius and deletion story ("terminate stack, destroy volume, certificate of deletion"), simple data residency (EU VM/hosting), easier customer-specific retention. Cost: more VMs (a small VM per customer), update fan-out, monitoring; mitigate with IaC (e.g., one compose template, Renovate, scripted rollouts). Practical for tens of customers, not hundreds.
- Multi-tenant: cheaper per customer and one upgrade path, but SOC 2/ISO auditors and buyer questionnaires will ask about logical isolation evidence, shared encryption keys, noisy-neighbour and cross-tenant tests; LibreChat's tenant features are recent and the Mongo/Postgres layers remain shared. Not recommended as the first security-selling posture for this team.
- Hybrid: pooled stack for small/trial customers with clear disclosure, dedicated stack for customers who require it, priced as a tier.

### Gaps
- No independent pen-test or audit evidence for LibreChat multi-tenancy found.
- No cost benchmarks (VM sizes, hosting) were researched.
- Spanish/EU "data sovereignty" legal framing (GDPR transfer rules, US-parent provider risk for LLM APIs) was not researched here; routing prompts to US LLM providers weakens the sovereignty story regardless of hosting.

---

## Q4. LiteLLM enterprise-gated features and license cost

### Takeaway
LiteLLM publishes no enterprise price. SSO (above 5 users), SCIM, JWT auth, audit logs, secret managers, key rotation, RBAC/org-team admin, per-key guardrails, tag/per-model budgets and IP allow-lists require the Enterprise `LITELLM_LICENSE`. Third-party estimates of around $30k/year are unofficial.

### Cited Findings
- Official pricing: Open Source $0 self-hosted; Enterprise "annual, sized to your usage", quoted by sales; SSO+SCIM, OIDC/JWT, audit logs, secret managers and key rotation, org/team admins, RBAC listed under Enterprise; air-gap available — [LiteLLM pricing](https://www.litellm.ai/pricing)
- Enterprise is one `LITELLM_LICENSE` key on the same gateway image; includes support channel and SOC 2 Type II report access via Trust Center; optional 24/7 SLAs; marketplace purchase via AWS/Azure available; free 30-day trial — [LiteLLM enterprise](https://docs.litellm.ai/docs/enterprise)
- Third-party figure: TrueFoundry (a competitor) cites about $30,000/year for an "Enterprise Premium" tier and about $250/month for a Basic tier, and notes LiteLLM does not publish prices — [TrueFoundry](https://www.truefoundry.com/blog/litellm-enterprise-pricing-tco-vs-truefoundry); also see [Activepieces](https://www.activepieces.com/blog/is-litellm-enterprise-pricing-worth-the-monthly-bill) (not opened). Treat as unverified and competitor-biased.
- Free in OSS: virtual keys, budgets and rate limits, spend tracking, Admin UI, load balancing, guardrails framework including Presidio, MCP gateway, spend-log retention — [LiteLLM enterprise](https://docs.litellm.ai/docs/enterprise); [Spend log deletion](https://docs.litellm.ai/docs/proxy/spend_logs_deletion)

### Inferences
- Team budgets and per-user budgets with rate limits are open source, so budget control does not force a license. Audit logs and SCIM do. For two founders on the admin UI, SSO is likely free (5-user allowance); a license becomes needed only if a customer demands LiteLLM-level audit logs, SCIM, or secret-manager integration.
- Alternative to paying: build the audit trail from LibreChat's Mongo records and LiteLLM spend logs, and put it behind your own export.

### Gaps
- Actual enterprise price: only obtainable via sales quote. The "Basic tier $250/month" and "$30k" numbers come from a competitor and were not corroborated.
- Whether the 5-user SSO allowance still stands in current releases (docs say so as of fetch date).

---

## Q5. Certification path and cost for a two-person startup (SOC 2, ISO 27001, ENS) and cheaper trust signals

### Takeaway
SOC 2 Type I is the fastest, cheapest attestation (months, low tens of thousands USD all-in); Type II needs a 3–12 month observation window. ISO 27001 is slower and costlier in year one but is the more recognised in EU; ENS Básico needs only a self-declaration, whereas Media requires accredited external certification and is relevant mainly for public-sector customers. Cheaper signals (security.txt, trust page, pen-test, DPA, sub-processor list, cyber insurance) can be delivered in weeks. All price figures are vendor-influenced and wide.

### Cited Findings

**SOC 2**
- Type I = controls designed at a point in time; Type II = controls operating over 3–12 months. Drata: Type I $7,500–$60,000, Type II $12,000–$100,000; SOC2Auditors.org: Type I $12K–$40K, Type II $15K–$75K, Big Four $60K–$450K. First-time Type II commonly 6–15 months; Type I about 3–6 months end to end including prep (Drata). About 70% of first-time pursuers go straight to Type II (Scrut) — [Drata](https://drata.com/learn/soc-2/type-1-vs-type-2); [SOC2Auditors](https://soc2auditors.org/insights/soc-2-type-1-vs-type-2/); [Scrut](https://www.scrut.io/soc-2/soc-2-type-1-vs-soc-2-type-2)
- One guide puts a lean startup's first Type I at $15,000–$40,000 total (auditor + platform + time); pen test add-on $5,000–$10,000 — [startupik / aggregator results](https://startupik.com/best-soc-2-compliance-software-startups/); [SOC2Auditors pricing](https://soc2auditors.org/insights/soc-2-software-pricing-comparison/)

**Compliance automation pricing (all unofficial except where noted)**
- Secureframe: entry from about $7,500/year (one source); Vendr median buyer about $20,000/year — [Vendr Secureframe](https://vendr.com/marketplace/secureframe)
- Vanta: no public pricing; estimates $10,000–$30,000/year for startups (March 2026) and $10,000–$250,000 observed overall — [SOC2Auditors Vanta](https://soc2auditors.org/insights/vanta-pricing/); [Tech Insider](https://tech-insider.org/vanta-vs-drata-vs-secureframe-2026/)
- Drata: quote-only; estimated $7,500–$100,000/year, Vendr median around $20,300 for the Advanced tier — [SOC2Auditors Drata](https://soc2auditors.org/insights/drata-pricing/)
- EU alternatives: Kertos (DE; ISO 27001, 27701, 42001, GDPR, NIS2, EU AI Act, SOC 2, TISAX, C5; EU hosting), Secfix (Munich; ISO 27001, NIS2, SOC 2), Kopexa (Kiel), DataGuard and heyData (Germany). Vanta EU bundle ISO 27001 + GDPR cited at $8k. None of the results mentioned ENS support or a Spanish vendor — [Kertos EU alternatives](https://www.kertos.io/en/compliance-hub/eu-alternatives-vanta-drata); [European Purpose](https://europeanpurpose.com/alternative-to/vanta)

**ISO 27001**
- Stage 1 (documentation) then Stage 2 (controls in operation), 4–8 weeks typically between stages; end-to-end timelines quoted 3–14 months or 9–18 months; certification audit alone about $8,000–$20,000 for 10–50 employee startups, or $3,500–$6,000 for 10–25 employees; year-one total $25,000–$90,000+ (one vendor) or $40,000–$180,000+ (another); surveillance audits at 60–70% of Stage 2 cost, recertification every three years — [heyData](https://heydata.eu/en/magazine/iso-27001-costs-2026-certification-sme); [Consilien](https://consilien.com/news/iso-27001-certification-cost-timeline); [Drata ISO audit cost](https://drata.com/learn/iso-27001/audit-cost)

**ENS (Esquema Nacional de Seguridad)**
- Categoría Básica: self-assessment leading to a Declaración de Conformidad; Media/Alta require external audit and certification issued by an ENAC-accredited body (AENOR, BSI, Applus, EQA, Bureau Veritas, OCA seen); a sample Media certificate is valid two years — [BSI ENS process PDF](https://www.bsigroup.com/siteassets/pdf/es-es/products-and-services/es-as-scert-govn-pp1926-proceso-de-certificacion-de-conformidad-con-el-esquema-nacional-de-seguridad-0026.pdf); [INCIBE sample certificate](https://www.incibe.es/sites/default/files/Certificado_RD_311_2022_ENS_MEDIA_INC.pdf); [Legiscope guide](https://www.legiscope.com/blog/esquema-nacional-seguridad-ens-guia.html)
- Cost for pymes: a consultancy guide gives EUR 8,000–25,000 (also EUR 8,000–60,000 elsewhere in the same guide) with audit being 30–50% of total; third-party, not official — [Legiscope guide](https://www.legiscope.com/blog/esquema-nacional-seguridad-ens-guia.html)
- Cloud guidance: CCN-STIC 823 covers applying ENS to cloud environments; the Spanish cloud strategy includes certifying cloud infrastructures; CCN-STIC 890 / 890C (µCeENS) is a lighter profile for basic-category systems — [Microsoft/CCN-CERT](https://news.microsoft.com/es-es/2019/12/12/microsoft-and-ccn-cert-take-a-giant-step-in-securing-cloud-environments-aimed-at-spanish-public-government-agencies/); [RedIRIS ENS certificate](https://rediris.es/rediris/certificaciones/CertificadoENS-2024-058A-1.pdf); [Estrategia Cloud AAPP](https://administracionelectronica.gob.es/pae_Home/va/dam/jcr:f9ceb19b-882b-4221-8476-10d59305ff10/2022_12_Estrategia_Cloud_AAPP.pdf)

**Cheaper trust signals**
- Sources fetched did not directly cover security.txt, cyber-insurance, DPA templates or trust-page tools. LiteLLM itself uses a Trust Center for its SOC 2 report access — [LiteLLM enterprise](https://docs.litellm.ai/docs/enterprise). An EU trust-center alternative to Vanta's is cited (Orbiq) — [Orbiq](https://www.orbiqhq.com/comparisons/vanta-trust-center-alternative).

### Inferences
- Realistic sequencing for two people: (1) weeks 0–6: trust page, security.txt (RFC 9116), DPA + sub-processor list, SSO/MFA/backups/pinning in place, written policies; (2) month 2–4: third-party pen test (about $5–10k per the cited aggregator, scale to scope) plus fix cycle; (3) SOC 2 Type I or ISO 27001 depending on buyer geography. If buyers are Spanish/EU SMBs, ISO 27001 plus a GDPR bundle (and, for public sector, ENS) likely matter more than SOC 2, which is primarily a US-buyer demand. If only ENS Básico is needed, self-declaration is cheap but carries weight only with Spanish public-sector-adjacent buyers.
- Budget order of magnitude for first year, using the cited ranges: SOC 2 Type I about USD 15–40k all-in; ISO 27001 about USD 25–60k with automation tooling and lean scope (lower end of cited ranges, my judgement); ENS Media EUR 8–25k for the certification body plus consultant (cited range is unofficial). Type II or ISO surveillance are recurring.
- A small, single-tenant, well-bounded scope (one product, few staff, cloud-hosted on an already-certified provider) shortens audits and cost; inherit controls from the hosting provider (several hyperscalers hold ENS certificates, e.g., [Google Cloud ENS](https://cloud.google.com/security/compliance/ens?hl=en), [AWS CCN-STIC](https://aws.amazon.com/compliance/ccn-stic)).

### Gaps
- No primary-source (AICPA, ISO, CCN) pricing; all cost data is vendor/aggregator content, some affiliate-style.
- ENS timeline for a pyme not found; ENS applicability to private SaaS vendors selling to public bodies (whether the supplier's system must be certified, and its category) not verified; CCN-STIC 879 search returned nothing.
- Cyber-insurance cost/requirements, security.txt, DPA template sources, pen-test pricing beyond one aggregator figure, and Spanish compliance-automation vendors were not found/researched.
- Vanta/Drata/Secureframe official pricing pages were not accessed; prices may differ for 2026 startup programs.
