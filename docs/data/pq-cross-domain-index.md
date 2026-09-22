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
- `pq-reward-relationships.json` contains the first normalized relationship set, including documented skill, equipment, Dragon Ball farming and DLC edges.
- `pq-cross-domain-schema.json` defines the machine-readable edge format.

## Current completion state and next gate

The canonical relationship layer is now the authoritative source for **860 unique PQ edges**: 244 skills, 151 Super Souls, 125 equipment, 247 character references, 86 DLC requirements, and 7 farming routes. Canonical reverse/presentation projections for skills, Super Souls, equipment/accessories, characters, DLC, and farming have been audited for endpoint integrity; aliases and granularity conflicts remain explicit presentation metadata rather than alternate canonical identities.

The next deterministic gate is **consumer/page navigation integrity**: audit direct PQ pages, catalog indexes, and cross-domain presentation consumers so each displayed relationship resolves back to the canonical PQ and target identity. This pass must not add relationship edges. Legacy display names, bundle-vs-pack granularity, or unresolved page references must remain explicitly classified rather than inferred.

Canonical relationship data remains authoritative. Normalized research maps, verification status, reverse indexes, and presentation bridges are projections/evidence layers and must never override canonical relationships.
