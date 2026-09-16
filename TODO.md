# Dragon Ball Xenoverse 2 Wiki — Project TODO

This file is the working project tracker. Statuses describe repository work, not guesses about game facts.

## Done

- [x] Removed duplicate custom GitHub Pages workflows that could compete with native Pages deployment.
- [x] Removed the duplicate `docs/index.html` Pages entry point.
- [x] Added/expanded the homepage database status and progress indicators.
- [x] Added the internal-artifact cleanup script and cleanup workflow.
- [x] Reworked the skills-sync workflow to use the external research corpus, validation, and PR-based synchronization.
- [x] Established the canonical skills schema and verification states: `indexed`, `partially_verified`, `verified`.
- [x] Added skill research batches 01–13.
- [x] Completed duplicate checks before the recent skill batches.
- [x] Audited Skill Research Batch 13 against the external datamined corpus and independent references.
- [x] Promoted Batch 13 records with corroborated core facts: All Clear, Angry Hit, Burst Blitz.
- [x] Kept Angry Explosion and Angry Shout `partially_verified` because some current reward/damage details still lack independent reconciliation.
- [x] Updated Batch 13 provenance and verification notes in `docs/data/skill-research-batches/skill-batch-13.json`.
- [x] Updated `CHANGELOG.md` to track the current expansion/verification work.

## In Progress

- [ ] Continue skill research in batches, with a duplicate search before every batch.
- [ ] Verify one completed batch alongside each new research batch instead of only adding new records.
- [ ] Reconcile unresolved Skill fields against multiple independent sources before promoting records to `verified`.
- [ ] Expand the 672 indexed skill target toward fully researched records; 672 is the catalog target, not a claim that 672 are verified.
- [ ] Improve PQ verification, especially acquisition conditions, Ultimate Finish requirements, and reward provenance.
- [ ] Reconcile Awoken/Transformation records, separating CaC transformations from character-only forms.
- [ ] Improve mentor progression, training-stage rewards, and DLC mentor availability data.
- [ ] Continue removing internal/tool artifacts from repository text.
- [ ] Diagnose the cleanup workflow failure; the connector currently exposes failed jobs without usable step logs, so the failure cause is not yet established.
- [ ] Recheck native GitHub Pages deployment status after repository changes; do not mark it successful until an actual successful run is observable.
- [ ] Run/strengthen data audits for duplicate names, invalid enums, missing sources, contradictory CaC/race metadata, and incomplete acquisition fields.
- [ ] Beautify and improve the GitHub Pages website continuously, not as a deferred final phase: homepage, navigation, search/explorer UI, responsive layout, data cards, typography, accessibility, empty/error states, and visual consistency.
- [ ] Each working cycle must include at least one concrete website improvement when it can be safely made without disrupting data integrity.

## Productivity / Delivery Strategy

The project is being worked as parallel tracks so the site visibly improves while the research database grows:

1. **Research:** add the next non-duplicate skill batch.
2. **Verification:** re-verify one earlier batch and reconcile conflicting/unresolved fields.
3. **Website:** make at least one concrete Pages/UI improvement each cycle; prioritize improvements that expose the growing database rather than cosmetic churn.
4. **Data quality:** run or inspect validation and fix actionable failures.
5. **Cleanup:** continue removing internal/tool artifacts and keeping generated/public-facing content clean.
6. **Project tracking:** update this TODO and `CHANGELOG.md` in the same cycle.
7. **Deployment:** inspect GitHub Pages/Actions results and record blockers honestly.

## Verification Rules

- `indexed` = discovered/catalogued, not researched.
- `partially_verified` = some important facts have been checked, but one or more meaningful fields remain unresolved or source-dependent.
- `verified` = core identity/acquisition/mechanics have been reconciled against sufficient independent evidence; it does not mean every community damage measurement is exact.
- Never invent drop percentages, costs, unlock conditions, or character/CaC restrictions.
- Preserve source conflicts and uncertainty in the data rather than silently choosing a convenient value.

## Next Working Cycle

1. Select the next non-duplicate skill batch.
2. Research and add the batch.
3. Re-verify one earlier batch, including source reconciliation and corrections.
4. Make at least one tangible website/UI improvement.
5. Update this TODO tracker with completed and remaining work.
6. Update `CHANGELOG.md` with the concrete repository/data/site changes.
7. Run or inspect available validation/Actions results.
8. Only then report the completed work, actual results, and unresolved blockers.
