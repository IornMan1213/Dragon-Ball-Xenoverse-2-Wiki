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
