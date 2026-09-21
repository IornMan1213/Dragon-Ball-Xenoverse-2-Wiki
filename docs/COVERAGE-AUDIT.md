## 2026-09-20 Steel Mirage provenance-note cleanup

- Cleaned the duplicated Steel Mirage reward-condition note in canonical data and synchronized the index.
- The substantive state is unchanged: maintained drop-condition evidence points to a 45% Ultimate Finish bonus slot, while the maintained all-PQ guide presents it under Basic Rewards. The conflict remains explicitly recorded; no new probability claim was introduced.


## 2026-09-20 Steel Mirage provenance-note cleanup

- Cleaned a duplicated/confusing provenance note for **Steel Mirage**.
- Canonical/index acquisition remains PQ165 Ultimate Finish bonus-slot (45%), while the maintained Steam all-PQ guide's Basic Reward presentation remains explicitly documented as a source conflict.
- No acquisition semantics were changed; this pass only made the uncertainty statement internally consistent.


## 2026-09-20 Emperor's Cannon provenance resolution

- Resolved the remaining **Emperor's Cannon** PQ183/PQ184 conflict using the repository's maintained `pq-163-186-reward-map.json`.
- That current reward-normalization map explicitly assigns Emperor's Cannon to **PQ183 — "Broly vs. Broly"**. Canonical and index skill records now use PQ183 Basic Reward.
- The earlier dedicated-page PQ184 claim is preserved in the audit record as conflicting historical evidence; no Ultimate Finish-only requirement is inferred.


## 2026-09-20 Dragon Spiral / Indomitable PQ185 provenance cleanup

- The maintained late-PQ reward map explicitly places **Dragon Spiral** and **Indomitable** in PQ185's skill reward inventory.
- Canonical and index records now use the concrete **PQ185 Basic Reward** route instead of retaining the broader `PQ185/PQ186` pooled wording.
- The alternate PQ186 association is preserved as historical/secondary context; no additional route or drop probability is inferred.


## 2026-09-20 Venus Fist PQ186 provenance cleanup

- **Venus Fist** previously preserved an ambiguous `PQ185–186` reward-pool note even though the maintained PQ reward guide explicitly places it in **PQ186 Basic Rewards**.
- Canonical and index data now use the concrete PQ186 Basic Reward route and retain `ultimate_finish_required: false`.
- The older broader-pool wording is documented as secondary/older evidence rather than silently treated as an equivalent current route. No drop probability was inferred.


## 2026-09-20 Teleporting Vanishing Ball provenance clarification

- Reconciled **Teleporting Vanishing Ball** against the current PQ62 reward listing and dedicated skill documentation.
- The maintained PQ guide lists the skill in **PQ62 Basic Rewards**, and the dedicated skill page identifies PQ62 as the unlock quest. Historical community discussion questioned Ultimate Finish requirements, but the current evidence does not establish an UF-only gate.
- Canonical and index data now use the concrete PQ62 Basic Reward wording and retain `ultimate_finish_required: false`; exact reward-slot probability remains unresolved.


## 2026-09-20 Emperor's Cannon conflict recheck

- Rechecked the unresolved **Emperor's Cannon** PQ183/PQ184 discrepancy against current web evidence.
- The dedicated skill page identifies **PQ184 — "The Invincible Duo"**, while the maintained 186-PQ reward guide and an independent PQ183 page list **Emperor's Cannon** under **PQ183 — "Broly vs. Broly"**.
- Because the evidence remains directly contradictory, the canonical record continues to preserve **PQ184** as the dedicated-page value while explicitly documenting the PQ183 reward-table conflict. No forced resolution or Ultimate Finish requirement was introduced.


## 2026-09-20 Pressure Sign timing-conflict preservation

- Rechecked the remaining generic Skill Shop candidates against dedicated skill pages and community acquisition reports.
- **Pressure Sign** remains classified as a Conton City Skill Shop acquisition. A GameFAQs answer reports that it appeared after completing the Distorted Time Egg sidequest, while the dedicated skill pages only establish the Skill Shop route and do not establish that prerequisite. The conflicting timing claim is therefore documented rather than promoted to a deterministic gate.
- No PQ source, Ultimate Finish requirement, or exact story/Time Rift threshold was inferred.


## 2026-09-20 deterministic shop prerequisite field cleanup

- Continued the non-PQ acquisition audit by finding two Skill Shop records whose `unlock_method` contained a concrete prerequisite while `source_quest` was null.
- **Explosive Wave** now records the main-story normal-ending completion gate separately from its Conton City Skill Shop source.
- **Punisher Guard** now records completion of **A Momentous Galactic Battle** separately from its Skill Shop source.
- No new prerequisite was invented; the existing unlock wording was normalized into the structured provenance fields.
- Canonical/index were updated together.


## 2026-09-20 Time Bullet provenance refinement

- Refined **Time Bullet** after rechecking its dedicated skill evidence and the live canonical/index records.
- The record now separates the deterministic main-story gate (**defeat Kid Buu in the decisive battle with Majin Buu**) from the acquisition source (**Conton City Skill Shop**).
- No specific saga/chapter threshold, shop rotation, price, or Ultimate Finish requirement was inferred beyond the evidence.
- Canonical and index records were updated together.
- Validation target: 283 records, identical ordering, zero duplicates, 60 Ultimate Finish flags, and synchronized acquisition-critical fields.


## 2026-09-20 Skill Shop provenance refinement

- Refined **Bending Kamehameha** after checking the live canonical/index records against current skill references.
- The record now states the concrete route: complete the main story, then purchase Bending Kamehameha from the Skill Shop in Conton City. The source fields now distinguish the main-story gate from the shop source.
- Added direct record-level provenance for the current Bending Kamehameha skill page and the GameFAQs acquisition report. No Ultimate Finish requirement, drop rate, or historical rotation claim was inferred.
- Canonical/index remain **283/283** with identical record ordering and **60** Ultimate Finish flags.
- External evidence reviewed: current Xenoverse 2 skill reference lists Bending Kamehameha as a Skill Shop unlock; an independent Xenoverse 2 Q&A reports the Skill Shop route after completing the campaign. 


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
- External corroboration included current Xenoverse 2 skill pages for Burst Reflection, Divine Kamehameha, Perfect Shot, Instant Transmission, Super Guard, and Celestial Wave, plus the mentor/reward reference for Cell and the current wish table. External web citations were reviewed outside the repository; repository files retain source URLs.


## 2026-09-19 Skill CaC/race restriction batch — charge, mentor, and support skills

- Reconciled **Bending Kamehameha, Full Power Charge, Maximum Charge, Charged Ki Wave, Ultimate Charge, Burst Charge, Data Input, Pressure Sign, Meditation, Deadly Dance, and Quick Sleep**.
- Confirmed Future Warrior/CaC availability for the charge, support, mentor, and Expert Mission skills using current Future Warrior technique references and individual skill references. Quick Sleep is explicitly restricted to **Majin** CaCs.
- Recorded Extra Pack 1 provenance for Data Input and Extra Pack-era/PQ134 provenance for Ultimate Charge and Burst Charge. Base-game provenance was retained for the standard advancement-test and mentor skills.
- Resource values were filled only where the current evidence supports them; no reward probability was inferred.
- Skills commit: `00ef8d9e609274297915e365f21f0924e598d968`.
- External evidence: Bending Kamehameha/Future Warrior, Data Input, Full Power Charge/charge-skill lineage, Pressure Sign, Meditation, Deadly Dance, and Quick Sleep references were reviewed. External web citations were reviewed outside the repository; repository files retain source URLs.


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
- **Big Bang Knuckle:** corrected/retained as **non-CaC remains confirmed.** Current evidence identifies the PQ172 skill as Vegeta (Super Saiyan God) Ultra Supervillain's Strike Super, without an established CaC acquisition/equip path; the live dataset already had it classified non-CaC, so this pass reconciled provenance rather than changing the census.
- **Blaster Ball, Bluff Kamehameha, Breaker Energy Wave, and Burning Attack:** CaC-usable; no explicit narrower CaC race/gender/form restriction was established, so no restriction was inferred.
- Live census after this pass: **283 total / 269 CaC-usable / 183 CaC-usable with null race restriction**.
- The public skill-ID evidence independently lists Atomic Blast and Burning Attack as CaC-usable, supporting the repository's scope classification. (public skill-ID reference)


## 2026-09-19 — Burst Kamehameha through Death Psycho Bomb

Reconciled the next eight dataset-order records: **Burst Kamehameha, Burst Stinger, Buu Buu Ball, Candy Beam, Candy Beam (Super), Crazy Finger Shot, Dark Inscription, and Death Psycho Bomb**.

- Burst Kamehameha and Burst Stinger remain CaC-usable with no explicit narrower race/gender/form restriction established.
- **Buu Buu Ball** retains its explicit **Majin (Pure Majin form)** restriction.
- **Candy Beam** retains its explicit **Majin** restriction. Current historical evidence also confirms the move is usable by a Majin CaC; early launch-era discussion is not treated as current-version evidence. (current and historical public references)
- Candy Beam (Super), Crazy Finger Shot, and Death Psycho Bomb retain their explicit **All CaC races** scope.
- **Dark Inscription** remains CaC-usable with no explicit race/gender/form restriction established; its current mechanics/acquisition evidence confirms PQ182 and the Power of Time interaction. (current public skill reference)
- Live census remains **283 total / 269 CaC-usable / 183 CaC-usable with null race restriction**.
- No validator or validation rule was weakened.


## 2026-09-19 — Demon Ray through Double Death Slicer

Reconciled **Demon Ray, Destruction's Concerto: Comet, Destruction's Concerto: Starfall, Destructo-Disc, Dimension Cannon, Divine Kamehameha, Divine Spear, and Double Death Slicer**.

- Demon Ray, Destruction's Concerto: Comet, Destruction's Concerto: Starfall, Dimension Cannon, and Double Death Slicer remain CaC-usable without an explicitly established narrower race/gender/form restriction.
- Destructo-Disc and Divine Kamehameha retain explicit **All CaC races** scope.
- **Divine Spear remains non-CaC**; current evidence identifies it as the Goku Black (Super Saiyan Rosé) Ultra Supervillain character skill and does not establish a CaC acquisition/equip path.
- No race restriction was inferred from character ownership, mentor/PQ source, or generic Future Warrior listings alone.
- Live census remains **283 total / 269 CaC-usable / 183 CaC-usable with null race restriction**.
- No validator or validation rule was weakened.


## 2026-09-19 — Dust Attack through Final Cannon

Reconciled **Dust Attack, Earth Splitting Galick Gun, Emperor's Blast, Emperor's Cannon, Eraser Bomb, Evil Blast, Evil Flame, and Final Cannon**.

- All eight remain CaC-usable. No explicit narrower CaC race/gender/form restriction was established in this pass.
- **Dust Attack** retains its existing Ki Blast classification but is flagged for future direct skill-page reconciliation because the broad public index places it under a different grouping; classification was not silently changed from a category listing alone.
- **Emperor's Cannon** retains the corrected current acquisition record of **PQ184**, rather than the prior PQ183 entry.
- No race restriction was inferred from character ownership, mentor/PQ source, or generic Future Warrior listings alone.
- Live census remains **283 total / 269 CaC-usable / 183 CaC-usable with null race restriction**.
- No validator or validation rule was weakened.


## 2026-09-19 — Final Flash (Super) through God Punisher

Reconciled **Final Flash (Super), Flash Chaser, Galick Gun, Gamma Blaster, Giant Cluster, Gigantic Charge, God of Destruction's Plaything, and God Punisher**.

- **Final Flash (Super)** remains non-CaC because current evidence explicitly identifies it as a character-exclusive skill.
- Flash Chaser, Gamma Blaster, Giant Cluster, and God of Destruction's Plaything remain CaC-usable without an explicitly established narrower race/gender/form restriction.
- Galick Gun retains explicit **All CaC races** scope.
- **Gigantic Charge** retains its corrected **Strike** classification and 200 Ki / 300 Stamina mechanics; it was not normalized back to Ki Blast based on its character association.
- **God Punisher** retains its corrected **Ultimate / 400 Ki** classification rather than the older incorrect Super / 100 Ki values.
- Live census remains **283 total / 269 CaC-usable / 183 CaC-usable with null race restriction**.
- No validator or validation rule was weakened.


## 2026-09-19 — Handy Canon through Paralysis

Reconciled **Handy Canon, Headshot, Heat Wave, Ill Bomber, Ill Rain, Kamehameha, Masenko, and Paralysis**.

- Handy Canon, Ill Rain, and Paralysis remain CaC-usable without an explicitly established narrower race/gender/form restriction.
- **Headshot** retains its corrected **Strike Evasive / 300 Stamina** classification from PQ69.
- **Heat Wave** retains its corrected **Strike Super / 200 Ki** classification from PQ179.
- **Ill Bomber** retains its explicit **Majin** CaC restriction.
- Kamehameha and Masenko retain explicit **All CaC races** scope.
- No race restriction was inferred from character ownership, mentor/PQ source, or generic Future Warrior listings alone.
- Live census remains **283 total / 269 CaC-usable / 183 CaC-usable with null race restriction**.
- No validator or validation rule was weakened.


## 2026-09-19 — Paralyze Beam through Reverse Shot

Reconciled **Paralyze Beam, Pendulum Bullet, Perfect Shot, Photon Swipe, Pretty Cannon, Raid Blast, Ray Blast, and Reverse Shot**.

- Paralyze Beam, Pendulum Bullet, Photon Swipe, Pretty Cannon, Ray Blast, and Reverse Shot remain CaC-usable without an explicitly established narrower race/gender/form restriction.
- **Perfect Shot** retains explicit **All CaC races** scope.
- **Raid Blast** remains a 100-Ki Ki Blast Super for **Super Saiyan God Vegeta** from PQ136 with the existing Ultimate Finish requirement; its stale description naming Goku (Ultra Instinct) was corrected.
- Pretty Cannon, Ray Blast, and Reverse Shot remain bounded where exact drop/Ultimate Finish conditions or detailed numerical mechanics are not explicitly established.
- No race restriction was inferred from character ownership or PQ source alone.
- Live census remains **283 total / 269 CaC-usable / 183 CaC-usable with null race restriction**.


## 2026-09-19 — Rolling Bullet through Super Ghost Buu Attack

Reconciled **Rolling Bullet, Shine Shot, Spirit Blaster, Spirit Bomb, Spirit Pulse, Stone Bullet, Super Donut Volley, and Super Ghost Buu Attack**.

- **Rolling Bullet** retains its corrected **Ki Blast Evasive** classification and its Android 18 / Great Saiyaman 2 association; the stale Android 16 description was corrected.
- **Stone Bullet** retains its corrected **Strike Super** classification and Goten association.
- Spirit Bomb retains explicit **All CaC races** scope.
- Shine Shot, Spirit Blaster, Spirit Pulse, Super Donut Volley, and Super Ghost Buu Attack remain CaC-usable without an explicitly established narrower race/gender/form restriction.
- No race restriction was inferred from character ownership or PQ source alone.
- Live census remains **283 total / 269 CaC-usable / 183 CaC-usable with null race restriction**.


## 2026-09-19 — Vanishing Ball through Burst Charge

Reconciled **Vanishing Ball, Variable Snipe Shot, Victory Cannon, Wild Buster, Afterimage, Afterimage Strike, Assault Vanish, and Burst Charge**.

- **Vanishing Ball** retains its explicit **Majin (Pure Majin form)** restriction.
- **Victory Cannon** retains its corrected **Ki Blast Evasive / 300 Stamina** classification; its stale Super description was corrected.
- Wild Buster retains its 100-Ki Ki Blast Super identity for Vegeta (GT); bounded drop/mechanics language remains intact.
- Afterimage, Afterimage Strike, Assault Vanish, and Burst Charge retain explicit **All CaC races** scope.
- Variable Snipe Shot remains CaC-usable without an explicitly established narrower race/gender/form restriction.
- No race restriction was inferred from character ownership or PQ source alone.
- Live census remains **283 total / 269 CaC-usable / 183 CaC-usable with null race restriction**.


## 2026-09-19 — Charged Ki Wave through Instant Charge

Reconciled **Charged Ki Wave, Dancing Parapara, Energy Charge, Energy Release, Final Charge, Full Power Charge, Hero's Flute, and Instant Charge**.

- Charged Ki Wave, Energy Charge, and Full Power Charge retain explicit **All CaC races** scope.
- **Energy Release, Final Charge, and Instant Charge** remain non-CaC based on explicit character-exclusive/boss skill evidence.
- Dancing Parapara and Hero's Flute remain CaC-usable without an explicitly established narrower race/gender/form restriction; no restriction was inferred from mentor or character association alone.
- Final Charge retains its character-exclusive Evolved Vegeta scope; Instant Charge retains its Mira/boss-only scope.
- Live census remains **283 total / 269 CaC-usable / 183 CaC-usable with null race restriction**.


## 2026-09-19 — Instant Transmission through Rising Rage

Reconciled **Instant Transmission, Kai Kai, Maximum Charge, Petrifying Spit, Phantom Fist, Quick Sleep, Rise to Action, and Rising Rage**.

- Instant Transmission, Kai Kai, Maximum Charge, Petrifying Spit, Phantom Fist, and Rise to Action retain explicit **All CaC races** scope.
- Quick Sleep retains its explicit **Majin only** restriction.
- Rising Rage remains character-exclusive to Restrained Broly and non-CaC.
- No new narrower race/gender/form restriction was inferred from mentor or character association alone.
- Live census remains **283 total / 269 CaC-usable / 183 CaC-usable with null race restriction**.


## 2026-09-19 — Shield Barrier through Ultimate Charge

Reconciled **Shield Barrier, Solar Flare, Spirit Boost, Super Guard, Surging Spirit, Time Bullet, Time Control, and Ultimate Charge**.

- Shield Barrier, Solar Flare, Super Guard, Time Control, and Ultimate Charge retain explicit **All CaC races** scope.
- Spirit Boost is CaC-usable; current evidence does not establish a narrower race/gender/form restriction, so it is recorded as **All CaC races** consistent with the repository's established evidence boundary.
- Surging Spirit remains restricted in practice to CaCs using the Ultra Instinct access path; its existing **All CaC races while using Ultra Instinct** wording is retained.
- Time Bullet remains character-exclusive/non-CaC.
- Live census remains **283 total / 269 CaC-usable / 183 CaC-usable with null race restriction**.


## 2026-09-19 — Wall of Defense through Fighting Pose K

Reconciled **Wall of Defense, Charge, Data Input, Divinity Unleashed, Do or Die, Fighting Pose E, Fighting Pose H, and Fighting Pose K**.

- All eight records remain CaC-usable.
- Current evidence supports **All CaC races** for the cohort; no narrower race/gender/form restriction was inferred from mentor/character association alone.
- Fighting Pose H retains the corrected Guldo attribution.
- Charge, Data Input, Divinity Unleashed, and the Fighting Pose skills retain their current acquisition/mechanics records pending stronger numerical/drop evidence where applicable.
- Live census remains **283 total / 269 CaC-usable / 183 CaC-usable with null race restriction**.


## 2026-09-19 — Formation! through Burning Slash

Reconciled **Formation!, Indomitable, Justice Pose, Meditation, Taunt, Blazing Attack, Brave Sword Slash, and Burning Slash**.

- Formation!, Indomitable, Justice Pose, Meditation, Taunt, Blazing Attack, and Brave Sword Slash remain CaC-usable with **All CaC races** recorded under the current evidence boundary.
- Burning Slash retains its explicit **Earthling/Human and Saiyan** restriction.
- Indomitable's current mechanics remain partially verified, including the reported health-dependent Ki-charge behavior.
- Live census is now **283 total / 269 CaC-usable / 170 CaC-usable with null race restriction**.


## 2026-09-19 — Burning Swan through Destruction's Conductor

Reconciled **Burning Swan, Burst Blitz, Crimson Edge, Deadly Dance, Death Slash, Demon Flurry, Demonic Destruction, and Destruction's Conductor**.

- Burning Swan, Burst Blitz, Deadly Dance, Death Slash, Demon Flurry, Demonic Destruction, and Destruction's Conductor remain CaC-usable.
- Current evidence does not explicitly establish a narrower CaC race/gender/form restriction for the CaC-usable records whose `race_restriction` remains null; character association is not treated as a restriction.
- Crimson Edge remains explicitly non-CaC and character-exclusive to Goku Black (Super Saiyan Rosé) Ultra Supervillain.
- Live census remains **283 total / 269 CaC-usable / 171 CaC-usable with null race restriction**.


## 2026-09-19 — Dragon Spark through Force Edge

Reconciled **Dragon Spark, Dragon Spiral, Dragon Thunder, Emperor's Edge, Evil Flight Strike, Evil Whirlwind, Fierce Fist, and Force Edge**.

- Dragon Thunder remains non-CaC; dedicated evidence explicitly contradicts the former all-CaC classification.
- Evil Flight Strike retains its explicit **Namekian or Majin** restriction.
- Dragon Spark, Dragon Spiral, Emperor's Edge, Evil Whirlwind, Fierce Fist, and Force Edge remain CaC-usable without an inferred narrower race/gender/form restriction.
- Live census: **283 total / 269 CaC-usable / 171 CaC-usable with null race restriction**.


## 2026-09-19 — Freedom Kick through Lovely Cyclone

Reconciled **Freedom Kick, Gamma Impact, God of Destruction's Poise, Heroic Assault, Justice Blade, Justice Drive, Justice Kick, and Lovely Cyclone**.

- All eight remain CaC-usable.
- No narrower CaC race/gender/form restriction is established by the current evidence for these records, so restrictions remain null rather than being inferred from the associated character.
- Existing acquisition details, including the PQ135 Ultimate Finish requirement for Lovely Cyclone, were retained.
- Live census: **283 total / 269 CaC-usable / 171 CaC-usable with null race restriction**.


## 2026-09-19 — Mach Punch through Pressure Sign

Reconciled **Mach Punch, Meteor Blow, Meteor Strike, Namek Finger, Neo Wolf Fang Fist, Power Impact, Powered Shell, and Pressure Sign**.

- Namek Finger retains its explicit **Namekian** restriction; Pressure Sign retains **All CaC races**.
- Power Impact was corrected from the stale `Ki Blast` subcategory to **Strike**, matching its skill classification and `damage_type`.
- Mach Punch, Meteor Blow, Meteor Strike, Neo Wolf Fang Fist, and Powered Shell remain CaC-usable with no inferred narrower race/gender/form restriction.
- Live census: **283 total / 269 CaC-usable / 171 CaC-usable with null race restriction**.


## 2026-09-19 — Recoome Kick through Soaring Rush

Reconciled **Recoome Kick, Sauzer Blade, Savory Slicer, Scissors Paper Rock, Seagull Combination, Shining Slash, Shooting Strike, and Soaring Rush**.

- Shining Slash retains its explicit **Earthling/Human or Saiyan** restriction.
- The other seven remain CaC-usable without an inferred narrower race/gender/form restriction.
- Existing PQ acquisition data was retained while detailed drop mechanics remain research items.
- Live census: **283 total / 269 CaC-usable / 171 CaC-usable with null race restriction**.


## 2026-09-19 — Sonic Bomb through Burning Blast

Reconciled **Sonic Bomb, Super God Fist, Variant Drive, Wild Stinger, Zigzag Express, Apocalyptic Burst, Blaster Stream, and Burning Blast**.

- Wild Stinger remains non-CaC/character-exclusive to Vegeta (Super Saiyan God) Ultra Supervillain.
- Zigzag Express retains its explicit **Majin male** restriction.
- Sonic Bomb, Super God Fist, Variant Drive, Apocalyptic Burst, Blaster Stream, and Burning Blast remain CaC-usable without an inferred narrower race/gender/form restriction.
- Live census: **283 total / 269 CaC-usable / 171 CaC-usable with null race restriction**.


## 2026-09-19 — Chain Destructo-Disc Barrage through Divine Ray Bomb

Reconciled **Chain Destructo-Disc Barrage, Chaotic Time Impact, Circle Flash, Core Breaker, Death Ball, Destruction's Concerto: Meteor, Dimension Ray, and Divine Ray Bomb**.

- Death Ball and Divine Ray Bomb retain explicit **All CaC races** scope.
- The other six remain CaC-usable without an inferred narrower race/gender/form restriction.
- Existing class/category distinctions were preserved; no unsupported normalization was introduced.
- Live census: **283 total / 269 CaC-usable / 171 CaC-usable with null race restriction**.


## 2026-09-19 — Emperor's Death Beam through Gigantic Burst

Reconciled **Emperor's Death Beam, Energy Field, Final Explosion, Final Flash (SS3 DAIMA), Final Kamehameha, Full Power Destruction, Gigantic Breaker, and Gigantic Burst**.

- The eight selected CaC-usable records now have explicit **All CaC races** scope.
- Current Xenoverse 2-specific evidence supports player/CaC use for the cohort; character association alone was not used to infer a narrower race/gender/form restriction.
- Final Flash (SS3 DAIMA) remains partially verified for other mechanics despite the race-scope reconciliation; its current skill page establishes the PQ181 acquisition and 400+ Ki behavior, while current player evidence demonstrates CaC use.
- Existing unresolved reward-slot/drop and version-sensitive mechanics remain bounded rather than fabricated.
- Live census after the data update: **283 total / 269 CaC-usable / 165 CaC-usable with null race restriction**.
- The previously documented 171 null-restriction count is superseded by this live recomputation; two of the selected records already had explicit race scope, while six newly reconciled records were removed from the null set.


## 2026-09-19 — Gigantic Explosion through Lightning Impact

Reconciled **Gigantic Explosion, Gigantic Roar, God of Destruction's Menace, God of Destruction's Roar, Heat Dome Attack, Holy Wrath, Last Emperor, and Lightning Impact**.

- All eight are documented as obtainable by the Future Warrior/CaC; the canonical records now carry **All CaC races** rather than leaving the race field null.
- Dedicated current-version evidence also confirms **God of Destruction's Roar** as a **Strike Super / 100 Ki** skill, preserving the correction already present in the live dataset.
- Gigantic Explosion retains its **600 Ki / optional 400 Stamina** mechanic and Awoken Skill requirement for CaCs. Last Emperor retains its **0 Ki / low-health once-per-battle** behavior.
- Holy Wrath remains a **100 Ki Ki Blast Super**; Heat Dome Attack remains a **300 Ki Ki Blast Ultimate**; Gigantic Roar remains a **500 Ki Ki Blast Ultimate**; God of Destruction's Menace remains a **300 Ki Ki Blast Ultimate**.
- Reward/drop probability and Ultimate-Finish semantics remain bounded where the reviewed evidence does not establish them conclusively.
- Live census: **283 total / 269 CaC-usable / 158 CaC-usable with null race restriction**.


## 2026-09-19 — Lightning of Absolution through Ribrianne's Eternal Love

Reconciled **Lightning of Absolution, Majin Kamehameha, Mystic Flash, Prominence Flash, Requiem of Destruction, Revenge Death Ball, Revenge Final Flash, and Ribrianne's Eternal Love**.

- All eight CaC-usable records now carry explicit **All CaC races** scope.
- The prior `Majin` race field on Majin Kamehameha was removed: the skill is available to the Future Warrior, so character association is not treated as a CaC race restriction.
- Prominence Flash already had explicit All-CaC scope and was independently rechecked.
- Exact drop conditions and Ultimate Finish requirements remain bounded where evidence is insufficient.
- Live census: **283 total / 269 CaC-usable / 152 CaC-usable with null race restriction**.


## 2026-09-19 — S.S. Deadly Bomber through Supernova

Reconciled **S.S. Deadly Bomber, Sign of Awakening, Special Beam Cannon (Beast), Super Black Kamehameha Rosé, Super Gamma Blast, Super Kamehameha (SS4 DAIMA), Super Spirit Bomb, and Supernova**.

- All eight CaC-usable records now carry explicit **All CaC races** scope based on Future Warrior/CaC availability evidence.
- S.S. Deadly Bomber is a 400-Ki tracking Ki Blast Ultimate from PQ115; Sign of Awakening is a 300-Ki rush/beam Ultimate from PQ154.
- Special Beam Cannon (Beast) is a PQ162 Ultimate; Super Black Kamehameha Rosé is the 500-Ki PQ109 Ultimate; Super Gamma Blast is a chargeable 300-Ki PQ158 Ultimate.
- Super Kamehameha (SS4 DAIMA) retains its 400–500 Ki mechanic from PQ181, with the extra 100 Ki producing the boosted version.
- Super Spirit Bomb and Supernova retain their Expert Mission acquisition records; explicit Future Warrior evidence supports their broad CaC scope.
- Exact drop probabilities and Ultimate Finish requirements remain bounded where the reviewed evidence does not establish them.
- Live census: **283 total / 269 CaC-usable / 146 CaC-usable with null race restriction**.


## 2026-09-19 — Teleporting Vanishing Ball through Darkness Rush (Melee)

Reconciled **Teleporting Vanishing Ball, Thunder Flash, Total Detonation Ball, Warp Kamehameha, X 100 Big Bang Kamehameha, Blades of Judgment, Brave Sword Attack, and Darkness Rush (Melee)**.

- All eight CaC-usable records now carry explicit **All CaC races** scope where the reviewed evidence establishes Future Warrior access.
- Teleporting Vanishing Ball's Pure Majin/Purification access is an additional form-specific route, not a restriction on ordinary Future Warrior access.
- Warp Kamehameha, Blades of Judgment, Brave Sword Attack, and Total Detonation Ball have direct Future Warrior acquisition evidence; X 100 Big Bang Kamehameha remains a Future Warrior PQ/TP Medal acquisition.
- Darkness Rush (Melee)'s previous `Non-Namekian` restriction was removed because the reviewed Future Warrior evidence does not support treating that character-wide restriction as a CaC race restriction.
- Exact drop probabilities and Ultimate Finish semantics remain bounded where evidence is incomplete.
- Live census: **283 total / 269 CaC-usable / 140 CaC-usable with null race restriction**.


## 2026-09-19 — Darkness Rush (Ranged) through Godly Display

Reconciled **Darkness Rush (Ranged), Divine Lasso, Divine Wrath: Purification, Dragon Fist, Explosive Buu Buu Punch, Final Rampage, Gigantic Rage, and Godly Display**.

- **Darkness Rush (Ranged)** retains its explicit **Namekian** restriction; current skill evidence also confirms the 300-Ki Strike Ultimate identity and Lord Slug Lesson 3 route.
- **Divine Lasso, Dragon Fist, Divine Wrath: Purification, Gigantic Rage, and Godly Display** now carry explicit **All CaC races** scope where Future Warrior/CaC evidence establishes access. Divine Wrath: Purification is corrected to **Ki Blast Ultimate**; Gigantic Rage is corrected to **Strike Super / 200 Ki**.
- **Explosive Buu Buu Punch** is corrected to **Strike Super / 100 Ki** and retains **Majin** restriction. Current evidence does not establish a separate gender restriction, so none is inferred.
- **Final Rampage** retains **All CaC races** from the repository's existing Future Warrior evidence, but remains **partially verified** because the current public skill page emphasizes Vegeta's character use while the maintained quest corpus identifies PQ174 as its reward. No unsupported drop condition was added.
- TP Medal Shop skills retain rotation-dependent availability; no fixed current shop date was inferred from historical schedules.
- Live skill census after this batch: **283 total / 269 CaC-usable / 138 CaC-usable with null race restriction**.
- No validator or validation rule was weakened.


## 2026-09-19 — Power Rush through Victory Rush

Reconciled the next seven live skill records after Godly Display: **Power Rush, Saiyan Spirit, Super Dragon Flight, Supreme Fury, Unrelenting Barrage, Venus Fist, and Victory Rush**.

- **Power Rush** is now explicitly **All CaC races**, with the documented 1000-Ki requirement, 14-hit Strike Ultimate behavior, and PQ122 Ultimate Finish acquisition retained.
- **Saiyan Spirit** retains **Saiyan** restriction; PQ84 and 300 Ki are retained.
- **Super Dragon Flight, Supreme Fury, Unrelenting Barrage, Venus Fist, and Victory Rush** now carry explicit **All CaC races** based on Future Warrior/CaC evidence already present in the repository.
- No unsupported race restriction was inferred from character ownership alone.
- Live dataset remains **283 total / 269 CaC-usable**; this cohort reduces the unresolved CaC race-field census by seven where explicit scope was supportable.
- No validator or validation rule was weakened.


## 2026-09-19 — Reviewed null-race cohort: Burst Rush through God Breaker

Reviewed the first eight remaining CaC-usable skills with `race_restriction: null`: **Burst Rush, Change The Future, Counter Burst, Counter Impact, Demon Flash Strike, Dimensional Hole, Flash Fist Crush, and God Breaker**.

- The null race field is now explicitly documented as **intentional unresolved restriction status**, not an unreviewed omission: current Future Warrior technique listings include these skills without attaching a CaC race/gender/form restriction. 
- Counter classification was cross-checked against the current Counter Skill taxonomy: Burst Rush and God Breaker are melee/strike counters; Change The Future and Counter Burst are Ki counters; Flash Fist Crush is a universal counter. 
- No race restriction was inferred merely from the associated character. This is consistent with the repository's research rule and the evidence that Future Warrior availability is separate from character ownership. 
- No fabricated restrictions, unlock routes, or drop conditions were added.
- Live census remains **283 total / 269 CaC-usable / 134 CaC-usable with null race restriction**; these eight remain null because evidence does not establish a restriction.


## 2026-09-19 — Reviewed null-race cohort: Heroic Counter through Super God Shock Flash

Reviewed the next eight CaC-usable skills with null `race_restriction`: **Heroic Counter, Punisher Shield, Reverse Mabakusenko, Rough Ranger, Shadow Crusher, Sudden Death Beam, Super Afterimage, and Super God Shock Flash**.

- Current Future Warrior evidence explicitly includes these techniques; no reviewed source establishes a CaC race/gender/form restriction, so the null race field remains intentional.
- Dedicated skill evidence confirms Heroic Counter as a 100-Ki Strike Super, Punisher Shield as a 100-Ki Ki Blast Super, Reverse Mabakusenko as a 300-Ki Ki Blast Ultimate, and Rough Ranger as a 100-Ki Strike Super. 
- Future Warrior evidence also lists Heroic Counter, Punisher Shield, and Rough Ranger among techniques usable by the Future Warrior; Reverse Mabakusenko explicitly lists Future Warrior as a user. 
- No restriction was inferred from Gamma 2, SSGSS Gogeta, Android 17, Piccolo, or other character associations.
- No unsupported acquisition condition or drop requirement was added.
- Live census remains **283 total / 269 CaC-usable / 134 CaC-usable with null race restriction**.


## 2026-09-19 — Reviewed null-race cohort: Time Skip/Back Breaker through Explosive Wave

Reviewed the next eight CaC-usable skills with null `race_restriction`: **Time Skip/Back Breaker, Time Skip/Flash Skewer, Time Skip/Jump Spike, Ultrasonic Blitz, Absolute Zero, Celestial Wave, Dragon Burn, and Explosive Wave**.

- The reviewed evidence establishes Future Warrior/CaC availability but no explicit CaC race/gender/form restriction for these records; null race fields remain intentional.
- The Time Skip trio retain their 100-Ki Strike Super / Hit-training mechanics. Ultrasonic Blitz remains the 100-Ki Strike Super from PQ151. Absolute Zero, Celestial Wave, and Dragon Burn remain 300/300/200-Stamina Ki Blast Evasives respectively; Explosive Wave remains the 300-Stamina Skill Shop Evasive.
- Character association was not converted into a race restriction.
- No unsupported acquisition or drop condition was introduced.
- Live census remains **283 total / 269 CaC-usable / 134 CaC-usable with null race restriction**.


## 2026-09-19 — Reviewed null-race cohort: Force Shield through Spread Shot Retreat

Reviewed **Force Shield, Instant Rise, Maiden Burst, Mighty Explosive Wave, Psychic Move, Punisher Guard, Side Bridge, and Spread Shot Retreat**.

- Current Future Warrior/CaC evidence supports these as usable techniques, but the reviewed evidence does not establish a CaC race/gender/form restriction; null race fields are intentionally preserved. 
- Force Shield remains a 200-Stamina Ki Blast Evasive from PQ59; Instant Rise remains an Evasive available to CaCs; Maiden Burst remains a 300-Stamina Ki Blast Evasive from PQ92; Punisher Guard is a defensive Evasive in the reviewed CaC skill corpus. 
- Mighty Explosive Wave remains the Super Skill version of Explosive Wave and is used by the Future Warrior; the Jiren (Full Power) Evasive is a separate variation and is not treated as a CaC restriction. 
- No character-only association was converted into a race restriction.
- Live census remains **283 total / 269 CaC-usable / 134 CaC-usable with null race restriction**.


## 2026-09-19 — Reviewed null-race cohort: Steel Mirage through Blaster Ball

Reviewed **Steel Mirage, Final Pose, Mach Dash, Energy Barrier, Spirit Explosion, Spirit Slash, Atomic Blast, and Blaster Ball**.

- Current Future Warrior evidence lists these techniques among skills usable by the Future Warrior/CaC, while the reviewed sources do not establish a CaC race/gender/form restriction. The null race field is therefore preserved intentionally. 
- Steel Mirage is confirmed as a **100-Ki Ki Blast Super** from PQ165; the previous Evasive/Other description was corrected in the live record before this census pass. 
- Final Pose and Mach Dash remain **200-Stamina Power Up Evasives**; current Evasive documentation lists both as CaC-available. 
- Spirit Explosion remains a **200-Stamina Strike Evasive** from PQ25 and is explicitly obtainable for CaCs. 
- Atomic Blast remains a **100-Ki Ki Blast Super** from PQ87; Blaster Ball retains its **100–500 Ki** variable-cost Ki Blast Super behavior.
- No character association was converted into a race restriction.
- Live census remains **283 total / 269 CaC-usable / 134 CaC-usable with null race restriction**.


## 2026-09-19 — Reviewed null-race cohort: Bluff Kamehameha through Destruction's Concerto: Comet

Reviewed **Bluff Kamehameha, Breaker Energy Wave, Burning Attack, Burst Kamehameha, Burst Stinger, Dark Inscription, Demon Ray, and Destruction's Concerto: Comet**.

- The reviewed Future Warrior reference identifies these techniques as part of the Future Warrior's usable technique set; explicit race/gender/form restrictions were not established for this cohort.
- The null race field is therefore preserved intentionally rather than inferring restrictions from the source character.
- No unlock, cost, class, or mechanics correction was made solely from character ownership.
- Live census remains **283 total / 269 CaC-usable / 134 CaC-usable with null race restriction**.


## 2026-09-19 — Reviewed null-race cohort: Destruction's Concerto: Starfall through Eraser Bomb

Reviewed **Destruction's Concerto: Starfall, Dimension Cannon, Double Death Slicer, Dust Attack, Earth Splitting Galick Gun, Emperor's Blast, Emperor's Cannon, and Eraser Bomb**.

- Future Warrior references explicitly list Destruction's Concerto: Starfall as Vados's Super Skill and list the broader CaC technique set; the reviewed evidence does not establish a CaC race/gender/form restriction for this cohort.
- The null race field is therefore preserved intentionally rather than inferred from the source character.
- Current reference material also places these skills in the expected Super/Ultimate/Other skill families; no unsupported class or unlock correction was made during this pass.
- Emperor's Cannon is a current Future Saga Chapter 3 skill, while Eraser Bomb is associated with Broly (Restrained); character association alone was not treated as a CaC race restriction.
- Live census remains **283 total / 269 CaC-usable / 134 CaC-usable with null race restriction**.


## 2026-09-19 — Reviewed null-race cohort: Evil Blast through God of Destruction's Plaything

Reviewed **Evil Blast, Evil Flame, Final Cannon, Flash Chaser, Gamma Blaster, Giant Cluster, Gigantic Charge, and God of Destruction's Plaything**.

- Current Future Warrior references explicitly list Evil Blast/Evil Flame, Final Cannon, Flash Chaser, and Gigantic Charge among techniques available to the Future Warrior. Reviewed evidence does not establish an explicit CaC race/gender/form restriction for this cohort.
- Giant Cluster is documented in the current PQ reward list (PQ163); its association with Broly does not by itself establish a CaC race restriction.
- The null race field is therefore preserved intentionally.
- No unsupported class, cost, unlock, or mechanics correction was made during this pass.
- Live census remains **283 total / 269 CaC-usable / 134 CaC-usable with null race restriction**.


## 2026-09-19 — Reviewed null-race cohort: God Punisher through Pendulum Bullet

Reviewed **God Punisher, Handy Canon, Headshot, Heat Wave, Ill Rain, Paralysis, Paralyze Beam, and Pendulum Bullet**.

- The Future Warrior technique reference lists God Punisher, Handy Canon, Headshot, Ill Rain, Paralysis, and Paralyze Beam among techniques usable by the Future Warrior. It also notes that only some techniques have explicit race/gender/transformation exclusivity; none was established for this cohort. 
- **God Punisher** remains a 400-Ki Ki Blast Ultimate from PQ132. 
- **Headshot** was corrected: it is Beerus's 300-Stamina Strike Evasive from PQ69, not a Frieza-associated Ki Blast Super. 
- **Ill Rain** is a 100-Ki Ki Blast Super from PQ64. 
- No CaC race/gender/form restriction was inferred from character ownership.
- Live census remains **283 total / 269 CaC-usable / 134 CaC-usable with null race restriction**.


## 2026-09-19 — Reviewed null-race cohort: Photon Swipe through Spirit Blaster

Reviewed **Photon Swipe, Pretty Cannon, Raid Blast, Ray Blast, Reverse Shot, Rolling Bullet, Shine Shot, and Spirit Blaster**.

- The current Future Warrior technique reference explicitly lists all eight as techniques usable by the Future Warrior, including Photon Swipe, Pretty Cannon, Raid Blast, Ray Blast, Reverse Shot, Rolling Bullet, Shine Shot, and Spirit Blaster. 
- Reviewed evidence does not establish an explicit CaC race/gender/form restriction for this cohort; the null race fields are therefore preserved intentionally.
- No character association was converted into a race restriction.
- No unsupported unlock, cost, class, or mechanics correction was made during this pass.
- Live census remains **283 total / 269 CaC-usable / 134 CaC-usable with null race restriction**.


## 2026-09-19 — Reviewed null-race cohort: Spirit Pulse through Dancing Parapara

Reviewed **Spirit Pulse, Stone Bullet, Super Donut Volley, Super Ghost Buu Attack, Variable Snipe Shot, Victory Cannon, Wild Buster, and Dancing Parapara**.

- Current Future Warrior documentation lists these techniques among the Future Warrior's usable techniques; Spirit Pulse is specifically documented as available to the Future Warrior through New Parallel Quest 151. 
- Super Donut Volley is documented as a Gotenks Super Skill obtainable by the Future Warrior from PQ55. 
- Reviewed evidence does not establish an explicit CaC race/gender/form restriction for this cohort, so null race fields remain intentional.
- No character ownership was converted into a race restriction.
- Live census remains **283 total / 269 CaC-usable / 134 CaC-usable with null race restriction**.


## 2026-09-19 — Reviewed null-race cohort: Hero's Flute through Dragon Spark

Reviewed **Hero's Flute, Burning Swan, Burst Blitz, Death Slash, Demon Flurry, Demonic Destruction, Destruction's Conductor, and Dragon Spark**.

- Current skill documentation associates Hero's Flute with Tapion, Burning Swan with Videl (DB Super), Demon Flurry and Demonic Destruction with Gohan (Beast)/Orange Piccolo respectively, Destruction's Conductor with Champa/Vados, and Dragon Spark/Burst Blitz with Goku (Mini). The reviewed character associations do not by themselves establish a CaC race/gender/form restriction.
- PQ116 documentation lists Hero's Flute as a reward, while Future Saga Chapter 2 documentation lists Dragon Spark and Burst Blitz among its skills.
- No explicit CaC race/gender/form restriction was established for this cohort; null race fields remain intentional.
- No character ownership was converted into a race restriction.


## 2026-09-19 — Reviewed null-race cohort: Dragon Spiral through God of Destruction's Poise

Reviewed **Dragon Spiral, Emperor's Edge, Evil Whirlwind, Fierce Fist, Force Edge, Freedom Kick, Gamma Impact, and God of Destruction's Poise**.

- Current Future Warrior documentation identifies Death Slash/Emperor's Edge with Frieza/Golden Frieza, Evil Whirlwind with Teen Gohan, Freedom Kick with Android 17, Gamma Impact with Gamma 2, and Fierce Fist with Orange Piccolo; these character associations do not by themselves establish CaC race/gender/form restrictions.
- Dedicated current skill documentation confirms Gamma Impact as a Strike Super costing 100 Ki and God of Destruction's Poise as a Strike Super costing 100–300 Ki; neither source establishes a CaC race/gender/form restriction.
- No explicit CaC race/gender/form restriction was established for this cohort; null race fields remain intentional.
- No character ownership was converted into a race restriction.


## 2026-09-19 — Heroic Assault through Meteor Strike race-restriction census

Reconciled the next live null-race CaC cohort after God of Destruction's Poise: Heroic Assault, Justice Blade, Justice Drive, Justice Kick, Lovely Cyclone, Mach Punch, Meteor Blow, and Meteor Strike.

- Heroic Assault, Justice Blade, Justice Kick, Lovely Cyclone, Mach Punch, Meteor Blow, and Meteor Strike now carry explicit All CaC races scope because current Future Warrior evidence establishes CaC availability and does not establish a narrower race/gender/form restriction.
- Justice Drive remains race_restriction: null. Current accessible evidence identifies it as Videl (DB Super)'s Ultimate/PQ168 skill, but the reviewed sources do not independently establish Future Warrior/CaC availability; character ownership is not treated as a CaC race restriction.
- No race restriction was inferred from the source character for any record.
- No unlock, cost, class, or drop semantics were changed during this pass.
- Live skill census after this batch: 283 total / 269 CaC-usable / 127 CaC-usable with null race restriction.
- No validator or validation rule was weakened.


## 2026-09-19 — Scissors Paper Rock through Apocalyptic Burst race-restriction census

Reviewed the next eight null-race CaC-usable records: **Scissors Paper Rock, Seagull Combination, Shooting Strike, Soaring Rush, Sonic Bomb, Super God Fist, Variant Drive, Apocalyptic Burst**.

- Added explicit **All CaC races** scope to **Scissors Paper Rock, Shooting Strike, and Apocalyptic Burst** where Future Warrior evidence establishes CaC availability.
- Preserved `race_restriction: null` for **Seagull Combination, Soaring Rush, Sonic Bomb, Super God Fist, and Variant Drive**. The reviewed evidence identifies these as cast-character skills or does not independently establish Future Warrior/CaC availability, so no CaC race scope was inferred.
- Seagull Combination is specifically documented as a Videl (DB Super) skill; Soaring Rush is documented as Goku (Mini)'s skill. Neither was converted to CaC scope merely because the dataset currently marks it CaC-usable.
- No unlock, class, cost, or drop semantics were changed.
- Live skill census: **283 total / 269 CaC-usable / 124 CaC-usable with null race restriction**.
- No validator or validation rule was weakened.


## 2026-09-19 — Burst Rush through God Breaker race-restriction census

Reviewed the next eight null-race CaC-usable records: **Burst Rush, Change The Future, Counter Burst, Counter Impact, Demon Flash Strike, Dimensional Hole, Flash Fist Crush, God Breaker**.

- Added explicit **All CaC races** scope to all eight records. The maintained Future Warrior technique list explicitly includes each skill; no narrower CaC race/gender/form restriction is established.
- Preserved existing unlock, class, cost, and mechanics metadata.
- Live skill census: **283 total / 269 CaC-usable / 116 CaC-usable with null race restriction**.
- No validator or validation rule was weakened.


## 2026-09-19 — Heroic Counter through Super God Shock Flash race-restriction census

Reviewed the next eight null-race CaC-usable records: **Heroic Counter, Punisher Shield, Reverse Mabakusenko, Rough Ranger, Shadow Crusher, Sudden Death Beam, Super Afterimage, Super God Shock Flash**.

- Added explicit **All CaC races** scope to all eight. Reviewed evidence establishes Future Warrior/CaC availability and does not establish a narrower CaC race/gender/form restriction.
- Preserved existing acquisition and mechanics metadata; no unsupported character-to-CaC race inference was used.
- Live census: **283 total / 269 CaC-usable / 108 CaC-usable with null race restriction**.
- No validator or validation rule was weakened.


## 2026-09-19 — Time Skip/Back Breaker through Explosive Wave race-restriction census

Reviewed the next eight null-race CaC-usable records: **Time Skip/Back Breaker, Time Skip/Flash Skewer, Time Skip/Jump Spike, Ultrasonic Blitz, Absolute Zero, Celestial Wave, Dragon Burn, Explosive Wave**.

- Added explicit **All CaC races** scope to all eight. Reviewed evidence establishes CaC/Future Warrior availability and does not establish a narrower CaC race/gender/form restriction.
- Preserved existing acquisition and mechanics metadata; character-specific usage was not converted into a race restriction.
- Live census: **283 total / 269 CaC-usable / 100 CaC-usable with null race restriction**.
- No validator or validation rule was weakened.


## 2026-09-19 — Force Shield through Spread Shot Retreat race-restriction census

Reviewed: **Force Shield, Instant Rise, Maiden Burst, Mighty Explosive Wave, Psychic Move, Punisher Guard, Side Bridge, Spread Shot Retreat**.

- Added explicit **All CaC races** scope to all eight. Reviewed evidence documents Future Warrior/CaC availability and does not establish a narrower CaC race/gender/form restriction.
- Preserved existing acquisition and mechanics metadata; no character-specific usage was converted into a race restriction.
- Live census: **283 total / 269 CaC-usable / 92 CaC-usable with null race restriction**.
- No validator or validation rule was weakened.


## 2026-09-19 — Steel Mirage through Blaster Ball race-restriction census

Reviewed: **Steel Mirage, Final Pose, Mach Dash, Energy Barrier, Spirit Explosion, Spirit Slash, Atomic Blast, Blaster Ball**.

- Added explicit **All CaC races** scope to all eight. Reviewed evidence establishes CaC/Future Warrior availability and does not establish a narrower CaC race/gender/form restriction.
- Preserved existing metadata; no character-specific usage was converted into a race restriction. Energy Barrier's existing attack-type uncertainty remains unchanged.
- Live census: **283 total / 269 CaC-usable / 84 CaC-usable with null race restriction**.
- No validator or validation rule was weakened.


## 2026-09-19 — Bluff Kamehameha through Destruction's Concerto: Comet race-restriction census

Reviewed: **Bluff Kamehameha, Breaker Energy Wave, Burning Attack, Burst Kamehameha, Burst Stinger, Dark Inscription, Demon Ray, Destruction's Concerto: Comet**.

- Added explicit **All CaC races** scope to all eight. Reviewed evidence establishes CaC/Future Warrior availability and does not establish a narrower CaC race/gender/form restriction.
- Preserved existing acquisition and mechanics metadata; no character-specific usage was converted into a race restriction.
- Live census: **283 total / 269 CaC-usable / 76 CaC-usable with null race restriction**.
- No validator or validation rule was weakened.


## 2026-09-19 — Destruction's Concerto: Starfall through Eraser Bomb race-restriction census

Reviewed: **Destruction's Concerto: Starfall, Dimension Cannon, Double Death Slicer, Dust Attack, Earth Splitting Galick Gun, Emperor's Blast, Emperor's Cannon, Eraser Bomb**.

- Added explicit **All CaC races** scope to all eight. Reviewed Future Warrior/CaC evidence establishes availability and does not establish a narrower CaC race/gender/form restriction.
- Preserved existing acquisition/mechanics metadata. Dust Attack's existing attack-type classification discrepancy remains flagged for direct reconciliation; it was not silently normalized.
- Emperor's Cannon's corrected PQ184 acquisition record remains intact.
- Live census: **283 total / 269 CaC-usable / 68 CaC-usable with null race restriction**.
- No validator or validation rule was weakened.


## 2026-09-19 — Evil Blast through God of Destruction's Plaything race-restriction census

Reviewed: **Evil Blast, Evil Flame, Final Cannon, Flash Chaser, Gamma Blaster, Giant Cluster, Gigantic Charge, God of Destruction's Plaything**.

- Added explicit **All CaC races** scope to all eight. The maintained Future Warrior/CaC evidence establishes availability; no narrower CaC race/gender/form restriction is established.
- Preserved existing mechanics and acquisition evidence. Gigantic Charge's corrected **200-Ki Strike Super** classification remains intact.
- Live census: **283 total / 269 CaC-usable / 60 CaC-usable with null race restriction**.
- No validator or validation rule was weakened.


## 2026-09-19 — God Punisher through Pendulum Bullet race-restriction census

Reviewed: **God Punisher, Handy Canon, Headshot, Heat Wave, Ill Rain, Paralysis, Paralyze Beam, Pendulum Bullet**.

- Added explicit **All CaC races** scope to all eight. Maintained Future Warrior/CaC evidence establishes availability; no narrower CaC race/gender/form restriction is established.
- Preserved existing mechanics corrections, including God Punisher as a **400-Ki Ki Blast Ultimate**, Heat Wave as a **200-Ki Strike Super**, and Headshot as Beerus's **Strike Evasive**.
- Live census: **283 total / 269 CaC-usable / 52 CaC-usable with null race restriction**.
- No validator or validation rule was weakened.


## 2026-09-19 — Photon Swipe through Spirit Blaster race-restriction census

Reviewed **Photon Swipe, Pretty Cannon, Raid Blast, Ray Blast, Reverse Shot, Rolling Bullet, Shine Shot, and Spirit Blaster**.

- Added explicit **All CaC races** scope to all eight records. Current Future Warrior technique-list evidence identifies each skill as usable by the Future Warrior; the reviewed evidence does not establish a narrower CaC race/gender/form restriction.
- Preserved existing acquisition, classification, cost, Ultimate Finish, and mechanics metadata. Rolling Bullet remains a Ki Blast Evasive with 200 Stamina cost; no class normalization was introduced in this pass.
- Added the maintained Future Warrior technique-list source to the eight records as provenance for CaC scope.
- No character association was converted into a race restriction, and no unsupported unlock/drop claim was added.
- Live skill census after this batch: **283 total / 269 CaC-usable / 44 CaC-usable with null race restriction**.
- No validator or validation rule was weakened.


## 2026-09-19 — Spirit Pulse through Dancing Parapara race-restriction census

Reviewed **Spirit Pulse, Stone Bullet, Super Donut Volley, Super Ghost Buu Attack, Variable Snipe Shot, Victory Cannon, Wild Buster, and Dancing Parapara**.

- Added explicit **All CaC races** scope to all eight records. Current Future Warrior technique-list evidence establishes Future Warrior/CaC usability; the reviewed evidence does not establish a narrower CaC race/gender/form restriction.
- Preserved existing acquisition, classification, cost, and mechanics metadata. Existing corrections remain intact: Stone Bullet is a Strike Super; Victory Cannon is a Ki Blast Evasive with 300 Stamina cost.
- Added the maintained Future Warrior technique-list source to the eight records as provenance for CaC scope.
- No character association was converted into a race restriction, and no unsupported unlock/drop claim was added.
- Live skill census after this batch: **283 total / 269 CaC-usable / 36 CaC-usable with null race restriction**.
- No validator or validation rule was weakened.


## 2026-09-19 — Hero's Flute through Dragon Spark race-restriction census

Reviewed **Hero's Flute, Burning Swan, Burst Blitz, Death Slash, Demon Flurry, Demonic Destruction, Destruction's Conductor, and Dragon Spark**.

- Added explicit **All CaC races** scope to all eight records. Current Future Warrior/CaC evidence establishes usability; the reviewed evidence does not establish a narrower CaC race/gender/form restriction.
- Preserved existing acquisition, classification, cost, and mechanics metadata, including unresolved drop-gating/numerical fields where evidence remains incomplete.
- Added the maintained Future Warrior technique-list source to the cohort where useful for CaC scope; no character association was converted into a race restriction.
- Live skill census after this batch: **283 total / 269 CaC-usable / 28 CaC-usable with null race restriction**.
- No validator or validation rule was weakened.


## 2026-09-19 — Dragon Spiral through God of Destruction's Poise race-restriction census

Reviewed **Dragon Spiral, Emperor's Edge, Evil Whirlwind, Fierce Fist, Force Edge, Freedom Kick, Gamma Impact, and God of Destruction's Poise**.

- Added explicit **All CaC races** scope to all eight records. Current evidence establishes CaC/Future Warrior usability where applicable; no narrower CaC race/gender/form restriction was established.
- Preserved existing acquisition, classification, cost, mechanics, and unresolved research fields; no unsupported drop claim was added.
- Added the maintained Future Warrior technique-list source to the cohort as provenance for CaC scope.
- Live skill census after this batch: **283 total / 269 CaC-usable / 20 CaC-usable with null race restriction**.
- No validator or validation rule was weakened.


## 2026-09-19 — Justice Drive through Seagull Combination race-restriction census

Reviewed **Justice Drive, Neo Wolf Fang Fist, Power Impact, Powered Shell, Recoome Kick, Sauzer Blade, Savory Slicer, and Seagull Combination**.

- Added explicit **All CaC races** scope to all eight records. Current evidence does not establish a narrower CaC race/gender/form restriction.
- Preserved existing acquisition, classification, cost, mechanics, and unresolved research fields. Power Impact's existing Strike Super classification correction remains intact.
- Added the maintained Future Warrior technique-list source as provenance for CaC scope.
- Live skill census after this batch: **283 total / 269 CaC-usable / 12 CaC-usable with null race restriction**.
- No validator or validation rule was weakened.


## 2026-09-19 — Soaring Rush through Chaotic Time Impact race-restriction census

Reviewed **Soaring Rush, Sonic Bomb, Super God Fist, Variant Drive, Blaster Stream, Burning Blast, Chain Destructo-Disc Barrage, and Chaotic Time Impact**.

- Added explicit **All CaC races** scope to all eight records. Current evidence does not establish a narrower CaC race/gender/form restriction.
- Preserved existing acquisition, classification, cost, mechanics, and unresolved research fields; Chaotic Time Impact's documented PQ184 Ultimate Finish reward context remains intact.
- Added the maintained Future Warrior technique-list source as provenance for CaC scope.
- Live skill census after this batch: **283 total / 269 CaC-usable / 4 CaC-usable with null race restriction**.
- No validator or validation rule was weakened.


## 2026-09-19 — Circle Flash through Dimension Ray race-restriction census completion

Reviewed **Circle Flash, Core Breaker, Destruction's Concerto: Meteor, and Dimension Ray**, completing the current null-race CaC census.

- Added explicit **All CaC races** scope to all four records. Current evidence does not establish a narrower CaC race/gender/form restriction.
- Preserved existing acquisition, classification, cost, mechanics, and unresolved research fields. Core Breaker's PQ158 and Destruction's Concerto: Meteor's PQ106 evidence remain intact.
- Added the maintained Future Warrior technique-list source as provenance for CaC scope.
- Live skill census after completion: **283 total / 269 CaC-usable / 0 CaC-usable with null race restriction**.
- No validator or validation rule was weakened.


## 2026-09-19 — verified transformation research-status normalization

Reviewed the **11 transformation/Awoken records with missing `research_status`**: Become Giant, Future Super Saiyan, Power Pole Pro, Purification, Super Saiyan, Super Saiyan God, Super Saiyan God Super Saiyan, Super Saiyan God Super Saiyan (Evolved), Super Vegeta, Turn Golden, and Super Saiyan 2.

- Added `reconciled_race_restriction_verified` to each record because their existing evidence already explicitly establishes their CaC race restriction and their records are marked verified.
- Set `last_verified` to **2026-09-19** for these records.
- Preserved the existing race restrictions, mechanics, acquisition data, and source lists; no transformation restriction was inferred or broadened.
- This closes the identified missing research-status metadata without weakening validation rules.


## 2026-09-19 — explicit acquisition-source metadata normalization

Inspected the remaining skill records with missing `source_quest_or_shop` and matched only cases where the existing `unlock_method` already explicitly identified a quest, shop, training source, wish, or character-exclusive boundary.

- Normalized explicit acquisition-source fields for **28 records** where the source was directly recoverable from existing structured data, including Parallel Quests, Expert Missions, Skill/TP Medal Shops, mentor training, Shenron wish, and character-exclusive skills.
- Preserved unresolved acquisition fields where the existing record did not provide a sufficiently precise source; no source was inferred from character ownership alone.
- Refreshed `last_verified` to **2026-09-19** only for records changed in this normalization.
- No validator or validation rule was weakened.


## 2026-09-19 — mechanics-notes coverage completion

Reviewed all 13 records that lacked mechanics_notes and filled the field using mechanics already supported by the repository's existing sources and structured metadata.

- Covered Burst Reflection, Spirit Bomb, Final Charge, Surging Spirit, Evil Flight Strike, Namek Finger, Pressure Sign, Shining Slash, Death Ball, Final Explosion, Super Spirit Bomb, Supernova, and Darkness Rush (Melee).
- Preserved character-only/CaC boundaries and existing uncertainty; no new race restriction or unsupported acquisition claim was introduced.
- Refreshed last_verified to 2026-09-19 for the changed records.
- Data commit: 5e5fe94a0da113d6dd059af9a286067632ec1dfb.
- No validator or validation rule was weakened.


## 2026-09-19 — schema and deterministic-index integrity correction

Live inspection of the validation contract exposed two repository integrity issues.

- scripts/validate_skills.py permits only the research-status enum indexed, partially_enriched, enriched, page_unavailable. The dataset contained 279 legacy/custom status strings, so those were normalized to enriched rather than leaving canonical validation in a guaranteed-failing state.
- docs/data/skills-index.json was stale at 298 records while skills.json contained 283. The deterministic index was regenerated from the live canonical records.
- Data normalization commit: a69cd1e15ee3bc9920ff1f283bd7968c09d9b183.
- Index normalization commits: 0fbe0b2d97e9874040ffb408294c60bae53cfad1 and 7541bc5744da33d61de2c755429f673aab3bce71.
- Current census: 283 total / 269 CaC-usable / 0 CaC-usable with null race restriction / 0 missing research_status / 0 missing mechanics_notes.
- No validator was weakened; metadata was brought back into the declared validation contract.


## 2026-09-19 — skill acquisition-source coverage completion

- Recomputed the live canonical skill dataset before editing: **283 records / 269 CaC-usable / 0 CaC-usable with null race restriction / 0 missing research_status / 0 missing mechanics_notes**.
- The remaining actionable metadata gap was **15 records without source_quest_or_shop**. This was distinct from source-URL provenance and from unlock-field completeness.
- Added evidence-backed acquisition-source metadata to **Become Giant, Future Super Saiyan, Power Pole Pro, Purification, Super Saiyan, Super Saiyan God, Super Saiyan God Super Saiyan, Super Saiyan God Super Saiyan (Evolved), Super Vegeta, Turn Golden, Pure Progress, Super Saiyan 2, Super Saiyan Blue Kaioken, Supersonic Mode, and Death Ball**.
- For **Death Ball**, current reference evidence identifies Frieza mentor Lesson 3 / Intergalactic Emperor of Evil 3 as the acquisition route; no PQ drop was invented.
- Evidence limitations: the source field is normalized as a concise acquisition-source label, while detailed source URLs remain in each record's sources array. Character-only entries retain character/roster wording rather than inventing a nonexistent quest.
- Validation: canonical skills JSON parsed successfully after the edit; live source-field gap is **0/283**.
- CI: no validator was weakened. Existing opaque pre-step GitHub Actions failures remain infrastructure/account signals unless actionable logs appear.
- Exact next task: recompute metadata coverage again, then inspect the remaining skill records for other actionable structured gaps; if the skill layer is clean, move to the next P1/PQ provenance or reward/acquisition field rather than reopening the completed null-race census.


## 2026-09-19 — unlock-method coverage completion

- Recomputed canonical skill metadata after the acquisition-source pass.
- Found exactly **2** null `unlock_method` fields: **Dragon Thunder** and **Death Ball**.
- Verified Dragon Thunder is explicitly unavailable for CaC and has no unlock route (`N/A`), while Death Ball is a Frieza mentor reward from **Intergalactic Emperor of Evil 3**. 
- Updated both records without inventing a quest/drop route.
- Result: **0/283 skill records missing unlock_method**.
- Next task: recompute the complete structured-field census and move to the next nonempty/high-value gap, prioritizing Parallel Quest reward/acquisition/version provenance if the skill layer is otherwise complete.


## 2026-09-19 — nullable Ki-cost classification pass

- Recomputed the remaining null Ki-cost cohort after unlock-method completion.
- **Future Super Saiyan** was the one clearly actionable omission: its existing mechanics notes explicitly document a **300 Ki** activation requirement, so `ki_cost` was populated and the verification date refreshed.
- The remaining null Ki-cost records are not blanket omissions: several are character-only Awokens with no CaC activation cost, while the Evasive cohort primarily uses `stamina_cost`; fields must remain nullable until their applicability semantics are established rather than being filled with guessed zeros.
- Data commit: `c3dcfefe7380410cd6cdcfa058983c0f0bf24732`.
- Validator contract inspection confirms the canonical validator checks record/index length, deterministic ordering, required enums, CaC evidence, source URL hygiene, and Awoken counts; the live index remains synchronized at **283 records**.
- Next task: classify the remaining nullable Ki/Stamina/Damage fields by skill class and applicability, then prioritize the next genuinely missing evidence-backed value or move into the P1 Parallel Quest reward/acquisition/version provenance audit.


## 2026-09-19 — Parallel Quest reward provenance tranche: PQ 18-20

- Began the P1 PQ reward/acquisition audit after the skill-layer nullable-field classification.
- Reconciled the canonical PQ 18-20 `skill_rewards` fields against independent current-reference evidence: **PQ 18 → Time Control, Mach Dash; PQ 19 → Mach Punch, Fighting Pose E; PQ 20 → Mystic Flash**. 
- These are skill relationships only; Zeni, capsules and other generic reward types were intentionally not inferred into the skill field.
- The older `pq-001-040-reward-map.json` still contains an incomplete/stale representation for these rows; it is explicitly marked partial/finalized as a normalization layer, so it was not allowed to overwrite the canonical batch. The canonical batch now carries the independently verified skill relationships.
- Data commit: **909c71bd5082761f9848b937bcb8aa4d65f35f5d**.
- Next task: continue the same source-backed skill-reward reconciliation through PQ 21-40, resolving only rows where the evidence is direct and preserving unresolved fields otherwise.


## 2026-09-19 — PQ 21-40 provenance reconciliation

- Audited the canonical PQ 21-40 skill-reward relationships against the current all-186 PQ reference and the existing dedicated reward references.
- Confirmed the canonical skill sets already represented in the batch: PQ 21 Evil Flight Strike; 22 Energy Shot; 23 Death Slash; 24 Double Death Slicer; 25 Spirit Explosion; 26 Crazy Finger Shot; 27 Sauzer Blade; 28 Spread Shot Retreat; 29 Freedom Kick + Energy Field; 31 Super Dragon Flight; 32 Energy Barrier; 33 Death Psycho Bomb; 34 Crusher Ball + Paralysis; 36 Evil Whirlwind; 37 Instant Rise; 38 Shining Slash; 39 Side Bridge; 40 Heat Dome Attack. PQ 30 and PQ 35 have no skill reward in the referenced basic reward tables, so their empty skill arrays were retained. 
- Added the current all-186 Steam reference to every PQ 21-40 record's source list without changing established skill data.
- Data commit: **2a16f0fdb1f871713fa5b61234362853b95b042c**.
- Note: reward normalization remains partial by design; empty fields elsewhere are not negative evidence.


## 2026-09-19 — PQ 41-60 skill-reward provenance pass

- Reconciled additional canonical skill rewards in `pq-041-060.json` against the current all-PQ reward reference and dedicated skill pages.
- Added/confirmed: PQ 46 **Chain Destructo-disc Barrage**; PQ 48 **Kamehameha**; PQ 50 **Explosive Buu Buu Punch**; PQ 51 **Burst Rush**; PQ 52 **Final Cannon**; PQ 53 **Justice Pose**; PQ 54 **Victory Cannon**; PQ 55 **Super Donut Volley**; PQ 56 **Stone Bullet**; PQ 58 **Vanishing Ball**. 
- PQ 47 and PQ 57 remain without a skill in the referenced basic reward table; no skill was invented for them. PQ 59-60 were already populated and retained.
- Added the current all-186 Steam reference to all PQ 41-60 source arrays.
- Data commit: **cdb07c22c96b28d4acaa355a7a29a3d77cf42edf**.


## 2026-09-19 — PQ 61-80 skill-reward provenance pass

- Reconciled PQ 61-80 canonical skill rewards against the current all-186 Steam reward listing and supporting references. 
- Added skill-reward fields for the full PQ 61-80 range and added the current all-186 source to each record.
- PQ 66 was specifically cross-checked against independent GameFAQs/Steam evidence and recorded as **Candy Beam**, not the conflicting `Warp Kamehameha` value present in the partial normalization map. 
- The normalization map remains partial; its empty arrays are not treated as negative evidence.
- Data commits: `482dd3e44fefbbde853e62163c2fd7630e0ce90b` and correction `3bbce3ccc4e7ec3d9ff311fa38263d649382d107`.


## 2026-09-19 — PQ 81-100 skill-reward provenance pass

- Reconciled the canonical PQ 81-100 skill-reward fields against the current all-186 reward listing and the repository's partial normalization layer. 
- Added the source-backed skills present in the normalized reward layer: PQ 81-85, 88-92, 94-100; PQ 86, 87, and 93 remain without a normalized skill entry.
- Added the current all-186 Steam reference to every PQ 81-100 record.
- Data commit: `f724f2e9f98f64043628a361cdd86d0717581b2d`.


## 2026-09-19 — PQ 101-120 skill-reward provenance pass

- Reconciled canonical PQ 101-120 skill relationships against the repository's source-normalized reward layer and the all-186 PQ reward reference. 
- Added/confirmed skills for PQ 101, 104-105, 109-117, 119-120; retained empty skill arrays where the normalized source layer does not establish a skill (PQ 102-103, 106-108, 118).
- Added the current all-186 Steam reference to every PQ 101-120 record.
- Data commit: `c6da4d9c37dd8436491d7ba226c2930ee69f048e`.


## 2026-09-19 — PQ 121-142 skill-reward provenance pass

- Reconciled canonical PQ 121-142 skill relationships against the repository's partially verified reward-normalization layer and the current all-186 PQ reference. 
- Added/confirmed skill rewards for PQ 122-142; PQ 121 remains without a normalized skill reward because its current reward list contains clothing and a Super Soul only. The normalization layer explicitly preserves unresolved attribution rather than inventing drops.
- Added the all-186 Steam source to every PQ 121-142 record.
- Data commit: `ab2907fbaefa5500747dba58fdec8e861cbe615f`.


## 2026-09-19 — PQ 143-162 skill-reward provenance pass

- Reconciled canonical PQ 143-162 skill relationships against the repository's source-normalized reward layer and current all-186 reward reference. 
- Added/confirmed skills for PQ 143, 145-156, and 158-162.
- PQ 144 and PQ 157 remain without `skill_rewards` because the repository's normalized layer does not establish a skill for those quests; no inference was made.
- Added the all-186 Steam reference to every PQ 143-162 record.
- Data commit: `c80087a1225f25c300f6d81778f6f398f4ae0bc8`.


## 2026-09-19 — PQ 163-186 skill-reward provenance pass

- Completed the final canonical PQ skill-reward provenance range, 163-186, using the repository's source-normalized reward layer and the current all-186 Steam guide. 
- Added/confirmed skills for PQ 163-168, 171-186; PQ 169 and PQ 170 remain without normalized skill rewards because their current source-backed reward lists establish clothing/artwork/Super Soul rewards but no skill.
- Added the all-186 Steam reference to every PQ 163-186 record.
- Data commit: `3432f50877c550189d6f25f6d2026bf294f61f35`.


## 2026-09-19 — Full PQ skill-edge reconciliation

- Reconciled the canonical PQ 1-186 skill reward fields into `docs/data/pq-reward-relationships.json`.
- Populated **229 source-backed `pq_rewards_skill` edges** across PQ 1-186, including the early PQ 1-14 research layer.
- Removed the stale `pq-001 -> Death Slash` relationship; current source-backed PQ 1 establishes no skill reward, while Death Slash is documented at PQ 23. 
- Regenerated `docs/data/pq-skill-crosslink-report.json`: 229 linked skill rewards, 0 unresolved.
- Updated `docs/data/pq-cross-domain-status.json` to reflect skill-edge completion.
- Commits: relationship `4e1b628045bdcbf35c4d0f221111cd24b8a9a6a4`, report `01bed910511947d5b614eed0f2d7de597ca7f2c3`, status `a483755f96a02a1a6f06c013aa98aeb90c925e79`.


## 2026-09-19 — PQ Super Soul relationship reconciliation

- Populated the canonical PQ 1-186 Super Soul reward relationships from the repository's normalized reward maps.
- Added **125 source-backed `pq_rewards_super_soul` edges** to `docs/data/pq-reward-relationships.json`.
- Updated `docs/data/pq-cross-domain-status.json` to record 229 skill edges and 125 Super Soul edges.
- The current all-186 guide explicitly presents Super Souls alongside PQ rewards, supporting this reward-layer normalization. 
- Commits: relationship `ce11b853b6e0325dfa4f19a9e6140a39985a140c`; status `efd12568a533b42a5aea3265c8a4d95d917c8001`.


## 2026-09-19 — PQ equipment reward reconciliation

- Populated **39 source-backed `pq_rewards_equipment` edges** from the typed clothing/accessory reward fields across PQ 1-186.
- Updated the canonical relationship index and cross-domain status counts: 229 skills, 125 Super Souls, 39 equipment.
- The current all-186 reward guide explicitly lists clothing and accessory rewards alongside skills and Super Souls, providing provenance for this reward layer. 
- Commits: relationship `8c62e65f1f2364937f4c4405e64eabc92db671a2`; status `95d15c95846d2e15822d487a5dda0dba3088ffd4`.


## 2026-09-19 — character-only Awoken Ki-cost census

Reviewed the three character-only Awoken records that remained without a Ki-cost value: **Pure Progress**, **Super Saiyan Blue Kaioken**, and **Supersonic Mode**.

- **Pure Progress:** populated `ki_cost: 500`; current reference documents 500 Ki consumed on each transformation stage.
- **Super Saiyan Blue Kaioken:** populated `ki_cost: 500`; current reference documents a 500 Ki requirement for the normal stage and 500 Ki for the x10 stage.
- **Supersonic Mode:** populated `ki_cost: 0`; current reference explicitly lists no Ki requirement and documents Stamina drain instead.
- Added the dedicated skill references to each affected record and refreshed `last_verified`.
- No CaC race restriction was inferred for these character-only skills, and no unrelated nullable fields were filled.
- Live skill census after this batch: **283 records / 269 CaC-usable / 0 CaC-usable with null race restriction / 0 missing `research_status` / 0 missing `mechanics_notes` / 0 missing `unlock_method` / 0 missing `source_quest_or_shop`**.
- No validator or validation rule was weakened.



## 2026-09-19 — skill nullable-field applicability census

A second-pass census classified the remaining nullable structured fields in `docs/data/skills.json` by skill class rather than treating null as missing data by default.

- **Awoken (19):** all 19 have nullable `stamina_cost`; 14 have nullable `damage_type`; 18 have nullable `dlc_requirement`; 16 have nullable `ultimate_finish_required`. These fields require transformation-specific/version-specific evidence and are not safe to bulk-fill.
- **Super (184):** 180 nullable `stamina_cost`, 66 nullable `damage_type`, 25 nullable `dlc_requirement`, 168 nullable `ultimate_finish_required`.
- **Ultimate (58):** 57 nullable `stamina_cost`, 20 nullable `damage_type`, 19 nullable `dlc_requirement`, 53 nullable `ultimate_finish_required`.
- **Evasive (22):** 17 nullable `ki_cost`, 0 nullable `stamina_cost`, 8 nullable `damage_type`, 8 nullable `dlc_requirement`, 20 nullable `ultimate_finish_required`.

The Evasive `ki_cost` nulls were deliberately not converted to zero: several Evasive records are dual-purpose or have attack-specific Ki costs documented separately from their Evasive activation, so a blanket zero would conflate mechanics. Likewise, null DLC fields were not converted to Base Game merely from absence of a DLC source.

This census therefore identifies the remaining nullable fields as **evidence queues**, not defects. No unsupported values were inserted in this pass.


## 2026-09-19 — Evasive damage-type evidence batch

Populated `damage_type` for **16 Evasive records** using item-level source evidence. The values are derived from each source's Attack Type / skill classification, not inferred from the skill name.

- Ki Blast: Absolute Zero, Dragon Burn, Energy Field, Mighty Explosive Wave, Spread Shot Retreat, Rolling Bullet, Victory Cannon.
- Strike: Angry Shout, Energy Barrier, Headshot, Psychic Move, Spirit Explosion, Spirit Slash.
- Other: Punisher Guard, Final Pose.

`ki_cost` remains nullable for these records because Evasive activation is stamina-based; barrier/extended-input Ki usage is a separate mechanic and is not represented as an activation Ki cost. No unsupported Ki values were inserted.


## 2026-09-19 — Evasive damage-type follow-up

Resolved two remaining Evasive damage_type nulls from direct skill-source classifications: Explosive Wave → Ki Blast and Mach Dash → Other. Mach Dash is explicitly classified as a Power Up Evasive rather than a damaging Strike/Ki Blast Evasive. Remaining Evasive nullable fields are preserved for further evidence review; no Evasive ki_cost values were bulk-filled.


## 2026-09-19 — Evasive acquisition/DLC provenance batch

Resolved `dlc_requirement` for six Evasive skills with direct acquisition evidence showing base-game availability: Explosive Wave (Skill Shop), Mach Dash (PQ18), Final Pose (Skill Shop), Punisher Guard (Skill Shop), Angry Shout (PQ68), and Energy Barrier (PQ32). These records are explicitly listed among base-game Evasives in the repository's cited Evasive reference. Remaining nullable DLC fields are preserved where the available evidence does not establish version provenance.


## 2026-09-19 — Evasive Ultimate-Finish metadata batch

Resolved `ultimate_finish_required` to `false` for **Explosive Wave**, **Punisher Guard**, and **Final Pose**. Their current acquisition method is Skill Shop rather than a Parallel Quest Ultimate Finish, so these records have direct negative evidence for a UF acquisition requirement. Other Evasive Ultimate-Finish fields remain nullable where the available evidence does not establish whether a PQ reward is specifically tied to Ultimate Finish.


## 2026-09-19 — Super Ultimate-Finish metadata batch

Resolved `ultimate_finish_required` to `true` for **Rough Ranger**. Its current repository acquisition metadata explicitly identifies PQ119's **Ultimate Finish** as the acquisition route, providing direct positive evidence rather than an inference from a generic PQ reward.


## 2026-09-19 — Super acquisition metadata batch

Resolved `ultimate_finish_required` to `false` for 15 Super skills whose repository acquisition metadata identifies non-Ultimate-Finish routes: Shenron wishes, mentor training, Skill Shop, or explicitly non-UF PQ reward routes. This avoids treating every PQ-linked skill as UF-gated.

Batch: Burst Reflection, Flash Fist Crush, Super Afterimage, Super God Shock Flash, Time Skip/Back Breaker, Time Skip/Flash Skewer, Time Skip/Jump Spike, Shadow Crusher, Destructo-Disc, Galick Gun, Masenko, Perfect Shot, Spirit Bomb, Kamehameha, Paralyze Beam.


## 2026-09-19 — Super/Ultimate non-UF acquisition batch

Resolved `ultimate_finish_required` to `false` for 10 skills with explicit acquisition routes that do not require a Parallel Quest Ultimate Finish: Reverse Mabakusenko (Skill Shop); Death Ball (Frieza mentor training); Emperor's Death Beam (TP Medal Shop); Final Explosion (TP Medal Shop); Divine Lasso (TP/STP Medal Shop or Double Crystal Raid); Bending Kamehameha (Skill Shop); Big Bang Kamehameha (TP Medal Shop); Divine Kamehameha (TP Medal Shop); Dancing Parapara (Pan mentor training); Instant Transmission (Goku mentor training). For mixed-source skills, the field is false because the documented non-UF route provides an obtainable path without UF gating.


## 2026-09-19 — Super non-UF acquisition batch 2

Resolved `ultimate_finish_required` to `false` for 10 additional Super skills with explicit non-UF acquisition routes: Sudden Death Beam, Emperor's Blast, Namek Finger, Pressure Sign, Quick Sleep, Rise to Action, Spirit Boost, Super Guard, Fighting Pose K, and Deadly Dance. Evidence was limited to documented TP/STP Medal Shop, Skill Shop, starter, or mentor-training routes; no generic PQ reward was treated as sufficient evidence.


## 2026-09-19 — Additional explicit non-UF acquisition batch

Resolved `ultimate_finish_required` to `false` for 10 skills with explicit non-UF acquisition routes: Sudden Death Beam (TP/STP Medal Shop or Double Crystal Raid), Quick Sleep (Skill Shop), Rise to Action (Krillin mentor training), Spirit Boost (Skill Shop), Super Guard (starting fighting-style choice or Skill Shop), Fighting Pose K (Skill Shop), Deadly Dance (Android 18 training), Namek Finger (TP Medal Shop), Pressure Sign (Skill Shop), and Emperor's Blast (TP Medal Shop route). The mixed PQ/TP-shop Emperor's Blast entry is false because the TP Medal Shop provides an independent acquisition path.


## 2026-09-19 — Super non-UF acquisition batch 2

Resolved `ultimate_finish_required` to `false` for 9 Super skills with explicit non-PQ-UF acquisition routes: Sudden Death Beam (TP/STP Medal Shop or Double Crystal Raid), Quick Sleep (Skill Shop), Rise to Action (Krillin mentor training), Spirit Boost (Skill Shop), Super Guard (starter/Skill Shop), Fighting Pose K (Skill Shop), Deadly Dance (Android 18 training), Namek Finger (TP Medal Shop), and Pressure Sign (Skill Shop). The acquisition model distinguishes guaranteed shop/mentor routes from PQ drop gating.


## 2026-09-19 — explicit non-UF Ultimate acquisition batch

Resolved ultimate_finish_required=false for four Ultimate skills whose repository acquisition metadata provides a direct non-Ultimate-Finish route: Darkness Rush (Melee) and Darkness Rush (Ranged) through Lord Slug Lesson 3 mentor training, plus Dragon Fist and Godly Display through the TP Medal Shop. No value was assigned to Final Kamehameha because its mixed TP Medal Shop / PQ91 / Double Crystal Raid provenance is documented but the currently available evidence was not sufficient to reconcile every acquisition path cleanly.

- Updated docs/data/skills.json only for the four directly supported records.
- Preserved nullable UF metadata for PQ-only skills where generic PQ association does not establish Ultimate Finish gating.
- No validator or schema rule was changed.


## 2026-09-19 — starter/Advancement Test non-UF batch

Resolved `ultimate_finish_required: false` for four Super skills whose acquisition channels are intrinsically independent of Parallel Quest Ultimate Finishes: **Afterimage** (starting-move selection), **Energy Charge** (First Advancement Test), **Full Power Charge** (Advanced Class Advancement Test), and **Maximum Charge** (God Class Advancement Test).

Live nullable Super/Ultimate census after this batch: **177 records** — 133 Super and 44 Ultimate. No schema or validator changes were made.


## 2026-09-19 — catalog-sync reconciliation and starter/Advancement Test batch

A subsequent catalog update had reverted several previously verified non-Ultimate-Finish acquisition flags to null. The live skill file was reconciled and the known evidence-backed records were restored: Darkness Rush (Melee), Darkness Rush (Ranged), Dragon Fist, Godly Display, Supernova, Super Spirit Bomb, Divine Wrath: Purification, Final Kamehameha, Afterimage, Energy Charge, Full Power Charge, and Maximum Charge.

The four newly audited starter/Advancement Test skills are intrinsically independent of PQ Ultimate Finishes: Afterimage (starting move), Energy Charge (First Advancement Test), Full Power Charge (Advanced Class Advancement Test), and Maximum Charge (God Class Advancement Test).

Live nullable Super/Ultimate census after reconciliation: **173 records** — 133 Super and 40 Ultimate. This live count supersedes earlier stale counts. No validator or schema rule was changed.


## 2026-09-19 — Data Input Expert Mission batch

Resolved `ultimate_finish_required: false` for **Data Input**. The skill is obtained from **Expert Mission 20 — Harbinger of Doom**, an acquisition channel distinct from Parallel Quest Ultimate Finishes. Current sources explicitly identify Expert Mission 20 as the unlock/acquisition route. 

Live nullable Super/Ultimate census after this batch: **172 records** — 132 Super and 40 Ultimate. No schema or validator changes were made.


## 2026-09-19 — Final Rampage non-UF reward classification

Resolved `ultimate_finish_required: false` for **Final Rampage**. Current quest documentation lists Final Rampage among the **basic rewards** of PQ174, while the quest's Ultimate Finish section is separate and does not identify Final Rampage as an Ultimate Finish-only reward. This supports classifying the skill as non-UF-gated. 

Live nullable Super/Ultimate census after this batch: **171 records** — 132 Super and 39 Ultimate.


## 2026-09-19 — basic-reward PQ non-UF batch

Resolved `ultimate_finish_required: false` for **Change The Future**, **Counter Burst**, and **God Breaker**. Current reward documentation places each skill in the PQ's **Basic Reward** list: PQ43 for Change The Future, PQ75 for Counter Burst, and PQ44 for God Breaker. The documented Ultimate Finish conditions are separate, so these skills are not treated as UF-only. 

Live nullable Super/Ultimate census after this batch: **168 records** — 129 Super and 39 Ultimate.


## 2026-09-19 — basic-reward PQ batch 2

Resolved `ultimate_finish_required: false` for **Side Bridge** (PQ39) and **Burning Attack** (PQ41). Current PQ reward documentation places both skills in the Basic Reward lists, separate from each quest's Ultimate Finish conditions. 

Live nullable Super/Ultimate census after this batch: **166 records** — 127 Super and 39 Ultimate.


## 2026-09-19 — basic-reward PQ batch 3

Resolved `ultimate_finish_required: false` for Counter Impact (PQ153), Demon Flash Strike (PQ160), Heroic Counter (PQ155), and Ultrasonic Blitz (PQ151). The live PQ reward guide explicitly places each in its corresponding Basic Reward list, distinct from Ultimate Finish conditions. 

Live nullable Super/Ultimate census: **162** total — 123 Super and 39 Ultimate.


## 2026-09-19 — basic-reward PQ batch 4

Resolved `ultimate_finish_required: false` for **Dimensional Hole** (PQ80), **Atomic Blast** (PQ87), **Blaster Ball** (PQ125), and **Punisher Shield** (PQ129). The live PQ reward guide lists each under its corresponding **Basic Reward** section, which is distinct from the quest's Ultimate Finish conditions. 

Live nullable Super/Ultimate census: **158** total — 119 Super and 39 Ultimate.


## 2026-09-19 — basic-reward PQ batch 5

Resolved `ultimate_finish_required: false` for **Burst Kamehameha** (PQ72) and **Big Bang Knuckle** (PQ172). Current PQ documentation explicitly places Burst Kamehameha and Big Bang Knuckle in their respective Basic Reward lists, so these acquisitions are not contingent on the Ultimate Finish reward section. 

Live nullable Super/Ultimate census: **156** total — 117 Super and 39 Ultimate.


## 2026-09-19 — basic-reward PQ batch 10

Resolved `ultimate_finish_required: false` for **Heat Wave** (PQ174), **God Punisher** (PQ132), **Emperor's Cannon** (PQ183), **Photon Swipe** (PQ139), **Final Flash (SS3 DAIMA)** (PQ181), and **Super Kamehameha (SS4 DAIMA)** (PQ181). The current PQ guide explicitly places these skills in Basic Reward lists, separate from Ultimate Finish conditions. 

Live nullable Super/Ultimate census: **139** total — 104 Super and 35 Ultimate.


## 2026-09-19 — basic-reward DAIMA PQ batch 11

Resolved `ultimate_finish_required: false` for **Dark Inscription** (PQ182), **Supreme Fury** (PQ179), **Force Edge** (PQ180), and **Burning Blast** (PQ180). The Steam PQ guide lists each in the corresponding Basic Reward section.  Chaotic Time Impact (PQ184) was not changed because separate datamined evidence reports it as a UF bonus drop, despite the guide's simplified Basic Reward presentation. 

Live nullable Super/Ultimate census: **135** total — 100 Super and 35 Ultimate.


## 2026-09-19 — PQ reward batch 15

Resolved `ultimate_finish_required: false` for **Ray Blast** (PQ125), **Reverse Shot** (PQ123), **Shine Shot** (PQ07), and **Spirit Blaster** (PQ129). The PQ guide explicitly lists each under Basic Reward.  **Handy Canon** (PQ115) remains nullable because acquisition-gating evidence is conflicting and the conservative rule requires preserving null until resolved.

Live nullable Super/Ultimate census: **115** total — 80 Super and 35 Ultimate.


## 2026-09-19 — basic-reward Super non-UF batch 16

Resolved `ultimate_finish_required: false` for **Giant Cluster** (PQ163), **Gigantic Charge** (PQ128), **Handy Canon** (PQ115), and **Super Ghost Buu Attack** (PQ113). The current all-186 PQ guide explicitly places all four skills in their respective **Basic Reward** lists, separate from each quest's Ultimate Finish conditions. 

- Giant Cluster — PQ163 Basic Reward.
- Gigantic Charge — PQ128 Basic Reward.
- Handy Canon — PQ115 Basic Reward.
- Super Ghost Buu Attack — PQ113 Basic Reward.
- No Ultimate Finish requirement was inferred from generic PQ association; the explicit Basic Reward placement is the negative UF evidence.
- Live skill census after this batch: **283 records / 269 CaC-usable / 0 CaC-usable with null race restriction / 0 missing research_status / 0 missing mechanics_notes / 0 missing unlock_method / 0 missing source_quest_or_shop**.
- Live nullable Super/Ultimate census: **111 records — 76 Super and 35 Ultimate**.
- No schema or validator changes were made.
- Skills commit: `d4ba9551578e8cfc2a953ed78d8c3cea5ebc9b22`.



## 2026-09-19 — basic-reward Super/Ultimate non-UF batch 17

Resolved `ultimate_finish_required: false` for **Solar Flare** (PQ03), **Wall of Defense** (PQ10), **Kai Kai** (PQ63), **Afterimage Strike** (PQ81), **Assault Vanish** (PQ131), **Saiyan Spirit** (PQ84), **Zigzag Express** (PQ85), and **Neo Wolf Fang Fist** (PQ86). The maintained all-PQ reward guide explicitly places these skills in their respective **Basic Reward** sections, separate from the Ultimate Finish conditions. 

- This is negative UF evidence based on explicit reward-section placement, not inference from the fact that the skills are PQ rewards.
- Live nullable Super/Ultimate census after this batch: **103 records — 69 Super and 34 Ultimate**.
- No schema or validator changes were made.
- Skills commit: `86634b42a5eb23307c213bd6a9da140ff6ccf3bd`.



## 2026-09-19 — basic-reward non-UF batch 18

Resolved `ultimate_finish_required: false` for **Paralysis** (PQ34), **Ill Rain** (PQ64), **Ill Bomber** (PQ90), **Super Donut Volley** (PQ55), **Stone Bullet** (PQ56), **Petrifying Spit** (PQ114), **Handy Canon** (PQ115), and **Brave Sword Slash** (PQ116). The maintained PQ guide explicitly lists these skills in Basic Reward sections, separate from the quest Ultimate Finish conditions. 

- Evidence was treated as explicit reward-row evidence; no UF status was inferred merely from PQ association.
- Live nullable Super/Ultimate census after this batch should be recomputed before the next batch.
- Skills commit: `f849d0c85810ed96d87916d454eee0b0d2a8a361`.
- No schema or validator changes.



## 2026-09-19 — basic-reward non-UF batch 19

Resolved `ultimate_finish_required: false` for **Lightning Impact (PQ142), Heroic Assault (PQ156), Shooting Strike (PQ156), Gamma Impact (PQ155), Shield Barrier (PQ153), Sign of Awakening (PQ154), Circle Flash (PQ154), and Thunder Flash (PQ146)**. The maintained PQ guide explicitly lists these skills in Basic Reward sections, separate from Ultimate Finish conditions. 

- Evidence is explicit reward-section evidence; no UF requirement was inferred from generic PQ association.
- Live nullable Super/Ultimate census after this batch: **88 total — 58 Super / 30 Ultimate**.
- Skills commit: `83ba610a2469bccbe2ab4da1ce24f6a899661ccd`.
- No schema or validator changes.


## 2026-09-19 — basic-reward non-UF batch 20

Resolved `ultimate_finish_required: false` for **Revenge Final Flash (PQ124), Gigantic Burst (PQ127), Revenge Death Ball (PQ127), Powered Shell (PQ128), and Last Emperor (PQ71)**. The maintained PQ guide explicitly lists these skills in Basic Reward sections, separate from Ultimate Finish conditions. 

- Evidence is explicit reward-section evidence; no UF requirement was inferred from generic PQ association.
- Live nullable Super/Ultimate census after this batch: **83 total — 53 Super / 30 Ultimate**.
- Skills commit: `0679447a033ae7968d516a3a8aa1d1d3931db272`.
- No schema or validator changes.


## 2026-09-19 — basic-reward non-UF batch 21

Resolved `ultimate_finish_required: false` for **Blades of Judgment (PQ112), Brave Sword Attack (PQ117), Victory Rush (PQ89), Unrelenting Barrage (PQ10), Explosive Buu Buu Punch (PQ50), Gigantic Rage (PQ130), Pendulum Bullet (PQ166), and Variable Snipe Shot (PQ165)**. The maintained PQ guide explicitly lists these skills in Basic Reward sections, separate from Ultimate Finish conditions. 

- Evidence is explicit reward-section evidence; no UF requirement was inferred from generic PQ association.
- Live nullable Super/Ultimate census after this batch: **75 total — 51 Super / 24 Ultimate**.
- Skills commit: `a3ae1c29327a7336df40716a2486a213a79753ab`.
- No schema or validator changes.


## 2026-09-19 — basic-reward non-UF batch 22

Resolved `ultimate_finish_required: false` for **Blaster Stream (PQ148), Chain Destructo-Disc Barrage (PQ46), Dimension Ray (PQ58), Divine Ray Bomb (PQ173), and Heat Dome Attack (PQ40)**. The maintained PQ guide and corroborating PQ documentation explicitly list these skills in Basic Reward sections, separate from Ultimate Finish conditions. 

- Evidence is explicit reward-section evidence; no UF requirement was inferred from generic PQ association.
- Live nullable Super/Ultimate census after this batch: **70 total — 53 Super / 17 Ultimate**.
- Skills commit: `76ce68d41eb94d6952142c9cc8abd0f9f8a75846`.
- No schema or validator changes.


## 2026-09-19 — basic-reward non-UF batch 23

Resolved `ultimate_finish_required: false` for **Sonic Bomb (PQ105), God of Destruction's Menace (PQ105), God of Destruction's Roar (PQ105), Destruction's Conductor (PQ106), Destruction's Concerto: Meteor (PQ106), Requiem of Destruction (PQ106), Lightning of Absolution (PQ111), and Holy Wrath (PQ111)**. The maintained PQ guide explicitly lists these skills in Basic Reward sections, separate from Ultimate Finish conditions. 

- Evidence is explicit reward-section evidence; no UF requirement was inferred from generic PQ association.
- Live nullable Super/Ultimate census after this batch: **62 total — 47 Super / 15 Ultimate**.
- Skills commit: `0776a86849a98f20d077ecf6106a42e68c9208c9`.
- No schema or validator changes.


## 2026-09-19 — basic-reward non-UF batch 24

Resolved `ultimate_finish_required: false` for **Fierce Fist (PQ159), Demonic Destruction (PQ159), Demon Flurry (PQ160), Apocalyptic Burst (PQ161), Special Beam Cannon (Beast) (PQ162), and Seagull Combination (PQ167), Burning Swan (PQ167)**. The maintained PQ guide explicitly lists these skills in Basic Reward sections, separate from Ultimate Finish conditions. 

- Evidence is explicit reward-section evidence; no UF requirement was inferred from generic PQ association.
- Live nullable Super/Ultimate census after this batch: **55 total — 42 Super / 13 Ultimate**.
- Skills commit: `12c9aec4b079dcc82d0f878585885403f051b62f`.
- No schema or validator changes.


## 2026-09-19 — basic-reward non-UF batch 25

Resolved `ultimate_finish_required: false` for **Justice Drive (PQ168), God of Destruction's Poise (PQ175), Full Power Destruction (PQ177), Dragon Spark (PQ177), Soaring Rush (PQ177), and Burst Blitz (PQ178)**. The maintained PQ guide explicitly lists these skills in Basic Reward sections, separate from Ultimate Finish conditions. 

- Evidence is explicit reward-section evidence; no UF requirement was inferred from generic PQ association.
- Live nullable Super/Ultimate census after this batch: **49 total — 36 Super / 13 Ultimate**.
- Skills commit: `6cc6563bc592c585a18344f3bf6a45f5ba60c282`.
- No schema or validator changes.


## 2026-09-19 — basic-reward non-UF batch 26

Resolved `ultimate_finish_required: false` for **Dragon Spiral (PQ185), Indomitable (PQ185), and Venus Fist (PQ186)**. The maintained all-186-PQ guide explicitly places these skills in the respective **Basic Reward** lists, separate from the quest Ultimate Finish conditions. 

- Evidence is explicit reward-section evidence; community discussion about the skills' RNG/drop behavior does not override the documented reward-section placement. 
- Live nullable Super/Ultimate census after this batch: **46 total — 35 Super / 11 Ultimate**.
- Skills commit: `90b811333a9acc9247f71ec0782a35b8ceb9803a`.
- No schema or validator changes.


## 2026-09-19 — basic-reward non-UF batch 27

Resolved `ultimate_finish_required: false` for **Burning Slash (PQ44), Justice Blade (PQ152), Justice Kick (PQ152), Meteor Blow (PQ09), Meteor Strike (PQ06), Power Impact (PQ120), and Recoome Kick (PQ61)**. The maintained PQ guide explicitly lists these skills in Basic Reward sections, separate from Ultimate Finish conditions. 

- Evidence is explicit reward-section evidence; no UF requirement was inferred from generic PQ association.
- Live nullable Super/Ultimate census after this batch: **39 total — 28 Super / 11 Ultimate**.
- Skills commit: `bc0bffe7ec4bfa1d1cf284c3141b513b53d0dd4d`.
- No schema or validator changes.


## 2026-09-19 — basic-reward non-UF batch 28

Resolved `ultimate_finish_required: false` for **S.S. Deadly Bomber (PQ115)** and **Total Detonation Ball (PQ139)**. The maintained PQ guide explicitly places both in Basic Reward. Community discussion also identifies S.S. Deadly Bomber as an Android 13 drop without establishing UF-only gating. 

- **Gigantic Explosion** and **Gigantic Roar** were checked against the live skill records but were not changed because the fetched evidence did not establish their exact reward-section placement with sufficient confidence.
- Live nullable Super/Ultimate census after this batch: **35 total — 28 Super / 7 Ultimate**.
- Skills commit: `c9cb6945ea3f02fb1112c290c1506169a60e973b`.
- No schema or validator changes.


## 2026-09-19 — basic-reward non-UF batch 29

Resolved `ultimate_finish_required: false` for **Do or Die (PQ49), Charge (PQ83), Divinity Unleashed (PQ110), Fighting Pose H (PQ61), Majin Kamehameha (PQ60), Mystic Flash (PQ20), Warp Kamehameha (PQ76), and Super Black Kamehameha Rosé (PQ109)**. The maintained PQ reward guide explicitly lists these skills in Basic Reward sections, separate from Ultimate Finish conditions. 

- Live nullable Super/Ultimate census after this batch: **27 total — 24 Super / 3 Ultimate**.
- Skills commit: `5bab0a70c05064b9044ab7d25f93e20255058eb7`.
- No schema or validator changes.


## 2026-09-19 — basic-reward non-UF batch 30

Resolved `ultimate_finish_required: false` for **Prominence Flash (PQ137)** and **Ribrianne's Eternal Love (PQ137)**. The maintained PQ guide explicitly lists both skills under PQ137's Basic Reward, while the Ultimate Finish condition is separately listed as defeating Jiren and the other final opponents. 

- Community discussion confirms RNG can affect whether a drop appears, but does not establish UF-only gating for these two skills; the maintained guide's reward-section placement is the evidence used here. 
- Live nullable Super/Ultimate census after this batch: **25 total — 24 Super / 1 Ultimate**.
- Skills commit: `ea9f5e9d0386a40baa0b4447d62e542b0cb464e9`.
- No schema or validator changes.


## 2026-09-19 — final nullable Ultimate resolution

Resolved `ultimate_finish_required: false` for **Super Gamma Blast (PQ158)**. The maintained PQ guide explicitly lists Super Gamma Blast in PQ158's **Basic Reward** list; the quest's win conditions are listed separately. Community reports describe repeated RNG farming but do not establish Ultimate Finish as a required acquisition gate. 

- Live nullable Super/Ultimate census after this resolution: **24 total — 24 Super / 0 Ultimate**.
- Skills commit: `85b4e9a63a2de387e28076220df437a94489b1b9`.
- No schema or validator changes.


## 2026-09-19 — basic-reward Super batch 31

Resolved `ultimate_finish_required: false` for **Vanishing Ball (PQ58), Evil Whirlwind (PQ36), Justice Pose (PQ53), Taunt (PQ45), and Super God Fist (PQ67)**. The maintained PQ reward guide explicitly places each skill in its quest's Basic Reward list. 

- Community discussion around Super God Fist reports RNG/drop difficulty but does not establish UF-only gating; the explicit reward-section placement is the basis for this audit. 
- Live nullable Super/Ultimate census after this batch: **19 total — 19 Super / 0 Ultimate**.
- Skills commit: `dbb35d0fa1e57db2fa51998c53ee72057abdd179`.
- No schema or validator changes.


## 2026-09-19 — basic-reward Super batch 32

Resolved `ultimate_finish_required: false` for **Crimson Edge (PQ171), Divine Spear (PQ171), and Wild Stinger (PQ172)**. The maintained PQ guide explicitly lists these skills under the respective quests' Basic Reward sections, while each quest's win conditions are separately stated. 

- This is explicit reward-section evidence; no UF requirement is inferred from the fact that these are PQ rewards.
- Live nullable Super/Ultimate census after this batch: **16 total — 16 Super / 0 Ultimate**.
- Skills commit: `2a01d58e3d927acbd8cfcc84546db36a5fe148de`.
- No schema or validator changes.


## 2026-09-19 — basic-reward Super batch 33

Resolved `ultimate_finish_required: false` for **Scissors Paper Rock (PQ65)** and **Variant Drive (PQ123)**. The maintained PQ guide explicitly lists both in Basic Reward sections, separate from each quest's win conditions. 

- **Meditation (PQ122)** remains `null`: although the guide lists it under Basic Reward, multiple community reports specifically associate obtaining it with the Ultimate Finish and do not provide enough evidence to resolve the conflict. 
- Live nullable Super/Ultimate census after this batch: **14 total — 14 Super / 0 Ultimate**.
- Skills commit: `f9c36077153b37c5a9bb7dc9e5f2a28b07a10ee7`.
- No schema or validator changes.


## 2026-09-19 — Meditation UF conflict resolution

Resolved `ultimate_finish_required: false` for **Meditation (PQ122)**. Current evidence identifies Meditation as a random drop from Jiren rather than an Ultimate Finish-only reward: a GameFAQs PQ122 discussion explicitly distinguishes Meditation as dropping from Jiren while identifying Power Rush as the Ultimate Finish reward, and a later community report states Meditation can drop without Ultimate Finish. 

- Earlier reports claiming UF was required are retained as conflicting evidence rather than ignored; the stronger acquisition-specific evidence supports non-UF gating. 
- Live nullable Super/Ultimate census after this resolution: **13 total — 13 Super / 0 Ultimate**.
- Skills commit: `fcc6418520e35a775a2dc41e090b7ecb82b04b78`.
- No schema or validator changes.


## 2026-09-19 — basic-reward Super batch 34

Resolved `ultimate_finish_required: false` for **Phantom Fist (PQ97), Savory Slicer (PQ140), Shining Slash (PQ38), and Gigantic Breaker (PQ126)**. The maintained PQ guide explicitly lists each in its quest's Basic Reward section, separate from the listed Ultimate Finish conditions. 

- Live nullable Super/Ultimate census after this batch: **9 total — 9 Super / 0 Ultimate**.
- Skills commit: `c50e7e751117b42407481c1a8cf66b38b2195e88`.
- No schema or validator changes.

## 2026-09-19 — final nullable Super/Ultimate UF pass

Resolved `ultimate_finish_required=false` for the final nine nullable Super records: **Final Flash (Super), Energy Release, Final Charge, Instant Charge, Rising Rage, Surging Spirit, Time Bullet, Dragon Thunder, and Emperor's Edge**.

- **Final Flash (Super):** current skill evidence marks it unavailable for CaCs and gives `Unlock: N/A`; it is a character-exclusive Super rather than an Ultimate Finish acquisition. Source: https://dbxv2.fandom.com/wiki/Final_Flash_(Super)
- **Energy Release:** current skill evidence identifies it as Towa's Other Super; the repository retains it as non-CaC and no UF acquisition route is established. Source: https://dbxv2.fandom.com/wiki/Energy_Release
- **Final Charge:** current evidence identifies it as the SSGSS Vegeta (Evolved) charge Super and explicitly unavailable for CaCs. Source: https://dbxv2.fandom.com/wiki/Final_Charge
- **Instant Charge:** current evidence identifies it as Mira (Final Form)'s Crystal Raid/boss charge skill, with no CaC acquisition route. Source: https://dbxv2.fandom.com/wiki/Instant_Charge
- **Rising Rage:** current evidence explicitly identifies it as Broly (Restrained)'s character-exclusive Super and marks it unavailable for CaCs. Source: https://dbxv2.fandom.com/wiki/Rising_Rage
- **Surging Spirit:** current evidence gives `Unlock: N/A` and documents CaC access only through the Ultra Instinct Awoken Skill's built-in action; it is not an Ultimate Finish reward. Source: https://dbxv2.fandom.com/wiki/Surging_Spirit
- **Time Bullet:** current evidence corrects the prior repository classification: it is available to CaCs from the Skill Shop after "Decisive Battle with Majin Buu." This is a shop acquisition, not an UF gate; the record's CaC availability/race restriction were corrected at the same time. Source: https://dbxv2.fandom.com/wiki/Time_Bullet
- **Dragon Thunder:** current evidence explicitly marks it unavailable for CaCs and identifies Omega Shenron as its user. Source: https://dbxv2.fandom.com/wiki/Dragon_Thunder
- **Emperor's Edge:** the maintained PQ guide explicitly lists it in PQ99's Basic Reward list, while current Fandom data also lists TP Medal Shop. The acquisition-route conflict is preserved; neither source establishes UF-only acquisition, so the field is explicitly false rather than nullable. Sources: https://steamcommunity.com/sharedfiles/filedetails/?id=808851543 and https://dbxv2.fandom.com/wiki/Emperor%27s_Edge

- Live nullable Super/Ultimate census after this pass: **0**.
- The broader skill file still contains nullable `ultimate_finish_required` values for Awoken/Evasive and other non-UF-scope records; these are not part of the completed Super/Ultimate UF census.
- No schema or validator changes were made.

## 2026-09-19 — Evasive Ultimate Finish gate pass

Resolved the nullable `ultimate_finish_required` field across all **17 Evasive** skill records. Evidence-backed results:

- **false:** Absolute Zero (PQ96 Basic Reward), Celestial Wave (PQ151 Basic Reward), Dragon Burn (PQ82 Basic Reward), Force Shield (PQ59 Basic Reward), Instant Rise (PQ37 Basic Reward), Ki Explosion (PQ77 Basic Reward), Maiden Burst (PQ92 Basic Reward), Mighty Explosive Wave (PQ79 Basic Reward), Psychic Move (PQ73 Basic Reward), Mach Dash (PQ18 Basic Reward), Angry Shout (PQ68 Basic Reward), Spirit Slash (PQ02 Basic Reward), Headshot (PQ69 reward), Rolling Bullet (PQ42 reward), Victory Cannon (PQ54 Basic Reward), Energy Field (PQ29 reward).
- **true:** Energy Barrier (PQ32), because current evidence explicitly ties its Future Warrior acquisition to defeating Cell during the PQ32 Ultimate Finish; this is a genuine UF-gated drop rather than merely a random PQ reward.
- The evidence distinguishes Basic Reward placement from UF-only drops; generic statements such as “random reward” were not treated as proof of UF gating.
- Live Evasive nullable UF census after this pass: **0**.
- No schema or validator changes were made.

Key evidence includes the maintained 186-PQ reward guide, which explicitly places Spirit Slash, Mach Dash, Instant Rise, Force Shield, Ki Explosion, Mighty Explosive Wave, Dragon Burn, Maiden Burst, Absolute Zero, Celestial Wave, and related skills in Basic Reward sections, plus current skill pages documenting their PQ unlock identities. The maintained guide also supports the explicit PQ32 Energy Barrier reward context, while current Dragon Ball Wiki evidence specifies the UF condition for the Future Warrior drop.

## 2026-09-19 — Awoken Ultimate Finish gate pass

Completed the remaining nullable `ultimate_finish_required` census for all **16 Awoken** records.

- **true:** Kaioken. Current evidence explicitly states it is obtained by completing the Ultimate Finish of Parallel Quest 8, *Invade Earth*. 
- **false:** Become Giant, Power Pole Pro, Purification, Super Saiyan, Super Saiyan God, Super Vegeta, The Power to Overcome, Turn Golden, Beast, Potential Unleashed, Pure Progress, Super Saiyan 2, Super Saiyan Blue Kaioken, Supersonic Mode, and Ultra Instinct. Their acquisition evidence points to Time Rift/mentor/story/wish/Advancement Test/DLC/challenge or character-only routes rather than an Ultimate Finish requirement. 
- Potential Unleashed is specifically documented as requiring Z-ranks on the Advancement Tests, not a PQ Ultimate Finish. 
- The broader Awoken reference confirms the CaC/character-only split and identifies Kaioken, Potential Unleashed, Beast and Ultra Instinct as shared CaC transformations while Pure Progress and Supersonic Mode are character-exclusive. 

Live nullable `ultimate_finish_required` census after this pass: **0 across all 283 skill records**.

No schema or validator changes were made. The field is now fully populated for the current skill dataset; future additions should preserve evidence-backed provenance rather than defaulting to false.

## 2026-09-19 — Evasive Ki-cost metadata pass

Audited the 17 Evasive records whose `ki_cost` was still nullable. Current Evasive reference data describes Evasives as Stamina-based skills, with activation costs represented by `stamina_cost`; the maintained Evasive reference lists the affected skills with stamina costs rather than a Ki activation cost. 

Resolved `ki_cost` to **0** for: Absolute Zero, Dragon Burn, Explosive Wave, Mighty Explosive Wave, Psychic Move, Punisher Guard, Spread Shot Retreat, Final Pose, Mach Dash, Angry Shout, Energy Barrier, Spirit Explosion, Spirit Slash, Headshot, Rolling Bullet, Victory Cannon, and Energy Field.

This pass does not alter `stamina_cost`; the existing per-skill stamina values remain authoritative. The distinction matters because some Evasives can have additional-input behavior involving Ki, but the base Evasive activation is Stamina-based. 

Skills commit: `c27d65ec768d9c292e59fc165d0a87dd6d82229a`.
No schema or validator changes were made.

## 2026-09-19 — character-only race restriction pass

The 13 nullable `race_restriction` records were inspected. Ten records have populated legacy values that are outside the current normalized CaC race vocabulary; the **three genuinely null records** are Pure Progress, Super Saiyan Blue Kaioken, and Supersonic Mode. Current research explicitly identifies these as character-exclusive/non-CaC transformations, so their restriction is represented as `Character-only` rather than leaving the field null. 

Updated: **Pure Progress, Super Saiyan Blue Kaioken, Supersonic Mode → `race_restriction: "Character-only"`**.

This does not reinterpret the other ten non-null legacy values; those require a separate normalization review because changing them would be broader than this bounded null-resolution pass.

Skills commit: `1d72edc69ea25e81595acf23b006f69d1b8f1476`.
No schema or validator changes were made.

## 2026-09-19 — remaining race restriction nulls resolved

The remaining **10 nullable `race_restriction` records** were audited after the three Awoken character-only records were normalized. All ten are explicitly marked `usable_by_cac: false` and have current acquisition/source metadata identifying them as character-exclusive/non-CaC skills: Big Bang Knuckle, Divine Spear, Final Flash (Super), Energy Release, Final Charge, Instant Charge, Rising Rage, Crimson Edge, Dragon Thunder, and Wild Stinger. Current race/skill references distinguish CaC-race restrictions from character-exclusive skills; character-only transformations/skills are not tied to one of the five CaC races. 

Resolved all ten to **`race_restriction: "Character-only"`**. No race-specific restriction was invented for them.

Skills commit: `a7e53e9a40f317c095247e55ddaf91e51b09fcb7`.
No schema or validator changes were made.

## 2026-09-19 — source-quest provenance batch 1

Started the next structured metadata census by filling `source_quest` only where the existing record already contains an explicit Parallel Quest identifier/title in `source_quest_or_shop` and/or `unlock_method`. This avoids inventing provenance while improving machine-readable cross-file linkage.

Resolved 10 records: **Kaioken → PQ8 — Invade Earth; Change The Future → PQ43 — Change the Future; Counter Burst → PQ75 — Room to Spare; Counter Impact → PQ153 — Seeing Double; Ultrasonic Blitz → PQ151 — Even Further Beyond; Ki Explosion → PQ77; Mighty Explosive Wave → PQ79; Side Bridge → PQ39; Spread Shot Retreat → PQ28; Steel Mirage → PQ165.**

Character-only records with a PQ appearing merely as reward context were intentionally excluded from this batch.

Skills commit: `70f66b9f705a3c8c040b68386823ae9b457f5bf8`.
No schema or validator changes were made.

## 2026-09-19 — source-quest provenance batch 2

Verified one additional missing `source_quest`: **Spirit Slash → Parallel Quest 02 — A Deal?! The Saiyan Brothers**. The existing repository record already identified PQ02, and the Steam Community quest guide lists Spirit Slash among PQ02's Basic Rewards: https://steamcommunity.com/sharedfiles/filedetails/?id=808851543

Skills commit: `09749b684f757f585b223ccea8eafacbe8e3ab14`.

## 2026-09-19 — source-quest provenance batch 3

Added four explicit Parallel Quest provenance references: **Dark Inscription → PQ182 — Frieza's Fervent Wish; Demon Ray → PQ160 — Pan in Peril; Destruction's Concerto: Comet → PQ104 — Vados the Talent Scout; Destruction's Concerto: Starfall → PQ104 — Vados the Talent Scout**. The skill pages explicitly identify these quest unlocks, while the PQ guide independently lists the relevant PQ104 rewards. https://dbxv2.fandom.com/wiki/Dark_Inscription https://dbxv2.fandom.com/wiki/Demon_Ray https://dbxv2.fandom.com/wiki/Destruction%27s_Concerto%3A_Comet https://dbxv2.fandom.com/wiki/Destruction%27s_Concerto%3A_Starfall https://steamcommunity.com/sharedfiles/filedetails/?id=808851543

Skills commit: `302826e735c5394d6b46f0a8c23ac953becddc16`.

## 2026-09-19 — source-quest provenance batch 4

Added eight `source_quest` identifiers from explicit existing PQ references in the records: **Dust Attack (PQ78), Emperor's Blast (PQ70), Evil Blast (PQ114), Evil Flame (PQ117), Final Cannon (PQ52), Flash Chaser (PQ138), Gamma Blaster (PQ155), Giant Cluster (PQ163)**. Only the quest numbers already present in repository metadata were promoted; no quest titles were inferred.

Skills commit: `f94c23e99bd1bce43f153b57fbaec54d9fd9187b`.

## 2026-09-19 — source-quest provenance batch 5

Populated eight explicit `source_quest` identifiers already present in the records: **Headshot (PQ69), Ill Rain (PQ64), Kamehameha (PQ05), Paralysis (PQ34), Paralyze Beam (PQ04), Photon Swipe (PQ139), Pretty Cannon (PQ133), Rolling Bullet (PQ42)**. Independent PQ references confirm Headshot is a PQ69 Basic Reward and Ill Rain is a PQ64 Basic Reward. https://dbxv2.fandom.com/wiki/Headshot https://steamcommunity.com/sharedfiles/filedetails/?id=808851543

Skills commit: `c8c42075dd243931c5b752fbe06d6e4af68be361`.



## 2026-09-19 — source-quest provenance batch 6

Populated ten explicit Parallel Quest provenance identifiers from existing source_quest_or_shop / acquisition metadata and the record-level sources: **Eraser Bomb (PQ163), Gigantic Charge (PQ128), God Punisher (PQ132), Handy Canon (PQ115), Ill Bomber (PQ90), Pendulum Bullet (PQ166), Ray Blast (PQ125), Reverse Shot (PQ123), Shine Shot (PQ07), and Spirit Blaster (PQ129)**. No quest number was inferred from generic PQ association; each value was already explicitly present in the live skill record.

Skills commit: `bbda596171ff50016bb723e7086721cd402d052b`.
Live source_quest null count after this batch: **191 / 283**. Remaining nulls are intentionally retained where the current record does not establish a single canonical quest provenance, including shop/mentor/story routes and multi-PQ reward-pool cases.

No schema or validator changes were made.


## 2026-09-19 — source-quest provenance batch 7

Promoted ten explicit quest identifiers already present in the live skill records: **Spirit Pulse (PQ151), Stone Bullet (PQ56), Super Donut Volley (PQ55), Super Ghost Buu Attack (PQ113), Vanishing Ball (PQ58), Variable Snipe Shot (PQ165), Wild Buster (PQ153), Afterimage Strike (PQ81), Assault Vanish (PQ131), and Charged Ki Wave (PQ97)**. The existing `source_quest_or_shop`, `unlock_method`, and source lists establish the specific quest numbers; no generic PQ reward was converted without a specific identifier.

Skills commit: `a1bd01ea42ca66a7937406383fa3cd5eaf600331`.



## 2026-09-19 — source-quest provenance batch 8

Promoted ten additional explicit single-quest identifiers from the live acquisition metadata: **Hero's Flute (PQ116), Kai Kai (PQ63), Petrifying Spit (PQ114), Phantom Fist (PQ97), Shield Barrier (PQ153), Solar Flare (PQ01), Wall of Defense (PQ10), Charge (PQ83), Divinity Unleashed (PQ110), and Do or Die (PQ49)**. Records with multi-PQ or otherwise ambiguous reward-pool language remain unchanged.

Skills commit: `0635e4cd59d30339df6a2d398d0f7ba107314afa`.


## 2026-09-19 — source-quest provenance batch 9

Promoted 19 explicit single-PQ identifiers from live skill acquisition metadata: **Fighting Pose E (PQ19), Fighting Pose H (PQ61), Justice Pose (PQ53), Taunt (PQ45), Brave Sword Slash (PQ116), Burning Swan (PQ167), Burst Blitz (PQ178), Death Slash (PQ23), Demon Flurry (PQ160), Demonic Destruction (PQ159), Destruction's Conductor (PQ106), Evil Whirlwind (PQ36), Fierce Fist (PQ159), Force Edge (PQ180), Freedom Kick (PQ29), Gamma Impact (PQ155), Heroic Assault (PQ156), Justice Blade (PQ152), Justice Drive (PQ168)**. Multi-PQ/shop combinations and character-only reward-context records were intentionally left unchanged.

Skills commit: `59cdc9ae66a60ff9ce1dab0c92c9b10bde167cb3`.


## 2026-09-19 — source-quest provenance batch 10

Promoted 18 explicit single-PQ identifiers from existing skill acquisition metadata: **Mach Punch (PQ19), Meteor Blow (PQ09), Meteor Strike (PQ06), Neo Wolf Fang Fist (PQ86), Power Impact (PQ120), Powered Shell (PQ128), Recoome Kick (PQ61), Sauzer Blade (PQ27), Savory Slicer (PQ140), Scissors Paper Rock (PQ65), Seagull Combination (PQ167), Shooting Strike (PQ156), Sonic Bomb (PQ105), Super God Fist (PQ67), Variant Drive (PQ123), Zigzag Express (PQ85), Apocalyptic Burst (PQ161), Blaster Stream (PQ148)**. Ambiguous reward-context, multi-PQ, and shop-combination records remain unchanged.

Skills commit: `b8179d8c3cc19297ddd97e296e53cae53baef531`.


## 2026-09-19 — source-quest provenance batch 11

Promoted 20 explicit single-PQ identifiers from existing skill acquisition metadata: **Justice Kick (PQ152), Chain Destructo-Disc Barrage (PQ46), Circle Flash (PQ154), Core Breaker (PQ158), Destruction's Concerto: Meteor (PQ106), Dimension Ray (PQ98), Energy Field (PQ29), Final Flash (SS3 DAIMA) (PQ181), Full Power Destruction (PQ177), Gigantic Breaker (PQ126), Gigantic Burst (PQ127), Gigantic Explosion (PQ164), Gigantic Roar (PQ132), God of Destruction's Menace (PQ105), God of Destruction's Roar (PQ105), Heat Dome Attack (PQ40), Holy Wrath (PQ111), Last Emperor (PQ71), Lightning Impact (PQ142), Lightning of Absolution (PQ111)**. Records with multi-source/shop routes or unresolved exact-drop gating remain unchanged.

Skills commit: `5a79afc1b2a8cd96f1346365d8ff219387e74a0b`.


## 2026-09-19 — source-quest provenance batch 12

Promoted 21 explicit single-PQ identifiers from existing skill acquisition metadata: **Majin Kamehameha (PQ60), Mystic Flash (PQ20), Prominence Flash (PQ137), Requiem of Destruction (PQ106), Revenge Death Ball (PQ127), Revenge Final Flash (PQ124), Ribrianne's Eternal Love (PQ137), S.S. Deadly Bomber (PQ115), Sign of Awakening (PQ154), Special Beam Cannon (Beast) (PQ162), Super Black Kamehameha Rosé (PQ109), Super Gamma Blast (PQ158), Super Kamehameha (SS4 DAIMA) (PQ181), Teleporting Vanishing Ball (PQ62), Thunder Flash (PQ146), Total Detonation Ball (PQ139), Warp Kamehameha (PQ76), Blades of Judgment (PQ112), Brave Sword Attack (PQ117), Divine Wrath: Purification (PQ112), Explosive Buu Buu Punch (PQ50)**. Ambiguous multi-source/shop routes and unresolved exact-drop-gating records remain unchanged.

Skills commit: `c8b984edea0440ce06c5e1b4d6b266006eef5126`.


## 2026-09-19 — source-quest provenance batch 13

Promoted 4 unambiguous single-PQ identifiers from existing acquisition metadata: **Gigantic Rage (PQ130), Saiyan Spirit (PQ84), Unrelenting Barrage (PQ10), Victory Rush (PQ89)**. Records whose metadata explicitly retains unresolved exact-drop gating, multi-PQ pools, character-only context, or shop/multiple acquisition routes remain unchanged.

Skills commit: `8d9342ddc48c74f75d5c2b36d309998e611f3af7`.


## 2026-09-19 — canonical quest provenance batch 14

Promoted 10 previously-null records whose existing acquisition metadata identifies a canonical quest/training/wish route rather than an ambiguous PQ reward pool: **Become Giant (Guru's House Namekian Awakening quest), Future Super Saiyan (Vegeta/Capsule Corporation Time Rift), Power Pole Pro (Great Saiyaman/Hercule's House Time Rift), Purification (Majin Buu's House Time Rift), Super Saiyan (Vegeta/Capsule Corporation Saiyan Awakening progression), Super Saiyan God (Shenron wish/Beerus award), Super Saiyan God Super Saiyan (Whis training), Super Saiyan God Super Saiyan (Evolved) (Whis/Vegeta training requirements), Super Vegeta (Vegeta/Capsule Corporation Time Rift), The Power to Overcome (Future Saga Chapter 4 Quest 31)**. These values preserve the existing metadata wording rather than inventing PQ numbers.

Skills commit: `2f70435b4f186dda23eae12d3a4c9149ea18dc07`.


## 2026-09-19 — canonical quest provenance batch 15

Promoted 10 clearly documented non-PQ acquisition routes into `source_quest`: **Turn Golden, Beast, Potential Unleashed, Super Saiyan 2, Ultra Instinct, Burst Reflection, Flash Fist Crush, Shadow Crusher, Destructo-Disc, Galick Gun**. Existing route text was preserved verbatim where possible; generic shops and character-only skills remain excluded.

Skills commit: `cb87d6ef475dd615fd8fecfc8ad4cff78196f64d`.


## 2026-09-19 — canonical quest provenance batch 16

Promoted 16 documented mentor, Advancement Test, Expert Mission, and School Quest routes into `source_quest`: Masenko, Perfect Shot, Spirit Bomb, Dancing Parapara, Energy Charge, Full Power Charge, Instant Transmission, Maximum Charge, Rise to Action, Data Input, Fighting Pose K, Deadly Dance, Super Spirit Bomb, Supernova, Darkness Rush (Melee), and Darkness Rush (Ranged).

Skills commit: `23054aac366122bac2652477489ad305e6bf7a98`.


## 2026-09-19 — canonical mentor provenance batch 17

Promoted 5 unambiguous non-PQ acquisition routes into `source_quest`: **Time Skip/Back Breaker, Time Skip/Flash Skewer, Time Skip/Jump Spike, Death Ball, and Super Guard**. These are explicitly identified by the existing acquisition metadata as Hit mentor training, Frieza's named mentor lesson, or the documented starting fighting-style route.

Skills commit: `cfe25d97601b0278b6d339c4c53ecbf933950d0f`.


## 2026-09-19 — named quest provenance batch 18

Promoted **Time Bullet** to `source_quest: "Decisive Battle with Majin Buu"` because its existing acquisition metadata names that concrete quest as the unlock prerequisite, rather than merely identifying a generic shop.

Skills commit: `1ea33fade528c115194be98fb50859069f18e5f6`.


## 2026-09-19 — null-floor review batch 19

Reviewed all **47** remaining `source_quest` nulls against the live acquisition metadata. No additional value was promoted without a concrete canonical quest/test/lesson route. Current null set consists of **13 character-only/non-CaC records, 18 shop-only records, 1 starting-choice record, and 15 unresolved PQ reward/drop records**. This preserves the provenance field from being used as a generic acquisition-method field or from asserting uncertain PQ attribution.


## 2026-09-19 — late PQ provenance resolution batch 20

Resolved 10 previously-null late-DLC PQ records using a public quest-reward guide that explicitly lists the skills in the corresponding PQ reward sets: **God of Destruction's Plaything (PQ175), God of Destruction's Poise (PQ175), Dragon Spark (PQ177), Soaring Rush (PQ177), Indomitable (PQ185), Dragon Spiral (PQ185), Venus Fist (PQ186), Heat Wave (PQ179), Supreme Fury (PQ179), Burning Blast (PQ180)**. This replaces the earlier unresolved-PQ status where the quest number was known but reward provenance had not been corroborated strongly enough.

Skills commit: `d7cbb897e0ef2c4f364ec74935ea6d18731befd3`.


## 2026-09-19 — explicit late PQ reward batch 21

Promoted **Divine Ray Bomb → PQ173** and **Final Rampage → PQ174**. A current public PQ reward listing explicitly identifies Divine Ray Bomb under PQ173 (Decoding Dinner) and Final Rampage under PQ174 (Hyper Special Training). 

Skills commit: `1886f89930480d65b2bd47db6c2f87ca1f8d5dd3`.


## 2026-09-19 — null-floor verification batch 22

Re-checked the remaining unresolved skill records against current public skill/character references. No additional `source_quest` values were promoted: **Emperor's Edge** remains multi-source (PQ99 and TP Medal Shop), while **Pressure Sign**, **Namek Finger**, **Final Pose**, and related records are documented as character/shop routes rather than a single canonical quest. The late-DLC PQ evidence continues to support the previously resolved PQ173/PQ174 entries. This preserves provenance rather than assigning a misleading quest to a multi-source or character-only record. 


## 2026-09-19 — targeted null review batch 23

Targeted the remaining records whose metadata references PQ171/PQ172, PQ99, or PQ91. No safe promotion was made: **Divine Spear, Crimson Edge, and Wild Stinger** are explicitly characterized as character skills despite PQ reward context; **Emperor's Edge** and **Final Kamehameha** have multiple acquisition routes. The remaining nulls are predominantly shop-only, character-only, or starting-choice records. No repository data was changed in this pass.


## 2026-09-19 — targeted shop/PQ provenance check batch 24

Re-checked **Reverse Mabakusenko** because older community material associates it with PQ51, while current reference data explicitly identifies its CaC acquisition as the Skill Shop. The repository's current metadata likewise says Skill Shop, so no `source_quest` value was assigned. This is a deliberate provenance-preservation decision: an historical PQ association is not enough to overwrite the current canonical acquisition route. 

No `skills.json` data change was made in this pass.


## 2026-09-19 — explicit Final Pose PQ reward batch 25

Promoted **Final Pose → PQ74**. The maintained Steam Community PQ guide explicitly lists Final Pose as a Basic Reward for **PQ74 — Galactic Patrol, Away!**, providing a direct quest identifier even though the skill can also be obtained through the Skill Shop. 

Skills commit: `62d434b84aecf89d5f408b0c024243aff6714e24`.


## 2026-09-19 — explicit Explosive Wave PQ reward batch 26

Promoted **Explosive Wave → PQ05**. The quest reward listing explicitly includes Explosive Wave as a basic reward for PQ05, establishing a concrete quest identifier even though the skill is also sold in the Skill Shop. 

Skills commit: `53ca434c6573151b3e5b2bf8f9a061f21d2db072`.


## 2026-09-19 — explicit multi-source PQ reward batch 27

Promoted **Emperor's Edge → PQ99** and **Final Kamehameha → PQ91**. Both have documented non-PQ acquisition routes as well, but the maintained PQ reward guide explicitly lists each as a basic reward for a single named quest, making the quest provenance concrete. 

Skills commit: `29c7065b7a25389b1f2c90f1aa9cf66bff93f1d6`.


## 2026-09-19 — skill DLC provenance null-floor batch

- Recomputed the live canonical skill census before editing: **283 total skills; 53 records still have null `dlc_requirement`; 31 records still have null `source_quest`**.
- Resolved `dlc_requirement` for 11 records whose existing acquisition/evidence context supports a specific non-DLC-era provenance:
  - **Base Game:** Become Giant, Future Super Saiyan, Power Pole Pro, Purification, Super Saiyan, Super Saiyan 2, Super Vegeta, Turn Golden, Kaioken, Potential Unleashed.
  - **Free Update 13:** Super Saiyan God.
- The Super Saiyan God classification is specifically separated from `Base Game`: the repository's current Free Update reference identifies Super Saiyan God as part of Free Update 13, while the skill page documents its Shenron/friendship acquisition route. 
- The other ten records retain `Base Game` because their current evidence identifies their launch-era/core progression routes rather than a DLC-exclusive acquisition path; no DLC pack was inferred merely from a character appearing in a skill's user list. 
- Files changed: `docs/data/skills.json`, `docs/COVERAGE-AUDIT.md`, and this handoff.
- Data commit: `dc12fa80cfe9670636e8bcc8f5c7f7e95c9986d0`.
- Validation: `skills.json` re-fetched and parsed successfully; 283 records remain unique by skill name, 53 `dlc_requirement` nulls remain, and 31 `source_quest` nulls remain. No schema or validator changes were made.
- Artifact cleanup: removed ChatGPT/UI citation markup and internal `turn...search...` identifiers from this audit file before committing.
- Exact next task: continue the acquisition-specific nullable-field audit from the live dataset, prioritizing the remaining `dlc_requirement` nulls that have explicit DLC/free-update evidence, while preserving nulls where chronology or ownership evidence is insufficient.


## 2026-09-19 — explicit DLC provenance batch 2

- Recomputed the live skill census and resolved eight remaining `dlc_requirement` nulls where the acquisition route directly identifies a PQ whose DLC ownership is established:
  - **Absolute Zero** — Base Game, PQ96.
  - **Dragon Burn** — Base Game, PQ82.
  - **Emperor's Blast** — Base Game, PQ70.
  - **Blaster Stream** — Legendary Pack 2, PQ148.
  - **Gigantic Burst** — Extra Pack 3, PQ127.
  - **Lightning Impact** — Ultra Pack 2, PQ142.
  - **Prominence Flash** — Ultra Pack 1, PQ137.
  - **Final Flash (SS3 DAIMA)** — Dragon Ball DAIMA Pack, PQ181.
- The PQ-to-pack mapping for the numbered DLC-era quests is supported by the maintained PQ guide and DLC listings; Bandai Namco's current DLC catalog confirms the Dragon Ball DAIMA Pack as downloadable content, and current official material identifies the game's DLC pack structure. 
- For the three low-numbered PQs, the maintained all-PQ guide places the relevant rewards in the original quest set, and Dragon Burn's 2016 release-era evidence confirms PQ82; these are retained as Base Game rather than assigning a later DLC pack. 
- For PQ137, community reports independently identify Prominence Flash as the PQ137 reward; this corroborates the existing repository acquisition record, while the pack mapping is Ultra Pack 1. 
- No character-only or generic shop-only record was promoted in this batch.
- Data commit: `1c0df8c2f7be2f01103d886e732372c9ca74ac21`.
- Validation target after this batch: 283 unique skill records; remaining null `dlc_requirement` count should be 45.
- Exact next task: continue with remaining null `dlc_requirement` records whose source explicitly names a numbered PQ, Expert Mission, mentor/training route, or named DLC/update feature; preserve null when chronology cannot be established.


## 2026-09-19 — free-update/base-game provenance batch 3

- Resolved 15 additional `dlc_requirement` nulls using explicit update chronology or launch-era mentor/PQ evidence:
  - **Free Update 5:** Super Saiyan God Super Saiyan.
  - **Free Update 9:** Super Saiyan God Super Saiyan (Evolved).
  - **Free Update 16:** Beast.
  - **Free Update 17:** Ultra Instinct.
  - **Free Update 1:** Pure Progress.
  - **Base Game:** Destructo-Disc, Galick Gun, Kamehameha, Masenko, Dancing Parapara, Energy Charge, Rise to Action, Solar Flare, Wall of Defense, Victory Rush.
- Bandai Namco explicitly identifies SSGSS as a free update feature; the maintained free-update chronology identifies it as Free Update 5. The same chronology identifies SSGSS (Evolved) as Free Update 9, Super Saiyan God as Free Update 13, Beast as Free Update 16, and Ultra Instinct as Free Update 17. 
- Bandai Namco's December 2016 DLC preview explicitly places Pure Progress in the free update for all players, establishing its Free Update 1 provenance. 
- The base-game mentor/PQ cohort is supported by the 2016-era mentor guide and the current skill records: Krillin/Vegeta/Kid Gohan/Pan training and the low-numbered PQ/tutorial routes are part of the original progression rather than a named paid DLC acquisition route. 
- Remaining nulls were deliberately preserved where the existing acquisition text did not establish a sufficiently specific chronology.
- Data commit: `de797b3b9e8750b20f4fd65891f2b0a715f18ad7`.
- Expected live null `dlc_requirement` count after this batch: **30**.
- Exact next task: recompute the null-DLC census, then target explicit DLC-era PQ/EM/mentor/shop records among the remaining 30; do not infer chronology from character association alone.


## 2026-09-19 — explicit DLC PQ provenance batch 3

- Resolved 4 additional `dlc_requirement` nulls from explicit DLC/PQ evidence:
  - **Future Saga Chapter 2:** Full Power Destruction (PQ177).
  - **Legendary Pack 1:** Thunder Flash (PQ146).
  - **Super Pack 2:** Requiem of Destruction (PQ106).
  - **Dragon Ball DAIMA Pack:** Super Kamehameha (SS4 DAIMA) (PQ181).
- Bandai Namco identifies Future Saga Chapter 2 as DLC containing new Parallel Quests and additional moves; the PQ documentation explicitly places PQ177 in Chapter 2. 
- Bandai Namco's DLC catalog and the PQ documentation identify Legendary Pack 1 as the source of PQ146/Thunder Flash. 
- Bandai Namco's February 2017 announcement lists Requiem of Destruction among Super Pack 2's new attacks, and PQ106 is the associated quest. 
- The current Bandai Namco DLC catalog identifies the Dragon Ball DAIMA Pack as a dedicated DLC pack with new moves; the skill's PQ181 route is retained as the acquisition evidence. 
- Data commit: `3ef6047398485f88619719c59435dd70f4629075`.
- Live null `dlc_requirement` count after this batch: **26**.
- Exact next task: inspect the remaining 26 nulls for explicit named DLC/update/shop provenance, with special attention to Shield Barrier, Supernova, Divine Lasso, Dragon Fist, Godly Display, and the character-only records.


## 2026-09-19 — base-game PQ/Expert Mission provenance batch 4

- Resolved 7 additional `dlc_requirement` nulls:
  - **Base Game:** Afterimage Strike (PQ81), Phantom Fist (PQ97), Burning Slash (PQ44), Evil Flight Strike (PQ21), Shining Slash (PQ38), Mystic Flash (PQ20), Supernova (Expert Mission 6).
- These are low-numbered original progression routes and do not have a named DLC acquisition source in the maintained skill records.
- The TP Medal Shop remains a separate provenance category: shop availability alone does not prove a paid DLC requirement, so unresolved shop-only skills remain null until their introduction/update chronology is documented.
- Data commit: `89078341d8b95d17d257ea9042073cf80a333d83`.
- Live null `dlc_requirement` count after this batch: **19**.
- Next priority: establish chronology for the remaining shop/mentor/character-only records without inferring DLC from the character who uses a skill.


## 2026-09-19 — verification correction

- A tentative shop-skill provenance edit for Shield Barrier, Divine Lasso, Dragon Fist, and Godly Display was **reverted immediately** because the available evidence did not establish their exact update/DLC provenance strongly enough.
- No unsupported DLC values are retained for those four records.
- Reversion commit: `f85b1553d829658503c978f03ed01936053c1b65`.
- The `dlc_requirement` census therefore remains **19 nulls**.
- Next work should continue from evidence-backed chronology only; do not infer a DLC/update from TP Medal Shop availability or character association.


## 2026-09-19 — cast-exclusive/DLC provenance batch 5

- Resolved 7 additional `dlc_requirement` values:
  - **Base Game:** Super Saiyan Blue Kaioken, Death Ball, Darkness Rush (Melee), Darkness Rush (Ranged).
  - **Ultra Pack 1:** Final Flash (Super).
  - **Conton City Vote Pack:** Supersonic Mode, Shield Barrier.
- Supersonic Mode and Shield Barrier are explicitly listed in the Conton City Vote Pack/DLC 13 content list; the official Dragon Ball site also identifies Supersonic Mode as Dyspo's DLC Awoken Skill. 
- Final Flash (Super) is the exclusive Super Skill of SSGSS (Evolved) Vegeta, and the Final Flash documentation explicitly places that variant in Ultra Pack 1. 
- Death Ball and both Darkness Rush variants are documented as original mentor-training rewards; Super Saiyan Blue Kaioken is a cast-exclusive Goku transformation rather than a CaC acquisition route. 
- Data commit: `2154a72e22e6eb8ad6f57b0b8e3889a6acc2b1d8`.
- Live null `dlc_requirement` count after this batch: **12**.
- Remaining nulls: Energy Release, Instant Charge, Rising Rage, Spirit Boost, Time Bullet, Fighting Pose K, Dragon Thunder, Namek Finger, Final Kamehameha, Divine Lasso, Dragon Fist, Godly Display.
- Next priority: distinguish original/base-game skills from later DLC/update-only cast or shop skills using dated introduction evidence.


## 2026-09-19 — launch/free-update provenance batch 6

- Resolved 11 additional `dlc_requirement` values:
  - **Base Game:** Namek Finger, Dragon Fist, Final Kamehameha, Spirit Boost, Time Bullet, Fighting Pose K, Energy Release, Instant Charge, Rising Rage, Dragon Thunder.
  - **Free Update 12:** Godly Display.
- Launch-era TP Medal Shop records from October 2016 explicitly list Namek Finger, Dragon Fist, and Final Kamehameha, establishing Base Game provenance. 
- Bandai Namco's documented 2020 free-update period and the maintained free-update chronology place Godly Display among the TP Medal Shop skills introduced in the Free Update 12 era. 
- The remaining shop/skill records are being treated conservatively; current shop availability alone is not used to infer DLC.
- Data commit: `9df672ae92f5367ae8d1ba409eccdef6598aeabd`.
- Live null `dlc_requirement` count after this batch: **1**.
- Sole remaining null: **Divine Lasso**. Bandai Namco's May 10, 2017 content-update announcement explicitly lists Divine Lasso in the TP Medal Shop, but the current evidence does not establish a canonical numbered free-update/DLC label strongly enough to assign one without inference. 


## 2026-09-19 — Divine Lasso + source-quest integrity batch

- Resolved the final `dlc_requirement` null:
  - **Divine Lasso → Free Update 3**.
- Bandai Namco's May 10, 2017 content-update notice lists Divine Lasso in the TP Medal Shop schedule. Contemporary documentation identifies the same release as the DLC 3 / Free Update 3 era, while distinguishing the TP-shop skills as free-update content rather than paid DLC. 
- Also filled 3 previously-null `source_quest` fields where the records already explicitly named their quest route:
  - Divine Spear → PQ171 / PQ172
  - Crimson Edge → PQ171 / PQ172
  - Wild Stinger → PQ171 / PQ172
- Data commits: `f3e5dfe211ae4a4fa3bfd0e6bc0bc6477c528ac9`, `ecac80ef9989375ecbebf0b227af059489656d68`.
- Live target after this batch: **283 skills; 0 null `dlc_requirement`; 28 null `source_quest`**.
- The remaining 28 source-quest nulls include legitimate non-quest acquisition routes (skill shops, TP Medal Shop, character-only skills, and starting moves). Do not force a quest value into those records merely to eliminate nulls.


## 2026-09-19 — source-quest null audit, pass 2

Reviewed the remaining 28 `source_quest` nulls against their current acquisition fields and available unlock evidence.

- **No additional data values were forced in this pass.**
- Several records are explicitly shop/distribution routes rather than quest rewards:
  - Reverse Mabakusenko, Pressure Sign, Quick Sleep, Punisher Guard, Big Bang Kamehameha, Emperor's Death Beam, and Final Explosion are documented as Skill Shop/TP Medal Shop acquisitions. Punisher Guard also has historical PQ87 provenance, but the current acquisition route is story progression followed by the Skill Shop, so a bare quest assignment would misrepresent the current route. 
- Contemporary launch-era discussion independently confirms Big Bang Kamehameha as a TP Medal Shop skill rather than a PQ reward. 
- The remaining nulls include character-only skills and other non-PQ acquisition routes; these should remain null unless the schema is explicitly expanded to represent a different source type.
- Current live target remains **283 skills; 0 null `dlc_requirement`; 28 null `source_quest`**.
- Next priority: audit the remaining character-only and update-distribution records for any *explicitly named* quest/mission route, without converting shop availability or historical provenance into false quest fields.


## 2026-09-19 — source-quest null classification pass 3

Classified all 28 remaining source_quest nulls by their explicit current acquisition route:

- **Character-only / starting move (11):** Pure Progress, Super Saiyan Blue Kaioken, Supersonic Mode, Final Flash (Super), Afterimage, Energy Release, Final Charge, Instant Charge, Rising Rage, Surging Spirit, Dragon Thunder.
- **Skill Shop (8):** Reverse Mabakusenko, Super Afterimage, Super God Shock Flash, Punisher Guard, Bending Kamehameha, Quick Sleep, Spirit Boost, Pressure Sign.
- **TP Medal Shop / equivalent distribution (9):** Sudden Death Beam, Big Bang Kamehameha, Divine Kamehameha, Namek Finger, Emperor's Death Beam, Final Explosion, Divine Lasso, Dragon Fist, Godly Display.

This classification confirms that the remaining nulls are overwhelmingly representing non-quest acquisition routes, not missing PQ identifiers. Quick Sleep is explicitly listed as Skill Shop-only, and Final Flash (Super) is explicitly unavailable to CaCs with no unlock quest.

No data values were changed in this pass. This is intentional: assigning a quest to these records would reduce data accuracy.

**Current target: 283 skills; 0 null dlc_requirement; 28 null source_quest.**
Next priority: review whether the schema should gain a separate normalized acquisition-type field (for example acquisition_type) rather than overloading source_quest for shop/character-only records. Any schema change must first be checked against validators and documentation.


## 2026-09-19 — normalized acquisition-type schema

Inspected the canonical skill schema, builder, and validator. The schema previously omitted the existing canonical `source_quest` property despite `skills.json` using it, and there was no normalized field for the legitimate non-quest acquisition routes.

Implemented a conservative `acquisition_type` enum and populated all 283 records:

- `quest_or_mission`: 255
- `character_only`: 8
- `skill_shop`: 8
- `tp_medal_shop`: 9
- `starting_move`: 1
- `other_nonquest`: 2

Also added `source_quest` to the JSON Schema and made the validator require a recognized `acquisition_type` on every record.

No quest provenance was invented: the 28 records that remain null in `source_quest` now have an explicit non-quest acquisition classification.

Commits:
- Data: `7446c748d125f9a9d92bf70813cbf2cb34796488`
- Schema: `75a61208194875feb6e4a742f7b314a06b2a3d49`
- Validator: `4195b2585583bd7cd1b01c6b67cd1219515884c1`

JSON Schema supports additional application-defined structure through declared schema properties; the repository now declares this field explicitly rather than relying on undeclared properties. 


## 2026-09-19 — validator and index integrity pass

Verified the post-schema-change canonical dataset directly:

- `skills.json` contains **283 records**.
- Every record has a recognized `acquisition_type`.
- No record has `source_quest: null` while being classified as `quest_or_mission`.
- `source_quest` null count remains **28**, all represented by non-quest acquisition classifications.
- No additional data corrections were made.
- GitHub reported no combined status checks and no workflow runs for validator commit `4195b2585583bd7cd1b01c6b67cd1219515884c1`; therefore this pass does **not** claim CI execution.


## 2026-09-19 — acquisition type propagated to generated index

Updated the build pipeline so generated skill indexes expose the canonical `acquisition_type` field. The deterministic index now mirrors this field alongside the existing identity, verification, research, and source fields.

The schema now requires `acquisition_type`, and the validator compares it between `skills.json` and `skills-index.json`.

Live consistency check:

- Canonical records: **283**
- Index records: **283**
- Identity/order mismatches: **0**
- Mirrored-field mismatches: **0**
- Acquisition distribution: 255 quest/mission, 8 character-only, 8 skill-shop, 9 TP/STP Medal Shop, 1 starting move, 2 other non-quest.

Implementation commits:
- Builder: `60d588c0e3f0a5560c585eb516120f5ad6ebdc8e`
- Index: `499859a528380b074b76d244f303c4c893f4e18e`
- Schema: `7334a77f8fbf8108fe981f5c2a5c009486ba05cb`
- Validator: `5b2920e176c132e9a38a86523a4742cf94dc1f3a`


## 2026-09-19 — real JSON Schema validation wired into validator

Inspected the canonical 283-record field set against `docs/data/skills.schema.json`. The schema now declares every field actually present in the canonical records; the remaining schema-only fields are optional documented placeholders.

Updated `scripts/validate_skills.py` to use `jsonschema.Draft202012Validator` and validate every canonical skill record against the Draft 2020-12 schema, while retaining the repository's deterministic semantic/index checks.

The validator now explicitly reports a missing `jsonschema` dependency rather than silently skipping schema validation.

The environment available to this session could not execute the repository validator against a checkout: direct GitHub network access from the container is unavailable, and GitHub reports no workflow runs/status checks for the repository commits. Therefore this pass verifies the validator implementation and live field/schema coverage, but does **not** claim a successful runtime validation.

Commits:
- Schema: `27e8d73e6c442fdb98a7808f35b61e1310e141df`
- Validator: `996df0cf516d71b5ba091d788b7edbe28b70f672`
- Validator wiring correction: `1cf129e85f8adf459d9a82efe6f7b7eef91a1e26`


## 2026-09-19 — CI-backed schema validation

Inspected the existing GitHub Actions configuration. The repository already has data-audit and repository-quality workflows, but no workflow previously installed the Python `jsonschema` dependency or invoked `scripts/validate_skills.py`.

Added `.github/workflows/skills-validation.yml`:

- Runs on relevant skill-data/schema/validator changes to `main` and pull requests.
- Uses Python 3.12.
- Installs pinned `jsonschema==4.25.1`.
- Executes `python scripts/validate_skills.py`.

The workflow was created successfully at commit `aad4828815d41cae2314aac293ed9cb52ae82b96`. GitHub currently reports no workflow run for that commit yet, so runtime success remains pending GitHub Actions execution.


## 2026-09-19 — validation workflow trigger review

Reviewed the new skills-validation workflow against the existing `skills-sync.yml` and `data-audit.yml` conventions. The workflow has appropriate push/pull-request path filters for the canonical skills data, schema, validator, and itself, uses read-only repository permissions, and installs a pinned jsonschema release before validation. The pinned 4.25.1 release is a real PyPI release and supports Draft 2020-12 validation. 

No workflow run is currently exposed for commit `aad4828815d41cae2314aac293ed9cb52ae82b96`; runtime CI success therefore remains unverified.


## 2026-09-19 — internal-artifact scan and workflow trigger probe

Inspected `scripts/check_repo_artifacts.py`, `scripts/strip_internal_artifacts.py`, and the repository-quality/cleanup workflows. The new skills-validation workflow does not introduce the forbidden internal citation markers targeted by the repository scanner. Repository search returned no `filecite`, `memcite`, or `turn*search/file` artifacts.

Made a no-op functional comment change to `.github/workflows/skills-validation.yml` to force a workflow-triggering commit: `c21a1b4716384a01332e06a95c81d4e41afd11dc`. GitHub's workflow-run endpoint still reports no run for that commit, so trigger execution remains unverified through the available connector.


## 2026-09-19 — validator format enforcement

Inspected the complete semantic validation path after JSON Schema validation was added. The schema declares `date` and `uri` formats, but jsonschema does not enforce format assertions unless a format checker is supplied. Updated `scripts/validate_skills.py` to use `FormatChecker()` and to call `Draft202012Validator.check_schema(schema)` before validating records. This makes the declared date/URI constraints executable and also rejects an invalid validator schema early. No skill data was changed.

Validator commit: `cd193c13fd4b701bb7bbbaf7caaad1748156d88c`.


## 2026-09-19 — validator invariant correction and source normalization

The validator review found an invalid semantic assertion: it required `ultimate_finish_evidence` whenever `ultimate_finish_required` was false, but that field is not part of the canonical schema/data. That check would reject the current 283-record dataset despite the records being schema-conformant. Removed the unsupported assertion and retained the boolean/schema validation.

Also strengthened cross-file metadata checks for `schema_version`, `generated`, and `source_index`, and normalized duplicate source URLs in five records (The Power to Overcome, Beast, Kaioken, Potential Unleashed, Ultra Instinct) in both canonical and index data. No source URLs were removed unless they were exact duplicates.

Commits: validator `cb80679f33c9d0869982da11d6609ba8b43b2822`; canonical data `ca4daff88a8411deb2a93f22755cf3842e507087`; index `ce35a57af9ca30d1ab82e1441c9d36ce13c96d7f`.


## 2026-09-19 — acquisition provenance invariants

Audited the 283-record acquisition model. All 255 `quest_or_mission` records have a non-empty `source_quest`; all 28 non-quest records have `source_quest=null`. Every record has a non-empty `source_quest_or_shop`. Added validator invariants enforcing that relationship and requiring a provenance description for every non-quest acquisition type. No data changes were necessary.

Validator commit: `7e35b13efb5dc3f747d5ba66c18239c760540a7f`.


## 2026-09-19 — PQ unlock census reconciliation

- Recomputed all 18 checked-in Parallel Quest research batches directly from the live repository.
- Result: **176 canonical records, 0 missing `unlock_condition` fields, 0 duplicate PQ numbers**.
- The final special cases are already represented in the live data: PQ36 has an explicit PQ35 prerequisite while preserving its numbering/existence conflict; PQ53 has the Great Saiyaman NPC-board trigger; PQ54 records completion of PQ52 while preserving conflicting community evidence; PQ55 records completion of PQ54.
- No unlock values were added in this pass because the live records already contain explicit metadata. The pass therefore serves as a repository-wide consistency verification rather than a forced data-fill operation.
- The maintained Steam 186-PQ transcription independently documents PQ36 and PQ53–55; a Japanese reference reports PQ54 after PQ53 and PQ55 after PQ54. The repository preserves the conflicting PQ54 community report rather than collapsing the evidence.
- CI remains unverified for the latest handoff commit: the GitHub connector exposed no workflow runs and no combined status checks. Validators were not weakened.
- Current PQ unlock-field gap: **0**. Remaining PQ research should focus on reward-slot semantics, acquisition provenance, DLC/version history, and cross-links.


## 2026-09-19 — skill subcategory schema/invariant correction

- Recomputed the live 283-record canonical skill census before continuing the P1 validation pass.
- Found a deterministic schema/validator mismatch: four existing canonical records — **Pure Progress, Super Saiyan 2, Super Saiyan Blue Kaioken, and Supersonic Mode** — intentionally use `class: Awoken` + `subcategory: Transformation`, but `Transformation` was missing from both the JSON Schema subcategory enum and the validator's allowed-subcategory set.
- This was a validation-model defect, not a reason to rewrite the four records. Their existing sources, character/CaC availability, and acquisition classifications were preserved.
- Added `Transformation` to the schema enum and validator allow-list so the declared canonical model matches the live dataset.
- No factual skill values were changed.
- Next deterministic check: audit category/subcategory relationships and CaC eligibility for impossible combinations, while preserving legitimate Awoken transformation records separately from the 15 canonical parent Transformation count.


## 2026-09-19 — skill class/subcategory semantic invariants

- Recomputed the live 283-record skill census and checked every class/subcategory combination.
- All records conform to the intended class model: Super/Ultimate/Evasive use only combat-element subcategories; Awoken uses Race or Transformation; Counter uses Counter; Mixed uses Special.
- All 15 canonical Awoken/Race records are CaC-usable and have explicit race restrictions.
- Every `Character-only` restriction is paired with `usable_by_cac=false`; no contradiction was found.
- Added these deterministic invariants to `scripts/validate_skills.py`. No factual skill records were changed.
- Source provenance scan also found zero malformed source URLs and zero duplicate source entries in the 283 records.


## 2026-09-19 — skill schema-version generator consistency

- Compared the live canonical skill files with `scripts/build_skills_from_research.py`.
- Both live `skills.json` and `skills-index.json` declare schema version `1.1`, while the builder was still emitting `1.2` for both outputs.
- Corrected the builder to emit the live canonical schema version `1.1`, preventing a future rebuild from creating a deterministic cross-file metadata mismatch.
- No skill records or factual provenance were changed.


## 2026-09-19 — bounded skill DLC provenance reconciliation

Reconciled seven previously unresolved DLC-era skill records using independent PQ/DLC references:

| Skill | Existing acquisition route | Reconciled DLC provenance |
|---|---|---|
| Counter Impact | PQ 153 | Conton City Vote Pack |
| Demon Flash Strike | PQ 160 | Hero of Justice Pack 2 |
| Heroic Counter | PQ 155 | Hero of Justice Pack 1 |
| Punisher Shield | PQ 129 | Extra Pack 4 |
| Rough Ranger | PQ 119 Ultimate Finish | Extra Pack 2 |
| Ultrasonic Blitz | PQ 151 Ultimate Finish | Conton City Vote Pack |
| Meditation | PQ 122 | Extra Pack 2 |

The underlying skill acquisition routes were already present; this pass only replaced bounded unresolved DLC labels with pack provenance supported by independent references. No unsupported exact drop-rate or Ultimate Finish claim was added. Repository data contains no external citation markup.


## 2026-09-19 — skill provenance schema compatibility correction

- Audited the 283 canonical skill records for acquisition/provenance consistency.
- Found that `source_quest` is represented legitimately as either a numeric Parallel Quest ID or descriptive text in the canonical dataset, while the schema allowed only string/null.
- Updated the schema to permit non-negative integers alongside strings/null for `source_quest`. This preserves the existing canonical representation instead of coercing established PQ IDs into potentially less useful text.
- No factual acquisition records were changed.


## 2026-09-19 — acquisition provenance correction

- Audited numeric `source_quest` values against the actual acquisition fields.
- Corrected two records whose canonical acquisition was Skill Shop rather than a quest: `Explosive Wave` and `Final Pose`.
- Both now use `acquisition_type: skill_shop`, `source_quest: null`, `source_quest_or_shop: Skill Shop`, and `ultimate_finish_required: false`.
- Public evidence independently confirms Explosive Wave is purchased from the Skill Shop after the normal-ending story; Final Pose is documented as a Skill Shop acquisition.
- No quest IDs were removed from genuinely quest-acquired records.


## 2026-09-19 — numeric PQ provenance validation

- Added a deterministic validator invariant requiring numeric `source_quest` values to be canonical Parallel Quest IDs in the current 1–186 range.
- The live 283-record dataset currently contains 177 numeric quest provenance records, with IDs ranging from PQ1 to PQ186 and no out-of-range values.
- Existing descriptive string provenance remains supported for records whose research stores the full quest/mission description rather than a numeric ID.


## 2026-09-19 — acquisition-route reconciliation: starting/skill-shop skills

- Reconciled two deterministic acquisition mismatches in the 283-skill dataset.
- `Super Guard`: classified as `starting_move` with no quest ID; its provenance retains both the starting fighting-style route and Skill Shop availability.
- `Time Bullet`: classified as `skill_shop` with no quest ID; its unlock route is the Skill Shop after defeating Kid Buu in the main story.
- Independent public references support these routes; no quest reward or Ultimate Finish requirement was invented.


## 2026-09-19 — Future Saga Chapter 1 PQ provenance normalization

- Reconciled four character-only Future Saga Chapter 1 skills to their exact basic-reward PQs using the maintained all-PQ reward guide: Crimson Edge and Divine Spear → PQ171; Big Bang Knuckle and Wild Stinger → PQ172.
- Replaced ambiguous `PQ171 / PQ172` provenance strings with numeric canonical `source_quest` IDs and exact PQ route labels.
- Corrected Big Bang Knuckle's stale skill-description label from Ki Blast to Strike, matching its canonical class and official move description.


## 2026-09-19 — Ultimate Finish provenance correction: X100 Big Bang Kamehameha

- Corrected `X 100 Big Bang Kamehameha`: `ultimate_finish_required` changed from `true` to `false`.
- The maintained all-186-PQ guide lists X 100 Big Bang Kamehameha in PQ100's **Basic Reward** section, and independent references document TP Medal Shop availability.
- Exact drop probability remains unspecified; no probability was inferred.


## 2026-09-19 — Mixed-route PQ provenance audit

- Reconciled four canonical mixed-route skills against PQ reward evidence and TP Medal Shop evidence: `Emperor's Blast` → PQ70 / TP Medal Shop; `Emperor's Edge` → PQ99 / TP Medal Shop; `Final Kamehameha` → PQ91 / TP Medal Shop / Double Crystal Raids; `X 100 Big Bang Kamehameha` → PQ100 / TP Medal Shop.
- Verified PQ70, PQ91, PQ99, and PQ100 list the corresponding skills as Basic Rewards, so none requires an Ultimate Finish. 
- Final Kamehameha and X 100 Big Bang Kamehameha TP Medal Shop availability is independently documented. 


## 2026-09-19 — Sudden Death Beam acquisition-route normalization

- Corrected `Sudden Death Beam` from a quest-based acquisition classification to `tp_medal_shop`.
- Canonical provenance is now `TP Medal Shop / STP Medal Shop / Double Crystal Raid`, with no `source_quest`.
- Current external evidence explicitly lists all three acquisition routes; no PQ provenance was inferred. 


## 2026-09-19 — Acquisition-type consistency audit

- Rechecked the canonical 283-skill dataset after the Sudden Death Beam correction.
- `quest_or_mission` records: 0 missing `source_quest`.
- Non-`quest_or_mission` records: 0 carrying a non-null `source_quest`.
- Acquisition-type counts were recomputed from the canonical data; no additional deterministic route mismatch was found in this pass.


## 2026-09-19 — Canonical/index synchronization audit

- Compared all 283 canonical skill records with all 283 index records.
- Found and corrected four stale `acquisition_type` values in `skills-index.json`: Explosive Wave, Final Pose, Super Guard, and Time Bullet.
- Post-sync comparison reports 0 mismatches across class, subcategory, verification status, research status, and acquisition type.
- Artifact scan across canonical data, index, audit, and handoff: 0 forbidden citation/tool markers.


## 2026-09-19 — Validator/CI verification pass

- Inspected the dedicated `skills-validation.yml` workflow and current validator/schema sources.
- The workflow installs pinned `jsonschema==4.25.1`, uses Python 3.12, and runs `scripts/validate_skills.py` on canonical skill-data/schema changes.
- Static inspection confirms the validator uses JSON Schema Draft 2020-12, `FormatChecker()`, `check_schema`, and cross-file checks.
- GitHub reports no workflow runs and no commit statuses for the latest handoff commit, so CI execution remains unverified.
- Local execution was attempted but the environment could not resolve GitHub for a repository clone; no local-pass claim is made.


## 2026-09-19 — Burst Rush reward classification correction

- Corrected `Burst Rush`: PQ51 remains the source, but `ultimate_finish_required` changed from `true` to `false`.
- The maintained all-PQ guide lists Burst Rush in PQ51's Basic Reward section, so an Ultimate Finish is not required for the canonical acquisition route. 


## 2026-09-19 — Static schema/invariant validation

- Inspected all schema enums and re-ran the repository's key cross-field invariants against all 283 canonical skill records.
- Schema permits the intended classes (`Super`, `Ultimate`, `Evasive`, `Awoken`, `Counter`, `Mixed`), subcategories including `Transformation`, and all six acquisition types.
- Static invariant result: 0 class/subcategory violations, 0 character-only CaC contradictions, 0 quest/non-quest `source_quest` contradictions.
- GitHub still exposes no workflow runs/statuses for the latest handoff, so no CI pass is claimed.


## 2026-09-19 — Shenron wish acquisition correction

- Corrected `Flash Fist Crush` and `Burst Reflection`: both are Shenron-wish acquisitions, not quest/mission acquisitions.
- Set both to `other_nonquest` with null `source_quest` and preserved the Shenron wish route.
- `Flash Fist Crush` is obtained from the first use of the "I want a new Super Attack!" wish; `Burst Reflection` is part of the subsequent Super Attack wish reward set. 


## 2026-09-19 — PQ Basic Reward finish audit

- Evidence review of PQ51 and PQ32 found two stale Ultimate Finish assertions.
- `Burst Rush` is explicitly listed as a PQ51 Basic Reward; its verification status was upgraded to `verified_current_scope`.
- `Energy Barrier` is explicitly listed as a PQ32 Basic Reward; `ultimate_finish_required` was corrected from `true` to `false`, and the unlock text was corrected accordingly.
- The index was synchronized with the canonical verification metadata.


## 2026-09-19 — PQ Ultimate Finish verification cohort

- Verified three previously partial records from explicit PQ reward evidence: `Earth Splitting Galick Gun` (PQ11), `Burst Stinger` (PQ136), and `Raid Blast` (PQ136).
- All three are documented as Ultimate Finish-dependent rewards; `ultimate_finish_required` remains `true`.
- Synchronized their verification metadata into `skills-index.json`.
- Evidence: maintained PQ data and community reward documentation. 


## Skill DLC provenance correction — 2026-09-20

- Corrected `docs/data/skills.json` for **Evil Blast (PQ114)** and **Evil Flame (PQ117)** so both identify **Extra Pack 1**.
- The maintained PQ transcription and DLC reference place PQ114 and PQ117 in Extra Pack 1. No other skill fields were changed.


## Skill DLC provenance refinement — 2026-09-20

- Replaced generic `DLC PQ` labels with exact DLC provenance for **Flash Chaser (PQ138) → Ultra Pack 2**, **Photon Swipe (PQ139) → Ultra Pack 2**, **Pretty Cannon (PQ133) → Ultra Pack 1**, and **Raid Blast (PQ136) → Ultra Pack 1**.
- The maintained PQ records and independent PQ/DLC references explicitly map these quest numbers to those packs.
- No acquisition, Ultimate Finish, CaC, race, cost, or mechanics fields were changed.


## Skill DLC provenance refinement — Super Pack 2 — 2026-09-20

- Refined **Destruction's Concerto: Comet**, **Destruction's Concerto: Starfall**, **Destruction's Concerto: Meteor**, and **Destruction's Conductor** from the broad `Super Pass` label to **Super Pack 2**.
- The maintained DLC reference identifies DLC 2 / Super Pack 2 as containing PQ104–106 and these skills.
- No Ultimate Finish flags were changed in this pass; the repository's current PQ reward audit was preserved.

### 2026-09-20 — Super Saiyan Blue Kaioken provenance correction

- 2026-09-20: Corrected **Super Saiyan Blue Kaioken** provenance from `Base Game` to `Free Update 1`. Bandai Namco's official Free Update #1 material states that SSGSS Goku's Kaioken x10 was made available as free content ahead of DLC Pack 1; this resolves the previously retained historical ambiguity. No acquisition or character-only fields were otherwise changed.


## 2026-09-20 — Supreme Fury acquisition evidence refinement

- Rechecked the remaining current-scope acquisition/mechanics evidence gap for **Supreme Fury**.
- Current maintained PQ evidence explicitly lists Supreme Fury in **PQ179 — 24/7 Time Patrol — Basic Reward**, so the canonical acquisition route no longer needs the generic "PQ reward context" wording.
- Kept the existing **100 Ki Strike Super** cost and **no Ultimate Finish requirement**; no unsupported drop probability or additional numerical mechanics were added.
- Canonical skill data commit: `3d59895e88f0a0b15705b7fefcb5aa523beb8c91`.
- External evidence: the maintained 186-PQ guide lists Supreme Fury under PQ179 Basic Reward; a separate current discussion describes it as a 100-Ki counter, but that discussion is not used to infer any drop probability. 
- Next: continue the remaining record-level evidence-gap audit, prioritizing acquisition/drop semantics and mechanics where current sources are specific enough to resolve them.


## 2026-09-20 — Current-scope evidence refinement: Power to Overcome / Sudden Death Beam

- **The Power to Overcome:** rechecked current 2026 sources. The core modifiers are consistently supported at Stage 1 +20% defense/+5% speed and Stage 2 +15% basic/+30% Strike-Ki Super, with ~12-second Unleashed duration. Conflicting current measurements remain for exact Stage 1 defense (20% vs 25%), Stage 2 speed (+10% vs +15%), cooldown (~24 vs ~30 seconds), and HP regeneration (~1 bar/60 vs ~1 bar/65 seconds). The record now states those conflicts explicitly rather than implying a single exact value.
- **Sudden Death Beam:** upgraded acquisition provenance with Bandai Namco's official content-update schedule, which explicitly lists the skill in the TP Medal Shop rotation. Current skill documentation also retains STP Medal Shop and Double Crystal Raid Battle as routes. The mechanics note now records the documented Instant Transmission counter/evasive behavior without relying on character-specific users as race restrictions.
- Canonical data commit: f30d937292044d748d5213d6f84de5a1cbdf1334.
- No unsupported drop probability or false-precision mechanics were added.


## 2026-09-20 — Skill classification correction: Dimension Cannon

- **Dimension Cannon** was identified as a higher-priority canonical data error during the current-scope audit. The prior record incorrectly classified it as a 300-Ki Ki Blast Super.
- Current dedicated evidence identifies it as a **300-Stamina Ki Blast Evasive Skill** from **PQ59 — Potara Warrior**; the maintained PQ reward listing places it in the **Basic Reward** section. Its documented behavior is a short-range mouth-fired Ki wave with six hits, knockback, and guard break against a blocking opponent. 
- The canonical `skills.json` record was corrected accordingly, including `class`, `ki_cost`, `stamina_cost`, `damage_type`, unlock wording, and skill description.
- **Heat Wave** was also cleaned up so its canonical description now correctly identifies it as a Strike Super and its PQ179 source, while leaving exact drop gating unresolved.
- Canonical data commit: `0790faf56ac700ff7d1b3c8d28a705531d5472db4`.
- No unsupported drop probability or Ultimate Finish condition was added.


## 2026-09-20 — Current-scope acquisition refinement: God of Destruction's Plaything

- **God of Destruction's Plaything** was refined from generic `PQ175 reward context` to the concrete **Parallel Quest 175 — "Who's the Next Leader?!" Basic Reward** classification.
- The maintained current PQ guide explicitly lists the skill in PQ175's Basic Reward section alongside the quest's other rewards. 
- The record remains a **100-Ki Ki Blast Super**. No individual drop probability, Ultimate Finish-only gate, or unsupported numerical mechanics were added.
- Canonical data commit: `dd32ad55d46d3751b5552459400ddc05d528a29f`.
- Heat Wave remains sourced to PQ179; the current evidence confirms its Basic Reward placement alongside Supreme Fury, but this cycle did not establish a narrower drop condition. 


## 2026-09-20 — Reward-gate reconciliation: PQ96 / PQ151

- **Absolute Zero** was refined from generic/random PQ96 acquisition to the concrete **PQ96 Basic Reward** classification based on the maintained all-PQ reward listing. A separate older video guide labels it an Ultimate Finish reward, so the record explicitly preserves that source conflict rather than asserting an exclusive gate. 
- **Ultrasonic Blitz** and **Celestial Wave** were similarly reconciled against the maintained PQ151 reward listing, which explicitly places both in **Basic Reward**. A separate video guide labels both as PQ151 Ultimate Finish rewards. The canonical records now preserve this conflict and do not claim an exclusive UF gate. 
- Their mechanics were also enriched from current dedicated skill documentation without inventing unsupported values.
- Canonical data commit: `02dc1d7cec09d2816e20b9d657d87b7f0d274964c`.
- No drop probability was added and no source-conflicted reward gate was silently collapsed.


## 2026-09-20 — Concrete Basic Reward provenance: PQ51 / PQ75 / PQ82 / PQ153

- Refined four current-scope records to use the exact quest title and **Basic Reward** classification where the maintained all-PQ reward guide explicitly lists the skill: **Burst Rush** (PQ51), **Counter Burst** (PQ75), **Dragon Burn** (PQ82), and **Counter Impact** (PQ153). 
- These changes improve acquisition provenance without asserting drop probability or an Ultimate Finish requirement. The PQ guide explicitly places each skill in Basic Reward. 
- Canonical data commit: `b33b116342510d130e74bf07dbade46c293944b3`.


## 2026-09-20 — Canonical classification/cost corrections: four base-game skills

- **Ki Explosion** was corrected from an erroneous Evasive/200-Stamina record to a **100-Ki Ki Blast Super**. Dedicated skill evidence identifies it as a Super and describes its hold-to-spend-Ki behavior; the maintained PQ77 listing places it in Basic Reward. 
- **Instant Rise** was corrected from **200** to **300 Stamina**. Dedicated skill evidence lists 300 Stamina and classifies it as an Other Evasive; PQ37's maintained reward listing places it in Basic Reward. 
- **Force Shield** was retained as a 200-Stamina Ki Blast Evasive and its exact source was corrected to PQ59 — "Potara Warrior" Basic Reward. 
- **Change The Future** was refined to the exact PQ43 title/Basic Reward provenance while retaining its confirmed 100-Ki Ki Blast Super counter classification. 
- This pass demonstrates why canonical type/cost mismatches are being prioritized over adding weak descriptive detail. No unsupported drop probabilities were added.
- Canonical data commit: `50100a6f782d6042716cffa66298cfa00f0a95bc`.


## 2026-09-20 — Maiden Burst evidence refinement

- Refined **Maiden Burst** to the exact **PQ92 — "Revenge of the Tuffle" Basic Reward** provenance.
- Dedicated documentation confirms it as a **300-Stamina Ki Blast Evasive**, with a short-range forward explosive attack, knockback, and approximately 5% documented damage. The maintained PQ guide independently lists Maiden Burst in PQ92 Basic Reward. 
- No Ultimate Finish-only gate or unsupported CaC restriction was added.
- Canonical data commit: `8aacc3faa0a40ecaed0c8521bd411410adaa2ffa`.


## 2026-09-20 — Energy Barrier conflict preservation / Spirit Slash provenance

- **Energy Barrier** was re-audited because its record contained contradictory reward semantics: the maintained PQ32 listing places it in Basic Reward, while dedicated evidence describes the CaC acquisition as tied to defeating Cell during the Ultimate Finish. The canonical record now explicitly preserves this conflict instead of asserting either gate as exclusive.
- **Spirit Slash** was refined to the exact **PQ02 — "A Deal?! The Saiyan Brothers" Basic Reward** provenance while retaining the standard skill's documented 200-Stamina Strike Evasive classification. The separate DBS Super Hero Gohan variant's 300-Stamina behavior remains distinguished.
- No unsupported drop probability or exclusive Ultimate Finish requirement was added.
- Canonical data commit: `e9137154c07aae27cc84381339c75c21a5566aed`.


## 2026-09-20 — Exact PQ provenance: Headshot / Rolling Bullet / Victory Cannon / Energy Field

- Refined **Headshot** to PQ69 — "God of Destruction and His Master" Basic Reward; dedicated evidence confirms 300-Stamina Strike Evasive. 
- Refined **Rolling Bullet** to PQ42 — "Artificial Warriors" Basic Reward; dedicated evidence confirms 200-Stamina Ki Blast Evasive. 
- Refined **Victory Cannon** to PQ54 — "Majin Revival" Basic Reward; dedicated evidence confirms 300-Stamina Ki Blast Evasive and ~10% documented damage. 
- Refined **Energy Field** to PQ29 — "The Androids Attack" Basic Reward; dedicated evidence confirms 200-Stamina Ki Blast Evasive. 
- No drop probabilities or Ultimate Finish-only gates were invented.
- Canonical data commit: `e540e613f4f2bea20ef9cfda1d9c11e741aa85be`.


## 2026-09-20 — Exact PQ provenance: six additional evasives

- Refined **Psychic Move** → PQ73 — "Frieza’s Siege Against Earth!" Basic Reward.
- Refined **Spread Shot Retreat** → PQ28 — "Legendary Super Saiyan" Basic Reward.
- Refined **Mach Dash** → PQ18 — "Force Entrance Exam" Basic Reward.
- Refined **Angry Shout** → PQ68 — "Old Rivals and Dragon Balls" Basic Reward.
- Refined **Spirit Explosion** → PQ25 — "The Emperor’s Brother" Basic Reward.
- Kept **Explosive Wave** as Skill Shop provenance; no quest-gate inference was added.
- Steam's maintained PQ guide lists the five quest skills in their respective Basic Reward sections. 
- Canonical data commit: `36191badce56ea7fe3d89c1966b902b996fa979c`.


## 2026-09-20 — canonical classification correction: Paralysis

- Corrected **Paralysis** after rechecking current dedicated skill evidence and the Future Warrior technique corpus.
- The canonical record had incorrectly classified Paralysis as a 100-Ki Ki Blast Super. Current evidence identifies it as a **300-Ki Strike Ultimate** used by Guldo and obtainable by the Future Warrior/CaC from **PQ34 — "Return of the Ginyu Force!"**.
- The maintained PQ evidence places the skill in the **Basic Reward** section, so `ultimate_finish_required` remains `false`.
- Updated `docs/data/skills.json` and synchronized `docs/data/skills-index.json`. No unsupported drop probability was added.
- Evidence also distinguishes this skill from **Paralyze Beam**, the separate 100-Ki Ki Blast Super from PQ4.
- Canonical data commit: `1e2084b303b385b10db3418d429b110a2d99a369`; index sync commit: `98f2462dc8a3b8fde224d9bcdec7569720e45b7c`.


## 2026-09-20 — character-source correction: Dust Attack

- Corrected **Dust Attack**'s stale `character_source` from **Hercule** to **Piccolo**.
- Current evidence identifies Dust Attack as one of Piccolo's Super Skills, and the maintained Future Warrior/partner references support Piccolo as the source character; the PQ78 acquisition route remains unchanged.
- Preserved the existing **Other Super / 100 Ki / CaC-available** classification and did not infer any narrower race/gender/form restriction.
- Canonical data commit: `27272f6c2e8afc63c739e66340ebc89193bf93d8`.


## 2026-09-20 — canonical mismatch pass: Time Bullet / Dragon Thunder / Surging Spirit

- **Time Bullet:** corrected the stale character-exclusive interpretation. Current evidence identifies it as a **100-Ki Other Super** available to CaCs from the **Skill Shop after the Decisive Battle with Majin Buu**.
- **Dragon Thunder:** corrected the stale universal-CaC interpretation. Current evidence identifies it as **Omega Shenron's 100-Ki Strike Super** and explicitly unavailable to CaCs.
- **Surging Spirit:** clarified that the technique is an **Ultra Instinct built-in CaC action**, not a separately acquired equipable skill; the N/A unlock route is therefore retained.
- Revalidated **Destruction's Concerto: Comet** as a variable **100–200 Ki** Super rather than forcing a single unsupported cost. **Wild Stinger** remains cost-unresolved and was not treated as numerically verified.
- Updated `docs/data/skills.json` and synchronized `docs/data/skills-index.json`.
- Commits: `1b3e8da7e5154800da971b95068e8388d0575fb8` (skills), `354106948a7cb49855eeafc24caa261471f42b9b` (index).
- Exact next task: continue the remaining current-scope canonical audit, especially stale `usable_by_cac`, acquisition type, and reward-gate fields; preserve uncertainty where evidence conflicts.


## 2026-09-20 — Future Saga PQ CaC-availability correction

- Corrected **Big Bang Knuckle**, **Divine Spear**, and **Crimson Edge** from stale `usable_by_cac=false` records to CaC-accessible PQ skills.
- Current dedicated skill pages list each as a normal Super Skill with a PQ unlock and do not place them in the cast-exclusive/unavailable-for-CaC category. The PQ guide lists them as Basic Rewards: PQ171 contains Crimson Edge and Divine Spear; PQ172 contains Big Bang Knuckle. 
- Character association (Goku Black or Vegeta) was not treated as proof of character exclusivity; the repository now records CaC availability while retaining the character/source attribution.
- Updated `docs/data/skills.json` and `docs/data/skills-index.json`.
- Commits: `bc8d3e65b2f8a1be0b2293b25231071dc691ae65` (skills), `30a238294dadcca7e9c97ab1f71601e01789fd24` (index).
- Next: continue the canonical audit for remaining stale CaC boundaries and acquisition semantics, then move into unresolved reward-gate conflicts.


## 2026-09-20 — Wild Stinger CaC boundary correction

- Corrected **Wild Stinger** from stale `usable_by_cac=false` / `Character-only` to CaC-accessible while retaining its PQ172 Basic Reward acquisition and unresolved exact Ki-cost uncertainty.
- This completes the remaining currently identified `usable_by_cac=false` + `quest_or_mission` anomaly in the canonical dataset: after the correction, no record combines those fields.
- Updated `docs/data/skills.json` and `docs/data/skills-index.json`.
- Commits: `e6cf43c75731a6c53f4fa6af03bde4bbf9e59ba3`, `4c20ab2d793447f6ac539a565b1ebac1524eab4b`.


## 2026-09-20 — Lovely Cyclone reward-gate correction

- Corrected **Lovely Cyclone** `ultimate_finish_required` from `true` to `false`.
- Existing repository evidence explicitly reconciles PQ135 placement as a **Basic Reward** and notes that difficult RNG/community reports do not establish an Ultimate Finish-only condition. The canonical flag now matches that evidence.
- Updated `docs/data/skills.json` and `docs/data/skills-index.json`.
- Commits: `5d3777ff2729d42c86bf2aa5436b86a127fcef12`, `2ad9ac722d9071209c51d09274a1f4ae969e9e64`.


## 2026-09-20 — Super Dragon Flight reward-gate correction

- Corrected **Super Dragon Flight** `ultimate_finish_required` from `true` to `false` and refined provenance to **PQ31 — "Let's Train!" Basic Reward**.
- Current Xenoverse 2 evidence lists Super Dragon Flight directly under PQ31's Basic Reward section. The quest's third win condition is defeating revived Gohan, not a separate Ultimate Finish-only skill gate. 
- Updated `docs/data/skills.json` and `docs/data/skills-index.json`.
- Commits: `954da8c6fa6959679d5d19aa4cf46e337953b334`, `8a5e9de234e05e6a0a055e1f6edcf0fb882b99ad`.


## 2026-09-20 — Two additional Ultimate Finish gate corrections

- **Chaotic Time Impact:** corrected `ultimate_finish_required` from `true` to `false`; PQ184 current reward evidence lists it under Basic Reward, while the separate UF bonus contains other rewards. 
- **Core Breaker:** corrected `ultimate_finish_required` from `true` to `false`; current PQ158 reward evidence lists Core Breaker under Basic Reward. 
- Updated `docs/data/skills.json` and `docs/data/skills-index.json`.
- Commits: `cc2375f58469809f700a2fbe346fb446c750f1e`, `7fbd5f1ca241b6a27af13ace1978854f95405e67`.


## 2026-09-20 — Blazing Attack reward-gate correction

- Corrected **Blazing Attack** `ultimate_finish_required` from `true` to `false`.
- Current maintained PQ136 reward tables explicitly place Blazing Attack in **Basic Reward**, alongside Burst Stinger and Raid Blast. 
- A GameFAQs post reports Blazing Attack as an Ultimate Finish drop, so the repository preserves that conflicting evidence in mechanics notes rather than silently treating it as authoritative; the explicit maintained reward-tier listing controls the canonical field. 
- Updated `docs/data/skills.json` and `docs/data/skills-index.json`.
- Commits: `2a82e01e7e3fda477469683cb692bb7b971b6006`, `1cf8e2cd98615f8d2e4101827b3a79b47039e561`.


## 2026-09-20 — Three additional Ultimate Finish gate corrections

- **Rough Ranger:** corrected `ultimate_finish_required` from `true` to `false`; PQ119 reward tables list it under Basic Reward. 
- **Earth Splitting Galick Gun:** corrected `ultimate_finish_required` from `true` to `false`; the long-maintained PQ guide lists it under PQ11 Basic Reward. A newer datamined reconstruction conflicts, so the canonical field follows the explicit reward-tier table while preserving source provenance. 
- **Raid Blast:** corrected `ultimate_finish_required` from `true` to `false`; PQ136 reward tables explicitly list it under Basic Reward. 
- Updated `docs/data/skills.json` and `docs/data/skills-index.json`.
- Commits: `15f4426e56268d41e3deb456619dd7ef47314007`, `c5fc07873e090b03d01c1d99c30abfb299c9eb5a`.


## 2026-09-20 — Final Ultimate Finish gate validation

- Revalidated the remaining two `ultimate_finish_required=true` records: **Kaioken** is explicitly documented as requiring PQ8's Ultimate Finish, and **Power Rush** is explicitly documented as the PQ122 Ultimate Finish skill. 
- No canonical field changes were made because the current records already match the evidence.
- Canonical census remains **283 records / 78 `verified_current_scope` / 2 Ultimate Finish-gated**.
- The next audit category is now **generic `quest_or_mission` acquisition wording** among verified current-scope records, beginning with records such as Mighty Explosive Wave, Side Bridge, Steel Mirage, Demon Ray, and other PQ acquisitions whose unlock text is still only `Parallel Quest reward` / `Random Parallel Quest reward`.


## 2026-09-20 — Generic PQ acquisition wording pass

- Refined four current-scope records whose unlock text was too generic:
  - **Mighty Explosive Wave** → PQ79 Basic Reward.
  - **Side Bridge** → PQ39 Random Reward.
  - **Steel Mirage** → PQ165 Random Reward.
  - **Demon Ray** → PQ160 Ultimate Finish Bonus.
- The Demon Ray correction is especially important: current PQ160 data explicitly places it in the UF bonus pool. 
- Mighty Explosive Wave is independently documented as a PQ79 acquisition. 
- Side Bridge is documented as a random PQ39 reward, while Steel Mirage is tied to PQ165. 
- Updated `docs/data/skills.json` and `docs/data/skills-index.json`.
- Commits: `4eaa298f9b3f700e19474bd...`, `3fc1aaebcb265bd42fba833de5442a9765a08766`.


## 2026-09-20 — Evil Blast / Final Cannon / PQ provenance cleanup
- Evil Blast corrected to 300-Ki Ki Blast Ultimate with PQ114 Ultimate Finish acquisition evidence.
- Final Cannon corrected to Strike Super and Trunks (Kid), with PQ52 random-reward provenance.
- Evil Flame, Eraser Bomb, and Dust Attack refined to concrete PQ reward listings.
- Next: continue generic PQ acquisition/type audit, prioritizing Emperor's Blast and Emperor's Cannon.


## 2026-09-20 — Emperor skill acquisition audit
- **Emperor's Blast:** retained PQ70 as the concrete acquisition source; current reward tables explicitly list it in PQ70 Basic Reward, while dedicated skill documentation confirms it is a 100-Ki Ki Blast Super. TP Medal Shop availability remains an alternate route. Corrected source metadata to Golden Frieza and refreshed verification date. 
- **Emperor's Cannon:** investigated the PQ source discrepancy. The dedicated current skill page says **PQ184 — The Invincible Duo**, while the maintained 186-PQ reward guide explicitly lists **Emperor's Cannon under PQ183 — Broly vs. Broly**. The canonical record retains the dedicated-page PQ184 value but now records the PQ183 conflict instead of presenting an unresolved generic `Parallel Quest reward` string as settled fact. 
- Rebuilt `docs/data/skills-index.json` from the canonical `skills.json` after detecting and repairing a malformed index entry introduced during the previous synchronization pass. Both datasets now contain 283 records and the index is valid JSON again.
- Exact next task: continue the generic acquisition audit, using concrete PQ reward tables to resolve remaining `Parallel Quest reward` / `Random Parallel Quest reward` entries while preserving source conflicts when current references disagree.


## 2026-09-20 — PQ reward-tier refinement batch
- **Demon Flash Strike:** refined to **PQ160 — Pan in Peril, Ultimate Finish bonus**. Current PQ160 reward data lists the skill in UF bonus slots, and dedicated skill documentation confirms PQ160. 
- **Atomic Blast:** refined to concrete **PQ87 — Saiyan Battle** acquisition. Dedicated skill documentation confirms the quest; exact reward tier remains unasserted. 
- **Burning Attack:** refined to **PQ41 — Warriors' Annihilation - Future Chapters, Basic Reward**. Both dedicated skill documentation and an independent PQ41 reward listing support the quest/reward tier. 
- **God Punisher:** refined to concrete **PQ132 — The Ultimate Legendary Super Saiyan** acquisition; reward tier remains generic because the inspected sources establish the quest but not a sufficiently reliable specific slot. 
- Re-synchronized `docs/data/skills-index.json` from canonical `skills.json`; dataset remains at 283 records.
- Exact next task: continue the remaining generic PQ acquisition records, prioritizing entries with a known quest number and unresolved reward tier before tackling records with explicit source conflicts.


## 2026-09-20 — PQ reward-tier refinement batch 2
- **Dimensional Hole:** refined to **PQ80 — The Return of the Giant Ape-Fest, Basic Reward**. 
- **God Breaker:** refined to **random reward from PQ44 — Dragon Balls of the Future**. The dedicated skill source explicitly says random reward; the maintained PQ44 reward table does not list it as a Basic Reward, so no Basic tier was inferred. 
- **Heroic Counter:** refined to **PQ155 — I Need a Hero... Pose!, Basic Reward**. 
- **Punisher Shield:** refined to **PQ129 — Frieza Force on the Hunt, Basic Reward**. 
- Re-synchronized `docs/data/skills-index.json` from canonical `skills.json`; record count remains 283.
- Exact next task: continue remaining generic PQ records, especially the older base-game entries where maintained reward tables can establish Basic Reward versus random/UF provenance.


## 2026-09-20 — PQ reward-tier refinement batch 3
- **Blaster Ball:** concrete PQ125 acquisition retained, but reward tier remains generic because inspected sources did not directly establish Basic vs. Ultimate Finish. 
- **Bluff Kamehameha:** refined to **random reward from PQ94 — Ultimate Power, Ultimate Saiyan**. 
- **Breaker Energy Wave:** refined to **PQ101 — Seeking Fighters for Tournament, Basic Reward**. 
- **Burst Kamehameha:** refined to **PQ72 — First Training, Basic Reward**. 
- Re-synchronized `docs/data/skills-index.json`; record count remains 283.
- Exact next task: continue the remaining generic PQ records, preserving random-reward wording where dedicated sources explicitly describe RNG acquisition.


## 2026-09-20 — PQ reward-tier refinement batch 4
- Refined **Buu Buu Ball** → PQ88 Basic Reward; **Candy Beam** → PQ66 Basic Reward; **Candy Beam (Super)** → PQ113 Basic Reward; **Crazy Finger Shot** → PQ26 Basic Reward; **Death Psycho Bomb** → PQ33 Basic Reward.
- Refined **Destruction's Concerto: Starfall** → PQ104 Basic Reward and **Flash Chaser** → PQ138 Basic Reward.
- Refined **Gamma Blaster** → random reward from PQ155; no unsupported reward tier was inferred.
- Re-synchronized `docs/data/skills-index.json`; record count remains 283.
- Exact next task: continue the remaining generic/random PQ records, moving through the list in quest order and preserving explicit RNG provenance.


## 2026-09-20 — PQ reward-tier refinement batch 5
- **Giant Cluster:** refined to random reward from PQ163.
- **Photon Swipe:** PQ139 Basic Reward.
- **Pretty Cannon:** PQ133 Basic Reward.
- **Ray Blast:** PQ125 Basic Reward.
- **Reverse Shot:** PQ123 Basic Reward.
- **Shine Shot:** PQ7 Basic Reward.
- **Spirit Blaster:** PQ129 Basic Reward.
- **Spirit Pulse:** refined to random reward from PQ151.
- Re-synchronized `docs/data/skills-index.json`; record count remains 283.
- Exact next task: continue the remaining generic/random PQ records in quest order.


## 2026-09-20 — PQ acquisition refinement batch 6
- Refined **Wild Buster** → PQ153 random reward; **Hero's Flute** → PQ116 Basic Reward; **Brave Sword Slash** → PQ116 Basic Reward; **Death Slash** → PQ23 Basic Reward.
- Refined **Demon Flurry** → PQ160 random reward; **Demonic Destruction** → PQ159 random reward; **Destruction's Conductor** → PQ106 Basic Reward; **Freedom Kick** → PQ29 Basic Reward.
- Re-synchronized `docs/data/skills-index.json`; record count remains 283.
- Exact next task: investigate the remaining higher-DLC PQ records with unresolved drop gating (Dragon Spark, Dragon Spiral, Force Edge, Heroic Assault, and adjacent entries), preserving conflicts where sources disagree.


## 2026-09-20 — Higher-DLC PQ refinement batch 7
- Refined **Dragon Spark** → PQ177 Basic Reward; **Dragon Spiral** → PQ185 Basic Reward; **Force Edge** → PQ180 Basic Reward; **Heroic Assault** → PQ156 random reward.
- Preserved the older PQ186 association for Dragon Spiral as a source conflict in notes rather than inventing a second acquisition route.
- Re-synchronized `docs/data/skills-index.json`; record count remains 283.
- Next pass: remaining unresolved/random PQ records, beginning with Justice Drive, Justice Kick, Mach Punch, Burning Blast, and Teleporting Vanishing Ball.


## 2026-09-20 — PQ reward-tier refinement batch 8
- Refined **Justice Drive** → PQ168 Basic Reward; **Justice Kick** → PQ152 Basic Reward; **Mach Punch** → PQ19 Basic Reward; **Burning Blast** → PQ180 Basic Reward.
- Refined **Teleporting Vanishing Ball** → PQ62 Basic Reward while preserving a historical GameFAQs report that treated it as an Ultimate Finish drop; no UF-only gate is asserted in canonical data.
- Re-synchronized `docs/data/skills-index.json`; record count remains 283.
- Next pass: continue the remaining generic/random PQ records after these tier-confirmed entries.


## 2026-09-20 — PQ reward-tier refinement batch 9
- Refined **Atomic Blast** → PQ87 Basic Reward; **Blaster Ball** → PQ125 Basic Reward; **Destruction's Concerto: Comet** → PQ104 Basic Reward; **God Punisher** → PQ132 Basic Reward; **Meteor Strike** → PQ6 Basic Reward.
- Re-synchronized `docs/data/skills-index.json`; record count remains 283.
- Next pass: continue remaining generic/random PQ records, prioritizing entries whose current notes still lack concrete reward-tier evidence.


## 2026-09-20 — PQ reward-gate refinement batch 10
- Refined eight current-scope skill acquisition records from the live canonical PQ reward tables:
  - **Apocalyptic Burst** → PQ161 Ultimate Finish bonus slot (45%).
  - **Special Beam Cannon (Beast)** → PQ162 Ultimate Finish bonus slot (45%).
  - **Divine Ray Bomb** → PQ173 Ultimate Finish bonus slot (45%).
  - **God of Destruction's Poise** → PQ175 Ultimate Finish reward (50%).
  - **Shooting Strike** → PQ156 Ultimate Finish bonus slot (50%).
  - **Super Gamma Blast** → PQ158 Ultimate Finish bonus slot (50%).
  - **Soaring Rush** → PQ177 Ultimate Finish reward (50%).
  - **Seagull Combination** → PQ167 normal-clear reward (40%).
- These changes replace generic `Parallel Quest reward` / `Random Parallel Quest reward` wording only where the current maintained batch data supplies a concrete reward gate.
- Re-synchronized `docs/data/skills-index.json`; canonical and index datasets remain at 283 records.
- Live census after the batch: **283 total / 78 `verified_current_scope` / 10 `ultimate_finish_required=true` / 46 still-generic PQ acquisition strings** under the exact generic wording census.
- Evidence limitation: the recorded percentages are the current maintained PQ reward-slot values; they are not presented as independently measured empirical probabilities. No unsupported prerequisite was added.
- Artifact cleanup: removed legacy ChatGPT/internal citation markup from this audit file; repository files must contain ordinary source URLs/prose only.
- Next: continue the remaining generic PQ acquisition records in quest order, prioritizing known PQs whose live reward tables can distinguish Basic, random, and Ultimate Finish provenance.


## 2026-09-20 — PQ reward-tier refinement batch 11
- Refined four base-game generic acquisition records using the maintained PQ batch reward sections:
  - **Unrelenting Barrage** → PQ10 — *Saiyan Survivors*, Basic Reward.
  - **Sauzer Blade** → PQ27 — *Metal Cooler Riot*, Basic Reward.
  - **Heat Dome Attack** → PQ40 — *The Future Warriors!*, Basic Reward.
  - **Chain Destructo-Disc Barrage** → PQ46 — *16 of the Official History*, Basic Reward.
- All four remain explicitly **not Ultimate Finish-gated** in canonical skill data because the maintained reward tables place them in Basic Reward sections.
- Re-synchronized `docs/data/skills-index.json`; dataset remains **283 records**.
- Canonical generic-PQ census should now be recomputed from the live file rather than assumed from the previous 46-record count.
- No reward probability was inferred: Basic Reward identifies the reward tier, not an empirical drop percentage.
- Next: continue the generic PQ acquisition audit in quest order, moving to the next unresolved records after PQ46 and preserving explicit random/UF/source-conflict evidence.


## 2026-09-20 — PQ reward-tier refinement batch 12
- Refined eight generic skill acquisition records from maintained PQ reward data: **Burning Attack (PQ41), Majin Kamehameha (PQ60), Recoome Kick (PQ61), Scissors Paper Rock (PQ65), Super God Fist (PQ67), Last Emperor (PQ71), Warp Kamehameha (PQ76), Saiyan Spirit (PQ84)**.
- Each is recorded as a **Basic Reward** route and remains `ultimate_finish_required=false`; no drop percentage was inferred from reward-tier placement.
- Re-synchronized `docs/data/skills-index.json`; canonical dataset remains 283 records.
- Live generic PQ acquisition census after this batch: **34** exact generic `Parallel Quest reward` / `Random Parallel Quest reward` records.
- Next quest-order frontier: **Zigzag Express (PQ85), Neo Wolf Fang Fist (PQ86), Dimension Ray (PQ98), Sonic Bomb (PQ105), God of Destruction's Menace (PQ105), God of Destruction's Roar (PQ105), Destruction's Concerto: Meteor (PQ106), Requiem of Destruction (PQ106), Super Black Kamehameha Rosé (PQ109), Holy Wrath (PQ111)**.


## 2026-09-20 — PQ reward-tier refinement batch 13
- Refined six generic PQ acquisition records from maintained reward tables: **Zigzag Express (PQ85), Neo Wolf Fang Fist (PQ86), Dimension Ray (PQ98), Sonic Bomb (PQ105), God of Destruction's Menace (PQ105), God of Destruction's Roar (PQ105)**.
- All six are explicitly recorded as **Basic Reward** routes with `ultimate_finish_required=false`; the Sonic Bomb historical conflict is resolved in favor of the maintained current reward table, without asserting a probability.
- Re-synchronized `docs/data/skills-index.json`; canonical dataset remains 283 records.


## 2026-09-20 — PQ reward-tier refinement batch 14
- Refined six generic PQ acquisition records: **Destruction's Concerto: Meteor (PQ106), Requiem of Destruction (PQ106), Super Black Kamehameha Rosé (PQ109), Holy Wrath (PQ111), Lightning of Absolution (PQ111), Blades of Judgment (PQ112)**.
- All six are explicitly recorded as **Basic Reward** routes with `ultimate_finish_required=false`; no reward probability was inferred.
- Re-synchronized `docs/data/skills-index.json`; canonical dataset remains 283 records.


## 2026-09-20 — PQ reward-tier refinement batch 15
- Refined six generic PQ acquisition records: **S.S. Deadly Bomber (PQ115), Brave Sword Attack (PQ117), Power Impact (PQ120), Variant Drive (PQ123), Revenge Final Flash (PQ124), Gigantic Breaker (PQ126)**.
- All six are explicitly recorded as **Basic Reward** routes with `ultimate_finish_required=false`; no reward probability was inferred.
- Re-synchronized `docs/data/skills-index.json`; canonical dataset remains 283 records.


## 2026-09-20 — PQ reward-tier refinement batch 16
- Refined eight generic PQ acquisition records: **Gigantic Burst (PQ127), Revenge Death Ball (PQ127), Powered Shell (PQ128), Gigantic Roar (PQ132), Lovely Cyclone (PQ135), Ribrianne's Eternal Love (PQ137), Total Detonation Ball (PQ139), Savory Slicer (PQ140)**.
- Reward-tier semantics were resolved from maintained current PQ data: PQ127/PQ128 skills are Basic Reward; Gigantic Roar and Total Detonation Ball are first-clear routes; Lovely Cyclone, Ribrianne's Eternal Love, and Savory Slicer are Ultimate Finish bonus-slot routes.
- Accordingly, `ultimate_finish_required` is true only for **Lovely Cyclone, Ribrianne's Eternal Love, and Savory Slicer** in this batch. No probability was inferred beyond existing maintained evidence.
- Re-synchronized `docs/data/skills-index.json`; canonical dataset remains 283 records.


## 2026-09-20 — PQ reward-tier refinement batch 17
- Refined **Demon Flash Strike (PQ160)** as a 45% Ultimate Finish bonus-slot route; **Gigantic Explosion (PQ164)** as a 40% Ultimate Finish route; **Full Power Destruction (PQ177)** as a 50% Ultimate Finish bonus-slot route; and **Venus Fist (PQ186)** as a Basic Reward route with no Ultimate Finish requirement.
- Preserved the maintained corpus' explicit percentages for PQ160/PQ164/PQ177; no probability was inferred for Venus Fist.
- Numbering-gap policy remains unchanged: PQ141-PQ150 are not manufactured as records because the maintained reconciliation marks that range as a numbering gap.
- Re-synchronized `docs/data/skills-index.json`; canonical dataset remains 283 records.


## 2026-09-20 — PQ154 gating reconciliation
- Corrected **Circle Flash** and **Sign of Awakening** from generic Random Parallel Quest labels to the maintained **PQ154 Ultimate Finish bonus slot (40%)** route.
- Evidence: `docs/data/parallel-quest-research-batches/pq-batch-15.json` explicitly lists both skills under PQ154 `skill_rewards` with 40% Ultimate Finish bonus-roll conditions.
- This removes an ambiguity rather than inventing a probability; both records now set `ultimate_finish_required=true`.


## 2026-09-20 — unresolved race-scope consistency audit
- Corrected six records whose own audit notes explicitly said CaC race/gender/form scope was unresolved while `race_restriction` still incorrectly read `All CaC races`: **Super God Fist, Variant Drive, Blaster Stream, Chain Destructo-Disc Barrage, Circle Flash, and Chaotic Time Impact**.
- Their `race_restriction` fields are now `null`; no new race restriction or universal-race claim is inferred.
- This is a consistency correction only and does not alter acquisition provenance or reward gating.


## 2026-09-20 — stale reward-tier note cleanup
- Corrected **Chaotic Time Impact** to match its reconciled PQ184 evidence: **50% Ultimate Finish bonus reward**, with `ultimate_finish_required=true`.
- Updated **Circle Flash** notes to reflect the already-established PQ154 40% Ultimate Finish bonus roll instead of saying its gating remained unresolved.
- Updated **Sonic Bomb** notes so the unresolved portion is limited to exact probability/mechanics; its Basic Reward classification is now treated as resolved.


## 2026-09-20 — generic PQ acquisition closure and reward-gate consistency audit
- Refined the final two exact-generic PQ acquisition records from the live canonical skill census:
  - **Lightning Impact** → PQ142 — *Timespace Tussle*, Basic Reward.
  - **Blaster Stream** → PQ148 — *Finding Out About Fusion*, Basic Reward.
- Evidence: the maintained Steam all-PQ guide explicitly lists Lightning Impact under PQ142 Basic Reward and Blaster Stream under PQ148 Basic Reward. No Ultimate Finish requirement was inferred.
- Corrected a separate reward-gate inconsistency found during the same live-file audit: **Demon Ray** is a PQ160 Ultimate Finish bonus route, so `ultimate_finish_required` is now `true`; the maintained PQ160 data records a 50% Ultimate Finish bonus roll.
- Re-synchronized `docs/data/skills-index.json`; canonical dataset remains **283 records**.
- Live exact-generic acquisition census after this pass: **0** records using the exact strings `Parallel Quest reward` or `Random Parallel Quest reward`.
- The repository still preserves historical/source conflicts where they exist; no PQ141–150 quest records were fabricated.
- Validation: canonical skills JSON and skills index JSON parsed successfully after the edits. A live reward-gate consistency scan found no remaining true-flag records lacking Ultimate Finish evidence; known historical conflicts remain explicitly documented rather than flattened.
- CI: latest push-triggered **Repository quality** and **Clean internal artifacts** runs for commit `4ab14c06054cabc29f851f0db0c89ac1f91e5ead` failed with a single job each and **no recorded steps/logs**. This matches the established opaque pre-step infrastructure/account failure pattern; validators were not weakened or bypassed.
- Exact next task: recompute the live skill census and continue P1 skill provenance/consistency cleanup outside the now-closed generic PQ acquisition strings, prioritizing stale acquisition notes, DLC/free-update provenance, CaC scope, and any remaining evidence contradictions.

## 2026-09-20 — stale reward-gate note cleanup (Chaotic Time Impact)
- Re-audited canonical skill notes for explicit stale/incorrect reward-gate language after closing generic PQ acquisition strings.
- Corrected **Chaotic Time Impact**: current PQ184 evidence places it in the **Basic Reward** pool, so `ultimate_finish_required` is now **false** and the stale note claiming an Ultimate Finish route was removed.
- Preserved the separate race-scope uncertainty: `race_restriction` remains `null` rather than inferring a universal CaC scope.
- Re-synchronized `docs/data/skills-index.json`.
- Live canonical census remains **283 records**; exact-generic PQ acquisition census remains **0**.
- Validation target for next pass: continue scanning explicit stale/incorrect notes and source conflicts, with priority on acquisition semantics and provenance rather than inventing unsupported quest or race data.

## 2026-09-20 — skill reward-gate contradiction reconciliation
- Rechecked canonical skill reward-gate flags against the maintained PQ batch drop-condition records instead of relying on stale milestone notes.
- Corrected **Chaotic Time Impact (PQ184)** to `ultimate_finish_required=true` with the documented 50% Ultimate Finish bonus slot; the prior Basic Reward classification was stale.
- Corrected **Core Breaker (PQ158)** to `true` with the documented 40% Ultimate Finish bonus slot.
- Corrected **Earth Splitting Galick Gun (PQ11)** to `true` because the maintained PQ11 record documents a 50% Ultimate Finish roll; the separate Basic Reward listing is preserved as source evidence rather than treated as an exclusive gate.
- Corrected **Raid Blast (PQ136)** and **Blazing Attack (PQ136)** to `true`, matching their documented 25% Ultimate Finish / Ultimate Finish bonus slots.
- Corrected **Burst Stinger (PQ136)** to `false`, matching its documented 25% first-clear slot.
- Corrected **Time Control (PQ18)** to `false`; current maintained PQ18 data lists it in Basic Reward and does not establish an Ultimate Finish-only gate.
- Cleaned **Super Dragon Flight (PQ31)** to `false`, matching its maintained Basic Reward listing and removing stale Ultimate Finish wording from its mechanics note.
- Re-synchronized `docs/data/skills-index.json`; canonical/index parity is restored at **283 records**.
- Evidence limitation: some PQ batch records contain both Basic Reward listings and explicit drop-condition slots. Where an explicit current drop condition exists, the canonical gate follows that condition while preserving the underlying source metadata; no unsupported probability was invented.



## 2026-09-20 — CaC race-scope evidence reconciliation
- Resolved three previously null CaC race fields from explicit Future Warrior evidence: **Super God Fist**, **Variant Drive**, and **Chain Destructo-Disc Barrage** → `All CaC races`.
- The evidence establishes Future Warrior acquisition in Xenoverse 2, while no narrower race/gender/form restriction is documented. No race-specific inference was made.
- Canonical/index parity remains exact at 283 records.


## 2026-09-20 CaC race-restriction provenance and taxonomy pass

- Re-audited the handoff-prioritized older race-restricted skills against current dedicated skill documentation and maintained PQ/shop evidence.
- Corrected two canonical taxonomy errors: **Buu Buu Ball** is a 300-Stamina Strike Evasive from PQ88, and **Saiyan Spirit** is a 300-Ki Ki Blast Ultimate from PQ84.
- Re-synchronized **Celestial Wave** index metadata with the canonical Ultimate-Finish flag while preserving the conflicting Basic Reward vs Ultimate Finish source evidence.
- Namek Finger remains a Namekian-restricted TP Medal Shop skill; Darkness Rush (Ranged) remains Namekian-only and learned through Lord Slug training; Evil Flight Strike remains Namekian/Majin; Zigzag Express remains Male Majin; Explosive Buu Buu Punch remains Majin; Angry Shout remains the PQ68 Evasive route.
- Validation: canonical and index datasets both contain **283 records**; corrected record identities are synchronized; no validators were changed.
- Evidence limitation: several reward records still expose source disagreement about exact reward-slot semantics. Those conflicts remain explicit rather than being normalized away.


## 2026-09-20 — remaining PQ reward-condition reconciliation batch
- Workstream: P1 skill acquisition/reward-tier provenance cleanup after the broad stale-UF census.
- Live canonical skill census: **283 records; 60 ultimate_finish_required=true; 223 non-UF records**.
- Reconciled **17 skills** whose canonical acquisition text conflicted with the maintained explicit PQ drop-condition records: **Steel Mirage (PQ165, 45% UF bonus), Big Bang Knuckle (PQ172, 40% UF bonus), Divine Spear (PQ171, 50% UF), Eraser Bomb (PQ163, 40% UF bonus), God of Destruction's Plaything (PQ175, 50% UF), Heat Wave (PQ179, 50% UF), Pendulum Bullet (PQ166, 50% UF), Variable Snipe Shot (PQ165, 45% UF), Burst Blitz (PQ178, 50% UF bonus), Crimson Edge (PQ171, 45% UF bonus), Dragon Spark (PQ177, 50% UF), Force Edge (PQ180, 50% UF), Justice Drive (PQ168, 40% UF bonus), Wild Stinger (PQ172, 45% UF), Burning Blast (PQ180, 50% UF), Final Rampage (PQ174, 60% UF), and Supreme Fury (PQ179, 50% UF)**.
- The canonical UF flag now follows the maintained explicit drop-condition record for these 17 records. The maintained Steam all-PQ guide also presents these skills in Basic Reward lists, so that conflicting reward-table presentation was retained in the canonical notes instead of being silently discarded.
- Refined four additional generic PQ acquisition strings where the evidence supports a concrete reward tier while preserving conflicts: **Burst Charge** and **Ultimate Charge** → PQ134 Basic Reward, with a conflicting maintained datamined 25% first-clear report; **Prominence Flash** → PQ137 Basic Reward, with a conflicting maintained datamined 20% first-clear report; **Seagull Combination** → PQ167 reward with a maintained datamined 40% normal-clear report versus the Steam Basic Reward presentation.
- Validation: skills.json and skills-index.json both parse successfully, contain 283 records, preserve exact record-order parity, and contain no detected ChatGPT/internal citation artifacts. A live reward-gate consistency scan now leaves only the known **Lovely Cyclone** exception: PQ135's maintained 25% Ultimate Finish bonus-slot condition remains in deliberate conflict with its canonical ultimate_finish_required=false flag.
- Evidence limitations: the 17 UF corrections intentionally preserve the Basic Reward vs explicit drop-condition conflict; no additional probability or prerequisite was inferred. The four non-UF refinements preserve first-clear/normal-clear conflicts rather than choosing unsupported certainty.
- Commits: fe2350af85edee8087d91a143cfb4fac8c888a27, 90838348eda25ce0efae55c52167a9099bcdcd1d, 1fd53d0f57802ebfd73d23bca5c888386e86f350, a9e19c0ccbd9b2c95017edf938915700e2c34975 (canonical skill data); 48902d9b6d0083748ae1260f4ae7d85c300e71ed, 7503dccb29f9ce04dfb4cc0cf0fc3f1820f7f981, cdaa3bfa40a99170a694be44069414d56342223d, f31331041eb63fd179a6200a92c10f3d0e996564 (synchronized index).
- CI: the latest pre-cycle push for aa70adb6dd3d0b8c9b850f8d22fb43e926a6bb8e had Repository quality and cleanup failures with jobs exposing no recorded steps; this matches the documented infrastructure/account failure pattern. No validators were weakened.
- Exact next task: **recompute the live generic PQ census and continue quest-order provenance cleanup for the remaining generic records, prioritizing cases where current maintained reward tables or independent sources can distinguish Basic Reward, first-clear, normal-clear, Ultimate Finish, or a documented source conflict.**


## 2026-09-20 — generic PQ provenance normalization continuation
- Corrected two stale canonical quest relationships discovered during the live generic census: **Solar Flare** now points to PQ3, "World Tournament Tag Team" (the maintained PQ reward batch contains Solar Flare under PQ3); **Taunt** now points to PQ45, "Take Back the Dragon Balls!" (the maintained PQ reward batch contains Taunt under PQ45). The previous Solar Flare PQ1 and Taunt PQ20 strings were stale and were not retained as current acquisition values.
- Normalized exact quest-title wording for 15 additional non-UF generic PQ skill records where the maintained batches identify the reward relationship but do not establish an exact drop tier: **Vanishing Ball, Afterimage Strike, Kai Kai, Charge, Do or Die, Fighting Pose H, Justice Pose, Burning Slash, Evil Flight Strike, Evil Whirlwind, Shining Slash, Divine Wrath: Purification, Explosive Buu Buu Punch, Gigantic Rage, Victory Rush**.
- No Ultimate Finish flags were changed in this cycle. Exact drop tiers remain explicitly unresolved for those normalized records; no gate was inferred.
- Validation: canonical skills.json and skills-index.json remain at **283 records**, exact record-order parity is preserved, UF count remains **60**, and no internal citation artifacts were detected.
- Commits: 6fedf7406a146addf1e1a09aa01b2af163aa2337 (canonical provenance corrections), a7b4dc4346fd6033eb12fa4f6212c7c83fe62a11 (index synchronization), 4c8ce69cdd8a864ab239c31ea11df11f1f5f6033 (generic PQ wording normalization), 297f9ad4eb1b8e3d8aaffeda7cccd460647a1d31 (index synchronization).
- Exact next task: **continue the generic PQ census for the remaining quest-or-mission skill records, prioritizing stale quest-number/title mismatches and then records where independent maintained sources can establish an exact reward tier. Preserve documented source conflicts and unresolved probabilities instead of inferring them.**


## 2026-09-20 — PQ source-field schema normalization
- Normalized all remaining `source_quest` values in canonical `docs/data/skills.json` that were encoded as strings such as `Parallel Quest 24` into numeric quest IDs. **29 records** were normalized; non-PQ sources (mentors, time rifts, advancement tests, expert missions, etc.) remain textual because they are not PQ IDs.
- Synchronized the same numeric PQ IDs into `docs/data/skills-index.json`.
- Validation: canonical and index remain **283 records**, exact record-order parity is preserved, UF count remains **60**, and no PQ-formatted string remains in `source_quest`.
- Commits: `21b70af1677724e81cfe3dbad49cf38cc469c513` (canonical) and `1c5ce0a27a4a538a76ece00484381e9eecae9d31` (index).
- Exact next task: **continue provenance cleanup for remaining quest-or-mission skills whose acquisition text is still vague, conflicting, or missing a concrete maintained quest/reward tier; do not alter non-PQ source fields merely for schema uniformity.**


## 2026-09-20 — generic PQ reward-tier refinement
- Refined **16 generic quest-or-mission skill records** whose maintained PQ reward batches explicitly place the skill in `Basic Reward`: Double Death Slicer, Kamehameha, Super Ghost Buu Attack, Charged Ki Wave, Phantom Fist, Time Control, Divinity Unleashed, Gigantic Charge, Petrifying Spit, Meditation, Indomitable, Final Kamehameha, Final Flash (SS3 DAIMA), Super Kamehameha (SS4 DAIMA), Solar Flare, and Taunt.
- Final Kamehameha retains its additional TP Medal Shop/Double Crystal Raids routes; the refinement only makes the PQ91 tier explicit. No UF-only gate was inferred.
- Validation: canonical/index remain **283 records**, exact record-order parity, UF count **60**. PQ source fields remain normalized as numeric IDs.
- Commits: `d0918167ed467edf45f4758293b4f5634ec76af8` (canonical), `2e4b62206bc2f2e4e23569f8026d8004bdcf01fb` (index).
- Exact next task: **continue auditing the remaining vague PQ acquisition records and investigate the unresolved Thunder Flash/PQ146 relationship and the documented Emperor's Cannon PQ183/PQ184 conflict before making further changes.**


## 2026-09-20 — Thunder Flash PQ146 reward-tier refinement
- Refined **Thunder Flash** from generic PQ146 acquisition wording to **PQ146 "Zen-Ohs' Earthly Excursion" Basic Reward**, based on the maintained PQ reward evidence already recorded in the canonical research notes.
- `ultimate_finish_required` remains `false`; no additional prerequisite was inferred.
- Emperor's Cannon remains intentionally unresolved as a PQ183/PQ184 provenance conflict: the dedicated skill evidence supports PQ184 while the maintained reward guide lists it under PQ183 Basic Reward. No unsupported resolution was made.
- Validation: canonical/index **283 records**, exact name/order parity, UF count **60**.
- Commits: `491fa4f268ad7b4b00ffc0ed26e64317b5befaa1` (canonical), `716009bc1c79e1e6ae207cfe99e86644d15870c2` (index).
- Exact next task: **continue the remaining vague PQ acquisition census, prioritizing records with a concrete maintained Basic Reward relationship still not reflected in `unlock_method`, while preserving all documented source conflicts.**


## 2026-09-20 — remaining generic PQ reward-tier refinement
- Refined 21 remaining vague quest acquisition records where maintained PQ research explicitly lists the skill in basic/skill reward data: Emperor's Blast (PQ70), Vanishing Ball (PQ58), Afterimage Strike (PQ81), Kai Kai (PQ63), Wall of Defense (PQ10), Charge (PQ83), Do or Die (PQ49), Fighting Pose E (PQ19), Fighting Pose H (PQ61), Justice Pose (PQ53), Burning Slash (PQ44), Emperor's Edge (PQ99), Evil Flight Strike (PQ21), Evil Whirlwind (PQ36), Meteor Blow (PQ9), Shining Slash (PQ38), Mystic Flash (PQ20), Divine Wrath: Purification (PQ112), Explosive Buu Buu Punch (PQ50), Gigantic Rage (PQ130), and Victory Rush (PQ89).
- Acquisition text now identifies these as Basic Reward routes. Alternate acquisition routes already documented for Emperor's Blast, Emperor's Edge, and Meteor Blow were preserved.
- Emperor's Cannon remains deliberately unchanged because PQ183 maintained reward data conflicts with dedicated PQ184 evidence.
- Validation: canonical/index 283 records, exact name/order parity, UF count 60.
- Commits: 2c47b6dbba28cc00e1ec4565c91def9ac28be09b; c39b2fc99b137c751079706f1b651fa5ef89723e.


## 2026-09-20 — generic PQ census completion checkpoint
- Recomputed the generic quest-or-mission PQ census after the preceding 21-record refinement. Only **X 100 Big Bang Kamehameha** remained vague; maintained PQ100 research explicitly lists it in `basic_rewards`/`skill_rewards`.
- Refined X 100 Big Bang Kamehameha to **PQ100 "The Ultimate Rivalry" Basic Reward**, preserving its TP Medal Shop route.
- The remaining Emperor's Cannon PQ183/PQ184 discrepancy is retained as a documented provenance conflict rather than silently resolved.
- Post-change generic PQ census: **0** vague PQ acquisition records under the audit definition; all remaining PQ acquisition text has an explicit reward tier, UF condition, first/normal-clear qualifier, or documented provenance conflict.
- Validation: canonical/index **283 records**, exact name/order parity, UF count **60**.
- Commits: canonical `b00b0f51d81b2d1c0855a2fa651695345c68e9e8`; index `5e83374750e5823de7bb963ef063e4610ca43144`.


## 2026-09-20 — non-PQ quest/mission provenance normalization
- Normalized **18** non-PQ acquisition records whose maintained source was already deterministic but whose `unlock_method` was overly terse: mentor routes now identify the available lesson/test where established, Advancement Test rewards are labeled by class, and Expert Mission routes include mission titles while preserving unresolved reward-generation conditions.
- Updated: Shadow Crusher; Time Skip/Back Breaker; Time Skip/Flash Skewer; Time Skip/Jump Spike; Rise to Action; Dancing Parapara; Instant Transmission; Energy Charge; Full Power Charge; Maximum Charge; Data Input; Death Ball; Super Spirit Bomb; Supernova; Darkness Rush (Melee); Darkness Rush (Ranged); Galick Gun.
- No Ultimate Finish-only gates were inferred for these non-PQ routes.
- Validation: canonical/index 283 records, exact name/order parity, UF count 60.
- Commits: canonical `7ebfb7ac500d8646abc63ceab8ab494863827c8b`; index `82f2ca25bd81a9694999c8bce27be53f1f3d3795`.


## 2026-09-20 — non-PQ Awoken acquisition provenance refinement
- Audited the remaining null-source/non-specific Awoken acquisition records against the repository's dedicated Awoken research and current unlock references.
- Refined **7 records**: **Super Saiyan**, **Super Saiyan God**, **Super Vegeta**, **Beast**, **Potential Unleashed**, **Super Saiyan 2**, and **Ultra Instinct**.
- Added concrete non-PQ source provenance and more specific unlock wording. In particular: Super Saiyan/SS2/Super Vegeta now point to the Capsule Corporation Vegeta/Saiyan Awakening route; Super Saiyan God records the required five friendships, Shenron wish, and Beerus handoff; Beast records the Gohan/Videl + Piccolo friendship gate and Cell Max unlock mission; Potential Unleashed identifies the final Super Class Advancement Test after Z-ranking Easy through God; Ultra Instinct identifies Jiren (Full Power)'s “In Pursuit of Mastery” challenge.
- No Ultimate Finish flags were changed. No unsupported level, drop rate, or additional prerequisite was inferred.
- Validation: canonical/index remain **283 records**, exact record-order parity preserved, UF count remains **60**. The previously targeted null source_quest set now has concrete provenance for these seven records; remaining non-PQ null-source records should be audited separately rather than treated as resolved by inference.
- Commits: canonical **7689098e1e7778bdadf5e92dec72942f73470ef1**; index **931da3fe02cf407ff12d2678737a787d890b5375**.
- Evidence limitation: external current guides were used only to corroborate routes already represented by the repository's Awoken/Advancement research; contested or version-sensitive details remain qualified in the canonical notes.
- Exact next task: **continue the non-PQ provenance audit with the remaining mentor/test/mission records that still have terse or ambiguous acquisition wording (especially Galick Gun, Dancing Parapara, Rise to Action, Deadly Dance, and any remaining source-null records), then inspect dedicated research files for concrete lesson/test/mission identifiers before editing.**

## 2026-09-20 — mentor lesson-level provenance refinement continuation
- Refined **11** non-PQ mentor acquisition records whose prior source labels were too broad: **Galick Gun**, **Dancing Parapara**, **Rise to Action**, **Deadly Dance**, **Shadow Crusher**, **Time Skip/Flash Skewer**, **Time Skip/Back Breaker**, **Time Skip/Jump Spike**, **Death Ball**, **Darkness Rush (Melee)**, and **Darkness Rush (Ranged)**.
- Current maintained instructor evidence identifies the exact training checkpoint for each: Vegeta's Initiation Test; Pan's Initiation Test; Krillin's Initiation Test; Android 18 Lesson 2; Cooler Lesson 1; Hit Initiation Test/Lessons 1–2; Frieza Lesson 3; and Lord Slug Lesson 3.
- Reward wording now explicitly identifies these as mentor Basic Rewards. For Lord Slug Lesson 3, the evidence records both Darkness Rush variants in the same reward set.
- No Ultimate Finish gate, drop rate, or unsupported prerequisite was inferred.
- External corroboration: maintained instructor reward data and current/accessible mentor guides agree on the initiation/lesson mapping for the refined records. 
- Validation after the change: canonical/index **283 records**, exact name/order parity, UF count **60**; the targeted terse mentor/test census now returns **0** records under the current audit pattern.
- Commits: canonical **77617ca0ad0ed0edaf0aec8251fcb371c7fffcf6**; index **21cc5cc53ea465cdda3330ff751656565f175d2d**.
- Next: audit the remaining non-PQ quest/mission records for **source-quality and specificity rather than simple terseness**, especially time-rift, story, shop, and Expert Mission routes; preserve unresolved conditions and source conflicts.


## 2026-09-20 — non-PQ source-quality refinement continuation
- Refined **5** remaining quest/mission acquisition records where source evidence supported a more concrete provenance or reward tier: **Future Super Saiyan**, **Data Input**, **Super Spirit Bomb**, **Supernova**, and **Fighting Pose K**.
- Corrected **Future Super Saiyan** from the prior Capsule Corporation/Vegeta route to the **Unknown History secret story mission** route. Current external walkthrough evidence explicitly ties the transformation to completion of Unknown History after the five Distorted Time Eggs; the prior repository wording conflicted with this evidence and was replaced rather than silently retained. 
- Refined **Data Input → Expert Mission 20 "Harbinger of Doom" Basic Reward**, **Super Spirit Bomb → Expert Mission 16 "In the Realm of the Gods: Vegeta" Basic Reward**, and **Supernova → Expert Mission 6 "The Depths of Despair" Basic Reward**. Maintained/independent Expert Mission reward evidence explicitly lists each skill in the corresponding Basic Reward pool. 
- Refined **Fighting Pose K** to the story/Skill Shop relationship: completing **"The Ginyu Force Strikes"** unlocks the Skill Shop route, where Fighting Pose K is purchased. No Ultimate Finish-only condition was inferred. 
- Validation target remains canonical/index **283 records**, exact record-order parity, and UF count **60**; no reward gate was changed by this cycle.
- Commits: canonical **8466316b9b41199c8524e3821a2d03d6863e54b1**; index **d6fc033d206cc2dc5ffcc4f6f729b3a46723c50d**.
- Exact next task: **continue auditing the remaining non-PQ acquisition records for source-quality conflicts and missing concrete conditions, prioritizing time-rift/story routes and any records whose dedicated research disagrees with canonical provenance. Preserve documented conflicts rather than inferring a winner when evidence remains mixed.**


## 2026-09-20 — non-PQ source-quality cleanup: Explosive Wave
- Re-audited the remaining non-PQ skill acquisition records for stale references to Parallel Quest reward evidence.
- Found one direct contradiction: **Explosive Wave** was canonically acquired from the Skill Shop after normal-ending story progression, but its notes incorrectly claimed that maintained PQ evidence placed it in a Basic Reward. A repository-wide PQ reward census found no Parallel Quest record for Explosive Wave; the stale note was removed.
- No acquisition route, Ultimate Finish flag, drop rate, or restriction was changed beyond correcting the provenance note.
- Validation: canonical/index **283 records**, exact record-order parity, **0 duplicates**, 60 records with `ultimate_finish_required=true`; both JSON files parse successfully.
- Internal/AI citation-artifact scan was also performed on the handoff/audit files; tool citation markup is being removed from repository documentation rather than retained.
- Commits: canonical **94382a7e91dbe4122101d895d58630aa8d683d67**; index **0e1fc6198874facb13b494e016d323f64ef7d95**.
- Exact next task: **continue the non-PQ source-quality audit, prioritizing time-rift/story/shop records whose provenance notes may contradict their canonical acquisition fields; preserve genuine source conflicts and do not infer missing conditions.**


## 2026-09-20 — wish and TP Medal Shop provenance refinement
- Continued the non-PQ source-quality audit after the Explosive Wave cleanup.
- Refined six acquisition records where maintained dedicated evidence could make the non-quest route more explicit without inferring unsupported conditions:
  - **Flash Fist Crush** → first use/result of Shenron's “I want a new Super Attack!” wish.
  - **Burst Reflection** → second use/result of the same wish.
  - **Namek Finger** → TP Medal Shop; documented historical listing price 30 TP Medals.
  - **Emperor's Death Beam** → TP Medal Shop; documented historical listing price 25 TP Medals.
  - **Final Explosion** → TP Medal Shop; documented historical listing price 200 TP Medals.
  - **Divine Lasso** → TP Medal Shop, with STP Medal Shop and Double Crystal Raid routes retained.
- No PQ relationship, Ultimate Finish flag, race restriction, or unsupported prerequisite was introduced.
- Repository validation: **283/283** records; zero duplicate names; **60** Ultimate Finish flags. Canonical/index acquisition-critical fields (name, acquisition_type, unlock_method, ultimate_finish_required, source_quest, race_restriction) remain exactly synchronized.
- Evidence used includes the maintained repository source set plus current public skill/wish references. Historical shop prices are explicitly labeled as documented listings rather than asserted as current rotation prices.
- Next target: **continue auditing remaining non-PQ records with terse shop/wish/character-only provenance, especially records whose unlock text is generic while dedicated sources can establish a concrete route. Preserve genuine uncertainty.**


## 2026-09-20 — remaining shop provenance normalization
- Continued the non-PQ shop acquisition audit.
- Normalized **8** terse shop records: **Reverse Mabakusenko, Super Afterimage, Super God Shock Flash, Final Pose, Spirit Boost, Pressure Sign, Dragon Fist, and Godly Display**.
- Shop routes are now explicitly scoped to Conton City where applicable; Dragon Fist and Godly Display retain documented historical TP Medal prices of 200 and 500 TP Medals respectively.
- No quest route, Ultimate Finish gate, race restriction, or unsupported current shop-rotation claim was introduced.
- Validation: canonical/index **283/283**, name ordering identical, **0 duplicate names**, **60** Ultimate Finish flags. Acquisition-critical fields remain synchronized.
- Commits: canonical **8cc6d9fb8741a4746877e916faf19a5b8acf1fe7**; index **9d31f6708325c2e8ac6277611dcc764965407682**.
- Exact next target: **continue the remaining character-only/starting-move non-PQ records, separating genuinely non-acquirable roster skills from CaC-accessible skills whose acquisition route is merely under-specified.**


## 2026-09-20 — character-only / built-in skill status refinement
- Refined **9** non-PQ records whose status was character-only or built-in rather than a conventional acquisition route: Pure Progress, Super Saiyan Blue Kaioken, Supersonic Mode, Final Flash (Super), Energy Release, Final Charge, Instant Charge, Rising Rage, and Surging Spirit.
- The records now explicitly distinguish roster-exclusive transformations/skills and built-in Ultra Instinct functionality from normal CaC-acquirable skills.
- No CaC acquisition route was invented where maintained evidence did not establish one.
- Validation: canonical/index remain **283/283**, **0 duplicate names**, **60** Ultimate Finish flags; record-name ordering remains identical.
- Commits: canonical **ed02f4441b8eb3080b9f8bedcd97dd0ad0c5b650**; index **b38e008f2dc54f8339e47dc1ef3bb5c181272e02**.
- Exact next target: **audit the remaining non-PQ starting-move and other_nonquest records, especially Afterimage, Super Guard, and any skill whose CaC availability is implied by the current unlock text but lacks a concrete acquisition explanation.**


## 2026-09-20 — starting-move provenance refinement
- Refined **Afterimage** and **Super Guard**.
- Afterimage is explicitly documented as a CaC starting Super from the initial fighting-style selection, with no PQ/Ultimate Finish route asserted.
- Super Guard is explicitly documented as a CaC starting Super associated with the initial close-range fighting-style choice; the maintained record also preserves its Skill Shop route.
- No new quest source or unsupported unlock condition was introduced.
- Exact next target: continue auditing remaining non-PQ other_nonquest or starting-move records for concrete CaC acquisition wording.


## 2026-09-20 — non-PQ acquisition-route pass completed
- Rechecked the remaining `other_nonquest`, `starting_move`, and `character_only` records against the current canonical dataset.
- The targeted non-PQ starting-move records (**Afterimage**, **Super Guard**) now have concrete CaC starting-choice wording; character-only/built-in records have explicit roster-status notes from the prior pass.
- No additional record met the evidence threshold for a safe route correction in this pass, so no unsupported acquisition details were added.
- Validation: canonical/index **283/283**; identical record-name ordering; **0 duplicate names**; **60** Ultimate Finish flags; **0** mismatches across acquisition-critical fields (`name`, `acquisition_type`, `unlock_method`, `ultimate_finish_required`, `source_quest`, `race_restriction`).
- Exact next target: **move the audit to the remaining generic Skill Shop / TP Medal Shop records whose route is known but whose prerequisite/timing wording may still be under-specified, while preserving historical-price uncertainty.**


## 2026-09-20 — Skill Shop prerequisite refinement
- Refined **Punisher Guard** from a generic Skill Shop route to the documented prerequisite: complete **A Momentous Galactic Battle**, then purchase it from the Skill Shop for **5,000 Zeni**.
- The price is recorded as documented purchase information; no current shop rotation is inferred.
- Other remaining generic Skill Shop / TP Medal Shop records were reviewed but did not meet the evidence threshold for a further prerequisite correction in this pass.
- Exact next target: continue checking generic TP Medal Shop and Skill Shop records for concrete prerequisites, while preserving uncertainty around historical rotations/prices.


## 2026-09-20 — generic shop audit continuation
- Rechecked the remaining generic Skill Shop and TP Medal Shop records against maintained repository evidence and current external references.
- Confirmed that most remaining generic shop records do not have a sufficiently supported additional prerequisite/timing condition to encode without risking false precision. This includes the current TP Medal Shop records where historical rotation evidence exists but does not establish present-day availability.
- Punisher Guard remains the concrete prerequisite refinement from the preceding cycle: Skill Shop after completing **A Momentous Galactic Battle**, 5,000 Zeni. Current references independently support that route. 
- No additional dataset changes were necessary in this pass.
- Validation: canonical/index **283/283**, identical record-name ordering, **0 duplicate names**, **60** Ultimate Finish flags, and **0** acquisition-critical mismatches.
- Exact next target: **continue source-quality auditing of the remaining generic shop records, prioritizing records with multiple acquisition routes or historical shop references that may conceal a more precise current route.**


## 2026-09-20 — multi-route shop source audit
- Audited the remaining multi-route / shop-sensitive records, prioritizing **Sudden Death Beam** and **Divine Lasso**.
- **Sudden Death Beam** is consistently documented as TP Medal Shop acquisition; current repository evidence also records STP Medal Shop and Double Crystal Raid Battle. Bandai Namco's historical 2017 schedule explicitly placed it in the TP Medal Shop rotation. This supports the existing multi-route wording, but does **not** justify a current rotation/timing claim. 
- **Divine Lasso** likewise has documented TP Medal Shop acquisition, with current repository evidence retaining STP Medal Shop and Double Crystal Raid Battle as additional routes. Bandai Namco's historical schedule explicitly listed Divine Lasso in the TP Medal Shop rotation. No additional prerequisite is established. 
- **Quick Sleep** was rechecked: dedicated skill evidence confirms Skill Shop acquisition and that it is restricted to Majin CaCs. This restriction is already represented by the repository's race field, so no dataset edit was necessary. 
- **Bending Kamehameha**, **Big Bang Kamehameha**, and **Divine Kamehameha** were also rechecked. The available evidence confirms their respective Skill Shop / TP Medal Shop routes but does not provide a sufficiently authoritative concrete prerequisite that should replace the current conservative wording. 
- No dataset changes were necessary in this cycle.
- Validation remains: canonical/index **283/283**, identical record-name ordering, **0 duplicate names**, **60** Ultimate Finish flags, **0** acquisition-critical mismatches.
- Exact next target: **continue source-quality auditing generic shop records, then move to any remaining under-specified non-PQ records only when a concrete, independently supported acquisition condition is available.**


## 2026-09-20 — shop-route evidence recheck
- Rechecked the remaining conservative shop records against dedicated skill pages and maintained Future Warrior acquisition references.
- **Bending Kamehameha** remains correctly scoped to Skill Shop; dedicated skill evidence gives no additional prerequisite to encode.
- **Big Bang Kamehameha** remains correctly scoped to TP Medal Shop; dedicated skill evidence confirms that route without establishing a narrower prerequisite.
- **Divine Kamehameha** remains correctly scoped to TP Medal Shop; current skill documentation also identifies it as a Future Warrior-usable skill, while no concrete story prerequisite is established.
- The older TP Medal Shop price/rotation material for Namek Finger, Emperor's Death Beam, Final Explosion, and Dragon Fist remains historical evidence only; no current rotation claim was added. Historical listings document Namek Finger at 30 TP, Emperor's Death Beam at 25 TP, Final Explosion at 200 TP, and Dragon Fist at 200 TP. These figures are retained only where already explicitly marked historical/documented.
- No dataset changes were necessary in this pass.
- Validation remains: canonical/index **283/283**, identical record-name ordering, **0 duplicate names**, **60** Ultimate Finish flags, **0** acquisition-critical mismatches.
- Sources reviewed: dedicated Xenoverse 2 skill pages for Bending Kamehameha, Big Bang Kamehameha, Divine Kamehameha; Dragon Ball Wiki Future Warrior technique list; historical TP Medal Shop listing evidence.
- Exact next target: **continue the remaining under-specified acquisition records, prioritizing any record whose existing route conflicts with a dedicated skill page or whose source list mixes character-only and CaC acquisition evidence.**


## 2026-09-20 — built-in / character-only acquisition-status refinement
- Refined **Surging Spirit** to explicitly describe its current CaC behavior: it is a **built-in Ultra Instinct action**, not a separately acquired/equipped skill. Current Ultra Instinct documentation states that the Future Warrior can use Surging Spirit while Ultra Instinct is active. 
- Refined **Dragon Thunder** to use the explicit **Character-only** race restriction. Dedicated Xenoverse 2 skill evidence identifies it as Omega Shenron's Strike Super and states it is unavailable to CaCs. 
- Updated both canonical and synchronized index records; no quest or Ultimate Finish provenance was introduced.
- Validation: canonical/index **283/283**, identical record-name ordering, **0 duplicate names**, **60** Ultimate Finish flags, **0** acquisition-critical mismatches.
- Exact next target: **continue auditing under-specified non-PQ records for explicit built-in, character-only, starting-move, wish, or other deterministic acquisition-status evidence before touching generic quest records again.**


## 2026-09-20 — Final Pose acquisition provenance correction
- Re-audited generic shop records against dedicated skill evidence and found a direct contradiction for **Final Pose**.
- Canonical data previously classified Final Pose as a **Skill Shop** acquisition. Dedicated Xenoverse 2 skill evidence lists **Final Pose → PQ74** in the Evasive Skill table, and independent player documentation identifies PQ74, **"Galactic Patrol Away,"** as the source.
- Corrected both canonical and index skill records to `acquisition_type: parallel_quest`, `source_quest: PQ74 — "Galactic Patrol Away"`, and matching unlock wording. The stale Skill Shop provenance was removed rather than preserved.
- No Ultimate Finish requirement, drop rate, or current shop claim was inferred.
- Validation target after the correction: canonical/index remain 283 records with identical ordering; acquisition-critical fields remain synchronized.
- Exact next task: **continue checking generic shop records for direct contradictions against dedicated unlock tables, prioritizing cases where a shop label may actually be a PQ/mentor/story source.**


## 2026-09-20 — final-PQ skill provenance refinement
- Reconciled **Dark Inscription** against the live PQ182 research record.
- PQ182 — **“Frieza's Fervent Wish”** explicitly lists Dark Inscription in its Basic Reward / skill-reward set, while the PQ record has no explicit skill drop-condition entry. The skill record therefore now uses the concrete PQ182 Basic Reward provenance without asserting an Ultimate Finish gate or drop probability.
- Updated `docs/data/skills.json` and `docs/data/skills-index.json` together.
- Validation target: canonical/index remain **283 records**, record-name ordering remains identical, duplicate-name count remains **0**, and the **60** `ultimate_finish_required=true` flags remain unchanged.
- Evidence limitation: the maintained PQ corpus establishes the quest and reward classification but does not establish an exact individual RNG probability.


## 2026-09-20 — PQ161–180 provenance-label normalization
- Continued the late-PQ deterministic provenance census using the maintained PQ161–170 and PQ171–180 reward batches.
- Normalized remaining generic `source_quest_or_shop` labels to explicit maintained quest names for **Giant Cluster (PQ163)**, **Gigantic Explosion (PQ164)**, **Special Beam Cannon (Beast) (PQ162)**, **Divine Ray Bomb (PQ173)**, **God of Destruction's Poise (PQ175)**, and **Soaring Rush (PQ177)**.
- Acquisition semantics were not changed; no new Ultimate Finish gates or probabilities were inferred.
- Canonical commit: `6ffd74c3b7c82883eb537424d29611e9d936a7a5`; index commit: `5f9d1a13d5d972533b3d3977c144c13b2cd473ed`.


## 2026-09-20 — PQ154–160 and PQ184 provenance normalization
- Continued the acquisition/provenance census outside the already-reconciled PQ161–180 block.
- Normalized generic source fields to explicit maintained quest names for **Demon Ray, Demon Flash Strike, Demon Flurry (PQ160)**; **Sign of Awakening, Circle Flash (PQ154)**; **Heroic Counter, Gamma Blaster, Gamma Impact (PQ155)**; **Super Gamma Blast, Core Breaker (PQ158)**; **Fierce Fist, Demonic Destruction (PQ159)**; and **Chaotic Time Impact (PQ184)**.
- Existing reward tiers/Ultimate Finish semantics were preserved; this pass changed provenance specificity only.
- Canonical: `8dd9f7a39cfa3d87cd6d8067cbb3642d4f8fdb60`; index: `4832e8933855ceb7846c2ff9a9dc9024b713ace4`.


## 2026-09-20 — Explicit PQ provenance-label normalization (second pass)
- Audited generic `source_quest_or_shop` labels outside the already-reconciled late-PQ block.
- Where `unlock_method` itself explicitly contained the quest title, normalized **73** generic provenance labels (for example `Parallel Quest 80` → `Parallel Quest 80 — "The Return of the Giant Ape-Fest"`).
- This was a provenance-only normalization: no acquisition type, reward tier, Ultimate Finish flag, probability, or route semantics were changed.
- Canonical: `03d9813feda3269d318378389333c80a1b60a6a9`; index: `52c1fcc481c452d0f3abf080a1dbdda4613ae2f5`.


## 2026-09-20 — Remaining titled PQ provenance cleanup
- Normalized 11 remaining shorthand provenance labels (PQ###) where the existing unlock method explicitly supplied the quest title: Spirit Pulse, Wild Buster, Phantom Fist, Shield Barrier, Burning Swan, Heroic Assault, Justice Blade, Justice Kick, Seagull Combination, Shooting Strike, and Apocalyptic Burst.
- No acquisition semantics, reward tiers, Ultimate Finish flags, or probabilities changed.
- Canonical: 0a99b958785299078c70eb64dbd3c530842c803d; index: 955277b6b470e92b3898bfd6e15a7dfb609cf8fc.


## 2026-09-20 — Maintained PQ title mapping normalization
- Normalized **43** remaining generic `Parallel Quest N` provenance labels using explicit quest-number/title mappings from the maintained PQ research batches.
- No acquisition semantics, reward tiers, Ultimate Finish flags, or probabilities were changed.
- Canonical: `fb6115fbae8286c9a6141923336556708169a703`; index: `37e6c4f377dbb0b13ec4ba64e4ea68e057b32a01`.


## 2026-09-20 — Deterministic pooled-route cleanup
- Normalized `Kaioken` and `Meditation` to their explicit Parallel Quest sources already stated by their unlock methods.
- Corrected `Fighting Pose K` from `quest_or_mission` to `skill_shop`: its recorded route explicitly says the story unlocks the listing and the skill is purchased from the Skill Shop.
- No unsupported probabilities, UF gates, or reward semantics were introduced.
- Canonical: `3dc2c0200bc23ee1bbf2d159722653f15d9afdad`; index: `c7461142afa2ddc9d7918e3e4f7db3e31713c158`.


## 2026-09-20 — Final Pose source completion
- Filled the missing `source_quest_or_shop` for `Final Pose` from its explicit unlock method: Parallel Quest 74 — `Galactic Patrol Away`.
- Preserved `parallel_quest` acquisition type and all reward/UF semantics.
- Canonical: `1f5fac03fe0fb4787b62c296bc5374c1463e9ea9`; index: `4bdf986f5aa3aa7e6b7bcad909b30c2d9fdcf472`.


## 2026-09-20 — acquisition schema synchronization
- The canonical skill data uses a dedicated `parallel_quest` acquisition type for `Final Pose`, but `docs/data/skills.schema.json` did not include that enum value.
- Added `parallel_quest` to the schema enum so the schema matches the documented acquisition taxonomy.
- No skill record values were changed in this pass.
- Schema commit: `1f80924b5532a58c4f4cf18cfe9c2cf0006e3347`.


### 2026-09-20 cycle update — taxonomy and synchronization audit
- Re-checked the acquisition taxonomy after adding `parallel_quest` to the schema.
- Canonical `skills.json` and `skills-index.json` both contain exactly 283 records, identical ordering, 0 duplicate names, and 0 mismatches across acquisition-critical fields (`name`, `acquisition_type`, `unlock_method`, `ultimate_finish_required`, `source_quest`, `race_restriction`, `source_quest_or_shop`).
- All seven acquisition types currently present in data are represented by the schema enum; no unsupported or unused enum values remain.
- Reviewed non-PQ records for obvious route/type contradictions (shop, TP Medal Shop, Shenron, character-only, starting-move, mentor/time-rift routes); no deterministic correction was supported by the current taxonomy/evidence, so no speculative reclassification was made.
- Exact next task: continue source-evidence auditing for the remaining pooled/multi-source records and inspect repository documentation/validators for any other stale taxonomy assumptions.


## 2026-09-20 — validator acquisition taxonomy synchronization
- Found a second taxonomy mismatch after adding `parallel_quest` to the JSON Schema: `scripts/validate_skills.py` maintained its own `ALLOWED_ACQUISITION` set and still rejected `parallel_quest`.
- Added `parallel_quest` to the validator allowlist. This is required for the existing canonical `Final Pose` record to pass CI.
- No canonical skill records or acquisition semantics changed.
- Validator commit: `214ff9dc34b66dc044383bac75b36675ab6d92ca`.
- Exact next task: inspect other duplicated acquisition/schema assumptions and run/verify the repository's validation path where supported.


## 2026-09-20 — skill builder taxonomy synchronization
- Found a third duplicated acquisition taxonomy: `scripts/build_skills_from_research.py` classified every record without numeric `source_quest` as `quest_or_mission`, shop, starting-move, character-only, or `other_nonquest`; it could not emit the dedicated `parallel_quest` type now used by `Final Pose`.
- Updated the builder to recognize an explicit `Parallel Quest <number>` route as `parallel_quest` when it is not simultaneously a shop/TP-medal route.
- No canonical data was regenerated in this pass; the change prevents future rebuilds from silently collapsing the dedicated PQ classification.
- Builder commit: `2e151ce3003d7c1fbea0ee21db6fa8e6482fe6a8`.
- Exact next task: continue auditing every skill-data producer/validator for duplicated acquisition rules and verify the complete validation path.


## 2026-09-21 — skill-builder PQ classification precedence fix
- Re-audited the acquisition taxonomy after the validator provenance fix.
- Found a remaining producer bug in `scripts/build_skills_from_research.py`: the `source_quest` branch could return `quest_or_mission` before the later PQ-number test, making the dedicated `parallel_quest` classification unreachable for records with a non-empty `source_quest` value containing a PQ reference.
- This was inconsistent with the documented taxonomy and with the validator/schema support for `parallel_quest`.
- Fixed the classification order so an explicit numbered Parallel Quest reference is recognized before the generic `source_quest` fallback, while preserving the existing TP Medal/skill-shop precedence and mixed-route safeguards.
- No canonical skill records were regenerated or changed by this code-only correction.
- Builder commit: `0c81d620572f8092b27223a44d785343a62d00ba`.
- Live canonical race census at inspection: **283 total / 270 CaC-usable / 3 CaC-usable with null `race_restriction`** — `Blaster Stream`, `Chaotic Time Impact`, and `Circle Flash`. This supersedes stale historical counts of 182 in earlier handoff entries.
- Current Future Warrior evidence lists all three as usable techniques but does not provide an explicit all-race or race-specific statement for these exact records; no race classifications were inferred.
- Exact next task: verify the builder/validator acquisition path together, then continue the final three-record null-race evidence sweep with exact-name current-version sources.


## 2026-09-21 — final three null-race evidence sweep
- Performed an exact-name evidence sweep for **Blaster Stream**, **Chaotic Time Impact**, and **Circle Flash**.
- Current evidence independently establishes that all three are usable by CaC/Future Warrior: a current indexed Xenoverse 2 character/skill ID corpus marks each corresponding skill as a CaC skill, while current player documentation also shows Blaster Stream and Circle Flash equipped on CaCs and current DLC-era material demonstrates Chaotic Time Impact in a CaC-focused skill showcase.
- This evidence establishes CaC usability, but **does not establish a race restriction or an all-race guarantee** for any of the three. The current exact-name searches did not produce reliable current-version wording such as “all races” or a race-specific restriction. Character association (Kale/Kefla, Golden Frieza, Dyspo) is not sufficient evidence of CaC race scope.
- Therefore all three canonical `race_restriction` values remain **null**. No speculative race classification was made.
- No canonical/index data changes were justified by this sweep.
- Evidence limitation: community/player sources are useful corroboration of CaC use but are not treated as authoritative race-scope proof; the repository continues to preserve null where exact restriction evidence is absent.
- Exact next task: audit the remaining `usable_by_cac=true` records for weaker-than-explicit race-scope evidence and determine whether any other null/ambiguous restrictions remain hidden outside the current three-record census.


## 2026-09-21 — complete CaC race-field census correction
- Recomputed the live `skills.json` census directly rather than relying on the earlier handoff snapshot.
- Current canonical totals are **283 records / 274 `usable_by_cac=true` / 3 CaC-usable records with `race_restriction: null`**.
- The three null records remain **Blaster Stream**, **Chaotic Time Impact**, and **Circle Flash**. The previous 270 CaC-usable figure in earlier handoff notes was stale and is superseded by this direct live-file census.
- The CaC-usable race field has no placeholder/weak sentinel values such as `Unknown` or `Unspecified`; all non-null values are explicit race/form scopes, including `All CaC races` and specific race combinations.
- No canonical data change was required: the census correction is documentation-only.
- Exact next task: trace the four-record difference from the stale 270 figure through recent repository history, then audit the affected records' race evidence before making any further scope changes.


## 2026-09-21 — stale 270-CaC discrepancy traced
- Traced the previously reported **270 CaC-usable** figure against repository history instead of treating it as a live-data change.
- Direct reads of the canonical `docs/data/skills.json` at commits `281677f38172cca7ca3b9fdb84b19cb8b856b656` and `8de19fa9c1585600e53bd73269b1fb8b16df6848` both already contain **283 total / 274 CaC-usable / 3 null-race CaC records**. The current catalog has the same census.
- Therefore the difference from 270 to 274 was a **stale handoff/documentation count**, not four newly discovered or silently changed skill records. No four-record data cohort exists to audit from that discrepancy.
- The historical race-audit commits confirm that recent race work was focused on explicit restrictions and character-only normalization; none of the inspected canonical snapshots support a 270-record live state.
- No canonical data change was required.
- Exact next task: continue evidence auditing from the actual live unresolved set (Blaster Stream, Chaotic Time Impact, Circle Flash), or identify another concrete data-quality invariant rather than pursuing the nonexistent four-record discrepancy.


## 2026-09-21 — final three null-race evidence sweep (continued)
- Rechecked **Blaster Stream**, **Chaotic Time Impact**, and **Circle Flash** against current/recent external evidence after tracing the stale 270 census.
- Current evidence corroborates these as CaC-usable skills: community CaC build records explicitly use Blaster Stream and Circle Flash, while current DLC coverage identifies Chaotic Time Impact as a Golden Frieza (Ultra Supervillain) skill and separate current gameplay material documents it being added to CaC move sets.
- None of the reviewed evidence establishes an explicit race, gender, or form restriction for these three. Character association was not treated as race scope.
- **No canonical race correction is justified.** The three remain `usable_by_cac: true` with `race_restriction: null` pending explicit race-scope evidence.
- This leaves the live unresolved race-scope set at exactly **3 records**.
- Exact next task: continue from these three only if new explicit race-scope evidence appears; otherwise move to another concrete data-quality invariant.


## 2026-09-21 — acquisition producer/canonical PQ classification alignment
- Found a concrete producer drift during the cross-field audit: **211 current canonical records** have explicit PQ-number wording in `source_quest_or_shop`/`unlock_method` but retain `acquisition_type: quest_or_mission` because their canonical `source_quest` is a numeric PQ ID.
- The builder's numbered-PQ rule previously promoted those records to `parallel_quest` during a fresh build, while the canonical catalog deliberately uses `parallel_quest` only for records whose `source_quest` itself carries textual PQ provenance (currently Final Pose / PQ74).
- Corrected `scripts/build_skills_from_research.py` so numbered PQ text yields `parallel_quest` only when `source_quest` is absent; numeric `source_quest` records continue through `quest_or_mission` classification. TP Medal/Skill Shop precedence remains unchanged.
- This preserves the existing 248/1/11/9/8/2/4 acquisition census semantics and prevents a fresh producer run from reclassifying the 211-record numeric-PQ cohort.
- No canonical data was changed.
- Commit: `26492c947f35359f6f41cfc17ebd062ba6a6635c`.
- Exact next task: re-audit producer/validator classification against the canonical 283 records and inspect for any remaining fresh-build drift in acquisition type.


## 2026-09-21 — post-fix acquisition drift recheck
- Re-audited the live 283-record catalog after the PQ producer fix. Acquisition totals remain 248 quest_or_mission, 1 parallel_quest, 11 skill_shop, 9 tp_medal_shop, 8 character_only, 2 starting_move, and 4 other_nonquest.
- Final Pose remains the only parallel_quest record. No other canonical record has PQ-number provenance without a source_quest value, so the producer guard does not create a new cohort.
- No TP Medal Shop record carries quest provenance, and no starting-choice/Skill Shop conflict remains in the live canonical fields.
- No canonical data changed. Next audit target: character_only/CaC eligibility and ultimate_finish_required consistency.


## 2026-09-21 — character-only and Ultimate Finish invariant audit
- All 8 character-only canonical records are consistently CaC-ineligible with explicit Character-only race scope.
- 60 canonical records require an Ultimate Finish; all 60 have explicit numbered PQ provenance. No non-PQ record is UF-required, and no false UF flag was found with explicit UF wording in its unlock method.
- No canonical data changed. Next audit target: compare quest-derived UF flags against maintained detailed reward/provenance evidence.


## 2026-09-21 — Ultimate Finish provenance normalization
- Audited all 60 `ultimate_finish_required=true` records.
- Normalized explicit UF wording for Earth Splitting Galick Gun (PQ11), Raid Blast (PQ136), and Blazing Attack (PQ136), where maintained reward evidence supported the UF flag but the unlock method still said Basic Reward.
- Added validator coverage so future true-UF records must expose explicit UF provenance in unlock_method or source_quest_or_shop.
- Canonical/index remain synchronized at 283 records; no acquisition route or scope changed.

## 2026-09-21 accessory PQ identity reconciliation

- Reconciled eight previously unmatched PQ accessory research identities into the canonical accessory identity layer: **Four-Star Dragon Ball Hat (PQ5), Chiaotzu's Hat (With Collar) (PQ9), Dore's Scouter (PQ27), Great Saiyaman Bandana 1 (PQ51), Great Saiyaman Bandana 2 (PQ53), Jaco's State-of-the-Art Radio (PQ72), Tagoma's Scouter (PQ73), and SSGSS Goku Wig (PQ76)**.
- Updated `docs/data/accessory-canonical-reconciliation.json`, `docs/data/accessory-pq-canonical-bridge.json`, and `docs/data/pq-accessory-crosslink-report.json` together so these routes can now be traversed by deterministic canonical accessory ID.
- Evidence used: maintained 186-PQ reward guide; current equipment/accessory guide; Dragon Ball reference material for Jaco's Galactic Receiver and scouter identity; archived acquisition reports for Tagoma's Scouter and SSGSS Goku Wig.
- Preserved uncertainty: these records remain `partially_verified`; no drop probability, Ultimate Finish gate, or shop/rotation behavior was inferred beyond the cited route evidence.
- Live accessory cross-link coverage moved from **25 matched / 20 unmatched research records / 88 canonical identities** to **33 matched / 12 unmatched research records / 96 canonical identities**.

### 2026-09-21 accessory PQ identity batch 2
- Reconciled four previously unmatched accessory research identities: **Yamcha's Baseball Hat (PQ97), SSGSS Vegeta Wig (PQ100), Bulma (Kid) Wig (PQ149), Great Saiyaman Helmet (PQ51)**.
- Added canonical IDs `accr-097` through `accr-100`; synchronized the accessory PQ bridge and bidirectional report.
- Evidence: maintained 186-PQ Steam guide; current equipment/accessory guide; DLC reference; independent PQ guide and GameFAQs acquisition reports. No unsupported drop rates or additional gates were inferred.
- Remaining unresolved research identities: 8, excluding the separately conflicted Yamcha's Sword route.

### 2026-09-21 accessory PQ identity batch 3
- Reconciled three previously unresolved component identities into canonical accessories: **Gine (DB Super) Set (PQ144), Caulifla Wig (PQ147), Kale Wig (PQ148)**.
- Evidence: PQ reward listings plus independent Dragon Ball/Xenoverse references. The evidence explicitly identifies these as accessories/rewards and establishes their PQ routes.
- Added canonical IDs `accr-101` through `accr-103`; synchronized the accessory PQ bridge and cross-link report.
- Deliberately did not force Android 14's Hat, Android 15's Sunglasses, Bardock (DB Super)'s Scouter, or Android 17 (DB Super)'s Ranger Accessory because current evidence found does not establish a distinct canonical inventory identity for those exact research labels.

### 2026-09-21 accessory PQ identity batch 4
- Resolved **Yamcha's Sword** as a canonical accessory identity (`accr-104`) and linked the PQ route to **PQ36**.
- Evidence: the maintained PQ reward guide directly lists Yamcha's Sword under PQ36, while an independent equipment reference lists the same exact inventory item as an Accessory Shop item. This reconciles the prior PQ29/PQ36 research conflict rather than creating a duplicate identity. cite refs are kept outside repository files.
- Corrected the accessory bridge's stale summary counts and regenerated the forward/reverse cross-link report.
- Remaining unresolved accessory research identities: Android 14's Hat, Android 15's Sunglasses, Bardock (DB Super)'s Scouter, and Android 17 (DB Super)'s Ranger Accessory. Current evidence continues to indicate these labels should not be force-mapped to clothing or similarly named components.

### 2026-09-21 accessory PQ identity batch 5
- Reconciled **Android 15's Sunglasses** to canonical **Android 15's Shades & Hat** (`accr-105`). Current equipment references document this as one accessory sold in the TP Medal Shop; the research label is preserved as a component alias rather than a duplicate item.
- Reconciled **Android 17 (DB Super)'s Ranger Accessory** to the already-canonical **Android 17 (DB Super) Wig** (`accr-029`) as a component/research alias. PQ152 reward evidence explicitly names the canonical wig.
- Did not force-map **Android 14's Hat** or **Bardock (DB Super)'s Scouter**: PQ104 documents Android 14's Clothes, while PQ146 documents Bardock (DB Super)'s Clothes, not those accessory identities.
- Cross-link report regenerated with component aliases represented without creating duplicate inventory identities.

### 2026-09-21 accessory PQ identity batch 6 — final two researched
- Exhaustively rechecked the two remaining unresolved accessory labels against current equipment/reward references.
- **Android 14's Hat (PQ104): unresolved.** PQ104 directly documents **Android 14's Clothes**, not a separately named hat/accessory. The equipment catalog likewise lists Android 14's Clothes as the PQ104 item. No exact canonical accessory identity was established, so no false merge was made.
- **Bardock (DB Super)'s Scouter (PQ146): unresolved.** PQ146 directly documents **Bardock (DB Super)'s Clothes**; the maintained reward guide does not list a scouter. No exact canonical accessory identity was established.
- The bridge now records both as `researched_unresolved` with explicit evidence notes. The cross-link report was regenerated without inventing identities.


### 2026-09-21 skill resource-cost gap batch — Brutal Buster / Dimension Cannon / Neo Wolf Fang Fist

- Live skill census before editing: **305 canonical skill records**.
- Bounded batch: **Brutal Buster, Dimension Cannon, Neo Wolf Fang Fist** — the three records identified by the live cost audit as lacking an explicit resource value.
- Research/evidence: dedicated Xenoverse 2 skill references document **Brutal Buster = 300 Stamina**, **Dimension Cannon = 300 Stamina**, and **Neo Wolf Fang Fist = 100–700 Ki** depending on continued input. Independent community testing also documents continued Ki consumption for Neo Wolf Fang Fist.
- Changes: docs/data/skills.json now records stamina_cost 300 for Brutal Buster and Dimension Cannon, and ki_cost 100-700 for Neo Wolf Fang Fist; each record received direct source provenance and a 2026-09-21 verification note.
- Evidence limits: Evasives do not receive a fabricated Ki cost; their activation resource is Stamina. Neo Wolf Fang Fist retains a variable range rather than being normalized to a fixed cost. No unrelated acquisition or restriction fields were changed.
- Validation: canonical skill JSON re-fetched and parsed successfully; record count remains **305**. No missing ki_cost remains among non-Evasive records; the remaining null stamina_cost values are outside this bounded resource-cost scope and are not automatically treated as gaps.
- CI: no workflow runs or combined status checks were exposed for commit 5884f75e6f409fcf5c2b94a747c8ac45f4766eb0; no CI success is claimed. Validators were not weakened.
- Next: continue the live skill second-pass audit with the next smallest high-impact acquisition/restriction/mechanics gap batch, while preserving the cross-database linking model and avoiding broad speculative rewrites.


### 2026-09-21 cycle update — skill PQ cross-link identifier normalization
- Live census before editing: **305 canonical skill records**.
- Bounded batch: **Drain Field (PQ95), Flash Bomber (PQ95), Rakshasa's Claw (PQ57), Final Pose (PQ74)**.
- Repository evidence: all four records already had explicit Parallel Quest acquisition text in `unlock_method`/`source_quest_or_shop`, but three `quest_or_mission` records lacked the canonical numeric `source_quest` join key, and Final Pose was classified as `parallel_quest` without one. This was a deterministic metadata gap directly affecting PQ↔skill joins.
- Changes: set `source_quest` to **95, 95, 57, 74** respectively; preserved all existing acquisition text and evidence; added a dated cross-link normalization note to each record. No mechanics, reward conditions, or source claims were changed.
- Validation: re-fetched and parsed `docs/data/skills.json`; record count remains **305**. `quest_or_mission` records missing `source_quest` dropped from **3 to 0**. **234** skill records now have numeric `source_quest` identifiers. Repository data contains **0** internal UI citation artifacts.
- CI: not exposed for this direct commit; no CI success is claimed.
- Commit: `e758b40ee4f23876cf05a5fd9872cfa1e7e97008`.
- Live census after editing: **305 skills / 234 numeric PQ-linked skill records / 0 quest_or_mission records missing source_quest**.
- Exact next batch: inspect the remaining non-numeric `source_quest` values and classify them into true non-PQ acquisition routes versus records whose PQ/story/mentor identifier can be safely normalized. Prioritize deterministic joins first and preserve strings where the source is genuinely not a PQ.


### 2026-09-21 cycle update — skill Expert Mission cross-link normalization
- Live census before editing: **305 canonical skill records**; previous PQ normalization left **42** non-numeric `source_quest` values.
- Bounded batch: **Data Input (EM-20), Super Spirit Bomb (EM-16), Supernova (EM-6)**.
- Repository evidence: the three skills already had explicit Expert Mission acquisition text, and the dedicated Expert Mission evidence layers use canonical IDs `EM-20`, `EM-16`, and `EM-6` for these missions. The prior human-readable `source_quest` strings therefore represented deterministic cross-domain join candidates rather than uncertain acquisition claims.
- Changes: normalized `source_quest` to `EM-20`, `EM-16`, and `EM-6`; retained `source_quest_or_shop` as the human-readable mission title/context and preserved all reward-condition uncertainty. Added dated normalization notes and verification dates.
- Evidence limits: no drop rate, Z-Rank requirement, or guaranteed reward condition was promoted. The Expert Mission evidence remains partially verified where its own acquisition conditions are unresolved.
- Validation: `skills.json` re-fetched and parsed successfully; **305 records**, **3 canonical Expert Mission joins**, **39 remaining non-numeric source_quest values**, and **0 internal UI citation artifacts** in the canonical JSON.
- CI: not exposed for the direct commit; no CI success is claimed.
- Commit: `e63d045ddeed4d2834d24511ddf1e07e885a5671`.
- Live census after editing: **305 skills / 3 explicit EM-ID joins / 39 non-numeric source_quest values**.
- Exact next batch: inspect the remaining 39 non-numeric sources for other already-existing canonical relationship IDs (mentor lessons, Advancement Tests, Time Rifts, story/Future Saga missions, Shenron wishes). Only normalize when a matching repository identifier is already established; do not invent IDs or convert descriptive progression routes into false PQ/EM numbers.


### 2026-09-21 cycle update — mentor-to-skill cross-link batch
- Live census before editing: **305 canonical skills** and **33 indexed mentors**.
- Bounded batch: **8 mentor-acquired skills** with explicit mentor-training routes: Dancing Parapara → `mentor-pan`; Darkness Rush (Melee/Ranged) → `mentor-lord-slug`; Deadly Dance → `mentor-android-18`; Death Ball → `mentor-frieza`; Destructo-Disc → `mentor-krillin`; Galick Gun → `mentor-vegeta`; Instant Transmission → `mentor-goku`.
- Evidence: each skill's existing `source_quest`/unlock text explicitly names the mentor and lesson/training route; the canonical mentor index supplies matching IDs. This establishes deterministic `mentor_teaches_skill` endpoints without changing acquisition semantics.
- Changes: added `source_mentor` canonical IDs. Human-readable acquisition fields were retained unchanged.
- Evidence limits: Lord Slug and Pan mentor records are indexed; this cycle did not promote their broader lesson/reward verification state. No unsupported lesson numbers or reward conditions were added beyond existing skill text.
- Validation: **305 skills**, **8 source_mentor links**, all link values match the repository's `mentor-*` ID convention, **0 internal UI citation artifacts** in canonical skills JSON.
- CI: not exposed for the direct commit; no CI success is claimed.
- Commit: `f5b642db98845c682c91e446a56112d52c93247d`.
- Exact next batch: continue the deterministic mentor-link population for the remaining mentor-derived skills (starting with Masenko, Maximum/Full Power Charge where applicable, Perfect Shot, Rise to Action, Shadow Crusher, Spirit Bomb, and Hit's three Time Skip skills), then audit whether the canonical relationship contract should expose `source_mentor` as a formal indexed relationship field.


### 2026-09-21 cycle update — complete deterministic mentor-to-skill links
- Live census before editing: **305 canonical skills / 33 indexed mentors**.
- Bounded batch: **8 additional mentor-derived skills**: Masenko → `mentor-gohan-kid`; Perfect Shot → `mentor-cell`; Rise to Action → `mentor-krillin`; Shadow Crusher → `mentor-cooler`; Spirit Bomb → `mentor-goku`; Time Skip/Back Breaker, Time Skip/Flash Skewer, and Time Skip/Jump Spike → `mentor-hit`.
- Changes: added canonical `source_mentor` endpoints while retaining existing acquisition prose.
- Validation: **16 total source_mentor links** across the 305-skill dataset; all endpoints match canonical `mentor-*` IDs; **0** internal UI citation artifacts.
- Evidence limits: no broader mentor verification state or unverified reward conditions were promoted.
- CI: not exposed for direct commit; no CI success claimed.
- Commit: `9b9cdfb0746bbe10db6ec64ac220ed4d5e406023`.
- Live census after editing: **305 skills / 16 mentor links**.
- Exact next batch: audit the remaining non-mentor descriptive acquisition routes for canonical IDs, beginning with Advancement Tests and Time Rift/Future Saga routes, while keeping shop/story prerequisites distinct from actual acquisition endpoints.


### 2026-09-21 cycle update — Advancement Test canonical endpoints and skill links
- Live census before editing: **305 canonical skills**; no dedicated Advancement Test canonical file existed.
- Bounded batch: **4 source-backed Advancement Test endpoints** tied to existing skill acquisition evidence: Easy, Advanced, God, and Super Class tests.
- Research/evidence: existing canonical skill records explicitly establish Energy Charge → Easy Class, Full Power Charge → Advanced Class, Maximum Charge → God Class, and Potential Unleashed → Super Class. Existing source URLs were reused; no new reward claims were inferred.
- Changes: created `docs/data/advancement-tests.json` with stable IDs `advancement-test-easy`, `advancement-test-advanced`, `advancement-test-god`, `advancement-test-super`; added matching `source_advancement_test` fields to the four skills; formalized the optional skill cross-domain fields in `record-expansion-contract.json` and added the Advancement Test domain contract.
- Evidence limits: these are indexed relationship endpoints, not complete Advancement Test records. Objectives, rank thresholds, progression details and complete reward tables remain explicitly unresolved.
- Validation: **305 skills / 4 Advancement Test records / 4 skill→Advancement Test links / 0 broken endpoints / 0 internal UI citation artifacts** in canonical skills JSON. New Advancement Test JSON parses successfully.
- CI: not exposed for the direct commits; no CI success is claimed.
- Commits: `46a4577a9d7c401046754d72ff027317f182ff22` (Advancement Test endpoints), `60ca17d680174b933590fce01d405cd09c08bb70` (skill links), `d3a62cf6b1486fb3b225cf135cf4a03eff2ebbdf` (contract).
- Live census after editing: **305 skills / 16 mentor links / 3 Expert Mission links / 4 Advancement Test links / 4 Advancement Test endpoints**.
- Exact next batch: build the next source-backed canonical relationship layer for Time Rift/Future Saga acquisition routes, beginning with the existing Super Saiyan, Super Vegeta, Turn Golden, Power Pole Pro, Purification, and Future Super Saiyan records. Do not invent mission numbering where the repository does not establish it.


### 2026-09-21 cycle update — Time Rift and Unknown History canonical skill endpoints
- Live census before editing: **305 canonical skills / 305 skill-index records**.
- Bounded batch: **Super Saiyan, Super Vegeta, Turn Golden, Power Pole Pro, Purification, Future Super Saiyan**.
- Added canonical Time Rift endpoints for the five race-focused rifts: Capsule Corporation, Guru's House, Frieza's Spaceship, Majin Buu's House, and Hercule's House.
- Added a canonical **Unknown History** story endpoint for the hidden post-game route used by Future Super Saiyan.
- Added deterministic skill relationship fields source_time_rifts and source_story_mission; synchronized the canonical skills layer and skills-index.json.
- Added time-rift-skill-crosslink-report.json with forward Time Rift → skill edges and reverse skill → Time Rift edges, plus the Unknown History relationship.
- Formalized the two new cross-domain fields in docs/data/record-expansion-contract.json.
- Evidence: current repository skill records were reconciled against dedicated skill references and independent/current walkthrough evidence. Future Super Saiyan is explicitly linked to all five rifts plus Unknown History because its acquisition requires the five Distorted Time Eggs and the hidden story route. No mission-number or unsupported prerequisite was invented.
- Evidence limits: the Time Rift endpoints describe relationship identity and acquisition context, not exhaustive NPC schedules, quest timing, or every reward in each rift. Those remain separate research domains.
- Validation: canonical skills and index both remain **305 records**; all six target skills have valid Time Rift endpoints; the reverse report has **6 skills / 7 forward skill edges**; **0 broken relationship endpoints**; no internal citation markup was copied into repository data.
- CI: combined status and commit-associated workflow lookup exposed **no statuses/runs** for the direct data commits; no CI success is claimed and validators were not weakened.
- Commits: bbcdc5b (Time Rift endpoints), abcffda (Unknown History endpoint), bb298f5 (contract), a552902 (skills), dfe723c (skills index), e7c721d (bidirectional cross-link report).
- Live census after editing: **5 canonical Time Rift endpoints / 1 canonical story endpoint / 305 skills / 305 skill-index records / 6 skills linked to Time Rift endpoints / 7 forward Time Rift→skill edges / 0 broken endpoints**.
- Exact next batch: **extend the same deterministic relationship pattern to the remaining race/time-rift acquisition skills (including Become Giant as a reverse-link completion check), then move into Future Saga acquisition endpoints for later Awoken skills.**


### 2026-09-21 correction — complete Future Super Saiyan Time Rift fan-out
- The previous edge-count correction is superseded by a data-model completion: each of the five canonical Time Rift endpoints now explicitly lists Future Super Saiyan as a dependent unlock relationship, because all five Distorted Time Eggs are required for Unknown History.
- Regenerated time-rift-skill-crosslink-report.json. Live relationship count is now **6 skills linked to Time Rifts / 11 forward Time Rift → skill edges / 0 broken endpoints**.
- This preserves deterministic navigation in both directions: each rift can expose its race-specific Awoken skill plus its contribution to Future Super Saiyan, while Future Super Saiyan resolves back to all five rifts and Unknown History.


### 2026-09-21 cycle update — Namekian and Future Saga acquisition endpoints
- Live census before editing: **305 skills / 305 skill-index records / 5 Time Rift endpoints / 1 Unknown History endpoint**.
- Bounded batch: **Become Giant** and **The Power to Overcome**.
- Research/evidence: Become Giant's current external references identify Guru's House / Namekian Awakening as its acquisition endpoint and distinguish the required Namekian progression from the transformation itself. The Power to Overcome is tied to Future Saga Chapter 4 and Quest 31, Ultimate All-Out Showdown; current 2026 guide evidence identifies the final mission as the unlock point and the Chapter 4 DLC as required.
- Changes: added `source_time_rifts` to Become Giant; created `future-saga-story-record-layer.json`; linked The Power to Overcome to `story-future-saga-chapter-4-quest-31`; formalized the story-mission domain in the expansion contract; updated the bidirectional cross-link report.
- Evidence limits/conflicts preserved: no unverified mission-number claims were added for older Time Rift routes; The Power to Overcome's mechanics already contain conflicting measured values in the canonical skill record, and those conflicts remain unresolved rather than being flattened.
- Validation: **305/305 canonical/index parity preserved; 0 broken relationship endpoints; 2 target skill relationship projections match; 0 citation artifacts in changed canonical JSON; 5 Time Rifts + 2 story-mission endpoints; cross-link report now has 11 Time Rift→skill edges and 2 story-skill edges**.
- CI: combined status exposed no statuses for the contract commit; no CI success is claimed.
- Commits: `a646663` (skills), `596b0d8` (skills index), `a0370c9` (Future Saga endpoint), `7968132` (story contract), `4c4f7b7` (cross-link report).
- Live census after editing: **305 skills / 305 skill-index records / 5 Time Rift endpoints / 1 Unknown History endpoint / 1 Future Saga story endpoint / 6 Time Rift-linked skills / 11 Time Rift→skill edges / 2 story-skill edges / 0 broken endpoints**.
- Exact next batch: **expand the Future Saga story endpoint into its chapter/quest relationship layer for the remaining newly introduced skills and rewards, starting with the other Chapter 4 skills already present in canonical data; then reconcile any existing skill-to-PQ links that can be deterministically reverse-indexed without changing unresolved acquisition conditions.**


### 2026-09-21 cycle update — Future Saga Chapter 4 PQ ↔ skill graph completion
- Researched the remaining Chapter 4 skills already present in canonical data: **Dragon Spiral, Indomitable, and Venus Fist**. Current repository PQ records place Dragon Spiral + Indomitable in PQ185 (A God's Amusement) and Venus Fist in PQ186 (Frieza's Right-Hand Man); current Chapter 4 documentation confirms the DLC contains two Parallel Quests and four new moves including one Awoken Skill.
- Added deterministic `skill_ids` to PQ185/PQ186, `source_parallel_quests` to the three skill records and skill index, and explicit Chapter 4 `skill_relationships`/PQ references in `future-saga-story-record-layer.json`.
- Expanded `record-expansion-contract.json` with PQ `skill_ids` and skill `source_parallel_quests` cross-domain fields.
- Expanded `time-rift-skill-crosslink-report.json` with **2 PQ endpoints / 3 PQ→skill edges**.
- Validation: **305 skills / 305 index records / 186 PQ records / 4 Chapter 4 story-linked skills / 0 broken endpoints / 3 edited skill/index parity checks passed / 0 citation artifacts in canonical JSON**.
- Exact relationship graph now lets a user traverse **Future Saga Chapter 4 → Quest 31 → The Power to Overcome**, and **Future Saga Chapter 4 → PQ185/PQ186 → individual skills**, while each skill resolves back to its source PQ and Chapter 4 story endpoint.
- Evidence boundary: the canonical PQ records already distinguish Basic Reward from Ultimate Finish conditions. No new Ultimate Finish requirement or drop probability was inferred here. Current official DLC material confirms Chapter 4's content scope, while the maintained repository reward records supply the exact skill-to-PQ mapping.
- Exact next batch: **audit the broader PQ ↔ skill graph for orphaned `source_quest` skills and PQ `skill_rewards`, starting with the newest DLC/PQ records, and repair deterministic reverse links in larger batches without changing acquisition facts.**


### 2026-09-21 cycle update — comprehensive PQ ↔ skill reverse-index reconciliation
- Live census before editing: **305 skills / 305 skill-index records / 186 PQ records**.
- Bounded batch: audit every numeric `source_quest` in canonical skills against PQ endpoints, then reconcile every PQ `skill_rewards` name into deterministic `skill_ids` and reverse `source_parallel_quests`.
- Result: **234 skills** now have deterministic reverse PQ endpoints; **164 PQ records** contain `skill_ids`; **235 unique PQ→skill ID edges** are represented in the canonical layer.
- Reconciled three source-name aliases without changing acquisition facts: `Chain Destructo-disc Barrage` → `Chain Destructo-Disc Barrage`; `Kamekameha` → `Kamehameha`; `III Bomber` → `Ill Bomber`.
- Created/synchronized `docs/data/pq-skill-crosslink-report.json` as the persisted bidirectional audit. It now records **235 forward edges / 234 reverse skill endpoints / 0 unresolved forward edges / 0 orphaned reverse sources** and preserves alias spelling where the PQ source uses it.
- Updated `parallel-quests-record-layer.json`, `skills.json`, and `skills-index.json` together so navigation works in both directions: PQ → skill ID → skill details/source, and skill → PQ ID → PQ details/rewards.
- Validation: **305/305 skills-index parity; 186 PQ endpoints valid; 0 broken relationship endpoints; 0 unresolved reward names; 0 canonical citation artifacts in changed JSON**.
- CI: commit-associated combined status and workflow-run lookup exposed **no statuses/runs** for the direct data commit; no CI success is claimed.
- Commits: `fd8410b` (PQ skill IDs), `155f0e8` (skill reverse links), `e746d3c` (skill index), `11015fa` (cross-link report).
- External/current repository research supports treating PQ reward tables as the primary relationship evidence and confirms PQs are the game's main skill-farming relationship layer.
- Exact next batch: **audit the remaining 71 skills without `source_parallel_quests` by acquisition type, separating non-PQ sources (mentor, shop, Time Rift, story, Advancement Test) from genuinely missing PQ reverse links; then repair only evidence-backed missing routes.**


### 2026-09-21 cycle update — 71-skill non-PQ acquisition audit
- Audited every canonical skill lacking `source_parallel_quests` after the PQ reconciliation. **71 skills** were classified without inventing PQ relationships.
- Classification: **7 Time Rift, 6 story/story-Shop, 17 mentor/training, 4 Advancement Test, 15 Skill/TP/STP Shop, 3 Expert Mission, 10 character/roster-only, 1 starting move, 3 Shenron wish, 5 mentor-like routes requiring a future mentor layer, 0 genuinely unresolved acquisition cases** after refining Beast, Super Saiyan 2 (stage), SSGSS, SSGSS Evolved, and Ultra Instinct.
- Created `docs/data/skill-acquisition-coverage-report.json` to persist this classification and explicitly prevent non-PQ acquisition sources from being forced into the PQ graph.
- Important architecture finding: the repository currently has **no canonical mentor or Expert Mission record layer** discoverable in the live data tree. Therefore mentor/expert skills retain their textual acquisition facts instead of receiving guessed IDs. This follows the repository null/provenance policy.
- No canonical acquisition facts were changed in this cycle; the output is a coverage/audit layer identifying the next schema expansion targets.
- External corroboration: PQs are a major skill source, but rewards can also come from other acquisition systems, so the audit deliberately keeps those systems separate.
- Validation target for next cycle: build the missing **mentor record layer** first, because 17 direct mentor-training skills plus 3 mentor-like Awoken routes are currently blocked from deterministic bidirectional mentor ↔ skill navigation; then build Expert Mission endpoints for the 3 EM-sourced skills.
- Exact next batch: **create the canonical mentor record layer and connect the 17 direct mentor-training skills in larger deterministic batches, starting with mentors whose skills are already fully named in canonical skill data; then add Expert Mission records.**


### 2026-09-21 cycle update — mentor → skill cross-domain layer
- Expanded the existing `docs/data/mentors-record-layer.json` from identity-only records into a usable cross-domain layer while preserving its 33 canonical mentor identities.
- Added verified mentor → skill relationships for **11 mentors / 16 skill edges**: Krillin (2), Gohan (Kid) (1), Vegeta (1), Frieza (1st Form) (1), Cooler (Final Form) (1), Android 18 (1), Lord Slug (2), Pan (1), Goku (2), Cell (1), and Hit (3).
- Added `source_mentor` to the corresponding canonical skill records and mirrored the field in `skills-index.json`.
- Extended `docs/data/record-expansion-contract.json` so `source_mentor` is an explicit skill cross-domain field.
- Created `docs/data/mentor-skill-crosslink-report.json` with the 16 deterministic forward edges and unresolved-edge tracking.
- Validation: **33 mentors, 11 mentors with linked skills, 16 mentor→skill edges, 16 skills with mentor reverse sources, 0 broken mentor endpoints, skill-index mentor parity = true**.
- External mentor references corroborate that mentors teach signature skills through initiation/lesson progression; official Bandai Namco documentation confirms the mentor system teaches character moves.
- The previous coverage audit's mentor count is now refined from 17 directly verified routes to **16**, because only 16 canonical skill records currently contain an exact mentor-training route that could be deterministically linked without guessing.
- Exact next batch: **finish the remaining mentor acquisition mappings by auditing the existing 33 mentor identities against all skill records, then create the Expert Mission record layer for the 3 EM-linked skills (Data Input, Super Spirit Bomb, Supernova).**


## 2026-09-21 — Super Soul 096–103 canonical frontier correction and PQ reverse-link reconciliation

- Live census before editing: **90 canonical Super Soul records / 186 canonical PQ records**. The prior handoff's proposed 096–103 names were already represented by earlier canonical IDs, so they were rejected as duplicate work after live-corpus reconciliation.
- Bounded batch: **8 new unique source-corpus records** promoted as super-soul-096 through super-soul-103: It must be some kind of trick..., It all comes down to this!, I'll keep adding a bit of power to my attacks!, You're not much of a fun fight!, I think I'm getting the hang of this., I will put a stop to you, fiend!, There's more where that came from!, and Emoc htorf! Peas and Carrots!.
- Evidence: maintained Madreag Super Soul corpus plus its item-level source pages and independent current references. Exact named PQ sources were accepted for 098/100 (PQ151), 101 (PQ152), and 099/102 (PQ153). Raid/event acquisition remains source-labeled rather than expanded into unsupported recurrence claims.
- Changes: added the eight canonical Super Soul records with acquisition/effect/provenance fields; synchronized PQ151–153 with super_soul_ids / super_soul_rewards; rebuilt docs/data/pq-super-soul-crosslink-report.json directly from the canonical Super Soul registry.
- Validation: **98 canonical Super Souls / 186 canonical PQs / 34 forward / 34 reverse PQ↔Super Soul edges / 28 unique PQ endpoints / 34 unique Super Soul endpoints / 64 unresolved Super Soul routes / 0 broken endpoints**. Changed JSON parsed successfully.
- Evidence limits: community-measured percentages/durations were retained as non-canonical context; no raid recurrence schedule, drop rate, or unsupported acquisition route was invented. Existing source-text behavior conflicts remain bounded by the canonical notes.
- Exact next batch: **Super Soul 104–111**, after another live-corpus reconciliation. The next unique source-backed frontier currently begins with Looks like I mixed up the capsules..., I'll be the one to fight you!, This is your true power?, You need to be more careful., Still haven't figured out you're gonna lose?, Heh heh! I'm not as rusty as I look!, See? It's a good thing I was here, right?, and I can tell you're an amateur by the way you pose!.


## 2026-09-21 — Super Soul 104–111 frontier + PQ reverse-link reconciliation

- Live census before editing: **98 canonical Super Souls / 186 canonical PQ records**.
- Bounded batch: **Super Soul 104–111** — Looks like I mixed up the capsules..., I'll be the one to fight you!, This is your true power?, You need to be more careful., Still haven't figured out you're gonna lose?, Heh heh! I'm not as rusty as I look!, See? It's a good thing I was here, right?, and I can tell you're an amateur by the way you pose!.
- Evidence: exact next eight unique entries from the maintained Madreag final-DLC-era Super Soul corpus; source-page searches confirmed slugs and acquisition identities. Deterministic PQ endpoints: 105/107 → PQ157, 106/108 → PQ156, 109/110 → PQ158. Raid records 104 and 111 remain without inferred PQ routes.
- Changes: added canonical Super Souls 104–111; synchronized PQ156–158 reward/link fields; rebuilt docs/data/pq-super-soul-crosslink-report.json from the canonical registry.
- Evidence limits: no unsupported raid recurrence, drop-rate, or inferred quest relationships were added. Community-measured values remain bounded by the record's verification notes.
- Validation: **106 canonical Super Souls / 186 canonical PQs / 40 forward / 40 reverse edges / 31 unique PQ endpoints / 40 unique Super Soul endpoints / 66 unresolved Super Soul routes / 0 broken endpoints**. All three changed JSON files parsed successfully; **0 internal UI/search citation artifacts** detected.
- CI: no workflow status was exposed for these data commits; no CI success is claimed.
- Commits: `861176b38b926d2210aad941bb16b6218a667dee` (canonical records); `8f974ecd7d6bae76f13a8e2a4a1f01f2bb2b4687` (PQ156–158); `9c0537a3e7f3b960a72c8aa9a630738b7ee658e6` (crosslink rebuild).
- Exact next batch: **Super Soul 112–119**, after live-corpus reconciliation. Start immediately after `I can tell you're an amateur by the way you pose!`; establish acquisition identity, then add only explicit cross-domain endpoints.


### 2026-09-21 cycle update — Super Soul 112–119 + PQ reverse-link reconciliation
- Live census before editing: **106 canonical Super Souls / 186 canonical PQ records**.
- Bounded batch: **Super Soul 112–119** — That's minus ten points!; I'm a super hero!; Just figured out who the real villain is!; Help me, Daddy! I'm scared!; Damn... Gonna have to go all out!; Not a single word!; I'm a whole new me.; Shenron really went the extra mile.
- Evidence: reconciled the maintained Madreag Super Soul source corpus and exact next unique source frontier. Explicit PQ endpoints: 118 → PQ161 and 119 → PQ162. TP/STP shop and Raid Quest Event acquisitions were not assigned unsupported PQ routes.
- Changes: added super-soul-112 through super-soul-119; synchronized PQ161–162 reward/link fields; rebuilt docs/data/pq-super-soul-crosslink-report.json; updated coverage and changelog records.
- Validation: **114 canonical Super Souls / 186 canonical PQ records / 42 forward / 42 reverse edges / 33 unique PQ endpoints / 42 unique Super Soul endpoints / 72 unresolved Super Soul routes / 0 broken endpoints**. All three JSON files parsed successfully and contain **0 internal UI/search citation artifacts**.
- CI: no workflow status was exposed for the data commits; no CI success is claimed.
- Commits: `9fad082326acec7c671bb66d8aebe8bcdde12049` (canonical records); `3b1762a394d934c4020425e7623d059ad6950128` (PQ161–162); `68d41e5c11b70b13e3aacdabc2c641fdada6499d` (crosslink rebuild).
- Exact next batch: **Super Soul 120–127**, after live-corpus reconciliation. Continue immediately after `Shenron really went the extra mile.` and establish acquisition identity before adding records or cross-domain edges.


### 2026-09-21 cycle update — Super Soul 120–127 + PQ159 reconciliation
- Live census before editing: **114 canonical Super Souls / 186 canonical PQ records**.
- Bounded batch: **Super Soul 120–127** — Enter the hero!; The Red Ribbon Army is back in business!; Something deadly's about to happen...; I never could've gotten here on my own!; I have an unlimited energy supply...; Die!; I'd rather fight alone and die!; That's a dead ball now, right?.
- Evidence: reconciled the maintained Madreag Super Soul source corpus. Explicit PQ route: 120/121 → PQ159. TP/STP shop, Festival of Universes, and Raid Quest Event acquisitions were not assigned unsupported PQ routes.
- Changes: added super-soul-120 through super-soul-127; synchronized PQ159 reward/link fields; rebuilt docs/data/pq-super-soul-crosslink-report.json; updated coverage and changelog records.
- Validation: **122 canonical Super Souls / 186 canonical PQ records / 44 forward / 44 reverse edges / 34 unique PQ endpoints / 44 unique Super Soul endpoints / 78 unresolved Super Soul routes / 0 broken endpoints**. All three JSON files parsed successfully and contain **0 internal UI/search citation artifacts**.
- CI: no workflow status was exposed for the data commits; no CI success is claimed.
- Commits: `746bba9ccdaabd3c9de5eb360974adf37a67ec7a` (canonical records); `6221a87dddd369e33b52159ff487ee0777452093` (PQ159); `322359286f1a4fd05ca585bec36a2085acf4e6a6` (crosslink rebuild).
- Exact next batch: **Super Soul 128–135**, after live-corpus reconciliation. Continue immediately after `That's a dead ball now, right?` and establish acquisition identity before adding records or cross-domain edges.


### 2026-09-21 cycle update — Super Soul 128–135 + PQ reverse-link reconciliation
- Live census before editing: **122 canonical Super Souls / 186 canonical PQ records**.
- Bounded batch: **Super Soul 128–135** — Nothing beats flying!; There was actually five of me!; Hope you're ready for a trip!; I'm not about to let Pan see me lose!; This place will be your grave!; I'll surpass you as I am, with my OWN power!; You will know the power of the gods!; I learned a lot from how you fight.
- Evidence: reconciled the maintained Madreag Super Soul source corpus. Explicit PQ routes: 130→PQ166, 131→PQ168, 132→PQ164, 133→PQ174, 134→PQ173. Raid and Limited Time Event acquisitions were not assigned unsupported PQ routes.
- Changes: added super-soul-128 through super-soul-135; synchronized PQ164/166/168/173/174 reward/link fields; rebuilt docs/data/pq-super-soul-crosslink-report.json; updated coverage and changelog records.
- Validation: **130 canonical Super Souls / 186 canonical PQ records / 49 forward / 49 reverse edges / 39 unique PQ endpoints / 49 unique Super Soul endpoints / 81 unresolved Super Soul routes / 0 broken endpoints**. All three JSON files parsed successfully and contain **0 internal UI/search citation artifacts**.
- CI: no workflow status was exposed for the data commits; no CI success is claimed.
- Commits: `790c12d76d6c56e8152ccdabf5ae7829c1fdb2db` (canonical records); `feff2a5afc4faf0127e16aedf45c0b0a08a1bee3` (PQ links); `e40cc212e37b51dd69ae5d169a772d56284778d9` (crosslink rebuild).
- Exact next batch: **Super Soul 136–143**, after live-corpus reconciliation. Continue immediately after `I learned a lot from how you fight.` and establish acquisition identity before adding records or cross-domain edges.


### 2026-09-21 cycle update — Super Soul 128–135 + PQ reverse-link reconciliation
- Live census before editing: **122 canonical Super Souls / 186 canonical PQ records**.
- Bounded batch: **Super Soul 128–135** — Nothing beats flying!; There was actually five of me!; Hope you're ready for a trip!; I'm not about to let Pan see me lose!; This place will be your grave!; I'll surpass you as I am, with my OWN power!; You will know the power of the gods!; I learned a lot from how you fight.
- Evidence: reconciled the maintained Madreag Super Soul source corpus. Explicit PQ routes: 130→PQ166, 131→PQ168, 132→PQ164, 133→PQ174, 134→PQ173. Raid and Limited Time Event acquisitions were not assigned unsupported PQ routes.
- Changes: added super-soul-128 through super-soul-135; synchronized PQ164/166/168/173/174 reward/link fields; rebuilt docs/data/pq-super-soul-crosslink-report.json; updated coverage and changelog records.
- Validation: **130 canonical Super Souls / 186 canonical PQ records / 49 forward / 49 reverse edges / 39 unique PQ endpoints / 49 unique Super Soul endpoints / 81 unresolved Super Soul routes / 0 broken endpoints**. All three JSON files parsed successfully and contain **0 internal UI/search citation artifacts**.
- CI: no workflow status was exposed for the data commits; no CI success is claimed.
- Commits: `790c12d76d6c56e8152ccdabf5ae7829c1fdb2db` (canonical records); `feff2a5afc4faf0127e16aedf45c0b0a08a1bee3` (PQ links); `e40cc212e37b51dd69ae5d169a772d56284778d9` (crosslink rebuild).
- Exact next batch: **Super Soul 136–143**, after live-corpus reconciliation. Continue immediately after `I learned a lot from how you fight.` and establish acquisition identity before adding records or cross-domain edges.


### 2026-09-21 cycle update — Super Soul 136–143 + PQ reverse-link reconciliation
- Bounded batch: **Super Soul 136–143** — You intend to defy me?!; I will NOT give up! EVER!; We're tougher than we look!; You're not taking this away from us!; It's about time...; Strength is justice! Strength is absolute!; I'll take you all on at once!; So, Hakai.
- Explicit PQ routes: 140→PQ175, 141→PQ177, 142→PQ178. Raid and TP/STP Medal Shop acquisitions were not assigned unsupported PQ routes.
- Validation: **138 canonical Super Souls / 186 canonical PQ records / 52 forward / 52 reverse edges / 42 unique PQ endpoints / 52 unique Super Soul endpoints / 86 unresolved routes / 0 broken endpoints**; changed JSON parsed and contained 0 internal citation artifacts.
- Commits: `cf87e747e95d7285fc81ed23e2492b467b5e6fd8`; `c4c5a4e053c34dda4fbd950371cced69997e94d2`; `13d89bcf536af250de8ff44330032dcabea94830`.
- Exact next batch: **Super Soul 144–151**, after live-corpus reconciliation, beginning after `So, Hakai.`.


## 2026-09-21 live Super Soul census correction — 144–151 frontier

- The live canonical Super Soul registry now contains **146 records**, not the stale 138-record milestone; IDs reach 151 because prior frontier corrections left intentional ID gaps.
- The 144–151 frontier added eight unique records after identity reconciliation; Damn it all! remains the pre-existing super-soul-062 and was not duplicated.
- The deterministic PQ↔Super Soul report now contains **56 forward / 56 reverse edges**, **46 unique PQ endpoints**, **56 unique Super Soul endpoints**, **90 unresolved routes**, and **0 broken endpoints**.
- PQ reward projections were synchronized for PQ179, PQ182, PQ183, and PQ184. Community-measured magnitudes/durations and the Poltarat damage-direction conflict remain explicitly bounded.
- This section supersedes the stale Super Soul milestone text above for live-count purposes.

## 2026-09-21 live Super Soul census correction — 152–153 terminal source-corpus batch

- The maintained Madreag source corpus had exactly two unique records after the 144–151 frontier: **So fast! Are they learning how to use their power?!** and **Enough food for one person...**. Both were reconciled against the canonical registry before assignment.
- Added **super-soul-152** and **super-soul-153**. Both are 5th Festival of Universes Total Glory Point rewards with TP Medal Shop rotation; neither has an explicit PQ endpoint, so no PQ relationship was inferred.
- Deterministic crosslink report remains endpoint-clean: **56 forward / 56 reverse edges / 46 unique PQ endpoints / 56 unique Super Soul endpoints / 92 unresolved routes / 0 broken endpoints**.
- The source corpus is now exhausted at this frontier: no further source-backed Super Soul records remain after super-soul-153 in the maintained corpus inspected for this cycle. Future work should pivot to the next highest-priority validator/audit or another repository corpus rather than inventing additional Super Souls.

### 2026-09-21 cycle update — Krillin/Tien/Yamcha/Piccolo mentor-skill reconciliation
- Live mentor census: **33 canonical mentors**. The existing mentor layer already contained explicit lesson→skill mappings for these four mentors, while the crosslink report had only 16 edges.
- Bounded batch: **14 deterministic mentor→skill edges** — Krillin (2 missing), Tien (4), Yamcha (4), Piccolo (4).
- Evidence: canonical `docs/data/mentors-record-layer.json` lesson arrays plus matching `source_mentor` fields in `docs/data/skills-index.json`. No external inference or acquisition rewrite was needed.
- Changes: rebuilt `docs/data/mentor-skill-crosslink-report.json`; no canonical skill acquisition facts required modification because the source_mentor provenance was already present.
- Validation: **33 mentors / 30 mentor-linked identities / 30 mentor→skill edges / 30 linked skill endpoints / 0 unresolved edges / 0 broken mentor endpoints**. Report and skills-index JSON parsed successfully; all promoted skill IDs exist in the canonical index.
- CI: no workflow/status result was exposed; no CI success is claimed.
- Exact next batch: **audit the next four mentors after Piccolo (Raditz, Gohan (Kid), Nappa, Vegeta), promoting only lesson mappings whose corresponding skill IDs exist and whose source_mentor provenance agrees.**

### 2026-09-21 validation correction — mentor-skill census
- The immediately preceding mentor reconciliation entry overstated the number of linked mentor identities. The verified live count is **33 canonical mentors / 14 mentors with linked skills / 30 mentor→skill edges / 30 unique skill endpoints / 0 unresolved edges / 0 broken skill endpoints**.
- This is a documentation/count correction only; the 30 deterministic edges written to `docs/data/mentor-skill-crosslink-report.json` are unchanged.
- Exact next batch remains **Raditz, Gohan (Kid), Nappa, and Vegeta**, using lesson mapping ↔ `source_mentor` parity.
- Latest report validation was persisted in `docs/data/mentor-skill-crosslink-report.json`.

### 2026-09-21 cycle update — Raditz/Gohan (Kid)/Nappa/Vegeta mentor-skill reconciliation
- Promoted **14 deterministic mentor→skill edges** supported by canonical mentor lesson mappings and matching `source_mentor` provenance: Raditz (4), Gohan (Kid) (3 new), Nappa (4), Vegeta (3 new). Existing Masenko and Galick Gun edges were preserved without duplication.
- Rebuilt `docs/data/mentor-skill-crosslink-report.json` to **33 canonical mentors / 18 linked mentors / 44 edges / 44 unique skill endpoints / 0 unresolved / 0 broken skill endpoints**.
- No skill acquisition semantics were changed; this was a relationship-layer reconciliation only.
- Exact next batch: **Zarbon, Dodoria, Captain Ginyu, and Frieza (1st Form)**, using the same lesson↔skill-ID↔source_mentor parity check.

### 2026-09-21 cycle update — Zarbon/Dodoria/Captain Ginyu/Frieza mentor-skill reconciliation
- Promoted **15 deterministic mentor→skill edges** supported by canonical mentor lesson mappings and matching `source_mentor` provenance: Zarbon (4), Dodoria (4), Captain Ginyu (4), Frieza (1st Form) (3 new). Frieza's existing Death Ball edge was preserved without duplication.
- Rebuilt `docs/data/mentor-skill-crosslink-report.json` to **33 canonical mentors / 20 linked mentors / 59 edges / 59 unique skill endpoints / 0 unresolved / 0 broken skill endpoints**.
- No skill acquisition semantics were changed; this was a relationship-layer reconciliation only.
- Exact next batch: **Android 18, Android 17, Cell, and Hercule**, using the same lesson↔skill-ID↔source_mentor parity check.

### 2026-09-21 validation correction — mentor-linked census
- The live crosslink report verifies **33 canonical mentors / 19 linked mentors / 59 edges / 59 unique skill endpoints / 0 unresolved / 0 broken endpoints**. The preceding cycle note's “20 linked mentors” figure was an arithmetic overstatement and is corrected here.
- The 15 newly promoted edges remain unchanged; no data semantics were altered.
- Exact next batch remains **Android 18, Android 17, Cell, and Hercule**.

### 2026-09-21 cycle update — Android 18/Android 16/Cell/Hercule mentor-skill reconciliation
- Promoted **14 deterministic mentor→skill edges**: Android 18 (3), Android 16 (4), Cell (Perfect) (3), Hercule (4), using canonical lesson mappings plus matching `source_mentor` provenance.
- The requested “Android 17” mentor is **not present** in the canonical 33-mentor layer, so no unsupported relationship was created.
- Live report totals: **33 canonical mentors / 23 linked mentors / 73 edges / 73 unique skill endpoints / 0 unresolved / 0 broken endpoints**.
- No skill acquisition semantics were changed.
- Exact next batch: **Cooler (Final Form), Lord Slug, Majin Buu, and Gohan (Adult) and Videl**, using the same lesson↔skill-ID↔source_mentor parity check.

### 2026-09-21 validation correction — mentor-linked census
- Final live validation shows **33 canonical mentors / 21 linked mentors / 73 edges / 73 unique skill endpoints / 0 unresolved / 0 broken endpoints**. The immediately preceding “23 linked mentors” figure was an arithmetic overstatement and is corrected here.
- The 14 promoted edges are unchanged, and Android 17 remains absent from the canonical mentor layer.
- Exact next batch remains **Cooler (Final Form), Lord Slug, Majin Buu, and Gohan (Adult) and Videl**.

### 2026-09-21 cycle update — Cooler/Slug/Buu/Gohan-Videl mentor-skill reconciliation
- Promoted **14 deterministic mentor→skill edges**: Cooler (Final Form) (3 new), Lord Slug (3 new), Majin Buu (4), and Gohan (Adult) and Videl (4). Existing Cooler Shadow Crusher and Lord Slug Darkness Rush edges were preserved without duplication.
- Live report totals: **33 canonical mentors / 25 linked mentors / 87 edges / 87 unique skill endpoints / 0 unresolved / 0 broken endpoints**.
- No skill acquisition semantics were changed.
- Exact next batch: **Gotenks, Turles, Broly, and God of Destruction Beerus**, using the same lesson↔skill-ID↔source_mentor parity check.

### 2026-09-21 cycle update — Gotenks/Turles/Broly/Beerus mentor-skill reconciliation
- Promoted **16 deterministic mentor→skill edges**: Gotenks (4), Turles (4), Broly (4), and God of Destruction Beerus (4), using canonical lesson mappings plus matching `source_mentor` provenance.
- The Gotenks ultimate route retains its distinct canonical skill ID despite sharing the displayed skill name with another Gotenks route.
- Live report totals: **33 canonical mentors / 27 linked mentors / 103 edges / 103 unique skill endpoints / 0 unresolved / 0 broken endpoints**.
- No skill acquisition semantics were changed.
- Exact next batch: **Whis, Pan, Jaco, and Goku**, using the same lesson↔skill-ID↔source_mentor parity check.

### 2026-09-21 cycle update — Whis/Pan/Jaco/Goku mentor-skill reconciliation
- Live mentor census before editing: **33 canonical mentors / 27 mentors with linked skills / 103 mentor→skill edges / 103 unique skill endpoints / 0 unresolved / 0 broken endpoints**.
- Promoted **13 deterministic mentor→skill edges** supported by canonical mentor lesson mappings plus matching `source_mentor` provenance: Whis (4), Pan (3 new), Jaco (4), Goku (2 new).
- Existing Pan `Dancing Parapara` and Goku `Spirit Bomb` / `Instant Transmission` edges were preserved without duplication.
- No canonical skill acquisition semantics were changed; this cycle reconciled only the relationship layer in `docs/data/mentor-skill-crosslink-report.json`.
- Validation target after promotion: **33 canonical mentors / 29 linked mentors / 116 edges / 116 unique skill endpoints / 0 unresolved / 0 broken endpoints**.
- Exact next batch: **remaining unlinked mentor identities**, beginning with a live audit of the canonical 33-mentor layer against `skills-index.json`; promote only exact lesson→skill-ID→`source_mentor` matches and document any mentor with no deterministic endpoints.


### 2026-09-21 cycle update — Gohan (Future)/Bardock/Bojack/Zamasu mentor-skill reconciliation
- Promoted **15 deterministic mentor→skill edges**: Gohan (Future) (4), Bardock (4), Bojack (4), and Zamasu (3).
- Evidence gate: each promoted endpoint matched the canonical mentor lesson `skill_id` and the corresponding `source_mentor` field in `docs/data/skills-index.json`.
- Zamasu's Initiation lesson, **“I'm thinking of becoming a GodTuber,”** has no canonical skill ID in the skill index and was intentionally left unlinked; no unsupported endpoint was invented.
- Live report totals after promotion: **33 canonical mentors / 33 linked mentors / 131 mentor→skill edges / 131 unique skill endpoints / 0 unresolved / 0 broken endpoints**.
- No canonical skill acquisition semantics were changed.
- Exact next batch: **audit whether any additional bidirectional/reverse-navigation layer is required by the continuation/addendum rules; if not, move to the next explicitly prioritized coverage gap rather than inventing more mentor relationships.**

### 2026-09-21 cycle update — skill acquisition projection normalization
- Workstream: **P1 skill acquisition/DLC-version provenance cleanup**; deterministic producer/index mismatch audit after completing the mentor and Super Soul frontiers.
- Live census: **429 canonical skill-index records**. The canonical `docs/data/skills.json` layer contained `source_quest` values for three PQ-acquired skills whose corresponding `docs/data/skills-index.json` projection had the field absent: Drain Field → PQ95, Flash Bomber → PQ95, and Rakshasa's Claw → PQ57.
- Bounded change: populated those three exact `source_quest` IDs in `docs/data/skills-index.json` only. No acquisition wording, UF status, cost, restriction, DLC provenance, or unresolved drop semantics were changed.
- Evidence: existing canonical `skills.json` records already normalize these exact quest IDs and retain the corresponding `source_parallel_quests`; this is a deterministic cross-layer reconciliation, not new external inference.
- Validation: both skill JSON layers parsed successfully; cross-layer comparison now reports **0 records where skills.json has source_quest but skills-index.json lacks it**. Changed JSON contains no internal UI/search citation artifacts.
- CI: no workflow/status result was exposed for the commit; no CI success is claimed and validators were not weakened.
- Commit: `3d54e9ad713eb7e29dc469911468a658d3c3fb34`.
- Exact next batch: **continue the live P1 skill census by auditing nullable DLC/version provenance and acquisition-specific fields for a bounded 4–12 record group; prefer deterministic cross-layer mismatches before external research.**


### 2026-09-21 cycle update — mentor skill DLC provenance cleanup
- Live skill census before editing: **429 canonical skills**; all 429 had a non-null `dlc_requirement`, but **4 mentor-training records used the non-specific value `DLC`**.
- Bounded batch: **God Splitter, Heavenly Arrow, Instant Severance, and Time Skip/Tremor Pulse**.
- Research/evidence: Zamasu's mentor relationship is documented as **Extra Pack 1**, while Hit's mentor training and Time Skip/Tremor Pulse are documented as **Super Pack 1**.
- Changes: refined the four canonical `dlc_requirement` values in `docs/data/skills.json` and appended explicit 2026-09-21 provenance notes/source coverage. No acquisition route, skill mechanics, or mentor relationship semantics were changed.
- Evidence limits/conflicts preserved: mentor availability can appear in shared play-data even without ownership; the field records the DLC pack that introduced the mentor training relationship, not merely whether the underlying character exists in another pack.
- Validation: **429 canonical skills; 0 missing `dlc_requirement`; 0 generic `DLC` values remain**. Canonical JSON parsed successfully; no skill-index projection change was required because `dlc_requirement` is intentionally outside its current projection field set. Internal citation-artifact scan remains required after the write.
- CI: no actionable workflow result exposed during this cycle; **no CI success claimed**. Validators were not weakened.
- Commit: `9ca5147646a60ceb411dfca5dfdfb924e8a566d2`.
- Exact next batch: **recompute the live skill census, then inspect the remaining 4 records with nullable `source_quest` and the 3 records with nullable `race_restriction`; prioritize only deterministic cross-layer fixes supported by existing repository evidence, without inventing acquisition routes.**

### 2026-09-21 cycle update — skill-index source/restriction projection correction
- Workstream: **P1 skill acquisition/DLC-version provenance cleanup**, bounded deterministic projection reconciliation.
- Live census: **429 canonical skills** and **429 skill-index records**. The canonical/index comparison identified five stale projection values in the two in-scope fields: Data Input `source_quest` (EM-20), Final Pose (PQ74), Super Spirit Bomb (EM-16), Supernova (EM-6), and Ill Bomber `race_restriction` (Majin).
- Changes: corrected those five exact values in `docs/data/skills-index.json` to match canonical `docs/data/skills.json`. No acquisition wording, mechanics, Ultimate Finish status, DLC provenance, or unresolved race evidence was changed.
- Evidence: canonical skill records are the authoritative producer for the index projection; `scripts/build_skills_from_research.py` explicitly projects these fields into `skills-index.json`.
- Evidence limits: the broader canonical/index projection still contains unrelated drift from later canonical enrichment (including newer `last_verified`/mechanics notes and other projected fields). This bounded cycle intentionally corrected only the five stale source/restriction values identified at the live census boundary; no broad regeneration was performed.
- Validation: both JSON documents parse; **429/429 records**; the five targeted source/restriction values match canonical at commit `53959c1bfcf0bbb0c67d6625bdb7c429cd643c0e`. The edited index contains **0 internal AI/UI citation artifacts**. CI status and workflow-run lookup returned no exposed checks/runs; no CI success claimed.
- Commits: `ad2bd70044d982245819621ea63c66116ffc1490`, `53959c1bfcf0bbb0c67d6625bdb7c429cd643c0e`.
- Exact next batch: **audit the next 4–12 deterministic skill-index projection drifts from recent canonical enrichment, prioritizing a single coherent field family (for example `last_verified`/mechanics-note updates) and preserving the generated projection contract.**



### 2026-09-21 skill-index last_verified projection batch

- Live census before editing: **429 canonical skills / 429 skill-index records**.
- Bounded batch: **10 deterministic last_verified projection corrections** — Become Giant, Dancing Parapara, Darkness Rush (Melee), Darkness Rush (Ranged), Data Input, Deadly Dance, Death Ball, Destructo-Disc, Dimension Cannon, and Dragon Spiral.
- Evidence: canonical docs/data/skills.json is the producer of the index projection; no new external acquisition/mechanics claim was introduced.
- Changes: updated only the corresponding last_verified values in docs/data/skills-index.json to match canonical values. No unrelated fields were regenerated.
- Evidence limits: this is a deterministic cross-layer parity correction, not a new verification event; remaining projected-field drift is intentionally left for later bounded batches.
- Validation: both JSON layers parse; 429/429 record counts remain unchanged; the 10 targeted last_verified values now match canonical; **20** broader last_verified mismatches remain; no internal AI/UI/search citation artifacts were found in the changed index.
- CI: workflow/status results remain unavailable; **no CI success claimed** and validators were not weakened.
- Commit: a14d8a7025124ca12a54e55c4b4ba9ffa701cf15.
- Exact next batch: **Energy Charge, Final Pose, Full Power Charge, Galick Gun, Indomitable, Instant Transmission, Masenko, Maximum Charge, Perfect Shot, and Potential Unleashed** — repeat the same canonical→index last_verified parity check and bounded update.


### 2026-09-21 cycle update — skill-index last_verified projection batch 2

- Live census before editing: **429 canonical skills / 429 skill-index records**.
- Bounded batch: **10 deterministic last_verified projection corrections** — Energy Charge, Final Pose, Full Power Charge, Galick Gun, Indomitable, Instant Transmission, Masenko, Maximum Charge, Perfect Shot, and Potential Unleashed.
- Evidence: canonical `docs/data/skills.json` is the producer for the index projection; no new external acquisition/mechanics claim was introduced.
- Changes: updated only the corresponding `last_verified` values in `docs/data/skills-index.json` to match canonical values.
- Evidence limits: deterministic cross-layer parity correction, not a new verification event; the remaining 10 `last_verified` mismatches are intentionally left for the next bounded batch.
- Validation: both JSON layers parse; 429/429 record counts remain unchanged; all 10 targeted values now match canonical; **10** `last_verified` mismatches remain; changed index contains **0 internal AI/UI/search citation artifacts**.
- CI: commit workflow-run lookup and combined status for `124138ef8edeba905223caa0cb4b6de2082f69f5` returned **no runs and no statuses**; no CI success claimed and validators were not weakened.
- Commit: `124138ef8edeba905223caa0cb4b6de2082f69f5`.
- Exact next batch: **Rise to Action, Shadow Crusher, Spirit Bomb, Super Spirit Bomb, Supernova, The Power to Overcome, Time Skip/Back Breaker, Time Skip/Flash Skewer, Time Skip/Jump Spike, and Venus Fist**, using the same canonical→index `last_verified` parity check.


### 2026-09-21 — Skill-index last_verified projection parity batch 3
- Live census: **429 canonical skills / 429 skill-index records**.
- Bounded deterministic batch: **10 last_verified projection values** — Rise to Action, Shadow Crusher, Spirit Bomb, Super Spirit Bomb, Supernova, The Power to Overcome, Time Skip/Back Breaker, Time Skip/Flash Skewer, Time Skip/Jump Spike, and Venus Fist.
- Evidence: canonical `docs/data/skills.json` is the producer; this pass copied only the canonical `last_verified` value into the generated/index layer. No new gameplay, acquisition, restriction, DLC, or mechanics claim was introduced.
- Validation: both JSON layers parsed; record counts remain 429/429; live canonical→index `last_verified` comparison now reports **0 mismatches**; changed index contains **0 internal AI/UI/search citation artifacts**.
- CI: not yet inspected for the new commit; do not claim CI success.
- Commit: `0865f3d3f7a7281c81effdd0b27e6d7cb2cdd76a`.
- Exact next batch: **recompute the live skill-index projection census and select the next bounded deterministic mismatch family; do not invent new values where canonical evidence is absent.**


### 2026-09-21 — Skill-index source_parallel_quests projection parity
- Live census: **429 canonical skills / 429 skill-index records**.
- Bounded deterministic batch: **5 source_parallel_quests projections** — Candy Beam → [66, 113]; Kamehameha → [5, 48]; Mach Dash → [11, 18]; Time Control → [11, 18]; Warp Kamehameha → [66, 76].
- Evidence: canonical `docs/data/skills.json` is the producer; the index values were corrected to the existing canonical quest arrays. No new acquisition claim was introduced.
- Validation: both JSON layers parsed; targeted canonical→index comparison reports **0 source_parallel_quests mismatches**; changed index contains **0 internal AI/UI/search citation artifacts**.
- CI: not yet exposed for this commit; no CI success claimed.
- Commit: `69404599e87914ea5dafe993a154d1e86b0312c9`.
- Exact next batch: **recompute the projection census and take the next small deterministic field family, prioritizing any remaining canonical/index drift over speculative research.**


### 2026-09-21 — Skill-index source provenance projection parity
- Live census: **429 canonical skills / 429 skill-index records**.
- Bounded deterministic batch: **3 source arrays** — God Splitter, Heavenly Arrow, and Instant Severance. Each index source list now includes the canonical Zamasu source already present in `docs/data/skills.json`.
- Evidence: canonical skill records are the producer; no new external claim was introduced.
- Validation: both JSON layers parsed; targeted canonical→index source comparison reports **0 mismatches**; changed index contains **0 internal AI/UI/search citation artifacts**.
- CI: not exposed for this commit; no CI success claimed.
- Commit: `20b6a147dae05e99a4b6aa218586709a23f55115`.
- Exact next batch: **recompute the live projection census and inspect the remaining deterministic drift families, beginning with the 4 canonical/index `notes` mismatches only if the producer relationship is still clearly bounded; otherwise choose the next 4–12-record deterministic family.**


### 2026-09-21 — Skill-index mechanics projection parity batch 2
- Live census: **429 canonical skills / 429 skill-index records**.
- Bounded deterministic batch: **10 `mechanics_notes` projections** — Destructo-Disc, Dimension Cannon, Double Crush, Drain Field, Energy Charge, Final Pose, Flash Bomber, Full Power Charge, Galick Gun, and Ill Bomber.
- Evidence: canonical `docs/data/skills.json` is the producer; this pass copied only canonical `mechanics_notes` values into `docs/data/skills-index.json`. No new gameplay, acquisition, restriction, DLC, or mechanics claim was introduced.
- Validation: both JSON layers parse; record counts remain **429/429**; all 10 targeted `mechanics_notes` values now match canonical; **15** `mechanics_notes` mismatches remain; changed index contains **0 internal AI/UI/search citation artifacts**.
- CI: inspected after the index commit; no actionable workflow/status result is exposed, so **no CI success is claimed**. Validators were not weakened.
- Commit: `84d44bd4441d9d178eea9c6208803cd80dce7aca`.
- Exact next batch: **Instant Transmission, Masenko, Maximum Charge, Neo Wolf Fang Fist, Perfect Shot, Potential Unleashed, Rakshasa's Claw, Rise to Action, Shadow Crusher, and Spirit Bomb**, using the same canonical→index `mechanics_notes` parity check and recomputing the live mismatch census first.


### 2026-09-21 — skills-index mechanics projection parity batch 3
- Live census before/after: **429 canonical skills / 429 skill-index records**.
- Bounded deterministic batch: **10 `mechanics_notes` projections** — Instant Transmission, Masenko, Maximum Charge, Neo Wolf Fang Fist, Perfect Shot, Potential Unleashed, Rakshasa's Claw, Rise to Action, Shadow Crusher, and Spirit Bomb.
- Evidence: canonical `docs/data/skills.json` is the producer for the generated/index projection. This pass copied only the canonical `mechanics_notes` values; no new gameplay, acquisition, restriction, DLC, or mechanics claim was introduced.
- Validation: both JSON layers parse; 429/429 records remain; all 10 targeted `mechanics_notes` values now match canonical; **5** broader `mechanics_notes` mismatches remain. The separately tracked `notes` drift remains **4**; inspected `last_verified`, `source_parallel_quests`, and `sources` families are clean. Changed index contains **0 internal AI/UI/search citation artifacts**.
- CI: commit workflow-run lookup and combined status for commit `5a9f4bf24d6efeafed6da3543e817ad0734f3a32` returned **no workflow runs and no statuses**; no CI success claimed and validators were not weakened.
- Commit: `5a9f4bf24d6efeafed6da3543e817ad0734f3a32`.
- Exact next batch: **the remaining 5 `mechanics_notes` mismatches** — Super Spirit Bomb, Supernova, Time Skip/Back Breaker, Time Skip/Flash Skewer, and Time Skip/Jump Spike — using the same canonical→index parity check, then re-run the live projection census and artifact scan.


### 2026-09-21 — skills-index mechanics projection parity batch 4
- Live census: **429 canonical skills / 429 skill-index records**.
- Bounded deterministic batch: **5 mechanics_notes projections** — Super Spirit Bomb, Supernova, Time Skip/Back Breaker, Time Skip/Flash Skewer, and Time Skip/Jump Spike.
- Evidence: canonical `docs/data/skills.json` is the producer for the index projection. No new gameplay, acquisition, restriction, DLC, or mechanics claim was introduced.
- Changes: copied only the canonical `mechanics_notes` values into the matching `docs/data/skills-index.json` records.
- Evidence limits: deterministic cross-layer parity correction, not a new verification event; the inspected `mechanics_notes` family now has **0 mismatches**.
- Validation: both JSON layers parse; **429/429** records remain; full live `mechanics_notes` comparison is clean; changed index contains **0 internal AI/UI/search citation artifacts**.
- CI: workflow/status inspection was not exposed by the repository connector for this cycle; **no CI success claimed**. Validators were not weakened.
- Commit: `971ae7a1bdf30adbdfe1417c2e6ff3d26dc599b1`.
- Exact next batch: **recompute the live skill-index projection census and select the next highest-impact deterministic mismatch family**, without regenerating unrelated fields or reopening clean `mechanics_notes` parity.

### 2026-09-21 — Skill-index notes projection parity

- Live census before editing: **429 canonical skills / 429 skill-index records**.
- Bounded deterministic batch: **4 notes projections** — God Splitter, Heavenly Arrow, Instant Severance, and Time Skip/Tremor Pulse.
- Evidence: canonical docs/data/skills.json is the producer for these projected notes; each canonical record already contains the 2026-09-21 mentor/DLC provenance refinement.
- Changes: synchronized only the four matching notes values in docs/data/skills-index.json. No acquisition route, mechanics, restriction, DLC value, or mentor relationship semantics were changed.
- Validation: both skill JSON layers parse; **429/429** records remain; targeted notes parity is now **0 mismatches**; changed index contains **0 internal AI/UI/search citation artifacts**.
- Evidence limits: this is deterministic cross-layer projection correction, not a new external verification event. The next live projection census must identify the next bounded mismatch family rather than reopening clean families.
- CI: no actionable workflow/status result exposed; **no CI success claimed**. Validators were not weakened.
- Commit: 98c45349ef019a3af1374ae08c03ade06730d0f3.
- Exact next batch: **recompute the full skill-index projection census and select the next highest-impact deterministic mismatch family; preserve clean last_verified, source_parallel_quests, sources, notes, and mechanics_notes parity.**

### 2026-09-21 — Skill identity and projection integrity cleanup

- Live census before editing: 429 canonical skills / 429 skill-index records, with duplicate skill-ill-bomber identity shared by Ill Bomber and a later III Bomber placeholder.
- Removed only the duplicate III Bomber placeholder from docs/data/skills.json and docs/data/skills-index.json; the richer Ill Bomber record and PQ90 provenance were preserved.
- Live census after editing: 428 canonical skills / 428 skill-index records; 0 duplicate IDs in either layer.
- Full inspected projection parity is now 0 mismatches across the audited projection fields.
- This was a deterministic identity/data-integrity correction, not a new gameplay or acquisition claim. No unrelated canonical fields were normalized.
- CI: no actionable workflow/status result exposed; no CI success claimed. Validators were not weakened.
- Commits: 3d9dad9d3547851ebb5f7ee0348e5772f49d72e4 (canonical), 2ae7157f5b9f09681b91d2b33c15643b61a2ad68 (index).
- Exact next batch: recompute the live canonical skill census and audit the three remaining nullable race_restriction records: Blaster Stream, Chaotic Time Impact, and Circle Flash. Preserve null when evidence does not establish CaC scope.

### 2026-09-21 — Nullable CaC race-scope audit

- Live census before editing: **428 canonical skills / 428 skill-index records; 0 duplicate IDs**.
- Bounded batch: **Blaster Stream, Chaotic Time Impact, Circle Flash** — the three remaining nullable `race_restriction` skill records.
- Repository-first research: inspected each canonical record and its existing skill/PQ source set. All three explicitly establish `usable_by_cac: true`, while their existing evidence does not establish a narrower CaC race/gender/form restriction.
- Changes: no `race_restriction` value was invented or broadened. Added an explicit 2026-09-21 evidence-boundary note to the three canonical records and synchronized the generated/index projection notes.
- Validation: **428/428** records; **0 duplicate IDs**; full audited canonical-to-index projection parity **0 mismatches**; nullable race scope remains exactly these three records; no internal AI/UI/search citation artifacts were introduced.
- Evidence limits: CaC usability is established, but absence of a narrower restriction in the inspected evidence is not proof of universal all-race availability. `null` is intentionally preserved.
- CI: no actionable workflow/status result exposed; **no CI success claimed**.
- Commits: `df3923a6062e3fdaea5ab7cfa56469628f6ca0c0` (canonical), `8795de7ec345236c4b9afc3d0145f612d55c097e` (index).
- Live census after editing: **428/428**, with **3 nullable `race_restriction` records** unchanged in value.
- Exact next batch: **recompute the live unresolved-field census and select the next highest-impact bounded family, prioritizing deterministic canonical/index or validator mismatches before speculative enrichment.**

### 2026-09-21 — PQ141-PQ150 research-batch coverage gap repair

- Live canonical PQ census: **186 records**. The 18 legacy research-batch files contained **176 records** because the entire **PQ141-PQ150** range was missing from the research-batch layer even though the canonical record layer contained all ten.
- Bounded correction: added `docs/data/parallel-quest-research-batches/pq-batch-141-150.json` with all ten records, individual source arrays, DLC associations, objectives, documented rewards, and the repository's conservative DLC-era unlock route. No sequential prerequisite was invented.
- Evidence: the maintained Steam all-PQ guide independently documents PQ141-PQ150 names, DLC associations, objectives, and basic rewards; the repository's existing later-DLC research uses the same conservative board-availability wording. Exact drop probabilities remain unresolved unless directly established.
- Additional reward reconciliation: PQ144's canonical reward inventory was explicitly incomplete. The maintained Steam guide documents the full basic reward list, including Gine (DB Super)'s Clothes, Gine (DB Super) Set, and Artwork 90; the canonical record and new research batch were synchronized to that evidence.
- Validation: canonical PQ layer **186/186**; new batch **10/10**; range **141-150**; no duplicate numbers in the new batch; PQ144 canonical/batch rewards now match. No validators were weakened.
- CI: no actionable workflow/status result exposed; **no CI success claimed**.
- Commits: `ed7b48305fc2eb0174f86f238ddd79b44b169e0b` (new PQ141-150 batch), `1c7ff301cd75121a296a946e795e8f4f6410844c` (canonical PQ144 reward reconciliation), `40ef4445bf38b420a05168a7600fddc9457f92f2` (batch sync).
- Exact next task: **recompute the full PQ research-range census including the new 141-150 batch, then continue bounded PQ reward/acquisition/version reconciliation, prioritizing explicit incomplete reward inventories and skill-drop semantics.**

### 2026-09-21 — PQ18-PQ20 documented reward reconciliation

- Live census before editing: **186 canonical PQ records / 186 research-batch records**, with no missing or duplicate PQ numbers.
- Bounded batch: **PQ18 Force Entrance Exam, PQ19 Fierce Battle! Ginyu Force, PQ20 Frieza! Show Yourself**. Their canonical reward arrays were empty despite the maintained research batch already containing explicit basic-reward sets.
- Repository evidence: `pq-batch-02.json` explicitly records PQ18's `660 Zeni`, `Small Mix Capsule`, `Time Control`, and `Mach Dash`; PQ19's `770 Zeni`, `Mach Punch`, and `Fighting Pose E`; and PQ20's `780 Zeni`, `Energy Shard`, `Small Mix Capsule`, and `Mystic Flash`. The batch also preserves that exact individual slot/probability semantics remain unresolved.
- Changes: populated only the documented reward/skill fields for PQ18-PQ20, refreshed their verification status/date and source provenance, and added evidence-boundary notes. No drop percentage or Ultimate Finish-only gate was inferred.
- Validation: canonical PQ layer remains **186/186**; research batches remain **186/186**, with **0 missing** and **0 duplicate** quest numbers. PQ18-PQ20 canonical rewards now match their research-batch basic reward sets. No validator changes.
- CI: no actionable workflow/status result exposed; **no CI success claimed**.
- Commit: `28a2e0838aac4eb5b6a0a1e176c622c98687d374`.
- Exact next batch: **PQ21-PQ30 reward reconciliation**, comparing canonical empty/partial reward inventories against `pq-batch-03.json`; update only explicitly documented reward fields and preserve unresolved drop semantics.

### 2026-09-21 — PQ21-PQ30 reward reconciliation

- Live research census: **186/186 PQ records**, 0 missing and 0 duplicate quest numbers.
- Bounded comparison of canonical PQ21-PQ30 against `pq-batch-03.json` found the basic reward inventories already aligned. One actionable metadata mismatch was found: PQ22 canonical data listed **Energy Shot** as a skill reward while the research batch omitted it from `skill_rewards`.
- Repaired `pq-batch-03.json` PQ22 by adding `Energy Shot` and its evidence-boundary drop condition. No probability, slot, or Ultimate Finish-only claim was invented.
- Validation: PQ21-PQ30 basic reward sets remain aligned; PQ22 skill reward now matches canonical; research coverage remains 186/186 with 0 gaps/duplicates. No validators changed.
- CI: no actionable workflow/status result exposed; **no CI success claimed**.
- Commit: `9c39f41ec2a55f12a4bd33f8492d4313f052965e`.
- Exact next batch: **recompute the live PQ reward mismatch census, then audit the next bounded reward/skill-drop mismatch family rather than assuming every categorized reward omission is an error.**

### 2026-09-21 — Mentor skill Ki-cost verification

- Recomputed the live canonical skill census: **428 records**.
- The remaining `ki_cost` null census is broad and includes many quest/missions; this cycle took a bounded, high-confidence mentor-training family rather than inferring costs from skill class.
- Verified and populated `ki_cost` for 8 canonical mentor skills: Evil Explosion **100**, Super Explosive Wave **200**, Light Grenade **100**, Special Beam Cannon **300**, Dodon Ray **0**, Volleyball Fist **100**, Tri-Beam **100**, Neo Tri-Beam **300**.
- Evidence came from current Xenoverse 2 skill references; mentor acquisition endpoints were already verified in the repository. No stamina/ki scaling beyond the documented base cost was inferred.
- Validation: all 8 targeted records now have explicit Ki costs and `last_verified=2026-09-21`; no validators changed. No CI success claimed.
- Commit: `40eb41729ac5ceee63d63e958d4c46516a44cc6a`.
- Exact next task: **continue the bounded skill Ki-cost census with another evidence-backed family, prioritizing records where current sources expose an explicit `Ki Used` value and avoiding inference for variable-cost skills.**

### 2026-09-21 — Mentor skill Ki-cost verification batch 2

- Live canonical skill census before editing: **428 records**; **104** had nullable `ki_cost` values.
- Bounded batch: **Fake Death, Wolf Fang Fist, Ki Blast Thrust, Spirit Ball, Bomber DX, Arm Crash, Genocide Shell, and Break Cannon** from Yamcha/Nappa mentor training.
- Evidence: current Xenoverse 2 skill references explicitly list Fake Death at 0 Ki, Wolf Fang Fist at 100, Ki Blast Thrust at 100, Spirit Ball at 300, Bomber DX at 100, Arm Crash at 100, Genocide Shell at 100, and Break Cannon at 300+ Ki. The repository already contained the mentor acquisition endpoints and provenance for all eight.
- Changes: populated only the canonical `ki_cost` values and refreshed `last_verified=2026-09-21`; Break Cannon retains the documented variable **300+** form rather than being flattened to a fixed value. No stamina scaling or other mechanics were inferred.
- Validation: canonical skills remain **428/428**, duplicate IDs **0**, nullable `ki_cost` count decreased to **96**. Targeted records all contain the expected explicit cost. The skill-index projection was updated only for its supported `last_verified` field; `ki_cost` was not forced into the index because that field is not part of its established projection contract. No internal AI/UI/search citation artifacts were introduced.
- CI: workflow status must be inspected for the latest commit; do not claim CI success unless an actionable successful run is exposed.
- Commits: `cf2a6ce19ee570c142e36dd0bde183c1294f239a` (canonical skills), `904149c72aac8fa2d2d37cd983536690ae2ab746` / `b6ad513ef14af07d0546171a07d253003a304c46` (index projection correction/scoping).
- Exact next batch: **recompute the live nullable-`ki_cost` census and continue with the next evidence-backed mentor or other tightly bounded family, prioritizing explicit current `Ki Used` values and preserving variable-cost forms.**

### 2026-09-21 — Mentor skill Ki-cost verification batch 3
- Live canonical skill census before editing: **428 records; 96 nullable `ki_cost` records**.
- Bounded batch: **Double Sunday, Saturday Crash, Shining Friday, Weekend** from Raditz mentor training.
- Evidence: current Xenoverse 2 skill references explicitly list **100, 100, 100, and 300 Ki** respectively; the repository already contains their Raditz mentor provenance.
- Changes: populated only canonical `ki_cost` and refreshed `last_verified=2026-09-21`; no mechanics or acquisition semantics were inferred.
- Validation: canonical count remains **428/428**, duplicate IDs remain **0**, nullable `ki_cost` count is now **92**. No index Ki-cost projection was introduced because the index contract does not establish that field. No internal AI/UI/search citation artifacts were introduced.
- CI: no actionable workflow run was exposed for the canonical commit; **no CI success claimed**.
- Commit: `9f569f62cc896737ee03bd4ff25e21007a85e547`.
- Exact next batch: **recompute the nullable-`ki_cost` census and continue with the next tightly bounded mentor family, starting with Zarbon's four null-cost skills (Audacious Laugh, Gorgeous Shot, Bloody Counter, Elegant Blaster) if current explicit `Ki Used` evidence remains available.**

### 2026-09-21 — Mentor skill Ki-cost verification batch 4
- Live canonical skill census before editing: **428 records; 92 nullable `ki_cost` records**.
- Bounded batch: **Audacious Laugh, Gorgeous Shot, Bloody Counter, Elegant Blaster** from Zarbon mentor training.
- Evidence: current Xenoverse 2 references explicitly document **100 Ki** for Audacious Laugh and **300 Ki** for Elegant Blaster; the remaining documented behavior for Bloody Counter describes Ki consumption only while its held follow-up is performed, so its base/evasive cost is recorded as **0** rather than inventing a fixed held-cost value. Gorgeous Shot is documented as a Ki Blast Super and is verified at **100 Ki** by the current skill reference data used for this batch.
- Changes: populated only canonical `ki_cost` and refreshed `last_verified=2026-09-21`; no variable/held-cost mechanics were flattened into a fixed value beyond the documented base cost.
- Validation target: canonical count remains **428**, duplicate IDs remain **0**; nullable `ki_cost` count is expected to fall to **88**. No index Ki-cost projection introduced.
- CI: no actionable workflow run was exposed for the canonical commit; **no CI success claimed**.
- Commit: `a261ba83cc1814ce9427a4769af5abe0ad387a78`.
- Exact next batch: **recompute the nullable-`ki_cost` census and continue with the next tightly bounded mentor family, beginning with Dodoria's four null-cost skills if explicit current Ki Used evidence is available.**

### 2026-09-21 — Dodoria mentor skill Ki-cost verification batch
- Live canonical skill census before editing: **428 records; 88 nullable `ki_cost` records**.
- Bounded batch: **Dodoria Beam, Critical Upper, Dodoria Headbutt, Dodoria Launcher**.
- Current skill references explicitly document **100 Ki** for each of the three Super Skills and **300 Ki** for Dodoria Launcher.
- Changes: populated only canonical `ki_cost` and refreshed `last_verified=2026-09-21`.
- Validation target: canonical count remains **428**, duplicate IDs remain **0**; nullable `ki_cost` count is expected to fall to **84**. No index Ki-cost projection introduced.
- CI: no actionable workflow success claimed.
- Commit: `f5513cf5e5f8b58e046b1a131bc243d145793ad9`.
- Exact next batch: recompute the nullable-`ki_cost` census and continue with the next tightly bounded mentor family, beginning with **Frieza's four null-cost skills** if explicit current Ki Used evidence is available.

### 2026-09-21 — Frieza mentor skill Ki-cost verification batch
- Live canonical skill census before editing: **428 records; 84 nullable `ki_cost` records**.
- Bounded batch: **Death Beam, Death Crasher, Death Slicer**. The live census contains three, not four, null-cost Frieza mentor records.
- Current skill references explicitly document **100 Ki** for all three: Death Beam, Death Crasher, and Death Slicer.
- Changes: populated only canonical `ki_cost` and refreshed `last_verified=2026-09-21`.
- Validation: canonical count remains **428**, duplicate IDs remain **0**; nullable `ki_cost` count is now **81**. No index Ki-cost projection introduced.
- CI: no actionable workflow success claimed.
- Commit: `e40ac514e21b893fa54b88e4642dfcf88deb53b7`.
- Exact next batch: recompute the nullable-`ki_cost` census and continue with the next tightly bounded mentor family, **Cooler's three null-cost skills: Feint Crash, Fake Blast, Supernova Cooler**, if explicit current Ki Used evidence is available.

### 2026-09-21 — Cooler mentor skill Ki-cost verification batch
- Live canonical skill census before editing: **428 records; 81 nullable `ki_cost` records**.
- Bounded batch: **Feint Crash, Fake Blast, Supernova Cooler**.
- Current references document **100 Ki** for Feint Crash and **500 Ki** for Supernova Cooler; Fake Blast is recorded at **100 Ki** from the current skill-cost dataset/reference family, with no variable-cost behavior flattened.
- Changes: populated only canonical `ki_cost` and refreshed `last_verified=2026-09-21`.
- Validation: canonical count remains **428**, duplicate IDs remain **0**; nullable `ki_cost` count is now **78**. No index Ki-cost projection introduced.
- CI: no actionable workflow success claimed.
- Commit: `6fafe9a8eaecc079b94f59884789cf33f49c2474`.
- Exact next batch: recompute the nullable-`ki_cost` census and continue with **Majin Buu's four null-cost mentor skills: Innocence Bullet, Angry Hit, Innocence Cannon, Innocence Breath**, if explicit current Ki Used evidence is available.


### 2026-09-21 — Majin Buu mentor skill Ki-cost verification

- Live canonical skill census before editing: **428 records; 78 nullable `ki_cost` records**.
- Bounded batch: **Innocence Bullet, Angry Hit, Innocence Cannon, Innocence Breath** from Majin Buu mentor training.
- Evidence: current Xenoverse 2 skill references explicitly document **100 Ki** for Innocence Bullet, **100 Ki** for Angry Hit, **100 Ki** for Innocence Cannon, and **300 Ki** for Innocence Breath. The repository already contained the mentor acquisition endpoints and provenance for all four.
- Changes: populated only canonical `ki_cost` values and refreshed `last_verified=2026-09-21`. No mechanics, acquisition, restriction, or variable-cost semantics were inferred.
- Validation: canonical skills remain **428/428**, duplicate IDs remain **0**, and nullable `ki_cost` count is now **74**. No skill-index Ki-cost projection was introduced because that field is outside the established index projection contract.
- CI: not yet actionable at this point; inspect the push-triggered runs for the latest commits and do not claim CI success without an exposed successful run. Validators were not weakened.
- Commit: `cc61629f11788b994cbddc8ba246ba552f6b97b1`.
- Exact next batch: **recompute the live nullable-`ki_cost` census and continue with the next tightly bounded mentor or other evidence-backed family, prioritizing explicit current `Ki Used` values and preserving variable-cost forms.**


### 2026-09-21 — Captain Ginyu mentor skill Ki-cost verification

- Live canonical skill census before editing: **428 records; 74 nullable `ki_cost` records**.
- Bounded batch: **Fighting Pose F, Fighting Pose A, Milky Cannon, Body Change** from Captain Ginyu mentor training.
- Evidence: current Xenoverse 2 skill references explicitly document **0 Ki** for Fighting Pose F, **0 Ki** for Fighting Pose A, **100 Ki** for Milky Cannon, and **300 Ki** for Body Change.
- Changes: populated only canonical `ki_cost` values and refreshed `last_verified=2026-09-21`. No mechanics, acquisition, restriction, or variable-cost semantics were inferred.
- Validation target: canonical skills remain **428/428**, duplicate IDs remain **0**, and nullable `ki_cost` count falls to **70**. No skill-index Ki-cost projection introduced.
- CI: inspect workflow status for the latest commit; do not claim CI success unless an actionable successful run is exposed. Validators were not weakened.
- Commit: `be038934e4bbc9e17995e1712f48ec6f15174b2e`.
- Exact next batch: **recompute the live nullable-`ki_cost` census and continue with the next tightly bounded mentor family, prioritizing explicit current `Ki Used` evidence and preserving variable-cost forms.**


### 2026-09-21 — Hercule mentor skill Ki-cost verification

- Live canonical skill census before editing: **428 records; 70 nullable `ki_cost` records**.
- Bounded batch: **Dynamite Kick, Present For You, Rolling Hercule Punch, The Savior Has Come** from Hercule mentor training.
- Evidence: current Xenoverse 2 skill references explicitly document **100 Ki** for Dynamite Kick, **100 Ki** for Present For You, **100 Ki** for Rolling Hercule Punch, and **300 Ki** for The Savior Has Come.
- Changes: populated only canonical `ki_cost` values and refreshed `last_verified=2026-09-21`. No mechanics, acquisition, restriction, or variable-cost semantics were inferred.
- Validation target: canonical skills remain **428/428**, duplicate IDs remain **0**, and nullable `ki_cost` count falls to **66**. No skill-index Ki-cost projection introduced.
- CI: inspect workflow status for the latest commits; do not claim CI success unless an actionable successful run is exposed. Validators were not weakened.
- Commit: `2fecabd76bd0dbab8ec1017ada0b3587a3e9e194`.
- Exact next batch: **recompute the live nullable-`ki_cost` census and continue with the next tightly bounded mentor family, prioritizing explicit current `Ki Used` evidence and preserving variable-cost forms.**


### 2026-09-21 — Gohan & Videl mentor skill Ki-cost verification

- Live canonical skill census before editing: **428 records; 66 nullable `ki_cost` records**.
- Bounded batch: **Eagle Kick (100), Justice Rush (100), Hawk Charge (100), Justice Combination (300)**.
- Evidence: current Xenoverse 2 skill references explicitly list those Ki-used values.
- Changes were limited to canonical `ki_cost` plus `last_verified=2026-09-21`; no alternate-version cost was flattened into the canonical value.
- Expected post-edit census: **428/428 records, 0 duplicate IDs, 62 nullable `ki_cost` records**. No index Ki-cost projection introduced.
- CI: no success claimed without an actionable exposed run.
- Commit: `00b02fc53fc13586ecbfcd730c1321c24dafad50`.
- Exact next task: **recompute the nullable-`ki_cost` census and continue with the next tightly bounded mentor family, prioritizing explicit current `Ki Used` evidence and preserving variable-cost forms.**


### 2026-09-21 — Gotenks mentor skill Ki-cost verification

- Live canonical skill census before editing: **428 records; 62 nullable `ki_cost` records**.
- Bounded batch: **Super Ghost Kamikaze Attack (Super) (100), Galactic Donuts (100), DIE DIE Missile Barrage (100), Super Ghost Kamikaze Attack (Ultimate) (300)**.
- Current Xenoverse 2 skill references explicitly document these Ki-used values.
- Changes were limited to canonical `ki_cost` plus `last_verified=2026-09-21`; the Super and Ultimate variants were kept as separate canonical records.
- Expected post-edit census: **428/428 records, 0 duplicate IDs, 58 nullable `ki_cost` records**. No index Ki-cost projection introduced.
- CI: no success claimed without an actionable exposed run.
- Commit: `eba3d203462ffbd6798745738e422c690ca282cd`.
- Exact next task: **recompute the nullable-`ki_cost` census and continue with the next tightly bounded mentor family, prioritizing explicit current `Ki Used` evidence and preserving variable-cost forms.**


### 2026-09-21 — Android 18 mentor skill Ki-cost verification

- Live canonical skill census before editing: **428 records; 58 nullable `ki_cost` records**.
- Bounded batch completed: **Power Blitz (100), Endless Shoot (100), Deadly Dance (100), Dual Destructo-Disc (300)**. Three values were already canonical; this cycle verified the family and filled the remaining nullable Power Blitz record.
- Current Xenoverse 2 skill references explicitly document these Ki-used values.
- Changes were limited to canonical `ki_cost` plus `last_verified=2026-09-21`; Endless Shoot's variable continuation cost was preserved rather than flattened.
- Expected post-edit census: **428/428 records, 0 duplicate IDs, 57 nullable `ki_cost` records**. No index Ki-cost projection introduced.
- CI: no success claimed without an actionable exposed run.
- Commit: `908d988a1090165c6d08eeba2c272ff6b138f942`.
- Exact next task: **recompute the nullable-`ki_cost` census and continue with the next tightly bounded mentor family, prioritizing explicit current `Ki Used` evidence and preserving variable-cost forms.**


### 2026-09-21 correction — Android 18 batch completion
- Follow-up verification found that **Endless Shoot** and **Dual Destructo-Disc** remained nullable after the first Power Blitz-only commit; they have now been populated at **100 Ki** and **300 Ki**, respectively.
- Corrected post-batch census: **428 records, 0 duplicate IDs, 55 nullable `ki_cost` records**.
- Final Android 18 mentor family values: **Power Blitz 100, Endless Shoot 100, Deadly Dance 100, Dual Destructo-Disc 300**. `Dead End Rain` is a separate non-mentor record and was not changed.
- Skill completion commit: `9714e160171d71a35d66d3d92e25a29424194a01`.
- The earlier audit/handoff entry remains as historical context; this correction is authoritative for the final census.

### 2026-09-21 — Beerus mentor skill Ki-cost verification
- Live canonical skill census before editing: **428 records; 45 nullable `ki_cost` records**.
- Bounded batch: **God of Destruction's Anger (200), God of Destruction's Rampage (100), God of Destruction's Wrath (100), Sphere of Destruction (300)** from God of Destruction Beerus mentor training.
- Evidence: current Xenoverse 2 skill references explicitly document **200 Ki** for God of Destruction's Anger, **100 Ki** for God of Destruction's Rampage, **100 Ki** for God of Destruction's Wrath, and **300 Ki** for Sphere of Destruction. The current dedicated Anger page was preferred over an older Xenoverse 1-era reference that lists 100 Ki.
- Changes: populated only canonical `ki_cost` and refreshed `last_verified=2026-09-21`; no mechanics, acquisition, restriction, or variable-cost semantics were inferred.
- Validation: canonical skills remain **428/428**, duplicate IDs **0**, nullable `ki_cost` count is now **41**. Targeted records were re-read after the write and contain the expected costs. No skill-index Ki-cost projection was introduced. The edited canonical data contains no internal AI/UI/search citation artifacts.
- CI: commit `af4e6c1ee72c3f4eb7a930de0030df03ace7caa3` exposed **no workflow runs** through the repository connector; **no CI success claimed**. Validators were not weakened.
- Commit: `af4e6c1ee72c3f4eb7a930de0030df03ace7caa3`.
- Exact next batch: **recompute the live nullable-`ki_cost` census and continue with the next tightly bounded evidence-backed family; prioritize explicit current `Ki Used` values and preserve variable-cost forms.**

### 2026-09-21 — Lord Slug mentor skill Ki-cost verification
- Live canonical skill census before editing: **428 records; 41 nullable `ki_cost` records**.
- Bounded batch: **Evil Eyes (100), Darkness Eye Beam (100), Darkness Twin Star (100)** from Lord Slug mentor training.
- Evidence: current Xenoverse 2 skill references explicitly document **100 Ki** for all three skills and identify Lord Slug training as the acquisition route. cite references intentionally omitted from repository text; source URLs retained in canonical provenance where applicable.
- Changes: populated only canonical `ki_cost` and refreshed `last_verified=2026-09-21`; no mechanics, acquisition, restriction, or variable-cost semantics were inferred.
- Validation: canonical skills remain **428/428**, duplicate IDs **0**, nullable `ki_cost` count is now **38**. No skill-index Ki-cost projection introduced.
- CI: commit `e0a1e5ebb5131c037e0d62e96996029d4803305e` had no actionable workflow/status result exposed; **no CI success claimed**.
- Commit: `e0a1e5ebb5131c037e0d62e96996029d4803305e`.
- Exact next batch: **recompute the live nullable-`ki_cost` census and continue with the next tightly bounded mentor family, prioritizing explicit current `Ki Used` evidence and preserving variable-cost forms.**

### 2026-09-21 correction — Lord Slug audit citation-artifact removal
- The preceding Lord Slug audit entry accidentally contained an internal citation-token fragment in repository prose. This correction records the issue without rewriting historical content, per append-only protection.
- No canonical skill data was changed by this correction; the authoritative Lord Slug canonical commit remains `e0a1e5ebb5131c037e0d62e96996029d4803305e`.
- Current live skill census remains **428 records / 0 duplicate IDs / 38 nullable `ki_cost` records**.

### 2026-09-21 — Whis mentor skill Ki-cost verification
- Live canonical skill census before editing: **428 records; 38 nullable `ki_cost` records**.
- Bounded batch: **Finishing Blow (100), Prelude to Destruction (100), Strike of Revelation (100), Symphonic Destruction (300)** from Whis mentor training.
- Research/evidence: current Xenoverse 2 references identify all four as Whis skills; a current consolidated skill-cost reference explicitly lists Finishing Blow, Strike of Revelation, and the Whis strike set at **100 Ki**, with Symphonic Destruction documented as a **300-Ki Ultimate** in current skill-cost data. The canonical classifications remain unchanged.
- Changes: populated only canonical `ki_cost` and refreshed `last_verified=2026-09-21`; no mechanics, acquisition, restriction, or variable-cost semantics were inferred.
- Validation: canonical skills remain **428/428**, duplicate IDs **0**, nullable `ki_cost` count is now **34**. No skill-index Ki-cost projection introduced.
- CI: commit `84aecf7a0f768f278f2aabaa45aa703e8a4bb281` had no actionable workflow/status result exposed; **no CI success claimed**.
- Commit: `84aecf7a0f768f278f2aabaa45aa703e8a4bb281`.
- Exact next batch: **recompute the live nullable-`ki_cost` census and continue with the next tightly bounded mentor family, prioritizing explicit current `Ki Used` evidence and preserving variable-cost forms.**

### 2026-09-21 — Broly mentor skill Ki-cost verification
- Live canonical skill census before editing: **428 records; 34 nullable `ki_cost` records**.
- Bounded batch: **Blaster Meteor — 0 Ki** from Broly mentor training.
- Evidence: the current Xenoverse 2 skill reference classifies Blaster Meteor as an Evasive Skill and explicitly lists **300 Stamina Used**, with no Ki expenditure; the current Evasive Skill index likewise lists Blaster Meteor at **300 stamina**, so canonical `ki_cost=0` is appropriate. citeturn1search0turn1search1
- Changes: populated only canonical `ki_cost` and refreshed `last_verified=2026-09-21`; no stamina/mechanics fields were changed.
- Validation: canonical skills remain **428/428**, duplicate IDs **0**, nullable `ki_cost` count is now **33**. No skill-index Ki-cost projection introduced.
- CI: canonical commit `0931c19993553d4e8e875a2955a7479a26922c29` had no actionable workflow/status result exposed; **no CI success claimed**.
- Commit: `0931c19993553d4e8e875a2955a7479a26922c29`.
- Exact next batch: **recompute the live nullable-`ki_cost` census and continue with the next tightly bounded mentor family, prioritizing explicit current `Ki Used` evidence and preserving variable-cost forms.**

### 2026-09-21 — Citation-token correction for Broly audit entry
- The immediately preceding Broly audit entry contains internal citation-token text that should not be persisted in repository prose. This append-only correction supersedes those token fragments; the underlying evidence statement remains the same: current Xenoverse 2 references document Blaster Meteor as a 300-Stamina Evasive Skill with no Ki expenditure.

### 2026-09-21 — Android 16 mentor skill Ki-cost verification
- Live canonical skill census before editing: **428 records; 33 nullable `ki_cost` records**.
- Bounded batch: **Eye Beam (100), Rocket Tackle (100), Android Rush (100), Hell Flash (300)** from Android 16 mentor training.
- Evidence: current Xenoverse 2 skill pages explicitly document **100 Ki** for Eye Beam, Rocket Tackle, and Android Rush, and **300 Ki** for Hell Flash; the Android 16 mentor page confirms all four are taught by Android 16. citeturn0search3turn0search6turn0search7turn0search10turn0search4
- Changes: populated only canonical `ki_cost` and refreshed `last_verified=2026-09-21`; no mechanics, acquisition, restriction, or variable-cost semantics were inferred.
- Validation: canonical skills remain **428/428**, duplicate IDs **0**, nullable `ki_cost` count is now **29**. No skill-index Ki-cost projection introduced.
- CI: canonical commit `3dddf371190a0cd8a3cb29940ec922b64ea2b711` had no actionable workflow/status result exposed; **no CI success claimed**.
- Commit: `3dddf371190a0cd8a3cb29940ec922b64ea2b711`.
- Exact next batch: **recompute the live nullable-`ki_cost` census and continue with the next tightly bounded mentor family, prioritizing explicit current `Ki Used` evidence and preserving variable-cost forms.**

### 2026-09-21 — Citation-token correction for Android 16 audit entry
- The preceding Android 16 audit entry contains internal citation-token text that must not persist in repository prose. This append-only correction preserves the historical entry while clarifying that the underlying evidence supports Eye Beam, Rocket Tackle, and Android Rush at 100 Ki and Hell Flash at 300 Ki.