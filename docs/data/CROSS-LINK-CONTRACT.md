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

### Canonical endpoint alias and granularity bridge

The file docs/data/pq-endpoint-alias-granularity-map.json is the deterministic presentation/identity bridge for known endpoint naming and DLC-granularity conflicts. It does not modify docs/data/pq-reward-relationships.json and must never be counted as additional canonical edges.

- Equipment name variants are explicit conflict records until inventory-level evidence establishes identity.
- Broad DLC pass/bundle labels may map to one or more individually canonical pack requirements; this is a granularity mapping, not an entity merge.
- One-to-many mappings must remain labeled as granularity and must not be converted into duplicate canonical relationships.
- Downstream pages may use this bridge to resolve navigation while retaining the canonical target identity and provenance.


### Shop endpoint implementation baseline — 2026-09-23

The skill acquisition shop layer now has stable canonical endpoint IDs in docs/data/skill-shop-endpoints.json:

- `shop-skill` — Skill Shop
- `shop-tp-stp-medal` — TP / STP Medal Shop

The layer currently projects **23 canonical skill edges** (**12 Skill Shop + 11 TP/STP Medal Shop**) with deterministic forward and reverse indexes. It is derived from skills.json acquisition classifications and does not manufacture alternate event/raid relationships from prose. Historical rotation and price evidence remains provenance, not proof of current availability.


### Time Rift / story / tournament endpoint implementation baseline — 2026-09-23

Added `docs/data/time-rift-story-tournament-endpoints.json` with **11 deterministic endpoints** and **13 forward skill edges**: four Time Rift progression endpoints, two story-mission endpoints, and five Conton City Tournament match endpoints. Match 5 legitimately maps to two skills. Tokipedia, Conton City Patrol, and the Ultra Instinct special-acquisition route are represented in their dedicated endpoint layers; the Ultra Instinct route is source-backed and remains separate from unrelated endpoint types.


### Expert Mission acquisition endpoint baseline — 2026-09-23
- `docs/data/expert-mission-endpoints.json` defines stable endpoint IDs `em-03` through `em-20` from the existing Expert Mission acquisition index.
- The layer currently yields **18 mission endpoints / 18 canonical skill edges / 0 unresolved reward-name gaps**.
- Unresolved names are retained as producer→consumer gaps; no fabricated skill IDs are allowed.
- `docs/data/expert-mission-endpoint-audit-2026-09-23.json` records structural validation and the unresolved set.


### Mentor endpoint baseline — 2026-09-23
- Added `docs/data/mentor-endpoints.json`: **33 mentor endpoints**, **132 lesson→skill edges**, **131 unique skill endpoints**, and **1 typed non-skill lesson reward** (Zamasu initiation Super Soul).
- Reverse lookup is included so skill records can navigate back to mentor/lesson producers.
- No unsupported skill ID is assigned to non-skill rewards; mentor roster count discrepancy remains separate.


### Tokipedia endpoint implementation baseline — 2026-09-23
- Added `docs/data/tokipedia-endpoints.json` with **4 deterministic Tokipedia completion endpoints** and **4 forward skill edges**: Confusion Blade (20%), Sneaky Strike (40%), Energy Minefield (75%), and Remote Serious Bomb (80%).
- Reverse lookup is included for skill→Tokipedia navigation.
- Reconciled Energy Minefield's stale `source_quest_or_shop` value from 60% to the evidence-backed 75% endpoint.
- Tokipedia completion thresholds are requirements, not inferred drop probabilities; unrelated Extra Story rewards are not promoted without explicit Tokipedia evidence.


### Conton City Patrol endpoint implementation baseline — 2026-09-23
- Added `docs/data/conton-city-patrol-endpoints.json` with **3 deterministic Patrol skill endpoints** and **3 forward skill edges**: Conton City Patrol 04 → Gigantic Cross, Patrol 10 → Saiyan Blaster, Patrol 17 → Gigantic Nova.
- Reverse skill→Patrol navigation is included.
- Patrol event endpoints remain separate from Broly mentor-training rewards; no duplicate route is collapsed without evidence.


## 2026-09-23 — Special acquisition endpoint baseline

The special acquisition endpoint layer in `docs/data/special-acquisition-endpoints.json` provides stable endpoint IDs for acquisition routes that are not PQ, mentor, Expert Mission, shop, Time Rift/story/tournament, Tokipedia, or Conton City Patrol records. It exposes forward endpoint→skill edges and reverse skill→endpoint navigation. Canonical `skills.json` remains authoritative; the endpoint layer must not invent unsupported acquisition conditions or duplicate canonical skill records.


## 2026-09-23 — Character-exclusive skill endpoint baseline

`docs/data/character-exclusive-skill-endpoints.json` exposes stable cast/boss character→skill edges for skills whose canonical records explicitly classify them as character-only. These are exposure/navigation edges, not acquisition edges. A character-exclusive endpoint must not imply CaC unlockability or a shop/quest route; canonical `skills.json` remains authoritative for acquisition and usability classification.


## 2026-09-23 — Full skill endpoint reverse parity baseline

The full current canonical skill layer now has endpoint coverage across the combined PQ and non-PQ producer/exposure layers: **469/469 canonical skill IDs are represented**. The audit is `docs/data/full-skill-endpoint-reverse-parity-audit-2026-09-23.json`. The current union is 469 canonical skill IDs after the 2026-09-24 Hyper/Ice endpoint reconciliation. A skill may have multiple legitimate producers; `skill-super-explosive-wave` is intentionally exposed through both Piccolo Lesson 1 and Future Gohan initiation. Duplicate identity creation is prohibited, while distinct producer relationships remain valid.


### 2026-09-24 — Cross-domain consumer baseline correction
- The live canonical PQ relationship baseline is **853 edges**: 244 skill, 145 Super Soul, 124 equipment, 247 character, 86 DLC, and 7 farming.
- Historical 854/146/143 and older 862/151/125/88 snapshots remain preserved as historical correction context and must not be used as current consumer counts.
- The full skill endpoint union is **469/469**, with zero uncovered canonical skill IDs after the Hyper Drain, Hyper Movement, Ice Cannon, and Ice Claw reconciliation.

### 2026-09-25 — Full skill endpoint parity current-baseline correction
- The current cross-domain consumer audit establishes **470 canonical skill IDs / 470 endpoint-union skill IDs / 0 uncovered IDs**.
- The current endpoint projection contains **239 PQ-linked unique skills** and **230 unique non-PQ endpoint targets**; these sets are not additive because legitimate multi-producer skills can occur in both domains.
- `docs/data/full-skill-endpoint-reverse-parity-audit-2026-09-23.json` has been synchronized to the current 470-record audit boundary. The older 469-record wording remains only in historical records where it documents the earlier state.
- No acquisition edge, endpoint identity, canonical skill identity, or historical snapshot was changed by this correction.
