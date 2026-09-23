# Parallel Quest Cross-Domain Index

This layer turns the PQ database into a relationship graph rather than a flat quest list.

## Canonical scope

The current numbered PQ scope is **PQ 1-186**. Bandai Namco identifies Future Saga Chapter 4 as the final DLC and confirms that it adds new Parallel Quests; current player-facing references list PQ 185 and PQ 186. The older PQ36 numbering-gap claim is retained only as historical provenance and must not remove PQ36 from the current canonical range.

## Relationship graph

Every populated PQ record should eventually resolve these edges:

- `PQ -> Skill`
- `PQ -> Super Soul`
- `PQ -> Clothing / Accessory`
- `PQ -> Character / Enemy`
- `PQ -> DLC`
- `PQ -> Unlock Method`
- `PQ -> Farming Route`

The reverse indexes should then expose:

- `Skill -> PQs`
- `Super Soul -> PQs`
- `Equipment -> PQs`
- `Character -> PQs`
- `DLC -> PQs`

## Evidence policy

Reward relationships are only created when a source explicitly identifies the item as a reward. Character appearance alone is not evidence of a reward relationship. Farming relationships identify documented farming routes and do not imply guaranteed drops. Conflicting source values remain conflicts until reconciled.

## Current implementation

- `parallel-quests-canonical-index.json` defines the batch aggregation for PQ 1-186.
- `pq-reward-relationships.json` contains the normalized relationship set, including documented skill, Super Soul, equipment, character, DLC, and farming edges.
- `pq-cross-domain-schema.json` defines the machine-readable edge format.
- `pq-endpoint-identity-resolution-audit.json` records the current exact endpoint-resolution census across skills, Super Souls, equipment, characters, and DLC.

- `docs/data/pq-non-pq-cross-domain-audit-current-projection-correction-2026-09-23.json` records the latest deterministic current-projection correction for Super Soul 146/143 parity and 853 total-edge state.

## Current completion state and next gate

The canonical relationship layer is now the authoritative source for **853 unique PQ edges**: **244 skills, 145 Super Souls, 124 equipment, 247 character references, 86 DLC requirements, and 7 farming routes**. Canonical reverse/presentation projections have been reconciled for current endpoint integrity; the false PQ99 `Mr. Shape Up L` equipment endpoint has been removed while the underlying PQ reward evidence remains preserved. Two equipment naming conflicts and six DLC granularity mappings remain explicit bridge metadata rather than alternate canonical identities.

The next deterministic gate is **non-PQ consumer/navigation integrity**: audit remaining registered presentation and reverse-navigation consumers for stale relationship baselines, one-way navigation, scalar/list assumptions, and endpoint-name drift. This pass must not add relationship edges. Legacy display names, bundle-vs-pack granularity, or unresolved identity conflicts must remain explicitly classified rather than inferred.

Canonical relationship data remains authoritative. Normalized research maps, verification status, reverse indexes, and presentation bridges are projections/evidence layers and must never override canonical relationships.

- `docs/data/pq-non-pq-current-endpoint-census-correction-2026-09-23.json` records the current Super Soul endpoint-census correction (145 forward / 142 reverse) without rewriting dated historical snapshots.

- `docs/data/pq-non-pq-current-reconciliation-note-correction-2026-09-23.json` — current PQ relationship reconciliation wording corrected from stale 859 baseline/unresolved 151/148 discrepancy to live 853 / 145 / 142; historical values preserved.

- `docs/data/pq-current-state-consumer-census-2026-09-23.json` — bounded current-state consumer census; no remaining deterministic scalar/list/endpoint-count drift found; baseline 853 / 145 / 124 / 247 / 86 / 7, Super Soul reverse 142.
