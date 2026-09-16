# Exhaustive Dragon Ball Xenoverse 2 Wiki Plan

This project is being built as an exhaustive database/wiki rather than a collection of summary pages. Coverage means the underlying records, relationships, acquisition paths, mechanics, provenance and verification state are represented **and** the reader-facing pages contain substantial prose explaining what each thing is, how it works, where it comes from, and how it connects to the rest of the game.

## Core principles

1. **Coverage before prose, then hard prose.** Every expected entity gets a canonical record, followed by a real writeup rather than a one-line placeholder.
2. **Indexed is not verified.** Category membership or a secondary source can establish an indexed record, but mechanics, costs, requirements and rewards are promoted only after verification.
3. **Conflicts are data.** If reputable sources disagree, preserve the conflict and identify what still needs verification instead of silently choosing a value.
4. **Cross-link everything.** Skills, quests, characters, mentors, DLC, shops, rewards and equipment should point to one another through stable identifiers.
5. **Search must be blanket search.** A reader should be able to type a broad term such as `Ki`, `Goku`, `Super Saiyan`, `Ultimate Finish`, `TP Medal`, `mentor`, `stamina break`, or a quest number and receive pages that actually discuss the term. Search ranks exact titles first, then descriptions, page text and paths, and also matches individual words in multi-word queries.
6. **Automate completeness checks.** Duplicate names, missing sources, missing categories, missing required prose sections, broken references and stale audits should be detectable by scripts/CI.

## Hard-writing standard

A canonical entity is not considered reader-complete just because it appears in a table or JSON file. Each individual record should eventually have enough written information to answer the questions a player would reasonably ask.

### Skills
Every skill writeup should cover, where the evidence exists:

- What the move does and what makes it distinct.
- Skill type: Super, Ultimate, Evasive, Awoken, Power-Up, Counter, Grab, or other applicable category.
- Activation/input behavior and important timing details.
- Ki and/or stamina costs.
- Damage/mechanical behavior and notable secondary effects.
- Follow-ups, charged/alternate versions, combo interactions and restrictions.
- CaC availability versus cast/boss/raid-only availability.
- Exact acquisition route, including the specific quest, mentor lesson, shop or DLC source.
- Practical PvE/PvP considerations without pretending subjective advice is a verified fact.
- Known patches or version-dependent behavior.
- Related skills, characters, quests, mentors, Super Souls and DLC.
- Source and verification state.

### Missions and quests
Every mission writeup should cover:

- Mission number and name.
- Unlock/progression route.
- Map/arena and starting conditions.
- Main objectives and failure conditions.
- Enemy waves and reinforcements in encounter order.
- Time/health/condition triggers.
- Ultimate Finish requirements and what changes when they are met.
- Full known reward pool, separating normal rewards from Ultimate Finish rewards when evidence supports the distinction.
- Skill, Super Soul, clothing, accessory, material and currency rewards.
- Farming notes and known efficient approaches.
- Related characters, skills and DLC.
- Verification state and source trail.

### Characters
Every character/form/preset record should eventually explain:

- Identity and source material/context where useful.
- Race/species and form.
- Playable, NPC, boss, partner or other status.
- Preset/form distinctions and alternate variants.
- Unlock route and prerequisites.
- Equipped/associated skills and Awoken state when documented.
- DLC/free-update/event provenance.
- Partner Customization availability and key requirements when applicable.
- Character-exclusive rewards or skills.
- Relevant quests, story appearances and relationships.
- Naming aliases that matter for searching.
- Verification state and source trail.

### Every other domain
The same standard applies to mentors, Super Souls, QQ Bangs, clothing, accessories, items, shops, DLC, story chapters, Future Saga content, raids, Expert Missions, Conton City locations, Shenron wishes, advancement tests, attributes, races, mechanics, glitches, achievements and farming methods.

If a page only says **what something is** but does not explain **how to obtain it, how it works, what it connects to, and what is known/unknown**, it is still an incomplete writeup.

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

## Search architecture

The published site now has a generated `/search-data.json` index built from the Jekyll pages and a client-side full-text search interface at `/Search/`. The same search entry point is exposed in wiki navigation so users do not have to know which category contains an answer.

Search is intentionally broad rather than category-locked. As the written corpus grows, adding a new skill, mission, character or mechanics section automatically makes its terminology searchable through the generated index.

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
- Required hard-writing sections exist or are explicitly marked not yet researched.
- Cross-references resolve.
- Source conflicts are tracked.
- The domain's last-audited date is current.
- CI/audit output is clean or known exceptions are documented.

## Current priority order

1. Finish the skill universe and source/category audit.
2. Establish automated coverage, duplicate, prose-completeness and reference checks.
3. Expand Characters, Mentors, PQs, Expert Missions, Super Souls and QQ Bangs to record-level coverage **with individual hard-written entries**.
4. Expand DLC, Story/Future Saga, Shenron, shops, clothing/equipment and partner customization.
5. Add raids, Crystal Raids, achievements, maps and deeper mechanics.
6. Promote indexed records to partially verified and verified as evidence is collected.
7. Keep the search corpus growing with the written corpus so every new fact becomes discoverable by its natural terminology.
