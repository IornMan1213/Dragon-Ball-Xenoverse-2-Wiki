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
- Current canonical/index files remain synchronized after the pass.
- Remaining work: preserve the already-complete Super/Ultimate Ki-cost coverage while moving the active audit frontier to acquisition semantics and individual mechanics.

### Current canonical validation checkpoint — 2026-09-18
- Canonical skills: **294** records.
- Skills index: **294** records.
- Duplicate canonical identities: **0**.
- Canonical/index ordering and identity keys: synchronized.
- Null Ki-cost fields among Super/Ultimate records: **0**.
- The repository currently differs from older 298-record milestone text elsewhere in this document; do not treat that historical count as the present catalog size without re-running the validation.
- The four Evasive corrections above are retained in the current canonical/index state.

### Super/Ultimate Ki-cost audit frontier — 2026-09-18
- Canonical catalog currently contains 298 skill records; an inspection found 84 Super/Ultimate records with null Ki cost.
- These nulls are concentrated in older category-sourced records and therefore represent a metadata backlog, not evidence that the skills cost 0 Ki.
- Current research sources support that Super/Ultimate costs vary by individual skill, so costs must be verified per skill rather than inferred from class (for example, published references describe Super skills as spanning multiple Ki-bar costs).
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
- External references confirm Energy Charge consumes no resources, while Instant Transmission is described as costing no Ki/Stamina; charge-skill references also identify the charge family separately from ordinary attacks.
- Remaining null-cost records require individual evidence review, especially newer DLC/Ultimate skills and skills whose costs may vary by stage or version.


### Super/Ultimate Ki-cost audit — 2026-09-18
- Verified and synchronized six researched costs: Crimson Edge 100, Divine Ray Bomb 300, Final Rampage 500, Dark Inscription 100, Emperor's Cannon 100, and Chaotic Time Impact 600.
- External references corroborate these values and the associated PQ acquisitions for the Future Saga skills.
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
- Time Control is independently corroborated at 100 Ki, while the distinct Super Dragon Flight and Super Dragon Flight (Ultimate) entries are corroborated at 100 and 300 Ki respectively.
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
- Research sources describe Super/Ultimate costs in bars and note that individual skills can use nonstandard/variable costs, so future corrections must remain skill-specific.
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


### Ultimate Finish requirement audit — 2026-09-18
- Audited the canonical skill layer's explicit `ultimate_finish_required` values alongside PQ reward evidence.
- The catalog currently has **6 explicit true flags** and **1 explicit false flag**; all other records remain null rather than being inferred.
- The five true flags are supported by PQ evidence: Earth Splitting Galick Gun (PQ11), Time Control (PQ18), Super Dragon Flight (PQ31), X 100 Big Bang Kamehameha (PQ100), Power Rush (PQ122), and Chaotic Time Impact (PQ184). The maintained PQ records distinguish Ultimate Finish reward slots from ordinary skill drops. citeturn3search0turn2search0turn2search1
- The explicit false flag on Spread Shot Retreat is retained as a documented non-UF acquisition case; no broad assumption that all PQ skills require Ultimate Finish is being introduced. citeturn2search1turn2search2
- Next: reconcile acquisition semantics at the individual reward-slot level (ordinary enemy drop vs UF-only reward vs post-quest roll) before expanding additional true/false flags.


### Super/Ultimate Ki-cost + PQ unlock-method milestone — 2026-09-18
- Audited all **179 Super** and **66 Ultimate** canonical records: no Super/Ultimate record currently has a null Ki-cost field.
- Preserved documented nonstandard/variable costs rather than normalizing them to a class default; examples include variable/threshold costs and 400–600 Ki Ultimates.
- Filled the missing `unlock_method` for five researched PQ Ultimates where the canonical record already identifies the source PQ: **Blaster Stream (PQ148), Full Power Destruction (PQ177), Gigantic Burst (PQ127), Lightning Impact (PQ142), and Requiem of Destruction (PQ106)**.
- Web references corroborate the PQ unlocks and costs for these records; Requiem's acquisition is additionally documented as DLC Super Pack 2 content. citeturn1search0turn1search1turn1search4turn1search14
- Remaining gap: many older canonical records still lack acquisition semantics even when their identity/cost is established. Research them individually rather than filling from class or character assumptions.


### Acquisition-method audit milestone — 2026-09-18
- Added evidence-backed acquisition semantics for 9 previously incomplete Super/Ultimate records: Burst Rush (PQ51 Ultimate Finish), Change The Future (PQ43 Ultimate Finish), God Breaker (PQ44), Dimensional Hole (PQ80), Flash Fist Crush (Shenron wish), Heroic Counter (PQ155), Punisher Shield (PQ129), Rough Ranger (PQ119 Ultimate Finish), and Demon Flash Strike (PQ160).
- The cited references document the corresponding PQ/wish acquisition routes; the distinction between ordinary PQ reward and Ultimate Finish remains explicit rather than treating all PQ skills as UF-only. citeturn1search0turn1search4turn1search1turn1search6turn1search10turn1search17turn1search8turn1search9
- Current Super/Ultimate Ki-cost coverage remains complete (no null Ki-cost fields). Acquisition coverage still has older records requiring individual research; no class-wide defaults are being inferred.


### Skill acquisition-method follow-up — 2026-09-18
- Added evidence-backed acquisition routes for **Burst Charge (PQ134)**, **Shield Barrier (PQ153)**, and **Ultimate Charge (PQ134)**.
- Current research confirms these are Parallel Quest rewards; costs and skill classifications remain separately represented.
- Hero's Flute (PQ116) and Power Impact (PQ120) were already present with acquisition metadata and were cross-checked during this pass. citeturn1search0turn1search1turn1search2turn1search8
- Remaining acquisition backlog is concentrated in older canonical records with missing route semantics; continue individually and preserve multi-route/UF distinctions.


### Core skill acquisition-method pass — 2026-09-18
- Added evidence-backed acquisition semantics for six previously incomplete core skills: **Kamehameha (PQ05)**, **Galick Gun (Vegeta training)**, **Masenko (Kid Gohan training)**, **Final Flash (Vegeta training)**, **Afterimage Strike (PQ81)**, and **Destructo-Disc (story progression)**.
- Sources distinguish mentor-training rewards from PQ rewards; Destructo-Disc is retained as a story-progression acquisition rather than being mislabeled as a PQ drop. citeturn1search1turn1search6turn1search7turn1search3turn1search5turn1search14
- Remaining acquisition gaps should continue to be researched individually, with multi-route and Ultimate-Finish distinctions preserved.


### Power Up Super duration audit — 2026-09-18
- Added documented duration metadata for Fighting Pose E (20s), Fighting Pose K (8s), Justice Pose (20s), and Meditation (20s).
- Research also confirms Fighting Pose G has race-dependent behavior: 25s for Male Saiyans versus 20s for Female Saiyans and other races, while its displayed base duration is 20s. This should remain represented as a mechanic/race exception rather than flattening it into a single universal value.
- The Power Up audit remains incomplete; additional skills should be checked individually for duration, cost, activation behavior, and race/version exceptions.


### Counter-skill acquisition pass — 2026-09-18
- Added an evidence-backed acquisition route for **Reverse Mabakusenko**: Skill Shop.
- The skill remains classified as **Ultimate / Ki Blast** and retains its counter behavior; acquisition was not inferred from its Counter taxonomy.
- Source evidence identifies it as a Skill Shop purchase for the Future Warrior. citeturn1search1turn1search0
- Continue counter-skill acquisition research individually; do not treat the Counter category as an acquisition source.


### Counter-skill acquisition audit — 2026-09-18
- Added evidence-backed acquisition routes for Burst Reflection (Dragon Ball wish), Counter Burst (PQ75), Counter Impact (PQ153), Shadow Crusher (Cooler training), Sudden Death Beam (TP/STP Medal Shops and Double Crystal Raid), Super God Shock Flash (Skill Shop), Time Skip/Back Breaker, Time Skip/Flash Skewer, and Time Skip/Jump Spike (Hit training), and Ultrasonic Blitz (PQ151).
- Counter taxonomy remains separate from acquisition semantics; no skill was assigned an acquisition route merely because it is categorized as a counter.
- Sources include the current Fandom skill pages and mentor/category references. citeturn2search0turn2search4turn2search5turn2search1turn2search3turn2search2turn3search1turn3search2turn3search3turn3search0
- Continue auditing the remaining counter skills and multi-route acquisition cases individually.


### Super/Ultimate resource-cost audit — 2026-09-18
- Audited all 245 canonical Super/Ultimate records for missing Ki costs: **0 missing**.
- Zero-cost entries are concentrated in charge/power-up style skills and are retained pending individual mechanics review; zero does not mean unverified.
- Nonstandard costs were reviewed rather than normalized blindly. Documented examples include Chaotic Time Impact (600), Gigantic Explosion (600), Death Ball (400), S.S. Deadly Bomber (400), Emperor's Death Beam (400+), Final Flash (SS3 DAIMA) (400+), Super Kamehameha (SS4 DAIMA) (400–500), and Thunder Flash (300–600). Sources/mechanics are preserved in the canonical records.
- This confirms the current catalog has complete Ki-cost field coverage for Super/Ultimate records, while exact historical/version-specific costs remain a targeted research concern.


### Evasive acquisition-route audit — 2026-09-18
- Filled documented acquisition routes for 8 previously incomplete Evasive records: Absolute Zero, Dragon Burn, Explosive Wave, Angry Shout, Energy Barrier, Punisher Guard, Final Pose, and Mach Dash.
- Sources distinguish PQ rewards, Skill Shop acquisition, and historical/name-change cases; the catalog preserves those distinctions instead of collapsing them into a generic “PQ reward” label. citeturn2search1turn1search8turn1search10turn1search2turn1search4turn2search0turn1search7turn1search3turn1search9
- Current Evasive layer now has no missing stamina costs and no missing acquisition routes among these 20 canonical Evasive records.


### Core acquisition-route pass — 2026-09-18
- Added sourced acquisition semantics for 12 additional skills with previously blank unlock routes: Super Afterimage, Divine Kamehameha, Perfect Shot, Spirit Bomb, Afterimage, Assault Vanish, Charged Ki Wave, Phantom Fist, Quick Sleep, Full Power Charge, Maximum Charge, and Instant Transmission.
- Evidence distinguishes Skill Shop, TP Medal Shop, mentor/training, Parallel Quest, and advancement-test routes rather than collapsing them into a generic source label. citeturn1search19turn1search7turn1search1turn1search14turn1search9turn1search2turn1search0turn2search11turn2search0turn2search5turn2search3turn2search2
- Final Charge remains intentionally unassigned an acquisition route in this pass because available evidence identifies it as a character-exclusive skill unavailable to CaCs; character-only availability is not the same as a player acquisition route. citeturn2search15turn2search10
- Next acquisition frontier: the remaining blank Super/Ultimate routes, especially character-exclusive, shop, mentor, and story/progression cases, audited individually.


### Ultimate acquisition-route pass — 2026-09-18
- Added sourced acquisition semantics for Final Explosion, Divine Lasso, Supernova, Super Spirit Bomb, and Victory Rush.
- Evidence covers TP/STP Medal Shop, Double Crystal Raid, Expert Mission, and Parallel Quest routes. Final Explosion is documented as TP Medal Shop; Divine Lasso as TP/STP Medal Shop plus Double Crystal Raid; Supernova as Expert Mission 6; Super Spirit Bomb as Expert Mission 16; Victory Rush as PQ89. citeturn1search1turn1search4turn2search0turn2search2turn1search3
- These routes are marked partially verified rather than treated as immutable across shop rotations, DLC/version history, or platform differences.
- Remaining acquisition frontier is 31 Super/Ultimate records with blank unlock routes; continue individually rather than inferring from class, user, or PQ proximity.


### Super/Ultimate Ki-cost audit — 2026-09-18
- Audited canonical Super and Ultimate records for missing Ki costs: **0 missing**.
- Nonstandard Ultimate costs were preserved rather than normalized away: Chaotic Time Impact (600), Death Ball (400), Emperor's Death Beam (400+), Final Flash (SS3 DAIMA) (400+), Gigantic Explosion (600), S.S. Deadly Bomber (400), Super Kamehameha (SS4 DAIMA) (400–500), and Thunder Flash (300–600).
- These values are supported by the current Ultimate Attack reference and individual skill references where available; variable-cost skills remain explicitly represented as ranges rather than being reduced to a single nominal cost. citeturn1search0turn1search1turn1search2
- Next metadata pass should focus on acquisition/unlock semantics, Ultimate Finish requirements, CaC/race restrictions, DLC/version provenance, and mechanics rather than filling already-present cost fields.


### Super acquisition-route pass — 2026-09-18
- Added sourced acquisition semantics for six previously blank Super routes: Super Guard, Dancing Parapara, Energy Charge, Rise to Action, Solar Flare, and Wall of Defense.
- Evidence covers starting-style/Skill Shop, Pan training, Advancement Test, Krillin training, and PQ reward routes. citeturn0search0turn0search1turn0search2turn0search3turn0search10turn1search0
- Rising Rage and Instant Charge remain intentionally blank because available references identify them as character-exclusive/raid-boss skills rather than normal player acquisition routes; no generic route is being inferred. citeturn1search2turn1search4
- Remaining blank Super/Ultimate acquisition routes should continue to be audited individually, with character-exclusive skills separated from player acquisition semantics.


### Super acquisition / character-exclusive pass — 2026-09-18
- Enriched four previously blank acquisition routes: Rising Rage, Instant Charge, Energy Release, and Time Bullet.
- Character-only evidence is now represented explicitly rather than leaving acquisition blank: Rising Rage is tied to Broly (Restrained); Instant Charge to Mira (Final Form)/boss use; Energy Release and Time Bullet are documented as non-CaC character-exclusive skills.
- Research references also distinguish ordinary obtainable charge skills from cast/raid-exclusive variants; this prevents treating every Super with a known cost as automatically obtainable by CaCs. citeturn1search0turn1search1turn1search10turn1search12
- Continue the same field-by-field acquisition audit for the remaining blank Super/Ultimate routes, prioritizing skills where character-only, mentor/training, shop, PQ, raid, or DLC provenance can be established without inference.


### Acquisition-route audit milestone — 2026-09-18
- Enriched four remaining blank Super/Ultimate acquisition fields: Burst Rush (PQ51), Change The Future (PQ43), Demon Flash Strike (PQ160), and Reverse Mabakusenko (Skill Shop).
- Burst Rush's PQ51 route is specifically tied to the Ultimate Finish condition; the other three are recorded without inventing an Ultimate Finish requirement. citeturn3search1turn3search2turn3search4turn4search0turn4search2turn4search13
- Continue auditing blank acquisition routes individually, especially cast-only/raid-only skills and skills whose source is a mentor, shop, PQ, or DLC route.


### Super/Ultimate resource-cost audit — 2026-09-18
- Audited all canonical Super and Ultimate records for missing Ki-cost values; none are null or undefined.
- Reviewed the nonstandard-cost set rather than coercing it into the common 0/100/200/300/500 pattern: Chaotic Time Impact (600), Death Ball (400), Emperor's Death Beam (400+), Final Flash (SS3 DAIMA) (400+), Gigantic Explosion (600), S.S. Deadly Bomber (400), Super Kamehameha (SS4 DAIMA) (400–500), and Thunder Flash (300–600).
- These values are retained as variable/string costs where the attack can consume additional Ki; this preserves gameplay semantics instead of falsely converting them to a single fixed cost. Community/reference evidence independently supports Death Ball at 400 Ki and Emperor's Death Beam at a 400-Ki minimum with additional Ki consumption. citeturn1search0turn1search1turn1search5
- Next cost pass should target acquisition/version provenance and Ultimate Finish requirements rather than changing already-populated fixed costs without contrary evidence.


### Skill acquisition metadata normalization — 2026-09-18
- Converted five already-explicit PQ references embedded in unlock text into the structured `source_quest` field: Dimensional Hole (PQ80), God Breaker (PQ44), Heroic Counter (PQ155), Punisher Shield (PQ129), and Rough Ranger (PQ119 Ultimate Finish).
- This is a normalization-only change: no quest number was inferred from a generic “Parallel Quest reward” statement.
- Next acquisition pass should continue distinguishing exact PQ numbers, Ultimate Finish gating, shops, mentors/training, wishes, raids, and character-only acquisition routes.


### Super/Ultimate acquisition-route audit — 2026-09-18
- Continued the second-pass metadata audit after the earlier cost normalization work.
- Canonical skill layer currently contains 294 records (179 Super, 66 Ultimate); every Super/Ultimate record currently has a non-null Ki cost field.
- Explicit PQ reward entries now have a numeric `source_quest` or equivalent explicit quest field; the remaining acquisition backlog is concentrated in non-PQ/shop/character-specific routes and records without a `last_verified` date.
- Added sourced acquisition metadata for Meditation: PQ122, “The Final Battle Before The Final Battle?!”. A Steam community discussion explicitly identifies PQ122 as the acquisition quest; this is retained as partially enriched rather than promoted to fully verified because the source is community evidence. citeturn2search3
- Research caution: Data Input has conflicting historical community descriptions around Expert Mission 20 versus TP Medal Shop availability, so it remains unresolved rather than being assigned a single acquisition route from weak evidence. citeturn3search0turn3search2


### Super/Ultimate Ki-cost audit — 2026-09-18
- Audited canonical Super/Ultimate records for missing Ki-cost values: **0 missing**.
- Reviewed the zero-Ki Super records as a distinct case rather than treating 0 as missing data. Dimensional Hole is explicitly documented at 0 Ki; charge/power-up style Supers can likewise have 0 activation cost. citeturn1search0turn1search1
- Verified representative nonzero/variable costs: Power Impact 100 Ki, Wild Buster 100 Ki with an additional 100 Ki input, Full Power Destruction 500 Ki, and Super Kamehameha (SS4 DAIMA) 400–500 Ki.
- No blanket normalization was applied; variable and input-dependent costs remain represented as documented data.


### Explicit PQ source-field enrichment — 2026-09-18
- Added structured source_quest / source_quest_or_shop values for 16 canonical skills where the PQ number is explicitly documented by researched skill pages: Burst Rush (PQ51), Demon Flash Strike (PQ160), Force Shield (PQ59), Instant Rise (PQ37), Maiden Burst (PQ92), Spirit Explosion (PQ25), Psychic Move (PQ73), Buu Buu Ball (PQ88), Angry Shout (PQ68), Energy Barrier (PQ32), Dimension Cannon (PQ59), Victory Cannon (PQ54), Dragon Burn (PQ82), Absolute Zero (PQ96), Celestial Wave (PQ151), and Mach Dash (PQ18). citeturn2search0turn2search1turn2search2turn2search3turn2search4
- These are structured provenance enrichments only; no Ultimate Finish requirement was inferred from a generic PQ reward listing.


### Explicit PQ source-field enrichment pass 2 — 2026-09-18
- Added structured source_quest/source_quest_or_shop fields for 12 additional canonical skills with explicit PQ provenance: Atomic Blast (PQ87), Blaster Ball (PQ125), Bluff Kamehameha (PQ94), Breaker Energy Wave (PQ101), Burning Attack (PQ41), Burst Kamehameha (PQ72), Burst Stinger (PQ136), Candy Beam (PQ66), Candy Beam (Super) (PQ113), Crazy Finger Shot (PQ26), Death Psycho Bomb (PQ33), and Double Death Slicer (PQ24).
- This pass intentionally records only explicit quest-number provenance; it does not infer Ultimate Finish requirements, drop percentages, or reward-slot semantics.
- Current canonical skill catalog: 294 records; all Super/Ultimate records have a non-null Ki-cost representation, including documented variable/input-dependent forms.
- A crosslink-report integrity issue remains to be repaired: the persisted report summary says 205 linked rewards, but its serialized resolved_skill_rewards array is incomplete. The validator source is the authoritative regeneration path; this is tracked rather than silently treating the stale report as complete.


### Super/Ultimate Ki-cost audit — 2026-09-18
- Canonical skill records were scanned for missing Ki costs: **0 Super/Ultimate records have null Ki cost**.
- A targeted anomaly review found legitimate nonstandard values (including 0-cost reinforcement/charge skills and 400/600-Ki Ultimates), so no blanket normalization was applied.
- Current research sources also document that skill costs vary by move rather than mapping rigidly to class; therefore remaining work is source-by-source verification of individual costs and version history.


### Canonical Awoken parent reconciliation — 2026-09-18
- Restored the four missing universal canonical Awoken parent records: Kaioken, Potential Unleashed, Beast, and Ultra Instinct.
- These records already existed in the dedicated `awoken-skills.json` canonical CaC dataset, so this was a reconciliation of two canonical layers rather than new speculative entries.
- Canonical skill catalog is back to **298 records** with **15** Awoken parent records; the deterministic index is also 298 records and has no duplicate canonical identities.
- The four additions retain partially verified status and existing dedicated Awoken sources; exact unlock chains remain a follow-up research task rather than being upgraded to fully verified.
- Validator note: `scripts/validate_skills.py` still references a `target_category_counts` structure that is absent from the current skills JSON/index. This is a validator/data-contract drift issue and should be repaired separately rather than hidden by changing the data to fit an obsolete field.


### Resource-cost audit milestone — 2026-09-18
- Canonical skill catalog remains at 298 records.
- All canonical Super and Ultimate records currently have a non-null Ki-cost field; no blanket defaulting was performed.
- The 20 zero-Ki Super records are concentrated in charge, utility, and Power Up skills (including Instant Transmission, Final Charge, Surging Spirit, Fighting Pose variants, and related entries), so their zero values remain candidates for evidence-level verification rather than automatic correction.
- Web lookup of the Fandom skill pages was blocked by robots.txt in this pass; no unsupported costs were inferred from that failed lookup.


### Super/Ultimate Ki-cost audit — 2026-09-18
- Completed a targeted audit of canonical Super/Ultimate records with zero Ki cost.
- Corrected **Rise to Action** from 0 to **100 Ki**, matching its current skill reference.
- Retained documented zero-cost skills where current references support zero cost, including Dimensional Hole, Instant Transmission, and Meditation. citeturn1search0turn0search2turn0search0
- Did not normalize costs by class alone: charging, transformation-adjacent, counter, and utility skills can legitimately use 0 or nonstandard costs.
- Remaining work: continue individual verification of nonzero and historically/version-sensitive Ki costs, then audit Ultimate Finish flags and acquisition/version provenance.


### Super/Ultimate Ki-cost audit milestone — 2026-09-18
- Audited all 245 canonical Super/Ultimate records for missing Ki-cost values; **0** are null/missing.
- Zero-Ki records are concentrated in charge/power-up/utility techniques and were retained rather than normalized generically.
- Variable costs are preserved for resource-dumping techniques: Emperor's Death Beam (400+), Final Flash (SS3 DAIMA) (400+), Super Kamehameha (SS4 DAIMA) (400–500), and Thunder Flash (300–600). This matches the available skill references, including the current Ultimate Attack index and individual DAIMA pages. citeturn1search0turn1search1turn1search2
- Fixed high-cost examples such as Death Ball (400) and Full Power Destruction (500) also match the indexed reference data. citeturn1search1
- No blanket cost correction was applied where evidence did not establish a discrepancy. Next pass should target acquisition/version provenance and Ultimate Finish semantics rather than inferring costs from class.


### Super/Ultimate Ki-cost audit — 2026-09-18
- Audited canonical Super/Ultimate records for missing Ki costs: **0 missing** across the 298-record catalog.
- Investigated four nonstandard Ultimate costs rather than normalizing them to common 300/500 values: Death Ball (400), S.S. Deadly Bomber (400), Gigantic Explosion (600), and Chaotic Time Impact (600).
- Current external references independently document all four values. citeturn1search0turn1search2turn1search3turn1search4
- No canonical Ki-cost changes were required in this pass. Continue with mechanics/acquisition/Ultimate-Finish/version metadata instead of forcing standardized costs.


### Super/Ultimate Ki-cost audit — 2026-09-18
- Audited the canonical catalog for missing Ki-cost values across all Super and Ultimate records: **0 missing values** remain.
- External reference checks support the documented cost model without treating class alone as a cost rule: Prominence Flash is documented at 300 Ki, while community references distinguish common 300-Ki ultimates from 500-Ki high-cost ultimates.
- No blanket cost normalization was applied; variable, zero-cost, and higher-cost skills require skill-specific evidence.


### Super/Ultimate Ki-cost audit — 2026-09-18
- Audited the canonical Super and Ultimate records for missing Ki-cost values: **0 missing** across the current 298-record catalog.
- The current distribution contains documented fixed costs of 0/100/200/300/400/500/600 Ki plus explicitly variable ranges (`400+`, `400-500`, `300-600`), so costs were not normalized by class alone.
- This is a completeness milestone for the resource-cost field, not a claim that every individual cost has been independently re-tested against primary game data.
- Next pass remains acquisition semantics, Ultimate Finish requirements, race/gender/CaC restrictions, and DLC/version provenance for suspicious or weakly sourced records.


### Super/Ultimate Ki-cost audit — 2026-09-18
- Audited the canonical Super and Ultimate records for missing Ki-cost values: none remain.
- Non-fixed documented costs are intentionally preserved for Emperor's Death Beam (400+), Final Flash (SS3 DAIMA) (400+), Super Kamehameha (SS4 DAIMA) (400–500), and Thunder Flash (300–600); these must not be normalized to a single inferred value.
- Next pass: verify acquisition semantics, character/source restrictions, Ultimate Finish requirements, and DLC/version provenance for these variable-cost skills and remaining partially verified records.


### Super/Ultimate resource-cost audit — 2026-09-18
- Completed a schema-level cost completeness pass across all 298 canonical skills: every Super and Ultimate record has a non-null Ki-cost field and a non-empty source/verification state.
- Cost values are intentionally not normalized to a single default: the catalog preserves zero-cost skills, standard 100/300/500 Ki costs, higher costs, and variable/extendable costs such as 300–600, 400+, and 400–600.
- External references corroborate variable-cost semantics for Thunder Flash (300–600), Final Flash (SS3 DAIMA) (400+), and One-Handed Kamehameha mk.II (400–600).
- Next pass should target semantic accuracy of acquisition/unlock routes and Ultimate Finish requirements rather than filling already-complete cost fields.


### Super/Ultimate Ki-cost audit — 2026-09-18
- Canonical audit found **0 Super/Ultimate records with a missing Ki-cost field** across all 298 skills.
- Zero-cost entries are concentrated in charge, power-up, and utility skills; sampled sources explicitly confirm 0 Ki for Dimensional Hole, Burst/charge-family behavior, and Fighting Pose E. These values are therefore not being mass-normalized to 100/300 based on class alone.
- Charge skills require special treatment because their Ki recovery is their mechanic rather than an upfront Ki expenditure; Ultimate Charge and Final Charge sources document their charging behavior rather than a conventional fixed spend.
- Next metadata pass: individually audit non-zero Super/Ultimate costs, acquisition semantics, CaC restrictions, and Ultimate Finish evidence.


### Super/Power Up cost audit — 2026-09-18
- Audited zero-cost Super records rather than assuming all Power Up skills cost 0 Ki.
- Corrected **Do or Die** and **Formation!** from 0 to **100 Ki**, matching their documented skill pages. citeturn2search4turn2search6
- Confirmed **Dimensional Hole** is legitimately **0 Ki** and replaced its broad category-only source with the specific skill page. citeturn1search0
- This reinforces the audit rule: resource costs must be verified per skill, especially for Power Up/charge/counter skills.

### Super/Ultimate Ki-cost audit — 2026-09-18
- Canonical catalog currently has 245 Super/Ultimate records and none with a missing `ki_cost` field.
- A focused anomaly pass found six intentionally nonstandard values requiring source-aware handling rather than normalization: Chaotic Time Impact (600), Emperor's Death Beam (400+), Final Flash (SS3 DAIMA) (400+), Gigantic Explosion (600), Super Kamehameha (SS4 DAIMA) (400–500), and Thunder Flash (300–600).
- Current external reference material confirms variable-cost behavior for Super Kamehameha (SS4 DAIMA) and Final Flash (SS3 DAIMA), and confirms 300–600-style scaling exists for charged/variable Ultimate attacks.
- These values are preserved rather than forced into a fixed 100/300/500 taxonomy. Next pass should reconcile each anomaly against its individual skill page and in-game behavior/version history.

### Super/Ultimate Ki-cost audit milestone — 2026-09-18
- Audited the canonical 298-record skill layer for missing Ki costs among `Super` and `Ultimate` records: **0 missing**.
- Spot-checked nonstandard costs rather than applying class-based defaults: Dimensional Hole remains 0 Ki; Divine Kamehameha is 200 Ki (2 bars); Divine Spear is 200 Ki (2 bars). Independent community references corroborate these nonstandard values. citeturn1search3turn1search0turn1search4
- This pass confirms field completeness, not universal source-level verification. The remaining priority is evidence-depth: acquisition route, race/gender restrictions, Ultimate Finish semantics, DLC/version provenance, and mechanics for older partially verified records.


### Super/Ultimate Ki-cost audit — 2026-09-18
- Audited the canonical 298-record skill layer for missing Ki costs: **0 Super/Ultimate records have null or missing `ki_cost`**.
- The current zero-Ki Super entries are concentrated in charge, Power Up, movement/utility, and character-specific support skills; they were not mass-normalized because class alone does not imply a fixed cost.
- External research corroborates that Xenoverse 2 has distinct resource models and that some charge/support skills use zero Ki to activate while building or modifying resources. citeturn0search0turn0search2
- Next pass: verify the **semantics and evidence** behind individual nonstandard/zero-cost skills, then audit Ultimate Finish requirements and acquisition/version provenance rather than applying blanket cost assumptions.


### Nonstandard Ultimate Ki-cost provenance — 2026-09-18
- Individually rechecked the six flagged nonstandard Ultimate costs instead of normalizing them by class.
- Confirmed variable/extended-cost behavior for Final Flash (SS3 DAIMA) (400+), Super Kamehameha (SS4 DAIMA) (400–500), Thunder Flash (300–600), and Emperor's Death Beam (400+). citeturn1search0turn1search1turn1search2turn1search3turn1search4
- Gigantic Explosion remains a 600-Ki Ultimate; community reporting independently describes the 600-Ki cost. citeturn1reddit53
- Added direct skill-page provenance to the canonical/index records where it was missing. Costs remain source-aware and are not flattened into 300/500 defaults.
- Next evidence-depth target: Ultimate Finish requirements and acquisition/version provenance, especially older partially verified skills.


### Ultimate Ki-cost audit — 2026-09-18
- Refined documented baseline costs for five variable/standard Ultimate records: Prominence Flash 300; Super Kamehameha (SS4 DAIMA) 400 baseline with 500 maximum; Final Flash (SS3 DAIMA) 400+; Full Power Destruction 500; Revenge Death Ball 300+.
- These values preserve variable-cost mechanics rather than collapsing them into a generic Ultimate cost.
