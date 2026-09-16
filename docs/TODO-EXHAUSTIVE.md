# EXHAUSTIVE / EXCESSIVE WIKI TODO

> **Theme:** exhaustive and excessive. Nothing is considered “done” merely because a name exists in an index. A finished domain needs coverage, hard writing, relationships, sources, verification, searchability, and quality checks.
>
> **Status vocabulary:** `[ ]` not started · `[~]` in progress / partially complete · `[x]` completed and checked · `[?]` blocked or awaiting evidence.

## 0. Master completion rules

- [ ] Every canonical entity has an individual reader-facing record or is explicitly documented as a non-entity/source artifact.
- [ ] Every record has a stable ID/name and canonical category.
- [ ] Every factual record has provenance/source URLs.
- [ ] Every record has verification status: `indexed`, `partially_verified`, or `verified`.
- [ ] No unsupported mechanics, costs, unlocks, rewards, dates, or restrictions are invented.
- [ ] Conflicting sources are preserved and documented rather than silently reconciled.
- [ ] Every domain has expected-count vs actual-count reconciliation.
- [ ] Every domain has duplicate detection.
- [ ] Every domain has missing-field detection.
- [ ] Every domain has cross-reference validation.
- [ ] Every domain has hard-writing completeness checks.
- [ ] Every domain is represented in blanket search.
- [ ] Search finds body-text mentions, not just page titles.
- [ ] Aliases, alternate spellings, abbreviations, old names and common player terminology are indexed.
- [ ] Every page has useful navigation to related records.
- [ ] Every source artifact is free of internal ChatGPT/file citation markers.
- [ ] Every generated index is reproducible from source data.
- [ ] Every audit has a date and result.
- [ ] Every “complete” claim is backed by an explicit audit.

---

# 1. Search / information architecture

- [x] Add dedicated `/Search/` page.
- [x] Add Search Everything navigation throughout the site.
- [x] Make search-first homepage.
- [ ] Verify generated `search-data.json` contains every published Markdown/HTML entity page.
- [ ] Verify search corpus contains JSON-backed records that do not yet have dedicated pages.
- [ ] Add weighted title/name matching.
- [ ] Add description/body/path matching.
- [ ] Add multi-word AND/OR query behavior and document it.
- [ ] Add aliases and alternate names to search records.
- [ ] Add category/type badges to search results.
- [ ] Add verification-status badges to results.
- [ ] Add breadcrumbs/path information to results.
- [ ] Add search filters for Skills / Characters / Quests / Items / Mechanics / Guides / DLC / etc.
- [ ] Add query highlighting in result excerpts.
- [ ] Add “no result” suggestions based on partial matches.
- [ ] Add typo-tolerant matching where practical.
- [ ] Add exact-name result pinning.
- [ ] Add stable URL/query-state for searches.
- [ ] Audit mobile search UX.
- [ ] Audit search performance with the full corpus.
- [ ] Add a search-index audit that fails on missing published pages.

# 2. Skills — exhaustive universe

## 2.1 Inventory and reconciliation

- [~] Maintain master `skills.json` seed index.
- [~] Preserve source category counts.
- [ ] Reconcile all skill categories against current source material.
- [ ] Determine the canonical unique skill count after removing duplicate category membership.
- [ ] Identify skills that appear in multiple categories.
- [ ] Identify category artifacts, redirects, templates and navigation pages accidentally counted as skills.
- [ ] Identify DLC-only skills.
- [ ] Identify free-update skills.
- [ ] Identify event/Festival/raid-only skills.
- [ ] Identify Crystal Raid skills.
- [ ] Identify Partner Customization-only skills.
- [ ] Identify boss/NPC/cast-exclusive skills.
- [ ] Identify skills unavailable to CaCs.
- [ ] Identify race-restricted skills.
- [ ] Identify gender-restricted skills.
- [ ] Identify form/Awoken-dependent skills.
- [ ] Identify DUAL skills and partner requirements.
- [ ] Identify special/cinematic/unused skills.
- [ ] Identify renamed/variant skills.
- [ ] Identify duplicate-name skills with different implementations.
- [ ] Produce a final canonical skill manifest.

## 2.2 Skill verification — every record

For **every skill**, verify or explicitly mark unknown:

- [ ] Canonical name.
- [ ] Alternate names / aliases.
- [ ] Skill class.
- [ ] Subcategory.
- [ ] Strike / Ki Blast / hybrid / utility classification.
- [ ] CaC availability.
- [ ] Race restriction.
- [ ] Gender restriction.
- [ ] Form restriction.
- [ ] Ki cost.
- [ ] Stamina cost.
- [ ] Health cost if any.
- [ ] Input/activation method.
- [ ] Charge/hold behavior.
- [ ] Follow-up inputs.
- [ ] Hit count.
- [ ] Tracking behavior.
- [ ] Guard interaction.
- [ ] Stamina-break interaction.
- [ ] I-frame / invulnerability behavior where documented.
- [ ] Counter conditions.
- [ ] Cancel conditions.
- [ ] Transformation interactions.
- [ ] Super Soul interactions.
- [ ] Partner/customization interactions.
- [ ] Exact unlock method.
- [ ] Exact mission/quest number and name.
- [ ] Ultimate Finish requirement.
- [ ] Shop name and availability/rotation where applicable.
- [ ] Mentor and lesson number where applicable.
- [ ] DLC/update/event provenance.
- [ ] Drop chance when evidence supports it.
- [ ] Reward-slot behavior when evidence supports it.
- [ ] In-game description.
- [ ] Detailed mechanics writeup.
- [ ] Combo notes.
- [ ] PvE notes.
- [ ] PvP notes, clearly identified as analysis rather than fact.
- [ ] Known version/patch changes.
- [ ] Known bugs/glitches.
- [ ] Related characters.
- [ ] Related missions.
- [ ] Related DLC.
- [ ] Related Super Souls/items.
- [ ] Source list.
- [ ] Last verification date.
- [ ] Verification confidence/state.

## 2.3 Existing research batches

- [~] Batch 01: 5 enriched records — still `partially_verified`.
- [~] Batch 02: 6 enriched records — still `partially_verified`.
- [~] Batch 03: 6 enriched records — still `partially_verified`.
- [~] Batch 04: 6 enriched records — still `partially_verified`.
- [~] Batch 05: 5 enriched records — still `partially_verified`.
- [ ] Resolve duplicate records across batches.
- [ ] Reconcile all batch records into canonical `skills.json` only after evidence is sufficient.
- [ ] Promote verified fields individually rather than falsely promoting entire records.
- [ ] Generate dedicated skill pages from canonical records.

## 2.4 Current skill research queue

### Batch 01
- [ ] Quick Sleep
- [ ] Saiyan Blaster
- [ ] Gigantic Cluster
- [ ] Remote Serious Bomb
- [ ] Impulse Slash

### Batch 02
- [ ] Kamehameha
- [ ] Quick Sleep — duplicate of Batch 01
- [ ] Saiyan Blaster — duplicate of Batch 01
- [ ] Gigantic Cluster — duplicate of Batch 01
- [ ] Remote Serious Bomb — duplicate of Batch 01
- [ ] Impulse Slash — duplicate of Batch 01

### Batch 03
- [ ] Eraser Bomb
- [ ] Spirit Pulse
- [ ] Gigantic Explosion
- [ ] Surging Spirit
- [ ] Sword of Hope
- [ ] DUAL Remote Serious Bomb

### Batch 04
- [ ] Evil Flight Strike
- [ ] Lightning Impact
- [ ] Excellent Full Course
- [ ] Photon Swipe
- [ ] Ultimate Charge
- [ ] Burst Charge

### Batch 05
- [ ] Divinity Unleashed
- [ ] Super Dragon Fist
- [ ] God Splitter
- [ ] Kaioken Assault
- [ ] Burst Rush

## 2.5 Skill hard-writing

- [ ] Create individual prose page for every canonical skill.
- [ ] Add “What it does” section to every skill.
- [ ] Add “How to unlock” section.
- [ ] Add “Costs and restrictions” section.
- [ ] Add “Mechanics” section.
- [ ] Add “Combos and interactions” section.
- [ ] Add “PvE” section.
- [ ] Add “PvP” section when relevant.
- [ ] Add “Related content” section.
- [ ] Add “Verification” section.
- [ ] Cross-link every skill to its source quests/mentors/characters/DLC.

# 3. Characters

- [~] Canonical character reconciliation exists.
- [ ] Verify canonical roster count against current source categories.
- [ ] Reconcile base characters vs forms vs presets.
- [ ] Reconcile DLC character records.
- [ ] Reconcile cast-exclusive/boss/NPC records.
- [ ] Verify race/species for every record.
- [ ] Verify playable/NPC/boss/partner status.
- [ ] Verify every form.
- [ ] Verify every preset.
- [ ] Verify unlock route.
- [ ] Verify DLC/update provenance.
- [ ] Verify associated skills.
- [ ] Verify associated Super Souls.
- [ ] Verify quest appearances.
- [ ] Verify Partner Customization eligibility.
- [ ] Verify customization keys.
- [ ] Write individual hard-written entry for every character.
- [ ] Add aliases and search terms for every character.
- [ ] Cross-link characters ↔ skills ↔ quests ↔ DLC.

# 4. Parallel Quests

- [ ] Establish complete canonical PQ manifest.
- [ ] Verify every PQ number.
- [ ] Verify every PQ name.
- [ ] Verify unlock/progression requirement.
- [ ] Verify map/arena.
- [ ] Verify starting enemies.
- [ ] Verify reinforcement waves.
- [ ] Verify conditions/triggers.
- [ ] Verify failure conditions.
- [ ] Verify Ultimate Finish requirement.
- [ ] Verify Ultimate Finish effects.
- [ ] Verify complete reward pool.
- [ ] Verify skill rewards.
- [ ] Verify Super Soul rewards.
- [ ] Verify clothing/accessory rewards.
- [ ] Verify item/material rewards.
- [ ] Verify TP/Zeni/experience information where appropriate.
- [ ] Write every PQ individually.
- [ ] Add farming notes.
- [ ] Cross-link PQs to every referenced skill/character/item.

# 5. Main Story / Future Saga / Extra Story

- [ ] Complete story chapter manifest.
- [ ] Verify mission ordering.
- [ ] Verify objectives.
- [ ] Verify enemies.
- [ ] Verify unlocks.
- [ ] Verify rewards.
- [ ] Verify story prerequisites.
- [ ] Verify branching/alternate conditions.
- [ ] Verify Extra Story / Infinite History progression.
- [ ] Verify Future Saga chapters and content.
- [ ] Write exhaustive walkthroughs.

# 6. Expert Missions

- [ ] Establish complete EM manifest.
- [ ] Verify each mission number/name.
- [ ] Verify enemy/boss behavior.
- [ ] Verify Giant Ki Blast mechanics.
- [ ] Verify objectives.
- [ ] Verify rewards/drop pools.
- [ ] Verify skill drops.
- [ ] Verify raid/online mechanics where relevant.
- [ ] Write individual EM pages.
- [ ] Add practical offline/online strategy sections.

# 7. Raids / Crystal Raids / Festival / Events

- [ ] Establish historical event manifest.
- [ ] Verify raid bosses.
- [ ] Verify reward pools.
- [ ] Verify exclusive skills.
- [ ] Verify exclusive Super Souls.
- [ ] Verify clothing/accessories.
- [ ] Verify Partner Keys.
- [ ] Verify event requirements and timing.
- [ ] Document historical availability separately from current availability.
- [ ] Verify Crystal Raid rules and rewards.
- [ ] Write event mechanics and farming guides.

# 8. Mentors / Instructors

- [ ] Complete mentor manifest.
- [ ] Verify spawn/unlock conditions.
- [ ] Verify every lesson.
- [ ] Verify every skill reward.
- [ ] Verify friendship mechanics.
- [ ] Verify mentor customization.
- [ ] Verify Dual Ultimate relationships.
- [ ] Verify Advancement Test requirements.
- [ ] Write every mentor individually.

# 9. Super Souls

- [ ] Establish complete Super Soul manifest.
- [ ] Verify exact name.
- [ ] Verify effect text.
- [ ] Verify activation condition.
- [ ] Verify duration/stacking behavior.
- [ ] Verify source.
- [ ] Verify DLC/update/event provenance.
- [ ] Verify race/form/skill interactions.
- [ ] Write every Super Soul.
- [ ] Cross-link Super Souls to relevant builds, skills and characters.

# 10. QQ Bangs / Clothing / Accessories

- [ ] Establish clothing manifest.
- [ ] Verify clothing names.
- [ ] Verify stats.
- [ ] Verify sources.
- [ ] Verify mixing recipes/materials.
- [ ] Verify QQ Bang outcomes.
- [ ] Document RNG/variation rules.
- [ ] Verify accessory effects.
- [ ] Write individual equipment entries.
- [ ] Build searchable relationship graph between clothing → QQ Bang → stats.

# 11. Items / Capsules / Materials / Currency

- [ ] Complete item manifest.
- [ ] Verify item effects.
- [ ] Verify shop sources.
- [ ] Verify mission sources.
- [ ] Verify mixing sources.
- [ ] Verify TP Medal uses.
- [ ] Verify Zeni uses.
- [ ] Verify Dragon Ball uses.
- [ ] Verify rare materials.
- [ ] Write every important item/material.

# 12. Shops

- [ ] Skill Shop inventory.
- [ ] TP Medal Shop inventory.
- [ ] Clothing Shop inventory.
- [ ] Item Shop inventory.
- [ ] Accessory Shop inventory.
- [ ] Rotation/history tracking.
- [ ] Unlock/progression requirements.
- [ ] Price verification.
- [ ] DLC restrictions.
- [ ] Historical vs current availability.

# 13. Awoken Skills / Transformations

- [ ] Complete Awoken manifest.
- [ ] Verify race restrictions.
- [ ] Verify unlock conditions.
- [ ] Verify stat modifiers.
- [ ] Verify Ki/stamina/health behavior.
- [ ] Verify drain/regen behavior.
- [ ] Verify form-specific attacks.
- [ ] Verify level/friendship/story requirements.
- [ ] Verify DLC requirements.
- [ ] Write exhaustive individual transformation pages.

# 14. CaC races / genders / attributes / progression

- [ ] Human/Majin/Saiyan/Namekian/Frieza Race documentation.
- [ ] Male/female differences.
- [ ] Basic attack mechanics.
- [ ] Ki Blast Supers.
- [ ] Strike Supers.
- [ ] Ki Blast Ultimate scaling.
- [ ] Strike Ultimate scaling.
- [ ] Health/stamina/Ki systems.
- [ ] Attribute caps and updates.
- [ ] Level cap history.
- [ ] Advancement Tests.
- [ ] Guru/elder progression systems.
- [ ] Tosok leveling.
- [ ] QQ Bang optimization.

# 15. Conton City / locations / NPCs

- [ ] Map/location manifest.
- [ ] Shops and vendors.
- [ ] Mentors.
- [ ] Time Rift locations.
- [ ] NPC quest chains.
- [ ] TP Medal / Dragon Ball NPCs.
- [ ] Transportation/online hub systems.
- [ ] Unlock conditions.
- [ ] Write important locations individually.

# 16. Shenron / Dragon Balls / wishes

- [ ] Verify all wishes.
- [ ] Verify wish unlocks.
- [ ] Verify Dragon Ball farming routes.
- [ ] Verify time/availability constraints.
- [ ] Verify character wishes.
- [ ] Verify skill wishes.
- [ ] Verify item/material wishes.
- [ ] Write every wish and acquisition method.

# 17. DLC / Updates / Version history

- [ ] Complete DLC pack manifest.
- [ ] Super Pass.
- [ ] Extra Pass.
- [ ] Ultra Packs.
- [ ] Legendary Pack.
- [ ] Hero of Justice Pack.
- [ ] Future Saga chapters.
- [ ] DAIMA content.
- [ ] Legend Patrol / platform-specific content.
- [ ] Free updates.
- [ ] Level-cap history.
- [ ] Skill changes.
- [ ] Character changes.
- [ ] Event changes.
- [ ] Historical availability.

# 18. Mechanics encyclopedia

- [ ] Ki system.
- [ ] Stamina system.
- [ ] Stamina break.
- [ ] Vanish.
- [ ] Guard.
- [ ] Perfect block/just guard behavior.
- [ ] Step/step vanish.
- [ ] Dash.
- [ ] Basic attack strings.
- [ ] Heavy attacks.
- [ ] Charged attacks.
- [ ] Ki cancel mechanics.
- [ ] Stamina damage.
- [ ] Ki damage.
- [ ] Strike vs Ki Blast scaling.
- [ ] Grab mechanics.
- [ ] Counter mechanics.
- [ ] Armor/super armor.
- [ ] Hyper armor.
- [ ] I-frames.
- [ ] Tracking.
- [ ] Knockback/knockdown.
- [ ] Ground vs air behavior.
- [ ] Giant character mechanics.
- [ ] Raid boss mechanics.
- [ ] Expert Mission mechanics.
- [ ] Dual Ultimate mechanics.
- [ ] Customization mechanics.
- [ ] Friendship mechanics.
- [ ] Drop/reward mechanics.
- [ ] RNG mechanics.
- [ ] Z-Rank scoring.
- [ ] Time limits.
- [ ] AI behavior.

# 19. Builds / practical guides

- [ ] Beginner CaC builds.
- [ ] Race-specific builds.
- [ ] Gender-specific builds.
- [ ] Strike builds.
- [ ] Ki Blast builds.
- [ ] Hybrid builds.
- [ ] PvE builds.
- [ ] Expert Mission builds.
- [ ] Raid builds.
- [ ] Farming builds.
- [ ] PvP reference builds.
- [ ] Awoken-specific builds.
- [ ] QQ Bang recommendations with sourced reasoning.
- [ ] Super Soul recommendations with documented effects.
- [ ] Skill synergy explanations.

# 20. Farming / completion

- [ ] Skill farming hub.
- [ ] PQ farming hub.
- [ ] TP Medal farming.
- [ ] Zeni farming.
- [ ] Dragon Ball farming.
- [ ] Super Soul farming.
- [ ] Clothing farming.
- [ ] QQ Bang material farming.
- [ ] Leveling.
- [ ] Friendship farming.
- [ ] Partner Key farming.
- [ ] Raid farming.
- [ ] Crystal Raid farming.
- [ ] Event farming.

# 21. Achievements / completion checklists

- [ ] Achievements/trophies manifest.
- [ ] Verify requirements.
- [ ] Link achievements to relevant missions/content.
- [ ] Create skill completion checklist.
- [ ] Create character completion checklist.
- [ ] Create PQ completion checklist.
- [ ] Create DLC completion checklist.
- [ ] Create Super Soul completion checklist.
- [ ] Create equipment completion checklist.

# 22. Glitches / bugs / edge cases

- [ ] Establish bug/glitch taxonomy.
- [ ] Verify reproducibility.
- [ ] Record affected versions.
- [ ] Record affected platforms.
- [ ] Distinguish exploit from intended mechanic.
- [ ] Record patches that fixed issues.
- [ ] Cross-link affected skills/missions/characters.

# 23. Sources / research discipline

- [ ] Establish source hierarchy.
- [ ] Prefer in-game evidence for exact mechanics.
- [ ] Use official Bandai/Dimps material for release/DLC facts where available.
- [ ] Use established wiki/reference sources for discovery and cross-checking.
- [ ] Use community sources for leads, clearly marked as community evidence.
- [ ] Never convert a community opinion into a factual field.
- [ ] Track source date.
- [ ] Track verification date.
- [ ] Track conflicting evidence.
- [ ] Track stale information after updates.

# 24. Automation / repository quality

- [x] Internal-artifact scanner exists.
- [ ] Verify scanner against entire current tree.
- [ ] Fix any remaining internal artifacts.
- [ ] Add duplicate-record checker.
- [ ] Add missing-required-field checker.
- [ ] Add orphan-reference checker.
- [ ] Add JSON schema validation.
- [ ] Add Markdown/front-matter validation.
- [ ] Add search-index completeness validation.
- [ ] Add hard-writing completeness validation.
- [ ] Add source URL validation where practical.
- [ ] Add stale-verification report.
- [ ] Add canonical-count reconciliation report.
- [ ] Make CI output actionable.
- [ ] Resolve current pre-step GitHub Actions failure.
- [ ] Verify Pages deployment after site changes.

# 25. GitHub Pages / presentation

- [x] Search-first homepage.
- [x] Search navigation.
- [x] Dedicated search page.
- [x] Wiki navigation shell.
- [ ] Verify all navigation URLs resolve.
- [ ] Verify all existing pages use compatible layouts.
- [ ] Add category landing pages.
- [ ] Add record cards/tables where appropriate.
- [ ] Add mobile navigation polish.
- [ ] Add page-level “related content” blocks.
- [ ] Add source/verification visual treatment.
- [ ] Add last-updated metadata.
- [ ] Add generated “recently researched” section.
- [ ] Add generated “needs verification” dashboard.
- [ ] Add generated “coverage” dashboard.
- [ ] Add generated “orphan pages” dashboard.

# 26. Current skill verification campaign

**Campaign rule:** work through the entire canonical skill manifest category-by-category. Do not mark a skill `verified` merely because a source page exists. Exact acquisition, mechanics, costs, restrictions and availability must be reconciled. When evidence is insufficient, keep the record `partially_verified` and create a concrete follow-up task.

### Campaign order

- [~] Ki Blast Supers — 183 indexed category entries.
- [ ] Strike Supers — 130.
- [ ] Ki Blast Ultimates — 110.
- [ ] Strike Ultimates — 30.
- [ ] Other Supers — 32.
- [ ] Power Up Supers — 20.
- [ ] Ki Blast Evasives — 23.
- [ ] Strike Evasives — 16.
- [ ] Other Evasives — 11.
- [ ] Power Up Evasives — 2.
- [ ] Saiyan Skills — 10.
- [ ] Majin Skills — 10.
- [ ] Namekian Skills — 4.
- [ ] Frieza Race Skills — 4.
- [ ] Human Skills — 4.
- [ ] Unavailable for CaC — 37.
- [ ] Counter Skills — 25.
- [ ] Transformations — 18.

> Category totals are source-index totals and may overlap. The final unique canonical count must be reconciled rather than simply summing these numbers.

### Research batches currently in repository

- [x] Batch 01 created.
- [x] Batch 02 created.
- [x] Batch 03 created.
- [x] Batch 04 created.
- [x] Batch 05 created.
- [ ] Reconcile duplicates across batches.
- [ ] Verify every batch record.
- [ ] Promote only evidence-backed fields.
- [ ] Continue creating batches until the canonical skill manifest is exhausted.

# 27. Final “exhaustive” gate

The wiki is **not** complete until all of these are true:

- [ ] Every canonical skill verified or explicitly unresolved with a documented reason.
- [ ] Every canonical character verified or explicitly unresolved.
- [ ] Every canonical mission verified or explicitly unresolved.
- [ ] Every canonical item/equipment record verified or explicitly unresolved.
- [ ] Every major mechanic has a hard-written explanation.
- [ ] Every DLC/update is documented.
- [ ] Every major relationship is cross-linked.
- [ ] Search can find every entity and every major concept by natural-language terms.
- [ ] All source/provenance fields are present.
- [ ] All internal artifacts are removed.
- [ ] All automated audits pass.
- [ ] Pages build successfully.
- [ ] No broken navigation remains.
- [ ] Coverage dashboards show no unexplained gaps.
- [ ] “Verified” means actually verified—not merely indexed.
