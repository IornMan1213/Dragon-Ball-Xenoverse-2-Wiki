### 2026-09-27 continuation — PQ equipment endpoint promotion
- [x] Promoted 11 explicit named accessory identities into `equipment-accessories-record-layer.json`: Four-Star Dragon Ball Hat, Chiaotzu's Hat (With Collar), Dore's Scouter, Jaco's State-of-the-Art Radio, Tagoma's Scouter, SSGSS Goku Wig, Yamcha Baseball Hat, SSGSS Vegeta Wig, Bulma (Kid) Wig, Android 14's Hat, and Bardock (DB Super)'s Scouter.
- [x] Linked all 11 through `accessory-pq-canonical-bridge.json`.
- [x] Recomputed the PQ equipment projection against the live endpoint layers: 123 unique canonical targets, 51 exact endpoint matches, 72 remaining identity gaps.
- [x] Refreshed the endpoint coverage audit and bridge summary.
- [x] Preserved unresolved route/condition semantics; no reward probability was inferred.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] **Exact next:** continue evidence-backed promotion of the remaining 72 endpoint gaps, prioritizing explicit inventory identities and preserving ambiguous set/component records.

### 2026-09-27 continuation — Research/Super Soul validator hardening
- [x] Research-batch validation now rejects malformed roots and non-list `corrections`/`records` containers instead of silently skipping them.
- [x] Super Soul record validation now catches only expected OSError/JSON decode failures.
- [x] Added `docs/data/research-super-soul-validator-hardening-audit-2026-09-27.json`.
- [x] No canonical data changed.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] **Exact next:** finish the remaining validator integrity sweep and begin substantive endpoint/cross-domain enrichment where integrity is already sufficient.

### 2026-09-27 continuation — Super Soul/equipment audit hardening
- [x] Hardened `audit_super_soul_mechanics_coverage.py` for JSON/root/record integrity.
- [x] Hardened `audit_pq_equipment_endpoint_coverage.py` for relationship and endpoint-container integrity and non-coercive identities.
- [x] Added `docs/data/super-soul-pq-equipment-audit-hardening-2026-09-27.json`.
- [x] No canonical data changed.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] **Exact next:** continue the integrity sweep, then move into larger substantive cross-domain enrichment gaps.

### 2026-09-27 continuation — Partner/Awoken tooling hardening
- [x] Hardened `validate_partner_skill_relationships.py` for malformed JSON and malformed evidence without uninitialized-variable failures.
- [x] Hardened `normalize_awoken_transformation_category.py` input/root/container validation before canonical mutation.
- [x] Added `docs/data/partner-awoken-normalization-hardening-audit-2026-09-27.json`.
- [x] No canonical data changed.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] **Exact next:** continue the validator/audit sweep and then target substantive cross-domain coverage gaps rather than cosmetic work.

### 2026-09-27 continuation — Super Soul audit and PQ reverse-validator hardening
- [x] Repaired `scripts/audit_super_soul_consumer_coverage.py`, including malformed source containing a literal escaped newline that joined statements.
- [x] Removed assertion-dependent control flow from `scripts/validate_skill_pq_crosslinks.py`; validation now fails deterministically under `python -O` as well.
- [x] Preserved canonical source-of-truth policy; no canonical records were changed.
- [x] Runtime/CI remains intentionally non-blocking.
- [ ] **Exact next:** inspect remaining audit/validator scripts for assertion use, unsafe coercion, and malformed-container handling, then consolidate any related hardening into auditable commits.

### 2026-09-27 continuation — General wiki audit hardening
- [x] Hardened `scripts/audit_wiki_data.py` against unreadable/malformed JSON and type-coercive identity handling.
- [x] Added explicit non-empty string validation for IDs/names and provenance source entries.
- [x] Added explicit verification-status type validation.
- [x] Added `docs/data/general-wiki-audit-hardening-2026-09-27.json`.
- [x] No canonical data changed.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] **Exact next:** continue inspecting remaining research/audit tooling for substantive integrity gaps.

### 2026-09-27 continuation — Awoken/skill builder integrity hardening
- [x] Hardened `apply_awoken_overrides.py` against malformed JSON, wrong root/container types, and malformed Awoken identity fields.
- [x] Removed Awoken identity coercion during override matching.
- [x] Hardened `build_skills_from_research.py` existing-record identity loading so malformed identity fields are not silently normalized.
- [x] Added `docs/data/awoken-skill-builder-integrity-audit-2026-09-27.json`.
- [x] No canonical data was intentionally changed.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] **Exact next:** continue auditing remaining builders/auditors for concrete schema, identity, provenance, and cross-domain integrity gaps.

### 2026-09-27 continuation — Skills/PQ reconciliation validator hardening
- [x] Hardened `scripts/validate_skills.py` against malformed JSON, wrong root/container types, and malformed canonical identity fields.
- [x] Removed identity coercion in the canonical skill-key projection.
- [x] Hardened `scripts/reconcile_pq_forward_reverse.py` against malformed JSON and invalid PQ identifiers before numeric projection.
- [x] Added `docs/data/skills-and-pq-reconciliation-validator-audit-2026-09-27.json`.
- [x] No canonical data changed.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] **Exact next:** continue auditing remaining consumers/builders for concrete schema and provenance integrity gaps.

### 2026-09-27 continuation — PQ validator hardening
- [x] Hardened `validate_pq_equipment_crosslinks.py`: enforce canonical `pq-001`–`pq-186` identifiers, reject unsupported relationship statuses, and reject whitespace-only sources.
- [x] Hardened `validate_pq_cross_domain_index.py`: forward index must resolve inside `docs/data/`.
- [x] Added `docs/data/pq-validator-hardening-audit-2026-09-27.json`.
- [x] No canonical relationship/data records changed.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] **Exact next:** continue validator/consumer integrity audit, prioritizing substantive schema and cross-domain consistency gaps.

### 2026-09-27 continuation — Skill→PQ crosslink validator hardening
- [x] Hardened `scripts/validate_skill_pq_crosslinks.py` against malformed canonical skills JSON and malformed checked-in reverse-index JSON.
- [x] Replaced the validator's core canonical-schema `assert` checks with explicit failures so optimization cannot disable them.
- [x] Preserved deterministic 474-skill / 246-edge / 170-PQ expectations.
- [x] No canonical skill or relationship data changed.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] **Exact next:** continue auditing validators/consumers for substantive schema, identity, provenance, and cross-link integrity gaps.

### 2026-09-27 continuation — Super Soul/Awoken validator hardening
- [x] Hardened `scripts/validate_super_soul_record_layer.py`: every provenance source entry must be a non-empty string.
- [x] Hardened `scripts/validate_awoken_model.py`: deterministic malformed-JSON handling for skills, overrides, and canonical transformation roster sources.
- [x] No canonical data changed.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] **Exact next:** inspect another validator/consumer for substantive schema, identity, provenance, or cross-link integrity gaps.

### 2026-09-27 continuation — PQ index validator hardening
- [x] Hardened `scripts/validate_pq_skill_links.py`: deterministic JSON errors; strict reverse-index root/entry/skill-list validation; explicit canonical relationship-list validation.
- [x] Hardened `scripts/validate_pq_cross_domain_index.py`: deterministic malformed-JSON failure handling.
- [x] No canonical PQ relationship data changed.
- [ ] Runtime/CI execution remains intentionally non-blocking.
- [ ] **Exact next:** inspect the next deterministic validator/consumer for a concrete integrity gap; prioritize substantive schema/identity checks over cosmetic work.

### 2026-09-27 continuation — Presentation/Awoken validator hardening
- [x] Hardened `scripts/validate_character_presentation_consumers.py`: explicit malformed-JSON/root checks and replaced bare `assert` validation with deterministic failures.
- [x] Hardened `scripts/validate_awoken_integrity.py`: explicit malformed-JSON handling and source-root object checks.
- [x] No canonical data changed.
- [ ] Runtime/CI execution remains intentionally non-blocking.
- [ ] **Exact next:** inspect another deterministic validator/consumer for a concrete integrity gap and continue evidence-backed coverage work.

### 2026-09-27 continuation — Research-batch validator hardening
- [x] Inspected `scripts/validate_research_batches.py`.
- [x] Found a concrete type-integrity gap: Python `bool` values could pass the PQ-number `int` test.
- [x] Hardened PQ-number validation to reject booleans explicitly.
- [x] Found coercive `str(...)` construction of skill identity keys; malformed class/subcategory values could be silently normalized into canonical-key comparisons.
- [x] Require skill identity fields `name`, `class`, and `subcategory` to be strings before constructing research-batch keys.
- [x] No canonical research data changed.
- [ ] Runtime validator execution/CI/build remains intentionally unverified.
- [ ] **Exact next:** inspect the next deterministic validator/consumer for a concrete integrity gap.

### 2026-09-27 continuation — Super Soul record-layer validator hardening
- [x] Inspected `scripts/validate_super_soul_record_layer.py`.
- [x] Found a concrete schema-integrity gap: malformed JSON roots and non-object relationship/record containers could reach downstream projections without explicit type validation.
- [x] Added deterministic JSON/root validation for both the Super Soul endpoint layer and canonical PQ relationship store.
- [x] Require `verified_relationships` to be a list and Super Soul records to be objects before field access.
- [x] Prevent malformed non-string relationship targets from becoming endpoint identities.
- [x] No canonical Super Soul or PQ relationship data changed.
- [ ] Runtime validator execution/CI/build remains intentionally unverified.
- [ ] **Exact next:** inspect the next deterministic validator/consumer for a concrete integrity gap.

### 2026-09-27 continuation — Skill acquisition validator hardening
- [x] Inspected `scripts/validate_skill_acquisition_metadata.py`.
- [x] Found a concrete validator-integrity flaw: all substantive checks used Python `assert`, which can be disabled with `python -O`, potentially turning invalid data into a false PASS.
- [x] Replaced bare assertions with explicit deterministic failures.
- [x] Added explicit malformed-JSON handling and per-record required-field/type checks.
- [x] Preserved strict rejection of boolean PQ IDs and the existing acquisition consistency rules.
- [x] No canonical skill data changed.
- [ ] Runtime validator execution/CI/build remains intentionally unverified.
- [ ] **Exact next:** inspect the next deterministic validator/consumer for a concrete integrity gap.

### 2026-09-27 continuation — Partner Customization integer identity hardening
- [x] Inspected the live `scripts/validate_partner_customization_character_navigation.py`.
- [x] Found a concrete Python type-integrity gap: `bool` is a subclass of `int`, so boolean values could satisfy positive-integer checks for Partner Customization key numbers.
- [x] Hardened key-number and reconciliation-key validation, including malformed-field reporting, to explicitly reject booleans.
- [x] No canonical Partner Customization or character data changed.
- [ ] Runtime validator execution/CI/build remains intentionally unverified.
- [ ] **Exact next:** inspect the next deterministic validator/consumer for a concrete integrity gap.

### 2026-09-27 continuation — Awoken integrity identity validation hardening
- [x] Inspected the live `scripts/validate_awoken_integrity.py`.
- [x] Found a concrete identity-integrity gap: canonical and override keys used `str(...)` coercion, and canonical records were projected directly into a dictionary, allowing malformed identity fields to be silently normalized or duplicate identities to overwrite earlier records.
- [x] Replaced coercive identity construction with explicit non-empty string validation for `name`, `class`, and `subcategory`.
- [x] Added deterministic duplicate canonical-identity rejection before override matching.
- [x] Required both canonical and override record containers to be lists.
- [x] No canonical Awoken data changed.
- [ ] Runtime validator execution/CI/build remains intentionally unverified.
- [ ] **Exact next:** inspect the next deterministic validator/consumer for a concrete integrity gap.

### 2026-09-27 continuation — PQ→skill link validator validation-order hardening
- [x] Inspected the live `scripts/validate_pq_skill_links.py`.
- [x] Found a concrete robustness gap: malformed relationship identifiers were used in duplicate-set construction and PQ integer parsing before type/format/range validation, allowing malformed values to trigger uncontrolled exceptions.
- [x] Hardened each canonical PQ-skill row to require an object, a `pq-001`–`pq-186` identifier, and a non-empty string skill target before duplicate detection or numeric projection.
- [x] No canonical PQ-skill relationship data was changed.
- [ ] Runtime validator execution/CI/build remains intentionally unverified.
- [ ] **Exact next:** inspect the next deterministic validator/consumer for another concrete integrity gap; then resume evidence-backed enrichment.

### 2026-09-27 continuation — PQ reward validator root/count schema hardening
- [x] Inspected the live `scripts/validate_pq_reward_relationships.py`.
- [x] Found a concrete schema-integrity gap: the validator consumed the top-level documents and `current_counts` without first requiring object roots and an exact six-key, non-negative-integer count contract.
- [x] Hardened the validator to require object roots for both the relationship store and schema, require exactly `skill`, `super_soul`, `equipment`, `character`, `dlc`, and `farming` count keys, and reject boolean/negative/non-integer count values.
- [x] No canonical PQ relationship data was changed.
- [ ] Runtime validator execution/CI/build remains intentionally unverified.
- [ ] **Exact next:** inspect the next deterministic validator/consumer for a concrete integrity gap; preserve the evidence boundary and avoid speculative relationship reconstruction.

### 2026-09-27 continuation — Canonical recovery count validation hardening
- [x] Inspected the live `scripts/validate_canonical_database_recovery.py`.
- [x] Found a concrete recovery-integrity gap: it previously verified only that `current_counts` had the six expected keys, without recomputing those counts from `verified_relationships`.
- [x] Hardened the validator to parse every stored relationship row, reject unknown relationship types, recompute all six counts, require exact equality with the declared counts, and require the recovered baseline to total **840** relationships.
- [x] Added `docs/data/canonical-database-recovery-validator-audit-2026-09-27.json`; no canonical relationship data changed.
- [ ] Runtime validator execution/CI/build remains intentionally unverified.
- [ ] **Exact next:** inspect the next deterministic validator/consumer for a concrete integrity gap, then return to evidence-backed database enrichment once the validation surface is hardened.

### 2026-09-27 continuation — Awoken model validator identity hardening
- [x] Inspected the live `scripts/validate_awoken_model.py` after the PQ equipment coverage validator hardening.
- [x] Found a concrete integrity gap: the validator used `str(...)` identity coercion and a dict projection that could silently collapse malformed/duplicate canonical skill keys instead of deterministically rejecting them.
- [x] Hardened the validator to require expected JSON root/container types, non-empty string identity fields, explicit duplicate-key rejection, valid roster names, and non-boolean integer Ki costs.
- [x] Added `docs/data/awoken-model-validator-audit-2026-09-27.json`; no canonical Awoken data changed.
- [ ] Runtime validator execution/CI/build remains intentionally unverified.
- [ ] **Exact next:** inspect the next live deterministic validator/consumer for a concrete integrity gap; continue evidence-backed database enrichment only where canonical source evidence is explicit.

### 2026-09-27 continuation — PQ equipment endpoint coverage validator hardening
- [x] Fresh live census confirmed the canonical skill mechanics frontier is already **474/474**, so no artificial Batch 496 was opened.
- [x] Inspected the live `scripts/validate_pq_equipment_endpoint_coverage.py`.
- [x] Found a concrete schema/type-integrity gap: the validator coerced relationship targets and endpoint names with `str(...)`, allowing malformed non-string JSON values to become apparently valid identities.
- [x] Hardened the validator to require object roots, list-valued `records`, object records, non-empty string relationship targets, and non-empty string endpoint names before normalization/set operations.
- [x] Updated `docs/data/pq-equipment-endpoint-coverage-audit-2026-09-27.json` to record the hardening contract; canonical equipment data remains unchanged.
- [ ] Runtime validator execution/CI/build remains intentionally unverified.
- [ ] **Exact next:** inspect the next live deterministic validator/consumer for another concrete integrity gap; continue evidence-backed database enrichment only where canonical source evidence is explicit.

### 2026-09-27 continuation — PQ equipment endpoint recovery-forward batch
- [x] Freshly re-censused the remaining PQ equipment endpoint gaps after database recovery; did not reuse an older candidate list as authoritative.
- [x] Promoted four explicit canonical accessory identities from existing repository evidence: **Gamma 1's Helmet (PQ156), Golden Frieza Head (PQ182), Dragon Ball Balloon (PQ184), and Goku (Ultra Supervillain Quelled) Wig (PQ185)**.
- [x] Preserved evidence boundaries: Gamma 1's Helmet remains partially verified; Golden Frieza Head and the Goku (Ultra Supervillain Quelled) Wig remain indexed where exact reward-slot mechanics are unresolved; Dragon Ball Balloon retains the separate 50% Ultimate-Finish evidence without collapsing it into a guaranteed basic reward.
- [x] Refreshed the canonical accessory endpoint layer plus PQ equipment projection, integrity audit, and endpoint-coverage audit.
- [x] Current PQ equipment projection remains **125 canonical edges / 123 unique targets**; endpoint records increased from **108 to 112**, exact identity matches from **42 to 46**, and explicit identity gaps decreased from **81 to 77**.
- [ ] Runtime validator execution/CI/build remains intentionally unverified.
- [ ] **Exact next:** fresh live census before Batch 496; continue evidence-backed endpoint promotion where identity is explicit, then resume highest-value unaudited canonical skill/data enrichment.

### 2026-09-27 continuation — Canonical PQ reward database recovery verification
- [x] Reconciled the apparent missing-forward-layer report against the live main tree rather than recreating data from partial reverse indexes.
- [x] Confirmed docs/data/pq-reward-relationships.json is present on current main through GitHub's live code-search index; the large-file content endpoint is connector-limited, not evidence of file absence.
- [x] Confirmed the live indexed forward layer retains the established **840-edge** baseline: **236 skills / 137 Super Souls / 125 equipment / 247 character / 88 DLC / 7 farming**.
- [x] Recorded recovery source commit 02b6306341c2d3a6cf6f6213a25386949d07a7ce and recovery audit docs/data/pq-reward-database-recovery-audit-2026-09-27.json.
- [x] Corrected the stale PQ cross-domain forward-source audit so the live forward file is no longer incorrectly treated as absent.
- [x] No replacement reward relationships were fabricated and no canonical forward data was overwritten.
- [ ] Runtime validator execution/CI/build remains intentionally unverified.
- [ ] **Exact next:** continue from the restored 840-edge canonical PQ relationship baseline; fresh-audit the remaining equipment endpoint-enrichment frontier and then resume Batch 496 skill/data enrichment.

### 2026-09-27 continuation — Runtime/CI intentionally non-blocking; Batch 495 data enrichment
- [x] User-directed policy for this continuation: treat runtime execution/CI as non-blocking for the time being and continue substantive data/research work instead of waiting on runtime infrastructure.
- [x] Fresh live mechanics frontier was re-censused after Batch 494; no stale candidate list was reused.
- [x] Enriched 8 previously unaudited canonical skill records: Burst Charge, Super Gamma Blast, Justice Kick, Sauzer Blade, Lightning Impact, Instant Rise, Jumping Energy Wave, and Power Impact.
- [x] Added eight current-evidence audit records plus Batch 495 and its thin-frontier audit; registered all artifacts in docs/data/pq-cross-domain-index.json.
- [x] Preserved acquisition conflicts and source-bound numerical evidence rather than inventing reward probabilities, frames, or hidden mechanics.
- [x] No missing general PQ reward dataset was fabricated; docs/data/pq-reward-relationships.json remains an evidence boundary.
- [x] Runtime/CI note: runtime validator execution, GitHub Actions, and build execution are intentionally not gating this data-research cycle. Continue substantive repository data work while those systems are unavailable; mark runtime status unverified rather than treating it as a blocker.
- [ ] Exact next: fresh live census before Batch 496 and continue enriching the highest-value remaining unaudited canonical skill/data records; do not reuse the Batch 495 candidate list.

### 2026-09-27 continuation — Partner skill relationship identity validation-order hardening
- [x] Inspected the live `scripts/validate_partner_skill_relationships.py`.
- [x] Found a concrete robustness gap: malformed/unhashable canonical skill IDs or partner names could reach `Counter`/set construction, and malformed relationship-row identifiers could reach set membership/duplicate-key tracking before type validation, causing uncontrolled `TypeError` failures.
- [x] Reordered canonical identity projections to use only explicitly valid non-empty strings before hash/set operations.
- [x] Hardened relationship-row validation so skill and partner identifiers are type/emptiness checked before canonical-set membership and duplicate tracking.
- [x] Updated `docs/data/partner-skill-relationship-validator-audit-2026-09-26.json`.
- [x] No canonical Partner Customization relationship, skill, character, or acquisition data changed.
- [ ] Runtime validator execution and CI/build remain unverified.
- [x] Preserved the evidence boundary around inferred Partner Customization assignments and other missing cross-domain data.
- [ ] **Exact next:** inspect the remaining live deterministic validator/consumer layer for another concrete integrity gap; do not reconstruct the missing general PQ reward layer.

### 2026-09-27 continuation — Character presentation identity validation-order hardening
- [x] Inspected the live `scripts/validate_character_presentation_consumers.py`.
- [x] Found a concrete robustness gap: preset/partner/reconciliation identifier projections could reach `set()`/sorting before malformed values were explicitly validated, allowing unhashable malformed IDs to raise uncontrolled `TypeError` failures.
- [x] Reordered projections to operate on explicitly valid non-empty string identifiers while retaining dedicated malformed-ID checks and making the uniqueness contract require every preset record ID to be valid.
- [x] Updated `docs/data/characters/character-presentation-consumer-audit.json`.
- [x] No canonical character, preset, or Partner Customization data changed.
- [ ] Runtime validator execution and CI/build remain unverified.
- [x] Preserved the evidence boundary around inferred character identity and missing cross-domain relationship data.
- [ ] **Exact next:** inspect the remaining live deterministic validator/consumer layer for another concrete integrity gap; do not invent missing PQ reward data.

### 2026-09-27 continuation — Skill→PQ endpoint validation-order hardening
- [x] Inspected the live `scripts/validate_skill_pq_crosslinks.py` after the prior duplicate guard.
- [x] Found a concrete robustness gap: duplicate detection ran before endpoint type/range validation, so a malformed unhashable `source_parallel_quests` value could reach `set()` and raise an uncontrolled `TypeError`.
- [x] Hardened the validator so a present `source_parallel_quests` field must be a list, each endpoint is validated as a non-boolean integer in supported range **1–186**, and only then is duplicate detection performed.
- [x] Updated `docs/data/skill-pq-cross-domain-linkage-integrity-audit-2026-09-26.json`; the canonical **474-skill / 246-edge / 170-represented-PQ** projection remains unchanged.
- [x] No canonical skill, PQ reward, or cross-domain relationship data was inferred or modified.
- [ ] Runtime validator execution and CI/build remain unverified.
- [x] **Exact next:** inspect the remaining live validator/consumer layer for another concrete integrity gap; preserve the missing general `docs/data/pq-reward-relationships.json` evidence boundary.

### 2026-09-27 continuation — Skill acquisition endpoint-order hardening
- [x] Hardened `scripts/validate_skill_acquisition_metadata.py` so malformed/unhashable PQ endpoints are rejected before duplicate-set construction.
- [x] Hardened canonical skill-ID uniqueness ordering so type validation precedes set construction.
- [x] Updated the acquisition integrity audit; canonical data remains unchanged.
- [ ] Runtime validator execution and CI/build remain unverified.
- [x] Preserved the evidence boundary around missing `docs/data/pq-reward-relationships.json`.
- [ ] Next deterministic audit: inspect the remaining live validator/consumer/projection layer for a concrete integrity gap.

### 2026-09-27 continuation — Partner skill validator root-container hardening
- [x] Hardened `scripts/validate_partner_skill_relationships.py` so relationship, skill, and character-bridge JSON roots must be objects before `.get()` access.
- [x] Added the hardening record to `docs/data/partner-skill-relationship-validator-audit-2026-09-26.json`.
- [x] No canonical relationship data changed; existing 474-skill / 3-relationship projection remains unchanged.
- [ ] Runtime validator execution and CI/build remain unverified.
- [x] Preserved evidence boundary: do not reconstruct missing `docs/data/pq-reward-relationships.json` without an evidence-complete producer/source.
- [ ] Next deterministic audit: inspect remaining live validator/consumer or projection for another concrete integrity gap.

### 2026-09-27 continuation — Skill→PQ pre-projection duplicate hardening
- [x] Inspected the live `scripts/validate_skill_pq_crosslinks.py`.
- [x] Added an explicit pre-projection duplicate `source_parallel_quests` guard so duplicate endpoints are rejected before reverse-index generation.
- [x] Updated `docs/data/skill-pq-cross-domain-linkage-integrity-audit-2026-09-26.json`; the canonical **474 skills / 246 edges / 170 represented PQs** projection remains unchanged.
- [ ] Runtime validator execution and CI/build remain unverified.
- [x] **Exact next:** inspect the remaining live validator for another concrete integrity gap; preserve all missing-PQ/reward evidence boundaries.

### 2026-09-27 continuation — PQ cross-domain forward-path integrity hardening
- [x] Inspected the live `scripts/validate_pq_cross_domain_index.py` after the Partner skill validator.
- [x] Found a path-integrity gap: an absolute forward-index path could bypass the repository root when resolved with `ROOT / forward`, and parent-directory traversal was not rejected.
- [x] Hardened the validator to require the declared forward index to be repository-relative and reject absolute/traversal paths before filesystem resolution.
- [x] Updated `docs/data/pq-cross-domain-index-validator-audit-2026-09-26.json`; the existing missing `docs/data/pq-reward-relationships.json` boundary remains unchanged.
- [ ] Runtime validator execution and CI/build remain unverified.
- [x] **Exact next:** inspect the next live deterministic validator for another concrete schema/type/range/identity/projection gap; do not reconstruct the missing general PQ reward layer without an evidence-complete source.

### 2026-09-27 continuation — Partner skill identity uniqueness hardening
- [x] Inspected the live `scripts/validate_partner_skill_relationships.py` as the next deterministic relationship validator.
- [x] Found a projection gap: canonical skill IDs and bridge partner names were converted to sets, so duplicate identity records could be silently collapsed and escape detection.
- [x] Hardened the validator to detect duplicate canonical skill IDs and duplicate canonical bridge partner names before set-based relationship resolution.
- [x] Updated `docs/data/partner-skill-relationship-validator-audit-2026-09-26.json`; the existing **474-skill / 3 explicit relationship** projection remains unchanged.
- [ ] Runtime validator execution and CI/build remain unverified.
- [x] **Exact next:** inspect the remaining live deterministic validator/consumer for another concrete schema/type/range/identity/projection mismatch; preserve the missing general PQ reward layer as an evidence boundary.

### 2026-09-27 continuation — Character presentation source-container hardening
- [x] Inspected the live `scripts/validate_character_presentation_consumers.py` as the next deterministic consumer after the skill-acquisition validator.
- [x] Found a robustness gap: canonical names and consumer records were projected into sets/maps before their container/item types were validated, allowing malformed data to raise uncontrolled type errors rather than deterministic validation failures.
- [x] Hardened the validator to require canonical character names to be a list of non-empty strings and bridge/preset/Partner Customization/reconciliation sources to be lists of objects before projections run.
- [x] Updated `docs/data/characters/character-presentation-consumer-audit.json`; the established clean identity/navigation projection and canonical data remain unchanged.
- [ ] Runtime validator execution and CI/build remain unverified.
- [x] **Exact next:** inspect the remaining live deterministic validator/consumer for another concrete schema/type/range/identity/projection mismatch; preserve the missing general PQ reward layer as an evidence boundary.

### 2026-09-27 continuation — Skill acquisition PQ-container falsey fallback hardening
- [x] Inspected the next live deterministic validator, `scripts/validate_skill_acquisition_metadata.py`, after confirming the repository currently has only six live `validate_*.py` scripts and the previously hardened targets are already covered.
- [x] Found a concrete acceptance gap: `source_parallel_quests` used a falsey fallback (`or []`), so a present malformed value such as `null`, `false`, `0`, or an empty string could be coerced into an apparently valid empty endpoint list.
- [x] Hardened the validator to distinguish an omitted field (no explicit endpoints) from a present value: present `source_parallel_quests` values must be lists before duplicate/type/range checks run.
- [x] Updated `docs/data/skill-acquisition-metadata-integrity-audit-2026-09-26.json` with the hardening record; no canonical skill acquisition data was changed.
- [ ] Runtime validator execution and CI/build remain unverified.
- [x] **Exact next:** inspect the remaining live deterministic consumer/projection layer for another concrete schema, type/range, identity, or source-vs-build-output mismatch; keep `docs/data/pq-reward-relationships.json` as an explicit evidence boundary until an evidence-complete producer exists.

### 2026-09-27 TODO progress update — Skill→PQ endpoint uniqueness hardening
- [x] Hardened `scripts/validate_skill_pq_crosslinks.py` against duplicate PQ IDs and boolean-as-integer PQ IDs inside canonical skill endpoint lists.
- [x] Recorded **0 duplicate / 0 boolean** endpoint violations in the Skill→PQ linkage audit; canonical **474 / 246 / 170** projection remains unchanged.
- [x] Preserved the evidence boundary around the missing general PQ reward forward layer.
- [ ] Runtime validator execution and CI/build remain unverified.
- [x] **Exact next:** continue with the next live deterministic validator/consumer or projection.

### 2026-09-26 TODO progress update — PQ cross-domain forward-source boundary confirmed
- [x] Confirmed `docs/data/pq-reward-relationships.json` is still absent from live `main`; the hardened cross-domain index validator correctly detects this.
- [x] Searched for a current general-PQ reward producer/generator and found only historical/audit references, not an evidence-complete replacement source.
- [x] Corrected the PQ index validator audit to distinguish structural schema success from the unresolved forward-source reachability failure.
- [x] Preserved the separate canonical Skill→PQ reverse layer; it does not establish the missing general PQ reward dataset.
- [ ] Do not reconstruct the missing forward/reverse PQ reward datasets without a complete canonical producer.
- [x] **Exact next:** continue with the next live validator/consumer or identify a complete producer for the missing PQ reward layer before any regeneration.

### 2026-09-26 TODO progress update — PQ cross-domain index schema hardening
- [x] Hardened `scripts/validate_pq_cross_domain_index.py` to require exactly **7** reverse-index declarations, unique report paths, and `farming.source` to match the canonical `forward_index`.
- [x] Added and registered `docs/data/pq-cross-domain-index-validator-audit-2026-09-26.json` with the expanded structural contract recorded as passing.
- [x] Preserved all canonical PQ relationship/provenance boundaries; no missing reward/reverse dataset was reconstructed.
- [ ] Runtime validator execution and CI/build remain unverified.
- [x] **Exact next:** continue with the next validator/consumer that is actually present in the live repository, prioritizing deterministic schema/identity/projection gaps over stale historical index entries.

### 2026-09-26 TODO progress update — Skill acquisition metadata schema hardening
- [x] Hardened `scripts/validate_skill_acquisition_metadata.py` against malformed root/field types, duplicate `source_parallel_quests` IDs, and boolean-as-integer PQ endpoints.
- [x] Recorded the expanded acquisition schema contract as **11/11** passing in `docs/data/skill-acquisition-metadata-integrity-audit-2026-09-26.json`.
- [x] Preserved the canonical **474-skill** dataset; no acquisition relationship was added or inferred.
- [ ] Runtime validator execution and CI/build remain unverified.
- [x] **Exact next:** continue the next live validator/consumer referenced by the PQ cross-domain index, prioritizing deterministic integrity gaps while keeping absent PQ reward/reverse datasets as provenance unless a complete source/generator exists.

### 2026-09-26 TODO progress update — Partner Customization key-ID projection hardening
- [x] Found a remaining deterministic schema/projection gap in `scripts/validate_partner_customization_character_navigation.py`: stable customization-key record IDs were not validated against their numeric key numbers.
- [x] Added explicit non-empty string, uniqueness, and exact `customization-key-01..20` projection checks.
- [x] Updated the navigation audit to **21/21** passing boolean checks while preserving the existing **20 / 20 / 34 / 152 / 20** navigation counts.
- [x] No canonical relationship or character data changed.
- [ ] Runtime validator execution and CI/build remain unverified.
- [x] **Exact next:** continue the next live validator/consumer or deterministic projection audit for evidence-backed schema/type/range/stale-cache drift.

### 2026-09-26 TODO progress update — Cross-domain reachability baseline refreshed
- [x] Recomputed the live cross-domain index against the current `main` Git tree.
- [x] Updated the reachability audit to **727 tree blobs / 1,634 reference occurrences / 742 reachable / 892 unreachable**.
- [x] Preserved all historical/planned references and the 18-item critical unreachable set.
- [x] No unsupported PQ reward/reverse data was generated.
- [ ] Runtime execution/CI remains unverified.
- [x] Exact next: continue the next live deterministic cross-domain validator/consumer audit.
### 2026-09-26 TODO progress update — Partner Customization recovery-audit count synchronization
- [x] Corrected the stale recovery-audit summary from 16 to the actual **18/18** passing boolean checks.
- [x] Confirmed the recovery audit is reachable on current `main` and removed the transient unreachable classification from the reachability audit.
- [x] No canonical character, preset, navigation, or partner-skill data was altered.
- [ ] Runtime execution/CI remains unverified.
- [x] Exact next: inspect the next live deterministic cross-domain validator/consumer for evidence-backed integrity drift.
### 2026-09-26 TODO progress update — Partner Customization recovery-audit reachability reconciled
- [x] Detected that the cross-domain index registers the Partner Customization recovery audit even though the file is absent from current `main`.
- [x] Recorded that reachability discrepancy without deleting the provenance registration or inventing a replacement artifact.
- [x] Corrected the live Partner Customization navigation audit metadata from an implicit 16-check summary to its actual **18 boolean checks, all passing**.
- [x] Kept canonical navigation data and partner-skill relationship evidence unchanged.
- [ ] Runtime execution/CI remains unverified.
- [x] Exact next: inspect the next live deterministic cross-domain validator/consumer for evidence-backed integrity drift.
### 2026-09-26 TODO progress update — Cross-domain reachability scalar drift corrected
- [x] Corrected docs/data/cross-domain-index-reference-reachability-audit-2026-09-26.json: its critical-reference count said 20 while its actual enumerated critical set contained 18.
- [x] Synchronized the scalar with the enumerated live set; no provenance references were deleted.
- [x] Current reachability baseline remains 730 live tree paths / 1,631 reference occurrences / 739 reachable / 892 unreachable.
- [x] Preserved the evidence boundary around the absent general PQ reward/reverse datasets.
- [ ] Runtime execution/CI remains unverified.
- [x] Exact next: inspect the next live cross-domain validator/consumer for a concrete deterministic integrity mismatch.
### 2026-09-26 TODO progress update — Character presentation validator hardened for optional generated explorer
- [x] Found and fixed a concrete live-validator failure: `scripts/validate_character_presentation_consumers.py` unconditionally required generated `docs/Characters-All.html`, which is absent from the source tree.
- [x] The validator now treats the generated explorer as optional build output and validates its navigation contract only when present; source-data checks remain mandatory.
- [x] Corrected the Markdown consumer regex input to use a real newline rather than a literal `\\n` sequence.
- [x] Refreshed `docs/data/characters/character-presentation-consumer-audit.json` with the optional-artifact status and latest validator commit.
- [x] No canonical data or relationship identity was inferred or changed.
- [ ] Runtime execution/CI remains unverified.
- [x] **Exact next:** inspect the next live cross-domain validator/consumer for a similar deterministic source-vs-build-output mismatch.
### 2026-09-26 continuation — Skill↔PQ deterministic validator hardening
- [x] Inspected the live skill→PQ validator and discovered a malformed literal `\\n` sequence in the checked-in Python source; corrected it rather than leaving a runtime syntax hazard.
- [x] Implemented the validator's documented exact checked-in reverse-projection comparison: `pq_ids` must equal the deterministic projection of `skills.json` `source_parallel_quests`, including skill counts, IDs, names, and relationship status.
- [x] Updated `docs/data/skill-pq-cross-domain-linkage-integrity-audit-2026-09-26.json` to record the correction and validation contract.
- [x] No PQ reward relationships were fabricated; the validator remains strictly grounded in the canonical skill corpus.
- [ ] Exact next: runtime-execute the hardened validator if repository execution is available; otherwise continue the next live deterministic cross-domain validator and keep CI/build status explicitly unverified.

### 2026-09-26 continuation — Partner skill relationship validator identity hardening
- [x] Hardened `scripts/validate_partner_skill_relationships.py` to validate both canonical skill IDs and canonical `partner_name` identities through `docs/data/characters/character-id-identity-bridge.json`.
- [x] Retained duplicate-pair, relationship-type, required-evidence, and evidence-file existence checks; no relationship data was fabricated or expanded.
- [x] Updated `docs/data/partner-skill-relationship-validator-audit-2026-09-26.json` to document the expanded validation scope and identity bridge dependency.
- [x] Static reconciliation of the three existing relationships remains clean: all three partner names resolve through the canonical character bridge and all six evidence paths are present.
- [ ] Exact next: continue the highest-priority deterministic cross-domain audit, prioritizing the remaining critical unreachable PQ reward/reverse datasets and only generating projections when a complete canonical source and deterministic generator are available.

### 2026-09-26 continuation — Partner/custom skill relationship census completed
- [x] Performed a repository-wide evidence census using Partner Customization + skill identifiers, partner identifiers, and the canonical `custom_partner_availability` relationship marker.
- [x] Confirmed the relationship layer remains at **3 explicit canonical assignments**: Arm Crash → Bardock, Arm Crash → Turles, and Reverse Mabakusenko → Majin Buu (Gohan Absorbed).
- [x] Investigated Phantom Fist, Dual Masenko, Flash Strike, and Psycho Barrier without promoting unsupported skill→partner edges; generic user/skillset mentions and page references are not treated as explicit assignments.
- [x] Added `docs/data/partner-skill-relationship-census-2026-09-26.json` and registered it in `docs/data/pq-cross-domain-index.json`.
- [x] Preserved the canonical 474-skill corpus boundary and the separate partner/custom relationship model.
- [ ] Exact next: investigate partner-only/non-CaC skills as a separate domain only if explicit corpus/schema evidence establishes that domain; otherwise continue the highest-priority live cross-domain deterministic validation work.

### 2026-09-26 continuation — Historical character/preset/navigation recovery reconciled
- [x] Inspected Git history for the previously reported missing character/preset/navigation artifacts and recovered the latest coherent historical versions/replacements already established by the repository's 2026-09-26 recovery work.
- [x] Confirmed the live `main` tree now exposes the canonical character identity bridge, 51-record preset layer, current presentation consumer scan, Skills↔Super Souls navigation audit, numeric preset loadout audit, Partner Customization navigation audit, and its validator.
- [x] Confirmed the stale `current-character-consumer-scan.json` reference is represented by the canonical `docs/data/current-presentation-consumer-scan-2026-09-24.json` replacement; the live PQ cross-domain index already points to the replacement rather than recreating the stale filename.
- [x] Recomputed the Partner Customization navigation contract directly from the live files: **20 keys / 20 reconciliation records / 34 bridge records / 152 canonical character names / 20 page links**, with all identity, uniqueness, parity, and navigation checks passing.
- [x] Preserved the evidence boundary: preset recovery restores presentation/navigation records only; it does not infer complete numeric loadouts, acquisition routes, DLC ownership, or Partner Customization skill relationships.
- [x] Updated the persistent handoff/TODO state so the recovery task is no longer left as an unfinished next step.
- [ ] Exact next: use the live cross-domain reachability audit to inspect the remaining critical unreachable primary/reverse datasets (especially the PQ reward relationship layer) and determine whether an evidence-complete deterministic source/generator exists before recreating anything.
- [ ] CI/build remains unverified in this environment.
- [ ] `docs/AI-CONTINUATION-PROMPT-EFFICIENCY-ADDENDUM.md` remains unavailable at the expected repository path (GitHub 404).

### 2026-09-26 continuation — Partner character navigation reference reachability audit
- [x] Attempted live fetches for the character/preset/navigation artifacts needed to reconcile Partner Customization mappings.
- [x] Confirmed six PQ cross-domain index references are currently unreachable on `main`: character identity bridge, current character consumer scan, skills↔Super Souls reference navigation audit, numeric preset loadout audit, Partner Customization character navigation audit, and its validator script.
- [x] Added `docs/data/partner-character-navigation-reference-existence-audit-2026-09-26.json` documenting the current reachability boundary and registered it in `docs/data/pq-cross-domain-index.json`.
- [x] Preserved the evidence rule: missing referenced artifacts are not treated as evidence that the underlying data/work never existed, and no unsupported Partner Customization skill edge was added.
- [ ] Exact next: inspect Git history for the missing artifact paths (or their replacements), recover the latest valid versions, and reconcile them against canonical character/preset records.

### 2026-09-26 continuation — Phantom Fist evidence reconciliation
- [x] Read the complete live Batch 473 record for **Phantom Fist** and its current-evidence audit.
- [x] Confirmed the evidence names **Hit, Mira, Frost, and Fu** as users/skillset contexts, but does not explicitly identify a Partner Customization assignment.
- [x] Removed the prior unresolved placeholder relationship from `docs/data/partner-skill-relationships.json`; the relationship index now contains only confirmed partner endpoints rather than an invented/unspecified partner.
- [ ] Exact next: broaden the search from skill artifacts into canonical character/preset/navigation datasets to find explicit skill→partner mappings, if present.

### 2026-09-26 continuation — Partner/custom relationship reconciliation boundary
- [x] Searched exact and variant Partner Customization phrases across live skill research artifacts.
- [x] Confirmed **Phantom Fist** is surfaced by the repository's `Partner Customization + skill_id` search, but the returned evidence does not expose an explicit partner assignment; therefore no confirmed skill→partner pair was inferred.
- [x] Recorded this as an explicit unresolved discovery marker in `docs/data/partner-skill-relationships.json`, preserving the evidence boundary.
- [ ] Exact next: inspect the complete Batch 473 record around Phantom Fist and then reconcile partner-character navigation/preset data once the actual character-navigation artifact is recoverable.

### 2026-09-26 continuation — Partner/custom relationship census follow-up
- [x] Performed a live repository-wide search for the exact **Partner Customization** phrase across the skill corpus/research artifacts.
- [x] Expanded the census beyond the three seeded relationship pairs; the live search found only four skill-related artifacts containing the exact phrase: Arm Crash research/audit and Reverse Mabakusenko research/audit. No additional explicit partner-skill pair was discovered from this corpus search.
- [x] Confirmed that Flash Strike and Psycho Barrier merely cite the Partner Customization reference page; their current evidence does not explicitly document a partner assignment, so no relationship was inferred.
- [ ] Exact next: broaden the census to partner-character navigation data and skill-user/preset records, then reconcile explicit partner availability against the canonical skill IDs without creating duplicates.
- [ ] Validator execution and CI/build remain unverified in this environment.

### 2026-09-26 continuation — Partner/custom skill relationship layer implemented
- [x] Audited the live repository for existing Partner Customization relationship data; existing artifacts documented partner context inside skill audits/research, but no dedicated canonical skill→partner relationship index was present.
- [x] Added `docs/data/partner-skill-relationships.json` with a reusable relationship layer separating canonical `skill_id` identity from partner/custom availability.
- [x] Seeded only explicit, evidence-backed canonical relationships: **Arm Crash → Bardock**, **Arm Crash → Turles**, and **Reverse Mabakusenko → Majin Buu (Gohan Absorbed)**.
- [x] Added `scripts/validate_partner_skill_relationships.py` to enforce canonical skill IDs, unique skill/partner pairs, relationship type, and evidence presence.
- [x] Preserved the Dual Masenko boundary: it remains excluded because the live canonical corpus has no `skill-dual-masenko` record and partner availability alone is not sufficient to manufacture one.
- [ ] Exact next: execute the new validator, then perform a systematic evidence-backed census of all existing skill audits/research batches for additional explicit Partner Customization relationships.
- [ ] CI/build remains unverified.

### 2026-09-26 continuation — Partner/custom skill domain boundary resolved
- [x] Researched the unresolved Dual Masenko / PQ118 question against current external references and the live repository.
- [x] Added `docs/data/partner-custom-skill-domain-boundary-audit-2026-09-26.json` and registered it in `docs/data/pq-cross-domain-index.json`.
- [x] Confirmed Dual Masenko is both a Future Warrior/CaC-acquirable TP Medal Shop skill and a Future Trunks Custom Partner skill; therefore partner availability does not justify a duplicate canonical skill record.
- [x] Established the modeling rule: partner/custom availability should be represented as a relationship/domain layer attached to an existing skill ID where the skill is already canonical; genuinely partner-only moves require separate-domain evidence before adding records.
- [x] Kept PQ118 → Dual Masenko unpromoted because current evidence supports TP Medal Shop acquisition and partner customization, while a third-party PQ guide conflicts with that boundary.
- [ ] Exact next: audit the repository for existing partner/custom relationship data and, if absent, design a reusable partner-skill relationship schema/index without duplicating canonical skills.
- [ ] CI/build remains unverified.
- [ ] Efficiency addendum remains unavailable at the expected repository path (GitHub 404).

### 2026-09-26 continuation — Acquisition metadata external corroboration pass
- [x] Re-read the live handoff/TODO and inspected the current acquisition integrity audit.
- [x] The deterministic acquisition audit remains clean: **474/474 records, 0 missing required acquisition fields, 0 internal metadata anomalies**.
- [x] Externally corroborated representative non-PQ acquisition boundaries: Super Guard is documented as a starting skill/Skill Shop skill; Godly Display is documented as a TP Medal Shop skill; current external material also identifies Soaring Fist and Divine Kamehameha as TP/STP Medal Shop skills. These checks support retaining the repository's non-PQ acquisition model rather than converting shop endpoints into PQ endpoints.
- [x] No canonical acquisition correction was made because the audit exposed no internally inconsistent record requiring correction.
- [x] Preserved the PQ121 evidence boundary: external material confirms Godly Display's TP Medal Shop acquisition, so no unsupported PQ121→Godly Display edge was introduced.
- [ ] Exact next: investigate the separate partner/custom-skill domain question around Dual Masenko/PQ118 and determine whether a non-CaC/partner skill corpus should be modeled separately, using explicit schema evidence before adding records.
- [ ] CI/build remains unverified.
- [ ] Efficiency addendum remains unavailable at the expected repository path (GitHub 404).

- [x] Audited internal acquisition metadata consistency across all 474 canonical skills; added `docs/data/skill-acquisition-metadata-integrity-audit-2026-09-26.json` and `scripts/validate_skill_acquisition_metadata.py`, and registered both in `docs/data/pq-cross-domain-index.json`.
- [x] Verified required acquisition fields (`unlock_method`, `source_quest_or_shop`, `acquisition_type`) are populated for the full canonical corpus and checked their consistency with explicit PQ endpoints.
- [ ] Investigate any acquisition metadata anomalies surfaced by the audit before making canonical corrections; external evidence must support each correction.

### 2026-09-26 TODO progress update — PQ unrepresented-endpoint evidence reconciliation
- [x] Reconciled all **16 currently unrepresented PQ IDs** against current PQ reward references and live canonical skill evidence.
- [x] Added `docs/data/pq-unrepresented-skill-endpoint-evidence-reconciliation-2026-09-26.json` and registered it in `docs/data/pq-cross-domain-index.json`.
- [x] Preserved the canonical evidence boundary: no new skill→PQ edge was promoted solely from a third-party reward label, non-skill reward, or ambiguous mapping.
- [x] Confirmed PQs **1, 30, 35, 47, 48, 93, 102, 103, 107, 108, 144, 157, 169, 170** have no currently supported canonical skill endpoint in the reviewed evidence.
- [x] PQ **118** remains unresolved at the canonical-schema level because external material associates a non-canonical/partner-style `Dual Masenko` reward with it, but the live repository has no canonical `skill-dual-masenko` record.
- [x] PQ **121** was not linked to Godly Display because the live repository's current Godly Display audit records TP Medal Shop acquisition; the external PQ121 association is therefore retained as conflicting evidence rather than promoted.
- [ ] Investigate whether partner/custom skills such as Dual Masenko belong in a separate skill domain before expanding the canonical skill corpus.
- [ ] CI/build remains unverified.
- [ ] Efficiency addendum remains unavailable at the expected repository path (GitHub 404).

### 2026-09-26 TODO progress update — Live skill↔PQ cross-domain linkage pass
- [x] Audited the live 474-record canonical skill corpus for explicit `source_parallel_quests` relationships.
- [x] Added `docs/data/skill-pq-reverse-index-2026-09-26.json` with all PQ IDs 1–186 represented explicitly.
- [x] Added `docs/data/skill-pq-cross-domain-linkage-integrity-audit-2026-09-26.json` and `scripts/validate_skill_pq_crosslinks.py`.
- [x] Registered the new reverse index, audit, and validator in `docs/data/pq-cross-domain-index.json`.
- [x] Current deterministic totals: **474 unique skills, 242 skills with PQ endpoints, 246 skill→PQ edges, 170 represented PQ IDs, 16 unrepresented PQ IDs, 0 invalid PQ IDs**.
- [x] Preserved the evidence boundary: an unrepresented PQ ID means only that no current canonical skill record explicitly points to it; it does **not** mean the PQ has no skill rewards.
- [x] The historical 244-edge PQ↔skill invariant is now documented as stale against the live 246-edge canonical corpus.
- [ ] Reconcile PQ IDs **1, 30, 35, 47, 48, 93, 102, 103, 107, 108, 118, 121, 144, 157, 169, 170** against a real PQ/reward corpus and promote only evidence-backed canonical skill endpoints.
- [ ] CI/build remains unverified.
- [ ] Efficiency addendum remains unavailable at the expected repository path (GitHub 404).

### 2026-09-26 TODO progress update — Mechanics frontier exhausted; integrity/linkage work begins
- [x] Fresh Batch 492 census found **0** canonical skills lacking a registered current-evidence audit; all **474** skill IDs are covered.
- [x] Corrected seven stale attack-type descriptions and synchronized the corrections across both canonical skill datasets.
- [x] Added and registered a full skill-corpus data-integrity audit.
- [x] Confirmed 0 missing sources, mechanics notes, unlock methods, or source-quest/shop endpoints across the canonical skill corpus.
- [ ] CI/build remains unverified.
- [ ] Efficiency addendum remains unavailable at the expected path (GitHub 404).
- [x] **Exact next:** begin deterministic cross-domain linkage/provenance validation between canonical skills and PQ/acquisition datasets; prioritize broken or unresolved skill↔PQ endpoints and only make evidence-backed corrections.

### 2026-09-26 TODO progress update — Skill Research Batch 491 completed
- [x] Fresh live mechanics frontier census performed after Batch 490.
- [x] Researched and synchronized **Gigantic Cluster, Holy Wrath, Gigantic Charge, Pendulum Bullet, and Heat Dome Attack**.
- [x] Canonical/index datasets remain **474/474**.
- [x] Added five current-evidence audits, Batch 491 research/thin-frontier artifacts, and registered all seven artifacts in the cross-domain index.
- [x] Evidence boundaries preserved; source discrepancies remain explicitly documented rather than normalized into unsupported certainty.
- [ ] CI/build remains unverified.
- [ ] Efficiency addendum remains unavailable at the expected path (GitHub 404).
- [x] **Exact next:** fresh unaudited mechanics-frontier census excluding Batch 491 and all prior registered current-evidence audits; do not reuse stale candidates.

### 2026-09-26 TODO progress update — Skill Research Batch 490 completed
- [x] Fresh live mechanics frontier census performed after Batch 489.
- [x] Researched and synchronized **Breaker Energy Wave, Emperor's Cannon, Dark Inscription, Gigantic Cluster, Heat Wave, Special Beam Cannon (Beast), Crimson Edge, and Potential Unleashed**.
- [x] Canonical/index parity remains **474/474**, with **0 missing / 0 extra IDs** and ordered parity true.
- [x] Added Batch 490 research/thin-frontier artifacts and eight current-evidence audits; all ten artifacts registered in the cross-domain index.
- [x] Evidence boundaries preserved, including the Emperor's Cannon acquisition conflict and source-bounded Special Beam Cannon (Beast) damage figures.
- [ ] CI/build remains unverified.
- [ ] Efficiency addendum remains unavailable at the expected path (GitHub 404).
- [x] **Exact next:** fresh unaudited mechanics-frontier census excluding Batch 490 and every prior registered current-evidence audit; do not reuse stale candidates.

### 2026-09-26 TODO progress update — Skill Research Batch 489 completed
- [x] Fresh live mechanics frontier census performed after Batch 488 with corrected audit filename normalization.
- [x] Researched and synchronized **God of Destruction's Roar, God of Destruction's Menace, Hero's Flute, Beast, Rakshasa's Claw, Reverse Mabakusenko, Indomitable, and Body Change**.
- [x] Canonical/index parity remains **474/474**, with **0 missing / 0 extra IDs** and ordered parity true.
- [x] Added Batch 489 research/thin-frontier artifacts and eight current-evidence audits; all ten artifacts registered in the cross-domain index.
- [x] Evidence boundaries preserved, including explicit player-reported status for Indomitable's health-threshold behavior.
- [ ] CI/build remains unverified; no workflow success is claimed.
- [ ] Efficiency addendum remains unavailable at the expected path (GitHub 404).
- [x] **Exact next:** fresh unaudited mechanics-frontier census excluding Batch 489 and every prior registered current-evidence audit; do not reuse stale candidate lists.

### 2026-09-26 TODO progress update — Skill Research Batch 488 completed
- [x] Fresh live 474-record mechanics frontier was re-censused after Batch 487 and excluded every skill ID represented by a registered current-evidence audit.
- [x] Researched and synchronized **Fierce Fist, Venus Fist, Handy Canon, Full Power Destruction, Prominence Flash, Galick Gun, Ill Rain, and Gigantic Cross**.
- [x] Canonical/index parity remains **474/474**, with **0 missing / 0 extra IDs** and ordered parity true.
- [x] Added Batch 488 research/thin-frontier artifacts and eight current-evidence audits; all ten artifacts are registered in `docs/data/pq-cross-domain-index.json`.
- [x] Evidence boundaries preserved. Venus Fist low-Health behavior and 3-Ki-bar reports are source-bounded; no exact hit/scaling modifier was invented.
- [ ] CI/build remains unverified; no workflow success is claimed.
- [ ] Efficiency addendum remains unavailable at the expected path (GitHub 404).
- [x] **Exact next:** fresh unaudited mechanics-frontier census excluding Batch 488 and every prior registered current-evidence audit; do not reuse stale candidate lists.


### 2026-09-26 continuation — Skill Research Batch 487 completed
- [x] Fresh live frontier was rechecked rather than blindly reusing the prior frontier.
- [x] Completed current-evidence mechanics enrichment for **Super Saiyan Blue Kaioken, Super Saiyan 2, Super Vegeta, Namek Finger, Bending Kamehameha, Flash Strike, Finishing Blow, and Sudden Death Beam**.
- [x] Synchronized canonical and index skill datasets; validation is **474/474**, with **0 missing / 0 extra IDs**.
- [x] Added Batch 487 research, thin-frontier audit, and current-evidence provenance registrations.
- [x] Preserved evidence boundaries: unsupported exact frames, hidden interactions, probabilities, and patch-independent scaling remain unresolved.
- [ ] CI/build remains unverified.
- [x] **Exact next:** fresh unaudited frontier census; do not reuse stale candidate lists.
### 2026-09-26 continuation — Batch 486 canonical mechanics enrichment

- [x] Re-censused the live 474-record frontier after Batch 485 and excluded known completed/audited records rather than duplicating them.
- [x] Researched and synchronized **Final Flash (Super), God Splitter, Majin Kamehameha, and Feint Crash**.
- [x] Added four dedicated current-evidence audits, the Batch 486 research record, and the thin-frontier audit.
- [x] Registered all Batch 486 artifacts in `docs/data/pq-cross-domain-index.json`.
- [x] Canonical/index datasets remain **474/474** with no record additions or removals.
- [ ] CI/build remains unverified; no workflow success is claimed.
- [x] **Exact next:** fresh live frontier census before Batch 487; current shortest candidates after excluding completed work are **Meteor Burst → Kill Driver → Fighting Pose G → Bluff Kamehameha → Punisher Shield → Fighting Pose B → Fake Death → Mach Dash**. Recheck the provenance registry before promotion.


### 2026-09-26 TODO progress update — Skill Research Batch 484 completed
- [x] Fresh 474-record frontier census excluded the completed Batches 481–483 and all skill IDs represented by the live registered current-evidence audit set.
- [x] Researched Spirit Slash, Gigantic Burst, Gigantic Roar, Emperor's Cannon, Gigantic Breaker, The Power to Overcome, God of Destruction's Menace, and Flash Chaser.
- [x] Enriched/synchronized all eight canonical/index records; parity remains 474/474, with no additions/removals.
- [x] Added eight current-evidence audits, docs/data/skill-research-batches/skill-batch-484.json, and docs/data/skill-batch-484-thin-frontier-mechanics-audit-2026-09-26.json.
- [x] Registered Batch 482/483 continuity records and Batch 484 provenance in docs/data/pq-cross-domain-index.json.
- [x] Preserved evidence boundaries: source-reported damage, timing, modifier, and hit-count values remain bounded; unsupported frames, probabilities, hidden interactions, and patch-independent scaling were not inferred.
- [ ] CI/build remains unverified; no workflow success is claimed.
- [x] Exact next: fresh unaudited mechanics frontier excluding Batch 484 and all prior registered current-evidence audits; current shortest remaining candidates are Dancing Parapara, God of Destruction's Roar, God Punisher, Super Saiyan God Super Saiyan (Evolved), Total Detonation Ball, Future Super Saiyan, Godly Display, and Final Pose.

### 2026-09-26 TODO progress update — Skill Research Batch 482 completed
- [x] Researched and synchronized **Death Ball, Galick Gun, Sphere of Destruction, Breaker Energy Wave, Hyper Drain, Handy Canon, Fierce Fist, Venus Fist**.
- [x] Canonical/index parity remains **474/474**.
- [x] Historical damage tests are labeled source-bound; unresolved mechanics were not guessed.
- [x] Batch 482 research checkpoint and canonical synchronization completed.
- [ ] CI/build remains unverified.
- [x] **Exact next:** fresh unaudited mechanics frontier excluding Batch 482 and all prior current-evidence-audited records.

### 2026-09-26 TODO progress update — Skill Research Batch 481 completed
- [x] Researched and synchronized **Dark Inscription, Reverse Mabakusenko, Body Change, Hero's Flute, Indomitable, Crusher Ball, Rakshasa's Claw**.
- [x] Added Batch 481 research/current-evidence artifact and cross-domain registration.
- [x] Canonical/index parity remains **474/474**.
- [x] Indomitable community-reported mechanics are explicitly bounded; acquisition/drop remains open.
- [ ] CI/build remains unverified.
- [x] **Exact next:** fresh frontier census excluding Batch 481 and all prior registered current-evidence audits; prioritize **Death Ball → Galick Gun → Sphere of Destruction → Breaker Energy Wave → Hyper Drain → Handy Canon → Fierce Fist → Venus Fist**.

### 2026-09-26 TODO progress update — Skill Research Batch 480 completed
- [x] Fresh 474-record mechanics frontier excluded every skill with a registered current-evidence audit and selected **Evil Explosion, Prominence Flash, Ill Rain, Power Impact, Gigantic Cross, Full Power Destruction, Photon Swipe, God of Destruction's Plaything**.
- [x] Enriched and synchronized all eight records in `docs/data/skills.json` and `docs/data/skills-index.json`; parity remains **474/474**, with 0 missing / 0 extra IDs.
- [x] Added eight current-evidence audits, Batch 480 research/thin-frontier artifacts, and provenance registrations.
- [x] Corrected stale Photon Swipe character-source attribution to **Android 21**.
- [ ] CI/build remains unverified; no workflow success is claimed.
- [x] **Exact next:** fresh unaudited mechanics frontier excluding Batch 480 and all prior current-evidence-audited records.
- [x] **Exact next frontier after Batch 480:** **God of Destruction's Plaything, Dark Inscription, Reverse Mabakusenko, Body Change, Hero's Flute, Indomitable, Crusher Ball, and Rakshasa's Claw**. These are the shortest canonical mechanics records remaining after excluding all registered current-evidence audits; the next cycle must re-census live state before promoting them.

### 2026-09-26 TODO progress update — Skill Research Batch 479 completed
- [x] Fresh 474-record mechanics frontier selected **Taunt, Demonic Destruction, Neo Tri-Beam, Divine Lasso, Chaotic Time Impact, Gamma Impact, Gigantic Nova, Brutal Buster** after excluding all registered current-evidence-audited skills.
- [x] Enriched/synchronized all eight records; canonical/index remain **474/474**, **0 missing / 0 extra**.
- [x] Added eight audit artifacts, Batch 479 research/thin-frontier records, and provenance registry entries.
- [x] Preserved evidence boundaries; unsupported exact frames, scaling, probabilities, and hidden conditions remain unresolved.
- [ ] CI/build remains unverified.
- [ ] Efficiency addendum remains unavailable at expected path (GitHub 404).
- [x] **Exact next:** fresh unaudited mechanics census for Batch 480.

### 2026-09-26 TODO progress update — Skill Research Batch 478 completed
- [x] Fresh 474-record mechanics frontier excluded every skill with a registered current-evidence audit and selected **Thunder Flash, Celestial Wave, Saiyan Spirit, Bomber DX, Time Bullet, Galick Cannon, Death Beam, Gamma Blaster**.
- [x] Enriched and synchronized all eight records in `docs/data/skills.json` and `docs/data/skills-index.json`; canonical/index remain **474/474** with **0 missing / 0 extra**.
- [x] Added eight current-evidence audits, the Batch 478 research/thin-frontier artifacts, and provenance registry entries.
- [x] Preserved evidence boundaries; unsupported exact frames, scaling, probabilities, and hidden conditions remain unresolved.
- [ ] CI/build status remains unverified; no workflow success is claimed.
- [ ] Efficiency addendum remains unavailable at the expected path (GitHub 404).
- [x] **Exact next:** run another fresh unaudited mechanics frontier census excluding Batch 478 and all prior current-evidence-audited records.

### 2026-09-26 TODO progress update — Skill Research Batch 477 completed
- [x] Fresh 474-record mechanics frontier excluded every skill with a registered current-evidence audit and selected **Double Sunday, Super Black Kamehameha Rosé, Apocalyptic Burst, Destruction's Concerto: Meteor, Demon Flash Strike, Afterimage, Excellent Full Course, Ultra Instinct**.
- [x] Enriched and synchronized all eight records in `docs/data/skills.json` and `docs/data/skills-index.json`; canonical/index remain **474/474** with **0 missing / 0 extra**.
- [x] Added eight current-evidence audits, the Batch 477 research/thin-frontier artifacts, and provenance registry entries.
- [x] Preserved evidence boundaries; unsupported exact frames, scaling, probabilities, and hidden conditions remain unresolved.
- [ ] CI/build status remains unverified; no workflow success is claimed.
- [ ] Efficiency addendum remains unavailable at the expected path (GitHub 404).
- [x] **Exact next:** run another fresh unaudited mechanics frontier census excluding Batch 477 and all prior current-evidence-audited records.

### 2026-09-26 TODO progress update — Skill Research Batch 476 completed
- [x] Fresh 474-record mechanics frontier excluded every skill with a registered current-evidence audit and selected **Assault Rain, Saiyan Blaster, Soaring Rush, Heroic Assault, Endless Shoot, Deadly Dance, All Clear, Spirit Bomb**.
- [x] Enriched and synchronized all eight records in `docs/data/skills.json` and `docs/data/skills-index.json`; canonical/index remain **474/474** with **0 missing / 0 extra**.
- [x] Added eight current-evidence audits, the Batch 476 research/thin-frontier artifacts, and provenance registry entries.
- [x] Preserved evidence boundaries; unsupported exact frames, scaling, probabilities, and hidden conditions remain unresolved.
- [ ] CI/build status remains unverified; no workflow success is claimed.
- [ ] Efficiency addendum remains unavailable at the expected path (GitHub 404).
- [x] **Exact next:** run another fresh unaudited mechanics frontier census excluding Batch 476 and all prior current-evidence-audited records.

### 2026-09-26 TODO progress update — Skill Research Batch 475 completed
- [x] Fresh 474-record mechanics frontier excluded every skill with a registered current-evidence audit and selected **Blazing Attack, S.S. Deadly Bomber, Soaring Fist, Timespace Impact, Psycho Barrier, Shadow Crusher, Spirit Ball, Double Crush**.
- [x] Enriched and synchronized all eight records in `docs/data/skills.json` and `docs/data/skills-index.json`; canonical/index remain **474/474** with **0 missing / 0 extra**.
- [x] Added eight current-evidence audits, the Batch 475 research/thin-frontier artifacts, and provenance registry entries.
- [x] Preserved evidence boundaries; unsupported exact frames, scaling, probabilities, and hidden conditions remain unresolved.
- [ ] CI/build status remains unverified; no workflow success is claimed.
- [ ] Efficiency addendum remains unavailable at the expected path (GitHub 404).
- [x] **Exact next:** run another fresh unaudited mechanics frontier census excluding Batch 475 and all prior current-evidence-audited records.

### 2026-09-26 continuation — Batch 472 canonical reconciliation

- [x] Used the newly verified full-blob access path to reconcile Batch 472 against the live canonical skill datasets.
- [x] Synchronized **7 of 8** Batch 472 research records into both `docs/data/skills.json` and `docs/data/skills-index.json`: Big Bang Knuckle, God Breaker, Heroic Counter, Counter Impact, Time Skip/Back Breaker, Time Skip/Flash Skewer, and Time Skip/Jump Spike.
- [x] Preserved source-reported numerical values as source-specific and retained existing provenance/restriction boundaries.
- [x] Confirmed **Punisher Drive has no canonical skill record** in the current 474-record dataset, so it was not fabricated or inserted merely to force batch parity.
- [x] Post-write validation confirms **474/474** records in both canonical datasets.
- [ ] CI/build remains unverified.
- [ ] `docs/AI-CONTINUATION-PROMPT-EFFICIENCY-ADDENDUM.md` remains unavailable at the expected path.
- [x] **Exact next:** reconcile any remaining Batch 473/472 audit artifacts against canonical records that actually exist, then begin a fresh unaudited mechanics frontier excluding all registered current-evidence audits.

### 2026-09-26 continuation — Canonical synchronization breakthrough

- [x] Found the safe large-file path: GitHub blob fetch returns the complete canonical JSON blobs even when normal file fetch is truncated; canonical writes can then be performed against the exact blob SHA.
- [x] Promoted **Arm Crash, Phantom Fist, Justice Combination, Headshot, and Gigantic Rage** from the Batch 473 evidence layer into both `docs/data/skills.json` and `docs/data/skills-index.json`.
- [x] Updated their canonical `mechanics_notes`, `last_verified`, research/audit registry state, and preserved evidence boundaries.
- [x] Verified that **Time Skip/Molotov has no discoverable canonical repository record** under that exact name, so it was deliberately not fabricated into the 474/473 canonical dataset.
- [x] This resolves the previously documented large-file synchronization blocker for JSON datasets; future cycles should use blob fetch/update rather than the truncated file-content response.
- [ ] CI/build remains unverified.
- [ ] `docs/AI-CONTINUATION-PROMPT-EFFICIENCY-ADDENDUM.md` remains unavailable at the expected repository path.
- [x] **Exact next:** use the newly available full-blob canonical path to reconcile the remaining verified-but-pending Batch 472/473 audit artifacts against canonical records, then perform a fresh unaudited census and continue larger-batch mechanics enrichment.

### 2026-09-26 continuation — Batch 474 canonical-frontier verification

- [x] Re-inspected the handoff and TODO state and performed a repository-wide audit search rather than blindly duplicating Batch 473.
- [x] Confirmed that several Batch 473 candidates do not have discoverable current-evidence audit matches through the repository search surface, so they remain **verification candidates**, not falsely marked complete.
- [x] Added `docs/data/skill-research-batches/skill-batch-474.json` to record this frontier and the evidence boundary.
- [ ] Resolve the six Batch 474 candidates against the canonical skill datasets using a safe large-file access/write path; only then promote them to canonical mechanics records.
- [ ] Canonical `skills.json` / `skills-index.json` synchronization remains the blocking infrastructure issue.
- [ ] CI/build remains unverified.
- [ ] `docs/AI-CONTINUATION-PROMPT-EFFICIENCY-ADDENDUM.md` still appears unavailable at the expected repository path.
- [x] **Exact next:** investigate the repository's generated/indexed skill-data files and GitHub tree/file APIs for a non-truncating canonical update path, then synchronize the oldest verified-but-pending mechanics records before starting another research batch.

### 2026-09-26 continuation — Skill Research Batch 473 completed

- [x] Performed the fresh unaudited mechanics frontier after Batch 472, excluding prior registered current-evidence audits.
- [x] Completed **Arm Crash, Phantom Fist, Time Skip/Molotov, Justice Combination, Headshot, and Gigantic Rage** with current Xenoverse 2-specific mechanics/acquisition evidence and bounded source attribution.
- [x] Added six current-evidence audit artifacts plus Batch 473 research and thin-frontier artifacts.
- [x] Registered all eight Batch 473 artifacts in `docs/data/pq-cross-domain-index.json`.
- [x] Preserved source-reported numerical values without presenting them as universal balance constants; unsupported frames, scaling formulas, hidden interactions, and probabilities remain unresolved.
- [ ] Canonical `docs/data/skills.json` and `docs/data/skills-index.json` synchronization remains pending because the live canonical blobs are too large/truncated by the available GitHub content-fetch/update path; no canonical parity claim is made for Batches 472–473.
- [ ] CI/build remains unverified.
- [ ] `docs/AI-CONTINUATION-PROMPT-EFFICIENCY-ADDENDUM.md` remains unavailable at the expected repository path (GitHub 404).
- [x] **Exact next:** perform another fresh unaudited mechanics-frontier census excluding Batch 473 and every prior current-evidence audit; continue research and then synchronize the canonical datasets when a safe large-file write path is available.

### 2026-09-26 continuation — Skill Research Batch 472 prepared

- [x] Performed a fresh unaudited mechanics frontier after Batch 471 and selected **Big Bang Knuckle, God Breaker, Heroic Counter, Counter Impact, Punisher Drive, Time Skip/Back Breaker, Time Skip/Flash Skewer, and Time Skip/Jump Spike**.
- [x] Added the Batch 472 research artifact, thin-frontier audit, eight current-evidence audit artifacts, and registered all nine artifacts in `docs/data/pq-cross-domain-index.json`.
- [x] Rechecked current Xenoverse 2-specific mechanics and acquisition evidence from dedicated skill references plus official/secondary corroboration where available.
- [x] Preserved source-reported damage values as source-reported values and bounded unsupported frame data, scaling formulas, probabilities, and hidden interactions.
- [ ] Canonical `docs/data/skills.json` and `docs/data/skills-index.json` synchronization remains pending because the live canonical blobs are too large for the available GitHub file-content fetch/update path in this cycle; no canonical parity claim is made for Batch 472.
- [ ] CI/build remains unverified.
- [x] **Exact next:** perform another fresh unaudited mechanics frontier excluding Batch 472 and every prior current-evidence audit; then synchronize the next completed batch into the canonical skill datasets when the canonical blobs are writable.

### 2026-09-26 TODO progress update — Skill Research Batch 471 completed
- [x] Researched **Fighting Pose H, Brave Heat, Super Ghost Buu Attack, Supreme Fury, Rocket Tackle, Trap Shooter, Murder Grenade, and Chain Destructo-Disc Barrage**.
- [x] Enriched/synchronized canonical and index datasets; validation remains 474/474 with 0 missing / 0 extra.
- [x] Added eight audits, Batch 471 research/thin-frontier artifacts, and provenance registrations.
- [ ] CI/build remains unverified.
- [x] **Exact next:** fresh unaudited mechanics frontier excluding Batch 471 and all prior current-evidence-audited records.

### 2026-09-26 TODO progress update — Skill Research Batch 470 completed
- [x] Researched **Energy Release, Super Destructo-Disc, Android Rush, Burning Attack, Chaos Shot, Surging Spirit, Reverse Shot, and Grand Smasher**.
- [x] Enriched/synchronized canonical and index datasets; validation target remains 474/474 with 0 missing / 0 extra.
- [x] Added eight current-evidence audits, Batch 470 research/thin-frontier artifacts, and provenance registrations.
- [x] Preserved the built-in Ultra Instinct semantics of Surging Spirit and bounded all unsupported mechanics rather than inferring them.
- [ ] CI/build remains unverified.
- [ ] Efficiency addendum remains unavailable at the expected path (GitHub 404).
- [x] **Exact next:** fresh unaudited mechanics frontier excluding Batch 470 and all prior current-evidence-audited records.

### 2026-09-26 TODO progress update — Skill Research Batch 469 completed
- [x] Researched **Fighting Pose C, Burst Kamehameha, Supernova, Freedom Kick, Super Elite Combo, Atomic Blast, Super Ghost Kamikaze Attack (Super), and Super God Shock Flash**.
- [x] Enriched/synchronized canonical and index datasets; validation target remains 474/474 with 0 missing / 0 extra.
- [x] Added eight current-evidence audits, Batch 469 research/thin-frontier artifacts, and provenance registrations.
- [x] Preserved Atomic Blast's reward-source conflict and Super Ghost Super/Ultimate variant separation.
- [ ] CI/build remains unverified.
- [ ] Efficiency addendum remains unavailable at the expected path (GitHub 404).
- [x] **Exact next:** fresh unaudited mechanics frontier excluding Batch 469 and all prior current-evidence-audited records.

### 2026-09-26 TODO progress update — Skill Research Batch 468 completed
- [x] Researched **Super Saiyan Blue Kaioken, Super Saiyan 2, Supernova Cooler, Super Vegeta, Maiden Burst, Counter Burst, Bluff Kamehameha, and Super Dragon Flight**.
- [x] Enriched/synchronized canonical and index datasets; validation target remains 474/474 with 0 missing / 0 extra.
- [x] Added eight current-evidence audits, Batch 468 research/thin-frontier artifacts, and provenance registrations.
- [x] Corrected/clarified the distinct Super Dragon Flight Ultimate variant versus the 100-Ki Super variant.
- [x] Preserved evidence boundaries and source/version conflicts.
- [ ] CI/build remains unverified.
- [x] **Exact next:** fresh unaudited mechanics frontier excluding Batch 468 and all prior current-evidence-audited records.

### 2026-09-26 TODO progress update — Skill Research Batch 467 completed
- [x] Researched **Seagull Combination, Remote Serious Bomb, Shooting Strike, Energy Dome, Kaioken, Gorgeous Shot, Gravity Impact, and Hawk Charge**.
- [x] Enriched/synchronized canonical and index datasets; parity remains **474/474**, 0 missing / 0 extra.
- [x] Added eight current-evidence audits, Batch 467 research/thin-frontier artifacts, and provenance registrations.
- [x] Preserved evidence boundaries and explicit source/version conflicts.
- [ ] CI/build remains unverified.
- [x] **Exact next:** fresh unaudited mechanics frontier excluding Batch 467 and all prior current-evidence-audited records.

### 2026-09-26 continuation — Skill Research Batch 437 completed

- [x] Fresh unaudited mechanics frontier selected **Majin Kamehameha, Mach Dash, Revenge Death Ball, and Namek Finger** after reconciling the live Batch 436 state and excluding prior current-evidence-audited records.
- [x] Added four current-evidence audits plus Batch 437 research and thin-frontier audit artifacts.
- [x] Corrected **Majin Kamehameha** from stale **Ultimate** classification to **Super**, while retaining its 100-Ki Ki Blast, PQ60 endpoint, three charge stages, 5-to-15-hit behavior, approximately 10%-to-15% source-reported damage, and Majin CaC restriction.
- [x] Expanded **Mach Dash** mechanics with the 200-Stamina Power Up Evasive, 1.5% speed increase, PQ18 endpoint, and the documented 11.5-vs-12-second source discrepancy.
- [x] Expanded **Revenge Death Ball** mechanics with its 300+ Ki resource model, 12-to-22-hit charge scaling, source-reported 30%-to-70% damage range, 300 Ki input consumption, and remaining-Ki charge behavior.
- [x] Expanded **Namek Finger** mechanics with its 100-Ki Namekian-only grab/stun behavior, documented 10% damage, and the current Skill Shop vs maintained TP Medal Shop provenance distinction.
- [x] Synchronized all four records into both canonical skill datasets and refreshed their current-scope verification date to 2026-09-26.
- [x] Registered the Batch 437 research record, thin-frontier audit, and four skill audits in docs/data/pq-cross-domain-index.json.
- [x] Validated **474/474** canonical/index records with ordered ID parity, **0 missing / 0 extra**, and six Batch 437 registry entries.
- [ ] CI/build remains unverified; no workflow success is claimed.
- [ ] **Repository efficiency addendum check:** `docs/AI-CONTINUATION-PROMPT-EFFICIENCY-ADDENDUM.md` currently returns GitHub 404 and therefore could not be read or verified.
- [x] **Exact next:** run another fresh unaudited mechanics frontier census excluding Batch 437 and every prior current-evidence-audited record, then continue the canonical research/synchronization cycle.

### 2026-09-26 continuation — Skill Research Batch 436 completed

- [x] Fresh unaudited mechanics frontier selected **Candy Beam (Super), Big Bang Kamehameha, Dimensional Hole, and God of Destruction's Poise** after excluding Batch 435 and all prior current-evidence-audited records.
- [x] Added four current-evidence audits plus Batch 436 research and thin-frontier audit artifacts.
- [x] Rechecked current Xenoverse 2-specific cost, classification, acquisition, transformation/counter/charge behavior, and bounded numeric mechanics against dedicated skill references; unsupported exact frames, hidden interactions, patch-independent scaling, and probabilities remain bounded.
- [x] Synchronized all four records into both canonical skill datasets and refreshed their current-scope verification date to 2026-09-26.
- [x] Registered the Batch 436 research record, thin-frontier audit, and four skill audits in docs/data/pq-cross-domain-index.json.
- [x] Validated **474/474** canonical/index records with **0 missing / 0 extra**.
- [ ] CI/build remains unverified; no workflow success is claimed.
- [x] **Exact next:** run another fresh unaudited mechanics frontier census excluding Batch 436 and every prior current-evidence-audited record, then continue the canonical research/synchronization cycle.

### 2026-09-26 continuation — Skill Research Batch 435 completed

- [x] Fresh unaudited mechanics frontier selected **Kaioken Kamehameha, Super Saiyan God Super Saiyan, Double Sunday, and Excellent Full Course** after excluding Batch 434 and all prior current-evidence-audited records.
- [x] Added four current-evidence audits plus Batch 435 research and thin-frontier audit artifacts.
- [x] Rechecked current Xenoverse 2-specific cost, classification, acquisition, sequence/transformation behavior, and bounded numeric mechanics against dedicated skill references; unsupported exact frames, hidden interactions, patch-independent scaling, and probabilities remain bounded.
- [x] Synchronized all four records into both canonical skill datasets and refreshed their current-scope verification date to 2026-09-26.
- [x] Registered the Batch 435 research record, thin-frontier audit, and four skill audits in docs/data/pq-cross-domain-index.json.
- [x] Validated **474/474** canonical/index records with **0 missing / 0 extra**.
- [ ] CI/build remains unverified; no workflow success is claimed.
- [x] **Exact next:** run another fresh unaudited mechanics frontier census excluding Batch 435 and every prior current-evidence-audited record, then continue the canonical research/synchronization cycle.

### 2026-09-26 continuation — Skill Research Batch 434 completed

- [x] Corrected the fresh unaudited frontier to **Pressure Sign, Blaster Shell, Destruction's Concerto: Meteor, and Darkness Twin Star** after excluding every earlier current-evidence-audited record; the previously attempted Kaioken Kamehameha entry was removed from Batch 434 because it already had a 2026-09-25 current-evidence audit.
- [x] Added four current-evidence audits plus Batch 434 research and thin-frontier audit artifacts.
- [x] Rechecked current Xenoverse 2-specific cost, classification, acquisition, counter/projectile/defensive behavior, and bounded numeric mechanics against dedicated skill references; unsupported exact frames and patch-independent values remain bounded.
- [x] Synchronized all four records into both canonical skill datasets and refreshed their current-scope verification date to 2026-09-26.
- [x] Registered the Batch 434 research record, thin-frontier audit, and four skill audits in docs/data/pq-cross-domain-index.json.
- [x] Validated **474/474** canonical/index records with **0 missing / 0 extra**.
- [ ] CI/build remains unverified; no workflow success is claimed.
- [x] **Exact next:** run another fresh unaudited mechanics frontier census excluding Batch 434 and every prior current-evidence-audited record, then continue the canonical research/synchronization cycle.

### 2026-09-26 continuation — Skill Research Batch 434 completed

- [x] Fresh unaudited mechanics frontier selected **Pressure Sign, Kaioken Kamehameha, Super Saiyan God Super Saiyan, and Blaster Shell** after excluding Batch 433 and all earlier current-evidence-audited records.
- [x] Added four current-evidence audits plus Batch 434 research and thin-frontier audit artifacts.
- [x] Rechecked current Xenoverse 2-specific cost, classification, acquisition, counter/beam/transformation/projectile behavior, and bounded numeric mechanics against dedicated skill references; unsupported exact frames and patch-independent values remain bounded.
- [x] Synchronized all four records into both canonical skill datasets and refreshed their current-scope verification date to 2026-09-26.
- [x] Registered the Batch 434 research record, thin-frontier audit, and four skill audits in docs/data/pq-cross-domain-index.json.
- [x] Validated **474/474** canonical/index records with **0 missing / 0 extra**.
- [ ] CI/build remains unverified; no workflow success is claimed.
- [x] **Exact next:** run another fresh unaudited mechanics frontier census excluding Batch 434 and every prior current-evidence-audited record, then continue the canonical research/synchronization cycle.


### 2026-09-26 continuation — Skill Research Batch 433 completed

- [x] Fresh unaudited mechanics frontier selected **One-Handed Kamehameha mk.II, Innocence Cannon, Sonic Bomb, and Energy Minefield** after excluding Batch 432 and all prior current-evidence-audited records.
- [x] Added four current-evidence audits plus Batch 433 research and thin-frontier audit artifacts.
- [x] Rechecked current Xenoverse 2-specific cost, classification, acquisition, sequence behavior, resource usage, and bounded numeric mechanics against dedicated skill references; secondary/community evidence was explicitly qualified.
- [x] Synchronized all four records into both canonical skill datasets and refreshed their current-scope verification date to 2026-09-26.
- [x] Registered the Batch 433 research record, thin-frontier audit, and four skill audits in `docs/data/pq-cross-domain-index.json`.
- [x] Validated **474/474** canonical/index records with **0 missing / 0 extra**.
- [ ] CI/build remains unverified; no workflow success is claimed.
- [x] **Exact next:** run another fresh unaudited mechanics frontier census excluding Batch 433 and every prior current-evidence-audited record, then continue the canonical research/synchronization cycle.

### 2026-09-26 continuation — Skill Research Batch 432 completed

- [x] Fresh unaudited mechanics frontier selected **Super Gamma Blast, Super Ghost Kamikaze Attack, Final Flash (Super), and Super God Shock Flash** after excluding Batch 431 and all prior current-evidence-audited records.
- [x] Added four current-evidence audits plus Batch 432 research and thin-frontier audit artifacts.
- [x] Rechecked current Xenoverse 2-specific cost, classification, acquisition context, charge/projectile/counter behavior, hit counts, and bounded numeric claims against dedicated skill references.
- [x] Synchronized all four records into both canonical skill datasets and refreshed their current-scope verification date to 2026-09-26.
- [x] Registered the Batch 432 research record, thin-frontier audit, and four skill audits in `docs/data/pq-cross-domain-index.json`.
- [x] Validated **474/474** canonical/index records with **0 missing / 0 extra**.
- [ ] CI/build remains unverified; no workflow success is claimed.
- [x] **Exact next:** run another fresh unaudited mechanics frontier census excluding Batch 432 and every prior current-evidence-audited record, then continue the canonical research/synchronization cycle.

### 2026-09-26 continuation — Skill Research Batch 431 completed

- [x] Fresh unaudited 474-record mechanics frontier selected **Crazy Finger Shot, Fighting Pose D, Innocence Bullet, and Justice Rush** after excluding Batch 430 and all records with prior current-evidence audit registrations.
- [x] Added four current-evidence audits plus Batch 431 research and thin-frontier audit artifacts.
- [x] Rechecked current Xenoverse 2-specific mechanics, resource costs, acquisition context, hit/sequence behavior, effect duration, and bounded numeric claims against dedicated skill references; legacy community numeric evidence was kept explicitly bounded where current documentation did not establish the value.
- [x] Synchronized all four records into both canonical skill datasets and refreshed their current-scope verification date to 2026-09-26.
- [x] Registered the Batch 431 research record, thin-frontier audit, and four skill audits in docs/data/pq-cross-domain-index.json.
- [x] Validated **474/474** canonical/index records with **0 missing / 0 extra**.
- [ ] CI/build remains unverified; no workflow success is claimed.
- [x] **Exact next:** run another fresh unaudited mechanics frontier census excluding Batch 431 and every prior current-evidence-audited record, then continue the canonical research/synchronization cycle.

### 2026-09-26 continuation — Skill Research Batch 430 completed

- [x] Fresh unaudited 474-record mechanics frontier selected **Light Grenade, Sneaky Strike, Sonic Rush, and Eagle Kick** after excluding records with prior current-evidence audit registrations.
- [x] Added four current-evidence audits plus `docs/data/skill-research-batches/skill-batch-430.json` and the Batch 430 thin-frontier mechanics audit.
- [x] Rechecked current Xenoverse 2-specific mechanics, acquisition endpoints, resource costs, hit/sequence behavior, and bounded numeric claims against dedicated skill references and independent corroboration where available.
- [x] Synchronized all four records into both canonical skill datasets and refreshed their current-scope verification date to 2026-09-26.
- [x] Registered the Batch 430 research record, thin-frontier audit, and four skill audits in `docs/data/pq-cross-domain-index.json`.
- [x] Validated **474/474** canonical/index IDs with **0 missing / 0 extra**.
- [ ] CI/build remains unverified; no workflow success is claimed.
- [x] **Exact next:** run another fresh unaudited mechanics frontier census excluding Batch 430 and every prior current-evidence-audited record, then continue the canonical research/synchronization cycle.
### 2026-09-26 continuation — Skill Research Batch 429 completed

- [x] Fresh unaudited frontier census selected **Energy Charge, Shield Barrier, Ice Claw, and Raid Blast** after excluding all records with prior current-evidence audit registrations.
- [x] Added four current-evidence audits plus Batch 429 research and thin-frontier audit records.
- [x] Rechecked current Xenoverse 2-specific mechanics, acquisition endpoints, resource costs, defensive/attack behavior, and bounded numeric claims against dedicated skill references and independent corroboration where available.
- [x] Synchronized all four records into both canonical skill datasets and refreshed their current-scope verification date to 2026-09-26.
- [x] Registered the Batch 429 research record, thin-frontier audit, and four skill audits in docs/data/pq-cross-domain-index.json.
- [x] Validated **474/474** canonical/index IDs with **0 missing / 0 extra**.
- [ ] CI/build remains unverified; no workflow success is claimed.
- [x] **Exact next:** run another fresh unaudited mechanics frontier census excluding Batch 429 and every prior current-evidence-audited record, then continue the canonical research/synchronization cycle.

### 2026-09-26 continuation — Skill Research Batch 428 completed

- [x] Fresh unaudited frontier census selected **Mach Punch, Power Wall, Spirit Pulse, and Finish Breaker** after excluding all records with prior current-evidence audit registrations.
- [x] Added four current-evidence audits plus `docs/data/skill-research-batches/skill-batch-428.json` and the Batch 428 thin-frontier mechanics audit.
- [x] Rechecked current Xenoverse 2-specific mechanics, acquisition endpoints, resource costs, hit/sequence behavior, and bounded numeric claims against dedicated skill references and independent corroboration where available.
- [x] Synchronized all four records into both canonical skill datasets and refreshed their current-scope verification date to 2026-09-26.
- [x] Registered the Batch 428 research record, thin-frontier audit, and four skill audits in `docs/data/pq-cross-domain-index.json`.
- [x] Validated **474/474** canonical/index IDs with **0 missing / 0 extra**.
- [ ] CI/build remains unverified; no workflow success is claimed.
- [x] **Exact next:** run another fresh unaudited mechanics frontier census excluding Batch 428 and every prior current-evidence-audited record, then continue the canonical research/synchronization cycle.

### 2026-09-26 continuation — Skill Research Batch 427 completed

- [x] Fresh unaudited frontier census selected **Hyper Drain, Death Ball, Super Saiyan God Super Saiyan (Evolved), Evil Rise Strike**.
- [x] Added four current-evidence audits and `docs/data/skill-research-batches/skill-batch-427.json`.
- [x] Rechecked current Xenoverse 2 mechanics, acquisition endpoints, resource costs, and bounded numeric claims using dedicated skill references plus independent corroboration where available.
- [x] Synchronized all four records into both canonical skill datasets.
- [x] Registered all Batch 427 artifacts in `docs/data/pq-cross-domain-index.json`.
- [x] Validated **474/474** canonical/index IDs with **0 missing / 0 extra**.
- [ ] CI/build remains unverified; no workflow success is claimed.
- [x] **Exact next:** run another fresh unaudited mechanics frontier census and continue the canonical research/synchronization cycle.

### 2026-09-26 continuation — Skill Research Batch 426 completed

- [x] Fresh unaudited frontier census selected **Elite Beam, Sphere of Destruction, Crusher Ball, Do or Die** after excluding prior current-evidence audit registrations.
- [x] Added four current-evidence audit files and `docs/data/skill-research-batches/skill-batch-426.json`.
- [x] Rechecked current Xenoverse 2-specific mechanics, acquisition endpoints, resource costs, and bounded numeric claims against dedicated skill references and independent technique documentation.
- [x] Synchronized all four records into `docs/data/skills.json` and `docs/data/skills-index.json`.
- [x] Registered all Batch 426 artifacts in `docs/data/pq-cross-domain-index.json`.
- [x] Validated **474/474** canonical/index IDs with **0 missing / 0 extra**.
- [ ] CI/build remains unverified; no workflow success is claimed.
- [x] **Exact next:** run another fresh unaudited mechanics frontier census and continue canonical research/synchronization without inventing unsupported values.

### 2026-09-26 continuation — Skill Research Batch 425 completed

- [x] Fresh canonical frontier census found the shortest four records without a prior current-evidence audit: **DIE DIE Missile Barrage, Victory Cannon, Maiden Blast, Darkness Eye Beam**.
- [x] Added four current-evidence audit records plus `docs/data/skill-research-batches/skill-batch-425.json`.
- [x] Evidence review incorporated current Xenoverse 2 skill/mentor documentation and historical Steam patch-note context where relevant; historical balance changes are kept separate from timeless current-state claims.
- [x] Synchronized all four Batch 425 mechanics/provenance updates into both `docs/data/skills.json` and `docs/data/skills-index.json`.
- [x] Registered the Batch 425 research record and all four audits in `docs/data/pq-cross-domain-index.json`.
- [x] Validated canonical/index parity: **474 canonical records / 474 index records / 0 missing IDs / 0 extra IDs**.
- [ ] CI/build status remains unverified; no workflow success is claimed.
- [x] **Exact next:** run a fresh unaudited mechanics frontier census excluding Batch 425 and all earlier audited records, then research and synchronize the next canonical batch. Continue preserving unresolved frame data, hidden interactions, probabilities, and patch-independent balance boundaries instead of inventing values.

### 2026-09-26 continuation — Batch 424 large-blob recovery and partial canonical synchronization

- [x] Recovered the safe large-blob path: `fetch_blob` successfully returned the full 1.25 MB canonical `skills.json` blob and the full projection blob, allowing complete-file edits without reconstructing either dataset.
- [x] Synchronized **Full Power Charge** into both `docs/data/skills.json` and `docs/data/skills-index.json`; refreshed its verification date to 2026-09-26 and added the Batch 424 evidence/provenance note.
- [x] Validated canonical/index parity after the large-blob write: **474/474 IDs**, zero missing, zero extra.
- [x] Confirmed the three other Batch 424 evidence names — **Burning Spin, Final Shine Attack, Savage Strike** — do not currently exist as exact canonical records in the 474-record skill dataset. Their evidence audits remain preserved, but are now explicitly marked evidence-only / pending canonical identity reconciliation rather than being falsely promoted.
- [x] Updated `skill-batch-424.json` and all four Batch 424 audit files to reflect the actual synchronization state.
- [ ] CI/build status remains unverified; no workflow success is claimed.
- [x] **Exact next:** reconcile the three evidence-only Batch 424 names against the canonical skill inventory/import sources (do not invent IDs), then continue the fresh under-audited mechanics frontier using canonical records only.

### 2026-09-26 continuation — Skill Research Batch 424 evidence layer completed

- [x] Performed a fresh current-evidence frontier check against the live cross-domain registry and selected four skills without a dedicated current-evidence audit: **Full Power Charge, Burning Spin, Final Shine Attack, and Savage Strike**.
- [x] Added four source-backed current-evidence audits plus `docs/data/skill-research-batches/skill-batch-424.json`.
- [x] Registered the Batch 424 research record and all four audits in `docs/data/pq-cross-domain-index.json`.
- [x] Preserved evidence conflicts and boundaries: Burning Spin's conflicting 300-vs-400 Ki presentation is not silently normalized; Final Shine Attack's open-ended 300+ Ki presentation is retained; exact frames, hidden interactions, probabilities, and patch-independent balance values remain unresolved where unsupported.
- [ ] Canonical `docs/data/skills.json` and projection `docs/data/skills-index.json` are **not yet synchronized** for Batch 424. The live GitHub connector currently returns zero content for these oversized blobs, so a safe complete-file rewrite is not possible without a recovered large-blob path.
- [ ] CI/build status remains unverified; no workflow success is claimed.
- [x] **Exact next:** recover a safe large-blob read/write path, synchronize the four Batch 424 mechanics/provenance updates into both canonical layers, validate canonical/index parity, then continue the next fresh frontier census excluding all records with a prior current-evidence audit.

### 2026-09-26 continuation — Skill Research Batch 420 completed

- [x] Fresh 474-record mechanics frontier census excluded Batches 396–419 and selected **Core Breaker, Destruction's Concerto: Comet, Earth Splitting Galick Gun, Eye Beam, God of Destruction's Anger, Victory Cannon, Fighting Pose D, and Darkness Rush (Melee)** as the next eight shortest genuinely under-detailed canonical mechanics records.
- [x] Enriched and synchronized canonical `docs/data/skills.json` and projection `docs/data/skills-index.json`; canonical/index remain **474/474**.
- [x] Added source-backed mechanics including Core Breaker's PQ158/Ultimate-Finish context, Comet's orb/conductor interaction, Earth Splitting Galick Gun's 23-hit beam behavior, Eye Beam's three-projectile movement behavior, God of Destruction's Anger's stamina-depleting guard break, Victory Cannon's recoil movement, Fighting Pose D's 20-second Boost Dash buff, and Darkness Rush (Melee)'s seven-hit grab/rush sequence.
- [x] Added eight Batch 420 current-evidence audits plus `docs/data/skill-research-batches/skill-batch-420.json` and registered the artifacts in `docs/data/pq-cross-domain-index.json`.
- [x] Preserved evidence boundaries: exact frames, hidden interactions, unsupported scaling, patch-independent balance values, and unresolved reward probabilities remain unresolved rather than inferred.
- [ ] CI/build status remains unverified; no workflow success is claimed.
- [x] **Exact next:** run a fresh 474-record frontier census excluding Batches 396–420 and enrich the next 4–12 shortest genuinely under-detailed canonical mechanics records, synchronizing canonical/index/provenance in the same cycle.

### 2026-09-26 continuation — Skill Research Batch 419 completed

- [x] Fresh 474-record mechanics frontier census excluded Batches 396–418 and selected **Power Rush, Super Explosive Wave, Do or Die, Masenko, Death Slicer, Mighty Explosive Wave, Time Control, Darkness Eye Beam, Evil Ray Strike, Dragon Spark, Become Giant, and Crazy Finger Shot** as the next twelve shortest genuinely under-detailed canonical mechanics records.
- [x] Enriched and synchronized canonical `docs/data/skills.json` and projection `docs/data/skills-index.json`; canonical/index remain **474/474**.
- [x] Corrected **Super Explosive Wave**'s canonical classification from Evasive to **Super**, matching its dedicated Super-variant documentation.
- [x] Added source-backed current mechanics details including documented damage/hit counts, charge/input behavior, tracking/guard-break behavior, time-stop behavior, and Become Giant's current-scope transformation modifiers where directly supported.
- [x] Added twelve Batch 419 current-evidence audits plus Batch 419 frontier/research artifacts and registered them in `docs/data/pq-cross-domain-index.json`.
- [x] Preserved evidence boundaries: exact frames, hidden interactions, patch-independent scaling, and unresolved reward probabilities remain unresolved rather than inferred.
- [ ] CI/build status remains unverified; no workflow success is claimed.
- [x] **Exact next:** run a fresh 474-record frontier census excluding Batches 396–419 and enrich the next 4–12 shortest genuinely under-detailed canonical mechanics records, synchronizing canonical/index/provenance in the same cycle.

### 2026-09-26 continuation — Skill Research Batch 416 completed

- [x] Fresh 474-record frontier census excluded Batches 396–415 and selected **Wild Hunt, Destructive Fission, Fruit of the Tree of Might, and Power Blitz** as the next four shortest genuinely under-detailed canonical mechanics records.
- [x] Expanded current Xenoverse 2-specific mechanics coverage and synchronized canonical `docs/data/skills.json` and projection `docs/data/skills-index.json` for all four.
- [x] Wild Hunt now records the four-hit uppercut/rush sequence and source-reported ~15% total damage while preserving unresolved frame/escape timing.
- [x] Destructive Fission now records the tracking Hakai orb, hit interruption, additional-input unblockable explosion, and approximately 20-second active lifetime from current evidence.
- [x] Fruit of the Tree of Might now records its 30-second power-up duration and additional-input teleport/stun behavior.
- [x] Power Blitz now records the two-hit pincer/tracking behavior and source-reported ~15% total damage.
- [x] Added Batch 416 research data, thin-frontier audit, and four current-evidence audit files; registered all artifacts in `docs/data/pq-cross-domain-index.json`.
- [x] Preserved evidence boundaries: exact frames, hidden interactions, exact scaling, and patch-independent balance values were not inferred where unresolved.
- [ ] CI/build status remains unverified; no workflow success is claimed.
- [x] **Exact next:** run a fresh 474-record frontier census excluding Batches 396–416 and enrich the next 4–12 shortest genuinely under-detailed canonical mechanics records, synchronizing canonical/index/provenance in the same cycle.

### 2026-09-25 continuation — Skill Research Batch 415 completed

- [x] Fresh live 474-record mechanics frontier census excluded Batches 396–414 and selected **God of Destruction's Wrath, Symphonic Destruction, Demon Ray, and Fighting Pose E** as the next four shortest genuinely under-detailed canonical mechanics records.
- [x] Expanded current Xenoverse 2-specific mechanics coverage and synchronized canonical `docs/data/skills.json` and projection `docs/data/skills-index.json` for all four.
- [x] Corrected **Symphonic Destruction** to the documented **Ki Blast Ultimate** classification in both canonical layers; the prior projection incorrectly labeled it Strike.
- [x] Promoted **Demon Ray**'s documented 300-Stamina use-while-hit mechanic into the canonical stamina field while retaining its PQ160 Ultimate Finish acquisition semantics.
- [x] Added Batch 415 research data, thin-frontier audit, and four current-evidence audit files; registered all artifacts in `docs/data/pq-cross-domain-index.json`.
- [x] Preserved evidence boundaries: exact frames, projectile counts, exact multipliers/scaling, hidden conditions, and patch-independent damage were not inferred.
- [ ] CI/build status remains unverified; no workflow success is claimed.
- [x] **Exact next:** run a fresh 474-record frontier census excluding Batches 396–415 and enrich the next 4–12 shortest genuinely under-detailed canonical mechanics records, synchronizing canonical/index/provenance in the same cycle.

### 2026-09-25 continuation — Skill Research Batch 414 completed

- [x] Fresh 474-record frontier census excluded Batches 396–413 and selected **Eagle Kick, Destructive Flare, Double Crush, and God of Destruction's Rampage** as the next four shortest genuinely under-detailed canonical mechanics records.
- [x] Expanded current Xenoverse 2-specific mechanics coverage and synchronized canonical `docs/data/skills.json` and projection `docs/data/skills-index.json` for all four.
- [x] Added Batch 414 research data, thin-frontier audit, and four current-evidence audit files; registered them in `docs/data/pq-cross-domain-index.json`.
- [x] Preserved evidence boundaries: exact frame data, universal scaling, armor timing, and charge timing were not inferred where unsupported.
- [ ] CI/build status remains unverified; no workflow success is claimed.
- [x] **Exact next:** run a fresh 474-record frontier census excluding Batches 396–414 and enrich the next 4–12 shortest genuinely under-detailed canonical mechanics records, synchronizing canonical/index/provenance in the same cycle.


### 2026-09-25 continuation — Skill Research Batch 413 completed

- [x] Fresh 474-record frontier census excluded Batches 396–412 and selected **Dimension Ray, Big Bang Attack, Sudden Storm, and Bending Kamehameha** as the next four shortest genuinely under-detailed canonical mechanics records.
- [x] Expanded current Xenoverse 2-specific mechanics coverage and synchronized canonical `docs/data/skills.json` and projection `docs/data/skills-index.json` for all four.
- [x] Added Batch 413 research data, thin-frontier audit, and four current-evidence audit files; registered them in `docs/data/pq-cross-domain-index.json`.
- [x] Preserved evidence boundaries: exact frame data, universal scaling, and unsupported timing values were not inferred.
- [ ] CI/build status remains unverified; no workflow success is claimed.
- [x] **Exact next:** run a fresh 474-record frontier census excluding Batches 396–413 and enrich the next 4–12 shortest genuinely under-detailed canonical mechanics records, synchronizing canonical/index/provenance in the same cycle.


### 2026-09-25 continuation — Skill Research Batch 412 completed

- [x] Fresh 474-record frontier census excluded Batches 396–411 and selected **Super Elite Combo, Super Dragon Flight, Shadow Crusher, Confusion Blade, Kai Kai, Neo Tri-Beam, Time Bullet, and Death Beam** as the next eight shortest genuinely under-detailed canonical mechanics records.
- [x] Expanded current Xenoverse 2-specific mechanics coverage and synchronized canonical `docs/data/skills.json` and projection `docs/data/skills-index.json` for all eight.
- [x] Added Batch 412 research data, thin-frontier audit, and eight current-evidence audit files; registered them in `docs/data/pq-cross-domain-index.json`.
- [x] Preserved evidence boundaries: exact frame data, universal scaling, hidden targeting rules, and unsupported timing values were not inferred.
- [ ] CI/build status remains unverified; no workflow success is claimed.
- [x] **Exact next:** run a fresh 474-record frontier census excluding Batches 396–412 and enrich the next 4–12 shortest genuinely under-detailed canonical mechanics records, synchronizing canonical/index/provenance in the same cycle.


### 2026-09-25 continuation — Skill Research Batch 411 completed

- [x] Fresh 474-record frontier census excluded Batches 396–410 and selected **Ki Explosion, Demonic Destruction, Dragon Thunder, Beast, Blazing Attack, Super Destructo-Disc, Trap Shooter, and Explosive Buu Buu Punch** as the next eight shortest genuinely under-detailed canonical mechanics records.
- [x] Expanded current Xenoverse 2-specific mechanics coverage and synchronized canonical `docs/data/skills.json` and projection `docs/data/skills-index.json` for all eight.
- [x] Added Batch 411 research data, thin-frontier audit, and eight current-evidence audit files; registered them in `docs/data/pq-cross-domain-index.json`.
- [x] Preserved evidence boundaries: exact frame data, universal damage scaling, hidden thresholds, armor timing, and reward probabilities were not inferred where unsupported.
- [ ] CI/build status remains unverified; no workflow success is claimed.
- [x] **Exact next:** run a fresh 474-record frontier census excluding Batches 396–411 and enrich the next 4–12 shortest genuinely under-detailed canonical mechanics records, synchronizing canonical/index/provenance in the same cycle.


### 2026-09-25 continuation — Skill Research Batch 410 completed

- [x] Fresh 474-record mechanics frontier census excluded completed Batches 396–409 and selected **Last Emperor, Special Beam Cannon (Beast), Shine Shot, and Hyper Movement** as the next four short genuinely under-detailed canonical records.
- [x] Deepened current Xenoverse 2-specific mechanics coverage and synchronized canonical `docs/data/skills.json` and projection `docs/data/skills-index.json` for all four.
- [x] Added Batch 410 research data, thin-frontier audit, and four current-evidence audits; registered all artifacts in `docs/data/pq-cross-domain-index.json`.
- [x] Preserved evidence boundaries: exact frames, hidden low-health thresholds, reward probabilities, charge timing, and patch-independent damage values were not inferred.
- [ ] CI/build status remains unverified; no workflow success is claimed.
- [x] **Exact next:** run a fresh 474-record frontier census excluding Batches 396–410 and enrich the next 4–12 shortest genuinely under-detailed canonical mechanics records, synchronizing canonical/index/provenance in the same cycle.


### 2026-09-25 continuation — Skill Research Batch 409 completed

- [x] Fresh 474-record mechanics frontier census excluded completed Batches 396–408 and selected **Milky Cannon, Side Bridge, Dragon Fist, Psycho Barrier, Death Psycho Bomb, Double Death Slicer, Kill Driver, and Scatter Kamehameha** as the next eight shortest genuinely under-detailed canonical records.
- [x] Expanded current Xenoverse 2-specific mechanics boundaries for all eight and synchronized both canonical skill layers.
- [x] Added Batch 409 research data and registered it in the cross-domain index.
- [x] Preserved evidence boundaries: exact frame data, precise charge scaling, unresolved damage variation, and hidden conditions were not inferred.
- [ ] CI/build status remains unverified.
- [ ] **Exact next:** run a fresh 474-record frontier census excluding Batches 396–409 and enrich the next 4–12 shortest genuinely under-detailed canonical mechanics records, synchronizing canonical/index/provenance in the same cycle.


### 2026-09-25 continuation — Skill Research Batch 408 completed

- [x] Fresh 474-record mechanics frontier census excluded completed Batches 396–407 and selected **Perfect Shot, Celestial Wave, Super Guard, Spirit Bomb, Afterimage, Burst Reflection, S.S. Deadly Bomber, and Thunder Flash** as the next eight shortest genuinely under-detailed canonical records.
- [x] Expanded current Xenoverse 2-specific mechanics boundaries for all eight and synchronized both canonical skill layers (`docs/data/skills.json` and `docs/data/skills-index.json`).
- [x] Added Batch 408 research data, thin-frontier audit, and eight current-evidence audit files.
- [x] Registered Batch 408 and all eight per-skill audits in `docs/data/pq-cross-domain-index.json`.
- [x] Preserved evidence conflicts and limits: Celestial Wave's reward-tier conflict remains explicit; no unsupported frame data, patch-independent balance values, hidden gates, or drop probabilities were inferred.
- [ ] CI/build status remains unverified; no workflow success is claimed.
- [ ] **Exact next:** run a fresh 474-record frontier census excluding Batches 396–408 and enrich the next 4–12 shortest genuinely under-detailed canonical mechanics records, synchronizing canonical/index/provenance in the same cycle.


### 2026-09-25 continuation — Skill Research Batch 399 completed

- [x] Fresh 474-record frontier census excluded Batches 396–398 and selected **Sonic Bomb, Seagull Combination, Death Crasher, Fighting Pose F, Super Dragon Flight**.
- [x] Refreshed canonical mechanics/provenance in both `docs/data/skills.json` and `docs/data/skills-index.json` for all five.
- [x] Added Batch 399 and five current-evidence audits; the Super Dragon Flight audit was finalized through the Git object/tree path after the contents wrapper rejected a new-file request without a SHA.
- [x] Registered Batch 399 and all five audits in `docs/data/pq-cross-domain-index.json`.
- [x] Evidence remained bounded: Sonic Bomb's PQ105 Basic Reward placement is retained despite historical conflicting reports; Seagull Combination's optional unblockable branch, Death Crasher's charge scaling, Fighting Pose F's 12-second Hyper Armor/Stamina behavior, and Super Dragon Flight's PQ31 Basic Reward placement were documented without inventing unresolved frame or probability values.
- [ ] CI/build status remains unverified; no workflow success is claimed.
- [ ] **Exact next:** run another 474-record frontier census excluding Batches 396–399 and enrich the next least-detailed canonical records, synchronizing both canonical layers and cross-domain provenance in the same cycle.


### 2026-09-25 continuation — Skill Research Batch 398 completed

- [x] Fresh 474-record thin-frontier census excluded completed Batches 396–397 and selected **Chaos Shot, Innocence Cannon, Zigzag Express, Burst Charge, Sauzer Blade**.
- [x] Refreshed current Xenoverse 2 mechanics/acquisition boundaries in both canonical skill layers for all five records.
- [x] Added `docs/data/skill-research-batches/skill-batch-398.json` and five current-evidence audit files.
- [x] Registered Batch 398 and all five audits in `docs/data/pq-cross-domain-index.json`.
- [x] Preserved bounded evidence policy: no unsupported frame data or reward probabilities were promoted; Zigzag Express's Male Majin restriction and PQ85 route, Burst Charge's short-burst behavior, Chaos Shot's 2/9-hit branches, Innocence Cannon's 30%/launch behavior, and Sauzer Blade's five-hit/weak-Ki-Blast cancellation behavior were documented from current references. citeturn1search1turn1search2turn1search3turn1search0turn1search9
- [ ] CI/build status remains unverified; no workflow success is claimed.
- [ ] **Exact next:** run another 474-record frontier census excluding completed Batch 398 targets, then enrich the next shortest genuinely under-detailed records and synchronize both canonical layers.


### 2026-09-25 continuation — Skill Research Batch 397 completed

- [x] Fresh thin-frontier census selected the seven shortest mechanics records after Batch 396: **Kai Kai, Psycho Escape, Supernova Cooler, Super Elite Combo, Energy Dome, Eye Beam, One-Handed Kamehameha mk.II**.
- [x] Added `docs/data/skill-research-batches/skill-batch-397.json` and seven current-evidence audit files.
- [x] Refreshed canonical mechanics/provenance in both `docs/data/skills.json` and `docs/data/skills-index.json` for all seven records.
- [x] Canonical/index parity rechecked: **474/474**, zero missing IDs in either direction; the seven target mechanics strings match exactly between layers.
- [x] Registered Batch 397 and all seven audit files in `docs/data/pq-cross-domain-index.json`.
- [x] Evidence policy remained bounded: no unsupported frame data, hidden prerequisites, reward probabilities, or unverified balance values were introduced. Psycho Escape community timing observations remain explicitly separated from canonical numeric claims.
- [ ] CI/build status remains unverified; no workflow success is claimed.
- [ ] **Exact next:** run the next 474-record thin-frontier census, excluding the completed Batch 397 targets, and continue source-backed enrichment/canonical synchronization with the next least-detailed records.


### 2026-09-25 continuation — Batch 396 canonical synchronization completed

- [x] Recovered the large canonical blobs through the Git object API after the earlier contents-path limitation; the previous handoff's zero-length-read limitation is resolved for this cycle.
- [x] Promoted **Fighting Pose B, Fighting Pose D, Fighting Pose G, Fighting Pose I, and Fighting Pose J** into `docs/data/skills.json`.
- [x] Synchronized the same five IDs and mechanics into `docs/data/skills-index.json`.
- [x] Canonical/index parity validation passed: **474/474 records**, zero missing IDs in either direction, zero duplicate skill IDs in the checked sets.
- [x] Added `docs/data/skill-batch-396-canonical-sync-audit-2026-09-25.json` documenting the promotion and validation.
- [x] Batch 396 research artifacts and all five current-evidence audits remain registered in the cross-domain index.
- [ ] CI/build status is still unverified; no workflow success is claimed.
- [ ] **Exact next:** run a fresh thin-frontier census over all 474 canonical skill records, identify the next shortest/least-enriched mechanics records, then perform another bounded evidence pass and synchronize both canonical layers in the same cycle where safely possible.


### 2026-09-25 cycle completion — Skill Batch 396 research-layer mechanics enrichment

- [x] Fresh post-Batch-395 frontier work continued with five thin Fighting Pose records: **Fighting Pose B, Fighting Pose D, Fighting Pose G, Fighting Pose I, Fighting Pose J**.
- [x] Added five current-evidence audits under `docs/data/` and `docs/data/skill-research-batches/skill-batch-396.json`.
- [x] Added and registered `docs/data/skill-batch-396-thin-frontier-mechanics-audit-2026-09-25.json` plus all five per-skill audits and Batch 396 in `docs/data/pq-cross-domain-index.json`.
- [x] Current evidence confirms B/D/G/I core Power Up identities, 0-Ki cost, effects, and documented acquisition context; J remains deliberately bounded where the current source set does not justify an exact multiplier/duration.
- [x] No unsupported reward probabilities, hidden prerequisites, frame data, or patch-independent balance claims were promoted.
- [ ] **Canonical synchronization remains pending:** the GitHub connector currently returns zero-length content for the large `docs/data/skills.json` and `docs/data/skills-index.json` files, so no unsafe whole-file replacement was attempted and no canonical sync is falsely claimed.
- [ ] CI remains unverified; no workflow success is claimed.
- [ ] **Exact next:** safely synchronize Batch 396 mechanics into canonical/index skill records when a writable large-file path is available; validate canonical/index parity, then continue the next genuinely thin post-Batch-396 frontier.


### 2026-09-25 cycle completion — Batch 52 PQ78-PQ80 verification

- [x] Promoted **Dust Attack**, **Mighty Explosive Wave**, and **Dimensional Hole** to `verified_current_scope` in `docs/data/skill-research-batches/skill-batch-52.json`.
- [x] Added current-evidence audits for all three skills under `docs/data/`.
- [x] Registered all three audits in `docs/data/pq-cross-domain-index.json`.
- [x] Dust Attack: corroborated as the PQ78 Super Skill; reward RNG/Ultimate-Finish semantics remain unresolved.
- [x] Mighty Explosive Wave: corroborated as the PQ79 100-Ki Ki Blast Super; distinguished from Jiren (Full Power)'s separate Evasive variant.
- [x] Dimensional Hole: corroborated as the PQ80 0-Ki Ki Blast counter Super; documented the Basic Ki Blast absorption/portal-return behavior.
- [x] Validation: parsed Batch 52 and cross-domain index after writes; audit registrations resolve to the newly created files.
- [ ] CI remains unverified; no workflow success is claimed.
- [ ] **Next priority:** continue exhaustive skill research beyond Batch 52, preserving cross-domain PQ ↔ skill links and bounded provenance/reward semantics.

### 2026-09-25 cycle completion — Ki Explosion current-evidence provenance promotion

- [x] Added `docs/data/skill-ki-explosion-current-evidence-audit-2026-09-25.json`.
- [x] Promoted **Ki Explosion** in Skill Research Batch 52 to `verified_current_scope`.
- [x] Confirmed current Xenoverse 2-specific 100-Ki Ki Blast Super identity, PQ77 endpoint, short-range explosion, and hold-to-prolong behavior; preserved the historical 200→100 Ki change from Bandai Namco's DLC 2 announcement.
- [x] Added independent PQ77 acquisition discussion while keeping Ultimate-Finish/guarantee semantics unresolved and avoiding unsupported drop probabilities.
- [x] Registered the current-evidence audit in `docs/data/pq-cross-domain-index.json`.
- [x] Validation: parsed Batch 52 and the cross-domain index; confirmed the Ki Explosion record is promoted and the audit registration resolves to the existing file.
- [ ] CI remains unverified; no workflow success is claimed.
- [x] **Exact next:** continue Batch 52 with **Dust Attack**, then **Mighty Explosive Wave** and **Dimensional Hole**, using the same bounded current-evidence policy.

[object Object]
### 2026-09-25 completion — full skill endpoint parity current-baseline correction
- [x] Corrected the current full endpoint parity audit from the superseded 469-record union to the verified current **470/470** union.
- [x] Recorded current counts: 239 PQ-linked unique skills, 230 unique non-PQ endpoint targets, 470 endpoint-union skills, 0 uncovered IDs.
- [x] Updated the cross-link contract and registered the correction.
- [x] Preserved historical 469/465 snapshots and made no relationship or identity changes.
- [ ] CI remains unverified.
- [ ] **Exact next:** continue remaining current-facing consumer parity or the next genuinely unresolved source-backed provenance target.

### 2026-09-25 completion — Super Soul 034 current community-evidence refresh
- [x] Added a bounded evidence audit for Super Soul 034 (PQ186 reward identity plus current community mechanics lead).
- [x] Registered the audit in the cross-domain index and preserved explicit unresolved mechanics/Limit Burst fields.
- [x] No relationship or canonical identity changes; no historical snapshot rewritten.
- [ ] CI remains unverified.
- [ ] **Exact next:** continue the remaining source-backed P1 provenance/data queue with direct Xenoverse 2-specific evidence; do not promote mechanics from community reports alone.


### 2026-09-25 completion — Skill Research Batch 339
- [x] Added Batch 339 for Psycho Escape, Justice Pose, and Kaioken acquisition/mechanics reconciliation.
- [x] Preserved existing canonical identities and relationships; no unsupported drop rates or reward gates added.
- [x] Registered the batch in the cross-domain index.
- [ ] CI remains unverified.
- [ ] **Exact next:** continue the remaining source-backed P1 provenance/data queue with the next under-enriched canonical record.


### 2026-09-25 completion — Canonical skill provenance normalization
- [x] Promoted Ice Cannon to `verified_current_scope` on direct current Xenoverse 2 evidence.
- [x] Corrected x10 Kamehameha canonical source-label capitalization/wording.
- [x] Preserved unresolved probability/prerequisite fields.
- [ ] CI remains unverified.
- [ ] **Exact next:** continue the remaining under-enriched canonical skill provenance queue using direct current Xenoverse 2 evidence.


### 2026-09-25 completion — Skill Research Batch 340
- [x] Added Batch 340 for Assault Rain and Blue Hurricane Expert Mission provenance/mechanics promotion.
- [x] Promoted both canonical records to `verified_current_scope` with directly supported acquisition, cost, classification, and mechanics fields.
- [x] Registered Batch 340 in the cross-domain index.
- [x] Preserved unresolved drop/guarantee conditions and made no unsupported relationship changes.
- [ ] CI remains unverified.
- [ ] **Exact next:** continue the remaining under-enriched canonical skill provenance queue.


### 2026-09-25 completion — Skill Research Batch 341
- [x] Added Batch 341 for Dead End Bullet provenance/mechanics promotion.
- [x] Promoted Dead End Bullet to `verified_current_scope` with supported EM08 acquisition, 300-Ki cost, classification, and mechanics.
- [x] Registered Batch 341 in the cross-domain index.
- [x] Preserved unresolved drop/guarantee conditions.
- [ ] CI remains unverified.
- [ ] Exact next: continue the remaining partially verified/under-enriched canonical skill provenance queue.


### 2026-09-25 completion — Last Emperor current-evidence provenance refresh
- [x] Added a bounded current-evidence audit for **Last Emperor** and registered it in the cross-domain index.
- [x] Refreshed Batch 52 provenance/evidence for Last Emperor and strengthened the 0-Ki, low-health, one-use mechanics boundary.
- [x] Preserved unresolved PQ71 reward-slot/probability and Ultimate Finish semantics; no unsupported acquisition gate or numeric combat value was added.
- [ ] CI remains unverified.
- [ ] **Exact next:** continue the remaining partially verified/under-enriched canonical skill provenance queue with a target where direct current Xenoverse 2 evidence can promote a canonical field.


### 2026-09-25 completion — Requiem of Destruction current-evidence provenance refresh
- [x] Added a bounded current-evidence audit for **Requiem of Destruction** and registered it in the cross-domain index.
- [x] Refreshed Batch 316 with current 300-Ki Ki Blast Ultimate, PQ106, Super Pack 2, and partner-customization evidence.
- [x] Preserved the conflicting Basic Reward vs. reported Ultimate-Finish semantics; no unsupported reward gate or drop probability was added.
- [ ] CI remains unverified.
- [ ] **Exact next:** continue the remaining partially verified/under-enriched skill provenance queue.


### 2026-09-25 completion — Buu Buu Ball current-evidence provenance promotion
- [x] Added the current-evidence audit for **Buu Buu Ball** and registered it in the cross-domain index.
- [x] Promoted Batch 54's research record to `verified_current_scope` for classification, 300-Stamina cost, Majin restriction, and PQ88 endpoint.
- [x] Preserved unresolved Ultimate-Finish/drop semantics; no unsupported probability or guarantee was added.
- [ ] CI remains unverified.
- [ ] **Exact next:** continue the remaining partially verified/under-enriched skill provenance queue.


### 2026-09-25 completion — Atomic Blast current-evidence provenance promotion
- [x] Added the current-evidence audit for **Atomic Blast** and registered it in the cross-domain index.
- [x] Promoted Batch 54's research record to `verified_current_scope` for identity, 100-Ki cost, Ki Blast Super classification, PQ87 endpoint, and charge behavior.
- [x] Preserved unresolved reward-tier/drop semantics; no unsupported requirement or probability was added.
- [ ] CI remains unverified.
- [ ] **Exact next:** continue the remaining partially verified/under-enriched skill provenance queue.


### 2026-09-25 completion — III Bomber current-evidence provenance promotion
- [x] Added current-evidence audit for III Bomber and registered it in the cross-domain index.
- [x] Promoted Batch 54 research status to `verified_current_scope` for classification, 100-Ki cost, Majin CaC restriction, PQ90 endpoint, and documented mechanics.
- [x] Preserved unresolved reward probability and Ultimate-Finish semantics.
- [ ] CI remains unverified.
- [x] **Exact next:** continue with Final Kamehameha and the remaining under-enriched Batch 54 provenance queue.


### 2026-09-25 completion — Final Kamehameha current-evidence provenance promotion
- [x] Added current-evidence audit and registered it in the cross-domain index.
- [x] Promoted Batch 54 Final Kamehameha to `verified_current_scope` for classification, 500-Ki cost, PQ91 endpoint, current alternate acquisition routes, and 22-hit beam mechanics.
- [x] Preserved unresolved Ultimate-Finish/drop-probability semantics.
- [ ] CI remains unverified.
- [x] **Exact next:** continue the remaining under-enriched Batch 54/provenance queue.


### 2026-09-25 completion — Counter Burst current-evidence provenance promotion
- [x] Added current-evidence audit and registered it in the cross-domain index.
- [x] Promoted Batch 52 Counter Burst to `verified_current_scope` for classification, 100-Ki cost, PQ75 endpoint, six-hit counter mechanics, and partner-customization context.
- [x] Preserved unresolved reward/drop semantics.
- [ ] CI remains unverified.
- [x] **Exact next:** continue the remaining under-enriched Batch 52 skill provenance queue.


### 2026-09-25 completion — Last Emperor current-evidence provenance promotion
- [x] Completed and refreshed the Last Emperor current-evidence audit.
- [x] Promoted Batch 52 Last Emperor to `verified_current_scope` for classification, 0-Ki cost, low-health/single-use mechanics, PQ71 provenance, and bounded beam evidence.
- [x] Preserved unresolved reward/drop semantics.
- [ ] CI remains unverified.
- [x] **Exact next:** continue Batch 52 with Burst Kamehameha.


### 2026-09-25 completion — Burst Kamehameha current-evidence provenance promotion
- [x] Promoted Batch 52's **Burst Kamehameha** record to `verified_current_scope` using current Xenoverse 2-specific skill evidence and independent PQ72 reward/drop discussion.
- [x] Confirmed Ki Blast Super classification, 100-Ki initial cost plus a second 100-Ki extension input, PQ72 endpoint, and multi-hit beam behavior.
- [x] Preserved unresolved Ultimate-Finish/drop semantics; no unsupported numeric probability or gate was added.
- [x] Registered the current-evidence audit in `docs/data/pq-cross-domain-index.json`.
- [ ] CI remains unverified.
- [x] **Exact next:** continue Batch 52 with **Psychic Move** and then the next remaining under-enriched record where direct current Xenoverse 2 evidence can promote a canonical research field.


### 2026-09-25 cycle completion — Psychic Move current-evidence provenance promotion
- [x] Promoted **Psychic Move** in Skill Research Batch 52 to `verified_current_scope` using current Xenoverse 2-specific skill evidence plus independent PQ73 reward/drop reports.
- [x] Confirmed Strike Evasive classification, 300 Stamina cost, CaC usability, PQ73 endpoint, teleport-behind behavior, short-range shockwave, knockback, and approximately 5% documented damage.
- [x] Preserved unresolved reward semantics: no Ultimate-Finish-only requirement or numeric drop probability was inferred.
- [x] Added and registered `docs/data/skill-psychic-move-current-evidence-audit-2026-09-25.json`.
- [x] Validation: parsed Batch 52 and the cross-domain index and confirmed the promoted record and audit registration.
- [ ] CI remains unverified; no workflow success is claimed.
- [x] **Exact next:** continue Batch 52 with **Final Pose**, applying the same bounded current-evidence policy.


### 2026-09-25 cycle completion — Final Pose current-evidence provenance promotion
- [x] Promoted **Final Pose** in Skill Research Batch 52 to `verified_current_scope` using current Xenoverse 2-specific skill evidence plus PQ74/reward corroboration.
- [x] Confirmed Power Up Evasive classification, **200 Stamina** current XV2-specific value, close-range shockwave, knockback, approximately 2% documented damage, and temporary basic-attack increase lasting about 11.5–12 seconds.
- [x] Preserved the historical **300-Stamina discrepancy** instead of silently overwriting it; the current XV2-specific 200 value is canonical.
- [x] Added and registered `docs/data/skill-final-pose-current-evidence-audit-2026-09-25.json`.
- [x] Preserved unresolved reward probability/guarantee semantics.
- [x] Validation: parsed Batch 52 and the cross-domain index and confirmed the promoted record and audit registration.
- [ ] CI remains unverified; no workflow success is claimed.
- [x] **Exact next:** continue Batch 52 with **Counter Burst**, applying the same bounded current-evidence policy.


### 2026-09-25 cycle completion — Counter Burst current-evidence audit
- [x] Revalidated **Counter Burst** in Skill Research Batch 52 as `verified_current_scope`.
- [x] Confirmed 100 Ki Ki Blast Super classification, Ki-counter shield behavior, stronger returned blast, six-hit counter-projectile documentation, PQ75 acquisition, and Partner Customization context.
- [x] Preserved unresolved exact stamina expenditure and reward-rate/guarantee semantics rather than inferring them.
- [x] Confirmed current-evidence audit registration in `docs/data/pq-cross-domain-index.json`.
- [x] Validation completed against the live Batch 52 record and cross-domain index.
- [ ] CI remains unverified; no workflow success is claimed.
- [x] **Exact next:** continue Batch 52 with **Warp Kamehameha**.


### 2026-09-25 cycle completion — Warp Kamehameha current-evidence provenance promotion
- [x] Promoted **Warp Kamehameha** in Skill Research Batch 52 to `verified_current_scope` using current Xenoverse 2-specific skill evidence and PQ76 corroboration.
- [x] Confirmed **400 Ki**, Ki Blast Ultimate classification, teleport-to-locked-target behavior, tracking/beam characteristics, knockback, and approximately 30% damage over 24 hits.
- [x] Confirmed PQ76 — **Eternal Rival** as the acquisition endpoint and preserved Partner Customization context.
- [x] Preserved the historical **300-Ki discrepancy** from the older general Xenoverse reference rather than silently overwriting it.
- [x] Added and registered `docs/data/skill-warp-kamehameha-current-evidence-audit-2026-09-25.json`.
- [x] Preserved unresolved numeric drop-probability semantics.
- [x] Validation completed against live Batch 52 and cross-domain registration.
- [ ] CI remains unverified; no workflow success is claimed.
- [x] **Exact next:** continue Batch 52 with **Ki Explosion**.

### 2026-09-25 Batch 54 PQ98-PQ100 continuation
- [x] Add current-evidence audit for Dimension Ray.
- [x] Add current-evidence audit for Emperor's Edge.
- [x] Add current-evidence audit for X100 Big Bang Kamehameha.
- [x] Synchronize the three audits into canonical Batch 54 records and register PQ ↔ skill cross-domain links.



### 2026-09-25 completion — Neo Wolf Fang Fist current-evidence provenance promotion
- [x] Promoted Batch 54 **Neo Wolf Fang Fist** to `verified_current_scope` with current 100–700 Ki, Strike Super, 9–33 hit continuable-rush, and PQ86 evidence.
- [x] Added and registered the dedicated current-evidence audit.
- [x] Preserved historical resource-behavior reports without using them to override current evidence; reward probability and hidden Ultimate-Finish semantics remain unresolved.
- [ ] CI remains unverified.
- [x] **Exact next:** continue the remaining source-backed P1 provenance queue with the next under-enriched canonical skill.


### 2026-09-25 completion — Maiden Burst current-evidence provenance promotion
- [x] Promoted Batch 54 **Maiden Burst** to `verified_current_scope` with current 300-Stamina Ki Blast Evasive, PQ92, and mechanics evidence.
- [x] Reconciled and registered the existing current-evidence audit.
- [x] Preserved the acquisition-history conflict and unresolved reward probability/hidden-gate semantics.
- [ ] CI remains unverified.
- [x] **Exact next:** continue the remaining source-backed P1 provenance queue with the next under-enriched canonical skill.


### 2026-09-25 completion — Batch 54 PQ94/PQ95/PQ97 provenance promotion
- [x] Promoted **Bluff Kamehameha**, **Drain Field**, **Charged Ki Wave**, and **Phantom Fist** to `verified_current_scope`.
- [x] Added and registered four current-evidence audits.
- [x] Preserved unresolved reward probability/Ultimate-Finish semantics and historical conflicts.
- [ ] CI remains unverified.
- [x] **Exact next:** continue the remaining under-enriched canonical skill provenance queue after live census.


### 2026-09-25 completion — Batch 54 PQ86-PQ100 full provenance census
- [x] Promoted **Absolute Zero** to `verified_current_scope`.
- [x] Set all 15 Batch 54 records to explicit `research_status: enriched` without altering unresolved reward semantics.
- [x] Added and registered the Absolute Zero current-evidence audit.
- [ ] CI remains unverified.
- [x] **Exact next:** fresh repository-wide census for the next under-enriched/partially-verified canonical skill batch outside Batch 54.


### 2026-09-25 completion — Expert Mission skill provenance promotion
- [x] Promoted **Death Meteor**, **Death Wave**, **Hellzone Grenade**, and **Murder Grenade** to `verified_current_scope`.
- [x] Added and registered four current-evidence audits.
- [x] Preserved unresolved Expert Mission reward probability/guarantee semantics.
- [ ] CI remains unverified.
- [x] **Exact next:** continue with **Shocking Death Ball** and **Spirit Sword**, then the next partially verified Expert Mission skill.


### 2026-09-25 completion — Expert Mission EM04/06/14/17 provenance promotion
- [x] Promoted **Super Destructo-Disc**, **Supernova**, **Shocking Death Ball**, and **Spirit Sword** to `verified_current_scope`.
- [x] Added and registered four current-evidence audits.
- [x] Synchronized canonical skill and Expert Mission acquisition projections.
- [x] Preserved unresolved reward probability/first-clear/UF semantics and historical reward conflicts.
- [ ] CI remains unverified.
- [x] **Exact next:** continue the remaining partially verified Expert Mission records, starting with **Dead End Bullet**, **Assault Rain**, **Super Electric Strike**, and **Angry Explosion**.


### 2026-09-25 cycle validation — Expert Mission acquisition live census
- Live census after editing: **18** EM03-20 non-tutorial acquisition records; **8 verified_current_scope**, **10 partially_verified**; **18 exact drop rates unresolved**.
- Canonical/index parity validated for the eight promoted skills: all show `verified_current_scope`, `research_status: enriched`, and `last_verified: 2026-09-25`.
- Exact next: promote the next bounded tranche beginning with **Dead End Bullet, Assault Rain, Super Electric Strike, and Angry Explosion**.


### 2026-09-25 cycle completion — Expert Mission EM08-12 acquisition projection reconciliation
- Live census before editing: 18 EM03-20 non-tutorial acquisition records; 8 verified, 10 partially verified.
- [x] Reconciled **Dead End Bullet**, **Assault Rain**, **Super Electric Strike**, and **Angry Explosion** from stale `partially_verified` acquisition projections to `verified_current_scope`.
- [x] Closed Skill Research Batch 335 (EM09-12) and registered four dedicated current-evidence audits.
- [x] Evidence confirms current 300-Ki Ki Blast Ultimate classification and EM08/09/11/12 endpoints; maintained Expert Mission reward evidence corroborates the mission reward endpoints.
- [x] Preserved unresolved exact reward probability, first-clear guarantee, and unsupported Ultimate-Finish-only semantics.
- [x] Validation: live acquisition census is now **12 verified / 6 partially verified / 18 unresolved exact drop rates**; canonical records for all four were already `verified_current_scope`, so this cycle closes the projection parity gap.
- [ ] CI remains unverified; no workflow success is claimed.
- [x] **Exact next:** continue the remaining six partially verified Expert Mission records: **Dead End Rain, Blue Hurricane, Super Spirit Bomb, Focus Flash, Tail Slicer, Data Input**, beginning with a live canonical/source census.


### 2026-09-25 cycle completion — Expert Mission EM13/15/16/18/19/20 provenance closure
- Live census before editing: 18 EM03-20 non-tutorial acquisition records; 12 verified / 6 partially verified.
- [x] Promoted **Dead End Rain**, **Blue Hurricane**, **Super Spirit Bomb**, **Focus Flash**, **Tail Slicer**, and **Data Input** to `verified_current_scope` in the canonical skill layer and acquisition projection.
- [x] Added six current-evidence audits and registered all six cross-domain links.
- [x] Existing repository evidence confirms current classifications/costs and EM13/15/16/18/19/20 endpoints; Data Input's historical DLC/update provenance conflict remains preserved.
- [x] Preserved unresolved exact drop probability, first-clear guarantee, and unsupported Ultimate-Finish-only semantics.
- [x] Live validation after editing: **18 verified / 0 partially verified / 18 total**, with exact drop rates unresolved.
- [ ] CI remains unverified; no workflow success is claimed.
- [x] **Exact next:** perform a fresh repository-wide census for the next under-enriched/partially-verified canonical skills outside the now-closed EM03-20 acquisition tranche; prioritize deterministic index/provenance gaps before broad descriptive expansion.


### 2026-09-25 cycle completion — Victory Rush cross-domain audit registration repair
- Live census before editing: canonical skill baseline **470**; Batch 54 **Victory Rush** was already `verified_current_scope` and its dedicated current-evidence audit already existed, but the audit was missing from `docs/data/pq-cross-domain-index.json`.
- [x] Revalidated current evidence: Victory Rush is a **300-Ki Strike Ultimate** acquired from **PQ89 — Super-Super Ultimate Series of Battles!**; current documentation supports the teleporting 13-hit rush ending in an axe kick.
- [x] Preserved unresolved reward semantics: `ultimate_finish_required` remains `null`; no drop probability or hidden gate was inferred.
- [x] Registered `skill_victory_rush_current_evidence_audit_2026_09_25` in `docs/data/pq-cross-domain-index.json`, restoring the audit's cross-domain discoverability without changing canonical skill identity or acquisition relationship data.
- [x] Validation: parsed the updated cross-domain index; confirmed the new registration resolves exactly to `docs/data/skill-victory-rush-current-evidence-audit-2026-09-25.json`. Existing Victory Rush research/audit files remain intact.
- [ ] CI remains unverified; no workflow success is claimed.
- [x] Commit: `00657db919550b4d5b114992df14108bdbde3402`.
- [x] **Exact next:** perform the fresh repository-wide under-enriched/partially-verified census required by the handoff; prioritize the next deterministic provenance/index gap or a bounded current-evidence target outside the completed PQ86-PQ100 Batch 54 tranche.


### 2026-09-25 cycle completion — Hyper Drain / Hyper Movement / Ice Cannon / Ice Claw current-evidence promotion
- Live canonical census before promotion: **469 records**; exactly **4** remained `partially_verified | enriched`: Hyper Drain, Hyper Movement, Ice Cannon, and Ice Claw.
- [x] Added four dedicated current-evidence audits and registered all four in `docs/data/pq-cross-domain-index.json`.
- [x] Promoted all four canonical records to `verified_current_scope` and refreshed their index projections to `last_verified: 2026-09-25`.
- [x] Hyper Drain: current evidence establishes Strike Super, 100 Ki, CaC-only use, Skill Shop after Android Warfare, and 1-Stamina/2-Ki drain behavior.
- [x] Hyper Movement: current evidence establishes Strike Evasive, 200 Stamina, TP Medal Shop, teleport/punch behavior, and knockback interception use.
- [x] Ice Cannon: current evidence establishes 300-Ki Ki Blast Ultimate, Shenron-wish acquisition, five-hit freezing projectile, and approximately 3-second freeze.
- [x] Ice Claw: current evidence establishes 100-Ki Strike Super, Shenron-wish acquisition, two-hit claw attack, and blinding effect.
- [x] Refreshed Hyper Drain and Hyper Movement shop endpoint timestamps to 2026-09-25.
- [x] Validation: canonical/index parity is clean for all four; current status census is now **264 verified_current_scope + 178 verified/enriched + 27 verified/verified = 469 total**, with **0 partially_verified** canonical skills.
- [ ] CI remains unverified; no workflow success is claimed.
- [x] **Exact next:** begin the next under-enriched frontier: the **27 `verified | verified` canonical records**. Start with a fresh evidence census for **Apocalyptic Burst, Blaster Stream, Chain Destructo-Disc Barrage, and Circle Flash**, and promote/enrich only fields directly supported by current Xenoverse 2 evidence.


### 2026-09-25 cycle completion — Apocalyptic Burst / Blaster Stream / Chain Destructo-Disc Barrage / Circle Flash enrichment
- Fresh live census: **469 canonical skills**; before this cycle, **27** were `verified | verified`. The bounded target was the first four records in that frontier.
- [x] Added four dedicated current-evidence audits and registered all four in `docs/data/pq-cross-domain-index.json`.
- [x] Promoted the four from `verified` research status to `enriched`; refreshed canonical/index `last_verified` to **2026-09-25**.
- [x] Corrected a concrete stale canonical value: **Apocalyptic Burst Ki cost 500 → 300**, supported by current Xenoverse 2 skill documentation and independent Dragon Ball reference.
- [x] Apocalyptic Burst mechanics expanded: charged guard-breaking opening kick, weak-Ki-Blast cancellation aura, two follow-up kicks, finishing Ki Blast, and Evasive/Limit Burst prevention during the attack. PQ161 reward-tier conflict remains preserved.
- [x] Blaster Stream mechanics expanded: charge-dependent damage/hit count and follow-up Ki Wave; PQ148 Basic Reward and unresolved race scope remain preserved.
- [x] Chain Destructo-Disc Barrage mechanics expanded: five sequential Destructo-Discs and unblockable behavior; PQ46 Basic Reward and unresolved probability remain preserved.
- [x] Circle Flash mechanics expanded: ring projectile capture/cutscene and explosion; 300 Ki and 40% documented damage retained, while Basic-vs-Ultimate-Finish reward evidence remains explicitly conflicting.
- [x] Validation: canonical status census is now **264 verified_current_scope/enriched + 182 verified/enriched + 23 verified/verified = 469**. All four targets have current dates and enriched research status. Index records match the shared status/date fields; index intentionally does not duplicate every canonical field such as Ki cost.
- [ ] CI remains unverified; no workflow success is claimed.
- [x] **Exact next:** continue the remaining `verified | verified` frontier with **Core Breaker, Death Ball, Destruction's Concerto: Meteor, Dimension Ray**, performing the same current-evidence census and only correcting fields with direct support.


### 2026-09-25 cycle completion — Core Breaker / Death Ball / Destruction's Concerto: Meteor / Dimension Ray enrichment
- Fresh live census: **469 canonical skills**; the remaining `verified | verified` frontier was **23** after the previous cycle. This bounded batch completed the next four.
- [x] Added current-evidence audits for **Core Breaker**, **Death Ball**, and **Destruction's Concerto: Meteor**; the existing **Dimension Ray** audit was revalidated and registered.
- [x] Promoted all four to `research_status: enriched` and refreshed canonical/index `last_verified` to **2026-09-25**.
- [x] Core Breaker: retained **500 Ki Strike Ultimate**, PQ158, and the maintained **40% Ultimate-Finish bonus slot**; no narrower CaC race restriction inferred.
- [x] Death Ball: retained **400 Ki Ki Blast Ultimate**, Frieza Lesson 3 deterministic mentor acquisition, and documented tracking/18-hit mechanics; no RNG or Ultimate-Finish gate inferred.
- [x] Destruction's Concerto: Meteor: retained **100-200 Ki Ki Blast Super**, PQ106 Basic Reward, and Super Pack 2 provenance; corrected the stale skill description from Ultimate to **Super**.
- [x] Dimension Ray: retained **400 Ki Ki Blast Ultimate**, PQ98 Basic Reward, and documented 19-hit wide barrage; no drop probability or hidden gate inferred.
- [x] Validation: **264 verified_current_scope/enriched + 186 verified/enriched + 19 verified/verified = 469**. All four canonical/index shared status/date fields match and all four cross-domain audit registrations resolve.
- [ ] CI remains unverified; no workflow success is claimed.
- [x] **Exact next:** continue the remaining `verified | verified` frontier with **Gigantic Explosion, God of Destruction's Poise, Meteor Strike, Namek Finger**, using the same bounded current-evidence policy.


### 2026-09-25 cycle completion — Gigantic Explosion / God of Destruction's Poise / Meteor Strike / Namek Finger enrichment
- Fresh live census: **469 canonical skills**; the remaining `verified | verified` frontier was **19**. This bounded batch completed the next four.
- [x] Added and registered dedicated current-evidence audits for all four skills.
- [x] Promoted all four to `research_status: enriched` and refreshed canonical/index `last_verified` to **2026-09-25**.
- [x] Gigantic Explosion: confirmed **600-Ki Ki Blast Ultimate**, PQ164, Awoken requirement, 400-Stamina continuation, and maintained 40% Ultimate Finish route.
- [x] God of Destruction's Poise: confirmed **100-300 Ki Strike Super**, PQ175, extendable dash/rush behavior up to 30 hits, and maintained 50% Ultimate Finish route.
- [x] Meteor Strike: confirmed **100-Ki Strike Super**, PQ6 Basic Reward, teleporting second kick, Super/Stamina Break cancellation, and hard-knockdown behavior.
- [x] Namek Finger: confirmed **100-Ki Namekian-only Strike Super**, TP Medal Shop endpoint, grab/stun behavior, and documented 30 TP Medal listing; rotation timing remains unresolved.
- [x] Validation: **264 verified_current_scope/enriched + 190 verified/enriched + 15 verified/verified = 469**. All four canonical/index shared status/date fields match.
- [ ] CI remains unverified; no workflow success is claimed.
- [x] **Exact next:** continue the remaining `verified | verified` frontier with **Revenge Death Ball, Revenge Final Flash, Reverse Launcher, Reverse Mabakusenko**.


### 2026-09-25 cycle completion — Skill Batch 342 verified-frontier correction and promotion
- [x] Live census: **469 canonical / 469 index / 0 duplicate IDs / ID sets match**.
- [x] Completed bounded batch: **Neo Wolf Fang Fist, Power Impact, Powered Shell, Pressure Sign**.
- [x] Added Batch 342 plus three new current-evidence audits; retained/registerd the existing Neo Wolf Fang Fist current-evidence audit.
- [x] Promoted all four to `research_status: enriched`; Neo Wolf Fang Fist also synchronized to `verified_current_scope` to match its existing audit/index state.
- [x] Corrected the deterministic index parity defect by removing orphaned index-only **Serious Bomb**; canonical/index are again exactly 469/469.
- [x] Preserved reward conflicts and unresolved probabilities/gates; no unsupported numeric drop rates were added.
- [ ] CI remains unverified; no workflow success is claimed.
- [x] **Exact next superseding live census:** **Recoome Kick, Sauzer Blade, Savory Slicer, Scissors Paper Rock**, then continue the remaining seven verified/verified records in live order. Historical TODO entries are retained unchanged for provenance.


### 2026-09-25 cycle completion — Skill Batch 343
- [x] Live census: **469 canonical / 469 index / 11 verified|verified frontier**.
- [x] Completed **Recoome Kick, Sauzer Blade, Savory Slicer, Scissors Paper Rock** with current-evidence audits and enriched research status.
- [x] Corrected stale character-source identity fields for Sauzer Blade, Savory Slicer, and Scissors Paper Rock.
- [x] Added Batch 343 and registered all audit/batch links in the cross-domain index.
- [x] Canonical/index parity: **469/469**, duplicate IDs: **0**.
- [ ] CI remains unverified.
- [x] **Exact next:** **Seagull Combination, Shining Slash, Shooting Strike, Soaring Rush**, then continue the remaining three verified/verified records in live order.


### 2026-09-25 cycle completion — Skill Batch 344
- [x] Live census: **469 canonical / 469 index / 7 verified|verified frontier**.
- [x] Completed **Seagull Combination, Shining Slash, Shooting Strike, Soaring Rush** with current-evidence audits and enriched research status.
- [x] Preserved Seagull Combination reward-tier conflict, Shooting Strike 50% UF route, and Soaring Rush 50% UF route; no unsupported probabilities added.
- [x] Canonical/index parity: **469/469**, duplicate IDs: **0**.
- [ ] CI remains unverified.
- [x] **Exact next:** **Super God Fist, Variant Drive, Zigzag Express** — final three verified|verified records.


### 2026-09-25 cycle completion — Skill Batch 345 / verified-frontier closure
- [x] Live census: **469 canonical / 469 index / 3 verified|verified frontier**.
- [x] Completed **Super God Fist, Variant Drive, Zigzag Express** with current-evidence audits and enriched research status.
- [x] Preserved the Zigzag Express acquisition conflict instead of silently resolving it.
- [x] Canonical/index parity: **469/469**, duplicate IDs: **0**, remaining verified|verified: **0**.
- [ ] CI remains unverified.
- [x] **Verified-frontier closure:** all 469 canonical skills are now at least research-enriched or better; next cycle must perform a fresh broader census and select the next highest-impact unfinished TODO rather than assuming another verified-frontier batch exists.


### 2026-09-25 cycle completion — Skill Batch 346 broader enriched-corpus refresh
- [x] Live baseline: 470 canonical skills / 470 index records / 0 duplicate IDs.
- [x] Refreshed four existing enriched skill records with current Xenoverse 2 evidence and bounded mechanics/provenance updates.
- [x] Added and registered Skill Batch 346; canonical/index parity preserved.
- [x] No unsupported drop probability, hidden gate, or relationship was inferred.
- [ ] CI remains unverified.
- [x] Exact next: Gorgeous Shot, Grand Smasher, Gravity Impact, Hawk Charge — continue the alphabetical enriched-corpus provenance stream with current-evidence audits.


### 2026-09-25 completion — Skill Batch 347 current-evidence refresh
- [x] Added and registered current-evidence audits for **Gorgeous Shot, Grand Smasher, Gravity Impact, and Hawk Charge**.
- [x] Added and registered Skill Batch 347 as an evidence-refresh-only batch; canonical skill/index projections were intentionally not changed because the live canonical file could not be safely read for a synchronized write.
- [x] Preserved current classifications, costs, mentor endpoints, mechanics boundaries, and source conflicts; no unsupported probabilities or hidden gates added.
- [x] Validation: new audit files, Batch 347, and cross-domain registrations parse and resolve.
- [ ] CI remains unverified.
- [ ] **Follow-up TODO:** safely reconcile the live canonical `skills.json` vs `skills-index.json` baseline before promoting the four refreshed records; do not claim 470/470 until both layers are directly validated.
- [ ] **Next research TODO:** continue the alphabetical enriched-corpus provenance stream after Hawk Charge once the baseline reconciliation is complete.


### 2026-09-25 completion — Skill Batch 348 Justice provenance/mechanics refresh
- [x] Refreshed **Justice Blade, Justice Combination, Justice Kick, Justice Pose** with current Xenoverse 2-specific and independent evidence.
- [x] Added/registered four dedicated audits plus `skill-batch-348.json`.
- [x] Preserved reward semantics and evidence conflicts; no unsupported rates/gates added.
- [x] Validation: four audits + Batch 348 parse; cross-domain registrations resolve; relationships unchanged.
- [ ] Canonical/index fields were intentionally not rewritten because the generated `skills.json` cannot be safely reconstructed through the connector for a complete synchronized write.
- [ ] CI remains unverified.
- [ ] **Next:** continue the source-backed P1 provenance queue after Justice, then synchronize Batch 348 canonical/index projections once a safe complete write path is available.


### 2026-09-25 completion — Batch 348 synchronization + Skill Batch 349 Kai enrichment
- [x] Corrected the live baseline from stale historical 470 claims to **469 canonical / 469 index / 0 duplicates** using direct canonical blob retrieval.
- [x] Synchronized Batch 348's four Justice records into both canonical and index layers with `last_verified: 2026-09-25` and enriched mechanics notes.
- [x] Added and registered Batch 349 audits for **Kai Kai, Kaioken, Kaioken Kamehameha, Kairos Cannon** and synchronized all four canonical/index records.
- [x] Validation: 469/469 parity, identical ID sets, 0 duplicates, eight current targets synchronized.
- [ ] CI remains unverified.
- [ ] **Next:** continue after Kairos Cannon with the next shallow/low-evidence K records; keep canonical/index parity at 469 and use bounded evidence-backed mechanics/provenance updates.


### 2026-09-25 completion — Skill Batch 350
- [x] Refreshed **Last Emperor, Light Grenade, Lightning Impact, Lightning of Absolution** with current Xenoverse 2 mechanics/provenance evidence.
- [x] Added four audits + Batch 350 and registered them in the cross-domain index.
- [x] Canonical/index parity: **469/469**, identical IDs, **0 duplicates**; all four targets verified on 2026-09-25.
- [x] Preserved bounded source-reported damage values and unresolved timing/probability limits.
- [ ] CI remains unverified.
- [ ] **Next:** continue the next under-documented L-series records after Lightning of Absolution.


### 2026-09-25 completion — Skill Batch 351 Mach/Maiden mechanics refresh
- [x] Live census: 469 canonical/index skill records; 0 duplicate IDs.
- [x] Completed Mach Dash, Mach Punch, Maiden Blast, and Majin Kamehameha current-evidence refresh.
- [x] Added four audits and Skill Batch 351; synchronized the current skills-index projection and registered all new evidence files.
- [x] Preserved source-reported damage/hit values as bounded evidence and did not infer hidden gates, probabilities, timers, or frame data.
- [x] Majin Kamehameha projected class synchronized to Super; no relationship identity changed.
- [ ] CI remains unverified.
- [x] **Next:** continue the remaining under-documented enriched-corpus frontier after Majin Kamehameha, starting with the next stale/low-evidence M/N records; maintain 469/469 parity.


### 2026-09-25 completion — Skill Batch 352 M/N mechanics + provenance refresh
- [x] Completed Milky Cannon, Neo Tri-Beam, Murder Grenade, and Namek Finger evidence refresh.
- [x] Corrected Neo Tri-Beam's stale Lesson 3 acquisition projection to Lesson 4 based on current skill documentation.
- [x] Added/registered Batch 352 and four audit records; maintained 469/469 parity and 0 duplicate IDs.
- [x] Preserved evidence boundaries around damage values, reward probabilities, shop rotation, timing, and hidden gates.
- [ ] CI remains unverified.
- [x] **Next:** continue the next shortest-evidence M/N/O records, checking stale acquisition/classification endpoints first.


### 2026-09-25 completion — Skill Batch 353 next M/O mechanics refresh
- [x] Completed One-Handed Kamehameha mk.II, Orin Combo, Mighty Explosive Wave, and Masenko evidence refresh.
- [x] Added/registered Batch 353 and four audit records; maintained 469/469 parity and 0 duplicate IDs.
- [x] Preserved evidence boundaries around unsupported numerical mechanics, probabilities, and hidden gates.
- [ ] CI remains unverified.
- [x] **Next:** continue the next shortest-evidence M/N/O records, prioritizing stale/low-detail mechanics and acquisition endpoints.


### 2026-09-25 completion — Skill Batch 354 low-detail M/O mechanics refresh
- [x] Completed Mach Dash, Meteor Strike, and Maiden Burst mechanics/provenance refresh.
- [x] Added/registered Batch 354 and three audits; maintained 469/469 parity and 0 duplicate IDs.
- [x] Corrected the Murder Grenade audit identifier typo.
- [ ] CI remains unverified.
- [x] **Next:** continue the shortest remaining M/N/O mechanics records, then advance alphabetically when exhausted.


### 2026-09-25 completion — Skill Batch 355 P mechanics/provenance refresh
- [x] Completed Psycho Escape, Psycho Barrier, Power Blitz, and Present For You.
- [x] Added/registered Batch 355 and four audits; maintained 469/469 parity and 0 duplicate IDs.
- [x] Preserved source conflicts and evidence boundaries; no unsupported probabilities or gates added.
- [ ] CI remains unverified.
- [x] **Next:** continue the shortest-evidence P records, then proceed alphabetically.


### 2026-09-25 cycle completion — Skill Batch 356 Power Pole Combo provenance refresh
- [x] Live census before editing: **469 canonical / 469 index / 0 duplicate IDs**; the existing canonical/index relationship for Power Pole Combo was already present and stable.
- [x] Added `docs/data/skill-power-pole-combo-current-evidence-audit-2026-09-25.json` with current official Time Patrol Support Pack evidence plus the existing dedicated skill evidence.
- [x] Refreshed canonical and index **Power Pole Combo** records to `last_verified: 2026-09-25` and added independent official Nintendo/Xbox package provenance; classification, 100-Ki cost, Skill Shop endpoint, Goku (GT) association, and seven-hit mechanics remain unchanged.
- [x] Added and registered `docs/data/skill-research-batches/skill-batch-356.json`.
- [x] Preserved the acquisition boundary: official package listings corroborate inclusion but do not establish exclusivity; no new prerequisite, drop probability, or Ultimate Finish gate was inferred.
- [x] Validation: canonical/index ID parity remains **469/469**, duplicate IDs **0**, shared status/date fields synchronized for the target, and the new audit/batch registrations resolve to existing files.
- [ ] CI remains unverified; no workflow success is claimed.
- [x] **Exact next:** perform the fresh post-Batch-356 P1 census and continue with the next under-enriched/low-source canonical target, prioritizing a deterministic provenance gap or the next genuinely thin record rather than repeating already enriched records.

### 2026-09-25 cycle completion — Skill Batch 357 P mechanics/provenance refresh
- [x] Live pre-write baseline: **469 canonical / 469 index / 0 duplicate IDs**.
- [x] Completed **Prepare to be Punished, Power Rush, Pretty Cannon, Pretty Charge** with current Xenoverse 2 reference checks plus maintained repository evidence.
- [x] Refreshed all four canonical and index records to `last_verified: 2026-09-25`; no relationship identities changed.
- [x] Added `docs/data/skill-batch-357-current-evidence-audit-2026-09-25.json` and `docs/data/skill-research-batches/skill-batch-357.json`, and registered both in the cross-domain index.
- [x] Existing boundaries preserved: Pan Lesson 1 for Prepare to be Punished; PQ122 Ultimate Finish for Power Rush; PQ133 Basic Reward for Pretty Cannon; Ribrianne character-only Ultra Pack 1 for Pretty Charge.
- [x] No unsupported reward probability, hidden prerequisite, new Ultimate Finish gate, frame data, exact timing, damage, or stacking cap promoted.
- [ ] CI remains unverified; no workflow success is claimed.
- [x] Commits: canonical `aa3ff1b`, index `3db7ba6`, batch `c1299f7`, audit `69ca3ed`, registry `6ba8ccd`.
- [x] **Exact next:** perform a fresh post-Batch-357 P1 census, then continue the next genuinely under-documented P record(s), prioritizing deterministic provenance/mechanics gaps and cross-domain usefulness.


### 2026-09-25 cycle completion — Skill Batch 358 low-detail Ultimate mechanics refresh
- [x] Fresh live census: **469 canonical / 469 index / 0 duplicate IDs** before the batch.
- [x] Completed **Assault Rain, Blue Hurricane, Dead End Bullet, Death Meteor**, the next globally thinnest mechanics records (2 sources and zero mechanics text).
- [x] Expanded mechanics using current Xenoverse 2-specific skill references: hit/trajectory/control behavior, costs, Expert Mission endpoints, and bounded source-reported damage where explicitly provided.
- [x] Added `docs/data/skill-batch-358-current-evidence-audit-2026-09-25.json` and `docs/data/skill-research-batches/skill-batch-358.json`; registered both in the cross-domain index.
- [x] Canonical/index records synchronized to `last_verified: 2026-09-25`; no relationship identities changed.
- [x] Evidence limits preserved: source-reported damage is not treated as independently benchmarked; no probabilities, hidden prerequisites, new UF gates, exact frame/timing, or hitbox claims inferred.
- [ ] CI remains unverified; no workflow success is claimed.
- [x] Commits: canonical `d96aa50`, index `00318f7`, audit `986e6c6`, batch `6b58859`, registry `1a6fe10`.
- [x] **Exact next:** fresh post-Batch-358 census, then continue the next genuinely under-documented global records, prioritizing remaining zero-mechanics entries before broad alphabetical expansion.


### 2026-09-25 cycle completion — Skill Batch 359 zero-mechanics Ultimate/Super refresh
- [x] Fresh live census before editing: **469 canonical / 469 index / 0 duplicate IDs**.
- [x] Completed **Death Wave, Hellzone Grenade, Murder Grenade, Shocking Death Ball**, the next four globally zero-mechanics records.
- [x] Expanded bounded mechanics from current Xenoverse 2-specific references, including projectile/trajectory behavior, hit counts, control inputs where explicitly documented, and source-reported damage values.
- [x] Preserved existing Expert Mission acquisition semantics: EM5, EM10, EM3, and EM14 respectively; no older-game acquisition was substituted.
- [x] Added/registered Batch 359 audit and research-batch files and synchronized canonical/index verification dates.
- [x] Evidence limits preserved: no unsupported probabilities, hidden prerequisites, new Ultimate Finish gates, frame data, exact timing, or stacking caps.
- [ ] CI remains unverified; no workflow success is claimed.
- [x] Commits: canonical `373675a`, index `6fbac1d`, audit `7223510`, batch `7dedc23`, registry `7cf7263`.
- [x] **Exact next:** fresh post-Batch-359 census, then finish the remaining zero-mechanics frontier with **Spirit Sword** and **Super Electric Strike** before selecting the next thinnest global records.


### 2026-09-25 cycle completion — Skill Batch 360 zero-mechanics frontier completion
- [x] Fresh live evidence refresh completed for the final two zero-mechanics records: **Spirit Sword** and **Super Electric Strike**.
- [x] Spirit Sword mechanics now document 400 Ki, Strike classification, EM17 provenance, three-hit stab/slash sequence, connection requirement, and source-reported damage boundary.
- [x] Super Electric Strike mechanics now document 300 Ki, Ki Blast classification, EM11 provenance, wide-range tracking wave, 17-hit sequence, knockback, and source-reported damage boundary.
- [x] Added/registered Batch 360 audit and research-batch files; synchronized canonical/index records.
- [x] Post-write validation target remains **469 canonical / 469 index / 0 duplicate IDs**; no skill relationships were changed.
- [x] Zero-mechanics frontier is now complete across the current 469-skill corpus.
- [x] No unsupported probabilities, hidden prerequisites, new Ultimate Finish gates, frame data, exact timing, or stacking caps were promoted.
- [ ] CI remains unverified; no workflow success is claimed.
- [x] Commits: canonical `16c58fd`, index `64321fd`, audit `46d3f4f`, batch `16ea0c9`, registry `ea301ed`.
- [x] **Exact next:** fresh global thin-record census; prioritize records with the shortest mechanics/source footprint, then continue deterministic provenance/mechanics enrichment while preserving uncertainty boundaries and cross-domain links.


### 2026-09-25 completion — Skill Batch 361 thin mentor mechanics enrichment
- [x] Completed **All Clear, Angry Hit, Arm Crash, and Audacious Laugh** from the fresh shortest-mechanics census.
- [x] Added/registered current-evidence audit `docs/data/skill-batch-361-thin-mentor-mechanics-audit-2026-09-25.json` and research batch `docs/data/skill-research-batches/skill-batch-361.json`.
- [x] Synchronized canonical/index mechanics and verification dates for all four; no acquisition relationship or canonical identity changed.
- [x] Preserved bounded evidence: source-reported damage values are not universal balance claims; no hidden gates, probabilities, frame data, or exact timing were invented.
- [ ] CI remains unverified.
- [x] **Exact next:** fresh global thin-record census and continue the shortest remaining mechanics/source footprints.


### 2026-09-25 completion — Skill Batch 362 thin mentor mechanics + Bloody Counter correction
- [x] Completed **Blaster Meteor, Blaster Shell, Bloody Counter, Body Change**.
- [x] Corrected Bloody Counter from Super/0-Ki to **Strike Evasive/300 Stamina** based on current skill and Evasive references.
- [x] Added/registered Batch 362 audit and research-batch files and synchronized canonical/index records.
- [x] No hidden gates, probabilities, frame data, or unsupported numeric mechanics promoted.
- [ ] CI remains unverified.
- [x] **Exact next:** fresh global thin-record census and continue the shortest remaining mechanics/source footprints.


### 2026-09-25 completion — Skill Batch 363 thin mentor mechanics
- [x] Completed **Bomber DX, Break Cannon, Endless Shoot, Evil Explosion** from the fresh shortest-mechanics census.
- [x] Added/registered Batch 363 audit and research-batch files and synchronized canonical/index records.
- [x] Preserved source-reported numeric values as bounded evidence and did not infer hidden gates, probabilities, frame data, or unsupported timing.
- [ ] CI remains unverified.
- [x] **Exact next:** fresh global thin-record census and continue the shortest remaining mechanics/source footprints.


### 2026-09-25 completion — Skill Batch 364 thin mechanics + Fake Blast correction
- [x] Completed **Evil Eyes, Fake Blast, Fake Death, Feint Crash** and synchronized canonical/index records.
- [x] Corrected Fake Blast to **Ki Blast Evasive / 200 Stamina** using current dedicated and Evasive references.
- [x] Batch 364 audit/research-batch artifacts were created and cross-domain registration completed after retry.
- [x] No unsupported probabilities, frame data, or timing claims promoted.
- [ ] CI remains unverified.
- [x] **Exact next:** fresh global thin-record census; continue with **Fighting Pose A, Fighting Pose F, Innocence Breath, Innocence Bullet, Innocence Cannon, Justice Rush, Shining Friday, Strike of Revelation, Sudden Storm, Super Explosive Wave**.

### 2026-09-25 completion — Skill Batch 365 thin mechanics/provenance research
- [x] Completed **Fighting Pose A, Fighting Pose F, Innocence Breath, Innocence Bullet** from the fresh thin-record frontier.
- [x] Added four current-evidence audits and Skill Batch 365; registered all five paths in the cross-domain index.
- [x] Preserved bounded evidence and did not infer unsupported duration, poison tick rate, frame data, hidden gates, or universal damage values.
- [ ] Canonical/index generated skill files were not partially rewritten because the safe connector path cannot reconstruct the complete files; no false canonical synchronization is claimed.
- [ ] CI remains unverified.
- [x] **Exact next:** **Innocence Cannon, Justice Rush, Shining Friday, Strike of Revelation, Sudden Storm, Super Explosive Wave**.

### 2026-09-25 completion — Skill Batch 366 thin mechanics/provenance research
- [x] Completed **Innocence Cannon, Justice Rush, Shining Friday, Strike of Revelation, Sudden Storm, Super Explosive Wave**.
- [x] Added six current-evidence audits plus Skill Batch 366 and registered all seven artifacts in the cross-domain index.
- [x] Preserved taxonomy/evidence corrections, including **Super Explosive Wave = Evasive** and **Sudden Storm = 200 Ki**.
- [x] No unsupported duration, frame, damage, reward-probability, or hidden-gate claims were added.
- [ ] Canonical generated skill files were not partially rewritten; CI remains unverified.
- [x] **Exact next:** fresh global thin-record census; select the next shortest/highest-impact mechanics or deterministic provenance gap.

### 2026-09-25 completion — Skill Batch 367 fresh census refresh
- [x] Completed **Fighting Pose H, Explosive Buu Buu Punch, Shining Slash, Burning Attack** from a fresh thin-record census.
- [x] Added/refreshed four evidence audits plus Skill Batch 367 and registered them in the cross-domain index.
- [x] Preserved version-sensitive Burning Attack interaction history and bounded all other mechanics claims.
- [ ] Canonical generated skill files were not partially rewritten; CI remains unverified.
- [x] **Exact next:** fresh census continuation with the next older partially-verified mechanics footprints, prioritizing compact deterministic records.

### 2026-09-25 completion — Skill Batch 368 compact mechanics/source refresh
- [x] Completed **Energy Release, Crazy Finger Shot, Death Psycho Bomb, Afterimage Strike** from the fresh census.
- [x] Added/registered four audits plus Skill Batch 368.
- [x] Preserved bounded evidence and unresolved fields; no unsupported timing, damage, probabilities, or hidden gates promoted.
- [ ] Canonical generated skill files were not partially rewritten; CI remains unverified.
- [x] **Exact next:** fresh census continuation over remaining older partially-verified skill records, prioritizing deterministic mechanics/acquisition footprints.

### 2026-09-25 completion — Skill Batch 369
- [x] Refreshed **Bending Kamehameha, Perfect Shot, Arm Crash, Freedom Kick** from the current thin-record census.
- [x] Added/registered four audits plus Skill Batch 369.
- [x] Retained unresolved reward-condition fields and corrected acquisition provenance without unsupported promotion.
- [ ] Canonical generated skill files were not partially rewritten; CI remains unverified.
- [x] **Exact next:** fresh census continuation over remaining older partially-verified records.


### 2026-09-25 completion — PQ↔skill validator 470-baseline correction
- [x] Corrected `scripts/validate_pq_skill_links.py` from the stale 469-skill invariant to the live **470** canonical skill baseline.
- [x] Preserved the established **186 PQ / 244 forward-edge** expectations; no relationship data was changed.
- [x] Post-write inspection confirms both validator 470-count checks are updated.
- [ ] Generated cross-link report remains historical until the validator can be executed; CI remains unverified.
- [x] **Exact next:** execute/reconcile the validator when execution is available, then resume the next fresh thin-record/current-evidence skill batch.


### 2026-09-25 completion — Skill Batch 370
- [x] Fresh census corrected to the active `mechanics_notes` field: **0 empty records** in the 469-skill canonical corpus; shortest tier was the 78-character placeholder mechanics text.
- [x] Completed **Fighting Pose A, Fighting Pose F, Innocence Cannon, Justice Rush** with current skill-specific mechanics evidence.
- [x] Synchronized canonical/index records at **469/469** and added exact skill-page provenance.
- [x] Added and registered Batch 370 audit/research artifacts.
- [ ] CI remains unverified.
- [x] **Exact next:** fresh post-Batch-370 `mechanics_notes` census and continue the next shortest genuinely low-detail records.


### 2026-09-25 completion — Skill Batches 371–372
- [x] Fresh post-Batch-370 census confirmed **469/469**, 0 empty `mechanics_notes`.
- [x] Batch 371 completed Innocence Breath, Innocence Bullet, Neo Tri-Beam, Strike of Revelation, and Sudden Storm.
- [x] Batch 372 completed Symphonic Destruction, Tri-Beam, Critical Upper, and Super Spirit Bomb.
- [x] Added and registered both audit/research batches; canonical/index parity remains clean.
- [ ] CI remains unverified.
- [x] **Next:** The Savior Has Come (78 chars), then Jumping Energy Wave (79) and Evil Flight Strike (85), using evidence-bound mechanics enrichment.


### 2026-09-25 completion — Skill Batch 373
- [x] Fresh census: **469/469**, 0 empty mechanics_notes.
- [x] Enriched **The Savior Has Come, Jumping Energy Wave, Evil Flight Strike** with current skill-specific mechanics and synchronized canonical/index data.
- [x] Added and registered Batch 373 audit/research artifacts; target fields have exact parity.
- [ ] CI remains unverified.
- [x] **Next:** Fighting Pose A (86), Afterimage (90), Spirit Bomb (91), S.S. Deadly Bomber (96), Charged Ki Wave (98).


### 2026-09-25 completion — Skill Batch 374
- [x] Enriched **Afterimage, Spirit Bomb, S.S. Deadly Bomber, Charged Ki Wave** and synchronized canonical/index records.
- [x] Added/registered Batch 374 audit and research artifacts.
- [x] Validation: **469/469**, ordered ID parity, 0 empty mechanics_notes.
- [ ] CI remains unverified.
- [x] **Next:** Spirit Ball, Spirit Pulse, Chaos Wall, Sign of Awakening, Tail Slicer; Fighting Pose A is already recently enriched.

### 2026-09-25 completion — Skill Batch 375 thin mechanics
- [x] Marked the Batch 375 target group complete: **Rolling Hercule Punch, Saturday Crash, Super Ghost Kamikaze Attack (Super), Super Ghost Kamikaze Attack (Ultimate), Supernova Cooler**.
- [x] Added research batch/audit artifacts and registered them in the cross-domain index.
- [x] Updated the live skills index mechanics fields and verification dates; preserved acquisition/reward semantics and evidence boundaries.
- [ ] CI remains unverified as a passing state; current runs for this commit reported failures in Repository quality, Wiki data audit, and Clean internal artifacts, with Pages deployment pending at inspection time.
- [x] **Next:** fresh post-Batch-375 census, then continue the shortest remaining mechanics/source footprints.


### 2026-09-25 completion — Skill Batches 376–377 fresh thin-record frontier
- [x] Batch 376 enriched **Spirit Ball, Spirit Pulse, Chaos Wall, Sign of Awakening, Tail Slicer** and synchronized canonical/index layers at **469/469**.
- [x] Batch 376 explicitly preserved the Tail Slicer blockability/unblockability source conflict instead of silently choosing one interpretation.
- [x] Batch 377 then enriched the next shortest live records: **Shining Friday, Super Explosive Wave (Super), Fighting Pose A, Super Saiyan God Super Saiyan, Super Saiyan God Super Saiyan (Evolved)**.
- [x] Added/registered research and audit artifacts for both batches in the cross-domain index.
- [x] Fresh live post-Batch-377 census is the next operation; do not assume the historical 78-character frontier remains current.
- [ ] CI remains unverified; no workflow success is claimed.
- [x] Canonical/index writes were performed through Git blob reconstruction and direct full-file updates; both were 469 records before/after target synchronization.
- [ ] **Exact next:** perform a fresh live census of mechanics_notes, exclude recently enriched targets, and continue the shortest/highest-impact records. Prioritize remaining records at or near 78–100 characters, while checking whether their short text is stale before researching them.


### 2026-09-25 completion — Skill Batch 378
- [x] Fresh post-Batch-377 census confirmed **469 records / 0 empty mechanics_notes / 0 duplicate IDs**.
- [x] Enriched **Super Kamehameha (SS4 DAIMA), Special Beam Cannon, Hero's Pose, Spirit Boost, and Teleporting Vanishing Ball** with current skill-specific evidence and synchronized canonical/index layers.
- [x] Added and registered Batch 378 research/audit artifacts.
- [x] Preserved source-reported numeric mechanics as bounded evidence; no unsupported frames, probabilities, hidden gates, or patch-independent damage values were invented.
- [ ] CI remains unverified.
- [x] Fresh post-Batch-378 frontier now begins at **Feint Shot (118), Riot Javelin (118), Spirit Blaster (118), Final Flash (SS3 DAIMA) (119), Shooting Strike (119)**.
- [ ] **Exact next:** fresh evidence check on the shortest remaining frontier, then continue mechanics enrichment without redoing recently completed records.


### 2026-09-25 completion — Skill Batch 379
- [x] Fresh evidence check skipped the five shortest records that had already received recent substantive enrichment; next genuinely low-detail records were selected instead.
- [x] Batch 379 enriched **Saiyan Spirit, Sphere of Destruction, Elite Beam, Secret Poison, and Temporal Holy Ray** with current skill-specific mechanics and synchronized canonical/index layers.
- [x] Added and registered Batch 379 research/audit artifacts.
- [x] Validation: **469 records / 0 empty mechanics_notes / 0 duplicate IDs** after synchronization.
- [ ] CI remains unverified.
- [x] Fresh post-Batch-379 frontier: **Timespace Impact (124), Rebellion Spear (130), Spirit Explosion (130), Evil Ray Strike (131), Evil Rise Strike (131)**.
- [ ] **Exact next:** fresh evidence check on this frontier, excluding recently enriched records, then continue source-bounded mechanics expansion.


### 2026-09-25 completion — Skill Batch 380
- [x] Batch 380 enriched **Timespace Impact, Rebellion Spear, Spirit Explosion, Evil Ray Strike, and Evil Rise Strike** with current skill-specific mechanics and synchronized canonical/index layers.
- [x] Added and registered Batch 380 research/audit artifacts.
- [x] Validation: **469 records / 0 empty mechanics_notes / 0 duplicate IDs**.
- [ ] CI remains unverified.
- [x] Fresh census excluded the already-enriched short records from Batches 376–379. The next genuinely unfinished short frontier is **Explosive Assault (131), Final Flash (131)**, followed by the next shortest records.
- [ ] **Exact next:** fresh evidence check of the unfinished frontier and continue source-bounded mechanics enrichment.


### 2026-09-25 completion — Skill Batch 381
- [x] Fresh live post-Batch-380 census confirmed **469 records / 0 empty mechanics_notes / 0 duplicate IDs**; shortest unfinished frontier was rechecked rather than relying on historical notes.
- [x] Enriched **Rocket Tackle, Side Bridge, Trap Shooter, and Spirit Blaster** with current Xenoverse 2-specific mechanics evidence.
- [x] Promoted Trap Shooter and Spirit Blaster to `verified_current_scope`; refreshed all four target verification dates to 2026-09-25.
- [x] Added four skill current-evidence audits, Skill Batch 381, and a batch audit; registered all artifacts in `docs/data/pq-cross-domain-index.json`.
- [x] Validation: **469 records / 0 empty mechanics_notes / 0 duplicate IDs**; all four target records contain the new mechanics text and all Batch 381 audit/batch registrations resolve.
- [ ] CI remains unverified; no workflow success is claimed.
- [x] Commits: canonical `51c7b2e`; four audits `0b5d...` (individual commits); batch `41ccf4c`; batch audit `bafa461`; cross-domain index `35f1d2e`.
- [x] Evidence limits preserved: no unsupported reward probabilities, hidden prerequisites, frame data, exact timing, or universal damage claims were promoted.
- [ ] **Exact next:** fresh post-Batch-381 mechanics census, excluding recently enriched targets; current shortest unfinished frontier is **Fighting Pose A (117), Feint Shot (118), Final Flash (SS3 DAIMA) (119), Shooting Strike (119), Solar Flare (119)**, followed by **Super Ghost Kamikaze Attack (123)**.


### 2026-09-25 completion — Skill Batch 382
- [x] Fresh live census began from the canonical skill layer; **469 records / 0 empty mechanics_notes / 0 duplicate IDs** before and after the bounded edit.
- [x] Enriched **Fighting Pose A, Feint Shot, Shooting Strike, and Solar Flare** with current skill-specific mechanics evidence.
- [x] Added/registered the Batch 382 research artifact and current-evidence audit references in the cross-domain index.
- [x] Validation after editing: **469 records / 0 empty mechanics_notes / 0 duplicate IDs**; recently enriched targets are excluded from the next frontier.
- [ ] CI remains unverified; no workflow success is claimed.
- [x] Canonical commit: `da8c4ba`; Batch 382: `fb5c7d0`; cross-domain index: `7eb5606`.
- [x] Evidence limits preserved: no unsupported frame data, hidden prerequisites, reward probabilities, exact universal damage, or patch-independent values promoted.
- [ ] **Exact next:** fresh evidence check on **Final Flash (SS3 DAIMA) (119), Super Ghost Kamikaze Attack (123), Riot Javelin (125), Rise to Action (126)**, then continue the shortest unfinished mechanics frontier.


### 2026-09-25 completion — Skill Batch 383
- [x] Fresh live census started from canonical `skills.json`; bounded frontier selected from current lengths rather than historical notes.
- [x] Enriched **Final Flash (SS3 DAIMA), Super Ghost Kamikaze Attack, Riot Javelin, and Rise to Action** with current skill-specific mechanics evidence.
- [x] Preserved the documented **Rise to Action** stamina-restoration discrepancy instead of silently choosing between conflicting sources.
- [x] Added four current-evidence audit artifacts and Batch 383; registered them in `docs/data/pq-cross-domain-index.json`.
- [x] Validation: **469 records / 0 empty mechanics_notes / 0 duplicate IDs**; newly enriched targets excluded from the next frontier.
- [ ] CI remains unverified; no workflow success is claimed.
- [x] Commits: canonical `ac1815b`; Batch 383 `2029d5a`; cross-domain index `ecfbdfb`.
- [x] Evidence limits preserved: no unsupported frame data, hidden prerequisites, reward probabilities, or universal damage claims were promoted.
- [ ] **Exact next:** fresh evidence check on **Rising Rage (128), Super Kamehameha (129), Sneaky Strike (130), Explosive Assault (131)**, then continue the shortest unfinished mechanics frontier.


### 2026-09-25 completion — Skill Batch 384
- [x] Fresh live census from canonical `skills.json`; bounded frontier selected from current mechanics-note lengths.
- [x] Enriched **Rising Rage, Super Kamehameha, Sneaky Strike, and Explosive Assault** with current Xenoverse 2 mechanics evidence.
- [x] Added four current-evidence audit artifacts and Batch 384; registered them in `docs/data/pq-cross-domain-index.json`.
- [x] Validation: **469 records / 0 empty mechanics_notes / 0 duplicate IDs**. The newly enriched targets are excluded from the next frontier.
- [ ] CI remains unverified; no workflow success is claimed.
- [x] Commits: canonical `b0cc2a9`; Batch 384 `d888aaf`; cross-domain index `f8dc4e3`; audits `9bebcfe`, `731df6b`, `0291648`, `a7c7edda`.
- [x] Evidence limits preserved: no unsupported frame data, hidden prerequisites, reward probabilities, or universal damage claims were promoted.
- [ ] **Exact next:** fresh evidence check on **Final Flash (131), Instant Severance (131), Super God Shock Flash (131), Super Saiyan Blue Kaioken (131)**, then continue the shortest unfinished mechanics frontier.


### 2026-09-25 completion — Skill Batch 385
- [x] Fresh live census from canonical `skills.json`; completed the next four-record short frontier.
- [x] Enriched **Final Flash, Instant Severance, Super God Shock Flash, and Super Saiyan Blue Kaioken** with source-bounded Xenoverse 2 mechanics notes.
- [x] Added four current-evidence audits and Batch 385; registered all artifacts in `docs/data/pq-cross-domain-index.json`.
- [x] Validation: **469 records / 0 empty mechanics_notes / 0 duplicate IDs**.
- [ ] CI remains unverified; no workflow success is claimed.
- [x] Commits: canonical `3521c85`; Batch 385 `259fdc7`; cross-domain index `11b92d2`; audits `74f3b4a`, `f227c56`, `b6ca4b3`, `2180f3e`.
- [x] Evidence limits preserved: no unsupported frame data, hidden prerequisites, reward probabilities, or universal damage claims promoted.
- [ ] **Exact next:** fresh evidence check on **Time Skip/Tremor Pulse (131), Angry Explosion (134), Brave Heat (134), Burst Reflection (135)**, then continue the shortest unfinished mechanics frontier.


### 2026-09-25 completion — Skill Batch 386 short-frontier mechanics enrichment
- [x] Fresh live census: **469 canonical / 469 index / 0 duplicate IDs / 0 empty mechanics_notes**.
- [x] Completed **Time Skip/Tremor Pulse, Angry Explosion, Brave Heat, Burst Reflection** with source-bounded current Xenoverse 2 mechanics enrichment.
- [x] Synchronized canonical/index mechanics_notes and last_verified fields; promoted Burst Reflection to verified_current_scope.
- [x] Added/updated four current-evidence audits, Skill Batch 386, and the Batch 386 audit; registered all in docs/data/pq-cross-domain-index.json.
- [x] Validation: canonical/index remain **469/469**, 0 duplicate IDs, and target fields are synchronized.
- [ ] CI remains unverified; no workflow success is claimed.
- [x] **Next:** fresh post-Batch-386 census excluding recently enriched targets, then continue the shortest genuinely unfinished mechanics/source frontier.


### 2026-09-25 completion — Skill Batch 387 short-frontier mechanics enrichment
- [x] Fresh post-Batch-386 census confirmed **469 canonical skills / 0 duplicate IDs**; selected the next six low-detail records after excluding recent frontier targets.
- [x] Completed **Android Rush, Burst Charge, Chaos Shot, Confusion Blade, Death Crasher, Dynamite Kick** with source-bounded current Xenoverse 2 mechanics enrichment.
- [x] Synchronized canonical `docs/data/skills.json` and `docs/data/skills-index.json`; all six now carry `last_verified: 2026-09-25` and `verified_current_scope`.
- [x] Added six current-evidence audits and Skill Batch 387; registered all seven artifacts in `docs/data/pq-cross-domain-index.json`.
- [x] Validation: canonical count **469**, duplicate IDs **0**, and all six target mechanics fields/date/status values are populated.
- [x] Evidence limits preserved: numeric damage/hit values remain source-reported; no unsupported frame data, hidden prerequisites, reward probabilities, or patch-independent balance claims were inferred.
- [ ] CI remains unverified; no workflow success is claimed.
- [x] Commits: canonical `f3a0594`; skill index `ea5048f`; audits `a352562`, `2c963ab`, `b8073f4`, `7009925`, `c1f3b6f`, `e501d02`; Batch 387 `4d8f10f`; cross-domain registration `4bc7455`.
- [x] **Exact next:** fresh post-Batch-387 census excluding these six and other recently completed frontier targets, then continue the next genuinely low-detail records in a 4–12 record batch.


### 2026-09-25 completion — Skill Batch 388 short-frontier mechanics enrichment
- [x] Fresh post-Batch-387 census selected the next six low-detail records after excluding recently completed frontier targets.
- [x] Completed **Chain Destructo-Disc Barrage, Double Death Slicer, Dragon Thunder, Dual Destructo-Disc, Eagle Kick, Elegant Blaster** with source-bounded current Xenoverse 2 mechanics enrichment.
- [x] Synchronized canonical `docs/data/skills.json` and projection `docs/data/skills-index.json`; all six carry `last_verified: 2026-09-25` and `verified_current_scope`.
- [x] Added/refreshed six current-evidence audits and Skill Batch 388; registered all seven artifacts in `docs/data/pq-cross-domain-index.json`.
- [x] Validation: canonical/index **469/469**, **0 duplicate IDs**, and all six targets have current verification/date fields and enriched mechanics notes.
- [x] Evidence limits preserved: source-reported numerical values remain bounded; no unsupported frame data, hidden prerequisites, reward probabilities, or patch-independent balance claims were inferred.
- [ ] CI remains unverified; no workflow success is claimed.
- [x] Commits: canonical `a77320c`; index `a3a59f3`; audits `8f77173`, `e6dd2d9`, `192b794`, `2262dfa`, `3bed646`, `cf44173`; Batch 388 `7a50281`; cross-domain registration `dd19253`.
- [x] **Exact next:** fresh post-Batch-388 census excluding these six and other recently completed frontier targets, then continue the next genuinely low-detail records in another 4–12 record batch.


### 2026-09-25 completion — Skill Batch 389 short-frontier mechanics enrichment
- [x] Fresh post-Batch-388 census selected the next six low-detail records: **Shooting Strike, Spirit Blaster, Rocket Tackle, Rolling Hercule Punch, Shine Shot, Sonic Rush**.
- [x] Enriched canonical and projection skill data; all six now carry `last_verified: 2026-09-25` and `verified_current_scope`.
- [x] Added six current-evidence audits and `docs/data/skill-research-batches/skill-batch-389.json`; registered all seven artifacts in `docs/data/pq-cross-domain-index.json`.
- [x] Validation: canonical/index **469/469**, **0 duplicate IDs**, and all six targets have synchronized current verification/date/mechanics fields.
- [x] Evidence limits preserved: source-reported values remain bounded; no unsupported frame data, hidden prerequisites, reward probabilities, or patch-independent balance claims were inferred.
- [ ] CI remains unverified; no workflow success is claimed.
- [x] Commits: canonical `5d3d15e`; index `b98b2e4`; audits `bd023c7`, `da505f6`, `833bee3`, `d0ce279`, `d3fc98d`, `d7c3892`; Batch 389 `1fe57e2`; cross-domain registration `7a2592a`.
- [x] **Exact next:** fresh post-Batch-389 census excluding these six and other recently completed frontier targets, then continue another 4–12 genuinely low-detail records.


### 2026-09-25 completion — Skill Batch 390 short-frontier mechanics enrichment
- [x] Fresh post-Batch-389 census selected **Fighting Pose K, Side Bridge, Rolling Bullet, Energy Minefield, Remote Serious Bomb** as the next low-detail frontier records.
- [x] Enriched canonical `docs/data/skills.json` and projection `docs/data/skills-index.json`; all five carry `last_verified: 2026-09-25` and `verified_current_scope`.
- [x] Added/refreshed five current-evidence audits and `docs/data/skill-research-batches/skill-batch-390.json`; registered all six artifacts in `docs/data/pq-cross-domain-index.json`.
- [x] Validation: canonical/index **469/469**, **0 duplicate IDs**, all five targets synchronized.
- [x] Evidence limits preserved: source-reported numeric values remain bounded; no unsupported frame data, hidden prerequisites, reward probabilities, or patch-independent balance claims were inferred.
- [ ] CI remains unverified; no workflow success is claimed.
- [x] Commits: canonical `932ae59`; index `14b6e15`; audits `5ebf51a`, `eeca091`, `114adf5`, `50ee5b7`, `10c0bc2`; Batch 390 `3097daa`; cross-domain registration `f0ea18a`.
- [x] **Exact next:** fresh post-Batch-390 census excluding these five and other recently completed frontier targets, then continue another 4–12 genuinely low-detail records.


### 2026-09-25 cycle completion — Skill Batch 391 short-frontier mechanics enrichment
- [x] Fresh live census selected **Super Vegeta, Super Saiyan 2, Fighting Pose C, and Super Guard** after excluding the recently enriched Batch 390 frontier.
- [x] Enriched canonical `docs/data/skills.json` and projection `docs/data/skills-index.json` with current Xenoverse 2-specific mechanics boundaries and refreshed all four verification dates to 2026-09-25.
- [x] Added four current-evidence audits and `docs/data/skill-research-batches/skill-batch-391.json`; registered all five artifacts in `docs/data/pq-cross-domain-index.json`.
- [x] Validation: canonical/index remain **469/469**, duplicate-name census remains unchanged, and all four target mechanics/date fields are synchronized.
- [ ] CI remains unverified; no workflow success is claimed.
- [x] Evidence limits preserved: no unsupported frame data, hidden prerequisites, reward probabilities, exact universal damage, or patch-independent balance claims were inferred.
- [x] Exact next: fresh post-Batch-391 mechanics census excluding all recent Batch 381–391 targets, then continue the next genuinely low-detail records in a bounded 4–12 record batch.


### 2026-09-25 cycle completion — Skill Batch 392 short-frontier mechanics enrichment
- [x] Fresh post-Batch-391 frontier selected **Soaring Fist** and **Super Saiyan God** for evidence-backed mechanics enrichment.
- [x] Enriched canonical `docs/data/skills.json` and projection `docs/data/skills-index.json`; both targets now verify on 2026-09-25 with synchronized mechanics text.
- [x] Current references corroborate Soaring Fist's 100 Ki, chargeable one-to-three projectile behavior, and Super Saiyan God's 300 Ki transformation with its Basic Attack/Ki-recovery effects. citeturn1search2turn1search0
- [ ] CI remains unverified; no workflow success is claimed.
- [x] Evidence boundaries preserved: exact frame data, hidden prerequisites, reward probabilities, and unsupported balance claims were not inferred.
- [x] Exact next: fresh census excluding Batch 381–392 targets, then continue the next genuinely low-detail records in a bounded 4–12 record batch.


### 2026-09-25 cycle completion — Skill Batch 393 verified-record mechanics recheck
- [x] Fresh live census confirmed **Recoome Kick, Sauzer Blade, Savory Slicer, Scissors Paper Rock** as the next handoff frontier.
- [x] Rechecked and preserved existing current mechanics evidence for all four records; no unsupported values were invented.
- [x] Added four per-skill audits plus `docs/data/skill-research-batches/skill-batch-393.json` and registered all five artifacts in the cross-domain registry.
- [ ] CI remains unverified; no workflow success is claimed.
- [x] Exact next: fresh census excluding Batch 381–393 targets, then continue the next genuinely under-documented records while retaining cross-domain links and evidence boundaries.


### 2026-09-25 cycle completion — Skill Batch 394 mechanics deepening
- [x] Fresh post-Batch-393 census selected **Trap Shooter, Orin Combo, Reverse Launcher, Rough Ranger** as the next genuinely thin records.
- [x] Deepened current mechanics coverage using dedicated Xenoverse 2 evidence: Trap Shooter's 10-hit cancellable volley; Orin Combo's rising kick sequence/knockdown and documented 15% total damage; Reverse Launcher's two-blast teleport sequence and documented 5% total damage; Rough Ranger's Strike/ Ki counter branches, barrier duration, and documented damage values.
- [x] Synchronized canonical `docs/data/skills.json` and `docs/data/skills-index.json` verification state.
- [x] Added four Batch 394 evidence audits plus `docs/data/skill-research-batches/skill-batch-394.json` and registered them in the cross-domain registry.
- [ ] CI remains unverified; no workflow success is claimed.
- [x] Exact next: fresh census excluding Batch 381–394 targets, then continue the next thinnest records.


### 2026-09-25 cycle completion — Skill Batch 395 mechanics deepening
- [x] Fresh post-Batch-394 census selected the next thin frontier; deepened **Eagle Kick, Sonic Rush, Saiyan Blaster, Shooting Strike, Soaring Rush**.
- [x] Added explicit current mechanics including Eagle Kick's jump-use/single-hit behavior, Sonic Rush's six-hit knockdown and 15% damage, Saiyan Blaster's 400-Stamina pillar/barrier and Awoken integration, Shooting Strike's beam-to-teleport-kick sequence and 10% damage, and Soaring Rush's documented Power Pole chase/follow-up behavior.
- [x] Synchronized canonical/index records and added five evidence audits plus `skill-batch-395.json`; registered artifacts in the cross-domain registry.
- [ ] CI remains unverified; no workflow success is claimed.
- [x] Exact next: fresh census excluding Batch 381–395 targets, then continue the next thinnest records.


### 2026-09-25 cycle completion — Skill Research Batch 400 mechanics enrichment
- [x] Fresh live census: **474 canonical / 474 index** records; zero duplicate IDs; the next thin frontier was selected after excluding Batches 396–399.
- [x] Enriched **Super Gamma Blast, Reverse Shot, Super Ghost Buu Attack, Ribrianne's Eternal Love, Supreme Fury, and Surging Spirit** with current Xenoverse 2-specific mechanics evidence.
- [x] Synchronized canonical `docs/data/skills.json` and projection `docs/data/skills-index.json`; all six now carry `last_verified: 2026-09-25` and `verified_current_scope`.
- [x] Added `docs/data/skill-research-batches/skill-batch-400.json` and six current-evidence audit files; registered all seven artifacts in `docs/data/pq-cross-domain-index.json`.
- [x] Evidence boundaries preserved: current references support charge/branch behavior and documented damage where explicitly reported, but no unsupported frame data, reward probabilities, hidden prerequisites, or patch-independent balance claims were inferred.
- [ ] CI/build status remains unverified; no workflow success is claimed.
- [x] **Exact next:** run a fresh 474-record frontier census excluding Batches 396–400 and enrich the next 4–12 genuinely under-detailed canonical records, synchronizing both canonical layers and cross-domain provenance in the same cycle.


### 2026-09-25 cycle completion — Skill Research Batch 401 mechanics enrichment
- [x] Fresh 474-record frontier excluding Batches 396–400 selected **Fighting Pose I, Fighting Pose B, Fighting Pose D, and Android Rush**.
- [x] Deepened all four mechanics records with current Xenoverse 2-specific effect, sequence, duration, directional, and documented-damage details where directly supported.
- [x] Synchronized canonical `skills.json` and `skills-index.json`; all four remain `verified_current_scope` with 2026-09-25 verification.
- [x] Added `skill-research-batches/skill-batch-401.json` and registered it in the cross-domain registry.
- [x] Evidence boundaries preserved: unresolved multipliers, exact frames, hidden prerequisites, and reward probabilities were not inferred.
- [ ] CI remains unverified; no workflow success is claimed.
- [x] **Exact next:** continue Batch 401 with the next four genuinely under-detailed records from the fresh frontier, then complete the handoff entry after the full batch is finished.


### 2026-09-25 cycle completion — Skill Research Batch 401 continued
- [x] Completed the next four Batch 401 frontier records: **Scissors Paper Rock, Rocket Tackle, Holy Inscription, and Shining Slash**.
- [x] Deepened all four mechanics records with current Xenoverse 2-specific sequence, branching/input behavior, charge/chase behavior, hit counts, documented damage, and restriction details where directly supported.
- [x] Synchronized canonical `skills.json` and `skills-index.json`; all four remain `verified_current_scope` with 2026-09-25 verification.
- [x] Expanded `skill-research-batches/skill-batch-401.json` to the complete eight-record batch and added four current-evidence audits; registered them in the cross-domain registry.
- [x] Evidence boundaries preserved: exact frame timings, multipliers, reward probabilities, and unresolved stack/charge timing were not inferred.
- [ ] CI remains unverified; no workflow success is claimed.
- [x] **Exact next:** run a fresh 474-record census excluding Batches 396–401 and begin Batch 402 with the next 4–12 genuinely under-detailed records.


### 2026-09-25 cycle completion — Skill Research Batch 402 started
- [x] Fresh 474-record census excluding Batches 396–401 selected **Recoome Kick, Dual Destructo-Disc, Spirit Blaster, and Chain Destructo-Disc Barrage** as the next four genuinely under-detailed mechanics records.
- [x] Deepened all four canonical mechanics records with current Xenoverse 2-specific sequence, projectile/strike behavior, hit counts, documented damage, acquisition, and relevant character availability where directly supported.
- [x] Synchronized canonical `skills.json` and `skills-index.json`; all four remain `verified_current_scope` with 2026-09-25 verification.
- [x] Added `skill-batch-402.json` and four current-evidence audits; registered the batch in the cross-domain registry.
- [x] Evidence boundaries preserved: unresolved boost magnitudes, exact frames, tracking strength, exact Spirit Blaster damage/timing, and hidden probabilities were not inferred.
- [ ] CI remains unverified; no workflow success is claimed.
- [x] **Exact next:** continue Batch 402 with the next genuinely under-detailed records from the fresh frontier, beginning after these four.


### 2026-09-25 cycle completion — Skill Research Batch 402 continued
- [x] Completed the next four Batch 402 frontier records: **Turn Golden, Fighting Pose A, Shining Friday, and Savory Slicer**.
- [x] Deepened all four canonical mechanics records with current Xenoverse 2-specific transformation/effect, defensive status, attack sequence, documented duration/damage, and acquisition details where directly supported.
- [x] Synchronized canonical `skills.json` and `skills-index.json`; all four remain `verified_current_scope` with 2026-09-25 verification.
- [x] Expanded `skill-research-batches/skill-batch-402.json` to eight records and added four current-evidence audits; registry remains synchronized.
- [x] Evidence boundaries preserved: unresolved transformation timing, exact drain/combo multipliers, Shining Friday numerical mechanics, and activation/frame data were not inferred.
- [ ] CI remains unverified; no workflow success is claimed.
- [x] **Exact next:** continue Batch 402 with the next genuinely under-detailed records from the fresh frontier, beginning after these eight.


### 2026-09-25 TODO progress update — Skill Research Batch 403 completed

- [x] Fresh live 474-record frontier census excluded Batches 396–402 and selected **Buu Buu Ball, Dodoria Headbutt, Dodoria Launcher, and Elite Shooting** as the next shortest genuinely under-detailed mechanics records.
- [x] Enriched and synchronized canonical `docs/data/skills.json` and projection `docs/data/skills-index.json`; all four now carry `last_verified: 2026-09-25`, `research_status: enriched`, and `verified_current_scope`.
- [x] Added four current-evidence audits, `docs/data/skill-research-batches/skill-batch-403.json`, and `docs/data/skill-batch-403-thin-frontier-mechanics-audit-2026-09-25.json`; registered all artifacts in `docs/data/pq-cross-domain-index.json`.
- [x] Evidence boundaries preserved: no unsupported frame, timing, tracking, reward-probability, or patch-independent damage claims were promoted.
- [x] Validation performed in-memory before write: canonical/index record counts remain 474/474 and the four target IDs are present in both layers with synchronized mechanics strings.
- [ ] CI/build status remains unverified; no workflow success is claimed.
- [x] **Exact next:** run a fresh 474-record frontier census excluding Batches 396–403 and enrich the next 4–12 shortest genuinely under-detailed records, synchronizing canonical/index/provenance in the same cycle.


### 2026-09-25 TODO progress update — Batch 404 frontier selected
- [x] Fresh 474-record mechanics census after Batch 403 selected Feint Shot, Fighting Pose K, Justice Pose, and Dust Attack as the next thin frontier.
- [ ] Canonical/index write is pending due a GitHub contents API conflict on the large skills files; no completion is claimed yet.
- [x] Evidence review completed for the four selected skills.
- [x] Exact next after write recovery: synchronize canonical/index, add Batch 404 audits and provenance, then continue the next frontier.


### 2026-09-25 TODO progress update — Skill Research Batch 404 completed
- [x] Recovered the large Git-object write path for `skills.json`/`skills-index.json` by fetching their full blobs and writing through a new Git tree instead of the Contents API.
- [x] Enriched and synchronized **Feint Shot, Fighting Pose K, Justice Pose, and Dust Attack** in canonical and projection data; canonical/index remain 474/474.
- [x] Added/replaced the four current-evidence audits and Batch 404 artifacts and retained provenance registration.
- [x] Evidence boundaries preserved: unsupported exact frames, timing, tracking, damage, and cancel windows remain unresolved rather than being inferred.
- [ ] CI/build remains unverified; no workflow success is claimed.
- [x] **Exact next:** fresh 474-record census excluding Batches 396–404, then enrich the next 4–12 shortest genuinely under-detailed records and synchronize canonical/index/provenance in the same cycle.


### 2026-09-25 TODO progress update — Skill Research Batch 405 completed
- [x] Fresh 474-record frontier census after Batch 404 selected **Dynamite Kick, Super Saiyan, Burst Stinger, and Destruction's Concerto: Starfall** as the next shortest genuinely under-detailed records.
- [x] Enriched and synchronized canonical `docs/data/skills.json` and projection `docs/data/skills-index.json`; canonical/index remain 474/474.
- [x] Added four current-evidence audits, Batch 405 research data, thin-frontier audit, and provenance registry entries.
- [x] Evidence boundaries preserved; version-sensitive stat/damage values are explicitly bounded rather than presented as timeless balance facts.
- [ ] CI/build remains unverified; no workflow success is claimed.
- [x] **Exact next:** fresh 474-record census excluding Batches 396–405, then enrich the next 4–12 shortest genuinely under-detailed records and synchronize canonical/index/provenance.


### 2026-09-25 TODO progress update — Skill Research Batch 406 completed
- [x] Fresh 474-record frontier census after Batch 405 selected **Dodon Ray, Rebellion Spear, Dragon Burn, and Impulse Slash** as the next four shortest genuinely under-detailed records.
- [x] Enriched and synchronized canonical `docs/data/skills.json`, projection `docs/data/skills-index.json`, and provenance registry; canonical/index remain 474/474.
- [x] Added four Batch 406 current-evidence audits plus batch and thin-frontier audit artifacts.
- [x] Historical patch notes/community interaction reports were bounded as contextual evidence rather than promoted into timeless balance claims.
- [ ] CI/build remains unverified; no workflow success is claimed.
- [x] **Exact next:** fresh 474-record census excluding Batches 396–406, then enrich the next 4–12 shortest genuinely under-detailed records and synchronize canonical/index/provenance in the same cycle.


### 2026-09-25 TODO progress update — Skill Research Batch 407 completed
- [x] Fresh 474-record frontier census after Batch 406 selected **Death Crasher, Spirit Explosion, Ki Blast Thrust, and Dodoria Beam** as the next four shortest genuinely under-detailed records.
- [x] Enriched and synchronized canonical `docs/data/skills.json`, projection `docs/data/skills-index.json`, and provenance registry; canonical/index remain 474/474.
- [x] Added four Batch 407 current-evidence audits plus batch and thin-frontier audit artifacts.
- [x] Evidence boundaries preserved; exact current frames, damage, tracking, and cancel windows remain unresolved where not directly established.
- [ ] CI/build remains unverified; no workflow success is claimed.
- [x] **Exact next:** fresh 474-record census excluding Batches 396–407, then enrich the next 4–12 shortest genuinely under-detailed records and synchronize canonical/index/provenance in the same cycle.


### 2026-09-26 TODO progress update — Skill Research Batch 417 completed
- [x] Fresh 474-record mechanics frontier census excluded Batches 396–416 and selected **Rolling Bullet, Innocence Breath, Tri-Beam, Demon Flurry, Destructo-Disc, Ice Cannon, Super God Fist, Revenge Final Flash, Saturday Crash, Destruction's Conductor, Present For You, and Tyrant Lancer** as the next twelve shortest genuinely under-detailed records.
- [x] Enriched and synchronized canonical `docs/data/skills.json` and projection `docs/data/skills-index.json`; canonical/index remain 474/474.
- [x] Added twelve current-evidence audits, Batch 417 research data, thin-frontier audit, and provenance registry entries.
- [x] Evidence boundaries preserved; unsupported exact frames, hidden conditions, tracking parameters, patch-independent scaling, and outcome probabilities remain unresolved rather than inferred.
- [ ] CI/build remains unverified; no workflow success is claimed.
- [x] **Exact next:** fresh 474-record census excluding Batches 396–417, then enrich the next 4–12 shortest genuinely under-detailed records and synchronize canonical/index/provenance.


### 2026-09-26 TODO progress update — Skill Research Batch 418 completed
- [x] Fresh 474-record mechanics frontier census excluded Batches 396–417 and selected **Elegant Blaster, Candy Beam, Kamehameha, Prepare to be Punished, Wild Stinger, Dragon Blitz, Elite Beam, Solar Flare, The Savior Has Come, Wolf Fang Fist, Volleyball Fist, Fighting Pose F** as the next twelve shortest genuinely under-detailed records.
- [x] Enriched and synchronized canonical `docs/data/skills.json` and projection `docs/data/skills-index.json`; canonical/index remain 474/474.
- [x] Added twelve current-evidence audits, Batch 418 research data, thin-frontier audit, and provenance registry entries.
- [x] Evidence boundaries preserved; unsupported exact frames, hidden conditions, patch-independent scaling, and unresolved status-effect values remain unresolved rather than inferred.
- [ ] CI/build remains unverified; no workflow success is claimed.
- [x] **Exact next:** fresh 474-record census excluding Batches 396–418, then enrich the next 4–12 shortest genuinely under-detailed records and synchronize canonical/index/provenance.


### 2026-09-26 continuation — Skill Research Batch 421 completed

- [x] Fresh live 474-record mechanics frontier census identified the next genuinely under-detailed records without an existing research audit: **Hero's Pose, Rolling Hercule Punch, x10 Kamehameha, Justice Drive, Pretty Cannon, Super Ghost Kamikaze Attack (Ultimate), Emperor's Edge, and Energy Shot**.
- [x] Enriched and synchronized canonical `docs/data/skills.json` and projection `docs/data/skills-index.json` for all eight; canonical/index remain 474/474.
- [x] Added Batch 421 research data plus eight current-evidence audit files and registered them in `docs/data/pq-cross-domain-index.json`.
- [x] Evidence boundaries preserved: exact frames, hidden interactions, unsupported multipliers, patch-independent balance, and unsupported probabilities were not inferred.
- [ ] CI/build remains unverified; no workflow success is claimed.
- [x] **Exact next:** run a fresh 474-record frontier census excluding Batches 396–421, excluding records with any prior audit, then enrich the next 4–12 shortest genuinely under-detailed records and synchronize canonical/index/provenance in the same cycle.


### 2026-09-26 continuation — Skill Research Batch 422 completed

- [x] Fresh live 474-record frontier census excluding prior audited records identified the next eight shortest genuinely under-detailed records: **Audacious Laugh, Burning Shot, Divinity Unleashed, Divine Wrath: Purification, Pure Progress, Critical Upper, Prelude to Destruction, and Death Slash**.
- [x] Enriched and synchronized canonical `docs/data/skills.json` and projection `docs/data/skills-index.json`; canonical/index remain 474/474.
- [x] Added Batch 422 research data plus eight current-evidence audit files and registered every audit in `docs/data/pq-cross-domain-index.json`.
- [x] Preserved evidence boundaries: exact frames, hidden interactions, unsupported scaling, patch-independent balance, and unsupported reward probabilities were not inferred.
- [ ] CI/build remains unverified; no workflow success is claimed.
- [x] **Exact next:** run another fresh 474-record frontier census excluding Batches 396–422 and any record with a prior audit, then enrich the next 4–12 shortest genuinely under-detailed canonical mechanics records with synchronized canonical/index/provenance updates.


Batch 423 completed: eight skill mechanics records were enriched and synchronized. Next task: fresh 474-record frontier census excluding prior audited records and continue the shortest under-detailed records. CI/build remains unverified.


### 2026-09-26 TODO progress update — Skill Research Batch 438 completed

- [x] Fresh 474-record mechanics frontier census excluded every skill with a registered current-evidence audit and selected **Final Flash (SS3 DAIMA), God of Destruction's Anger, Evil Ray Strike, and Pretty Charge**.
- [x] Enriched and synchronized all four records in `docs/data/skills.json` and `docs/data/skills-index.json`; canonical/index remain 474/474 with 0 missing / 0 extra.
- [x] Added four current-evidence audits, Batch 438 research data, thin-frontier audit, and provenance registry entries.
- [x] Preserved evidence boundaries: exact frames, unsupported scaling, hidden interactions, exact charge/resource conversion, and unsupported reward probabilities remain unresolved where not directly evidenced.
- [ ] CI/build status remains unverified; no workflow success is claimed.
- [ ] Repository efficiency addendum check remains blocked because `docs/AI-CONTINUATION-PROMPT-EFFICIENCY-ADDENDUM.md` currently returns GitHub 404.
- [x] **Exact next:** run another fresh unaudited mechanics frontier census excluding Batch 438 and every prior current-evidence-audited record, then continue the canonical research/synchronization cycle.


### 2026-09-26 TODO progress update — Skill Research Batch 439 completed
- [x] Fresh 474-record mechanics frontier census excluded records with registered current-evidence audits and selected **Blades of Judgment, Sudden Death Beam, Super Saiyan God, and Change The Future** as the next shortest genuinely under-detailed records.
- [x] Enriched and synchronized all four records in `docs/data/skills.json` and `docs/data/skills-index.json`; canonical/index remain 474/474.
- [x] Added four current-evidence audits, `docs/data/skill-research-batches/skill-batch-439.json`, the Batch 439 thin-frontier audit, and six provenance registry entries.
- [x] Preserved evidence boundaries: exact frames, unsupported scaling, hidden interactions, exact drop probabilities, and unresolved combo coverage remain unresolved unless directly evidenced.
- [x] Preserved two documented source discrepancies instead of silently normalizing them: Blades of Judgment's secondary "Super Skill" label versus the canonical Ultimate classification, and Change The Future's in-game Strike wording versus documented Ki Blast counter behavior.
- [ ] CI/build status remains unverified; no workflow success is claimed.
- [ ] Repository efficiency addendum remains unavailable at the expected path; GitHub returns 404.
- [x] **Exact next:** run another fresh unaudited mechanics frontier census excluding Batch 439 and every prior current-evidence-audited record, then continue the canonical research/synchronization cycle.


### 2026-09-26 TODO progress update — Skill Research Batch 440 completed
- [x] Fresh 474-record unaudited mechanics frontier census selected **Paralyze Beam, Super Afterimage, Flash Strike, and Finishing Blow** as the next four shortest under-detailed records.
- [x] Enriched and synchronized all four records in `docs/data/skills.json` and `docs/data/skills-index.json`; canonical/index remain 474/474.
- [x] Added four current-evidence audits, Batch 440 research data, thin-frontier audit, and six provenance registry entries.
- [x] Preserved evidence boundaries: exact frames, exact damage/scaling, exact drop probabilities, hidden conditions, and formalization of community timing techniques remain unresolved where not directly evidenced.
- [ ] CI/build status remains unverified; no workflow success is claimed.
- [ ] Repository efficiency addendum remains unavailable at the expected path; GitHub returns 404.
- [x] **Exact next:** run another fresh unaudited mechanics frontier census excluding Batch 440 and every prior current-evidence-audited record, then continue the canonical research/synchronization cycle.


### 2026-09-26 TODO progress update — Skill Research Batch 441 completed
- [x] Fresh 474-record unaudited mechanics frontier census selected **Blaster Ball, Super Kamehameha (SS4 DAIMA), Paralysis, and Perfect Kamehameha**.
- [x] Enriched/synchronized all four canonical skill records and added four current-evidence audits plus Batch 441 research/frontier artifacts.
- [x] Registered all six Batch 441 artifacts in `docs/data/pq-cross-domain-index.json`; registry now contains 648 entries.
- [x] Preserved source-reported numerical claims as source-reported rather than patch-independent canonical values; unsupported frames, scaling, probabilities, and hidden conditions remain unresolved.
- [ ] CI/build remains unverified; no workflow success is claimed.
- [ ] `docs/AI-CONTINUATION-PROMPT-EFFICIENCY-ADDENDUM.md` remains unavailable at the expected path (GitHub 404).
- [x] **Exact next:** run another fresh unaudited mechanics frontier census excluding Batch 441 and every prior current-evidence-audited record, then continue the canonical research/synchronization cycle.


### 2026-09-26 TODO progress update — Skill Research Batch 442 completed
- [x] Fresh 474-record unaudited mechanics frontier census selected **Final Rampage, Formation!, Blaster Meteor, and Weekend**.
- [x] Enriched/synchronized all four canonical skill records and added four current-evidence audits plus Batch 442 research/frontier artifacts.
- [x] Registered all six Batch 442 artifacts; provenance registry now contains 654 entries.
- [x] Preserved source-reported damage/duration/probability values as source-bound and did not infer unsupported frame data, hidden gates, or patch-independent scaling.
- [ ] CI/build remains unverified; no workflow success is claimed.
- [ ] Efficiency addendum remains unavailable at expected path (GitHub 404).
- [x] **Exact next:** run another fresh unaudited mechanics frontier census excluding Batch 442 and every prior current-evidence-audited record, then continue the canonical research/synchronization cycle.


### 2026-09-26 TODO progress update — Skill Research Batch 443 completed
- [x] Fresh 474-record unaudited mechanics frontier census selected **Gigantic Omega, Gigantic Meteor, Meditation, and Brave Sword Attack**.
- [x] Enriched/synchronized all four canonical skill records and added four current-evidence audits plus Batch 443 research/frontier artifacts.
- [x] Registered all six Batch 443 artifacts; provenance registry now contains 660 entries.
- [x] Preserved source-reported numerical damage values as source-bound and did not infer unsupported frames, scaling, probabilities, or hidden conditions.
- [ ] CI/build remains unverified; no workflow success is claimed.
- [ ] Efficiency addendum remains unavailable at expected path (GitHub 404).
- [x] **Exact next:** run another fresh unaudited mechanics frontier census excluding Batch 443 and every prior current-evidence-audited record, then continue the canonical research/synchronization cycle.


### 2026-09-26 TODO progress update — Skill Research Batch 443 completed
- [x] Fresh 474-record unaudited mechanics frontier census selected **Gigantic Omega, Gigantic Meteor, Meditation, and Brave Sword Attack**.
- [x] Enriched/synchronized all four canonical skill records and added four current-evidence audits plus Batch 443 research/frontier artifacts.
- [x] Registered all six Batch 443 artifacts; provenance registry now contains 660 entries.
- [x] Preserved source-reported numerical damage values as source-bound and did not infer unsupported frames, scaling, probabilities, or hidden conditions.
- [ ] CI/build remains unverified; no workflow success is claimed.
- [ ] Efficiency addendum remains unavailable at expected path (GitHub 404).
- [x] **Exact next:** run another fresh unaudited mechanics frontier census excluding Batch 443 and every prior current-evidence-audited record, then continue the canonical research/synchronization cycle.


### 2026-09-26 TODO progress update — Skill Research Batch 444 completed
- [x] Fresh 474-record unaudited mechanics frontier census excluded every skill with a registered current-evidence audit and selected **Flash Fist Crush, Final Flash (Super), Evil Eyes, and Maximum Charge**.
- [x] Enriched and synchronized all four canonical skill records in `docs/data/skills.json` and `docs/data/skills-index.json`; canonical/index remain 474/474 with 0 missing / 0 extra.
- [x] Added four current-evidence audits, `docs/data/skill-research-batches/skill-batch-444.json`, the Batch 444 thin-frontier audit, and six provenance registry entries.
- [x] Preserved evidence boundaries: source-reported damage and relative charge-speed claims remain source-bound; unsupported frames, scaling, probabilities, tracking-strength values, and hidden conditions were not inferred.
- [ ] CI/build status remains unverified; no workflow success is claimed.
- [ ] Repository efficiency addendum remains unavailable at the expected path; GitHub returns 404.
- [x] **Exact next:** run another fresh unaudited mechanics frontier census excluding Batch 444 and every prior current-evidence-audited record, then continue the canonical research/synchronization cycle.


### 2026-09-26 TODO progress update — Skill Research Batch 445 completed
- [x] Researched **Quick Sleep, Fake Death, Meteor Burst, and Punisher Shield**.
- [x] Corrected Quick Sleep from 0 Ki to 300 Ki.
- [x] Canonical/index parity remains 474/474.
- [x] Added four audits, Batch 445 research, thin-frontier audit, and provenance entries.
- [ ] CI/build remains unverified.
- [x] **Exact next:** fresh unaudited mechanics frontier excluding Batch 445 and all prior audited records.


### 2026-09-26 TODO progress update — Skill Research Batch 446 completed
- [x] Researched **Giant Storm, God Splitter, Final Flash (Super), and Menacing Flare**.
- [x] Enriched/synchronized canonical and index datasets; parity **474/474**, 0 missing / 0 extra.
- [x] Added four current-evidence audits, Batch 446 research/thin-frontier artifacts, and provenance registrations.
- [x] Evidence boundaries preserved; unsupported exact frames, scaling, probabilities, and hidden conditions were not inferred.
- [ ] CI/build remains unverified.
- [ ] Efficiency addendum remains unavailable at expected path (GitHub 404).
- [x] **Exact next:** fresh unaudited mechanics frontier excluding Batch 446 and all prior current-evidence-audited records.


### 2026-09-26 TODO progress update — Skill Research Batch 447 completed
- [x] Researched **Hell Flash, Ice Cannon, Kill Driver, and Feint Crash**.
- [x] Enriched/synchronized canonical and index datasets; parity **474/474**, 0 missing / 0 extra.
- [x] Added four current-evidence audits, Batch 447 research/thin-frontier artifacts, and provenance registrations.
- [x] Preserved evidence boundaries; secondary Kill Driver damage observations remain source-reported rather than canonical constants.
- [ ] CI/build remains unverified.
- [ ] Efficiency addendum remains unavailable at expected path (GitHub 404).
- [x] **Exact next:** fresh unaudited mechanics frontier excluding Batch 447 and all prior current-evidence-audited records.


### 2026-09-26 TODO progress update — Skill Research Batch 448 completed
- [x] Fresh 474-record mechanics frontier census excluded every skill with a registered current-evidence audit and selected **Wild Buster, Blaster Bomb, Divine Spear, Hyper Tornado, Angry Hit, Meteor Strike, Mystic Flash, and Wall of Defense**.
- [x] Enriched and synchronized all eight records in `docs/data/skills.json` and `docs/data/skills-index.json`; canonical/index remain 474/474 with 0 missing / 0 extra.
- [x] Added eight current-evidence audits, `docs/data/skill-research-batches/skill-batch-448.json`, the Batch 448 thin-frontier audit, and provenance registry entries; registry now contains 694 entries.
- [x] Preserved evidence boundaries: source-reported damage and behavioral values remain source-bound; unsupported exact frames, scaling, probabilities, and hidden conditions remain unresolved.
- [ ] CI/build status remains unverified; no workflow success is claimed.
- [ ] Efficiency addendum remains unavailable at the expected path (GitHub 404).
- [x] **Exact next:** run another fresh unaudited mechanics frontier census excluding Batch 448 and every prior current-evidence-audited record, then continue the canonical research/synchronization cycle.


### 2026-09-26 TODO progress update — Skill Research Batch 449 completed
- [x] Fresh 474-record mechanics frontier census excluded every skill with a registered current-evidence audit and selected **Purification, Brave Sword Slash, Unrelenting Barrage, Burning Slash, Turn Golden, Gigantic Explosion, Burst Blitz, and Power Pole Pro**.
- [x] Enriched and synchronized all eight records in `docs/data/skills.json` and `docs/data/skills-index.json`; canonical/index remain 474/474 with 0 missing / 0 extra.
- [x] Added eight current-evidence audits, `docs/data/skill-research-batches/skill-batch-449.json`, the Batch 449 thin-frontier audit, and provenance registry entries.
- [x] Preserved evidence boundaries: source-reported values remain source-bound; unsupported exact frames, scaling, probabilities, and hidden conditions remain unresolved.
- [ ] CI/build status remains unverified; no workflow success is claimed.
- [ ] Efficiency addendum remains unavailable at the expected path (GitHub 404).
- [x] **Exact next:** run another fresh unaudited mechanics frontier census excluding Batch 449 and every prior current-evidence-audited record, then continue the canonical research/synchronization cycle.


### 2026-09-26 TODO progress update — Skill Research Batch 450 completed
- [x] Fresh 474-record mechanics frontier census excluded every skill with a registered current-evidence audit and selected **Ray Blast, Emperor's Blast, Final Cannon, Godly Chronos Cannon, Vanishing Ball, Evil Whirlwind, God of Destruction's Rampage, and Emperor's Death Beam**.
- [x] Enriched and synchronized all eight records in `docs/data/skills.json` and `docs/data/skills-index.json`; canonical/index remain 474/474 with 0 missing / 0 extra.
- [x] Added eight current-evidence audits, `docs/data/skill-research-batches/skill-batch-450.json`, the Batch 450 thin-frontier audit, and provenance registry entries.
- [x] Corrected stale Emperor's Blast attribution/mechanics wording from Hercule to Frieza/Golden Frieza using current skill evidence.
- [x] Preserved evidence boundaries: source-reported values remain source-bound; unsupported exact frames, scaling formulas, probabilities, and hidden conditions remain unresolved.
- [ ] CI/build status remains unverified; no workflow success is claimed.
- [ ] Efficiency addendum remains unavailable at the expected path (GitHub 404).
- [x] **Exact next:** run another fresh unaudited mechanics frontier census excluding Batch 450 and every prior current-evidence-audited record, then continue the canonical research/synchronization cycle.


### 2026-09-26 TODO progress update — Skill Research Batch 451 completed
- [x] Fresh 474-record mechanics frontier selected **Force Shield, Eraser Bomb, Evil Flame, Galactic Donuts, Energy Field, Bloody Counter, Supersonic Mode, and Big Bang Attack**.
- [x] Enriched and synchronized all eight records; canonical/index remain 474/474 with 0 missing / 0 extra.
- [x] Added eight audits, Batch 451 research/thin-frontier artifacts, and provenance entries.
- [ ] CI/build remains unverified.
- [x] **Exact next:** fresh unaudited mechanics frontier census excluding Batch 451 and all prior current-evidence-audited records.


### 2026-09-26 TODO progress update — Skill Research Batch 451 completed
- [x] Completed eight fresh frontier mechanics enrichments: Force Shield; Eraser Bomb; Evil Flame; Galactic Donuts; Energy Field; Bloody Counter; Supersonic Mode; Big Bang Attack.
- [x] Added eight evidence audits and Batch 451 research/frontier artifacts.
- [x] Synchronized canonical/index skill datasets; 474/474 with 0 missing / 0 extra.
- [x] Registered Batch 451 provenance.
- [ ] CI/build remains unverified.
- [x] Next: continue the fresh unaudited mechanics frontier.


### 2026-09-26 TODO progress update — Skill Research Batch 452 completed
- [x] Fresh 474-record mechanics frontier census excluded every skill with a registered current-evidence audit and selected **Orin Combo, Comet Strike, Meteor Crash, Assault Vanish, God of Destruction's Might, Psychic Move, Special Beam Cannon, and Impact Flare**.
- [x] Enriched and synchronized all eight records in `docs/data/skills.json` and `docs/data/skills-index.json`; canonical/index remain 474/474 with 0 missing / 0 extra.
- [x] Added eight current-evidence audits, Batch 452 research data, thin-frontier audit, and provenance registrations.
- [x] Preserved evidence boundaries: source-reported values remain source-bound; unsupported exact frames, scaling, probabilities, and hidden conditions remain unresolved unless directly evidenced.
- [ ] CI/build status remains unverified; no workflow success is claimed.
- [ ] Repository efficiency addendum remains unavailable at the expected path; GitHub returns 404.
- [x] **Exact next:** run another fresh unaudited mechanics frontier census excluding Batch 452 and every prior current-evidence-audited record, then continue the canonical research/synchronization cycle.


### 2026-09-26 TODO progress update — Skill Research Batch 453 completed
- [x] Fresh 474-record unaudited mechanics frontier census selected **Super Spirit Bomb, Reverse Launcher, Ultrasonic Blitz, Dragon Spiral, Destructive Fracture, Crush Cannon, Burning Blast, and Instant Transmission**.
- [x] Enriched and synchronized all eight canonical/index skill records; parity remains **474/474** with 0 missing / 0 extra.
- [x] Added Batch 453 research/thin-frontier artifacts, eight current-evidence audits, and provenance registrations.
- [x] Preserved evidence boundaries: source-reported values remain source-bound; unsupported exact frames, scaling, probabilities, and hidden conditions remain unresolved unless directly evidenced.
- [ ] CI/build remains unverified; no workflow success is claimed.
- [ ] Repository efficiency addendum remains unavailable at the expected path; GitHub returns 404.
- [x] **Exact next:** run another fresh unaudited mechanics frontier census excluding Batch 453 and every prior current-evidence-audited record, then continue the canonical research/synchronization cycle.


### 2026-09-26 TODO progress update — Skill Research Batch 454 completed
- [x] Researched **Evil Flight Strike, Meteor Blow, Secret Poison, Blaster Stream, Dead End Rain, Divine Ray Bomb, Ultimate Charge, and Punisher Guard**.
- [x] Enriched/synchronized canonical and index datasets; parity remains **474/474**, 0 missing / 0 extra.
- [x] Added Batch 454 research/thin-frontier artifacts, eight current-evidence audits, and provenance registrations.
- [x] Preserved evidence boundaries; unsupported exact frames, scaling, probabilities, and hidden conditions remain unresolved unless directly evidenced.
- [ ] CI/build remains unverified.
- [x] **Exact next:** fresh unaudited mechanics frontier excluding Batch 454 and all prior current-evidence-audited records.


### 2026-09-26 TODO progress update — Skill Research Batch 455 completed
- [x] Researched **Super Donut Volley, Dimension Cannon, Divine Kamehameha, Petrifying Spit, Meteor Explosion, Circle Flash, Stone Bullet, and Blue Hurricane**.
- [x] Enriched/synchronized canonical and index datasets; parity remains **474/474**, 0 missing / 0 extra.
- [x] Added Batch 455 research/thin-frontier artifacts, eight current-evidence audits, and provenance registrations.
- [x] Preserved evidence boundaries; unsupported exact frames, scaling, probabilities, and hidden conditions remain unresolved unless directly evidenced.
- [ ] CI/build remains unverified.
- [x] **Exact next:** fresh unaudited mechanics frontier excluding Batch 455 and all prior current-evidence-audited records.


### 2026-09-26 TODO progress update — Skill Research Batch 456 completed
- [x] Researched **Data Input, Dimension Ray, Pressure Sign, Blaster Shell, Fake Blast, Spirit Boost, Dust Attack, and Teleporting Vanishing Ball**.
- [x] Enriched/synchronized canonical and index datasets; parity remains **474/474**, 0 missing / 0 extra.
- [x] Added Batch 456 research/thin-frontier artifacts, eight current-evidence audits, and provenance registrations.
- [x] Preserved evidence boundaries; unsupported exact frames, scaling, probabilities, and hidden conditions remain unresolved unless directly evidenced.
- [ ] CI/build remains unverified.
- [x] **Exact next:** fresh unaudited mechanics frontier excluding Batch 456 and all prior current-evidence-audited records.


### 2026-09-26 TODO progress update — Skill Research Batch 457 completed
- [x] Fresh 474-record mechanics frontier selected **Rough Ranger, X 100 Big Bang Kamehameha, Evil Blast, Final Charge, Explosive Wave, Force Edge, Ill Bomber, and Heavenly Arrow** as the next eight current-mechanics records after Batch 456.
- [x] Enriched/synchronized canonical and index skill records; parity remains **474/474**, 0 missing / 0 extra / 0 duplicate IDs.
- [x] Added Batch 457 research/thin-frontier artifacts, eight current-evidence audits, and provenance registrations.
- [x] Preserved evidence boundaries; unsupported exact frames, scaling, probabilities, hidden conditions, and narrower CaC restrictions remain unresolved unless directly evidenced.
- [ ] CI/build status remains unverified; no workflow success is claimed.
- [x] **Exact next:** perform another fresh unaudited mechanics frontier census excluding Batch 457 and every prior registered current-evidence audit.

### 2026-09-26 TODO progress update — Skill Research Batch 458 completed
- [x] Researched **Super Black Kamehameha Rosé, Warp Kamehameha, Dead End Bullet, Super Saiyan God Super Saiyan, Super Electric Strike, Ki Explosion, Final Explosion, and Powered Shell**.
- [x] Enriched/synchronized canonical and index datasets; parity remains **474/474**, 0 missing / 0 extra / 0 duplicate IDs.
- [x] Added Batch 458 research/thin-frontier artifacts, eight current-evidence audits, and provenance registrations.
- [x] Preserved evidence boundaries; unsupported exact frames, scaling, probabilities, and hidden conditions remain unresolved unless directly evidenced.
- [ ] CI/build remains unverified.
- [x] **Exact next:** fresh registered-audit mechanics frontier excluding Batch 458 and all prior current-evidence-audited records.

### 2026-09-26 TODO progress update — Skill Research Batch 459 completed
- [x] Researched **Meditation, Fighting Pose B, Gigantic Meteor, Weekend, Fighting Pose G, Fighting Pose I, Fighting Pose J, and Gigantic Omega**.
- [x] Enriched/synchronized canonical and index datasets; parity remains **474/474**, 0 missing / 0 extra / 0 duplicate IDs.
- [x] Added Batch 459 research/thin-frontier artifacts, eight current-evidence audits, and provenance registrations.
- [x] Preserved evidence boundaries; unsupported exact frames, scaling, probabilities, and hidden conditions remain unresolved unless directly evidenced.
- [ ] CI/build remains unverified.
- [x] **Exact next:** fresh mechanics frontier excluding Batch 459 and all prior current-evidence-audited records.

### 2026-09-26 TODO progress update — Skill Research Batch 460 completed
- [x] Researched **Angry Shout, Darkness Twin Star, Steel Mirage, Hyper Movement, Charge, Burning Swan, Scatter Kamehameha, and Energy Barrier**.
- [x] Enriched/synchronized canonical and index datasets; parity remains **474/474**, 0 missing / 0 extra / 0 duplicate IDs.
- [x] Added Batch 460 research/thin-frontier artifacts, eight current-evidence audits, and provenance registrations.
- [x] Preserved source conflicts and evidence boundaries; unsupported exact frames, probabilities, hidden conditions, and patch-independent scaling remain unresolved.
- [ ] CI/build remains unverified.
- [x] **Exact next:** fresh registered-audit mechanics frontier excluding Batch 460 and all prior current-evidence audits.

### 2026-09-26 TODO progress update — Skill Research Batch 461 completed
- [x] Researched **Flash Bomber, Genocide Shell, Spread Shot Retreat, Tail Slicer, Break Cannon, Burst Rush, Temporal Holy Ray, and Victory Rush**.
- [x] Enriched/synchronized canonical and index datasets; parity remains **474/474**, 0 missing / 0 extra / 0 duplicate IDs.
- [x] Added Batch 461 research/thin-frontier artifacts, eight current-evidence audits, and provenance registrations.
- [x] Preserved source conflicts and evidence boundaries; unsupported exact frames, probabilities, hidden conditions, and patch-independent scaling remain unresolved.
- [ ] CI/build remains unverified.
- [x] **Exact next:** fresh registered-audit mechanics frontier excluding Batch 461 and all prior current-evidence audits.

### 2026-09-26 TODO progress update — Skill Research Batch 462 completed
- [x] Fresh 474-record mechanics frontier census excluded every skill with a registered current-evidence audit and selected **Riot Javelin, Explosive Assault, Instant Severance, Super Kamehameha, Blaster Ball, Brave Sword Attack, Super Kamehameha (SS4 DAIMA), and Blaster Meteor**.
- [x] Enriched and synchronized all eight records in docs/data/skills.json and docs/data/skills-index.json; canonical/index remain **474/474** with 0 missing / 0 extra / 0 duplicate IDs.
- [x] Added Batch 462 research/thin-frontier artifacts, eight current-evidence audits, and provenance registrations; registry now contains **837 entries**.
- [x] Preserved evidence boundaries; source-reported numerical values remain source-bound and unsupported exact frames, scaling, probabilities, and hidden conditions remain unresolved.
- [ ] CI/build status remains unverified; no workflow success is claimed.
- [ ] Repository efficiency addendum remains unavailable at the expected path; GitHub returns 404.
- [x] **Exact next:** fresh unaudited mechanics frontier excluding Batch 462 and all prior current-evidence-audited records.


### 2026-09-26 TODO progress update — Skill Research Batch 463 completed
- [x] Researched **Final Rampage, Perfect Kamehameha, Shocking Death Ball, Spirit Sword, Super Afterimage, Hell Flash, Punisher Shield, and Fake Death**.
- [x] Enriched/synchronized canonical and index datasets; parity remains **474/474**.
- [x] Added Batch 463 research/thin-frontier artifacts, eight current-evidence audits, and provenance registrations.
- [x] Preserved evidence boundaries; unsupported exact frames, scaling, probabilities, hidden conditions, and patch-independent scaling remain unresolved.
- [ ] CI/build remains unverified.
- [x] **Exact next:** fresh unaudited mechanics frontier excluding Batch 463 and all prior current-evidence-audited records.


### 2026-09-26 TODO progress update — Skill Research Batch 464 completed
- [x] Researched **Paralyze Beam, Meteor Burst, Final Kamehameha, Justice Blade, Strike of Revelation, Variant Drive, Giant Storm, and Lightning of Absolution**.
- [x] Enriched/synchronized canonical and index datasets; parity remains **474/474**.
- [x] Added eight current-evidence audits, Batch 464 research/thin-frontier artifacts, and provenance registrations.
- [x] Preserved evidence boundaries; unsupported exact frames, scaling, probabilities, and hidden conditions remain unresolved.
- [ ] CI/build remains unverified.
- [x] **Exact next:** fresh unaudited mechanics frontier excluding Batch 464 and all prior current-evidence-audited records.


### 2026-09-26 TODO progress update — Skill Research Batch 465 completed
- [x] Researched **Drain Field, Menacing Flare, Quick Sleep, Mach Punch, Power Wall, Spirit Pulse, Finish Breaker, and Fighting Pose E**.
- [x] Enriched/synchronized canonical and index datasets; parity remains **474/474**.
- [x] Added eight current-evidence audits, Batch 465 research/thin-frontier artifacts, and provenance registrations.
- [x] Preserved evidence boundaries; unsupported exact frames, scaling, probabilities, and hidden conditions remain unresolved.
- [ ] CI/build remains unverified.
- [x] **Exact next:** fresh unaudited mechanics frontier excluding Batch 465 and all prior current-evidence-audited records.


### 2026-09-26 TODO progress update — Skill Research Batch 466 completed
- [x] Researched **Destructive Flare, Instant Charge, Lovely Cyclone, Milky Cannon, Dragon Fist, Sign of Awakening, Variable Snipe Shot, and Crush Stream**.
- [x] Enriched/synchronized canonical and index datasets; parity remains **474/474**, 0 missing / 0 extra / 0 duplicate IDs.
- [x] Added Batch 466 research/thin-frontier artifacts, eight current-evidence audits, and provenance registrations.
- [x] Preserved evidence boundaries; unsupported exact frames, scaling, probabilities, hidden conditions, and patch-independent scaling remain unresolved unless directly evidenced.
- [ ] CI/build remains unverified; no workflow success is claimed.
- [x] **Exact next:** fresh unaudited mechanics frontier excluding Batch 466 and all prior current-evidence-audited records.


### 2026-09-26 continuation — Batch 487 verification
- [x] Fresh live frontier census completed after Batch 486.
- [x] Rechecked current Xenoverse 2 evidence for Super Saiyan Blue Kaioken, Super Saiyan 2, Super Vegeta, and Namek Finger.
- [x] Canonical `skills.json` verification state was updated for those four records.
- [ ] Batch 487 research/provenance artifacts remain to be completed.
- [ ] CI/build remains unverified.
- [x] Next: complete Batch 487 artifact registration, then proceed to Bending Kamehameha → Flash Strike → Finishing Blow → Sudden Death Beam after a fresh census.

### 2026-09-26 TODO progress update — Partner character navigation recovery
- [x] Inspected Git history for the missing Partner Customization navigation artifacts and recovered the latest coherent historical versions.
- [x] Restored the Partner Customization page, 20-key record/reconciliation layers, canonical character layer, character identity bridge, navigation audit, and hardened validator.
- [x] Added `docs/data/partner-customization-character-navigation-recovery-audit-2026-09-26.json` and registered it in `docs/data/pq-cross-domain-index.json`.
- [x] Live reconciliation: **20 keys / 20 reconciliation records / 29 bridge records / 149 canonical character names / 20 page links / 0 failed checks / 0 identity mismatches**.
- [ ] Exact next: reconcile the recovered character/preset layer against remaining live character consumer artifacts before expanding Partner Customization skill relationships.
- [ ] CI/build remains unverified.


### 2026-09-26 TODO progress update — Character/preset consumer reconciliation
- [x] Restored the missing 51-record character preset layer and related consumer artifacts from coherent historical commits.
- [x] Synchronized the canonical character baseline to **152** records.
- [x] Extended the explicit identity bridge **29 → 34** with Bardock, Raditz, Nappa, Recoome, and Zarbon, resolving all **17** preset character IDs.
- [x] Added/registered the character-preset consumer reconciliation audit.
- [x] Audited the cross-domain provenance index against the live tree: **1,608 references, 713 reachable, 895 unreachable**; historical/planned references remain preserved.
- [x] Added/registered the cross-domain index reachability audit.
- [ ] CI/build remains unverified.
- [x] **Exact next:** prioritize critical cross-domain references that are safely regenerable from canonical data and required by live navigation/validators.


### 2026-09-26 TODO progress update — Skill Research Batch 492 completed
- [x] Researched **Absolute Zero, Afterimage Strike, Bending Kamehameha, Time Skip/Tremor Pulse, and Rising Rage** from a fresh post-Batch-491 frontier.
- [x] Enriched/synchronized canonical and index datasets; parity remains **474/474**, with 0 missing / 0 extra IDs.
- [x] Added five current-evidence audits plus Batch 492 research/thin-frontier artifacts and provenance registrations.
- [x] Preserved evidence boundaries; unsupported exact frames, probabilities, hidden conditions, and patch-independent scaling remain unresolved unless directly evidenced.
- [ ] CI/build remains unverified.
- [x] **Exact next:** fresh unaudited mechanics frontier before Batch 493; do not reuse the Batch 492 candidate list.


### 2026-09-26 TODO progress update — Skill Research Batch 493 completed


### 2026-09-26 TODO progress update — Skill Research Batch 494 completed
- [x] Researched **Super Saiyan, Volleyball Fist, Angry Explosion, Side Bridge, and Confusion Blade** from a fresh post-Batch-493 frontier.
- [x] Added five current-evidence audits plus Batch 494 research/thin-frontier artifacts and provenance registrations.
- [x] Canonical skill corpus remains **474 records**; current-evidence coverage is **364**, with **119 unaudited** after the fresh census.
- [x] Preserved evidence boundaries; unsupported exact frames, hidden conditions, probabilities, and patch-independent scaling remain unresolved.
- [ ] CI/build remains unverified.
- [x] **Exact next:** fresh unaudited mechanics frontier before Batch 495; do not reuse the Batch 494 candidate list.

### 2026-09-26 continuation — Character/navigation reference reconciliation completed
- [x] Re-read the live continuation/TODO state and followed the pending highest-impact cross-domain recovery task rather than starting another redundant skill mechanics batch.
- [x] Reconciled the six previously unreachable character/preset/navigation references: character identity bridge, current presentation consumer scan, Skills/Super Souls navigation audit, numeric preset complete-loadout audit, Partner Customization navigation audit, and its validator.
- [x] Recovered the two missing historical audit artifacts (Skills/Super Souls navigation and numeric preset complete-loadout audit) from their known provenance commits.
- [x] Corrected the stale current-character-consumer-scan-2026-09-24.json index reference to the live restored current-presentation-consumer-scan-2026-09-24.json artifact instead of creating a duplicate alias.
- [x] Synchronized the Partner Customization navigation audit to the repaired 34-record identity bridge / 152-name canonical character layer and updated its validator provenance.
- [x] Updated the character-reference existence audit from action-required/missing to reconciled/reachable, preserving its historical boundary.
- [x] Refreshed the cross-domain index reachability audit after the recovery pass: 707 live files / 1,608 references / 720 reachable / 888 unreachable; historical/planned references remain preserved.
- [x] No unsupported Partner Customization skill-to-partner edge was added; navigation identity remains separate from skill availability evidence.
- [ ] CI/build remains unverified; no workflow success is claimed.
- [ ] The efficiency addendum remains unavailable at the expected repository path (GitHub 404).
- [x] Exact next: inspect the remaining critical unreachable cross-domain references and regenerate only those that are both required by live navigation/validators and safely derivable from canonical data. In particular, prioritize docs/data/pq-reward-relationships.json and the PQ reverse/crosslink artifacts if their canonical source layers are sufficient; otherwise record an explicit evidence boundary instead of manufacturing them.

### 2026-09-26 continuation — Critical PQ forward-layer regeneration boundary checked
- [x] Checked the remaining highest-priority unreachable PQ forward/reverse artifacts after character/navigation recovery: `pq-reward-relationships.json`, `pq-skill-crosslink-report.json`, `characters/pq-reverse-index.json`, `dlc/pq-reverse-index.json`, and `farming/pq-farming-reverse-index.json` remain absent from the live tree.
- [x] Confirmed the live skill→PQ reverse layer is independently canonical and reproducible from `docs/data/skills.json` via `scripts/validate_skill_pq_crosslinks.py`; it must not be conflated with the absent general PQ reward forward layer.
- [x] Did not fabricate a replacement `pq-reward-relationships.json` from partial/derived indexes because the repository currently lacks a complete canonical PQ reward source sufficient to regenerate it without inference.
- [x] Preserved the existing 16-PQ unrepresented-endpoint evidence boundary: absence from the skill reverse index does not prove absence of PQ skill rewards.
- [ ] CI/build remains unverified.
- [x] **Exact next:** continue with another concrete, safely regenerable cross-domain artifact (or a live canonical navigation/consumer gap) rather than recreating the missing general PQ reward layer from incomplete evidence.

### 2026-09-26 continuation — Character consumer baseline hardening completed
- [x] Inspected the live character presentation consumer audit after the prior recovery and found stale embedded bridge counts (`29`) despite the live canonical bridge having **34** records.
- [x] Synchronized `docs/data/characters/character-presentation-consumer-audit.json` to the live **152-character / 34-bridge** baseline, including its Partner Customization navigation and hardening count sections.
- [x] Synchronized `docs/data/partner-customization-character-navigation-recovery-audit-2026-09-26.json` to **20 keys / 20 reconciliation records / 34 bridge records / 152 canonical character names**, preserving the clean validation result.
- [x] Confirmed the live deterministic skill→PQ reverse generator remains grounded exclusively in `docs/data/skills.json` and explicitly avoids inferring absent PQ skill endpoints.
- [x] No unsupported character identity, DLC ownership, unlock, reward, or Partner Customization skill relationship was added.
- [ ] CI/build remains unverified; no workflow success is claimed.
- [x] **Exact next:** continue the cross-domain consumer audit by locating the next live artifact whose cached counts/references are stale against canonical producers, and repair that deterministic mismatch before starting another large mechanics batch.

### 2026-09-26 continuation — Stale character-navigation cache repaired
- [x] Fresh live audit search found another stale cached baseline in `docs/data/characters/partner-customization-character-navigation-audit.json`: its embedded counts still said **29 bridge records / 151 canonical characters** after the live reconciliation had reached **34 / 152**.
- [x] Repaired that audit against the live canonical baseline: **20 keys / 20 reconciliation records / 34 bridge records / 152 canonical character names / 20 page links**.
- [x] Added an explicit reconciliation note documenting that the five restored preset-character mappings changed the aggregate bridge count, not the navigation identity mappings.
- [x] Rechecked the canonical skill cross-domain layer: **474 skills / 246 explicit skill→PQ edges / 170 represented PQ IDs** remains internally consistent; no stale 473-count artifact was found in the live canonical linkage layer.
- [x] No unsupported relationship was inferred.
- [ ] CI/build remains unverified.
- [x] **Exact next:** continue searching for stale cached cross-domain counts against canonical producers, prioritizing character/DLC/PQ consumer artifacts before resuming the mechanics frontier.

### 2026-09-26 continuation — Cross-domain reachability baseline refreshed
- [x] Recomputed `docs/data/cross-domain-index-reference-reachability-audit-2026-09-26.json` directly from the live `main` Git tree and `pq-cross-domain-index.json` rather than relying on stale search-index snapshots.
- [x] Current occurrence-count baseline: **729 live tree paths / 1,630 index references / 738 reachable / 892 unreachable**. The count convention matches the existing audit (reference occurrences, not unique paths).
- [x] The unreachable set remains dominated by historical/planned provenance; the five general PQ reward/reverse layers still lack a complete canonical reward source and were not fabricated.
- [x] Character/navigation references restored in this continuation are now part of the reachable baseline.
- [ ] CI/build remains unverified.
- [x] **Exact next:** use this refreshed baseline to identify the next genuinely live-required, safely regenerable cross-domain consumer gap; avoid spending cycles on stale search-index results or historical-only references.

### 2026-09-26 continuation — Nested character consumer cache repaired
- [x] Inspected the live `docs/data/characters/character-presentation-consumer-audit.json` in full after the previous synchronization and found a remaining nested Partner Customization projection still reporting **29 bridge records**.
- [x] Synchronized that nested projection to the canonical live **34 bridge records / 152 canonical character names** baseline. Top-level and standalone Partner Customization consumer projections now agree.
- [x] Revalidated the three live character-facing artifacts checked in this pass: canonical character count remains **152**, the character presentation audit reports **34 bridge records**, and the standalone Partner Customization navigation audit reports **34 bridge records**.
- [x] No character identity mapping, preset numbering, acquisition route, or unsupported relationship was inferred or changed.
- [ ] CI/build remains unverified.
- [x] **Exact next:** continue the same live-consumer audit for the next stale embedded scalar/reference, prioritizing DLC/PQ navigation consumers that are actually present in the live tree rather than historical index-only paths.



### 2026-09-26 TODO progress update — Partner skill relationship validator correction
- [x] Inspected the live Partner Customization skill relationship validator and found a concrete canonical-schema mismatch: the validator read `skill_id` from `docs/data/skills.json`, while the canonical skill corpus stores stable IDs in `id`.
- [x] Corrected `scripts/validate_partner_skill_relationships.py` to use the canonical `id` field.
- [x] Revalidated the relationship layer: **474 canonical skills / 3 partner-skill relationships / 3 unique pairs / 0 unknown targets / 0 duplicate pairs / 0 invalid relationship types / 0 missing evidence**; clean.
- [x] Added and registered `docs/data/partner-skill-relationship-validator-audit-2026-09-26.json`.
- [x] Refreshed cross-domain reachability after the new audit registration: **730 tree paths / 1,631 references / 739 reachable / 892 unreachable**.
- [x] No unsupported Partner Customization relationship was added.
- [ ] CI/build remains unverified; no workflow success is claimed.
- [ ] Efficiency addendum remains unavailable at the expected repository path (GitHub 404).
- [x] **Exact next:** inspect the remaining critical unreachable cross-domain references for a live-required, safely regenerable artifact; preserve historical/planned references and do not manufacture the absent general PQ reward layer from incomplete sources.


### 2026-09-26 TODO progress update — Partner evidence-path validation hardening
- [x] Hardened `scripts/validate_partner_skill_relationships.py` to verify every declared relationship evidence path exists in the live repository.
- [x] Rechecked all 3 Partner Customization skill relationships and all 6 evidence paths: **0 missing evidence files; clean**.
- [x] Updated the corresponding validator audit and maintained its cross-domain registration.
- [ ] CI/build remains unverified.
- [x] **Exact next:** continue from the remaining critical cross-domain references and prioritize a live-present DLC/PQ navigation consumer or safely regenerable reverse-navigation artifact.


### 2026-09-26 TODO progress update — Live-tree character consumer reconciliation
- [x] Confirmed the historical `scripts/validate_character_explorer.py` reference is not a live source-tree file; the active validator is `scripts/validate_character_presentation_consumers.py`.
- [x] Reconciled `docs/data/characters/character-presentation-consumer-audit.json` so its active consumer list names only the live presentation validator; documented generated HTML explorer artifacts as build outputs rather than source-tree invariants.
- [x] Updated the cross-domain reachability audit and persistent handoff with this distinction.
- [ ] CI/build remains unverified.
- [x] **Exact next:** inspect remaining critical unreachable references for stale/deleted validator registrations that can be safely reconciled without fabricating canonical PQ reward/reverse-index data.


### 2026-09-26 TODO progress update — Critical unreachable-reference reconciliation
- [x] Checked all 18 critical-unreachable cross-domain references against the live `main` tree.
- [x] Classified the 18 absent paths: 13 dated/historical audit snapshots; 5 primary/reverse dataset classes requiring evidence-complete sources before regeneration.
- [x] Added and registered `docs/data/critical-unreachable-reference-reconciliation-audit-2026-09-26.json`.
- [x] Preserved historical/provenance references; no unsupported dataset reconstruction was performed.
- [ ] CI/build remains unverified.
- [x] **Exact next:** inspect the next live, safely testable cross-domain validator or consumer and make a concrete integrity improvement.


### 2026-09-26 TODO progress update — Skill→PQ reverse projection drift guard
- [x] Hardened `scripts/validate_skill_pq_crosslinks.py` with exact checked-in reverse-index equality against the deterministic `skills.json → source_parallel_quests` projection.
- [x] Updated and registered the corresponding linkage audit.
- [x] This closes a concrete integrity gap where aggregate counts could pass despite individual PQ edge drift.
- [ ] CI/build remains unverified.
- [x] **Exact next:** inspect the next live cross-domain validator/consumer for an equivalent deterministic projection drift gap.


### 2026-09-26 continuation — Batch 494 frontier metadata reconciliation
- [x] Reconciled the stale Batch 494 mechanics-frontier scalar against the later full-corpus integrity audit.
- [x] Confirmed the live canonical skill corpus remains **474 records**, with **474 unique skill IDs represented by registered current-evidence audit paths** and **0 unaudited IDs** after stable-ID normalization.
- [x] Preserved the historical Batch 494 entry and its original 364/119 figures as historical context; they are no longer treated as the current frontier state.
- [x] Added and registered `docs/data/skill-mechanics-frontier-state-reconciliation-2026-09-26.json` documenting the correction and evidence boundary.
- [x] No canonical skill, mechanics, acquisition, or relationship data was changed by this reconciliation.
- [ ] CI/build/runtime execution remains unverified.
- [x] **Exact next:** continue deterministic cross-domain/provenance/data-integrity work; do not start Batch 495 from the stale 119-item list unless a fresh live census establishes genuinely unaudited canonical skill IDs.


### 2026-09-26 continuation — Absent DLC/PQ consumer registrations reconciled
- [x] Directly checked the remaining DLC/PQ consumer registrations named by the cross-domain index: `docs/data/dlc/dlc-presentation-consumer-audit.json`, `docs/data/pq-endpoint-navigation-current-audit-2026-09-24.json`, and `docs/data/pq-current-consumer-baseline-synchronization-2026-09-24.json` are absent from the live `main` tree.
- [x] Confirmed repository search resolves these names only through the cross-domain index; no live consumer file currently requires reconstruction.
- [x] Preserved the index references as historical/provenance records and did not manufacture replacements without a current producer/consumer contract.
- [x] Updated `docs/data/cross-domain-index-reference-reachability-audit-2026-09-26.json` with the direct absence check and evidence boundary.
- [ ] CI/build/runtime remains unverified.
- [x] **Exact next:** continue auditing live-present validators/consumers and deterministic projections for concrete drift; leave absent historical/index-only artifacts untouched unless a current source layer requires them.


### 2026-09-26 continuation — Skill acquisition validator hardening
- [x] Inspected the live `scripts/validate_skill_acquisition_metadata.py` and found a concrete acceptance bug: the TP Medal Shop rule accepted the misspelled token `stp medal shop` as valid.
- [x] Removed that accidental alternate; TP Medal Shop validation now requires the canonical `tp medal shop` phrase.
- [x] Updated and registered `docs/data/skill-acquisition-metadata-integrity-audit-2026-09-26.json`; the existing **474-record / 0 anomaly** audit remains the recorded result, and no canonical acquisition data was changed.
- [ ] CI/build/runtime remains unverified; the validator was hardened but no workflow success is claimed.
- [x] **Exact next:** continue inspecting live validators for concrete schema/acceptance gaps and harden them without inventing or changing unsupported canonical data.


### 2026-09-26 continuation — Skill acquisition PQ endpoint validation hardened
- [x] Found a second concrete acceptance gap in `scripts/validate_skill_acquisition_metadata.py`: non-empty `source_parallel_quests` values were previously accepted without validating type or supported PQ range.
- [x] Hardened the validator so every declared `source_parallel_quests` endpoint must be an integer in the supported **PQ 1–186** range.
- [x] Updated `docs/data/skill-acquisition-metadata-integrity-audit-2026-09-26.json` to record the new check; the live audit remains **474 records / 0 invalid endpoints / 0 metadata anomalies**.
- [x] Refreshed the existing cross-domain registration; no canonical skill data or unsupported PQ relationship was added.
- [ ] CI/build/runtime remains unverified.
- [x] **Exact next:** continue auditing live validators for concrete acceptance/schema gaps, prioritizing deterministic cross-domain integrity without reconstructing unsupported datasets.


### 2026-09-26 continuation — Partner skill relationship schema hardening
- [x] Found a live validator acceptance gap in `scripts/validate_partner_skill_relationships.py`: malformed relationship containers/records and malformed evidence values were not explicitly rejected, and an empty relationship corpus could pass structural checks.
- [x] Hardened the validator to require the current canonical **3 relationship records**, object-shaped records, list-shaped evidence, and non-empty string evidence paths before filesystem resolution.
- [x] Updated `docs/data/partner-skill-relationship-validator-audit-2026-09-26.json`; the current corpus remains clean with **3 relationships / 6 evidence files**.
- [x] No additional Partner Customization assignment or unsupported skill relationship was inferred.
- [ ] CI/build/runtime remains unverified.
- [x] **Exact next:** continue auditing the remaining live validators for concrete schema/acceptance gaps, without reconstructing unsupported canonical datasets.

### 2026-09-26 continuation — Skill↔PQ validator source-syntax repair
- [x] Re-inspected the live `scripts/validate_skill_pq_crosslinks.py` after the previous hardening entry and found that the checked-in `OUT.write_text(...)` call still contained an actual line break inside the string literal, making the validator syntactically invalid despite the documented hardening.
- [x] Repaired that source-level syntax defect on `main` in commit `af9ce4881eaeba8a8007e475142f7400cc90b6f0`; the exact checked-in reverse-projection equality guard remains intact.
- [x] Updated `docs/data/skill-pq-cross-domain-linkage-integrity-audit-2026-09-26.json` to record the repair and distinguish source-syntax correction from runtime validation.
- [x] No canonical skill/PQ relationship data was changed.
- [ ] Runtime validator execution and CI/build remain unverified in this environment.
- [ ] `docs/AI-CONTINUATION-PROMPT-EFFICIENCY-ADDENDUM.md` remains unavailable at the expected repository path (GitHub 404).
- [x] **Exact next:** inspect the next live validator/consumer for a concrete acceptance, schema, or deterministic-projection gap; prioritize executable integrity and only make evidence-backed data changes.

### 2026-09-26 continuation — Skill acquisition validator schema hardening
- [x] Inspected the next live deterministic validator, `scripts/validate_skill_acquisition_metadata.py`, and found that it assumed the `records` container and record shapes without explicitly rejecting malformed schema input.
- [x] Hardened the validator to require a list of exactly **474 object records**, unique non-empty string canonical `id` values, non-empty string skill names, and the required acquisition fields before applying acquisition/PQ consistency rules.
- [x] Updated `docs/data/skill-acquisition-metadata-integrity-audit-2026-09-26.json` to record the new schema guard; the existing audit remains **474 records / 0 metadata anomalies / 0 invalid PQ endpoints**.
- [x] No canonical acquisition or skill data was changed.
- [ ] Runtime validator execution and CI/build remain unverified in this environment.
- [x] **Exact next:** continue auditing the next live validator/consumer for a concrete schema or deterministic-projection acceptance gap; preserve the evidence boundary around unsupported PQ reward data.

### 2026-09-26 continuation — Partner relationship validator schema hardening
- [x] Audited the next live validator, `scripts/validate_partner_skill_relationships.py`, and found it assumed the relationship source plus canonical skill/bridge containers were correctly shaped.
- [x] Hardened the validator to reject malformed top-level relationship data, malformed `skills.records` / bridge `records` containers, non-object records, and non-string/empty canonical IDs or partner names.
- [x] Preserved the existing canonical-ID, canonical-name, uniqueness, relationship-type, exact-count, and evidence-path checks.
- [x] Updated `docs/data/partner-skill-relationship-validator-audit-2026-09-26.json` with the schema-hardening record; the known 3 relationship pairs remain clean.
- [x] No canonical relationship assignments were added, removed, or inferred.
- [ ] Runtime validator execution and CI/build remain unverified in this environment.
- [x] **Exact next:** inspect the next live validator/consumer for another concrete schema, type/range, or deterministic-projection acceptance gap.

### 2026-09-26 continuation — Partner navigation validator projection hardening
- [x] Inspected the live `scripts/validate_partner_customization_character_navigation.py` and found two concrete gaps: source/record containers were assumed to have valid shapes, and page search links validated the displayed name but not that the query parameter deterministically matched that name.
- [x] Hardened the validator to reject malformed source containers, non-list records, and non-object key/reconciliation/bridge records.
- [x] Added an exact page-link projection check requiring each `Search/?q=` value to equal the linked partner name with spaces encoded as `+`.
- [x] Updated `docs/data/characters/partner-customization-character-navigation-audit.json` to record the hardening; no canonical character or Partner Customization relationship data changed.
- [ ] Runtime validator execution and CI/build remain unverified in this environment.
- [x] **Exact next:** inspect the next live validator/consumer for another concrete deterministic projection, schema, or stale-cache integrity gap.

### 2026-09-26 continuation — Partner Customization navigation schema hardening
- [x] Inspected the live `scripts/validate_partner_customization_character_navigation.py` after the prior projection hardening and found a remaining deterministic schema gap: key, reconciliation, and bridge record fields were type-checked only partially, allowing malformed/empty identity fields to reach later joins.
- [x] Hardened the validator to require positive integer key numbers, non-empty string character IDs and partner names, and non-empty canonical bridge names for the relevant record types.
- [x] Updated `docs/data/characters/partner-customization-character-navigation-audit.json` with the hardening record; the established **20 keys / 20 reconciliation records / 34 bridge records / 152 canonical character names / 20 page links** contract is unchanged.
- [x] No canonical character, preset, DLC, acquisition, or partner-skill relationship data was changed.
- [ ] Runtime validator execution and CI/build remain unverified in this environment.
- [ ] `docs/AI-CONTINUATION-PROMPT-EFFICIENCY-ADDENDUM.md` remains unavailable at the expected repository path (GitHub 404).
- [x] **Exact next:** inspect the next live deterministic validator/consumer for another concrete schema, type/range, stale-cache, or deterministic-projection acceptance gap; preserve the evidence boundary around absent general PQ reward/reverse datasets.
### 2026-09-26 continuation — Skill→PQ reverse-index schema hardening
- [x] Inspected the live `scripts/validate_skill_pq_crosslinks.py` and identified a deterministic schema gap before the existing projection checks: malformed canonical skill containers/records could fail later through implicit indexing rather than being rejected by explicit schema assertions.
- [x] Hardened the validator so the canonical skill container must expose a list of exactly 474 object records; every record must have a non-empty string `id` and `name`; and `source_parallel_quests`, when present, must be a list before PQ endpoint validation/projection.
- [x] Updated `docs/data/skill-pq-cross-domain-linkage-integrity-audit-2026-09-26.json` to record the hardening. The expected **474 skills / 246 skill→PQ edges / 170 represented PQ IDs** contract is unchanged.
- [x] No canonical skill, PQ, acquisition, or reverse-index relationship data was changed.
- [ ] Runtime validator execution and CI/build remain unverified in this environment.
- [x] **Exact next:** inspect the next live validator/consumer for another concrete schema, type/range, stale-cache, or deterministic-projection acceptance gap; preserve the evidence boundary around PQs that have no explicit canonical skill endpoint in the current corpus.
### 2026-09-26 continuation — PQ cross-domain index contract validator
- [x] Inspected the live `docs/data/pq-cross-domain-index.json` after the skill→PQ hardening pass.
- [x] Added `scripts/validate_pq_cross_domain_index.py` to make the index's structural contract explicit: object root, schema/version and PQ 1-186 scope, live forward-index target, exactly the seven declared reverse-index entity classes, required key/value fields, farming source field, duplicate detection, and non-empty completion rule.
- [x] Updated `docs/data/cross-domain-index-reference-reachability-audit-2026-09-26.json` with the validator provenance and evidence boundary.
- [x] No PQ relationship endpoints, reward claims, or historical provenance references were changed or fabricated.
- [ ] Runtime validator execution and CI/build remain unverified in this environment.
- [x] **Exact next:** inspect the next live cross-domain consumer/validator or deterministic projection, prioritizing concrete schema/type/range/stale-reference acceptance gaps over recreating absent historical/index-only datasets.
### 2026-09-26 continuation — Skill→PQ reverse artifact metadata hardening
- [x] Re-inspected the live `scripts/validate_skill_pq_crosslinks.py` and its checked-in `docs/data/skill-pq-reverse-index-2026-09-26.json` projection.
- [x] Hardened the validator so a present reverse artifact must be an object and its schema version, scope, source, generated date, canonical skill count, represented-PQ count, and total edge count must match the deterministic contract before the per-PQ projection comparison.
- [x] Updated `docs/data/skill-pq-cross-domain-linkage-integrity-audit-2026-09-26.json` with the hardening and evidence boundary.
- [x] No skill→PQ relationships were added, removed, inferred, or otherwise changed.
- [ ] Runtime validator execution and CI/build remain unverified in this environment.
- [x] **Exact next:** inspect the next live cross-domain consumer/validator or deterministic projection, especially remaining live PQ endpoint/navigation validation, for another concrete schema/type/range/stale-cache gap; do not reconstruct absent historical reward/reverse datasets without an evidence-complete producer.
### 2026-09-26 continuation — Partner Customization bridge schema hardening
- [x] Inspected the live Partner Customization navigation validator and found a concrete remaining schema gap: bridge `character_id` values and canonical character-name list entries were not fully type/emptiness checked before dictionary/set operations.
- [x] Hardened `scripts/validate_partner_customization_character_navigation.py` so bridge IDs and canonical character names must be non-empty strings before joins/projections; malformed bridge IDs can no longer reach implicit hashing failures or partial joins.
- [x] Updated `docs/data/characters/partner-customization-character-navigation-audit.json` with the hardening record.
- [x] No character identity, Partner Customization, DLC, acquisition, or skill relationship data changed.
- [ ] Runtime validator execution and CI/build remain unverified in this environment.
- [x] **Exact next:** inspect the next live consumer/validator or deterministic projection for another concrete schema/type/range/stale-reference gap; preserve the evidence boundary around absent PQ reward/reverse datasets.


### 2026-09-27 continuation — Restore missing repository files onto main
- [x] Investigated the report that main showed only a small subset of the repository while other branches still contained the broader codebase.
- [x] Confirmed the live main tree was sparse at the repository root: it contained only docs/ and scripts/, while the recovery source branch ai/continue-skill-acquisition-2026-09-19 still contained the missing root files, GitHub workflows, wiki pages, older research records, and other repository artifacts.
- [x] Created safety branch recovery-before-main-restoration-2026-09-27 at the pre-restoration main commit 8eb55741ddd8d21273434f52bec444178871544a before changing main.
- [x] Restored every file path present on the recovery source branch that was absent from current main, while preserving the current main version for paths that already existed there. This avoids replacing the newer current canonical/evidence work with older branch versions while recovering missing files.
- [x] Committed the restored union as 9e15797821d41304c7c62d889a79cf0acaf3fa05 (Restore missing repository files onto main) and moved main to that commit with a fast-forward update.
- [x] Manually confirmed restored critical paths on main: README.md, .github/workflows/data-audit.yml, docs/index.md, docs/data/pq-reward-relationships.json, and scripts/validate_skill_acquisition_metadata.py.
- [x] Live recursive tree inspection after restoration reports 1,502 tree entries and root files CHANGELOG.md, CONTRIBUTING.md, README.md, and TODO.md; main is no longer the sparse docs/scripts-only state.
- [ ] Runtime validator execution and CI/build remain intentionally unverified and non-blocking per current project policy.
- [x] **Exact next:** continue substantive data/research work from the restored main state; do not treat runtime/CI availability as a blocker.

### 2026-09-27 continuation — Canonical database recovery integrity verified
- [x] Re-opened the restored live main database rather than trusting the web UI/file preview, which can appear empty for large JSON blobs.
- [x] Verified docs/data/skills.json is materially present on main as a 1,339,174-byte blob and parsed successfully to 474 canonical skill records with 474 unique IDs.
- [x] Verified docs/data/skills-index.json independently contains 474 records / 474 unique IDs.
- [x] Verified docs/data/skill-pq-reverse-index-2026-09-26.json independently declares 474 canonical skills / 246 Skill→PQ edges / 170 represented PQ IDs.
- [x] Verified docs/data/pq-reward-relationships.json is materially present after restoration; its current relationship-count summary remains 236 skills / 137 Super Souls / 125 equipment / 247 characters / 88 DLC / 7 farming.
- [x] Added docs/data/canonical-database-recovery-integrity-audit-2026-09-27.json and registered it in docs/data/pq-cross-domain-index.json.
- [x] This confirms the critical canonical database was not lost merely because large-file previews returned blank; no unsupported reconstruction was performed.
- [ ] Runtime/CI remains intentionally non-blocking and unverified.
- [ ] Exact next: continue forward from the recovered 474-record canonical corpus with a fresh live census for the next substantive data/research batch; do not rebuild already-recovered skill data from older branches.

### 2026-09-27 continuation — Fresh post-recovery skill census and next-domain pivot
- [x] Performed a fresh live census of the recovered canonical skill corpus instead of reusing the pre-corruption Batch 495 candidate list.
- [x] All **474/474** canonical skill records currently have `research_status: enriched`; there is no remaining unaudited mechanics frontier inside the canonical skill corpus at this checkpoint.
- [x] Added `scripts/validate_canonical_database_recovery.py` to make the recovery contract reproducible: 474 unique canonical skills, exact skills-index identity, 474/246/170 Skill→PQ reverse metrics, and required PQ reward count keys.
- [x] Added the validator reference to `docs/data/canonical-database-recovery-integrity-audit-2026-09-27.json`.
- [x] External source review confirms the repository's established all-PQ guide remains a useful independent reward-list source; no reward values were bulk-inferred from a secondary guide in this checkpoint.
- [ ] Runtime execution/CI remains intentionally non-blocking and unverified.
- [ ] **Exact next:** pivot the substantive research cycle from already-enriched skill mechanics to the highest-priority cross-domain gap: expand/reconcile PQ reward relationships and reverse navigation using evidence-complete PQ sources, while preserving the existing partial-source/evidence boundary and never treating missing canonical edges as negative reward claims.

### 2026-09-27 continuation — PQ reward relationship integrity and recovery-forward correction
- [x] Re-read the live handoff/TODO and inspected the restored PQ reward layer rather than assuming the earlier missing-source note was still current.
- [x] Corrected the recovery understanding: `docs/data/pq-reward-relationships.json` is present on `main` and contains **840 unique relationship rows** across PQ 1–186.
- [x] Independently checked every relationship row against the repository schema contract: **0 malformed rows, 0 duplicate `(pq, relationship, target)` keys**, and exact count parity with the stored summary: **236 skills / 137 Super Souls / 125 equipment / 247 characters / 88 DLC / 7 farming**.
- [x] Added `scripts/validate_pq_reward_relationships.py`, a deterministic structural validator for the canonical PQ relationship store. It deliberately does not infer absent rewards.
- [x] Added `docs/data/pq-reward-relationship-integrity-audit-2026-09-27.json` with the current passing structural census.
- [x] Registered the new validator and audit in `docs/data/pq-cross-domain-index.json`.
- [x] Preserved the partial normalized reverse-index boundary: `pq-unified-reverse-index-1-186.json` is explicitly `source_normalized_partial`; its missing entries are not negative claims and must not be used to delete canonical forward relationships.
- [ ] Runtime execution/CI remains intentionally non-blocking and unverified.
- [ ] **Exact next:** reconcile the canonical 840-row forward relationship store against the normalized reverse-index projections and identify deterministic projection drift (without deleting source-backed forward edges); then expand reverse navigation only from evidence-backed canonical relationships.

### 2026-09-27 continuation — Exact PQ forward↔reverse reconciliation completed
- [x] Compared the canonical `docs/data/pq-reward-relationships.json` forward store against `docs/data/pq-reward-normalization/pq-unified-reverse-index-1-186.json` across every relationship class.
- [x] **All 840 forward relationships have exact reverse projection parity**: 236 Skill, 137 Super Soul, 125 equipment, 247 character, 88 DLC, and 7 farming relationships; **0 forward-only mismatches and 0 reverse-only mismatches**.
- [x] Equipment parity was checked across the union of both reverse buckets (`clothing` + `accessories`), resolving the apparent 38-item clothing-only discrepancy without changing data.
- [x] Added `scripts/reconcile_pq_forward_reverse.py`, which treats the canonical forward store as authoritative and reports projection drift without silently mutating/inferencing relationships.
- [x] Added `docs/data/pq-forward-reverse-reconciliation-audit-2026-09-27.json` and registered it in `docs/data/pq-cross-domain-index.json`.
- [x] This establishes the recovered PQ relationship layer as an internally consistent **840-edge forward/reverse projection** at the current evidence boundary.
- [ ] Runtime execution/CI remains intentionally non-blocking and unverified.
- [ ] **Exact next:** move from projection integrity to the next concrete cross-domain consumer gap: inspect PQ/skill page-generation/navigation consumers for stale, missing, or non-bidirectional links, then harden the highest-impact deterministic consumer without altering canonical evidence.

### 2026-09-27 continuation — PQ→skill consumer projection repaired
- [x] Found and corrected a concrete stale consumer: `docs/data/pq-skill-crosslink-report.json` was still based on the historical PQ-batch projection (229 links / 283 canonical skill names) instead of the recovered canonical forward relationship layer.
- [x] Reworked `scripts/validate_pq_skill_links.py` to derive its PQ→skill consumer projection from `docs/data/pq-reward-relationships.json`, with the live skill→PQ reverse artifact used to validate target identity.
- [x] Regenerated `docs/data/pq-skill-crosslink-report.json` to **236 current canonical forward skill edges**, resolving all 236 and preserving four documented presentation-name aliases: Chain Destructo-disc Barrage → Chain Destructo-Disc Barrage; III Bomber → Ill Bomber; Starfall → Destruction's Concerto: Starfall; Giant Cluster → Gigantic Cluster.
- [x] Added `docs/data/pq-skill-consumer-reconciliation-audit-2026-09-27.json` and registered it in `docs/data/pq-cross-domain-index.json`.
- [x] Historical 229-link/283-name output is retained as provenance metadata rather than treated as current truth.
- [ ] Runtime/CI remains intentionally non-blocking/unverified.
- [ ] **Exact next:** inspect the other declared PQ reverse consumers (Super Soul, equipment/accessory, character, DLC, farming) for the same stale-report/source mismatch; repair the highest-impact deterministic consumer next, without altering canonical evidence-backed forward relationships.

### 2026-09-27 continuation — Super Soul consumer endpoint gap identified
- [x] Audited the next declared PQ consumer domain instead of assuming reverse-index parity means page-level endpoint completeness.
- [x] Canonical forward store contains **137 source-backed PQ→Super Soul edges / 134 unique targets** and remains authoritative.
- [x] The normalized PQ acquisition index is explicitly partial (PQ 41-186) and contains 80 acquisition records; it must not be interpreted as exhaustive negative evidence.
- [x] The promoted `super-souls-record-layer.json` currently contains only **42 detailed records**, so many source-backed PQ Super Soul targets do not yet have a fully promoted detailed endpoint record.
- [x] Added `scripts/audit_super_soul_consumer_coverage.py` and `docs/data/super-soul-consumer-endpoint-coverage-audit-2026-09-27.json` to track this gap without deleting or weakening any canonical forward relationship.
- [x] Registered the audit/validator in `docs/data/pq-cross-domain-index.json`.
- [ ] Runtime/CI remains intentionally non-blocking/unverified.
- [ ] **Exact next:** use the existing Super Soul research/acquisition batches to expand the detailed Super Soul endpoint layer from evidence-backed records, prioritizing the 134 canonical PQ targets lacking detailed coverage; do not fabricate trigger/effect/Limit Burst fields merely to close the endpoint count.

### 2026-09-27 continuation — PQ→Super Soul consumer projection refreshed
- [x] Added/refreshed `docs/data/pq-super-soul-crosslink-report.json` from the authoritative `pq-reward-relationships.json` rather than stale historical PQ projections.
- [x] Projection contains **137 canonical PQ→Super Soul edges / 134 unique targets** with no unresolved canonical target identities.
- [x] **122** targets appear in the partial PQ 41-186 Super Soul acquisition index; **8** currently have promoted detailed Super Soul records. The remaining detail gaps are explicitly retained as enrichment work, not treated as missing rewards.
- [x] Registered the projection in `docs/data/pq-cross-domain-index.json` and strengthened the Super Soul coverage validator to check projection parity.
- [ ] Runtime/CI remains intentionally non-blocking/unverified.
- [ ] **Next:** inspect the equipment/accessory consumer layer for the same stale-source/projection mismatch, then repair the highest-impact deterministic projection from canonical forward relationships while preserving partial reverse-index semantics.

### 2026-09-27 continuation — PQ→Equipment consumer reconciliation
- [x] Audited the PQ equipment/accessory consumer layers against authoritative `docs/data/pq-reward-relationships.json`.
- [x] Added `docs/data/pq-equipment-crosslink-report.json`, projecting all **125 canonical PQ→equipment edges / 123 unique targets** without inventing or deleting relationships.
- [x] Compared both endpoint layers: `equipment-accessories-record-layer.json` and `equipment-record-layer.json`. Only **16** canonical targets currently have exact endpoint-name records; **107 unique target identities remain endpoint-enrichment gaps**.
- [x] Explicitly classified endpoint gaps as incomplete consumer-layer coverage, not evidence that the canonical PQ reward relationship is false or unavailable.
- [x] Registered the projection in `docs/data/pq-cross-domain-index.json`.
- [ ] Runtime/CI remains intentionally non-blocking/unverified.
- [ ] **Next:** inspect the PQ→Character consumer layer for stale-source/projection mismatch and rebuild its deterministic projection from canonical forward relationships where needed; then continue DLC and farming consumers.

### 2026-09-27 continuation — PQ→Character consumer reconciliation
- [x] Audited the PQ→character consumer layer against authoritative `docs/data/pq-reward-relationships.json` (`pq_features_character`).
- [x] Added `docs/data/pq-character-crosslink-report.json`: **247 canonical edges / 75 unique character targets**.
- [x] All **75/75 unique character identities** resolve against `characters-record-layer.json` (including its DLC character-name layer); no endpoint identity gaps remain for this canonical projection.
- [x] Corrected an initial projection-counting implementation issue before finalizing the report; endpoint identity comparison is now exact string-set matching.
- [x] Registered the character consumer projection in `pq-cross-domain-index.json`.
- [ ] Runtime/CI remains intentionally non-blocking/unverified.
- [ ] **Next:** inspect the PQ→DLC consumer layer and rebuild/validate its deterministic projection from canonical forward relationships; then inspect farming-route consumer coverage.

### 2026-09-27 continuation — PQ→DLC consumer reconciliation
- [x] Audited PQ→DLC provenance relationships against authoritative `docs/data/pq-reward-relationships.json` (`pq_requires_dlc`).
- [x] Added `docs/data/pq-dlc-crosslink-report.json`: **88 canonical edges / 21 unique DLC targets**.
- [x] Compared the projection with `docs/data/dlc-source-baseline.json`; the baseline contains **7 official pack-set taxonomy entries**, while the canonical PQ layer also tracks individual packs/chapters. The mismatch is documented as endpoint taxonomy incompleteness rather than a contradiction.
- [x] Registered the DLC consumer projection in `pq-cross-domain-index.json`.
- [ ] Runtime/CI remains intentionally non-blocking/unverified.
- [ ] **Next:** inspect PQ farming-route consumer coverage and reconcile it against the canonical forward relationship store; then continue remaining cross-domain/exhaustive enrichment gaps.

### 2026-09-27 continuation — PQ farming-route consumer reconciliation
- [x] Reconciled the canonical `pq_farming_route` relationships from `docs/data/pq-reward-relationships.json`.
- [x] Added `docs/data/pq-farming-crosslink-report.json`: **7 canonical farming-route edges / 1 target (Dragon Balls)** across PQ 015, 022, 044, 045, 068, 083, and 088.
- [x] Preserved explicit source provenance: six relationships from the all-186 PQ guide and one from Twinfinite; no additional farming routes were inferred.
- [x] Registered the farming consumer projection in `pq-cross-domain-index.json`.
- [ ] Runtime/CI remains intentionally non-blocking/unverified.
- [ ] **Next:** run a whole cross-domain projection/status audit now that skill, Super Soul, equipment, character, DLC, and farming consumers have deterministic canonical projections; identify the highest-impact remaining exhaustive enrichment gap rather than repeating completed consumer work.

### 2026-09-27 continuation — Super Soul endpoint promotion and integrity hardening
- [x] Reconciled the canonical **137 PQ→Super Soul edges / 134 unique targets** against the existing partial PQ acquisition layer and detailed Super Soul endpoint layer.
- [x] Promoted **116 additional evidence-backed Super Soul names** from `docs/data/super-souls/pq-acquisition-index-041-186.json` into `docs/data/super-souls-record-layer.json` as deterministic `indexed` endpoint records. The record layer now contains **158 records**, including the existing detailed records.
- [x] Promotion intentionally populated only identity/acquisition/provenance fields. Trigger, effect, magnitude, duration, stacking, Limit Burst, and other mechanics remain null/unresolved rather than being inferred.
- [x] Current canonical PQ target endpoint coverage improved to **124/134**, leaving **10 explicit target-level enrichment gaps**: `I'm neither Kami nor Piccolo...`, `Time to dismantle you androids!`, `I am the universe's strongest!`, `I got back my youth and vigor!`, `Goku the legendary Super Saiyan!`, `I'll use all my strength to kill you.`, `I wanted to kill you with my own hands.`, `I am...Super Vegeta!!`, `This fight...is truly pointless...`, and `I actually felt that one...`.
- [x] Refreshed `docs/data/super-soul-consumer-endpoint-coverage-audit-2026-09-27.json` and `docs/data/pq-super-soul-crosslink-report.json` to reflect the new endpoint coverage and preserve the partial-source boundary.
- [x] Added `scripts/validate_super_soul_record_layer.py` and `docs/data/super-soul-record-layer-integrity-audit-2026-09-27.json` to enforce unique IDs/names, required source/verification fields, and canonical PQ target coverage without fabricating mechanics.
- [x] Registered the validator/audit in `docs/data/pq-cross-domain-index.json`.
- [ ] Runtime/CI remains intentionally non-blocking and unverified.
- [ ] **Exact next:** investigate the remaining 10 Super Soul target identities against existing repository research/evidence and promote only evidence-complete records; after that, continue the broader cross-domain/exhaustive enrichment frontier (especially equipment's 107 endpoint gaps and DLC taxonomy/detail gaps).

### 2026-09-27 continuation — Super Soul endpoint identity completion
- [x] Investigated all **10 remaining canonical PQ→Super Soul endpoint gaps** against repository PQ batches, unified reverse indexing, and the canonical relationship store.
- [x] Confirmed each remaining target has source-backed PQ acquisition evidence; no new relationship was invented.
- [x] Promoted all 10 remaining identities into `docs/data/super-souls-record-layer.json`. The layer now contains **168 records** and has **134/134 canonical PQ Super Soul target identity coverage**.
- [x] Refreshed `super-soul-consumer-endpoint-coverage-audit-2026-09-27.json` and `pq-super-soul-crosslink-report.json`; endpoint identity gaps are now **0**.
- [x] Mechanics remain explicitly unresolved where evidence is absent; indexed endpoint creation does not imply verified effects, triggers, magnitude, stacking, or Limit Burst behavior.
- [ ] Runtime/CI remains intentionally non-blocking and unverified.
- [ ] **Next:** move from endpoint identity completion to mechanics/enrichment coverage, then address the largest remaining cross-domain gap (equipment endpoint enrichment and DLC detail/taxonomy) rather than creating duplicate relationship projections.

### 2026-09-27 continuation — Super Soul mechanics enrichment pass
- [x] Enriched the **10 previously identity-only canonical Super Soul endpoints** using independently surfaced item/character evidence: trigger conditions, effects, magnitudes, Limit Bursts, character associations, and CAC usability where supported.
- [x] Updated `docs/data/super-souls-record-layer.json` (168 records total); canonical PQ relationship identities were not altered.
- [x] Mechanics field population increased to **44 trigger conditions, 52 effect descriptions, 46 effect magnitudes, 42 Limit Bursts, and 52 CAC-usability values**.
- [x] Added `docs/data/super-soul-mechanics-enrichment-audit-2026-09-27.json` and registered it in `pq-cross-domain-index.json`.
- [x] Kept unresolved values explicit; no unsupported numeric conversion, duration, stacking, or trigger behavior was invented.
- [ ] Runtime/CI remains intentionally non-blocking and unverified.
- [ ] **Next:** continue deterministic Super Soul mechanics enrichment from the staged research/evidence corpus, prioritizing records with acquisition identity already resolved but missing structured effects/triggers; then return to equipment endpoint enrichment and DLC detail coverage.


### 2026-09-27 continuation — Super Soul audit drift reconciliation
- [x] Added `scripts/audit_super_soul_mechanics_coverage.py`, a deterministic read-only coverage auditor over the canonical 168-record Super Soul layer; it reports field population without inferring mechanics or promoting secondary evidence into canonical facts.
- [x] Refreshed `docs/data/super-soul-record-layer-integrity-audit-2026-09-27.json` to the current **168 records / 134 canonical PQ targets / 134 endpoint matches / 0 endpoint gaps**. The prior 158-record audit was stale after the final ten endpoint promotions.
- [x] Reconciled `docs/data/super-soul-mechanics-enrichment-audit-2026-09-27.json` with the live canonical record layer. Current coverage is **44 trigger conditions, 52 effect descriptions, 46 effect magnitudes, 40 durations, 25 stacking behaviors, 42 Limit Burst values, 22 Limit Burst effects, 52 CAC-usability values, 3 race restrictions, and 30 DLC requirements**; `limit_burst_trigger` remains unpopulated across the 168 records.
- [x] Registered the new mechanics auditor and both refreshed audits in `docs/data/pq-cross-domain-index.json`.
- [x] Confirmed staged Super Soul research batches 03–04 do not contain additional values that can be deterministically merged into currently-null canonical schema fields without a separate evidence reconciliation; no speculative promotion was made.
- [ ] Runtime/CI remains intentionally non-blocking and unverified.
- [ ] **Next:** continue evidence-backed Super Soul mechanics reconciliation where repository sources can fill currently-null canonical fields; otherwise pivot to the **107 unique PQ→equipment endpoint-enrichment gaps** and the **21-target PQ→DLC taxonomy/detail gap**. Preserve canonical relationship data as authoritative and keep unresolved mechanics explicit.

### 2026-09-27 continuation — Super Soul mechanics coverage audit hardening
- [x] Re-audited the current 168-record Super Soul endpoint layer after the mechanics enrichment pass; canonical PQ→Super Soul endpoint identity remains 134/134.
- [x] Refreshed `docs/data/super-soul-record-layer-integrity-audit-2026-09-27.json` so its counts no longer describe the pre-promotion 158-record state; it now records 168 unique records, 134/134 canonical endpoint coverage, and zero endpoint identity gaps.
- [x] Added `scripts/audit_super_soul_mechanics_coverage.py`, a deterministic coverage-only auditor that reports population/missing counts for trigger, effect, magnitude, duration, stacking, Limit Burst, CAC, race, and DLC fields without inferring mechanics.
- [x] Registered the mechanics coverage auditor and refreshed integrity audit in `docs/data/pq-cross-domain-index.json`.
- [x] Current field census: trigger 44/168, effect text 52/168, effect magnitude 46/168, duration 40/168, stacking 25/168, Limit Burst 42/168, Limit Burst effect 22/168, CAC usability 52/168, race restriction 3/168, DLC requirement 30/168. These are coverage measurements, not negative claims.
- [ ] Runtime/CI remains intentionally non-blocking and unverified.
- [ ] **Next:** use only existing repository evidence/staged research to make a substantive Super Soul mechanics enrichment batch; if no additional evidence-backed batch is available, pivot to the 107 unique PQ→equipment endpoint-enrichment gaps and avoid creating duplicate projections.



### 2026-09-27 continuation — Super Soul audit refresh and equipment endpoint coverage correction
- [x] Refreshed `docs/data/super-soul-record-layer-integrity-audit-2026-09-27.json` after the final ten endpoint promotions: **168 records**, **134/134 canonical PQ target identities**, zero endpoint gaps; mechanics remain explicitly partial.
- [x] Added `scripts/audit_super_soul_mechanics_coverage.py` as a deterministic field-population auditor; it does not infer mechanics.
- [x] Added `scripts/audit_pq_equipment_endpoint_coverage.py` for deterministic canonical PQ→equipment endpoint identity auditing.
- [x] Re-audited `docs/data/pq-equipment-crosslink-report.json` against the live endpoint layers. Current exact identity coverage is **15/123 unique canonical targets**, leaving **108 endpoint-enrichment gaps**; the earlier 16/123 figure was stale.
- [x] Refreshed and registered the equipment projection without altering any canonical PQ→equipment relationship.
- [ ] Runtime/CI remains intentionally non-blocking and unverified.
- [ ] **Next:** use existing equipment/accessory research evidence to promote unambiguous endpoint identities into the appropriate clothing/equipment or accessory layer; do not merge ambiguous names or classify clothing as accessories. Then continue DLC detail/taxonomy enrichment.


### 2026-09-27 continuation — equipment endpoint audit write recovery
- [x] GitHub content writes are operational again; the earlier 404 write blocker is no longer preventing repository updates.
- [x] Refreshed `docs/data/pq-equipment-crosslink-report.json` to schema 1.2 with the current **15/123 exact endpoint identity matches** and **108 explicit endpoint-enrichment gaps**.
- [x] Confirmed `scripts/audit_pq_equipment_endpoint_coverage.py` already exists on `main`; no duplicate script was created.
- [x] Preserved the canonical `pq_rewards_equipment` relationship store as authoritative; no relationship was deleted, reclassified, or invented.
- [ ] Runtime/CI remains intentionally non-blocking and unverified.
- [ ] **Next:** promote only unambiguous equipment/accessory endpoint identities from existing evidence, prioritizing records with explicit canonical inventory names and PQ routes; preserve ambiguous/component-only cases as backlog. Then continue DLC detail/taxonomy enrichment.


### 2026-09-27 continuation — PQ equipment consumer integrity baseline
- [x] Added deterministic `scripts/validate_pq_equipment_crosslinks.py` and integrity audit `docs/data/pq-equipment-crosslink-integrity-audit-2026-09-27.json`.
- [x] Current canonical equipment projection: **125 edges / 123 unique targets**; endpoint layers: **118 records / 15 exact matches / 108 identity gaps**.
- [ ] Continue evidence-backed reconciliation of the 108 endpoint gaps; use `docs/data/accessory-pq-canonical-remaining.json` as an explicit backlog and do not infer inventory identities from generic set/component labels.
- [ ] Runtime/CI remains intentionally non-blocking and unverified.


### 2026-09-27 continuation — PQ equipment endpoint identity promotion
- [x] Promoted 9 unambiguous canonical PQ→equipment endpoint identities: 8 clothing/equipment + 1 accessory.
- [x] Current PQ equipment projection: 125 edges / 123 unique targets; 127 endpoint records; 24 exact identity matches; 99 explicit endpoint-enrichment gaps.
- [x] Refreshed PQ equipment crosslink report and integrity audit; canonical relationships remain authoritative.
- [ ] Continue evidence-backed promotion of the remaining 99 endpoint identities; preserve ambiguous/component-only cases and route conflicts.
- [ ] Runtime/CI remains intentionally non-blocking and unverified.


## 2026-09-27 continuation update — equipment endpoint expansion
- Completed and retained: Super Soul integrity audit refresh; canonical PQ Super Soul endpoint identity remains 134/134 across 168 records.
- Completed: promoted 10 evidence-backed canonical PQ equipment identities into the equipment endpoint layer and refreshed the PQ equipment crosslink projection.
- Current PQ equipment crosslink state: 125 canonical edges, 123 unique targets, 34 endpoint identity matches, 89 explicit endpoint-enrichment gaps.
- Remaining: continue the giant equipment endpoint backlog using canonical forward relationships plus independent source evidence; preserve historical disagreements and do not infer generic accessory/set labels into new identities.
- Runtime/CI remains intentionally ignored until billing/runtime access is restored.


### 2026-09-27 continuation — PQ equipment endpoint expansion batch
- [x] Promoted 9 additional unambiguous canonical PQ→equipment endpoint identities from existing repository evidence: Janemba Head; Caulifla Wig; Kale Wig; Bulma (Kid) Wig; Gamma 2's Helmet; Android 13's Clothes; Zamasu's Clothes; Flying Nimbus!!; Gohan (Beast) Wig.
- [x] Updated both endpoint layers without changing canonical relationship semantics: five accessory records and four equipment records.
- [x] Refreshed the PQ equipment projection and integrity audit against the live endpoint layers using exact identity matching.
- [x] Current state: 125 canonical PQ→equipment edges, 123 unique targets, 108 endpoint records, 42 exact endpoint identity matches, 81 explicit endpoint-enrichment gaps.
- [x] Preserved ambiguous/component-only identities and did not infer generic set labels into new records.
- [ ] Runtime/CI remains intentionally non-blocking and unverified.
- [ ] **Exact next:** continue the remaining 81 endpoint identities using existing accessory/equipment research evidence, prioritizing explicit inventory names and retaining route/source conflicts; then revisit DLC detail/taxonomy coverage.


## 2026-09-27 — PQ Equipment Endpoint Frontier

- [x] Audit current canonical PQ→equipment endpoint coverage (125 edges / 123 unique targets / 42 endpoint matches / 81 gaps).
- [ ] Promote evidence-backed endpoint identities for the 81 missing PQ equipment targets without altering canonical reward relationships.
- [ ] Enrich promoted equipment endpoints with acquisition/provenance/mechanics fields where supported.
- [ ] Re-run deterministic endpoint coverage/reconciliation after promotion.
- [ ] Refresh stale Super Soul integrity audit once the GitHub write path is stable.

### 2026-09-27 continuation — PQ equipment endpoint batch
- [x] Promoted 5 explicit named accessory endpoints from PQ 121–142 research: Broly Wig (Legendary Super Saiyan), Kakunsa's Wig and Mask, Kakunsa's Tail, Rozie's Hood and Goggles, Universe 7 Baseball Cap.
- [x] Recomputed canonical PQ→equipment endpoint coverage: 125 edges / 123 unique targets / 56 exact endpoint identities / 67 remaining identity gaps.
- [x] Refreshed the endpoint coverage report and audit from the live canonical relationship source.
- [x] Kept reward-slot certainty, route/version provenance, and unresolved semantics separate from identity promotion.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] **Exact next:** continue evidence-backed promotion of the remaining 67 endpoint identities, prioritizing explicit inventory names from PQ research and avoiding generic set/component labels.

### 2026-09-27 continuation — PQ 152–183 accessory endpoint batch
- [x] Promoted 13 explicitly named accessory endpoints from PQ reward normalization: Android 17 (DB Super) Ranger Wig, King Vegeta (DB Super) Wig, Gamma 2 Helmet, Dr. Hedo Hood, Red Ribbon Army Helmet, Videl (DB Super) Wig, SS4 Goku (DAIMA) Wig & Tail, SS3 Vegeta (DAIMA) Wig, Glorio Wig, Panzy Wig, Golden Frieza Head, Cheelai's Coat, and Broly Wig (Black Hair, Normal).
- [x] Recomputed live PQ→equipment coverage: 125 edges / 123 unique targets / 68 exact endpoint identities / 55 remaining identity gaps.
- [x] Refreshed the endpoint report and audit; reward conditions and version provenance remain explicitly unresolved where not established.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] **Exact next:** promote the remaining 55 endpoint identities using explicit reward-normalization evidence, with clothing/accessory domain classification kept separate.

### 2026-09-27 continuation — legacy PQ accessory endpoint batch
- [x] Promoted 7 explicit accessory identities: Goku Wig, Perfect Cell's Wings, Pan's Bandanna, Yamcha's Baseball Hat, SS4 Wig & Tail (Goku), Resistance Helmet, Toppo's Moustache.
- [x] Recomputed PQ→equipment coverage: 125 edges / 123 unique targets / 75 exact endpoint identities / 48 remaining identity gaps.
- [x] Removed an intermediate unsupported clothing promotion batch rather than retaining guessed PQ attribution; canonical data remains evidence-backed.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] **Exact next:** continue promoting only explicitly evidenced remaining endpoint identities, then reconcile clothing records separately from accessories.


### 2026-09-27 TODO progress update — Database recovery-forward equipment endpoint completion
- [x] Re-verified recovered canonical skill/index blobs: **474 canonical skills / 474 unique IDs / 474 index IDs**, with the independent Skill→PQ reverse projection at **246 edges / 170 PQ IDs**.
- [x] Freshly reconciled canonical PQ→equipment targets against both live endpoint layers.
- [x] Added 48 explicit source-backed equipment endpoint identities as equip-053–equip-100, keeping stats/slot/component/reward-condition uncertainty explicit.
- [x] PQ equipment endpoint coverage is now **123/123 exact target identities**, with **0 remaining identity gaps** and **194 endpoint records**.
- [x] Refreshed all three PQ equipment endpoint/crosslink audit artifacts.
- [ ] Runtime/CI remains unverified and non-blocking.
- [ ] **Next:** fresh census and substantive enrichment in the next highest-value incomplete cross-domain area; preserve canonical source-of-truth and evidence boundaries.


### 2026-09-27 TODO progress update — Unified Super Soul PQ acquisition cross-link recovery
- [x] Re-audited **137 PQ→Super Soul edges / 134 unique targets** against the detailed record layer.
- [x] Replaced the structurally incomplete 041-186 acquisition index with `docs/data/super-souls/pq-acquisition-index-001-186.json` covering **PQ 1-186**, **92 populated PQ rows**, and **134 unique Super Soul targets**.
- [x] Added missing acquisition rows for PQ5, 12, 21, 22, 26, 28, 29, 30, 35, 36, 38, and 40; preserved multi-PQ acquisition relationships.
- [x] Updated the Super Soul consumer audit and crosslink report to **134/134 acquisition-index coverage with 0 missing targets**.
- [x] Updated the audit script and cross-domain registry; retired the superseded partial index.
- [x] No unsupported mechanics, drop rates, or trigger behavior were inferred.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] **Exact next:** fresh 134-target Super Soul mechanics frontier census and evidence-backed enrichment of the next shortest genuinely under-detailed records.


### 2026-09-27 TODO progress update — Super Soul mechanics batch 2
- [x] Enriched five additional indexed Super Souls: Finally, some excitement.; I...hate you!!!; Strengthen me, Shadow Dragons!; Revival of the Demon Realm is at hand; I'll make you regret that!.
- [x] Refreshed the Super Soul mechanics enrichment audit and advanced field coverage to trigger 54/168, effect 62/168, magnitude 56/168, duration 46/168, stacking 27/168, Limit Burst 52/168, Limit Burst effect 32/168, CaC 62/168.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] Next: continue evidence-backed mechanics enrichment without treating missing fields as negative facts.


### 2026-09-27 TODO progress update — Super Soul mechanics batch 3
- [x] Enriched Don't quit! Get up!, This is not a weapon., I've been saving this! Kaioken!, Now you understand. Surrender., and How Dare You...! That's My Bulma.
- [x] Refreshed mechanics/integrity audits and advanced coverage to trigger 59/168, effect 67/168, magnitude 61/168, duration 49/168, stacking 28/168, Limit Burst 57/168, Limit Burst effect 37/168, CaC 67/168.
- [x] Reduced the remaining partial mechanics frontier to **115 records**.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] Next: continue evidence-backed enrichment without treating missing fields as negative facts.


### 2026-09-27 TODO progress update — Super Soul mechanics batch 4
- [x] Enriched Earth is in your hands now!, Get serious, would you?, Now we're even., Time to get serious, I guess., and Hmph! For justice!.
- [x] Refreshed mechanics/integrity audits and advanced coverage to trigger 64/168, effect 72/168, magnitude 66/168, duration 54/168, stacking 30/168, Limit Burst 62/168, Limit Burst effect 42/168, CaC 72/168.
- [x] Reduced the remaining partial mechanics frontier to **110 records**.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] Next: continue evidence-backed enrichment without inferring undocumented mechanics.


### 2026-09-27 TODO progress update — Super Soul mechanics batch 5
- [x] Enriched This heat...will be your downfall!, Right, then... Let's begin the experiment!, For beauty! For elegance! For love!, This Super Saiyan 2 is crazy strong!, and Don't think I'm the same as before!.
- [x] Refreshed mechanics/integrity audits and advanced coverage to trigger 69/168, effect 77/168, magnitude 71/168, duration 59/168, stacking 32/168, Limit Burst 67/168, Limit Burst effect 47/168, CaC 77/168.
- [x] Reduced the remaining partial mechanics frontier to **105 records**.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] Next: continue evidence-backed enrichment without treating missing fields as negative facts.


### 2026-09-27 TODO progress update — Super Soul mechanics batch 6
- [x] Enriched Super Souls super-soul-097 through super-soul-101.
- [x] Refreshed mechanics/integrity audits: trigger 74/168, effect 82/168, magnitude 76/168, duration 64/168, stacking 33/168, Limit Burst 72/168, Limit Burst effect 52/168, CaC 82/168.
- [x] Reduced the remaining partial mechanics frontier to **100 records**.
- [x] Preserved the Veku source discrepancy as research data rather than collapsing conflicting evidence.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] Next: continue evidence-backed enrichment without treating missing fields as negative facts.


### 2026-09-27 TODO progress update — Super Soul mechanics batch 7
- [x] Enriched super-soul-102 through super-soul-106.
- [x] Refreshed mechanics/integrity audits: trigger 79/168, effect 87/168, magnitude 81/168, duration 66/168, stacking 36/168, Limit Burst 77/168, Limit Burst effect 57/168, CaC 87/168.
- [x] Reduced the remaining partial mechanics frontier to **95 records**.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] Next: continue evidence-backed enrichment without treating missing fields as negative facts.


### 2026-09-27 TODO progress update — Super Soul mechanics batch 8
- [x] Enriched super-soul-107 through super-soul-111.
- [x] Refreshed mechanics/integrity audits: trigger 84/168, effect 92/168, magnitude 86/168, duration 71/168, stacking 39/168, Limit Burst 82/168, Limit Burst effect 62/168, CaC 92/168.
- [x] Reduced the remaining partial mechanics frontier to **90 records**.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] Next: continue evidence-backed enrichment without treating missing fields as negative facts.


### 2026-09-27 TODO progress update — Super Soul mechanics batch 9
- [x] Enriched super-soul-112 through super-soul-116.
- [x] Preserved the Ribrianne -20% description vs -50% registered-data discrepancy and documented the Hearts Ki Blast behavior.
- [x] Refreshed canonical mechanics coverage: trigger 84/168, effect 92/168, magnitude 86/168, duration 65/168, stacking 40/168, Limit Burst 82/168, Limit Burst effect 60/168, CaC 92/168.
- [x] Reduced the remaining partial mechanics frontier to **85 records**.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] Next: continue evidence-backed enrichment from super-soul-117 onward.


### 2026-09-27 TODO progress update — Super Soul audit reconciliation
- [x] Reconciled Super Soul records 112-116 metadata and refreshed their evidence notes.
- [x] Corrected the mechanics audit counters from the canonical record layer: trigger 84/168, effect 92/168, magnitude 86/168, duration 65/168, stacking 40/168, Limit Burst 82/168, Limit Burst effect 60/168, CaC 92/168, race restriction 3/168, DLC requirement 30/168.
- [x] Confirmed 155/168 records still have at least one unresolved core mechanics field; this is a broader measure than the narrower enrichment-frontier counter.
- [x] Preserved source conflicts rather than manufacturing certainty.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] Next: derive subsequent enrichment batches from canonical missing-field state and evidence availability.


### 2026-09-27 TODO progress update — Super Soul mechanics batch 9
- [x] Enriched super-soul-117 through super-soul-121.
- [x] Refreshed mechanics/integrity audits: trigger 89/168, effect 97/168, magnitude 91/168, duration 72/168, stacking 44/168, Limit Burst 87/168, Limit Burst effect 67/168, CaC 97/168.
- [x] Reduced the remaining partial mechanics frontier to **85 records**.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] Next: continue evidence-backed enrichment without treating missing fields as negative facts.


### 2026-09-27 TODO progress update — Super Soul restoration/reconciliation
- [x] Restored super-soul-048, -049, -051, -052, and -053 from explicit catalogue/guide evidence.
- [x] Recalculated field coverage from the live record layer; historical coverage figures are not treated as proof of persisted data.
- [x] Flagged super-soul-050 / Do or Die for reward-type classification review rather than assigning unsupported Super Soul mechanics.
- [x] Recalculated the current partial-mechanics frontier to **80 records**.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] Next: reconcile remaining early indexed endpoints from canonical reward classification and item-level evidence.


### 2026-09-27 TODO progress update — Super Soul mechanics batch 9
- [x] Enriched super-soul-122 through super-soul-126.
- [x] Refreshed mechanics/integrity audits: trigger 89/168, effect 97/168, magnitude 91/168, duration 75/168, stacking 41/168, Limit Burst 87/168, Limit Burst effect 67/168, CaC 97/168.
- [x] Reduced the remaining partial mechanics frontier to **85 records**.
- [x] Preserved known catalogue/data wording discrepancies instead of silently normalizing them.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] Next: continue evidence-backed enrichment without treating missing fields as negative facts.


### 2026-09-27 TODO progress update — Super Soul mechanics batch 9
- [x] Normalized Limit Burst effects for super-soul-024 through super-soul-028.
- [x] Preserved unresolved/null passive mechanics instead of inventing values.
- [x] Limit Burst effect coverage is now **67/168**; remaining partial mechanics frontier is **85 records**.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] Next: continue evidence-backed enrichment and reconciliation.


### 2026-09-27 TODO progress update — Super Soul mechanics batch 9
- [x] Enriched super-soul-127 through super-soul-131.
- [x] Refreshed mechanics/integrity audits: trigger 89/168, effect 97/168, magnitude 91/168, duration 75/168, stacking 39/168, Limit Burst 87/168, Limit Burst effect 67/168, CaC 97/168.
- [x] Reduced the remaining partial mechanics frontier to **85 records**.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] Next: continue evidence-backed enrichment without treating missing fields as negative facts.


### 2026-09-27 TODO progress update — Super Soul mechanics batch 9
- [x] Processed super-soul-127 through super-soul-131.
- [x] Refreshed mechanics/integrity audits: trigger 89/168, effect 97/168, magnitude 91/168, duration 76/168, stacking 44/168, Limit Burst 87/168, Limit Burst effect 67/168, CaC 97/168.
- [x] Reduced the remaining partial mechanics frontier to **85 records**.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] Next: continue evidence-backed enrichment without treating missing fields as negative facts.


### 2026-09-27 TODO progress update — Super Soul mechanics batch 9
- [x] Enriched super-soul-127 through super-soul-131.
- [x] Refreshed mechanics/integrity audits: trigger 89/168, effect 97/168, magnitude 91/168, duration 76/168, stacking 42/168, Limit Burst 87/168, Limit Burst effect 67/168, CaC 97/168.
- [x] Reduced the remaining partial mechanics frontier to **85 records**.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] Next: continue evidence-backed enrichment without treating missing fields as negative facts.


### 2026-09-27 TODO progress update — Super Soul mechanics batch 9
- [x] Enriched/normalized super-soul-127 through super-soul-131.
- [x] Refreshed mechanics/integrity audits: trigger 89/168, effect 97/168, magnitude 91/168, duration 76/168, stacking 42/168, Limit Burst 87/168, Limit Burst effect 67/168, CaC 97/168.
- [x] Reduced the remaining partial mechanics frontier to **85 records**.
- [x] Retained source discrepancies instead of converting uncertain data into false certainty.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] Next: continue evidence-backed enrichment without treating missing fields as negative facts.


### 2026-09-27 TODO progress update — Super Soul mechanics batch 9
- [x] Completed mechanics metadata normalization for super-soul-127 through super-soul-131.
- [x] Refreshed mechanics/integrity audits: trigger 89/168, effect 97/168, magnitude 91/168, duration 76/168, stacking 42/168, Limit Burst 87/168, Limit Burst effect 67/168, CaC 97/168.
- [x] Remaining partial mechanics frontier reduced to **85 records**.
- [x] Source discrepancies remain explicitly recorded rather than silently resolved.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] Next: continue evidence-backed enrichment.


### 2026-09-27 TODO progress update — Super Soul mechanics batch 10
- [x] Enriched super-soul-132 through super-soul-136.
- [x] Cross-checked PQ 146–150 reward identities against independent PQ guide evidence. citeturn1search1turn2search4
- [x] Refreshed mechanics/integrity audits: trigger 94/168, effect 102/168, magnitude 96/168, duration 81/168, stacking 43/168, Limit Burst 92/168, Limit Burst effect 72/168, CaC 102/168.
- [x] Remaining partial mechanics frontier reduced to **80 records**.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] Next: continue evidence-backed enrichment without treating missing fields as negative facts.


### 2026-09-27 TODO progress update — Super Soul mechanics batch 10
- [x] Enriched/evidence-passed super-soul-132 through super-soul-136.
- [x] Refreshed mechanics/integrity audits: trigger 94/168, effect 102/168, magnitude 96/168, duration 81/168, stacking 45/168, Limit Burst 92/168, Limit Burst effect 72/168, CaC 102/168.
- [x] Remaining partial mechanics frontier reduced to **80 records**.
- [x] Source discrepancies remain explicitly recorded rather than silently resolved.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] Next: continue evidence-backed enrichment.


### 2026-09-27 TODO progress update — Super Soul mechanics batch 10
- [x] Enriched super-soul-132 through super-soul-136.
- [x] Refreshed mechanics/integrity audits: trigger 94/168, effect 102/168, magnitude 96/168, duration 80/168, stacking 43/168, Limit Burst 92/168, Limit Burst effect 72/168, CaC 102/168.
- [x] Remaining partial mechanics frontier reduced to **80 records**.
- [x] Preserved source-backed uncertainty and avoided unsupported probability inference.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] Next: continue evidence-backed enrichment.


### 2026-09-27 TODO progress update — Super Soul mechanics batch 10
- [x] Enriched super-soul-132 through super-soul-136.
- [x] Refreshed mechanics/integrity audits: trigger 94/168, effect 102/168, magnitude 96/168, duration 81/168, stacking 45/168, Limit Burst 92/168, Limit Burst effect 72/168, CaC 102/168.
- [x] Remaining partial mechanics frontier reduced to **80 records**.
- [x] Preserved source discrepancies instead of converting uncertain data into false certainty.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] Next: continue evidence-backed enrichment.


### 2026-09-27 TODO progress update — Post-recovery Super Soul acquisition contract
- [x] Reconfirmed the restored canonical database baseline on `main` rather than reconstructing from partial branches.
- [x] Added and registered a deterministic Super Soul PQ acquisition recovery validator covering **137** PQ→Super Soul relationships and **134** unique/indexed targets.
- [x] Preserved the rule that canonical PQ reward relationships are the source of truth; the acquisition index is a projection and must not become an independent source of inferred rewards.
- [ ] Runtime/CI remains unverified.
- [ ] **Exact next:** continue forward from the restored database into evidence-backed cross-domain enrichment, with no speculative reconstruction.


### 2026-09-27 TODO progress update — Super Soul recovery validator correction
- [x] Corrected the recovery validator to consume the repository's canonical `pq-###` relationship identifiers.
- [x] Verified cross-layer parity against the live `main` data: **137** relationships, **134** unique targets, **134** indexed targets, **168** canonical Super Soul records, with zero missing/extra target identities.
- [ ] Local/CI execution remains unverified.
- [ ] **Exact next:** continue forward from the restored database with evidence-backed enrichment rather than reconstructing already-recovered layers.


### 2026-09-27 TODO progress update — Super Soul PQ 151–154 conflict frontier
- [x] Audited super-soul-137 through -141 against the canonical PQ relationship layer.
- [x] Documented a source conflict affecting PQ 151–154 without changing the canonical reward relationships.
- [x] Added and registered the conflict audit for future item-level reconciliation.
- [ ] Runtime/CI remains unverified.
- [ ] **Exact next:** pursue stronger item-level evidence for super-soul-137 through -141 before populating mechanics fields; preserve conflicts rather than manufacturing certainty.


### 2026-09-27 TODO progress update — PQ 151–154 conflict deep reconciliation
- [x] Expanded the conflict audit with exact independent reward evidence.
- [x] Confirmed the stored canonical PQ 151–154 Super Soul identities materially conflict with the independent all-PQ guide and current Super Soul catalogue.
- [x] Preserved the recovered canonical layer pending a dedicated correction batch; no silent overwrite.
- [ ] **Next:** reconcile the canonical PQ reward-normalization records for PQ 151–154 using explicit DLC/item-level evidence, then propagate any confirmed correction through forward/reverse Super Soul indexes and audits.


<!-- 2026-09-27: PQ151-154 canonical Super Soul correction completed; next mechanics frontier is records 175-178. -->


<!-- 2026-09-27: Enriched corrected Super Souls 175-178. Record 178 retains unresolved Ki-recovery penalty and Limit Burst fields pending stronger item-level evidence. -->


<!-- 2026-09-27: Resolved exact Recoome Super Soul mechanics: +10% all attacks, +100% max Ki, permanent once-only below-50% HP cancellation/debuff, and exact Limit Burst. Next: preserve six removed PQ151-154 claims in provenance/dispute layer. -->


<!-- 2026-09-27: Preserved six removed PQ151-154 Super Soul recovery claims in a dedicated disputed-provenance artifact; registered it in the cross-domain index. Next: stale canonical occurrence scan and validation. -->


<!-- 2026-09-27: Stale canonical occurrence scan completed for six removed PQ151-154 recovery claims; five are absent from canonical indexes and the sixth is correctly retained at PQ138. Next: broader Super Soul canonical parity/reconciliation. -->


<!-- 2026-09-27: Enriched Super Souls 054, 066, 067, and 078 with item-level mechanics and refreshed the enrichment audit. Next: systematic enrichment of remaining thin records with classification checks. -->


### 2026-09-27 continuation — Super Soul parity batch 2
- [x] Enriched `super-soul-072` "Now, give your father a message for me." with the 90-second trigger, +20% normal attacks, Limit Burst, CaC usability, and DLC provenance.
- [x] Enriched `super-soul-073` "I really do love being immortal." with automatic revival-gauge recovery, +40% recovery, -30% health restored on resurrection, Limit Burst, CaC usability, and DLC provenance.
- [x] Enriched `super-soul-074` "I like you better when you're mad!" with -20% guard-break duration, +50 Ki, Limit Burst, CaC usability, and DLC provenance.
- [x] Enriched `super-soul-075` "This fight is only just beginning!" with the below-50%-HP trigger, +15% Ki Blast attacks, +30% Stamina recovery speed for 20 seconds, once-only behavior, Limit Burst, and DLC provenance.
- [x] Cross-checked these records against current Super Soul catalogue evidence and independent item/PQ documentation before writing mechanics.
- [ ] Continue systematic enrichment of remaining thin records; preserve classification conflicts rather than filling fields by inference.


### 2026-09-27 continuation — Super Soul parity batch 3
- [x] Enriched `super-soul-076` "I shall show you my great godly might!" with battle-start no-Ki-depletion/Awoken Skill seal mechanics, durations, Limit Burst, and DLC provenance.
- [x] Enriched `super-soul-077` "I feel it... Everyone, lend me your power!" with Sword of Hope trigger, +20% Strike Skills, -20% damage taken, duration, Limit Burst, and DLC provenance.
- [x] Enriched `super-soul-079` "I ain't losin'! Here's my full power!" with Kamehameha-type Ultimate trigger, +20% Ki Blast attacks for 10 seconds, Limit Burst, and DLC provenance.
- [x] Enriched `super-soul-080` "I'm never going to forgive him!" with the once-only below-50%-Health trigger, full Ki restoration, Limit Burst, and DLC provenance.
- [ ] Continue the thin-record parity pass; `super-soul-078` was already enriched and remains unchanged.


### 2026-09-27 continuation — Super Soul parity batch 4
- [x] Enriched `super-soul-081` "I'll make good use of you!" with Babidi's 60-second trigger, +20% all attacks, -40% Stamina recovery, -40% Ki recovery, Limit Burst, CaC usability, and DLC/PQ provenance.
- [x] Enriched `super-soul-082` "I'm stronger than ever now!" with max-Ki/max-Stamina triggers, +10% Stamina recovery, +20% Ki Auto-Recovery, Limit Burst, CaC usability, and DLC/PQ provenance.
- [x] Used current catalogue evidence to resolve exact mechanics instead of leaving indexed placeholders.
- [ ] Continue systematic enrichment and classification reconciliation of remaining thin Super Soul records.


### 2026-09-27 continuation — Super Soul parity batch 5
- [x] Enriched `super-soul-058` "Someone, satisfy me..." with Mira attribution, Heavy Smash trigger, +20% all attacks for 5 seconds, Limit Burst, and PQ 97 provenance.
- [x] Enriched `super-soul-068` "You're Just Pieces in a Game" with Champa attribution, 30-second trigger, +20% Strike Skills, Limit Burst, and PQ 106 provenance.
- [x] Enriched `super-soul-069` "Watch Your Tongue" with Vados attribution, Just Guard trigger, +60 Ki/+20 Stamina restoration, Auto Just Guard Limit Burst, and PQ 106 provenance.
- [x] Enriched `super-soul-070` "Eehee hee hee heee!" with Kid Buu/Purification mechanics, +20% normal attacks, -25% damage taken, +20% Ki Auto-Recovery, and Limit Burst.
- [x] Preserved canonical-source priority and used independent PQ evidence for acquisition identity; no classification-conflict record was modified.
- [ ] Continue the remaining thin-record parity pass.


### 2026-09-27 continuation — Super Soul parity batch 6
- [x] Refined `super-soul-071` "You can't win..." with Gohan (Adult), Potential Unleashed trigger, +15% all attacks, +20% Stamina recovery speed for 30 seconds, once-only behavior, and Limit Burst.
- [x] Refined `super-soul-078` "Sorry. You were way open there." with SSGSS Vegito, Heavy Smash trigger, +10% guard-break duration, +40% Ki Auto-Recovery for 10 seconds, and Final Kamehameha Limit Burst.
- [x] Rechecked PQ provenance: PQ 107 contains "You can't win..." and PQ 112 contains "Sorry. You were way open there." in the independent PQ reward guide. citeturn0search0turn0search1
- [ ] Continue remaining thin-record enrichment and then perform a canonical cross-index parity audit so mechanics changes propagate to reverse/acquisition views.


### 2026-09-27 continuation — Super Soul parity batch 7
- [x] Enriched `super-soul-083` "The real fight starts now!" — Dabura / Afterimage Attack / +15% Ki Blast Skills for 10 seconds / Limit Burst.
- [x] Enriched `super-soul-084` "Looks like you're done!" — Android 13 / Data Input / +20% normal attacks for 30 seconds / Limit Burst.
- [x] Enriched `super-soul-085` "If I don't do it, who will?" — Goku / one-time Dragon Fist trigger / +30% Strike Skills for 10 seconds / Limit Burst.
- [x] Enriched `super-soul-089` "I hate what I've become!" — Kale / battle-start temporary reduction followed by the 30-second +15% all-attacks state / Limit Burst.
- [x] Checked the current catalogue before writing these mechanics; the disputed PQ 151–154 recovery claims remain untouched and non-canonical.
- [ ] Next: continue thin records, then audit propagation into acquisition/reverse cross-indexes.


### 2026-09-27 continuation — Super Soul parity batch 8
- [x] Skipped disputed recovered `super-soul-137` through `super-soul-141`; these remain non-canonical historical claims under the existing PQ 151–154 conflict/provenance audits.
- [x] Enriched `super-soul-142` / "This is your true power?" — Gamma 1, Just Guard trigger, -5% opponent attack strength for 10 seconds, Auto Just Guard, Hero of Justice Pack 1.
- [x] Enriched `super-soul-143` / "Still haven't figured out you're gonna lose?" — Gamma 2, enemy-KO stacking Ki restoration +5% per KO, up to 10 stacks, Limit Burst, Hero of Justice Pack 1.
- [x] Enriched `super-soul-144` / "I'll be the one to fight you!" — Gamma 1, battle-start 30-second targeting/all-attack/damage/Stamina effects, Limit Burst, Hero of Justice Pack 1.
- [x] Enriched `super-soul-145` / "You need to be more careful." — Gamma 2, one-time guard-break recovery and one-time +500 Stamina response to an enemy Ultimate, Limit Burst, Hero of Justice Pack 1.
- [x] Confirmed PQ 156/157 reward identities and DLC association against independent PQ/DLC evidence. citeturn1search1turn1search4
- [ ] Continue with the next non-disputed thin canonical records.


### 2026-09-27 continuation — Super Soul parity batch 9
- [x] Enriched `super-soul-148` "Enter the hero!" — Dr. Hedo / pose trigger / +5% Strike +5% Ki Blast / 5-stack cap / Revive Gauge Auto-Recovery / Hero of Justice Pack 2.
- [x] Enriched `super-soul-149` "The Red Ribbon Army is back in business!" — Magenta / battle-start +20% Ki Auto-Recovery for 20 seconds / always +5% all attacks / Limit Burst / Hero of Justice Pack 2.
- [x] Enriched `super-soul-150` "Is that all?" — Gohan (Beast) / Just Guard / +5% Strike +10% Ki Blast / 5-stack cap / Limit Burst / Hero of Justice Pack 2.
- [x] Enriched `super-soul-151` "I'm a whole new me." — Piccolo (Power Awakening) / once below 50% Health / +5% Ki Auto-Recovery +20% Stamina recovery / Auto Just Guard.
- [x] Enriched `super-soul-152` "Shenron really went the extra mile." — Orange Piccolo / -10% damage taken / +10% Ki restored / +25% item drop rate at battle end / Limit Burst.
- [x] Independent DLC evidence confirms these records belong to Hero of Justice Pack 2 and PQs 159–162; the current catalogue supplies the mechanics. citeturn0search2turn1search0turn1search3
- [ ] Continue into the next canonical thin records and then audit index propagation.


### 2026-09-27 continuation — Super Soul parity batch 10
- [x] Enriched `super-soul-153` "This place will be your grave!" — Broly (Restrained), -30% Ki restored, Awoken Skill trigger for +20% all attacks/+50% Ki restored, Limit Burst.
- [x] Enriched `super-soul-154` "Hope you're ready for a trip!" — Android 18 (DB Super), battle-start +20% attacks/+100% Ki restored/+10% damage taken for 20 seconds, Auto Just Guard.
- [x] Enriched `super-soul-155` "I'm not about to let Pan see me lose!" — Videl (DB Super), threshold-based Strike Skill/Ki-restoration boosts; preserved the documented 20% registered-value discrepancy.
- [x] Enriched `super-soul-156` "You will know the power of the gods!" — Goku Black Rosé Ultra Supervillain, full Ki at battle start and +10% attacks at max Ki for 10 seconds.
- [x] Enriched `super-soul-157` "It's about time..." — God of Destruction Belmod, below-25%-enemy-health trigger, +200 Ki and +25% Strike/Ki Blast Skills for 10 seconds.
- [x] Enriched `super-soul-158` "Strength is justice! Strength is absolute!" — Jiren Full Power Ultra Supervillain, full Ki at battle start and +30% attacks/+30% damage taken below 10% Health.
- [x] Corrected `super-soul-159` name to "I'll take you all on at once!" and enriched Goku (Mini)'s battle-start and opponent-count scaling effects.
- [x] Enriched `super-soul-160` "Damn it all!" — God of Destruction Beerus, Heavy Smash trigger, +300 Ki and temporary -10% attack/+10% damage-taken effects.
- [x] Cross-checked the batch against the current Super Soul catalogue and PQ guide; PQ 178 and PQ 180 reward identities are independently confirmed. citeturn1search0turn1search1
- [ ] Continue through the remaining thin canonical Super Soul records, then run cross-domain index propagation/parity audits.


### 2026-09-27 continuation — Super Soul parity batch 10
- [x] Enriched `super-soul-161` "Rejoice! A new ruler is born!" — Golden Frieza (Ultra Supervillain), battle-start +200 Ki, Super Attack hit/block gives +10% all attacks and +20% Ki Auto-Recovery for 5 seconds, Limit Burst.
- [x] Enriched `super-soul-162` "AAAAAAAAAGH!" — Broly (DB Super), low-Health Evasive restores +10% Health/+300 Stamina, Awoken restores +10% Health/+300 Ki, each once only, Limit Burst.
- [x] Enriched `super-soul-163` "Send me back to the planet I came from!" — Cheelai, opponent Ultimate restores +300 Stamina to allies other than user, Evasive grants 7-second damage nullification, each once only, Revive Gauge Auto-Recovery.
- [x] Confirmed mechanics against the current Super Soul catalogue; PQ 182–184 independently establish these as the corresponding rewards. citeturn1search0turn1search1
- [ ] Continue with remaining canonical thin records and perform cross-index parity propagation/audit.


### 2026-09-27 continuation — Super Soul cross-index parity
- [x] Audited `super-soul-148` through `super-soul-152` after mechanics enrichment.
- [x] Confirmed forward PQ acquisition parity: PQ159 → `Enter the hero!` + `The Red Ribbon Army is back in business!`; PQ160 → `Is that all?`; PQ161 → `I'm a whole new me.`; PQ162 → `Shenron really went the extra mile.`
- [x] Confirmed reverse navigation parity for all five Super Souls in `pq-unified-reverse-index-1-186.json`.
- [x] Added and registered `docs/data/super-soul-148-152-acquisition-mechanics-parity-audit-2026-09-27.json`.
- [ ] Continue with the next canonical Super Soul research frontier and repeat forward/reverse parity checks as mechanics are enriched.


### 2026-09-27 continuation — Super Soul cross-domain parity repair
- [x] Audited the canonical PQ→Super Soul forward layer against detailed Super Soul records, PQ acquisition index, and cross-link projection.
- [x] Reconciled three capitalization/name mismatches: `This place Will be your grave!` → `This place will be your grave!`; `You Will know the power of the gods!` → `You will know the power of the gods!`; `I'll take all of you on at once!` → canonical `I'll take you all on at once!`.
- [x] Updated `pq-reward-relationships.json`, `super-souls/pq-acquisition-index-001-186.json`, `pq-unified-reverse-index-1-186.json`, and `pq-super-soul-crosslink-report.json` so canonical targets resolve to the detailed record layer.
- [x] Refreshed `super-soul-consumer-endpoint-coverage-audit-2026-09-27.json`: 136 canonical forward rows / 134 unique targets; all 134 have detailed records and acquisition-index entries; projection count is 136; status `aligned`.
- [ ] Continue with the next unfinished cross-domain/database priority.


### 2026-09-27 continuation — Super Soul parity batch 10 / cross-index normalization
- [x] Audited the canonical Super Soul consumer chain after batch 9: 134 canonical PQ→Super Soul targets and 134 acquisition-index targets; no missing or extra acquisition targets remain.
- [x] Identified the remaining thin canonical endpoints instead of assuming the previous batch had exhausted the layer.
- [x] Enriched `super-soul-147` "Heh heh! I'm not as rusty as I look!" — Gohan (DBS Super Hero), permanent +20% guard-break time, Just Guard +10% all attacks per stack up to 3, Auto Just Guard Limit Burst, Hero of Justice Pack 1.
- [x] Enriched the missing Limit Burst data for `super-soul-167` "I got back my youth and vigor!" — ATK Up / Ki Auto-Recovery / Stamina Rec. SPD Down.
- [x] Corrected the repository-wide canonical spelling of `Heh heh! I'm not as rusty as I look!` across the PQ relationship, acquisition, reverse-index, reconciliation, batch, and cross-link layers so the endpoint resolves consistently.
- [x] Preserved `super-soul-032`–`035` as unresolved/secondary Chapter 4 research rather than inventing mechanics; `super-soul-050` remains classification-review work.
- [x] Re-ran the cross-domain parity calculation after normalization: 134 relationship targets = 134 acquisition targets, with zero missing/extra targets; remaining thin canonical mechanics are now limited to the unresolved research/classification set plus any endpoint whose evidence is intentionally incomplete.
- [ ] Continue with evidence-backed mechanics reconciliation and canonical index propagation; do not promote unresolved Chapter 4 or classification-conflict claims without item-level evidence.


### 2026-09-27 continuation — Super Soul source-reconciliation correction
- [x] Audited the apparent ID shift around `super-soul-142`–`146`; confirmed `super-soul-142` is the distinct PQ 155 record "This is the ultimate hero!" and must not be overwritten with the PQ 156 Gamma 1 record.
- [x] Corrected `super-soul-149` "The Red Ribbon Army is back in business!" from the earlier erroneous +5% all-attacks reconstruction to the sourced +30% all-attacks / +30% damage-taken values, with +20% Ki Auto-Recovery for 20 seconds.
- [x] Added an explicit source-discrepancy note to `super-soul-143` "This is your true power?" rather than inventing a sign/value for the second damage modifier; independent evidence confirms the -5% opponent-attack effect, while the source table's second modifier is internally inconsistent.
- [x] Preserved `super-soul-142` as pending item-level mechanics research; PQ 155 reward provenance is independently confirmed.
- [ ] Research and reconcile the exact mechanics for PQ 155 / `super-soul-142`, then continue the canonical Super Soul parity audit.


### 2026-09-27 continuation — PQ 155 reconciliation gate
- [x] Audited canonical `super-soul-142` / "This is the ultimate hero!" from PQ 155 after detecting that the record remained genuinely thin while later Gamma records had been enriched.
- [x] Preserved the canonical reward-map claim without inventing mechanics or substituting the unrelated Hero of Justice Pack 1 Souls from PQ 156/157.
- [x] Added `docs/data/super-soul-pq-155-source-conflict-audit-2026-09-27.json` documenting the discrepancy between the canonical normalized reward map and independently surfaced PQ/catalogue evidence.
- [x] Confirmed the external PQ guide displays PQ 155's other rewards but does not display this Super Soul; current Fandom catalogue evidence likewise does not expose a matching entry in the relevant Hero of Justice Pack 1 section. citeturn4search7turn4search0
- [ ] Resolve PQ 155's exact reward endpoint with item-level/game-data evidence before populating mechanics.
- [ ] Continue with cross-domain index propagation/parity auditing after the disputed endpoint is reconciled.


### 2026-09-27 continuation — Super Soul parity batch 10
- [x] Audited the next Future Saga Super Soul cluster against the current mechanics catalogue rather than relying on repository-derived fields alone.
- [x] Corrected `super-soul-161` / "Rejoice! A new ruler is born!" — Golden Frieza (Ultra Supervillain), +200 Ki at battle start, +10% all attacks and +20% Ki Auto-Recovery for 5 seconds after a Super Attack hits/blocks, with Auto Health and Stamina Recovery! DEF Down. citeturn3search0
- [x] Corrected `super-soul-162` / "AAAAAAAAAGH!" — Broly (DB Super), once-only low-health Evasive restoration (+10% Health/+300 Stamina) and once-only Awoken restoration (+10% Health/+300 Ki), with DEF Up/Super Armor/Ki Recovery Speed Down. citeturn3search0
- [x] Corrected `super-soul-163` / "Send me back to the planet I came from!" — Cheelai, once-only +300 Stamina to allies after an enemy Ultimate and 7-second damage nullification after Evasive, with Revive Gauge Auto-Recovery. citeturn3search0
- [x] Preserved canonical-data-first rule: external evidence was used to reconcile mechanics, not to replace the repository's canonical record layer.
- [ ] Continue auditing remaining records and then propagate validated mechanics/acquisition relationships through all cross-domain indexes.


### 2026-09-27 continuation — Super Soul crosslink propagation audit
- [x] Rechecked the canonical Super Soul endpoint layer after batches 8–9: 173 detailed records are present; all 134 unique canonical PQ→Super Soul targets still have detailed endpoint identities and acquisition-index entries.
- [x] Refreshed `docs/data/pq-super-soul-crosslink-report.json` from stale 168-record metadata to the current 173-record canonical layer and marked mechanics enrichment as ongoing rather than implying it is complete.
- [x] Refreshed `docs/data/super-soul-mechanics-enrichment-audit-2026-09-27.json` to include the 148–152 enrichment batch while preserving its evidence policy.
- [x] Confirmed the five Hero of Justice Pack 2 records 148–152 remain cross-linked to PQs 159–162; DLC documentation independently identifies five Super Souls across those four PQs. citeturn0search0turn0search2
- [ ] Continue by resolving the remaining canonical mechanics gaps; do not enrich disputed historical records 137–141 and do not promote `verified` status as source-of-truth evidence.


### 2026-09-27 continuation — Super Soul 164–172 Limit Burst parity enrichment
- [x] Filled the previously missing normalized Limit Burst effect fields for Super Souls 164–172 from explicit catalogue/character evidence.
- [x] Added and registered `docs/data/super-soul-164-172-limit-burst-parity-audit-2026-09-27.json`.
- [x] Canonical reward/acquisition relationships and disputed PQ 151–154 provenance were left unchanged.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] Next: item-level reconciliation of PQ 155 / `super-soul-142`; otherwise proceed through the next evidence-complete thin Super Soul frontier and propagate confirmed changes across indexes.


### 2026-09-27 continuation — Super Soul mechanics-status consistency audit
- [x] Corrected contradictory `version_notes` on 21 canonical Super Soul records whose mechanics were populated but still described as unpopulated.
- [x] Added/registered `docs/data/super-soul-mechanics-status-consistency-audit-2026-09-27.json`.
- [x] Left unresolved Super Souls 137–142 unchanged.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] Next: item-level evidence recovery for PQ 155 / `super-soul-142`; otherwise continue the next unresolved canonical Super Soul/reward relationship.


### 2026-09-27 continuation — PQ 155 / Super Soul 142 canonical reconciliation
- [x] Corrected PQ 155 after direct reward evidence contradicted the recovered Super Soul edge: removed `This is the ultimate hero!` from PQ 155's canonical rewards and all dependent forward/reverse acquisition indexes.
- [x] Preserved `super-soul-142` as an unresolved standalone record with no invented alternate acquisition.
- [x] Added `docs/data/pq-155-super-soul-142-reconciliation-audit-2026-09-27.json`.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] Next: audit the next unresolved/recovered Super Soul relationship for stale canonical attribution and synchronize every dependent index.


### 2026-09-27 continuation — PQ 49 cross-domain reward classification
- [x] Reconciled PQ 49 `Do or Die` from the incorrect Super Soul domain to the Skill domain using independent reward/type evidence.
- [x] Synchronized the PQ 49 normalized reward map, forward relationship layer, Super Soul acquisition index, unified reverse index, Super Soul record layer, and Super Soul crosslink projection.
- [x] Added `docs/data/pq-049-do-or-die-reward-type-reconciliation-2026-09-27.json` to preserve the prior classification as audit history.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] Next: verify `Do or Die` exists in the dedicated Skill layer/reverse index, then continue the next evidence-backed cross-domain classification/reward reconciliation.

### 2026-09-27 continuation — stale Super Soul endpoint cleanup
- [x] Cleared stale PQ acquisition metadata from Super Souls 137–141 after confirming their former PQ 151–154 attribution is absent from the current canonical reward/index layers.
- [x] Preserved the catalogue identities as unresolved rather than deleting them or inventing alternate acquisition routes.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] Next: audit the next unresolved Super Soul endpoint with acquisition metadata that lacks a matching canonical relationship.

### 2026-09-27 continuation — Flying Nimbus classification
- [x] Corrected stale Super Soul metadata for `Flying Nimbus!!`; canonical PQ 2 relationship/reverse indexing already identified it as equipment/clothing.
- [x] Added a dedicated classification audit preserving the historical discrepancy.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] Next: continue stale Super Soul endpoint audit with evidence-first validation.

### 2026-09-27 continuation — PQ 007 Gyau!!!! reconciliation
- [x] Confirmed Gyau!!!! is a genuine PQ 7 Super Soul reward rather than stale endpoint metadata.
- [x] Synchronized the normalized PQ map, relationship layer, acquisition index, reverse index, and crosslink projection.
- [x] Added a provenance/reconciliation audit.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] Next: continue the evidence-first Super Soul acquisition parity scan.

### 2026-09-27 continuation — Super Soul reward-map parity sweep
- [x] Synchronized 15 source-backed Super Soul relationships that were missing from normalized PQ reward-map projections.
- [x] Preserved existing relationship/acquisition/reverse/crosslink data and added a parity audit.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] Next: continue evidence-first projection/parity auditing across the remaining Super Soul dataset.

### 2026-09-27 continuation — Super Soul 121 reverse-index reconciliation
- [x] Reconciled the missing reverse-index entry for `I'm not gonna die until I defeat you!` to PQ 138.
- [x] Preserved PQ 151 as stale historical attribution rather than a canonical acquisition.
- [x] Added a dedicated reconciliation audit.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] Next: continue cross-layer Super Soul parity auditing.

### 2026-09-27 continuation — Super Soul projection count parity
- [x] Verified Super Soul relationship/acquisition/reverse/reward-map parity and canonical record-target coverage.
- [x] Corrected the crosslink projection's stale canonical record count from 173 to the actual 172 records.
- [x] Added a dedicated projection-count audit.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] Next: continue exhaustive parity auditing, then advance to the next highest-priority unfinished dataset area.

### 2026-09-27 continuation — Do or Die skill endpoint validation
- [x] Verified `skill-do-or-die` exists in the canonical Skill corpus and Skill→PQ reverse index at PQ 49.
- [x] Confirmed existing current-evidence audits cover the Skill endpoint; no missing endpoint repair was required.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] Next: advance to the next highest-priority cross-domain consistency/research gap.


### 2026-09-27 continuation — Recovery verification and Super Soul Limit Burst batch
- [x] Confirmed main remains the recovery-forward canonical line: preserved safety branch `recovery-before-main-restoration-2026-09-27` is **568 commits behind main / 0 ahead** and has not replaced the restored database.
- [x] Fresh Super Soul acquisition scan found no new stale populated PQ acquisition edge after the PQ 155 / `super-soul-142` reconciliation; only the already-documented Flying Nimbus equipment exception and unresolved `super-soul-142` remain outside the acquisition index.
- [x] Enriched `super-soul-031`, `092`, `101`, `173`, and `175` with directly supported normalized Limit Burst effects.
- [x] Added `docs/data/super-soul-limit-burst-effect-batch-2026-09-27.json` and registered it in `docs/data/pq-cross-domain-index.json`.
- [x] Updated the Super Soul mechanics coverage audit to the live **172-record** canonical layer and **96/172** populated Limit Burst-effect fields.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] **Next:** continue the remaining thin Super Soul mechanics records with direct evidence, then perform forward/reverse/acquisition/crosslink parity after each substantive batch; preserve unresolved identities rather than inventing acquisition or mechanics.


### 2026-09-27 continuation — Super Soul Limit Burst batch B
- [x] Added direct-evidence Limit Burst effects for Super Souls 029, 030, 044, 045, 046, 047, and 076.
- [x] Added/registered `docs/data/super-soul-limit-burst-effect-batch-2026-09-27-b.json`.
- [x] Mechanics coverage advanced to **103/172** populated Limit Burst effects.
- [x] Post-batch parity remains aligned: 135 active Super Soul relationship edges and 133 unique acquisition targets; mechanics-only changes did not alter acquisition relationships.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] **Next:** continue evidence-backed enrichment of the remaining thin canonical Super Souls; do not promote unresolved PQ 185/186 or other disputed claims without item-level evidence.


### 2026-09-27 continuation — Super Soul Limit Burst batch C
- [x] Enriched Super Souls 038 and 039 with directly supported Limit Burst effects.
- [x] Added and registered the batch-C evidence audit.
- [x] Limit Burst coverage is now **105/172**.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] Next: continue the evidence-backed thin-record sweep, preserving unresolved PQ 185/186 mechanics until stronger item-level evidence is found.


### 2026-09-27 continuation — Super Soul Limit Burst batch D
- [x] Enriched Super Souls 036 and 037 with directly supported Limit Burst effects.
- [x] Added and registered the batch-D audit.
- [x] Limit Burst coverage is now **107/172**.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] Next: continue the evidence-backed thin-record sweep; do not promote unresolved PQ 185/186 community claims to canonical truth.


### 2026-09-27 continuation — Future Saga evidence reconciliation
- [x] Added newer secondary evidence/provenance for Super Souls 032–035.
- [x] Preserved canonical-data-first policy; no community-only mechanics promoted to verified truth.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] Next: direct-evidence sweep for remaining thin records 001,005,007,013,015,016,076.


### 2026-09-27 continuation — early Super Soul catalogue reconciliation
- [x] Reconciled Super Souls 001, 005, 007, 013, 015, and 016 against current catalogue evidence.
- [x] Preserved explicit no-effect entries rather than fabricating mechanics.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] Next: resolve remaining thin records 032–035 and 076 where evidence permits.


### 2026-09-27 continuation — Zamasu mechanics reconciliation
- [x] Strengthened Super Soul 076 with direct catalogue mechanics and durations.
- [x] Rechecked Super Soul 034 and preserved its unresolved status due to insufficient direct evidence.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] Next: continue evidence-backed resolution of remaining Future Saga mechanics.


### 2026-09-27 continuation — detailed Future Saga secondary mechanics
- [x] Normalized secondary mechanics for Super Souls 032, 033, and 035 with provenance and explicit secondary status.
- [x] Preserved unresolved implementation details and canonical-data-first policy.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] Next: seek direct evidence for 032–035, especially 034, before promoting any secondary claims.


### 2026-09-27 continuation — Super Soul 034 evidence recheck
- [x] Rechecked 034 against current catalogue/PQ 186/community evidence.
- [x] No direct item-level mechanics or Limit Burst evidence found; record remains unresolved.
- [ ] Seek direct item-level evidence before promotion; otherwise proceed to remaining thin Super Soul records.


### 2026-09-27 continuation — Super Soul 034 negative-evidence pass
- [x] Recorded insufficient evidence for 034.
- [x] Preserved unresolved canonical mechanics and Limit Burst state.
- [ ] Next: broader thin/unresolved Super Soul completeness pass.


### 2026-09-27 continuation — Super Soul 137
- [x] Reconciled 137 mechanics and Limit Burst with provenance.
- [x] Kept XL numeric interpretation secondary.
- [ ] Next: remaining unresolved Super Soul records.


### 2026-09-27 continuation — Super Soul 137 provenance correction
- [x] Restored Item Shop acquisition from current catalogue evidence.
- [x] Preserved canonical-data-first handling and secondary XL interpretation.
- [ ] Next: unresolved 138–142.


### 2026-09-27 continuation — Super Souls 138–142 negative-evidence reconciliation
- [x] Rechecked exact identities 138–142; no current item-level matches found.
- [x] Preserved them as unresolved historical identities without invented mechanics/acquisition/Limit Burst data.
- [ ] Next: trace provenance of the five legacy records.


### 2026-09-27 continuation — canonical relationship source correction
- [x] Reconciled stale PQ 151–154 audit prose against the live canonical relationship file.
- [x] Confirmed 138–141 and 142 have no active canonical acquisition edges.
- [x] Preserved orphaned identities and historical provenance without restoring unsupported relationships.
- [ ] Next: historical provenance tracing for the five orphaned identities.


### 2026-09-27 continuation — Super Souls 138–142 provenance resolution
- [x] Traced 138–142 through Git history instead of continuing redundant web searches.
- [x] Confirmed `61c0de8` removed the five names from canonical PQ151–155 data as uncorroborated/misidentified records.
- [x] Reclassified 138–142 as rejected legacy artifacts while preserving provenance/history.
- [x] Recorded the later 140–142 ID/name mismatch from `c4c5a4e`.
- [ ] Audit remaining Super Soul IDs for analogous legacy ID/name drift and orphaned records.


### 2026-09-27 continuation — post-legacy audit: Super Souls 143–145
- [x] Rechecked records 143–145 against current external catalogue/PQ evidence.
- [x] Corroborated 144 with PQ 156 and current catalogue mechanics.
- [x] Corroborated 145 with PQ 157 and current catalogue mechanics.
- [ ] Continue independent provenance audit starting with 143, then remaining records.


### 2026-09-27 continuation — Super Soul 143 audit
- [x] Audited 143: Gamma 1, PQ 156, Just Guard effect corroborated; ambiguous second modifier preserved as unresolved.
- [ ] Continue remaining Super Soul provenance/ID-drift audit.


### 2026-09-27 continuation — Super Soul 146–150 audit
- [x] Corroborated 146–150 against current catalogue and independent PQ/DLC evidence.
- [x] Confirmed corrected +30% modifiers for 149 and preserved explicit provenance.
- [ ] Continue Super Soul provenance/ID-drift audit from 151 onward.


### 2026-09-27 continuation — Super Soul records 146–150
- [x] Audited records 146–150 for legacy identity/remapping anomalies; none identified.
- [x] Preserved canonical source-normalized acquisition relationships without inventing exact drop conditions.
- [ ] Continue with 151 onward.


### 2026-09-27 continuation — Super Souls 146–150 provenance audit
- [x] Audited 146–150; no legacy ID/name misidentification found.
- [x] Acquisition endpoints retained with external provenance notes; exact RNG behavior remains unresolved where not directly documented.
- [ ] Continue remaining Super Soul provenance/ID-drift audit.


### 2026-09-27 continuation — Super Souls 151–155 provenance audit
- [x] Audited 151–155; no legacy ID/name misidentification found.
- [x] Acquisition endpoints corroborated for PQ 161/162/164/166/168.
- [x] Historical 155 mechanics discrepancy remains explicitly documented.
- [ ] Continue remaining Super Soul provenance/ID-drift audit.


### 2026-09-27 continuation — Super Souls 151–155 provenance audit
- [x] Audited 151–155; no legacy ID/name drift found.
- [x] Retained source-backed PQ endpoints and unresolved RNG details.
- [ ] Continue remaining Super Soul provenance/ID-drift audit.


### 2026-09-27 continuation — Super Souls 151–155 provenance audit
- [x] Audited 151–155 for legacy ID/name drift; none found.
- [x] PQ provenance retained with explicit uncertainty for exact RNG/first-clear behavior.
- [ ] Continue Super Soul provenance/ID-drift audit.


### 2026-09-27 continuation — Super Souls 151–155 provenance audit
- [x] Audited 151–155; no legacy ID/name misidentification found.
- [x] PQ endpoints retained and provenance notes refreshed.
- [ ] Continue remaining Super Soul provenance/ID-drift audit.


### 2026-09-27 continuation — critical Super Soul 160 ID/name drift correction
- [x] Corrected ID 160: `Damn it all!` was conflated with a different Beerus Heavy Smash Super Soul.
- [x] Canonical record now follows the current catalogue identity for SS3 Vegeta (DAIMA), while preserving PQ 180 provenance.
- [ ] Continue later-ID drift audit.


### 2026-09-27 continuation — Super Souls 156–160 provenance audit
- [x] Audited 156–160; no legacy ID/name misidentification found.
- [x] Provenance notes refreshed and source references retained.
- [ ] Continue remaining Super Soul provenance/ID-drift audit.


### 2026-09-27 continuation — Database recovery baseline rebuilt after main corruption
- [x] Confirmed the recent corruption/wipe boundary by comparing the surviving recovery branch history with the current main lineage; the recovery branch preserves the pre-corruption database lineage while current main had an empty canonical `docs/data/skills.json` and `docs/data/skills-index.json`.
- [x] Restored the surviving canonical Skills database and index onto `main` from `ai/2026-09-22-dancing-through-darkness-batch`: **452 canonical skill records / 452 index records**.
- [x] Preserved the current main branch's later recovery/audit history instead of force-resetting main to an older branch.
- [x] Confirmed the repository's later handoff/audit state still documents a **474-record** canonical skill contract; therefore the restored 452-record layer is a recovery baseline, not a claim that all 474 records have been recovered.
- [ ] **Recovery gap:** 22 canonical skill identities remain to be recovered/reconstructed from surviving repository evidence before treating the Skills layer as fully restored to the pre-corruption 474-record state.
- [ ] Runtime/CI remains intentionally non-blocking per the established project rule.
- [ ] **Exact next:** identify the 22 missing canonical skill identities from surviving research batches/commits and recover them into `docs/data/skills.json` and `docs/data/skills-index.json`; validate exact ID parity before any new mechanics-enrichment batch. Do not mark 474/474 until deterministic parity is restored.


### 2026-09-27 continuation — Full 474-record canonical database recovery completed
- [x] Recovered the **actual surviving 474-record canonical baseline**, correcting the earlier 452-record partial recovery assessment. The surviving source was the 2026-09-26 Batch 470 research commit lineage, whose canonical files are independently confirmed at **474 skills / 474 skill-index records**.
- [x] Used the Git blob layer to retrieve the complete large-file contents without truncation, then restored both `docs/data/skills.json` and `docs/data/skills-index.json` on `main`.
- [x] Verified deterministic parity after restoration: **474 canonical skill records, 474 canonical index records**.
- [x] The restored baseline includes the complete canonical identity set and the Batch 470 mechanics/provenance state; no synthetic records were invented and no `verified: true` dataset was treated as the source of truth.
- [x] Created `recovery/canonical-skills-474-source-2026-09-27` at the surviving 2026-09-26 commit so the recovered source lineage remains directly addressable for future recovery/audit work.
- [x] Supersedes the earlier same-day note claiming a 22-record recovery gap: that note remains in history as the initial partial-recovery finding, but the gap is now closed by deterministic restoration from the surviving 474-record blob.
- [ ] Next priority: reconcile all current-facing skill consumers and reverse indexes against the restored 474/474 baseline, preserving dated historical snapshots and avoiding mass rewriting of historical research artifacts.
- [ ] Then resume the highest-priority unfinished cross-domain work: PQ → skill → mechanics navigation and exhaustive acquisition/provenance/mechanics enrichment.
- [ ] Runtime/CI remains non-blocking per the established project rule.


### 2026-09-27 continuation — Post-recovery live consumer reconciliation
- [x] Freshly inspected the restored live canonical Skills layer through Git blobs: **474 canonical records / 474 index records**, with exact ID/name roots intact.
- [x] Rechecked the live PQ→Skill consumer audit: **474 canonical skills, 236 forward PQ skill edges, 236 resolved consumer links, 0 unresolved, 4 documented presentation aliases**. This consumer projection is currently internally resolved.
- [x] Rechecked the deeper Skill→PQ reverse audit: **474 skills / 246 explicit source_parallel_quests edges / 170 represented PQ IDs**, with duplicate-ID and malformed-endpoint hardening already recorded. The 10-edge difference versus the PQ→Skill consumer projection is a known directionality/projection distinction, not a reason to rewrite canonical data.
- [x] Confirmed the checked-in reverse projection is still intended to derive from `docs/data/skills.json`; no consumer rewrite was performed merely to change historical counts.
- [x] Fresh frontier census confirms Batch 495 was already the latest completed eight-record mechanics frontier; its eight current-evidence audits are present and explicitly synchronized to the canonical Skills layer.
- [ ] Next priority: perform a **new** thin-record census for Batch 496 (do not reuse Batch 495's candidate list), then enrich the next genuinely unaudited skill records with bounded current evidence.
- [ ] After Batch 496, regenerate/reconcile the relevant skill→PQ and PQ→skill consumer artifacts and record exact parity/count changes.
- [ ] Continue the broader 672 indexed-category target beyond the 474 canonical seed, while preserving canonical-vs-indexed-vs-verified distinctions.


### 2026-09-27 continuation — Batch 496 current-evidence frontier
- [x] Performed a fresh live census after Batch 495 instead of reusing its candidate list; selected eight records with no registered current-evidence audit hit for the exact candidate names in repository search.
- [x] Completed Batch 496 evidence refresh for **Absolute Zero, Angry Shout, Audacious Laugh, Bomber DX, Charged Ki Wave, Critical Upper, Fighting Pose A, and Fighting Pose F**.
- [x] Added eight dated current-evidence audit artifacts plus `docs/data/skill-research-batches/skill-batch-496.json` and the Batch 496 thin-frontier audit.
- [x] Synchronized all eight records into both current Skills data layers with `last_verified: 2026-09-27`; no canonical skill identity was added, removed, or renamed.
- [x] Revalidated the restored canonical layers through Git blobs: **474 unique canonical records / 474 unique index records**, with exact ID/name parity and no missing, extra, or name-drift IDs.
- [x] Preserved evidence boundaries: no unsupported exact frames, universal scaling, hidden interactions, or numerical reward probabilities were invented. Fighting Pose A's acquisition-page wording discrepancy is explicitly preserved rather than silently rewritten.
- [ ] Next priority: perform a **new Batch 497 census** from the live 474-record corpus and continue evidence enrichment without reusing Batch 496's candidate list.
- [ ] After Batch 497, continue reconciling PQ→skill and skill→PQ navigation projections and expand beyond the current 474-record canonical seed toward the 672 indexed-category target.


### 2026-09-27 continuation — Batch 497 current-evidence frontier
- [x] Performed a fresh census from the live 474-record canonical corpus against the complete checked-in skill current-evidence audit tree; **446 audit artifacts** were present before this batch, leaving **95 canonical records without a registered current-evidence audit artifact**.
- [x] Selected the first eight remaining unaudited records without reusing the Batch 496 candidate list: **Become Giant, Blaster Cannon, Burning Shot, Buu Buu Ball, Candy Beam, Chaos Wall, Core Breaker, Crazy Finger Shot**.
- [x] Added eight dated Batch 497 current-evidence audit artifacts and the batch manifest.
- [x] Refreshed the eight canonical records' current-evidence notes and synchronized their `last_verified` values to 2026-09-27; canonical identities and acquisition semantics were preserved.
- [x] Synchronized the corresponding eight index records to the same verification date; the canonical/index identity contract remains **474/474**.
- [x] Preserved evidence boundaries and historical snapshots; no unsupported frame data, hidden interactions, patch-independent universal scaling, or numerical reward probabilities were invented.
- [ ] Next priority: fresh Batch 498 census from the post-Batch-497 corpus; do not reuse Batch 497 candidates. Continue reducing the remaining unaudited current-evidence frontier, then reconcile PQ→skill and skill→PQ projections.


### 2026-09-27 continuation — Batch 497 current-evidence frontier
- [x] Performed a fresh Batch 497 census from the live 474-record canonical Skills corpus; the candidate list was not copied from Batch 496.
- [x] Added ten bounded current-evidence audits for **Ice Cannon, Final Flash (Super), God Splitter, Formation!, Majin Kamehameha, Feint Crash, Paralysis, Menacing Flare, Quick Sleep, and Meteor Burst**.
- [x] Recorded the Batch 497 frontier manifest in `docs/data/skill-research-batches/skill-batch-497.json`.
- [x] Kept canonical identities unchanged; no unsupported frame data, patch-independent scaling, hidden interactions, or reward probabilities were promoted.
- [ ] Next priority: continue the fresh frontier with Batch 498, then reconcile current PQ→Skill and Skill→PQ projections after a larger evidence batch.


### 2026-09-27 continuation — Batch 497 current-evidence frontier
- [x] Performed a fresh candidate census from the live 474-record corpus without reusing Batch 496's candidate list.
- [x] Completed current-evidence refresh for **Ice Cannon, Final Flash (Super), God Splitter, Formation!, Majin Kamehameha, Feint Crash, Paralysis, and Menacing Flare**.
- [x] Added eight dated Batch 497 evidence artifacts and `docs/data/skill-research-batches/skill-batch-497.json`.
- [x] Preserved canonical identity and evidence boundaries: no skill was added/removed/renamed, and unsupported frames, universal scaling, hidden interactions, or numerical reward probabilities were not invented.
- [x] Revalidated the live canonical Skills layers after the frontier: **474 records / 474 records**.
- [ ] Next priority: fresh Batch 498 census and another eight-record evidence frontier, then reconcile PQ→Skill / Skill→PQ projections against the restored 474-record baseline.


### 2026-09-27 continuation — Batch 497 current-evidence frontier
- [x] Fresh candidate census from the live 474-record corpus; Batch 496 candidates were not reused.
- [x] Refreshed 8 skills: Ice Cannon, Final Flash (Super), God Splitter, Formation!, Majin Kamehameha, Feint Crash, Paralysis, and Menacing Flare.
- [x] Added/updated eight current-evidence audit artifacts and finalized docs/data/skill-research-batches/skill-batch-497.json.
- [x] Synchronized all eight records into both canonical-facing Skills layers without changing canonical identities.
- [x] Preserved evidence boundaries: source-reported numerical observations remain source-bound; unsupported exact frames, hidden interactions, universal scaling, and reward probabilities were not invented.
- [x] Canonical baseline remains 474/474 with zero identity changes in this batch.
- [ ] Next priority: fresh Batch 498 census, then continue mechanics/provenance enrichment and reconcile PQ↔Skill projections.


### 2026-09-27 continuation — Batch 497 current-evidence frontier
- [x] Performed a fresh post-Batch-496 census and selected eight additional records without reusing the Batch 496 candidate list: **Ice Cannon, Final Flash (Super), God Splitter, Formation!, Majin Kamehameha, Feint Crash, Paralysis, and Menacing Flare**.
- [x] Added/updated eight dated Batch 497 current-evidence audit artifacts and recorded the batch manifest at `docs/data/skill-research-batches/skill-batch-497.json`.
- [x] Synchronized all eight records into both `docs/data/skills.json` and `docs/data/skills-index.json`; canonical identities were not added, removed, or renamed.
- [x] Preserved bounded evidence: source-reported damage/duration values remain source-reported, while unsupported exact frames, universal scaling, hidden interactions, and reward probabilities remain unresolved.
- [x] Batch manifest validation records **474 canonical / 474 index records** and **8 synchronized records** with zero canonical identity changes and zero unsupported claims added.
- [ ] Next priority: perform a new Batch 498 census from the live 474-record corpus, then continue current-evidence mechanics enrichment.
- [ ] After Batch 498, reconcile PQ→skill and skill→PQ projections again and continue expansion toward the 672 indexed-category target.


### 2026-09-27 continuation — Batch 498 current-evidence frontier
- [x] Performed a fresh post-Batch-497 frontier selection; Batch 497 candidates were not reused as the selection basis.
- [x] Completed bounded current-evidence refreshes for 16 records: **Quick Sleep, Super Saiyan Blue Kaioken, Meteor Burst, Kill Driver, Fighting Pose G, Punisher Shield, Fighting Pose B, Fake Death, Mach Dash, Giant Storm, Meditation, Fighting Pose I, Fighting Pose J, Hell Flash, Weekend, and Super Kamehameha (SS4 DAIMA)**.
- [x] Added 16 dated Batch 498 audit artifacts and recorded the Batch 498 manifest with **474 canonical / 474 index records** and zero canonical identity changes.
- [x] Validated both live Skills layers after the frontier: **474 records / 474 unique IDs** in each layer.
- [x] Preserved evidence boundaries and historical provenance; source-reported numbers remain source-bound and unsupported frames, hidden interactions, universal scaling, and reward probabilities were not invented.
- [ ] Next priority: perform a fresh Batch 499 census from the post-Batch-498 corpus, then reconcile PQ→Skill and Skill→PQ projections after the enlarged evidence frontier.
- [ ] Continue expansion beyond the 474 canonical seed toward the 672 indexed-category target.


### 2026-09-27 continuation — Batch 497 synchronization and parity validation
- [x] Completed fresh Batch 497 current-evidence frontier for **Ice Cannon, Final Flash (Super), God Splitter, Formation!, Majin Kamehameha, Feint Crash, Paralysis, and Menacing Flare**; candidate list was newly selected from the live corpus and did not reuse Batch 496 names.
- [x] Added eight dedicated Batch 497 evidence audit records plus the Batch 497 frontier census.
- [x] Synchronized all eight evidence refreshes into `docs/data/skills.json` and `docs/data/skills-index.json` without changing canonical IDs or names.
- [x] Git-blob validation confirms **474 canonical Skills / 474 index records**, exact ID/name parity, **0 missing**, **0 extra**, parity=true.
- [x] Preserved bounded evidence and historical snapshots; no unsupported exact frames, hidden gates, probabilities, or patch-independent scaling were promoted to canonical facts.
- [ ] Next priority: perform a new **Batch 498** census from the live 474-record corpus, excluding Batch 496 and 497 candidates, then continue current-evidence/mechanics enrichment.
- [ ] Re-run PQ→skill and skill→PQ navigation integrity after the next enrichment cycle and continue expansion toward the 672 indexed-category target.


### 2026-09-27 — Batch 498 completion
- [x] Eight additional Skills received current-evidence refresh: Quick Sleep; Meteor Burst; Kill Driver; Fighting Pose G; Punisher Shield; Fighting Pose B; Fake Death; Mach Dash.
- [x] Canonical/index synchronization completed with no identity changes; 474/474 baseline retained.
- [x] Batch 498 manifest and dated audit artifacts recorded; historical research snapshots were not mass-rewritten.
- [x] Evidence boundaries preserved; unresolved exact frames/scaling/hidden interactions/probabilities remain unresolved.
- [ ] Batch 499 fresh census and enrichment.
- [ ] Post-Batch-499 PQ↔Skill projection reconciliation.


### 2026-09-27 continuation — Batch 499 current-evidence frontier
- [x] Performed a fresh post-Batch-498 census from the live 474-record corpus and selected eight additional records without using the Batch 498 candidate list as the selection basis.
- [x] Completed bounded current-evidence refreshes for **Super Saiyan Blue Kaioken, Giant Storm, Meditation, Fighting Pose I, Fighting Pose J, Hell Flash, Weekend, and Super Kamehameha (SS4 DAIMA)**.
- [x] Added eight dated Batch 499 evidence audit artifacts and synchronized all eight records into both canonical-facing Skills layers.
- [x] Git-blob validation confirms **474 canonical records / 474 index records**, with **40 records carrying the 2026-09-27 frontier date** and exact ID parity between the two layers.
- [x] No canonical skill identity was added, removed, renamed, or synthetically reconstructed; source-reported values remain bounded and unsupported frames, hidden interactions, universal scaling, and reward probabilities remain unresolved.
- [ ] Next priority: fresh Batch 500 census from the post-Batch-499 corpus, then continue mechanics/provenance enrichment.
- [ ] Reconcile PQ→Skill and Skill→PQ navigation projections after the next enrichment cycle and continue expansion beyond the 474 canonical seed toward the 672 indexed-category target.


### 2026-09-27 continuation — Batch 500 current-evidence frontier
- [x] Performed a fresh post-Batch-499 census from the live 474-record corpus and selected 16 additional records without reusing the prior frontier candidate lists: **Gigantic Meteor, Super Saiyan 2, Supernova Cooler, Gigantic Omega, Brave Sword Attack, Super Vegeta, Blaster Ball, Perfect Kamehameha, Namek Finger, Blaster Meteor, Flash Strike, Paralyze Beam, Super Black Kamehameha Rosé, Finishing Blow, Bending Kamehameha, and Sudden Death Beam**.
- [x] Added 16 dated Batch 500 current-evidence audit artifacts and recorded `docs/data/skill-research-batches/skill-batch-500.json`.
- [x] Synchronized all 16 records into `docs/data/skills.json` and `docs/data/skills-index.json`; canonical identities were unchanged.
- [x] Validation manifest records **474 canonical / 474 index records**, **16 synchronized records**, and zero canonical identity changes or unsupported claims added.
- [x] Preserved source-bound numerical observations and explicit evidence boundaries; no unsupported exact frames, hidden interactions, universal scaling, or reward probabilities were promoted to canonical facts.
- [ ] Next priority: fresh **Batch 501** census from the live corpus, excluding all prior frontier candidates, followed by another larger mechanics/provenance enrichment cycle.
- [ ] After Batch 501, reconcile PQ→Skill and Skill→PQ projections and identify unresolved cross-domain endpoints rather than rewriting historical snapshots.
- [ ] Continue expansion beyond the 474 canonical seed toward the 672 indexed-category target; runtime/CI remains non-blocking.


### 2026-09-27 continuation — Batch 500 current-evidence frontier
- [x] Performed a fresh post-Batch-499 census from the live 474-record corpus; Batch 496–499 candidate lists were not reused as the selection basis.
- [x] Completed bounded current-evidence refreshes for **Orin Combo, Maiden Burst, Counter Burst, Super Kamehameha, Final Rampage, Revenge Death Ball, Super Afterimage, and Bluff Kamehameha**.
- [x] Added eight dedicated Batch 500 audit artifacts and finalized `docs/data/skill-research-batches/skill-batch-500.json`.
- [x] Synchronized all eight records into both canonical-facing Skills layers without changing canonical identities.
- [x] Maintained the restored **474/474** canonical/index baseline; evidence remains bounded and unsupported exact frames, hidden interactions, universal scaling, and reward probabilities were not promoted.
- [ ] Next priority: fresh Batch 501 census from the post-Batch-500 corpus, excluding prior frontier candidates, followed by current-evidence mechanics enrichment.
- [ ] Then reconcile PQ→Skill and Skill→PQ navigation projections and continue expansion toward the 672 indexed-category target.


### 2026-09-27 continuation — Batch 501 evidence frontier and numbering reconciliation
- [x] Preserved the existing Batch 500 manifest rather than overwriting it; it already contains a separate eight-record frontier.
- [x] Completed and synchronized a separate **Batch 501** eight-record current-evidence frontier: **Super Dragon Flight, Big Bang Kamehameha, Mach Punch, Gravity Impact, Sudden Storm, Change The Future, Stone Bullet, and Supernova Cooler**.
- [x] Corrected the eight live canonical-facing records from the provisional Batch 500 note label to Batch 501; no skill IDs, names, classifications, or acquisition endpoints were changed.
- [x] Added `docs/data/skill-research-batches/skill-batch-501.json` documenting the eight-record frontier and **474 canonical / 474 index** validation.
- [x] Preserved evidence boundaries and did not overwrite historical Batch 500 research.
- [ ] Next priority: fresh Batch 502 census from the live 474-record corpus, excluding prior frontier candidates, followed by bounded mechanics/provenance enrichment.
- [ ] Then reconcile PQ→Skill and Skill→PQ projections and continue expansion toward the 672 indexed-category target.


### 2026-09-27 continuation — Batch 500 current-evidence frontier
- [x] Performed a fresh post-Batch-499 census and selected eight records: Finish Breaker, Strike of Revelation, Force Shield, Super Donut Volley, Gorgeous Shot, Unrelenting Barrage, Hawk Charge, and Super Saiyan 2.
- [x] Added eight dedicated Batch 500 current-evidence audit artifacts and recorded docs/data/skill-research-batches/skill-batch-500.json.
- [x] Synchronized all eight records into both current Skills layers without canonical identity changes.
- [x] Git-blob validation confirms 474 canonical / 474 index records, unique IDs match, and ordered ID parity remains true.
- [x] Preserved bounded evidence and existing provenance conflicts; unsupported exact frames, hidden interactions, universal scaling, and reward probabilities were not promoted.
- [ ] Next priority: fresh Batch 501 census from the live 474-record corpus, excluding prior frontier candidates, then current-evidence/mechanics enrichment.
- [ ] After Batch 501, reconcile PQ→Skill and Skill→PQ projections and continue expansion toward the 672 indexed-category target.


### 2026-09-27 continuation — Batch 502 current-evidence frontier
- [x] Performed a fresh post-Batch-501 census from the live 474-record corpus, selecting eight records without reusing prior frontier candidates: **Freedom Kick, Ice Claw, Energy Dome, Force Edge, Fighting Pose H, Flash Bomber, Symphonic Destruction, and Burst Kamehameha**.
- [x] Added eight dedicated Batch 502 current-evidence audit artifacts and finalized `docs/data/skill-research-batches/skill-batch-502.json`.
- [x] Synchronized all eight records into both current Skills layers with no canonical identity changes.
- [x] Git-blob validation confirms **474 canonical / 474 index records**, unique-count parity intact.
- [x] Preserved bounded evidence and existing provenance conflicts; unsupported exact frames, hidden interactions, universal scaling, and reward probabilities were not promoted.
- [ ] Next priority: fresh Batch 503 census from the live 474-record corpus, excluding prior frontier candidates, then continue evidence/mechanics enrichment.
- [ ] After Batch 503, reconcile PQ→Skill and Skill→PQ navigation projections and continue expansion toward the 672 indexed-category target.


### 2026-09-27 continuation — Batch 503 current-evidence frontier
- [x] Performed a fresh post-Batch-502 census from the live 474-record corpus; prior frontier candidates were excluded from selection.
- [x] Completed bounded current-evidence refreshes for **Afterimage Strike, Big Bang Knuckle, Breaker Energy Wave, Brutal Buster, Chaotic Time Impact, Counter Impact, Crimson Edge, and Dancing Parapara**.
- [x] Added eight dedicated Batch 503 audit artifacts and finalized `docs/data/skill-research-batches/skill-batch-503.json`.
- [x] Synchronized all eight records into both current Skills layers with no canonical identity changes; Git-blob validation remains **474/474**.
- [x] Preserved evidence boundaries: unsupported exact frames, hidden interactions, universal scaling, and reward probabilities were not promoted to canonical facts.
- [ ] Next priority: fresh Batch 504 census from the live 474-record corpus, then reconcile PQ→Skill and Skill→PQ projections after the enrichment frontier.
- [ ] Continue expansion beyond the 474 canonical seed toward the 672 indexed-category target; runtime/CI remains non-blocking.


### 2026-09-27 continuation — Batch 500 finalized
- [x] Completed and finalized Batch 500 current-evidence frontier for **Gigantic Meteor, Gigantic Omega, Brave Sword Attack, Super Vegeta, Blaster Ball, Perfect Kamehameha, Namek Finger, and Warp Kamehameha**.
- [x] Added the missing Warp Kamehameha audit after detecting the initial seven-of-eight artifact write; no incomplete batch was left as the final state.
- [x] Synchronized all eight records into both current Skills layers without changing canonical identities.
- [x] Final Git-blob validation: **474 records / 474 unique IDs** in `skills.json` and **474 records / 474 unique IDs** in `skills-index.json`.
- [x] Batch 500 manifest finalized with 8 synchronized records, zero canonical identity changes, and zero unsupported claims promoted.
- [ ] Next priority: fresh **Batch 501** census from the live 474-record corpus, then continue evidence/mechanics enrichment and reconcile PQ→Skill / Skill→PQ projections.


### 2026-09-27 continuation — Batch 501 finalized
- [x] Completed a fresh post-Batch-500 frontier for **Super Saiyan Blue Kaioken, Giant Storm, Meditation, Fighting Pose I, Fighting Pose B, Fighting Pose J, Hell Flash, and Quick Sleep**; prior frontier candidates were excluded from selection.
- [x] Added eight dedicated Batch 501 current-evidence audit artifacts and finalized `docs/data/skill-research-batches/skill-batch-501.json`.
- [x] Synchronized all eight records into both `docs/data/skills.json` and `docs/data/skills-index.json`; canonical IDs/names were unchanged.
- [x] Preserved bounded evidence and existing provenance conflicts; unsupported exact frames, hidden interactions, universal scaling, and reward probabilities were not promoted.
- [x] Batch manifest validation remains **474 canonical / 474 index records**, 8 synchronized records, zero canonical identity changes, and evidence-boundary preservation.
- [ ] Next priority: fresh Batch 502 census from the live corpus, then reconcile PQ→Skill and Skill→PQ projections after the enrichment frontier.


### 2026-09-27 continuation — Batch 501 current-evidence frontier
- [x] Performed a fresh post-Batch-500 census from the live 474-record corpus; Batch 496–500 candidate names were excluded from selection.
- [x] Completed bounded current-evidence refreshes for **Fruit of the Tree of Might, Dead End Bullet, Super Saiyan, Super Saiyan God, Brave Heat, Fighting Pose D, Super Ghost Buu Attack, and Dead End Rain**.
- [x] Added eight dated Batch 501 evidence audit artifacts and finalized `docs/data/skill-research-batches/skill-batch-501.json`.
- [x] Synchronized all eight records into `docs/data/skills.json` and `docs/data/skills-index.json`; canonical identities were unchanged.
- [x] Preserved evidence boundaries: source-reported numerical observations remain source-bound; unsupported exact frames, hidden interactions, universal scaling, and reward probabilities were not invented.
- [x] Batch manifest records **474 canonical / 474 index records**, 8 synchronized records, zero canonical identity changes, and zero unsupported claims added.
- [ ] Next priority: fresh Batch 502 census, then continue mechanics/provenance enrichment.
- [ ] Reconcile PQ→Skill and Skill→PQ projections after the next enrichment cycle and continue expansion beyond the 474 canonical seed toward the 672 indexed-category target.


### 2026-09-27 continuation — Batch 502 current-evidence frontier
- [x] Performed a fresh post-Batch-501 census from the live 474-record corpus; selected **Super Saiyan God Super Saiyan, Fighting Pose C, Burning Attack, Final Kamehameha, God of Destruction's Wrath, Wolf Fang Fist, Ki Blast Thrust, and Punisher Guard** without reusing the prior frontier as the selection basis.
- [x] Added eight dedicated Batch 502 current-evidence audit artifacts and finalized the Batch 502 manifest/thin-frontier audit.
- [x] Synchronized all eight records into `docs/data/skills.json` and `docs/data/skills-index.json`; canonical IDs/names were unchanged.
- [x] Preserved source/provenance conflicts and evidence boundaries; unsupported exact frames, hidden interactions, universal scaling, and reward probabilities were not promoted.
- [x] Validation remains **474 canonical / 474 index records** with the restored identity baseline intact.
- [ ] Next priority: fresh **Batch 503** census from the live corpus, then reconcile PQ→Skill and Skill→PQ navigation projections after the enrichment frontier.
- [ ] Continue expansion beyond the 474 canonical seed toward the 672 indexed-category target.


### 2026-09-27 continuation — Batch 501 current-evidence frontier
- [x] Continued from the live 474-record corpus and refreshed eight records: Fighting Pose G, Weekend, Super Kamehameha (SS4 DAIMA), Kill Driver, Fake Death, Meteor Burst, Punisher Shield, and Mach Dash.
- [x] Synchronized all eight refreshes into both docs/data/skills.json and docs/data/skills-index.json; canonical identities were unchanged.
- [x] Preserved source-bounded numerical observations and unresolved frame/scaling/hidden-interaction fields; no synthetic canonical facts were introduced.
- [x] Git-blob validation confirms 474 records / 474 unique IDs in each live Skills layer.
- [ ] Next priority: fresh Batch 502 census from the post-Batch-501 corpus, excluding completed frontier candidates; then reconcile PQ→Skill and Skill→PQ projections and continue toward the 672 indexed-category target.


### 2026-09-27 continuation — Recovery baseline and Batch 504
- [x] Confirmed the restored canonical PQ reward database baseline is intact at 840 evidence-backed relationships; recovery validation now recomputes counts instead of trusting declared counts.
- [x] Confirmed PQ equipment endpoint enrichment is complete at 125 canonical edges / 123 unique targets / 123 exact endpoint matches / 0 identity gaps.
- [x] Completed Batch 504 current-evidence refresh for Afterimage, All Clear, Android Rush, Angry Explosion, Angry Hit, Apocalyptic Burst, Arm Crash, and Assault Rain from a fresh live 474-record census.
- [x] Synchronized all eight records into docs/data/skills.json and docs/data/skills-index.json; 474/474 identity parity remains intact.
- [x] Added Batch 504 manifest, thin-frontier audit, eight evidence audits, and cross-domain index registrations.
- [ ] Runtime/CI remains non-blocking.
- [ ] Next: fresh Batch 505 census, followed by PQ→Skill / Skill→PQ reconciliation and the next highest-value substantive cross-domain enrichment.

### 2026-09-27 continuation — Batch 505
- [x] Reconciled Skill→PQ reverse navigation at **474 canonical skills / 246 edges / 170 represented PQ IDs** with zero malformed duplicate/boolean PQ identifiers.
- [x] Preserved the 16-PQ unrepresented endpoint set as an evidence boundary; no unsupported Skill→PQ relationships were inferred.
- [x] Selected the next eight-record frontier: **Assault Vanish, Bloody Counter, Blue Hurricane, Body Change, Brave Sword Slash, Break Cannon, Burning Blast, Burning Slash**.
- [x] Added Batch 505 manifest and projection reconciliation audit.
- [ ] Complete bounded current-evidence enrichment for Batch 505, then continue cross-domain reconciliation and expansion beyond the 474 canonical seed toward the 672 indexed-category target.
- [ ] Runtime/CI remains non-blocking.

### 2026-09-27 continuation — Batch 505 current-evidence completion
- [x] Completed current-evidence refreshes for **Assault Vanish, Bloody Counter, Blue Hurricane, Body Change, Brave Sword Slash, Break Cannon, Burning Blast, Burning Slash**.
- [x] Synchronized canonical and index Skills layers with **0 identity changes**; 474/474 baseline remains intact.
- [x] Added all eight dated evidence audit artifacts and finalized Batch 505 manifest.
- [x] Preserved evidence boundaries and did not promote unsupported Skill→PQ relationships.
- [ ] Next: fresh Batch 506 census and next cross-domain enrichment; continue expansion beyond the 474 canonical seed toward the 672 indexed-category target.
- [ ] Runtime/CI remains non-blocking.

### 2026-09-27 continuation — Batch 506 current-evidence completion
- [x] Completed current-evidence refreshes for **Burning Swan, Burst Blitz, Burst Reflection, Burst Rush, Burst Stinger, Celestial Wave, Chain Destructo-Disc Barrage, and Chaos Shot**.
- [x] Canonical/index synchronization completed with **0 identity changes**.
- [x] Added eight audit artifacts, Batch 506 manifest, and cross-domain registrations.
- [x] Existing evidence conflicts and evidence boundaries were preserved; no unsupported Skill→PQ relationships were inferred.
- [ ] Next: fresh Batch 507 census and substantive cross-domain enrichment; continue expansion beyond the 474 canonical seed toward the 672 indexed-category target.
- [ ] Runtime/CI remains non-blocking.

### 2026-09-27 continuation — Batch 507 current-evidence completion
- [x] Completed current-evidence refreshes for **Candy Beam (Super), Charge, Circle Flash, Comet Strike, Confusion Blade, Crush Cannon, Crush Stream, and Crusher Ball**.
- [x] Canonical/index synchronization completed with **0 identity changes**; 474/474 baseline remains intact.
- [x] Added eight audit artifacts, Batch 507 manifest, and cross-domain registrations.
- [x] Preserved source-bounded evidence and did not infer unsupported Skill→PQ relationships.
- [ ] Next: fresh Batch 508 census and substantive cross-domain enrichment; continue expansion beyond the 474 canonical seed toward the 672 indexed-category target.
- [ ] Runtime/CI remains non-blocking.

### 2026-09-27 continuation — Batch 508 current-evidence completion
- [x] Refreshed **Burst Charge, Dark Inscription, Darkness Eye Beam, Darkness Rush (Melee), Darkness Rush (Ranged), Darkness Twin Star, Data Input, and Deadly Dance**.
- [x] Canonical Skills layer updated with **0 identity changes**; eight dated audit artifacts and Batch 508 manifest added.
- [ ] Complete index-layer synchronization after concurrent repository mutation; do not overwrite another writer's changes.
- [x] No unsupported Skill→PQ relationships or unsupported mechanics/probabilities were promoted.
- [ ] Next: reconcile index synchronization, then Batch 509 census and cross-domain enrichment toward the 672 indexed-category target.
- [ ] Runtime/CI remains non-blocking.

### 2026-09-27 continuation — Batch 506 additional frontier refresh
- [x] Added current-evidence refreshes for **Crusher Ball, Dark Inscription, Deadly Dance, Supreme Fury, Taunt, The Power to Overcome, Time Skip/Back Breaker**.
- [x] Preserved the pre-existing Batch 506 completed selection/history and extended the manifest rather than replacing it.
- [x] Canonical/index identity parity remains intact; no unsupported Skill→PQ edges were added.
- [ ] Next: fresh Batch 507 census and substantive cross-domain linkage/enrichment toward the 672 indexed-category target.
- [ ] Runtime/CI remains non-blocking.

### 2026-09-27 continuation — Batch 508 reconciliation and Batch 509 census
- [x] Completed the pending Batch 508 Skills-index synchronization; 474-record identity baseline remains intact.
- [x] Selected the next fresh frontier: **Death Ball, Death Beam, Death Crasher, Death Meteor, Death Psycho Bomb, Death Slash, Death Slicer, Death Wave**.
- [x] Added the Batch 509 frontier manifest.
- [ ] Complete Batch 509 evidence refreshes and then prioritize substantive cross-domain linkage toward the 672 indexed-category target.
- [ ] Runtime/CI remains non-blocking.

### 2026-09-27 continuation — Batch 509 completion
- [x] Refreshed **Death Ball, Death Beam, Death Crasher, Death Meteor, Death Psycho Bomb, Death Slash, Death Slicer, Death Wave** with current bounded evidence.
- [x] Canonical/index Skills synchronization completed with **0 identity changes**; 474/474 remains intact.
- [x] Added eight Batch 509 audit artifacts and finalized the manifest.
- [ ] Next: fresh Batch 510 census and cross-domain enrichment; continue expansion beyond the 474 canonical seed toward 672 indexed categories.
- [ ] Runtime/CI remains non-blocking.

### 2026-09-27 continuation — Batch 510 completion
- [x] Refreshed **Demon Flash Strike, Demon Flurry, Demon Ray, Demonic Destruction, Destruction's Concerto: Comet, Destruction's Concerto: Meteor, Destruction's Concerto: Starfall, Destruction's Conductor**.
- [x] Canonical/index synchronization completed with **0 identity changes**; 474/474 baseline preserved.
- [x] Added eight dated audit artifacts and finalized Batch 510 manifest.
- [x] Preserved evidence boundaries and added no unsupported Skill→PQ relationships.
- [ ] Next: fresh Batch 511 census and substantive cross-domain enrichment toward the 672 indexed-category target.
- [ ] Runtime/CI remains non-blocking.

### 2026-09-27 continuation — Batch 506 frontier census
- [x] Fresh census completed from the post-Batch-505 474-record corpus.
- [x] Selected **Burning Swan, Burst Blitz, Burst Charge, Burst Reflection, Burst Rush, Burst Stinger, Candy Beam (Super), Celestial Wave**.
- [x] Batch 506 manifest registered; canonical data remains the source of truth.
- [ ] Complete Batch 506 current-evidence refresh and cross-domain synchronization.
- [ ] Continue expansion beyond the 474 canonical seed toward the 672 indexed-category target.
- [ ] Runtime/CI remains non-blocking.

### 2026-09-27 continuation — Batch 506 current-evidence completion
- [x] Refreshed Burning Swan, Burst Blitz, Burst Charge, Burst Reflection, Burst Rush, Burst Stinger, Candy Beam (Super), and Celestial Wave.
- [x] Canonical/index synchronization completed with 0 identity changes; 474/474 baseline intact.
- [x] Added eight Batch 506 evidence audits and completed the frontier manifest.
- [x] Existing reward/source conflicts remain explicitly bounded.
- [ ] Next: Batch 507 census and cross-domain enrichment toward the 672 indexed-category target.

### 2026-09-27 continuation — Batch 506 census correction
- [x] Corrected the Batch 506 frontier after live-date validation removed four records that already had 2026-09-26 current-evidence audits.
- [x] Corrected frontier: **Burst Charge, Burst Reflection, Burst Stinger, Celestial Wave, Chain Destructo-Disc Barrage, Confusion Blade, Dark Inscription, Deadly Dance**.
- [ ] Complete the corrected Batch 506 current-evidence refresh and register its artifacts.

### 2026-09-27 continuation — Batch 506 completion
- [x] Refreshed eight frontier records: Burning Swan, Burst Blitz, Burst Charge, Burst Reflection, Burst Rush, Burst Stinger, Candy Beam (Super), Celestial Wave.
- [x] Canonical/index identity parity preserved at 474/474; eight audit artifacts registered.
- [x] Reward-tier/source conflicts and evidence boundaries preserved.
- [ ] Next: Batch 507 census plus cross-domain enrichment toward the 672 indexed-category target.


### 2026-09-27 continuation — Batch 507 live-state reconciliation
- [x] Verified Batch 507 completion against the live canonical layer: eight selected records now carry `last_verified: 2026-09-27`.
- [x] Batch 507 selected **Candy Beam (Super), Charge, Circle Flash, Comet Strike, Confusion Blade, Crush Cannon, Crush Stream, Crusher Ball** and preserved 474/474 identity parity.
- [x] Existing evidence boundaries and source conflicts remain preserved.
- [ ] Next: Batch 508 census and current-evidence enrichment, followed by cross-domain reconciliation.


### 2026-09-27 continuation — Batch 508 reconciliation
- [x] Batch 508 refreshed eight records and preserved 474/474 identity parity.
- [x] Completed the pending Skills index synchronization after concurrent mutation reconciliation.
- [x] Finalized the Batch 508 manifest; no unsupported Skill→PQ relationships or unsupported numeric claims were promoted.
- [ ] Next: Batch 509 fresh census and cross-domain enrichment toward the 672 indexed-category target.


### 2026-09-27 continuation — Batch 506 completion
- [x] Completed the corrected eight-record Batch 506 current-evidence frontier: **Burst Charge, Burst Reflection, Burst Stinger, Celestial Wave, Chain Destructo-Disc Barrage, Confusion Blade, Dark Inscription, Deadly Dance**.
- [x] Canonical/index Skills synchronization completed with **0 identity changes**; 474/474 baseline intact.
- [x] Batch 506 manifest finalized; existing source and reward-tier conflicts remain explicitly bounded.
- [ ] Next: fresh Batch 507 census followed by cross-domain projection reconciliation and continued expansion beyond the canonical 474 records toward the 672 indexed-category target.
- [ ] Runtime/CI remains non-blocking.

### 2026-09-27 continuation — Batch 506 completion
- [x] Completed current-evidence enrichment for the eight Batch 506 frontier records.
- [x] Preserved reward-tier/source conflicts and did not infer unsupported probabilities or Skill→PQ edges.
- [x] Batch 506 manifest finalized; 474/474 canonical/index identity baseline preserved.
- [ ] Next: Batch 507 fresh census plus cross-domain enrichment toward 672 indexed categories.


### 2026-09-27 continuation — Batch 506 completion
- [x] Batch 506 current-evidence refresh completed for eight frontier skills.
- [x] Canonical/index synchronization completed with 0 identity changes; 474/474 baseline retained.
- [x] Eight evidence audits registered; reward-tier conflicts remain explicitly preserved.
- [ ] Next: Batch 507 census and cross-domain enrichment toward the 672 indexed-category target.


### 2026-09-27 continuation — Batch 506 completion
- [x] Completed Batch 506 current-evidence refresh for **Burning Swan, Burst Blitz, Burst Charge, Burst Reflection, Burst Rush, Burst Stinger, Candy Beam (Super), and Celestial Wave**.
- [x] Preserved existing enriched canonical conclusions and unresolved reward-tier/trigger conflicts; no unsupported probabilities, frame data, hidden interactions, or scaling were promoted.
- [x] Batch 506 manifest finalized and dated audit artifacts are present for all eight selected records.
- [x] Canonical identity changes: **0**; recovered Skills baseline remains 474 records.
- [ ] Next exact: fresh Batch 507 census, then substantive cross-domain reconciliation toward the 672 indexed-category target.
- [ ] Runtime/CI remains non-blocking.

### 2026-09-27 continuation — Batch 506 completion
- [x] Completed current-evidence refreshes for Burning Swan, Burst Blitz, Burst Charge, Burst Reflection, Burst Rush, Burst Stinger, Candy Beam (Super), and Celestial Wave.
- [x] Preserved acquisition/reward conflicts and evidence boundaries; no unsupported probabilities, frame data, hidden interactions, or Skill→PQ edges were added.
- [x] Skills canonical/index identity parity remains 474/474.
- [ ] Next: fresh Batch 507 census and cross-domain enrichment toward the 672 indexed-category target.
- [ ] Runtime/CI remains non-blocking.

### 2026-09-27 continuation — Batch 506 completion
- [x] Refreshed **Burning Swan, Burst Blitz, Burst Charge, Burst Reflection, Burst Rush, Burst Stinger, Candy Beam (Super), Celestial Wave**.
- [x] Canonical/index Skills synchronization completed with **0 identity changes**; canonical baseline remains 474.
- [x] Added eight dated evidence audits and finalized Batch 506 manifest.
- [x] Preserved unresolved reward-tier/acquisition conflicts and evidence boundaries.
- [ ] Next: fresh Batch 507 census and substantive cross-domain enrichment toward the 672 indexed-category target.
- [ ] Runtime/CI remains non-blocking.

### 2026-09-27 continuation — Batch 506 completion
- [x] Refreshed **Burning Swan, Burst Blitz, Burst Charge, Burst Reflection, Burst Rush, Burst Stinger, Candy Beam (Super), Celestial Wave**.
- [x] Canonical/index Skills baseline remains **474/474**, with zero canonical identity changes.
- [x] Preserved documented reward-tier and provenance conflicts rather than inferring unsupported gates or probabilities.
- [ ] Next: fresh Batch 507 census and next substantive cross-domain enrichment toward the 672 indexed-category target.
- [ ] Runtime/CI remains non-blocking.

### 2026-09-27 continuation — Batch 506 current-evidence refresh
- [x] Refreshed eight frontier records: Burning Swan, Burst Blitz, Burst Charge, Burst Reflection, Burst Rush, Burst Stinger, Candy Beam (Super), Celestial Wave.
- [x] Canonical/index synchronization completed with 0 identity changes and 474/474 baseline intact.
- [x] Evidence conflicts and canonical-source rules preserved.
- [ ] Complete remaining Batch 506 audit-file registrations and cross-domain reconciliation.
- [ ] Continue toward the 672 indexed-category target; runtime/CI remains non-blocking.

### 2026-09-27 continuation — Batch 507 Skill↔PQ reconciliation
- [x] Reconciled canonical Skill `source_parallel_quests` with the PQ reward forward layer: 246 Skill→PQ edges / 170 represented PQ IDs.
- [x] Normalized four presentation aliases and promoted 14 canonical-supported missing endpoints.
- [x] Removed the conflicting Kamehameha→PQ48 forward edge; canonical record supports PQ5.
- [x] PQ forward relationship layer now totals 848 evidence-backed relationships, with 246 skill relationships.
- [x] Updated projection reconciliation documentation.
- [ ] Next: fresh Batch 507 census and next substantive cross-domain enrichment; preserve canonical-source priority and unresolved evidence boundaries.
- [ ] Runtime/CI remains non-blocking.

### 2026-09-27 continuation — Batch 506 current-evidence completion
- [x] Refreshed eight frontier records: Burning Swan, Burst Blitz, Burst Charge, Burst Reflection, Burst Rush, Burst Stinger, Candy Beam (Super), Celestial Wave.
- [x] Canonical Skills layer refreshed with zero identity changes.
- [x] Evidence boundaries and unresolved acquisition conflicts preserved.
- [x] Batch 506 manifest finalized.
- [ ] Register eight audit artifacts and synchronize `skills-index.json`.
- [ ] Continue cross-domain reconciliation and expansion beyond the 474 canonical seed toward the 672 indexed-category target.

### 2026-09-27 continuation — Batch 511 current-evidence completion
- [x] Fresh post-Batch-510 census from the live 474-record canonical corpus selected **Destructive Fission, Destructive Flare, Destructive Fracture, Destructo-Disc, DIE DIE Missile Barrage, Dimension Cannon, Dimension Ray, Dimensional Hole**.
- [x] Completed bounded current-evidence refreshes for all eight; canonical identity changes: **0**.
- [x] Synchronized docs/data/skills.json and docs/data/skills-index.json; added eight dated Batch 511 audit artifacts and finalized docs/data/skill-research-batches/skill-batch-511.json.
- [x] Registered Batch 511 and all eight audit artifacts in docs/data/pq-cross-domain-index.json.
- [x] Preserved canonical-source priority and did not infer unsupported Skill→PQ relationships, reward probabilities, hidden gates, exact frames, or patch-independent scaling.
- [ ] Runtime/CI remains non-blocking.
- [ ] **Exact next:** fresh Batch 512 census and next substantive cross-domain enrichment toward the 672 indexed-category target.

### 2026-09-27 continuation — Batch 512 current-evidence + PQ projection reconciliation
- [x] Fresh post-Batch-511 census selected **Divine Kamehameha, Divine Lasso, Divine Ray Bomb, Divine Spear, Divine Wrath: Purification, Divinity Unleashed, Do or Die, Dodon Ray** from the 474-record canonical corpus.
- [x] Completed bounded current-evidence refreshes for all eight; canonical identity changes: **0**.
- [x] Synchronized `docs/data/skills.json` and `docs/data/skills-index.json`; added eight Batch 512 evidence audits and finalized `docs/data/skill-research-batches/skill-batch-512.json`.
- [x] Reconciled live Skill→PQ projection metadata: **246 canonical edges = 246 forward Skill reward edges; 0 missing endpoints; 170 represented PQ IDs**.
- [x] Corrected stale consumer-audit metadata that still reported 236 links; aliases remain 4 and unresolved links remain 0.
- [x] Registered Batch 512 and the refreshed consumer reconciliation audit in `docs/data/pq-cross-domain-index.json`.
- [x] Preserved canonical-source priority and evidence boundaries; no unsupported Skill→PQ edges, probabilities, hidden gates, exact frames, or patch-independent scaling were inferred.
- [ ] Runtime/CI remains non-blocking.
- [ ] **Exact next:** fresh Batch 513 census, then continue expanding/reconciling PQ↔Skill↔other-domain navigation toward the 672 indexed-category target.


### 2026-09-27 continuation — Batch 513
- [x] Fresh lexical frontier census selected **Dodoria Beam, Dodoria Headbutt, Dodoria Launcher, Double Crush, Double Death Slicer, Double Sunday, Dragon Blitz, Dragon Burn**.
- [x] Refreshed all eight with current bounded evidence; canonical identity changes remain **0**.
- [x] Corrected **Double Death Slicer** from **Super / 100 Ki** to **Ultimate / 300 Ki** based on current Xenoverse 2-specific evidence.
- [x] Added eight evidence audits, finalized the Batch 513 manifest, and registered the artifacts in `docs/data/pq-cross-domain-index.json`.
- [x] Skill→PQ projection remains **246 canonical edges / 246 forward edges / 0 missing endpoints / 170 represented PQ IDs**; no new edge was inferred.
- [ ] Runtime/CI remains non-blocking.
- [ ] **Next:** fresh Batch 514 census and the next substantive cross-domain enrichment cycle.


### 2026-09-27 continuation — Canonical skills regression recovery + Batch 514
- [x] Detected a live canonical-skills regression: docs/data/skills.json had reverted to blob 89e78acb10b69caaf911799e624435314e68ece7, which lacked the completed Batch 496–513 canonical evidence history.
- [x] Recovered the canonical Skills database from the surviving Batch 513 canonical blob 8cacd72ea4f1d02db2e2366c304f3efe3b03678d rather than reconstructing canonical data from the projection/index layer.
- [x] Restored the full 474-record canonical Skills baseline and preserved the completed Batch 511–513 corrections/evidence, including the Double Death Slicer correction and the 2026-09-27 refresh history.
- [x] Re-synchronized docs/data/skills-index.json; both canonical and index layers contain 474 records and Batch 514 identity parity is intact.
- [x] Completed fresh Batch 514 current-evidence refreshes for Dragon Fist, Dragon Spark, Dragon Spiral, Dragon Thunder, Drain Field, Dual Destructo-Disc, Dust Attack, and Dynamite Kick with zero identity changes and no unsupported Skill→PQ relationships.
- [x] Added eight Batch 514 evidence audits, the Batch 514 manifest, and cross-domain index registrations.
- [x] Added docs/data/canonical-database-recovery-restoration-audit-2026-09-27.json documenting the regression and source-preserving restoration.
- [ ] Runtime/CI remains intentionally non-blocking and unverified.
- [ ] Exact next: fresh Batch 515 census from the restored 474-record canonical corpus; continue evidence-backed cross-domain enrichment and repair any newly detected canonical/projection drift before expanding the database further.


### 2026-09-27 continuation — Batch 515 canonical evidence refresh
- [x] Completed Batch 515 against the restored 474-record canonical corpus: refreshed 16 skills from Eagle Kick through Energy Shot.
- [x] Synchronized canonical `docs/data/skills.json` and `docs/data/skills-index.json`; both remain at 474 records.
- [x] Added `docs/data/skill-research-batches/skill-batch-515.json` and registered it in `docs/data/pq-cross-domain-index.json`.
- [x] No Skill identity changes, canonical field corrections, or new Skill→PQ relationship inferences were made in Batch 515.
- [x] Current evidence strengthened bounded mechanics/provenance for Eagle Kick, Earth Splitting Galick Gun, Elegant Blaster, Elite Beam, Elite Shooting, Emperor's Blast, Emperor's Cannon, Emperor's Death Beam, Emperor's Edge, Endless Shoot, Energy Barrier, Energy Charge, Energy Field, Energy Minefield, Energy Release, and Energy Shot.
- [x] Post-batch validation: canonical/index counts remain 474/474. The only remaining last_verified mismatches are the three pre-existing records Phantom Fist, Rise to Action, and Rising Rage; these were not normalized without resolving their provenance.
- [ ] 247 canonical skill records remain older than 2026-09-27.
- [ ] Exact next: Batch 516 starting at Eraser Bomb, Evil Blast, Evil Explosion, Evil Eyes, Evil Flame, Evil Flight Strike, Evil Ray Strike, Evil Rise Strike, Evil Whirlwind, Excellent Full Course, Explosive Assault, and Explosive Buu Buu Punch; continue in larger evidence-backed batches and resolve canonical/index drift separately.


### 2026-09-27 continuation — Batch 516 canonical evidence refresh
- [x] Completed Batch 516: refreshed 12 skills from Eraser Bomb through Explosive Buu Buu Punch against current Xenoverse 2 evidence.
- [x] Synchronized docs/data/skills.json and docs/data/skills-index.json; both remain at 474 records.
- [x] Added docs/data/skill-research-batches/skill-batch-516.json and registered it in docs/data/pq-cross-domain-index.json.
- [x] Batch 516 made zero skill identity changes, zero canonical field corrections, and zero new Skill→PQ relationship inferences.
- [x] Preserved existing acquisition/reward conflicts and unresolved frame, scaling, hidden-condition, and probability fields rather than normalizing them without evidence.
- [x] Post-batch validation: canonical/index counts are 474/474; the same three pre-existing last_verified mismatches remain isolated (Phantom Fist, Rise to Action, Rising Rage).
- [ ] 235 canonical skill records remain older than 2026-09-27.
- [ ] Exact next: Batch 517 beginning with Explosive Wave, Eye Beam, Fake Blast, Feint Shot, Fierce Fist, Fighting Pose E, Fighting Pose K, Final Cannon, Final Charge, and Final Explosion.

## 2026-09-27 — Batch 516 completed
- [x] Batch 516 current-evidence refresh: 12 Skill records from Eraser Bomb through Explosive Buu Buu Punch.
- [x] Canonical/index parity maintained; no identity or relationship changes.
- [ ] Continue stale canonical Skill frontier: 235 records remain, starting Explosive Wave → Eye Beam → Fake Blast → Feint Shot → Fierce Fist → Fighting Pose E → Fighting Pose K → Final Cannon.
- [ ] Resolve the three pre-existing canonical/index date mismatches only with provenance support.

### 2026-09-27 — Batch 517
- [x] Refreshed 10 skills: Explosive Wave; Eye Beam; Fake Blast; Feint Shot; Fierce Fist; Fighting Pose E; Fighting Pose K; Final Cannon; Final Charge; Final Explosion.
- [x] Canonical and index layers remain 474/474.
- [x] Batch manifest added and cross-domain index registered.
- [x] No identity, canonical-field, or Skill→PQ relationship changes.
- [ ] 225 canonical skill records remain older than 2026-09-27.
- [ ] Next: Batch 518 starts at Final Flash and continues alphabetically.


## 2026-09-27 — Batch 518 completed
- [x] Batch 518 current-evidence refresh: 12 Skill records from Final Flash through Galick Gun.
- [x] Canonical and index layers remain 474/474.
- [x] Batch manifest added and cross-domain index registered.
- [x] No identity, canonical-field, or Skill→PQ relationship changes.
- [ ] Resolve the three pre-existing canonical/index date mismatches only with provenance support.
- [ ] Continue stale canonical Skill frontier alphabetically after Galick Gun.


- [x] Batch 516 — refresh next 12 stale canonical Skills records (Eraser Bomb, Evil Blast, Evil Explosion, Evil Eyes, Evil Flame, Evil Flight Strike, Evil Ray Strike, Evil Rise Strike, Evil Whirlwind, Excellent Full Course, Explosive Assault, Explosive Buu Buu Punch); synchronize skills index; register cross-domain batch.
- [ ] Continue stale Skills frontier: Explosive Wave → Eye Beam → Fake Blast → Feint Shot → Fierce Fist → Fighting Pose E → Fighting Pose K → Final Cannon → Final Charge → Final Explosion → Final Flash → Final Flash (SS3 DAIMA) → continue alphabetically.

### 2026-09-27 continuation — Batch 519 canonical evidence refresh
- [x] Batch 519 refreshed 12 stale canonical Skill records from Gamma Blaster through Gigantic Roar.
- [x] Canonical/index parity remains 474/474; no identity or Skill→PQ relationship changes.
- [x] Added and registered the Batch 519 research manifest.
- [x] Preserved existing acquisition/reward conflicts and unresolved frame, hidden-condition, probability, and patch-independent-scaling fields.
- [ ] 201 canonical Skill records remain older than 2026-09-27.
- [ ] Continue stale Skill frontier: God Breaker → God of Destruction's Anger → God of Destruction's Menace → God of Destruction's Might → God of Destruction's Plaything → God of Destruction's Poise → God of Destruction's Rampage → God of Destruction's Roar → continue alphabetically.


### 2026-09-27 continuation — Skill evidence Batch 520
- [x] Refreshed 16 canonical skill records: God Breaker; God of Destruction's Anger; God of Destruction's Menace; God of Destruction's Might; God of Destruction's Plaything; God of Destruction's Poise; God of Destruction's Rampage; God of Destruction's Roar; God Punisher; Godly Chronos Cannon; Godly Display; Grand Smasher; Handy Canon; Headshot; Heat Dome Attack; Heat Wave.
- [x] Synchronized the 16 corresponding skills-index projections.
- [x] Added docs/data/skill-research-batches/skill-batch-520.json and registered it in docs/data/pq-cross-domain-index.json.
- [x] Preserved canonical acquisition/reward conflicts and did not infer unsupported probabilities, hidden gates, exact frames, or patch-independent scaling.
- [x] Canonical skill identity/relationship fields were unchanged; this cycle was evidence enrichment only.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] Exact next: continue from the stale frontier after Batch 520; re-fetch live SHAs before mutation.


### 2026-09-27 — Batch 521
- [x] Refreshed 16 stale canonical Skills records: Heavenly Arrow; Hellzone Grenade; Hero's Flute; Hero's Pose; Heroic Assault; Heroic Counter; Holy Inscription; Holy Wrath; Hyper Drain; Hyper Movement; Hyper Tornado; Ill Bomber; Ill Rain; Impact Flare; Impulse Slash; Indomitable.
- [x] Canonical/index parity maintained at 474 records; no identity, canonical-field, or Skill→PQ relationship changes.
- [x] Batch manifest added and cross-domain index registered.
- [ ] Continue stale Skill frontier alphabetically after Indomitable.
- [ ] Resolve the three pre-existing canonical/index last_verified mismatches only with provenance support.


### 2026-09-27 — Batch 522
- [x] Refreshed 20 stale canonical Skills records: Innocence Breath; Innocence Bullet; Innocence Cannon; Instant Charge; Instant Rise; Instant Severance; Instant Transmission; Jumping Energy Wave; Justice Blade; Justice Combination; Justice Drive; Justice Kick; Justice Pose; Justice Rush; Kai Kai; Kaioken; Kaioken Kamehameha; Kairos Cannon; Kamehameha; Ki Explosion.
- [x] Canonical/index parity maintained at 474 records; no identity, canonical-field, or Skill→PQ relationship changes.
- [x] Batch manifest added and cross-domain index registered.
- [ ] Continue stale Skill frontier alphabetically after Ki Explosion.
- [ ] Resolve the three pre-existing canonical/index last_verified mismatches only with provenance support.


### 2026-09-27 continuation — Skill evidence Batch 523
- [x] Refreshed 16 canonical skill records: Last Emperor; Light Grenade; Lightning Impact; Lightning of Absolution; Lovely Cyclone; Maiden Blast; Masenko; Maximum Charge; Meteor Blow; Meteor Crash; Meteor Explosion; Meteor Strike; Mighty Explosive Wave; Milky Cannon; Murder Grenade; Mystic Flash.
- [x] Synchronized the 16 corresponding skills-index projections.
- [x] Added docs/data/skill-research-batches/skill-batch-523.json and registered it in docs/data/pq-cross-domain-index.json.
- [x] Batch 523 made zero skill identity changes, zero canonical field corrections, and zero new Skill→PQ relationship inferences.
- [x] Preserved unresolved reward probabilities, exact frames, hidden conditions, disputed acquisition semantics, and patch-independent scaling rather than inferring them.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] Exact next: continue the stale canonical Skill frontier after Mystic Flash; re-fetch live SHAs before mutation.


### 2026-09-27 continuation — Skill evidence Batch 524
- [x] Refreshed 16 stale canonical skill records: Neo Tri-Beam; Neo Wolf Fang Fist; One-Handed Kamehameha mk.II; Pendulum Bullet; Perfect Shot; Petrifying Spit; Phantom Fist; Photon Swipe; Potential Unleashed; Power Blitz; Power Impact; Power Pole Combo; Power Pole Pro; Power Rush; Power Wall; Powered Shell.
- [x] Synchronized the corresponding skills-index projections; canonical/index record counts remain 474/474.
- [x] Added docs/data/skill-research-batches/skill-batch-524.json and registered it in docs/data/pq-cross-domain-index.json.
- [x] Batch 524 made zero skill identity changes, zero canonical field corrections, and zero new Skill→PQ relationship inferences.
- [x] Preserved unresolved reward probabilities, exact frames, hidden conditions, disputed acquisition semantics, and patch-independent scaling rather than inferring them.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] Exact next: continue the stale canonical Skill frontier after Powered Shell; re-fetch live SHAs before every mutation.


### 2026-09-27 continuation — Skill evidence Batch 525
- [x] Refreshed 16 stale canonical skill records: Prelude to Destruction; Prepare to be Punished; Present For You; Pressure Sign; Pretty Cannon; Pretty Charge; Prominence Flash; Psychic Move; Psycho Barrier; Psycho Escape; Punisher Guard; Punisher Shield; Pure Progress; Purification; Quick Sleep; Raid Blast.
- [x] Synchronized the 16 corresponding skills-index projections; canonical/index record counts remain 474/474.
- [x] Added docs/data/skill-research-batches/skill-batch-525.json and registered it in docs/data/pq-cross-domain-index.json.
- [x] Batch 525 made zero skill identity changes, zero canonical field corrections, and zero new Skill→PQ relationship inferences.
- [x] Preserved unresolved reward probabilities, exact frames, hidden conditions, disputed acquisition semantics, and patch-independent scaling rather than inferring them.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] Exact next: continue the stale canonical Skill frontier after Raid Blast; re-fetch live SHAs before every mutation.


### 2026-09-27 continuation — Recovery baseline correction / current frontier
- [x] Verified the live recovery baseline: 474 canonical skills, 474 skill-index records, 474 canonical Skill→PQ reverse records, 246 Skill→PQ edges, 170 represented PQs, and 840 canonical PQ reward relationships (236 skill / 137 Super Soul / 125 equipment / 247 character / 88 DLC / 7 farming).
- [x] Verified the current PQ equipment projection has 123 unique canonical targets and 123 endpoint identity matches with 0 gaps. Earlier notes reporting 72 remaining endpoint identity gaps are superseded by the later live reconciliation and must not be treated as outstanding work.
- [x] Verified Super Soul PQ acquisition parity: 137 canonical PQ→Super Soul edges, 134 unique targets, 134 acquisition-index targets, and 168 canonical Super Soul records.
- [x] Recovery remains source-bounded; no relationship or mechanic claims are to be reconstructed from secondary indexes when canonical source data survives.
- [ ] Runtime/CI remains intentionally non-blocking/unverified.
- [ ] **Current frontier:** substantive Super Soul mechanics enrichment and remaining cross-domain coverage gaps. The latest Super Soul mechanics audit reports 172 records in the mechanics layer, with 80 records still carrying partial mechanics coverage; missing fields remain unresolved rather than inferred.


### 2026-09-27 continuation — Super Soul mechanics audit correction
- [x] Corrected the Super Soul mechanics audit arithmetic: canonical layer has 172 records, therefore missing `limit_burst_trigger` count is 172.
- [x] Confirmed PQ 186 canonical reward relationships for both late Super Souls remain intact; independent PQ guide evidence also lists both rewards. No effect mechanics were inferred for the unresolved record.
- [ ] Continue evidence-backed Super Soul mechanics enrichment; do not fill missing mechanics solely to improve coverage counts.


### 2026-09-27 continuation — Active Super Soul coverage reconciliation
- [x] Corrected Super Soul mechanics coverage auditing so five explicitly rejected legacy/misidentified records are excluded from active counts while remaining preserved historically.
- [x] Active mechanics layer is now 167 records out of 172 historical records; coverage was recomputed without changing canonical gameplay data.
- [ ] Continue mechanics enrichment against active records; never restore rejected identities without new direct provenance evidence.


### 2026-09-27 continuation — Super Soul 035 Limit Burst enrichment
- [x] Added secondary evidence-backed `Auto Just Guard` Limit Burst data to Super Soul 035 and classified it as verified-secondary.
- [x] Active Limit Burst-effect coverage increased from 163/167 to **164/167**.
- [ ] Continue remaining active Super Soul mechanics gaps; do not promote secondary evidence to primary canonical truth without provenance support.
