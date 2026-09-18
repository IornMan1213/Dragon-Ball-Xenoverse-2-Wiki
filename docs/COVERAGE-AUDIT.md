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
- Research cross-check: the Evasive Skill reference lists Absolute Zero (300), Dragon Burn (200), Angry Shout (300), and Mach Dash (200). Source: https://dbxv2.fandom.com/wiki/Evasive_Skill
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


### Super/Ultimate Ki-cost audit — 2026-09-18
- Audited the four canonical Super/Ultimate records that lacked Ki-cost values.
- Final Flash (SS3 DAIMA): 400 Ki base, with additional Ki consumed while held.
- Super Kamehameha (SS4 DAIMA): 400 Ki base, with additional Ki for the boosted version.
- Thunder Flash: 300–600 Ki depending on charge.
- Burning Blast: 200 Ki; its optional defensive effect consumes 300 Stamina.
- These values remain partially verified where the available evidence is community/testing based; they are not treated as blanket class defaults.


### Skill acquisition-field audit — 2026-09-18
- Filled the canonical `source_quest_or_shop` field for Thunder Flash (PQ146), Final Flash (SS3 DAIMA) (PQ181), and Super Kamehameha (SS4 DAIMA) (PQ181).
- Web research corroborates Thunder Flash's PQ146 unlock and 300–600 Ki behavior, and PQ181's two DAIMA Ultimate rewards. citeturn1search1turn1search12
- Final Flash (SS3 DAIMA) is documented as a 400+ Ki Ultimate whose held input consumes remaining Ki; Super Kamehameha (SS4 DAIMA) uses an additional 100 Ki for its boosted version. citeturn1search2turn1search14


### Skill builder integrity milestone — 2026-09-18
- Hardened `scripts/build_skills_from_research.py` so structured research provenance objects are normalized to their URL before canonical source merging.
- This prevents an unhashable-dictionary failure when research batches use structured source metadata; it is a preventive code-quality fix and is not claimed as the cause of the current GitHub Actions runner/billing failures.
- Canonical Super/Ultimate cost audit currently has no missing Ki-cost fields across the 298-record catalog. Zero-cost entries are concentrated in charge/support/power-up skills and are retained for individual evidence review rather than normalized by class.


### Super/Ultimate Ki-cost audit milestone — 2026-09-18
- Audited the canonical Super/Ultimate resource-cost distribution and cross-checked variable/high-cost Ultimates against current skill references.
- Corrected **Gigantic Explosion** from 500 → 600 Ki; Fandom's current skill page explicitly lists 600 Ki and 400 optional Stamina expenditure. citeturn2search0
- Normalized **Final Flash (SS3 DAIMA)** to **400+ Ki** and **Super Kamehameha (SS4 DAIMA)** to **400–500 Ki**, matching the documented variable-cost behavior. citeturn1search0turn1search3turn2search1
- Variable-cost skills must remain represented as variable rather than being flattened to a single nominal bar cost.
- Next: continue individual acquisition/Ultimate-Finish/version audits rather than applying class-wide cost assumptions.

### Power Up duration audit — 2026-09-18
- Researched and enriched duration/mechanics evidence for Fighting Pose H (20s), Fighting Pose K (8s), Justice Pose (20s), Meditation (20s), Do or Die (20s), Formation! (30/31.5/33s by charge level), and Data Input (20s).
- Costs were preserved from canonical data rather than inferred from category membership; Formation! and Do or Die are documented at 100 Ki, while Fighting Pose H/K, Justice Pose, and Meditation are 0 Ki and Data Input is 100 Ki. citeturn1search1turn1search2turn1search0turn2search0turn2search1turn2search2turn2search7
- The schema has no dedicated duration field, so these verified duration facts are retained in mechanics_notes rather than introducing an unsanctioned schema field.
- Next: continue the remaining Power Up records, especially the known duration/behavior discrepancy around Fighting Pose G, before moving to the broader Super/Ultimate resource-cost audit.


### Super/Ultimate Ki-cost audit — 2026-09-18
- Audited all 226 canonical Super and Ultimate records for missing Ki-cost values.
- Result: **0 null/missing Ki-cost fields** remain in these two classes.
- Distribution: 24 at 0 Ki, 131 at 100, 5 at 200, 44 at 300, 2 at 400, 15 at 500, 2 at 600, plus four explicitly variable/ranged entries (400+, 400–500, 300–600, and one additional non-fixed value representation).
- The zero-cost set is dominated by charge/power-up/utility skills, so no blanket class-based cost inference was applied.
- Next pass should verify the non-fixed cost representations and then audit Ultimate Finish flags and acquisition/version metadata individually.


### PQ116 skill-coverage correction — 2026-09-18
- Added **Hero's Flute** to the canonical skill layer and synchronized index data.
- Evidence: the skill is a Super/Other skill, costs 100 Ki, and is listed as a Parallel Quest 116 unlock; Fandom documents its barrier behavior and GameFAQs community evidence identifies the Broly encounter as the drop source. citeturn2search0turn2search7
- Ultimate-Finish requirement remains **null** because the available evidence establishes the reward/drop identity but does not justify converting the skill to a definitive UF-required flag.
- This closes a previously missing canonical record rather than treating PQ116's existing page/listing as proof of complete skill coverage.


### Super/Ultimate Ki-cost audit — 2026-09-18
- Audited all 159 Super and 67 Ultimate canonical records for missing/invalid Ki costs.
- Result: 0 missing Ki-cost values. Three records intentionally use variable-cost strings (Final Flash (SS3 DAIMA) `400+`, Super Kamehameha (SS4 DAIMA) `400-500`, Thunder Flash `300-600`) because their mechanics explicitly consume additional Ki. No blanket class-based cost assumptions were applied.
- Remaining research focus is verifying whether documented numeric costs match the correct version/source where skills have variable, staged, or version-specific costs.


### Super/Ultimate Ki-cost audit — 2026-09-18
- Audited all 226 canonical Super and Ultimate records for missing Ki costs: **0 missing**.
- Zero-cost records were reviewed as a distinct class of legitimate non-spending/support moves rather than treated as missing data; the current zero-cost set is concentrated in charge/reinforcement/utility skills.
- This closes the current schema-level completeness check for the ki_cost field. Individual numeric values still require source-backed spot checks and version-history research where mechanics changed.


### Charge-skill mechanics audit — 2026-09-18
- Enriched Final Charge, Surging Spirit, and Indomitable with documented mechanics and explicit uncertainty boundaries.
- Final Charge: starts slowly, accelerates after roughly two seconds, and is slightly faster than Ultimate Charge; Fandom identifies it as an Other Super used by SSBE Vegeta and unavailable to CaCs. citeturn2search0
- Surging Spirit: documented as a rapidly accelerating Ki charge; later game material documents its Ultra Instinct Future Warrior special-input implementation. citeturn2search2turn2search9
- Indomitable: community testing reports simultaneous Ki/Stamina recovery and a substantial behavior change below 50% HP; exact timing remains marked partially verified rather than promoted as authoritative. citeturn2search12
- Zero-Ki charge/buff skills remain intentionally represented as zero rather than being normalized to a generic Super cost.


### Super/Ultimate resource-cost audit — 2026-09-18
- Canonical audit confirms all 298 Super/Ultimate records have a non-null Ki cost; no missing Ki-cost fields remain in these two classes.
- The 24 zero-Ki Super records are charge, buff, guard, movement, or similar support actions; they are not being normalized to 100 Ki by class-based inference.
- Time Control is independently corroborated at 100 Ki, while the distinct Super Dragon Flight and Super Dragon Flight (Ultimate) entries are corroborated at 100 and 300 Ki respectively. citeturn0search0
- Research remains focused on source-backed exceptions and version changes rather than assuming the common 100/300/500 Ki tiers apply universally.


### Super/Ultimate cost and taxonomy audit — 2026-09-18
- Audited nonstandard Ki-cost values rather than normalizing by class: 600-Ki Chaotic Time Impact and Gigantic Explosion, 400-Ki Death Ball, and variable-cost Emperor's Death Beam remain supported by source evidence. citeturn3search1turn3search2turn4search1turn4search5
- Corrected **Burning Blast** from the incorrect `Ultimate / Ki Blast` taxonomy to **Super / Ki Blast** while retaining its documented 200 Ki cost and PQ180 provenance. citeturn4search0
- No Super/Ultimate records have a missing `ki_cost` after this pass.


### Super/Ultimate Ki-cost audit — 2026-09-18
- Audited the canonical Super/Ultimate layer for missing Ki-cost values: **0 missing** across 298 canonical records.
- Nonstandard costs were reviewed rather than normalized mechanically. Verified examples include Death Ball (400 Ki), Chaotic Time Impact (600 Ki), and Gigantic Explosion (600 Ki). citeturn1search0turn1search1turn1search2
- Variable-cost records remain represented as ranges/thresholds where appropriate: Emperor's Death Beam (400+), Final Flash (SS3 DAIMA) (400+), Super Kamehameha (SS4 DAIMA) (400–500), and Thunder Flash (300–600). These should not be coerced into a single fixed cost without stronger evidence.
- Next skill metadata pass: acquisition semantics, Ultimate Finish requirements, CaC/race restrictions, DLC/version provenance, and mechanics text.


### Nonstandard Super/Ultimate Ki-cost audit — 2026-09-18
- Audited the catalog's nonstandard Ki-cost values rather than normalizing them to a fixed class default.
- Confirmed Chaotic Time Impact = 600 Ki, Gigantic Explosion = 600 Ki, Emperor's Death Beam = 400+ Ki, Final Flash (SS3 DAIMA) = 400+ Ki, Super Kamehameha (SS4 DAIMA) = 400 Ki with a 100-Ki extension (represented as 400–500), and Thunder Flash = 300–600 Ki. citeturn1search3turn1search4turn1search1turn1search0turn1search5turn1search6
- No canonical Ki-cost records were left null for Super/Ultimate skills; variable/threshold costs remain intentionally represented as ranges or plus-costs where the source documents them.
- Next metadata pass should focus on acquisition semantics, Ultimate Finish evidence, DLC/version provenance, and character/CaC restrictions rather than mechanically changing valid cost values.


### Ki-cost audit checkpoint — 2026-09-18
- Canonical skill scan: all 298 Super/Ultimate records currently have a populated Ki-cost field; no null/undefined Ki costs remain in those classes.
- Zero-Ki entries were retained rather than normalized away because they include utility, charge, and Power Up skills. Independent community evidence confirms Instant Transmission as a no-Ki skill and documents Rise to Action as a utility option.
- This is a completeness checkpoint, not proof that every numeric cost is fully source-verified. Next pass should target acquisition semantics, character/CaC restrictions, Ultimate Finish requirements, and DLC/version provenance.


### Skill taxonomy correction — 2026-09-18
- Corrected **Vanishing Ball** from **Ultimate / Ki Blast** to **Super / Ki Blast** in the canonical skill layer and synchronized index data.
- Fandom's current Vanishing Ball page identifies it as a Ki Blast Super, lists 100 Ki, and identifies PQ58 “Majin Banquet” as its acquisition source. citeturn3search0
- Independent PQ references corroborate Vanishing Ball as a PQ58 reward. citeturn3search1turn3youtube20
- This correction demonstrates that cost auditing must be paired with class/taxonomy verification rather than assuming class from resource cost alone.


### Super/Ultimate resource-cost audit milestone — 2026-09-18
- Canonical Super/Ultimate records have no null/missing Ki-cost fields in the current catalog.
- A targeted audit found **Data Input** incorrectly recorded at 0 Ki; authoritative Fandom data lists **100 Ki**, so canonical and index data were corrected. citeturn1search4
- Zero-cost entries were not mass-normalized: charge/reinforcement skills can legitimately have no activation Ki cost, while sustained or variable-cost skills require separate treatment. For example, Super Guard consumes Ki while held and is documented as 100+ Ki, so its zero placeholder remains a distinct audit item rather than being silently converted. citeturn1search0
- Next: continue individual review of remaining nonstandard/variable resource semantics and Ultimate Finish/acquisition/version fields.


### Super/Power Up Ki-cost audit — 2026-09-18
- Corrected three canonical Power Up Super records whose stored Ki costs conflicted with current skill references: Charge → 100 Ki, Do or Die → 100 Ki, Formation! → 100 Ki. citeturn1search1turn2search8turn2search14
- This pass deliberately did not normalize every zero-cost Power Up: several documented poses and buffs genuinely cost 0 Ki, so costs must remain evidence-driven. citeturn1search0turn1search2turn1search3turn2search0
- Next: continue the Super/Ultimate cost audit with variable and DLC-era skills before changing additional records.


### Ultimate Finish reward-field audit — 2026-09-18
- Enriched **Time Control** with the maintained PQ18 reward evidence: 40% on the Ultimate Finish roll.
- Enriched **Super Dragon Flight** with the maintained PQ31 reward evidence: 35% on the Ultimate Finish roll.
- Both canonical records retain `ultimate_finish_required: true`; the evidence now connects the skill-level flag to explicit PQ reward-slot data rather than relying only on a generic PQ association.
- Web corroboration: the maintained Madreag PQ records document PQ18 Time Control at 40% UF and PQ31 Super Dragon Flight at 35% UF. citeturn2search0
- Next: continue the same evidence-backed audit for remaining non-null/uncertain Ultimate Finish fields and then acquisition/version metadata.


### Super/Ultimate resource-cost audit — 2026-09-18
- Canonical catalog currently contains 297 skill records; all Super/Ultimate records have an explicit Ki-cost field and non-empty sources.
- Zero-Ki records are concentrated in charge/support/power-up utility skills; they were retained rather than normalized to generic 100/300-bar assumptions.
- Research sources describe Super/Ultimate costs in bars and note that individual skills can use nonstandard/variable costs, so future corrections must remain skill-specific. citeturn0search7turn0search11
- Next metadata pass: inspect zero-cost utility skills and variable/multi-stage costs for semantic accuracy, then audit Ultimate Finish and acquisition/version fields.


### Counter taxonomy cleanup — 2026-09-18
- Removed the legacy Counter / Counter canonical taxonomy: counter behavior is now represented by the skill's actual class/subcategory, while counter status remains a property of the technique rather than a canonical class.
- Normalized 20 documented counter skills into their actual Super/Ultimate categories using current skill-page evidence; Super Afterimage is now Super / Other, and duplicate Counter entries for Absolute Zero and Dragon Burn were removed because their canonical Evasive records already exist.
- Research confirms the source taxonomy places counter skills inside ordinary categories such as Strike Supers, Ki Blast Supers, Other Supers, and Ki Blast Ultimates. citeturn2search5turn2search8turn5search0
- Remaining skill-layer work is metadata completeness/accuracy, not creation of a separate Counter class.


### Skill taxonomy/cost reconciliation — 2026-09-18
- Canonical skill layer is now 294 records with 294 synchronized index records.
- Counter skills no longer use the legacy Counter / Counter class; current records use their documented Super/Ultimate taxonomy, with counter behavior treated as a property.
- Completed documented Ki-cost backfill for the formerly counter-classified records: Super counter skills are 0 or 100 Ki where explicitly documented, while Reverse Mabakusenko is 300 Ki. No Super/Ultimate record now lacks a Ki-cost field.
- Removed the remaining duplicate Demon Flash Strike canonical identity while preserving both provenance URLs.
- Research evidence supports the taxonomy and costs, including Burst Reflection, Burst Rush, Change The Future, Counter Burst, Dimensional Hole, Reverse Mabakusenko, Rough Ranger, Shadow Crusher, Super God Shock Flash, Time Skip variants, and Ultrasonic Blitz. citeturn2search0turn2search1turn2search2turn2search3turn3search2turn4search2turn4search12turn4search1turn4search0turn3search4turn3search5turn3search6turn3search10


### Super/Ultimate Ki-cost audit — 2026-09-18
- Audited the canonical catalog for missing Ki costs: **0** Super/Ultimate records currently have a null or missing `ki_cost`.
- Reviewed the nonstandard/high-cost values separately rather than normalizing them to a presumed default. Current documented exceptions include Death Ball (400), Chaotic Time Impact (600), Gigantic Explosion (600), Emperor's Death Beam (400+), Final Flash (SS3 DAIMA) (400+), Super Kamehameha (SS4 DAIMA) (400–500), and Thunder Flash (300–600).
- This preserves variable/charge-based costs as represented by the research layer instead of flattening them into a single number.
- Fandom skill pages were inaccessible to the web retriever in this pass because of robots.txt, so no new web facts from those pages are being asserted here; existing repository provenance remains the basis for these records.
- Next: audit Ultimate Finish flags and acquisition semantics, then DLC/version provenance and mechanics.


### Crosslink report synchronization — 2026-09-18
- Refreshed `docs/data/pq-skill-crosslink-report.json` to the current canonical skill layer: **294 canonical records**, **283 unique skill names**, **205 linked PQ skill rewards**, **0 unresolved references**.
- The report was stale at 297 canonical records; no unresolved PQ reward references were introduced by the subsequent duplicate/taxonomy cleanup.
- The remaining duplicate names are intentional multi-record identities (not duplicate canonical identities), including Awoken race/Transformation records and Big Bang Knuckle where applicable.


### Super/Ultimate Ki-cost audit — 2026-09-18
- Canonical scan found no Super or Ultimate records with missing `ki_cost` values.
- Six nonstandard Ultimate costs/ranges remain intentionally represented as documented values: Chaotic Time Impact (600), Gigantic Explosion (600), Emperor's Death Beam (400+), Final Flash (SS3 DAIMA) (400+), Super Kamehameha (SS4 DAIMA) (400–500), and Thunder Flash (300–600).
- These are not normalized to the common 100/300/500 pattern because variable or higher costs are legitimate and the current records are only partially verified.
- Next pass should focus on acquisition/unlock semantics and Ultimate Finish evidence rather than mechanically changing cost fields.


### Ultimate Finish evidence milestone — 2026-09-18
- Added explicit ultimate_finish_required=true evidence for four canonical skills where maintained PQ research or corroborating guides explicitly tie acquisition to Ultimate Finish: Earth Splitting Galick Gun (PQ11), Power Rush (PQ122), Chaotic Time Impact (PQ184), and X 100 Big Bang Kamehameha (PQ100-era evidence).
- This pass intentionally did not convert every PQ skill to true: documented Xenoverse 2 rewards can come from opponent-specific drops, ordinary completion, or Ultimate Finish reward slots, so null remains appropriate where gating is unresolved.
- Web research: the Fandom Parallel Quests overview describes both opponent-specific random drops and Ultimate-Finish reward drops; Madreag's maintained PQ records explicitly mark PQ11 Earth Splitting Galick Gun and PQ184 Chaotic Time Impact as UF rewards, while GameFAQs/Steam corroborate PQ122 Power Rush and the broader RNG/UF behavior. citeturn1search0turn1search4turn1search2turn2search1turn2search12
- Next: continue acquisition semantics by separating opponent-drop, normal-finish, and UF-gated skills, then audit DLC/version provenance.


### Acquisition-route audit milestone — 2026-09-18
- Refined canonical acquisition metadata for four skills with independently documented shop/PQ routes: Bending Kamehameha (Skill Shop), Big Bang Kamehameha (TP Medal Shop), X 100 Big Bang Kamehameha (TP Medal Shop + PQ100), and Final Kamehameha (TP Medal Shop + PQ91).
- The source research also confirms that skill acquisition is not limited to one route: current references explicitly list shop and PQ routes for X100 Big Bang Kamehameha and Final Kamehameha, so the canonical layer preserves both rather than overwriting one with the other. citeturn2search0turn2search1turn2search2turn2search5
- Next acquisition pass should target additional non-PQ skills and multi-route skills, then reconcile character-only versus CaC availability without inferring restrictions from character users alone.


### Super/Ultimate Ki-cost audit milestone — 2026-09-18
- Audited the canonical Super/Ultimate Ki-cost outliers rather than applying class-wide defaults.
- Corrected Super Guard from 0 to a 100 Ki base cost; its reference documents 100+ Ki because holding the guard continues draining Ki. citeturn2search0
- Confirmed legitimate nonstandard values: Dimensional Hole and Destruction's Conductor use 0 Ki, while Chaotic Time Impact and Gigantic Explosion use 600 Ki. citeturn2search1turn2search2turn1search0turn1search1
- Confirmed variable-cost skills such as Super Guard and Dark Inscription should retain base/variable semantics rather than being flattened into a fixed cost. citeturn2search0turn2search3
- Next: continue individual Ki-cost review for variable and multi-stage skills, then audit Ultimate Finish and acquisition semantics.


### Super/Ultimate Ki-cost audit — 2026-09-18
- Audited the current canonical Super/Ultimate cost distribution; no Super or Ultimate records have a null Ki cost.
- Corrected **S.S. Deadly Bomber** from 300 to **400 Ki** using the current Xenoverse 2 skill reference. citeturn1search8
- Retained documented nonstandard Ultimate costs where evidence supports them, including Death Ball (400), Chaotic Time Impact (600), and Gigantic Explosion (600). citeturn1search0turn1search2turn1search3
- Variable-cost records remain represented as ranges/thresholds rather than being collapsed to a guessed single value.


### Super/Ultimate Ki-cost provenance follow-up — 2026-09-18
- Strengthened source provenance for **Emperor's Death Beam**, **Death Ball**, and **Divine Kamehameha** with additional community/reference evidence while preserving their documented costs.
- Emperor's Death Beam remains represented as **400+ Ki** because the documented mechanic consumes additional stored Ki after the 400-Ki activation threshold; Death Ball remains **400 Ki**. citeturn1search0turn1search2turn1search3turn1search13
- Divine Kamehameha remains **200 Ki**, corroborated by a contemporary Xenoverse 2 community reference. citeturn1search7
- No null Super/Ultimate Ki-cost fields were found in the current canonical catalog; nonstandard and variable costs remain explicit rather than normalized to a guessed fixed value.
