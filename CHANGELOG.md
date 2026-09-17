# Changelog

## September 2026 (Ongoing Expansion)
- Added **Skill Research Batch 47** with five early/base-game skills from PQ29-PQ34: **Freedom Kick**, **Energy Field**, **Energy Barrier**, **Death Psycho Bomb**, and **Paralysis**.
- Duplicate-checked all five selected names against the live repository before addition; no code-search matches were returned.
- Cross-checked the batch against the maintained PQ reward transcription, current Xenoverse 2 skill-specific references, and independent Future Warrior/technique references.
- Preserved unresolved reward-slot and Ultimate-Finish semantics instead of inferring them. **Paralysis** also has a classification conflict across current references (Strike Ultimate vs. Super), so it remains `partially_verified` with the disagreement documented in its provenance.
- Batch 47 also records the already-established **Freedom Kick PQ29 correction** while leaving the historical Batch 17 and correction Batch 35 intact for auditability.

- Added **Skill Research Batch 46** with five early/base-game skills from PQ24-PQ28: **Double Death Slicer**, **Spirit Explosion**, **Crazy Finger Shot**, **Sauzer Blade**, and **Spread Shot Retreat**.
- Duplicate-checked all five selected names against the live repository before addition; no code-search matches were returned.
- Cross-checked Batch 46 against the current Xenoverse 2 skill guide, independent PQ reward transcriptions, and skill-specific references. Unsupported reward-slot semantics and Ultimate-Finish requirements remain unresolved.
- Double Death Slicer has player reports connecting acquisition to the Ultimate Finish, but the batch intentionally keeps `ultimate_finish_required` unresolved rather than converting anecdotal reports into canonical reward metadata.

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

- Added **Skill Research Batch 42** with five early/base-game PQ skills: **Recoome Eraser Gun**, **Mach Kick**, **Fighting Pose J**, **Time Control**, and **Unrelenting Barrage**.
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

- Added **Skill Research Correction Batch 37** to preserve Batch 36's historical research while correcting the final-DLC acquisition mapping.
- Added **Skill Research Batch 36** for the final DLC, **Future Saga Chapter 4**: **Dragon Spiral**, **Indomitable**, **Venus Fist**, and **The Power to Overcome**.
- Fixed `scripts/build_skills_from_research.py` so correction records can remove an obsolete canonical record when a correction changes its uniqueness key.
