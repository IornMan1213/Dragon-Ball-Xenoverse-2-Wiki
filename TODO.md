# Dragon Ball Xenoverse 2 Wiki — Project TODO

This file is the working project tracker. Statuses describe repository work, not guesses about game facts.

## Scope Standard — Exhaustive Game Encyclopedia

- [ ] Treat the wiki as an exhaustive, excessive reference for **every documented detail of Dragon Ball Xenoverse 2**, not merely a guide to the most popular content.
- [ ] Cover the full game surface area: story/Extra Missions, Parallel Quests, Expert Missions, Time Patrol/Conton City systems, mentors and training, skills, Awoken/Transformations, playable and non-playable characters, CaC/race restrictions, Super Souls, equipment/costumes/accessories, items, currencies, shops, drops/rewards, Dragon Balls/wishes, raids/events, modes, stages, maps/areas, mechanics, combat properties, progression, DLC/free updates, and other discoverable systems.
- [ ] For every record, prefer structured, consistently labeled fields over prose-only descriptions so the information can be searched, compared, validated, and reused by the website and machine-readable datasets.
- [ ] Preserve fine-grained distinctions that are easy to lose: CaC vs character-only availability, race/gender restrictions, DLC ownership vs in-game unlock conditions, first-clear vs repeat rewards, shop rotations, prerequisite progression, costs, resource consumption, damage type, hit behavior, status effects, defensive properties, combo interactions, PvE/PvP behavior, and known exceptions.
- [ ] Keep factual certainty explicit. Do not fill missing details merely to make a record look complete; use `indexed`, `partially_verified`, and `verified` appropriately and preserve source conflicts/unknowns.
- [ ] Use multiple sources where practical, distinguish datamined/researched values from community observations, and record provenance so later verification can replace provisional values without losing research history.
- [ ] Organize the information so exhaustive coverage remains readable: canonical data first, detailed notes second, source/provenance metadata alongside the relevant record, and dedicated indexes/explorers for navigation.
- [ ] Do not let website polish, automation, or batch throughput become a reason to omit game details. Site improvements must expose and organize the expanding database rather than substitute for research.

## Done

- [x] Audited Skill Research Batch 315 for canonical-identity duplication; removed five records already covered by earlier batches while preserving the earlier research history and evidence.
- [x] Confirmed current Xenoverse 2 evidence for Perfect Kamehameha as a 400-Ki Blast Ki Blast Ultimate taught by Perfect Cell; the earlier Batch 312 duplicate is retained as the canonical research history.

- [x] Removed duplicate custom GitHub Pages workflows that could compete with native Pages deployment.
- [x] Removed the duplicate `docs/index.html` Pages entry point.
- [x] Added/expanded the homepage database status and progress indicators.
- [x] Added the internal-artifact cleanup script and cleanup workflow.
- [x] Reworked the skills-sync workflow to use the external research corpus, validation, and PR-based synchronization.
- [x] Established the canonical skills schema and verification states: `indexed`, `partially_verified`, `verified`.
- [x] Added skill research batches 01–14.
- [x] Completed duplicate checks before the recent skill batches.
- [x] Audited Skill Research Batch 13 against the external datamined research corpus and independent references.
- [x] Promoted Batch 13 records with corroborated core facts: All Clear, Angry Hit, Burst Blitz.
- [x] Kept Angry Explosion and Angry Shout `partially_verified` because some current reward/damage details still lack independent reconciliation.
- [x] Audited Skill Research Batch 10 against independent references; core facts were reconfirmed while unresolved CaC/version-sensitive fields remained partial.
- [x] Added Batch 14 with Afterimage, Aura Slide, Big Bang Knuckle, Burning Attack, and Super Afterimage.
- [x] Promoted Batch 14 core records with corroborated identity/acquisition/mechanics: Aura Slide, Big Bang Knuckle, Burning Attack.
- [x] Kept Afterimage and Super Afterimage `partially_verified` where acquisition or technical interactions still need stronger reconciliation.
- [x] Added a new homepage research-standard section explaining exhaustive coverage, evidence states, cross-linking, and search-oriented organization.
- [x] Updated homepage CSS for the new research-standard panel with responsive cards.
- [x] Expanded `DLC-Overview.md` into an encyclopedia-level DLC index with paid-vs-free provenance, Future Saga coverage, a content audit matrix, verification policy, and downstream record requirements.
- [x] Added an Expert Missions system foundation covering unlock/count uncertainty, mechanics, reward taxonomy, cross-system links, verification rules, and an individual mission-record template.
- [x] Added a current 20-mission Expert Mission index with first-pass boss/reward mapping and explicit research states.
- [x] Added an Expert Mission status callout to the homepage and responsive styling for it.
- [x] Added the first 10 Super Soul records to the canonical machine-readable research layer.
- [x] Added Super Soul research batch 2, bringing the canonical catalogue to 18 populated records.
- [x] Cleaned internal citation artifacts from `docs/Super-Souls-Database.md` and expanded its research/schema guidance.
- [x] Updated the homepage to expose the 18-record Super Soul catalogue and added Super Souls to the main category navigation.
- [x] Added a Super Soul database status card to the homepage.
- [x] Added the QQ Bang research foundation covering synthesis, six-stat fields, recipe provenance, Super Mix Capsule Z, RNG handling, and verification rules.
- [x] Added the exhaustive Equipment Database research foundation covering individual gear records, slots, stats, acquisition taxonomy, DLC provenance, version history, and verification rules.
- [x] Exposed Equipment Database on the homepage status panel, popular destinations, and category navigation.
- [x] Added the first 10 structured Equipment records with stat, acquisition, restriction, provenance, and verification fields.
- [x] Cleaned internal citation artifacts from the new Equipment Database page before continuing.
- [x] Updated `CHANGELOG.md` to track the current expansion/verification/site work.
- [x] Hardened `scripts/check_repo_artifacts.py` to audit Git-tracked text files deterministically and recognize both content-reference and tool-result artifact patterns without self-triggering.
- [x] Expanded `.github/workflows/repo-quality.yml` pull-request path coverage to include every text format audited by the artifact checker, including TXT, BAT, XML, CSV, SCSS, TS, shell scripts, and the cleanup script/workflow itself.
- [x] Added Skill Research Batch 15 with five previously uncovered base-game skills: Dodoria Headbutt, Earth Splitting Galick Gun, Milky Cannon, Recoome Kick, and Time Control.
- [x] Duplicate-checked Batch 15 against the canonical skill catalog and prior skill research batches before addition; no duplicates were found.
- [x] Independently reconciled Batch 15 identity, category, acquisition, and core mechanics against current Xenoverse 2 references and corroborating sources; all five records are marked `verified` for their documented core fields.
- [x] Updated the skill-catalog build pipeline so curated repository research batches are imported into the canonical generated catalog instead of remaining disconnected research files.
- [x] Updated the Skills Sync workflow to run when curated skill research batches change, allowing Batch 15 to flow through canonical generation and validation automatically.
- [x] Added Skill Research Batch 16 with five additional early/base-game skills: Mach Punch, Fighting Pose E, Mystic Flash, Energy Shot, and Ginyu Force Special Combo.
- [x] Excluded Evil Flight Strike from Batch 16 because it was already present in the canonical indexed catalog.
- [x] Reconciled Batch 16 core identity, classification, acquisition, resource cost, and mechanics against multiple Xenoverse 2 references without inventing unsupported reward probabilities.
- [x] Re-verified Skill Research Batch 17 and added correction batch 35 for five proven acquisition/classification/mechanics errors: Heat Dome Attack/PQ40, Freedom Kick/PQ29, Rolling Bullet as Ki Blast Evasive/PQ42, Super Drain via Skill Shop after A Desperate Future, and Justice Pose/PQ53.
- [x] Added Skill Research Batch 19 with Charge, Stone Bullet, Double Buster, Finish Buster, and Justice Rush after a live duplicate check.
- [x] Preserved the pre-existing Skill Research Batch 18 instead of overwriting it when continuing the sequence.
- [x] Added **Skill Research Batch 36** covering the final DLC's new skills: Dragon Spiral, Indomitable, Venus Fist, and The Power to Overcome.
- [x] Verified the official Future Saga Chapter 4 scope and reconciled the new PQ skill acquisition routes against PQ185/PQ186 reward evidence.
- [x] Fixed the skill builder so correction batches can remove obsolete records when the correction changes the canonical uniqueness key.
- [x] Inspected and reran the Repository Quality artifact-check job after its failure; GitHub currently exposes no usable step logs, so the failure remains an unresolved workflow/infrastructure issue rather than a claimed validator failure.

## Current priority correction — 2026-09-18

The repository tracker is authoritative for continuation order. The current skill research frontier remains **Batch 316**. Batches 315–316 are now promoted into the canonical skill catalog after duplicate checks; the Parallel Quest audit is structurally complete through PQ186. The PQ audit now has an explicit unresolved cross-link report; PQ coverage is not considered fully reconciled until documented skill rewards resolve against canonical skill identities.

**Continuation order:**
1. **P0:** resolve or obtain observable evidence for the GitHub Actions pre-run failures; never weaken validators to make CI green.
2. **P1:** reconcile the existing final-DLC skill work (especially Batch 36) and the PQ-to-skill cross-link gap before adding another generic skill batch. The refreshed cross-link report identifies 120 unresolved PQ skill references against 117 unique canonical skill names; this is a data-reconciliation gap, not evidence that those skills do not exist.
3. **P1 coverage:** begin an exhaustive coverage audit of the currently thin wiki systems/pages. Record missing fields and missing records as TODO/data gaps instead of assuming the presence of a page means the system is complete.
4. **P2:** expand PQ, Awoken/Transformation, Expert Mission, Super Soul, Equipment, QQ Bang, character, story/Time Rift, shop/reward, and raid/event datasets with structured fields and provenance.
5. **P3:** expose the growing database through Pages navigation/search/explorer improvements only after data gaps are being tracked.

This correction is intentional: the project goal is an exhaustive encyclopedia, so raw skill-batch throughput must not crowd out major systems whose pages still lack exhaustive details.
- [ ] Maintain `docs/COVERAGE-AUDIT.md` as the active gap map; update it whenever a major system's record inventory or field-completeness state changes.

## In Progress

- [ ] **P0 — Clear remaining GitHub Actions validation failures.** Canonical skill verification statuses are now normalized to the schema (`partially_verified`), and cleanup now removes bare citation markers, but Repository Quality/Clean Internal Artifacts still fail on commit 2c20abe5. Skills Sync still needs a fresh run against the corrected research frontier.
- **Latest runner-level evidence (2026-09-18):** fresh push-triggered Skills Sync, Wiki Data Audit, Repository Quality, and Clean Internal Artifacts jobs all terminated within ~3–4 seconds with `steps: []`, `runner_id: 0`, and no exposed logs. This is consistent with failure before a runner step executed; the repository does not have enough connector evidence to attribute a specific GitHub-side cause.

- [ ] Continue skill research in batches only after the current P0/P1 verification work permits it; perform a duplicate search before every batch.
- [ ] Verify one completed batch alongside each new research batch instead of only adding new records.
- [ ] Reconcile unresolved Skill fields against multiple independent sources before promoting records to `verified`.
- [ ] Expand the 672 indexed skill target toward fully researched records; 672 is the catalog target, not a claim that 672 are verified.
- [ ] Deeply verify Batch 36's three Chapter 4 PQ skills and The Power to Overcome mechanics, including exact resource costs, reward-slot semantics, detailed effects, and version-sensitive behavior.
- [ ] Expand the Super Soul catalogue beyond the current 18 records; reconcile acquisition, triggers, effect magnitudes, durations, stacking, and Limit Burst behavior per soul.
- [ ] Promote Super Soul records only after core identity, acquisition, effects, and key mechanics are independently reconciled.
- [ ] Expand the Equipment Database from the initial records into the full individual clothing, equipment, accessory, shop, PQ, EM, raid, story, mentor, and DLC inventory.
- [ ] Build complete machine-readable equipment records with exact component slot, stat, acquisition, provenance, version, and verification fields.
- [ ] Expand QQ Bang research from system/recipe families into observed six-stat result records and reproducible recipe/result relationships.
- [ ] Expand the EM16–20 records into full mechanic/phase/reward tables and promote only when independently reconciled.
- [ ] Build individual EM01–15 records and reconcile the base-game vs later-content mission-count definitions.
- [x] Establish the structured Parallel Quest audit through PQ186, preserving known numbering gaps/conflicts instead of fabricating missing quests.
- [x] Promote/reconcile Batch 315 and Batch 316 Ki Blast Ultimate research into the canonical skill catalog after duplicate-key checks.
- [x] Promote the four Future Saga Chapter 4 skill records from Batch 36 into the canonical catalog and Awoken dataset.
- [x] Reconcile canonical matches from the PQ171-PQ186 frontier; 10 additional links are now resolved.
- [x] Add the four verified Future Saga Chapter 1 skill identities: Crimson Edge, Divine Spear, Big Bang Knuckle, and Wild Stinger.
- [x] Reconcile the researched PQ171-PQ180 skill identities currently supported by evidence.
- [ ] Reconcile the remaining PQ171-PQ186 skill names (not yet present in the canonical catalog) before expanding to earlier PQs.
- [ ] Reconcile the PQ-to-skill cross-link report (`docs/data/pq-skill-crosslink-report.json`): resolve the 175 currently unresolved reward references against canonical skill identities/research history, while preserving aliases and historical naming conflicts.
- [ ] Audit and expand Awoken/Transformation records as a first-class coverage track: separate CaC transformations from character-only forms, document resource costs, stages, race restrictions, unlock prerequisites, version history, and include The Power to Overcome where applicable.
- [ ] Improve mentor progression, training-stage rewards, and DLC mentor availability data.
- [ ] Expand Conton City and Time Rift records with complete NPC, service, progression, collectible, and access relationships.
- [ ] Continue removing internal/tool artifacts from repository text.
- [ ] Diagnose the cleanup/repository-quality artifact failure; `strip_internal_artifacts.py` now also removes bare `filecite`/`memcite` markers, but the workflows still fail and the connector exposes no usable logs.
- [ ] Recheck native GitHub Pages deployment status after repository changes; do not mark it successful until an actual successful run is observable.
- [ ] Run/strengthen data audits for duplicate names, invalid enums, missing sources, contradictory CaC/race metadata, and incomplete acquisition fields.
- [ ] Continue improving the GitHub Pages website: navigation, search/explorer UI, responsive layout, data cards, typography, accessibility, empty/error states, and visual consistency.
- [ ] Keep the exhaustive-coverage standard active across every content area. After P0 is cleared or while it remains externally blocked, prioritize coverage audits of underdeveloped systems/pages (PQs, Awoken/Transformations, Expert Missions, Super Souls, Equipment, QQ Bangs, story/Time Rifts, characters, shops/rewards, raids/events) rather than generating skill batches indefinitely.

## Productivity / Delivery Strategy

The project is being worked as parallel tracks so the site visibly improves while the research database grows:

1. **Research:** add the next non-duplicate skill/content batch.
2. **Verification:** re-verify one earlier batch and reconcile conflicting/unresolved fields.
3. **Website:** make at least one concrete Pages/UI improvement each cycle; prioritize improvements that expose the growing database rather than cosmetic churn.
4. **Data quality:** run or inspect validation and fix actionable failures.
5. **Cleanup:** continue removing internal/tool artifacts and keeping generated/public-facing content clean.
6. **Coverage:** continuously expand into the next under-documented game system instead of allowing one content category to become the whole project.
7. **Project tracking:** update this TODO and `CHANGELOG.md` in the same cycle.
8. **Deployment:** inspect GitHub Pages/Actions results and record blockers honestly.

## Verification Rules

- `indexed` = discovered/catalogued, not researched.
- `partially_verified` = some important facts have been checked, but one or more meaningful fields remain unresolved or source-dependent.
- `verified` = core identity/acquisition/mechanics have been reconciled against sufficient independent evidence; it does not mean every community damage measurement is exact.
- Never invent drop percentages, costs, unlock conditions, or character/CaC restrictions.
- Preserve source conflicts and uncertainty in the data rather than silently choosing a convenient value.
- Exhaustiveness means recording known details and known unknowns, not manufacturing certainty.

## Next Working Cycle

1. **P0:** verify the corrected Batch 314 against the repository duplicate/semantic validators and inspect the next Skills Sync/Data Audit workflow result.
2. **P1:** if validation is clean, synchronize accumulated research batches into the canonical skills.json/skills-index.json layer and verify the generated catalog rather than assuming sync occurred.
3. Re-verify one previously researched batch while continuing the next non-duplicate Ki Blast Ultimate coverage batch.
4. Continue resolving high-value unresolved skill fields with independent Xenoverse 2 sources; do not promote uncertain UF, cost, drop-rate, or acquisition fields.
5. Reconcile Batch 36 final-DLC skills and The Power to Overcome mechanics.
6. Deepen EM16–20 with exact phase/mechanic/reward tables where evidence supports them.
7. Continue EM01–15 individual records and reconcile the strongest independently documented missions first.
8. Populate the next Super Soul batch and resolve its acquisition/effect provenance.
9. Expand the individual Equipment population from the first 10 records into complete clothing and accessory coverage.
10. Expand QQ Bang observed-result research alongside the equipment records.
11. Update this TODO tracker and CHANGELOG.md as priorities change.
12. Inspect GitHub Pages deployment and repository-quality/data-audit results; record failures honestly.

## PQ Cross-Link Validation Snapshot — 2026-09-18

- 18 PQ research batches cover the numbered audit through PQ186, with PQ36 and the PQ141–150 numbering gap explicitly preserved as evidence conflicts/gaps.
- Cross-link audit found 212 unique PQ skill-reward references: 36 resolve to the current 108-name canonical skill catalog (including one documented alias), while 175 remain unresolved.
- The unresolved links are now persisted in `docs/data/pq-skill-crosslink-report.json` so reconciliation is trackable and does not get lost in transient command output.

## Current Validation Result

- Pages build/deployment for commit 05b3bbd succeeded.
- Skills Sync, Wiki Data Audit, Repository Quality, and Clean Internal Artifacts failed on the same commit; each was rerun once and remained failed.
- No usable step logs or failure annotations are exposed through the available GitHub connector, so the failure cause is not being guessed or mislabeled.

## Legacy Next-Cycle Notes


1. Re-verify Batch 36, starting with PQ185/PQ186 reward-slot semantics and the exact mechanics of Dragon Spiral, Indomitable, and Venus Fist.
2. Verify The Power to Overcome's exact activation/Overdrive behavior against independent technical research while retaining conflicting measurements as provenance rather than averaging them.
3. Select the next non-duplicate skill/content batch only after the final-DLC additions have been reconciled.
4. Make at least one tangible website/UI improvement that exposes the expanded final-DLC skill coverage.
5. Deepen EM16–20 with exact phase/mechanic/reward tables where evidence supports them.
6. Continue EM01–15 individual records and reconcile the strongest independently documented missions first.
7. Populate the next Super Soul batch and resolve its acquisition/effect provenance.
8. Expand the individual Equipment population from the first 10 records into complete clothing and accessory coverage.
9. Expand QQ Bang observed-result research alongside the equipment records.
10. Update this TODO tracker and `CHANGELOG.md`.
11. Run or inspect available validation/Actions results.
12. Only then report completed work, actual results, coverage gaps, and unresolved blockers.

## Verification Rules

- `indexed` = discovered/catalogued, not researched.
- `partially_verified` = some important facts have been checked, but one or more meaningful fields remain unresolved or source-dependent.
- `verified` = core identity/acquisition/mechanics have been reconciled against sufficient independent evidence; it does not mean every community damage measurement is exact.
- Never invent drop percentages, costs, unlock conditions, or character/CaC restrictions.
- Preserve source conflicts and uncertainty in the data rather than silently choosing a convenient value.
- Exhaustiveness means recording known details and known unknowns, not manufacturing certainty.
