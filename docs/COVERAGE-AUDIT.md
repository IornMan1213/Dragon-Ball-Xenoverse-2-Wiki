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
- Corrected/confirmed documented costs including Dragon Burn (200), Absolute Zero (300), Angry Shout (300), and Mach Dash (200).
- Current canonical distribution across 20 Evasive records is 11 at 200 Stamina and 9 at 300 Stamina.
- Canonical and index skill layers remain synchronized after the pass.
- Remaining work: audit Super/Ultimate mechanics, acquisition routes, Ultimate Finish requirements, DLC/version provenance, and restrictions individually; do not infer Ki costs from class alone because variable and nonstandard costs exist.


### Super/Ultimate Ki-cost audit — 2026-09-18
- Audited the full canonical Super/Ultimate cost distribution (279 records with Ki costs present).
- Verified the nonstandard high-cost outliers against external references: Chaotic Time Impact = 600 Ki, Gigantic Explosion = 600 Ki, Power Rush = 1000 Ki, and Emperor's Death Beam = 400+ Ki.
- No blanket normalization was applied: 0, variable, 400, 600, and 1000-cost skills can be legitimate mechanics. The audit therefore preserves documented exceptions instead of forcing a 100/300/500 pattern.
- Next cost work should focus on historical/version-sensitive values and mechanics for individual records rather than class-wide inference.


### Super/Ultimate Ki-cost audit milestone — 2026-09-18
- Canonical audit found no missing Ki-cost values among Super/Ultimate records.
- Zero-cost Supers are concentrated in charge, teleportation, power-up, and utility skills; they are not being normalized to a generic cost.
- Power Rush remains the sole 1000-Ki canonical skill and is independently documented as requiring 1000 Ki.
- Burst Charge and Ultimate Charge retain 0 Ki and now include an additional Steam PQ134 source; independent GameFAQs/Steam evidence states their drops require the PQ134 Ultimate Finish, supporting the existing `ultimate_finish_required: true` flags.
- Web access to the Fandom Evasive pages was blocked by robots.txt during this pass, so blocked pages were not treated as verified evidence.


### Indomitable charge-behavior evidence — 2026-09-18
- Added a recent Steam community-testing source to the canonical/index Indomitable record.
- The source describes simultaneous Ki/Stamina charging and a health-sensitive acceleration below 50% HP; exact timing remains marked partially verified rather than promoted to a hard mechanic.
- Surging Spirit remains documented as a zero-Ki charge skill; current sources describe its charge rate improving with continued use and its CaC access through Ultra Instinct's built-in action.


### Ki-cost audit milestone — 2026-09-18
- Audited the canonical Super/Ultimate ki_cost field for null/missing values: none remain among those classes.
- Reviewed nonstandard costs rather than normalizing them to generic 100/300/500 values. Confirmed examples include Power Rush at 1000 Ki, Chaotic Time Impact at 600 Ki, Gigantic Breaker at 200 Ki, and Gigantic Explosion at 600 Ki.
- Preserved variable costs for Final Flash (SS3 DAIMA) as 400+ and Super Kamehameha (SS4 DAIMA) as 400-500, matching the documented base cost and optional extra-Ki behavior.
- Next: continue acquisition/unlock-route and Ultimate Finish verification; cost completeness is not evidence of complete skill metadata.


### Super/Ultimate Ki-cost field audit — 2026-09-18
- Audited the canonical 298-skill catalog for missing Ki costs on all `Super` and `Ultimate` records: **0 missing**.
- The 19 explicit zero-Ki Super records are concentrated in charge, reinforcement/power-up, teleport, and other utility skills; they were retained rather than normalized to a class-wide default.
- This matches the repository's evidence-first rule: cost must be researched per skill because Super/Ultimate categories contain exceptions and variable mechanics. External reference material likewise distinguishes ordinary Super/Ultimate cost bands while documenting special utility/charge behavior.
- Next cost pass: spot-check non-zero and high-cost values against primary/wiki/empirical sources, prioritizing records with `indexed` or `partially_verified` status and recent DLC provenance.


### Super/Ultimate Ki-cost audit — 2026-09-18
- Canonical Super and Ultimate records have no missing Ki-cost fields in the current 298-record catalog.
- Five nonstandard Ultimate costs were explicitly spot-checked rather than normalized: Chaotic Time Impact (600), Death Ball (400), Gigantic Explosion (600), S.S. Deadly Bomber (400), and Power Rush (1000).
- Current source evidence supports retaining these values; Power Rush is explicitly documented at 1000 Ki, while Death Ball is documented at 400 Ki and Gigantic Explosion at 600 Ki.
- No blanket class-based cost inference was applied. Remaining second-pass work is to verify acquisition routes, CaC/race restrictions, Ultimate Finish semantics, DLC/version provenance, and mechanics for the full Super/Ultimate catalog.


### Super/Ultimate Ki-cost audit — 2026-09-18
- Audited the canonical Super/Ultimate cost distribution rather than applying class-based defaults.
- No Super/Ultimate records currently have a missing Ki cost.
- Verified documented nonstandard Ultimate costs: Chaotic Time Impact = 600 Ki, Gigantic Explosion = 600 Ki, and Power Rush = 1000 Ki.
- Zero-Ki Super/Power Up entries are intentional charge/stance-style exceptions and remain unchanged; they should not be normalized to 100 Ki without move-specific evidence.
- Next cost pass should focus on conditional/variable resource mechanics (including stamina-on-hit/alternate-input costs) and acquisition/version metadata rather than bulk cost normalization.


### Super/Ultimate Ki-cost baseline — 2026-09-18
- Canonical skill audit found no Super or Ultimate records with missing/null Ki costs; all 298 canonical records have a populated cost field.
- This is a completeness check, not proof that every numeric value is correct. Variable-cost, zero-cost, and nonstandard mechanics still require source-level verification.
- Fandom was not accessible for direct verification during this pass because its robots policy blocked retrieval; no unsupported values were inferred from that source.


### Super/Ultimate Ki-cost audit checkpoint — 2026-09-18
- Canonical validation found **0 missing Ki-cost values** among Super and Ultimate records (298 total skill records).
- The 19 zero-Ki Super records are not being normalized away: the current evidence confirms that zero-cost skills can be legitimate. For example, Dimensional Hole is explicitly documented as a Ki Blast Super with **0 Ki**; community references also document Instant Transmission as zero-Ki.
- This pass therefore preserves explicit zero-cost values and avoids inferring costs from skill class alone.
- Remaining priority: spot-check non-zero Super/Ultimate costs against individual skill evidence, especially historical/version-sensitive skills whose costs have changed over time. Official Steam patch notes demonstrate that skill Ki costs can change between versions.


### Awoken activation-cost baseline audit — 2026-09-18
- Corrected the canonical Awoken activation-cost baselines for eight records where the prior value represented a highest-stage/legacy value rather than the documented entry threshold: Kaioken (100; stages 100/300/500), Super Saiyan (300; stages 300/400/500), Super Vegeta (300; stage 2 = 400), Super Saiyan God (300), Turn Golden (300), Purification (300), Become Giant (300), and Power Pole Pro (0).
- Updated `docs/data/awoken-skills.json`, `docs/data/skills.json`, and `docs/data/skills-index.json` together and retained the stage-specific values in notes rather than collapsing multi-stage forms to a single generic cost.
- Research source: Madreag's consolidated transformation research table, which records the per-stage thresholds and resource behavior.
- The audit remains partially verified: some transformation mechanics and acquisition/version details still require per-record evidence.


### Ki-cost audit — 2026-09-18
- Canonical Super/Ultimate records: 244.
- All Super/Ultimate records currently have a non-null `ki_cost`; no missing Ki-cost fields remain in the canonical layer.
- The 19 zero-Ki entries are concentrated in charge/reinforcement/power-up style skills and are retained as explicit data rather than normalized to a class-wide default.
- Variable/nonstandard cost values are also present, so future cost verification remains skill-specific.
- Web research corroborates that Xenoverse 2 has skill-specific and version-sensitive resource costs; official patch notes document individual Ki-cost changes, while community references describe distinct charge-skill behavior.
- Next: verify suspicious/nonstandard Super/Ultimate costs individually and audit Ultimate Finish, acquisition, DLC/version, and restriction metadata rather than inferring values from class.


### Ultimate Finish flag audit — 2026-09-18
- Reviewed the current canonical `ultimate_finish_required=true` set: 14 records.
- Current flags include both ordinary Super/charge skills and Ultimate skills; therefore the field must remain skill-specific rather than inferred from the class name.
- Web evidence independently confirms Ultimate Finish gating for Burst Rush, Formation!, Lovely Cyclone, Burst Stinger, Raid Blast, Blazing Attack, and the PQ134 charge-skill rewards.
- No flags were changed in this pass because the remaining records require individual quest/drop verification rather than broad normalization.
- Next: reconcile each flagged record to its exact PQ and drop condition, then inspect the null/false population for missed or explicitly non-UF cases.


### Super/Ultimate Ki-cost audit — 2026-09-18
- Rechecked all 298 canonical skill records after the Evasive pass.
- Every Super and Ultimate record currently has a non-null Ki-cost field; no blanket class-based cost inference was applied.
- Zero-Ki records were reviewed as intentional resource/support cases rather than automatically treated as missing data (charge skills and Power Up skills are expected examples).
- The next pass should target acquisition semantics, Ultimate Finish requirements, DLC/version provenance, and mechanics where the current record is only partially verified.


### Super/Ultimate resource-cost audit — 2026-09-18
- Canonical audit found **0 Super/Ultimate records with missing `ki_cost`** across the 298-record skill catalog.
- Nonstandard values were retained rather than normalized by class: charge/stance skills legitimately use 0 Ki, while documented Ultimate values include 200/300/400/500 Ki and therefore require skill-specific evidence.
- The current pass treats unusual values as audit candidates, not errors; the next pass should verify acquisition semantics and Ultimate Finish requirements for the remaining high-impact records.


### High-cost Ultimate provenance audit — 2026-09-18
- Audited the nonstandard high-cost Ultimate records: Chaotic Time Impact (600 Ki), Gigantic Explosion (600 Ki), Emperor's Death Beam (400+ Ki), and Power Rush (1000 Ki).
- Preserved their nonstandard costs rather than normalizing them to a generic 300/500 Ki rule.
- Enriched acquisition/mechanics provenance where source evidence was available, including PQ184/PQ164 reward context and TP Medal Shop acquisition for Emperor's Death Beam.
- The remaining Super/Ultimate cost audit should focus on version-sensitive variable-cost skills and historical cost changes rather than assuming class-based defaults.


### Ultimate Finish provenance audit — 2026-09-18
- Reconciled the current 14 canonical `ultimate_finish_required: true` records to explicit Parallel Quest numbers where the repository already had sufficient evidence.
- Added/normalized source quest IDs for Burst Rush (PQ51), Earth Splitting Galick Gun (PQ11), Time Control (PQ18), Burst Charge and Ultimate Charge (PQ134), Formation! (PQ133), Lovely Cyclone (PQ135), Burst Stinger/Raid Blast/Blazing Attack (PQ136), Chaotic Time Impact (PQ184), X 100 Big Bang Kamehameha (PQ100), Power Rush (PQ122), and Super Dragon Flight (PQ31).
- External corroboration includes explicit Ultimate Finish/drop statements for Burst Rush, Formation!, and the PQ135–137 DLC skill drops. citeturn2search0turn2search1turn2search2
- No true flags were converted to false/null: the goal is provenance completeness, not assuming that absence of a source equals absence of a requirement.
