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


---

# 28. Live continuation synchronization — 2026-09-21

> **Authoritative handoff linkage:** This section is the live TODO state that must be kept synchronized with `docs/AI-CONTINUATION-PROMPT.md`. Historical checklist sections above are preserved; when they contain stale counts or broad campaign labels, this live section takes precedence for current-cycle execution.

## 28.1 Current canonical skill state

- [~] Canonical skill manifest: **428 records**.
- [x] Duplicate skill IDs: **0**.
- [~] Nullable canonical `ki_cost`: **18 records**.
- [~] Current bounded Ki-cost verification campaign is active and has reduced the nullable count from the earlier live baseline of 74 to 18 through evidence-backed batches.
- [x] Variable-cost values encountered in this campaign are preserved rather than flattened (for example, Energy Dome `up to 320`, One-Handed Kamehameha mk.II `400-600`, Grand Smasher `300-400`, and Break Cannon `300+`).
- [~] Remaining nullable `ki_cost` records are an explicit research queue, not assumed errors.

## 28.2 Completed Ki-cost verification frontier

The following bounded mentor/resource-cost batches are recorded in the continuation handoff and coverage audit:

- [x] Evil Explosion / Super Explosive Wave / Light Grenade / Special Beam Cannon / Dodon Ray / Volleyball Fist / Tri-Beam / Neo Tri-Beam.
- [x] Fake Death / Wolf Fang Fist / Ki Blast Thrust / Spirit Ball / Bomber DX / Arm Crash / Genocide Shell / Break Cannon.
- [x] Raditz mentor batch.
- [x] Zarbon mentor batch.
- [x] Dodoria mentor batch.
- [x] Frieza mentor batch.
- [x] Cooler mentor batch.
- [x] Majin Buu mentor batch.
- [x] Beerus mentor batch.
- [x] Lord Slug mentor batch.
- [x] Whis mentor batch.
- [x] Broly mentor batch.
- [x] Android 16 mentor batch.
- [x] Future Gohan mentor batch.
- [x] Bojack mentor batch.
- [x] Zamasu mentor batch.
- [x] Brutal Buster resource-cost verification.

## 28.3 Immediate live research queue

- [ ] Recompute the nullable `ki_cost` census before every bounded batch.
- [ ] Research the next unresolved skill/family using explicit current `Ki Used` evidence where available.
- [ ] Preserve `null` when evidence is insufficient or conflicting.
- [ ] Preserve fixed, zero, and variable/range costs distinctly.
- [ ] Refresh `last_verified` only for records actually verified in the batch.
- [ ] Validate 428 canonical records and 0 duplicate IDs after every canonical write.
- [ ] Inspect CI/status without claiming success when GitHub exposes no run/check.
- [ ] Keep `docs/AI-CONTINUATION-PROMPT.md`, `docs/COVERAGE-AUDIT.md`, `CHANGELOG.md`, and this live TODO state synchronized at the end of each cycle.

## 28.4 Current unresolved `ki_cost` records

As of the 2026-09-21 live census, the remaining nullable records are:

- [ ] Brutal Buster — resolved in the current cycle; remove from future unresolved census.
- [ ] Dimension Cannon
- [ ] Evil Ray Strike
- [ ] Evil Rise Strike
- [ ] Explosive Assault
- [ ] Finish Breaker
- [ ] Flash Strike
- [ ] Final Flash
- [ ] Time Skip/Tremor Pulse
- [ ] Orin Combo
- [ ] Scatter Kamehameha
- [ ] Giant Storm
- [ ] Angry Explosion
- [ ] Dead End Rain
- [ ] God of Destruction's Might
- [ ] Meteor Crash
- [ ] Fighting Pose C
- [ ] Psycho Escape
- [ ] Kaioken Kamehameha

**Correction:** Brutal Buster is **not** part of the remaining nullable census; its checkbox above is retained only as a completed-cycle trace. The authoritative unresolved count is **18**, matching `docs/data/skills.json`.

## 28.5 Synchronization rule

When the continuation handoff advances a research frontier, update this live TODO section in the same cycle. Do not rely on historical checklist labels or old category totals to determine the next action. The next chat should begin from the live canonical census and this section, then reconcile any discrepancy before editing data.


### 2026-09-21 — TODO live-queue correction
- The newly added live synchronization section intentionally listed Brutal Buster as a completed-cycle trace, but its checkbox could be misread as unresolved.
- Authoritative correction: **Brutal Buster is resolved and excluded from the 18-record nullable `ki_cost` queue**. The 18 unresolved names are the remaining records listed after it in the canonical census.
- Future cycles must derive this queue directly from the live `docs/data/skills.json` census rather than hand-maintaining names independently.


# 29. Append-only master task ledger — 2026-09-21

> **Operating rule requested by the repository owner:** this TODO is a giant, append-only task ledger. Never delete a task, historical section, completion record, or correction from this file. When work is completed, mark the corresponding task `[x]` in the current live ledger or add a completed ledger entry; when a task is discovered, append it as a new unchecked task. If an old historical checkbox conflicts with live state, preserve it and use a newer dated ledger entry as the authoritative state. Never erase history to make the checklist look cleaner.

## 29.1 Ledger rules

- [x] Preserve every existing line and historical section in this file.
- [x] Preserve every completed task as a permanent historical record.
- [x] Preserve every unresolved task until it is explicitly completed or superseded by a documented correction.
- [x] Add newly discovered work to this ledger instead of silently tracking it only in chat.
- [x] Mark a task `[x]` only after the repository change and validation for that task are complete.
- [~] Use `[~]` for work that is underway or partially verified.
- [ ] Use `[ ]` for discovered work that remains.
- [x] Record the date, files/records, evidence limits, validation, commits, and next task in the continuation handoff for every meaningful cycle.
- [x] Keep the handoff and this ledger synchronized in the same cycle.
- [x] Derive live record-level queues from canonical data before choosing the next task.
- [x] Do not replace historical checklist counts with new counts; append a dated live census when counts change.
- [x] Never treat an indexed record as verified solely because it exists.
- [x] Never flatten variable costs, conflicting evidence, historical differences, or unresolved provenance into false certainty.

## 29.2 Completed repository work recorded as permanent ledger history

### Core infrastructure / repository quality

- [x] Internal-artifact scanner exists.
- [x] Canonical skill JSON is parseable.
- [x] Canonical skill duplicate-ID census currently reports 0 duplicates.
- [x] Live TODO/handoff synchronization mechanism established.
- [x] Brutal Buster Ki-cost/resource-cost verification completed and recorded.
- [x] Historical handoff entries are preserved rather than rewritten.
- [x] Historical TODO sections are preserved rather than rewritten.

### Parallel Quest unlock-field frontier

- [x] PQ1–10 unlock wording frontier completed.
- [x] PQ12–20 unlock metadata refinement completed.
- [x] PQ21–50 bounded unlock metadata completed.
- [x] PQ51–60 unlock refinement completed.
- [x] PQ61–70 bounded unlock evidence completed.
- [x] PQ71–100 unlock-route review completed.
- [x] PQ101–110 DLC-era unlock provenance completed.
- [x] PQ111–120 DLC-era unlock provenance completed.
- [x] PQ121–130 DLC-era unlock provenance completed.
- [x] PQ131–140 DLC-era unlock provenance completed.
- [x] PQ151–160 DLC-era unlock provenance completed.
- [x] PQ36 special numbering/prerequisite case documented.
- [x] PQ53 special NPC-trigger case documented.
- [x] PQ54 conflicting unlock-route evidence documented rather than silently resolved.
- [x] PQ55 prerequisite documented.
- [x] Repository-wide PQ census reached 176 canonical records with explicit `unlock_condition` field on all 176 records.
- [x] Known PQ36 numbering/existence anomaly preserved as an unresolved historical/data-model issue.

### Skill Ki-cost verification frontier already completed

- [x] Evil Explosion / Super Explosive Wave / Light Grenade / Special Beam Cannon / Dodon Ray / Volleyball Fist / Tri-Beam / Neo Tri-Beam.
- [x] Fake Death / Wolf Fang Fist / Ki Blast Thrust / Spirit Ball / Bomber DX / Arm Crash / Genocide Shell / Break Cannon.
- [x] Raditz mentor batch.
- [x] Zarbon mentor batch.
- [x] Dodoria mentor batch.
- [x] Frieza mentor batch.
- [x] Cooler mentor batch.
- [x] Majin Buu mentor batch.
- [x] Beerus mentor batch.
- [x] Lord Slug mentor batch.
- [x] Whis mentor batch.
- [x] Broly mentor batch.
- [x] Android 16 mentor batch.
- [x] Future Gohan mentor batch.
- [x] Bojack mentor batch.
- [x] Zamasu mentor batch.
- [x] Brutal Buster resource-cost verification.

## 29.3 Current canonical skill Ki-cost queue

- [ ] Dimension Cannon.
- [ ] Evil Ray Strike.
- [ ] Evil Rise Strike.
- [ ] Explosive Assault.
- [ ] Finish Breaker.
- [ ] Flash Strike.
- [ ] Final Flash.
- [ ] Time Skip/Tremor Pulse.
- [ ] Orin Combo.
- [ ] Scatter Kamehameha.
- [ ] Giant Storm.
- [ ] Angry Explosion.
- [ ] Dead End Rain.
- [ ] God of Destruction's Might.
- [ ] Meteor Crash.
- [ ] Fighting Pose C.
- [ ] Psycho Escape.
- [ ] Kaioken Kamehameha.

### Ki-cost campaign execution tasks

- [ ] Recompute the nullable `ki_cost` census before every bounded research batch.
- [ ] Research one bounded family/batch at a time using explicit current `Ki Used` evidence where available.
- [ ] Preserve `null` where evidence is insufficient or conflicting.
- [ ] Preserve fixed, zero, and variable/range costs distinctly.
- [ ] Update `last_verified` only for records actually verified in the current batch.
- [ ] Validate 428 canonical skill records and 0 duplicate IDs after every canonical skill write.
- [ ] Recompute the exact unresolved queue after every canonical write.
- [ ] Update this TODO and the continuation handoff together after every meaningful batch.
- [ ] Check applicable GitHub Actions/status after each canonical or documentation cycle.
- [ ] Never claim CI success when GitHub exposes no successful check/run.
- [ ] Scan changed prose for internal AI/tool citation artifacts.

## 29.4 Skills — remaining exhaustive verification work

- [ ] Verify every canonical skill's exact name against current evidence.
- [ ] Verify every canonical skill category/type.
- [ ] Verify exact Ki cost.
- [ ] Verify exact Stamina cost where applicable.
- [ ] Verify acquisition route.
- [ ] Verify CaC availability.
- [ ] Verify race restrictions.
- [ ] Verify gender restrictions.
- [ ] Verify character-only status.
- [ ] Verify Ultimate Finish requirement where acquisition depends on it.
- [ ] Verify DLC/update provenance.
- [ ] Verify version-sensitive mechanics.
- [ ] Verify mechanics/inputs.
- [ ] Verify source provenance.
- [ ] Verify verification date.
- [ ] Resolve or explicitly document every remaining nullable/uncertain field.
- [ ] Reconcile duplicates across historical skill research batches.
- [ ] Promote only evidence-backed fields into canonical data.
- [ ] Create or complete hard-written prose for every canonical skill.
- [ ] Cross-link every skill to quests, mentors, characters, DLC, and related records.
- [ ] Build a final skill completeness audit showing no unexplained gaps.

## 29.5 Parallel Quests — remaining exhaustive work beyond unlock fields

- [ ] Verify every canonical PQ number/name.
- [ ] Verify map/arena.
- [ ] Verify starting enemies.
- [ ] Verify reinforcement waves.
- [ ] Verify conditions and triggers.
- [ ] Verify failure conditions.
- [ ] Verify Ultimate Finish requirements.
- [ ] Verify Ultimate Finish effects.
- [ ] Verify complete reward pools.
- [ ] Verify reward-slot semantics.
- [ ] Verify exact drop percentages where evidence exists.
- [ ] Verify skill rewards.
- [ ] Verify Super Soul rewards.
- [ ] Verify clothing/accessory rewards.
- [ ] Verify item/material rewards.
- [ ] Verify TP/Zeni/experience information where appropriate.
- [ ] Verify DLC/version provenance.
- [ ] Verify record-level sources.
- [ ] Cross-link every PQ to referenced skills, characters, items, equipment, and DLC.
- [ ] Write every PQ individually.
- [ ] Add farming notes.
- [ ] Preserve unresolved reward semantics rather than inventing certainty.

## 29.6 Awoken / Transformations

- [ ] Complete exhaustive manifest.
- [ ] Verify CaC vs character-only.
- [ ] Verify race/gender restrictions.
- [ ] Verify stages/forms.
- [ ] Verify resource requirements.
- [ ] Verify prerequisites.
- [ ] Verify effects/stat modifiers.
- [ ] Verify drain/regen behavior.
- [ ] Verify form-specific mechanics.
- [ ] Verify DLC/version provenance.
- [ ] Write individual transformation pages.
- [ ] Cross-link transformations to races, skills, characters, quests, and DLC.

## 29.7 Expert Missions

- [ ] Complete EM01–EM27 manifest.
- [ ] Verify mission numbers/names.
- [ ] Verify enemy/boss behavior.
- [ ] Verify Giant Ki Blast mechanics.
- [ ] Verify phases/objectives.
- [ ] Verify rewards/drop pools.
- [ ] Verify skill drops.
- [ ] Verify first-clear vs repeat behavior.
- [ ] Verify online/offline mechanics.
- [ ] Verify version differences.
- [ ] Write individual EM pages.
- [ ] Add practical mechanics/strategy documentation.

## 29.8 Characters

- [ ] Verify canonical roster count against current evidence.
- [ ] Reconcile base characters, forms, presets, bosses, NPCs, and partners.
- [ ] Verify DLC character records.
- [ ] Verify race/species.
- [ ] Verify playable/NPC/boss/partner status.
- [ ] Verify forms and presets.
- [ ] Verify unlock routes.
- [ ] Verify DLC/update provenance.
- [ ] Verify associated skills.
- [ ] Verify associated Super Souls.
- [ ] Verify quest appearances.
- [ ] Verify Partner Customization eligibility and keys.
- [ ] Write individual character entries.
- [ ] Add aliases/search terms.
- [ ] Cross-link characters to skills, quests, DLC, and related systems.

## 29.9 Super Souls

- [ ] Establish complete manifest.
- [ ] Verify exact names/effect text.
- [ ] Verify activation conditions.
- [ ] Verify duration/stacking.
- [ ] Verify Limit Burst.
- [ ] Verify acquisition/rotation.
- [ ] Verify DLC/update/event provenance.
- [ ] Verify race/form/skill interactions.
- [ ] Write individual Super Soul entries.
- [ ] Cross-link Super Souls to builds, skills, characters, quests, and equipment.

## 29.10 Equipment / QQ Bangs / Items

- [ ] Establish complete clothing manifest.
- [ ] Verify clothing names/stats/slots.
- [ ] Verify clothing sources and set relationships.
- [ ] Verify accessory effects/sources.
- [ ] Verify mixing recipes/materials.
- [ ] Verify QQ Bang outcomes and observed six-stat outputs.
- [ ] Document RNG/variation behavior.
- [ ] Establish complete item/material/capsule manifest.
- [ ] Verify item effects and shop/mission/mixing sources.
- [ ] Verify TP Medal, Zeni, Dragon Ball, and rare-material uses.
- [ ] Build searchable clothing → QQ Bang → stat relationships.
- [ ] Write individual equipment/item entries.

## 29.11 Story / Future Saga / Time Rifts / Conton City

- [ ] Complete story chapter/mission manifest.
- [ ] Verify mission ordering/objectives/enemies.
- [ ] Verify story unlocks/rewards/prerequisites.
- [ ] Verify branching and alternate conditions.
- [ ] Verify Extra Story / Infinite History progression.
- [ ] Verify Future Saga chapters/content.
- [ ] Verify Time Rift locations and NPC chains.
- [ ] Verify Conton City locations, shops, mentors, vendors, and progression gates.
- [ ] Write exhaustive walkthroughs and location pages.

## 29.12 Shops / Rewards / Raids / Events

- [ ] Complete Skill Shop inventory.
- [ ] Complete TP Medal Shop inventory.
- [ ] Complete Clothing Shop inventory.
- [ ] Complete Item Shop inventory.
- [ ] Complete Accessory Shop inventory.
- [ ] Track rotations/history.
- [ ] Verify unlock/progression requirements.
- [ ] Verify prices.
- [ ] Verify DLC restrictions.
- [ ] Distinguish historical vs current availability.
- [ ] Establish historical event/raid manifest.
- [ ] Verify raid bosses/reward pools/exclusive skills/Super Souls/equipment/Partner Keys.
- [ ] Verify event timing/recurrence and historical availability.
- [ ] Verify Crystal Raid rules/rewards.

## 29.13 Shenron / Dragon Balls

- [ ] Verify all wishes.
- [ ] Verify wish unlock conditions.
- [ ] Verify Dragon Ball farming routes.
- [ ] Verify time/availability constraints.
- [ ] Verify character/skill/item/material wishes.
- [ ] Write every wish and acquisition method.

## 29.14 DLC / Updates / Version History

- [ ] Complete DLC pack manifest.
- [ ] Verify Super Pass.
- [ ] Verify Extra Pass.
- [ ] Verify Ultra Packs.
- [ ] Verify Legendary Pack.
- [ ] Verify Hero of Justice Pack.
- [ ] Verify Future Saga chapters.
- [ ] Verify DAIMA content.
- [ ] Verify Legend Patrol/platform-specific content.
- [ ] Verify free updates.
- [ ] Track level-cap history.
- [ ] Track skill changes.
- [ ] Track character changes.
- [ ] Track event changes.
- [ ] Track historical availability.

## 29.15 Mechanics Encyclopedia

- [ ] Document Ki/stamina systems.
- [ ] Document stamina break, vanish, guard, perfect block/just guard, step/step vanish, dash, attack strings, charged attacks, and Ki cancel.
- [ ] Document stamina damage, Ki damage, strike vs Ki Blast scaling, grabs, counters, armor/super armor, hyper armor, I-frames, tracking, knockback/knockdown.
- [ ] Document ground/air behavior and giant-character mechanics.
- [ ] Document raid-boss and Expert Mission mechanics.
- [ ] Document Dual Ultimate, customization, friendship, drop/reward, RNG, Z-Rank, time-limit, and AI behavior systems.
- [ ] Cross-link mechanics to affected records.

## 29.16 Builds / Farming / Completion

- [ ] Create beginner and race/gender-specific CaC builds.
- [ ] Create strike, Ki Blast, hybrid, PvE, Expert Mission, raid, farming, PvP-reference, and Awoken-specific builds.
- [ ] Document QQ Bang recommendations with sourced reasoning.
- [ ] Document Super Soul recommendations with documented effects.
- [ ] Explain skill synergies.
- [ ] Build skill/PQ/TP Medal/Zeni/Dragon Ball/Super Soul/clothing/QQ Bang/level/friendship/Partner Key/raid/Crystal Raid/event farming hubs.
- [ ] Create skill, character, PQ, DLC, Super Soul, and equipment completion checklists.

## 29.17 Sources / automation / presentation

- [ ] Establish and document source hierarchy.
- [ ] Prefer in-game evidence for exact mechanics.
- [ ] Use official Bandai/Dimps material for release/DLC facts where available.
- [ ] Use established references for discovery and cross-checking.
- [ ] Mark community evidence as community evidence.
- [ ] Track source date, verification date, conflicts, and staleness.
- [ ] Verify scanner against the entire current tree.
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
- [ ] Resolve opaque pre-step GitHub Actions failures when actionable infrastructure evidence becomes available.
- [ ] Verify Pages deployment after site changes.
- [ ] Verify all navigation URLs resolve.
- [ ] Add category landing pages.
- [ ] Add record cards/tables where appropriate.
- [ ] Add mobile navigation polish.
- [ ] Add related-content blocks.
- [ ] Add source/verification visual treatment.
- [ ] Add last-updated metadata.
- [ ] Add generated recently-researched, needs-verification, coverage, and orphan-page dashboards.

## 29.18 Discovery rule for every future cycle

- [ ] Before editing, inspect the live canonical data and current repository state.
- [ ] If research reveals a new task, append it here immediately as a new unchecked item.
- [ ] If that task is completed in the same cycle, mark the newly appended item `[x]` and document the evidence/commit in the handoff.
- [ ] If a task is partially completed, leave the ledger item `[~]` and append a dated detail entry.
- [ ] Never delete a completed item just because the repository later changes.
- [ ] Never silently remove an unresolved item; use a dated correction/supersession entry.
- [ ] At cycle end, reconcile this ledger against `docs/AI-CONTINUATION-PROMPT.md`, canonical data, audit, and changelog.


### 2026-09-21 — Master ledger status update: Evil Ray Strike

- [x] **Evil Ray Strike Ki-cost verification completed.** Canonical `ki_cost=100`; `last_verified=2026-09-21`; canonical commit `dde2188588fdaff5c81c799f06a0bbadcfcc165b`.
- [x] Live canonical validation after the write: **428 records / 0 duplicate IDs / 17 nullable `ki_cost` records**.
- [x] Evidence boundary recorded: current skill-cost evidence establishes 100 Ki; no unrelated mechanics or acquisition fields were changed.
- [ ] Next unresolved Ki-cost task: recompute the live nullable census and select the next bounded evidence-backed record/family.

> The earlier `[ ] Evil Ray Strike` line in section 29.3 is retained as historical ledger state under the append-only rule. This dated entry is the authoritative completion marking for the task.


### 2026-09-21 — Bounded Ki-cost batch: Evil Rise Strike / Explosive Assault / Finish Breaker
- Live census before batch: **428 canonical skills; 0 duplicate IDs; 17 nullable ki_cost records**.
- Completed **Evil Rise Strike — 100 Ki**. Current skill reference explicitly lists Ki Used: 100 and Gohan (Kid) training acquisition.
- Completed **Explosive Assault — 300 Ki**. Current skill reference explicitly lists Ki Used: 300 and Gohan (Kid) training acquisition.
- Completed **Finish Breaker — 100 Ki**. Current skill reference explicitly lists Ki Used: 100 and Vegeta training acquisition.
- Canonical changes were limited to ki_cost and last_verified=2026-09-21 for these three records.
- Post-write validation: **428 records; 0 duplicate IDs; 14 nullable ki_cost records**. The three target values were re-read successfully; variable-cost records were untouched.
- Research source descriptions: current Xenoverse 2 skill-reference pages for Evil Rise Strike, Explosive Assault, and Finish Breaker; each page exposes the explicit Ki Used value.
- Canonical commit: 76057f81bf7da7aa477081f8c300d0472b1b498a.
- Exact next task: recompute the live nullable census and research the next bounded unresolved record/family; current queue begins with **Dimension Cannon, Flash Strike, Final Flash**.


### 2026-09-21 — Master ledger completion marking: bounded Ki-cost batch
- [x] Evil Rise Strike Ki-cost verification completed: 100 Ki.
- [x] Explosive Assault Ki-cost verification completed: 300 Ki.
- [x] Finish Breaker Ki-cost verification completed: 100 Ki.
- [x] Post-write canonical validation completed: 428 records / 0 duplicate IDs / 14 nullable ki_cost records.
- [ ] Next unresolved Ki-cost batch: Dimension Cannon / Flash Strike / Final Flash, after a fresh live census.

> Earlier unchecked entries remain permanently preserved. These dated [x] entries are the authoritative completion markings under the append-only ledger contract.


### 2026-09-21 — Master ledger completion marking: Flash Strike / Final Flash
- [x] Flash Strike Ki-cost verification completed: 100 Ki.
- [x] Final Flash Ki-cost verification completed: 300 Ki.
- [x] Post-write canonical validation completed: 428 records / 0 duplicate IDs / 12 nullable ki_cost records.
- [~] Dimension Cannon exact-cost research inspected but not completed; null preserved pending direct exact-skill evidence.
- [ ] Next unresolved Ki-cost task: Dimension Cannon exact-cost verification.


### 2026-09-21 — Master ledger completion marking: Dimension Cannon / Orin Combo / Scatter Kamehameha

- [x] **Dimension Cannon Ki-cost verification completed as an Evasive exception.** Canonical ki_cost remains null because the move consumes Stamina rather than Ki; canonical stamina_cost=300; last_verified=2026-09-21. Dedicated current skill evidence explicitly lists 300 Stamina. No unsupported Ki value was inserted.
- [x] **Orin Combo Ki-cost verification completed: 100 Ki.** Current skill evidence explicitly lists 100 Ki; canonical record updated with ki_cost=100 and last_verified=2026-09-21.
- [x] **Scatter Kamehameha Ki-cost verification completed: 300 Ki.** Current skill evidence explicitly lists 300 Ki; canonical record updated with ki_cost=300 and last_verified=2026-09-21.
- [x] Post-write canonical validation completed: **428 records / 0 duplicate IDs / 10 nullable ki_cost records**.
- [ ] Next unresolved Ki-cost queue after this batch: **Time Skip/Tremor Pulse, Giant Storm, Angry Explosion, Dead End Rain, God of Destruction's Might, Meteor Crash, Fighting Pose C, Psycho Escape, Kaioken Kamehameha**.

> Earlier unchecked/partial entries remain permanently preserved. These dated entries are the authoritative completion markings under the append-only ledger contract.


### 2026-09-21 — Master ledger completion marking: Time Skip/Tremor Pulse

- [x] **Time Skip/Tremor Pulse Ki-cost verification completed: 0 Ki.** Current skill evidence explicitly documents 0 Ki and 200 Stamina for the Evasive; the canonical record now records ki_cost=0 and preserves stamina_cost=200.
- [x] Evidence scope preserved: this cycle changed only the unresolved resource-cost field and verification state; no unsupported damage/mechanics claims were imported into canonical data.
- [x] Post-write canonical validation: 428 records; 0 duplicate IDs; nullable ki_cost count reduced from 10 to 9.
- [ ] Next unresolved Ki-cost queue: Giant Storm, Angry Explosion, Dead End Rain, God of Destruction's Might, Meteor Crash, Fighting Pose C, Psycho Escape, Kaioken Kamehameha, plus the documented Dimension Cannon Stamina-only exception.


### 2026-09-21 — Master ledger completion marking: Giant Storm

- [x] **Giant Storm Ki-cost verification completed: 300 Ki.** Current skill evidence explicitly documents kiCost: 300; canonical record updated with ki_cost=300.
- [x] Evidence scope preserved: only the unresolved resource-cost field was changed; unsupported combat totals were not imported.
- [x] Post-write canonical validation: 428 records / 0 duplicate IDs / 8 nullable ki_cost records.
- [ ] Next unresolved Ki-cost queue: **Angry Explosion, Dead End Rain, God of Destruction's Might, Meteor Crash, Fighting Pose C, Psycho Escape, Kaioken Kamehameha**, with Dimension Cannon retained as the documented Stamina-only exception.


### 2026-09-21 — Master ledger completion marking: Angry Explosion

- [x] **Angry Explosion Ki-cost verification completed: 300 Ki.** Current skill evidence explicitly lists Ki Used: 300; canonical record updated with ki_cost=300.
- [x] Evidence scope preserved: the source also documents that the move can consume additional Ki while being prolonged, but the canonical bounded field records the base listed cost only; no unsupported variable-cost formula was added.
- [x] Post-write canonical validation: **428 records / 0 duplicate IDs / 7 nullable ki_cost records**.
- [ ] Next unresolved Ki-cost queue: **Dead End Rain, God of Destruction's Might, Meteor Crash, Fighting Pose C, Psycho Escape, Kaioken Kamehameha**, with Dimension Cannon retained as the documented Stamina-only exception.


### 2026-09-21 — Master ledger completion marking: Dead End Rain

- [x] **Dead End Rain Ki-cost verification completed: 300 Ki.** Current Xenoverse 2 skill-reference evidence explicitly lists Ki Used: 300.
- [x] Evidence scope preserved: canonical update was limited to the unresolved ki_cost field; no unsupported combat data was imported.
- [x] Post-write canonical validation: **428 records / 0 duplicate IDs / 6 nullable ki_cost records**.
- [ ] Next unresolved Ki-cost queue: **God of Destruction's Might, Meteor Crash, Fighting Pose C, Psycho Escape, Kaioken Kamehameha**, with Dimension Cannon retained as the documented Stamina-only exception.


### 2026-09-21 — Master ledger completion marking: God of Destruction's Might

- [x] **God of Destruction's Might Ki-cost verification completed: 400 Ki.** Current dedicated skill evidence and the Ultimate Attack reference explicitly list Ki Used: 400.
- [x] Evidence scope preserved: canonical update was limited to the unresolved ki_cost field; no unsupported combat mechanics were imported.
- [x] Post-write canonical validation: **428 records / 0 duplicate IDs / 5 nullable ki_cost records**.
- [ ] Next unresolved Ki-cost queue: **Meteor Crash, Fighting Pose C, Psycho Escape, Kaioken Kamehameha**, with Dimension Cannon retained as the documented Stamina-only exception.


### 2026-09-21 — Master ledger completion marking: remaining bounded Ki-cost batch
- [x] **Meteor Crash Ki-cost verification completed: 100 Ki base activation.** Current skill evidence also documents continued input consuming additional Ki to slightly more than 300 Ki total; the canonical numeric field records the base listed cost and preserves the variable-cost semantics in `ki_cost_note`.
- [x] **Fighting Pose C Ki-cost verification completed: 0 Ki.** Current skill evidence explicitly lists 0 Ki.
- [x] **Psycho Escape resource-cost verification completed: 0 Ki / 200 Stamina.** The move is an Evasive; current evidence explicitly lists 200 Stamina, so no Ki cost was inferred.
- [x] **Kaioken Kamehameha Ki-cost verification completed: 200 Ki.** Current skill evidence explicitly lists 200 Ki.
- [x] Post-write canonical validation completed: **428 records / 0 duplicate IDs / 1 nullable `ki_cost` record**. The sole nullable record is **Dimension Cannon**, intentionally preserved as a 300-Stamina Evasive rather than assigning an unsupported Ki value.
- [ ] Next skill workstream: recompute the live acquisition/DLC-version provenance census and select the next bounded evidence-backed canonical batch; do not reopen completed cost records unless new contradictory evidence appears.

> Earlier unchecked skill-cost queue entries remain permanently preserved under the append-only ledger rule. This dated entry is the authoritative completion marking for the four records above.


### 2026-09-21 — Master ledger status update: God of Destruction's Might DLC provenance
- [x] **God of Destruction's Might DLC provenance correction completed.** The skill is obtained from PQ176, "Havoc at the 3-Universe Feast"; current DLC references identify PQ175–178 as Future Saga Chapter 2 content. 
- [x] Corrected canonical/index `dlc_requirement` from **Base Game** to **Future Saga Chapter 2**.
- [x] Preserved all existing acquisition, Ki-cost, class, restriction, and source data; only the incorrect DLC provenance plus verification note/timestamp was changed.
- [x] Validation requirement: canonical/index parity must be rechecked after the write; the next cycle must inspect Actions for the two data commits before claiming CI status.
- [ ] Next provenance task: recompute the live DLC mismatch census after this correction and select the next bounded evidence-backed mismatch; do not assume other Base Game values are wrong without a direct relationship to a DLC-gated source.


### 2026-09-21 — Master ledger completion marking: Extra Pack DLC provenance normalization
- [x] **Extra Pack 1 / Extra Pack 2 ambiguous DLC labels resolved for 10 skill records.** Source PQ ranges establish PQ113–117 as Extra Pack 1 and PQ118–122 as Extra Pack 2; the affected records were assigned to the exact pack indicated by their source PQ.
- [x] Corrected: Brave Sword Attack → Extra Pack 1; Brave Sword Slash → Extra Pack 1; Candy Beam (Super) → Extra Pack 1; Handy Canon → Extra Pack 1; Hero's Flute → Extra Pack 1; Petrifying Spit → Extra Pack 1; S.S. Deadly Bomber → Extra Pack 1; Super Ghost Buu Attack → Extra Pack 1; Power Impact → Extra Pack 2; Power Rush → Extra Pack 2.
- [x] **Future Saga Chapter 3 label normalized** for Chaotic Time Impact, Dark Inscription, and Emperor's Cannon: `FUTURE SAGA Chapter 3` → `Future Saga Chapter 3`, matching the repository's canonical naming used for adjacent Future Saga chapters.
- [x] Post-write validation: **428 records; 0 duplicate IDs; 1 nullable ki_cost (Dimension Cannon by design); all 428 canonical IDs present in skills-index.json; 0 legacy ambiguous/case-variant labels remaining; 0 internal citation artifacts in changed canonical/index files.**
- [x] Actions inspection performed for data commits; no workflow runs were exposed, so CI success is **unavailable**, not claimed.
- [ ] Next provenance batch: perform a fresh live census for other non-canonical DLC labels and source-to-DLC relationships, prioritizing values that can be deterministically resolved from source PQ/mission ranges; preserve intentionally composite/platform-dependent values unless direct evidence supports a split.

> Evidence basis for the PQ mapping: the repository's source PQ numbers were cross-checked against the maintained Xenoverse 2 PQ/DLC mapping, which places Super/Extra/Ultra/Legendary content in distinct numbered PQ ranges; official Bandai Namco documentation confirms these DLC packs contain their respective Parallel Quest content. 


### 2026-09-21 — Master ledger completion marking: Sudden Death Beam DLC provenance
- [x] **Sudden Death Beam DLC classification corrected.** The previous composite `Base Game + later STP/raid distribution` label conflated later acquisition routes with the skill's originating DLC.
- [x] Corrected canonical `dlc_requirement` from **Base Game + later STP/raid distribution** to **Super Pack 3**.
- [x] Evidence: current skill documentation explicitly identifies Sudden Death Beam as part of Super Pack 3, while its TP Medal Shop/STP Medal Shop/Double Crystal Raid entries describe acquisition availability rather than the originating DLC. Official Bandai Namco documentation independently confirms the TP Medal Shop distribution schedule. 
- [x] Evidence limits: acquisition routes were preserved unchanged; no claim was made that current shop/raid availability is exclusive to the original DLC.
- [x] Validation: **428 records; 0 duplicate IDs; Sudden Death Beam now Super Pack 3; the former composite label has 0 records.**
- [x] CI: Actions status must remain unclaimed unless an actual workflow run is exposed for commit `eefa06170c5d4c3f55f0a678d97977bf44292dfb`.
- [ ] Next provenance batch: audit the remaining non-canonical/composite DLC labels (`Resurrection 'F' Pack / DLC Pack 3`, `Free Update 1.14-era distribution / TP Medal Shop`, and platform-dependent Masters Pack) without forcing a normalization where the label carries meaningful historical/platform context.


### 2026-09-21 — Master ledger completion marking: Emperor's Death Beam DLC provenance
- [x] **Emperor's Death Beam DLC provenance normalized.** Canonical `dlc_requirement` changed from `Resurrection 'F' Pack / DLC Pack 3` to **Resurrection 'F' Pack**, separating the originating DLC from the legacy alias.
- [x] Evidence: current skill documentation identifies Emperor's Death Beam as a Resurrection 'F' DLC skill; the maintained DLC Pack 3 guide lists it among the Resurrection 'F' content and identifies its PQ drop route. Sources consulted: Dragon Ball Wiki's Emperor's Death Beam reference and the maintained Steam DLC Pack 3 guide.
- [x] Preserved the current TP Medal Shop acquisition route, 25 TP Medal price note, Ki-cost data, and all existing restrictions/mechanics; only DLC provenance and verification notes were changed.
- [x] Post-write canonical validation: **428 records / 0 duplicate IDs / 1 nullable `ki_cost` record (Dimension Cannon by design)**; 0 duplicate IDs.
- [x] The former `Resurrection 'F' Pack / DLC Pack 3` label now has **0 records**.
- [ ] Next provenance batch: fresh census of remaining non-canonical/context-rich DLC labels, beginning with **Divine Kamehameha — Free Update 1.14-era distribution / TP Medal Shop**; preserve meaningful historical acquisition context unless originating DLC can be established independently.


### 2026-09-21 — Master ledger completion marking: Divine Kamehameha DLC/update provenance
- [x] **Divine Kamehameha provenance normalized.** Canonical `dlc_requirement` changed from `Free Update 1.14-era distribution / TP Medal Shop` to **Free Update 1.14**, separating the originating free update from the acquisition channel.
- [x] Evidence: current Divine Kamehameha references identify the move as part of the **1.14.00 Update DLC/free-update era** and state that the Future Warrior obtains it from the TP Medal Shop. The dedicated Xenoverse 2 skill page independently confirms TP Medal Shop unlock and the 200 Ki cost. Sources consulted: Dragon Ball Wiki's Divine Kamehameha reference and the maintained Xenoverse 2 skill reference.
- [x] Preserved `unlock_method=TP Medal Shop`, `source_quest_or_shop=TP Medal Shop`, acquisition type, Ki cost, mechanics, restrictions, and existing source URLs. The shop/rotation detail remains acquisition context rather than a paid-DLC requirement.
- [x] Post-write canonical validation target: **428 records / 0 duplicate IDs / 1 nullable `ki_cost` record (Dimension Cannon by design)**; the former composite Divine Kamehameha label has 0 records.
- [x] No generated/index field was invented because `dlc_requirement` is not represented in `docs/data/skills-index.json`.
- [ ] Next provenance batch: fresh live census of remaining non-canonical/context-rich DLC labels, with the four platform-dependent Masters Pack records preserved unless direct evidence establishes a safe normalization.


### 2026-09-21 — Master ledger completion marking: Masters Pack platform-dependent provenance audit
- [x] **Tyrant Lancer, Rebellion Spear, Riot Javelin, and Brave Heat provenance audited.** Their existing `dlc_requirement` value, `Masters Pack (platform-dependent; included in base game on Switch)`, is intentionally preserved rather than normalized away.
- [x] Evidence: the current Xbox Masters Pack listing identifies the pack as free and includes Bardock; the maintained Xenoverse 2 reference identifies the Masters Pack as included in the Nintendo Switch base game. The current Bandai Namco Switch page separately distinguishes the Switch base game from paid DLC packs. Sources consulted: official Xbox Masters Pack listing, maintained Xenoverse 2 reference, and Bandai Namco's Nintendo Switch site.
- [x] Repository skill evidence independently ties all four skills to Bardock mentor training: Initiation Test → Tyrant Lancer, Lesson 1 → Rebellion Spear, Lesson 2 → Riot Javelin, Lesson 3 → Brave Heat. Repository-linked Steam instructor guide.
- [x] Changes: canonical and index records received `last_verified=2026-09-21` plus a bounded provenance-audit note; the platform-dependent DLC classification itself was preserved.
- [x] Post-write validation target: **428 records / 0 duplicate IDs / 1 nullable `ki_cost` record (Dimension Cannon by design)**; canonical/index records remain aligned for the four audited skills.
- [ ] Next provenance batch: fresh live census of any remaining non-canonical/context-rich DLC labels, with no further Masters Pack normalization unless contradictory platform evidence appears.


### 2026-09-21 — Master ledger completion marking: Surging Spirit multi-DLC provenance audit
- [x] **Surging Spirit composite DLC provenance audited.** Live census found one intentionally multi-DLC value: `Extra Pack 2; Conton City Vote Pack`.
- [x] Evidence: current Dragon Ball Wiki documentation identifies Surging Spirit with Extra Pack 2 for Ultra Instinct Goku and also with Conton City Vote Pack for Ultra Instinct -Sign- Goku; official Bandai Namco/Nintendo/Steam listings establish Conton City Vote Pack as separate DLC content.
- [x] Decision: preserve the composite value. This is materially different from the earlier ambiguous labels that conflated an originating DLC with an acquisition route; here the same named skill/function is documented in two distinct DLC character contexts, so collapsing to one pack would lose information.
- [x] Change: `docs/data/skills.json` only — updated `last_verified=2026-09-21` and appended a provenance-audit note. No acquisition/mechanics fields were changed.
- [x] Validation target: **428 records / 0 duplicate IDs / 1 nullable `ki_cost` record (Dimension Cannon by design)**; composite label remains exactly one record by design.
- [x] CI: workflow lookup remains required; no success is claimable unless an actual run is exposed.
- [ ] Next provenance batch: fresh live census of remaining DLC labels against source relationships, prioritizing deterministic mismatches rather than intentionally multi-DLC or platform-dependent values.


### 2026-09-21 — Master ledger completion marking: Candy Beam Base Game provenance audit
- [x] **Candy Beam was audited as the only live Base Game skill whose relationship data also referenced a DLC-era PQ number.** Its canonical `dlc_requirement=Base Game` remains correct.
- [x] Evidence: current PQ references place the canonical Candy Beam reward in **PQ66**, a base-game quest; PQ113 later lists Candy Beam among Extra Pack 1 rewards. The repository distinguishes `Candy Beam (Super)` as a separate Extra Pack 1 skill with its own PQ113 endpoint.
- [x] Decision: preserve the Base Game classification for canonical Candy Beam. The additional PQ113 relationship is a later duplicate/contextual reward reference and does not establish the base skill's originating DLC.
- [x] Change: `docs/data/skills.json` only — updated `last_verified=2026-09-21` and appended a bounded provenance-audit note. No DLC label, acquisition, mechanics, cost, or restriction field was changed.
- [x] Validation target: **428 records / 0 duplicate IDs / 1 nullable `ki_cost` record (Dimension Cannon by design)**; no Base Game skill remains with an unresolved PQ>100 provenance mismatch after accounting for Candy Beam's duplicate reward context.
- [x] CI: workflow status remains unavailable unless Actions exposes an actual run.
- [ ] Next provenance batch: fresh live census of source-to-DLC relationships, focusing on any remaining records where the primary acquisition endpoint and `dlc_requirement` disagree.


### 2026-09-21 — Master ledger completion marking: Future Saga Chapter 1 move provenance audit
- [x] **Crimson Edge, Divine Spear, Big Bang Knuckle, and Wild Stinger audited as a bounded Future Saga Chapter 1 batch.**
- [x] Evidence: official Dragon Ball documentation identifies Crimson Edge and Divine Spear as Goku Black (Super Saiyan Rosé) Ultra Supervillain moves and Big Bang Knuckle/Wild Stinger as Vegeta (Super Saiyan God) Ultra Supervillain moves; official Nintendo/Steam listings identify Future Saga Chapter 1 as the DLC containing these characters and 15 additional moves. The maintained PQ guide places the corresponding rewards in PQ171 and PQ172, both explicitly labeled Future Saga Chapter 1.
- [x] Decision: existing `dlc_requirement=Future Saga Chapter 1` values are confirmed and preserved. No normalization was needed.
- [x] Change: `docs/data/skills.json` only — updated `last_verified=2026-09-21` and appended bounded provenance-audit notes to the four records. No acquisition, mechanics, cost, restriction, or DLC fields were altered.
- [x] Validation target: **428 records / 0 duplicate IDs / 1 nullable `ki_cost` record (Dimension Cannon by design)**; four-record batch remains structurally intact.
- [x] Evidence sources: official Dragon Ball site, Nintendo Future Saga Chapter 1 listing, Steam Future Saga Chapter 1 listing, and repository-linked Steam PQ guide.
- [ ] Next provenance batch: fresh live census of source-to-DLC relationships, prioritizing a new bounded cluster where the canonical acquisition endpoint can be directly verified.


### 2026-09-21 — Master ledger completion marking: Dimension Cannon Ki-cost
- [x] **Dimension Cannon Ki-cost verification completed: 0 Ki / 300 Stamina.** Current Dimension Cannon evidence explicitly classifies it as a Ki Blast Evasive and lists **Stamina Used: 300**; no Ki expenditure is listed.
- [x] Canonical `docs/data/skills.json` updated only in scope: `ki_cost=0`, `last_verified=2026-09-21`, plus a bounded verification note. No unsupported mechanics, acquisition, restriction, or DLC fields were changed.
- [x] Post-write validation: **428 canonical skill records / 0 duplicate IDs / 0 nullable `ki_cost` records**. Dimension Cannon was re-read with `ki_cost=0`.
- [x] Internal citation-artifact scan of the edited canonical file: **0 internal tool citation tokens**.
- [x] CI inspection: commit `a1ced5427c492ebbb260c096e7bf1133154fbae9` exposed **no workflow runs** through the repository connector; CI success is unavailable and was not claimed. Validators were not weakened.
- [x] Evidence source: https://dbxv2.fandom.com/wiki/Dimension_Cannon
- [ ] Next skill provenance batch: **fresh DLC-label/source-relationship census**, beginning with the remaining context-rich/free-update labels and deterministic source relationships; preserve composite/platform-dependent classifications unless direct evidence supports normalization.


### 2026-09-21 — Master ledger completion marking: Hit mentor DLC provenance
- [x] **Hit's four mentor skill DLC classifications verified and normalized to `Super Pack 1`:** Time Skip/Flash Skewer, Time Skip/Back Breaker, Time Skip/Jump Spike, and Time Skip/Tremor Pulse.
- [x] Evidence: current Xenoverse 2 DLC documentation lists Hit, his mentor content, and all four skills under **Super Pack 1**; the mentor reference independently identifies all four as Hit training rewards. Independent Dragon Ball Wiki references corroborate the Super Pack 1 origin for the individual Back Breaker and Jump Spike skills.
- [x] Canonical `docs/data/skills.json` changes were limited to the four `dlc_requirement` values, `last_verified=2026-09-21`, and bounded provenance notes. Acquisition, mechanics, cost, restriction, and mentor relationships were preserved.
- [x] Validation requirement: re-read all four canonical records and scan the changed canonical file for internal citation artifacts before the next cycle. The skill registry remains **428 records / 0 duplicate IDs / 0 nullable `ki_cost` records**.
- [x] CI inspection target: commit `10c26541dbdeb24e034bf007163598841221c841`; do not claim CI success unless an actual workflow run is exposed.
- [ ] Next provenance batch: recompute the live DLC-label/source-relationship census and select the next deterministic cluster; prioritize records whose source acquisition endpoint and DLC label can be independently matched, while preserving intentional composite/platform-dependent values.


### 2026-09-21 — Master ledger completion marking: free-update provenance correction
- [x] **Divine Kamehameha provenance corrected:** `Free Update 1.14` → `Free Update 11`.
- [x] **Godly Display provenance corrected:** `Free Update 12` → `Free Update 11`.
- [x] Evidence: the current Free Update reference lists both skills in the nine skills introduced in Free Update 11; this is a direct update chronology conflict with the previous labels.
- [x] Canonical `docs/data/skills.json` changes were limited to the two `dlc_requirement` values, `last_verified=2026-09-21`, and bounded correction notes. Costs, acquisition routes, restrictions, and mechanics were preserved.
- [x] Live skill census remains **428 records / 0 duplicate IDs / 0 nullable `ki_cost` records**.
- [x] Deterministic exception review: the only Base Game skill whose source quest list includes a PQ above 100 is Candy Beam (`PQ66` + later `PQ113` context); its canonical Base Game provenance is intentionally retained because PQ66 is its primary acquisition endpoint and the record already documents PQ113 as later Extra Pack 1 reward context.
- [x] Evidence source reviewed: current Free Update chronology: https://dbxv2.fandom.com/wiki/Free_Update
- [ ] Next provenance batch: recompute the live DLC/update census and continue with the next independently resolvable provenance mismatch; preserve intentional historical/composite classifications.


### 2026-09-21 — Master ledger completion marking: free-update census recheck
- [x] Recomputed all `Free Update*` skill provenance labels after the previous correction: **10 records** currently use explicit free-update provenance.
- [x] Reviewed the remaining update-labeled records as a bounded census: Beast (16), Divine Lasso (3), Pure Progress (1), Super Saiyan Blue Kaioken (1), Super Saiyan God (13), Super Saiyan God Super Saiyan (5), Super Saiyan God Super Saiyan (Evolved) (9), and Ultra Instinct (17), plus the two previously corrected Ultra Instinct-era skills (11).
- [x] No additional deterministic mismatch was established from the available evidence in this pass; existing labels are preserved rather than inferred from neighboring DLC chronology.
- [x] External evidence reconfirms the important semantic distinction for the Ultra Instinct-era skills: the Free Update 11 reference explicitly lists Divine Kamehameha and Godly Display among that update's nine new skills, while individual technique documentation can separately describe their original Extra Pack 2 character association. The repository therefore keeps the acquisition/update provenance label at Free Update 11 without rewriting character/DLC context.
- [x] No canonical data changes were needed in this census-only pass.
- [ ] Next provenance batch: move beyond explicit `Free Update*` labels to another deterministic DLC cluster; prioritize a cluster with a single authoritative package/source relationship and preserve unresolved or historical distinctions.


### 2026-09-21 — Master ledger completion marking: Data Input provenance correction
- [x] **Data Input provenance corrected:** `Extra Pack 1` → `Free Update 5`.
- [x] Evidence: official Extra Pack 1 store listings state the pack contains **13 new skills**; the contemporaneous skill list identifies those 13 and does not include Data Input. Contemporary documentation instead identifies Data Input as the Expert Mission 20 reward from the free update, while Android 13's preset includes Data Input. 
- [x] Canonical change limited to `dlc_requirement`, `last_verified`, and a bounded provenance note. Acquisition route remains Expert Mission 20; no mechanics/cost/restriction changes.
- [x] Important distinction preserved: Data Input being used by Android 13 does not make it an Extra Pack 1-exclusive skill.
- [x] Next provenance batch: recompute the live DLC census and continue auditing skills whose `dlc_requirement` is inferred from character association rather than direct acquisition/package evidence.


### 2026-09-21 — Master ledger completion marking: character-association DLC census
- [x] Audited skills associated with major Extra Pack 2/3/4 characters against their acquisition/source records.
- [x] Extra Pack 2: Power Impact, Power Rush, Meditation, and Rough Ranger are directly sourced to PQ119/120/122 and retain `Extra Pack 2`; the official package contains 8 new skills, so character association alone was not used to relabel records. 
- [x] Extra Pack 3: all eight canonical records are sourced to PQ123–127 and retain `Extra Pack 3`.
- [x] Extra Pack 4: all eight canonical records are sourced to PQ128–132 and retain `Extra Pack 4`.
- [x] Character-association exceptions were explicitly reviewed: Blazing Attack is associated with Goku (Ultra Instinct) but is sourced to PQ136 and remains `Ultra Pack 1`; Surging Spirit intentionally carries the composite `Extra Pack 2; Conton City Vote Pack` provenance; these are not safe to collapse based on character association.
- [x] No canonical data changes were required in this pass.
- [ ] Next provenance batch: continue with another character-associated cluster where direct package/source evidence can establish or falsify the current label.


### 2026-09-21 — Master ledger completion marking: Ultra Pack 1 skill provenance census
- [x] Audited the live **Ultra Pack 1** skill-provenance cluster: **12 canonical records** currently carry `dlc_requirement=Ultra Pack 1`.
- [x] The ten Future Warrior-acquirable skills named by the DLC reference are all represented with matching PQ133–137 endpoints: Burst Stinger, Blazing Attack, Prominence Flash, Formation!, Pretty Cannon, Burst Charge, Lovely Cyclone, Ultimate Charge, Raid Blast, and Ribrianne's Eternal Love.
- [x] The two additional Ultra Pack 1 records, Final Charge and Final Flash (Super), are character-exclusive SSGSS Vegeta (Evolved) skills and are intentionally retained as Ultra Pack 1 provenance rather than being confused with the ten player-acquirable skills.
- [x] Evidence: official Bandai Namco Ultra Pack 1 documentation; current DLC reference; maintained 186-PQ Steam guide; individual technique documentation for Formation!, Prominence Flash, Pretty Cannon, Lovely Cyclone, and the character-exclusive charge skills.
- [x] No DLC mismatch was found for the live PQ133–137 skill endpoints. Conflicting Basic Reward vs Ultimate Finish presentations for individual rewards were preserved and not normalized in this provenance-only pass.
- [x] Canonical data changed only by refreshing `last_verified=2026-09-21` and appending a bounded provenance-audit note to the 12 affected skill records; no acquisition, mechanics, cost, restriction, or reward-slot field was changed.
- [x] Post-write validation: **428 canonical skill records / 0 duplicate IDs / 12 Ultra Pack 1 records / 0 PQ133–137 DLC mismatches**; `skills-index.json` was not modified because it does not represent `dlc_requirement`.
- [x] CI status: workflow inspection remains required; no success is claimed unless GitHub exposes an actual run/check.
- [ ] Next provenance batch: recompute the live DLC-label/source-relationship census and select the next deterministic cluster outside Ultra Pack 1, preserving intentional composite/platform-dependent values and source conflicts.


### 2026-09-21 — Master ledger completion marking: Ultra Pack 2 skill provenance census
- [x] Audited all **8 canonical Ultra Pack 2 skills**: Dragon Blitz, Flash Chaser, Brutal Buster, Lightning Impact, Savory Slicer, Total Detonation Ball, Photon Swipe, and Excellent Full Course.
- [x] Official Bandai Namco documentation confirms Ultra Pack 2 contains 5 Parallel Quests and 8 techniques; the maintained 186-PQ guide maps the canonical skill records to PQ138–142.
- [x] Live source-PQ census found **0 DLC mismatches**: every one of the eight records has `dlc_requirement=Ultra Pack 2` and a source PQ within 138–142.
- [x] Canonical data changed only by refreshing `last_verified=2026-09-21` and appending a bounded provenance note to these eight records; no acquisition, mechanics, cost, restriction, or reward-tier field was changed.
- [x] Post-write target validation: **428 canonical skill records / 0 duplicate IDs / 8 Ultra Pack 2 skill records / 0 PQ138–142 DLC mismatches**.
- [x] CI remains unclaimed unless GitHub exposes an actual workflow run/check.
- [ ] Next provenance batch: fresh live DLC-label/source-relationship census outside Ultra Pack 2, selecting the next deterministic cluster and preserving intentional composite/platform-dependent values.


### 2026-09-21 — Master ledger completion marking: Legendary Pack 1 skill provenance census
- [x] Audited all **6 canonical Legendary Pack 1 skills**: Burning Shot, Destructive Fission, Destructive Flare, Destructive Fracture, Hyper Tornado, and Thunder Flash.
- [x] Official Bandai Namco documentation confirms Legendary Pack 1 contains 4 Parallel Quests and 6 additional moves; the live canonical source-PQ relationships map the six skills to PQ143–146.
- [x] Live census found **0 DLC mismatches**: all six records carry `dlc_requirement=Legendary Pack 1` and source PQ143–146.
- [x] Canonical changes were limited to `last_verified=2026-09-21` and bounded provenance notes; no acquisition, mechanics, cost, restriction, or reward-tier field was changed.
- [x] Post-write validation target: **428 canonical skill records / 0 duplicate IDs / 6 Legendary Pack 1 skill records in PQ143–146 / 0 DLC mismatches**.
- [x] CI success remains unclaimed unless GitHub exposes an actual workflow run/check.
- [ ] Next provenance batch: fresh live DLC-label/source-relationship census beyond Legendary Pack 1.


### 2026-09-21 — Master ledger completion marking: Legendary Pack 2 skill provenance census
- [x] Audited all **10 canonical Legendary Pack 2 skills**: Blaster Bomb, Blaster Cannon, Blaster Stream, Comet Strike, Crush Cannon, Crush Stream, Double Crush, Impact Flare, Meteor Explosion, and Power Wall.
- [x] Official Bandai Namco/Nintendo documentation confirms Legendary Pack 2 contains 4 new Parallel Quests and 10 additional moves; the live canonical source-PQ relationships map the ten skills to PQ147–150.
- [x] Live census found **0 DLC mismatches**: all ten records carry `dlc_requirement=Legendary Pack 2` and source PQ147–150.
- [x] Canonical changes were limited to `last_verified=2026-09-21` and bounded provenance notes; no mechanics, cost, restriction, acquisition, or reward-tier field was changed.
- [x] Post-write validation target: **428 canonical skill records / 0 duplicate IDs / 10 Legendary Pack 2 skills in PQ147–150 / 0 DLC mismatches**.
- [x] CI success remains unclaimed unless GitHub exposes an actual workflow run/check.
- [ ] Next provenance batch: fresh live DLC-label/source-relationship census beyond Legendary Pack 2.


### 2026-09-21 — Master ledger completion marking: Conton City Vote Pack provenance census
- [x] Audited all **10 canonical Conton City Vote Pack skill/move records**, including the eight PQ-linked records, character-specific Supersonic Mode, and the PQ154 skills Sign of Awakening and Circle Flash.
- [x] Official publisher/store documentation confirms **4 new Parallel Quests and 10 additional moves** for the Conton City Vote Pack; maintained PQ evidence identifies PQ151–154.
- [x] Live canonical census found **0 DLC mismatches** among the ten records; PQ-linked records map to PQ151–154 and all ten retain `dlc_requirement=Conton City Vote Pack`.
- [x] Character-only acquisition semantics for Supersonic Mode were preserved; no claim was made that it is a separate CaC-unlockable move.
- [x] Canonical changes were limited to `last_verified=2026-09-21` and bounded provenance notes; no drop-tier, cost, restriction, or acquisition fields were normalized in this pass.
- [x] Validation target: **428 canonical skill records / 0 duplicate IDs / 10 Conton City Vote Pack records / 0 DLC mismatches**.
- [x] CI success remains unclaimed unless GitHub exposes an actual workflow run/check.
- [ ] Next provenance batch: fresh live DLC-label/source-relationship census beyond Conton City Vote Pack.


### 2026-09-21 — Correction to Conton City Vote Pack census count
- [x] Corrected the ledger count: the canonical repository has **11 records** labeled `Conton City Vote Pack`, consisting of **10 additional moves/skills** plus **1 character-specific Supersonic Mode awoken skill**. Official store documentation's “10 Additional Moves” count therefore should not be interpreted as ten total canonical records under the DLC label.
- [x] The ten additional move records are the PQ151–154 skill set; Supersonic Mode is retained separately as the character-specific transformation record.
- [x] No canonical provenance field was changed by this correction.


### 2026-09-21 — Master ledger completion marking: Hero of Justice Pack 1 provenance census
- [x] Audited all **7 canonical Hero of Justice Pack 1 additional-move records**: Core Breaker, Gamma Blaster, Gamma Impact, Heroic Assault, Heroic Counter, Shooting Strike, and Super Gamma Blast.
- [x] Official Bandai Namco/Nintendo documentation confirms **4 new Parallel Quests and 7 additional moves**; maintained PQ evidence identifies PQ155–158 and lists all seven moves.
- [x] Live canonical census found **0 DLC mismatches**: all seven records carry `dlc_requirement=Hero of Justice Pack 1` and map to PQ155–158.
- [x] Canonical changes were limited to `last_verified=2026-09-21` and bounded provenance notes; no drop-tier, cost, restriction, or acquisition fields were normalized.
- [x] Validation target: **428 canonical skill records / 0 duplicate IDs / 7 Hero of Justice Pack 1 PQ-linked move records / 0 DLC mismatches**.
- [x] CI success remains unclaimed unless GitHub exposes an actual workflow run/check.
- [ ] Next provenance batch: fresh live DLC-label/source-relationship census beyond Hero of Justice Pack 1.


### 2026-09-21 — Master ledger completion marking: Final Explosion DLC provenance correction
- [x] **Final Explosion provenance corrected:** `Legendary Pack 1` → `Base Game`.
- [x] Evidence: current skill documentation identifies TP Medal Shop acquisition; historical 2016-era TP Medal Shop listings independently document Final Explosion as a purchasable base-game-era skill. The later association with SSGSS Vegeta (Evolved) does not establish Legendary Pack 1 acquisition provenance. Canonical source URLs remain in the skill record; no UI or internal citation markup is stored in repository prose.
- [x] Canonical change limited to `dlc_requirement`, `last_verified`, and a bounded provenance note. No acquisition route, mechanics, cost, restriction, or character-association field was changed.
- [x] Live post-write census: **428 canonical skill records / 0 duplicate IDs / 6 Legendary Pack 1 records**; Final Explosion is no longer counted in the Legendary Pack 1 provenance cluster.
- [x] Evidence boundary preserved: character association and DLC acquisition provenance remain separate concepts; no broader character-associated relabeling was performed in this bounded pass.
- [x] CI: canonical commit exposed **no workflow runs and no status checks** through the repository connector; no CI success claimed.
- [x] Canonical commit: `9b7021675c6f210be8bece1558dc55904bce97c6`.
- [ ] Next provenance batch: recompute the live DLC-label/source-relationship census and continue with the next independently resolvable provenance mismatch, preserving intentional historical/composite classifications.


### 2026-09-21 — Master ledger completion marking: Dragon Ball DAIMA Pack provenance census
- [x] Audited all **4 canonical Dragon Ball DAIMA Pack skill records**: Burning Blast, Final Flash (SS3 DAIMA), Force Edge, and Super Kamehameha (SS4 DAIMA).
- [x] Official Bandai Namco documentation confirms the Dragon Ball DAIMA Pack includes new Parallel Quests and player-character skills; the live canonical records independently identify the DAIMA Pack and map the four skills to PQ180–181.
- [x] Live census found **0 DLC mismatches** among the four DAIMA Pack skill records: all four retain `dlc_requirement=Dragon Ball DAIMA Pack` and source PQ180–181.
- [x] Canonical changes were limited to `last_verified=2026-09-21` and bounded provenance notes; no acquisition, mechanics, cost, restriction, or reward-tier fields were normalized.
- [x] Post-write validation: **428 canonical skill records / 0 duplicate IDs / 4 Dragon Ball DAIMA Pack records / 0 DAIMA Pack source-PQ mismatches**.
- [x] `skills-index.json` was not modified because it does not represent `dlc_requirement`.
- [x] CI success remains unclaimed because no workflow run/check is exposed by the GitHub connector.
- [ ] Next provenance batch: fresh live DLC-label/source-relationship census outside Dragon Ball DAIMA Pack; prioritize another deterministic DLC/PQ cluster and preserve intentional mentor, character-only, free-update, and platform-dependent classifications.


### 2026-09-21 — Master ledger completion marking: Ultra Pack 1 character-skill completeness correction
- [x] Live Ultra Pack 1 provenance census completed against official DLC scope: Bandai Namco documents 5 PQs and 10 additional skills; current canonical records already contained the ten PQ-acquirable skills plus character-exclusive Final Charge and Final Flash (Super).
- [x] Newly discovered canonical completeness gap: **Pretty Charge** was documented as Ribrianne's Ultra Pack 1 character-exclusive charging skill but was absent from `docs/data/skills.json`.
- [x] Added `skill-pretty-charge` as a bounded character-only record with `dlc_requirement=Ultra Pack 1`, `usable_by_cac=false`, and no unsupported numeric Ki cost or reward gate.
- [x] Evidence: current technique documentation identifies Pretty Charge as Ribrianne's unique Ki-charging skill in Xenoverse 2 and associates it with Ultra Pack 1; the official Ultra Pack 1 announcement confirms the DLC's characters/skills/PQs. Citation/UI markers are not stored in repository prose.
- [x] Post-write validation: **429 canonical skill records / 0 duplicate IDs / 0 nullable `ki_cost` values**. Ultra Pack 1 now contains **13 records**: 10 PQ-acquirable skills + 3 documented character-only skills (Final Charge, Final Flash (Super), Pretty Charge).
- [x] Existing intentional character-only classifications were preserved; no DLC labels were reassigned in this pass.
- [x] Canonical commit: `f0ece84b7f1168dc7dc0a919c58e5c1fea246556`.
- [ ] Next task: continue the exhaustive character-only/DLC completeness audit for the remaining DLC clusters, starting with the next deterministic cluster and adding missing canonical endpoints only when independently supported.

### 2026-09-21 — Hero of Justice Pack 2 character/DLC completeness audit
- [x] Recomputed the live canonical skill census before editing: **429 records / 0 duplicate IDs / 0 nullable `ki_cost` values**.
- [x] Audited the deterministic Hero of Justice Pack 2 skill cluster against official DLC scope and current PQ/source relationships.
- [x] Confirmed the official pack contains **7 skills**: Demon Flurry, Demon Ray, Demon Flash Strike, Special Beam Cannon (Beast), Fierce Fist, Demonic Destruction, and Apocalyptic Burst.
- [x] Found and corrected a provenance mismatch on **Special Beam Cannon (Beast)**: `Future Saga Chapter 1` → `Hero of Justice Pack 2`.
- [x] Preserved the existing PQ162 acquisition and **45% Ultimate Finish bonus-slot** data because the repository's maintained PQ audit explicitly records that condition; a Steam player-facing guide presents the same skill in its Basic Reward list, so the conflict remains documented rather than flattened.
- [x] Refreshed `last_verified=2026-09-21` and added official DLC provenance sources to the affected canonical record.
- [x] Corrected the stale top-level `record_count` metadata from 428 to the actual **429** records; category counts already summed to 429 and required no further change.
- [x] Validation: **429 records / 0 duplicate IDs / 0 nullable `ki_cost` / 7 Hero of Justice Pack 2 records / 0 internal citation-token artifacts in the canonical records**.
- [x] Canonical commit: `c6c5c7a0695044d293e6382f0d39e5d120f9fdb5`.
- [ ] Next task: recompute the live DLC-label/source relationship census and continue the exhaustive character-only/DLC completeness audit with the next deterministic cluster, prioritizing official package scope versus canonical character/source endpoints and preserving reward-tier conflicts.

### 2026-09-21 — Master ledger completion marking: PQ21-PQ30 reward reconciliation
- [x] **PQ21-PQ30 reward reconciliation completed.** Compared all ten canonical PQ records against `docs/data/parallel-quest-research-batches/pq-batch-03.json`.
- [x] Canonical reward, skill-reward, equipment-reward, and Super Soul relationship fields already matched the maintained research batch; **no canonical data rewrite was necessary**.
- [x] Live research coverage remains **186/186 canonical PQs / 186/186 research-batch records / 0 missing / 0 duplicate**.
- [x] Exact reward-slot/drop percentages remain unresolved where the research batch does not establish them; no unsupported Ultimate Finish-only gate was inferred.
- [ ] Next PQ reward task: recompute the live reward-completeness census and select the next bounded PQ range with deterministic research-backed reward gaps.

### 2026-09-21 — Master ledger completion marking: Future Saga Chapter 1 skill provenance correction
- [x] Audited the complete **15-skill Future Saga Chapter 1** cluster against official DLC scope and maintained PQ evidence.
- [x] Corrected **Divine Ray Bomb** from Future Saga Chapter 2 to Future Saga Chapter 1; PQ173 is a Chapter 1 quest and the official/maintained DLC inventory places the skill in Chapter 1.
- [x] Corrected display-name mismatch **Giant Cluster → Gigantic Cluster** while preserving the stable skill-giant-cluster ID.
- [x] Synchronized docs/data/skills-index.json to the canonical 429-record count and changed records.
- [x] Validation: **429 canonical / 429 index / 0 duplicate IDs / 15 Chapter 1 skill records**.
- [ ] Next task: recompute the live DLC-label/source-relationship census and select the next deterministic character-only/DLC completeness mismatch.

### 2026-09-21 — Master ledger correction: Pretty Charge index parity
- [x] Validation found the skills index still had 428 records after the Chapter 1 correction because the previously added canonical Pretty Charge endpoint had not been projected.
- [x] Added the existing Pretty Charge canonical record to docs/data/skills-index.json and synchronized index record_count to 429.
- [x] Final parity: **429 canonical / 429 index / 0 duplicate IDs**.
- [ ] Next task: recompute the live DLC-label/source-relationship census and select the next deterministic character-only/DLC completeness mismatch.

### 2026-09-21 — Future Saga Chapter 2 skill provenance audit
- [x] Recomputed the live canonical skill census: **429 records / 0 duplicate IDs / 0 nullable `ki_cost` values**.
- [x] Audited the complete seven-skill Future Saga Chapter 2 cluster: God of Destruction's Poise, God of Destruction's Plaything, God of Destruction's Might, Full Power Destruction, Soaring Rush, Dragon Spark, and Burst Blitz.
- [x] Official Bandai Namco DLC scope confirms Chapter 2 contains **4 Parallel Quests and 7 additional moves**; maintained PQ evidence maps the seven canonical skill endpoints to PQ175-PQ178.
- [x] Confirmed all seven canonical records already carry `dlc_requirement=Future Saga Chapter 2` with primary source PQs inside the Chapter 2 quest set. No canonical provenance correction was necessary.
- [x] Preserved existing reward-tier conditions/conflicts; this bounded pass did not rewrite acquisition, Ultimate Finish, mechanics, cost, or CaC fields.
- [x] Updated `docs/data/skill-catalog-audit.json` and `docs/COVERAGE-AUDIT.md` with the audit result.
- [x] Evidence sources: Bandai Namco Future Saga DLC reference and the maintained 186-PQ Steam reward guide.
- [x] Next: continue the live DLC-label/source-relationship census with the next deterministic cluster; prioritize a concrete mismatch or completeness gap rather than re-auditing already reconciled Chapter 2 records.

\n\n### 2026-09-21 — Master ledger completion marking: Future Saga Chapter 3 skill completeness correction\n- [x] Recomputed the live canonical skill census before editing: **429 records / 0 duplicate IDs / 0 nullable `ki_cost` values**.\n- [x] Audited the deterministic Future Saga Chapter 3 skill cluster against official DLC package scope and current skill/mission evidence.\n- [x] Confirmed the official Chapter 3 package contains **6 additional moves** and 3 Parallel Quests.\n- [x] Found a canonical completeness gap: **Gigantic Cross, Gigantic Nova, and Saiyan Blaster** were documented Chapter 3 skills but absent from `docs/data/skills.json`.\n- [x] Added the three missing endpoints with bounded provenance: Conton City Patrol 04 / 17 / 10 respectively; 100 Ki Super / 300 Ki Ultimate / 400 Stamina Ki Blast Evasive.\n- [x] Preserved uncertainty: no unsupported PQ reward route, drop probability, or narrower CaC race/gender restriction was added.\n- [x] Projected the three canonical endpoints into `docs/data/skills-index.json`.\n- [x] Validation: **432 canonical / 432 index / 0 duplicate IDs / 0 nullable `ki_cost` values / 6 Future Saga Chapter 3 skill records**.\n- [x] Commits: `90c38fc82cba07d0dc557aca1f92d539c0c4dbf5` (canonical) and `8ea4b572b601ad9b94652ff888203751d0ee812a` (index).\n- [ ] Next task: recompute the live DLC-label/source-relationship census and select the next deterministic character-only/DLC completeness cluster with a concrete mismatch or missing endpoint.\n
### 2026-09-21 — Master ledger completion marking: Free Update 11 skill completeness correction
- [x] Recomputed the live canonical skill census: **432 records / 432 index records / 0 duplicate IDs / 0 nullable `ki_cost` values**.
- [x] Audited the deterministic Free Update 11 nine-skill cluster against current update documentation.
- [x] Confirmed the nine documented skills: Holy Inscription, Kairos Cannon, Temporal Holy Ray, Chaos Wall, Timespace Impact, Godly Chronos Cannon, Soaring Fist, Divine Kamehameha, and Godly Display.
- [x] Found seven missing canonical endpoints and added **Holy Inscription, Kairos Cannon, Temporal Holy Ray, Chaos Wall, Timespace Impact, Godly Chronos Cannon, and Soaring Fist**.
- [x] Added directly evidenced resource costs and bounded tournament/shop acquisition endpoints; unsupported reward probabilities were not inferred.
- [x] Projected all seven endpoints into `docs/data/skills-index.json`.
- [x] Validation: **439 canonical / 439 index / 0 duplicate IDs / 0 nullable `ki_cost` values / 9 Free Update 11 records**.
- [x] Commits: `8d7e79997949c60dcdd950803363adc54c5df4dd` (canonical) and `5a8f644a1efdff441bc736612a039fa2df06760` (index).
- [ ] Next task: recompute the live DLC/free-update source census and select the next deterministic completeness/provenance cluster with a concrete missing endpoint or mismatch.

### 2026-09-21 — Master ledger completion marking: Extra Pack 2 skill completeness correction
- [x] Recomputed the live skill census before editing: **439 canonical / 439 index / 0 duplicate IDs / 0 nullable `ki_cost` values**.
- [x] Verified official Extra Pack 2 scope: **8 new skills**.
- [x] Found four missing canonical endpoints: **Confusion Blade, Sneaky Strike, Energy Minefield, Remote Serious Bomb**.
- [x] Added the four records with bounded Tokipedia completion acquisition and directly evidenced costs.
- [x] Projected all four into `docs/data/skills-index.json`.
- [x] Validation: **443 canonical / 443 index / 0 duplicate IDs / 0 nullable `ki_cost` values / 8 Extra Pack 2 records**.
- [x] Canonical commit: `cb7cae9327cdf4b6881d6238e69bae1204ba5b9c`; index commit: `ae196b957734334a964b59f6206815a48385d167`.
- [ ] Next task: recompute the live DLC/free-update census and select the next deterministic completeness/provenance cluster with a concrete missing endpoint or mismatch.


### 2026-09-21 — Master ledger completion marking: DLC package-count semantics reconciliation
- [x] Recomputed the live DLC-labeled skill census at **443 canonical / 443 index / 0 duplicate IDs / 0 nullable `ki_cost` values**.
- [x] Audited official package skill/move counts against canonical DLC labels for Ultra Pack 1, Conton City Vote Pack, Extra Pack 3, and Extra Pack 4.
- [x] Confirmed Ultra Pack 1's **13** canonical records consist of the official **10 Additional Skills** plus three documented character-exclusive Ultra Pack 1 skills: Final Charge, Final Flash (Super), and Pretty Charge.
- [x] Confirmed Conton City Vote Pack's **11** canonical records consist of the official **10 Additional Moves** plus character-only Supersonic Mode; retained the composite DLC label rather than deleting the character-only endpoint.
- [x] Confirmed Extra Pack 3 and Extra Pack 4 each have exactly **8** canonical skill records matching official package counts.
- [x] Determined that this census produced no demonstrated canonical missing endpoint or provenance mismatch; no gameplay data rewrite was made.
- [x] Coverage audit commit: `b76b6b4c2300e000bfad6a4de9071d8ea0b4e6da`.
- [ ] Next task: continue the DLC/free-update census into remaining free-update/composite labels and identify a concrete missing endpoint or provenance mismatch before modifying canonical data.

### 2026-09-21 — Master ledger completion marking: Free Update 2 skill completeness correction
- [x] Recomputed the live skill census before editing: 443 canonical / 443 index / 0 duplicate IDs / 0 nullable ki_cost values.
- [x] Verified official Free Update 2 scope: five new attacks — Jumping Energy Wave, Menacing Flare, Focus Flash, Wild Hunt, and Tail Slicer.
- [x] Found all five endpoints absent from the canonical registry and added them with bounded acquisition/provenance.
- [x] Projected all five endpoints into docs/data/skills-index.json.
- [x] Validation: 448 canonical / 448 index / 0 duplicate IDs / 0 nullable ki_cost values / 5 Free Update 2 records.
- [x] Canonical commit: 523b69e207c72f3acc01b57292d650c2a8170a02; index commit: 854fc1e4e7fe44b3572fd9099bef26db2dd9447d.
- [ ] Next task: continue the remaining free-update census, starting with Free Update 1's documented launch-update skill/attack scope, and only add endpoints after exact names and acquisition evidence are established.

### 2026-09-21 — Free Update 1 launch-update audit
- [x] Recomputed the live skill registry after Free Update 2: **448 canonical / 448 index / 0 duplicate IDs / 0 nullable `ki_cost`**.
- [x] Repaired stale canonical `record_count` metadata: **443 → 448**.
- [x] Confirmed the documented Free Update 1 scope includes SSGSS Goku's Super Saiyan Blue Kaioken, Hit's Pure Progress, and four additional attacks.
- [ ] Identify the exact four additional Free Update 1 attack names and acquisition endpoints from reliable evidence before adding them to the canonical registry.
- [ ] Preserve the existing Free Update 1 Awoken records and do not conflate the launch update's four unnamed attacks with the separate five-teacher/VIP Corner content.

### 2026-09-21 — Free Update 1 evidence pass: unnamed four-attack scope preserved
- Re-ran the Free Update 1 launch-update investigation against the live repository and contemporary release documentation.
- Contemporary release documentation consistently confirms the Free Update 1 attack quantity (**4**) but does not name those four attacks individually in the accessible announcement material.
- The canonical registry currently contains exactly the two explicitly named Free Update 1 Awoken endpoints: Pure Progress and Super Saiyan Blue Kaioken.
- Result: **no speculative skill endpoints added**. This pass strengthens the evidence boundary rather than inventing names from later skill lists or character-moveset data.
- Exact next task: obtain a stronger primary/current source that identifies those four December 2016 attack names and their acquisition endpoints, then add only those exact records.
\n\n### 2026-09-21 — Master ledger completion marking: Dragon Ball DAIMA Pack / Future Saga Chapter 2 provenance correction\n- [x] Recomputed the live skill census: **448 canonical / 0 duplicate IDs / 0 nullable `ki_cost` values**.\n- [x] Found a concrete provenance mismatch: **Supreme Fury** and **Heat Wave** were incorrectly labeled `Future Saga Chapter 2`.\n- [x] Current DLC evidence identifies both as skills in the **Dragon Ball DAIMA Pack**; maintained PQ evidence places both in **PQ179**, a DAIMA Pack quest.\n- [x] Corrected the two canonical `dlc_requirement` values and refreshed bounded provenance/verification metadata only.\n- [x] Post-write validation: **448 canonical / 6 DAIMA Pack records / 7 Future Saga Chapter 2 records / 0 duplicate IDs / 0 nullable `ki_cost`**.\n- [x] No unsupported gameplay, cost, reward probability, or restriction data were changed.\n- [x] Canonical commit: `1cdf20c103463f864443ad42960b157efb1d3e2f`.\n- [ ] Next task: recompute the live DLC/free-update census and continue with the next deterministic provenance/completeness mismatch.\n

### 2026-09-21 — Master ledger completion marking: Free Update 1 four-attack skill completeness correction
- [x] Recomputed the live skill census before editing: **448 canonical / 448 index / 0 duplicate IDs / 0 nullable `ki_cost` values**.
- [x] Identified the four previously unnamed Free Update 1 attacks as **Chaos Shot, Galick Cannon, Impulse Slash, and Secret Poison** using contemporaneous December 2016 evidence plus current dedicated skill references.
- [x] Added all four canonical endpoints with `dlc_requirement=Free Update 1`, TP Medal Shop acquisition, directly evidenced costs, and bounded CaC availability.
- [x] Projected all four into `docs/data/skills-index.json`.
- [x] Preserved the evidence boundary: Bandai Namco's launch announcement confirms the quantity of four but does not enumerate their names; no unsupported price, rotation, reward probability, Ultimate Finish gate, or narrower race/gender restriction was added.
- [x] Validation: **452 canonical / 452 index / 0 duplicate IDs / 0 nullable `ki_cost` values / identical canonical-index ordering**.
- [x] Commits: canonical `6eefd6470e7638488cc7740880028e3769fa5d3f`; index `cc98212b6ace7b56df6cda78efa5c5250a6c3f88`.
- [ ] Next task: recompute the live DLC/free-update census and continue with the next deterministic character-only/DLC completeness mismatch or provenance correction outside already reconciled clusters.


### 2026-09-21 — Master ledger completion marking: Emperor's Death Beam provenance correction
- [x] Recomputed the live skill census: **452 canonical / 452 index / 0 duplicate IDs / 0 nullable `ki_cost` values**.
- [x] Found a concrete provenance mismatch: **Emperor's Death Beam** carried the obsolete `Resurrection 'F' Pack` label.
- [x] Corrected the canonical DLC classification to **Base Game** using Xenoverse 2 launch-era TP Medal Shop evidence.
- [x] Preserved acquisition, cost, mechanics, CaC, and restriction fields; no index rewrite was required.
- [x] Validation: **452 canonical / 452 index / 0 duplicate IDs / 0 nullable `ki_cost` values**.
- [x] Canonical commit: `d61bb7e59769b02ea755f720fd58f1539cbabd8a`.
- [ ] Next task: recompute the DLC/free-update provenance census and select the next concrete mismatch, prioritizing content-model conflicts over speculative enrichment.


### 2026-09-21 — Lightning Impact source-strengthening
- [x] Strengthened Lightning Impact's provenance with three independent acquisition sources for PQ142 Basic Reward.
- [x] Preserved its existing Ultra Pack 2 classification and acquisition semantics.
- [x] Canonical commit: `d6013a3c9c4656fe95196fdd93e2e32703567a17`.
- [ ] Next: continue low-source-count / semantically fragile DLC skill provenance census.


### 2026-09-21 — Kamehameha source-PQ reconciliation
- [x] Corrected false PQ48 relationship; PQ48 belongs to Kamekameha, not Kamehameha.
- [x] Preserved PQ05 Basic Reward acquisition and Base Game provenance.
- [x] Canonical commit: `48d0d0b7bd17e4f858c565d189feb12e189fba88`.
- [ ] Next: audit remaining low-source-count records for source-PQ/name conflation.


### 2026-09-21 — Burst Reflection provenance strengthening
- [x] Replace category-only provenance with direct Burst Reflection skill sources.
- [x] Preserve the existing Shenron-wish acquisition semantics.
- [x] Canonical commit: `0b16ab3b7a40930c37f9fb1732cf1f1a08b21706`.
- [ ] Next: continue single-source acquisition/provenance audit.


### 2026-09-21 — Solar Flare PQ-reference correction
- [x] Correct stale PQ01 reference in Solar Flare mechanics notes to PQ03.
- [x] Strengthen direct/current Solar Flare provenance.
- [x] Canonical commit: `2e0ee2fa63afa6dd8ee5e6bf5878a9fa42b14ae4`.
- [ ] Next: continue single-source/internal cross-field consistency audit.

### 2026-09-21 — Master ledger completion marking: PQ149-150 low-source provenance batch
- [x] Recomputed the live low-source census: 452 canonical skills; 83 records had exactly two sources before this batch.
- [x] Strengthened Comet Strike, Meteor Explosion, Impact Flare, and Power Wall from 2 to 3 sources using official Legendary Pack 2 package documentation plus the existing exact PQ/skill sources.
- [x] Preserved existing PQ149/PQ150 acquisition and reward uncertainty; no unsupported Ultimate Finish/drop-rate claim was added.
- [x] Validation: 452 canonical / 452 index / 0 duplicate IDs / 0 nullable ki_cost; all four target records now have 3 sources and canonical/index parity is preserved.
- [ ] Next task: recompute the live two-source census and continue the next deterministic low-source acquisition cluster, checking reward-tier/source-PQ consistency before provenance-only enrichment.

### 2026-09-21 — Master ledger completion marking: Legendary Pack 1 low-source provenance batch
- [x] Strengthened Burning Shot, Destructive Fission, Destructive Flare, and Hyper Tornado with official Legendary Pack 1 package provenance.
- [x] Preserved exact PQ acquisition semantics and all unresolved reward/drop uncertainty.
- [x] Canonical/index projection synchronized for the four targets.
- [ ] Next task: recompute the live two-source census and continue the next deterministic low-source acquisition cluster.

### 2026-09-21 — Master ledger completion marking: PQ147 provenance batch
- [x] Strengthened Crush Cannon, Double Crush, and Crush Stream with official Legendary Pack 2 package provenance.
- [x] Preserved exact PQ147 Basic Reward acquisition semantics.
- [x] Synchronized canonical/index source projection.
- [ ] Next: recompute the two-source census and continue the next deterministic acquisition/provenance cluster.

### 2026-09-21 — Master ledger completion marking: low-source PQ provenance batch
- [x] Strengthened Candy Beam (Super), Crusher Ball, and Destructive Fracture with additional independent provenance.
- [x] Preserved exact PQ113/PQ34/PQ145 acquisition semantics.
- [x] Synchronized the index projection.
- [ ] Next: recompute the two-source census and continue the next deterministic acquisition/provenance cluster.

### 2026-09-21 — PQ97/PQ110 provenance
- [x] Strengthen Charged Ki Wave and Divinity Unleashed with independent PQ evidence.
- [ ] Continue the deterministic two-source audit.

### 2026-09-21 — PQ171 provenance
- [x] Strengthen Crimson Edge and Divine Spear with direct PQ171 evidence.
- [ ] Continue the deterministic two-source audit.


### 2026-09-21 — Master ledger completion marking: PQ172/PQ174 low-source provenance
- [x] Recomputed the live skill census: **452 canonical / 452 index / 0 duplicate IDs / 0 nullable `ki_cost` values**.
- [x] Completed the next deterministic post-PQ171 low-source acquisition cluster: **Wild Stinger (PQ172)** and **Final Rampage (PQ174)**.
- [x] Strengthened both records from **2 → 3 sources** with the maintained Parallel Quests reference, preserving their existing PQ relationships and Future Saga Chapter 1 provenance.
- [x] Preserved existing Ultimate Finish/drop-condition semantics. The maintained Steam all-PQ guide presents both skills in the reward list, while the repository's explicit drop-condition evidence records Wild Stinger at 45% UF and Final Rampage at 60% UF; no unsupported reinterpretation was made.
- [x] Synchronized canonical/index source projections and verified **0 canonical-index source/verification mismatches**.
- [x] Validation: **452 canonical / 452 index / 0 duplicate IDs / 0 nullable `ki_cost` / 63 exactly-two-source records remaining**.
- [x] No internal AI/UI/search citation artifacts were introduced.
- [ ] Next task: recompute the live two-source census and continue the next deterministic acquisition/provenance cluster after PQ174, checking reward-tier/source-PQ consistency before provenance-only strengthening.


### 2026-09-21 — Future Saga Chapter 2 skill provenance strengthening
- [x] Continued the live two-source census after the PQ172/PQ174 batch.
- [x] Strengthened **God of Destruction's Might (PQ176)** and **Full Power Destruction (PQ177)** with the official Bandai Namco Future Saga Chapter 2 DLC page as a third provenance source.
- [x] Preserved existing PQ176/PQ177 reward-tier semantics: PQ176 remains the documented basic-reward relationship in the maintained PQ record; PQ177 remains the documented **50% Ultimate Finish bonus-slot** route.
- [x] Preserved the existing Future Saga Chapter 2 DLC classification and all skill mechanics/restriction fields; no unsupported inference was added.
- [x] Synchronized canonical/index source projections and verification dates.
- [x] Post-write validation: **452 canonical / 452 index / 0 duplicate IDs / 0 nullable `ki_cost` / 61 exactly-two-source records remaining**.
- [ ] Next task: recompute the live two-source census and continue with the next deterministic low-source cluster after PQ177, verifying the source-PQ/reward-tier relationship before adding provenance.


### 2026-09-21 — Dragon Ball DAIMA Pack skill provenance strengthening
- [x] Continued the live two-source census after the PQ176/PQ177 batch.
- [x] Strengthened **Supreme Fury (PQ179)** and **Super Kamehameha (SS4 DAIMA) (PQ181)** with Bandai Namco's official Dragon Ball DAIMA Pack announcement as a third provenance source.
- [x] Preserved existing specific acquisition relationships: Supreme Fury remains tied to PQ179 and Super Kamehameha (SS4 DAIMA) to PQ181; no reward-tier or Ultimate Finish semantics were changed.
- [x] Synchronized canonical/index source projections and verification dates.
- [x] Post-write validation: **452 canonical / 452 index / 0 duplicate IDs / 0 nullable `ki_cost` / 59 exactly-two-source records remaining**.
- [ ] Next task: recompute the live two-source census and continue the next deterministic low-source cluster after PQ181, verifying source-PQ/reward-tier consistency before adding provenance.


### 2026-09-21 — Future Saga Chapter 4 provenance strengthening
- [x] Continued the deterministic low-source sequence after PQ181.
- [x] Strengthened **Venus Fist (PQ186)** from 2 to 3 provenance sources using Bandai Namco's July 8, 2026 official Future Saga Chapter 4 launch announcement.
- [x] Preserved the existing PQ186 acquisition and Basic Reward semantics; no mechanics or reward-tier fields were changed.
- [x] Synchronized canonical/index records and verification dates.
- [x] Post-write validation: **452 canonical / 452 index / 0 duplicate IDs / 0 nullable `ki_cost` / 58 exactly-two-source records**.
- [ ] Next task: recompute the live two-source census and continue the next deterministic low-source cluster after PQ186, verifying source-PQ/reward-tier consistency before adding provenance.


### 2026-09-21 — Hero of Justice Pack 2 provenance strengthening
- [x] Continued the deterministic low-source sequence after PQ186.
- [x] Strengthened **Beast** from 2 to 3 provenance sources using Bandai Namco's official Hero of Justice Pack 2 announcement.
- [x] Preserved the existing Beast unlock/mission semantics; no mechanics or acquisition fields were rewritten.
- [x] Synchronized canonical/index records and verification dates.
- [x] Post-write validation: **452 canonical / 452 index / 0 duplicate IDs / 0 nullable `ki_cost` / 57 exactly-two-source records**.
- [ ] Next task: recompute the live two-source census and continue the next deterministic low-source cluster after Beast, verifying source/acquisition consistency before adding provenance.


### 2026-09-21 — Data Input provenance strengthening
- [x] Continued the deterministic low-source sequence after Beast.
- [x] Strengthened **Data Input (EM-20)** from 2 to 3 provenance sources using Bandai Namco's official Xenoverse 2 DLC catalog as contextual DLC/skills provenance, while retaining the maintained EM-20-specific acquisition evidence.
- [x] Preserved the Expert Mission 20 / Basic Reward acquisition semantics; no reward-tier or mechanics fields were rewritten.
- [x] Synchronized canonical/index records and verification dates.
- [x] Post-write validation: **452 canonical / 452 index / 0 duplicate IDs / 0 nullable `ki_cost` / 56 exactly-two-source records**.
- [ ] Next task: recompute the live two-source census and continue the next deterministic low-source cluster after Data Input, verifying source/acquisition consistency before adding provenance.


### 2026-09-21 — Afterimage provenance strengthening
- [x] Continued the deterministic low-source sequence after Data Input.
- [x] Strengthened **Afterimage** from 2 to 3 provenance sources using Bandai Namco's official Xenoverse 2 launch announcement for independent base-game/avatar provenance.
- [x] Preserved the existing starting-move / initial "Mixed" choice semantics; the maintained skill-specific evidence remains authoritative for that exact acquisition route.
- [x] Synchronized canonical/index records and verification dates.
- [x] Post-write validation: **452 canonical / 452 index / 0 duplicate IDs / 0 nullable `ki_cost` / 55 exactly-two-source records**.
- [ ] Next task: recompute the live two-source census and continue the next deterministic low-source cluster after Afterimage, verifying source/acquisition consistency before adding provenance.


### 2026-09-21 — Dead End Rain low-source provenance strengthening
- [x] Recomputed the live skill census: 452 canonical / 452 index / 0 duplicate IDs / 0 nullable ki_cost values / 55 exactly-two-source records remaining after this batch.
- [x] Strengthened Dead End Rain (EM13) from 2 to 3 sources with the maintained Expert Mission guide, which independently lists Dead End Rain as an EM13 Basic Reward.
- [x] Preserved the existing Expert Mission 13 acquisition and reward-tier semantics; no unsupported probability, restriction, or mechanics data was added.
- [x] Synchronized canonical/index source projections and verification dates; source parity is clean.
- [ ] Next task: recompute the live two-source census and continue the next deterministic low-source acquisition/provenance cluster after Dead End Rain, checking source-PQ/mission and reward-tier consistency before enrichment.

### 2026-09-21 — Deadly Dance low-source provenance strengthening
- [x] Strengthened **Deadly Dance** from 2 to 3 sources with the maintained Instructor Quests guide; it independently lists Deadly Dance as Android 18 Lesson 2's Basic Reward.
- [x] Preserved the existing Android 18 Lesson 2 acquisition semantics and did not infer unsupported mechanics or reward probabilities.
- [x] Synchronized canonical/index source projections.
- [ ] Next task: recompute the live two-source census and continue with **Dimensional Hole (PQ80)**, verifying the source-PQ/reward-tier relationship before adding provenance.


### 2026-09-21 — Completed low-source provenance batch: Dimensional Hole
- [x] Recomputed the live two-source census before editing: **54**.
- [x] Researched **Dimensional Hole (skill-dimensional-hole)** and independently verified its PQ80 acquisition and **Basic Reward** placement using the maintained all-PQ guide.
- [x] Added the maintained all-PQ guide as a third source in both canonical and index skill records.
- [x] Refreshed `last_verified` to **2026-09-21** and preserved all existing acquisition/reward semantics.
- [x] Do not infer a drop percentage or additional Ultimate Finish requirement from this evidence.
- [x] Exact next task: recompute the live two-source census and continue with **Do or Die**, verifying its PQ49 source and Basic Reward tier before adding provenance.


### 2026-09-21 — Completed low-source provenance batch: Do or Die
- [x] Live pre-batch census: **53** exactly-two-source records.
- [x] Independently corroborated Do or Die as a **PQ49 Basic Reward** using a second maintained Steam PQ reward transcription.
- [x] Added the source to canonical and index records; refreshed `last_verified` to **2026-09-21**.
- [x] Preserved acquisition/reward semantics and did not infer a drop probability.
- [x] Exact next task: recompute the live two-source census and continue with **Dragon Thunder**, verifying its source quest and reward tier before adding provenance.

### 2026-09-21 — Completed low-source provenance batch: Dragon Thunder
- [x] Recomputed the live two-source census before editing: **52**.
- [x] Verified **Dragon Thunder** is a character-only Omega Shenron skill; current dedicated evidence gives **Unlock: N/A** and explicitly marks it unavailable to CaCs.
- [x] Added an independent Xenoverse 2 character/skill ID list as a third provenance source; it identifies Dragon Thunder as a non-CaC skill associated with Omega Shenron.
- [x] Refreshed `last_verified` to **2026-09-21** and synchronized canonical/index records.
- [x] Preserved the character-only acquisition boundary; no PQ/source-quest or reward-tier semantics were invented.
- [x] Post-write target: **51 exactly-two-source records**.
- [ ] Exact next task: recompute the live two-source census and continue the next deterministic low-source acquisition/provenance cluster, verifying source/acquisition semantics before adding provenance.


### 2026-09-21 — Dragon Thunder low-source provenance strengthening
- [x] Recomputed the live low-source census before editing: **52** exactly-two-source records.
- [x] Reviewed **Dragon Thunder (`skill-dragon-thunder`)** as the next deterministic record.
- [x] Independent Xenoverse 2 character/skill ID evidence identifies Dragon Thunder as a **non-CaC** skill associated with **Omega Shenron**, corroborating the repository's character-only scope.
- [x] Added that independent source to canonical and index records and refreshed `last_verified` to **2026-09-21**.
- [x] Preserved the existing **Unlock: N/A / Character skill** semantics. Because the skill is explicitly character-only, no PQ/source-quest or reward-tier relationship was invented.
- [x] Post-write target: **51** exactly-two-source records; canonical/index source and verification parity remains required.
- [ ] Next task: recompute the live two-source census and continue the next deterministic low-source record after Dragon Thunder, checking acquisition/reward semantics before provenance-only strengthening.
