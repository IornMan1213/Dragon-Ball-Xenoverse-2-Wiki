# Changelog

## September 2026 (Ongoing Expansion)
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
- Reconciled Batch 16 identity, classification, acquisition route, resource cost, and core mechanics against current Xenoverse 2 references and corroborating research. Exact reward probabilities were not inferred where the sources did not establish them.
- Added Batch 16 to `docs/data/skill-research-batches/skill-batch-16.json` as the next canonical research layer for the skill catalog.

- Added **Skill Research Batch 15** with five previously uncovered base-game skills: **Dodoria Headbutt**, **Earth Splitting Galick Gun**, **Milky Cannon**, **Recoome Kick**, and **Time Control**.
- Duplicate-checked Batch 15 against `docs/data/skills.json` and prior skill research batches before addition; no duplicates were found.
- Reconciled Batch 15 identity, category, acquisition, resource cost, and core mechanics against current Xenoverse 2 skill references plus corroborating research sources. The five records are marked `verified` for their documented core fields; exact community damage measurements remain outside the promoted claims.
- Updated `scripts/build_skills_from_research.py` so repository-curated `skill-batch-*.json` research records are imported into the generated canonical skill catalog rather than remaining disconnected staging data.
- Updated `.github/workflows/skills-sync.yml` so curated skill research batches trigger the canonical build/validation workflow.
- Continued to preserve curated fields and verification states when external structured research is merged, preventing a weaker external record from overwriting a stronger repository record.

- Staged **Super Soul research batch 03** at `docs/data/super-souls-research-batch-03.json` with eight additional records (Burter, Jeice, Ginyu, Nail, Dende, Piccolo, Frieza, and Kid Gohan) kept at `partially_verified` pending acquisition/current-version reconciliation.
- Expanded `docs/Super-Souls-Database.md` to document the staged-batch workflow and canonical-vs-staged distinction so research additions are not mistaken for fully reconciled canonical records.
- Continued independent-source reconciliation for the new Super Soul batch using the current Xenoverse 2 Super Soul catalogue plus historical GameFAQs and NPC/world references where applicable.
- Conton City page expanded with key areas, shops, systems, and Time Rifts.
- Super Souls page expanded with acquisition methods, useful categories, and farming tips.
- Mentors, Parallel Quest Walkthrough, Skills Database, and other core pages previously strengthened.
- Added skill research batches 01–14, with duplicate checks performed before the recent batches.
- Audited Skill Research Batch 13 against the external datamined research corpus and independent references.
- Promoted **All Clear**, **Angry Hit**, and **Burst Blitz** to `verified` after corroborating their core identity/acquisition facts.
- Kept **Angry Explosion** and **Angry Shout** as `partially_verified` because current reward/damage details still need independent reconciliation.
- Audited Skill Research Batch 10 against independent references; core facts were reconfirmed without promoting records where CaC/version-sensitive evidence remained unresolved.
- Added **Batch 14** with **Afterimage**, **Aura Slide**, **Big Bang Knuckle**, **Burning Attack**, and **Super Afterimage**.
- Promoted **Aura Slide**, **Big Bang Knuckle**, and **Burning Attack** to `verified` after corroborating core identity, acquisition, and mechanics.
- Kept **Afterimage** and **Super Afterimage** `partially_verified` where acquisition or technical interactions still need stronger reconciliation.
- Added a new homepage **Research Standard** section explaining exhaustive coverage, evidence states, cross-linking, and search-oriented organization.
- Added responsive styling for the new research-standard panel in `docs/assets/home.css`.
- Expanded `docs/DLC-Overview.md` into an encyclopedia-level DLC index covering Future Saga Chapters 1–4, DLC families, paid-vs-free provenance, content audit requirements, evidence layers, and downstream record expectations.
- Explicitly separated DLC ownership from in-game unlock conditions so later character, skill, PQ, Super Soul, costume, and system records can retain both facts.
- Added a DLC content audit matrix covering characters, skills/Awokens, PQs, Extra Missions, Super Souls, equipment, illustrations, stages, systems, and events/raids.
- Added the Dragon Ball DAIMA paid-DLC versus free-update distinction to the DLC research standard.
- Added an **Expert Missions** system foundation with unlock/count uncertainty, boss-mechanic taxonomy, reward/economy categories, cross-system relationships, verification rules, and an individual mission-record template.
- Added a current **20-mission Expert Mission index** with first-pass boss/reward mapping and explicit research states.
- Added an **Expert Mission status callout** to the homepage with responsive styling so the new research track is visible from the main entry point.
- Removed an accidental external citation-artifact insertion from `docs/Expert-Missions.md` before continuing the cycle.
- Added the first **individual Expert Mission research layer for EM16–20**, with structured identity, boss/encounter data, timer/mechanic notes, reward layers, strategy evidence, unknown fields, source reconciliation, and explicit `partially_verified` status.
- Linked the EM16–20 research page from the main Expert Mission index.
- Updated `TODO.md` to track deeper EM16–20 verification and the upcoming EM01–15 individual records.
- Added an explicit **Exhaustive Game Encyclopedia** scope standard to `TODO.md`: the project is intended to document every documented detail of Xenoverse 2, with structured labels, provenance, uncertainty tracking, and distinctions such as CaC vs character-only, DLC ownership vs unlock method, normal vs Ultimate Finish rewards, and known exceptions.
- Updated the delivery strategy so coverage of under-documented game systems remains active alongside skill/PQ research rather than allowing the current batch focus to narrow the wiki's scope.
- Continued provenance-first research: unresolved values are kept explicitly uncertain instead of being invented or silently promoted.
