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

The PQ-to-skill cross-link audit is now fully reconciled: 298 canonical skill records/index records, 205 linked PQ skill rewards, and 0 unresolved PQ skill references. Do not reopen the resolved frontier unless new evidence identifies a conflict.
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
- Corrected/confirmed documented costs including Dragon Burn (200), Absolute Zero (300), Angry Shout (300), and Mach Dash (200).
- The Fandom Evasive overview confirms Evasive stamina costs commonly range from 200–300 and independently lists these four values. citeturn0search4turn0search0turn0search1turn0search2turn0search3
- Remaining work: audit the Super/Ultimate Ki-cost fields individually; do not infer costs from class alone because variable, zero-cost, and nonstandard skills exist.


### Super/Ultimate Ki-cost audit frontier — 2026-09-18
- Canonical catalog currently contains 298 skill records; an inspection found 84 Super/Ultimate records with null Ki cost.
- These nulls are concentrated in older category-sourced records and therefore represent a metadata backlog, not evidence that the skills cost 0 Ki.
- Current research sources support that Super/Ultimate costs vary by individual skill, so costs must be verified per skill rather than inferred from class (for example, published references describe Super skills as spanning multiple Ki-bar costs). citeturn0search8turn0search3
- Next pass should resolve a small evidence-backed batch of these null costs, prioritizing records already linked to PQs or named individual skill pages; preserve null where authoritative evidence is unavailable.


### Super/Ultimate Ki-cost audit — 2026-09-18
- Corrected five well-supported Super Skill Ki-cost fields: Big Bang Kamehameha, Bending Kamehameha, Destructo-Disc, Galick Gun, and Kamehameha → 100 Ki.
- Web corroboration supports the 100-Ki values for Big Bang Kamehameha and Kamehameha, while community/reference material supports the 100-Ki baseline for Galick Gun. citeturn1search3turn1search6turn1search5
- The broader audit remains intentionally conservative: variable-cost, character-specific, charge-based, and defensive/utility skills are not normalized by class alone.


### Super/Ultimate Ki-cost audit — 2026-09-18
- Filled three previously missing Ultimate Ki-cost fields where current accessible references independently document the values: Dragon Fist = 500 Ki, Divine Lasso = 300 Ki, Final Kamehameha = 500 Ki. citeturn2search0turn2search3turn1search2turn1search3
- Kept the remaining missing costs unresolved rather than inferring them from skill class or common cost tiers; several skills have variable or nonstandard resource behavior.
- Fandom access was partially blocked by robots.txt during this pass, so community sources were used only where they explicitly stated the cost and the records remain subject to stronger-source verification.


### Super/Ultimate Ki-cost audit milestone — 2026-09-18
- Began the second-pass Ki-cost audit instead of inferring costs from skill class.
- Verified and populated five previously missing legacy costs: Divine Kamehameha (200), Death Ball (400), Final Explosion (500), Supernova (500), and Super Spirit Bomb (300).
- Divine Kamehameha's current skill page explicitly lists 200 Ki; community/reference material independently reports Super Spirit Bomb at 300 Ki and Death Ball at 400 Ki. citeturn1search0turn1search1turn1search11
- This pass intentionally leaves uncertain/variable skills unresolved rather than assigning a class-based default.


### Super/Ultimate Ki-cost audit milestone — 2026-09-18
- Began the Super/Ultimate Ki-cost second pass using explicit cost evidence rather than class-based assumptions.
- Filled four previously missing values: Perfect Shot (100 Ki), Spirit Bomb (100 Ki), Godly Display (500 Ki), and Emperor's Death Beam (400 Ki).
- Evidence includes historical Xenoverse 2 community documentation for Perfect Shot, Spirit Bomb, and Emperor's Death Beam, plus documented Godly Display 500-Ki usage; these are recorded as research evidence rather than universal class defaults. citeturn1search2turn2search8turn2search3turn2search4
- The remaining null Ki-cost fields stay intentionally unresolved until skill-specific evidence is available.


### Super/Ultimate Ki-cost audit — 2026-09-18
- Began a second-pass Ki-cost audit for canonical Super/Ultimate skills rather than applying class-wide defaults.
- Filled documented Super-skill costs for 34 unique skill names in the current catalog, including zero-cost charge/utility skills and 100-Ki attacks.
- External references confirm Energy Charge consumes no resources, while Instant Transmission is described as costing no Ki/Stamina; charge-skill references also identify the charge family separately from ordinary attacks. citeturn0search9turn0search2
- Remaining null-cost records require individual evidence review, especially newer DLC/Ultimate skills and skills whose costs may vary by stage or version.


### Super/Ultimate Ki-cost audit — 2026-09-18
- Verified and synchronized six researched costs: Crimson Edge 100, Divine Ray Bomb 300, Final Rampage 500, Dark Inscription 100, Emperor's Cannon 100, and Chaotic Time Impact 600.
- External references corroborate these values and the associated PQ acquisitions for the Future Saga skills. citeturn0search0turn0search1turn0search2turn0search3turn0search4turn0search7
- Continue auditing the remaining null Ki-cost records individually; null remains intentional where the available evidence describes variable/conditional costs or has not yet established an exact value.


### Super/Ultimate Ki-cost audit — 2026-09-18
- Audited the canonical Super/Ultimate resource fields rather than applying class-wide defaults.
- Corrected documented fixed costs for Divine Spear (200), Wild Stinger (100), God of Destruction's Plaything (100), God of Destruction's Poise (100 base; up to 300 with extension), Dragon Spark (100), Soaring Rush (100), Burst Blitz (300), Supreme Fury (100), Heat Wave (100), and Force Edge (100). The cited Xenoverse 2 references explicitly document several of these values; variable-cost skills remain represented as variable/null where the research source does not establish one fixed activation cost. citeturn1search0turn2search0turn2search1turn2search2turn2search10turn2search12
- Normalized documented zero-cost support/charge skills including Indomitable, Taunt, Do or Die, Justice Pose, Fighting Pose H, Divinity Unleashed, and Formation! to ki_cost 0.
- Remaining null costs are an explicit research queue, not assumed values: variable/extended-cost DAIMA/Pikkon ultimates and Burning Blast require individual source verification before promotion to a fixed number.
