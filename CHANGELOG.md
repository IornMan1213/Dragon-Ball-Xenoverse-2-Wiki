## September 2026 — PQ ↔ skill relationship reconciliation

- Reconciled the canonical Parallel Quest skill endpoints against the current 429-record skill registry.
- Added missing `skill_ids` / `skill_rewards` edges for PQ11–14, PQ46, PQ49, PQ57, PQ66, PQ86–87, PQ106, PQ113, and PQ176 where the canonical skill registry already carried verified `source_parallel_quests` or the PQ record already carried the corresponding skill reward.
- Rebuilt `docs/data/pq-skill-crosslink-report.json` from the canonical PQ and skill registries: **244 forward / 244 reverse / 0 unresolved / 0 orphaned**.
- Preserved deterministic skill IDs and did not infer any new reward relationship from enemy appearance alone.

## September 2026 — deterministic skill IDs and cross-database linkage

- Added deterministic IDs to all 283 canonical skill records and synchronized the skill index.
- Added schema, builder, and validator enforcement so skill IDs survive research merges and corrections deterministically.
- Added `docs/data/CROSS-LINK-CONTRACT.md` defining stable identifiers, bidirectional relationship edges, provenance, unresolved links, and the connected-database roadmap.

## September 2026 — Awoken mechanics batch 44
- Synchronized current stage/resource mechanics across the canonical Awoken records from the consolidated research table and individual references.
- Added explicit resource, attack/defense, stamina/Ki drain, moveset, and transformation-specific mechanics without turning community build opinions into factual claims.

## September 2026 — Power to Overcome mechanics batch 43
- Enriched The Power to Overcome with current testing evidence for Stage 1 defense/speed, low-health recovery, unblockable sword strike, and Stage 2 damage/Ki behavior.
- Preserved conflicting Stage 2 speed/cooldown and exact regeneration values rather than choosing an unsupported number.

## September 2026 — Transformation stage reconciliation batch 42
- Reconciled **Super Saiyan 2** as the 400-Ki second stage of the Super Saiyan Awoken Skill rather than a separately equipped transformation.
- Reconciled **The Power to Overcome** core DLC/unlock/universal-CaC facts and its two-stage behavior while preserving conflicts over exact numeric stage modifiers.

## September 2026 — Core Awoken audit batch 41
- Promoted 11 core Awoken records from `partially_verified` to `verified` after reconciling CaC/race availability and unlock routes.
- Added exact current resource thresholds where supported, including staged Kaioken and Super Saiyan/Super Vegeta costs.
- Added batch 41 provenance and preserved the distinction between unlock eligibility and actual race usability.

## September 2026 — Saiyan Awoken verification
- Verified **Future Super Saiyan**, **Super Saiyan God Super Saiyan**, and **Super Saiyan God Super Saiyan (Evolved)** as Saiyan CaC Awoken Skills.
- Added exact level/friendship progression for SSGSS and Evolved and preserved the distinction between mentor award eligibility and actual race usability.

## September 2026 — Awoken classification correction
- Corrected three seeded Awoken records that incorrectly indicated CaC availability: **Pure Progress**, **Super Saiyan Blue Kaioken**, and **Supersonic Mode**.
- Added correction batch 37 and preserved the original research history.
- Super Soul tracker reference updated to the current **42-record** canonical population.

## September 2026 — Raid Super Soul Reconciliation
- Reconciled raid Super Souls **044–047** against item-level and community evidence.
- 044, 045 and 046 now have verified core effects; 047 remains partially verified due to unresolved stamina-damage reduction magnitude and historical raid mapping.
- Preserved uncertainty around recurrence schedules, drop probabilities, and categorical-to-numeric conversions.

## September 2026 — Raid Super Soul Candidate Batch 06
- Indexed four additional raid-exclusive Super Soul candidates **044–047** from raid catalog and community raid-exclusive evidence.
- Marked all four **partially verified** rather than inventing mechanics where item-level evidence remains incomplete.
- Canonical Super Soul population is now **42 indexed records**.

## September 2026 — Raid/Event Super Soul Batch 05
- Added research batch 05 and promoted four additional raid-associated Super Souls: **040–043**.
- Added reconciled acquisition/effect provenance for Cell, Hercule, Masked Saiyan, and Fused Zamasu raid families.
- Preserved unresolved numerical/recurrence details instead of inventing values.
- Canonical Super Soul population increased from **34 to 38**.

## September 2026 — Raid/Event Super Soul Batch 04
- Added research batch 04 for raid-associated Super Souls.
- Promoted canonical records **036–039** covering Hit and Broly raid reward families.
- Preserved conflicting evidence and categorical effect labels rather than inventing numeric values or drop rates.
- Canonical Super Soul population increased from **30 to 34**.

## September 2026 — FUTURE SAGA Chapter 4 Super Soul Expansion
- Added four Chapter 4 Super Soul identities to the canonical research layer: **032–035**.
- Added official DLC provenance plus PQ185/PQ186 acquisition leads and attributed community effect evidence where available.
- Kept item-level mechanics, exact reward mapping, and drop rates unresolved where evidence is insufficient.
- Canonical Super Soul population increased from **26 to 30** records.

## September 2026 — Super Soul Batch 03 Promotion
- Promoted Super Soul research batch 03 (IDs **024–031**) into the canonical research layer after duplicate, schema, acquisition, and independent-source reconciliation.
- Canonical Super Soul population increased from **18 to 26** records.
- Preserved unresolved shop-rotation timing and drop-rate semantics rather than inferring them.
- Refreshed `docs/data/coverage-gaps.json` and `TODO.md` so the PQ provenance milestone is no longer treated as an unresolved population gap and Super Soul expansion becomes the next data-coverage focus.

## September 2026 — PQ181–186 Final Provenance Pass
- Added record-level provenance to the final six records, **PQ181–PQ186**, with 2026-09-19 verification dates.
- Cross-checked DLC associations, Ultimate Finish conditions, and documented rewards against independent references.
- Preserved the explicitly documented PQ184 Chaotic Time Impact 50% Ultimate Finish bonus-slot rate and left unsupported probabilities unresolved.
- **All 176 canonical PQ records now have individual source arrays.**

## September 2026 — PQ171–180 Provenance Pass
- Added record-level provenance to **PQ171–PQ180** with 2026-09-19 verification dates.
- Cross-checked DLC associations, Ultimate Finish conditions, and documented rewards against independent references.
- Preserved explicit drop-rate evidence without inferring additional probabilities.
- Remaining unsourced PQ records reduced from 16 to **6 of 176**.

## September 2026 — PQ161–170 Provenance Pass
- Added record-level provenance to **PQ161–PQ170** with 2026-09-19 verification dates.
- Cross-checked quest/DLC associations, Ultimate Finish conditions, and documented rewards against independent references.
- Preserved existing explicit reward/drop-rate evidence without inferring additional probabilities.
- Remaining unsourced PQ records reduced from 26 to **16 of 176**.

## September 2026 — PQ91–100 Final Base-Game Provenance Pass
- Added record-level provenance to the final **PQ91–PQ100** base-game block with 2026-09-19 verification dates.
- Corrected the missing difficulty metadata to the documented **7-star** tier.
- Reconciled reward data, including PQ95 Flash Bomber/Drain Field, PQ96 GT Vegeta's Jacket/Absolute Zero, PQ97's expanded reward set, PQ98 Lord Slug's Clothes/Dimension Ray, and PQ100's x100 Big Bang Kamehameha/SSGSS Vegeta Wig/Whis Symbol Battle Suit.
- Cross-checked Ultimate Finish objectives against multiple independent references and kept unlock triggers conservative where evidence does not establish a unique prerequisite.
- Base-game PQ provenance gap reduced from 36 to **26 of 176 records** without individual `sources` arrays.

## September 2026 — PQ81–90 Provenance and Difficulty Pass
- Added record-level provenance to **PQ81–PQ90** with 2026-09-19 verification dates.
- Corrected the missing difficulty metadata for this block to the documented **7-star** tier.
- Cross-checked objectives and basic rewards against independent PQ/Ultimate Finish references.
- Reviewed unlock evidence conservatively; retained unresolved individual triggers where the sources do not establish a unique prerequisite.
- PQ provenance gap reduced from 46 to **36 of 176 records** without individual `sources` arrays.

## September 2026 — PQ71–80 Provenance Pass
- Added record-level provenance to **PQ71–PQ80** with 2026-09-19 verification dates.
- Cross-checked 7-star objectives and basic rewards against the maintained 186-PQ transcription and independent Ultimate Finish references.
- Reviewed unlock metadata conservatively; retained documented routes without introducing unsupported prerequisite claims because external evidence shows broader story progression can affect PQ availability.
- PQ provenance gap reduced from 56 to **46 of 176 records** without individual `sources` arrays.

## September 2026 — PQ61–70 Unlock and Provenance Reconciliation
- Added record-level provenance to **PQ61–PQ70** with 2026-09-19 verification dates.
- Reconciled unlock metadata against an independent PQ progression table: PQ61/PQ63 follow the Beerus/Wrath of the God of Destruction story arc; PQ62 and PQ64–PQ68 follow the documented PQ chain; PQ69 requires the Beerus-arc progression plus the documented Trunks interaction near the Time Nest; PQ70 follows the Resurrection of the Emperor/Golden Frieza story arc.
- Cross-checked objectives and basic rewards against the maintained 186-PQ transcription and independent Ultimate Finish references.
- Repository-wide PQ provenance gap is now **56 of 176 records** without individual `sources` arrays.

## September 2026 — PQ51–60 Provenance Pass
- Added record-level provenance to **PQ51–PQ60** with 2026-09-19 verification dates.
- Cross-checked the 5-star/6-star transition, objectives, and basic rewards against the maintained PQ transcription and independent objective references.
- Preserved PQ52's documented completion-of-PQ53 unlock behavior and the attributed PQ54/PQ55 unlock evidence rather than silently resolving conflicting historical reports.
- Repository-wide PQ provenance gap is now **66 of 176 records** without individual `sources` arrays.

## September 2026 — PQ41–50 Provenance Pass
- Added record-level provenance to **PQ41–PQ50** with 2026-09-19 verification dates.
- Cross-checked objectives and basic rewards against the maintained 186-PQ transcription and independent Ultimate Finish references.
- Kept reward-slot/drop percentages unresolved where direct evidence was not established.
- Repository-wide PQ provenance gap is now **72 of 176 records** without individual `sources` arrays.

## September 2026 — PQ31–40 Provenance Pass
- Added record-level provenance to **PQ31–PQ40** with 2026-09-19 verification dates.
- Cross-checked objectives and basic rewards against the maintained 186-PQ transcription and independent Ultimate Finish/objective references; no unsupported reward-slot percentages were introduced.
- Preserved the explicit PQ36 numbering/existence conflict rather than silently normalizing it.
- Repository-wide PQ provenance gap is now **82 of 176 records** without individual `sources` arrays.

## September 2026 — PQ21–30 Provenance and Reward Reconciliation
- Added explicit record-level `sources` arrays to all **PQ21–PQ30** records in `docs/data/parallel-quest-research-batches/pq-batch-03.json`.
- Reconciled their basic reward lists against the maintained 186-PQ transcription and independent PQ tables, correcting incomplete reward data in the batch.
- Strengthened PQ27 and PQ28 unlock metadata with the documented Metal Cooler and Appule NPC triggers respectively.
- Preserved conservative unlock wording where an exact quest-specific trigger could not be independently established.
- Updated `docs/COVERAGE-AUDIT.md`; **92 of 176 PQ records remain without individual record-level sources**.

## September 2026 — PQ11–20 Record-Level Provenance Pass
- Added explicit record-level `sources` arrays to all **PQ11–PQ20** records in `docs/data/parallel-quest-research-batches/pq-batch-02.json`.
- Rechecked the objective and Ultimate Finish data against the maintained Steam transcription and independent quest guides, with a current maintained PQ11 repository record used where applicable.
- Preserved unresolved reward-slot/drop semantics and did not add unsupported unlock gates during this pass.
- Updated `docs/COVERAGE-AUDIT.md`; the next bounded provenance pass is PQ21–PQ30.

## September 2026 — PQ Record-Level Provenance Pass
- Added explicit record-level `sources` arrays to all PQ1-PQ10 records in `docs/data/parallel-quest-research-batches/pq-batch-01.json`.
- Re-verified the batch against the maintained 186-PQ Steam transcription, the Steam PQ reward transcription, and an independent quest-objective reference.
- Kept exact reward-slot/drop percentages unresolved where the consulted evidence does not establish them; no unsupported probability claims were added.
- Updated `docs/COVERAGE-AUDIT.md` to track the remaining older-batch provenance gap.

# Changelog

## September 2026 — PQ Unlock Census Closure
- Completed the final four missing explicit Parallel Quest unlock fields: **PQ36, PQ53, PQ54, and PQ55**.
- PQ36 records completion of PQ35 as the reported prerequisite while preserving the separate PQ36 numbering/existence conflict.
- PQ53 records the Great Saiyaman 1 + 2 trigger on the floating Resort Island south of Conton City's Recreation Plaza.
- PQ54 records PQ52 as the direct completion-state report but preserves conflicting community evidence instead of presenting the route as unqualified certainty.
- PQ55 records PQ54 as its prerequisite.
- Recomputed all 18 research batches: **176 canonical PQ records; 0 missing explicit unlock_condition fields**. Field presence remains distinct from exact-route verification.


## September 2026 — PQ Cross-Link Reconciliation
- Persisted `docs/data/pq-skill-crosslink-report.json` after auditing all 18 Parallel Quest research batches.
- The audit found 212 unique PQ skill-reward references against 108 currently named canonical skill records: 36 resolve directly or through a documented `Kamekameha` → `Kamehameha` alias, while 175 remain unresolved.
- Treated the unresolved links as a canonical-data reconciliation gap rather than evidence that the skills are absent; this is now a tracked P1 task before further generic skill-batch expansion.
- Updated `TODO.md` and `docs/COVERAGE-AUDIT.md` so PQ work proceeds from the existing PQ1–PQ186 audit instead of recreating a PQ inventory.


## September 2026 (Ongoing Expansion)
- Added **Parallel Quest Audit Batch 4** covering **PQ31-PQ40** with structured records for quest identity, star difficulty, objective/lose-condition sequences, documented basic rewards, skill reward candidates, and Ultimate Finish triggers.
- Cross-checked PQ31-PQ40 against the maintained 186-PQ reward transcription plus independent hidden-objective references. Exact reward-slot/drop percentages remain unresolved where the accessible evidence does not establish them.
- Preserved the **PQ36 existence conflict** instead of silently deleting the quest: the long-running game-specific reward transcription and multiple independent guides document "The Cell Games Begin" as PQ36, while a newer independently maintained datamined corpus claims PQ36 was cut. The local audit retains the directly documented PQ36 record pending deeper game-file reconciliation.
- Added **Parallel Quest Audit Batch 3** covering **PQ21-PQ30** with structured objective, lose-condition, basic-reward, skill-reward, and Ultimate Finish records. Reward-slot/drop semantics remain unresolved where not directly established.
- Cross-checked PQ21-PQ30 against GameFAQs, Critical Hit, Steam's maintained PQ transcription, and independent hidden-objective references. Duplicate audit passed with zero duplicates.
- Added **Parallel Quest Audit Batch 2** covering **PQ11-PQ20** with structured quest identity, objective sequences, documented rewards, skill reward candidates, and Ultimate Finish triggers.
- Cross-checked PQ11-PQ20 against the maintained 186-PQ transcription and independent hidden-objective references. Exact reward-slot probabilities remain unresolved where the accessible sources do not establish them.
- Added **Parallel Quest Audit Batch 1** covering **PQ1-PQ10** with structured records for quest identity, star difficulty, objective/lose-condition sequences, historically documented basic rewards, skill reward candidates, and Ultimate Finish triggers.
- Cross-checked PQ1-PQ10 against the maintained 186-PQ transcription and independent hidden-objective references. Exact reward-slot probabilities remain unresolved where the accessible sources do not establish them, so no unsupported drop rates were added.
- Added the first structured PQ audit source file at `docs/data/parallel-quest-research-batches/pq-batch-01.json` and updated `docs/Parallel-Quest-Audit.md` with the verified coverage and audit policy.

- Added **Skill Research Batch 54** with fifteen base-game skills from PQ86-PQ100: **Neo Wolf Fang Fist**, **Atomic Blast**, **Buu Buu Ball**, **Victory Rush**, **III Bomber**, **Final Kamehameha**, **Maiden Burst**, **Bluff Kamehameha**, **Drain Field**, **Absolute Zero**, **Charged Ki Wave**, **Phantom Fist**, **Dimension Ray**, **Emperor's Edge**, and **X100 Big Bang Kamehameha**.
- Duplicate-audited all fifteen Batch 54 names against the live repository before addition; no repository-search matches were returned for the selected records. Existing **Charge** and **Flash Bomber** research was intentionally reused rather than duplicated.
- Cross-checked Batch 54 against the maintained PQ reward transcription, the all-186-PQ walkthrough, and an independent hidden-objective/Ultimate-Finish reference. Unsupported reward-slot and Ultimate-Finish semantics remain unresolved.
- Preserved the **III Bomber / Ill Bomber** naming discrepancy as provenance rather than silently creating two skills.
- **Neo Wolf Fang Fist** retains partially unresolved resource/extension mechanics pending deeper skill-specific reconciliation.

- Added **Skill Research Batch 53** with five base-game skills from PQ81-PQ85: **Afterimage Strike**, **Dragon Burn**, **Charge**, **Saiyan Spirit**, and **Zigzag Express**.
- Duplicate-audited all five Batch 53 names against the live repository; no repository-search matches were returned for the selected records.
- Cross-checked Batch 53 against the maintained PQ reward transcription, current skill-specific references, and independent technique material. Unsupported reward-slot and Ultimate-Finish semantics remain unresolved.

- Added **Skill Research Batch 52** with ten base-game skills from PQ71-PQ80: **Last Emperor**, **Burst Kamehameha**, **Psychic Move**, **Final Pose**, **Counter Burst**, **Warp Kamehameha**, **Ki Explosion**, **Dust Attack**, **Mighty Explosive Wave**, and **Dimensional Hole**.
- Duplicate-audited all ten Batch 52 names against the live repository; no code-search matches were returned for the selected records.
- Cross-checked Batch 52 against the maintained PQ reward transcription, GameFAQs, the historical XVGuide skill list, current skill-specific references, and an independent technique/character-ID reference. Unsupported reward-slot and Ultimate-Finish semantics remain unresolved.
- **Warp Kamehameha** has a current-vs-older Ki-cost discrepancy (400 vs. 300); the current skill-specific value is retained while the older value remains documented in provenance.
- **Psychic Move** and **Final Pose** retain unresolved stamina costs rather than receiving inferred values. **Dimensional Hole** is explicitly separated from the later Evasive Mighty Explosive Wave variant.

- Added **Skill Research Batch 51** with eleven early/base-game skills from PQ61-PQ70: **Recoome Kick**, **Fighting Pose H**, **Teleporting Vanishing Ball**, **Kai Kai**, **Ill Rain**, **Scissors Paper Rock**, **Candy Beam**, **Super God Fist**, **Angry Shout**, **Headshot**, and **Emperor's Blast**.
- Duplicate-audited all eleven Batch 51 names against the live repository; no repository-search matches were returned for the selected records.
- Cross-checked Batch 51 against the maintained PQ reward transcription, GameFAQs, current skill-specific references, and independent technique/character-ID material. Unsupported reward-slot and Ultimate-Finish semantics remain unresolved.
- **Kai Kai** retains unresolved resource costs because the accessible sources establish the teleportation technique but do not provide a sufficiently reliable current cost.
- The PQ66 **Candy Beam** record specifically represents the Evasive variant and is kept distinct from the later Candy Beam Super.

- Added **Skill Research Batch 50** with eleven newly researched early/base-game skills from PQ49-PQ60: **Do or Die**, **Explosive Buu Buu Punch**, **Burst Rush**, **Final Cannon**, **Victory Cannon**, **Super Donut Volley**, **Rakshasa's Claw**, **Vanishing Ball**, **Force Shield**, **Dimension Cannon**, and **Majin Kamehameha**.
- Duplicate-audited the selected Batch 50 names against the live repository before addition; the repository search returned no matches for the selected records. **Stone Bullet** and **Justice Pose** were intentionally excluded because their canonical research already exists.
- Cross-checked Batch 50 against the maintained PQ reward transcription, the current Xenoverse 2 skill guide, and current skill-specific references. Unsupported reward-slot and Ultimate-Finish semantics remain unresolved.
- **Do or Die** retains an unresolved CaC-availability field because the accessible current skill-specific reference identifies Nail/Piccolo users but does not establish a reliable CaC route.

- Added **Skill Research Batch 49** with seven early/base-game skills from PQ41-PQ48: **Burning Attack**, **Change The Future**, **God Breaker**, **Burning Slash**, **Taunt**, **Chain Destructo-Disc Barrage**, and **Kamekameha**.
- Duplicate-checked all seven selected names against the live repository; no code-search matches were returned. **Rolling Bullet** was intentionally excluded because its existing PQ42 correction is already canonical research.
- Cross-checked Batch 49 against the maintained PQ reward transcription, the current Xenoverse 2 skill guide, and current skill-specific references. Unsupported reward-slot and Ultimate-Finish semantics remain unresolved.

- Added **Skill Research Batch 48** with five early/base-game skills from PQ36-PQ40: **Evil Whirlwind**, **Instant Rise**, **Shining Slash**, **Side Bridge**, and **Heat Dome Attack**.
- Duplicate-checked all five selected names against the live repository; no code-search matches were returned.
- Cross-checked Batch 48 against the maintained PQ reward transcription, the current Xenoverse 2 skill guide, and current skill-specific references.
- **Instant Rise** has conflicting stamina figures between an older category table and the current skill-specific page; the batch uses the current specific reference's 300-stamina value and preserves the discrepancy in provenance.
- **Heat Dome Attack** confirms the previously established PQ40 correction and does not resurrect the obsolete historical attribution.

- Added **Skill Research Batch 47** with five early/base-game skills from PQ29-PQ34: **Freedom Kick**, **Energy Field**, **Energy Barrier**, **Death Psycho Bomb**, and **Paralysis**.
- Duplicate-checked all five selected names against the live repository; no code-search matches were returned.
- Cross-checked the batch against the maintained PQ reward transcription, current Xenoverse 2 skill-specific references, and independent Future Warrior/technique references.
- Preserved unresolved reward-slot and Ultimate-Finish semantics instead of inferring them. **Paralysis** also has a classification conflict across current references (Strike Ultimate vs. Super), so it remains `partially_verified` with the disagreement documented in its provenance.
- Batch 47 also records the already-established **Freedom Kick PQ29 correction** while leaving the historical Batch 17 and correction Batch 35 intact for auditability.

- Added **Skill Research Batch 46** with five early/base-game skills from PQ24-PQ28: **Double Death Slicer**, **Spirit Explosion**, **Crazy Finger Shot**, **Sauzer Blade**, and **Spread Shot Retreat**.
- Duplicate-checked all five selected names against the live repository; no code-search matches were returned.
- Cross-checked Batch 46 against the current Xenoverse 2 skill guide, independent PQ reward transcriptions, and skill-specific references. Unsupported reward-slot semantics and Ultimate-Finish requirements remain unresolved.

- Added **Skill Research Batch 45** with five early/base-game skills from PQ19-PQ23: **Fighting Pose E**, **Mystic Flash**, **Evil Flight Strike**, **Energy Shot**, and **Death Slash**.
- Duplicate-checked all five selected names against the live repository search; no code-search matches were returned.
- Cross-checked Batch 45 against the current Xenoverse 2 skill guide, independent PQ reward transcriptions, and skill-specific references. Reward-slot semantics and Ultimate-Finish requirements remain unresolved where the sources do not establish them.
- Confirmed a separate **Spinning Blade acquisition conflict** for follow-up correction: the historical PQ15 reward transcription lists it with Holstein Shock and Fighting Pose D, while the current skill-specific reference identifies TP Medal Shop as its unlock method. This conflict remains preserved rather than silently choosing one source.

- Added **Skill Research Batch 44** with five early/base-game Ginyu Force skills: **Holstein Shock**, **Ginyu Force Special Combo**, **Fighting Pose B**, **Fighting Pose D**, and **Mach Punch**.
- Duplicate-checked all five selected names against the live repository search; no code-search matches were returned. The canonical seeded index already contains some category-only records such as Mach Dash, so research batches are being used to enrich records rather than falsely treating every indexed name as absent.
- Cross-checked Batch 44 against the current Xenoverse 2 skill guide, independent PQ reward transcriptions, and skill-specific references. Exact reward-slot probabilities remain unresolved.

- Added **Skill Research Batch 43** with five previously absent early/base-game PQ skills: **Meteor Blow**, **Earth Splitting Galick Gun**, **Meteor Crash**, **Fighting Pose C**, and **Kaioken Kamehameha**.
- Duplicate-checked all five selected names against the live repository; **0 repository-search matches** were returned for each.
- Reconciled Batch 43 against the current Xenoverse 2 skill guide and independent PQ reward transcriptions. Earth Splitting Galick Gun also has a newer independently maintained PQ database entry reporting an Ultimate Finish reward roll; the batch keeps `ultimate_finish_required` unresolved rather than promoting that source-specific result into an unconditional field.

- Added **Skill Research Batch 42** with five previously absent early/base-game PQ skills: **Recoome Eraser Gun**, **Mach Kick**, **Fighting Pose J**, **Time Control**, and **Unrelenting Barrage**.
- Cross-checked Batch 42 against the current Xenoverse 2 skill guide, independent PQ reward transcriptions, and skill-specific references where available. Unsupported reward-slot, drop-probability, and technical fields remain unresolved.
- Identified that **Skill Research Batch 41 duplicates Batch 40's five records** rather than adding new catalog coverage; both batches remain preserved as historical research, but Batch 41 is not counted as five additional unique skills.

- Added **Skill Research Batch 41** with five early/base-game PQ skills: **Solar Flare**, **Paralyze Beam**, **Meteor Strike**, **Shine Shot**, and **Wall of Defense**.
- Cross-checked the five records against an independent searchable PQ reward transcription and a current Xenoverse 2 skill guide. Exact technical fields remain unresolved where the available evidence does not establish them.

- Added **Skill Research Batch 40** with five early/base-game PQ skills: **Solar Flare**, **Paralyze Beam**, **Meteor Strike**, **Shine Shot**, and **Wall of Defense**.
- Duplicate-checked all five selected names against the live repository code-search index; **0 matches** were returned for each selected record.
- Reconciled Batch 40 against current Xenoverse 2 quest/skill references. Solar Flare and Meteor Strike have documented Ki/classification data; Paralyze Beam, Shine Shot, and Wall of Defense retain unresolved technical fields rather than receiving inferred values.

- Added **Skill Research Correction Batch 39** after independently re-verifying Batch 38: Life Absorption is now documented at 10% life drain; Flash Bomber is identified as the PQ95 Ultimate Finish reward; and Energy Release is explicitly tied to Towa while its exact resource cost remains unresolved.
- Preserved Batch 38 as historical research and used correction metadata so the canonical builder can supersede only the contradicted fields.
- Added **Skill Research Batch 38** with five previously unrecorded skills found absent from the live repository search: **Drain Charge**, **Hyper Drain**, **Life Absorption**, **Energy Release**, and **Flash Bomber**.
- Duplicate-checked all five selected names against the live repository before addition; **0 repository-search matches** were found.
- Reconciled Batch 38 against current Xenoverse 2 references. Drain Charge, Hyper Drain, and Flash Bomber have documented acquisition/cost data; Energy Release remains partial because its current reference does not establish a CaC route or resource cost; Life Absorption was initially kept partial because current reference variants disagreed on the health-drain percentage, then corrected by Batch 39 using the current 10% reference.

- Added **Skill Research Correction Batch 37** to preserve Batch 36's historical research while correcting the final-DLC acquisition mapping: the directly enumerated PQ reward list places **Dragon Spiral** and **Indomitable** on PQ185 and **Venus Fist** on PQ186. A conflicting July 2026 acquisition guide says all three can drop from both PQs, so the disagreement is retained as provenance rather than silently erased.
- Kept `ultimate_finish_required` unresolved for all three final-DLC PQ skills because the available reward lists do not establish that the skills occupy an Ultimate-Finish-only slot.
- Enriched **The Power to Overcome** with independently reported 2026 mechanics: first-stage defense/movement/health-recovery behavior, unblockable sword-grab replacement, approximately 12-second Unleashed duration, 500-Ki activation, temporary extreme Ki regeneration, health drain, and reported attack/movement modifiers. Conflicting 24-vs-30-second cooldown measurements remain explicitly source-sensitive.
- Added `correction_of` and `correction_fields` metadata to Batch 37 so the canonical skill builder actually replaces the superseded Batch 36 acquisition/mechanics fields while preserving the original Batch 36 file for auditability.

- Added **Skill Research Batch 36** for the final DLC, **Future Saga Chapter 4**: **Dragon Spiral**, **Indomitable**, **Venus Fist**, and **The Power to Overcome**.
- Cross-checked Chapter 4's four-move scope against official Bandai Namco/platform listings. The three attack skills were tied to PQ185/PQ186 reward pools, while **The Power to Overcome** was recorded separately as the new CaC Awoken Skill.
- Kept the three new PQ skills `partially_verified` where exact mechanics/reward-slot details still need deeper reconciliation; no unsupported drop percentages were added.
- Added the final DLC's July 2026 provenance to the skill research layer, bringing the repository's research coverage through the final advertised Xenoverse 2 DLC release.
- Fixed `scripts/build_skills_from_research.py` so correction records can remove an obsolete canonical record when a correction changes its `(name.casefold(), class, subcategory)` uniqueness key. This specifically prevents a Super → Evasive correction such as Rolling Bullet from leaving the obsolete record behind.
- Inspected the post-fix Repository Quality workflow. The run failed in the internal-artifact checker job, but GitHub exposed no usable step logs; the failed job was rerun and is currently queued rather than being misreported as a code-validation result.

- Added **Skill Research Batch 19** with five newly researched skills: **Charge**, **Stone Bullet**, **Double Buster**, **Finish Buster**, and **Justice Rush**.
- Duplicate-checked the selected Batch 19 names against the live repository before research; **0 duplicates** were found for the selected records.
- Reconciled Batch 19 against current Xenoverse 2-specific references. Current-game acquisition routes were used instead of inheriting older Xenoverse 1 PQ numbering, and unsupported drop probabilities were left unresolved.
- Re-verified **Skill Research Batch 17** and found five proven corrections: **Heat Dome Attack** now points to PQ40; **Freedom Kick** to PQ29; **Rolling Bullet** is a Ki Blast Evasive from PQ42 rather than a Strike Super; **Super Drain** is a Skill Shop skill after *A Desperate Future* and transfers two stamina bars; and **Justice Pose** is from PQ53 with a documented 20-second all-stat boost.
- Added correction batch `docs/data/skill-research-batches/skill-batch-35.json` so the historical Batch 17 remains auditable while the canonical builder can apply the corrected fields.
- Preserved the pre-existing **Skill Research Batch 18** unchanged after detecting that an attempted continuation used the already-assigned batch number; the new five-record research was moved to **Batch 19** instead of overwriting historical research.


## September 2026 — Skill DLC provenance correction
- Corrected **Evil Blast (PQ114)** and **Evil Flame (PQ117)** to **Extra Pack 1** provenance.
- The prior combined DLC label was broader than the maintained PQ/DLC mapping; no other skill metadata was changed.


## September 2026 — Skill DLC provenance refinement
- Tightened four skill records from generic DLC wording to exact PQ-era provenance: **Flash Chaser → Ultra Pack 2**, **Photon Swipe → Ultra Pack 2**, **Pretty Cannon → Ultra Pack 1**, **Raid Blast → Ultra Pack 1**.
- No gameplay or acquisition-condition fields were changed.


## September 2026 — Super Pack 2 provenance refinement
- Refined four DLC 2 skill records from broad `Super Pass` provenance to exact **Super Pack 2** provenance.
- No gameplay, acquisition, or Ultimate Finish fields were changed.

### Data accuracy

- 2026-09-20: Corrected **Super Saiyan Blue Kaioken** provenance from `Base Game` to `Free Update 1`. Bandai Namco's official Free Update #1 material states that SSGSS Goku's Kaioken x10 was made available as free content ahead of DLC Pack 1; this resolves the previously retained historical ambiguity. No acquisition or character-only fields were otherwise changed.

## 2026-09-21 — Correct PQ title provenance for two UF skill records
- Corrected the canonical/index source_quest_or_shop and unlock_method labels for Flash Chaser (PQ138) and Photon Swipe (PQ139) to match the maintained PQ research titles.
- Flash Chaser now points to PQ138 — "The Battle for Earth"; Photon Swipe now points to PQ139 — "War and Pieces".
- Preserved the existing Ultimate Finish requirement and documented roll percentages; this is a provenance-label correction only.
- Independent current Steam PQ documentation and the repository's PQ research batches corroborate both PQ numbers/titles and reward associations.

## 2026-09-21 — Correct PQ title provenance for two UF skill records
- Corrected the canonical/index source_quest_or_shop and unlock_method labels for Flash Chaser (PQ138) and Photon Swipe (PQ139) to match the maintained PQ research titles.
- Flash Chaser now points to PQ138 — "The Battle for Earth"; Photon Swipe now points to PQ139 — "War and Pieces".
- Preserved the existing Ultimate Finish requirement and documented roll percentages; this is a provenance-label correction only.
- Independent current Steam PQ documentation and the repository's PQ research batches corroborate both PQ numbers/titles and reward associations.,,## 2026-09-21 — Canonical PQ IDs and bidirectional skill-link audit,- Expanded `docs/data/parallel-quests-record-layer.json` from a seven-record seed to the full **186-record** canonical numbered layer, with deterministic `pq-NNN` IDs.,- Synchronized **65** additional skill-reward edges from the maintained PQ research batches into the canonical PQ layer, preserving the evidence-backed reward names and existing uncertainty.,- Upgraded `scripts/validate_pq_skill_links.py` to use stable PQ/skill IDs, emit forward and reverse relationship data, recognize documented aliases, and report unresolved/orphaned endpoints.,- Added three previously missing canonical skill records: `Drain Field`, `Flash Bomber`, and `Rakshasa's Claw`. The live cross-link audit now resolves **217** forward PQ→skill edges across **215** reverse skill endpoints.,- The remaining unresolved canonical PQ→skill endpoints are 19 skills concentrated in PQ141-150 plus two earlier naming/catalog gaps (`Energy Shot`, `Crusher Ball`). They are preserved as explicit unresolved work rather than fabricated records.,,## 2026-09-21 — Complete the 19 unresolved PQ→skill endpoints,- Added all 19 previously unresolved skill endpoints to the canonical skill catalog: Energy Shot, Crusher Ball, Dragon Blitz, Brutal Buster, Excellent Full Course, Hyper Tornado, Burning Shot, Destructive Fracture, Destructive Flare, Destructive Fission, Crush Cannon, Double Crush, Crush Stream, Blaster Cannon, Blaster Bomb, Comet Strike, Meteor Explosion, Impact Flare, and Power Wall.,- Enriched the new records with deterministic IDs, class/subcategory, Ki/Stamina cost where documented, source PQ, DLC provenance, mechanics/description, CaC scope, evidence URLs, and explicit uncertainty language. No exact drop percentages were fabricated.,- Synchronized the deterministic skills index and regenerated the PQ↔skill relationship report.,- Current relationship audit is now **236 resolved forward PQ→skill edges / 234 reverse skill endpoints / 0 unresolved forward edges / 0 orphaned reverse source routes** across 186 canonical PQ records and 305 canonical skill records.,- External checks corroborate the PQ/reward mappings and move classifications: Energy Shot (PQ22), Crusher Ball (PQ34), PQ141 Dragon Blitz/Brutal Buster, PQ142 Excellent Full Course, PQ143 Hyper Tornado/Burning Shot, PQ145/146 Destructive skills, PQ147 Crush family, PQ148 Blaster family, PQ149 Comet Strike/Meteor Explosion, and PQ150 Impact Flare/Power Wall. citeturn0search8turn0search17turn2search6turn0search2turn3search1turn1search3turn0search1turn0search3turn2search1turn1search0turn1search5turn0search0turn1search2turn2search0turn2search4turn3search0turn3search2

## 2026-09-21 — Add PQ cross-links for equipment, accessories, and Super Souls
- Added deterministic PQ↔equipment, PQ↔accessory, and PQ↔Super Soul relationship reports with forward and reverse indexes.
- Current explicit relationship coverage: 15 equipment endpoints, 25 identity-matched accessory endpoints, and 10 Super Soul endpoints.
- Added `scripts/validate_pq_reward_crosslinks.py` for reproducible cross-domain auditing and registered the new reports in `pq-cross-domain-index.json`.
- Unresolved routes remain explicit: 15 equipment records, 20 accessory research records, and 32 Super Soul records currently lack a sufficiently explicit PQ endpoint. No speculative links were introduced.

## 2026-09-21 — Refine four canonical skill mechanics records
- Refined mechanics notes for Crush Cannon, Double Crush, Crush Stream, and Destructive Fission using current official/independent evidence and explicit uncertainty boundaries.
- Synchronized skills-index.json; live canonical/index count remains 305.
- Preserved version-sensitive behavior and did not add unsupported numerical damage, frame, or drop-rate claims.

## 2026-09-21 — Enrich twelve canonical skill mechanics records
- Replaced generic mechanics placeholders with evidence-backed mechanics/evidence boundaries for 12 skills spanning base-game and DLC PQ rewards.
- Synchronized canonical and index projections; both remain at 305 records.
- Preserved three surfaced cost conflicts for dedicated reconciliation rather than silently changing canonical values.

## 2026-09-21 — Resolve three skill Ki-cost conflicts
- Resolved Dimension Ray to 400 Ki and Majin Kamehameha to 100 Ki using current dedicated skill documentation and aggregate skill references.
- Corrected Neo Wolf Fang Fist from a misleading fixed scalar to a variable-cost representation, documenting its 100–700 Ki range.
- Synchronized canonical and index projections; both remain at 305 records.

## 2026-09-21 — Reconcile eight PQ accessory identities

- Added canonical accessory identities for **Four-Star Dragon Ball Hat, Chiaotzu's Hat (With Collar), Dore's Scouter, Great Saiyaman Bandana 1, Great Saiyaman Bandana 2, Jaco's State-of-the-Art Radio, Tagoma's Scouter, and SSGSS Goku Wig**.
- Synchronized the accessory PQ canonical bridge and bidirectional cross-link report so each of the eight research records resolves to a deterministic canonical accessory ID.
- Cross-link coverage is now **33 matched accessory PQ endpoints / 12 unresolved research identities / 96 canonical accessory identities**.
- No drop rates, Ultimate Finish requirements, or unsupported acquisition semantics were fabricated.

## 2026-09-21 — Accessory PQ identity batch 2
- Added four canonical accessory identities: Yamcha's Baseball Hat, SSGSS Vegeta Wig, Bulma (Kid) Wig, and Great Saiyaman Helmet.
- Synchronized the PQ accessory bridge and cross-link report; coverage now reflects 37 matched accessory PQ endpoints and 100 canonical accessory identities.
- Preserved unresolved/conflicted routes and did not infer unsupported acquisition mechanics.

## 2026-09-21 — Accessory PQ identity batch 3
- Added canonical identities for Gine (DB Super) Set, Caulifla Wig, and Kale Wig.
- Synchronized accessory PQ relationship data; unresolved research identities reduced without collapsing component/set records into unsupported identities.

## 2026-09-21 — Yamcha's Sword accessory reconciliation
- Added canonical `Yamcha's Sword` identity and linked its documented PQ36 route plus Accessory Shop route.
- Resolved the prior PQ29/PQ36 route conflict without duplicating the inventory identity.
- Refreshed accessory bridge census and cross-link projections.

## 2026-09-21 — Accessory identity batch 5
- Reconciled Android 15's Sunglasses → Android 15's Shades & Hat (TP Medal Shop).
- Reconciled Android 17 (DB Super)'s Ranger Accessory → existing Android 17 (DB Super) Wig identity for PQ152, preserving the research label as a component alias.
- Kept Android 14's Hat and Bardock (DB Super)'s Scouter unresolved because their PQ evidence documents clothing rewards instead.

## 2026-09-21 — Final unresolved accessory research pass
- Researched Android 14's Hat (PQ104) and Bardock (DB Super)'s Scouter (PQ146) against current equipment catalogs and PQ reward evidence.
- Both remain explicitly unresolved because the documented PQ rewards are the corresponding character Clothes, not exact accessory identities.
- Preserved the unresolved records rather than incorrectly linking them to clothing records.


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
- Each of the five canonical Time Rift endpoints now explicitly lists Future Super Saiyan as a dependent unlock relationship because all five Distorted Time Eggs are required for Unknown History.
- Regenerated the Time Rift/skill cross-link report: **6 skills / 11 forward Time Rift → skill edges / 0 broken endpoints**.


### 2026-09-21 cycle update — Namekian and Future Saga acquisition endpoints
- Live census before editing: **305 skills / 305 skill-index records / 5 Time Rift endpoints / 1 Unknown History endpoint**.
- Bounded batch: **Become Giant** and **The Power to Overcome**.
- Research/evidence: Become Giant's current external references identify Guru's House / Namekian Awakening as its acquisition endpoint and distinguish the required Namekian progression from the transformation itself. citeturn0search0turn0search11turn0search3 The Power to Overcome is tied to Future Saga Chapter 4 and Quest 31, Ultimate All-Out Showdown; current 2026 guide evidence identifies the final mission as the unlock point and the Chapter 4 DLC as required. citeturn0search8turn0youtube18
- Changes: added `source_time_rifts` to Become Giant; created `future-saga-story-record-layer.json`; linked The Power to Overcome to `story-future-saga-chapter-4-quest-31`; formalized the story-mission domain in the expansion contract; updated the bidirectional cross-link report.
- Evidence limits/conflicts preserved: no unverified mission-number claims were added for older Time Rift routes; The Power to Overcome's mechanics already contain conflicting measured values in the canonical skill record, and those conflicts remain unresolved rather than being flattened.
- Validation: **305/305 canonical/index parity preserved; 0 broken relationship endpoints; 2 target skill relationship projections match; 0 citation artifacts in changed canonical JSON; 5 Time Rifts + 2 story-mission endpoints; cross-link report now has 11 Time Rift→skill edges and 2 story-skill edges**.
- CI: combined status exposed no statuses for the contract commit; no CI success is claimed.
- Commits: `a646663` (skills), `596b0d8` (skills index), `a0370c9` (Future Saga endpoint), `7968132` (story contract), `4c4f7b7` (cross-link report).
- Live census after editing: **305 skills / 305 skill-index records / 5 Time Rift endpoints / 1 Unknown History endpoint / 1 Future Saga story endpoint / 6 Time Rift-linked skills / 11 Time Rift→skill edges / 2 story-skill edges / 0 broken endpoints**.
- Exact next batch: **expand the Future Saga story endpoint into its chapter/quest relationship layer for the remaining newly introduced skills and rewards, starting with the other Chapter 4 skills already present in canonical data; then reconcile any existing skill-to-PQ links that can be deterministically reverse-indexed without changing unresolved acquisition conditions.**


### 2026-09-21 cycle update — Future Saga Chapter 4 PQ ↔ skill graph completion
- Researched the remaining Chapter 4 skills already present in canonical data: **Dragon Spiral, Indomitable, and Venus Fist**. Current repository PQ records place Dragon Spiral + Indomitable in PQ185 (A God's Amusement) and Venus Fist in PQ186 (Frieza's Right-Hand Man); current Chapter 4 documentation confirms the DLC contains two Parallel Quests and four new moves including one Awoken Skill. citeturn0search0turn0search1turn0search2
- Added deterministic `skill_ids` to PQ185/PQ186, `source_parallel_quests` to the three skill records and skill index, and explicit Chapter 4 `skill_relationships`/PQ references in `future-saga-story-record-layer.json`.
- Expanded `record-expansion-contract.json` with PQ `skill_ids` and skill `source_parallel_quests` cross-domain fields.
- Expanded `time-rift-skill-crosslink-report.json` with **2 PQ endpoints / 3 PQ→skill edges**.
- Validation: **305 skills / 305 index records / 186 PQ records / 4 Chapter 4 story-linked skills / 0 broken endpoints / 3 edited skill/index parity checks passed / 0 citation artifacts in canonical JSON**.
- Exact relationship graph now lets a user traverse **Future Saga Chapter 4 → Quest 31 → The Power to Overcome**, and **Future Saga Chapter 4 → PQ185/PQ186 → individual skills**, while each skill resolves back to its source PQ and Chapter 4 story endpoint.
- Evidence boundary: the canonical PQ records already distinguish Basic Reward from Ultimate Finish conditions. No new Ultimate Finish requirement or drop probability was inferred here. Current official DLC material confirms Chapter 4's content scope, while the maintained repository reward records supply the exact skill-to-PQ mapping. citeturn0search0turn0search1
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
- External/current repository research supports treating PQ reward tables as the primary relationship evidence and confirms PQs are the game's main skill-farming relationship layer. citeturn0search3turn0search5turn0search6
- Exact next batch: **audit the remaining 71 skills without `source_parallel_quests` by acquisition type, separating non-PQ sources (mentor, shop, Time Rift, story, Advancement Test) from genuinely missing PQ reverse links; then repair only evidence-backed missing routes.**


### 2026-09-21 cycle update — 71-skill non-PQ acquisition audit
- Audited every canonical skill lacking `source_parallel_quests` after the PQ reconciliation. **71 skills** were classified without inventing PQ relationships.
- Classification: **7 Time Rift, 6 story/story-Shop, 17 mentor/training, 4 Advancement Test, 15 Skill/TP/STP Shop, 3 Expert Mission, 10 character/roster-only, 1 starting move, 3 Shenron wish, 5 mentor-like routes requiring a future mentor layer, 0 genuinely unresolved acquisition cases** after refining Beast, Super Saiyan 2 (stage), SSGSS, SSGSS Evolved, and Ultra Instinct.
- Created `docs/data/skill-acquisition-coverage-report.json` to persist this classification and explicitly prevent non-PQ acquisition sources from being forced into the PQ graph.
- Important architecture finding: the repository currently has **no canonical mentor or Expert Mission record layer** discoverable in the live data tree. Therefore mentor/expert skills retain their textual acquisition facts instead of receiving guessed IDs. This follows the repository null/provenance policy.
- No canonical acquisition facts were changed in this cycle; the output is a coverage/audit layer identifying the next schema expansion targets.
- External corroboration: PQs are a major skill source, but rewards can also come from other acquisition systems, so the audit deliberately keeps those systems separate. citeturn0search0turn0search3
- Validation target for next cycle: build the missing **mentor record layer** first, because 17 direct mentor-training skills plus 3 mentor-like Awoken routes are currently blocked from deterministic bidirectional mentor ↔ skill navigation; then build Expert Mission endpoints for the 3 EM-sourced skills.
- Exact next batch: **create the canonical mentor record layer and connect the 17 direct mentor-training skills in larger deterministic batches, starting with mentors whose skills are already fully named in canonical skill data; then add Expert Mission records.**


### 2026-09-21 cycle update — mentor → skill cross-domain layer
- Expanded the existing `docs/data/mentors-record-layer.json` from identity-only records into a usable cross-domain layer while preserving its 33 canonical mentor identities.
- Added verified mentor → skill relationships for **11 mentors / 16 skill edges**: Krillin (2), Gohan (Kid) (1), Vegeta (1), Frieza (1st Form) (1), Cooler (Final Form) (1), Android 18 (1), Lord Slug (2), Pan (1), Goku (2), Cell (1), and Hit (3).
- Added `source_mentor` to the corresponding canonical skill records and mirrored the field in `skills-index.json`.
- Extended `docs/data/record-expansion-contract.json` so `source_mentor` is an explicit skill cross-domain field.
- Created `docs/data/mentor-skill-crosslink-report.json` with the 16 deterministic forward edges and unresolved-edge tracking.
- Validation: **33 mentors, 11 mentors with linked skills, 16 mentor→skill edges, 16 skills with mentor reverse sources, 0 broken mentor endpoints, skill-index mentor parity = true**.
- External mentor references corroborate that mentors teach signature skills through initiation/lesson progression; official Bandai Namco documentation confirms the mentor system teaches character moves. citeturn0search4turn0search3
- The previous coverage audit's mentor count is now refined from 17 directly verified routes to **16**, because only 16 canonical skill records currently contain an exact mentor-training route that could be deterministically linked without guessing.
- Exact next batch: **finish the remaining mentor acquisition mappings by auditing the existing 33 mentor identities against all skill records, then create the Expert Mission record layer for the 3 EM-linked skills (Data Input, Super Spirit Bomb, Supernova).**


## 2026-09-21 — Pan/Jaco/Goku/Bardock mentor skill expansion
- Added 13 missing canonical mentor-taught skills across Pan, Jaco, Goku, and Bardock; existing Dancing Parapara, Spirit Bomb, and Instant Transmission records were reused rather than duplicated.
- Synchronized `skills.json`, `skills-index.json`, and `mentors-record-layer.json` so all 16 lesson endpoints for the four mentors now resolve to deterministic canonical skill IDs.
- Added evidence-bounded acquisition/classification/mechanics fields for Prepare to be Punished, Feint Shot, Maiden Blast, Hero's Pose, Elite Beam, Elite Shooting, Super Elite Combo, x10 Kamehameha, Super Kamehameha, Tyrant Lancer, Rebellion Spear, Riot Javelin, and Brave Heat.
- Preserved mentor provenance bidirectionally through `source_mentor` and mentor lesson `skill_id` fields. No unsupported drop rates, Ultimate Finish gates, or narrower CaC restrictions were inferred.
- Live skill census after expansion: **397 canonical skills / 397 skill-index records**; taxonomy totals remain synchronized.
- Mentor coverage after expansion: **108 linked lesson→skill edges / 21 fully linked mentors / 8 partially linked mentors / 34 unresolved lesson endpoints**.

## 2026-09-21 — Mentor graph validation correction
- Removed the unresolved Hit → Time Skip/Tremor Pulse ID from the mentor reverse index because no canonical skill record exists yet.
- Preserved Time Skip/Tremor Pulse as an explicit unresolved lesson endpoint rather than inventing a canonical skill record.
- Mentor relationship coverage remains **108 resolved lesson→skill edges / 21 unresolved lesson endpoints / 25 fully linked mentors / 4 partially linked mentors**, with **0 broken mentor→skill endpoints**.

## 2026-09-21 — Android 16 / Future Gohan / Bojack mentor expansion
- Expanded the canonical skill graph for **Android 16, Future Gohan, and Bojack**.
- Added **11 missing canonical skill records**: Eye Beam, Rocket Tackle, Android Rush, Hell Flash, Sonic Rush, Energy Dome, One-Handed Kamehameha mk.II, Reverse Launcher, Trap Shooter, Psycho Barrier, and Grand Smasher.
- Reused the existing canonical **Super Explosive Wave** record for Future Gohan rather than duplicating it; its `source_mentor` provenance now preserves both Piccolo and Future Gohan because both mentor endpoints teach the same canonical skill.
- Restored the previously empty Future Gohan lesson layer with all four exact lesson endpoints and synchronized the mentor coverage report.
- Evidence: maintained instructor guide plus independent mentor/skill references establish the exact lesson sequence and classifications. No unsupported numerical costs or drop rates were fabricated; combat mechanics remain intentionally deferred where not directly verified.
- Validation after expansion: **408 canonical skills / 408 skill-index records / taxonomy total 408 / 133 mentor lessons / 120 resolved mentor→skill edges / 13 unresolved lesson endpoints / 28 fully linked mentors / 4 partially linked mentors / 0 duplicate canonical skill IDs / 0 citation artifacts**.
- Next unresolved mentor frontier is now concentrated in existing incomplete endpoints rather than the completed Android 16/Future Gohan/Bojack batch.

## 2026-09-21 — Zamasu / Hit / Vegeta / Kid Gohan mentor graph expansion
- Completed the next mentor frontier for **Zamasu, Hit, Vegeta, and Gohan (Kid)**.
- Added **10 canonical skill records**: God Splitter, Heavenly Arrow, Instant Severance, Evil Ray Strike, Evil Rise Strike, Explosive Assault, Finish Breaker, Flash Strike, Final Flash, and Time Skip/Tremor Pulse.
- Correctly treated Zamasu's Initiation reward **I'm thinking of becoming a GodTuber** as a Super Soul rather than inventing a skill record for it.
- Restored Hit's previously unresolved **Time Skip/Tremor Pulse** endpoint after direct skill evidence verified that it is a Strike Evasive learned through Hit's Lesson 3.
- Synchronized canonical skills, skill index, mentor records, and coverage report.
- Validation: **418 canonical skills / 418 index records / 418 taxonomy total / 133 mentor lessons / 130 resolved mentor→skill edges / 3 unresolved endpoints / 31 fully linked mentors / 2 partially linked mentors / 0 duplicate canonical IDs**.
- Remaining unresolved endpoints are now: Krillin → Orin Combo, Krillin → Scatter Kamehameha, and Zamasu → I'm thinking of becoming a GodTuber (non-skill Super Soul).

## 2026-09-21 — Krillin mentor graph completion
- Added the two remaining missing Krillin mentor skill records: **Orin Combo** (Strike Super) and **Scatter Kamehameha** (Ki Blast Ultimate).
- Linked both lesson endpoints into the canonical skill graph and synchronized the skill index, mentor layer, and coverage report.
- Verified against the Krillin mentor/skill references; `Spread Shot Retreat` remains a separate Evasive used by Krillin and is not incorrectly inserted as a fourth mentor lesson reward.
- Validation: **420 canonical skills / 420 index records / 420 taxonomy total / 133 mentor lessons / 132 resolved mentor→skill edges / 1 unresolved endpoint / 32 fully linked mentors / 1 partially linked mentor / 0 duplicate canonical IDs**.
- The remaining unresolved endpoint is Zamasu's **I'm thinking of becoming a GodTuber**, which is a Super Soul rather than a skill and is intentionally retained as a typed unresolved non-skill reward.

## 2026-09-21 — Mentor Dual Ultimate relationship layer
- Expanded the mentor graph beyond ordinary lesson rewards by creating `docs/data/dual-ultimate-mentor-layer.json` with **33 mentor → Dual Ultimate relationships**, covering every current mentor.
- Each Dual Ultimate now links to its mentor and to the underlying canonical base skill where applicable; **33/33 base-skill links resolve**.
- Added the three previously missing ordinary base skills discovered during this audit: **Giant Storm**, **Angry Explosion**, and **Dead End Rain**. These are now canonical skill records and are linked from their corresponding Dual Ultimate records.
- This preserves an important distinction: a mentor's taught Ultimate does not necessarily equal its Dual Ultimate. Examples include Krillin → DUAL Chain Destructo-Disc Barrage, Android 18 → DUAL Dead End Rain, Majin Buu → DUAL Angry Explosion, and Ginyu → DUAL Milky Cannon.
- Validation: **423 canonical skills / 423 index records / 423 taxonomy total / 33 mentor Dual Ultimate records / 33 resolved Dual Ultimate → base-skill edges / 0 unresolved Dual Ultimate base links**.

## 2026-09-21 — PQ → canonical skill endpoint reconciliation
- Audited the existing PQ cross-domain relationship layer against the now-expanded canonical skill registry.
- Found **7 PQ reward targets** that existed as verified relationship edges but had no canonical skill endpoint: **III Bomber, Starfall, God of Destruction's Might, Meteor Crash, Fighting Pose C, Psycho Escape, and Kaioken Kamehameha**.
- Added six missing canonical skill records and resolved `Starfall` as the existing canonical **Destruction's Concerto: Starfall** alias.
- Synchronized `source_parallel_quests` so skill → PQ reverse navigation now retains the verified PQ IDs rather than relying only on prose acquisition fields.
- Updated `pq-skill-crosslink-report.json`: **236 forward skill edges / 236 reverse skill endpoints / 0 unresolved forward edges / 0 orphaned reverse sources**.
- Validation: **429 canonical skills / 429 index records / 429 taxonomy total**.


## 2026-09-21 — PQ to Super Soul relationship reconciliation
- Linked PQ006 (Saibamen's Revenge) to canonical Super Soul super-soul-009 (You cocky little...!).
- Updated pq-reward-relationships.json, parallel-quests-record-layer.json, and pq-super-soul-crosslink-report.json.
- Validation: 138 master PQ-to-Super Soul relationships; 11 canonical forward edges; 11 reverse edges; 31 unresolved canonical Super Soul endpoints; 0 bidirectional mismatches; 0 citation artifacts.
- CI: latest data-audit and cleanup runs failed with zero recorded steps. Validators were not weakened.


## 2026-09-21 — Super Soul 009 acquisition normalization
- Promoted the already source-backed PQ006 relationship into the canonical `super-soul-009` acquisition fields: `Parallel Quest` / `Parallel Quest 06` / `PQ 06 reward`.
- Preserved uncertainty: no drop percentage or special-drop condition was invented.
- Refreshed `last_verified` to 2026-09-21 and retained the existing sources while adding the maintained all-PQ reward guide.


## 2026-09-21 — Early Super Soul crosslink batch
- Reconciled canonical Super Souls 002, 004, and 007 against PQ002, PQ005, and PQ007 respectively using exact-name reward matches.
- Synchronized `parallel-quests-record-layer.json`, `pq-reward-relationships.json`, and `pq-super-soul-crosslink-report.json` in both directions.
- Normalized the three canonical Super Soul acquisition records to their PQ sources and explicitly preserved uncertainty about exact drop conditions/percentages.
- No Item Shop records (Super Souls 001, 003, 005, 006, 008) were forced into PQ relationships.


## 2026-09-21 — Super Soul 010–011 reconciliation
- Synchronized Super Soul 010 ("I'll kill all of you!!") with PQ022 and Super Soul 011 ("H-How could he?!") with PQ012.
- Added the missing structured `super_soul_rewards` entry to PQ012 and normalized both canonical Super Soul acquisition records to their source PQs.
- Preserved the existing bidirectional master/report relationships and did not force shop/NPC records 012–018 into PQ routes.


## 2026-09-21 — Super Soul 012–018 evidence-boundary audit
- Audited Super Souls 012–018 against all 186 canonical PQ reward records.
- No exact-name PQ reward matches were found, so no PQ relationships were manufactured.
- Preserved their existing non-PQ acquisition classifications and recorded the evidence boundary/verification date in the canonical Super Soul records.

## 2026-09-21 — Super Soul 024–047 crosslink audit
- Audited Super Souls 024–047 against the complete 186-PQ canonical reward layer.
- Confirmed PQ28 `Drop dead!!!` and the PQ185/PQ186 Super Soul reward mappings already represented in the canonical crosslink report; no additional PQ routes were inferred for the remaining records.
- Normalized Super Souls 032–035 to their exact-name PQ185/PQ186 reward provenance and refreshed verification dates.
- Preserved unresolved/non-PQ acquisition boundaries for Super Souls 024–030 and 036–047.

## 2026-09-21 — Super Soul 048-055 + PQ reverse-link reconciliation

- Added 8 canonical Super Soul records (super-soul-048 through super-soul-055): 40 ton weights!, Killed all Earthlings!, That's one down!, That offer's expired..., Why are you dodging?!, Guess you CAN fight..., Leave my daddy alone!, and Leave the rest to me!.
- Extended the Super Soul record layer with deterministic source_parallel_quests endpoints for all 13 currently PQ-sourced Super Soul records.
- Synchronized PQ58 and PQ131 with explicit super_soul_ids and super_soul_rewards endpoints.
- Updated docs/data/record-expansion-contract.json and docs/data/pq-super-soul-crosslink-report.json to formalize and audit the bidirectional relationship layer.
- Validation: 50 canonical Super Soul records; 13 forward / 13 reverse PQ↔Super Soul edges; 37 Super Souls remain without an explicit PQ endpoint; 0 broken relationship endpoints; 186 canonical PQ records; all changed JSON parsed successfully.
- Evidence limits: exact drop percentages were retained only where directly source-backed (including the documented 50% rolls for the two new PQ rewards); raid/shop/story acquisition details remain provenance-labeled rather than inferred.


## 2026-09-21 — Super Soul 056-063 + PQ reverse-link reconciliation

- Added 8 canonical Super Soul records (`super-soul-056` through `super-soul-063`).
- Synchronized PQ93, PQ160, and PQ180 with explicit Super Soul reward/ID endpoints.
- Rebuilt `docs/data/pq-super-soul-crosslink-report.json` from the live Super Soul registry: 16 forward / 16 reverse edges.
- Preserved evidence boundaries: Mix Shop, TP Medal Shop, and limited-time Raid routes remain provenance-labeled; the source corpus's community measurements are not promoted to exact canonical percentages where the effect text only specifies L/M/XL/XXL.
- Validation target for this bounded batch: canonical Super Soul count 58; no relationship endpoint should be orphaned.


## 2026-09-21 — Super Soul 064-071 + PQ reverse-link reconciliation

- Added canonical Super Soul records `super-soul-064` through `super-soul-071`: You can't win..., Thanks, Dende!, Flying Nimbus!!, Here it comes!, Now we're even., Just win, okay?, As if I'd lose!, and Buu Don't Wanna!.
- Synchronized PQ2, PQ105, PQ107, PQ118, and PQ133 with explicit Super Soul endpoints for the PQ-sourced records in this batch.
- Rebuilt `docs/data/pq-super-soul-crosslink-report.json` from the live Super Soul registry: **21 forward / 21 reverse edges**.
- Validation: **66 canonical Super Souls / 186 canonical PQs / 14 unique PQ endpoints / 21 unique Super Soul endpoints / 45 unresolved Super Soul routes / 0 broken relationship endpoints**. Changed JSON parsed successfully.
- Evidence limits preserved: source-backed acquisition types and quest identities were recorded without promoting community-measured percentages/durations to exact canonical values. No PQ relationship was inferred from character appearance or quest theme.


## 2026-09-21 — Super Soul 072-079 + PQ reverse-link reconciliation

- Added canonical Super Soul records `super-soul-072` through `super-soul-079`: Over here, you idiot..., That offer's expired..., Goku! Time for dinner!, That won't work on me!, I'll send you to Hell!!, Tien, please don't die, It's okay! I'll fix you!, and Leave my daddy alone!.
- Synchronized PQ135 with the explicit Super Soul endpoint for `That won't work on me!`; the other batch records retain their source-backed raid/shop/NPC acquisition routes without inferred PQ links.
- Rebuilt `docs/data/pq-super-soul-crosslink-report.json`: **22 forward / 22 reverse edges**, with **52** Super Souls lacking explicit PQ endpoints.
- Validation: **74 canonical Super Souls / 186 canonical PQs / 19 unique PQ endpoints / 22 unique Super Soul endpoints / 0 broken relationship endpoints**. Changed JSON parsed successfully.
- Evidence limits preserved: community-measured percentages/durations and disputed in-game magnitude interpretations were not promoted to exact canonical values. No PQ relationship was inferred from character appearance or quest theme.


## 2026-09-21 — Super Soul 080-087 + PQ reverse-link reconciliation

- Added canonical Super Soul records `super-soul-080` through `super-soul-087` from the maintained Madreag corpus.
- Synchronized PQ144 with `super-soul-080` and `super-soul-085`, PQ146 with `super-soul-086`, and PQ150 with `super-soul-087`.
- Rebuilt `docs/data/pq-super-soul-crosslink-report.json`: **26 forward / 26 reverse edges**.
- Validation: **82 canonical Super Souls / 186 canonical PQs / 22 unique PQ endpoints / 26 unique Super Soul endpoints / 56 unresolved routes / 0 broken endpoints**. Changed JSON parsed successfully.
- Evidence limits preserved: community measurements and the Zarbon recovery text-vs-behavior dispute remain explicitly non-canonical; no unsupported PQ relationships were inferred.


## 2026-09-21 — Super Soul 088-095 + PQ reverse-link reconciliation

- Added canonical Super Soul records `super-soul-088` through `super-soul-095` from the maintained Madreag corpus.
- Synchronized PQ147 with `super-soul-089`, PQ148 with `super-soul-090`, and PQ149 with `super-soul-088`.
- Rebuilt `docs/data/pq-super-soul-crosslink-report.json`: **29 forward / 29 reverse edges**.
- Validation: **90 canonical Super Souls / 186 canonical PQs / 25 unique PQ endpoints / 29 unique Super Soul endpoints / 61 unresolved routes / 0 broken endpoints**. Changed JSON parsed successfully.
- Evidence limits preserved: community measurements and source-text behavior disputes were not promoted to exact canonical values; raid/shop records without explicit PQ identity remain unresolved for PQ linkage.


## 2026-09-21 — Super Soul 096–103 frontier correction

- Reconciled the next Super Soul batch against the live Madreag source corpus before assigning IDs. The prior handoff candidate names were already represented by earlier canonical records, so no duplicates were created.
- Added canonical Super Souls 096–103: It must be some kind of trick..., It all comes down to this!, I'll keep adding a bit of power to my attacks!, You're not much of a fun fight!, I think I'm getting the hang of this., I will put a stop to you, fiend!, There's more where that came from!, and Emoc htorf! Peas and Carrots!.
- Synchronized PQ151, PQ152, and PQ153 with the five deterministic PQ-sourced records in this batch and rebuilt the bidirectional PQ↔Super Soul report.
- Validation: 98 canonical Super Souls; 34 forward / 34 reverse PQ↔Super Soul edges; 28 unique PQ endpoints; 64 unresolved Super Soul routes; 0 broken endpoints; changed JSON parsed successfully.
- Evidence limits preserved: raid/event records remain provenance-labeled; no unsupported recurrence schedule or drop percentage was promoted to canonical data.


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


### 2026-09-21 — Super Soul 144–151 frontier + PQ reverse-link reconciliation
- Live census before editing: **138 canonical Super Souls / 186 canonical PQs**; live IDs reached 143, so identity reconciliation was performed before assigning the next IDs.
- Added **8 unique** canonical records: super-soul-144 through super-soul-151. Damn it all! was already super-soul-062 and was not duplicated.
- Synchronized **PQ179, PQ182, PQ183, and PQ184** with their explicit Super Soul reward IDs.
- Rebuilt the PQ↔Super Soul report: **56 forward / 56 reverse edges / 46 unique PQ endpoints / 56 unique Super Soul endpoints / 90 unresolved routes / 0 broken endpoints**.
- Evidence limits preserved: no unsupported PQ links for Festival/TP Medal Shop acquisitions; community-measured magnitudes/durations remain bounded; the Poltarat damage-direction conflict remains explicit.
- Validation: changed JSON parsed successfully and the crosslink report was regenerated from the canonical registry. CI status was unavailable; no CI success is claimed.
- Exact next batch: **the next eight unique source-corpus Super Souls after Send me back to the planet I came from!, after live duplicate reconciliation.**

### 2026-09-21 — Super Soul 152–153 terminal source-corpus batch
- Added **super-soul-152** — So fast! Are they learning how to use their power?! — and **super-soul-153** — Enough food for one person... — from the final two unique records remaining after the prior source-corpus frontier.
- Both are 5th Festival of Universes Total Glory Point rewards with TP Medal Shop rotation; neither has an explicit PQ endpoint.
- Rebuilt the PQ↔Super Soul report: **56 forward / 56 reverse edges / 46 unique PQ endpoints / 56 unique Super Soul endpoints / 92 unresolved routes / 0 broken endpoints**.
- Evidence limits preserved: official/datamined trigger/effect classes are distinguished from community-measured magnitudes and durations; no unsupported PQ links were added.
- Validation: changed JSON parsed successfully; canonical/index parity and endpoint checks passed; internal UI/search citation artifact scan returned **0**. CI status remained unavailable; no CI success is claimed.
- Exact next work: **do not continue inventing Super Soul records from the exhausted maintained source corpus; pivot to the highest-priority deterministic validator/index mismatch or another explicitly prioritized repository corpus.**

### 2026-09-21 — Krillin/Tien/Yamcha/Piccolo mentor-skill reconciliation
- Promoted **14 deterministic mentor→skill edges** already represented by the canonical mentor lesson layer and skill-index source_mentor provenance: Krillin (2), Tien (4), Yamcha (4), Piccolo (4).
- Rebuilt `docs/data/mentor-skill-crosslink-report.json`: **33 mentors / 30 linked mentors / 30 edges / 30 linked skills / 0 unresolved / 0 broken endpoints**.
- No acquisition semantics were changed; this was a reverse-link/report reconciliation pass.
- Validation passed with JSON parsing and canonical skill-ID endpoint checks. CI status unavailable; no CI success claimed.
- Exact next batch: **Raditz, Gohan (Kid), Nappa, and Vegeta mentor mappings.**

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

## 2026-09-21 — Whis/Pan/Jaco/Goku mentor-skill reconciliation
- Promoted 13 deterministic mentor→skill relationship edges from the canonical mentor lesson mappings where the corresponding skill IDs and `source_mentor` provenance matched: Whis (4), Pan (3 new), Jaco (4), and Goku (2 new).
- Preserved existing Pan Dancing Parapara and Goku Spirit Bomb / Instant Transmission edges without duplication.
- Updated `docs/data/mentor-skill-crosslink-report.json`; canonical skill acquisition records were not rewritten.
- Live relationship census after the bounded batch: 33 mentors, 29 linked mentor identities, 116 edges, 116 unique skill endpoints, 0 unresolved, 0 broken endpoints.

## 2026-09-21 — Remaining mentor relationship reconciliation
- Promoted 15 deterministic mentor→skill edges for Gohan (Future) (4), Bardock (4), Bojack (4), and Zamasu (3).
- Zamasu's initiation lesson has no canonical skill ID and remains intentionally unlinked.
- Mentor crosslink report now validates 33 canonical mentors, 33 linked mentors, 131 edges, 131 unique endpoints, 0 unresolved, and 0 broken endpoints.

## 2026-09-21 — Skill acquisition projection normalization
- Reconciled three deterministic `source_quest` projection gaps in `docs/data/skills-index.json`: Drain Field → PQ95, Flash Bomber → PQ95, and Rakshasa's Claw → PQ57.
- The values already existed in canonical `docs/data/skills.json`; no acquisition semantics or evidence state were changed.
- Cross-layer validation now finds zero `skills.json` source-quest values missing from the skill index.


## 2026-09-21 — Mentor skill DLC provenance cleanup
- Refined the four previously generic `DLC` skill provenance values: God Splitter, Heavenly Arrow, and Instant Severance → Extra Pack 1; Time Skip/Tremor Pulse → Super Pack 1.
- Canonical file: `docs/data/skills.json`; no skill-index projection change was required.
- Validation: 429 skills; 0 missing DLC provenance; 0 generic `DLC` values remaining. CI status unavailable; no CI success claimed.
- Commit: `9ca5147646a60ceb411dfca5dfdfb924e8a566d2`.

### 2026-09-21 — Skill-index source/restriction projection correction
- Reconciled five deterministic projection values in `docs/data/skills-index.json` with canonical `docs/data/skills.json`: Data Input (EM-20), Final Pose (PQ74), Super Spirit Bomb (EM-16), Supernova (EM-6), and Ill Bomber's race restriction (Majin).
- No acquisition semantics or unresolved evidence were changed; this was a bounded generated-index synchronization pass.
- Validation: 429 canonical skills / 429 index records; the targeted values match at the validated commit. CI status unavailable; no CI success claimed.
- Commits: `ad2bd70044d982245819621ea63c66116ffc1490`, `53959c1bfcf0bbb0c67d6625bdb7c429cd643c0e`, `1edc204ca3a085a19747ea79337833696102c39c`.



### 2026-09-21 — skills-index projection parity

- Corrected 10 deterministic last_verified values in docs/data/skills-index.json to match canonical docs/data/skills.json.
- Scope: Become Giant, Dancing Parapara, Darkness Rush (Melee), Darkness Rush (Ranged), Data Input, Deadly Dance, Death Ball, Destructo-Disc, Dimension Cannon, Dragon Spiral.
- No new gameplay, acquisition, restriction, or DLC claims were introduced.
- Commit: a14d8a7025124ca12a54e55c4b4ba9ffa701cf15.


### 2026-09-21 — skills-index last_verified projection parity batch 2
- Corrected 10 deterministic `last_verified` values in `docs/data/skills-index.json` to match canonical `docs/data/skills.json`: Energy Charge, Final Pose, Full Power Charge, Galick Gun, Indomitable, Instant Transmission, Masenko, Maximum Charge, Perfect Shot, and Potential Unleashed.
- No new gameplay, acquisition, restriction, or DLC claims were introduced.
- Validation: 429 canonical skills / 429 index records; 10 targeted values match; 10 broader `last_verified` mismatches remain for the next bounded pass. CI status unavailable; no CI success claimed.
- Commit: `124138ef8edeba905223caa0cb4b6de2082f69f5`.


### 2026-09-21 — skills-index projection parity batch 3
- Corrected 10 deterministic `last_verified` values in `docs/data/skills-index.json` to match canonical `docs/data/skills.json`: Rise to Action, Shadow Crusher, Spirit Bomb, Super Spirit Bomb, Supernova, The Power to Overcome, Time Skip/Back Breaker, Time Skip/Flash Skewer, Time Skip/Jump Spike, and Venus Fist.
- Validation: 429 canonical skills / 429 index records; the live targeted field comparison now has **0 `last_verified` mismatches**; no internal citation artifacts were introduced.
- Commit: `0865f3d3f7a7281c81effdd0b27e6d7cb2cdd76a`.


### 2026-09-21 — skills-index source_parallel_quests projection parity
- Corrected 5 deterministic `source_parallel_quests` values in `docs/data/skills-index.json` to match canonical `docs/data/skills.json`: Candy Beam, Kamehameha, Mach Dash, Time Control, and Warp Kamehameha.
- Validation: 429 canonical skills / 429 index records; the targeted projection family now has **0 mismatches** and no internal citation artifacts.
- Commit: `69404599e87914ea5dafe993a154d1e86b0312c9`.


### 2026-09-21 — skills-index source provenance projection parity
- Corrected 3 deterministic `sources` projections in `docs/data/skills-index.json` for God Splitter, Heavenly Arrow, and Instant Severance to match canonical provenance, including the existing Zamasu source.
- Validation: 429 canonical skills / 429 index records; targeted source parity is clean and no internal citation artifacts were introduced.
- Commit: `20b6a147dae05e99a4b6aa218586709a23f55115`.


### 2026-09-21 — skills-index mechanics projection parity batch 1
- Live census: **429 canonical skills / 429 skill-index records**.
- Bounded deterministic batch: **10 `mechanics_notes` projections** — Brutal Buster, Crush Cannon, Crush Stream, Dancing Parapara, Darkness Rush (Melee), Darkness Rush (Ranged), Data Input, Deadly Dance, Death Ball, and Destructive Fission.
- Evidence: canonical `docs/data/skills.json` is the producer for the index projection; no new gameplay or acquisition claim was introduced.
- Changes: copied only the canonical `mechanics_notes` values into the corresponding `docs/data/skills-index.json` records.
- Evidence limits: deterministic cross-layer parity correction, not a new verification event; remaining projection drift is intentionally left for later bounded batches.
- Validation: both JSON layers parse; record counts remain **429/429**; all 10 targeted `mechanics_notes` values now match canonical; changed index contains **0 internal AI/UI/search citation artifacts**.
- CI: not yet inspected for this commit; do not claim CI success.
- Commit: `467a1148188343c36df72043bd959482d10f866f`.
- Exact next batch: **recompute the live projection census and continue with the next bounded `mechanics_notes` mismatch family; preserve canonical values and do not regenerate unrelated fields.**


### 2026-09-21 — skills-index mechanics projection parity batch 2
- Corrected 10 deterministic `mechanics_notes` projections in `docs/data/skills-index.json` to match canonical `docs/data/skills.json`: Destructo-Disc, Dimension Cannon, Double Crush, Drain Field, Energy Charge, Final Pose, Flash Bomber, Full Power Charge, Galick Gun, and Ill Bomber.
- Validation: 429 canonical skills / 429 index records; all 10 targeted values match; 15 broader `mechanics_notes` mismatches remain; no internal citation artifacts were introduced.
- CI status unavailable; no CI success claimed.
- Commit: `84d44bd4441d9d178eea9c6208803cd80dce7aca`.


### 2026-09-21 — skills-index mechanics projection parity batch 3
- Corrected 10 deterministic `mechanics_notes` projections in `docs/data/skills-index.json` to match canonical `docs/data/skills.json`: Instant Transmission, Masenko, Maximum Charge, Neo Wolf Fang Fist, Perfect Shot, Potential Unleashed, Rakshasa's Claw, Rise to Action, Shadow Crusher, and Spirit Bomb.
- Validation: 429 canonical skills / 429 index records; all 10 targeted values match; **5** broader `mechanics_notes` mismatches remain; no internal citation artifacts were introduced.
- CI status unavailable; no CI success claimed.
- Commit: `5a9f4bf24d6efeafed6da3543e817ad0734f3a32`.


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

## 2026-09-21 — Skill-index notes projection parity

- Synchronized the four remaining canonical-to-index notes projections for God Splitter, Heavenly Arrow, Instant Severance, and Time Skip/Tremor Pulse.
- The change is deterministic: index notes now match canonical docs/data/skills.json, including the already-recorded mentor DLC provenance refinement.
- No new gameplay, acquisition, restriction, or DLC claim was introduced.
- Validation: 429/429 skill records parse successfully; targeted notes parity is 0 mismatches; no internal AI/UI/search citation artifacts were found in the edited index.

## 2026-09-21 — Skill identity and projection integrity cleanup

- Removed the duplicate III Bomber placeholder that shared skill-ill-bomber with the richer Ill Bomber record.
- Canonical and index skill counts are now 428/428 with zero duplicate IDs.
- Full inspected canonical-to-index projection parity is clean; no gameplay or acquisition semantics were changed.

## 2026-09-21 — Nullable CaC race-scope audit

- Audited Blaster Stream, Chaotic Time Impact, and Circle Flash, the three remaining nullable `race_restriction` skill records.
- Existing evidence establishes CaC usability for all three but does not establish a narrower race/gender/form restriction. Preserved `null` rather than inferring universal race availability.
- Added explicit evidence-boundary notes to canonical and index records; canonical/index parity remains clean.

## 2026-09-21 — PQ141-PQ150 research-batch coverage repair

- Added the missing PQ141-PQ150 research batch with ten individually sourced records, DLC provenance, objectives, documented rewards, and conservative DLC-era unlock metadata.
- Reconciled PQ144's incomplete canonical reward inventory against the maintained Steam all-PQ guide and synchronized the new research batch.
- Canonical PQ coverage remains 186/186; the previously missing research range is now represented.

## 2026-09-21 — PQ18-PQ20 reward reconciliation

- Reconciled the canonical reward inventories for PQ18-PQ20 against the maintained research batch.
- Added the documented basic rewards and skill rewards already present in repository research data, while preserving unresolved individual drop-slot/probability semantics.
- Refreshed verification metadata and source provenance for the three records.

## 2026-09-21 — PQ21-PQ30 reward reconciliation

- Compared canonical PQ21-PQ30 rewards with research batch 03.
- Repaired the one actionable cross-layer omission: PQ22 `Energy Shot` in the research batch's `skill_rewards`.
- Preserved unresolved reward-slot/drop-probability semantics.

## 2026-09-21 — Mentor skill Ki-cost verification

- Added verified Ki costs for eight mentor-training skills: Evil Explosion, Super Explosive Wave, Light Grenade, Special Beam Cannon, Dodon Ray, Volleyball Fist, Tri-Beam, and Neo Tri-Beam.
- Preserved variable-cost mechanics and unresolved records rather than filling values by inference.

## 2026-09-21 — Mentor skill Ki-cost verification batch 2
- Verified Ki costs for Fake Death (0), Wolf Fang Fist (100), Ki Blast Thrust (100), Spirit Ball (300), Bomber DX (100), Arm Crash (100), Genocide Shell (100), and Break Cannon (300+).
- Refreshed canonical verification dates; preserved Break Cannon's variable-cost form.
- Kept the generated skill index scoped to its established projection fields rather than introducing a new Ki-cost projection.

## 2026-09-21 — Raditz mentor skill Ki-cost verification
- Verified Double Sunday (100), Saturday Crash (100), Shining Friday (100), and Weekend (300) Ki costs from current skill references.
- Updated only canonical Ki-cost and verification-date fields; unresolved mechanics remain untouched.

## 2026-09-21 — Zarbon mentor skill Ki-cost verification
- Verified Audacious Laugh (100), Gorgeous Shot (100), Bloody Counter (0 base/held-cost mechanic preserved), and Elegant Blaster (300) Ki costs.
- Updated only canonical Ki-cost and verification-date fields; held/variable behavior was not flattened into a fabricated fixed cost.

## 2026-09-21 — Dodoria mentor skill Ki-cost verification
- Verified Dodoria Beam (100), Critical Upper (100), Dodoria Headbutt (100), and Dodoria Launcher (300) Ki costs from current skill references.

## 2026-09-21 — Frieza mentor skill Ki-cost verification
- Verified Death Beam (100), Death Crasher (100), and Death Slicer (100) Ki costs from current skill references.
- The live canonical census contained three null-cost Frieza mentor records, so no unsupported fourth record was added.

## 2026-09-21 — Cooler mentor skill Ki-cost verification
- Verified Feint Crash (100), Fake Blast (100), and Supernova Cooler (500) Ki costs.


## 2026-09-21 — Majin Buu mentor skill Ki-cost verification

- Verified Ki costs for **Innocence Bullet (100)**, **Angry Hit (100)**, **Innocence Cannon (100)**, and **Innocence Breath (300)** from current Xenoverse 2 skill references.
- Updated only canonical `ki_cost` and `last_verified` fields; mentor acquisition provenance and unresolved mechanics were preserved.
- Live canonical skill census remains **428 records** with **74 nullable `ki_cost` records** after the bounded pass.
- Commit: `cc61629f11788b994cbddc8ba246ba552f6b97b1`.

## 2026-09-21 — Beerus mentor skill Ki-cost verification

- Verified Ki costs for **God of Destruction's Anger (200)**, **God of Destruction's Rampage (100)**, **God of Destruction's Wrath (100)**, and **Sphere of Destruction (300)** from current Xenoverse 2 skill references.
- Updated only canonical `ki_cost` and `last_verified` fields; no mechanics, acquisition, restriction, or variable-cost semantics were changed.
- Live canonical skill census after the bounded pass: **428 records, 0 duplicate IDs, 41 nullable `ki_cost` records**.
- Commit: `af4e6c1ee72c3f4eb7a930de0030df03ace7caa3`.
