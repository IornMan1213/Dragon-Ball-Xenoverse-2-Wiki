# Canonical Data Layer

This directory contains the machine-readable source of truth for the exhaustive Xenoverse 2 wiki.

## Principles

1. Enumeration and verification are separate states.
2. Source conflicts are retained instead of guessed away.
3. DLC is a relationship layer, not a duplicate content silo.
4. Variants are tracked separately from canonical identities when needed.
5. Every reward should resolve back to an acquisition source.
6. Missing records are tracked as gaps rather than silently omitted.

## Major contracts

- `wiki-coverage.json` — domain-level coverage state.
- `record-expansion-contract.json` — required fields across major databases.
- `completeness-rules.json` — non-negotiable audit rules.
- `source-priority.json` — source hierarchy.
- `cross-domain-relationship-types.json` — canonical relationship vocabulary.
- `audit-metrics.json` — eventual automated audit outputs.

## Population order

Skills → Characters → Parallel Quests → Super Souls → QQ Bangs → DLC relationships → Mentors → Expert Missions → Transformations → Mechanics → Equipment/shops → Story/Future Saga → remaining systems.
