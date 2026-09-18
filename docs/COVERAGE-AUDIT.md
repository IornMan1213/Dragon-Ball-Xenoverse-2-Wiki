---
layout: wiki
title: Exhaustive Coverage Audit
---

# Exhaustive Coverage Audit

**Audit date:** 2026-09-18

This audit exists to prevent the project from confusing the existence of a wiki page, index, or seeded catalogue with exhaustive documentation.

## Current finding

The repository has strong research foundations for several systems, but multiple sections are still **framework-first rather than encyclopedia-complete**. The next phase must therefore prioritize missing records and missing fields, not merely new page polish or raw batch count.

## Priority matrix

| Area | Current state | Highest-value missing detail | Priority |
|---|---|---|---|
| GitHub Actions validation | Blocked by reported billing error; connector also shows pre-run failures with no steps/logs | Restore executable validation path | P0 |
| Skills | Large seeded/indexed catalogue plus hundreds of research batches | Reconcile research into canonical data; exact costs, acquisition, CaC restrictions, mechanics, UF conditions, version history | P1 |
| Parallel Quests | Structured audit now covers PQ1–PQ186 with known numbering gaps/conflicts preserved; skill cross-links are not yet fully reconciled | Resolve 168 remaining PQ skill-reward references against canonical skill identities; then deepen reward-slot, acquisition, unlock, DLC/version and cross-system provenance | P1 |
| Awoken/Transformations | Foundation exists in skill/index material, but broad exhaustive record coverage remains incomplete | CaC vs character-only, race/gender restrictions, resource costs, stages, prerequisites, effects, exceptions, version history | P1 |
| Expert Missions | 20-mission index and individual-record framework exist | Complete EM01–20 mechanics, phases, rewards, skill drops, first-clear/repeat distinction, version differences | P1/P2 |
| Super Souls | 18 canonical records plus staged research | Expand inventory and reconcile triggers, magnitudes, durations, stacking, Limit Burst, acquisition/rotation | P2 |
| Equipment | Catalog/index foundation and initial records exist | Individual clothing/accessory inventory, exact stats, slot/set relationships, costs, PQ/EM/raid provenance, version history | P2 |
| QQ Bangs | System/research foundation exists | Reproducible recipe families, observed six-stat outputs, materials, RNG/version behavior | P2 |
| Characters | No exhaustive structured layer was located during this audit | Playable/NPC identity, forms, restrictions, skills, mentors, PQ/EM/story appearances, DLC/version provenance | P2 |
| Story / Time Rifts / Conton City | Referenced by other systems but not yet treated as a complete structured dataset | Missions, unlocks, NPCs, rewards, progression gates, locations, version/DLC relationships | P2 |
| Shops / rewards | Acquisition taxonomy exists inside individual databases | Complete inventories, costs, rotations, progression requirements, availability/version history | P2 |
| Raids / events | Mentioned as acquisition sources | Event inventory, dates/recurrence, rewards, Super Souls/equipment/skills, historical availability | P2 |
| GitHub Pages / navigation | Site polish exists | Expose structured research status and coverage gaps without hiding incomplete data | P3 |

## Exhaustive record standard

A record should be considered complete only when the applicable fields have been researched or explicitly marked unknown.

### Acquisition

Record the actual route, not merely DLC ownership:

- story/progression prerequisite
- PQ/EM/raid/event source
- shop and exact cost when applicable
- NPC/mentor source
- mixing/recipe source
- first-clear versus repeat acquisition
- reward-slot or RNG semantics
- DLC/free-update provenance
- historical/current availability

### Gameplay

Where applicable:

- resource cost
- damage type
- charge/stage behavior
- hit count and follow-ups
- tracking
- status effects
- defensive properties
- combo interactions
- PvE/PvP behavior
- transformations/forms involved
- known version differences

### Restrictions

Preserve separately:

- CaC availability
- race restriction
- gender restriction
- character-only availability
- partner/customization requirements
- DLC ownership
- progression prerequisites

### Evidence

Every important nontrivial claim should retain:

- source URL/reference
- verification state
- uncertainty
- conflicting-source notes
- historical/version context where relevant

## Immediate research sequence

1. Keep GitHub Actions blocked as a billing/infrastructure issue; do not weaken validators.
2. Reconcile the canonical skill layer against research and perform the active second-pass metadata audit: exact costs, acquisition routes, CaC/race/gender restrictions, character-only variants, Ultimate Finish requirements, DLC/version provenance, and mechanics.

The PQ-to-skill cross-link audit is currently represented by the repository's latest persisted reconciliation report; the canonical skill files presently contain 294 records each, with ordering and canonical identities synchronized. Treat older 298-record milestone text below as historical unless refreshed by the latest report. Do not reopen the resolved frontier unless new evidence identifies a conflict.
3. Deepen the existing Parallel Quest layer by filling remaining reward/acquisition/version fields now that skill cross-links are reconciled.
4. Audit Awoken/Transformation records against the same exhaustive field standard.
5. Finish EM01–20 verification.
6. Expand Super Souls, Equipment, and QQ Bang records.
7. Establish structured Characters, Story/Time Rift, Shops/Rewards, and Raid/Event layers.
8. Only then use page/UI work to expose the growing data surface.

## Important rule

**A missing field is research work. A page containing a list is not proof of exhaustive coverage.**

Unknown values remain unknown until evidence is found. The audit must never be satisfied by filling gaps with inferred values.


## Skill metadata audit milestone — 2026-09-18

- [x] Corrected invalid `Power Up` class values by normalizing Power Up records to `Super / Power Up`.
- [x] Corrected several Evasive taxonomy/resource errors, including Spirit Explosion, Celestial Wave, Mighty Explosive Wave, and Instant Rise.
- [x] Separated CaC race restrictions from skill class/subcategory for race-restricted skills.
- [x] Corrected Darkness Rush (Melee/Ranged) to `Ultimate / Strike` while preserving their distinct race restrictions.
- [x] Verified the currently explicit `ultimate_finish_required: true` records have supporting PQ evidence for Time Control (PQ18) and Super Dragon Flight (PQ31).
- [ ] Continue auditing remaining canonical skills for costs, restrictions, acquisition semantics, Ultimate Finish requirements, DLC/version provenance, and mechanics.


### Evasive stamina-cost audit — 2026-09-18
- Completed a focused Evasive stamina-cost pass against available skill references.
- Canonical Evasive records now have populated stamina costs; the audit specifically corrected/confirmed documented 200–300 stamina values rather than inferring costs from class alone.
- Next: individually audit Super/Ultimate Ki-cost values, with special attention to charge/reinforcement/utility skills and historically changed costs.

### Super/Ultimate Ki-cost audit baseline — 2026-09-18
- Canonical catalog: 298 records.
- 0 Super/Ultimate records have a missing `ki_cost` value.
- 18 Super records currently use an explicit 0 Ki cost; these are predominantly charge, reinforcement, power-up, or utility skills and are retained as explicit values pending per-skill verification.
- Historical evidence shows costs can change between patches (for example, x10 Kamehameha changed from 100 to 200 Ki in a 2017 official Steam announcement), so class-based defaults are not acceptable.
