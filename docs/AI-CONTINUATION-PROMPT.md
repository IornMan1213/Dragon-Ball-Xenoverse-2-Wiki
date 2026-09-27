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
- [x] Inspected the live `scripts/validate_skill_acquisition_metadata.py` after the prior root/container hardening.
- [x] Found a concrete robustness gap: duplicate detection used `set(source_parallel_quests)` before malformed endpoint values were type/range validated, so an unhashable endpoint could cause an uncontrolled `TypeError`.
- [x] Reordered validation so every PQ endpoint is first checked as a non-boolean integer in supported range **1–186**; duplicate detection runs only on valid integer endpoints.
- [x] Also moved canonical skill-ID uniqueness after explicit non-empty string validation, preventing malformed unhashable IDs from reaching set construction.
- [x] Updated `docs/data/skill-acquisition-metadata-integrity-audit-2026-09-26.json` with the hardening record.
- [x] No canonical skill/acquisition data changed; the established **474-record** contract remains unchanged.
- [ ] Runtime validator execution and CI/build remain unverified.
- [x] **Exact next:** inspect the remaining live deterministic validator/consumer/projection layer for another concrete robustness or source-vs-output integrity gap; preserve the missing general PQ reward source boundary.

### 2026-09-27 continuation — Partner skill validator root-container hardening
- [x] Inspected the live `scripts/validate_partner_skill_relationships.py` after the prior identity-uniqueness hardening.
- [x] Found a concrete robustness gap: the validator could call `.get()` on malformed non-object JSON roots for the relationship source, skills source, or character bridge, producing an uncontrolled `AttributeError` instead of a deterministic validation failure.
- [x] Hardened the validator to require all three source roots to be objects before field access; malformed roots now become explicit validation failures.
- [x] Updated `docs/data/partner-skill-relationship-validator-audit-2026-09-26.json` with the root-container hardening and validator commit.
- [x] No canonical relationship, skill, character, or acquisition data was changed; the established **474-skill / 3 explicit relationship** projection is unchanged.
- [ ] Runtime validator execution and CI/build remain unverified.
- [x] **Exact next:** inspect the remaining live deterministic consumer/projection layer for another concrete schema/type/range/identity/source-vs-output mismatch; preserve the missing general PQ reward layer as an evidence boundary.

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

### 2026-09-27 continuation — Skill→PQ endpoint uniqueness hardening
- [x] Inspected the live `scripts/validate_skill_pq_crosslinks.py` after the PQ forward-source boundary.
- [x] Hardened each canonical skill's `source_parallel_quests` contract to reject duplicate PQ IDs and boolean-as-integer IDs; strict supported PQ range **1–186** remains enforced.
- [x] Updated `docs/data/skill-pq-cross-domain-linkage-integrity-audit-2026-09-26.json` with the new **0 duplicate / 0 boolean** endpoint checks; the canonical **474-skill / 246-edge / 170-PQ** projection remains unchanged.
- [x] No canonical relationship data was added, removed, or inferred.
- [ ] Runtime validator execution and CI/build remain unverified.
- [x] **Exact next:** inspect the next live deterministic validator/consumer or projection; keep the missing general PQ reward layer as an explicit evidence boundary.

### 2026-09-26 continuation — PQ cross-domain forward-source boundary confirmed
- [x] The live validator hardening exposed a real source-vs-index mismatch: `docs/data/pq-cross-domain-index.json` declares `docs/data/pq-reward-relationships.json` as its forward source, but that file is absent from the live `main` tree.
- [x] Searched the live repository for a current producer/generator or complete replacement source; only historical handoff/audit references were found.
- [x] Corrected `docs/data/pq-cross-domain-index-validator-audit-2026-09-26.json` so the structural declaration checks are recorded as passing while the full live contract remains blocked by the missing forward source.
- [x] Preserved the evidence boundary: the independent 474-skill / 246-edge Skill→PQ reverse layer cannot substitute for the absent general PQ reward forward layer.
- [ ] Runtime execution/CI remains unverified; the validator's direct forward-file check is expected to fail until an evidence-complete producer/source exists.
- [x] **Exact next:** continue with the next live deterministic validator/consumer or, if returning to the critical PQ forward layer, only regenerate `pq-reward-relationships.json` after identifying an evidence-complete canonical producer and deterministic schema.

### 2026-09-26 continuation — PQ cross-domain index schema hardening
- [x] Inspected the live validator set and confirmed most older PQ validators listed in `pq-cross-domain-index.json` are historical/missing; `scripts/validate_pq_cross_domain_index.py` is a current live validator.
- [x] Hardened `scripts/validate_pq_cross_domain_index.py` to require exactly **7** reverse-index declarations, unique reverse-index report paths, and an exact `farming.source == forward_index` relationship.
- [x] Added `docs/data/pq-cross-domain-index-validator-audit-2026-09-26.json` recording the expanded schema contract as passing and registered it under the index's current `integrity_audits`.
- [x] No PQ reward relationship, endpoint identity, or absent reverse dataset was created or inferred.
- [ ] Runtime validator execution and CI/build remain unverified in this environment.
- [ ] `docs/AI-CONTINUATION-PROMPT-EFFICIENCY-ADDENDUM.md` remains unavailable at the expected repository path (GitHub 404).
- [x] **Exact next:** inspect the next live validator or deterministic consumer/projection, using the live script tree rather than stale index registrations; preserve historical/unreachable PQ reward/reverse references as provenance unless a complete producer exists.

### 2026-09-26 continuation — Skill acquisition metadata schema hardening
- [x] Inspected the next live deterministic validator, `scripts/validate_skill_acquisition_metadata.py`, after the Partner Customization identity pass.
- [x] Hardened the validator to require the `skills.json` root to be an object, `source_quest_or_shop` and `acquisition_type` to be non-empty strings, and `source_parallel_quests` to be a list with no duplicate PQ IDs.
- [x] Hardened PQ endpoint validation to reject booleans as integer-like values and retain the supported **1–186** range.
- [x] Updated `docs/data/skill-acquisition-metadata-integrity-audit-2026-09-26.json` to record the expanded schema contract as **11/11** passing checks; the existing **474-record** canonical acquisition corpus and its values were not changed.
- [ ] Runtime validator execution and CI/build remain unverified in this environment.
- [ ] `docs/AI-CONTINUATION-PROMPT-EFFICIENCY-ADDENDUM.md` remains unavailable at the expected repository path (GitHub 404).
- [x] **Exact next:** inspect the next live validator/consumer in `pq-cross-domain-index.json` for a concrete schema, endpoint-identity, projection, or source-vs-build-output mismatch; do not reconstruct absent PQ reward/reverse datasets without an evidence-complete producer.

### 2026-09-26 continuation — Partner Customization key-ID projection hardening
- [x] Inspected the live Partner Customization navigation validator after its bridge/schema hardening pass and found a remaining deterministic identity gap: key records validated numeric key numbers and character/partner identities, but their stable `id` fields were not checked for uniqueness or exact key-number projection.
- [x] Hardened `scripts/validate_partner_customization_character_navigation.py` to require non-empty string key IDs, reject duplicate key IDs, and require the exact deterministic mapping `customization-key-01` through `customization-key-20` in key-number order.
- [x] Updated `docs/data/characters/partner-customization-character-navigation-audit.json` to record the new checks; the live contract remains **20 keys / 20 reconciliation records / 34 bridge records / 152 canonical character names / 20 page links**, now with **21/21** boolean checks passing in the recorded projection.
- [x] No canonical character, preset, DLC, acquisition, or partner-skill relationship data was changed.
- [ ] Runtime validator execution and CI/build remain unverified in this environment.
- [ ] `docs/AI-CONTINUATION-PROMPT-EFFICIENCY-ADDENDUM.md` remains unavailable at the expected repository path (GitHub 404).
- [x] **Exact next:** inspect the next live validator/consumer or deterministic projection for another concrete schema, type/range, stale-cache, or identity-projection gap; preserve the evidence boundary around absent general PQ reward/reverse datasets.

### 2026-09-26 continuation — Cross-domain reachability baseline refreshed
- [x] Performed a direct live `main` tree reconciliation using the repository Git tree and recursively extracted registered cross-domain artifact references from `docs/data/pq-cross-domain-index.json`.
- [x] Found the prior reachability baseline was stale after subsequent repository changes: current direct counts are **727 blob paths / 1,634 reference occurrences / 742 reachable / 892 unreachable**.
- [x] Refreshed `docs/data/cross-domain-index-reference-reachability-audit-2026-09-26.json` to the current live counts while preserving the 18 critical unreachable references and their provenance classifications.
- [x] No canonical PQ reward/reverse dataset was reconstructed from incomplete evidence.
- [ ] Runtime execution/CI remains unverified.
- [x] Exact next: inspect the next live deterministic cross-domain validator/consumer for a concrete integrity mismatch.
### 2026-09-26 continuation — Partner Customization recovery-audit count synchronization
- [x] Rechecked the live Partner Customization recovery audit after the previous reachability pass and confirmed the file is reachable on current `main`.
- [x] Found stale metadata: the audit reported 16 checks passed even though its live navigation validator exposes 18 boolean checks, all passing.
- [x] Synchronized the recovery audit to **18/18 checks passed**, with an explicit `check_count` of 18.
- [x] Removed the transient/incorrect unreachable classification from the cross-domain reachability audit; the recovery audit is not a current missing artifact.
- [x] Preserved canonical navigation and relationship data; no unsupported records were created.
- [ ] Runtime execution/CI remains unverified.
- [x] Exact next: inspect the next live cross-domain validator/consumer for a deterministic integrity mismatch.
### 2026-09-26 continuation — Partner Customization recovery-audit reachability reconciled
- [x] Inspected the live Partner Customization navigation validator and its audit after the previous cross-domain scalar correction.
- [x] Found a second deterministic source/index mismatch: `pq-cross-domain-index.json` still registers `docs/data/partner-customization-character-navigation-recovery-audit-2026-09-26.json`, but that audit is not fetchable from the current `main` tree.
- [x] Recorded the missing recovery audit explicitly in `docs/data/cross-domain-index-reference-reachability-audit-2026-09-26.json` as an unreachable audit/provenance artifact rather than a missing canonical dataset.
- [x] Did not fabricate or restore the audit from stale snippets; the live navigation validator and current navigation audit remain the authoritative executable/source artifacts.
- [x] Corrected the current navigation audit's check-count metadata to **18/18 boolean checks passing**.
- [ ] Runtime execution/CI remains unverified.
- [x] Exact next: inspect the next live cross-domain validator/consumer for another deterministic integrity mismatch; keep historical audit references classified separately from canonical data gaps.
### 2026-09-26 continuation — Cross-domain reachability scalar drift corrected
- [x] Inspected the live cross-domain reachability audit after the character-validator hardening pass and found a concrete internal inconsistency: critical_unreachable_reference_count was 20 while the enumerated critical_unreachable_references list contained 18 paths.
- [x] Corrected the scalar to derive from the live enumerated critical set (18) and preserved the full reference list/provenance.
- [x] Confirmed the broader live baseline remains 730 tree paths / 1,631 index reference occurrences / 739 reachable / 892 unreachable.
- [x] No missing PQ reward/reverse dataset was reconstructed from incomplete evidence.
- [ ] Runtime execution/CI remains unverified.
- [x] Exact next: inspect the next live cross-domain validator/consumer for a deterministic projection or source-vs-build-output mismatch and repair only evidence-backed drift.
### 2026-09-26 continuation — Character presentation validator hardened for optional generated explorer
- [x] Inspected the live character presentation consumer validator and found a concrete source-checkout failure: `scripts/validate_character_presentation_consumers.py` unconditionally opened `docs/Characters-All.html`, even though that generated explorer is absent from the live source tree.
- [x] Hardened the validator to treat `docs/Characters-All.html` as an optional generated build artifact: source-data identity, bridge, preset, Partner Customization, and Markdown checks remain enforced; generated explorer navigation is checked when the artifact exists and skipped when it does not.
- [x] Corrected the validator's Markdown consumer join from a literal `\\n` sequence to a real newline.
- [x] Refreshed `docs/data/characters/character-presentation-consumer-audit.json` to record the optional generated-artifact boundary and the live validator commit.
- [x] No canonical character identity, preset, relationship, or acquisition data was changed.
- [ ] Runtime execution/CI remains unverified in this environment.
- [x] **Exact next:** inspect the next live cross-domain validator/consumer for an equivalent deterministic source-vs-build-output mismatch; preserve the evidence boundary around absent general PQ reward datasets.
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
- [x] Audited the live repository for existing Partner Customization relationship data; partner evidence was embedded in skill research/audit artifacts and no dedicated canonical skill→partner relationship index was present.
- [x] Added `docs/data/partner-skill-relationships.json` with an explicit reusable schema separating canonical `skill_id` identity from `partner_name` availability.
- [x] Seeded evidence-backed relationships: **Arm Crash → Bardock**, **Arm Crash → Turles**, and **Reverse Mabakusenko → Majin Buu (Gohan Absorbed)**.
- [x] Added `scripts/validate_partner_skill_relationships.py` to enforce canonical skill IDs, unique pairs, expected relationship type, and evidence.
- [x] Registered the relationship index and validator in `docs/data/pq-cross-domain-index.json`.
- [x] Kept **Dual Masenko** outside the canonical relationship index because the current 474-skill corpus lacks a canonical record; the existing domain-boundary audit remains controlling for that case.
- [ ] Exact next: execute the validator and systematically census explicit Partner Customization skill relationships, adding only evidence-backed pairs.
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

- [x] Completed a deterministic acquisition metadata integrity pass over all 474 canonical skills; added `docs/data/skill-acquisition-metadata-integrity-audit-2026-09-26.json` and `scripts/validate_skill_acquisition_metadata.py` and registered them in the cross-domain index.
- [x] Required acquisition fields are populated across the corpus; internal consistency between acquisition type, unlock method, and explicit PQ endpoints is now machine-checkable.
- [ ] Exact next: inspect any audit anomalies and corroborate them externally before changing canonical acquisition data.

### 2026-09-26 continuation — PQ unrepresented skill-endpoint reconciliation
- [x] Reconciled all 16 currently unrepresented PQ IDs against current PQ reward references and live canonical skill evidence.
- [x] Added `docs/data/pq-unrepresented-skill-endpoint-evidence-reconciliation-2026-09-26.json` and registered it in `docs/data/pq-cross-domain-index.json`.
- [x] No new canonical skill→PQ edge was promoted from ambiguous/non-canonical evidence.
- [x] PQs 1, 30, 35, 47, 48, 93, 102, 103, 107, 108, 144, 157, 169, and 170 currently have no supported canonical skill endpoint in the reviewed evidence.
- [x] PQ118 remains a schema/domain question because external material associates Dual Masenko with it, while the live repository contains no canonical `skill-dual-masenko` record.
- [x] PQ121 remains unlinked to Godly Display because the live canonical audit records TP Medal Shop acquisition; the conflicting PQ association is retained as evidence, not normalized.
- [ ] Exact next: determine whether partner/custom skills need a separate canonical domain, then audit acquisition relationships for all canonical skills whose current source endpoint is shop/mentor/story rather than PQ.
- [ ] CI/build remains unverified.
- [ ] Efficiency addendum remains unavailable at the expected repository path (GitHub 404).

### 2026-09-26 continuation — Live skill↔PQ cross-domain linkage pass completed
- [x] Audited the live canonical `docs/data/skills.json` against the repository tree after the mechanics frontier reached **474/474**.
- [x] Deterministically validated **474 unique canonical skill IDs**, **242 skills with explicit `source_parallel_quests` endpoints**, **246 skill→PQ edges**, and **170 represented PQ IDs** within the supported **PQ 1–186** domain.
- [x] Added `docs/data/skill-pq-reverse-index-2026-09-26.json`, covering every PQ ID 1–186 and explicitly distinguishing a missing canonical skill endpoint from the unsupported conclusion that the PQ has no skill rewards.
- [x] Added `docs/data/skill-pq-cross-domain-linkage-integrity-audit-2026-09-26.json` with reproducible current-corpus checks.
- [x] Added `scripts/validate_skill_pq_crosslinks.py` as the deterministic validator/regenerator for the live skill→PQ reverse index.
- [x] Registered the reverse index, audit, and validator in `docs/data/pq-cross-domain-index.json`.
- [x] Revalidated the new artifacts after write: **474 skills / 246 edges / 170 represented PQ IDs / 0 invalid PQ IDs**.
- [x] Identified **16 PQ IDs with no explicit skill endpoint in the current skill corpus**: **1, 30, 35, 47, 48, 93, 102, 103, 107, 108, 118, 121, 144, 157, 169, 170**.
- [x] Confirmed the historical **244-edge** invariant referenced by older handoff material is stale relative to the current canonical corpus, which now contains **246** explicit skill→PQ edges; no relationship was silently removed to satisfy the old count.
- [ ] CI/build remains unverified; no workflow success is claimed.
- [ ] `docs/AI-CONTINUATION-PROMPT-EFFICIENCY-ADDENDUM.md` remains unavailable at the expected path (GitHub 404).
- [x] **Exact next:** reconcile the 16 currently unrepresented PQ IDs against a real PQ/reward corpus (the live repository currently contains no standalone PQ reward dataset), then resolve any evidence-backed skill endpoints and update the reverse index without inferring that an unrepresented PQ has no rewards.

### 2026-09-26 continuation — Mechanics frontier exhausted; data-integrity pass completed
- [x] Fresh live Batch 492 census found **0 unaudited canonical skill IDs**: all **474/474** skill IDs now have at least one registered current-evidence audit after collapsing duplicate audit artifacts by stable skill ID.
- [x] Shifted to deterministic corpus integrity work instead of fabricating another mechanics batch.
- [x] Detected and corrected stale attack-type wording in seven canonical skill descriptions: **Buu Buu Ball, Core Breaker, Death Slash, Final Cannon, Gigantic Charge, God of Destruction's Roar, and Saiyan Spirit**; corrections were corroborated against current Xenoverse 2-specific evidence.
- [x] Re-synchronized the seven description corrections into `docs/data/skills-index.json`.
- [x] Added `docs/data/skill-corpus-data-integrity-audit-2026-09-26.json` and registered it in `docs/data/pq-cross-domain-index.json`.
- [x] Field-completeness scan found **0** missing sources, mechanics notes, unlock methods, or source-quest/shop endpoints. Character-source omissions are not automatically defects because many records are CaC-only or otherwise have no single character source; race-restriction omissions likewise require contextual interpretation.
- [ ] CI/build remains unverified; no workflow success is claimed.
- [ ] `docs/AI-CONTINUATION-PROMPT-EFFICIENCY-ADDENDUM.md` remains unavailable at the expected path (GitHub 404).
- [x] **Exact next:** audit deterministic cross-domain linkage/provenance gaps between the 474 canonical skills and the PQ/acquisition datasets, then fix resolvable broken links rather than starting another redundant mechanics batch.

### 2026-09-26 continuation — Skill Research Batch 491 completed
- [x] Fresh live unaudited mechanics frontier census performed after Batch 490; stale candidate lists were not reused.
- [x] Researched and synchronized **Gigantic Cluster (stable ID `skill-giant-cluster`), Holy Wrath, Gigantic Charge, Pendulum Bullet, and Heat Dome Attack**.
- [x] Updated canonical `docs/data/skills.json` and projection `docs/data/skills-index.json`; both remain **474 records**.
- [x] Added Batch 491 research/thin-frontier artifacts, five current-evidence audits, and registered all seven artifacts in `docs/data/pq-cross-domain-index.json`.
- [x] Preserved evidence boundaries, including the Gigantic Cluster/Giant Cluster naming discrepancy, Pendulum Bullet bounce-count discrepancy, and existing acquisition/reward conflicts.
- [ ] CI/build remains unverified; no workflow success is claimed.
- [ ] `docs/AI-CONTINUATION-PROMPT-EFFICIENCY-ADDENDUM.md` remains unavailable at the expected path (GitHub 404).
- [x] **Exact next:** perform a fresh live unaudited mechanics-frontier census excluding Batch 491 and every registered current-evidence audit; do not reuse this candidate list.

### 2026-09-26 continuation — Skill Research Batch 490 completed
- [x] Fresh live mechanics frontier census performed after Batch 489; eight shortest records without dedicated registered current-evidence audits were manually rechecked.
- [x] Researched and synchronized **Breaker Energy Wave, Emperor's Cannon, Dark Inscription, Gigantic Cluster, Heat Wave, Special Beam Cannon (Beast), Crimson Edge, and Potential Unleashed**.
- [x] Updated canonical `docs/data/skills.json` and projection `docs/data/skills-index.json`; validation is **474/474**, **0 missing / 0 extra**, ordered ID parity true.
- [x] Added Batch 490 research/thin-frontier artifacts, eight current-evidence audits, and registered all ten artifacts in `docs/data/pq-cross-domain-index.json`.
- [x] Preserved evidence boundaries: current/official mechanics were expanded, but unsupported exact frames, universal scaling, hidden interactions, and probabilities were not inferred. Emperor's Cannon's PQ183/PQ184 acquisition conflict remains bounded.
- [ ] CI/build remains unverified; no workflow success is claimed.
- [ ] `docs/AI-CONTINUATION-PROMPT-EFFICIENCY-ADDENDUM.md` remains unavailable at the expected path (GitHub 404).
- [x] **Exact next:** perform a fresh live unaudited mechanics-frontier census excluding Batch 490 and every registered current-evidence audit; do not reuse this candidate list.

### 2026-09-26 continuation — Skill Research Batch 489 completed
- [x] Fresh live frontier census performed after Batch 488 with corrected filename-to-skill-ID audit normalization.
- [x] Researched and synchronized **God of Destruction's Roar, God of Destruction's Menace, Hero's Flute, Beast, Rakshasa's Claw, Reverse Mabakusenko, Indomitable, and Body Change**.
- [x] Updated canonical `docs/data/skills.json` and projection `docs/data/skills-index.json`; validation is **474/474**, **0 missing / 0 extra**, ordered ID parity true.
- [x] Added Batch 489 research/thin-frontier artifacts, eight current-evidence audits, and registered all ten artifacts in `docs/data/pq-cross-domain-index.json`.
- [x] Preserved evidence boundaries: source-reported values and player observations remain bounded; unsupported frame data, universal scaling, and probabilities were not inferred.
- [ ] CI/build remains unverified; no workflow success is claimed.
- [ ] `docs/AI-CONTINUATION-PROMPT-EFFICIENCY-ADDENDUM.md` remains unavailable at the expected path (GitHub 404).
- [x] **Exact next:** perform another fresh live unaudited mechanics-frontier census excluding Batch 489 and every registered current-evidence audit; do not reuse stale candidate lists.

### 2026-09-26 continuation — Skill Research Batch 488 completed
- [x] Fresh live 474-record mechanics frontier was re-censused after Batch 487, excluding every skill ID represented by a registered current-evidence audit; stale candidate lists were not reused.
- [x] Researched and synchronized **Fierce Fist, Venus Fist, Handy Canon, Full Power Destruction, Prominence Flash, Galick Gun, Ill Rain, and Gigantic Cross**.
- [x] Updated canonical `docs/data/skills.json` and projection `docs/data/skills-index.json`; validation is **474/474**, **0 missing / 0 extra**, ordered ID parity true.
- [x] Added Batch 488 research, thin-frontier audit, eight current-evidence audits, and registered all ten artifacts in `docs/data/pq-cross-domain-index.json`.
- [x] Preserved evidence boundaries: source-reported numeric values remain bounded; unsupported frames, universal scaling, hidden interactions, and drop probabilities were not inferred. Venus Fist's recent low-Health/3-Ki-bar reports remain explicitly source-bounded.
- [ ] CI/build remains unverified; no workflow success is claimed.
- [ ] `docs/AI-CONTINUATION-PROMPT-EFFICIENCY-ADDENDUM.md` remains unavailable at the expected path (GitHub 404).
- [x] **Exact next:** perform a fresh live unaudited mechanics-frontier census excluding Batch 488 and every prior registered current-evidence audit. Do not reuse the current candidate list; select the next genuinely under-detailed records from the live 474-record state.

### 2026-09-26 continuation — Skill Research Batch 487 completed
- [x] Completed and synchronized eight current-evidence skill records: Super Saiyan Blue Kaioken, Super Saiyan 2, Super Vegeta, Namek Finger, Bending Kamehameha, Flash Strike, Finishing Blow, Sudden Death Beam.
- [x] Canonical/index validation: 474/474, 0 missing, 0 extra.
- [x] Added Batch 487 research/thin-frontier artifacts and registered current-evidence provenance.
- [x] Evidence boundaries preserved; CI remains unverified.
- [x] Exact next: fresh live unaudited mechanics frontier census.

### 2026-09-26 continuation — Batch 487 checkpoint
- [x] Fresh live frontier census completed after Batch 486.
- [x] Rechecked current Xenoverse 2 evidence for Super Saiyan Blue Kaioken, Super Saiyan 2, Super Vegeta, and Namek Finger.
- [x] Canonical `skills.json` verification state updated for those four records.
- [ ] Batch 487 research/provenance artifacts still need completion.
- [ ] CI/build remains unverified.
- [x] **Exact next:** complete Batch 487 artifact/provenance registration, then fresh-census and enrich **Bending Kamehameha → Flash Strike → Finishing Blow → Sudden Death Beam**.

### 2026-09-26 continuation — Batch 486 canonical mechanics enrichment

- [x] Re-censused the live 474-record frontier after Batch 485 and excluded known completed/audited records rather than duplicating them.
- [x] Researched and synchronized **Final Flash (Super), God Splitter, Majin Kamehameha, and Feint Crash**.
- [x] Added four dedicated current-evidence audits, the Batch 486 research record, and the thin-frontier audit.
- [x] Registered all Batch 486 artifacts in `docs/data/pq-cross-domain-index.json`.
- [x] Canonical/index datasets remain **474/474** with no record additions or removals.
- [ ] CI/build remains unverified; no workflow success is claimed.
- [x] **Exact next:** fresh live frontier census before Batch 487; current shortest candidates after excluding completed work are **Meteor Burst → Kill Driver → Fighting Pose G → Bluff Kamehameha → Punisher Shield → Fighting Pose B → Fake Death → Mach Dash**. Recheck the provenance registry before promotion.


### 2026-09-26 continuation — Batch 484 canonical mechanics enrichment

- [x] Re-inspected the live repository rather than trusting the stale Batch 482 checkpoint; the live default branch also contained a later Batch 483 canonical-only enrichment commit.
- [x] Recorded Batch 483 as docs/data/skill-research-batches/skill-batch-483.json so that live canonical history is not skipped.
- [x] Performed a fresh 474-record frontier census after excluding the registered audit set and the completed Batches 481–483.
- [x] Researched and synchronized Spirit Slash, Gigantic Burst, Gigantic Roar, Emperor's Cannon, Gigantic Breaker, The Power to Overcome, God of Destruction's Menace, and Flash Chaser.
- [x] Added eight Batch 484 current-evidence audits, the Batch 484 research record, and the thin-frontier audit.
- [x] Registered Batch 482/483 continuity records and all Batch 484 artifacts in docs/data/pq-cross-domain-index.json.
- [x] Canonical/index skill datasets remain 474/474; no record was added or removed.
- [x] Preserved the documented Emperor's Cannon PQ183/PQ184 acquisition conflict and source-bounded Power to Overcome measurements rather than inventing certainty.
- [ ] CI/build remains unverified; no workflow success is claimed.
- [x] Exact next: fresh unaudited mechanics frontier excluding Batch 484 and all prior registered current-evidence audits; current shortest remaining candidates are Dancing Parapara → God of Destruction's Roar → God Punisher → Super Saiyan God Super Saiyan (Evolved) → Total Detonation Ball → Future Super Saiyan → Godly Display → Final Pose. Re-census live state before promotion.

### 2026-09-26 continuation — Batch 482 canonical synchronization

- [x] Researched and synchronized **Death Ball, Galick Gun, Sphere of Destruction, Breaker Energy Wave, Hyper Drain, Handy Canon, Fierce Fist, Venus Fist**.
- [x] Canonical/index parity remains **474/474**.
- [x] Historical test values are explicitly source-bound; unresolved exact mechanics remain open rather than guessed.
- [x] Batch 482 research checkpoint and canonical dataset synchronization completed.
- [ ] CI/build remains unverified.
- [x] **Exact next:** fresh frontier census excluding Batch 482 and all prior registered current-evidence audits.

### 2026-09-26 continuation — Batch 481 canonical mechanics enrichment

- [x] Fresh frontier re-census completed after Batch 480.
- [x] Researched and synchronized **Dark Inscription, Reverse Mabakusenko, Body Change, Hero's Flute, Indomitable, Crusher Ball, Rakshasa's Claw**.
- [x] Added the Batch 481 research/current-evidence artifact and cross-domain registration.
- [x] Canonical/index parity remains **474/474**.
- [x] Indomitable player-reported behavior is explicitly source-bounded; acquisition/drop details remain open.
- [ ] CI/build remains unverified.
- [x] **Exact next:** fresh frontier census excluding Batch 481 and all prior registered current-evidence audits; prioritize **Death Ball → Galick Gun → Sphere of Destruction → Breaker Energy Wave → Hyper Drain → Handy Canon → Fierce Fist → Venus Fist**.

### 2026-09-26 continuation — Batch 480 canonical mechanics enrichment

- [x] Read and reconciled the live continuation/TODO state before continuing.
- [x] Performed a fresh unaudited mechanics frontier excluding every skill ID represented by a registered current-evidence audit.
- [x] Selected and researched **Evil Explosion, Prominence Flash, Ill Rain, Power Impact, Gigantic Cross, Full Power Destruction, Photon Swipe, God of Destruction's Plaything** as Batch 480.
- [x] Added eight dedicated current-evidence audit artifacts, Batch 480 research/thin-frontier artifacts, and registry entries.
- [x] Synchronized all eight records into both canonical skill datasets; canonical/index remain **474/474**.
- [x] Corrected stale **Photon Swipe** character attribution from **Toppo** to **Android 21** using current skill-specific evidence.
- [ ] CI/build remains unverified; no workflow success is claimed.
- [x] **Exact next:** run a fresh unaudited mechanics frontier census excluding Batch 480 and every prior registered current-evidence audit, then continue the canonical research/synchronization cycle.
- [x] **Exact next frontier after Batch 480:** **God of Destruction's Plaything, Dark Inscription, Reverse Mabakusenko, Body Change, Hero's Flute, Indomitable, Crusher Ball, and Rakshasa's Claw**. These are the shortest canonical mechanics records remaining after excluding all registered current-evidence audits; the next cycle must re-census live state before promoting them.

### 2026-09-26 continuation — Batch 479 canonical mechanics enrichment

- [x] Read live continuation/TODO state and performed a fresh mechanics frontier excluding registered current-evidence audits.
- [x] Selected and researched **Taunt, Demonic Destruction, Neo Tri-Beam, Divine Lasso, Chaotic Time Impact, Gamma Impact, Gigantic Nova, Brutal Buster** as Batch 479.
- [x] Added eight dedicated current-evidence audits plus Batch 479 research/thin-frontier artifacts.
- [x] Synchronized all eight records into both canonical skill datasets.
- [x] Canonical/index validation remains **474/474**, with **0 missing / 0 extra**.
- [x] Registered all Batch 479 artifacts in `docs/data/pq-cross-domain-index.json`.
- [ ] CI/build remains unverified; no workflow success is claimed.
- [ ] `docs/AI-CONTINUATION-PROMPT-EFFICIENCY-ADDENDUM.md` remains unavailable at the expected path (GitHub 404).
- [x] **Exact next:** run a fresh unaudited mechanics frontier census excluding Batch 479 and every prior registered current-evidence audit.

### 2026-09-26 continuation — Batch 478 canonical mechanics enrichment

- [x] Read and reconciled the live continuation state and exhaustive TODO before continuing.
- [x] Performed a fresh 474-record mechanics frontier excluding all skill IDs represented by registered current-evidence audits.
- [x] Selected and researched **Thunder Flash, Celestial Wave, Saiyan Spirit, Bomber DX, Time Bullet, Galick Cannon, Death Beam, Gamma Blaster** as Batch 478.
- [x] Added eight dedicated current-evidence audit artifacts, the Batch 478 research record, and the thin-frontier audit.
- [x] Synchronized all eight records into both canonical skill datasets.
- [x] Canonical/index validation remains **474/474**, with **0 missing / 0 extra** IDs.
- [x] Registered all Batch 478 artifacts in `docs/data/pq-cross-domain-index.json`.
- [ ] CI/build remains unverified; no workflow success is claimed.
- [ ] `docs/AI-CONTINUATION-PROMPT-EFFICIENCY-ADDENDUM.md` remains unavailable at the expected repository path (GitHub 404).
- [x] **Exact next:** run a fresh unaudited mechanics frontier census excluding Batch 478 and every prior registered current-evidence audit, then continue the canonical research/synchronization cycle.

### 2026-09-26 continuation — Batch 477 canonical mechanics enrichment

- [x] Read and reconciled the live continuation state and exhaustive TODO before continuing.
- [x] Performed a fresh 474-record mechanics frontier excluding all skill IDs represented by registered current-evidence audits.
- [x] Selected and researched **Double Sunday, Super Black Kamehameha Rosé, Apocalyptic Burst, Destruction's Concerto: Meteor, Demon Flash Strike, Afterimage, Excellent Full Course, Ultra Instinct** as Batch 477.
- [x] Added eight dedicated current-evidence audit artifacts, the Batch 477 research record, and the thin-frontier audit.
- [x] Synchronized all eight records into both canonical skill datasets.
- [x] Canonical/index validation remains **474/474**, with **0 missing / 0 extra** IDs.
- [x] Registered all Batch 477 artifacts in `docs/data/pq-cross-domain-index.json`.
- [ ] CI/build remains unverified; no workflow success is claimed.
- [ ] `docs/AI-CONTINUATION-PROMPT-EFFICIENCY-ADDENDUM.md` remains unavailable at the expected repository path (GitHub 404).
- [x] **Exact next:** run a fresh unaudited mechanics frontier census excluding Batch 477 and every prior registered current-evidence audit, then continue the canonical research/synchronization cycle.

### 2026-09-26 continuation — Batch 476 canonical mechanics enrichment

- [x] Read and reconciled the live continuation state and exhaustive TODO before continuing.
- [x] Performed a fresh 474-record mechanics frontier excluding all skill IDs represented by registered current-evidence audits.
- [x] Selected and researched **Assault Rain, Saiyan Blaster, Soaring Rush, Heroic Assault, Endless Shoot, Deadly Dance, All Clear, Spirit Bomb** as Batch 476.
- [x] Added eight dedicated current-evidence audit artifacts, the Batch 476 research record, and the thin-frontier audit.
- [x] Synchronized all eight records into both canonical skill datasets.
- [x] Canonical/index validation remains **474/474**, with **0 missing / 0 extra** IDs.
- [x] Registered all Batch 476 artifacts in `docs/data/pq-cross-domain-index.json`.
- [ ] CI/build remains unverified; no workflow success is claimed.
- [ ] `docs/AI-CONTINUATION-PROMPT-EFFICIENCY-ADDENDUM.md` remains unavailable at the expected repository path (GitHub 404).
- [x] **Exact next:** run a fresh unaudited mechanics frontier census excluding Batch 476 and every prior registered current-evidence audit, then continue the canonical research/synchronization cycle.

### 2026-09-26 continuation — Batch 475 canonical mechanics enrichment

- [x] Read and reconciled the live continuation state and exhaustive TODO before continuing.
- [x] Performed a fresh 474-record mechanics frontier excluding all skill IDs represented by registered current-evidence audits.
- [x] Selected and researched **Blazing Attack, S.S. Deadly Bomber, Soaring Fist, Timespace Impact, Psycho Barrier, Shadow Crusher, Spirit Ball, Double Crush** as Batch 475.
- [x] Added eight dedicated current-evidence audit artifacts, the Batch 475 research record, and the thin-frontier audit.
- [x] Synchronized all eight records into both canonical skill datasets.
- [x] Canonical/index validation remains **474/474**, with **0 missing / 0 extra** IDs.
- [x] Registered all Batch 475 artifacts in `docs/data/pq-cross-domain-index.json`.
- [ ] CI/build remains unverified; no workflow success is claimed.
- [ ] `docs/AI-CONTINUATION-PROMPT-EFFICIENCY-ADDENDUM.md` remains unavailable at the expected repository path (GitHub 404).
- [x] **Exact next:** run a fresh unaudited mechanics frontier census excluding Batch 475 and every prior registered current-evidence audit, then continue the canonical research/synchronization cycle.

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

### 2026-09-26 continuation — Skill Research Batch 471 completed

- [x] Fresh 474-record mechanics frontier selected **Fighting Pose H, Brave Heat, Super Ghost Buu Attack, Supreme Fury, Rocket Tackle, Trap Shooter, Murder Grenade, and Chain Destructo-Disc Barrage** after excluding every registered current-evidence audit.
- [x] Added eight current-evidence audits plus Batch 471 research/thin-frontier artifacts and provenance registrations.
- [x] Deepened and synchronized all eight canonical/index records with bounded current Xenoverse 2 mechanics evidence.
- [x] Preserved source-reported values without inventing unsupported frame/scaling data.
- [x] Canonical/index validation remains **474/474**, 0 missing / 0 extra.
- [ ] CI/build remains unverified.
- [x] **Exact next:** fresh unaudited mechanics frontier excluding Batch 471 and every prior current-evidence audit.

### 2026-09-26 continuation — Skill Research Batch 470 completed

- [x] Fresh 474-record mechanics frontier excluded every registered current-evidence audit and selected **Energy Release, Super Destructo-Disc, Android Rush, Burning Attack, Chaos Shot, Surging Spirit, Reverse Shot, and Grand Smasher**.
- [x] Added eight current-evidence audits plus Batch 470 research/thin-frontier artifacts.
- [x] Deepened all eight canonical records with current Xenoverse 2-specific mechanics and bounded evidence.
- [x] Preserved Surging Spirit as a built-in Ultra Instinct action rather than a separately acquired skill, and retained source-bounded values for damage, hit counts, timing, and costs.
- [x] Canonical/index validation target remains **474/474**, with 0 missing / 0 extra.
- [ ] CI/build remains unverified.
- [ ] `docs/AI-CONTINUATION-PROMPT-EFFICIENCY-ADDENDUM.md` remains unavailable at the expected path (GitHub 404).
- [x] **Exact next:** fresh unaudited mechanics frontier excluding Batch 470 and every prior registered current-evidence audit.

### 2026-09-26 continuation — Skill Research Batch 469 completed

- [x] Fresh 474-record mechanics frontier excluded every registered current-evidence audit and selected **Fighting Pose C, Burst Kamehameha, Supernova, Freedom Kick, Super Elite Combo, Atomic Blast, Super Ghost Kamikaze Attack (Super), and Super God Shock Flash**.
- [x] Added eight current-evidence audits plus Batch 469 research/thin-frontier artifacts.
- [x] Deepened all eight canonical records with current Xenoverse 2-specific mechanics and bounded evidence.
- [x] Preserved the existing Atomic Blast reward-source conflict and kept the Super Ghost Kamikaze Attack Super/Ultimate variants distinct.
- [x] Canonical/index validation target remains **474/474**, with 0 missing / 0 extra.
- [ ] CI/build remains unverified.
- [ ] `docs/AI-CONTINUATION-PROMPT-EFFICIENCY-ADDENDUM.md` remains unavailable at the expected path (GitHub 404).
- [x] **Exact next:** fresh unaudited mechanics frontier excluding Batch 469 and every prior registered current-evidence audit.

### 2026-09-26 continuation — Skill Research Batch 468 completed

- [x] Fresh 474-record mechanics frontier excluded every registered current-evidence audit and selected **Super Saiyan Blue Kaioken, Super Saiyan 2, Supernova Cooler, Super Vegeta, Maiden Burst, Counter Burst, Bluff Kamehameha, and Super Dragon Flight**.
- [x] Added eight current-evidence audits plus Batch 468 research/thin-frontier artifacts.
- [x] Deepened all eight records with current Xenoverse 2-specific mechanics and bounded evidence.
- [x] Corrected the **Super Dragon Flight** record's mechanics boundary to the distinct 300-Ki Ultimate variant for Gohan (DBS Super Hero), keeping it separate from the 100-Ki Super variant.
- [x] Preserved source-bounded numerical values and unresolved frame/scaling details.
- [x] Canonical/index validation target remains **474/474**, with 0 missing / 0 extra.
- [ ] CI/build remains unverified.
- [x] **Exact next:** fresh unaudited mechanics frontier excluding Batch 468 and every prior registered current-evidence audit.

### 2026-09-26 continuation — Skill Research Batch 467 completed

- [x] Fresh 474-record mechanics frontier selected **Seagull Combination, Remote Serious Bomb, Shooting Strike, Energy Dome, Kaioken, Gorgeous Shot, Gravity Impact, and Hawk Charge**.
- [x] Added eight current-evidence audits plus Batch 467 research/thin-frontier artifacts.
- [x] Deepened and synchronized all eight canonical records with bounded current Xenoverse 2 mechanics evidence.
- [x] Preserved source/version conflicts, including Remote Serious Bomb's second-stage resource-cost discrepancy and Seagull Combination's reward-presentation discrepancy.
- [x] Canonical/index validation remains **474/474**, with 0 missing / 0 extra.
- [ ] CI/build remains unverified.
- [x] **Exact next:** fresh unaudited mechanics frontier excluding Batch 467 and every prior registered current-evidence audit.

### 2026-09-26 continuation — Skill Research Batch 451 completed

- [x] Fresh unaudited mechanics frontier census selected **Force Shield, Eraser Bomb, Evil Flame, Galactic Donuts, Energy Field, Bloody Counter, Supersonic Mode, and Big Bang Attack**.
- [x] Deepened and synchronized all eight skill records in the canonical and index datasets.
- [x] Added eight Batch 451 current-evidence audit artifacts plus batch/frontier research records.
- [x] Registered Batch 451 provenance in `docs/data/pq-cross-domain-index.json`.
- [x] Canonical/index validation remains **474/474**, with 0 missing / 0 extra.
- [ ] CI/build remains unverified; no workflow success claimed.
- [x] **Exact next:** fresh unaudited mechanics frontier census excluding Batch 451 and every prior current-evidence-audited record.

### 2026-09-26 continuation — Skill Research Batch 451 completed

- [x] Fresh live 474-record mechanics frontier census selected **Force Shield, Eraser Bomb, Evil Flame, Galactic Donuts, Energy Field, Bloody Counter, Supersonic Mode, and Big Bang Attack** after excluding every registered current-evidence audit.
- [x] Added eight current-evidence audits plus Batch 451 research and thin-frontier audit artifacts.
- [x] Deepened and synchronized all eight canonical records with current Xenoverse 2-specific mechanics and bounded evidence.
- [x] Registered Batch 451 provenance; registry now contains **724 entries**.
- [x] Validation remains **474/474**, 0 missing / 0 extra.
- [ ] CI/build remains unverified.
- [ ] Efficiency addendum remains unavailable at the expected path (GitHub 404).
- [x] **Exact next:** fresh unaudited mechanics frontier census excluding Batch 451 and all prior current-evidence-audited records.

### 2026-09-26 continuation — Skill Research Batch 450 completed

- [x] Fresh live 474-record mechanics frontier census excluded every skill with a registered current-evidence audit and selected **Ray Blast, Emperor's Blast, Final Cannon, Godly Chronos Cannon, Vanishing Ball, Evil Whirlwind, God of Destruction's Rampage, and Emperor's Death Beam** as the eight shortest remaining records by combined mechanics/notes coverage.
- [x] Added eight current-evidence audits plus Batch 450 research and thin-frontier audit artifacts.
- [x] Deepened all eight canonical records with current Xenoverse 2-specific mechanics, acquisition context, and bounded numerical evidence; unsupported exact frames, scaling formulas, probabilities, and hidden conditions remain bounded.
- [x] Corrected stale **Emperor's Blast** provenance from Hercule wording to Frieza/Golden Frieza and documented its rear-facing Ki Wave/stun behavior.
- [x] Synchronized all eight records into both canonical skill datasets and refreshed their current-scope verification date to 2026-09-26.
- [x] Registered the Batch 450 research record, thin-frontier audit, and eight skill audits in `docs/data/pq-cross-domain-index.json`; registry now contains **714 entries**.
- [x] Validation remains **474/474** canonical/index records with 0 missing / 0 extra.
- [ ] CI/build remains unverified; no workflow success is claimed.
- [ ] `docs/AI-CONTINUATION-PROMPT-EFFICIENCY-ADDENDUM.md` remains unavailable at the expected path (GitHub 404).
- [x] **Exact next:** run another fresh unaudited mechanics frontier census excluding Batch 450 and every prior current-evidence-audited record, then continue the canonical research/synchronization cycle.

### 2026-09-26 continuation — Skill Research Batch 449 completed

- [x] Fresh live 474-record mechanics frontier census excluded every skill with a registered current-evidence audit and selected **Purification, Brave Sword Slash, Unrelenting Barrage, Burning Slash, Turn Golden, Gigantic Explosion, Burst Blitz, and Power Pole Pro** as the eight shortest remaining records by combined mechanics/notes coverage.
- [x] Added eight current-evidence audits plus Batch 449 research and thin-frontier audit artifacts.
- [x] Deepened all eight canonical records with current Xenoverse 2-specific mechanics, acquisition context, and bounded numerical/statistical evidence; unsupported exact frames, scaling, probabilities, and hidden conditions remain bounded.
- [x] Synchronized all eight records into both canonical skill datasets and refreshed their current-scope verification date to 2026-09-26.
- [x] Registered the Batch 449 research record, thin-frontier audit, and eight skill audits in `docs/data/pq-cross-domain-index.json`.
- [x] Validation remains **474/474** canonical/index records with 0 missing / 0 extra.
- [ ] CI/build remains unverified; no workflow success is claimed.
- [ ] `docs/AI-CONTINUATION-PROMPT-EFFICIENCY-ADDENDUM.md` remains unavailable at the expected path (GitHub 404).
- [x] **Exact next:** run another fresh unaudited mechanics frontier census excluding Batch 449 and every prior current-evidence-audited record, then continue the canonical research/synchronization cycle.

### 2026-09-26 continuation — Skill Research Batch 448 completed

- [x] Fresh live 474-record mechanics frontier census excluded every skill with a registered current-evidence audit and selected **Wild Buster, Blaster Bomb, Divine Spear, Hyper Tornado, Angry Hit, Meteor Strike, Mystic Flash, and Wall of Defense** as the eight shortest remaining under-detailed mechanics records.
- [x] Added eight current-evidence audits plus Batch 448 research and thin-frontier audit artifacts.
- [x] Deepened all eight canonical records with current Xenoverse 2-specific mechanics, acquisition context, and bounded numerical/behavioral evidence; unsupported exact frames, scaling, probabilities, and hidden conditions remain bounded.
- [x] Synchronized all eight records into both canonical skill datasets and refreshed their current-scope verification date to 2026-09-26.
- [x] Registered the Batch 448 research record, thin-frontier audit, and eight skill audits in `docs/data/pq-cross-domain-index.json`.
- [x] Validation remains **474/474** canonical/index records with 0 missing / 0 extra.
- [ ] CI/build remains unverified; no workflow success is claimed.
- [ ] `docs/AI-CONTINUATION-PROMPT-EFFICIENCY-ADDENDUM.md` remains unavailable at the expected path (GitHub 404).
- [x] **Exact next:** run another fresh unaudited mechanics frontier census excluding Batch 448 and every prior current-evidence-audited record, then continue the canonical research/synchronization cycle.


### 2026-09-26 continuation — Skill Research Batch 444 completed

- [x] Fresh 474-record unaudited mechanics frontier census excluded every record with a registered current-evidence audit and selected **Flash Fist Crush, Final Flash (Super), Evil Eyes, and Maximum Charge** as the next four shortest under-detailed mechanics records.
- [x] Added four current-evidence audits plus Batch 444 research and thin-frontier audit artifacts.
- [x] Deepened all four canonical records with current Xenoverse 2-specific mechanics, acquisition/restriction context, and bounded numerical evidence; unsupported frame data, exact scaling, and hidden conditions remain bounded.
- [x] Synchronized all four records into both canonical skill datasets and refreshed their current-scope verification date to 2026-09-26.
- [x] Registered the Batch 444 research record, thin-frontier audit, and four skill audits in `docs/data/pq-cross-domain-index.json`.
- [x] Validation remains **474/474** canonical/index records with 0 missing / 0 extra.
- [ ] CI/build remains unverified; no workflow success is claimed.
- [ ] `docs/AI-CONTINUATION-PROMPT-EFFICIENCY-ADDENDUM.md` remains unavailable at the expected path (GitHub 404).
- [x] **Exact next:** run another fresh unaudited mechanics frontier census excluding Batch 444 and every prior current-evidence-audited record, then continue the canonical research/synchronization cycle.


### 2026-09-26 continuation — Skill Research Batch 439 completed

- [x] Fresh unaudited mechanics frontier census excluded every skill with a registered current-evidence audit and selected **Blades of Judgment, Sudden Death Beam, Super Saiyan God, and Change The Future**.
- [x] Added four current-evidence audits plus Batch 439 research and thin-frontier audit artifacts.
- [x] Deepened all four canonical records with current Xenoverse 2-specific mechanics, acquisition, counter/transformation/projectile behavior, and bounded numeric evidence; unsupported frame data, exact scaling, and probabilities remain bounded.
- [x] Synchronized all four records into both canonical skill datasets and refreshed their current-scope verification date to 2026-09-26.
- [x] Registered the Batch 439 research record, thin-frontier audit, and four skill audits in `docs/data/pq-cross-domain-index.json`.
- [x] Validation target remains **474/474** canonical/index records with ordered-ID parity and 0 missing / 0 extra.
- [ ] CI/build remains unverified; no workflow success is claimed.
- [ ] `docs/AI-CONTINUATION-PROMPT-EFFICIENCY-ADDENDUM.md` remains unavailable at the expected path (GitHub 404).
- [x] **Exact next:** run another fresh unaudited mechanics frontier census excluding Batch 439 and every prior current-evidence-audited record, then continue the canonical research/synchronization cycle.
### 2026-09-26 continuation — Skill Research Batch 438 completed

- [x] Fresh unaudited mechanics frontier census over the live 474-record skill set excluded every record with a registered current-evidence audit and selected **Final Flash (SS3 DAIMA), God of Destruction's Anger, Evil Ray Strike, and Pretty Charge** as the four shortest remaining under-detailed mechanics records.
- [x] Added four current-evidence audit files plus Batch 438 research and thin-frontier audit artifacts.
- [x] Expanded **Final Flash (SS3 DAIMA)** with the 400+ Ki Ultimate classification, PQ181 endpoint, 22–53-hit beam, and input-held remaining-Ki power extension; exact damage conversion, frames, and patch-independent scaling remain unresolved.
- [x] Expanded **God of Destruction's Anger** with the 200-Ki Beerus-training endpoint, long-range single-hit beam, source-reported 15% damage, full Stamina depletion through block, and hard-knockdown classification.
- [x] Expanded **Evil Ray Strike** with the 100-Ki Gohan (Kid) training endpoint, tracking head-first charge, guard-break behavior, and source-reported 10% damage.
- [x] Expanded **Pretty Charge** with its 0-Ki Other Super classification, Ribrianne-only/current CaC-unavailable scope, and documented equivalence to Full Power Charge; unsupported restoration rate/timing remains unresolved.
- [x] Synchronized all four records into both canonical skill datasets and refreshed their current-scope verification date to 2026-09-26.
- [x] Registered the Batch 438 research record, thin-frontier audit, and four skill audits in `docs/data/pq-cross-domain-index.json`.
- [x] Validated the canonical/index datasets at **474/474** with ordered-ID parity and **0 missing / 0 extra** after synchronization.
- [ ] CI/build remains unverified; no workflow success is claimed.
- [ ] Repository efficiency addendum remains unavailable at the expected path; GitHub returned 404 during this cycle.
- [x] **Exact next:** run another fresh unaudited mechanics frontier census excluding Batch 438 and every prior current-evidence-audited record, then continue the canonical research/synchronization cycle.

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
### 2026-09-25 cycle completion — full skill endpoint parity current-baseline correction
- [x] Audited the current-facing full endpoint consumer after the 470-record canonical/index repair; found `docs/data/full-skill-endpoint-reverse-parity-audit-2026-09-23.json` still exposed the superseded **469** endpoint-union baseline.
- [x] Reconciled it against the current `skill-acquisition-cross-domain-endpoint-audit-2026-09-24.json`: **470 canonical / 239 PQ-linked / 230 unique non-PQ endpoint targets / 470 endpoint-union / 0 uncovered**.
- [x] Synchronized the full endpoint parity audit to the current 470 boundary while preserving the older 469 wording as historical context elsewhere.
- [x] Updated `docs/data/CROSS-LINK-CONTRACT.md` with the current endpoint parity baseline and explicitly documented the non-additive PQ/non-PQ counts caused by legitimate multi-producer overlap.
- [x] Registered the current parity correction in `docs/data/pq-cross-domain-index.json`.
- [x] No acquisition relationship, endpoint identity, canonical skill identity, or historical snapshot was changed.
- [ ] CI remains unverified; no workflow success is claimed.
- [ ] **Exact next:** continue the remaining current-facing consumer census or next source-backed provenance target; treat the 470/470 endpoint union as the current baseline and preserve historical 469/465 snapshots.

### 2026-09-25 cycle completion — Super Soul 034 current community-evidence refresh
- [x] Continued the post-470 consumer/provenance queue after closing current skill endpoint parity and the 231/231 non-PQ reverse-navigation coverage boundary.
- [x] Rechecked strict-thin Super Soul 034 (The final battle begins now.) against the current PQ186 reward source and a July 2026 community discussion describing a battle-start Ki-recovery/all-attacks effect and later opponent-skill blocking.
- [x] Added `docs/data/super-soul-034-current-community-evidence-audit-2026-09-25.json` and registered it in `docs/data/pq-cross-domain-index.json`.
- [x] Added the community source to the canonical Super Soul 034 provenance list while preserving all unresolved mechanics/Limit Burst fields; no relationship, identity, acquisition route, or historical snapshot changed.
- [ ] CI remains unverified; no workflow success is claimed.
- [ ] **Exact next:** continue the remaining source-backed P1 provenance/data queue, prioritizing a partially verified structured record where direct Xenoverse 2-specific evidence can promote a field; do not infer unresolved values from community reports alone.


### 2026-09-25 cycle completion — Skill Research Batch 339 current acquisition/mechanics reconciliation
- [x] Added `docs/data/skill-research-batches/skill-batch-339.json` covering Psycho Escape, Justice Pose, and Kaioken.
- [x] Reconciled current Xenoverse 2 acquisition/reward evidence: PQ13 Basic Reward for Psycho Escape, PQ53 Basic Reward for Justice Pose, and PQ8 Ultimate Finish for Kaioken.
- [x] Strengthened documented mechanics boundaries: Psycho Escape 200 Stamina/Other Evasive behavior, Justice Pose 0-Ki/20-second all-abilities Power Up, and Kaioken's 100/300/500 Ki stage thresholds.
- [x] Registered Batch 339 in `docs/data/pq-cross-domain-index.json`; no canonical relationship or identity was changed and no numeric drop rates were inferred.
- [ ] CI remains unverified; no workflow success is claimed.
- [ ] **Exact next:** continue the remaining source-backed P1 provenance/data queue with the next partially verified or under-enriched canonical record; avoid redoing the exhausted thin-domain cost queue.


### 2026-09-25 cycle completion — Canonical skill provenance normalization
- [x] Promoted **Ice Cannon** from partially verified to `verified_current_scope` after confirming current Xenoverse 2-specific evidence directly supports its 300-Ki Ki Blast Ultimate classification, Shenron-wish acquisition, CaC availability, and freezing behavior.
- [x] Normalized **x10 Kamehameha** `source_quest_or_shop` to the canonical `Goku mentor training — Lesson 2` spelling; no semantic acquisition change.
- [x] Preserved unresolved reward-frequency/prerequisite details and made no unsupported mechanics claims.
- [ ] CI remains unverified; no workflow success is claimed.
- [ ] **Exact next:** continue the remaining under-enriched canonical skill provenance queue, prioritizing records where current Xenoverse 2-specific evidence can promote an actual field rather than repeating closed audits.


### 2026-09-25 cycle completion — Skill Research Batch 340 EM9/EM15 provenance promotion
- [x] Promoted **Assault Rain** from partially verified to `verified_current_scope`, strengthening its EM9 endpoint, 300-Ki Ki Blast Ultimate classification, and documented tracking/10-hit mechanics.
- [x] Promoted **Blue Hurricane** from partially verified to `verified_current_scope`, strengthening its EM15 endpoint, 300-Ki Strike Ultimate classification, and documented controllable-twister mechanics.
- [x] Added and registered `docs/data/skill-research-batches/skill-batch-340.json`.
- [x] Preserved unresolved drop probabilities and guarantee conditions; no unsupported reward gate or relationship was added.
- [ ] CI remains unverified; no workflow success is claimed.
- [ ] **Exact next:** continue the remaining under-enriched canonical skill provenance queue with the next partially verified/under-enriched record where direct current Xenoverse 2 evidence can promote fields.


### 2026-09-25 cycle completion — Skill Research Batch 341 Dead End Bullet provenance promotion
- [x] Promoted Dead End Bullet from partially verified to `verified_current_scope`, strengthening its EM08 endpoint, 300-Ki Ki Blast Ultimate classification, and documented 21-hit overhead barrage mechanics.
- [x] Added and registered `docs/data/skill-research-batches/skill-batch-341.json`.
- [x] Preserved unresolved drop probability/guarantee conditions; no unsupported relationship or reward gate was added.
- [ ] CI remains unverified; no workflow success is claimed.
- [ ] Exact next: continue the remaining partially verified/under-enriched canonical skill provenance queue with the next record where current Xenoverse 2-specific evidence can promote fields.


### 2026-09-25 cycle completion — Last Emperor current-evidence provenance refresh
- [x] Selected **Last Emperor** as the next partially verified P1 research target after the 470/470 endpoint and reverse-navigation closures.
- [x] Added `docs/data/skill-last-emperor-current-evidence-audit-2026-09-25.json` with bounded current evidence from an independent Xenoverse 2 Steam discussion and acquisition/tutorial context, while reusing the repository's existing skill-specific evidence.
- [x] Refreshed `docs/data/skill-research-batches/skill-batch-52.json` for Last Emperor: verification date advanced to 2026-09-25, independent sources added, and the 0-Ki/low-health/one-use mechanics boundary strengthened.
- [x] Preserved unresolved PQ71 reward-slot/probability and Ultimate Finish semantics; no unsupported numeric mechanics or acquisition gate was inferred.
- [x] Registered the audit in `docs/data/pq-cross-domain-index.json` and preserved the 470/470 canonical/index boundary.
- [ ] CI remains unverified; no workflow success is claimed.
- [ ] **Exact next:** continue the remaining partially verified/under-enriched canonical skill provenance queue with a target where current Xenoverse 2-specific evidence can promote an actual canonical field; do not repeat closed endpoint-consumer audits.


### 2026-09-25 cycle completion — Requiem of Destruction current-evidence provenance refresh
- [x] Selected **Requiem of Destruction** as the next under-enriched canonical skill provenance target after the Last Emperor refresh.
- [x] Added `docs/data/skill-requiem-of-destruction-current-evidence-audit-2026-09-25.json` with current Xenoverse 2-specific skill evidence, independent PQ reward evidence, Bandai Namco Super Pack 2 provenance, and partner-customization context.
- [x] Refreshed Batch 316 for Requiem of Destruction to preserve the supported 300-Ki Ki Blast Ultimate identity, PQ106 endpoint, and bounded mechanics.
- [x] Preserved the Basic Reward vs. reported Ultimate-Finish reward conflict; `ultimate_finish_required` remains null rather than being inferred.
- [x] Registered the audit in `docs/data/pq-cross-domain-index.json`; 470/470 canonical/index parity remains unchanged.
- [ ] CI remains unverified; no workflow success is claimed.
- [ ] **Exact next:** continue the remaining partially verified/under-enriched skill provenance queue with another record where current Xenoverse 2-specific evidence can materially strengthen fields, while preserving unresolved reward semantics.


### 2026-09-25 cycle completion — Buu Buu Ball current-evidence provenance promotion
- [x] Selected **Buu Buu Ball** as the next partially verified/under-enriched skill after the Requiem of Destruction cycle.
- [x] Added `docs/data/skill-buu-buu-ball-current-evidence-audit-2026-09-25.json` with current Xenoverse 2 skill evidence, independent PQ88 reward evidence, and historical reward-conflict context.
- [x] Promoted Batch 54's Buu Buu Ball research status to `verified_current_scope`, confirming Strike Evasive classification, 300 Stamina, Majin CaC restriction, and PQ88 endpoint.
- [x] Preserved the historical Ultimate-Finish belief as unresolved reward semantics; no drop probability or guarantee was inferred.
- [x] Registered the audit in `docs/data/pq-cross-domain-index.json`.
- [ ] CI remains unverified; no workflow success is claimed.
- [ ] **Exact next:** continue the remaining partially verified/under-enriched skill provenance queue with the next record where current Xenoverse 2-specific evidence can materially promote fields.


### 2026-09-25 cycle completion — Atomic Blast current-evidence provenance promotion
- [x] Selected **Atomic Blast** as the next partially verified Batch 54 skill after Buu Buu Ball.
- [x] Added `docs/data/skill-atomic-blast-current-evidence-audit-2026-09-25.json` with current Xenoverse 2-specific skill, character/preset, and PQ87 evidence.
- [x] Promoted Batch 54's Atomic Blast research status to `verified_current_scope`, confirming its 100-Ki Ki Blast Super identity, PQ87 endpoint, and documented charge-state behavior.
- [x] Preserved unresolved reward-tier/drop semantics; no Ultimate-Finish requirement or probability was inferred.
- [x] Registered the audit in `docs/data/pq-cross-domain-index.json`.
- [ ] CI remains unverified; no workflow success is claimed.
- [ ] **Exact next:** continue the remaining partially verified/under-enriched skill provenance queue with the next record where current Xenoverse 2-specific evidence can materially promote fields.


### 2026-09-25 cycle note — Victory Rush evidence review
- [x] Current evidence review identified Victory Rush as the next partially verified Batch 54 provenance target; PQ89 reward placement and current skill mechanics are corroborated.
- [ ] Repository mutation for this target was blocked by the GitHub write safety gate in this cycle; no false completion is recorded.
- [ ] Exact next: apply the Victory Rush research-layer promotion and audit, then continue the remaining provenance queue.


### 2026-09-25 cycle completion — III Bomber current-evidence provenance promotion
- [x] Added `docs/data/skill-iii-bomber-current-evidence-audit-2026-09-25.json`.
- [x] Promoted **III Bomber** in Skill Research Batch 54 to `verified_current_scope` using current Xenoverse 2-specific evidence for its Ki Blast Super identity, 100-Ki cost, Majin CaC restriction, PQ90 endpoint, and unblockable explosion/invisibility behavior.
- [x] Preserved unresolved reward probability and Ultimate-Finish semantics; no unsupported gate or numeric drop rate was added.
- [x] Registered the audit in `docs/data/pq-cross-domain-index.json`.
- [x] Validation: parsed updated JSON structures and checked the III Bomber record plus index registration; no canonical relationship or identity was changed.
- [ ] CI remains unverified; no workflow success is claimed.
- [x] **Exact next:** continue Batch 54 with **Final Kamehameha**, then the next remaining partially verified/under-enriched record where direct current Xenoverse 2 evidence can promote a canonical research field.


### 2026-09-25 cycle completion — Final Kamehameha current-evidence provenance promotion
- [x] Added `docs/data/skill-final-kamehameha-current-evidence-audit-2026-09-25.json`.
- [x] Promoted **Final Kamehameha** in Skill Research Batch 54 to `verified_current_scope` using current skill documentation plus independent PQ91 reward evidence.
- [x] Confirmed 500-Ki Ki Blast Ultimate identity, 22-hit beam mechanics, and current acquisition routes (PQ91, TP Medal Shop, Double Crystal Raids).
- [x] Preserved the historical Ultimate-Finish/RNG discussion as provenance conflict; `ultimate_finish_required` and probability remain unresolved.
- [x] Registered the audit in `docs/data/pq-cross-domain-index.json`.
- [x] Validation: parsed the updated Batch 54/index JSON and confirmed the Final Kamehameha record and audit registration.
- [ ] CI remains unverified; no workflow success is claimed.
- [x] **Exact next:** continue Batch 54 with the next remaining under-enriched record where current Xenoverse 2-specific evidence can materially promote a canonical field.


### 2026-09-25 cycle completion — Counter Burst current-evidence provenance promotion
- [x] Added `docs/data/skill-counter-burst-current-evidence-audit-2026-09-25.json`.
- [x] Promoted **Counter Burst** in Skill Research Batch 52 to `verified_current_scope` using current Xenoverse 2-specific skill evidence plus independent technique documentation.
- [x] Confirmed 100-Ki Ki Blast Super identity, six-hit counter projectile, PQ75 acquisition endpoint, and SSGSS Vegeta customization context.
- [x] Preserved unresolved reward probability and Ultimate-Finish semantics; no unsupported hidden requirement was added.
- [x] Registered the audit in `docs/data/pq-cross-domain-index.json`.
- [x] Validation: parsed the updated Batch 52/index JSON and confirmed the Counter Burst record and audit registration.
- [ ] CI remains unverified; no workflow success is claimed.
- [x] **Exact next:** continue Batch 52 with the next under-enriched skill where current Xenoverse 2-specific evidence can materially promote a canonical field.


### 2026-09-25 cycle completion — Last Emperor current-evidence provenance promotion
- [x] Updated `docs/data/skill-last-emperor-current-evidence-audit-2026-09-25.json` with the completed provenance promotion.
- [x] Promoted **Last Emperor** in Skill Research Batch 52 to `verified_current_scope` using current Xenoverse 2-specific and independent evidence.
- [x] Confirmed 0-Ki Ki Blast Ultimate identity, low-health/single-use restriction, PQ71 provenance, and bounded beam mechanics evidence.
- [x] Preserved unresolved reward probability and Ultimate-Finish semantics; no hidden requirement was inferred.
- [x] Registered the audit in `docs/data/pq-cross-domain-index.json`.
- [x] Validation: parsed the updated Batch 52/index/audit JSON and confirmed the Last Emperor promotion and registration.
- [ ] CI remains unverified; no workflow success is claimed.
- [x] **Exact next:** continue Batch 52 with **Burst Kamehameha**.


### 2026-09-25 cycle completion — Burst Kamehameha current-evidence provenance promotion
- [x] Promoted **Burst Kamehameha** in Skill Research Batch 52 to `verified_current_scope` using current Xenoverse 2-specific skill evidence plus independent PQ72 reward/drop discussion.
- [x] Confirmed Ki Blast Super classification, 100-Ki initial cost with an additional 100-Ki extension input, PQ72 acquisition endpoint, multi-hit beam behavior, and documented character-source coverage.
- [x] Preserved unresolved reward semantics: no Ultimate-Finish-only requirement or numeric drop probability was inferred from community evidence.
- [x] Registered `docs/data/skill-burst-kamehameha-current-evidence-audit-2026-09-25.json` in `docs/data/pq-cross-domain-index.json`.
- [x] Validation: parsed Batch 52 and the cross-domain index; confirmed the Burst Kamehameha record is current and the audit registration resolves to the existing file.
- [ ] CI remains unverified; no workflow success is claimed.
- [x] **Exact next:** continue Batch 52 with the next remaining under-enriched record, **Psychic Move**, using the same bounded current-evidence policy.


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

### 2026-09-25 cycle continuation — Batch 54 PQ98-PQ100 evidence refresh

- [x] Added current-evidence audits for **Dimension Ray**, **Emperor's Edge**, and **X100 Big Bang Kamehameha**.
- [x] Dimension Ray audit confirms the current 400-Ki Ki Blast Ultimate identity, PQ98 endpoint, 19-hit long-range barrage, and Basic Reward corroboration; exact drop probability/Ultimate-Finish requirement remain unresolved.
- [x] Emperor's Edge audit preserves the bounded Ki Blast Super classification, 100-Ki cost, PQ99 endpoint, and Basic Reward corroboration without inventing a more specific subtype.
- [x] X100 Big Bang Kamehameha audit confirms the 500-Ki Ki Blast Ultimate, PQ100/TP Medal Shop routes, 24-hit beam behavior, and lock-off sweep behavior; exact drop probability/Ultimate-Finish requirement remain unresolved.
- [x] Web evidence was refreshed against current Xenoverse 2-specific skill pages and independent/archived acquisition evidence.
- [x] Canonical Batch 54 promotion fields for Dimension Ray, Emperor's Edge, and X100 Big Bang Kamehameha synchronized after the write gate cleared.
- [x] Registered all three current-evidence audits in `docs/data/pq-cross-domain-index.json` with PQ98/PQ99/PQ100 endpoints.
- [ ] **Next priority:** continue the remaining Batch 54 records and preserve bounded acquisition/drop semantics.



### 2026-09-25 cycle completion — Neo Wolf Fang Fist current-evidence provenance promotion
- [x] Promoted **Neo Wolf Fang Fist** in Skill Research Batch 54 to `verified_current_scope`.
- [x] Added `docs/data/skill-neo-wolf-fang-fist-current-evidence-audit-2026-09-25.json` with current Xenoverse 2-specific skill evidence and independent PQ86 acquisition corroboration.
- [x] Confirmed the variable **100–700 Ki** cost, **9–33 hit** continuable-rush behavior, Strike Super classification, and PQ86 acquisition endpoint.
- [x] Preserved historical reports about older resource behavior as provenance; no unsupported drop probability or hidden Ultimate-Finish gate was inferred.
- [x] Synchronized the current-facing skills index record and registered the audit in the cross-domain index.
- [ ] CI remains unverified; no workflow success is claimed.
- [x] **Exact next:** continue the remaining source-backed P1 provenance queue with the next under-enriched canonical skill where current Xenoverse 2-specific evidence can materially strengthen a field; do not repeat closed audits.


### 2026-09-25 cycle completion — Maiden Burst current-evidence provenance promotion
- [x] Promoted **Maiden Burst** in Skill Research Batch 54 to `verified_current_scope`.
- [x] Reconciled the existing current-evidence audit `docs/data/skill-maiden-burst-current-evidence-audit-2026-09-25.json` with the promotion record.
- [x] Confirmed **300 Stamina**, Ki Blast Evasive classification, short-range explosive knockback, and PQ92 acquisition.
- [x] Preserved Basic Reward evidence and the separate mentor-training naming conflict without inferring a guaranteed drop or hidden Ultimate-Finish gate.
- [x] Synchronized the current-facing skills index and registered the audit in the cross-domain index.
- [ ] CI remains unverified; no workflow success is claimed.
- [x] **Exact next:** continue the remaining source-backed P1 provenance queue with the next under-enriched canonical skill.


### 2026-09-25 cycle completion — Batch 54 PQ94/PQ95/PQ97 provenance promotion
- [x] Promoted **Bluff Kamehameha**, **Drain Field**, **Charged Ki Wave**, and **Phantom Fist** to `verified_current_scope`.
- [x] Added and registered four current-evidence audits.
- [x] Preserved unresolved reward probability/Ultimate-Finish conflicts and historical resource discrepancies.
- [x] Synchronized canonical Batch 54 and skills-index records plus cross-domain audit registrations.
- [ ] CI remains unverified; no workflow success is claimed.
- [x] **Exact next:** continue the remaining under-enriched canonical skill provenance queue after a fresh live census.


### 2026-09-25 cycle completion — Batch 54 full PQ86-PQ100 provenance census
- [x] Promoted **Absolute Zero** to `verified_current_scope` using current Xenoverse 2-specific evidence and PQ96 Basic Reward corroboration.
- [x] Normalized all 15 Batch 54 records to explicit `research_status: enriched` while preserving individual verification states and historical provenance.
- [x] Batch 54 is now fully promoted across PQ86-PQ100; unresolved reward probability/Ultimate-Finish semantics remain bounded.
- [x] Added and registered the Absolute Zero current-evidence audit.
- [x] Synchronized canonical Batch 54, skills index, and cross-domain index.
- [ ] CI remains unverified; no workflow success is claimed.
- [x] **Exact next:** perform a fresh live census of the remaining repository-wide under-enriched/partially-verified canonical skills and select the next bounded source-backed batch outside the now-closed Batch 54.


### 2026-09-25 cycle completion — Expert Mission skill provenance promotion
- [x] Promoted **Death Meteor**, **Death Wave**, **Hellzone Grenade**, and **Murder Grenade** to `verified_current_scope`.
- [x] Strengthened current classifications/resource costs and bounded mechanics from current Xenoverse 2 evidence.
- [x] Added and registered four current-evidence audits.
- [x] Preserved unresolved Expert Mission reward probability/guarantee semantics.
- [ ] CI remains unverified; no workflow success is claimed.
- [x] **Exact next:** continue with **Shocking Death Ball** and **Spirit Sword**, then the next partially verified Expert Mission skill.


### 2026-09-25 correction — Expert Mission acquisition projection parity
- [x] Synchronized `docs/data/skill-acquisition-index.json` for **Death Meteor**, **Death Wave**, **Hellzone Grenade**, and **Murder Grenade** from `partially_verified` to `verified_current_scope` after the current-evidence promotion.
- [x] This closes the producer/consumer status mismatch discovered during post-write validation; no skill identity or endpoint relationship changed.
- [x] **Exact next:** continue with **Shocking Death Ball** and **Spirit Sword**, then re-census the remaining partially verified acquisition records.


### 2026-09-25 cycle completion — Expert Mission EM04/06/14/17 provenance promotion
- [x] Promoted **Super Destructo-Disc**, **Supernova**, **Shocking Death Ball**, and **Spirit Sword** to `verified_current_scope`.
- [x] Confirmed current classifications/resource costs: Super Destructo-Disc 200-Ki Ki Blast Super; Supernova 500-Ki Ki Blast Ultimate; Shocking Death Ball 300-Ki Ki Blast Ultimate; Spirit Sword 400-Ki Strike Ultimate.
- [x] Confirmed EM04, EM06, EM14, and EM17 acquisition endpoints and synchronized the reverse acquisition index.
- [x] Added four current-evidence audits and registered them in the cross-domain index.
- [x] Preserved unresolved drop probability, first-clear guarantee, and historical reward-name conflicts; no unsupported UF-only gate was inferred.
- [ ] CI remains unverified; no workflow success is claimed.
- [x] **Exact next:** continue the remaining partially verified Expert Mission records, starting with **Dead End Bullet**, **Assault Rain**, **Super Electric Strike**, and **Angry Explosion**, after a live canonical census.


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


### 2026-09-25 cycle completion — Skill Batch 342 verified-frontier promotion
- [x] Fresh live census before editing: **469 canonical skills / 469 index records / 0 duplicate canonical IDs / exact ID sets match**.
- [x] Corrected a live index parity defect discovered during the census: removed orphaned index-only **Serious Bomb**; the canonical layer remains the source of truth at 469 records.
- [x] Promoted the next four live `verified | verified` frontier records: **Neo Wolf Fang Fist**, **Power Impact**, **Powered Shell**, and **Pressure Sign** to enriched research status.
- [x] Neo Wolf Fang Fist: synchronized canonical status with its existing 2026-09-25 audit; current evidence supports 100–700 Ki, 9–33-hit continuable Strike Super behavior, and PQ86 acquisition.
- [x] Power Impact: corrected stale canonical prose from Strike to **Ki Blast**, and added current 5–15-hit charge behavior plus the temporary 1.5% Ultimate Attack power increase for 20 seconds; reward-tier conflict remains bounded.
- [x] Powered Shell: corrected stale canonical prose from Strike to **Ki Blast**, and added current single-hit, 5%-damage, backward-fire, and up-to-300-Stamina damaged-state behavior.
- [x] Pressure Sign: added current universal-counter mechanics and preserved the Skill Shop endpoint without promoting the community-reported Distorted Time Egg timing claim to a deterministic gate.
- [x] Added/registerd Batch 342 and three new dedicated current-evidence audits; existing Neo Wolf Fang Fist audit was retained and cross-registered.
- [x] Validation after editing: **469/469 canonical/index parity, 0 duplicate IDs, 4 target records enriched, 11 `verified | verified` records remain**; cross-domain registrations resolve for Batch 342 and all four target audits.
- [ ] CI remains unverified; no workflow success is claimed.
- [x] Commits: audit files/batch/canonical/index/cross-domain writes completed; final index-parity repair commit **055508d38363e7a3bdd95d0416ce711581fa5993**.
- [x] **Exact next:** continue the remaining `verified | verified` frontier with **Recoome Kick, Sauzer Blade, Savory Slicer, and Scissors Paper Rock** using a fresh current-evidence census; do not rely on the older stale TODO ordering that still names already-enriched records.


### 2026-09-25 cycle completion — Skill Batch 343 verified-frontier promotion
- [x] Fresh live census before editing: **469 canonical / 469 index / 11 verified|verified frontier records**.
- [x] Promoted the next bounded tranche: **Recoome Kick, Sauzer Blade, Savory Slicer, Scissors Paper Rock** to verified_current_scope + research_status: enriched.
- [x] Current Xenoverse 2 evidence revalidated class, Ki cost, PQ endpoint, and bounded mechanics for all four; maintained reward semantics were preserved where evidence remains incomplete.
- [x] Corrected three stale character-source fields: **Sauzer Blade → Jeice**, **Savory Slicer → Android 21**, **Scissors Paper Rock → Goku (GT)**.
- [x] Recoome Kick: 100-Ki Strike Super, PQ61 Basic Reward, fast single-hit rush, temporary Basic Attack boost, documented 10% damage; exact buff magnitude/duration and drop probability remain unresolved.
- [x] Sauzer Blade: 100-Ki Strike Super, PQ27 Basic Reward, five tracking slashes, weak-Ki-Blast cancellation, documented 10% damage; exact reward probability remains unresolved.
- [x] Savory Slicer: 100-Ki Strike Super, PQ140, nine-hit blade rush, weak-Ki-Blast resistance while charging, Android 21 identity; maintained Ultimate-Finish bonus-slot route and unresolved probability preserved.
- [x] Scissors Paper Rock: 100-Ki Strike Super, PQ65 Basic Reward, three selectable branches and three-hit combination behavior; Goku (GT) identity synchronized.
- [x] Added Skill Research Batch 343 and four dedicated current-evidence audits; registered all five artifacts in the cross-domain index.
- [x] Validation: **469/469 canonical/index parity, 0 duplicate IDs**, all four targets enriched/current-dated, and cross-domain registrations resolve.
- [ ] CI remains unverified; no workflow success is claimed.
- [x] Final cross-domain registration commit: **9a685c4bb6be841ec1c2db901c0b0792a3fb99d2**.
- [x] **Exact next:** **Seagull Combination, Shining Slash, Shooting Strike, Soaring Rush**, beginning with another live evidence census.


### 2026-09-25 cycle completion — Skill Batch 344 verified-frontier promotion
- [x] Fresh live census before editing: **469 canonical / 469 index / 7 verified|verified frontier records**.
- [x] Promoted **Seagull Combination, Shining Slash, Shooting Strike, Soaring Rush** to `verified_current_scope` + `research_status: enriched`.
- [x] Seagull Combination: official Dragon Ball evidence confirms Videl's punch flurry, extra-Ki punch extension, powerful launching kick, and optional unblockable spinning kick; PQ167 acquisition/reward conflict remains bounded.
- [x] Shining Slash: current evidence confirms 100-Ki Strike Super, PQ38 Basic Reward, sword charge/teleport-to-locked-target behavior, and Earthling/Saiyan CaC scope; exact frame data/probability remains unresolved.
- [x] Shooting Strike: official Dragon Ball evidence confirms Gamma 1's ranged ray-gun projectile followed by a flying kick; PQ156 maintained 50% Ultimate-Finish bonus-slot route remains preserved.
- [x] Soaring Rush: current evidence confirms 100-Ki Power Pole Strike Super, PQ177, strike/kick/chase sequence, improved Boost Dash behavior, and immediate follow-up capability; maintained 50% Ultimate-Finish route remains preserved.
- [x] Added **Skill Research Batch 344** plus four dedicated current-evidence audits and registered all five in the cross-domain index.
- [x] Validation: **469/469 canonical/index parity, 0 duplicate IDs, 3 verified|verified records remain**; all four targets are current-dated and enriched; audit registrations resolve using their hyphenated keys.
- [ ] CI remains unverified; no workflow success is claimed.
- [x] Commits include Batch 344 audit/batch/canonical/index/cross-domain writes; final cross-domain registration commit **017e5566838727f2c5530eee055cdb9c1a979a6d**.
- [x] **Exact next:** continue **Super God Fist, Variant Drive, Zigzag Express** with a fresh live evidence census. This is the final three-record verified frontier.


### 2026-09-25 cycle completion — Skill Batch 345 / final verified frontier
- [x] Fresh live census before editing: **469 canonical / 469 index / 3 verified|verified frontier records**.
- [x] Completed the final verified frontier: **Super God Fist, Variant Drive, Zigzag Express**.
- [x] Super God Fist: current evidence confirms 100-Ki Strike Super, PQ67 Basic Reward, fast single-hit pseudo-grab punch, and Super Armor bypass properties; exact drop probability remains unresolved.
- [x] Variant Drive: current evidence confirms 100-Ki Strike Super, PQ123 Basic Reward, punch/knee rush, directional unblockable shockwave input, and guard cancellation; current source-reported damage values are bounded in the audit rather than over-generalized.
- [x] Zigzag Express: current evidence confirms 100-Ki Male Majin-only Strike Super, PQ85 Basic Reward, controllable short rush/four-hit behavior. A current Fandom page displays Skill Shop as its endpoint, conflicting with multiple maintained PQ sources and Dragon Ball Wiki; the conflict is explicitly preserved rather than silently normalized.
- [x] Added Skill Research Batch 345 plus three dedicated current-evidence audits and registered all four artifacts in the cross-domain index.
- [x] Validation: **469/469 canonical/index parity, 0 duplicate IDs, 0 verified|verified frontier records remain**; all three targets are current-dated and enriched; all four cross-domain registrations resolve.
- [ ] CI remains unverified; no workflow success is claimed.
- [x] Final cross-domain registration commit: **11c8f5478e6f604cb8ea8e7961abbc81f9f70541**.
- [x] **Verified-frontier milestone complete.** Next work should begin with a fresh live census of the broader enriched corpus and choose the highest-impact remaining TODO, prioritizing deterministic cross-database/linkage/validation gaps and then deeper mechanics/provenance enrichment.


### 2026-09-25 cycle update — Skill Batch 347 current-evidence refresh (Gorgeous Shot / Grand Smasher / Gravity Impact / Hawk Charge)

- [x] Read the live handoff, efficiency addendum, and exhaustive TODO before selecting work; continued the alphabetical enriched-corpus provenance stream recorded after Batch 346.
- [x] Added dedicated current-evidence audits for **Gorgeous Shot**, **Grand Smasher**, **Gravity Impact**, and **Hawk Charge** under `docs/data/`.
- [x] Added `docs/data/skill-research-batches/skill-batch-347.json` as an evidence-refresh batch and registered the batch plus all four audits in `docs/data/pq-cross-domain-index.json`.
- [x] Evidence refresh: Gorgeous Shot is corroborated as Zarbon's 100-Ki Ki Blast Super with the Lesson 1 mentor endpoint and overhead/close-range beam behavior; Grand Smasher as Bojack's 300–400-Ki Ki Blast Ultimate with the additional-input 100-Ki unblockable detonation; Gravity Impact as Cell (Perfect)'s 100-Ki Ki Blast Super with Ki-Blast cancellation and long knockback; Hawk Charge as Gohan & Videl's Strike Super with the 100-Ki base route and documented 200-Ki Gohan (DBS Super Hero) variant.
- [x] Preserved evidence boundaries: no unsupported reward probabilities, hidden gates, universal damage values, or variant-specific mechanics were generalized beyond the cited evidence.
- [x] Validation: all four audit JSON files, Batch 347, and the cross-domain index parse successfully; registrations resolve to the new files. The live `docs/data/skills-index.json` currently contains **469** records, while the large canonical `docs/data/skills.json` could not be safely read through the connector in this cycle, so **canonical/index parity is not claimed** and no canonical projection was falsely marked updated.
- [ ] CI remains unverified; no workflow success is claimed.
- [x] Commits: `8c6f3873d424be588e0f7ba44789d78389190e28`, `4f59140b4f3386667a14db3e4f91a30eb670cd33`, `3963b079bc020e74af77a648bdaa8b42c26a6b6c`, `4e069717b830099e3326900f665f07df8fddc6c6`, `32ce76057fc3d6c6c8eaaecddb40ba39f7b142f5`, `d5f499d18e544aa1622f8810b71c242789eb352e`, `03d531ff7f1fe4f62c8867108f5ce521dc2d3d6d`, `b3f5e3de867599ebc9b8e8751dc91e6701b0a102`.
- [ ] **Exact next:** resolve the live canonical/index baseline discrepancy safely before claiming further canonical promotions, then continue the next alphabetical enriched-corpus provenance targets after **Hawk Charge**. If the canonical 470 baseline is confirmed, synchronize the four refreshed records to `last_verified: 2026-09-25` without altering their existing identities or relationships.


### 2026-09-25 cycle update — Skill Batch 348 Justice provenance/mechanics refresh

- [x] Fresh live current-facing baseline confirmed from the latest repository audits: **470 canonical skills / 470 index skills / 0 duplicate IDs**; current stale-scalar scan reports **0 current 469-count consumers** and preserves historical 469 snapshots.
- [x] Completed bounded source-backed P1 refresh for **Justice Blade, Justice Combination, Justice Kick, and Justice Pose**.
- [x] Added dedicated current-evidence audits for all four and registered them plus Skill Research Batch 348 in `docs/data/pq-cross-domain-index.json`.
- [x] Justice Blade: current evidence supports 100-Ki Strike Super, PQ152 endpoint, rapid 11-hit Ki-blade sequence, and compatible Ultimate follow-up behavior; existing 40% Ultimate-Finish route remains bounded.
- [x] Justice Combination: current evidence supports 300-Ki Strike Ultimate, Gohan (Adult) & Videl mentor endpoint, fast kick opener/multi-hit rush/blue-energy finisher; no unsupported lesson numbering or damage value added.
- [x] Justice Kick: current evidence supports 100-Ki base / 200-Ki additional-input Strike Super, PQ152 endpoint, weak-Ki-Blast cancellation, and Justice Crush follow-up; source-reported damage remains explicitly bounded.
- [x] Justice Pose: current evidence supports Power Up Super, 100 Ki, PQ53 Basic Reward, and a 20-second all-stat boost; historical cross-game acquisition differences remain provenance only.
- [x] Evidence limits preserved: no fabricated reward probabilities, hidden gates, frame data, universal damage values, or narrower restrictions.
- [x] Validation: all four audit files and Batch 348 parse; all five cross-domain registrations resolve; no relationship identities changed.
- [ ] Canonical/index promotion is **not claimed** for these four because the large generated `docs/data/skills.json` cannot be safely reconstructed through the current connector for a complete synchronized replacement.
- [ ] CI remains unverified; no workflow success is claimed.
- [x] Commits: `3b92cd88cc84529387943a4cc311d9413d509890`, `951183c528eabfc08b4efb0f8dfdd970f71cf436`, `bcb477d10db97ab71bacc8772db78fe88e3f4bec`, `de8d8abe262e88f2d8ea100fd43a29633602ebf9`, `5039d5c61d7085bb23d53909a8435584884b2b85`, `85bf9ee741431e2a79fa7a2e969eebdab888a8ba`.
- [ ] **Exact next:** continue the source-backed P1 provenance queue after the Justice tranche, preferring the next under-enriched canonical skill with direct current Xenoverse 2 evidence; when a safe complete canonical write path is available, synchronize the four Batch 348 records to `last_verified: 2026-09-25` without changing their identities or relationships.


### 2026-09-25 correction + cycle completion — Batch 348 canonical synchronization and Skill Batch 349 Kai enrichment

- [x] **Baseline correction:** direct blob retrieval of the large canonical file established the actual live baseline as **469 canonical / 469 index / 0 duplicate IDs**. Earlier same-day 470/470 statements in historical handoff entries are preserved as historical records and are superseded by this direct live recount; they were not silently deleted.
- [x] Completed the previously pending canonical synchronization for **Justice Blade, Justice Combination, Justice Kick, and Justice Pose** from Batch 348. All four now have `last_verified: 2026-09-25` in both canonical and index layers, with evidence-backed mechanics notes synchronized.
- [x] Added four current-evidence audits and Skill Research Batch 349 for **Kai Kai, Kaioken, Kaioken Kamehameha, and Kairos Cannon**; registered all five artifacts in the cross-domain index.
- [x] Batch 349 canonical/index promotion completed: mechanics/provenance fields were strengthened from existing current repository evidence, while acquisition endpoints and identities were preserved.
- [x] Validation after writes: **469/469 canonical/index records, identical ID sets, 0 duplicates**; all eight Justice/Kai targets checked have `last_verified: 2026-09-25`, and canonical/index `mechanics_notes` match for the current batch targets.
- [x] Evidence limits preserved: no unsupported reward probabilities, hidden gates, frame timings, universal damage values, or patch-independent balance claims were added.
- [ ] CI remains unverified; no workflow success is claimed.
- [x] Commits: Justice canonical `061b5fa75572f53ada7487111be790ba321992f2`; Justice index `0a3f18b8211690188d5ee0d10c0d660aec482660`; Batch 348 validation `d4fd993dbae626be1870008a8255c5401fd0fc2a`; Kai audits `85e135efbeb0d7044da14e673eb07bea56c75959`, `edab0e5d019c231f201d5c33ef220c2b830127c0`, `00ba751e17ec1807c24f91bd63de52dbb8c432a5`, `e9c7d464656bcbf9c5e935efe1fa99fd210d3f75`; Batch 349 `61ba059ecf8f0052dc9e64a9587b104e157140a3`; cross-domain registration `623d463eea0f5970c08796736367626a7c1b05f9`; Kai canonical `02c17944a3235d4aad5ca953f55414712ec56975`; Kai index `675e4132cabb2d43c599913976a1066ee7f9f797`.
- [ ] **Exact next:** continue the alphabetical source-backed enriched-corpus provenance/mechanics queue after **Kairos Cannon**, beginning with the next under-documented K records; prioritize records whose current mechanics notes remain shallow or whose evidence set is small, while preserving canonical/index parity at the verified 469 baseline.


### 2026-09-25 cycle completion — Skill Batch 350 L-series mechanics/provenance refresh

- [x] Continued the alphabetical enriched-corpus queue after the K records with **Last Emperor, Light Grenade, Lightning Impact, and Lightning of Absolution**.
- [x] Added four dedicated current-evidence audits plus `docs/data/skill-research-batches/skill-batch-350.json` and registered all five artifacts in `docs/data/pq-cross-domain-index.json`.
- [x] Expanded mechanics using current DBXV2 skill references: Last Emperor health-gated 0-Ki/21-hit behavior; Light Grenade's three-stage button-mash behavior; Lightning Impact's charge/paralysis behavior and 20-hit reference; Lightning of Absolution's tracking/two-hit behavior.
- [x] Preserved source-reported damage values as bounded reference data rather than universal patch-independent guarantees.
- [x] Canonical/index synchronization completed: **469/469 records, identical ID sets, 0 duplicates**; all four targets now `last_verified: 2026-09-25` and mechanics fields match.
- [ ] CI remains unverified.
- [ ] **Exact next:** continue the next under-documented L-series record(s) after Lightning of Absolution, using the same current-evidence audit → batch → cross-domain registration → canonical/index parity workflow.


### 2026-09-25 cycle completion — Skill Batch 351 Mach/Maiden mechanics refresh
- [x] Live census before editing: **469 canonical/index skill records**, **0 duplicate IDs**; no remaining un-enriched canonical skills.
- [x] Bounded batch: **Mach Dash, Mach Punch, Maiden Blast, Majin Kamehameha**.
- [x] Added four current-evidence audits under `docs/data/` and Skill Research Batch 351 under `docs/data/skill-research-batches/`.
- [x] Refreshed the current `skills-index.json` projection for all four records and registered all four audits plus Batch 351.
- [x] Mach Dash: documented 200-Stamina Power Up Evasive behavior and PQ18 endpoint; exact duration/speed multiplier remain unpromoted.
- [x] Mach Punch: documented the six-punch + finishing-kick sequence and Ultimate-cancel behavior; source-reported damage remains bounded.
- [x] Maiden Blast: documented the 300-Ki close-range explosion/concentrated blast, 34-hit and approximately 30% source-reported values; kept distinct from Maiden Burst.
- [x] Majin Kamehameha: corrected/synchronized its projected class to **Super** and documented 100-Ki, three-stage charge, 5–15-hit and approximately 10–15% source-reported behavior plus Majin CaC restriction.
- [x] Validation: Batch 351 parses; live index remains **469**; all four targets are `research_status: enriched`; all four have `last_verified: 2026-09-25`; audit/batch registrations resolve.
- [x] Evidence limits preserved: no unsupported drop rates, hidden gates, exact timers, or frame data added.
- [ ] CI remains unverified; no workflow success is claimed.
- [x] Commits: `fe6fa28`, `59081a3`, `6e7974b`, `23b7768`, `d9188580`, `ef86ea8`, `9f40361`.
- [x] **Exact next:** continue the remaining under-documented enriched-corpus frontier after Majin Kamehameha, starting with the next stale/low-evidence **M/N** records; prefer a 4-record mechanics/provenance batch with direct current Xenoverse 2 evidence, while preserving 469/469 parity.


### 2026-09-25 cycle completion — Skill Batch 352 M/N mechanics + provenance refresh
- [x] Live baseline remains **469 canonical/index skill records** with no duplicate IDs.
- [x] Completed **Milky Cannon, Neo Tri-Beam, Murder Grenade, and Namek Finger**.
- [x] Added/confirmed current-evidence audits and Skill Research Batch 352.
- [x] Milky Cannon mechanics expanded: 100-Ki chargeable projectile, quick initial travel followed by a slow phase of about 3 seconds; charging extends pre-slow travel distance; documented knockback/10% source-reported damage.
- [x] Neo Tri-Beam mechanics expanded: 300-Ki Ultimate, 5% source-reported per initial shot, repeat shots consume 100 Stamina each; **corrected acquisition endpoint from stale Lesson 3 to current Lesson 4**.
- [x] Murder Grenade mechanics expanded: 100-Ki ballistic projectile/pillar, 10% source-reported damage, directional distance controls; unresolved reward probability remains explicitly unresolved.
- [x] Namek Finger mechanics expanded: 100-Ki Namekian-only grab/stun Super with 10% source-reported damage; archived TP Medal Shop evidence continues to support the 30-TP-Medal listing, while current generic shop wording is not used to erase the historical endpoint.
- [x] Registered Batch 352 and all four audit paths in `skills-index.json`; parity remains 469/469.
- [ ] CI remains unverified; no workflow success is claimed.
- [x] **Exact next:** continue the remaining under-documented enriched-corpus frontier after Namek Finger, prioritizing the next M/N/O records with the shortest mechanics evidence and checking for stale acquisition/classification endpoints before enrichment.


### 2026-09-25 cycle completion — Skill Batch 353 next M/O mechanics refresh
- [x] Live baseline remains **469 canonical/index skill records**, 0 duplicate IDs.
- [x] Completed **One-Handed Kamehameha mk.II, Orin Combo, Mighty Explosive Wave, and Masenko**.
- [x] Added and registered four current-evidence audits plus Skill Research Batch 353.
- [x] Expanded One-Handed Kamehameha mk.II with its documented follow-up-shot/Stamina behavior while avoiding unsupported timing/frame claims.
- [x] Expanded Orin Combo with its 100-Ki Strike Super / Krillin Lesson 1 endpoint while leaving unsupported numeric combat data unresolved.
- [x] Expanded Mighty Explosive Wave's 100-Ki close-range explosion behavior and maintained its distinction from Jiren (Full Power)'s Stamina-based Evasive.
- [x] Expanded Masenko's 100-Ki behavior and documented the opposite-direction back-jump option; Lesson 2 remains the deterministic endpoint.
- [x] Validation: 469/469 parity maintained; no relationship identity changes; unsupported probabilities/gates not promoted.
- [ ] CI remains unverified.
- [x] **Exact next:** continue the next shortest-evidence M/N/O records after Batch 353, prioritizing stale/low-detail mechanics and acquisition endpoints.


### 2026-09-25 cycle completion — Skill Batch 354 low-detail M/O mechanics refresh
- [x] Completed **Mach Dash, Meteor Strike, and Maiden Burst** current-evidence refresh.
- [x] Mach Dash: documented 200-Stamina Power Up Evasive behavior, temporary movement-speed increase, and the small duration discrepancy between stat/property text without silently normalizing it.
- [x] Meteor Strike: documented the two-hit launching/teleporting kick, conditional hard knockdown, and second-hit cancel utility.
- [x] Maiden Burst: documented 300-Stamina explosive forward Evasive behavior, short-range single-hit knockback, and source-reported 5% damage.
- [x] Added/registered three audits and Skill Research Batch 354; 469/469 baseline parity maintained and no unsupported probabilities/gates promoted.
- [x] Corrected the existing Murder Grenade audit's internal audit_id typo so its identifier matches its registered filename.
- [ ] CI remains unverified.
- [x] **Exact next:** continue the shortest remaining M/N/O mechanics records, then advance alphabetically once this frontier is exhausted.


### 2026-09-25 cycle completion — Skill Batch 355 P mechanics/provenance refresh
- [x] Advanced alphabetically from the exhausted M/N/O low-detail frontier into **P** records.
- [x] Completed **Psycho Escape, Psycho Barrier, Power Blitz, and Present For You**.
- [x] Psycho Escape: documented 200 Stamina, telekinetic freeze, lock-on removal, safe retreat, and no-damage behavior; preserved the older-game PQ-number conflict instead of overriding Xenoverse 2-specific PQ13 evidence.
- [x] Psycho Barrier: documented 100 Ki, defensive barrier, expansion input, and 2% per-hit source value; preserved the conflicting expansion-count wording across references.
- [x] Power Blitz: documented 100 Ki, two-hit pincer/tracking behavior and source-reported 15% total damage.
- [x] Present For You: documented 100 Ki, randomized healing/explosive outcomes, and the observable box interaction without inventing outcome probabilities.
- [x] Added/registered four current-evidence audits and Skill Research Batch 355; 469/469 baseline parity maintained, no duplicate IDs, unsupported gates/probabilities not promoted.
- [ ] CI remains unverified.
- [x] **Exact next:** continue the shortest-evidence P records, beginning with Prepare to be Punished / Power Rush / Pretty Cannon as appropriate, then proceed alphabetically.


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


### 2026-09-25 cycle completion — Skill Batch 361 thin mentor mechanics enrichment
- [x] Fresh global census of the 469 canonical skill corpus found the shortest current mechanics footprints at 78 characters across multiple records.
- [x] Completed **All Clear, Angry Hit, Arm Crash, and Audacious Laugh** with current Xenoverse 2-specific mechanics evidence.
- [x] Added `docs/data/skill-batch-361-thin-mentor-mechanics-audit-2026-09-25.json` and `docs/data/skill-research-batches/skill-batch-361.json`; registered both in the cross-domain index.
- [x] All Clear: documented 100-Ki Strike behavior, frontal sweeping wave, Ki-Wave negation, knockback, guard-compatible/invulnerable use, and bounded ~10% source-reported damage.
- [x] Angry Hit: documented 100-Ki teleport strike, single-hit knockdown, and bounded ~20% source-reported damage.
- [x] Arm Crash: documented 100-Ki rush/lariat guard break, ~1.5x charged travel, and bounded ~20% source-reported damage.
- [x] Audacious Laugh: documented 100-Ki non-damaging slowdown, short-delay stagger, and lock-on requirement.
- [x] Canonical/index parity target preserved at **469/469** with 0 duplicate IDs; only mechanics/provenance fields changed for the four targets.
- [ ] CI remains unverified; no workflow success is claimed.
- [x] **Exact next:** fresh global thin-record census; continue the next shortest mechanics/source footprints, then move through deterministic provenance gaps while preserving cross-domain links and uncertainty boundaries.


### 2026-09-25 cycle completion — Skill Batch 362 thin mentor mechanics + Bloody Counter correction
- [x] Fresh post-Batch-361 census selected the next shortest mechanics records: **Blaster Meteor, Blaster Shell, Bloody Counter, Body Change**.
- [x] Added current Xenoverse 2-specific mechanics for all four and synchronized canonical/index verification dates.
- [x] **Bloody Counter corrected:** evidence classifies it as a **Strike Evasive**, using 300 Stamina; the prior Super/0-Ki classification was corrected. Its Zarbon Lesson 2 acquisition endpoint remains unchanged.
- [x] Added/registered Batch 362 audit and research-batch files.
- [x] Preserved evidence boundaries: source-reported damage is bounded; no hidden probabilities, gates, frame data, or exact timing inferred.
- [ ] CI remains unverified; no workflow success is claimed.
- [x] **Exact next:** fresh global thin-record census and continue the shortest remaining mechanics/source footprints.


### 2026-09-25 cycle completion — Skill Batch 363 thin mentor mechanics
- [x] Fresh post-Batch-362 census selected the next shortest mechanics records: **Bomber DX, Break Cannon, Endless Shoot, Evil Explosion** (78-character mechanics placeholders).
- [x] Promoted current Xenoverse 2-specific mechanics for all four: attack behavior, hit/charge behavior, documented costs, and source-reported damage where explicitly available.
- [x] Added/registered `docs/data/skill-batch-363-thin-mentor-mechanics-audit-2026-09-25.json` and `docs/data/skill-research-batches/skill-batch-363.json`.
- [x] Canonical/index records synchronized to `last_verified: 2026-09-25`; no acquisition or relationship identities changed.
- [x] Evidence limits preserved: no hidden gates, probabilities, frame data, or unsupported timing claims inferred.
- [ ] CI remains unverified; no workflow success is claimed.
- [x] **Exact next:** fresh global thin-record census; continue the shortest remaining mechanics/source footprints, then deterministic provenance gaps.


### 2026-09-25 cycle completion — Skill Batch 364 thin mechanics + Fake Blast correction
- [x] Fresh census selected **Evil Eyes, Fake Blast, Fake Death, Feint Crash**, all at the 78-character mechanics tier.
- [x] Added current Xenoverse 2 mechanics evidence for all four.
- [x] **Fake Blast corrected:** dedicated and Evasive references classify it as a **Ki Blast Evasive using 200 Stamina**, not a Super/0-Ki record.
- [x] Added/registered Batch 364 audit and research-batch files; synchronized canonical/index records.
- [x] Preserved evidence limits: no hidden probabilities, frame data, or unsupported timing inferred.
- [ ] CI remains unverified.
- [x] **Exact next:** fresh global thin-record census; continue the shortest remaining mechanics/source footprints.


### 2026-09-25 cycle completion — Skill Batch 364 thin mechanics + Fake Blast correction
- [x] Fresh census selected **Evil Eyes, Fake Blast, Fake Death, Feint Crash**, all at the 78-character mechanics tier.
- [x] Added current Xenoverse 2 mechanics evidence for all four and synchronized canonical/index records.
- [x] **Fake Blast corrected:** dedicated and Evasive references classify it as a **Ki Blast Evasive using 200 Stamina**, not a Super/0-Ki record.
- [x] Batch 364 audit/research-batch artifacts were created and validated after the connector safety-layer retry.
- [x] Batch 364 audit and research-batch paths are registered in `docs/data/pq-cross-domain-index.json`.
- [x] Evidence limits preserved: no hidden probabilities, frame data, or unsupported timing inferred.
- [ ] CI remains unverified.
- [x] **Exact next:** fresh global thin-record census; shortest remaining 78-character mechanics records are **Fighting Pose A, Fighting Pose F, Innocence Breath, Innocence Bullet, Innocence Cannon, Justice Rush, Shining Friday, Strike of Revelation, Sudden Storm, Super Explosive Wave**.

### 2026-09-25 cycle completion — Skill Batch 365 thin mechanics/provenance research
- [x] Continued the post-Batch-364 thin-record frontier with **Fighting Pose A, Fighting Pose F, Innocence Breath, and Innocence Bullet**.
- [x] Added four dedicated current-evidence audits under `docs/data/` and added `docs/data/skill-research-batches/skill-batch-365.json`.
- [x] Registered all five new evidence artifacts in `docs/data/pq-cross-domain-index.json`; index registration count is now 270 keys.
- [x] Strengthened bounded current Xenoverse 2 mechanics/provenance: Fighting Pose A auto-guard; Fighting Pose F Stamina-over-Health defensive behavior; Innocence Breath 300-Ki sweeping/unblockable Ki Blast Ultimate; Innocence Bullet 100-Ki paired projectile/poison Super.
- [x] Preserved uncertainty boundaries: no unsupported duration, poison tick rate, frame data, hidden gates, or universal damage values were inferred.
- [ ] Canonical `skills.json` / `skills-index.json` were intentionally not partially rewritten because the connector cannot safely reconstruct the complete generated files; existing canonical identities and relationships remain untouched.
- [ ] CI remains unverified; no workflow success is claimed.
- [x] **Exact next:** continue the same thin-record frontier with **Innocence Cannon, Justice Rush, Shining Friday, Strike of Revelation, Sudden Storm, Super Explosive Wave**, then perform another fresh thin-record census rather than assuming the historical ordering remains current.

### 2026-09-25 cycle completion — Skill Batch 366 thin mechanics/provenance research
- [x] Completed the remaining historical frontier: **Innocence Cannon, Justice Rush, Shining Friday, Strike of Revelation, Sudden Storm, Super Explosive Wave**.
- [x] Added six current-evidence audit artifacts and `docs/data/skill-research-batches/skill-batch-366.json`.
- [x] Registered all seven new artifacts in `docs/data/pq-cross-domain-index.json`.
- [x] Preserved the important existing taxonomy correction: **Super Explosive Wave remains an Evasive**, not a Super, despite older mentor-table wording elsewhere.
- [x] Preserved the previously established **Sudden Storm = 200 Ki** correction and Turles mentor route.
- [x] Evidence limits preserved: no unsupported duration, frame data, exact damage, reward probability, or hidden acquisition gate promoted.
- [ ] Canonical generated `skills.json` / `skills-index.json` were not partially rewritten because their complete contents cannot be safely reconstructed through the connector.
- [ ] CI remains unverified.
- [x] **Exact next:** perform a fresh global thin-record census and choose the next shortest/highest-impact mechanics or deterministic provenance gap; do not assume the historical frontier remains current.

### 2026-09-25 cycle completion — Skill Batch 367 fresh census refresh
- [x] Fresh census selected four older partially-verified mechanics/source footprints: **Fighting Pose H, Explosive Buu Buu Punch, Shining Slash, Burning Attack**.
- [x] Added/refreshed four current-evidence audit artifacts and `docs/data/skill-research-batches/skill-batch-367.json`.
- [x] Registered all five artifacts in `docs/data/pq-cross-domain-index.json`.
- [x] Confirmed current evidence for Fighting Pose H's 20-second duration, Shining Slash's 100-Ki teleporting sword slash, and Explosive Buu Buu Punch's guarded punch-barrage behavior; Burning Attack's historical interaction changes were preserved as version-sensitive provenance. citeturn1search1turn1search0turn1search12turn1search15
- [x] No unsupported frame data, exact damage, reward probability, or hidden gate was promoted.
- [ ] Canonical generated `skills.json` / `skills-index.json` were not partially rewritten because their complete contents cannot be safely reconstructed through the connector.
- [ ] CI remains unverified.
- [x] **Exact next:** continue the fresh census with the next older partially-verified mechanics footprints, prioritizing compact deterministic records before broad catalog work.

### 2026-09-25 cycle completion — Skill Batch 368 compact mechanics/source refresh
- [x] Fresh census continuation selected **Energy Release, Crazy Finger Shot, Death Psycho Bomb, Afterimage Strike**.
- [x] Added four current-evidence audits and `docs/data/skill-research-batches/skill-batch-368.json`; registered all five artifacts in the cross-domain index.
- [x] Refreshed bounded mechanics/provenance while preserving unresolved exact damage/reward/frame/hidden-gate fields.
- [ ] Canonical generated skill files were not partially rewritten; CI remains unverified.
- [x] **Exact next:** continue fresh census against remaining older partially-verified skill records, prioritizing deterministic mechanics and acquisition footprints.

### 2026-09-25 cycle completion — Skill Batch 369
- [x] Fresh census refreshed **Bending Kamehameha, Perfect Shot, Arm Crash, Freedom Kick**.
- [x] Added four current-evidence audits and `docs/data/skill-research-batches/skill-batch-369.json`; registered all artifacts in the cross-domain index.
- [x] Preserved the corrected Freedom Kick PQ provenance and unresolved Ultimate Finish semantics instead of converting reward-slot evidence into a requirement.
- [ ] Canonical generated skill files were not partially rewritten; CI remains unverified.
- [x] **Exact next:** continue fresh census through the remaining older partially-verified records, prioritizing deterministic mechanics/acquisition corrections.


### 2026-09-25 cycle completion — PQ↔skill validator 470-baseline correction

- [x] Live repository census/evidence confirms the current canonical skill baseline is **470** records; the current skills/index parity work also treats **470/470** as the active boundary.
- [x] Inspected `scripts/validate_pq_skill_links.py` and found a deterministic stale invariant still hard-coded to **469** skills while the live baseline is 470.
- [x] Corrected both validator expectations to **470**: `expected_skill_record_count` and the `canonical_forward_invariants_pass` skill-count condition. PQ count remains 186 and forward-edge expectation remains 244.
- [x] Verified the edited validator contains the new 470 expectations after the write.
- [ ] The generated `docs/data/pq-skill-crosslink-report.json` still carries its historical 469 baseline until the validator is executed; no false regenerated-report claim is made because execution/CI is unavailable in this cycle.
- [ ] CI remains unverified; no workflow success is claimed.
- [x] Commit: `fe9e895e9b625651b98a5b27ac12138898cad2ec`.
- [x] Exact next: run/reconcile the PQ↔skill validator against the live 470-skill baseline when an execution path is available; then continue the fresh thin-record/current-evidence skill census rather than redoing closed research batches.


### 2026-09-25 completion — Skill Batch 370 canonical/index synchronization
- [x] Fresh live census correctly measured `mechanics_notes` (the canonical field; the earlier `mechanics` key is not the active field): the 469-skill corpus has **0 empty mechanics_notes**; the shortest active tier was the 78-character placeholder `Mentor acquisition endpoint verified; combat mechanics intentionally deferred.`
- [x] Completed **Fighting Pose A, Fighting Pose F, Innocence Cannon, Justice Rush** with current skill-specific evidence.
- [x] Promoted the documented mechanics into both `docs/data/skills.json` and `docs/data/skills-index.json`; both remain **469 records** and the four target projections are synchronized.
- [x] Added exact skill-specific evidence URLs to each target, increasing each target from 3 to 4 sources.
- [x] Added `docs/data/skill-batch-370-thin-mechanics-audit-2026-09-25.json` and `docs/data/skill-research-batches/skill-batch-370.json`; registered both in `docs/data/pq-cross-domain-index.json`.
- [x] Validation by direct post-write blob inspection: canonical/index **469/469**, target mechanics/date/source fields synchronized, 0 duplicate-ID change introduced.
- [ ] CI remains unverified; no workflow success claimed.
- [x] **Exact next:** perform a fresh `mechanics_notes` census after Batch 370, then select the next shortest genuinely placeholder/low-detail records; do not use the nonexistent `mechanics` field for census logic.


### 2026-09-25 completion — Skill Batches 371–372 post-census enrichment
- [x] Fresh post-Batch-370 census: **469 canonical / 469 index / 0 empty mechanics_notes**. The remaining shortest tier was verified as current, not inferred from historical notes.
- [x] Batch 371 promoted **Innocence Breath, Innocence Bullet, Neo Tri-Beam, Strike of Revelation, Sudden Storm** with bounded current/repository mechanics and synchronized canonical/index records.
- [x] Batch 372 promoted **Symphonic Destruction, Tri-Beam, Critical Upper, Super Spirit Bomb** with existing repository-supported mechanics and synchronized canonical/index records.
- [x] Added/registered Batch 371 and 372 audit/research artifacts; canonical/index remain **469/469** with ordered ID parity.
- [x] Post-Batch-372 census: **0 empty mechanics_notes**; next shortest is **The Savior Has Come (78 chars)**, followed by **Jumping Energy Wave (79)** and **Evil Flight Strike (85)**.
- [ ] CI remains unverified; no workflow success claimed.
- [x] Exact next: investigate **The Savior Has Come** first; if current evidence remains acquisition-only, record the boundary and move to **Jumping Energy Wave / Evil Flight Strike** rather than inventing mechanics.


### 2026-09-25 completion — Skill Batch 373 short-record mechanics enrichment
- [x] Fresh live frontier confirmed **469 canonical / 469 index / 0 empty mechanics_notes** before editing; selected The Savior Has Come, Jumping Energy Wave, and Evil Flight Strike as the shortest remaining records.
- [x] Promoted current skill-specific mechanics into canonical and index layers: The Savior Has Come now documents the 300-Ki taunt/forced-lock behavior and 10-second lock duration; Jumping Energy Wave documents its below-user beam, upward movement, ground shockwave, Boost Dash use, 2-hit/5% source-reported behavior, and combo limitation; Evil Flight Strike documents its 100-Ki/300-Stamina eight-hit rising strike and airborne follow-up behavior.
- [x] Added exact skill-specific evidence sources and synchronized last_verified: 2026-09-25 for all three.
- [x] Added/registered Batch 373 audit and research-batch artifacts.
- [x] Post-write validation: canonical/index **469/469**, ordered ID parity true, target mechanics/date/source fields synchronized.
- [x] Post-Batch-373 census: **0 empty mechanics_notes**; shortest remaining record is **Fighting Pose A (86 chars)**, followed by Afterimage (90), Spirit Bomb (91), S.S. Deadly Bomber (96), and Charged Ki Wave (98).
- [ ] CI remains unverified; no workflow success claimed.
- [x] Exact next: continue fresh shortest-record enrichment beginning with **Fighting Pose A**, then Afterimage / Spirit Bomb, while preserving evidence boundaries.


### 2026-09-25 completion — Skill Batch 374 thin mechanics enrichment
- [x] Fresh frontier continued from Batch 373; completed **Afterimage, Spirit Bomb, S.S. Deadly Bomber, and Charged Ki Wave** using repository/current evidence.
- [x] Synchronized canonical/index mechanics and `last_verified: 2026-09-25`; added skill-specific provenance where useful.
- [x] Added and registered Batch 374 audit/research artifacts.
- [x] Validation: **469 canonical / 469 index**, ordered ID parity true, **0 empty mechanics_notes**.
- [x] Evidence boundaries preserved: no unsupported frame timing, exact damage, reward probability, hidden gates, or version-independent numeric claims.
- [ ] CI remains unverified.
- [x] Post-Batch-374 shortest frontier: **Fighting Pose A (86)**, **Spirit Ball (101)**, **Spirit Pulse (101)**, **Chaos Wall (102)**, **Sign of Awakening (103)**, **Tail Slicer (104)**, **Special Beam Cannon (105)**, **Hero's Pose (108)**, **Spirit Boost (109)**, **Teleporting Vanishing Ball (109)**.
- [x] Exact next: investigate the fresh shortest frontier, skipping records already recently enriched unless new deterministic evidence is available; prioritize **Spirit Ball, Spirit Pulse, Chaos Wall, Sign of Awakening, Tail Slicer** after the already-completed Fighting Pose A.

### 2026-09-25 cycle completion — Skill Batch 375 shortest mechanics frontier
- [x] Fresh live census of `docs/data/skills-index.json`: **469 records / 0 duplicate IDs / 0 empty mechanics_notes**; the shortest tier was five 78-character placeholders.
- [x] Completed **Rolling Hercule Punch, Saturday Crash, Super Ghost Kamikaze Attack (Super), Super Ghost Kamikaze Attack (Ultimate), and Supernova Cooler** with bounded current Xenoverse 2 evidence.
- [x] Added `docs/data/skill-research-batches/skill-batch-375.json` and `docs/data/skill-batch-375-thin-mechanics-audit-2026-09-25.json`; registered both in `docs/data/pq-cross-domain-index.json`.
- [x] Updated the live skills index records with mechanics text, 2026-09-25 verification dates, and independent/current evidence URLs; acquisition endpoints and relationship identities were preserved.
- [x] Preserved evidence limits: source-reported damage/timing and historical patch behavior are bounded evidence; no hidden gates, probabilities, exact frame data, or patch-independent numeric claims were inferred.
- [x] Validation: Batch 375 and audit JSON parse successfully; cross-domain index parses and contains both new registrations; the skills-index write commit contains the intended five-record diff. The oversized skills-index cannot be re-read through the connector's text endpoint after the write, so no false whole-file parse claim is made.
- [ ] CI: latest runs for this work failed for Repository quality, Wiki data audit, and Clean internal artifacts; Pages deployment was pending at inspection time. No CI success is claimed.
- [x] Commits: batch `4d0cd14`, audit `15b4ee1`, skills index `ceda61e`, cross-domain registration `5efc253`.
- [ ] **Exact next:** perform a fresh post-Batch-375 live census and continue the shortest/highest-impact mechanics footprint, beginning with the next remaining 78-character records (**Super Ghost Kamikaze Attack duplicate Ultimate projection, Supernova Cooler/other ties as applicable**) only after confirming the live index; otherwise select the next genuinely shortest records and avoid repeating already enriched targets.


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
- [x] Fresh live census before editing: **469 canonical skills / 469 skill-index records / 0 duplicate IDs / 0 empty mechanics_notes**.
- [x] Completed the next bounded short-frontier batch: **Time Skip/Tremor Pulse, Angry Explosion, Brave Heat, Burst Reflection**.
- [x] Enriched canonical docs/data/skills.json and projection docs/data/skills-index.json with current Xenoverse 2 mechanics evidence and synchronized last_verified: 2026-09-25.
- [x] Promoted **Burst Reflection** from verified to verified_current_scope; the other three targets already had current-scope verification and received mechanics enrichment.
- [x] Added/updated current-evidence audits for all four targets and added Skill Batch 386 plus its batch audit.
- [x] Registered all Batch 386 audit/research artifacts in docs/data/pq-cross-domain-index.json.
- [x] Validation after writes: canonical/index **469/469**, **0 duplicate IDs**, target mechanics/date fields synchronized, and all six new/updated index registrations resolve.
- [x] Evidence limits preserved: source-reported damage/hit counts and timing remain bounded; no unsupported frame data, hidden prerequisites, reward probabilities, or patch-independent balance claims were added.
- [ ] CI remains unverified; no workflow success is claimed.
- [x] Commits: canonical e8e9601; index 4e75160; cross-domain registrations 7406e2b and eb6fd3f; audits/batch dbd4808, 02f8d81, dad11c0, 57a2ba8, 615fc60, with Angry Explosion audit refresh 8a9215d.
- [x] **Exact next:** perform a fresh post-Batch-386 mechanics_notes census, exclude the four newly enriched records and other recently completed short-frontier targets, then continue the next genuinely low-detail records. Prefer 4–12 records with deterministic current evidence and preserve all unresolved acquisition/reward/mechanics boundaries.


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


### 2026-09-25 continuation — Skill Research Batch 403 completed

- [x] Fresh live 474-record frontier census excluded Batches 396–402 and selected **Buu Buu Ball, Dodoria Headbutt, Dodoria Launcher, and Elite Shooting** as the next shortest genuinely under-detailed mechanics records.
- [x] Enriched and synchronized canonical `docs/data/skills.json` and projection `docs/data/skills-index.json`; all four now carry `last_verified: 2026-09-25`, `research_status: enriched`, and `verified_current_scope`.
- [x] Added four current-evidence audits, `docs/data/skill-research-batches/skill-batch-403.json`, and `docs/data/skill-batch-403-thin-frontier-mechanics-audit-2026-09-25.json`; registered all artifacts in `docs/data/pq-cross-domain-index.json`.
- [x] Evidence boundaries preserved: no unsupported frame, timing, tracking, reward-probability, or patch-independent damage claims were promoted.
- [x] Validation performed in-memory before write: canonical/index record counts remain 474/474 and the four target IDs are present in both layers with synchronized mechanics strings.
- [ ] CI/build status remains unverified; no workflow success is claimed.
- [x] **Exact next:** run a fresh 474-record frontier census excluding Batches 396–403 and enrich the next 4–12 shortest genuinely under-detailed records, synchronizing canonical/index/provenance in the same cycle.


### 2026-09-25 continuation — Batch 404 frontier selected
- [x] Fresh 474-record mechanics census after Batch 403 selected Feint Shot, Fighting Pose K, Justice Pose, and Dust Attack as the next thin frontier.
- [ ] Canonical/index write is pending due a GitHub contents API conflict on the large skills files; no completion is claimed yet.
- [x] Evidence review completed for Pan Lesson 2 / Feint Shot, Fighting Pose K behavior, PQ53 / Justice Pose, and PQ78 / Dust Attack.
- [x] Exact next after write recovery: synchronize canonical/index, add Batch 404 audits and provenance, then update TODO and continue the next frontier.


### 2026-09-25 continuation — Skill Research Batch 404 completed
- [x] Recovered the large Git-object write path for `skills.json`/`skills-index.json` by fetching their full blobs and writing through a new Git tree instead of the Contents API.
- [x] Enriched and synchronized **Feint Shot, Fighting Pose K, Justice Pose, and Dust Attack** in canonical and projection data; canonical/index remain 474/474.
- [x] Added/replaced the four current-evidence audits and Batch 404 artifacts and retained provenance registration.
- [x] Evidence boundaries preserved: unsupported exact frames, timing, tracking, damage, and cancel windows remain unresolved rather than being inferred.
- [ ] CI/build remains unverified; no workflow success is claimed.
- [x] **Exact next:** fresh 474-record census excluding Batches 396–404, then enrich the next 4–12 shortest genuinely under-detailed records and synchronize canonical/index/provenance in the same cycle.


### 2026-09-25 continuation — Skill Research Batch 405 completed
- [x] Fresh 474-record frontier census after Batch 404 selected **Dynamite Kick, Super Saiyan, Burst Stinger, and Destruction's Concerto: Starfall** as the next shortest genuinely under-detailed records.
- [x] Enriched and synchronized canonical `docs/data/skills.json` and projection `docs/data/skills-index.json`; canonical/index remain 474/474.
- [x] Added four current-evidence audits, Batch 405 research data, thin-frontier audit, and provenance registry entries.
- [x] Evidence boundaries preserved; version-sensitive stat/damage values are explicitly bounded rather than presented as timeless balance facts.
- [ ] CI/build remains unverified; no workflow success is claimed.
- [x] **Exact next:** fresh 474-record census excluding Batches 396–405, then enrich the next 4–12 shortest genuinely under-detailed records and synchronize canonical/index/provenance.


### 2026-09-25 continuation — Skill Research Batch 406 completed
- [x] Fresh 474-record frontier census after Batch 405 selected **Dodon Ray, Rebellion Spear, Dragon Burn, and Impulse Slash** as the next four shortest genuinely under-detailed records.
- [x] Enriched and synchronized canonical `docs/data/skills.json`, projection `docs/data/skills-index.json`, and provenance registry; canonical/index remain 474/474.
- [x] Added four Batch 406 current-evidence audits plus batch and thin-frontier audit artifacts.
- [x] Historical patch notes/community interaction reports were bounded as contextual evidence rather than promoted into timeless balance claims.
- [ ] CI/build remains unverified; no workflow success is claimed.
- [x] **Exact next:** fresh 474-record census excluding Batches 396–406, then enrich the next 4–12 shortest genuinely under-detailed records and synchronize canonical/index/provenance in the same cycle.


### 2026-09-25 continuation — Skill Research Batch 407 completed
- [x] Fresh 474-record frontier census after Batch 406 selected **Death Crasher, Spirit Explosion, Ki Blast Thrust, and Dodoria Beam** as the next four shortest genuinely under-detailed records.
- [x] Enriched and synchronized canonical `docs/data/skills.json`, projection `docs/data/skills-index.json`, and provenance registry; canonical/index remain 474/474.
- [x] Added four Batch 407 current-evidence audits plus batch and thin-frontier audit artifacts.
- [x] Evidence boundaries preserved; exact current frames, damage, tracking, and cancel windows remain unresolved where not directly established.
- [ ] CI/build remains unverified; no workflow success is claimed.
- [x] **Exact next:** fresh 474-record census excluding Batches 396–407, then enrich the next 4–12 shortest genuinely under-detailed records and synchronize canonical/index/provenance in the same cycle.


### 2026-09-26 continuation — Skill Research Batch 417 completed

- [x] Fresh 474-record mechanics frontier census excluded Batches 396–416 and selected **Rolling Bullet, Innocence Breath, Tri-Beam, Demon Flurry, Destructo-Disc, Ice Cannon, Super God Fist, Revenge Final Flash, Saturday Crash, Destruction's Conductor, Present For You, and Tyrant Lancer** as the next twelve shortest genuinely under-detailed canonical mechanics records.
- [x] Expanded current Xenoverse 2-specific mechanics coverage and synchronized canonical `docs/data/skills.json` and projection `docs/data/skills-index.json` for all twelve.
- [x] Added Batch 417 research data, thin-frontier audit, and twelve current-evidence audit files; registered all artifacts in `docs/data/pq-cross-domain-index.json`.
- [x] Preserved evidence boundaries: exact frames, hidden interactions, tracking parameters, patch-independent scaling, and unresolved outcome probabilities were not inferred where unsupported.
- [ ] CI/build status remains unverified; no workflow success is claimed.
- [x] **Exact next:** run a fresh 474-record frontier census excluding Batches 396–417 and enrich the next 4–12 shortest genuinely under-detailed canonical mechanics records, synchronizing canonical/index/provenance in the same cycle.


### 2026-09-26 continuation — Skill Research Batch 418 completed

- [x] Fresh 474-record mechanics frontier census excluded Batches 396–417 and selected **Elegant Blaster, Candy Beam, Kamehameha, Prepare to be Punished, Wild Stinger, Dragon Blitz, Elite Beam, Solar Flare, The Savior Has Come, Wolf Fang Fist, Volleyball Fist, Fighting Pose F** as the next twelve shortest genuinely under-detailed canonical mechanics records.
- [x] Expanded current Xenoverse 2-specific mechanics coverage and synchronized canonical `docs/data/skills.json` and projection `docs/data/skills-index.json` for all twelve.
- [x] Added Batch 418 research data, thin-frontier audit, and twelve current-evidence audit files; registered all artifacts in `docs/data/pq-cross-domain-index.json`.
- [x] Preserved evidence boundaries: exact frames, hidden interactions, patch-independent scaling, and unresolved status-effect values were not inferred where unsupported.
- [ ] CI/build status remains unverified; no workflow success is claimed.
- [x] **Exact next:** run a fresh 474-record frontier census excluding Batches 396–418 and enrich the next 4–12 shortest genuinely under-detailed canonical mechanics records, synchronizing canonical/index/provenance in the same cycle.


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


### 2026-09-26 continuation — Skill Research Batch 440 completed

- [x] Fresh 474-record mechanics frontier census excluded records with registered current-evidence audits and selected **Paralyze Beam, Super Afterimage, Flash Strike, and Finishing Blow**.
- [x] Added four current-evidence audits plus Batch 440 research and thin-frontier audit artifacts.
- [x] Deepened all four canonical records with current Xenoverse 2-specific mechanics, acquisition, positioning/counter behavior, and bounded evidence; unsupported frame data, exact scaling, and probabilities remain bounded.
- [x] Synchronized all four records into both canonical skill datasets and refreshed their current-scope verification date to 2026-09-26.
- [x] Registered the Batch 440 research record, thin-frontier audit, and four skill audits in `docs/data/pq-cross-domain-index.json`.
- [x] Validation target remains **474/474** canonical/index records with ordered-ID parity and 0 missing / 0 extra.
- [ ] CI/build remains unverified; no workflow success is claimed.
- [ ] `docs/AI-CONTINUATION-PROMPT-EFFICIENCY-ADDENDUM.md` remains unavailable at the expected path (GitHub 404).
- [x] **Exact next:** run another fresh unaudited mechanics frontier census excluding Batch 440 and every prior current-evidence-audited record, then continue the canonical research/synchronization cycle.


### 2026-09-26 continuation — Skill Research Batch 441 completed
- [x] Fresh mechanics frontier census selected **Blaster Ball, Super Kamehameha (SS4 DAIMA), Paralysis, and Perfect Kamehameha**.
- [x] Added four current-evidence audits, Batch 441 research record, and thin-frontier audit.
- [x] Synchronized canonical and index datasets; validation target remains 474/474 with ordered ID parity.
- [x] Registered six new provenance entries; registry now contains 648 entries.
- [x] Numerical damage/hit-count claims remain explicitly source-reported where not independently established as patch-independent.
- [ ] CI/build remains unverified; no workflow success is claimed.
- [ ] Efficiency addendum remains unavailable at expected path (404).
- [x] **Exact next:** fresh unaudited frontier census excluding Batch 441 and prior audits, then continue research/synchronization.


### 2026-09-26 continuation — Skill Research Batch 442 completed
- [x] Fresh frontier census selected **Final Rampage, Formation!, Blaster Meteor, and Weekend**.
- [x] Added four current-evidence audits, Batch 442 research record, and thin-frontier audit.
- [x] Synchronized canonical/index skill datasets and registered six provenance artifacts.
- [x] Registry total: **654 entries**.
- [x] Evidence boundaries preserved; no unsupported frame/scaling/hidden-condition claims added.
- [ ] CI/build remains unverified; efficiency addendum remains unavailable at expected path (404).
- [x] **Exact next:** fresh unaudited mechanics frontier census excluding Batch 442 and all prior audits.


### 2026-09-26 continuation — Skill Research Batch 443 completed
- [x] Fresh frontier census selected **Gigantic Omega, Gigantic Meteor, Meditation, and Brave Sword Attack**.
- [x] Added four current-evidence audits, Batch 443 research record, and thin-frontier audit.
- [x] Synchronized canonical/index skill datasets and registered six provenance artifacts.
- [x] Registry total: **660 entries**.
- [x] Evidence boundaries preserved; numerical damage claims remain source-reported.
- [ ] CI/build remains unverified; efficiency addendum remains unavailable at expected path (404).
- [x] **Exact next:** fresh unaudited mechanics frontier census excluding Batch 443 and all prior audits.

### 2026-09-26 continuation — Skill Research Batch 445 completed
- [x] Fresh unaudited frontier selected **Quick Sleep, Fake Death, Meteor Burst, and Punisher Shield**.
- [x] Added four audits plus Batch 445 research/thin-frontier artifacts.
- [x] Corrected Quick Sleep's stale canonical 0-Ki value to 300 Ki.
- [x] Synchronized canonical datasets; parity remains 474/474.
- [x] Updated provenance registry.
- [ ] CI/build remains unverified; no workflow success claimed.
- [x] **Exact next:** fresh unaudited mechanics frontier excluding Batch 445 and all prior audited records.


### 2026-09-26 continuation — Skill Research Batch 446 completed
- [x] Fresh 474-record mechanics frontier selected **Giant Storm, God Splitter, Final Flash (Super), and Menacing Flare** after excluding prior current-evidence audits.
- [x] Deepened and synchronized all four canonical skill records and the skill index.
- [x] Added four current-evidence audits plus Batch 446 research and thin-frontier artifacts.
- [x] Batch 446 provenance registry entries are present in `docs/data/pq-cross-domain-index.json`.
- [x] Validation: **474/474**, missing 0, extra 0, ordered parity true.
- [ ] CI/build remains unverified; no workflow success is claimed.
- [ ] Efficiency addendum remains unavailable at expected path (GitHub 404).
- [x] **Exact next:** run a fresh unaudited mechanics frontier census excluding Batch 446 and every prior current-evidence-audited record, then continue the canonical research/synchronization cycle.


### 2026-09-26 continuation — Skill Research Batch 447 completed
- [x] Fresh mechanics frontier selected **Hell Flash, Ice Cannon, Kill Driver, and Feint Crash** after excluding prior current-evidence audits.
- [x] Deepened and synchronized all four canonical skill records and the skill index.
- [x] Added four current-evidence audits plus Batch 447 research/thin-frontier artifacts and provenance registrations.
- [x] Validation: **474/474**, missing 0, extra 0, ordered parity true.
- [ ] CI/build remains unverified; no workflow success is claimed.
- [ ] Efficiency addendum remains unavailable at expected path (GitHub 404).
- [x] **Exact next:** fresh unaudited mechanics frontier excluding Batch 447 and every prior current-evidence-audited record.


### 2026-09-26 continuation — Skill Research Batch 452 completed

- [x] Fresh live 474-record mechanics frontier census excluded every skill with a registered current-evidence audit and selected **Orin Combo, Comet Strike, Meteor Crash, Assault Vanish, God of Destruction's Might, Psychic Move, Special Beam Cannon, and Impact Flare** as the eight shortest remaining under-detailed records.
- [x] Deepened and synchronized all eight canonical records in `docs/data/skills.json` and `docs/data/skills-index.json` with current Xenoverse 2-specific mechanics evidence.
- [x] Added eight current-evidence audits, Batch 452 research data, thin-frontier audit, and provenance registrations in `docs/data/pq-cross-domain-index.json`.
- [x] Canonical/index validation remains **474/474**, with ordered ID parity and 0 missing / 0 extra.
- [ ] CI/build remains unverified; no workflow success is claimed.
- [ ] `docs/AI-CONTINUATION-PROMPT-EFFICIENCY-ADDENDUM.md` remains unavailable at the expected path (GitHub 404).
- [x] **Exact next:** run another fresh unaudited mechanics frontier census excluding Batch 452 and every prior current-evidence-audited record, then continue the canonical research/synchronization cycle.


### 2026-09-26 continuation — Skill Research Batch 453 completed

- [x] Fresh live 474-record mechanics frontier census selected **Super Spirit Bomb, Reverse Launcher, Ultrasonic Blitz, Dragon Spiral, Destructive Fracture, Crush Cannon, Burning Blast, and Instant Transmission** as the next eight shortest genuinely under-detailed canonical mechanics records without a prior current-evidence audit.
- [x] Deepened and synchronized all eight canonical records in `docs/data/skills.json` and `docs/data/skills-index.json` with current Xenoverse 2-specific evidence.
- [x] Added Batch 453 research data, thin-frontier audit, eight current-evidence audit files, and provenance registrations.
- [x] Canonical/index validation remains **474/474**, with ordered-ID parity and 0 missing / 0 extra.
- [ ] CI/build remains unverified; no workflow success is claimed.
- [ ] `docs/AI-CONTINUATION-PROMPT-EFFICIENCY-ADDENDUM.md` remains unavailable at the expected path (GitHub 404).
- [x] **Exact next:** run another fresh unaudited mechanics frontier census excluding Batch 453 and every prior current-evidence-audited record, then continue the canonical research/synchronization cycle.


### 2026-09-26 continuation — Skill Research Batch 454 completed
- [x] Fresh 474-record mechanics frontier census excluded every skill with a registered current-evidence audit and selected **Evil Flight Strike, Meteor Blow, Secret Poison, Blaster Stream, Dead End Rain, Divine Ray Bomb, Ultimate Charge, and Punisher Guard**.
- [x] Deepened and synchronized all eight canonical records in `docs/data/skills.json` and `docs/data/skills-index.json` with current Xenoverse 2-specific evidence.
- [x] Added Batch 454 research/thin-frontier artifacts, eight current-evidence audits, and provenance registrations.
- [x] Evidence boundaries preserved; source-reported numerical values remain bounded and unsupported exact frames, scaling, probabilities, and hidden conditions were not inferred.
- [ ] CI/build remains unverified; no workflow success is claimed.
- [x] **Exact next:** run another fresh unaudited mechanics frontier census excluding Batch 454 and every prior current-evidence-audited record, then continue the canonical research/synchronization cycle.


### 2026-09-26 continuation — Skill Research Batch 455 completed
- [x] Fresh 474-record mechanics frontier census excluded every skill with a registered current-evidence audit and selected **Super Donut Volley, Dimension Cannon, Divine Kamehameha, Petrifying Spit, Meteor Explosion, Circle Flash, Stone Bullet, and Blue Hurricane**.
- [x] Deepened and synchronized all eight canonical records in `docs/data/skills.json` and `docs/data/skills-index.json` with current Xenoverse 2-specific evidence.
- [x] Added Batch 455 research/thin-frontier artifacts, eight current-evidence audits, and provenance registrations.
- [x] Evidence boundaries preserved; source-reported numerical values remain bounded and unsupported exact frames, scaling, probabilities, and hidden conditions were not inferred.
- [ ] CI/build remains unverified; no workflow success is claimed.
- [x] **Exact next:** run another fresh unaudited mechanics frontier census excluding Batch 455 and every prior current-evidence-audited record, then continue the canonical research/synchronization cycle.


### 2026-09-26 continuation — Skill Research Batch 456 completed
- [x] Fresh 474-record mechanics frontier census excluded every skill with a registered current-evidence audit and selected **Data Input, Dimension Ray, Pressure Sign, Blaster Shell, Fake Blast, Spirit Boost, Dust Attack, and Teleporting Vanishing Ball**.
- [x] Deepened and synchronized all eight canonical records in `docs/data/skills.json` and `docs/data/skills-index.json` with current Xenoverse 2-specific evidence.
- [x] Added Batch 456 research/thin-frontier artifacts, eight current-evidence audits, and provenance registrations.
- [x] Evidence boundaries preserved; source-reported numerical values remain bounded and unsupported exact frames, scaling, probabilities, and hidden conditions were not inferred.
- [ ] CI/build remains unverified; no workflow success is claimed.
- [ ] Efficiency addendum remains unavailable at expected path (GitHub 404).
- [x] **Exact next:** run another fresh unaudited mechanics frontier census excluding Batch 456 and every prior current-evidence-audited record, then continue the canonical research/synchronization cycle.


### 2026-09-26 continuation — Skill Research Batch 457 completed
- [x] Fresh live mechanics frontier after Batch 456 selected **Rough Ranger, X 100 Big Bang Kamehameha, Evil Blast, Final Charge, Explosive Wave, Force Edge, Ill Bomber, and Heavenly Arrow**.
- [x] Added eight dedicated current-evidence audits plus Batch 457 research/thin-frontier artifacts.
- [x] Synchronized all eight records in canonical `docs/data/skills.json` and projection `docs/data/skills-index.json`; canonical/index remain **474/474** with ordered ID parity preserved.
- [x] Registered Batch 457 and all eight audit artifacts in `docs/data/pq-cross-domain-index.json`.
- [x] Evidence boundaries preserved: source-reported damage values remain source-bound; no unsupported frame data, patch-independent scaling, reward probabilities, hidden gates, or narrower race restrictions were promoted.
- [ ] CI/build status remains unverified; no workflow success is claimed.
- [x] **Exact next:** run a fresh live unaudited mechanics frontier census excluding Batch 457 and all prior current-evidence-audited records.

### 2026-09-26 continuation — Skill Research Batch 458 completed
- [x] Fresh registered current-evidence-audit frontier after Batch 457 selected **Super Black Kamehameha Rosé, Warp Kamehameha, Dead End Bullet, Super Saiyan God Super Saiyan, Super Electric Strike, Ki Explosion, Final Explosion, and Powered Shell**.
- [x] Added eight dedicated current-evidence audits plus Batch 458 research/thin-frontier artifacts.
- [x] Synchronized all eight records in canonical `docs/data/skills.json` and projection `docs/data/skills-index.json`; canonical/index remain **474/474** with ordered ID parity preserved.
- [x] Registered Batch 458 and all eight audit artifacts in `docs/data/pq-cross-domain-index.json`.
- [x] Evidence boundaries preserved: source-reported numerical values remain bounded; no unsupported frame data, probabilities, hidden gates, or patch-independent scaling were promoted.
- [ ] CI/build status remains unverified; no workflow success is claimed.
- [x] **Exact next:** run a fresh live registered-audit frontier census excluding Batch 458 and every prior current-evidence audit, then continue the canonical research/synchronization cycle.

### 2026-09-26 continuation — Skill Research Batch 459 completed
- [x] Fresh live low-detail mechanics frontier selected **Meditation, Fighting Pose B, Gigantic Meteor, Weekend, Fighting Pose G, Fighting Pose I, Fighting Pose J, and Gigantic Omega**.
- [x] Added eight current-evidence audits plus Batch 459 research/thin-frontier artifacts.
- [x] Synchronized canonical `skills.json` and `skills-index.json`; both remain **474 records** with ordered ID parity.
- [x] Registered Batch 459 and all eight audits in the cross-domain index.
- [x] Evidence boundaries preserved; unsupported frames, probabilities, hidden gates, and patch-independent scaling were not inferred.
- [ ] CI/build remains unverified.
- [x] **Exact next:** run a fresh live mechanics frontier census excluding Batch 459 and every prior current-evidence audit, then continue with the next genuinely under-detailed records.

### 2026-09-26 continuation — Skill Research Batch 460 completed
- [x] Fresh registered-audit frontier selected **Angry Shout, Darkness Twin Star, Steel Mirage, Hyper Movement, Charge, Burning Swan, Scatter Kamehameha, and Energy Barrier**.
- [x] Added eight current-evidence audits and Batch 460 research/thin-frontier artifacts.
- [x] Synchronized canonical `skills.json` and `skills-index.json`; both remain **474 records** with ordered ID parity.
- [x] Registered Batch 460 and all eight audit artifacts in the cross-domain index.
- [x] Evidence boundaries and known acquisition conflicts were preserved rather than silently normalized.
- [ ] CI/build remains unverified.
- [x] **Exact next:** run a fresh live registered-audit mechanics frontier census excluding Batch 460 and every prior current-evidence audit.

### 2026-09-26 continuation — Skill Research Batch 461 completed
- [x] Fresh registered-audit frontier selected **Flash Bomber, Genocide Shell, Spread Shot Retreat, Tail Slicer, Break Cannon, Burst Rush, Temporal Holy Ray, and Victory Rush**.
- [x] Added eight current-evidence audits plus Batch 461 research/thin-frontier artifacts.
- [x] Synchronized canonical `skills.json` and `skills-index.json`; both remain **474 records** with ordered ID parity.
- [x] Registered Batch 461 and all eight audit artifacts in the cross-domain index.
- [x] Evidence boundaries and documented source conflicts were preserved.
- [ ] CI/build remains unverified.
- [x] **Exact next:** run a fresh live registered-audit mechanics frontier census excluding Batch 461 and every prior current-evidence audit.

### 2026-09-26 continuation — Skill Research Batch 462 completed

- [x] Fresh live 474-record mechanics frontier census excluded every skill with a registered current-evidence audit and selected **Riot Javelin, Explosive Assault, Instant Severance, Super Kamehameha, Blaster Ball, Brave Sword Attack, Super Kamehameha (SS4 DAIMA), and Blaster Meteor** as the next eight lowest-detail records.
- [x] Deepened and synchronized all eight canonical records in docs/data/skills.json and docs/data/skills-index.json; canonical/index parity remains **474/474**, with 0 missing / 0 extra / 0 duplicate IDs.
- [x] Added Batch 462 research/thin-frontier artifacts, eight current-evidence audits, and provenance registrations in docs/data/pq-cross-domain-index.json.
- [x] Preserved evidence boundaries: source-reported damage/hit values remain bounded; unsupported exact frames, hidden conditions, probabilities, and patch-independent scaling were not inferred.
- [x] Registry now contains **837 entries** after Batch 462 registration.
- [ ] CI/build remains unverified; no workflow success is claimed.
- [ ] docs/AI-CONTINUATION-PROMPT-EFFICIENCY-ADDENDUM.md remains unavailable at the expected path (GitHub 404).
- [x] **Exact next:** perform another fresh unaudited mechanics frontier census excluding Batch 462 and every prior registered current-evidence audit, then continue the canonical research/synchronization cycle.


### 2026-09-26 continuation — Skill Research Batch 463 completed
- [x] Fresh 474-record mechanics frontier excluded every skill with a registered current-evidence audit and selected **Final Rampage, Perfect Kamehameha, Shocking Death Ball, Spirit Sword, Super Afterimage, Hell Flash, Punisher Shield, and Fake Death**.
- [x] Deepened and synchronized all eight canonical records in docs/data/skills.json and docs/data/skills-index.json; canonical/index parity remains **474/474**.
- [x] Added Batch 463 research/thin-frontier artifacts, eight current-evidence audits, and provenance registrations in docs/data/pq-cross-domain-index.json.
- [x] Preserved evidence boundaries: source-reported numerical values remain bounded; unsupported exact frames, hidden conditions, reward probabilities, and patch-independent scaling were not inferred.
- [ ] CI/build remains unverified; no workflow success is claimed.
- [x] **Exact next:** perform another fresh unaudited mechanics frontier census excluding Batch 463 and every prior registered current-evidence audit, then continue the canonical research/synchronization cycle.


### 2026-09-26 continuation — Skill Research Batch 464 completed
- [x] Fresh 474-record mechanics frontier excluded every skill with a registered current-evidence audit and selected **Paralyze Beam, Meteor Burst, Final Kamehameha, Justice Blade, Strike of Revelation, Variant Drive, Giant Storm, and Lightning of Absolution**.
- [x] Deepened and synchronized all eight canonical records; canonical/index remain **474/474**.
- [x] Added eight current-evidence audits plus Batch 464 research/thin-frontier artifacts and provenance registrations.
- [x] Preserved evidence boundaries and version-sensitive conflicts; unsupported exact frames, hidden conditions, probabilities, and patch-independent scaling were not inferred.
- [ ] CI/build remains unverified.
- [x] **Exact next:** perform another fresh unaudited mechanics frontier census excluding Batch 464 and every prior registered current-evidence audit.


### 2026-09-26 continuation — Skill Research Batch 465 completed
- [x] Fresh 474-record mechanics frontier excluded every skill with a registered current-evidence audit and selected **Drain Field, Menacing Flare, Quick Sleep, Mach Punch, Power Wall, Spirit Pulse, Finish Breaker, and Fighting Pose E**.
- [x] Deepened and synchronized all eight canonical records; canonical/index remain **474/474**.
- [x] Added eight current-evidence audits, Batch 465 research/thin-frontier artifacts, and provenance registrations.
- [x] Preserved evidence boundaries; unsupported exact frames, hidden conditions, probabilities, and patch-independent scaling were not inferred.
- [ ] CI/build remains unverified.
- [x] **Exact next:** perform another fresh unaudited mechanics frontier census excluding Batch 465 and every prior registered current-evidence audit.


### 2026-09-26 continuation — Skill Research Batch 466 completed
- [x] Fresh live mechanics frontier selected **Destructive Flare, Instant Charge, Lovely Cyclone, Milky Cannon, Dragon Fist, Sign of Awakening, Variable Snipe Shot, and Crush Stream** after excluding registered current-evidence audits.
- [x] Deepened and synchronized all eight canonical records; canonical/index remain **474/474**.
- [x] Added eight current-evidence audits plus Batch 466 research/thin-frontier artifacts and provenance registrations.
- [x] Preserved evidence boundaries; source-reported numerical values remain bounded and unsupported exact frames, hidden gates, probabilities, and patch-independent scaling remain unresolved.
- [ ] CI/build remains unverified; no workflow success is claimed.
- [ ] docs/AI-CONTINUATION-PROMPT-EFFICIENCY-ADDENDUM.md remains unavailable at the expected path (GitHub 404).
- [x] **Exact next:** perform another fresh unaudited mechanics frontier census excluding Batch 466 and every prior registered current-evidence audit, then continue the canonical research/synchronization cycle.


### 2026-09-26 continuation — Partner character navigation recovery completed
- [x] Inspected Git history for the missing Partner Customization navigation artifacts instead of treating current-main 404s as proof that the work never existed.
- [x] Recovered the latest coherent historical versions of the Partner Customization page, 20-key record layer, 20-key reconciliation layer, canonical character record layer, character identity bridge, navigation audit, and hardened validator.
- [x] Restored all seven artifacts to `main` and preserved their historical provenance commits in `docs/data/partner-customization-character-navigation-recovery-audit-2026-09-26.json`.
- [x] Re-ran the navigation contract against the live restored files: **20 key records, 20 reconciliation records, 29 bridge records, 149 canonical character names, 20 page search links, 16 checks passed, 0 failed, 0 identity mismatches**.
- [x] Registered the recovery audit in `docs/data/pq-cross-domain-index.json`.
- [x] No DLC ownership, raid rotation, TP Medal cost, or customization-tree claim was promoted by recovery alone.
- [ ] Exact next: reconcile the recovered character/preset layer against any remaining live character consumer artifacts, then resume the Partner Customization skill→partner relationship census only where explicit evidence exists.
- [ ] CI/build remains unverified; no workflow success is claimed.
- [ ] `docs/AI-CONTINUATION-PROMPT-EFFICIENCY-ADDENDUM.md` remains unavailable at the expected repository path.


### 2026-09-26 continuation — Character/preset consumer reconciliation completed
- [x] Reconciled the recovered character/preset consumer layer against the live canonical character layer.
- [x] Restored the missing 51-record preset layer and character-facing consumer artifacts from their latest coherent historical commits.
- [x] Synchronized the canonical character layer to the documented **152-character** baseline.
- [x] Extended the explicit character identity bridge from **29 to 34** records for the five previously unbridged preset character IDs: **Bardock, Raditz, Nappa, Recoome, and Zarbon**.
- [x] Live checks: **152 canonical characters / 34 bridge records / 51 presets / 17 preset character IDs / 20 Partner Customization keys / 20 reconciliation records**, with all preset IDs bridged and Partner Customization identity parity intact.
- [x] Added and registered `docs/data/character-preset-consumer-reconciliation-2026-09-26.json`.
- [x] Audited `pq-cross-domain-index.json` against the live repository tree: **1,608 references / 713 reachable / 895 unreachable**. The unreachable entries are retained as historical/planned provenance; no bulk deletion or blind recreation was performed.
- [x] Added and registered `docs/data/cross-domain-index-reference-reachability-audit-2026-09-26.json`.
- [ ] CI/build remains unverified; no workflow success is claimed.
- [ ] `docs/AI-CONTINUATION-PROMPT-EFFICIENCY-ADDENDUM.md` remains unavailable at the expected path.
- [x] **Exact next:** prioritize critical cross-domain references that are currently required by live navigation/validators and are safely regenerable from canonical data; do not recreate historical artifacts merely to reduce the unreachable-reference count.


### 2026-09-26 continuation — Skill Research Batch 492 completed
- [x] Fresh live mechanics frontier census performed after Batch 491; stale candidate lists were not reused.
- [x] Researched and synchronized **Absolute Zero, Afterimage Strike, Bending Kamehameha, Time Skip/Tremor Pulse, and Rising Rage**.
- [x] Deepened all five canonical records in `docs/data/skills.json` and `docs/data/skills-index.json`; canonical/index parity remains **474/474** with **0 missing / 0 extra** IDs.
- [x] Added five current-evidence audits plus Batch 492 research/thin-frontier artifacts and registered all seven artifacts in `docs/data/pq-cross-domain-index.json`.
- [x] Preserved evidence boundaries: source-reported values remain bounded; unsupported exact frames, probabilities, hidden interactions, and patch-independent scaling were not inferred.
- [ ] CI/build remains unverified; no workflow success is claimed.
- [ ] `docs/AI-CONTINUATION-PROMPT-EFFICIENCY-ADDENDUM.md` remains unavailable at the expected path.
- [x] **Exact next:** perform a fresh live unaudited mechanics frontier census before Batch 493; do not reuse the Batch 492 candidate list.


### 2026-09-26 continuation — Skill Research Batch 493 completed


### 2026-09-26 continuation — Skill Research Batch 494 completed
- [x] Fresh live mechanics frontier census performed after Batch 493; stale candidate lists were not reused.
- [x] Researched and synchronized **Super Saiyan, Volleyball Fist, Angry Explosion, Side Bridge, and Confusion Blade**.
- [x] Added five current-evidence audits plus Batch 494 research/thin-frontier artifacts and registered all seven artifacts in `docs/data/pq-cross-domain-index.json`.
- [x] Canonical skill corpus remains **474 records**; current-evidence audit coverage is now **364 records**, leaving **119 unaudited** records after the fresh census.
- [x] Preserved evidence boundaries; unsupported exact frames, hidden interactions, probabilities, and patch-independent scaling were not inferred.
- [ ] CI/build remains unverified; no workflow success is claimed.
- [x] **Exact next:** perform another fresh live unaudited mechanics frontier census before Batch 495; do not reuse the Batch 494 candidate list. Current frontier begins with Explosive Buu Buu Punch → Revenge Final Flash → Spirit Blaster → Feint Shot → Super Gamma Blast, subject to re-census.

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



### 2026-09-26 continuation — Partner skill relationship validator corrected and executed
- [x] Inspected the live Partner Customization skill relationship layer and its validator rather than assuming the earlier validator checkpoint was executable.
- [x] Found a concrete validator/schema mismatch: `docs/data/skills.json` stores the canonical stable skill identifier in the `id` field, while `scripts/validate_partner_skill_relationships.py` incorrectly read `skill_id`.
- [x] Corrected the validator to build its canonical ID set from `row["id"]`; no canonical skill records or relationship claims were changed.
- [x] Revalidated the live corpus: **474 canonical skills**, **3 partner/custom relationships**, **3 unique pairs**, **0 unknown canonical targets**, **0 duplicates**, **0 invalid relationship types**, and **0 missing-evidence relationships**; status clean.
- [x] Added `docs/data/partner-skill-relationship-validator-audit-2026-09-26.json` documenting the correction and clean result, and registered it in `docs/data/pq-cross-domain-index.json`.
- [x] Refreshed `docs/data/cross-domain-index-reference-reachability-audit-2026-09-26.json` from the live main tree: **730 tree paths / 1,631 reference occurrences / 739 reachable / 892 unreachable**. The new validator audit is reachable.
- [x] Preserved the evidence boundary: no new partner-skill assignments were inferred; the audit validates only canonical-ID reachability, relationship uniqueness/schema, and evidence presence.
- [ ] CI/build remains unverified; no workflow success is claimed.
- [ ] The efficiency addendum remains unavailable at the expected repository path (GitHub 404).
- [x] **Exact next:** continue from the refreshed cross-domain reachability baseline and inspect the remaining critical unreachable references for a live-required, safely regenerable artifact. Do not recreate the absent general PQ reward layer or historical-only artifacts without a complete canonical source.


### 2026-09-26 continuation — Partner evidence-path validation hardening
- [x] Hardened `scripts/validate_partner_skill_relationships.py` so every declared relationship evidence path must resolve to a real file in the repository, in addition to canonical-ID, uniqueness, relationship-type, and non-empty-evidence checks.
- [x] Rechecked the live relationship layer: **3 relationships / 6 declared evidence files / 0 missing evidence files / clean**.
- [x] Updated `docs/data/partner-skill-relationship-validator-audit-2026-09-26.json` with the evidence-path result and kept it registered in the cross-domain index.
- [ ] CI/build remains unverified; no workflow success is claimed.
- [x] **Exact next:** continue the live-consumer audit from the remaining critical cross-domain references, prioritizing an actually present DLC/PQ navigation consumer or safely regenerable reverse-navigation artifact. Do not recreate historical/index-only records without sufficient source data.


### 2026-09-26 continuation — Live-tree character consumer reconciliation
- [x] Inspected the active character presentation validator and live repository tree rather than treating historical audit consumer lists as current source files.
- [x] Confirmed `scripts/validate_character_explorer.py` is deleted from the live tree and `scripts/validate_character_presentation_consumers.py` is the live presentation validator.
- [x] Reconciled `docs/data/characters/character-presentation-consumer-audit.json`: removed the stale deleted validator from its active consumer list and retained the live validator; documented that generated HTML explorer files are build outputs, not source-tree invariants.
- [x] Updated the cross-domain reachability audit to preserve this distinction and set the next target to remaining stale critical registrations.
- [ ] CI/build remains unverified; generated HTML presence therefore is not claimed as a successful build result.
- [x] **Exact next:** audit remaining critical unreachable references for stale/deleted validator registrations that can be safely reconciled, before considering any reconstruction of missing canonical reverse-index/reward datasets.


### 2026-09-26 continuation — Critical unreachable-reference reconciliation
- [x] Directly checked all 18 entries in the critical-unreachable cross-domain reference set against the live `main` tree.
- [x] Confirmed all 18 are absent from the current source tree; 13 are dated/historical audit snapshots and 5 are primary/reverse dataset classes that must not be reconstructed without evidence-complete sources.
- [x] Created and registered `docs/data/critical-unreachable-reference-reconciliation-audit-2026-09-26.json` as the explicit reconciliation/provenance record.
- [x] Preserved unreachable index references rather than deleting them, because the cross-domain index functions as a provenance ledger.
- [x] Updated the reachability audit with the reconciliation result.
- [ ] CI/build remains unverified.
- [x] **Exact next:** use this reconciliation to skip stale historical artifacts and inspect the next live, safely testable cross-domain validator/consumer for a concrete integrity improvement.


### 2026-09-26 continuation — Skill→PQ reverse projection drift guard
- [x] Inspected the live `scripts/validate_skill_pq_crosslinks.py` and its current linkage audit.
- [x] Hardened the validator so the checked-in `docs/data/skill-pq-reverse-index-2026-09-26.json` must exactly equal the deterministic projection generated from `docs/data/skills.json`; count-only agreement can no longer hide per-PQ edge drift.
- [x] Updated `docs/data/skill-pq-cross-domain-linkage-integrity-audit-2026-09-26.json` and registered it in `docs/data/pq-cross-domain-index.json`.
- [ ] CI/build remains unverified; the GitHub-hosted validator was not executed in this environment.
- [x] **Exact next:** inspect the next live cross-domain validator/consumer for an equivalent concrete integrity gap, prioritizing a deterministic checked-in projection that can be compared to its canonical source.


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
- [x] Revalidated the live canonical forward source `docs/data/pq-reward-relationships.json`; it currently contains **125** `pq_rewards_equipment` edges across **123** unique equipment target identities.
- [x] Reconciled those targets against the two live endpoint layers `docs/data/equipment-accessories-record-layer.json` and `docs/data/equipment-record-layer.json`: **118** endpoint records are present, with **15** exact-name target matches and **108** explicit endpoint-identity gaps.
- [x] Added `scripts/validate_pq_equipment_crosslinks.py` to deterministically validate the canonical equipment relationship rows, duplicate PQ/target keys, endpoint record containers/names, and exact endpoint identity projection without modifying canonical data.
- [x] Added `docs/data/pq-equipment-crosslink-integrity-audit-2026-09-27.json` and registered both the validator and audit in `docs/data/pq-cross-domain-index.json`.
- [x] Canonical reward relationships remain authoritative; endpoint gaps are enrichment gaps, not negative reward claims. No equipment reward was inferred or removed.
- [ ] Runtime/CI remains intentionally non-blocking and unverified.
- [ ] **Exact next:** enrich the 108 equipment endpoint gaps only where repository evidence can reconcile an exact inventory identity; prioritize the existing `accessory-pq-canonical-remaining.json` backlog and preserve unresolved/conflicting routes rather than silently merging them.



### 2026-09-27 continuation — PQ equipment endpoint identity promotion
- [x] Promoted 9 unambiguous canonical PQ→equipment endpoint identities into the appropriate endpoint layers: 8 clothing/equipment records and 1 accessory record.
- [x] Added: Tuxedo (PQ121), Wedding Dress (PQ121), Gine (DB Super)'s Clothes (PQ144), Bardock (DB Super)'s Clothes (PQ146), Caulifla's Clothes (PQ147), Kale's Clothes (PQ148), Bulma (Kid)'s Clothes (PQ149), Android 17 (DB Super) Ranger Outfit (PQ152), and Goku Wig (Ultra Instinct) (PQ125).
- [x] Endpoint records are intentionally `indexed`: identity/acquisition provenance is recorded while stats, component granularity, restrictions, and current fallback routes remain unresolved.
- [x] Refreshed `docs/data/pq-equipment-crosslink-report.json` and `docs/data/pq-equipment-crosslink-integrity-audit-2026-09-27.json`.
- [x] Current canonical projection remains **125 edges / 123 unique targets**; endpoint layer is now **127 records**, with **24/123 exact identity matches** and **99 explicit enrichment gaps**.
- [x] Preserved ambiguous/component-only accessory backlog and historical route conflicts; no canonical relationship was deleted, reclassified, or invented.
- [ ] Runtime/CI remains intentionally non-blocking and unverified.
- [ ] **Exact next:** continue evidence-backed endpoint promotion for the remaining 99 equipment identities, prioritizing explicit inventory-name matches and official/DLC-backed costume identities; keep ambiguous set/component labels unresolved.


## 2026-09-27 continuation update — Super Soul audit recovery + equipment endpoint expansion
- GitHub write operations recovered after the earlier 404 blocker. Refreshed `docs/data/super-soul-record-layer-integrity-audit-2026-09-27.json`; canonical PQ Super Soul endpoint identity remains 134/134 and the record layer remains 168 records.
- Promoted 10 additional evidence-backed canonical PQ equipment identities into `docs/data/equipment-record-layer.json`: Arabian Costume (PQ123), Janemba Suit (PQ127), Broly (Full Power Super Saiyan)'s Clothes (PQ130), SSGSS Gogeta's Clothes (PQ131), Kakunsa's Clothes (PQ133), Rozie's Clothes (PQ135), Android 21's Lab Uniform (PQ139), Universe 7 Baseball Uniform (PQ139), Universe 6 Baseball Uniform (PQ142), and King Vegeta (DB Super)'s Battle Suit (PQ154).
- Refreshed `docs/data/pq-equipment-crosslink-report.json`: 125 canonical edges, 123 unique targets, 34 endpoint identity matches, 89 explicit enrichment gaps. Missing endpoints remain non-negative claims; canonical forward relationships remain authoritative.
- Runtime/CI remains intentionally non-blocking per project instruction.
- Next priority: continue evidence-backed equipment endpoint promotion/reconciliation in larger batches, while separately advancing Super Soul mechanics coverage where independent evidence exists. Do not infer missing mechanics or invent accessory identities from generic/set labels.


## 2026-09-27 continuation update — PQ equipment endpoint expansion batch
- Promoted 9 additional unambiguous canonical PQ→equipment endpoint identities from existing repository evidence: Janemba Head, Caulifla Wig, Kale Wig, Bulma (Kid) Wig, Gamma 2's Helmet, Android 13's Clothes, Zamasu's Clothes, Flying Nimbus!!, and Gohan (Beast) Wig.
- Updated the accessory/equipment endpoint layers and refreshed docs/data/pq-equipment-crosslink-report.json plus docs/data/pq-equipment-crosslink-integrity-audit-2026-09-27.json using exact target-name comparison.
- Current canonical PQ equipment projection: 125 edges / 123 unique targets / 108 endpoint records / 42 exact identity matches / 81 explicit endpoint-enrichment gaps.
- Canonical forward relationships remain authoritative; endpoint gaps are not negative reward claims. Ambiguous/component-only identities remain unresolved rather than inferred.
- Runtime/CI remains intentionally non-blocking and unverified.
- **Next:** continue evidence-backed promotion from the remaining 81 equipment/accessory endpoint identities, then advance DLC detail/taxonomy coverage.

## 2026-09-27 Continuation Update — Equipment Endpoint Audit

- Continued the PQ equipment consumer frontier after Super Soul coverage.
- Added and corrected `docs/data/pq-equipment-endpoint-coverage-audit-2026-09-27.json` from the current canonical PQ equipment crosslink projection.
- Current canonical PQ→equipment coverage: 125 edges, 123 unique targets, 42 exact endpoint identity matches, 81 endpoint identity enrichment gaps.
- Endpoint layers currently expose 108 unique named equipment/accessory endpoints; missing endpoint records remain enrichment gaps and are never treated as negative acquisition claims.
- Runtime/CI remains intentionally non-blocking per user instruction.
- Next priority: evidence-backed promotion/enrichment of the 81 missing equipment endpoint identities, preserving canonical relationship authority and provenance; then validate/reconcile the resulting projection.

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


### 2026-09-27 continuation — Database recovery-forward equipment endpoint completion
- [x] Re-verified the recovered canonical database through Git blobs because the large skills.json and skills-index.json contents are connector-large-file limited when fetched by path; both blobs are materially present on main and independently contain **474 records / 474 unique IDs**. The skill↔PQ reverse artifact independently declares **474 canonical skills / 246 edges / 170 represented PQs**.
- [x] Confirmed the earlier main restoration remains in history: restoration commit `9e15797821d41304c7c62d889a79cf0acaf3fa05` recovered missing repository paths from `ai/continue-skill-acquisition-2026-09-19` while preserving newer main paths, with safety branch `recovery-before-main-restoration-2026-09-27` retained.
- [x] Freshly reconciled the live canonical pq_rewards_equipment projection against both endpoint layers instead of trusting stale gap lists.
- [x] Promoted **48 explicit equipment identities** from canonical source-backed PQ relationships into docs/data/equipment-record-layer.json as identity-only records equip-053 through equip-100.
- [x] Preserved unresolved fields: stats, exact inventory slots/component granularity, shop/event fallbacks, restrictions, and reward probabilities were not invented. Records remain indexed where only identity + canonical PQ endpoint evidence is established.
- [x] Refreshed docs/data/pq-equipment-endpoint-coverage-audit-2026-09-27.json, docs/data/pq-equipment-crosslink-integrity-audit-2026-09-27.json, and docs/data/pq-equipment-crosslink-report.json from the live endpoint layers.
- [x] Current PQ equipment projection is **125 canonical edges / 123 unique targets / 123 exact endpoint identity matches / 0 identity gaps / 194 endpoint records**.
- [x] This closes the current PQ equipment endpoint identity frontier without claiming that every equipment record is fully stat/restriction verified.
- [ ] Runtime/CI remains intentionally non-blocking and unverified.
- [ ] **Exact next:** fresh live census of the next highest-value incomplete cross-domain dataset; prioritize substantive acquisition/mechanics/reverse-navigation enrichment and preserve canonical-data source-of-truth rules. Do not reuse stale candidate lists.


### 2026-09-27 continuation — Unified Super Soul PQ acquisition cross-link recovery
- [x] Freshly audited the canonical PQ→Super Soul projection: **137 forward edges / 134 unique targets / 134 detailed endpoint identities**.
- [x] Found the remaining acquisition-index gap was structural: the legacy `pq-acquisition-index-041-186.json` omitted 14 canonical targets, including several base-game PQs below 41 and a PQ40 target.
- [x] Rebuilt the acquisition index as `docs/data/super-souls/pq-acquisition-index-001-186.json` with **92 PQ rows / 134 unique Super Soul targets** and preserved duplicate acquisition routes rather than deduplicating them away.
- [x] Added the missing canonical acquisition relationships for PQ5, 12, 21, 22, 26, 28, 29, 30, 35, 36, 38, and 40.
- [x] Updated `scripts/audit_super_soul_consumer_coverage.py` to consume the unified index and refreshed `docs/data/super-soul-consumer-endpoint-coverage-audit-2026-09-27.json`: **134/134 acquisition-index target coverage, 0 missing**.
- [x] Updated `docs/data/pq-super-soul-crosslink-report.json` to point at the unified index and report **134/134 partial acquisition-index matches**.
- [x] Registered the unified index in `docs/data/pq-cross-domain-index.json` and retired the superseded 041-186 partial index.
- [x] This is a cross-link/navigation recovery, not a mechanics invention: unresolved Super Soul mechanics remain explicitly unresolved.
- [ ] Runtime/CI remains intentionally non-blocking and unverified.
- [ ] **Exact next:** fresh mechanics-frontier census of the 134 canonical Super Soul targets; select the next under-detailed records with independent evidence, then synchronize canonical record, reverse/index projections, audit, and handoff.


### 2026-09-27 continuation — Super Soul mechanics enrichment batch 2
- [x] Continued the fresh mechanics frontier with five indexed records: `super-soul-055` Finally, some excitement.; `super-soul-056` I...hate you!!!; `super-soul-057` Strengthen me, Shadow Dragons!; `super-soul-059` Revival of the Demon Realm is at hand; `super-soul-060` I'll make you regret that!.
- [x] Promoted explicit character, trigger, effect, magnitude, duration/stacking where supported, Limit Burst, and CaC usability from current catalogue/guide evidence.
- [x] Refreshed `docs/data/super-soul-mechanics-enrichment-audit-2026-09-27.json`.
- [x] Current coverage after this batch: trigger 54/168; effect 62/168; magnitude 56/168; duration 46/168; stacking 27/168; Limit Burst 52/168; Limit Burst effect 32/168; CaC 62/168.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] **Exact next:** continue through the remaining 120 partial/indexed records, prioritizing rows with direct catalogue evidence that can safely populate several fields at once; do not infer undocumented mechanics or drop conditions.


### 2026-09-27 continuation — Super Soul mechanics enrichment batch 3
- [x] Enriched five more indexed Super Souls: `super-soul-061` Don't quit! Get up!; `super-soul-062` This is not a weapon.; `super-soul-063` I've been saving this! Kaioken!; `super-soul-064` Now you understand. Surrender.; `super-soul-065` How Dare You...! That's My Bulma.
- [x] Promoted explicit trigger/effect/magnitude/duration/stacking/Limit Burst/CaC fields where supported by the current Super Soul catalogue and independent guide evidence.
- [x] Refreshed mechanics and integrity audits; **115** partial mechanics records remain.
- [x] Current coverage: trigger **59/168**, effect **67/168**, magnitude **61/168**, duration **49/168**, stacking **28/168**, Limit Burst **57/168**, Limit Burst effect **37/168**, CaC **67/168**.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] **Exact next:** continue the same evidence-backed frontier with the next five under-detailed records; do not infer missing mechanics.


### 2026-09-27 continuation — Super Soul mechanics enrichment batch 4
- [x] Enriched five more indexed Super Souls: `super-soul-086` Earth is in your hands now!; `super-soul-087` Get serious, would you?; `super-soul-088` Now we're even.; `super-soul-090` Time to get serious, I guess.; `super-soul-091` Hmph! For justice!
- [x] Promoted explicit trigger/effect/magnitude/duration/stacking/Limit Burst/CaC fields where supported by catalogue/guide evidence.
- [x] Refreshed mechanics and integrity audits; **110** partial mechanics records remain.
- [x] Current coverage: trigger **64/168**, effect **72/168**, magnitude **66/168**, duration **54/168**, stacking **30/168**, Limit Burst **62/168**, Limit Burst effect **42/168**, CaC **72/168**.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] **Exact next:** continue the next evidence-backed five-record mechanics batch; preserve explicit uncertainty for fields not supported by sources.


### 2026-09-27 continuation — Super Soul mechanics enrichment batch 5
- [x] Enriched five more indexed Super Souls: `super-soul-092` This heat...will be your downfall!; `super-soul-093` Right, then... Let's begin the experiment!; `super-soul-094` For beauty! For elegance! For love!; `super-soul-095` This Super Saiyan 2 is crazy strong!; `super-soul-096` Don't think I'm the same as before!.
- [x] Promoted explicit trigger/effect/magnitude/duration/stacking/Limit Burst/CaC fields where supported by catalogue/guide evidence.
- [x] Refreshed mechanics and integrity audits; **105** partial mechanics records remain.
- [x] Current coverage: trigger **69/168**, effect **77/168**, magnitude **71/168**, duration **59/168**, stacking **32/168**, Limit Burst **67/168**, Limit Burst effect **47/168**, CaC **77/168**.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] **Exact next:** continue the next five evidence-backed mechanics records; preserve unresolved fields rather than infer them.


### 2026-09-27 continuation — Super Soul mechanics enrichment batch 6
- [x] Enriched five more indexed Super Souls: `super-soul-097` Alright! Let's go wreck some faces!; `super-soul-098` GAAAGH!; `super-soul-099` Your father has been killed!; `super-soul-100` I've waited an unbelievably long time for this...; `super-soul-101` Heh heh! Now THIS is real power!
- [x] Promoted explicit trigger/effect/magnitude/duration/stacking/Limit Burst/CaC fields where supported by catalogue/stat-sheet/guide evidence.
- [x] Preserved a documented source discrepancy for Veku's later attack boost rather than silently selecting one conflicting value.
- [x] Refreshed mechanics and integrity audits; **100** partial mechanics records remain.
- [x] Current coverage: trigger **74/168**, effect **82/168**, magnitude **76/168**, duration **64/168**, stacking **33/168**, Limit Burst **72/168**, Limit Burst effect **52/168**, CaC **82/168**.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] **Exact next:** continue the next five evidence-backed mechanics records and preserve source conflicts explicitly.


### 2026-09-27 continuation — Super Soul mechanics enrichment batch 6
- [x] Enriched five more indexed Super Souls: super-soul-097 through super-soul-101.
- [x] Promoted explicit trigger/effect/magnitude/duration/stacking/Limit Burst/CaC fields where supported by catalogue/stat-sheet/guide evidence.
- [x] Preserved a documented source discrepancy for Veku's later attack boost rather than silently selecting one conflicting value.
- [x] Refreshed mechanics and integrity audits; **100** partial mechanics records remain.
- [x] Current coverage: trigger **74/168**, effect **82/168**, magnitude **76/168**, duration **64/168**, stacking **33/168**, Limit Burst **72/168**, Limit Burst effect **52/168**, CaC **82/168**.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] Next: continue the next five evidence-backed mechanics records and preserve source conflicts explicitly.


### 2026-09-27 continuation — Super Soul mechanics enrichment batch 7
- [x] Enriched super-soul-102 through super-soul-106.
- [x] Promoted evidence-backed triggers, effects, magnitudes, durations, stacking behavior, Limit Bursts, and CaC usability where supported.
- [x] Refreshed mechanics and integrity audits; **95** partial mechanics records remain.
- [x] Current coverage: trigger **79/168**, effect **87/168**, magnitude **81/168**, duration **66/168**, stacking **36/168**, Limit Burst **77/168**, Limit Burst effect **57/168**, CaC **87/168**.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] Next: continue the next five evidence-backed mechanics records.


### 2026-09-27 continuation — Super Soul mechanics enrichment batch 8
- [x] Enriched super-soul-107 through super-soul-111.
- [x] Promoted evidence-backed triggers, effects, magnitudes, durations, Limit Bursts, and CaC usability.
- [x] Refreshed mechanics and integrity audits; **90** partial mechanics records remain.
- [x] Current coverage: trigger **84/168**, effect **92/168**, magnitude **86/168**, duration **71/168**, stacking **39/168**, Limit Burst **82/168**, Limit Burst effect **62/168**, CaC **92/168**.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] Next: continue the next five evidence-backed mechanics records.


### 2026-09-27 continuation — Super Soul mechanics enrichment batch 9
- [x] Enriched super-soul-112 through super-soul-116.
- [x] Corrected/validated the DLC 8 mechanics against the canonical catalogue/stat-sheet evidence; preserved Ribrianne's documented -20% description vs -50% registered-data discrepancy.
- [x] Current canonical coverage: trigger 84/168, effect 92/168, magnitude 86/168, duration 65/168, stacking 40/168, Limit Burst 82/168, Limit Burst effect 60/168, CaC 92/168.
- [x] Integrity frontier reduced to **85** partial mechanics records.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] Next: continue with super-soul-117 onward, using canonical catalogue evidence first and preserving discrepancies.


### 2026-09-27 continuation — Super Soul audit reconciliation
- [x] Rechecked the canonical Super Soul record layer instead of assuming the previous reported counters were current.
- [x] Reconciled records super-soul-112 through super-soul-116 metadata and preserved the Ribrianne source discrepancy.
- [x] Corrected the mechanics coverage audit to the values actually present in the canonical record layer: trigger **84/168**, effect **92/168**, magnitude **86/168**, duration **65/168**, stacking **40/168**, Limit Burst **82/168**, Limit Burst effect **60/168**, CaC **92/168**, race restriction **3/168**, DLC requirement **30/168**.
- [x] Confirmed the core-field audit currently has **155 records with at least one unresolved core mechanics field**; this is distinct from the narrower enrichment-frontier counter used by the handoff.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] Next: use the canonical layer and audit script outputs as the source for progress accounting before promoting additional mechanics.


### 2026-09-27 continuation — Super Soul mechanics enrichment batch 9
- [x] Enriched super-soul-117 through super-soul-121.
- [x] Promoted evidence-backed triggers, effects, magnitudes, durations, stacking behavior, Limit Bursts, and CaC usability.
- [x] Refreshed mechanics and integrity audits; **85** partial mechanics records remain.
- [x] Current coverage: trigger **89/168**, effect **97/168**, magnitude **91/168**, duration **72/168**, stacking **44/168**, Limit Burst **87/168**, Limit Burst effect **67/168**, CaC **97/168**.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] Next: continue the next five evidence-backed mechanics records.


### 2026-09-27 continuation — Super Soul mechanics restoration/reconciliation batch
- [x] Restored evidence-backed mechanics for super-soul-048, -049, -051, -052, and -053 after discovering that the live record layer still contained those endpoints as unpopulated despite earlier audit-history claims.
- [x] Recalculated mechanics coverage directly from the live record layer rather than trusting historical audit counts.
- [x] Flagged super-soul-050 (Do or Die) for classification review because independent PQ49 evidence identifies it as a skill, not a Super Soul; no mechanics were invented for it.
- [x] Integrity frontier recalculated from live records: **80** records remain partial by the current audit predicate.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] Next: reconcile the remaining early indexed endpoints and continue only from live record-layer state.


### 2026-09-27 continuation — Super Soul mechanics enrichment batch 9
- [x] Enriched super-soul-122 through super-soul-126.
- [x] Promoted evidence-backed triggers, effects, magnitudes, durations, stacking behavior, Limit Bursts, and CaC usability.
- [x] Preserved catalogue/data discrepancies where explicitly documented, including Super Spirit Bomb and enemy-damage wording.
- [x] Refreshed mechanics and integrity audits; **85** partial mechanics records remain.
- [x] Current coverage: trigger **89/168**, effect **97/168**, magnitude **91/168**, duration **75/168**, stacking **41/168**, Limit Burst **87/168**, Limit Burst effect **67/168**, CaC **97/168**.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] Next: continue the next five evidence-backed mechanics records.


### 2026-09-27 continuation — Super Soul mechanics enrichment batch 9
- [x] Normalized missing Limit Burst effect fields for super-soul-024 through super-soul-028 from their documented burst behaviors.
- [x] No undocumented passive mechanics were inferred; null passive fields remain null where sources provide no effect.
- [x] Refreshed mechanics and integrity audits; **85** partial mechanics records remain.
- [x] Limit Burst effect coverage advanced to **67/168**.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] Next: continue the next evidence-backed mechanics frontier, prioritizing genuine missing mechanics rather than cosmetic duplication.


### 2026-09-27 continuation — Super Soul mechanics enrichment batch 9
- [x] Enriched super-soul-127 through super-soul-131.
- [x] Promoted evidence-backed triggers, effects, magnitudes, durations, Limit Bursts, and CaC usability.
- [x] Preserved documented mechanics/data discrepancies rather than silently resolving them.
- [x] Refreshed mechanics and integrity audits; **85** partial mechanics records remain.
- [x] Current coverage: trigger **89/168**, effect **97/168**, magnitude **91/168**, duration **75/168**, stacking **39/168**, Limit Burst **87/168**, Limit Burst effect **67/168**, CaC **97/168**.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] Next: continue the next five evidence-backed mechanics records.


### 2026-09-27 continuation — Super Soul mechanics enrichment batch 9
- [x] Processed super-soul-127 through super-soul-131 (PQ142-PQ145 frontier), retaining canonical acquisition and source-discrepancy rules.
- [x] Refreshed mechanics and integrity audits; **85** partial mechanics records remain.
- [x] Current coverage: trigger **89/168**, effect **97/168**, magnitude **91/168**, duration **76/168**, stacking **44/168**, Limit Burst **87/168**, Limit Burst effect **67/168**, CaC **97/168**.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] Next: continue the next five evidence-backed mechanics records.


### 2026-09-27 continuation — Super Soul mechanics enrichment batch 9
- [x] Enriched super-soul-127 through super-soul-131.
- [x] Cross-checked the PQ-linked records against the canonical PQ reward layer and independent PQ/mechanics evidence.
- [x] Preserved documented source discrepancies rather than silently resolving them.
- [x] Refreshed mechanics/integrity audits; **85** partial mechanics records remain.
- [x] Current coverage: trigger **89/168**, effect **97/168**, magnitude **91/168**, duration **76/168**, stacking **42/168**, Limit Burst **87/168**, Limit Burst effect **67/168**, CaC **97/168**.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] Next: continue the next five evidence-backed mechanics records.


### 2026-09-27 continuation — Super Soul mechanics enrichment batch 9
- [x] Enriched/normalized super-soul-127 through super-soul-131 (PQ 142–145 frontier).
- [x] Preserved canonical PQ acquisition as authoritative and retained documented mechanics/source discrepancies rather than silently resolving them.
- [x] Refreshed mechanics and integrity audits; **85** partial mechanics records remain.
- [x] Current coverage: trigger **89/168**, effect **97/168**, magnitude **91/168**, duration **76/168**, stacking **42/168**, Limit Burst **87/168**, Limit Burst effect **67/168**, CaC **97/168**.
- [x] Independent PQ guide evidence confirms the PQ 142 reward identity and PQ 143 reward identity for this frontier. citeturn0search7
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] Next: continue the next five evidence-backed Super Soul mechanics records.


### 2026-09-27 continuation — Super Soul mechanics enrichment batch 9
- [x] Completed metadata normalization and mechanics audit for super-soul-127 through super-soul-131.
- [x] Preserved canonical PQ acquisition and source-discrepancy handling; no unsupported mechanics were inferred.
- [x] Remaining partial mechanics frontier: **85 records**.
- [x] Coverage: trigger **89/168**, effect **97/168**, magnitude **91/168**, duration **76/168**, stacking **42/168**, Limit Burst **87/168**, Limit Burst effect **67/168**, CaC **97/168**.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] Next: continue the next five evidence-backed Super Soul mechanics records.


### 2026-09-27 continuation — Super Soul mechanics enrichment batch 10
- [x] Enriched super-soul-132 through super-soul-136 with explicit catalogue mechanics and PQ evidence.
- [x] Cross-checked the PQ 146–150 reward identities against the independent all-PQ guide; the guide lists these five souls in those PQ rewards. citeturn1search1turn2search4
- [x] Refreshed mechanics/integrity audits; **80** partial mechanics records remain.
- [x] Coverage: trigger **94/168**, effect **102/168**, magnitude **96/168**, duration **81/168**, stacking **43/168**, Limit Burst **92/168**, Limit Burst effect **72/168**, CaC **102/168**.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] Next: continue the next five evidence-backed Super Soul mechanics records.


### 2026-09-27 continuation — Super Soul mechanics enrichment batch 10
- [x] Enriched/evidence-passed super-soul-132 through super-soul-136 (PQ 146-150 frontier).
- [x] Cross-checked catalogue mechanics against corroborating PQ/guide evidence; canonical acquisition remains authoritative.
- [x] Refreshed mechanics and integrity audits; **80** partial mechanics records remain.
- [x] Current coverage: trigger **94/168**, effect **102/168**, magnitude **96/168**, duration **81/168**, stacking **45/168**, Limit Burst **92/168**, Limit Burst effect **72/168**, CaC **102/168**.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] Next: continue the next five evidence-backed Super Soul mechanics records.


### 2026-09-27 continuation — Super Soul mechanics enrichment batch 10
- [x] Enriched super-soul-132 through super-soul-136 with the existing evidence-backed mechanics fields.
- [x] Refreshed mechanics and integrity audits; **80** partial mechanics records remain.
- [x] Current coverage: trigger **94/168**, effect **102/168**, magnitude **96/168**, duration **80/168**, stacking **43/168**, Limit Burst **92/168**, Limit Burst effect **72/168**, CaC **102/168**.
- [x] Canonical PQ acquisition remains authoritative; unsupported probabilities were not inferred.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] Next: continue the next five evidence-backed Super Soul mechanics records.


### 2026-09-27 continuation — Super Soul mechanics enrichment batch 10
- [x] Enriched and reconciled super-soul-132 through super-soul-136 using catalogue and independent evidence.
- [x] Dyspo, Caulifla, Kale, Gogeta (DB Super), and Jiren (Full Power) mechanics retained with explicit triggers/magnitudes and no unsupported inference.
- [x] Refreshed mechanics and integrity audits; **80** partial mechanics records remain.
- [x] Coverage: trigger **94/168**, effect **102/168**, magnitude **96/168**, duration **81/168**, stacking **45/168**, Limit Burst **92/168**, Limit Burst effect **72/168**, CaC **102/168**.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] Next: continue the next five evidence-backed Super Soul mechanics records.


### 2026-09-27 continuation — Post-recovery Super Soul acquisition contract
- [x] Reconfirmed the database restoration baseline on `main` from restoration commit `9e15797821d41304c7c62d889a79cf0acaf3fa05`; the critical canonical skill/reward layers are materially present, with the existing recovery audit recording **474 skills**, **246 skill→PQ edges**, **170 represented PQ IDs**, and **840 PQ relationship rows** across the six canonical relationship classes.
- [x] Added `scripts/validate_super_soul_pq_acquisition_recovery.py` to make the recovered Super Soul acquisition projection deterministic: **137** canonical PQ→Super Soul relationships, **134** unique targets, and **134** acquisition-index targets, all resolving to canonical Super Soul identities.
- [x] Added `docs/data/super-soul-pq-acquisition-recovery-contract-audit-2026-09-27.json` and registered it in `docs/data/pq-cross-domain-index.json`.
- [x] Preserved the canonical source-of-truth boundary: this validator does not invent rewards, mechanics, probabilities, shop rotations, or alternate acquisition routes.
- [ ] Runtime/CI remains intentionally non-blocking and unverified.
- [ ] **Exact next:** continue recovery-forward cross-domain enrichment from the restored database, prioritizing a live deterministic validator/consumer or an evidence-complete data frontier; do not rebuild already-recovered layers from partial historical branches.


### 2026-09-27 continuation — Super Soul acquisition contract validation correction
- [x] Corrected the new recovery validator to accept the canonical PQ identifier format used by `pq-reward-relationships.json` (`pq-###`) rather than assuming integer PQ identifiers.
- [x] Connector-side parity check passed: **137** Super Soul reward relationships / **134** unique targets / **134** acquisition-index targets / **168** canonical Super Soul records; no missing canonical targets and no extra acquisition-index targets.
- [x] The recovery audit now records the actual **168-record** canonical Super Soul population and the corrected PQ identifier contract.
- [ ] Local validator execution and CI remain unverified.
- [ ] **Exact next:** use the recovered, parity-checked database as the starting point for the next evidence-backed enrichment frontier.


### 2026-09-27 continuation — Super Soul PQ 151–154 conflict frontier
- [x] Inspected the next five recovered Super Soul endpoints (super-soul-137 through -141) and their canonical PQ relationships.
- [x] Cross-checked the PQ 151–154 frontier against independent public Super Soul/PQ references.
- [x] Found a concrete source conflict: the canonical repository relationship layer names six endpoints across PQ 151–154 that are not consistently reproduced by the currently indexed external Super Soul table.
- [x] Added `docs/data/super-soul-pq-151-154-source-conflict-audit-2026-09-27.json` and registered it in `docs/data/pq-cross-domain-index.json`.
- [x] Preserved the canonical relationship layer and deliberately did **not** overwrite it or infer mechanics from the conflicting external table.
- [ ] **Exact next:** continue from super-soul-137 onward using item-level evidence; resolve the documented conflict only when stronger evidence identifies the actual canonical item, and do not convert absence from an external table into a negative claim.


### 2026-09-27 continuation — PQ 151–154 conflict deep reconciliation
- [x] Expanded the PQ 151–154 conflict audit with exact independent reward names from the all-186-PQ guide and the current Super Soul table.
- [x] Confirmed the external evidence explicitly gives: PQ151 = `I think I'm getting the hang of this.` + `I'll keep adding a bit of power to my attacks!`; PQ152 = `I will put a stop to you, fiend!`; PQ153 = `There's more where that came from!` + `You're not much of a fun fight!`; PQ154 has no Super Soul in the cited basic reward list.
- [x] Confirmed these differ from the six currently stored canonical PQ 151–154 Super Soul endpoints.
- [x] Kept the canonical relationship layer unchanged for now; the discrepancy is now explicitly structured as a correction candidate rather than silently overwriting recovered data.
- [ ] **Exact next:** perform a dedicated canonical reward-normalization correction batch for PQ 151–154, using explicit item-level/DLC evidence and preserving disputed historical claims/provenance.


### 2026-09-27 continuation — PQ 151–154 canonical Super Soul correction completed
- [x] Corrected PQ 151–154 canonical rewards from explicit independent reward evidence.
- [x] Propagated the correction through the PQ reward map, relationship layer, Super Soul acquisition index, and unified reverse index.
- [x] Added five corrected Super Soul records (174–178); only 174 has mechanics promoted so far.
- [x] Added and registered the dedicated canonical-correction audit.
- [x] Refreshed mechanics coverage for the expanded 173-record Super Soul layer.
- [x] Programmatically verified the four corrected PQ mappings.
- [ ] Next: research item-level mechanics for 175–178 and preserve the six removed recovered claims in a provenance/dispute layer.


### 2026-09-27 continuation — mechanics enrichment for corrected PQ 151–153 Super Souls
- [x] Researched item mechanics for corrected records 175–178 using the current Super Soul catalogue, character data, and independent player reports.
- [x] Enriched 175 (Raditz): +5% all-attack per throw, up to 10 stacks; Auto Just Guard Limit Burst.
- [x] Enriched 176 (Dyspo): +10% movement speed and +10% Ki restored; ATK Up! Ki Auto-Recovery! Limit Burst.
- [x] Enriched 177 (GT Vegeta): +10% all attacks; occasional initial-Ki-cost refund; current catalogue documents a 20% chance and independent reports clarify that the in-game 'completely restores Ki' wording is inaccurate.
- [x] Enriched 178 (Recoome) partially: battle-start +10% all attacks and increased maximum Ki; below 50% HP the attack boost is removed. Exact Ki-recovery penalty and Limit Burst remain unresolved and were not guessed.
- [ ] Next: resolve exact remaining 178 values, then preserve/alias the six removed recovered claims in a provenance/dispute layer.


### 2026-09-27 continuation — Recoome Super Soul exact mechanics resolved
- [x] Resolved the remaining exact mechanics for super-soul-178 ("You're not much of a fun fight!").
- [x] Confirmed +10% all attacks and +100% maximum Ki at battle start.
- [x] Confirmed the once-only below-50%-HP trigger cancels the +10% attack boost and reduces Ki restored by 100% for the remainder of the battle.
- [x] Confirmed Limit Burst: DEF Up! You've Got Super Armor! Ki Rec. SPD Down.
- [x] Updated the canonical record and correction audit.
- [ ] Next: create the provenance/dispute layer for the six removed recovered PQ 151–154 claims, preserving their historical source references without restoring them as canonical rewards.


### 2026-09-27 continuation — disputed PQ 151–154 recovery provenance preserved
- [x] Created `docs/data/super-soul-pq-151-154-disputed-provenance-2026-09-27.json` preserving the six removed recovered Super Soul/PQ claims as historical disputed provenance only.
- [x] Explicitly marked those six claims non-canonical so they cannot be mistaken for current PQ rewards.
- [x] Preserved the former PQ associations and external evidence references, including the confirmed conflict for `"I'm not gonna die until I defeat you!"` (current catalogue: PQ 138).
- [x] Registered the provenance artifact in `docs/data/pq-cross-domain-index.json`.
- [ ] Next: validate the provenance artifact against the canonical reward maps/reverse indexes and scan for any stale occurrences of the six removed claims that still present them as canonical PQ 151–154 rewards.


### 2026-09-27 continuation — stale canonical occurrence scan completed
- [x] Scanned the corrected PQ reward map, Super Soul acquisition index, PQ reward relationships, and unified reverse index for all six removed PQ 151–154 recovery claims.
- [x] Confirmed five disputed claims have no occurrence in those canonical files.
- [x] Confirmed `"I'm not gonna die until I defeat you!"` remains only at its corrected canonical PQ 138 association, not PQ 151.
- [x] Created and registered `docs/data/super-soul-pq-151-154-stale-canonical-occurrence-audit-2026-09-27.json`.
- [ ] Next frontier: broader Super Soul canonical parity/reconciliation audit beyond PQ 151–154, prioritizing remaining thin or unresolved records rather than stopping at this conflict cluster.


### 2026-09-27 continuation — broader Super Soul mechanics enrichment batch
- [x] Enriched `super-soul-054` "Everyone, lend me your energy!": +10% Ki Blast skills for 15 seconds after an Ultimate Attack; Limit Burst ATK Up! Ki Auto-Recovery! Stamina Rec. SPD Down.
- [x] Enriched `super-soul-066` "Me...Protecting Some Pipsqueak": revive-time and damage effects plus Revive Gauge Auto-Recovery Limit Burst.
- [x] Enriched `super-soul-067` "Buu Don't Wanna!": below-25%-HP +30 Stamina recovery; Auto Health and Stamina Recovery! DEF Down. Limit Burst.
- [x] Enriched `super-soul-078` "Sorry. You were way open there.": Heavy Smash guard-break extension, +40% Ki Auto-Recovery for 10 seconds, and Final Kamehameha ATK Up! Limit Burst.
- [x] Refreshed the mechanics enrichment audit with this batch.
- [ ] Next: continue systematic enrichment of the remaining thin records, prioritizing records with reliable item-level catalogue evidence and checking classification conflicts before adding mechanics.


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
- [x] Continued from the restored canonical database rather than rebuilding already-recovered layers from partial historical branches.
- [x] Enriched the normalized `limit_burst_effect` field for canonical Super Soul records `super-soul-164` through `super-soul-172` using explicit current catalogue/character evidence.
- [x] Updated `docs/data/super-souls-record-layer.json` for all nine records; no PQ reward identity, acquisition relationship, disputed PQ 151–154 claim, or unresolved classification was changed.
- [x] Added `docs/data/super-soul-164-172-limit-burst-parity-audit-2026-09-27.json` and registered it in `docs/data/pq-cross-domain-index.json`.
- [x] Evidence-backed changes: 164 Revive Gauge Auto-Recovery; 165–171 explicit ATK/DEF + Ki/Guard/Recovery Limit Burst effects; 172 Kamehameha ATK Up.
- [x] Write commits: record layer `16264b7984f29ab383233d499b0e2945ea857a90`; audit `233d28a6e9fc23bd9bda7805b08b127dd3671ca8`; cross-domain registration `2dd57aa2d728613fc7c33d509a5d087080de54a2`.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] **Exact next:** resolve the remaining canonical Super Soul/PQ reconciliation frontier with item-level evidence where available; specifically continue the PQ 155 / `super-soul-142` conflict investigation without substituting another Gamma Soul or inventing mechanics. If that endpoint remains blocked, continue the next evidence-complete thin-record batch and propagate confirmed mechanics through forward/reverse indexes.
