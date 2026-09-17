# Changelog

## September 2026 (Ongoing Expansion)
- Added **Skill Research Batch 43** with five previously absent early/base-game PQ skills: **Meteor Blow**, **Earth Splitting Galick Gun**, **Meteor Crash**, **Fighting Pose C**, and **Kaioken Kamehameha**.
- Duplicate-checked all five selected names against the live repository before addition; **0 repository-search matches** were returned for each.
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
- Kept Batch 38 records `partially_verified` pending independent reconciliation of remaining reward-slot, acquisition, and technical fields.

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
