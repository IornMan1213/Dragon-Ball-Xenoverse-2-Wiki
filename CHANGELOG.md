# Changelog

## September 2026 (Ongoing Expansion)
- Added **Skill Research Batch 38** with five previously unrecorded skills found absent from the live repository search: **Drain Charge**, **Hyper Drain**, **Life Absorption**, **Energy Release**, and **Flash Bomber**.
- Duplicate-checked all five selected names against the live repository before addition; **0 repository-search matches** were found.
- Reconciled Batch 38 against current Xenoverse 2 references. Drain Charge, Hyper Drain, and Flash Bomber have documented acquisition/cost data; Energy Release remains partial because its current reference does not establish a CaC route or resource cost; Life Absorption remains partial because current reference variants disagree on the health-drain percentage.
- Preserved the Life Absorption 5%-vs-10% discrepancy instead of choosing an unsupported canonical value.
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

- Added **Skill Research Batch 17** with five previously uncovered early/base-game PQ skills: **Heat Dome Attack**, **Freedom Kick**, **Rolling Bullet**, **Super Drain**, and **Justice Pose**.
- Duplicate-checked Batch 17 against the current canonical skill catalog and repository search before addition; **0 duplicates** were found for the selected records.
- Reconciled Batch 17 acquisition and core identity/mechanics against multiple Xenoverse 2 references. **Heat Dome Attack** and **Super Drain** were promoted to `verified`; **Freedom Kick**, **Rolling Bullet**, and **Justice Pose** remain `partially_verified` where technical details remain unresolved.
- Re-verified the Batch 16 research layer while preparing Batch 17; no corrections were required.
- Added Batch 17 to `docs/data/skill-research-batches/skill-batch-17.json` so it participates in the repository's curated skill research pipeline.

- Added **Skill Research Batch 16** with five previously uncovered early/base-game skills: **Mach Punch**, **Fighting Pose E**, **Mystic Flash**, **Energy Shot**, and **Ginyu Force Special Combo**.
- Duplicate-checked the selected Batch 16 records against the current canonical skill response and repository search before addition; **Evil Flight Strike was explicitly excluded because it was already indexed**.
- Reconciled Batch 16 identity, classification, acquisition route, resource cost, and core mechanics against multiple Xenoverse 2 references and corroborating research. Exact reward probabilities were not inferred where the sources did not establish them.
- Added Batch 16 to `docs/data/skill-research-batches/skill-batch-16.json` as the next canonical research layer for the skill catalog.

- Added **Skill Research Batch 15** with five previously uncovered base-game skills: **Dodoria Headbutt**, **Earth Splitting Galick Gun**, **Milky Cannon**, **Recoome Kick**, and **Time Control**.
- Duplicate-checked Batch 15 against `docs/data/skills.json` and prior skill research batches before addition; no duplicates were found.
- Reconciled Batch 15 identity, category, acquisition, resource cost, and core mechanics against current Xenoverse 2 skill references plus corroborating research sources. The five records are marked `verified` for their documented core fields; exact community damage measurements remain outside the promoted claims.
