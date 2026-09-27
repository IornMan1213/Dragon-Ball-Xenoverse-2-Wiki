# Super Souls Research

This is the exhaustive research layer for Super Souls. It is intentionally separate from skills, QQ Bangs, and character records so acquisition provenance and conditional effects can be reconciled independently.

## Record standard

Each soul should eventually document its canonical name, source character, CaC/race restrictions, DLC provenance, acquisition method, exact source quest/shop/event, first-clear versus repeat behavior, shop rotation, trigger condition, effect magnitude, duration, stacking behavior, Limit Burst trigger/effect, version notes, verification state, and sources.

## Verification

- `indexed`: identity/source catalogued; mechanics incomplete.
- `partially_verified`: important identity/acquisition/effect facts checked; meaningful fields unresolved.
- `verified`: core identity, acquisition, effect, and key mechanics reconciled against sufficient evidence.

A `verified` record does not imply every community measurement has been reproduced.

## Acquisition families

Track these independently:

- Parallel Quests
- Expert Missions
- story and Extra Missions
- raids/events
- TP Medal Shop rotations
- mentor/instructor progression
- DLC content
- free updates
- other special sources

A DLC character's soul must not automatically inherit the character's DLC provenance as its acquisition source. The actual in-game source should be recorded.

## Effect model

Super Souls can be conditional. Records should preserve exact conditions involving health, Ki, stamina, transformations, Just Guards, damage, skill use, elapsed time, ally state, KO/revive state, quest score, and special events whenever evidence supports them.

Do not convert descriptive magnitude labels such as S/M/L/XL into percentages without independent evidence.

## Limit Burst

Limit Burst is a separate mechanic layer. Record its activation condition, effect, duration, and version-specific behavior independently from the ordinary passive effect.

## QQ Bang relationship

QQ Bangs and Super Souls are separate systems. QQ Bangs represent the clothing-stat override layer; Super Souls provide passive/conditional effects. Build pages may combine their effects, but canonical records must not merge their statistics.

## Research sources

The current research seed includes the Madreag Xenoverse 2 corpus, current secondary Super Soul references, and official publisher material for DLC/update provenance. Exact effects and acquisition details require individual reconciliation.

Machine-readable source: [`docs/data/super-souls-record-layer.json`](./data/super-souls-record-layer.json).

## Cross-system relationships

Super Souls connect to skills, Awoken Skills, QQ Bangs, equipment, characters, mentors, Parallel Quests, Expert Missions, raids, DLC/free updates, and combat/build mechanics. The eventual catalogue should let every soul resolve back to its acquisition source and forward to the mechanics it modifies.
