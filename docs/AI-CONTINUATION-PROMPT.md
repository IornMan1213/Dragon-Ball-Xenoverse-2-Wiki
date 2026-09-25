[object Object]
### 2026-09-25 cycle completion — Skill Research Batch 337: Lightning Impact variant reconciliation
- [x] Inspected the live post-470/470 state and checked for a newer research batch before editing; no Batch 337 artifact existed.
- [x] Added `docs/data/skill-research-batches/skill-batch-337.json` for **Lightning Impact** internal-variant provenance.
- [x] Reconciled the Xenoverse 2 variant boundary: short ID **1100** is the CaC-usable/player variant, while short ID **1103** is a separate CaC-unusable/cast variant sharing the display name.
- [x] Preserved the canonical `skill-lightning-impact` identity and existing **PQ142 — Timespace Tussle** relationship; no duplicate canonical skill was created from the internal variant distinction.
- [x] Registered Batch 337 in `docs/data/pq-cross-domain-index.json` and advanced `docs/data/skill-catalog-audit.json` to **337**.
- [x] Preserved unresolved cast-variant acquisition, version-sensitive combat values, and presentation differentiation rather than inventing them.
- [ ] CI remains unverified; no workflow success is claimed.
- [ ] **Exact next:** continue the remaining current-facing cross-domain/variant provenance gaps or the next source-backed research target; preserve the 470/470 canonical boundary and avoid duplicate identities for internal variants.
