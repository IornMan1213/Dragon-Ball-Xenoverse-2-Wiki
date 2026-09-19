---
layout: wiki
title: Exhaustive Coverage Audit
---

# Exhaustive Coverage Audit

**Audit date:** 2026-09-19

This audit exists to prevent the project from confusing the existence of a wiki page, index, or seeded catalogue with exhaustive documentation.

## 2026-09-19 live PQ unlock census correction

Live repository census: 176 canonical PQ records, 176 unique numbers, 0 duplicates, and 0 records missing an explicit `unlock_condition` field. PQ36, PQ53–55, PQ131–140, and PQ151–160 now all have explicit unlock metadata. This field census does not make every route exact: PQ54 retains conflicting community evidence, PQ36 retains the known numbering/existence anomaly, and some DLC-era entries intentionally retain bounded DLC-ownership + PQ-board wording where an individual prerequisite was not independently established.

Historical cycle counts below remain unchanged for provenance; this section is the current live census.

## Current finding

The repository has strong research foundations for several systems, but multiple sections are still **framework-first rather than encyclopedia-complete**. Unlock-field presence must not be mistaken for exact unlock-route verification: several PQ batches use explicitly bounded wording where sources establish placement/objectives but not the individual trigger. The next phase must therefore prioritize missing records and missing fields, not merely new page polish or raw batch count.

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


## Parallel Quest provenance pass — 2026-09-19

- Completed a record-level provenance pass for **PQ1–PQ10**.
- All 10 records now carry explicit source URLs in their individual records, rather than relying only on the batch-level source list.
- Sources used for the pass: the maintained 186-PQ Steam transcription, the Steam PQ reward transcription, and an independent Ultimate Finish reference.
- The pass deliberately did **not** add reward-slot percentages or other probability claims where the consulted sources do not establish them.
- Remaining provenance work: older PQ batches still contain records without individual `sources` arrays; continue in bounded batches and preserve unresolved reward semantics. The PQ11–PQ20 provenance pass is complete.

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
- External corroboration includes explicit Ultimate Finish/drop statements for Burst Rush, Formation!, and the PQ135–137 DLC skill drops.
- No true flags were converted to false/null: the goal is provenance completeness, not assuming that absence of a source equals absence of a requirement.


### High-cost Ultimate Ki audit — 2026-09-18
- Verified three nonstandard Ultimate Ki costs against external references rather than normalizing them to a generic 300/500 pattern:
  - Chaotic Time Impact — 600 Ki; PQ184 and Ultimate Finish reward evidence are consistent.
  - Gigantic Explosion — 600 Ki, with an additional 400 Stamina expenditure to continue while taking damage.
  - Power Rush — 1000 Ki (10 bars), independently documented by contemporary player testing and reference material.
- No cost normalization was performed because the canonical values already match the evidence.
- This pass confirms that remaining resource-cost work must be skill-specific, including variable-cost attacks and conditional Stamina expenditures.


### Super/Ultimate Ki-cost completeness audit — 2026-09-18
- Canonical catalog now has no missing `ki_cost` values among Super or Ultimate skills (298/298 records remain indexed).
- Nonstandard documented costs were retained rather than normalized away: Chaotic Time Impact 600, Gigantic Explosion 600, Power Rush 1000, Emperor's Death Beam 400+, Final Flash (SS3 DAIMA) 400+, and Super Kamehameha (SS4 DAIMA) 400–500.
- This confirms the next cost pass should focus on **evidence quality and semantics** (variable/charge-based costs and version/DLC context), not filling nulls with class defaults.


### Ki-cost taxonomy correction — 2026-09-18
- Corrected **Gigantic Breaker** from `Ultimate / Ki Blast` to `Super / Ki Blast`; authoritative indexed skill data identifies it as a Super Attack and documents a 200 Ki cost.
- Preserved its 200 Ki cost; this is an example of why the audit does not infer cost solely from broad attack families.
- Confirmed several intentionally nonstandard Ultimate costs during this pass: Chaotic Time Impact (600), Gigantic Explosion (600), Power Rush (1000), Death Ball (400), S.S. Deadly Bomber (400), and the DAIMA Ultimates' variable 400+ / 400–500 costs.


### Skill acquisition-route audit — 2026-09-18
- Researched and enriched acquisition metadata for 11 canonical skills where the unlock route had been missing: Big Bang Knuckle (PQ172), Burning Slash (PQ44), Deadly Dance (Android 18 training), Evil Flight Strike (PQ21), Namek Finger (TP Medal Shop / Namekian Future Warrior), Pressure Sign (Conton City Skill Shop), Shining Slash (PQ38), Darkness Rush (Melee/Ranged) (Lord Slug training, Lesson 3), Dragon Fist (TP Medal Shop), and Godly Display (TP Medal Shop, 500 TP Medals). Sources include the Xenoverse 2 Fandom skill pages and corroborating Dragon Ball Wiki/GameFAQs/Steam material.
- Preserved uncertainty for Dragon Thunder and Death Ball rather than inventing acquisition routes.
- Canonical/index synchronization remains the validation gate; future passes should continue filling acquisition semantics only when evidence is explicit.


### Ki-cost audit — 2026-09-18
- Canonical Super and Ultimate records were checked for missing Ki-cost fields: **0 missing** across the current catalog.
- The audit also flagged that nonstandard costs exist and therefore must be researched individually rather than normalized by class: current canonical Ultimates include 400-Ki entries (Death Ball and S.S. Deadly Bomber), while authoritative skill references also document variable costs such as 300+ or 400+.
- Next pass should focus on suspicious/nonstandard costs and acquisition/version provenance, rather than filling nulls.


### Super/Ultimate Ki-cost audit — 2026-09-18
- Canonical audit found **0 missing Ki-cost values** across all Super and Ultimate records (298 total skill records overall).
- The remaining zero-Ki entries are concentrated in charge/reinforcement/utility skills plus Dimensional Hole and Indomitable; Dimensional Hole is explicitly documented as 0 Ki in the current Fandom skill page.
- No blanket class-based cost normalization was applied; variable/nonstandard costs require per-skill evidence.
- Next cost pass should focus on sampled nonzero Super/Ultimate values and version/DLC changes rather than filling nulls.


### Super/Ultimate Ki-cost audit — 2026-09-18
- Audited all 298 canonical skill records for missing or structurally invalid Ki costs on Super and Ultimate skills.
- Result: **0 missing Ki-cost fields**, **0 negative/out-of-range values**, and canonical/index Ki-cost values are synchronized.
- The 19 zero-cost Super/Ultimate entries are charge/reinforcement/utility-style skills or other explicitly non-spending mechanics; they were preserved rather than forcing a class-based default.
- Nonstandard costs (including variable/threshold-style entries) remain explicitly represented where the data model supports them; no blanket 100/300/500 replacement was applied.
- External research corroborates the game's use of distinct 100/300/500 Ki thresholds and nonstandard transformation/resource models, while individual skill costs still require skill-specific evidence.
- Next metadata frontier: audit **Ultimate Finish requirements and acquisition semantics** for remaining canonical Super/Ultimate skills, then reconcile DLC/version provenance and mechanics notes.

### Super/Ultimate Ki-cost audit — 2026-09-18
- Audited all 298 canonical skill records for missing Ki costs in the Super/Ultimate classes: none are null or empty.
- Reviewed the nonstandard numeric Ultimate costs (400, 600, and 1000) and variable-cost representations (400+, 400–500); these are retained rather than normalized to common 100/300/500 patterns because class alone is not sufficient evidence of a fixed cost.
- Current Super/Ultimate cost distribution includes 19 zero-cost, 154 100-Ki, 6 200-Ki, 45 300-Ki, 2 400-Ki, 13 500-Ki, 2 600-Ki, and 1 1000-Ki records, plus variable-cost records.
- Next metadata pass: acquisition semantics, character-only/CaC restrictions, Ultimate Finish requirements, DLC/version provenance, and mechanics evidence for the remaining canonical skills.


### Super/Ultimate Ki-cost audit — 2026-09-18
- Canonical Super/Ultimate records were checked for missing or malformed Ki-cost values.
- No Super/Ultimate records had null/missing Ki costs.
- Three variable-cost Ultimate records were normalized to the repository's documented string representation: Emperor's Death Beam = 400+, Final Flash (SS3 DAIMA) = 400+, Super Kamehameha (SS4 DAIMA) = 400–500.
- Fixed 0-Ki Super records were retained where the skill is a charge, reinforcement, utility, or other documented zero-cost technique; zero is not treated as missing data.
- Research sources describe Super attacks as generally costing 1–3 bars and Ultimates 3–7, but individual variable-cost mechanics require per-skill handling rather than class-based inference.


### Super/Ultimate Ki-cost completeness audit — 2026-09-18
- Canonical skill audit confirms all Super and Ultimate records currently have a populated `ki_cost` field; no missing/null Ki costs remain in the 298-record canonical catalog.
- Numeric Ki-cost distribution was checked rather than normalized by class: 0-cost utility/power-up skills are retained where documented, while standard values span 100–1000 Ki.
- Three variable/non-numeric cost formats remain intentionally preserved as mechanics data: Emperor's Death Beam (400+), Final Flash (SS3 DAIMA) (400+), and Super Kamehameha (SS4 DAIMA) (400–500). These should not be coerced into a single numeric value.
- Next metadata frontier: verify individual Ultimate Finish requirements and acquisition semantics, then DLC/version provenance and mechanics for records that still have partial verification.


### Super/Ultimate Ki-cost audit — 2026-09-18
- Canonical audit confirms all 298 skill records are represented in the current skill catalog and every record classified as Super or Ultimate has a non-null Ki cost.
- No nonstandard positive Ki-cost values were found in the canonical layer; this is a completeness check, not proof that every historical/version-specific cost is current.
- Research sources confirm that skill costs can change across versions (for example, official Steam patch notes documented x10 Kamehameha changing from 100 to 200 Ki), so future work should preserve version/history evidence rather than treating one value as timeless.
- Next metadata pass: verify acquisition route, DLC/version provenance, CaC/race/gender restrictions, Ultimate Finish requirements, and mechanics against individual sources.


### Skill acquisition-route audit — 2026-09-18
- Enriched six previously under-documented Super/Ultimate acquisition records from current source evidence: Final Flash (Super), Galick Gun, Kamehameha, Masenko, Energy Charge, and Final Kamehameha.
- Final Flash (Super) is explicitly character-only/unavailable to CaCs; Kamehameha is PQ05; Galick Gun and Masenko are training rewards; Energy Charge is tied to advancement/playstyle rewards; Final Kamehameha has TP Medal Shop, PQ91, and Double Crystal Raid acquisition paths.
- Canonical and index records were updated together and timestamped 2026-09-18.
- Remaining acquisition backlog is still large; continue in evidence-backed batches rather than filling routes by inference.


### Parallel Quest reward/acquisition enrichment — 2026-09-18
- Audited PQ161–PQ170 against the maintained Steam transcription and Madreag's current datamined PQ records.
- Added the documented generic unlock condition for this DLC block: owning the relevant DLC and having the PQ board open.
- Added explicit skill-drop semantics for the skills in PQ161–PQ168, distinguishing normal-clear drops from Ultimate Finish and Ultimate Finish bonus-slot drops. PQ169–170 correctly remain skillless rather than receiving fabricated skill rewards.
- Corrected the audit status for this block from unresolved drop-rate semantics to verified reward/drop-rate coverage where the external record explicitly established it.
- No probability was inferred; values were copied only where the external research record explicitly documented them.
- Next PQ priority: continue reward/acquisition enrichment through the remaining numbered blocks, then perform a full unresolved-field census before broadening to Awoken/Transformation mechanics.


### Parallel Quest reward/acquisition enrichment — 2026-09-18 (PQ171–PQ178)
- Audited PQ171–PQ178 against the maintained Steam transcription and Madreag's current datamined PQ records.
- Added the documented generic DLC/PQ-board unlock condition and exact skill-drop semantics for the block.
- Preserved the distinction between ordinary Ultimate Finish drops and Ultimate Finish bonus-slot drops; no drop probability was inferred.
- PQ171–178 now have explicit reward/drop-rate verification rather than the previous unresolved drop-rate status.

### GitHub Actions diagnostic — 2026-09-18
- New push-triggered workflow runs were observed after the PQ updates, but validation is not yet reportable as successful.
- Wiki data audit run 35385230606 terminated with `failure`; its only job (105730467465) exposed no steps and no logs through the GitHub API. Repository quality and cleanup runs were still queued/in progress at the time of inspection, while a Pages run was cancelled.
- Because the failed audit terminated before actionable step/log output was available, the failure cause cannot responsibly be classified as script, dependency, permission, billing, runner, or GitHub infrastructure from the available evidence. The project therefore continues local/repository validation without weakening validators or repeatedly rerunning an opaque failure.


### Parallel Quest reward/acquisition enrichment — 2026-09-18 (PQ179–PQ180)
- Extended the same evidence-backed enrichment through the Dragon Ball DAIMA Pack quests PQ179–PQ180.
- Added the documented DLC/PQ-board unlock condition and 50% Ultimate Finish skill-drop semantics for Heat Wave, Supreme Fury, Force Edge, and Burning Blast.
- Kept the skill/drop arrays aligned with canonical reward records after validation; no inferred percentages were introduced.


### Parallel Quest final-block reconciliation — 2026-09-18 (PQ181–PQ186)
- Completed the final numbered PQ block against the maintained Steam transcription and the current datamined corpus.
- Added the documented DLC/PQ-board unlock condition to PQ181–PQ186.
- Preserved unresolved skill-drop rates for PQ181–PQ183 and PQ185–PQ186 rather than inventing percentages from the basic-reward list.
- Confirmed PQ184's **Chaotic Time Impact** as a **50% Ultimate Finish bonus-slot** skill drop from the maintained datamined page.
- The Steam guide independently confirms the final PQ181–PQ186 objective sequences and listed rewards.
- This completes the numbered PQ acquisition pass; the next priority is a repository-wide unresolved-field census and reconciliation, followed by the Awoken/Transformation second-pass audit.


### Repository-wide Parallel Quest unresolved-field census — 2026-09-18
- Audited all 18 checked-in PQ research batches covering **176 canonical quest records (PQ1–PQ186, with the known numbering gap at PQ36)**.
- **Unlock conditions:** 24 of the 176 canonical quest records currently have no explicit `unlock_condition`. The remaining gaps are concentrated in PQ36, PQ53–55, PQ131–140, and PQ151–160. PQ101–120 have now been researched and populated with DLC-ownership/PQ-board unlock routes.
- The maintained general PQ documentation states that PQs are unlocked through story progression, blue-mark NPC prompts, or prerequisite PQ completion; PQ101+ require the appropriate DLC. This establishes the general mechanism, but does **not** safely provide an exact per-PQ unlock route for every missing record, so the census records these as research gaps rather than fabricating generic unlock text.
- **Skill/drop alignment:** all explicitly populated skill-reward arrays through PQ1–PQ180 are aligned with their corresponding skill-drop conditions; PQ181, 182, 183, 185, and 186 intentionally remain unresolved because the exact drop-slot percentages have not yet been established in the maintained evidence. PQ184 is explicitly documented at 50% Ultimate Finish bonus slot.
- **Sources:** the older PQ batches frequently lack record-level `sources` fields even where their verification notes identify the evidence basis. This is now a separate provenance-enrichment priority rather than silently copying one global source into every record.
- The next data pass should therefore prioritize **exact unlock-route research for the 34 remaining missing records**, followed by **record-level provenance normalization**, then the remaining Awoken/Transformation audit.

## 2026-09-19 PQ unlock research milestone

- **PQ71–80:** reviewed and normalized; several exact-looking prerequisites were removed where the consulted evidence did not directly establish them. The records now preserve uncertainty rather than presenting inferred sequential unlocks as fact.
- **PQ81–90:** reviewed against independent PQ objective/UF references. These sources establish the quests and their objectives, but did not establish reliable individual unlock triggers, so the records use bounded uncertainty wording.
- The numeric unlock-field gap in the earlier 2026-09-19 wording was stale; the live census now finds **34 records without any explicit `unlock_condition` field**, and that number is **not equivalent to 34 unresolved exact unlock routes**; populated fields must be classified by evidence quality in future work.

## 2026-09-19 PQ101–110 unlock research milestone

- Recomputed the live unlock census across all 18 canonical PQ research batches: 176 records total; 54 records without an explicit unlock_condition.
- Researched PQ101–110 individually against current Madreag datamined quest records plus the maintained Steam PQ guide, GameFAQs UF discussion, and DLC mapping.
- PQ101–103 are now recorded as requiring Super Pack 1 ownership with the PQ board open; PQ104–106 use Super Pack 2; PQ107–109 use Super Pack 3; PQ110 uses Super Pack 4.
- Added record-level source URLs to PQ101–110 so the unlock claims retain provenance instead of relying only on the batch-level source list.
- No sequential prerequisite was invented between these DLC quests; the current evidence describes them as DLC-gated entries on the PQ board.
- Exact reward-slot semantics remain unresolved where the consulted evidence did not directly establish them.

## 2026-09-19 PQ111–120 unlock research milestone

- Recomputed the live unlock census before editing the batch: 176 canonical PQ records across 18 research batches.
- Researched PQ111–120 as the next DLC frontier. Current evidence maps PQ111–112 to Super Pack 4, PQ113–117 to Extra Pack 1, and PQ118–120 to Extra Pack 2. The maintained Steam DLC mapping explicitly groups these PQ ranges by pack. - Recorded the conservative unlock route as owning the relevant DLC pack and having the Parallel Quest board open. This mirrors the evidence-backed DLC-era convention already used for PQ101–110 and avoids inventing sequential PQ prerequisites.
- Added record-level provenance for all ten records: Madreag's individual datamined quest page, the maintained Steam all-PQ guide, the Steam DLC-to-PQ mapping discussion, and the DLC reference page.
- Updated the live numeric gap from 44 to 34 missing `unlock_condition` fields. Remaining missing records are PQ36, PQ53–55, PQ121–140, and PQ151–160.
- Evidence limitation: the consulted mapping establishes DLC ownership/availability but does not prove additional story, NPC, or sequential prerequisites for each of PQ111–120; none were invented.


## 2026-09-19 PQ121–130 unlock research milestone

- Recomputed the live PQ unlock census before editing the batch: **176 canonical records** across 18 research batches.
- Researched **PQ121–130** individually as the next DLC-era frontier.
- Current DLC mapping places PQ121–122 in **Extra Pack 2**, PQ123–127 in **Extra Pack 3**, and PQ128–130 in **Extra Pack 4**. The maintained Steam DLC mapping and Bandai Namco's official DLC pages establish the corresponding pack/PQ groupings. 
- Added the conservative unlock route to all ten records: **own the relevant DLC pack and have the Parallel Quest board available**. No sequential prerequisite was invented.
- Added record-level provenance to all ten records using the maintained Steam PQ guide, the Steam DLC-to-PQ mapping discussion, and Bandai Namco's official DLC reference.
- The live numeric gap is now **24 records without an explicit `unlock_condition` field**: PQ36, PQ53–55, PQ131–140, and PQ151–160.
- Evidence limitation: the consulted DLC mapping establishes pack ownership/quest availability, but does not independently prove additional story, NPC, or prerequisite-PQ gates for each of PQ121–130. Those were intentionally not added.

## 2026-09-19 PQ91–100 unlock research milestone

- **PQ91–97:** verified as a sequential PQ chain (each quest follows the preceding PQ) against an independent Japanese PQ reference and corroborating community reports.
- **PQ98:** preserved as a special progression gate: completion of the base-game story, all five Time Eggs, and the Unknown History story are required by the consulted reference.
- **PQ99–100:** verified as the continuation of the PQ chain after PQ98.
- This batch reduces the numeric count of records with no `unlock_condition` field; exact evidence quality remains separately tracked and must not be inferred from field presence alone.


## 2026-09-19 PQ131–140 unlock research milestone

- Recomputed the live PQ unlock census after the PQ131–140 pass: **176 canonical PQ records** remain in the 18 checked-in research batches.
- Researched **PQ131–140** as the next DLC-era unlock frontier. The maintained Steam DLC mapping places PQ131–132 in **Extra Pack 4**, PQ133–137 in **Ultra Pack 1**, and PQ138–140 in **Ultra Pack 2**. Bandai Namco's official DLC reference independently confirms that Extra Pack 4 and Ultra Pack 1/2 contain the relevant DLC-era Parallel Quest content.
- Added the conservative unlock route to all ten records: **own the relevant DLC pack and have the Parallel Quest board available**. No sequential prerequisite, story gate, or NPC trigger was manufactured where the consulted evidence did not establish one.
- Added record-level provenance and an explicit bounded unlock-verification state to all ten records in `docs/data/parallel-quest-research-batches/pq-batch-14.json`.
- The live numeric gap is now **14 records without an explicit `unlock_condition` field**: **PQ36, PQ53–55, and PQ151–160**.
- Evidence limitation: the DLC mapping establishes the pack-to-PQ relationship and the repository's conservative DLC-era availability convention, but does not independently establish additional individual story/NPC/prerequisite-PQ gates for these ten records. Those details remain unresolved rather than inferred.


## 2026-09-19 PQ151–160 unlock research milestone

- Recomputed the live PQ census after the PQ131–140 pass: 176 canonical records across 18 batches.
- Researched PQ151–160. Current DLC mapping is PQ151–154 → Conton City Vote Pack; PQ155–158 → Hero of Justice Pack 1; PQ159–160 → Hero of Justice Pack 2. The maintained Steam guide independently lists the same PQ/DLC groupings, while the DLC reference confirms the four PQs in the Conton City Vote Pack.
- Added the conservative unlock route to all ten records: own the listed DLC pack and have the Parallel Quest board available. No unsupported sequential/story/NPC prerequisite was added.
- Added record-level source provenance, `unlock_verification`, and 2026-09-19 verification dates to `docs/data/parallel-quest-research-batches/pq-batch-15.json`.
- Live missing `unlock_condition` count is now **4**: PQ36, PQ53–55.


## 2026-09-19 PQ missing-unlock closure milestone

- Recomputed the live Parallel Quest unlock census after researching the four remaining missing records: **176 canonical records across 18 research batches; 0 records remain without an explicit `unlock_condition` field**.
- PQ36 now records completion of PQ35 as its unlock route, while preserving the independent numbering/existence conflict around PQ36 and treating the prerequisite evidence as separate provenance.
- PQ53 now records the Great Saiyaman 1 + 2 trigger on the floating Resort Island south of Conton City's Recreation Plaza.
- PQ54 now records PQ52 as the direct reported prerequisite, but remains `partially_verified_conflicting_community_evidence` because a separate community reply attributes the unlock to the earlier Great Saiyaman blue-exclamation quest.
- PQ55 records completion of PQ54 as its prerequisite.
- Evidence sources are retained at record level; no generic sequential prerequisite was propagated beyond what the sources support.
- This closes the explicit PQ unlock-field census, but **does not mean every unlock route is fully verified**. PQ54 remains contested, and other populated records may still use bounded board/story wording rather than an exact NPC/PQ trigger.
- Next PQ priority is therefore **record-level provenance and reward/acquisition/version semantics**, followed by the next P1 system audit rather than inventing more unlock fields.


## 2026-09-19 PQ missing-unlock closure milestone

- Recomputed the live Parallel Quest unlock census after researching the four remaining missing records: **176 canonical records across 18 research batches; 0 records remain without an explicit `unlock_condition` field**.
- PQ36 now records completion of PQ35 as its unlock route, while preserving the independent numbering/existence conflict around PQ36.
- PQ53 now records the Great Saiyaman 1 + 2 trigger on the floating Resort Island south of Conton City's Recreation Plaza.
- PQ54 now records PQ52 as the direct reported prerequisite, but remains `partially_verified_conflicting_community_evidence` because a separate community reply attributes the unlock to the earlier Great Saiyaman blue-exclamation quest.
- PQ55 records completion of PQ54 as its prerequisite.
- Evidence sources are retained at record level; no generic sequential prerequisite was propagated beyond what the sources support.
- This closes the explicit PQ unlock-field census, but **does not mean every unlock route is fully verified**. PQ54 remains contested, and other populated records may still use bounded board/story wording rather than an exact NPC/PQ trigger.
- Next PQ priority is **record-level provenance and reward/acquisition/version semantics**, followed by the next P1 system audit rather than inventing more unlock fields.


## Parallel Quest provenance pass — PQ21–PQ30 — 2026-09-19

- Completed record-level provenance for **PQ21–PQ30**; all ten records now carry explicit `sources` arrays and a 2026-09-19 verification date.
- Reconciled the basic reward lists against the maintained 186-PQ transcription and independent PQ tables. This corrected several incomplete reward records, including PQ22, PQ26, PQ28, PQ29, and PQ30.
- Strengthened PQ27 and PQ28 unlock metadata with their documented NPC triggers: Metal Cooler near Master Cell for PQ27 and Appule in the Bamboo Forest for PQ28.
- Preserved conservative unlock wording for the remaining quests where the available evidence did not establish an exact quest-specific trigger.
- Repository-wide census after this pass: **176 canonical records; 0 missing `unlock_condition` fields; 92 records still lacking individual `sources` arrays**.


## Parallel Quest provenance pass — PQ31–PQ40 — 2026-09-19

- Completed record-level provenance for **PQ31–PQ40**; all ten records now carry explicit source URLs and a 2026-09-19 verification date.
- Cross-checked the objective sequences and basic reward lists against the maintained 186-PQ transcription and independent Ultimate Finish/objective tables. The repository's existing reward data for this batch matches the primary transcription; no unsupported reward-slot percentages were added.
- PQ36's existing numbering/existence conflict remains explicitly documented and was independently cross-checked; it was not silently removed or normalized.
- Repository-wide census after this pass: **176 canonical records; 0 missing `unlock_condition` fields; 82 records still lacking individual `sources` arrays**.


## Parallel Quest provenance pass — PQ41–PQ50 — 2026-09-19

- Completed record-level provenance for **PQ41–PQ50**; all ten records now carry explicit source URLs and a 2026-09-19 verification date.
- Cross-checked objective sequences and basic rewards against the maintained 186-PQ transcription and independent Ultimate Finish/objective tables.
- Preserved unresolved reward-slot/drop semantics rather than converting documented rewards into unsupported percentages.
- Repository-wide census after this pass: **176 canonical records; 0 missing `unlock_condition` fields; 72 records still lacking individual `sources` arrays**.


## Parallel Quest provenance pass — PQ51–PQ60 — 2026-09-19

- Completed record-level provenance for **PQ51–PQ60**; all ten records now carry explicit source URLs and a 2026-09-19 verification date.
- Independently cross-checked the transition from the 5-star PQs into the 6-star block, including objectives and basic rewards.
- PQ52's unusual documented unlock behavior (completion of PQ53) is preserved because multiple long-running guide sources report it despite the apparent numbering reversal; it is not silently normalized.
- PQ54/PQ55 unlock evidence remains attributed to the underlying community report, including the direct report that PQ52 unlocked PQ54 and PQ54 unlocked PQ55.
- Repository-wide census after this pass: **176 canonical records; 0 missing `unlock_condition` fields; 66 records still lacking individual `sources` arrays**.


## Parallel Quest provenance pass — PQ61–PQ70 — 2026-09-19

- Completed record-level provenance for **PQ61–PQ70**; all ten records now carry explicit source URLs and a 2026-09-19 verification date.
- Reconciled the previously conservative unlock metadata against an independent Japanese PQ progression table: PQ61/PQ63 are tied to the Beerus/Wrath of the God of Destruction story arc; PQ62 and PQ64–PQ68 follow the documented PQ chain; PQ69 requires the Beerus-arc progression plus the documented Trunks interaction near the Time Nest; PQ70 is tied to the Resurrection of the Emperor/Golden Frieza story arc.
- Cross-checked objective sequences and basic rewards against the maintained 186-PQ transcription and independent Ultimate Finish references.
- Repository-wide census after this pass: **176 canonical records; 0 missing `unlock_condition` fields; 56 records still lacking individual `sources` arrays**.


## Parallel Quest provenance pass — PQ71–PQ80 — 2026-09-19

- Completed record-level provenance for **PQ71–PQ80**; all ten records now carry explicit source URLs and a 2026-09-19 verification date.
- Cross-checked the 7-star objective sequences and documented basic rewards against the maintained 186-PQ transcription and independent Ultimate Finish references. 
- Unlock metadata was reviewed conservatively. The maintained records retain their documented routes; external evidence also indicates PQ availability can depend on broader story progression rather than a single universal sequential prerequisite, so no stronger unsupported claim was introduced. 
- Repository-wide census after this pass: **176 canonical records; 0 missing `unlock_condition` fields; 46 records still lacking individual `sources` arrays**.


## Parallel Quest provenance pass — PQ81–PQ90 — 2026-09-19

- Completed record-level provenance for **PQ81–PQ90**; all ten records now carry explicit source URLs and a 2026-09-19 verification date.
- Corrected missing difficulty metadata: PQ81–PQ90 are documented as the base game's **7-star** block. 
- Cross-checked objective sequences and basic rewards against the maintained 186-PQ transcription plus independent Ultimate Finish/objective tables. 
- PQ83 progression has community evidence for the 81→82→83 sequence, while general documentation notes that base-game PQs can also be surfaced through story progression and Conton City NPCs; individual unlock fields therefore remain conservative where a unique trigger is not established. 
- Repository-wide census after this pass: **176 canonical records; 0 missing `unlock_condition` fields; 36 records still lacking individual `sources` arrays**.


## Parallel Quest provenance pass — PQ91–PQ100 — 2026-09-19

- Completed record-level provenance for the final **PQ91–PQ100** base-game block; all ten records now carry explicit source URLs and 2026-09-19 verification dates.
- Corrected missing difficulty metadata: PQ91–PQ100 are documented as **7-star** quests. 
- Reconciled reward data against the maintained 186-PQ transcription. In particular, PQ95 includes **Flash Bomber** and **Drain Field**; PQ96 includes **GT Vegeta's Jacket** and **Absolute Zero**; PQ97 includes its documented clothing/capsule/super-soul set plus **Charged Ki Wave** and **Phantom Fist**; PQ98 includes **Lord Slug's Clothes** and **Dimension Ray**; PQ100 includes **x100 Big Bang Kamehameha**, **SSGSS Vegeta Wig**, and **Whis Symbol Battle Suit**. 
- Cross-checked final Ultimate Finish objectives against multiple independent tables; PQ100 requires the 8-minute condition before the SSGSS Goku/Vegeta phase. 
- Unlock metadata was deliberately kept conservative where sources establish only general story/PQ progression or disagree on a unique prerequisite. Base-game PQs are generally surfaced through story progression, blue-NPC prompts, or other PQ completion. 
- Repository-wide census after this pass: **176 canonical records; 0 missing `unlock_condition` fields; 26 records still lacking individual `sources` arrays**.


## Parallel Quest provenance pass — PQ161–PQ170 — 2026-09-19

- Completed record-level provenance for **PQ161–PQ170**; all ten records now carry explicit source URLs and a 2026-09-19 verification date.
- Independent references confirm the quest names, DLC associations, Ultimate Finish conditions, and documented rewards. PQ161–162 belong to Hero of Justice Pack 2, while PQ163–170 are Future Saga Chapter 1 content. 
- The existing explicit drop-rate statements were preserved; no new probabilities were inferred. PQ161's 7-minute condition, PQ162's player-health-over-50% condition, and PQ163–170's listed time/target conditions were cross-checked against independent Ultimate Finish records. 
- Repository-wide census after this pass: **176 canonical records; 0 missing `unlock_condition` fields; 16 records still lacking individual `sources` arrays**.


## Parallel Quest provenance pass — PQ171–PQ180 — 2026-09-19

- Completed record-level provenance for **PQ171–PQ180**; all ten records now carry explicit source URLs and a 2026-09-19 verification date.
- Independent references cross-check the Future Saga Chapter 1/2 and Dragon Ball DAIMA DLC associations, Ultimate Finish conditions, and documented rewards for these quests. 
- No new reward probabilities were inferred; existing explicit drop-rate evidence in the maintained corpus was preserved.
- Repository-wide census after this pass: **176 canonical records; 0 missing `unlock_condition` fields; 6 records still lacking individual `sources` arrays**.


## Parallel Quest provenance pass — PQ181–PQ186 — 2026-09-19

- Completed record-level provenance for the **final six unsourced PQ records, PQ181–PQ186**; all six now carry explicit source URLs and a 2026-09-19 verification date.
- Independent references cross-check the DLC associations, Ultimate Finish conditions, and documented rewards. The maintained Steam transcription identifies PQ181 as Dragon Ball DAIMA Pack, PQ182–184 as Future Saga Chapter 3, and PQ185–186 as Future Saga Chapter 4. 
- PQ184's documented `Chaotic Time Impact` 50% Ultimate Finish bonus-slot rate was independently cross-checked; no unsupported probabilities were added to PQ181–183 or PQ185–186. 
- Repository-wide provenance census after this pass: **176 canonical records; 0 missing `unlock_condition` fields; 0 records lacking individual `sources` arrays**.


## 2026-09-19 Skill indexed-Evasive reconciliation — batch 45

- Reconciled eight indexed Evasive records: Absolute Zero, Dragon Burn, Explosive Wave, Punisher Guard, Final Pose, Mach Dash, Angry Shout, and Energy Barrier.
- Verified CaC availability, acquisition route, stamina cost, current naming, and descriptive mechanics against the current Evasive Skill reference and individual skill references.
- Updated `docs/data/skills.json` and the existing `docs/data/skill-research-batches/skill-batch-45.json`. Records remain `partially_verified` because exact reward-slot/drop gating remains unresolved.
- No unsupported drop percentages were added. Canonical skill population remains 283 unique records.


## 2026-09-19 Skill indexed-record completion pass

- Audited all 18 records that remained `indexed` after canonical skill deduplication and the Evasive batch.
- Reconciled CaC availability, acquisition route, source location, Ki cost, and core descriptive mechanics for Destructo-Disc, Emperor's Blast, Final Flash (Super), Galick Gun, Kamehameha, Masenko, Afterimage Strike, Dancing Parapara, Energy Charge, Energy Release, Instant Charge, Rise to Action, Rising Rage, Solar Flare, Spirit Boost, Time Bullet, Wall of Defense, and Final Kamehameha.
- Character-only records were explicitly retained as non-CaC rather than inferred from category membership. Exact reward-slot probabilities and disputed/version-sensitive details remain unresolved where evidence is insufficient.
- `docs/data/skills.json` updated in commit `8f82dd22a7e0d43f4186da95295807b1fd8feedd`.
- The connector could not create a new `skill-batch-48.json` because its create-file wrapper returned a GitHub 422 requiring a SHA even though the target path was new. No existing historical batch was overwritten to work around this tooling limitation.


## 2026-09-19 Skill acquisition/CaC reconciliation follow-up

- Continued P1 canonical skill research after clearing the `indexed` status backlog.
- Reconciled another high-impact partial cohort covering counter skills and remaining Evasives: CaC eligibility, concrete PQ/mentor/shop acquisition locations, base-game versus DLC-era provenance where supported, and zero-Ki Evasive costs where the maintained corpus supports them.
- Records touched include Burst Reflection, Burst Rush, Change The Future, Counter Burst, Counter Impact, Demon Flash Strike, Dimensional Hole, Flash Fist Crush, God Breaker, Heroic Counter, Punisher Shield, Reverse Mabakusenko, Rough Ranger, Shadow Crusher, Sudden Death Beam, Super Afterimage, Super God Shock Flash, Time Skip/Back Breaker, Time Skip/Flash Skewer, Time Skip/Jump Spike, Ultrasonic Blitz, Celestial Wave, Force Shield, Instant Rise, Ki Explosion, and Maiden Burst.
- Exact DLC-pack provenance for several late PQ records remains intentionally unresolved rather than inferred solely from quest numbering.
- `docs/data/skills.json` commit: `4ec88f3820e2a38d49f3cfa10e6256b244e679c7`.


## 2026-09-19 Skill CaC/provenance reconciliation batch

- Reconciled a focused partial cohort against current Xenoverse 2 references: **Burst Reflection, Divine Kamehameha, Perfect Shot, Spirit Bomb, Instant Transmission, Super Guard, Afterimage, and Celestial Wave**.
- Added/confirmed CaC eligibility and documented the relevant acquisition routes. Supported resource values were also filled: Divine Kamehameha 200 Ki, Perfect Shot 100 Ki, Instant Transmission 0 Ki, Super Guard's Ki-drain behavior, and Celestial Wave's 300 Stamina.
- Divine Kamehameha's TP Medal Shop distribution is version/update-sensitive, so the record retains provenance rather than claiming a timeless shop state. Celestial Wave remains associated with the Conton City Vote Pack/PQ151 provenance.
- These records remain `partially_verified` because this pass establishes acquisition/CaC facts, not exhaustive reward-slot probability or every historical version boundary.
- Skills commit: `28a6fb4b85a7a6eabf4b60052a8a92f7a5c6bee1`.
- External corroboration included current Xenoverse 2 skill pages for Burst Reflection, Divine Kamehameha, Perfect Shot, Instant Transmission, Super Guard, and Celestial Wave, plus the mentor/reward reference for Cell and the current wish table. cite references are external only; repository files retain source URLs.


## 2026-09-19 Skill CaC/race restriction batch — charge, mentor, and support skills

- Reconciled **Bending Kamehameha, Full Power Charge, Maximum Charge, Charged Ki Wave, Ultimate Charge, Burst Charge, Data Input, Pressure Sign, Meditation, Deadly Dance, and Quick Sleep**.
- Confirmed Future Warrior/CaC availability for the charge, support, mentor, and Expert Mission skills using current Future Warrior technique references and individual skill references. Quick Sleep is explicitly restricted to **Majin** CaCs.
- Recorded Extra Pack 1 provenance for Data Input and Extra Pack-era/PQ134 provenance for Ultimate Charge and Burst Charge. Base-game provenance was retained for the standard advancement-test and mentor skills.
- Resource values were filled only where the current evidence supports them; no reward probability was inferred.
- Skills commit: `00ef8d9e609274297915e365f21f0924e598d968`.
- External evidence: Bending Kamehameha/Future Warrior, Data Input, Full Power Charge/charge-skill lineage, Pressure Sign, Meditation, Deadly Dance, and Quick Sleep references were reviewed. cite references are external only; repository files retain source URLs.


## 2026-09-19 Future Warrior ultimate-skill reconciliation

- Reconciled **Big Bang Kamehameha, Super Spirit Bomb, Emperor's Death Beam, and Final Explosion** from Future Warrior-specific Xenoverse 2 references.
- Big Bang Kamehameha is explicitly obtainable by the Future Warrior through the TP Medal Shop; Super Spirit Bomb is a Future Warrior reward from Expert Mission 16; Emperor's Death Beam is obtainable by the Future Warrior; Final Explosion is obtainable by the Future Warrior from the TP Medal Shop. 
- Added CaC eligibility, race scope, acquisition/provenance, and supported resource data without promoting the records to `verified` because exact historical/version and reward-state semantics remain separate audit questions.
- Skills commit: `ed425d388377902aed738ba03ae49b85342d3c41`.


## 2026-09-19 DAIMA/Future Saga CaC boundary investigation

- Investigated the remaining high-priority null-CaC cohort against current technique/Ultimate Attack references.
- The Future Warrior technique index explicitly notes that CaC techniques can have race/gender/transform restrictions and should not be inferred solely from a character's equipped moves. 
- The DAIMA-specific **Burning Blast, Force Edge, Final Flash (SS3 DAIMA), and Super Kamehameha (SS4 DAIMA)** remain unresolved for direct CaC eligibility. Current references identify them in the corresponding DAIMA character skillsets and list their PQ unlocks, but do not provide sufficiently explicit Future Warrior eligibility to justify changing `usable_by_cac` from null. 
- Likewise, Future Saga Chapter 2 is documented by Bandai Namco as adding seven moves and four Parallel Quests, but the official announcement does not establish individual CaC eligibility. 
- Deliberately left these fields unresolved rather than converting absence of evidence into `false` or assuming all PQ rewards are CaC-compatible.


## 2026-09-19 Future Warrior skill-evidence batch — PQ/shop techniques

- Reconciled **Phantom Fist, Shield Barrier, Assault Vanish, Fighting Pose K, Death Ball, Supernova, Divine Lasso, Lightning Impact, and Prominence Flash** using explicit Future Warrior evidence. Phantom Fist is obtained by Future Warrior from PQ97; Shield Barrier from PQ153; Assault Vanish from PQ131's Legendary Finish; Fighting Pose K is among the Fighting Poses the Future Warrior can learn; Divine Lasso is purchasable by the Future Warrior from the TP Medal Shop; Lightning Impact and Prominence Flash explicitly list Future Warrior users. 
- These records remain `partially_verified`; CaC eligibility is now evidenced, but exact reward-slot/drop semantics and historical version boundaries remain separate verification requirements.


## 2026-09-19 Future Warrior/form-exclusive reconciliation

- Reconciled the remaining high-value CaC gaps **Surging Spirit, Dragon Fist, Divine Ray Bomb, Dragon Thunder, Final Rampage, Godly Display, Supreme Fury, and Victory Rush** where the live Future Warrior technique corpus supports CaC/form access.
- `Surging Spirit` is recorded as CaC-usable specifically through the **Ultra Instinct Future Warrior** form rather than as an unrestricted standalone CaC skill. The Future Warrior technique reference explicitly documents this form-exclusive access. 
- The remaining records were populated with CaC eligibility while retaining `partially_verified`; exact reward/drop semantics and version boundaries are not being collapsed into the CaC field.
- Skills commit: `6f1a988f2eee96c59e137999f6842cd628b49c73`.


## 2026-09-19 explicit race-restriction reconciliation

- Reconciled race/gender restrictions for **Saiyan Spirit, Explosive Buu Buu Punch, Zigzag Express, Ill Bomber, Candy Beam, Buu Buu Ball, Shining Slash, Burning Slash, Evil Flight Strike, Darkness Rush (Melee), and Darkness Rush (Ranged)**.
- The Future Warrior technique reference explicitly identifies Saiyan Spirit as Saiyan-only; Explosive Buu Buu Punch, Ill Bomber, Candy Beam, and Buu Buu Ball as Majin-restricted; Zigzag Express as male Majin-restricted; Shining/Burning Slash as Human-or-Saiyan; Evil Flight Strike as Namekian-or-Majin; and the two Darkness Rush variants as Namekian versus non-Namekian. 
- These restrictions are now recorded instead of the generic/unresolved race scope. Records remain `partially_verified`.


## 2026-09-19 recent-DLC unresolved-CaC evidence refinement

- Recalculated the canonical skill census: **18 records still have `usable_by_cac: null`**, while **184 CaC-eligible records still have an unresolved `race_restriction`**.
- Reviewed recent Future Saga/DAIMA candidates including **Dark Inscription, Emperor's Cannon, Chaotic Time Impact, Burst Blitz, Dragon Spark, and Soaring Rush**. Current evidence identifies Golden Frieza (Ultra Supervillain) as the user/preset holder for the first three and Goku (Mini) as the user for the latter three, but does not by itself establish a valid CaC route. 
- These records therefore remain unresolved rather than being promoted to `usable_by_cac: true` or `false` from weak inference. This preserves the audit's evidence standard.
- Skills commit: `b9a8e3ae8baa7c8acbe11c150266a01b1f0c747b`.


## 2026-09-19 explicit Future Warrior corrections

- Re-audited the remaining null-CaC cohort against the live Future Warrior technique corpus.
- **Mystic Flash** and **Thunder Flash** were found to be explicitly documented as Future Warrior techniques, so both are now `usable_by_cac: true`. The source identifies Mystic Flash as Nail's Ultimate Skill usable by the Future Warrior and Thunder Flash as Pikkon's Ultimate Skill usable by the Future Warrior. 
- No race restriction was inferred for either record because the source does not establish one.
- Skills commit: `cbb114e5cef2b499450dc937367d3b95e7a1e202`.


## 2026-09-19 Requiem of Destruction verification

- **Requiem of Destruction** was removed from the null-CaC cohort. Its technique page explicitly lists the Future Warrior as a user and states that in Xenoverse 2 it is obtainable by the Future Warrior from New Parallel Quest 104, "Vados the Talent Scout." 
- The record is now `usable_by_cac: true`; no race restriction was inferred.
- Skills commit: `6cc97745e9856af45e52d148aa3d40f6f14f7184`.


## 2026-09-19 DLC evidence boundary re-audit

- Re-audited the remaining unresolved recent-DLC skills against explicit character/PQ evidence. Current sources continue to identify **God of Destruction's Plaything/Poise** as Belmod's skills and **Force Edge/Burning Blast** as SS3 Vegeta (DAIMA)'s skills; PQ reward listings establish acquisition availability but not automatically CaC eligibility. 
- The Future Saga Chapter 2 DLC source lists its seven new skills and four PQs, but does not establish individual CaC eligibility. 
- Preserved these records as unresolved instead of treating a PQ reward or character moveset as proof of CaC access.
- Skills commit: `dd675147e02a668b79a8b94b2293a8d55d27fbf9`.


## 2026-09-19 DAIMA CaC evidence reconciliation

- Explicit CaC evidence was found for **Force Edge, Burning Blast, Final Flash (SS3 DAIMA), and Super Kamehameha (SS4 DAIMA)**. A published Xenoverse 2 video specifically presents the DAIMA skills as "CaC Super & Ultimate Attacks," while additional community evidence documents Final Flash (SS3 DAIMA) and Burning Blast being used in CaC builds/combo testing. 
- These four records are now `usable_by_cac: true`. No race restriction was inferred from these sources.
- This is stronger than merely observing that the skills are PQ rewards or equipped by DAIMA characters, but the records remain `partially_verified` because exact reward-slot/drop semantics are still a separate verification requirement.
- Skills commit: `9db1be415b06fbfde8288f0eb8e47548477b30f6`.


## 2026-09-19 CaC build evidence correction

- **God of Destruction's Plaything** was previously left unresolved because PQ reward/Belmod moveset evidence did not prove CaC access. A separate CaC build source explicitly lists the skill as usable in a custom-character moveset. 
- Corrected the canonical record to `usable_by_cac: true`; no race restriction was inferred.
- This remains `partially_verified` because the exact acquisition/drop semantics are a separate evidence requirement.
- Skills commit: `c4c98ee41354038d4e0701c8d82a0f18c52b0df3`.


## 2026-09-19 explicit DLC CaC reconciliation — second pass

- Reconciled six remaining null-CaC records with stronger evidence: **Blaster Stream, God of Destruction's Poise, Full Power Destruction, Soaring Rush, Burst Blitz, and Dragon Spark**.
- Blaster Stream is explicitly documented as obtainable by the Future Warrior from PQ148. 
- A DLC 17 CaC-focused source explicitly groups the Belmod, Jiren Full Power, and Goku Mini skills as **CaC Super & Ultimate Attacks**, covering God of Destruction's Poise, Full Power Destruction, Soaring Rush, Burst Blitz, and Dragon Spark. 
- Independent player testing also documents Full Power Destruction and God of Destruction's Poise being used on a CaC. 
- All six are now `usable_by_cac: true`; no race restriction was inferred. Exact reward/drop semantics remain separate from CaC eligibility, so they remain `partially_verified`.
- Skills commit: `6bb28b3140b30047c04a22436593cfc4feb55157`.


## 2026-09-19 Heat Wave CaC evidence

- **Heat Wave** was found in a documented player CaC build, providing direct evidence of in-game custom-character use rather than relying on the skill's character/PQ provenance. 
- Corrected `usable_by_cac` to `true`; no race restriction was inferred from that build.
- The record remains `partially_verified` because the build establishes use, not the complete acquisition/drop semantics.
- Skills commit: `7e4650b290fdf48c6b1c237286b1a7772ff6cd25`.


## 2026-09-19 final null-CaC cohort closure

- Closed the final three `usable_by_cac: null` records: **Dark Inscription, Emperor's Cannon, and Chaotic Time Impact**.
- A DLC 20 CaC-focused source explicitly presents all three Golden Frieza skills as **CaC Super & Ultimate Attacks**. 
- The Future Warrior technique reference establishes that the custom protagonist can learn character-origin techniques through the game's skill acquisition systems, but character preset ownership alone was not used as proof. 
- All three are now `usable_by_cac: true`; no race restriction was inferred from this evidence. Acquisition/drop gating remains separately marked as research where unresolved.
- Skills commit: `256d88f05c339da6bfcab7a7c7b3f1d18bd68a1e`.


## 2026-09-19 race-restriction census kickoff

- Recomputed the live skills cohort after closing the null-CaC audit: **283 total skill records, 270 CaC-usable, 202 CaC-usable records still lacking a race restriction value**.
- The Future Warrior technique reference explicitly states that some techniques are race/gender/form exclusive and specifically identifies **Majin Kamehameha** as an imitation used by members of the Majin race. 
- Updated **Majin Kamehameha** to `race_restriction: "Majin"`.
- This is a restriction census, not a character-source inference: the repository will continue requiring explicit Future Warrior/CaC evidence before assigning a restriction.
- Skills commit: `574e87cde26b8e8ed1bdaa410e7b59786e3e4305`.


## 2026-09-19 race census — universal CaC batch

- Used the Future Warrior technique reference to distinguish explicitly available techniques from race-exclusive techniques. The reference lists **Kamehameha, Masenko, Energy Charge, Solar Flare, Afterimage Strike, Rise to Action, Wall of Defense, Destructo-Disc, and Galick Gun** among Future Warrior techniques and provides no race restriction for these entries. 
- Reconciled all nine to `race_restriction: "All CaC races"` rather than leaving them ambiguous.
- This is evidence of CaC availability across the selectable Future Warrior races; it is not inferred from the source character's race.
- Skills commit: `d248c4be6598c338181efd83a9c5edbe1472e496`.


## 2026-09-19 race census — universal technique batch 2

- Reconciled **Candy Beam (Super)** as `All CaC races`: independent Xenoverse 2 documentation explicitly states the Super Buu (Gohan Absorbed) Candy Beam can be used by non-Majin characters, while the Evasive Candy Beam remains Majin-CaC-only. 
- Reconciled **Petrifying Spit** and **Kai Kai** as `All CaC races`: the Future Warrior reference lists both among the Warrior's general/all-race techniques, while separately identifying race-exclusive abilities elsewhere. 
- Skills commit: `dc4fc4234876c747429e81a73cf8be8be4c946e6`.


## 2026-09-19 race census — explicit restriction batch

- Reconciled **Zigzag Express → Majin male**. The Future Warrior reference explicitly says it can only be used by a male Majin, and the skill page independently states the same restriction. 
- Reconciled **Namek Finger → Namekian**. The Future Warrior reference explicitly identifies it as usable by a Namekian Future Warrior. 
- Skills commit: `8425c7ed5804608fdbd38df7668d9495e94642a8`.


## 2026-09-19 race census — provenance hardening

- Recomputed the live race backlog: **189 CaC-usable skill records still have `race_restriction` unset**.
- No new restriction was inferred in this pass. Instead, hardened provenance for the already reconciled race-specific cohort by adding the dedicated Future Warrior technique reference to **Saiyan Spirit, Explosive Buu Buu Punch, Zigzag Express, Quick Sleep, Ill Bomber, Burning Slash, Shining Slash, Evil Flight Strike, Namek Finger, and Majin Kamehameha**.
- The reference explicitly distinguishes race/gender-restricted techniques from general Future Warrior techniques; examples include Saiyan Spirit (Saiyan), Explosive Buu Buu Punch/Ill Bomber/Quick Sleep (Majin), Zigzag Express (male Majin), Shining/Burning Slash (Human or Saiyan), Evil Flight Strike (Namekian or Majin), Namek Finger (Namekian), and Majin Kamehameha (Majin). 
- This pass intentionally made no blanket assumptions about the remaining 189 records.
- Skills commit: `7dad27d834189474438cae340de541b1ad1ca168`.


## 2026-09-19 race/form census — Pure Majin batch

- Reconciled six form-exclusive records from the Future Warrior technique reference: **Angry Shout, Vanishing Ball, Super Vanishing Ball, Teleporting Vanishing Ball, Pearl Flash, and Buu Buu Ball** → `Majin (Pure Majin form)`.
- The reference explicitly places these techniques under **Purification (Pure Majin)** and identifies them as usable by the Pure Majin Future Warrior. It separately identifies Quick Sleep as a Majin technique and Pure Majin-specific in the form section. 
- This distinction matters: these are not merely general Majin-race restrictions; their documented use is tied to the Pure Majin/Purification form.
- Skills commit: `156e8fce946ffd4085ebb86e0accb41e943b0706`.


### Correction — Pure Majin batch representation check (2026-09-19)
- Live `docs/data/skills.json` contains four of the six techniques discussed in the prior audit entry: **Angry Shout, Buu Buu Ball, Vanishing Ball, and Teleporting Vanishing Ball**. Those four are now explicitly marked `Majin (Pure Majin form)`.
- **Pearl Flash** and **Super Vanishing Ball** are documented by the external Future Warrior reference as Pure Majin techniques, but they are **not currently represented as records in `skills.json`**, so no phantom records were created. They remain data-model/content backlog items rather than falsely being counted as reconciled records. 


## 2026-09-19 skill race-restriction evidence boundary

The current race-restriction pass was rechecked against the accessible Future Warrior technique reference. That source explicitly distinguishes skills restricted to a race/gender/form from ordinary character-origin skills, and directly documents restrictions including Saiyan Spirit (Saiyan), Explosive Buu Buu Punch (Majin), Zigzag Express (male Majin), Quick Sleep (Majin), Ill Bomber (Majin), Shining Slash/Burning Slash (Human or Saiyan), Candy Beam/Buu Buu Ball (Majin), Evil Flight Strike (Namekian or Majin), and Namek Finger (Namekian). Existing canonical records already capture these restrictions, so no duplicate or speculative edits were made in this cycle. The remaining null-race cohort is therefore not safely reducible merely from character ownership or from absence of a restriction sentence. Future batches must require explicit Future Warrior race/gender/form wording before replacing null.


## 2026-09-19 independent Future Warrior provenance hardening

Rechecked the live skill census and added an independent accessible Future Warrior reference to 13 already-reconciled race/gender/form-restricted skill records: Saiyan Spirit, Explosive Buu Buu Punch, Zigzag Express, Ill Bomber, Candy Beam, Buu Buu Ball, Shining Slash, Burning Slash, Evil Flight Strike, Darkness Rush (Melee), Darkness Rush (Ranged), Majin Kamehameha, and Namek Finger. This is provenance hardening only; no race values were inferred or changed in this batch. The independent reference explicitly states the relevant Future Warrior restrictions. The live census remains **283 total / 270 CaC-usable / 186 CaC-usable with null race restriction**. The remaining null cohort requires the same explicit-evidence threshold.


## 2026-09-19 Future Warrior unrestricted-provenance batch

Added the independent Future Warrior technique reference to seven existing CaC-usable records: **Demon Ray, Stone Bullet, Hero's Flute, Brave Sword Slash, Dimension Ray, God of Destruction's Roar, and Brave Sword Attack**. This batch strengthens acquisition/user provenance without assigning a race restriction: the accessible reference identifies these techniques as part of the Future Warrior's Xenoverse 2 technique set, but does not provide a sufficiently explicit universal-race statement for each record. The repository therefore keeps the race restriction field null for these records rather than converting them to `All CaC races` by inference. The live race backlog remains **186** CaC-usable records with null race restriction.

## 2026-09-19 Future Warrior provenance expansion — batch 2

Added the independent Future Warrior technique reference to 20 existing CaC-usable records: **Burst Rush, Change The Future, God Breaker, Psychic Move, Atomic Blast, Burning Attack, Crazy Finger Shot, Death Psycho Bomb, Emperor's Blast, Charge, Blazing Attack, Burst Blitz, Evil Whirlwind, Freedom Kick, Mach Punch, Recoome Kick, Sauzer Blade, Final Explosion, Heat Dome Attack, and Victory Rush**. These edits strengthen evidence/provenance only. The reference establishes Future Warrior usage but does not by itself establish an all-race classification for each technique, so no `race_restriction` value was invented. 

## 2026-09-19 Future Warrior provenance expansion — batch 3

Added the independent Future Warrior technique reference to 30 additional existing CaC-usable records: **Counter Burst, Counter Impact, Demon Flash Strike, Dimensional Hole, Flash Fist Crush, Heroic Counter, Punisher Shield, Reverse Mabakusenko, Rough Ranger, Shadow Crusher, Sudden Death Beam, Super Afterimage, Super God Shock Flash, Time Skip/Back Breaker, Time Skip/Flash Skewer, Time Skip/Jump Spike, Ultrasonic Blitz, Absolute Zero, Dragon Burn, Force Shield, Instant Rise, Ki Explosion, Maiden Burst, Mighty Explosive Wave, Punisher Guard, Side Bridge, Spread Shot Retreat, Steel Mirage, Final Pose, and Mach Dash**. This is provenance-only: the reference establishes Future Warrior technique usage, but does not establish universal race access for these records. Race restrictions remain null unless separately supported by explicit evidence.

## 2026-09-19 Future Warrior provenance expansion — batch 4

Added the Future Warrior technique reference to 25 additional existing CaC-usable records: **Energy Barrier, Spirit Explosion, Spirit Slash, Blaster Ball, Bluff Kamehameha, Breaker Energy Wave, Burst Kamehameha, Burst Stinger, Dark Inscription, Destruction's Concerto: Comet, Destruction's Concerto: Starfall, Dimension Cannon, Double Death Slicer, Dust Attack, Earth Splitting Galick Gun, Emperor's Cannon, Eraser Bomb, Evil Blast, Evil Flame, Final Cannon, Flash Chaser, Gamma Blaster, Giant Cluster, Gigantic Charge, and God Punisher**. This remains provenance-only; no race classification was inferred from character ownership or technique listing.

## 2026-09-19 Future Warrior provenance expansion — batch 5

Added the Future Warrior technique reference to 24 additional existing CaC-usable records: **Handy Canon, Headshot, Heat Wave, Ill Rain, Paralysis, Paralyze Beam, Pendulum Bullet, Photon Swipe, Pretty Cannon, Raid Blast, Ray Blast, Reverse Shot, Rolling Bullet, Shine Shot, Spirit Blaster, Spirit Pulse, Super Donut Volley, Super Ghost Buu Attack, Variable Snipe Shot, Victory Cannon, Wild Buster, Dancing Parapara, Spirit Boost, and Time Control**. This is provenance-only. The accessible evidence does not by itself establish unrestricted race access, so `race_restriction` was not changed.

## 2026-09-19 Future Warrior cross-source provenance

Added a second independent Future Warrior reference to 8 existing CaC-usable records: **Mach Dash, Stone Bullet, Hero's Flute, Formation!, Brave Sword Slash, Dimension Ray, God of Destruction's Menace, and Brave Sword Attack**. This is a provenance corroboration pass, not a race-classification pass. The Codex reference explicitly documents the Future Warrior's race-dependent technique cases and also lists these techniques; where it does not state a restriction, the canonical `race_restriction` remains unchanged.

## 2026-09-19 Explicit form-restriction audit

Reviewed the Future Warrior source's form-exclusive sections for Great Namekian, Pure Majin, Golden-form Frieza Race, and Ultra Instinct techniques. The source explicitly identifies several transformation-specific techniques, but none of those exact technique names is present in the current canonical `docs/data/skills.json` inventory. Therefore this pass produced **no canonical classification changes** and preserved the existing 186-record null-race frontier.

## 2026-09-19 explicit-restriction cross-check

Cross-checked the source's explicitly stated Future Warrior race/gender restrictions against the live canonical skill inventory. The complete explicit set represented by the source — Saiyan Spirit; Explosive Buu Buu Punch; Zigzag Express; Quick Sleep; Ill Bomber; Shining Slash; Burning Slash; Candy Beam; Buu Buu Ball; Evil Flight Strike; Namek Finger; Darkness Rush (Ranged); Darkness Rush (Melee); and Majin Kamehameha — has **no remaining CaC-usable record with a null `race_restriction`**. This confirms the previously reconciled restriction cohort is still closed. The remaining 186 null records require separate evidence rather than inference.

## 2026-09-19 Death Psycho Bomb — explicit unrestricted evidence

`Death Psycho Bomb` was the first new classification from the expanded independent-source pass. The dedicated technique page explicitly states that in Xenoverse 2 it can be obtained by the Future Warrior from PQ33 and **can be used by the Future Warrior regardless of race**. The canonical skill had `usable_by_cac: true` and a null `race_restriction`, so it is now classified as **All CaC races**. This is an evidence-backed classification, not an inference from Frieza ownership. 

## 2026-09-19 Justice Pose — explicit unrestricted evidence

`Justice Pose` was reclassified from null to **All CaC races**. The dedicated source states that the Xenoverse 2 Super Skill can be used by the Future Warrior **regardless of race or gender** and distinguishes this from the separately named emote restriction. This directly matches the canonical CaC skill record. 

## 2026-09-19 — dedicated technique provenance

Added direct technique-page provenance to six existing CaC-usable skill records without changing their race classifications: `Mach Dash`, `Energy Barrier`, `Blaster Ball`, `Crazy Finger Shot`, `Evil Flame`, and `Final Cannon`. The search produced no new explicit race/unrestricted statement strong enough to reclassify the remaining null-race cohort in this pass. Existing classifications were therefore left unchanged.

## 2026-09-19 Crazy Finger Shot — explicit unrestricted evidence

`Crazy Finger Shot` was reclassified from null to **All CaC races**. The dedicated `Death Bullet` reference explicitly states that the Future Warrior, regardless of race, can use Death Bullets as part of the `Crazy Finger Shot` Super Skill. This is direct evidence for the canonical skill's unrestricted race access, distinct from the separate Frieza-race basic Ki Blast behavior. 

## 2026-09-19 Raid Blast — dedicated provenance

Added the dedicated `Niagara Pummel` reference to the existing `Raid Blast` skill record. The source confirms the Xenoverse 2 identity and Future Warrior acquisition route (New Parallel Quest 136), but does not establish a race restriction, so `race_restriction` remains unchanged.

## 2026-09-19 Counter Burst — dedicated provenance

Added the dedicated `Counter Burst` technique reference to the existing skill record. It confirms the Xenoverse 2 skill and Future Warrior PQ75 acquisition route, but does not provide an explicit race/gender restriction. The null `race_restriction` value is therefore retained.

## 2026-09-19 Super Spirit Bomb — independent Future Warrior corroboration

Added The Codex Future Warrior reference to the existing `Super Spirit Bomb` record. The source explicitly states that the Future Warrior can learn/use Spirit Bomb and Super Spirit Bomb regardless of selected race, independently corroborating the existing `All CaC races` classification. No new classification was inferred from this pass. The same audit confirmed that `Brave Heat`, `Power Pole`, and `Power Pole Combo` are discussed by external Future Warrior references but are not canonical records in the current `skills.json`; no records were fabricated.

## 2026-09-19 — null-race batch: counter/time-skip skills

Reviewed `Rough Ranger`, `Shadow Crusher`, `Sudden Death Beam`, `Super Afterimage`, `Super God Shock Flash`, `Time Skip/Back Breaker`, `Time Skip/Flash Skewer`, `Time Skip/Jump Spike`, `Ultrasonic Blitz`, `Absolute Zero`, `Dragon Burn`, and `Explosive Wave`. Existing Future Warrior/dedicated technique references confirm these as usable techniques, but the checked evidence does not explicitly establish a race/gender restriction or unrestricted-race statement. No classifications were changed.

## 2026-09-19 — null-race batch: defensive/evasive skills

Reviewed `Force Shield`, `Instant Rise`, `Ki Explosion`, `Maiden Burst`, `Mighty Explosive Wave`, `Psychic Move`, `Punisher Guard`, `Side Bridge`, `Spread Shot Retreat`, `Steel Mirage`, `Final Pose`, and `Mach Dash`. The checked Future Warrior index and dedicated skill pages establish technique identity and Future Warrior availability. A secondary Future Warrior profile groups Force Shield and several other abilities under an “All Races” section, but this is not sufficiently direct to overwrite the canonical null race fields because it does not provide a skill-by-skill race-access statement. No classifications were changed.

## 2026-09-19 — null-race batch: barriers, counters, and offensive skills

Reviewed `Energy Barrier`, `Spirit Explosion`, `Spirit Slash`, `Atomic Blast`, `Blaster Ball`, `Bluff Kamehameha`, `Breaker Energy Wave`, `Burning Attack`, `Burst Kamehameha`, `Burst Stinger`, `Dark Inscription`, and `Demon Ray`. Dedicated/reference pages confirm Future Warrior use for the checked techniques, but the reviewed evidence does not provide sufficiently explicit individual race/gender restrictions or an individual “regardless of race” statement for these records. No `race_restriction` classifications were changed.

## 2026-09-19 — null-race batch: DLC/character-derived techniques

Reviewed `Destruction's Concerto: Comet`, `Destruction's Concerto: Starfall`, `Dimension Cannon`, `Double Death Slicer`, `Dust Attack`, `Earth Splitting Galick Gun`, `Emperor's Blast`, `Emperor's Cannon`, `Eraser Bomb`, `Evil Blast`, `Evil Flame`, and `Final Cannon`. Current dedicated/reference evidence confirms Future Warrior acquisition or use where documented, but does not establish sufficiently explicit individual race/gender restrictions for these records. The Future Warrior index also lists several of them without a race qualifier; omission is not treated as proof of universal access. No `race_restriction` fields were changed.

## 2026-09-19 — null-race batch: later DLC/mentor techniques

Reviewed `Flash Chaser`, `Gamma Blaster`, `Giant Cluster`, `Gigantic Charge`, `God of Destruction's Plaything`, `God Punisher`, `Handy Canon`, `Headshot`, `Heat Wave`, `Ill Rain`, `Paralysis`, and `Paralyze Beam`. Direct technique references were checked where available. Four records (`Flash Chaser`, `Gamma Blaster`, `God Punisher`, `Headshot`) received additional direct technique-page provenance; the evidence confirms Future Warrior acquisition/use but does not establish a new race restriction. No `race_restriction` values were changed for this cohort.

## 2026-09-19 — null-race batch: late offensive/evasion skills

Reviewed `Pendulum Bullet`, `Photon Swipe`, `Pretty Cannon`, `Raid Blast`, `Ray Blast`, `Reverse Shot`, `Rolling Bullet`, `Shine Shot`, `Spirit Blaster`, `Spirit Pulse`, `Stone Bullet`, and `Super Donut Volley`. Added direct technique-page provenance for `Photon Swipe`, confirming its Xenoverse 2 identity and Future Warrior acquisition from New Parallel Quest 139. The checked evidence does not establish a new individual race/gender restriction for the cohort, so no `race_restriction` values were changed.

## 2026-09-19 race-restriction census — next unresolved cohort

Recomputed the live canonical skill census before editing: **283 total / 270 CaC-usable / 183 CaC-usable with null `race_restriction`**. The earlier 186-count frontier is stale because Death Psycho Bomb, Justice Pose, and Crazy Finger Shot have since received explicit unrestricted-race classifications.

Reviewed the next 12 null-race CaC records: **Super Ghost Buu Attack, Variable Snipe Shot, Victory Cannon, Wild Buster, Dancing Parapara, Hero's Flute, Spirit Boost, Time Control, Charge, Divinity Unleashed, Do or Die, and Fighting Pose E**.

- Current Xenoverse 2 sources confirm Future Warrior acquisition/use for these records but do not provide sufficiently explicit individual race/gender/form restrictions for the canonical race field in this cohort.
- The official Dragon Ball site confirms Variable Snipe Shot as Android 18's Xenoverse 2 Super Attack, but does not establish CaC race access; it therefore cannot support a race classification for the canonical record.
- The accessible Xenoverse 2 technique list likewise identifies Future Warrior usage but explicitly warns that only some techniques have race/gender/transformation restrictions; omission is not treated as proof of universal access.
- Older Xenoverse (not Xenoverse 2) skill pages explicitly label some matching skills as usable by all races, including Time Control, Victory Cannon, Dancing Parapara, and Fighting Pose E. Because this audit is version-sensitive and the current Xenoverse 2 evidence does not independently establish that same restriction state, those older-game labels were **not** promoted into current Xenoverse 2 classifications.
- No `race_restriction` values were changed in this cohort. This is an evidence-boundary result, not an assumption that the skills are restricted.

Sources consulted include the accessible Future Warrior technique reference, dedicated Xenoverse 2 skill pages, the official Dragon Ball announcement for Variable Snipe Shot, and legacy Xenoverse skill pages used only to identify version-sensitive evidence boundaries.


## 2026-09-19 — null-race counter provenance batch

Reviewed the next unresolved cohort: **Burst Rush, Change The Future, Counter Burst, Counter Impact, Demon Flash Strike, Dimensional Hole, Flash Fist Crush, God Breaker, Heroic Counter, Punisher Shield, Reverse Mabakusenko, and Rough Ranger**. Dedicated Xenoverse 2 technique pages were added as direct provenance for **Counter Impact, Flash Fist Crush, God Breaker, Heroic Counter, Punisher Shield, and Rough Ranger**. These pages establish the technique identity, user/acquisition details, and mechanics, but do **not** provide an explicit CaC race/gender/form restriction or an explicit unrestricted-race statement. Consequently, all 12 records retain their existing null race_restriction values. Character ownership and the counter-skill category were not treated as race evidence.


## 2026-09-19 — counter/time-skip provenance batch

Reviewed the next unresolved null-race cohort: **Shadow Crusher, Sudden Death Beam, Super Afterimage, Super God Shock Flash, Time Skip/Back Breaker, Time Skip/Flash Skewer, Time Skip/Jump Spike, and Ultrasonic Blitz**. Added direct Xenoverse 2 technique-page provenance for all eight records. The checked pages document skill identity, unlock/acquisition, notable users, and mechanics; they do not explicitly establish CaC race/gender/form restrictions or universal race access. Therefore no race_restriction classifications were changed. Character ownership, mentor status, and category membership were not treated as race evidence. Shadow Crusher is specifically documented as obtained through Cooler training, while the three Time Skip skills are taught by Hit; those acquisition facts do not establish CaC race scope.


## 2026-09-19 — evasive-skill provenance boundary

Reviewed the next unresolved null-race cohort: **Absolute Zero, Dragon Burn, Explosive Wave, and Force Shield**. Existing direct Xenoverse 2 provenance was already present for Absolute Zero, Dragon Burn, and Force Shield; Explosive Wave received its direct Xenoverse 2 skill-page provenance. Current evidence identifies these as Evasive Skills and documents users/unlock information, but does not explicitly establish CaC race/gender/form restrictions or universal race access for these records. No `race_restriction` classifications were changed. The Evasive Skill category's CaC list was not treated as sufficient race-specific evidence.


## 2026-09-19 — evasive cohort and explicit CaC scope

Reviewed **Instant Rise, Ki Explosion, Maiden Burst, Mighty Explosive Wave, Psychic Move, Punisher Guard, Side Bridge, and Spread Shot Retreat**. Direct Xenoverse 2 pages were checked. **Ki Explosion** explicitly states that it is available for **all CaCs**, so its `race_restriction` was classified as `All CaC races` and `last_verified` set to `2026-09-19`. Instant Rise only states availability for CaCs without an all-races statement; the remaining reviewed pages identify NPC users/unlock data without explicit CaC race scope. Those records remain null. NPC ownership and broad Evasive Skill/category listings were not used as race evidence.


## 2026-09-19 — evasive/early-super provenance batch

Reviewed **Steel Mirage, Final Pose, Mach Dash, Energy Barrier, Spirit Explosion, Spirit Slash, Atomic Blast, and Blaster Ball**. The live data already had direct Xenoverse 2 provenance for seven; **Blaster Ball** received its missing dedicated Xenoverse 2 page URL. The available evidence reviewed does not explicitly establish CaC race/gender/form restrictions for these records, so no `race_restriction` values were changed. General Future Warrior lists, category membership, NPC ownership, and acquisition references were not promoted into race classifications.


## 2026-09-19 — early super provenance boundary

Reviewed **Bluff Kamehameha, Breaker Energy Wave, Burning Attack, and Burst Kamehameha** against current Xenoverse 2 sources. Breaker Energy Wave explicitly states it is available for CaCs, while Burst Kamehameha is documented as a Future Warrior reward; these establish CaC access but not an explicit race/gender/form scope. Bluff Kamehameha and Burning Attack likewise have current-version Future Warrior/custom-partner evidence but no explicit current-version race scope. Therefore no `race_restriction` values were changed. Older Xenoverse 1 race labels were not promoted into Xenoverse 2 classifications. No data provenance changes were necessary because all four already had dedicated current-version skill-page URLs in the canonical records.


## 2026-09-19 — super-skill evidence boundary

Reviewed **Burst Stinger, Dark Inscription, Demon Ray, and Destruction's Concerto: Comet** using current Xenoverse 2 skill/character pages. Burst Stinger is documented on Vegeta (Super Saiyan God), Dark Inscription on Golden Frieza (Ultra Supervillain), Demon Ray on Gohan (Beast), and Destruction's Concerto: Comet on Vados; these user associations do not by themselves establish CaC race/gender/form restrictions. The current sources did not provide explicit race scope for these records, so their null `race_restriction` values were preserved. Burst Stinger lacked a dedicated current-version provenance URL in the canonical record, so that URL was added. No race classifications were inferred from NPC identity or acquisition method.


## 2026-09-19 — next super-skill verification boundary

Reviewed **Destruction's Concerto: Starfall, Dimension Cannon, Double Death Slicer, and Dust Attack** against current Xenoverse 2 evidence. Starfall is documented as a Vados skill; Dimension Cannon as a Super Buu skill; Double Death Slicer as a Frieza (Full Power) skill; and the available canonical/current record for Dust Attack does not expose explicit CaC race/gender/form scope. These character associations and acquisition data do not establish a race restriction for CaCs. All four therefore retain null `race_restriction`. Their verification dates were refreshed to 2026-09-19. No new provenance URL was required.


## 2026-09-19 — Earth/Emperor cohort verification boundary

Reviewed **Earth Splitting Galick Gun, Emperor's Blast, Emperor's Cannon, and Eraser Bomb** against current Xenoverse 2 sources. Current records document named-character/custom-partner usage and/or acquisition, but the evidence reviewed does not explicitly establish a CaC race/gender/form restriction. For example, Earth Splitting Galick Gun is documented for Vegeta and multiple customize partners, while Emperor's Cannon is documented for Golden Frieza (Ultra Supervillain); neither establishes a CaC race restriction. Internal web citation markers omitted from repository text. All four therefore retain null `race_restriction`. Their verification dates were refreshed to 2026-09-19.


## 2026-09-19 — Evil/Flash provenance boundary

Reviewed **Evil Blast, Evil Flame, Final Cannon, and Flash Chaser** against current Xenoverse 2 evidence. Evil Blast is a Dabura counter obtainable by the Future Warrior and later usable by custom partners; Evil Flame is a Dabura skill obtainable by the Future Warrior and later available to a custom partner; Final Cannon is a Future Warrior reward and is available to multiple custom partners; Flash Chaser is a Future Warrior-obtainable Majuub skill and later a Goku (GT) custom-partner skill. These facts establish CaC access where documented, but do not explicitly establish a CaC race/gender/form restriction. All four therefore retain null `race_restriction`. Added dedicated current-version URLs for Evil Blast, Evil Flame, and Flash Chaser; refreshed verification dates for all four.


## 2026-09-19 — Gamma/Gigantic provenance boundary

Reviewed **Gamma Blaster, Giant Cluster, Gigantic Charge, and God of Destruction's Plaything** against current Xenoverse 2 evidence. Current records identify these as character/custom-partner or acquisition-linked skills, but the reviewed evidence does not explicitly establish a CaC race/gender/form restriction. Therefore all four retain null `race_restriction`. Added dedicated current-version provenance URLs for Giant Cluster and Gigantic Charge, and refreshed verification dates for the four records. No race inference was made from character identity or acquisition method.


## 2026-09-19 — God/Headshot provenance boundary

Reviewed **God Punisher, Handy Canon, Headshot, and Heat Wave** against current Xenoverse 2 evidence. God Punisher is documented as an SSGSS Gogeta skill, Handy Canon as an Android 13 skill obtainable from PQ 115, Headshot as Beerus's evasive skill, and Heat Wave as SS4 Goku (DAIMA)'s super skill from PQ 179. The reviewed evidence does not explicitly establish a CaC race/gender/form restriction for these records, so null `race_restriction` is preserved. Added dedicated current-version provenance URLs for God Punisher and Handy Canon and refreshed all four verification dates.


## 2026-09-19 — status/paralysis provenance boundary

Reviewed **Ill Rain, Paralysis, Paralyze Beam, and Pendulum Bullet** against current Xenoverse 2 evidence. The reviewed records establish current-version skill identity and acquisition/user context, but do not explicitly establish a CaC race/gender/form restriction. Null `race_restriction` is therefore preserved for all four. Added/normalized dedicated current-version provenance URLs for all four and refreshed their verification dates.


## 2026-09-19 — Photon/Raid provenance boundary

Reviewed **Photon Swipe, Pretty Cannon, Raid Blast, and Ray Blast** against current Xenoverse 2 evidence. The reviewed evidence establishes current-version skill identity and user/acquisition context but does not explicitly establish a CaC race/gender/form restriction. Null `race_restriction` is preserved for all four. Added dedicated current-version provenance URLs for all four and refreshed their verification dates.


## 2026-09-19 — Reverse/Spirit provenance boundary

Reviewed **Reverse Shot, Rolling Bullet, Shine Shot, and Spirit Blaster**. The current repository sources establish Xenoverse 2 skill identity and acquisition/user context, but the reviewed evidence does not explicitly establish CaC race/gender/form scope. Null `race_restriction` is therefore preserved for all four. Added dedicated current-version provenance URLs for Reverse Shot and Spirit Blaster and refreshed verification dates for all four. A fresh web search for current dbxv2 Fandom pages was blocked by robots.txt, so no unsupported external claim was substituted.


## 2026-09-19 — Spirit/Buu provenance boundary

Reviewed **Spirit Pulse, Stone Bullet, Super Donut Volley, and Super Ghost Buu Attack**. Current-version evidence establishes skill identity and user/acquisition context, but the reviewed evidence does not explicitly establish CaC race/gender/form scope. Null `race_restriction` is preserved for all four. Added dedicated current-version provenance URLs for Stone Bullet and Super Ghost Buu Attack and refreshed verification dates for all four. No race inference was made from NPC identity or acquisition method.


## 2026-09-19 — Fighting Pose/Burst boundary

Reviewed **Fighting Pose H, Formation!, Indomitable, Taunt, Blazing Attack, Brave Sword Slash, Burning Swan, and Burst Blitz** as the next unresolved CaC-usable null-race cohort. The reviewed current-version evidence did not establish an explicit CaC race/gender/form restriction or unrestricted-all-CaC statement sufficient to change `race_restriction`; all eight remain null. Verification dates were refreshed to 2026-09-19. No race inference was made from character association or acquisition context.


## 2026-09-19 — Death/Demon/Destruction boundary

Reviewed **Death Slash, Demon Flurry, Demonic Destruction, and Destruction's Conductor** as the next unresolved CaC-usable null-race cohort. Current-version sources identify their skill availability/association but do not provide an explicit race/gender/form restriction or explicit unrestricted-all-CaC statement sufficient to change `race_restriction`. All four remain null. Verification dates were refreshed to 2026-09-19. No race inference was made from mentor/character ownership or acquisition context.


## 2026-09-19 — Dragon/Emperor/Gamma boundary

Reviewed **Dragon Spark, Dragon Spiral, Emperor's Edge, Evil Whirlwind, Fierce Fist, Force Edge, Freedom Kick, and Gamma Impact** as the next unresolved CaC-usable null-race cohort. Current evidence establishes these as Xenoverse 2 skills but does not explicitly establish a race/gender/form restriction or unrestricted-all-CaC statement sufficient to change `race_restriction`. All eight remain null. Verification dates were refreshed to 2026-09-19. Dragon Spiral also received a dedicated current-version skill-page URL.


## 2026-09-19 — Gamma/Justice boundary

Reviewed **God of Destruction's Poise, Heroic Assault, Justice Blade, and Justice Drive** as the next unresolved CaC-usable null-race cohort. Current-version evidence confirms these Xenoverse 2 skills and their associated users/availability, but does not explicitly establish a race/gender/form restriction or an unrestricted-all-CaC statement sufficient to change `race_restriction`. All four remain null. Verification dates were refreshed to 2026-09-19.


## 2026-09-19 — Justice/Power boundary

Reviewed **Justice Kick, Lovely Cyclone, Mach Punch, Meteor Blow, Meteor Strike, Neo Wolf Fang Fist, Power Impact, and Powered Shell** as the next unresolved CaC-usable null-race cohort. Current-version evidence confirms skill identity/availability but does not explicitly establish a race/gender/form restriction or unrestricted-all-CaC statement sufficient to change `race_restriction`. All eight remain null. Verification dates were refreshed to 2026-09-19; dedicated dbxv2 Fandom provenance was added for Lovely Cyclone, Power Impact, and Powered Shell where absent.


## 2026-09-19 — Recoome/Sonic boundary

Reviewed **Recoome Kick, Sauzer Blade, Savory Slicer, Scissors Paper Rock, Seagull Combination, Shooting Strike, Soaring Rush, and Sonic Bomb** as the next unresolved CaC-usable null-race cohort. Current-version evidence confirms skill identity/availability but does not explicitly establish a race/gender/form restriction or unrestricted-all-CaC statement sufficient to change `race_restriction`. All eight remain null. Verification dates were refreshed to 2026-09-19; dedicated dbxv2 Fandom provenance was added for Savory Slicer where absent.


## 2026-09-19 — null-race cohort: Super God Fist through Circle Flash

Recomputed the live canonical skill census before editing: **283 total / 270 CaC-usable / 182 CaC-usable with null `race_restriction`**. Reviewed the next eight unresolved records after Sonic Bomb: **Super God Fist, Variant Drive, Apocalyptic Burst, Blaster Stream, Burning Blast, Chain Destructo-Disc Barrage, Chaotic Time Impact, and Circle Flash**.

- Added or normalized dedicated current-version Xenoverse 2 skill-page provenance for all eight records.
- Current evidence confirms skill identity, user/acquisition context, and mechanics, but the reviewed pages do **not** explicitly establish CaC race/gender/form scope or an explicit unrestricted-all-CaC statement for these records.
- Character ownership, Parallel Quest availability, partner customization, and skill-category membership were not treated as race evidence.
- No `race_restriction` classifications changed; all eight remain null. Verification dates were refreshed to **2026-09-19**.
- Web evidence included the dedicated Xenoverse 2 pages for Super God Fist, Variant Drive, Apocalyptic Burst, Blaster Stream, Burning Blast, Chain Destructo-Disc Barrage, Chaotic Time Impact, and Circle Flash. The sources document their current-version users and acquisition/skill data but do not supply the missing CaC race-scope statement. Internal web citation markers omitted from repository text.



## 2026-09-19 — class/provenance reconciliation: Core Breaker through Gigantic Breaker

A live evidence pass found several field-level classification errors in the next null-race cohort. Corrected the canonical records without inferring unsupported race restrictions:

- **Core Breaker:** corrected from Ki Blast to **Strike**, with 500 Ki; current evidence identifies it as Gamma 2's Strike Ultimate and explicitly says the Future Warrior can randomly obtain it from PQ158.
- **Destruction's Concerto: Meteor:** corrected from Ultimate to **Super**, with a 100–200 Ki range; current evidence identifies it as Vados's Ki Blast Super and says the Future Warrior can obtain it from PQ106.
- **Energy Field:** corrected from Ultimate to **Evasive** and restored its 200 Stamina cost; current evidence identifies it as a Ki Blast Evasive skill.
- **Gigantic Breaker:** corrected to **Super / Ki Blast**, 200 Ki; current evidence says the Future Warrior can obtain it as a random PQ126 reward.

These are classification/provenance corrections, not race-scope inferences. The four records remain without a `race_restriction` value because the reviewed evidence does not explicitly establish a CaC race/gender restriction or unrestricted race scope. Final Flash (SS3 DAIMA), Final Kamehameha, and Full Power Destruction remain queued for a separate explicit-CaC evidence pass.

Sources reviewed include the dedicated Xenoverse 2 skill pages and Future Warrior technique index; those sources support the Future Warrior acquisition/use statements and corrected skill classes above. 


## 2026-09-19 — explicit CaC-scope review: Final Flash (SS3 DAIMA), Final Kamehameha, Full Power Destruction

Reviewed the three queued Ultimate Ki Blast records against their dedicated current-version Xenoverse 2 pages. All three have their identity, classification, costs, and acquisition/user data documented, but the reviewed pages do not provide an explicit CaC race/gender/form scope statement. Accordingly, **no `race_restriction` value was inferred or changed**.

- **Final Flash (SS3 DAIMA):** PQ181; 400+ Ki; SS3 Vegeta (DAIMA); Ki Blast Ultimate. The page documents the attack and acquisition but does not explicitly establish CaC learnability.
- **Final Kamehameha:** TP Medal Shop / PQ91 / Double Crystal Raids; 500 Ki; Vegito/SSGSS Vegito users; Ki Blast Ultimate. User presets do not establish CaC race scope.
- **Full Power Destruction:** PQ177; 500 Ki; Jiren (Full Power) Ultra Supervillain / Jiren Customize Partner; Ki Blast Ultimate. Character/partner availability does not establish CaC race scope.

The canonical records now explicitly document this evidence boundary in their research notes and remain queued for stronger explicit CaC-scope evidence rather than speculative classification. 


## 2026-09-19 — queued skill classification reconciliation

Reviewed the next queued cohort. Four records received evidence-backed reconciliation:

- **Gigantic Burst:** confirmed as a 500-Ki Ki Blast Ultimate, PQ127, and explicitly documented as available for CaCs.
- **God of Destruction's Roar:** corrected from **Ultimate / Ki Blast / 300 Ki** to **Super / Strike / 100 Ki**. The dedicated page describes the move as a Champa Strike Super that drains Stamina.
- **God of Destruction's Menace:** confirmed as a 300-Ki Ki Blast Ultimate from PQ105 via the current Ultimate Attack index.
- **Gigantic Roar:** confirmed as a 500-Ki Ki Blast Ultimate from PQ132; no unsupported CaC race scope was inferred.

The remaining queued records (Gigantic Explosion, Heat Dome Attack, Holy Wrath, Last Emperor) remain pending stronger dedicated current-version evidence review.

## 2026-09-19 — Heat Dome / Zamasu / Last Emperor reconciliation

Reviewed four queued records against dedicated current-version skill pages:

- **Heat Dome Attack:** confirmed as a 300-Ki Ki Blast Ultimate from PQ40.
- **Holy Wrath:** corrected from Ultimate/300 Ki to **Super/100 Ki**; PQ111 and Ki Blast classification confirmed.
- **Last Emperor:** corrected from 300 Ki to **0 Ki**; confirmed as a health-gated Ki Blast Ultimate from PQ71.
- **Lightning of Absolution:** confirmed/corrected as a **100-Ki Ki Blast Super** from PQ111.

No CaC race/gender/form restriction was inferred from character-only users. The dedicated pages establish skill identity and acquisition but do not, by themselves, establish a specific CaC race scope.

## 2026-09-19 — counter-skill cohort evidence reconciliation

Reviewed the queued counter-skill cohort and refreshed the canonical evidence notes for **Burst Rush, Change The Future, Counter Burst, Counter Impact, Demon Flash Strike, Dimensional Hole, Flash Fist Crush, and God Breaker**. Current evidence supports their recorded skill classes, attack subcategories, Ki costs, counter roles, and listed acquisition sources. Counter Impact is specifically documented as a 100-Ki Ki Blast Super from PQ153; Burst Rush is a 100-Ki Strike Super from PQ51; Change The Future is a 100-Ki Ki Blast Super from PQ43; and God Breaker is a 100-Ki Ki Blast Super from PQ44. 

No CaC race/gender/form restriction was inferred from character or partner users. The canonical records now explicitly preserve that evidence boundary.

## 2026-09-19 — remaining counter-skill reconciliation

Reviewed **Heroic Counter, Punisher Shield, Reverse Mabakusenko, and Rough Ranger** against current dedicated skill pages. Confirmed their current classes, attack types, costs, counter roles, and acquisition sources. Heroic Counter is a 100-Ki Strike Super from PQ155; Punisher Shield is a 100-Ki Ki Blast Super from PQ129; Reverse Mabakusenko is a 300-Ki Ki Blast Ultimate from the Skill Shop; and Rough Ranger is a 100-Ki Strike Super from PQ119. 

No CaC race/gender/form restriction was inferred from their character users or partner customization data.

## 2026-09-19 — Mystic Flash / Requiem of Destruction review

Reviewed the two remaining records from the prior queue against dedicated current-version skill pages.

- **Mystic Flash:** confirmed as a **300-Ki Ki Blast Ultimate**, obtained from PQ20; notable users are Nail and customizable Piccolo.
- **Requiem of Destruction:** confirmed as a **300-Ki Ki Blast Ultimate**, obtained from PQ106; notable users are Vados and Whis Customize Partner.

Neither dedicated page explicitly establishes CaC race/gender/form scope, so no race restriction was inferred. 

## 2026-09-19 — Counter skill cohort continuation

Reconciled the next dataset-order cohort: Shadow Crusher, Sudden Death Beam, Super Afterimage, Super God Shock Flash, Time Skip/Back Breaker, Time Skip/Flash Skewer, Time Skip/Jump Spike, and Ultrasonic Blitz.

Dedicated current-version evidence confirms the classifications and 100-Ki costs for the reviewed skills, along with their acquisition routes where available. Hit's three Time Skip skills are mentor-training rewards; Ultrasonic Blitz is from PQ151; Shadow Crusher is from Cooler (Final Form) training; Super God Shock Flash is a Skill Shop skill. Sudden Death Beam retains its existing TP Medal Shop / STP Medal Shop / Double Crystal Raid acquisition record because a dedicated page could not be freshly retrieved in this pass.

No unsupported CaC race/gender/form restrictions were inferred.

## 2026-09-19 — Evasive skill cohort

Reconciled Absolute Zero, Celestial Wave, Dragon Burn, Explosive Wave, Force Shield, Instant Rise, Ki Explosion, and Maiden Burst against current skill-list evidence. Confirmed their Evasive classifications, stamina costs, and acquisition routes where documented. Force Shield was normalized to **Ki Blast** rather than Other. Existing explicit all-CaC-races coverage for Ki Explosion was retained; no unsupported race/gender/form restrictions were inferred for the other records.


## 2026-09-19 — Mixed Evasive cohort reconciliation

Reviewed Mighty Explosive Wave, Psychic Move, Punisher Guard, Side Bridge, Spread Shot Retreat, Steel Mirage, Final Pose, and Mach Dash against dedicated current-version pages.

Important metadata corrections: **Side Bridge** is a 100-Ki **Ki Blast Super** from PQ39, not an Evasive; **Steel Mirage** is a 100-Ki **Ki Blast Super** from PQ165, not an Evasive. Mighty Explosive Wave is documented as a Ki Blast Super/Evasive with 100 Ki for the attack and 300 Stamina for its Evasive function. The remaining records retain their Evasive classifications and current stamina costs. No unsupported CaC race/gender/form restrictions were inferred.


## 2026-09-19 — Shout, barrier, and Ki-skill cohort

Reconciled Angry Shout, Energy Barrier, Spirit Explosion, Spirit Slash, Atomic Blast, Bending Kamehameha, Big Bang Kamehameha, and Big Bang Knuckle against current skill evidence.

- Angry Shout retains its explicit **Pure Majin form** CaC restriction.
- Spirit Explosion and Spirit Slash are confirmed Strike Evasives at 200 Stamina (with the DBS Super Hero Spirit Slash variant at 300).
- Atomic Blast is confirmed as a 100-Ki Ki Blast Super from PQ87.
- Bending Kamehameha is a 100-Ki Skill Shop Ki Blast Super and retains its explicit all-CaC-races coverage.
- Big Bang Kamehameha is a 100-Ki TP Medal Shop Ki Blast Super and retains its explicit all-CaC-races coverage.
- Big Bang Knuckle is corrected to a **100-Ki Strike Super** from PQ172; the current evidence does not establish CaC acquisition, so it remains non-CaC.
- Energy Barrier remains a 300-Stamina Evasive; its barrier behavior is confirmed, but the attack-type field is retained pending stronger direct evidence.


## 2026-09-19 — Ki Blast Super cohort

Reconciled Blaster Ball, Bluff Kamehameha, Breaker Energy Wave, Burning Attack, Burst Kamehameha, Burst Stinger, Buu Buu Ball, and Candy Beam against current skill pages.

- Blaster Ball confirmed at **100–500 Ki** with repeated-input extension.
- Burning Attack confirmed at **100 Ki / PQ41**.
- Burst Kamehameha confirmed at **100–200 Ki / PQ72**, with additional input extending the beam.
- Buu Buu Ball retains its explicit **Pure Majin-form** restriction.
- Candy Beam retains its explicit **Majin CaC** restriction; its separate 200-Ki Candy Beam (Super) variant was not conflated with this 100-Ki record.
- No unsupported CaC race/gender/form restrictions were inferred for the remaining records.


## 2026-09-19 — Extended Ki Blast Super cohort

Reconciled Candy Beam (Super), Crazy Finger Shot, Dark Inscription, Death Psycho Bomb, Demon Ray, Destruction's Concerto: Comet, Destruction's Concerto: Starfall, and Destructo-Disc against current skill evidence.

- Candy Beam (Super) corrected to **200 Ki**; transformation/candy effect and all-CaC-races scope retained.
- Crazy Finger Shot confirmed **100 Ki**, extendable to 14 blasts with additional Ki expenditure.
- Dark Inscription confirmed **100+ Ki** with additional-input/Power of Time mechanics.
- Death Psycho Bomb confirmed **100 Ki** and psychic-grab/explosion behavior.
- Demon Ray confirmed **100 Ki / 300 Stamina** and its follow-up/use-while-hit mechanic.
- Destruction's Concerto: Comet confirmed **100–200 Ki** and tracking/conductor interaction.
- Destruction's Concerto: Starfall confirmed as the PQ104 Vados Super Skill with the two-sphere/conductor behavior.
- Destructo-Disc confirmed **100 Ki**, Krillin training acquisition, tracking and unblockable behavior.


## 2026-09-19 — Dimension/Divine/Emperor cohort

Reconciled Dimension Cannon, Divine Kamehameha, Divine Spear, Double Death Slicer, Dust Attack, Earth Splitting Galick Gun, Emperor's Blast, and Emperor's Cannon.

- Dimension Cannon confirmed at **300 Ki / PQ59**.
- Divine Kamehameha confirmed at **200 Ki**, TP Medal Shop, all CaC races.
- Divine Spear remains **not established as CaC-usable** in current evidence.
- Double Death Slicer confirmed at **100 Ki / PQ24**.
- Dust Attack remains flagged: the broad Super Attack index places it under **Other**, while the dataset currently carries a Ki Blast classification; direct skill-page reconciliation is still needed before changing the canonical class.
- Earth Splitting Galick Gun confirmed at **200 Ki / PQ11**; existing Ultimate Finish gate retained.
- Emperor's Blast confirmed at **100 Ki**.
- **Emperor's Cannon corrected from PQ183 to PQ184** based on its dedicated current skill page.


## 2026-09-19 — Eraser/Evil/Final/Gamma cohort

Reconciled Eraser Bomb, Evil Blast, Evil Flame, Final Cannon, Final Flash (Super), Flash Chaser, Galick Gun, and Gamma Blaster.

- Eraser Bomb confirmed **100 Ki / PQ163**.
- Evil Blast confirmed **100 Ki / PQ114**.
- Evil Flame confirmed **100 Ki / PQ117**.
- Final Cannon confirmed **100 Ki / PQ52**.
- Final Flash (Super) retained as **200 Ki / character-exclusive / not CaC-equippable**.
- Flash Chaser confirmed **100 Ki / PQ138**.
- Galick Gun confirmed **100 Ki / Vegeta mentor training / all CaC races**.
- Gamma Blaster confirmed **100 Ki / PQ155**.
- No unsupported race/gender/form restrictions were inferred.


## 2026-09-19 — Giant/God/Headshot/Heat cohort

Reconciled Giant Cluster, Gigantic Charge, God of Destruction's Plaything, God Punisher, Handy Canon, Headshot, Heat Wave, and Ill Bomber.

- **Gigantic Charge corrected:** 200 Ki / Strike Super / 300 Stamina while being hit, PQ128.
- **God Punisher corrected:** 400 Ki / Ki Blast Ultimate, PQ132; prior 100-Ki Super classification was incorrect.
- **Headshot corrected:** Strike Evasive / 300 Stamina / PQ69; prior Ki Blast Super classification was incorrect.
- **Heat Wave corrected:** 200 Ki / Strike Super / PQ179.
- Handy Canon confirmed 100 Ki / Ki Blast Super / PQ115.
- Ill Bomber confirmed 100 Ki / Ki Blast Super / PQ90 and restricted to Majin CaCs.
- Giant Cluster and God of Destruction's Plaything retained their existing costs while mechanics/restriction evidence remains bounded.


## 2026-09-19 — Ill Rain through Photon Swipe cohort

Reconciled Ill Rain, Kamehameha, Masenko, Paralysis, Paralyze Beam, Pendulum Bullet, Perfect Shot, and Photon Swipe. Confirmed classifications, costs, acquisition, and explicit CaC restrictions where supported; no unsupported race restrictions were inferred.


## 2026-09-19 — Pretty Cannon through Spirit Bomb cohort

Reconciled Pretty Cannon, Raid Blast, Ray Blast, Reverse Shot, Rolling Bullet, Shine Shot, Spirit Blaster, and Spirit Bomb.

- **Raid Blast:** corrected character source to Super Saiyan God Vegeta; retained 100-Ki Ki Blast Super and PQ136/Ultimate Finish requirement.
- **Spirit Blaster:** corrected character source to SSGSS Gogeta; retained 100-Ki Ki Blast Super and PQ129.
- **Rolling Bullet:** corrected from Super Ki Blast to **Ki Blast Evasive**, 200 Stamina, PQ42; Android 18/Great Saiyaman 2 users.
- Other cohort records retained their supported 100-Ki Super classifications/acquisition data.


## 2026-09-19 — Spirit Pulse through Wild Buster cohort

Reconciled Spirit Pulse, Stone Bullet, Super Donut Volley, Super Ghost Buu Attack, Vanishing Ball, Variable Snipe Shot, Victory Cannon, and Wild Buster.

- **Stone Bullet corrected:** Strike Super / 100 Ki / PQ56; charge extends range. Hercule's character implementation is a Ki Blast variant.
- **Victory Cannon corrected:** Ki Blast Evasive / 300 Stamina / PQ54.
- Spirit Pulse mechanics reconciled with current Ultra Instinct behavior.
- Variable Snipe Shot mechanics reconciled with the official Android 18 (DB Super) description.


## 2026-09-19 — Afterimage through Energy Release cohort

Reconciled Afterimage, Afterimage Strike, Assault Vanish, Burst Charge, Charged Ki Wave, Dancing Parapara, Energy Charge, and Energy Release.

- **Assault Vanish:** confirmed 100 Ki + 100 Stamina, PQ131, all CaC races.
- **Burst Charge:** confirmed rapid-start/slowdown charging behavior, PQ134, all CaC races.
- **Charged Ki Wave:** confirmed as a stamina-charging Other Super, PQ97.
- **Energy Release:** confirmed Towa-exclusive and non-CaC; it is a slow Ki-charging stance.
- Other movement/charge mechanics and explicit CaC provenance were reconciled without inferring unsupported race restrictions.


## 2026-09-19 — Final Charge through Petrifying Spit cohort

Reconciled Final Charge, Full Power Charge, Hero's Flute, Instant Charge, Instant Transmission, Kai Kai, Maximum Charge, and Petrifying Spit.

- Final Charge and Instant Charge retained as character/boss-exclusive, non-CaC skills.
- Full Power Charge and Maximum Charge confirmed as CaC charge skills from Advanced/God Class Advancement Tests.
- Hero's Flute confirmed as Tapion's 100-Ki barrier skill from PQ116.
- Instant Transmission confirmed as Goku Lesson 1, 0-resource teleport usable by all CaC races.
- Kai Kai confirmed as Whis's 100-Ki ally/partner teleport from PQ63.
- Petrifying Spit confirmed as Dabura's 100-Ki petrification skill from PQ114, usable by all CaC races.


## 2026-09-19 — Phantom Fist through Super Guard cohort

Reconciled Phantom Fist, Quick Sleep, Rise to Action, Rising Rage, Shield Barrier, Solar Flare, Spirit Boost, and Super Guard.

- Phantom Fist confirmed as 100-Ki PQ97 Other Super, all CaC races.
- Quick Sleep confirmed as 0-Ki Skill Shop Other Super, restricted to Majin CaCs.
- Rise to Action confirmed as 100-Ki Krillin mentor skill, all CaC races.
- Rising Rage retained as Restrained Broly-exclusive, non-CaC.
- Shield Barrier confirmed as 100-Ki PQ153 Other Super, all CaC races.
- Solar Flare confirmed as 100-Ki PQ01 Other Super, all CaC races.
- Spirit Boost confirmed as 0-Ki Skill Shop defensive barrier, usable by CaCs.
- Super Guard confirmed as 100-Ki base/Skill Shop barrier, all CaC races.


## 2026-09-19 — Surging Spirit through Divinity Unleashed cohort

Reconciled Surging Spirit, Time Bullet, Time Control, Ultimate Charge, Wall of Defense, Charge, Data Input, and Divinity Unleashed.

- Surging Spirit retained as Ultra Instinct-associated charging functionality, with current CaC access through the Awoken Skill action.
- Time Bullet retained as 100-Ki character-exclusive/non-CaC utility skill.
- Time Control confirmed as 100-Ki PQ18 Ultimate Finish reward and opponent-freeze skill.
- Ultimate Charge confirmed as 0-Ki PQ134 Ultimate Finish reward, all CaC races, with charge rate improving over time.
- Wall of Defense confirmed as 0-Ki PQ10 protective ally-intercept skill, all CaC races.
- Charge confirmed as 100-Ki Goku/PQ83 Power Up Super.
- Data Input confirmed as 100-Ki Expert Mission 20 auto-dodge skill, all CaC races.
- Divinity Unleashed corrected to 100 Ki and documented as the 100-Ki threshold charge/buff skill from PQ110.


## 2026-09-19 — Do or Die through Meditation cohort

Reconciled Do or Die, Fighting Pose E, Fighting Pose H, Fighting Pose K, Formation!, Indomitable, Justice Pose, and Meditation.

- Do or Die confirmed as 100-Ki/PQ49 with 10% damage reduction for 20 seconds.
- Fighting Pose E attribution corrected to Recoome; 0 Ki/PQ19, Basic Attack boost for 20 seconds.
- Fighting Pose H attribution corrected to Guldo; 0 Ki/PQ61, damage reduction for 20 seconds.
- Fighting Pose K confirmed as Recoome's 0-Ki Skill Shop Super Armor pose, 8-second duration.
- Formation! confirmed as Ribrianne's 100-Ki PQ133 Ultimate Finish skill with three documented duration levels.
- Indomitable retained as 0-Ki Future Saga Chapter 4 skill with health-sensitive Ki/Stamina charging; exact thresholds remain partially verified.
- Justice Pose confirmed as 0-Ki/PQ53 all-stat buff for 20 seconds.
- Meditation confirmed as 0-Ki/PQ122 maximum-Ki/auto-recovery buff with current 20-second duration; stacking interactions remain version-sensitive.


## 2026-09-19 — Taunt through Deadly Dance cohort

Reconciled Taunt, Blazing Attack, Brave Sword Slash, Burning Slash, Burning Swan, Burst Blitz, Crimson Edge, and Deadly Dance.

- Taunt confirmed as 0-Ki Hercule/PQ45 Power Up Super.
- Blazing Attack confirmed as 100-Ki Goku (Ultra Instinct)/PQ136 Ultimate Finish Strike Super.
- Brave Sword Slash confirmed as 100-Ki Tapion/PQ116 Strike Super, CaC-usable.
- Burning Slash confirmed as 100-Ki/PQ44 Strike Super restricted to Human/Earthling and Saiyan CaCs.
- Burning Swan confirmed as 100-Ki Videl/Future Saga Chapter 1 PQ167 Strike Super.
- Burst Blitz confirmed as 300-Ki Goku (Mini)/Future Saga Chapter 2 PQ178 Strike Super.
- Crimson Edge retained as 100-Ki Goku Black (Rosé) Ultra Supervillain Strike Super and non-CaC.
- Deadly Dance confirmed as 100-Ki Android 18 mentor Strike Super, all CaC races.


## 2026-09-19 — Deadly Dance through Emperor's Edge cohort

Reconciled the next eight dataset-order skills after Deadly Dance against current Xenoverse 2 evidence.

- **Death Slash:** Future Warrior/CaC availability is supported through the maintained Future Warrior technique index; no explicit CaC race/gender/form restriction was established, so the race field remains null.
- **Demon Flurry:** current skill evidence confirms the PQ160 acquisition and Future Warrior availability; no explicit CaC race/gender/form restriction was established.
- **Demonic Destruction:** current skill evidence confirms PQ159 acquisition and Future Warrior availability; no explicit CaC race/gender/form restriction was established.
- **Destruction's Conductor:** current evidence identifies it as a Future Warrior reward from PQ106; no explicit CaC race/gender/form restriction was established.
- **Dragon Spark:** current dedicated evidence confirms the PQ177 skill identity; it does not explicitly establish CaC race/gender/form scope, so the existing null restriction is preserved.
- **Dragon Spiral:** current Chapter 4/PQ185–186 evidence confirms the skill identity and CaC availability recorded in the dataset, but does not explicitly establish a CaC race/gender/form restriction.
- **Dragon Thunder:** corrected to **non-CaC**. Dedicated Xenoverse 2 evidence explicitly marks the Omega Shenron 100-Ki Strike Super as unavailable for CaCs; the prior all-CaC-races value was removed.
- **Emperor's Edge:** current evidence confirms Future Warrior availability; no explicit CaC race/gender/form restriction was established.

The live skill census remains **283 total / 269 CaC-usable / 182 CaC-usable with null race restriction**. The Dragon Thunder correction reduced CaC-usable count by one without changing the null-race count because its previous race field was populated.


## 2026-09-19 — Evasive-skill scope reconciliation after Side Bridge

Reconciled the next eight dataset-order records after Side Bridge: **Spread Shot Retreat, Steel Mirage, Final Pose, Mach Dash, Angry Shout, Energy Barrier, Spirit Explosion, and Spirit Slash**.

- Current evidence supports CaC availability for all eight records. No new race/gender/form restriction was inferred for Spread Shot Retreat, Steel Mirage, Final Pose, Mach Dash, Energy Barrier, Spirit Explosion, or Spirit Slash.
- **Angry Shout retains the explicit Pure Majin-form restriction.** The current Future Warrior technique index places Angry Shout under the Purification (Pure Majin) form-exclusive techniques. (current Future Warrior technique index reference)
- **Celestial Wave was also tightened during this pass:** its previous all-CaC-races value was removed because the reviewed current evidence establishes CaC availability but did not explicitly establish an all-races restriction. This is an evidence-boundary correction, not a change to CaC usability.
- Live census after the correction: **283 total / 269 CaC-usable / 183 CaC-usable with null race restriction**.
- No race restriction was inferred merely from character ownership, mentor source, PQ source, or inclusion in a generic Future Warrior technique list.


## 2026-09-19 — Atomic Blast through Burning Attack

Reconciled the next eight dataset-order records: **Atomic Blast, Bending Kamehameha, Big Bang Kamehameha, Big Bang Knuckle, Blaster Ball, Bluff Kamehameha, Breaker Energy Wave, and Burning Attack**.

- **Atomic Blast:** CaC-usable; current evidence does not explicitly establish a race/gender/form restriction, so the race field remains null.
- **Bending Kamehameha:** retained explicit `All CaC races` scope.
- **Big Bang Kamehameha:** retained explicit `All CaC races` scope. Current public documentation also confirms that the skill's historical behavior changed across updates; the repository records current-version mechanics rather than older teleport behavior. (current public update-history references)
- **Big Bang Knuckle:** corrected/retained as **non-CaC**. Current evidence identifies the PQ172 skill as Vegeta (Super Saiyan God) Ultra Supervillain's Strike Super, without an established CaC acquisition/equip path.
- **Blaster Ball, Bluff Kamehameha, Breaker Energy Wave, and Burning Attack:** CaC-usable; no explicit narrower CaC race/gender/form restriction was established, so no restriction was inferred.
- Live census after the Big Bang Knuckle correction: **283 total / 268 CaC-usable / 184 CaC-usable with null race restriction**.
- The public skill-ID evidence independently lists Atomic Blast and Burning Attack as CaC-usable, supporting the repository's scope classification. (public skill-ID reference)
