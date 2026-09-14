# Exhaustive Dragon Ball Xenoverse 2 Wiki Plan

This project is being built as an exhaustive database/wiki rather than a collection of summary pages. Coverage means the underlying records, relationships, acquisition paths, mechanics, provenance and verification state are represented.

## Core principles

1. **Coverage before prose.** Every expected entity gets a canonical record before detailed writeups are considered complete.
2. **Indexed is not verified.** Category membership or a secondary source can establish an indexed record, but mechanics, costs, requirements and rewards are promoted only after verification.
3. **Conflicts are data.** If reputable sources disagree, preserve the conflict and identify what still needs verification instead of silently choosing a value.
4. **Cross-link everything.** Skills, quests, characters, mentors, DLC, shops, rewards and equipment should point to one another through stable identifiers.
5. **Automate completeness checks.** Duplicate names, missing sources, missing categories, broken references and stale audits should be detectable by scripts/CI.

## Exhaustive scope

### Skills and combat data
- All Super, Ultimate, Evasive, Power-Up, Counter and Awoken skills.
- Race-restricted, cast-exclusive, boss/raid-exclusive, festival and unavailable-for-CaC skills.
- Variants and alternate names.
- Ki/stamina costs, damage type, activation conditions, mechanics, combo notes, PvE/PvP notes and exact acquisition.
- Dual Ultimates and relationships between mentor, cast and DLC sources.

### Content databases
- Characters, forms, presets and playable/cast status.
- Mentors, lessons, friendship, unlocks and rewards.
- Parallel Quests, Ultimate Finishes, objectives, enemies and complete reward pools.
- Expert Missions, raid battles and Crystal Raids.
- Story, Future Saga and Time Rift progression.
- DLC packs/passes and every included content item.

### Items and progression
- Super Souls, QQ Bangs, clothing, accessories and costumes.
- Skill Shop and TP Medal Shop inventories, rotations and historical availability.
- Capsules, mixing materials and currencies.
- Shenron wishes and Dragon Ball acquisition/progression.
- Races, attributes, levels, advancement tests and Conton City systems.
- Partner customization, keys and customization options.

### Reference and guide systems
- Maps and locations.
- Achievements/trophies.
- Combat/system mechanics.
- Farming routes and evidence-based builds.
- Update/DLC history.

## Data quality states

- `indexed`: record exists because category/source membership was established; details still require verification.
- `partially_verified`: some mechanics or acquisition fields have been checked, but the record is incomplete.
- `verified`: required factual fields have been checked against an authoritative or corroborated source set.

## Required relationship model

Examples:

- Skill -> source quest/shop/mentor/DLC/character.
- Quest -> rewards/skills/Super Souls/clothing/capsules/enemies/objectives.
- Character -> forms/presets/skills/DLC/PQ availability.
- Mentor -> lessons/skills/friendship/unlocks.
- Super Soul -> source/effect/activation condition/DLC.
- QQ Bang -> clothing/materials/mixing outcome.
- DLC -> characters/PQs/skills/items/Super Souls.

## Audit gates

Before a domain is declared exhaustive:

- Expected category/record count reconciles with the source index.
- No unintended duplicate canonical records remain.
- Every record has provenance.
- Required fields are present or explicitly marked unknown.
- Cross-references resolve.
- Source conflicts are tracked.
- The domain's last-audited date is current.
- CI/audit output is clean or known exceptions are documented.

## Current priority order

1. Finish the skill universe and source/category audit.
2. Establish automated coverage and duplicate/reference checks.
3. Expand Characters, Mentors, PQs, Expert Missions, Super Souls and QQ Bangs to record-level coverage.
4. Expand DLC, Story/Future Saga, Shenron, shops, clothing/equipment and partner customization.
5. Add raids, Crystal Raids, achievements, maps and deeper mechanics.
6. Promote indexed records to partially verified and verified as evidence is collected.
