# 2026-09-22 — Domain-aware accessory reconciliation

## Completed

- Rechecked the live accessory residual backlog and canonical equipment/accessory layers.
- Confirmed Resistance Helmet (pqacc-021, PQ111) is already canonically represented as equip-135, category accessory.
- Confirmed Gine (DB Super)'s Accessory (pqacc-026, PQ144) is already canonically represented as equip-050, Gine (DB Super) Set, category accessory.
- Corrected docs/data/accessory-pq-canonical-remaining.json so both records distinguish absence of a dedicated acc-### identity from absence of a canonical inventory identity.
- Corrected the residual census to report 14 genuinely without a canonical inventory identity, with 2 additional research records domain-resolved through the canonical equip-### accessory namespace.
- Added and registered docs/data/accessory-domain-resolution-audit-2026-09-22.json.
- Registered the audit in docs/data/pq-cross-domain-index.json.
- Verified the edited residual backlog after write and removed a transient duplicate census field before finalizing.

## Validation

- Resistance Helmet: equip-135 appears in the canonical equipment record layer, equipment/accessory layer, and PQ111 equipment crosslink.
- Gine Set: equip-050 appears in the canonical equipment record layer, equipment/accessory layer, and PQ144 equipment crosslink.
- No new acc-### identity was invented.
- No existing canonical equipment relationship was overwritten.
- Domain-aware audit status: pass.

## Current interpretation

The dedicated accessory bridge intentionally remains acc-###-only. Its null canonical ID for these two records means no dedicated acc-### endpoint, not no canonical inventory endpoint. The canonical equipment graph supplies the actual inventory identity.

## Exact next task

Proceed through the remaining 14 research records with the same domain-aware check, prioritizing exact-name canonical equipment/accessory endpoints before considering any new acc-### identity. In particular, investigate Android 13's Hat, Android 14's Hat, Bardock (DB Super)'s Scouter, Kale's Accessory, and Caulifla's Accessory before the DAIMA-era records. Preserve set/component boundaries and never infer a canonical identity solely from a clothing or component label.

## Commits

- 418ee2135e2bf5f2a364796bbde1e0ff9ed6fdfa — domain-aware reconciliation audit
- a9d490fd217ea174f0608705085897bf751edd78 — registry update
- 33f015d783d671c408d5ed86d91a156c948d1191 — residual census correction
- 883de242363e74c5058a92e4a454aaff3143e5a5 — census field normalization

Static GitHub validation only; CI success is not claimed.
