# Cross-Database Link Contract

**Status:** Active architectural contract  
**Last updated:** 2026-09-21

The wiki is intended to behave as a connected knowledge graph, not as a collection of isolated tables. Relationship data must be deterministic, evidence-backed, and traversable in both directions whenever both endpoints are represented in the repository.

## Core traversal requirement

The data layer must support:

**Parallel Quest → rewards/unlocks → Skill → mechanics/description → acquisition source → Parallel Quest**

The same pattern should be extended as evidence and canonical records become available:

- Parallel Quest ↔ Skills
- Parallel Quest ↔ Equipment / Accessories
- Parallel Quest ↔ Super Souls
- Mentor ↔ Skills
- Character ↔ Skills
- DLC ↔ Parallel Quests / Skills / Characters
- Shop ↔ obtainable records
- Raid/Event ↔ rewards
- Transformation/Awoken Skill ↔ prerequisites / related skills

## Identifier contract

Use stable canonical identifiers instead of display-name matching whenever an endpoint has a structured record identity.

| Entity | Canonical identity currently available | Link key policy |
| --- | --- | --- |
| Skill | New deterministic `id` field | `skill-{name-slug}`; collision suffix uses class/subcategory |
| Parallel Quest | Numeric quest number in research batches; `pq-{number:03d}` in record-layer contexts | Numeric PQ number is authoritative |
| Accessory | `acc-###` | Existing record-layer ID |
| Super Soul | `super-soul-###` | Existing record-layer ID |
| Mentor | `mentor-{slug}` | Existing record-layer ID |
| Character | Canonical character identity/name layer | Introduce stable character IDs before broad relationship population |
| DLC | Existing DLC datasets use their own identifiers where available | Do not invent IDs from prose |
| Shop / Event / Raid | Varies by dataset | Establish a stable ID before making it a relationship endpoint |

Skill IDs are generated from the canonical skill name and are validated against the same deterministic rule used by the producer. A correction that changes a skill's canonical name must therefore regenerate the destination ID rather than inherit the superseded ID.

## Relationship rules

1. **Bidirectional when possible.** If a PQ declares a skill reward, the skill-side acquisition data should identify that PQ.
2. **No name-only mass linking.** Display-name similarity is a discovery aid, not sufficient proof for a canonical relationship.
3. **Preserve uncertainty.** If a source suggests a relationship but does not establish it, keep it in research/provenance data rather than creating a false canonical edge.
4. **Aliases are explicit.** Known spelling/transcription variants belong in an alias map or relationship metadata; they must not create duplicate canonical entities.
5. **Numbering anomalies remain explicit.** PQ36 remains a current player-facing record while its historical cut-quest conflict is preserved.
6. **Relationship validators are audit tools, not data generators.** A missing endpoint is a research finding; validators must not silently invent the target.
7. **Cross-links must survive rebuilds.** Generated indexes and catalogs must derive relationship identifiers from canonical fields or explicit research records, not from transient UI text.
8. **Provenance stays attached.** Relationship evidence should retain the source URLs and verification status of the underlying claim.

## Current implementation baseline

The repository already contains a PQ → skill cross-link validator at `scripts/validate_pq_skill_links.py` and a generated `docs/data/pq-skill-crosslink-report.json`. The skill catalog now has deterministic IDs so future relationship reports can reference skills without relying on display names.

The next implementation stages are to:

1. add deterministic PQ IDs to the canonical PQ record layer;
2. make the PQ ↔ skill relationship report emit both forward and reverse indexes;
3. audit PQ ↔ equipment/accessory and PQ ↔ Super Soul relationships using the same contract;
4. establish stable character and DLC identifiers;
5. expand the relationship contract to mentors, shops, raids/events, and transformations;
6. expose these relationships to the search/UI layer only after the underlying edges are validated.

## Validation expectations

Every relationship batch should report:

- endpoint entity counts;
- forward edge count;
- reverse edge count;
- exact matches;
- explicit aliases;
- unresolved/orphaned endpoints;
- evidence status;
- source coverage;
- the exact files and records audited.

A successful validation means the relationship structure is internally consistent. It does **not** mean every real-world game relationship has been discovered.

