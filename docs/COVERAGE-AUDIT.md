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


### Super/Ultimate Ki-cost audit — 2026-09-18
- Canonical audit found all 298 skill records populated with a Ki-cost field; no Super or Ultimate record currently has a missing/null Ki cost.
- This is a completeness milestone, not proof that every numeric cost is correct. Variable-cost, zero-cost, and version-specific skills still require evidence-level review.
- External Fandom searches were attempted for spot verification but were blocked by robots.txt in this environment, so no Fandom claim is treated as independently verified in this pass.
- Next metadata focus: spot-audit nonstandard/variable costs and Ultimate Finish requirements, then acquisition/version provenance.


### Super/Ultimate Ki-cost exception audit — 2026-09-18
- Audited the nonstandard/high Ki-cost entries rather than applying class-wide defaults.
- Confirmed Chaotic Time Impact = 600 Ki, Gigantic Explosion = 600 Ki, Thunder Flash = 300–600 Ki, and Emperor's Death Beam = 400+ Ki. These values are consistent with current Xenoverse 2 reference pages. citeturn0search3turn0search4turn0search0turn0search2
- No normalization was made where the variable-cost notation itself is meaningful.
- Next cost work should target ordinary Super/Ultimate records with weak provenance or mechanics uncertainty, not mechanically overwrite documented variable/600+ costs.


### Ki-cost audit — 2026-09-18
- Canonical Super/Ultimate records were scanned for missing Ki costs: **0 missing** across the current catalog.
- A second pass identified six nonstandard Ultimate costs (400/600 Ki) rather than treating the common 300/500 values as universal defaults: Chaotic Time Impact (600), Death Ball (400), Final Flash (SS3 DAIMA) (400), Gigantic Explosion (600), S.S. Deadly Bomber (400), and Super Kamehameha (SS4 DAIMA) (400).
- External corroboration supports the nonstandard-cost principle and specifically documents Death Ball at 400 Ki and Gigantic Explosion at 600 Ki; older GameFAQs/Steam/community material also documents other 400/500-cost Ultimate variants. citeturn1search0turn1reddit36turn1search8
- These values are retained pending skill-specific authoritative/version-aware verification rather than normalized away.


### Ki-cost completeness checkpoint — 2026-09-18
- Canonical audit confirms all 298 current skill records have a populated `ki_cost` field where the schema expects it; no Super/Ultimate records are missing Ki cost.
- Zero-Ki entries are concentrated in charge, teleport/utility, and Power Up records and are therefore retained pending individual mechanics verification rather than normalized to a default cost.
- Next pass should target the semantics behind non-zero Super/Ultimate costs, especially variable-cost and version-specific skills, plus Ultimate Finish evidence.


### Super/Ultimate Ki-cost audit milestone — 2026-09-18
- Canonical audit found **no missing Ki-cost values** among Super or Ultimate records (298 total skill records checked).
- Nonstandard costs are present and must remain evidence-driven: Super records include 200/300 Ki entries, while Ultimate records include 200, 300, 400, 500, 600, and variable-range costs.
- Spot-check research supports retaining non-100/300 values rather than normalizing by class: Xenoverse 2 references document chargeable/extended skills whose base cost differs from their maximum spend, and community/research sources document 200-Ki supers such as x10 Kamehameha. citeturn1search5turn1search12
- Next skill pass should target **acquisition semantics, Ultimate Finish requirements, CaC/race restrictions, DLC/version provenance, and mechanics**, not blanket Ki-cost normalization.


### Super/Ultimate resource-cost audit — 2026-09-18
- Canonical audit confirms all 298 records in the current catalog have an explicit Ki-cost field when classified as Super or Ultimate; there are no null/missing Ki costs in those classes.
- Zero-Ki Super records were reviewed as a special case rather than treated as missing data. They include charge/support/power-up skills and therefore require semantic verification rather than blanket normalization.
- Research sources distinguish ordinary Ki costs from charge/support mechanics and document examples such as 1-bar Supers and 3–5-bar Awoken costs; these sources are useful corroboration but are not sufficient to overwrite individual canonical values without skill-specific evidence. citeturn0search0turn0search1
- Next metadata frontier: verify the zero-cost special cases individually, then audit Ultimate Finish semantics and acquisition/version provenance.


### Super/Ultimate Ki-cost completeness audit — 2026-09-18
- Canonical catalog check: all 278 Super/Ultimate records currently have a non-null `ki_cost`; no missing Ki-cost fields remain in those two classes.
- Nonstandard documented values were preserved rather than normalized away: Chaotic Time Impact (600), Death Ball (400), Emperor's Death Beam (400+), Final Flash (SS3 DAIMA) (400), Gigantic Explosion (600), S.S. Deadly Bomber (400), Super Kamehameha (SS4 DAIMA) (400), and Thunder Flash (300–600).
- This pass confirms field completeness, not universal mechanic correctness; exact costs, charge behavior, and version-specific changes remain candidates for evidence-level review.


### Super/Ultimate Ki-cost audit — 2026-09-18
- Canonical audit found no missing Ki-cost fields among the 298 skill records: all Super and Ultimate records have a populated `ki_cost` value.
- Nonstandard values were reviewed rather than normalized by class: charge/recovery and support Supers legitimately use 0 Ki; Emperor's Death Beam is variable (`400+`); Thunder Flash is variable (`300-600`); Chaotic Time Impact and Gigantic Explosion are 600 Ki.
- Current web evidence independently supports these exceptions and the 600-Ki values. citeturn1search1turn1search2turn1search3turn1search4
- This closes the missing-cost portion of the Super/Ultimate pass; the remaining metadata audit should focus on acquisition semantics, race/gender restrictions, character-only availability, Ultimate Finish requirements, DLC/version provenance, and mechanics.


### Super/Ultimate Ki-cost audit — 2026-09-18
- Canonical audit found no null Ki-cost fields among Super or Ultimate records.
- A targeted 400-Ki review verified Death Ball and S.S. Deadly Bomber at 400 Ki, while the DAIMA Final Flash and Super Kamehameha variants require a 400-Ki base and have additional Ki-dump behavior. citeturn1search0turn1search1turn1search2turn1search3
- The canonical ki_cost field remains the base activation cost; variable/additional consumption is documented in mechanics rather than flattened into a misleading fixed number.
- Next: audit Ultimate Finish requirements and acquisition semantics, especially where PQ reward evidence distinguishes normal drops from Ultimate Finish-only rewards.


### Ultimate Finish provenance audit — 2026-09-18
- Re-audited the canonical records currently marked `ultimate_finish_required: true`; the live catalog contains 15 such records, not the earlier five-record snapshot.
- Independent PQ evidence supports Ultimate Finish gating for Burst Charge and Ultimate Charge on PQ134 and Formation! on PQ133. citeturn2search0turn2search1turn2search8
- These flags are being treated as evidence-backed acquisition requirements, not as a generic property of all PQ rewards. Remaining true flags require individual quest-level verification.


### Super/Ultimate Ki-cost audit — 2026-09-18
- Canonical audit found **no Super or Ultimate records with a missing Ki-cost field**.
- A zero-cost review found the zero-cost set is concentrated in charge, reinforcement/power-up, and utility skills; these should not be normalized to generic 100/300 Ki values.
- External research confirms charge-skill behavior varies by skill and that Fighting Pose K/Meditation interactions have changed across game versions, reinforcing the need to preserve individual metadata rather than infer costs from class. citeturn0reddit27turn0search1
- Next cost pass should focus on nonzero values that are potentially stale, especially DLC/Future Saga skills and skills with version-sensitive mechanics.


### Ultimate cost/mechanics spot-audit — 2026-09-18
- Verified the two 600-Ki Ultimate records in the current canonical layer: **Chaotic Time Impact** (PQ184) and **Gigantic Explosion** (PQ164). Fandom's Ultimate Attack index and per-skill pages explicitly report 600 Ki for both. citeturn1search0turn1search1turn1search2
- Refined their canonical mechanics notes to preserve the Awoken requirement/400-Stamina continuation behavior of Gigantic Explosion and the Power of Time scaling/reset behavior of Chaotic Time Impact.
- The canonical catalog currently has no null Ki cost among Super/Ultimate records and no null stamina cost among Evasive records; this is a field-completeness milestone, not proof that every individual value is fully independently verified.


### Super/Ultimate Ki-cost audit — 2026-09-18
- Audited all 298 canonical skill records for missing Ki costs: **0 Super/Ultimate records are missing a Ki-cost field**.
- Found 19 documented zero-Ki Super/Ultimate entries; these are charge/power-up/utility skills and were retained rather than normalized to a guessed positive cost.
- Two records use variable/string cost notation rather than a scalar: Emperor's Death Beam (`400+`) and Thunder Flash (`300-600`). These values were preserved because replacing them with a single number would discard documented mechanics.
- No canonical identity duplicates were found; the canonical and index layers remain synchronized.
- Research limitation: Fandom pages were not accessible in the latest web pass because robots.txt blocked retrieval, so no unsupported cost corrections were made.


### Super/Ultimate Ki-cost audit — 2026-09-18
- Audited the catalog for missing and nonstandard Ki-cost values; no Super/Ultimate record currently has a null Ki cost.
- Verified the four nonstandard values rather than normalizing them to generic 100/300/500 assumptions: Chaotic Time Impact = 600 Ki, Gigantic Explosion = 600 Ki, Emperor's Death Beam = 400+ Ki, and Thunder Flash = 300–600 Ki. citeturn1search3turn1search4turn1search0turn1search1
- This preserves variable/extended-cost mechanics as data, rather than treating the displayed starting cost as the entire resource requirement.
- Next metadata frontier: audit Ultimate Finish requirements and acquisition semantics, then DLC/version provenance and mechanics for remaining canonical skills.


### Super/Ultimate Ki-cost audit — 2026-09-18
- Audited all 298 canonical skill records for missing Ki costs: **0 Super/Ultimate records are missing a Ki-cost value**.
- Current distribution is 19 at 0, 154 at 100, 6 at 200, 44 at 300, 4 at 400, 14 at 500, 2 at 600, plus explicitly variable/ongoing costs represented as `400+` (Emperor's Death Beam) and `300-600` (Thunder Flash).
- The nonstandard high-cost entries were retained rather than normalized to a generic 300/500-bar assumption. External research independently documents 600-Ki costs for Chaotic Time Impact and Gigantic Explosion, and variable costs for Thunder Flash/Emperor's Death Beam. citeturn0search0turn0search13
- This closes the **missing Ki-cost field** portion of the second-pass skill metadata audit; exact acquisition/version/Ultimate-Finish/mechanics verification remains active.


### Super/Ultimate resource-cost baseline — 2026-09-18
- Canonical audit confirms all current Super and Ultimate records have a non-null `ki_cost`; no blank Ki-cost fields remain in the 298-record catalog.
- This is a completeness baseline, not proof that every numeric cost is correct. Variable, zero-cost, and version-specific mechanics still require record-level evidence.
- External Fandom pages were not accessible during this pass because robots.txt blocked retrieval, so no unsupported numeric corrections were made from that source.
- Next cost pass should sample documented numeric values against accessible primary/secondary references and prioritize unusual costs, variable-cost attacks, and character/DLC-specific variants.


### Super/Ultimate Ki-cost completeness audit — 2026-09-18
- Audited all 298 canonical skill records in the current skills.json layer for missing Ki costs across Super and Ultimate classes.
- Result: **0 missing Ki-cost fields**. This is a completeness milestone, not proof that every numeric value is correct.
- Explicit zero-cost records were reviewed as a separate class of data because charge/reinforcement/stance skills can legitimately have 0 Ki. They remain preserved rather than normalized to a generic Super cost.
- External research confirms that Xenoverse 2 has distinct resource models and that skill costs vary by move; therefore costs must continue to be verified individually rather than inferred from class alone.
- Next cost pass: verify suspicious/nonstandard numeric values and variable-cost mechanics, then audit acquisition routes and Ultimate Finish requirements.


### Super/Ultimate Ki-cost audit — 2026-09-18
- Audited all canonical Super and Ultimate records for missing, malformed, or nonstandard Ki-cost values.
- No Super/Ultimate records have a missing Ki-cost field.
- Eight nonstandard values were retained rather than normalized: Chaotic Time Impact (600), Death Ball (400), Emperor's Death Beam (400+), Final Flash (SS3 DAIMA) (400), Gigantic Explosion (600), S.S. Deadly Bomber (400), Super Kamehameha (SS4 DAIMA) (400), and Thunder Flash (300–600). These require individual source-backed verification rather than class-based assumptions.
- Current web lookup of the Fandom source was blocked by robots.txt, so this pass did not overwrite those values without accessible corroboration.


### Power Up description cleanup — 2026-09-18
- Corrected five canonical Power Up skill descriptions that duplicated the taxonomy label (for example, “Power Up Power Up”) into normal skill descriptions.
- Affected records: Divinity Unleashed, Fighting Pose H, Justice Pose, Taunt, and Formation!.
- This is presentation/data-quality cleanup only; no resource cost or gameplay value was inferred from the wording.


### Resource-cost and Ultimate-Finish provenance pass — 2026-09-18
- Audited all 298 canonical Super/Ultimate records for missing Ki-cost values: **0 missing**.
- Zero-Ki entries were retained where the skill is a charge/buff/pose/utility action rather than forcing a class-based default cost. For example, Dimensional Hole and Fighting Pose K are explicitly documented at 0 Ki. citeturn1search1turn1search0
- Confirmed the existing `ultimate_finish_required: true` state for Burst Charge: PQ134 sources describe Burst Charge/Ultimate Charge as Ultimate Finish rewards. citeturn2search0turn2search12
- Confirmed the existing Ultimate Finish requirement for Formation! from PQ133 documentation. citeturn2search3
- Do not normalize remaining costs by class; variable/zero-cost mechanics require skill-specific evidence.


### Super/Ultimate Ki-cost audit — 2026-09-18
- Canonical Super/Ultimate records have no null Ki-cost fields.
- Targeted source verification corrected **Power Rush** from 500 to **1000 Ki**; current reference material identifies it as the game's mandatory 1000-Ki attack. citeturn0search2turn0search8
- **Special Beam Cannon (Beast)** remains **500 Ki**, independently documented by the skill reference. citeturn0search0turn0search1
- Future passes should continue spot-checking nonstandard/variable costs rather than applying class-wide defaults.
