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
