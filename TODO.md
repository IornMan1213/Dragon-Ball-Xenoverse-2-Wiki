# Dragon Ball Xenoverse 2 Wiki — Project TODO

This file is the working project tracker. Statuses describe repository work, not guesses about game facts.

## Scope Standard — Exhaustive Game Encyclopedia

- [ ] Treat the wiki as an exhaustive, excessive reference for **every documented detail of Dragon Ball Xenoverse 2**, not merely a guide to the most popular content.
- [ ] Cover the full game surface area: story/Extra Missions, Parallel Quests, Expert Missions, Time Patrol/Conton City systems, mentors and training, skills, Awoken/Transformations, playable and non-playable characters, CaC/race restrictions, Super Souls, equipment/costumes/accessories, items, currencies, shops, drops/rewards, Dragon Balls/wishes, raids/events, modes, stages, maps/areas, mechanics, combat properties, progression, DLC/free updates, and other discoverable systems.
- [ ] For every record, prefer structured, consistently labeled fields over prose-only descriptions so the information can be searched, compared, validated, and reused by the website and machine-readable datasets.
- [ ] Preserve fine-grained distinctions that are easy to lose: CaC vs character-only availability, race/gender restrictions, DLC ownership vs in-game unlock conditions, normal clear vs Ultimate Finish rewards, first-clear vs repeat rewards, shop rotations, prerequisite progression, costs, resource consumption, damage type, hit behavior, status effects, defensive properties, combo interactions, PvE/PvP behavior, and known exceptions.
- [ ] Keep factual certainty explicit. Do not fill missing details merely to make a record look complete; use `indexed`, `partially_verified`, and `verified` appropriately and preserve source conflicts/unknowns.
- [ ] Use multiple sources where practical, distinguish datamined/researched values from community observations, and record provenance so later verification can replace provisional values without losing research history.
- [ ] Organize the information so exhaustive coverage remains readable: canonical data first, detailed notes second, source/provenance metadata alongside the relevant record, and dedicated indexes/explorers for navigation.
- [ ] Do not let website polish, automation, or batch throughput become a reason to omit game details. Site improvements must expose and organize the expanding database rather than substitute for research.

## Done

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
- [x] Added the first individual Expert Mission research layer for EM16–20, including structured identity, rewards, mechanics, strategy evidence, unknowns, and verification status.
- [x] Linked the EM16–20 individual records from the Expert Mission system index.
- [x] Added the first 10 Super Soul records to the canonical machine-readable research layer.
- [x] Added Super Soul research batch 2, bringing the canonical catalogue to 18 populated records.
- [x] Cleaned internal citation artifacts from `docs/Super-Souls-Database.md` and expanded its research/schema guidance.
- [x] Updated the homepage to expose the 18-record Super Soul catalogue and added Super Souls to the main category navigation.
- [x] Added a Super Soul database status card to the homepage.
- [x] Added the QQ Bang research foundation covering synthesis, six-stat fields, recipe provenance, Super Mix Capsule Z, RNG handling, and verification rules.
- [x] Added the exhaustive Equipment Database research foundation covering individual gear records, slots, stats, acquisition taxonomy, DLC provenance, version history, and verification rules.
- [x] Exposed Equipment Database on the homepage status panel, popular destinations, and category navigation.
- [x] Added the first 10 structured Equipment records with stat, acquisition, restriction, provenance, and verification fields.
- [x] Cleaned internal web-citation artifacts from the new Equipment Database page before continuing.
- [x] Updated `CHANGELOG.md` to track the current expansion/verification/site work.

## In Progress

- [ ] Continue skill research in batches, with a duplicate search before every batch.
- [ ] Verify one completed batch alongside each new research batch instead of only adding new records.
- [ ] Reconcile unresolved Skill fields against multiple independent sources before promoting records to `verified`.
- [ ] Expand the 672 indexed skill target toward fully researched records; 672 is the catalog target, not a claim that 672 are verified.
- [ ] Expand the Super Soul catalogue beyond the current 18 records; reconcile acquisition, triggers, effect magnitudes, durations, stacking, and Limit Burst behavior per soul.
- [ ] Promote Super Soul records only after core identity, acquisition, effects, and key mechanics are independently reconciled.
- [ ] Expand the Equipment Database from the initial 10 records into the full individual clothing, equipment, accessory, shop, PQ, EM, raid, story, mentor, and DLC inventory.
- [ ] Build complete machine-readable equipment records with exact component slot, stat, acquisition, provenance, version, and verification fields.
- [ ] Expand QQ Bang research from system/recipe families into observed six-stat result records and reproducible recipe/result relationships.
- [ ] Expand the EM16–20 records into full mechanic/phase/reward tables and promote only when independently reconciled.
- [ ] Build individual EM01–15 records and reconcile the base-game vs later-content mission-count definitions.
- [ ] Improve PQ verification, especially acquisition conditions, Ultimate Finish requirements, and reward provenance.
- [ ] Reconcile Awoken/Transformation records, separating CaC transformations from character-only forms.
- [ ] Improve mentor progression, training-stage rewards, and DLC mentor availability data.
- [ ] Expand Conton City and Time Rift records with complete NPC, service, progression, collectible, and access relationships.
- [ ] Continue removing internal/tool artifacts from repository text.
- [ ] Diagnose the cleanup workflow failure; the connector currently exposes failed jobs without usable step logs, so the failure cause is not yet established.
- [ ] Recheck native GitHub Pages deployment status after repository changes; do not mark it successful until an actual successful run is observable.
- [ ] Run/strengthen data audits for duplicate names, invalid enums, missing sources, contradictory CaC/race metadata, and incomplete acquisition fields.
- [ ] Continue improving the GitHub Pages website: navigation, search/explorer UI, responsive layout, data cards, typography, accessibility, empty/error states, and visual consistency.
- [ ] Keep the exhaustive-coverage standard active across every content area; do not narrow the project to skills/PQs merely because those are the current research batches.

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

1. Select the next non-duplicate skill/content batch.
2. Research and add the batch with exhaustive field coverage appropriate to that content type.
3. Re-verify one earlier batch, including source reconciliation and corrections.
4. Make at least one tangible website/UI improvement.
5. Deepen EM16–20 with exact phase/mechanic/reward tables where evidence supports them.
6. Continue EM01–15 individual records and reconcile the strongest independently documented missions first.
7. Populate the next Super Soul batch and resolve its acquisition/effect provenance.
8. Expand the individual Equipment population from the first 10 records into complete clothing and accessory coverage.
9. Expand QQ Bang observed-result research alongside the equipment records.
10. Update this TODO tracker and `CHANGELOG.md`.
11. Run or inspect available validation/Actions results.
12. Only then report completed work, actual results, coverage gaps, and unresolved blockers.
