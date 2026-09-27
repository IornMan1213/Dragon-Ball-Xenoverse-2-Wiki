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

## Next expansion order

1. Complete all skill reward edges across PQ 1-186.
2. Complete all Super Soul reward edges.
3. Complete all clothing/accessory reward edges.
4. Resolve Ultimate Finish/drop-slot attribution conflicts.
5. Add reverse indexes for every reward domain.
6. Link each reward to its canonical skill, Super Soul, equipment, character and DLC record.
