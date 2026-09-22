# 2026-09-22 — Gine accessory identity correction

## Correction

The previous continuation cycle incorrectly treated **Gine (DB Super)'s Accessory / pqacc-026** as lacking current canonical inventory evidence.

Live repository inspection shows that the maintained canonical equipment/accessory records already contain:

- `equip-050` — **Gine (DB Super) Set**
- category: `accessory`
- acquisition: PQ144

The PQ equipment crosslink independently maps PQ144 to `equip-050`, and the canonical equipment/accessory record layer contains the same identity.

## Important domain boundary

`equip-050` is a canonical equipment/accessory identity, but it is **not** an `acc-###` identity in the dedicated accessory identity layer. Therefore this cycle deliberately does **not** create a duplicate `acc-071` or any other speculative accessory ID.

The correct relationship is already represented by the canonical equipment graph. The dedicated `accessory-pq-canonical-bridge.json` should retain `canonical_id: null` for pqacc-026 if its schema is strictly restricted to `acc-###` IDs, but its unresolved explanation should be interpreted as **no dedicated acc-### identity**, not **no canonical inventory identity**.

## Evidence checked

- `docs/data/equipment-record-layer.json`
- `docs/data/equipment-accessories-record-layer.json`
- `docs/data/pq-equipment-crosslink-report.json`
- `docs/data/pq-reward-relationships.json`
- `docs/data/accessory-pq-canonical-bridge.json`
- `docs/data/accessory-pq-canonical-remaining.json`

The repository changelog also records that Gine (DB Super) Set was already added during the equipment/accessory detail batch.

## Changes this cycle

- Added `docs/data/accessory-gine-identity-correction-2026-09-22.json`.
- No duplicate canonical accessory identity was created.
- No existing canonical relationship was overwritten.

## Exact next task

1. Update the residual accessory backlog and related audit/report language so pqacc-026 distinguishes **domain-resolved via equip-050** from **unresolved dedicated acc-### identity**.
2. Recompute the accessory/PQ census with domain-aware accounting.
3. Then proceed to `pqacc-021` Resistance Helmet, checking whether it likewise already has a canonical equipment/accessory endpoint before creating any new `acc-###` identity.

## Validation boundary

Static GitHub inspection was used. No CI success is claimed.
