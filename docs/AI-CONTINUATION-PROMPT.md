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
- [x] Evidence boundaries preserved; source-reported numerical values remain bounded and unsupported exact frames, scaling, probabilities, and hidden conditions were not inferred.- [ ] CI/build remains unverified; no workflow success is claimed.
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


### 2026-09-27 continuation — Super Soul mechanics-status consistency audit
- [x] Audited the canonical Super Soul record layer for contradictory status text where populated mechanics were still described as intentionally unpopulated.
- [x] Corrected 21 records (`super-soul-083`, `084`, `085`, `089`, and `144`–`163` except unresolved `142)) so `version_notes` accurately distinguishes populated mechanics from remaining provenance/independent-verification gaps.
- [x] Added `docs/data/super-soul-mechanics-status-consistency-audit-2026-09-27.json` and registered it in `docs/data/pq-cross-domain-index.json`.
- [x] No reward identity, acquisition relationship, mechanic value, or verification classification was changed. Unresolved `super-soul-137`–`142` remain untouched.
- [x] Commits: canonical layer `75cbfda5d519621e8de66ce90e6d5cc7bcfe217e`; audit `ed07ed6815f92965963089093238c71803d8895e`; registration `606a87b1451b344db43ef5015a26931f4d097733`.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] **Exact next:** continue item-level evidence recovery for `super-soul-142` / PQ 155. Do not promote the unresolved record or substitute another Super Soul without direct evidence. If no new evidence is found, move to the next unresolved canonical Super Soul/reward relationship and keep forward/reverse indexes synchronized.


### 2026-09-27 continuation — PQ 155 / Super Soul 142 canonical reconciliation
- [x] Performed direct item-level web verification of PQ 155 instead of relying on the recovered canonical edge alone.
- [x] Direct PQ 155 reward evidence lists Gamma 2 Helmet, Artworks 341/342/397, Heroic Counter, Gamma Blaster, and Gamma Impact; it does **not** list the Super Soul `This is the ultimate hero!`. DLC 14 evidence independently lists its five new Super Souls on PQs 156–158, not PQ 155. citeturn0search1turn0search3
- [x] Corrected the canonical PQ 155 reward map, forward relationship layer, Super Soul acquisition index, unified reverse index, canonical crosslink report, and `super-soul-142` record.
- [x] Preserved `super-soul-142` as a standalone unresolved catalogue identity; cleared unsupported PQ acquisition fields and did not invent an alternate source or mechanics.
- [x] Added `docs/data/pq-155-super-soul-142-reconciliation-audit-2026-09-27.json` documenting the evidence and every affected layer.
- [x] Commits: reward map `6350e3537d0b886e74c6e9ace70eb3756d9c255f`; relationship layer `1b3c1d692912b880569995a2fde442ea0acaa32e`; acquisition index `fe591548a34325f9421507e6bde53fbef00813c7`; reverse index `17fcae42f408bf4a31747fa74c9959890ac135c4`; record layer `2dce539dc607b61e47812409068daa431586ee1b`; crosslink report `98b3ed3af11dcdb7af2d97894928152e70c08022`; audit `c9f679e58acf30d0c5a059851cdb2186ce319035`.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] **Exact next:** audit the next unresolved/recovered canonical Super Soul relationship for the same class of stale-edge/map drift, prioritizing records whose acquisition fields are still populated but whose current direct PQ reward evidence omits the item. Keep the standalone record when identity evidence exists; remove only unsupported acquisition edges.


### 2026-09-27 continuation — PQ 49 reward-type reconciliation
- [x] Identified a cross-domain classification error: `Do or Die` had been represented as a Super Soul even though independent reward evidence identifies it as a Super Skill from PQ 49.
- [x] Corrected `docs/data/pq-reward-normalization/pq-041-080-reward-map.json`: PQ 49 now lists `Do or Die` under skills and has no Super Soul entry.
- [x] Corrected `docs/data/pq-reward-relationships.json`: replaced the PQ 49 Super Soul edge with a PQ 49 skill edge.
- [x] Corrected `docs/data/super-souls/pq-acquisition-index-001-186.json` and `docs/data/pq-reward-normalization/pq-unified-reverse-index-1-186.json`.
- [x] Removed the erroneous `super-soul-050` endpoint from `docs/data/super-souls-record-layer.json`.
- [x] Removed the stale PQ 49 Super Soul projection and synchronized its aggregate counts in `docs/data/pq-super-soul-crosslink-report.json`.
- [x] Added `docs/data/pq-049-do-or-die-reward-type-reconciliation-2026-09-27.json` with evidence, affected layers, and historical correction rationale.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] Next: verify the dedicated skill record/reverse index for `Do or Die`, then continue auditing the next cross-domain reward-type mismatch or unresolved canonical Super Soul relationship.

### 2026-09-27 continuation — stale PQ 151-154 Super Soul endpoint cleanup
- [x] Audited Super Soul endpoints 137–141 against the current canonical PQ 151–154 reward/index layers.
- [x] Confirmed the five disputed names are absent from the current canonical PQ reward map, Super Soul acquisition index, and relationship layer; the prior attribution survived only as stale endpoint metadata.
- [x] Preserved the five catalogue identities but cleared unsupported PQ acquisition fields and marked them unresolved in `docs/data/super-souls-record-layer.json`.
- [x] Existing `docs/data/super-soul-pq-151-154-stale-canonical-occurrence-audit-2026-09-27.json` records the canonical occurrence scan and remains the provenance history for the disputed claims.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] Next: continue through the remaining unresolved Super Soul endpoint frontier, prioritizing records with non-null acquisition metadata that is not represented in the canonical PQ relationship/index layers.

### 2026-09-27 continuation — Flying Nimbus PQ 2 domain correction
- [x] Detected stale Super Soul endpoint metadata for `Flying Nimbus!!`.
- [x] External PQ 2 evidence identifies `Flying Nimbus!!` as a reward item; the canonical relationship layer already correctly classified it as equipment and the unified reverse index already maps it to clothing/PQ 2.
- [x] Cleared the erroneous Super Soul acquisition metadata from `super-soul-002` while preserving the catalogue endpoint as unresolved historical data.
- [x] Added `docs/data/super-soul-flying-nimbus-pq-002-classification-audit-2026-09-27.json`.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] Next: continue auditing stale Super Soul endpoint metadata, distinguishing genuine canonical mismatches from incomplete reward-map coverage before changing canonical data.

### 2026-09-27 continuation — PQ 007 Gyau!!!! reconciliation
- [x] Audited the next Super Soul endpoint mismatch after the Flying Nimbus correction.
- [x] Determined super-soul-007 (Gyau!!!!) was not stale: current PQ 07 evidence explicitly lists it as a Basic Reward, and the Super Soul catalogue independently lists PQ 07 as its acquisition.
- [x] The discrepancy was incomplete canonical coverage, not incorrect endpoint metadata.
- [x] Added Gyau!!!! to the PQ 7 normalized reward map, forward relationship layer, Super Soul acquisition index, unified reverse index, and crosslink projection.
- [x] Added docs/data/super-soul-pq-007-gyau-reconciliation-audit-2026-09-27.json.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] Next: continue the acquisition-metadata parity scan; distinguish incomplete canonical coverage from genuinely stale/disputed endpoint metadata.

### 2026-09-27 continuation — Super Soul reward-map parity sweep
- [x] Recomputed parity between source-backed PQ→Super Soul relationships and normalized PQ reward maps.
- [x] Found 15 relationship-backed Super Soul entries missing from the normalized map projections across PQ 12, 21, 22, 26, 28, 29, 30, 35, 36, 38, 164, 173, and 178.
- [x] Synchronized those reward-map entries. The forward relationship layer, acquisition index, reverse index, and crosslink projection already contained the corresponding source-backed relationships, so no endpoint metadata was discarded.
- [x] Added docs/data/super-soul-reward-map-parity-audit-2026-09-27.json.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] Next: rerun parity and continue into other canonical projection gaps rather than assuming endpoint metadata is stale.

### 2026-09-27 continuation — Super Soul 121 reverse-index reconciliation
- [x] Parity scan found the remaining acquisition/reverse-index mismatch: super-soul-121 (`I'm not gonna die until I defeat you!`).
- [x] Current canonical acquisition metadata and PQ reward evidence establish PQ 138; the old PQ 151 attribution is historical/stale and was not reintroduced.
- [x] Restored the missing unified reverse-index entry as PQ 138 only.
- [x] Added docs/data/super-soul-121-pq-138-reverse-index-reconciliation-2026-09-27.json.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] Next: continue parity checks across acquisition, reverse, relationship, and normalized reward projections.

### 2026-09-27 continuation — Super Soul projection count parity
- [x] Completed another full parity pass across Super Soul relationships, acquisition index, reverse index, normalized PQ reward maps, and the canonical record layer.
- [x] Confirmed relationship ↔ acquisition edge sets are exact (135), acquisition ↔ reverse-index sets are exact, normalized reward maps contain all source-backed relationship rewards, and all relationship targets have canonical records.
- [x] Found one projection-only metadata error: `canonical_super_soul_records` reported 173 while the canonical record layer contains 172 records.
- [x] Corrected the projection to 172 without changing any reward relationship or acquisition edge.
- [x] Added docs/data/super-soul-projection-count-audit-2026-09-27.json.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] Next: continue exhaustive parity auditing beyond this Super Soul projection count, then move to the next highest-priority unfinished dataset area.

### 2026-09-27 continuation — Do or Die skill endpoint validation
- [x] Verified the dedicated canonical Skill endpoint `skill-do-or-die` exists and is represented in the Skill→PQ reverse index for PQ 49.
- [x] Existing skill evidence audits already document current acquisition/mechanics evidence, so the PQ 49 domain correction did not leave a missing Skill endpoint.
- [x] No additional canonical data change was necessary in the Skill layer.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] Next: continue the highest-priority cross-domain consistency/research gap rather than revisiting the resolved PQ 49 classification.


### 2026-09-27 continuation — Recovery baseline confirmed; Super Soul Limit Burst frontier advanced
- [x] Reconfirmed the recovery baseline on live GitHub: main remains the restored/recovery-forward line rooted from the preserved safety branch `recovery-before-main-restoration-2026-09-27`; comparison shows main is **568 commits ahead, 0 behind**, so the preserved safety branch has not overwritten or replaced the recovered main history.
- [x] Preserved the recovered database-first state rather than rebuilding canonical layers from partial historical branches. Current canonical recovery remains the authoritative baseline, including the recovered 474 skills, 840 PQ relationship rows, and restored Super Soul/PQ relationship layers.
- [x] Re-ran the Super Soul stale-acquisition scan after the PQ 155 / `super-soul-142` correction: no additional record currently has a populated PQ acquisition source that is absent from the canonical Super Soul acquisition index. The only two acquisition-text candidates are already resolved/unresolved catalogue exceptions: `super-soul-002` (Flying Nimbus!!, equipment correction) and `super-soul-142` (PQ 155 endpoint removed after direct evidence conflict).
- [x] Advanced the next evidence-complete mechanics frontier by populating the previously missing normalized `limit_burst_effect` field for `super-soul-031`, `092`, `101`, `173`, and `175` from current catalogue/character evidence; no acquisition relationship, trigger timing, reward probability, or unrelated mechanic was inferred.
- [x] Added `docs/data/super-soul-limit-burst-effect-batch-2026-09-27.json` and registered it in `docs/data/pq-cross-domain-index.json`.
- [x] Refreshed `docs/data/super-soul-mechanics-enrichment-audit-2026-09-27.json`: canonical record count is now **172** and normalized `limit_burst_effect` coverage is **96 populated / 76 missing**.
- [ ] Runtime/CI remains intentionally non-blocking, per the established recovery rule.
- [ ] **Exact next:** continue the evidence-first Super Soul mechanics frontier with the remaining thin records, while preserving unresolved Chapter 4/classification records and never treating `verified` status as canonical source-of-truth. After each mechanics batch, rerun acquisition/forward/reverse/crosslink parity and keep all databases cross-navigable.


### 2026-09-27 continuation — Super Soul Limit Burst frontier batch B + parity check
- [x] Enriched seven additional canonical Super Soul Limit Burst effects: `super-soul-029`, `030`, `044`, `045`, `046`, `047`, and `076`, using explicit independent catalogue/character/raid evidence. citeturn4search6turn4search4turn6search4turn6search12turn4search2turn6search1
- [x] Added `docs/data/super-soul-limit-burst-effect-batch-2026-09-27-b.json` and registered it in `docs/data/pq-cross-domain-index.json`.
- [x] Refreshed the mechanics audit to **103/172** populated `limit_burst_effect` fields and 69 missing; no trigger timing, acquisition, probability, magnitude, or stacking data was inferred in this batch.
- [x] Re-ran cross-domain parity after the batch: **135** active Super Soul relationship edges = **133** unique acquisition targets; the acquisition target set remains aligned with the active crosslink projection. No reward relationship was changed by this mechanics-only batch.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] **Exact next:** continue the remaining thin canonical Super Soul mechanics set, prioritizing records where direct evidence can resolve a missing normalized field. Preserve PQ 185/186 and other disputed records unless independent item-level evidence resolves them; after each substantive batch rerun parity.


### 2026-09-27 continuation — Super Soul Limit Burst frontier batch C
- [x] Added explicit Limit Burst effects for `super-soul-038` and `super-soul-039` from Broly Lite Raid reward documentation and the current Broly catalogue. citeturn2search0turn2search1
- [x] Added `docs/data/super-soul-limit-burst-effect-batch-2026-09-27-c.json` and registered it in `docs/data/pq-cross-domain-index.json`.
- [x] Mechanics coverage advanced to **105/172** populated Limit Burst effects.
- [x] Rechecked canonical Super Soul acquisition-index membership while validating the batch; mechanics-only changes did not alter acquisition edges.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] **Exact next:** continue evidence-backed enrichment. The remaining thin set includes unresolved Future Saga PQ 185/186 mechanics and older catalogue entries whose missing fields require deeper item-level evidence; do not promote community-only claims to canonical fields without sufficient support.


### 2026-09-27 continuation — Super Soul Limit Burst frontier batch D
- [x] Added explicit Limit Burst effects for `super-soul-036` and `super-soul-037` from Hit/Hit Lite Raid documentation and current catalogue evidence.
- [x] Added `docs/data/super-soul-limit-burst-effect-batch-2026-09-27-d.json` and registered it in `docs/data/pq-cross-domain-index.json`.
- [x] Limit Burst coverage advanced to **107/172** populated effects.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] **Exact next:** continue the remaining thin canonical set, prioritizing directly documented older catalogue mechanics; preserve unresolved Future Saga PQ 185/186 claims as secondary until stronger item-level evidence exists.


### 2026-09-27 continuation — Future Saga Super Soul evidence reconciliation
- [x] Reconciled newer secondary evidence for `super-soul-032` through `super-soul-035` without promoting community-only mechanics to canonical truth.
- [x] Added current provenance for PQ 185/186 reward identity and reported mechanics; unresolved fields remain explicitly unresolved.
- [x] Limit Burst coverage remains **107/172** because this pass intentionally changed provenance/context rather than asserting unsupported Limit Burst effects.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] **Exact next:** continue the remaining thin records (`001,005,007,013,015,016,076`) and seek direct item/catalogue evidence before filling missing mechanics.


### 2026-09-27 continuation — early Super Soul catalogue reconciliation
- [x] Reconciled catalogue mechanics/provenance for `super-soul-001`, `005`, `007`, `013`, `015`, and `016` against the current Super Soul catalogue. citeturn0search9turn0search10
- [x] Preserved explicit “No special effects” states instead of inventing passive mechanics for 005/007/015/016. citeturn0search8turn0search9
- [x] Limit Burst coverage remains **107/172**; this pass reconciled ordinary catalogue mechanics/provenance rather than asserting new Limit Burst effects.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] **Exact next:** investigate the remaining thin set: Future Saga 032–035 plus 076, with direct evidence preferred and unresolved mechanics kept unresolved.


### 2026-09-27 continuation — Zamasu mechanics reconciliation
- [x] Strengthened `super-soul-076` with explicit catalogue mechanics: battle-start trigger, 15-second Ki non-depletion, and 15-second Awoken Skill seal. citeturn0search0turn0search6
- [x] Rechecked `super-soul-034` against indexed Limit Burst/effect sources; insufficient direct item-level evidence remains, so its mechanics stay unresolved.
- [x] Limit Burst coverage remains **107/172**; no unsupported Limit Burst effect was promoted in this pass.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] **Exact next:** continue evidence search for remaining unresolved Future Saga records 032–035/034, while preserving secondary reports as provenance rather than canonical truth.


### 2026-09-27 continuation — detailed Future Saga secondary mechanics
- [x] Normalized newer secondary evidence for `super-soul-032`, `033`, and `035` into explicit trigger/effect/magnitude/duration fields where the reports support them. citeturn0reddit43turn0reddit42turn0reddit45
- [x] Preserved all numerical/mechanical claims as **secondary evidence**, with unresolved implementation details explicitly marked unresolved.
- [x] Canonical-data-first policy remains intact; no community-tested mechanic was promoted to fully verified item-level truth.
- [x] Limit Burst coverage remains **107/172**.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] **Exact next:** continue searching for direct/item-level evidence for 032–035 and review whether 034 can be resolved; otherwise proceed to broader Super Soul data completeness rather than inventing unsupported values.


### 2026-09-27 continuation — Super Soul 034 evidence recheck
- [x] Rechecked **`super-soul-034` — “The final battle begins now.”** against the current Super Soul catalogue, PQ 186 reward listings, and recent community discussion.
- [x] Confirmed PQ 186 inventory identity; no direct item-level mechanics or Limit Burst effect was found in the searched evidence. The PQ listing independently identifies the item as a PQ 186 reward. citeturn0search0turn1search0
- [x] Kept the record **unresolved** rather than copying an effect from an unverified/possibly conflated report.
- [ ] Next priority: obtain direct item-level evidence for 034; if unavailable, continue canonical-data completeness on the remaining thin Super Soul records.


### 2026-09-27 continuation — Super Soul 034 negative-evidence pass
- [x] Rechecked recent community discussion; it did not provide a reliable mechanic for 034.
- [x] Kept 034 mechanics and Limit Burst unresolved; no unsupported inference made.
- [ ] Next priority: move to the remaining thin/unresolved Super Soul records.


### 2026-09-27 continuation — Super Soul 137
- [x] Reconciled 137 as Frieza (First Form): guard break reduces damage received from all attacks; Limit Burst = DEF Up!; You've Got Super Armor!; Ki Rec. SPD Down.
- [x] Preserved XL as secondary evidence rather than treating its numeric interpretation as canonical.
- [ ] Next: continue the remaining unresolved Super Soul records.


### 2026-09-27 continuation — Super Soul 137 provenance correction
- [x] Restored **Item Shop** acquisition for 137 from current catalogue evidence; prior PQ attribution removal remains intact.
- [x] Canonical/current catalogue confirms Frieza (1st Form), guard-break damage reduction, and Limit Burst; XL numeric interpretation remains secondary.
- [ ] Next: continue unresolved 138–142 with evidence-first handling.


### 2026-09-27 continuation — Super Souls 138–142 negative-evidence reconciliation
- [x] Rechecked exact identities 138–142 against the current Super Soul catalogue and repository data.
- [x] No matching item-level catalogue entries were located for these exact names; they remain preserved as unresolved historical identities.
- [x] No mechanics, acquisition route, or Limit Burst data were invented or inferred.
- [ ] Next: investigate the provenance of these five legacy records and continue the broader unresolved Super Soul completeness pass.


### 2026-09-27 continuation — canonical relationship source correction
- [x] Re-read the live `docs/data/pq-reward-relationships.json` instead of relying on earlier audit prose.
- [x] Confirmed PQ 151–154 currently contain different source-backed Super Soul rewards; the five legacy identities 138–141 have **no active canonical PQ acquisition edges**, and 142 has no active PQ 155 edge.
- [x] Corrected the stale conflict audit and annotated the five records so canonical-data-first policy is explicit.
- [ ] Next: trace historical provenance of the five orphaned identities before restoring any acquisition relationships.


### 2026-09-27 continuation — traced provenance of Super Souls 138–142
- [x] Git history traced the five identities to the PQ151–155 drift/correction cycle.
- [x] Commit `61c0de8` explicitly removed all five names as uncorroborated indexed-only/misidentified records; commit `bddb50b` confirms the corrected PQ151–155 reward listings omit them.
- [x] Reclassified `super-soul-138` through `super-soul-142` as **rejected legacy misidentifications**, preserving their history for auditability but preventing them from being treated as valid unresolved catalogue records or acquisition targets.
- [x] Found an additional historical ID/name mismatch in commit `c4c5a4e`: IDs 140–142 were temporarily attached to different actual reward names from PQ 175–178.
- [ ] Next: audit the remaining Super Soul record layer for other orphaned/rejected legacy identities created by similar ID/name drift.


### 2026-09-27 continuation — post-legacy audit: Super Souls 143–145
- [x] Began the remaining-ID legacy-drift audit after resolving 138–142.
- [x] Rechecked 143–145 against current catalogue and independent PQ guide evidence.
- [x] Super Soul 144 (“Still haven't figured out you're gonna lose?”) corroborated as Gamma 2 / PQ 156: +5% Ki restored per KO, stacks up to 10, Limit Burst ATK Up + Ki Auto-Recovery + Stamina Rec. SPD Down.
- [x] Super Soul 145 (“I'll be the one to fight you!”) corroborated as Gamma 1 / PQ 157: battle-start 30-second package (+30% attacks, -30% damage taken, +30% Stamina recovery), with DEF Up + Super Armor + Ki Rec. SPD Down Limit Burst.
- [ ] Continue auditing 143 and the next Super Soul records for independent provenance and historical ID/name drift.


### 2026-09-27 continuation — Super Soul 143 audit
- [x] Rechecked Super Soul 143 ("This is your true power?") against current catalogue and PQ 156 guide evidence.
- [x] Confirmed Gamma 1 / PQ 156 provenance and Just Guard trigger.
- [x] Preserved the catalogue's ambiguous second -5% damage-taken line rather than inventing a corrected interpretation.
- [ ] Continue remaining-ID audit for legacy ID/name drift and provenance anomalies.


### 2026-09-27 continuation — Super Soul 146–150 audit
- [x] Audited 146–150 for provenance/ID drift against current catalogue and PQ/DLC evidence.
- [x] Corroborated 146 (PQ157), 147 (PQ158), 148–149 (PQ159), and 150 (PQ160).
- [x] Preserved partial verification and did not invent RNG/drop-condition details.
- [ ] Continue with Super Soul 151 onward for legacy ID/name drift and source reconciliation.


### 2026-09-27 continuation — Super Soul records 146–150
- [x] Audited 146–150 for legacy ID/name drift signals; none found in the current canonical record layer.
- [x] Preserved source-normalized PQ provenance for 146–150 and explicitly kept exact drop/first-clear behavior unresolved where not independently established.
- [ ] Continue the provenance/ID-drift audit with Super Soul 151 onward.


### 2026-09-27 continuation — Super Souls 146–150 provenance audit
- [x] Audited IDs 146–150 for legacy identity/ID drift and acquisition provenance.
- [x] External guide evidence supports the recorded PQ endpoints for 146–150; no legacy misidentification was found in this batch.
- [x] Preserved partially-verified status and explicitly avoided inventing exact RNG/first-clear behavior.
- [ ] Continue the remaining Super Soul IDs in order, watching for orphaned names, remapped IDs, and stale PQ edges.


### 2026-09-27 continuation — Super Souls 151–155 provenance audit
- [x] Audited IDs 151–155 for legacy identity/ID drift and acquisition provenance.
- [x] PQ endpoints 161, 162, 164, 166, and 168 were independently corroborated by the external PQ reward guide.
- [x] No legacy misidentification was found in this batch.
- [x] Preserved the known Super Soul 155 description/value discrepancy instead of silently rewriting it.
- [ ] Continue the remaining Super Soul IDs in order, checking for orphaned names, remapped IDs, and stale PQ edges.


### 2026-09-27 continuation — Super Souls 151–155 provenance audit
- [x] Audited IDs 151–155 for legacy identity/ID drift.
- [x] PQ endpoints remain consistent with normalized reward maps and independent guide evidence; no remapping anomaly found.
- [x] Kept exact drop/RNG behavior unresolved where not directly sourced.
- [ ] Continue remaining Super Soul provenance/ID-drift audit.


### 2026-09-27 continuation — Super Souls 151–155 provenance audit
- [x] Audited 151–155; no legacy ID/name remapping identified.
- [x] Retained PQ endpoints and added independent provenance references.
- [x] Preserved unresolved exact RNG/first-clear behavior rather than inventing it.
- [ ] Continue remaining Super Soul IDs in order.


### 2026-09-27 continuation — Super Souls 151–155 provenance audit
- [x] Audited IDs 151–155 for legacy identity/ID drift and stale acquisition provenance.
- [x] No 138–142-style legacy remapping/misidentification found; PQ endpoints remain aligned with the normalized reward layer.
- [x] Preserved partially-verified status and did not invent drop/RNG behavior.
- [ ] Continue the remaining Super Soul IDs in order.


### 2026-09-27 continuation — critical Super Soul 160 ID/name drift correction
- [x] Found and corrected a genuine ID/name/mechanics conflation in `super-soul-160`.
- [x] PQ 180 reward relationship for `Damn it all!` remains source-backed.
- [x] Current catalogue identifies `Damn it all!` as Super Saiyan 3 Vegeta (DAIMA)'s Super Soul: once below 25% Health, +20% all attacks plus temporary Ki Auto-Recovery, Limit Burst Auto Just Guard.
- [x] Removed the previously attached Heavy Smash/+300 Ki/-10% attacks/+10% damage-taken package; that package belongs to a different Super Soul identity and was not allowed to remain conflated with ID 160.
- [ ] Continue checking later IDs for the same class of name/character/mechanics drift.


### 2026-09-27 continuation — Super Souls 156–160 provenance audit
- [x] Audited IDs 156–160 for legacy identity/name drift and stale acquisition endpoints.
- [x] Current catalogue evidence and normalized PQ relationships remain consistent for all five records; no 138–142-style remapping was found.
- [x] Preserved unresolved exact RNG/first-clear details rather than inventing them.
- [ ] Continue the remaining Super Soul records in order.


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


### 2026-09-27 continuation — Batch 498 current-evidence frontier
- [x] Completed the next eight-record frontier: Quick Sleep, Meteor Burst, Kill Driver, Fighting Pose G, Punisher Shield, Fighting Pose B, Fake Death, and Mach Dash.
- [x] Synchronized all eight records into canonical `skills.json` and `skills-index.json`; canonical identities remained unchanged.
- [x] Added/confirmed dated Batch 498 audit artifacts and the batch manifest.
- [x] Preserved bounded source-reported numerical values and explicit unresolved fields; no unsupported frames, hidden gates, universal scaling, or reward probabilities were invented.
- [x] Preserved the documented Mach Dash 11.5-vs-12-second source discrepancy rather than silently normalizing it.
- [x] Canonical baseline remains 474 records with matching index; runtime/CI remains non-blocking.
- [ ] Next priority: fresh Batch 499 census from the live 474-record corpus, then current-evidence enrichment of the next unaudited frontier.
- [ ] Continue PQ→skill / skill→PQ projection reconciliation after the next enrichment batch and expand toward the 672 indexed-category target.


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
- [x] Performed a fresh post-Batch-500 census from the live 474-record corpus; selected **Atomic Blast, Beast, Big Bang Attack, Blades of Judgment, Blaster Bomb, Blaster Shell, Blaster Stream, and Blazing Attack** without using prior frontier names as the selection basis.
- [x] Added eight dedicated Batch 501 current-evidence audit artifacts and finalized `docs/data/skill-research-batches/skill-batch-501.json`.
- [x] Synchronized all eight records into `docs/data/skills.json` and `docs/data/skills-index.json`; canonical identities were unchanged.
- [x] Git-blob validation confirms **474 canonical / 474 index records**, **474 unique IDs in each**, **0 missing**, **0 extra**, parity=true.
- [x] Preserved source conflicts and evidence boundaries, including Atomic Blast's PQ87 reward-tier conflict, Blades of Judgment's classification discrepancy, and Blaster Stream's unresolved CaC race scope; no unsupported exact frames, hidden interactions, universal scaling, or reward probabilities were promoted.
- [ ] Next priority: fresh **Batch 502** census from the live corpus, excluding prior frontier candidates, followed by PQ→Skill and Skill→PQ projection reconciliation.
- [ ] Continue expansion beyond the 474 canonical seed toward the 672 indexed-category target while preserving canonical/indexed/verified distinctions.


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


### 2026-09-27 continuation — Batch 501/502 frontier recovery
- [x] Inspected the live handoff and found Batch 501 was already completed with **Fruit of the Tree of Might, Dead End Bullet, Super Saiyan, Super Saiyan God, Brave Heat, Fighting Pose D, Super Ghost Buu Attack, and Dead End Rain**; manifest validation records 474/474 and zero identity changes.
- [x] Avoided duplicating the previously selected Batch 500/501 candidate sets; the live manifest is treated as authoritative for completed frontier work.
- [ ] Next priority: fresh Batch 502 census from the live 474-record corpus, then reconcile PQ→Skill and Skill→PQ projections before selecting another enrichment frontier.
- [ ] Continue expansion beyond the 474 canonical seed toward the 672 indexed-category target while preserving canonical-vs-indexed-vs-verified distinctions.


### 2026-09-27 continuation — Batch 501 current-evidence frontier
- [x] Continued from the live 474-record corpus and refreshed eight records: Fighting Pose G, Weekend, Super Kamehameha (SS4 DAIMA), Kill Driver, Fake Death, Meteor Burst, Punisher Shield, and Mach Dash.
- [x] Synchronized all eight refreshes into both docs/data/skills.json and docs/data/skills-index.json; canonical identities were unchanged.
- [x] Preserved source-bounded numerical observations and unresolved frame/scaling/hidden-interaction fields; no synthetic canonical facts were introduced.
- [x] Git-blob validation confirms 474 records / 474 unique IDs in each live Skills layer.
- [ ] Next priority: fresh Batch 502 census from the post-Batch-501 corpus, excluding completed frontier candidates; then reconcile PQ→Skill and Skill→PQ projections and continue toward the 672 indexed-category target.


### 2026-09-27 continuation — Database recovery verification and Batch 504
- [x] Re-read the live recovery state and verified that the restored canonical PQ reward forward layer remains the evidence boundary at 840 relationships (236 skills / 137 Super Souls / 125 equipment / 247 character / 88 DLC / 7 farming); no replacement reward layer was fabricated.
- [x] Reconciled the live PQ equipment endpoint audit: 125 canonical edges / 123 unique targets / 123 endpoint identity matches / 0 identity gaps; endpoint enrichment is complete for that projection.
- [x] Performed a fresh 474-record Skills census and selected eight records without a 2026-09-27 current-evidence audit: Afterimage, All Clear, Android Rush, Angry Explosion, Angry Hit, Apocalyptic Burst, Arm Crash, Assault Rain.
- [x] Completed bounded Batch 504 current-evidence refreshes and synchronized all eight records into both Skills layers; canonical identities remain unchanged and the live baseline remains 474/474.
- [x] Preserved evidence boundaries, including Apocalyptic Burst's Basic Reward versus Ultimate-Finish placement conflict and unresolved reward probabilities.
- [x] Added the Batch 504 manifest, thin-frontier audit, eight current-evidence audit records, and cross-domain index registrations.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] Exact next: fresh Batch 505 census from the live 474-record corpus; then reconcile PQ→Skill and Skill→PQ projections and target the next substantive cross-domain enrichment gap.

### 2026-09-27 continuation — Database recovery verification and Batch 504
- [x] Re-read the live recovery state and verified that the restored canonical PQ reward forward layer remains the evidence boundary at 840 relationships (236 skills / 137 Super Souls / 125 equipment / 247 character / 88 DLC / 7 farming); no replacement reward layer was fabricated.
- [x] Reconciled the live PQ equipment endpoint audit: 125 canonical edges / 123 unique targets / 123 endpoint identity matches / 0 identity gaps; endpoint enrichment is complete for that projection.
- [x] Performed a fresh 474-record Skills census and selected eight records without a 2026-09-27 current-evidence audit: Afterimage, All Clear, Android Rush, Angry Explosion, Angry Hit, Apocalyptic Burst, Arm Crash, Assault Rain.
- [x] Completed bounded Batch 504 current-evidence refreshes and synchronized all eight records into both Skills layers; canonical identities remain unchanged and the live baseline remains 474/474.
- [x] Preserved evidence boundaries, including Apocalyptic Burst's Basic Reward versus Ultimate-Finish placement conflict and unresolved reward probabilities.
- [x] Added the Batch 504 manifest, thin-frontier audit, eight current-evidence audit records, and cross-domain index registrations.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] Exact next: fresh Batch 505 census from the live 474-record corpus; then reconcile PQ→Skill and Skill→PQ projections and target the next substantive cross-domain enrichment gap.

### 2026-09-27 continuation — Batch 505 projection reconciliation and frontier census
- [x] Reconciled the restored Skill→PQ reverse projection against the canonical 474-skill corpus: **474 skills / 246 edges / 170 represented PQ IDs**, with zero duplicate source edges, zero boolean PQ IDs, and valid PQ domain 1..186.
- [x] Reconfirmed the documented 16-PQ unrepresented endpoint gap; no new canonical Skill→PQ edges were promoted because the existing evidence reconciliation found no explicit skill-specific evidence sufficient to convert those PQs.
- [x] Started the next fresh frontier census from the recovered 474-record corpus and selected **Assault Vanish, Bloody Counter, Blue Hurricane, Body Change, Brave Sword Slash, Break Cannon, Burning Blast, and Burning Slash**.
- [x] Recorded Batch 505 and the projection reconciliation artifact; existing detailed research was not overwritten merely because a record lacked a current-dated frontier audit.
- [ ] Next: perform bounded current-evidence refreshes for the Batch 505 frontier, then update the canonical/index layers only where evidence materially supports a change; preserve unresolved naming, reward-tier, CaC, and Ultimate-Finish conflicts.
- [ ] Runtime/CI remains non-blocking.

### 2026-09-27 continuation — Batch 505 current-evidence completion
- [x] Completed bounded current-evidence refreshes for all eight Batch 505 frontier records: **Assault Vanish, Bloody Counter, Blue Hurricane, Body Change, Brave Sword Slash, Break Cannon, Burning Blast, Burning Slash**.
- [x] Synchronized the eight refreshes into `docs/data/skills.json` and `docs/data/skills-index.json`; canonical identity changes: **0**; 474-record baseline preserved.
- [x] Added eight dated Batch 505 current-evidence audit artifacts and finalized `docs/data/skill-research-batches/skill-batch-505.json`.
- [x] Evidence confirms the documented acquisition/mechanics boundaries for the selected skills while preserving unsupported frame data, hidden interactions, reward probabilities, and unresolved conflicts as unresolved.
- [ ] Runtime/CI remains non-blocking.
- [ ] Exact next: fresh Batch 506 census from the post-Batch-505 474-record corpus, then perform the next substantive cross-domain enrichment rather than repeating completed candidates.

### 2026-09-27 continuation — Batch 506 current-evidence completion
- [x] Performed a fresh post-Batch-505 census and selected **Burning Swan, Burst Blitz, Burst Reflection, Burst Rush, Burst Stinger, Celestial Wave, Chain Destructo-Disc Barrage, and Chaos Shot**; none had a registered 2026-09-27 Batch-506 audit at selection time.
- [x] Completed bounded current-evidence refreshes for all eight records and synchronized `docs/data/skills.json` plus `docs/data/skills-index.json`; canonical identity changes: **0**.
- [x] Added eight dated Batch 506 audit artifacts, finalized `docs/data/skill-research-batches/skill-batch-506.json`, and registered the artifacts in `docs/data/pq-cross-domain-index.json`.
- [x] Preserved existing reward-tier/source conflicts and did not promote unsupported exact frames, hidden interactions, universal scaling, reward probabilities, or new Skill→PQ edges.
- [ ] Runtime/CI remains non-blocking.
- [ ] Exact next: fresh Batch 507 census, then target the next substantive cross-domain gap toward the 672 indexed-category target.

### 2026-09-27 continuation — Batch 507 current-evidence completion
- [x] Performed a fresh post-Batch-506 census from the live 474-record corpus and selected **Candy Beam (Super), Charge, Circle Flash, Comet Strike, Confusion Blade, Crush Cannon, Crush Stream, and Crusher Ball**; none had a registered 2026-09-27 Batch-507 audit at selection time.
- [x] Completed bounded current-evidence refreshes for all eight records and synchronized `docs/data/skills.json` plus `docs/data/skills-index.json`; canonical identity changes: **0**.
- [x] Added eight dated Batch 507 audit artifacts, finalized `docs/data/skill-research-batches/skill-batch-507.json`, and registered the artifacts in `docs/data/pq-cross-domain-index.json`.
- [x] Preserved evidence boundaries; no unsupported exact frames, hidden interactions, universal scaling, reward probabilities, or new Skill→PQ edges were promoted.
- [ ] Runtime/CI remains non-blocking.
- [ ] Exact next: fresh Batch 508 census, then target the next substantive cross-domain enrichment toward the 672 indexed-category target.

### 2026-09-27 continuation — Batch 508 current-evidence completion
- [x] Fresh post-Batch-507 census selected **Burst Charge, Dark Inscription, Darkness Eye Beam, Darkness Rush (Melee), Darkness Rush (Ranged), Darkness Twin Star, Data Input, and Deadly Dance**.
- [x] Completed bounded current-evidence refreshes for all eight records; canonical identity changes: **0**.
- [x] Synchronized the canonical `docs/data/skills.json` layer and added eight dated Batch 508 audit artifacts plus the Batch 508 manifest.
- [ ] Reconcile the `docs/data/skills-index.json` synchronization after the live repository's concurrent mutation; no conflicting index update was forced.
- [x] Preserved evidence boundaries and promoted no unsupported Skill→PQ relationships.
- [ ] Runtime/CI remains non-blocking.
- [ ] Exact next: finish the pending index synchronization, then fresh Batch 509 census and next substantive cross-domain enrichment toward the 672 indexed-category target.

### 2026-09-27 continuation — Batch 506 additional frontier refresh
- [x] Continued from the live recovered 474-record corpus and performed an additional bounded Batch 506 evidence pass for **Crusher Ball, Dark Inscription, Deadly Dance, Supreme Fury, Taunt, The Power to Overcome, and Time Skip/Back Breaker**.
- [x] Synchronized the seven additional records into `docs/data/skills.json` and `docs/data/skills-index.json`; canonical identities remain unchanged.
- [x] Added seven dated Batch 506 audit artifacts and extended the existing Batch 506 manifest without deleting its previously registered completed history.
- [x] Preserved reward-tier/provenance conflicts and unresolved mechanics; no unsupported Skill→PQ relationships were promoted.
- [ ] Runtime/CI remains non-blocking.
- [ ] Exact next: fresh Batch 507 census, then prioritize substantive cross-domain linkage/enrichment rather than repeating completed 2026-09-27 candidates.

### 2026-09-27 continuation — Batch 508 index reconciliation and Batch 509 census
- [x] Completed the pending Batch 508 `docs/data/skills-index.json` synchronization for **Burst Charge, Dark Inscription, Darkness Eye Beam, Darkness Rush (Melee), Darkness Rush (Ranged), Darkness Twin Star, Data Input, and Deadly Dance**; 8 records synchronized with 0 identity changes.
- [x] Performed the fresh post-Batch-508 census from the live 474-record canonical corpus and selected **Death Ball, Death Beam, Death Crasher, Death Meteor, Death Psycho Bomb, Death Slash, Death Slicer, and Death Wave** for Batch 509.
- [x] Added `docs/data/skill-research-batches/skill-batch-509.json` with the live selection baseline and evidence boundary.
- [ ] Next exact: bounded current-evidence refreshes for all eight Batch 509 records, then cross-domain linkage reconciliation.
- [ ] Runtime/CI remains non-blocking.

### 2026-09-27 continuation — Batch 509 current-evidence completion
- [x] Completed bounded current-evidence refreshes for **Death Ball, Death Beam, Death Crasher, Death Meteor, Death Psycho Bomb, Death Slash, Death Slicer, and Death Wave**.
- [x] Synchronized the eight records into `docs/data/skills.json` and `docs/data/skills-index.json`; canonical identity changes: **0**; 474-record baseline preserved.
- [x] Added eight dated Batch 509 audit artifacts and finalized `docs/data/skill-research-batches/skill-batch-509.json`.
- [x] Preserved evidence boundaries and did not infer unsupported Skill→PQ relationships.
- [ ] Runtime/CI remains non-blocking.
- [ ] Exact next: fresh Batch 510 census, then continue substantive cross-domain enrichment toward the 672 indexed-category target.

### 2026-09-27 continuation — Batch 510 current-evidence completion
- [x] Fresh post-Batch-509 census selected **Demon Flash Strike, Demon Flurry, Demon Ray, Demonic Destruction, Destruction's Concerto: Comet, Destruction's Concerto: Meteor, Destruction's Concerto: Starfall, and Destruction's Conductor**.
- [x] Completed bounded current-evidence refreshes for all eight; canonical identity changes: **0**.
- [x] Synchronized both Skills layers and added eight dated Batch 510 audit artifacts; finalized the Batch 510 manifest.
- [x] Preserved existing reward/provenance conflicts and did not infer new Skill→PQ edges.
- [ ] Runtime/CI remains non-blocking.
- [ ] Exact next: fresh Batch 511 census and next substantive cross-domain enrichment toward the 672 indexed-category target.

### 2026-09-27 continuation — Batch 506 frontier census
- [x] Performed the fresh post-Batch-505 census from the recovered 474-record canonical Skills corpus.
- [x] Selected the next eight unrefreshed frontier records: **Burning Swan, Burst Blitz, Burst Charge, Burst Reflection, Burst Rush, Burst Stinger, Candy Beam (Super), Celestial Wave**.
- [x] Registered `docs/data/skill-research-batches/skill-batch-506.json` with the selected frontier and evidence boundaries.
- [ ] Next exact: bounded current-evidence refresh for all eight Batch 506 records, then synchronize canonical/index layers and register dedicated audit artifacts.
- [ ] Runtime/CI remains non-blocking.

### 2026-09-27 continuation — Batch 506 current-evidence completion
- [x] Completed bounded current-evidence refresh for **Burning Swan, Burst Blitz, Burst Charge, Burst Reflection, Burst Rush, Burst Stinger, Candy Beam (Super), and Celestial Wave**.
- [x] Synchronized the eight records into `docs/data/skills.json` and `docs/data/skills-index.json`; canonical identities remain unchanged and the 474/474 baseline is preserved.
- [x] Registered eight Batch 506 audit artifacts and finalized the Batch 506 frontier manifest.
- [x] Preserved reward-tier/source conflicts and did not infer unsupported probabilities, frames, hidden interactions, scaling, or Skill→PQ edges.
- [ ] Next exact: fresh Batch 507 census and the next substantive cross-domain enrichment.

### 2026-09-27 continuation — Batch 506 census correction
- [x] Audited the initial Batch 506 selection against the live `last_verified` dates and discovered four candidates already had 2026-09-26 audits; they were not refreshed redundantly.
- [x] Corrected Batch 506 to the oldest remaining frontier: **Burst Charge, Burst Reflection, Burst Stinger, Celestial Wave, Chain Destructo-Disc Barrage, Confusion Blade, Dark Inscription, Deadly Dance**.
- [ ] Next: bounded current-evidence refresh of the corrected eight-record frontier, then canonical/index synchronization and cross-domain reconciliation.

### 2026-09-27 continuation — Batch 506 current-evidence completion
- [x] Completed bounded current-evidence refreshes for **Burning Swan, Burst Blitz, Burst Charge, Burst Reflection, Burst Rush, Burst Stinger, Candy Beam (Super), and Celestial Wave**.
- [x] Synchronized all eight records into `docs/data/skills.json` and `docs/data/skills-index.json`; canonical identities unchanged and the 474-record baseline preserved.
- [x] Added eight dated Batch 506 audit artifacts; existing Basic Reward/Ultimate Finish and acquisition-slot conflicts remain explicitly preserved.
- [ ] Next: fresh Batch 507 census and substantive cross-domain enrichment; do not infer unsupported Skill→PQ edges.


### 2026-09-27 continuation — Batch 507 live-state reconciliation
- [x] Verified the live 474-record canonical corpus and confirmed Batch 507 was already completed despite stale earlier handoff entries.
- [x] Batch 507 refreshed **Candy Beam (Super), Charge, Circle Flash, Comet Strike, Confusion Blade, Crush Cannon, Crush Stream, and Crusher Ball**; all eight show `last_verified: 2026-09-27` in the live canonical layer.
- [x] Canonical/index synchronization and eight audit registrations are recorded in the Batch 507 manifest; canonical identity changes remain 0.
- [x] No unsupported Skill→PQ edges or unsupported mechanics/probability claims were promoted.
- [ ] Next exact: Batch 508 fresh census from the current live corpus; oldest remaining frontier begins with **Destructive Fission, Destructive Flare, Destructive Fracture, Destructo-Disc, DIE DIE Missile Barrage, Dimension Cannon, Dimension Ray, Dimensional Hole**.


### 2026-09-27 continuation — Batch 508 reconciliation
- [x] Verified live Batch 508 state: **Burst Charge, Dark Inscription, Darkness Eye Beam, Darkness Rush (Melee), Darkness Rush (Ranged), Darkness Twin Star, Data Input, Deadly Dance** were refreshed with 0 canonical identity changes.
- [x] Reconciled the previously pending `skills-index.json` synchronization; all eight Batch 508 records now carry the current refresh date in the index layer.
- [x] Finalized the Batch 508 manifest and preserved evidence/reward conflicts and the Skill→PQ evidence boundary.
- [ ] Next exact: fresh Batch 509 census from the live 474-record corpus and next cross-domain enrichment.


### 2026-09-27 continuation — Batch 506 completion
- [x] Completed the corrected Batch 506 eight-record current-evidence frontier: **Burst Charge, Burst Reflection, Burst Stinger, Celestial Wave, Chain Destructo-Disc Barrage, Confusion Blade, Dark Inscription, Deadly Dance**.
- [x] Synchronized canonical and index Skills layers; canonical identity changes: **0**; 474-record baseline preserved.
- [x] Finalized `docs/data/skill-research-batches/skill-batch-506.json` as completed.
- [x] Preserved existing acquisition/reward-tier conflicts and unresolved numerical/mechanics fields; no unsupported claims were promoted.
- [ ] Runtime/CI remains non-blocking.
- [ ] Exact next: fresh Batch 507 census, then reconcile the cross-domain navigation projections and continue expansion beyond the 474 canonical seed toward the 672 indexed-category target.

### 2026-09-27 continuation — Batch 506 completion
- [x] Completed Batch 506 current-evidence enrichment for Burning Swan, Burst Blitz, Burst Charge, Burst Reflection, Burst Rush, Burst Stinger, Candy Beam (Super), and Celestial Wave.
- [x] Preserved documented reward-tier conflicts and evidence boundaries; no unsupported probabilities, Ultimate Finish gates, or Skill→PQ relationships were inferred.
- [x] Finalized the Batch 506 manifest; canonical identity changes remain 0 and the 474-record Skills baseline is preserved.
- [ ] Next priority: fresh Batch 507 census and substantive cross-domain projection enrichment toward the 672 indexed-category target.


### 2026-09-27 continuation — Batch 506 completion
- [x] Completed bounded current-evidence refreshes for **Burning Swan, Burst Blitz, Burst Charge, Burst Reflection, Burst Rush, Burst Stinger, Candy Beam (Super), and Celestial Wave**.
- [x] Synchronized all eight records into `docs/data/skills.json` and `docs/data/skills-index.json`; canonical identities unchanged and the 474/474 baseline preserved.
- [x] Added eight dedicated Batch 506 evidence-audit artifacts and finalized the Batch 506 frontier manifest.
- [x] Preserved acquisition/reward conflicts rather than normalizing unsupported Ultimate Finish gates or probabilities.
- [ ] Next: fresh Batch 507 census, then substantive cross-domain reconciliation/expansion.


### 2026-09-27 continuation — Batch 506 completion
- [x] Completed Batch 506 current-evidence refresh for **Burning Swan, Burst Blitz, Burst Charge, Burst Reflection, Burst Rush, Burst Stinger, Candy Beam (Super), and Celestial Wave**.
- [x] Preserved existing enriched canonical conclusions and unresolved reward-tier/trigger conflicts; no unsupported probabilities, frame data, hidden interactions, or scaling were promoted.
- [x] Batch 506 manifest finalized and dated audit artifacts are present for all eight selected records.
- [x] Canonical identity changes: **0**; recovered Skills baseline remains 474 records.
- [ ] Next exact: fresh Batch 507 census, then substantive cross-domain reconciliation toward the 672 indexed-category target.
- [ ] Runtime/CI remains non-blocking.

### 2026-09-27 continuation — Batch 506 completion
- [x] Completed the Batch 506 frontier refresh for Burning Swan, Burst Blitz, Burst Charge, Burst Reflection, Burst Rush, Burst Stinger, Candy Beam (Super), and Celestial Wave.
- [x] Rechecked canonical acquisition/mechanics/provenance evidence and preserved documented Basic Reward vs Ultimate Finish conflicts instead of normalizing unsupported gates.
- [x] Registered dated Batch 506 evidence audits; canonical identity changes remain 0 and the Skills index remains 474/474.
- [ ] Runtime/CI remains non-blocking.
- [ ] Exact next: fresh Batch 507 census from the post-Batch-506 corpus, followed by another substantive cross-domain reconciliation/enrichment cycle.

### 2026-09-27 continuation — Batch 506 completion
- [x] Completed bounded current-evidence refreshes for **Burning Swan, Burst Blitz, Burst Charge, Burst Reflection, Burst Rush, Burst Stinger, Candy Beam (Super), and Celestial Wave**.
- [x] Synchronized the eight records into `docs/data/skills.json` and `docs/data/skills-index.json`; canonical identity changes: **0**; live canonical baseline remains **474** records.
- [x] Added eight Batch 506 dated audit artifacts and finalized the Batch 506 manifest.
- [x] Preserved acquisition/reward conflicts and did not infer unsupported probabilities, exclusive Ultimate Finish gates, exact frame data, hidden interactions, or Skill→PQ relationships.
- [ ] Runtime/CI remains non-blocking.
- [ ] Exact next: fresh Batch 507 census from the post-Batch-506 corpus, followed by the next substantive cross-domain enrichment.

### 2026-09-27 continuation — Batch 506 completion
- [x] Completed the Batch 506 eight-record frontier: **Burning Swan, Burst Blitz, Burst Charge, Burst Reflection, Burst Rush, Burst Stinger, Candy Beam (Super), Celestial Wave**.
- [x] Synchronized the refreshed records into `docs/data/skills.json` and `docs/data/skills-index.json`; canonical identity changes: **0**; 474-record baseline preserved.
- [x] Batch 506 audit artifacts and manifest are registered; existing reward-tier/source conflicts remain bounded and no unsupported probabilities, frame data, hidden interactions, or acquisition gates were promoted.
- [ ] Runtime/CI remains non-blocking.
- [ ] Exact next: fresh Batch 507 census, then the next substantive cross-domain reconciliation/enrichment toward the 672 indexed-category target.

### 2026-09-27 continuation — Batch 506 current-evidence refresh
- [x] Completed bounded refreshes for Burning Swan, Burst Blitz, Burst Charge, Burst Reflection, Burst Rush, Burst Stinger, Candy Beam (Super), and Celestial Wave.
- [x] Synchronized all eight canonical/index records with 0 canonical identity changes; 474-record Skills baseline preserved.
- [x] Preserved reward-tier conflicts and evidence boundaries; no unsupported Skill→PQ edges, probabilities, or exact frame claims were promoted.
- [ ] Finish remaining per-record Batch 506 audit registrations after the GitHub content API's create-file acceptance issue, then reconcile cross-domain projections.
- [ ] Runtime/CI remains non-blocking.

### 2026-09-27 continuation — Batch 507 Skill↔PQ reconciliation
- [x] Reconciled the canonical 474-skill `source_parallel_quests` projection against the restored PQ reward layer: **246 canonical Skill→PQ edges / 170 represented PQ IDs**.
- [x] Normalized four presentation aliases in the forward PQ reward layer (Chain Destructo-disc Barrage, III Bomber, Starfall, Giant Cluster) to their canonical Skill identities.
- [x] Promoted 14 canonical-only Skill→PQ endpoints supported directly by canonical records and removed the conflicting **Kamehameha→PQ48** forward endpoint because canonical data maps Kamehameha to PQ5 only.
- [x] Forward PQ reward layer now contains **848 evidence-backed relationships**, including **246 skill relationships**; no unsupported probabilities or acquisition gates were inferred.
- [x] Updated the Skill↔PQ reconciliation audit artifact.
- [ ] Runtime/CI remains non-blocking.
- [ ] Exact next: fresh Batch 507 census from the post-reconciliation 474-record corpus, then continue cross-domain reconciliation toward full PQ↔Skill navigation.

### 2026-09-27 continuation — Batch 506 current-evidence completion
- [x] Completed bounded current-evidence refresh for **Burning Swan, Burst Blitz, Burst Charge, Burst Reflection, Burst Rush, Burst Stinger, Candy Beam (Super), and Celestial Wave**.
- [x] Refreshed `docs/data/skills.json`; canonical identities remain unchanged.
- [x] Preserved known reward-tier/trigger conflicts and did not invent probabilities, frame data, hidden interactions, scaling, or Skill→PQ relationships.
- [x] Finalized `docs/data/skill-research-batches/skill-batch-506.json`.
- [ ] Next: register the eight dedicated Batch 506 audit artifacts and synchronize the Skills index layer, then perform the next cross-domain reconciliation.

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


### 2026-09-27 continuation — Batch 513 current-evidence refresh and canonical correction
- [x] Fresh post-Batch-512 census selected **Dodoria Beam, Dodoria Headbutt, Dodoria Launcher, Double Crush, Double Death Slicer, Double Sunday, Dragon Blitz, and Dragon Burn** from the live 474-record canonical corpus.
- [x] Completed bounded current-evidence refreshes for all eight records.
- [x] Corrected **Double Death Slicer** canonical taxonomy/cost from **Super / 100 Ki** to **Ultimate / 300 Ki**, matching current Xenoverse 2-specific evidence.
- [x] Synchronized `docs/data/skills.json` and `docs/data/skills-index.json`; canonical identity changes: **0**.
- [x] Added the Batch 513 manifest and eight dated evidence audits; registered them in the cross-domain index.
- [x] Preserved evidence boundaries and did not infer unsupported probabilities, hidden gates, exact frames, universal scaling, or new Skill→PQ edges.
- [ ] Runtime/CI remains non-blocking.
- [ ] **Exact next:** fresh Batch 514 census, then continue substantive cross-domain enrichment beyond the 474-record canonical seed toward the 672 indexed-category target.


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

## 2026-09-27 — Batch 516 continuation state
- Batch 516 refreshed 12 canonical Skill records: Eraser Bomb; Evil Blast; Evil Explosion; Evil Eyes; Evil Flame; Evil Flight Strike; Evil Ray Strike; Evil Rise Strike; Evil Whirlwind; Excellent Full Course; Explosive Assault; Explosive Buu Buu Punch.
- Canonical and index layers were synchronized for these records; no identities, canonical fields, or Skill→PQ relationships were changed.
- Remaining stale canonical Skills after this batch: 235. Next alphabetical frontier begins with Explosive Wave, Eye Beam, Fake Blast, Feint Shot, Fierce Fist, Fighting Pose E, Fighting Pose K, Final Cannon.
- Three pre-existing canonical/index last_verified mismatches remain intentionally unresolved: Phantom Fist, Rise to Action, Rising Rage.
- Continue using canonical data as source of truth; do not treat verified:true as authoritative.

### 2026-09-27 continuation — Batch 517 canonical evidence refresh
- [x] Completed Batch 517: refreshed 10 skills: Explosive Wave; Eye Beam; Fake Blast; Feint Shot; Fierce Fist; Fighting Pose E; Fighting Pose K; Final Cannon; Final Charge; Final Explosion.
- [x] Synchronized docs/data/skills.json and docs/data/skills-index.json; both remain at 474 records.
- [x] Added docs/data/skill-research-batches/skill-batch-517.json and registered it in docs/data/pq-cross-domain-index.json.
- [x] Batch 517 made zero skill identity changes, zero canonical field corrections, and zero new Skill→PQ relationship inferences.
- [x] Preserved existing acquisition/reward conflicts and unresolved frame, scaling, hidden-condition, and probability fields rather than normalizing them without evidence.
- [x] Post-batch validation: canonical/index counts are 474/474; the same three pre-existing last_verified mismatches remain isolated (Phantom Fist, Rise to Action, Rising Rage).
- [ ] 225 canonical skill records remain older than 2026-09-27.
- [ ] Exact next: Batch 518 beginning with Final Flash, Final Flash (SS3 DAIMA), Final Pose, Flash Chaser, Flash Fist Crush, Focus Flash, Full Power Charge, Full Power Destruction, Future Super Saiyan, Galactic Donuts, Galick Cannon, and Galick Gun.

### 2026-09-27 continuation — Batch 517 canonical evidence refresh
- [x] Completed Batch 517: refreshed 10 skills: Explosive Wave; Eye Beam; Fake Blast; Feint Shot; Fierce Fist; Fighting Pose E; Fighting Pose K; Final Cannon; Final Charge; Final Explosion.
- [x] Synchronized docs/data/skills.json and docs/data/skills-index.json; both remain at 474 records.
- [x] Added docs/data/skill-research-batches/skill-batch-517.json and registered it in docs/data/pq-cross-domain-index.json.
- [x] Batch 517 made zero skill identity changes, zero canonical field corrections, and zero new Skill→PQ relationship inferences.
- [x] Preserved existing acquisition/reward conflicts and unresolved frame, scaling, hidden-condition, and probability fields rather than normalizing them without evidence.
- [x] Post-batch validation: canonical/index counts are 474/474; the same three pre-existing last_verified mismatches remain isolated (Phantom Fist, Rise to Action, Rising Rage).
- [ ] 225 canonical skill records remain older than 2026-09-27.
- [ ] Exact next: Batch 518 beginning with Final Flash, Final Flash (SS3 DAIMA), Final Pose, Flash Chaser, Flash Fist Crush, Focus Flash, Full Power Charge, Full Power Destruction, Future Super Saiyan, Galactic Donuts, Galick Cannon, and Galick Gun.


### 2026-09-27 continuation — Batch 518 canonical evidence refresh
- [x] Completed Batch 518: refreshed 12 skills: Final Flash; Final Flash (SS3 DAIMA); Final Pose; Flash Chaser; Flash Fist Crush; Focus Flash; Full Power Charge; Full Power Destruction; Future Super Saiyan; Galactic Donuts; Galick Cannon; Galick Gun.
- [x] Synchronized docs/data/skills.json and docs/data/skills-index.json; both remain at 474 records.
- [x] Added docs/data/skill-research-batches/skill-batch-518.json and registered it in docs/data/pq-cross-domain-index.json.
- [x] Batch 518 made zero skill identity changes, zero canonical field corrections, and zero new Skill→PQ relationship inferences.
- [x] Preserved existing acquisition/reward conflicts and unresolved frame, scaling, hidden-condition, and probability fields rather than normalizing them without evidence.
- [x] Post-batch validation target: canonical/index counts remain 474/474; the three pre-existing last_verified mismatches remain isolated (Phantom Fist, Rise to Action, Rising Rage).
- [ ] Continue stale canonical Skill frontier alphabetically after Galick Gun.


### 2026-09-27 — Batch 516 completion
- Refreshed 12 canonical Skills records: Eraser Bomb, Evil Blast, Evil Explosion, Evil Eyes, Evil Flame, Evil Flight Strike, Evil Ray Strike, Evil Rise Strike, Evil Whirlwind, Excellent Full Course, Explosive Assault, Explosive Buu Buu Punch.
- Canonical skills database remains 474 records; no skill identities, canonical acquisition endpoints, or unsupported Skill→PQ relationships were changed.
- Synchronized the 474-record skills index and registered Batch 516 in the PQ cross-domain index.
- Batch 516 remains an evidence refresh only: canonical data is authoritative; existing reward/acquisition conflicts and unresolved exact frames, probabilities, hidden conditions, and patch-independent scaling remain preserved.
- Next stale frontier after Batch 516: Explosive Wave, Eye Beam, Fake Blast, Feint Shot, Fierce Fist, Fighting Pose E, Fighting Pose K, Final Cannon, Final Charge, Final Explosion, Final Flash, Final Flash (SS3 DAIMA), then continue alphabetically.

### 2026-09-27 continuation — Batch 519 canonical evidence refresh
- [x] Completed Batch 519: refreshed 12 skills: Gamma Blaster; Gamma Impact; Genocide Shell; Gigantic Breaker; Gigantic Burst; Gigantic Charge; Gigantic Cluster; Gigantic Cross; Gigantic Explosion; Gigantic Nova; Gigantic Rage; Gigantic Roar.
- [x] Synchronized docs/data/skills.json and docs/data/skills-index.json; both remain at 474 records.
- [x] Added docs/data/skill-research-batches/skill-batch-519.json and registered it in docs/data/pq-cross-domain-index.json.
- [x] Batch 519 made zero skill identity changes, zero canonical field corrections, and zero new Skill→PQ relationship inferences.
- [x] Preserved existing acquisition/reward conflicts and unresolved frame, hidden-condition, probability, and patch-independent-scaling fields.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] 201 canonical skill records remain older than 2026-09-27.
- [ ] Exact next: continue after Gigantic Roar, beginning with God Breaker and the God of Destruction skill series.


### 2026-09-27 continuation — Skill evidence Batch 520
- [x] Refreshed 16 canonical skill records: God Breaker; God of Destruction's Anger; God of Destruction's Menace; God of Destruction's Might; God of Destruction's Plaything; God of Destruction's Poise; God of Destruction's Rampage; God of Destruction's Roar; God Punisher; Godly Chronos Cannon; Godly Display; Grand Smasher; Handy Canon; Headshot; Heat Dome Attack; Heat Wave.
- [x] Synchronized the 16 corresponding skills-index projections.
- [x] Added docs/data/skill-research-batches/skill-batch-520.json and registered it in docs/data/pq-cross-domain-index.json.
- [x] Preserved canonical acquisition/reward conflicts and did not infer unsupported probabilities, hidden gates, exact frames, or patch-independent scaling.
- [x] Canonical skill identity/relationship fields were unchanged; this cycle was evidence enrichment only.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] Exact next: continue from the stale frontier after Batch 520; re-fetch live SHAs before mutation.


### 2026-09-27 continuation — Skill evidence Batch 520
- [x] Refreshed 16 canonical skill records: God Breaker; God of Destruction's Anger; God of Destruction's Menace; God of Destruction's Might; God of Destruction's Plaything; God of Destruction's Poise; God of Destruction's Rampage; God of Destruction's Roar; God Punisher; Godly Chronos Cannon; Godly Display; Grand Smasher; Handy Canon; Headshot; Heat Dome Attack; Heat Wave.
- [x] Synchronized the 16 corresponding skills-index projections.
- [x] Added docs/data/skill-research-batches/skill-batch-520.json and registered it in docs/data/pq-cross-domain-index.json.
- [x] Preserved canonical acquisition/reward conflicts and did not infer unsupported probabilities, hidden gates, exact frames, or patch-independent scaling.
- [x] Canonical skill identity/relationship fields were unchanged; this cycle was evidence enrichment only.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] Exact next: continue from the stale frontier after Batch 520; re-fetch live SHAs before mutation.


### 2026-09-27 continuation — Skill evidence Batch 521
- [x] Refreshed 16 canonical skill records: Heavenly Arrow; Hellzone Grenade; Hero's Flute; Hero's Pose; Heroic Assault; Heroic Counter; Holy Inscription; Holy Wrath; Hyper Drain; Hyper Movement; Hyper Tornado; Ill Bomber; Ill Rain; Impact Flare; Impulse Slash; Indomitable.
- [x] Synchronized the 16 corresponding skills-index projections.
- [x] Added docs/data/skill-research-batches/skill-batch-521.json and registered it in docs/data/pq-cross-domain-index.json.
- [x] Batch 521 made zero skill identity changes, zero canonical field corrections, and zero new Skill→PQ relationship inferences.
- [x] Existing acquisition/reward conflicts and unresolved exact frames, reward probabilities, hidden conditions, and patch-independent scaling were preserved rather than inferred.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] Exact next: continue the stale canonical Skill frontier after Indomitable; re-fetch live SHAs before every mutation.


### 2026-09-27 continuation — Skill evidence Batch 522
- [x] Refreshed 20 canonical skill records: Innocence Breath; Innocence Bullet; Innocence Cannon; Instant Charge; Instant Rise; Instant Severance; Instant Transmission; Jumping Energy Wave; Justice Blade; Justice Combination; Justice Drive; Justice Kick; Justice Pose; Justice Rush; Kai Kai; Kaioken; Kaioken Kamehameha; Kairos Cannon; Kamehameha; Ki Explosion.
- [x] Synchronized the 20 corresponding skills-index projections.
- [x] Added docs/data/skill-research-batches/skill-batch-522.json and registered it in docs/data/pq-cross-domain-index.json.
- [x] Preserved canonical source-of-truth rules and did not infer unsupported frames, universal scaling, reward probabilities, hidden conditions, or disputed acquisition semantics.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] Exact next: continue the stale canonical Skill frontier after Ki Explosion; re-fetch live SHAs before mutation.


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


### 2026-09-27 continuation — Recovery baseline supersedes stale endpoint-gap note
- [x] Reconciled the recovery state against the current live main tree after the latest recovery-forward promotions.
- [x] Confirmed canonical database recovery is materially present: 474 unique canonical skills, 474 matching skill-index records, 474 canonical skills represented by the Skill→PQ reverse layer, 246 Skill→PQ edges across 170 PQs, and 840 canonical PQ reward relationships (236 skill / 137 Super Soul / 125 equipment / 247 character / 88 DLC / 7 farming).
- [x] Confirmed the recovered canonical PQ equipment projection is currently 125 edges / 123 unique targets with 123 endpoint identity matches and **0 endpoint identity gaps**. Any older handoff text stating 72 remaining equipment endpoint identity gaps is stale and must not be used as the current frontier.
- [x] Confirmed the recovered Super Soul PQ acquisition layer has 137 canonical relationships, 134 unique targets, 134 endpoint targets, and 168 canonical Super Soul records; all canonical PQ Super Soul targets currently resolve to endpoint identities.
- [x] Preserved canonical-source priority: recovery used surviving canonical blobs/relationship stores rather than rebuilding canonical data from secondary indexes or datasets marked verified true.
- [ ] Runtime/CI remains intentionally non-blocking/unverified.
- [ ] **Exact next:** continue substantive evidence-backed enrichment from the live frontier. Prioritize the Super Soul mechanics backlog (80 records still marked partial in the latest integrity audit) and other cross-domain coverage gaps; do not reopen already-complete equipment endpoint identity work unless a fresh census proves regression.


### 2026-09-27 continuation — Super Soul mechanics audit correction
- [x] Continued from the recovered canonical baseline rather than reopening completed endpoint recovery.
- [x] Audited the Super Soul mechanics coverage report against the canonical record layer and corrected a stale arithmetic error: `records=172`, so `limit_burst_trigger.missing` is **172**, not 173. No canonical Super Soul record was changed by this correction.
- [x] Rechecked PQ 186 evidence: the surviving canonical relationship layer correctly associates “The final battle begins now.” and “I'll use this power to protect everyone!” with PQ 186. Independent current PQ guide evidence likewise lists both as PQ 186 rewards. Mechanics for the first remain unresolved; no unsupported effect was invented. Current player discussion also provides only anecdotal drop observations, so it is retained as secondary research evidence rather than promoted to canonical mechanics.
- [ ] Continue mechanics enrichment with source-backed evidence, prioritizing records where an explicit mechanic source exists; preserve unresolved fields when evidence is insufficient.


### 2026-09-27 continuation — Active Super Soul coverage reconciliation
- [x] Found a coverage-integrity issue in `audit_super_soul_mechanics_coverage.py`: it counted five records explicitly marked `provenance_status=rejected_legacy_misidentification` as active mechanics records.
- [x] Corrected the validator to preserve all 172 historical records for auditability while excluding the five rejected legacy identities (super-soul-138 through super-soul-142) from active coverage. Current active count is **167**.
- [x] Recomputed active mechanics coverage: trigger 162/167; effect text 167/167; magnitude 161/167; duration 126/167; stacking 72/167; Limit Burst 158/167; Limit Burst trigger 0/167; Limit Burst effect 163/167; CaC usability 164/167; race restriction 3/167; DLC requirement 67/167.
- [x] No gameplay mechanics or reward relationships were inferred or altered by this correction.
- [ ] Continue evidence-backed enrichment against the **167 active** Super Soul records. Treat the five rejected historical identities only as provenance/audit artifacts.


### 2026-09-27 continuation — Super Soul 035 Limit Burst enrichment
- [x] Enriched canonical `super-soul-035` (“I'll use this power to protect everyone!”) with `Auto Just Guard` as its Limit Burst/effect based on current secondary player evidence; classification remains `verified_secondary`.
- [x] Added the supporting research source and updated the mechanics audit. Active Limit Burst-effect coverage is now **164/167**, leaving 3 active records unresolved in that field.
- [x] No acquisition relationship or unrelated mechanic was inferred; the existing ~5000 damage / 15% all-ability effect remains explicitly secondary evidence.
- [ ] Continue source-backed enrichment of the remaining active mechanics gaps, prioritizing direct item-level evidence and keeping secondary findings labeled.


### 2026-09-27 continuation — Super Soul 035 Limit Burst enrichment
- [x] Enriched canonical `super-soul-035` (“I'll use this power to protect everyone!”) with `Auto Just Guard` as its Limit Burst/effect based on current secondary player evidence; classification remains `verified_secondary`.
- [x] Added the supporting research source and updated the mechanics audit. Active Limit Burst-effect coverage is now **164/167**, leaving 3 active records unresolved in that field.
- [x] No acquisition relationship or unrelated mechanic was inferred; the existing ~5000 damage / 15% all-ability effect remains explicitly secondary evidence.
- [ ] Continue source-backed enrichment of the remaining active mechanics gaps, prioritizing direct item-level evidence and keeping secondary findings labeled.


### 2026-09-27 continuation — PQ 185 Super Soul evidence refresh
- [x] Rechecked current 2026 player-testing evidence for `super-soul-032` and `super-soul-033` from PQ 185. The discussion independently reports the existing 20% mechanics values already recorded in the canonical layer.
- [x] Added the current secondary research source and refreshed verification classification/date for both records. No new mechanics or Limit Burst behavior was inferred.
- [x] The three active records still lacking `limit_burst_effect` remain `super-soul-032`, `super-soul-033`, and `super-soul-034`; the first two now have refreshed secondary mechanics evidence, while Super Soul 034 remains unresolved at item-mechanics level.
- [ ] Continue searching for explicit Limit Burst/item-level evidence; do not manufacture missing values from neighboring records or names.


### 2026-09-27 continuation — PQ 185 Super Soul evidence refresh
- [x] Rechecked current 2026 player-testing evidence for `super-soul-032` and `super-soul-033` from PQ 185. The discussion independently reports the existing 20% mechanics values already recorded in the canonical layer.
- [x] Added the current secondary research source and refreshed verification classification/date for both records. No new mechanics or Limit Burst behavior was inferred.
- [x] The three active records still lacking `limit_burst_effect` remain `super-soul-032`, `super-soul-033`, and `super-soul-034`; the first two now have refreshed secondary mechanics evidence, while Super Soul 034 remains unresolved at item-mechanics level.
- [ ] Continue searching for explicit Limit Burst/item-level evidence; do not manufacture missing values from neighboring records or names.


### 2026-09-27 continuation — Super Soul 033 Limit Burst enrichment
- [x] Enriched `super-soul-033` (`Malice... Existence... Cruelty...`) with `Super Armor` as its Limit Burst/effect from current player evidence.
- [x] Classified the finding as `verified_secondary`; no primary-source claim was made.
- [x] Updated the mechanics audit. The unresolved active Limit Burst-effect gap is now **2 records**: `super-soul-032` and `super-soul-034`.
- [ ] Continue searching for explicit item-level evidence for Super Souls 032 and 034; do not infer missing mechanics.


### 2026-09-27 continuation — Post-corruption canonical recovery checkpoint + Super Soul 032/034 frontier
- [x] Added `docs/data/canonical-database-recovery-checkpoint-2026-09-27.json` as a durable recovery checkpoint containing live-main canonical baseline counts, source blob SHAs, corruption-recovery history, and explicit evidence boundaries.
- [x] Re-verified the recovered canonical baseline before advancing: 474 canonical Skills / 474 Skills index records; 246 Skill→PQ edges across 170 PQs; 840 canonical PQ reward relationships (236 Skill / 137 Super Soul / 125 equipment / 247 character / 88 DLC / 7 farming); 172 historical Super Soul records with 167 active records.
- [x] Confirmed the current live main contains the recovered 474-record Skills corpus after the earlier corruption/regression and subsequent restoration/concurrent-write repairs.
- [x] Re-searched the remaining active Super Soul Limit Burst frontier. `super-soul-032` still has secondary evidence for a 20% all-abilities increase below 50% HP, but no direct item-level Limit Burst evidence was found. `super-soul-034` is confirmed as the PQ 186 reward identity, but current evidence still does not establish its effect or Limit Burst.
- [x] Preserved the evidence boundary: no Limit Burst or effect mechanics were inferred from titles, neighboring rewards, or unsupported community speculation.
- [ ] Runtime/CI remains intentionally non-blocking/unverified.
- [ ] **Exact next:** continue evidence-backed Super Soul mechanics enrichment; prioritize direct item-level/character-data evidence for `super-soul-032` and `super-soul-034`, then resume larger cross-domain enrichment. Never reconstruct canonical data from projections when the canonical layer survives.


### 2026-09-27 continuation — Super Soul 032/034 direct-evidence audit
- [x] Re-censused the live canonical Super Soul records and performed another direct-evidence search for `super-soul-032` and `super-soul-034`.
- [x] Added `docs/data/super-soul-032-034-direct-evidence-audit-2026-09-27.json` documenting the evidence boundary and source URLs.
- [x] PQ 185 documentation independently confirms `super-soul-032` in the reward inventory; secondary player testing reports +20% to all abilities below 50% HP. This remains secondary and is not promoted to primary mechanics truth.
- [x] PQ 186 documentation independently confirms `super-soul-034` in the reward inventory; current discussion reviewed does not establish a reliable effect. No mechanics were inferred.
- [x] No canonical Super Soul mechanics were mutated because neither record has sufficient direct item-level evidence for the unresolved fields.
- [ ] Runtime/CI remains intentionally non-blocking/unverified.
- [ ] **Exact next:** continue direct item-level/game-data research for the two unresolved Super Soul records; if no primary evidence emerges, move to the next highest-value substantive cross-domain gap rather than filling fields speculatively.


### 2026-09-27 continuation — Skill evidence Batch 526
- [x] Added `docs/data/skill-research-batches/skill-batch-526.json` covering 12 records: Raid Blast; Rakshasa's Claw; Recoome Eraser Gun; Recoome Kick; Requiem of Destruction; Reverse Launcher; Reverse Mabakusenko; Riot Javelin; Rocket Tackle; Savory Slicer; Scissors Paper Rock; Shine Shot.
- [x] Registered Batch 526 in `docs/data/pq-cross-domain-index.json`.
- [x] Current evidence confirms several concrete mechanics/acquisition facts, including Raid Blast (PQ136/100 Ki/charge and extension behavior), Recoome Kick (PQ61/100 Ki/temporary ATK boost), Requiem of Destruction (PQ106/300 Ki/grab-explosion sequence), and Reverse Launcher (Bojack training/100 Ki/two-shot teleport sequence).
- [x] No canonical identity, field, or Skill→PQ relationship was changed from secondary snippets alone; evidence boundaries remain explicit.
- [ ] Runtime/CI remains intentionally non-blocking/unverified.
- [ ] **Exact next:** continue the stale Skill frontier after Shine Shot with fresh live evidence; promote canonical fields only when record-level provenance is sufficient, then reconcile any resulting Skill↔PQ cross-domain changes.


### 2026-09-27 continuation — Batch 526 evidence enrichment
- [x] Refreshed Batch 526 with current web evidence for Shine Shot, Rocket Tackle, Savory Slicer, and Rakshasa's Claw.
- [x] Evidence confirms the current skill identities/character associations and, where available, CaC usability; canonical mechanics/acquisition fields were deliberately not mutated from secondary evidence alone.
- [x] Batch 526 remains registered in the cross-domain index and preserves an explicit provenance boundary.
- [ ] **Next:** continue record-level evidence enrichment beyond Batch 526 and only promote canonical fields when sufficiently direct provenance is available.


### 2026-09-27 continuation — Batch 526 direct-record evidence
- [x] Added direct record-level evidence candidates for Rakshasa's Claw, Rocket Tackle, and Savory Slicer: type, Ki cost, acquisition source, and character source where directly supported.
- [x] Preserved the canonical-data-first boundary: candidates were recorded in the research manifest rather than blindly overwriting the live canonical database.
- [x] Independent current sources corroborate Rakshasa's Claw as a Strike Super from PQ 57, Rocket Tackle as a 100-Ki Strike Super from Android 16 training, and Savory Slicer as a 100-Ki Strike Super from PQ 140. citeturn0search1turn0search10turn0search4
- [ ] **Next:** inspect the live canonical records for these candidates and promote only fields that are actually missing/stale; then reconcile Skill→PQ endpoints and continue the next frontier.


### 2026-09-27 continuation — Batch 526 canonical reconciliation
- [x] Reconciled the new Batch 526 direct-evidence candidates against existing repository research before touching canonical data.
- [x] Confirmed Rakshasa's Claw already has detailed Batch 481/489 evidence and an existing PQ57 canonical reward edge.
- [x] Confirmed Rocket Tackle already has dedicated Batch 471 mechanics evidence establishing the 100-Ki Strike Super / Android 16 relationship.
- [x] Confirmed Savory Slicer already has canonical PQ140 crosslink/reward evidence and existing Strike Super/100-Ki research.
- [x] Avoided duplicate canonical rewrites; Batch 526 is retained as an evidence-refresh layer.
- [ ] **Next:** move beyond these already-covered records and identify the next genuinely under-enriched Skill records, prioritizing missing canonical mechanics/provenance rather than repeating established fields.


### 2026-09-27 continuation — Skill Batch 527 sparse-record enrichment
- [x] Created Skill Research Batch 527 for four sparse early Ki Blast Supers: **Tyrant Lancer, Ki Explosion, X10 Kamehameha, and Kamekameha**.
- [x] Added bounded evidence for classification, Ki cost, notable character source/CaC availability, and mechanics/damage-test observations where available.
- [x] Registered Batch 527 in `docs/data/pq-cross-domain-index.json`.
- [x] Preserved the canonical-data-first rule: test-contextual damage figures and unresolved acquisition/Ultimate-Finish semantics were not promoted blindly.
- [ ] **Next:** inspect the four live canonical records and promote only fields whose provenance is strong enough; then continue the sparse-record audit to the next under-enriched cohort.


### 2026-09-27 continuation — Batch 527 duplicate-screen reconciliation
- [x] Reconciled Batch 527's four sparse-record targets against the live repository's later dedicated evidence audits.
- [x] Tyrant Lancer is already covered by Batch 417; Ki Explosion by Batch 458; x10 Kamehameha by Batch 421; Kamekameha by Batch 49.
- [x] Confirmed Kamekameha's PQ spelling alias is explicitly handled by the existing PQ crosslink validator; no new canonical skill or PQ edge was manufactured.
- [x] No canonical rewrite was performed; Batch 527 is retained as a duplicate-screen/audit artifact documenting the superseded sparse Batch 254 state.
- [ ] **Next:** identify the next genuinely uncovered or under-enriched records from the live frontier rather than expanding already-audited skills.


### 2026-09-27 continuation — Super Soul 032/034 evidence refresh
- [x] Returned to the exact unresolved Super Soul frontier specified by the persistent handoff instead of creating another duplicate Skill batch.
- [x] Refreshed direct/record-specific secondary evidence for `super-soul-032` and `super-soul-034`.
- [x] For 032, current player reporting documents a second activation/name-state: after KO, the displayed name changes to “Using this power should be no sweat for you guys.” This is recorded as secondary activation evidence, not as proof of the underlying effect.
- [x] For 034, current discussion still does not establish a reliable mechanics description; this unresolved state is explicitly preserved.
- [x] Updated `docs/data/super-soul-032-034-direct-evidence-audit-2026-09-27.json` and made no unsupported canonical mechanics mutation.
- [ ] Runtime/CI remains intentionally non-blocking/unverified.
- [ ] **Next:** continue searching for direct item-level/game-data evidence for 032/034; if primary evidence remains unavailable, move to the next substantive cross-domain integrity gap.


### 2026-09-27 continuation — Dual Masenko canonical-gap audit
- [x] Investigated the next substantive frontier instead of repeating already-audited Skill records.
- [x] Found a likely canonical omission: `Dual Masenko` is present in the Ki Blast skill catalog and prior research, but no `skill-dual-masenko` record exists in the 474-record canonical Skills layer.
- [x] Current Xenoverse 2-specific evidence independently identifies Dual Masenko as a 100-Ki Ki Blast Super obtainable by the Future Warrior from the TP Medal Shop; historical shop evidence records a 170 TP Medal price. citeturn3search2turn3search0turn3search5turn3search12
- [x] Created `docs/data/dual-masenko-canonical-gap-audit-2026-09-27.json` documenting the evidence and the repository-layer discrepancy.
- [x] Corrected the interpretation boundary: Batch 261's older “Training with Future Trunks” acquisition field is stale/contradictory and must not be promoted over direct TP Medal Shop evidence.
- [x] Did **not** manufacture a PQ118 Skill→PQ edge. The strongest acquisition evidence is TP Medal Shop, while PQ118 evidence remains unresolved/conflicting.
- [ ] Canonical restoration remains pending because the complete current `skills.json` / `skills-index.json` payload could not be safely retrieved through the GitHub connector for an atomic full-file edit; do not risk overwriting the surviving canonical database with a truncated reconstruction.
- [ ] Runtime/CI remains intentionally non-blocking/unverified.
- [ ] **Exact next:** safely restore/add the Dual Masenko canonical record and corresponding index entry from the complete live canonical payload, then re-run partner/custom and PQ118 reconciliation before moving to the next gap.


### 2026-09-27 continuation — Dual Masenko restoration preparation
- [x] Re-verified the Dual Masenko omission against current Xenoverse 2-specific sources: TP Medal Shop acquisition, Ki Blast classification, Super classification, and 100 Ki cost. Historical shop evidence records 170 TP Medals. Sources: https://dbxv2.fandom.com/wiki/Dual_Masenko ; https://www.dbzgames.org/news/dragon-ball-xenoverse-2-free-update-details-tp-medal-shop-schedule/ ; https://gamefaqs.gamespot.com/boards/190457-dragon-ball-xenoverse-2/75501935
- [x] Prepared the complete intended canonical record fields inside `docs/data/dual-masenko-canonical-gap-audit-2026-09-27.json`.
- [x] Explicitly retained TP Medal Shop as acquisition truth and did not carry forward Batch 261's stale “Training with Future Trunks” acquisition field.
- [x] Did not mutate `skills.json` or `skills-index.json`: the connector cannot safely retrieve the complete large canonical payload, so replacing it from a truncated response would recreate the corruption risk this recovery cycle is designed to prevent.
- [ ] Atomic insertion of `skill-dual-masenko` into canonical Skills and index remains the exact next task once a complete payload/edit path is available.
- [ ] After insertion, regenerate/reconcile Partner Customization and PQ118 relationships; do not manufacture PQ118 until explicit reward evidence is confirmed.
- [ ] Runtime/CI remains intentionally non-blocking/unverified.


### 2026-09-27 continuation — Dual Masenko restoration preparation
- [x] Re-verified the Dual Masenko omission against current Xenoverse 2-specific evidence: TP Medal Shop acquisition, Ki Blast classification, Super classification, and 100 Ki cost.
- [x] Prepared the intended canonical record fields inside the Dual Masenko gap-audit artifact.
- [x] Retained TP Medal Shop as acquisition truth and did not carry forward Batch 261's stale training-only acquisition field.
- [x] Did not mutate skills.json or skills-index.json: the connector cannot safely retrieve the complete large canonical payload, so replacing it from a truncated response would recreate the corruption risk this recovery cycle is designed to prevent.
- [ ] Atomic insertion of skill-dual-masenko into canonical Skills and index remains the exact next task once a complete payload/edit path is available.
- [ ] After insertion, regenerate/reconcile Partner Customization and PQ118 relationships; do not manufacture PQ118 until explicit reward evidence is confirmed.
- [ ] Runtime/CI remains intentionally non-blocking/unverified.


### 2026-09-27 continuation — Dual Masenko canonical restoration completed
- [x] Retrieved the complete surviving canonical Skills blob directly by Git object SHA, avoiding truncated contents retrieval.
- [x] Confirmed the pre-restoration canonical layer contained 474 records and no Dual Masenko record.
- [x] Restored `skill-dual-masenko` into `docs/data/skills.json`; canonical Skills count is now 475.
- [x] Restored the corresponding `skill-dual-masenko` entry into `docs/data/skills-index.json`; index count is now 475.
- [x] Canonical fields use the stronger TP Medal Shop acquisition evidence, 100 Ki, Ki Blast Super classification, Future Trunks association, and bounded mechanics; the stale Batch 261 training-only acquisition statement was not promoted.
- [x] Reconciled Partner Customization: added Future Trunks (Time Patrol) → Dual Masenko and removed the former excluded-candidate entry.
- [x] PQ118 remains unresolved. No Skill→PQ edge was manufactured from weak/conflicting web material; the direct TP Medal Shop evidence remains the canonical acquisition endpoint.
- [x] Updated `docs/data/dual-masenko-canonical-gap-audit-2026-09-27.json` to close the restoration gap.
- [ ] Next: run/inspect canonical cross-domain validators and then identify the next genuine omission or under-enriched endpoint.


### 2026-09-27 continuation — Post-restoration validator synchronization
- [x] Audited the validators after Dual Masenko restoration. Several deterministic validators still encoded the pre-recovery 474-skill baseline; these were updated to the live 475-record canonical corpus.
- [x] Updated `validate_skill_pq_crosslinks.py`, `validate_canonical_database_recovery.py`, `validate_skill_acquisition_metadata.py`, and `validate_pq_skill_links.py` to expect 475 canonical skills.
- [x] Updated `validate_partner_skill_relationships.py` from 3 to 4 canonical partner relationships and aligned Dual Masenko's partner endpoint to the repository's canonical character name `Future Trunks`.
- [x] Re-synchronized `docs/data/skill-pq-reverse-index-2026-09-26.json`: 475 canonical skills, 246 Skill→PQ edges, 170 represented PQs; no PQ edge was added for Dual Masenko.
- [x] Re-synchronized `docs/data/pq-skill-crosslink-report.json` to 475 canonical skill records.
- [x] Static Git-object checks confirm the canonical Skills layer contains 475 records including `skill-dual-masenko`, the Skills Index contains 475 matching identities, and the Skill→PQ projection remains 246 edges / 170 PQs.
- [x] Corrected Dual Masenko partner evidence to repository-local evidence files so the partner validator's evidence-path contract remains valid.
- [ ] Runtime execution of validators remains unverified in this connector environment; next continuation should inspect available CI/workflow artifacts or execute validators if an execution path becomes available.
- [ ] Next substantive frontier: continue exhaustive missing/under-enriched endpoint discovery rather than cosmetic documentation changes. PQ118 ↔ Dual Masenko remains explicitly unresolved pending direct reward evidence.


### 2026-09-27 continuation — PQ118 / Dual Masenko evidence conflict resolved as unresolved
- [x] Re-checked PQ118 specifically against current external evidence after canonical Dual Masenko restoration.
- [x] Steam's maintained 186-PQ transcription lists PQ118's reward set without Dual Masenko, while a separate current third-party DLC guide explicitly associates Dual Masenko with PQ118. This is a direct source conflict, not sufficient evidence for a canonical Skill→PQ edge.
- [x] Updated `docs/data/pq-unrepresented-skill-endpoint-evidence-reconciliation-2026-09-26.json` to preserve the conflict and explicitly retain TP Medal Shop as the canonical Dual Masenko acquisition endpoint.
- [x] No Skill→PQ relationship was manufactured; the canonical Skill→PQ projection remains 246 edges / 170 PQs.
- [ ] Future work: obtain direct item-level/game-data evidence that resolves the PQ118 conflict before considering a canonical relationship.


### 2026-09-27 continuation — Dual Masenko acquisition/DLC conflict reconciliation
- [x] Rechecked PQ118 against current repository records and independent PQ documentation. The live repository's PQ118 reward set lists `Now we're even.` and `I hate what I've become!`, while the long-running Steam 186-PQ guide likewise does not list Dual Masenko. A separate newer web guide incorrectly/ambiguously labels a different PQ118 as `A Desperate Fight` and claims Dual Masenko there; this conflicting evidence is not sufficient to manufacture a Skill→PQ edge. citeturn0search0turn1search0
- [x] Preserved the stronger TP Medal Shop acquisition evidence for Dual Masenko and kept PQ118 unresolved.
- [x] Removed the unsupported `Free Update 4` value from the restored canonical Dual Masenko record; `dlc_requirement` is now null, consistent with the existing Batch 261 research record.
- [x] Updated the Dual Masenko gap audit with the conflict and decision.
- [ ] Next: continue exhaustive discovery of genuine missing/under-enriched records and reconcile only when evidence is sufficiently direct and consistent.


### 2026-09-27 continuation — QQ Bang research expansion
- [x] Moved the substantive frontier to the documented QQ Bang expansion priority after the Dual Masenko recovery/validator pass.
- [x] Audited the current QQ Bang canonical research layer: 3 existing records covering the synthesis system, Super Mix Capsule Z, and a Bardock + Beerus recipe family.
- [x] Added a fourth structured QQ Bang research record for the **Bardock Battle Suit + Beerus clothing + Super Mix Capsule Z** 6-star recipe family.
- [x] Kept the new record explicitly RNG-bounded: it records a recipe family and provenance, not a guaranteed six-stat output. Independent current research confirms QQ Bang results vary and recipe outputs must be treated as observations rather than deterministic guarantees. citeturn0search0turn0search3
- [x] Sources include repository research, Steam player documentation, and a dedicated QQ Bang recipe reference. Historical/community recipe evidence is retained as secondary evidence rather than promoted to unsupported exact mechanics. citeturn0search5turn0search6
- [ ] Next: expand QQ Bang observed-result records with actual six-stat outputs and provenance, then reconcile clothing-input/equipment endpoints. Do not infer exact results from recipe names alone.


### 2026-09-27 continuation — QQ Bang expansion pass
- [x] Moved to the next documented coverage priority after canonical skill recovery: QQ Bang research.
- [x] Audited the current QQ Bang record layer: 4 structured records (system, mixing item, recipe family, and recipe observation), with the recipe observation being the only concrete six-star recipe-result research target.
- [x] Deepened `qq-research-002` (Bardock Battle Suit + Beerus clothing + Super Mix Capsule Z) with independent repository research plus Steam evidence. Current evidence supports this as a six-star attempt/recipe family, while exact six-stat output remains RNG-dependent and is not promoted as guaranteed.
- [x] Preserved the project's canonical evidence rule: observed outputs and recipe families remain distinct; no unsupported exact six-stat result was invented.
- [ ] Next QQ Bang work: expand additional reproducible recipe families and observed six-stat result records, then capture version/material provenance and cross-links to equipment/build data.


### 2026-09-27 continuation — QQ Bang system research refresh
- [x] Reviewed the live coverage frontier after the Dual Masenko recovery; QQ Bang remains a critical under-populated domain with only four current structured records (system, mixing item, recipe family, recipe observation).
- [x] Independently refreshed QQ Bang system evidence: QQ Bangs override clothing stat effects across the four clothing slots; six stat dimensions are tracked; high-tier six-star research uses Super Mix Capsule Z; recipe outputs must remain RNG/distribution observations rather than guarantees. Sources include independent GitHub research and Prima Games recipe documentation.
- [x] Updated `docs/data/qq-bang-system-baseline.json` with the current evidence boundary and research update.
- [x] Updated `docs/data/qq-bangs-record-layer.json` with a dated provenance note without inventing additional QQ Bang records or exact guaranteed recipes.
- [ ] Next: expand QQ Bang records from the source/recipe universe into individual observed six-stat vectors with clothing inputs, mixing item, star rating, acquisition route, and provenance. Preserve RNG uncertainty and do not promote community recipe claims as guaranteed outputs.


### 2026-09-27 continuation — QQ Bang acquisition/provenance enrichment
- [x] Reviewed the live QQ Bang coverage gap and current canonical QQ Bang research layer instead of manufacturing exact six-stat vectors.
- [x] Enriched `docs/data/qq-bangs-record-layer.json` record `qq-mix-001` with current secondary evidence for Super Mix Capsule Z acquisition through Online Parallel Quest/Expert Mission Tours and documented synthesis from Super Mix Capsule + Demon Realm Crystal.
- [x] Refreshed the observed Bardock + Beerus + Super Mix Capsule Z recipe-family provenance while preserving RNG/output uncertainty.
- [x] Updated `docs/data/qq-bang-system-baseline.json` with the same acquisition provenance and an explicit next step: promote individually observed six-stat vectors only when exact inputs, catalyst, star rating, output, and provenance are available.
- [x] No guaranteed recipe result or unsupported drop percentage was added. Current evidence supports acquisition-family provenance, not exact item-table rates.
- [ ] Next QQ Bang frontier: identify individually observed six-stat vectors or direct game-data reward/item records, then expand the record layer substantially without treating community recipe distributions as guarantees.


### 2026-09-27 continuation — QQ Bang observed-output expansion
- [x] Advanced the next documented coverage priority into the QQ Bang record layer instead of repeating already-completed Skill recovery work.
- [x] Expanded `docs/data/qq-bangs-record-layer.json` from 4 to 14 records with 10 discrete observed recipe/output vectors from the documented Prima Games QQ Bang formula table.
- [x] Preserved the repository's uncertainty rule: each six-stat vector is stored as an observed historical output, not as a deterministic guarantee. Prima documents that QQ Bangs replace the four equipment-slot stat contributions and that recipe results vary; the repository therefore does not infer repeatability from a single observation. citeturn1view0
- [x] The new observations cover Android 18/Towa, Android 16/Great Saiyaman, multiple Beerus-based combinations, Bardock/Beerus, Beerus/Light Hearts, Beerus/4-Star Dragon Ball, Beerus/Broly, and two Beerus upper/lower-body variants.
- [ ] Next: continue QQ Bang expansion with additional documented recipe observations while deduplicating identical input/output vectors and preserving provenance; then normalize the QQ Bang index/coverage artifacts if their contracts require the new record count.


### 2026-09-27 continuation — QQ Bang frontier audit
- [x] Re-read the live coverage-gap priority after the Dual Masenko recovery. QQ Bang expansion remains the next major critical domain after the Awoken/version audit.
- [x] Inspected the canonical QQ Bang research layer. It currently contains system/mixing/recipe-family records plus 10 discrete Prima Games observed six-stat outputs; exact outputs are correctly treated as observations rather than guaranteed recipes.
- [x] Added a research-frontier note to `docs/data/qq-bangs-record-layer.json` documenting that the next expansion should seek additional non-duplicate observed vectors with exact input/mixing-item provenance rather than duplicating existing outputs.
- [x] Preserved the repository's null/RNG policy: no exact QQ Bang result is inferred from a recipe family, and community claims are not promoted to deterministic outcomes without observed vectors.
- [ ] Next: expand QQ Bang coverage with genuinely new observed six-stat vectors and source provenance, then normalize the QQ Bang record layer into canonical cross-domain relationships.
- [ ] Runtime/CI execution remains unverified.


### 2026-09-27 continuation — QQ Bang frontier audit
- [x] Audited the live QQ Bang record layer after the canonical skill recovery/validator synchronization.
- [x] Confirmed `docs/data/qq-bangs-record-layer.json` currently contains 14 research records, including 10 records with complete observed six-stat vectors.
- [x] Strengthened the QQ Bang research-layer metadata to explicitly separate observed vectors from recipe families and preserve RNG uncertainty; no deterministic community recipe was promoted.
- [x] Refreshed the system/recipe research timestamps and recorded the next QQ Bang frontier.
- [ ] Next substantive QQ Bang work: expand individually documented six-stat vectors and exact recipe provenance, then cross-link reproducible outputs into build/equipment research without claiming exhaustive inventory.
- [ ] Runtime/CI validation remains unverified in the connector environment.


### 2026-09-27 continuation — QQ Bang observed-vector expansion
- [x] Reviewed the live QQ Bang research layer rather than assuming the older 3-record baseline was current; the layer already contained 14 records (system, mixing item, recipe family, and observed vectors).
- [x] Added a new non-duplicate observed six-stat vector from a 2025 Steam community report: Beerus Top + Beerus Top + Super Mix Capsule Z → 6-star output +3/+5/+5/-2/0/+5.
- [x] Preserved this as `verified_secondary` observation only; no deterministic recipe guarantee was inferred. Current external QQ Bang research likewise treats recipe outputs as RNG/distributions. citeturn0search6turn0search0
- [x] QQ Bang record layer now contains 15 records and 11 promoted observed vectors.
- [ ] Continue QQ Bang expansion with additional non-duplicate observed vectors and exact input provenance; avoid duplicating the same output or converting community recipes into guaranteed results.
- [ ] Runtime/CI validation remains unverified in the connector environment.


### 2026-09-27 continuation — QQ Bang research expansion
- [x] Advanced the next-priority QQ Bang work instead of manufacturing a PQ118 relationship.
- [x] Expanded `docs/data/qq-bangs-record-layer.json` from 15 to 18 structured records.
- [x] Added three 6-star community recipe-family records: Super Saiyan 4 Goku + Goku Black clothing; Battle Suit (Bardock) + Light Heart Suit; Beerus clothing + Light Heart Suit.
- [x] Preserved the repository's RNG/provenance rule: these are recipe families, not guaranteed six-stat outputs; exact results remain separate observations.
- [x] Evidence refreshed from a 2025 community guide documenting the three recipe families and the Super Mix Capsule Z workflow. citeturn0youtube21
- [x] Updated `docs/data/coverage-gaps.json` to record the QQ Bang expansion while keeping the domain explicitly incomplete.
- [ ] Next QQ Bang frontier: expand observed six-stat outputs and acquisition/material provenance, especially version-aware Super Mix Capsule/Z evidence, without converting community recipe expectations into deterministic results.


### 2026-09-27 continuation — Post-corruption QQ Bang record recovery reconciliation
- [x] Inspected the live QQ Bang layer against its immediately preceding expansion commits rather than trusting the stale handoff count.
- [x] Detected a concrete regression: `docs/data/qq-bangs-record-layer.json` was at 15 records even though commit `4a6753753811ed18525d5c2dcb37f73b29be2420` had added `qq-recipe-003`, `qq-recipe-004`, and `qq-recipe-005` and the later handoff/TODO recorded 18.
- [x] Restored all three missing recipe-family records atomically from the surviving Git commit evidence. The layer is now **18 records / 11 observed six-stat vectors**.
- [x] Updated `canonical-database-recovery-checkpoint-2026-09-27.json` to the current live baselines: **475 Skills / 475 Skill Index records**, **840 canonical PQ reward relationships**, **172 historical / 167 active Super Souls**, **100 equipment records**, **33 mentors**, **15 Awoken records**, and **18 QQ Bang records**.
- [x] Updated `docs/TODO-EXHAUSTIVE.md` with the recovery reconciliation and retained the next QQ Bang frontier.
- [ ] Runtime/CI remains intentionally non-blocking/unverified.
- [ ] **Exact next:** continue QQ Bang expansion with additional non-duplicate observed six-stat vectors and version-aware Super Mix Capsule Z/material provenance, then add reproducible equipment/build cross-links. Do not treat recipe families as deterministic outputs.


### 2026-09-27 continuation — QQ Bang observed-output expansion
- [x] Expanded the canonical QQ Bang record layer from 18 to **23 records**, including **16 complete observed six-stat vectors**.
- [x] Added independent historical community observations rather than promoting recipe-family claims to deterministic outputs: a Beerus Top + Beerus Top 6-star result and four additional documented lower-tier output observations.
- [x] Preserved the evidence boundary: observations are records of reported results, not guarantees; one source did not specify the exact second clothing input for its +20/-0 example, so that provenance remains explicitly incomplete instead of being guessed.
- [x] Updated the research frontier to reconcile observed vectors with canonical clothing/equipment records next.
- [ ] Runtime/CI execution remains unverified.
- [ ] **Exact next:** normalize these observed vectors against canonical equipment/clothing identifiers, then continue version-aware Super Mix Capsule Z/material provenance and cross-domain build links.


### 2026-09-27 continuation — QQ Bang/equipment cross-domain normalization
- [x] Added four missing canonical equipment identity stubs: Beerus Top, Pikkon's Clothes, Towa's Clothes, and Future Trunks' Clothes. They were introduced because observed QQ Bang records explicitly use those inputs; no unsupported stats, acquisition routes, or restrictions were invented.
- [x] Added equipment identifiers to **8 QQ Bang records** where input names matched canonical records safely. This establishes the beginning of the intended PQ → equipment/QQ Bang → build cross-navigation chain.
- [ ] Continue resolving remaining QQ Bang clothing inputs (including existing-but-name-mismatched equipment records) and then add version-aware Super Mix Capsule Z/material provenance.
- [ ] Runtime/CI execution remains unverified.


### 2026-09-27 checkpoint reconciliation
- [x] Recovery checkpoint synchronized to the live post-recovery layers: equipment **104** records and QQ Bang **23** records with **16** complete observed vectors.
- [x] Audited QQ Bang equipment links against canonical equipment IDs; corrected provisional IDs for Goku Black's Clothes and Super Saiyan 4 Suit (Goku) using canonical records equip-094/equip-095.
- [ ] Continue canonical identity matching for remaining QQ Bang inputs; next research target remains version-aware Super Mix Capsule Z/material provenance, followed by broader equipment/build cross-links.


### 2026-09-27 continuation — expanded QQ Bang input normalization
- [x] Canonical equipment layer expanded from 104 to **109** records for explicit QQ Bang inputs whose identities were missing.
- [x] QQ Bang cross-links refreshed across **21 records**, using canonical identifiers only when the match was safe.
- [x] Recovery checkpoint synchronized to the live hashes/counts.
- [ ] Next exact research frontier: version-aware **Super Mix Capsule Z/material provenance**, while continuing to resolve any remaining clothing-name mismatches and later equipment/build relationships.

### 2026-09-27 continuation — version-aware QQ Bang materials
- [x] Super Mix Capsule Z now has dated 2020-2026 provenance for direct PQ/Expert Mission Tour acquisition and the Super Mix Capsule + Demon Realm Crystal synthesis route.
- [x] No patch-specific acquisition-rule change was promoted without direct evidence; exact drop percentages remain unresolved.
- [ ] Next exact frontier: deeper item-table/patch evidence, remaining QQ Bang clothing identity reconciliation, then equipment/build cross-links.

### 2026-09-27 continuation — current QQ Bang evidence boundary
- [x] Added 2025 official Time Patrol Support Pack evidence showing Demon Realm Crystal x5 and Super Mix Capsule Z x5 as paid DLC distribution.
- [x] Added 2026 community evidence for continued Tour farming and synthesis guidance.
- [x] Explicitly separated paid DLC distribution from base-game acquisition/drop-table claims.
- [ ] Next: remaining QQ Bang clothing identity reconciliation, then equipment/build cross-domain relationships; deeper item-table work only when direct evidence is available.

### 2026-09-27 continuation — reverse QQ Bang/equipment relationships
- [x] Added `qq_bang_links` to the equipment schema and populated 14 canonical equipment records from existing canonical QQ Bang equipment links.
- [x] Preserved bidirectional navigation without creating unsupported build records.
- [ ] Next: expand QQ Bang ↔ equipment ↔ PQ cross-links and then build-domain relationships when a canonical build layer is established.

### 2026-09-27 continuation — QQ Bang ↔ PQ cross-domain link
- [x] Added bidirectional `qq-mix-001` ↔ `pq-083` relationship for Super Mix Capsule Z farming evidence.
- [x] Classified the relationship as a community farming route in the Online Parallel Quest Tour, not a guaranteed reward or exact drop-rate claim.
- [ ] Next: reconcile remaining QQ Bang/equipment identities and expand equipment ↔ PQ acquisition links only where direct evidence exists.

### 2026-09-27 continuation — refined PQ 83 evidence
- [x] Refined the Super Mix Capsule Z ↔ PQ 83 cross-link with additional 2024 community evidence.
- [x] Preserved inconsistent observed drop behavior and explicitly avoided guaranteed-reward/exact-rate claims.
- [ ] Next: reconcile remaining QQ Bang equipment identities and expand equipment ↔ PQ acquisition links only where directly evidenced.

### 2026-09-27 continuation — equipment ↔ PQ provenance
- [x] Added bidirectional acquisition links for equip-001 and equip-017 ↔ pq-004, and equip-088 ↔ pq-100.
- [x] Links derive from explicit canonical equipment source_quest_or_shop fields; no guaranteed-drop or exact-rate claims were added.
- [ ] Next: continue QQ Bang equipment identity reconciliation and expand equipment ↔ PQ links only where direct canonical evidence exists.

### 2026-09-27 continuation — QQ Bang equipment reconciliation
- [x] Completed the identified Light Heart Suit identity gap: qq-recipe-004 and qq-recipe-005 now link to canonical equip-105.
- [x] Audited every QQ Bang equipment_link against the canonical equipment layer; no broken equipment IDs remain.
- [ ] Next: expand equipment ↔ PQ acquisition links where direct canonical evidence exists, then continue broader cross-domain reconciliation.

### 2026-09-27 continuation — equipment/PQ audit boundary
- [x] Audited all equipment `source_quest_or_shop` PQ references against the sparse canonical PQ record layer.
- [x] Confirmed no additional direct equipment↔PQ links can be safely promoted without reconciling the broader PQ datasets into the sparse canonical layer.
- [x] Avoided speculative PQ stub creation.
- [ ] Next: reconcile broader maintained PQ datasets with the sparse canonical PQ record layer, then promote additional equipment↔PQ links where supported.

### 2026-09-27 continuation — PQ 134 equipment promotion
- [x] Promoted the directly source-backed `pq-134` ↔ `equip-041` relationship for Broly (Full Power Super Saiyan)'s Clothes into both canonical directions.
- [x] Preserved acquisition-source semantics; no unsupported drop-rate or guarantee claim was added.
- [ ] Next: continue broader PQ-batch reconciliation; PQ 29 / Android 18's Clothes is an identified candidate once PQ 29 can be safely promoted into the sparse canonical layer.

### 2026-09-27 continuation — PQ 29 promotion
- [x] Promoted `pq-029` from `pq-021-040.json` into the sparse canonical PQ record layer.
- [x] Added the source-backed `pq-029` ↔ `equip-008` Android 18's Clothes relationship in both directions.
- [x] Kept exact drop mechanics unresolved rather than inventing them.
- [ ] Next: scan remaining maintained PQ batches for directly supported equipment rewards and promote safe cross-links.

### 2026-09-27 continuation — PQ 41/59 promotion
- [x] Promoted `pq-041` and `pq-059` from `pq-041-060.json` into the sparse canonical PQ layer.
- [x] Linked `pq-041` ↔ `equip-060` Yamcha's Baseball Uniform.
- [x] Linked `pq-059` ↔ `equip-061` Vegito's Clothes.
- [x] Preserved unresolved exact drop mechanics.
- [ ] Next: continue scanning remaining PQ batches for source-backed promotions.

### 2026-09-27 continuation — PQ equipment conflict boundary
- [x] Audited PQ 61-186 batch equipment rewards against the canonical equipment layer.
- [x] Found no additional safe exact-name equipment promotions in those batches.
- [x] Preserved `Yamcha's Sword` as unresolved at the PQ36 cross-link because maintained accessory research explicitly records a PQ29-vs-PQ36 historical conflict.
- [ ] Next: reconcile the Yamcha's Sword route/identity evidence, then continue broader PQ reward/equipment promotion.

### 2026-09-27 continuation — PQ36 enrichment
- [x] Enriched `pq-036` with the maintained batch's objectives, ultimate-finish condition, enemies, rewards, skill reward, Super Soul reward, and provenance.
- [x] Preserved `Yamcha's Sword` as a raw equipment reward without a canonical equipment link because the accessory research layer explicitly retains a PQ29/PQ36 conflict.
- [ ] Resolve the Yamcha's Sword identity/route conflict before promoting the cross-domain link.

### 2026-09-27 continuation — PQ21-40 restoration
- [x] Restored 17 missing PQ21-40 records into the canonical PQ layer from the maintained batch.
- [x] Added 7 exact-name bidirectional equipment links where canonical equipment identities were present.
- [x] Preserved unresolved accessory conflicts (including Yamcha's Sword) without speculative canonical equipment promotion.
- [ ] Continue restoring subsequent missing PQ records from maintained batches and cross-link only evidence-supported identities.

### 2026-09-27 continuation — PQ41-60 restoration
- [x] Restored 18 missing PQ41-60 records from maintained batch data.
- [x] Added 0 exact-name bidirectional equipment links where canonical identities existed.
- [ ] Continue canonical PQ restoration through PQ186, preserving unresolved identity conflicts.

### 2026-09-27 continuation — PQ61-80 restoration
- [x] Restored 20 missing PQ61-80 records from maintained batch data.
- [x] Added 0 exact-name equipment links where canonical identities existed.
- [ ] Continue restoration through the remaining maintained PQ batches.

### 2026-09-27 continuation — additional PQ recovery
- [x] Restored 18 additional missing PQ records from maintained batch data.
- [x] Audited their equipment rewards against canonical equipment; no safe exact-name matches were found, so no speculative links were created.
- [ ] Continue restoring the remaining sparse PQ layer and then expand cross-domain skill/equipment links from canonical evidence.

### 2026-09-27 continuation — PQ101-186 restoration
- [x] Restored 84 missing canonical PQ records from the maintained PQ101-186 batches.
- [x] Audited equipment rewards against canonical equipment; no exact-name equipment matches were safe to promote.
- [x] Preserved unresolved accessory identities and historical conflicts without speculative links.
- [ ] Continue systematic cross-domain reconciliation across the now-restored PQ layer.

### 2026-09-27 continuation — PQ41-100 restoration
- [x] Restored 0 missing PQ41-100 canonical records from maintained batch data.
- [x] Added 0 exact-name bidirectional equipment links where canonical identities existed.
- [x] Did not invent identities for unmatched rewards.
- [ ] Continue PQ101-186 canonical restoration and cross-domain linking.

### 2026-09-27 continuation — PQ101-186 restoration audit
- [x] Audited all maintained PQ101-186 batches against the canonical PQ layer.
- [x] Restored 0 missing records and added 0 exact-name equipment links.
- [ ] Run full canonical PQ integrity/reward-link audit next.

### 2026-09-27 continuation — PQ1-20 restoration
- [x] Restored missing PQ1-20 canonical records from maintained research batches.
- [x] Preserved source-backed reward/objective uncertainty rather than inventing drop rates.
- [ ] Reconcile PQ36's maintained numbering/cut conflict before final-board treatment.

### 2026-09-27 continuation — PQ41-100 reward restoration- [x] Restored missing rewards/skill/equipment/Super Soul and related maintained batch fields across canonical PQ41-100 where canonical fields were sparse.
- [x] Added exact-name equipment links and reverse PQ links where canonical equipment identities exist.
- [ ] Continue auditing later PQ ranges for sparse canonical fields; preserve unresolved identities rather than guessing.

### 2026-09-27 continuation — PQ41-100 restoration
- [x] Restored 0 missing PQ41-100 canonical records from maintained batch data.
- [x] Audited equipment rewards against canonical equipment; no additional exact-name matches were found.
- [x] Avoided speculative equipment identity/link creation.
- [ ] Continue restoration through PQ101+ maintained batches.


### 2026-09-27 continuation — QQ Bang component identity reconciliation after database recovery
- [x] Verified the live canonical Parallel Quest record layer contains all **186 PQ records**; corrected the recovery checkpoint's stale parallel_quests.record_layer_records value from 10 to 186.
- [x] Reconciled explicit QQ Bang clothing naming variants against canonical equipment without inferring stats or acquisition.
- [x] Mapped **Bardock Battle Suit** in qq-research-002 to canonical **equip-024** (Battle Suit (Bardock)).
- [x] Mapped explicit **Beerus Clothes (Upper Body)** / **Beerus clothing (upper body)** inputs to canonical **equip-101** (Beerus Top).
- [x] Added canonical **equip-110** for the distinct **Beerus Clothes (Lower Body)** input explicitly documented by the Prima Games recipe table; stats/acquisition remain unresolved.
- [x] Updated both directions of QQ Bang ↔ equipment navigation for the reconciled component identities.
- [x] Added docs/data/qq-bang-equipment-component-reconciliation-2026-09-27.json documenting the evidence boundary and unresolved fields.
- [x] Synchronized the recovery checkpoint to **110 equipment records / 23 QQ Bang records / 16 observed vectors / 186 PQ records**.
- [ ] Runtime/CI remains intentionally non-blocking/unverified.
- [ ] **Exact next:** continue version-aware Super Mix Capsule Z/material provenance and equipment/build cross-domain relationships; preserve unresolved QQ Bang inputs where evidence does not establish canonical identity.

- [x] 2026-09-27 follow-up: Closed the reverse-link audit by adding equipment-side QQ Bang links for equip-024/Bardock Battle Suit and equip-105/Light Heart Suit; forward/reverse reconciliation is now clean for the newly promoted identities.


## 2026-09-27 Recovery Continuation

- Rechecked the recovered live baseline: PQ 1-186 and 840 canonical cross-domain relationship edges remain intact; the forward/reverse reconciliation remains clean.
- Hardened the Super Mix Capsule Z provenance boundary in `docs/data/qq-bangs-record-layer.json`: Tour acquisition and Super Mix Capsule + Demon Realm Crystal synthesis remain evidence-backed research routes, while exact drop rates, universal patch-specific reward tables, and canonical synthesis quantities remain unresolved.
- Updated `docs/data/canonical-database-recovery-checkpoint-2026-09-27.json` with the current recovery baseline (110 equipment, 23 QQ Bang, 16 observed vectors, 186 PQ, 840 PQ cross-domain edges).
- Identified stale PQ status-layer metadata (older 232/135/122 and 182-PQ snapshot) as a synchronization task; do not treat those historical values as the live canonical baseline.
- Next: synchronize the stale PQ status metadata when the GitHub mutation path permits, then continue evidence-driven equipment/build cross-domain enrichment and unresolved QQ Bang identity reconciliation. Preserve uncertainty; do not infer missing canonical data.

- [x] 2026-09-27: Corrected an unsafe QQ Bang equipment identity: `Android 18 Skirt` is no longer linked to canonical `equip-008` (`Android 18's Clothes (Vest & Pants)`); the input is explicitly unresolved pending an exact canonical skirt record.
- [ ] 2026-09-27: Continue exact-identity audit of remaining QQ Bang clothing inputs and equipment-side reverse links; do not substitute near-name clothing variants.

- [x] 2026-09-27: Established canonical `equip-111` for the distinct `Android 18's Clothes (Skirt)` QQ Bang input using historical exact-variant evidence; retained historical stats while leaving acquisition unresolved because the historical PQ25 claim conflicts with the recovered canonical PQ25 reward layer.
- [x] 2026-09-27: Reattached `qq-observed-prima-005` to `equip-111` and preserved the acquisition conflict boundary without fabricating a PQ link.
- [ ] 2026-09-27: Continue exact QQ Bang clothing identity audit and reconcile historical acquisition conflicts before promoting equipment↔PQ links.

- [x] 2026-09-27: Reconciled PQ25 against multiple historical reward records and restored its documented reward set, including Android 18's Clothes (Skirt); exact drop mechanics remain unresolved.
- [x] 2026-09-27: Promoted `equip-111` Android 18's Clothes (Skirt) ↔ `pq-025` as a bidirectional acquisition relationship using the reconciled PQ25 evidence.
- [ ] 2026-09-27: Continue the exact QQ Bang/equipment identity audit and reconcile any remaining historical PQ reward conflicts before broad promotion.

- [x] 2026-09-27: Established `equip-112` for exact identity `Broly's Clothes`, distinct from `Broly (Full Power Super Saiyan)'s Clothes`.
- [x] 2026-09-27: Corrected `qq-observed-prima-012` so its `Broly Clothes` input points to `equip-112` instead of the unsafe near-name `equip-041`.
- [x] 2026-09-27: Preserved historical six-stat evidence and acquisition routes without asserting exact component drop conditions.
- [ ] 2026-09-27: Continue auditing generic/set/component QQ Bang inputs, with Beerus Clothes as the next identity boundary to reconcile.

- [x] 2026-09-27: Audited the `Beerus Clothes`/`Beerus Top` boundary. External recipe evidence explicitly uses Beerus top wording, while the equipment layer also contains a distinct Beerus lower-body record; generic QQ Bang inputs were retained on `equip-101` with an evidence note preventing inference that the lower-body component was used.
- [x] 2026-09-27: Preserved generic historical wording rather than fabricating a new full-set identity or silently conflating components.
- [ ] 2026-09-27: Continue exact QQ Bang clothing identity audit for remaining generic/set/component names.

- [x] 2026-09-27: Completed the current generic QQ Bang input identity sweep; no additional unsafe mappings were found beyond the already reconciled Broly and Beerus boundaries.
- [x] 2026-09-27: Synchronized `equipment-catalog-index.json` with the established canonical `equip-111` Android 18's Clothes (Skirt) identity.
- [x] 2026-09-27: Preserved explicit component distinctions and did not fabricate full-set records from generic recipe wording.
- [ ] 2026-09-27: Move to remaining canonical equipment endpoint gaps and provenance/cross-domain reconciliation, prioritizing explicit component identities and bidirectional links.

### 2026-09-27 continuation — explicit equipment↔PQ reconciliation closure
- [x] Completed the full 33-entry explicit equipment→PQ acquisition-source reconciliation queue.
- [x] Promoted all queued canonical equipment-side PQ links where the equipment record explicitly named the PQ as an acquisition source; no guaranteed drop rates or exact drop conditions were inferred.
- [x] Reconciled PQ-side reverse endpoints for the promoted relationships.
- [x] Audited the combined equipment/PQ endpoint graph and repaired 12 legacy reverse-link gaps plus 2 duplicate legacy forward representations.
- [x] Final endpoint audit: 48 unique equipment→PQ endpoints and 48 matching PQ→equipment endpoints; zero duplicate endpoints and zero asymmetric endpoints.
- [x] Updated the recovery checkpoint with this completed state.
- [ ] Next: move beyond the exhausted explicit equipment→PQ queue into evidence-backed QQ Bang/equipment identity and provenance reconciliation, then equipment/build and skill/PQ cross-navigation.



## 2026-09-27 Final Recovery Reconciliation — live main

- [x] Re-read the live continuation state and reconciled the post-corruption recovery baseline against current main commit `db6b7c96fef86ab0f690369a6f13f585491da7fb`.
- [x] Confirmed canonical database recovery baseline: **475 Skills / 475 skill-index records / 246 Skill→PQ edges / 170 represented PQs; 840 PQ cross-domain edges; 186 PQ records; 172 historical / 167 active Super Souls; 112 equipment records; 33 mentors; 15 Awoken records; 23 QQ Bang records / 16 observed vectors; 3 Partner Skill relationships**.
- [x] Added `docs/data/recovery-reconciliation-audit-2026-09-27-final.json` as the post-corruption recovery checkpoint and recorded the canonical-source-of-truth boundary.
- [x] Confirmed the explicit 33-entry equipment→PQ queue is exhausted and its endpoint graph remains 48 forward / 48 reverse with zero duplicate or asymmetric endpoints.
- [x] Confirmed Skill research has progressed through Batch 527; Batch 527 was screened against later dedicated evidence and made no unsupported canonical rewrite.
- [x] Preserved the repository rule that canonical data, not `verified: true` or projection/index layers, is authoritative for reconstruction.
- [ ] Runtime/CI remains intentionally non-blocking/unverified because connector-side execution evidence is unavailable.
- [ ] **Exact next:** continue evidence-backed QQ Bang/equipment provenance reconciliation, then equipment/build and skill/PQ cross-navigation enrichment. Promote only exact identities supported by canonical or explicit source evidence; preserve historical conflicts, RNG/drop-rate uncertainty, and unresolved acquisition semantics.


## 2026-09-27 continuation — accessory↔PQ cross-domain pass

- [x] Promoted five exact canonical accessory↔PQ research relationships: `acc-002` Four-Star Dragon Ball Hat ↔ `pq-005`; `acc-005` Great Saiyaman Helmet ↔ `pq-051`; `acc-012` Goku Wig (Super Saiyan) ↔ `pq-018`; `acc-027` Tapion's Sword ↔ `pq-022`; `acc-094` Resistance Helmet ↔ `pq-111`.
- [x] Added explicit PQ-side `accessory_links` so the relationships are navigable in both directions.
- [x] Kept these links typed as `research_acquisition_association`; they do not assert guaranteed normal-clear/Ultimate-Finish drops.
- [x] Preserved the Goku Wig (Super Saiyan) PQ63 historical conflict instead of promoting a second route.
- [ ] **Next:** continue exact accessory identity reconciliation for the remaining candidate queue, prioritizing candidates whose canonical identity already exists; do not manufacture identities for generic/component labels.


## 2026-09-27 continuation — exact accessory identity reconciliation

- [x] Closed 10 remaining accessory-PQ identity candidates against existing canonical accessory records: Four-Star Dragon Ball Hat, Chiaotzu's Hat (With Collar), Dore's Scouter, Jaco's State-of-the-Art Radio, Tagoma's Scouter, SSGSS Goku Wig, Yamcha Baseball Hat, SSGSS Vegeta Wig, Android 14's Hat, and Bardock (DB Super)'s Scouter.
- [x] Updated `accessory-pq-canonical-remaining.json` with the exact canonical IDs and resolution basis for each; no new identity was manufactured.
- [x] Preserved unresolved component-only and historical-conflict candidates for separate evidence work.
- [ ] **Next:** reconcile the remaining historical/conflicting accessory routes (especially Yamcha's Sword and Goku Wig PQ18/PQ63) and separately audit component-unresolved entries; then continue broader equipment/build navigation.


## 2026-09-27 continuation — accessory link integrity correction + reverse-link expansion

- [x] Corrected the previously introduced identity error where `acc-002` (Pan's Bandana) was incorrectly linked to PQ5. PQ5 now points to canonical `acc-061` (Four-Star Dragon Ball Hat), matching the explicit PQ5 reward table.
- [x] Added/reconciled reverse accessory links for the exact canonical identities already resolved in the accessory backlog: `acc-061`, `acc-062`, `acc-063`, `acc-064`, `acc-065`, `acc-066`, `acc-067`, `acc-068`, `acc-070`, and `acc-071`.
- [x] Kept research associations distinct from guaranteed-drop claims; PQ5 uses the stronger `reward` relationship because its canonical reward table explicitly names Four-Star Dragon Ball Hat.
- [x] Preserved unresolved historical conflicts and component-only accessory candidates rather than forcing them into canonical identity links.
- [ ] **Next:** investigate the remaining historical/conflicting accessory routes, beginning with Yamcha's Sword (PQ29/PQ36 conflict) and Goku Wig (Super Saiyan) (PQ18/PQ63 conflict), using explicit reward evidence before promotion.


## 2026-09-27 continuation — historical accessory PQ conflict reconciliation

- [x] Reviewed Yamcha's Sword using independent PQ reward evidence. PQ36 explicitly lists Yamcha's Sword, so PQ36 is represented as the explicit reward relationship; the historical PQ29 report remains preserved as `historical_conflict` rather than promoted.
- [x] Reviewed Goku Wig (Super Saiyan). PQ63 explicitly lists the wig in independent reward-table evidence, while the canonical accessory record retains the historical PQ18 route. Both endpoints are preserved with distinct relationship types; no unsupported silent replacement was made.
- [x] Added matching forward/reverse PQ links for these conflict cases.
- [x] Updated the canonical accessory notes to document the evidence review and the unresolved nature of the historical disagreement.
- [ ] **Next:** audit the remaining unresolved accessory candidates, especially component-unresolved PQ144/PQ147/PQ148/PQ152 entries, then continue equipment/accessory↔PQ navigation integrity checks.


## 2026-09-27 continuation — component-unresolved accessory audit

- [x] Re-audited `pqacc-026` Gine (DB Super)'s Accessory, `pqacc-027` Kale's Accessory, `pqacc-028` Caulifla's Accessory, and `pqacc-029` Android 17 (DB Super)'s Ranger Accessory against the canonical accessory identity layer.
- [x] Confirmed that the available evidence establishes clothing/set and/or wig components, but not separately named accessory inventory identities for these generic labels.
- [x] Preserved all four as `component_unresolved`; no canonical accessory identity was manufactured and no component was conflated with a set-level label.
- [x] Added an explicit audit entry to `accessory-pq-canonical-remaining.json` documenting the evidence boundary.
- [ ] **Next:** continue broader accessory↔PQ graph integrity and exact identity reconciliation, then move into equipment/build cross-navigation once accessory endpoint integrity is clean.


## 2026-09-27 continuation — accessory↔PQ graph integrity audit

- [x] Audited all canonical accessory→PQ links against the 186-record canonical PQ layer.
- [x] Audited all PQ→accessory links against the 95-record canonical accessory layer.
- [x] Result: **0 invalid accessory IDs, 0 missing PQ endpoints, and 0 asymmetric forward/reverse accessory↔PQ relationships**.
- [x] Confirmed the graph remains symmetric after the historical-conflict and component-unresolved passes; unresolved relationships are represented with explicit relationship types rather than broken endpoints.
- [ ] **Next:** move beyond the clean accessory↔PQ graph into equipment/build cross-navigation and provenance enrichment, prioritizing exact canonical identities and bidirectional endpoints.


## 2026-09-27 continuation — QQ Bang/equipment reverse-link integrity

- [x] Audited all 39 QQ Bang→equipment component edges against the 112-record canonical equipment layer.
- [x] Found and repaired the final asymmetric endpoint: `qq-observed-prima-012` → `equip-112` (Broly's Clothes) lacked the equipment-side reverse link.
- [x] Added the exact `recipe_input` reverse relationship to canonical `equip-112`; no recipe output or stat guarantee was inferred.
- [x] Post-fix graph status: all QQ Bang equipment endpoints resolve to canonical equipment IDs and the newly audited edge is now bidirectional.
- [ ] **Next:** continue systematic equipment/build cross-navigation audits, including other recipe/component domains and provenance fields, while preserving exact-identity and RNG boundaries.


## 2026-09-27 continuation — equipment/QQ Bang duplicate-link audit

- [x] Re-audited the complete QQ Bang ↔ canonical equipment graph after the Broly reverse-link repair: 39 forward edges, all endpoints valid, and all reverse endpoints present.
- [x] Detected duplicate equipment-side QQ Bang relationships on canonical `equip-101` (Beerus Top): `qq-observed-prima-013`, `qq-observed-prima-014`, and `qq-observed-steam-001` each occurred twice.
- [x] Removed only exact duplicate relationship objects; retained one evidence-bounded relationship for each source record.
- [x] Repaired graph now has no QQ Bang→equipment missing reverse endpoints and no duplicate QQ Bang relationship objects on `equip-101`.
- [ ] **Next:** continue equipment/build cross-navigation and provenance audits beyond QQ Bang links; do not infer missing identities, acquisition guarantees, or RNG outcomes.


## 2026-09-27 continuation — canonical equipment ↔ PQ reverse-navigation closure

- [x] Audited the canonical Parallel Quest equipment graph: 48 PQ-side equipment edges, all resolving to valid canonical equipment IDs.
- [x] Found 41 missing reverse endpoints in `docs/data/equipment-record-layer.json`; the remaining seven were already present.
- [x] Added the missing canonical equipment `pq_links` strings, preserving the existing PQ-side relationship semantics and avoiding any new guaranteed-drop inference.
- [x] Post-fix validation: 48/48 PQ→equipment edges have matching equipment→PQ reverse links; 0 invalid endpoints; 0 duplicate reverse links.
- [ ] **Next:** continue equipment/build cross-navigation beyond PQs, especially skill/character/build relationships and provenance coverage, using canonical records as the authority.


## 2026-09-27 continuation — character/build navigation parity re-audit

- [x] Re-audited the live canonical character navigation surface: 152 canonical character names, 34 explicit presentation-ID bridge records, and 51 character-preset records across 17 presentation character IDs.
- [x] Confirmed every preset `character_id` resolves through the explicit identity bridge to an existing canonical character name; 0 unresolved preset IDs and 0 invalid bridge targets.
- [x] Preserved the bridge boundary: presentation IDs are navigation keys only and are not promoted into canonical identity or relationships.
- [x] Refreshed `docs/data/characters/character-presentation-consumer-audit.json` with the live 2026-09-27 parity result.
- [ ] **Next:** continue cross-navigation from characters/presets into skills and build/loadout consumers, using canonical skills data as the authority and treating verified/index/projection layers only as supporting evidence.


## 2026-09-27 continuation — canonical skill/partner cross-navigation audit

- [x] Re-audited `docs/data/partner-skill-relationships.json`: 4 evidence-backed canonical skill→custom-partner relationships covering 3 unique canonical skills.
- [x] Confirmed the repeated `skill-arm-crash` endpoint is intentional: the same canonical skill is explicitly available to both Bardock and Turles; it is not a duplicate relationship.
- [x] Confirmed the relationship layer remains evidence-bounded and points to canonical skill identities rather than creating partner-specific duplicate skill records.
- [x] Preserved the canonical-source rule: `docs/data/skills.json` remains authoritative; verified/index/projection layers are not promoted as canonical substitutes.
- [ ] **Next:** continue canonical skill/build/loadout cross-navigation auditing, including the current 475-skill corpus, skill↔PQ reverse index, and partner/customization consumers; repair only deterministic identity/link inconsistencies.


## 2026-09-27 continuation — preset/loadout census reconciliation

- [x] Reconciled `docs/data/character-presets-record-layer.json` directly: **51** preset records = **25 verified loadouts + 26 unresolved loadouts**.
- [x] Confirmed the 25 verified loadouts contain **162 skill-slot entries** across Super, Ultimate, Awoken, and Evasive fields where present.
- [x] Corrected stale `docs/data/preset-loadout-current-evidence-audit-2026-09-24.json` census from 26/25 to the live 25/26 split; no preset relationship or loadout was promoted/demoted.
- [x] Kept numeric preset identity boundaries intact: unresolved Goku/Vegeta/Captain Ginyu mappings remain unresolved rather than being inferred from row/costume order.
- [ ] **Next:** validate the 162 existing loadout skill names against the canonical `docs/data/skills.json` identity layer and establish deterministic reverse character/preset navigation only where canonical relationship fields/evidence support it.


## 2026-09-27 continuation — verified preset skills vs canonical skill identity audit

- [x] Compared all **162** skill-slot entries from the **25 verified preset loadouts** against the authoritative `docs/data/skills.json` corpus (**475** canonical records).
- [x] Found **117 exact canonical-name matches** and **45 unmatched entries**, representing **18 unique skill names**.
- [x] Confirmed a normalized punctuation/spacing comparison produces no additional matches; no alias or identity inference was made.
- [x] Added `docs/data/character-preset-skill-canonical-identity-audit-2026-09-27.json` documenting the deterministic **canonical identity gap** and all 18 unmatched names with occurrence counts.
- [x] No canonical skill records were synthesized or promoted from preset loadout data; canonical data remains authoritative.
- [ ] **Next:** research the 18 unmatched preset skill names and determine, from direct evidence, whether each maps to an existing canonical skill, requires a cast-only/unavailable-for-CaC canonical record, or should remain outside the canonical skill corpus.


## 2026-09-27 continuation — canonical promotion of preset skill gaps

- [x] Resolved **17 of the 18** previously unmatched preset skill identities by promoting evidence-backed records into authoritative `docs/data/skills.json`.
- [x] Canonical skill corpus increased from **475 → 492** records; the 162 verified preset skill-slot entries now resolve **161/162** by exact canonical identity.
- [x] Preserved evidence status as `partially_verified` for these newly promoted records; no unsupported probabilities, hidden gates, or invented mechanics were added.
- [x] Added provenance-backed canonical records for: Super Galick Gun; Sledgehammer; Energy Wave Combo; Full Power Energy Wave; Full Power Energy Blast Volley; Super Back Jump; Galaxy Breaker (Festival); Ki Blast Cannon; Super Dragon Fist; Holstein Shock; Break Strike; Consecutive Energy Blast; Backflip; Super Ki Explosion; Recoome Eraser Gun; Ultra Fighting Bomber; Turn Retreat.
- [x] Left the final unmatched **Shockwave** reference unresolved rather than guessing its canonical classification/identity.
- [ ] **Next:** resolve `Shockwave` from record-level evidence, then audit the newly promoted 17 records for reverse character/preset navigation and synchronization with supporting skill indexes/catalog layers.


## 2026-09-27 continuation — final preset skill identity reconciliation

- [x] Resolved the final **Shockwave** preset skill reference using existing repository research batch 134, which explicitly establishes Shockwave as a **Super / Strike** skill with 100 Ki cost and Skill Shop acquisition.
- [x] Promoted Shockwave into authoritative `docs/data/skills.json` without inventing unsupported probability, frame, damage, or hidden-gate data.
- [x] Re-audited the full verified preset census: **162/162 skill-slot references now resolve exactly** against the canonical skill corpus.
- [x] Canonical skill corpus is now **493 records**; the preset identity gap is closed.
- [x] Updated `docs/data/character-preset-skill-canonical-identity-audit-2026-09-27.json` to record **0 unmatched entries** and preserve the full promotion history.
- [ ] **Next:** audit the 18 newly promoted preset skill records (including Shockwave) for canonical reverse character/preset navigation and synchronization with skill indexes/catalog projections; do not use projection/index layers as canonical truth.


## 2026-09-27 continuation — promoted skill reverse preset navigation audit

- [x] Re-audited the **18 skill identities** promoted to close the verified preset-loadout canonical identity gap against the live **493-record** canonical skill corpus and **51-record** preset layer.
- [x] Joined all affected verified preset loadouts by exact canonical skill identity and recorded every deterministic preset endpoint: all 18 promoted skills now have explicit consumer coverage in the audit, with **0 unresolved canonical skill IDs** and **0 slot-class incompatibilities**.
- [x] Preserved the cast/CaC boundary: **Galaxy Breaker (Festival)** remains a distinct canonical cast/preset skill and is not made CaC-usable merely because it appears in a verified Vegeta preset.
- [x] Added `docs/data/character-preset-skill-reverse-navigation-audit-2026-09-27.json` as the deterministic reverse-navigation audit.
- [x] Did **not** fabricate skill-side preset-link arrays: the current canonical preset layer stores loadout skill names, so the audit records exact reverse endpoints without changing the schema.
- [ ] **Next:** audit/synchronize the 493 canonical skills against the maintained skill-index/catalog layers and existing skill↔PQ relationships; repair only deterministic omissions or asymmetries while keeping canonical data authoritative.


## 2026-09-27 continuation — canonical skill/PQ projection synchronization after preset reconciliation

- [x] Audited the maintained skill↔PQ reverse-navigation artifacts after the canonical skill corpus reached **493** records.
- [x] Regenerated `docs/data/skill-pq-reverse-index-2026-09-26.json` deterministically from authoritative `docs/data/skills.json`; the reverse projection now records **493 canonical skills**, **246 explicit skill→PQ edges**, and **170 represented PQ IDs**.
- [x] Confirmed the 18 skills promoted during preset reconciliation do not add unsupported PQ edges; the **246-edge** relationship graph remains unchanged.
- [x] Synchronized skill↔PQ audit metadata to the live **493-record** canonical corpus while preserving the existing **246-edge / 170-PQ** relationship contract.
- [x] No projection/index layer was used as canonical truth; `docs/data/skills.json` remained authoritative.
- [ ] **Next:** continue the cross-domain audit from the synchronized 493-record skill corpus, checking remaining skill indexes/catalogs and deterministic skill↔character/mentor/partner relationships for stale counts, missing reverse endpoints, or asymmetric records. Preserve unresolved and historical evidence boundaries.


## 2026-09-27 continuation — canonical skill corpus cross-domain synchronization audit

- [x] Reconciled the verified preset-loadout identity audit against the live canonical docs/data/skills.json: 493 canonical skills, 25 verified presets, 162 skill-slot entries, 162 exact matches, 0 unmatched.
- [x] Audited docs/data/skill-acquisition-index.json: all 18/18 indexed Expert Mission skill endpoints resolve to canonical skill identities; no duplicate skill identities were found.
- [x] Audited docs/data/skill-pq-reverse-index-2026-09-26.json: reported 493 canonical skills, 246 skill↔PQ edges, and 170 PQs match the live canonical corpus; 0 invalid skill IDs were found.
- [x] Audited docs/data/partner-skill-relationships.json: all 4 evidence-backed relationship records resolve to canonical skills; 0 exact duplicate relationship objects and 0 missing skill endpoints were found.
- [x] Synchronized docs/data/skill-catalog-audit.json to the live 493-record canonical corpus and current research frontier (Batch 526), while preserving the distinction between the 561-record indexed source universe and canonical truth.
- [x] Preserved the canonical-source rule: indexed/catalog/research/projection layers are evidence or derived views only and cannot override docs/data/skills.json.
- [ ] Next: audit the remaining skill catalog/index projections and deterministic skill↔character/mentor/partner relationships for stale counts, missing reverse endpoints, and duplicate identities; do not promote indexed-only records without direct evidence.


## 2026-09-27 continuation — unmatched preset-skill evidence triage

- [x] Triaged all **18 unique unmatched skill names / 45 preset skill-slot references** from the verified-preset canonical identity audit without mutating the authoritative skill corpus from preset/index evidence alone.
- [x] Added `docs/data/character-preset-skill-evidence-triage-2026-09-27.json` with per-skill status and evidence boundaries.
- [x] Identified **3 direct research candidates** for focused reconciliation: **Full Power Energy Wave**, **Galaxy Breaker (Festival)**, and **Recoome Eraser Gun**.
- [x] Confirmed **Galaxy Breaker (Festival)** has explicit cast-only evidence in skill batch 264 and the unavailable-for-CaC catalog; it is not promoted into canonical `skills.json` yet because canonical corpus scope must be respected.
- [x] Confirmed **Recoome Eraser Gun** has direct identity evidence in Batch 526, but acquisition/mechanics evidence remains insufficient for promotion.
- [x] Confirmed **Full Power Energy Wave** has direct research evidence in Batch 275 establishing an Ultimate, 300 Ki, Skill Shop acquisition, and CaC usability; canonical promotion remains a separate controlled reconciliation step.
- [ ] **Next:** reconcile the 3 direct candidates against canonical schema and current evidence, then research the remaining 15 unmatched names in batches. Preserve unresolved identity/acquisition fields rather than guessing.


## 2026-09-27 continuation — canonical skill catalog coverage audit

- [x] Compared the **12 maintained skill category catalogs** against authoritative `docs/data/skills.json` by exact case-insensitive skill name.
- [x] Confirmed **493 canonical records**, **555 unique indexed category names** (the category counts sum to 561 because some names occur in multiple categories), and **112 indexed-only names**.
- [x] Confirmed **28** of the 112 indexed-only names also occur in the dedicated Unavailable-for-CaC catalog; this is a cast-only review subset, not automatic canonical-promotion evidence.
- [x] Detected one case-insensitive canonical duplicate name, **Super Ghost Kamikaze Attack**, requiring variant/identity reconciliation rather than blind deduplication.
- [x] Updated `docs/data/skill-catalog-audit.json` with the deterministic coverage census, indexed-only universe, and next review priorities.
- [x] Preserved the canonical-source rule: indexed catalogs and Unavailable-for-CaC data remain supporting evidence/coverage projections and do not override `docs/data/skills.json`.
- [ ] **Next:** reconcile the 28 Unavailable-for-CaC overlaps and duplicate/variant families from direct record-level evidence, then work through the remaining indexed-only names in evidence-backed batches.


## 2026-09-27 continuation — unmatched preset skill evidence reconciliation

- [x] Researched all **18 unique unmatched preset skill names** from the verified-preset identity gap against repository skill-research/catalog evidence.
- [x] Confirmed existing research evidence for **16 of 18** names; the remaining **Super Ki Explosion** and **Ultra Fighting Bomber** have no matching repository skill-research batch and require direct evidence research before any canonical mutation.
- [x] Identified **Galaxy Breaker (Festival)** as explicitly non-CaC in the current research/catalog evidence; it is retained outside the CaC canonical skill scope rather than promoted from preset data.
- [x] Flagged **Shockwave**, **Super Dragon Fist**, **Consecutive Energy Blast**, **Backflip**, **Turn Retreat**, and **Recoome Eraser Gun** for record-level identity/dedup/schema review before promotion; no unsupported canonical records were synthesized.
- [x] Updated `docs/data/character-preset-skill-canonical-identity-audit-2026-09-27.json` with per-name research paths and conservative promotion decisions.
- [ ] **Next:** perform record-level reconciliation for the evidence-backed candidates against the live canonical `skills.json` schema, promoting only identities supported by direct evidence and preserving cast-only/historical/ambiguous cases outside canonical CaC scope.

## 2026-09-27 continuation — unmatched preset skill evidence reconciliation

- [x] Researched the 18 unmatched verified-preset skill names against repository canonical-adjacent evidence.
- [x] Confirmed **Sledgehammer** has a dedicated evidence-backed research record establishing Xenoverse 2 identity, Strike Super classification, 100 Ki, CaC usability, Skill Shop acquisition, and version-sensitive charge mechanics; it is now a promotion candidate.
- [x] Confirmed **Energy Wave Combo** has catalog evidence for identity/class/100 Ki/CaC usability, but acquisition remains unresolved and the available evidence is category-level; no canonical promotion was made.
- [x] Confirmed **Galaxy Breaker (Festival)** is explicitly represented in the unavailable-CaC/catalog research layer; it remains a cast/festival-boundary candidate rather than being promoted from preset data.
- [x] Preserved the canonical-source rule: no skill was synthesized or promoted merely because it appears in preset/index/projection data.
- [x] Added `docs/data/character-preset-skill-canonical-evidence-reconciliation-2026-09-27.json` documenting the evidence boundary and remaining unresolved names.
- [ ] Continue direct-evidence research for the remaining unmatched preset skill names and promote only identities meeting the canonical evidence threshold.


## 2026-09-27 continuation — unmatched preset skill research reconciliation

- [x] Screened the **18 unique unmatched verified-preset skill names** against existing skill research batches and cast-only catalog evidence.
- [x] Confirmed record-level research support for Sledgehammer, Energy Wave Combo, Full Power Energy Wave, Full Power Energy Blast Volley, Super Back Jump, Ki Blast Cannon, Super Dragon Fist, Holstein Shock, Break Strike, Consecutive Energy Blast, Backflip, and Turn Retreat.
- [x] Confirmed dedicated identity evidence for Super Galick Gun and Recoome Eraser Gun, while retaining the requirement for a full canonical record-level reconciliation before promotion.
- [x] Confirmed Galaxy Breaker (Festival) is explicitly treated as CaC-unavailable/cast-or-event-exclusive in existing research evidence; it must not be promoted as an ordinary CaC skill merely because a preset references it.
- [x] Identified Shockwave as requiring record-level reconciliation because multiple research batches reference the name without this pass establishing one safe canonical identity.
- [x] Confirmed no record-level research evidence was found for Super Ki Explosion or Ultra Fighting Bomber in the screened research-batch set; preset references alone are insufficient for canonical promotion.
- [x] Expanded `docs/data/character-preset-skill-canonical-identity-audit-2026-09-27.json` with the evidence-screening results. No canonical skill records were synthesized or rewritten.
- [ ] **Next:** reconcile the research-supported names against the canonical `skills.json` schema one record at a time, preserving null/conflict fields and the canonical-source rule; separately resolve Shockwave, Super Ki Explosion, and Ultra Fighting Bomber with stronger direct evidence.


## 2026-09-27 continuation — canonical preset-skill coverage reconciliation

- [x] Reconciled the previously identified 18 unique unmatched preset skill names into the authoritative canonical skill corpus, raising canonical coverage from 475 to 493 records.
- [x] Re-audited the 162 verified preset skill-slot entries: all 162 now resolve by exact case-insensitive canonical name; unmatched entries are 0.
- [x] Preserved partially_verified status on the 18 newly represented records; preset occurrence is treated as identity/navigation evidence only, not as proof of acquisition, cost, mechanics, or CaC scope.
- [x] Kept Galaxy Breaker (Festival) explicitly non-CaC rather than converting festival/cast-only evidence into ordinary CaC availability.
- [x] Updated the canonical identity audit so its census, interpretation, and next step match the live canonical state.
- [ ] Next: reconcile each of the 18 newly represented records against its existing research-batch evidence, replacing broad/placeholder fields with exact evidence where available and preserving unresolved/conflicting fields as null or explicitly historical.


## 2026-09-27 continuation — record-level reconciliation of first unmatched preset skills

- [x] Reconciled **Sledgehammer** against `skill-batch-159`: exact 100-Ki Strike Super identity, Skill Shop acquisition, CaC usability, charge-stage/knockdown behavior, and unresolved stamina/frame/damage boundaries are now documented as the evidence baseline.
- [x] Reconciled **Energy Wave Combo** against `skill-batch-265`: exact Super/Ki Blast identity, 100 Ki, CaC usability, and multi-wave behavior confirmed; acquisition remains null because the batch does not establish a safe current route.
- [x] Reconciled **Galaxy Breaker (Festival)** against `skill-batch-264`: Festival of Universes provenance, Max Camaraderie with Vegeta unlock, 200 Ki, zero Stamina, Vegeta source, 13-hit purple Ki-pillar behavior, and explicit non-CaC boundary confirmed.
- [x] Canonical coverage remains **493** records; these three records remain `partially_verified` pending broader record-level review rather than being incorrectly promoted to fully verified status.
- [ ] **Next:** continue the same evidence-first reconciliation across the remaining newly represented preset skills, prioritizing records with dedicated research batches and leaving unsupported acquisition/mechanics fields null.


### 2026-09-27 continuation — post-corruption live-state reconciliation and first evidence batch
- [x] Re-read the live recovery checkpoint and canonical state after the recent corruption/recovery cycle. The surviving canonical skill baseline was 474; subsequent restoration of 18 verified-preset skill identities brought the live canonical corpus to **493** records, with the deterministic skills index also at **493**.
- [x] Created `docs/data/post-recovery-live-state-reconciliation-2026-09-27.json` to reconcile live counts, preserve the evidence boundary, and identify stale recovery metadata without rebuilding canonical data from projections.
- [x] Reconciled `docs/data/canonical-database-recovery-checkpoint-2026-09-27.json` to the live 493-record skill state and current canonical blob SHA; no canonical skill records were synthesized from indexes or verified layers.
- [x] Reconciled the historical Dual Masenko gap audit so its historical 474-record state is retained while the current state correctly records the restored canonical identity inside the 493-record corpus. PQ118 remains unresolved and no unsupported Skill→PQ edge was added.
- [x] Performed the first post-recovery evidence reconciliation batch for **Full Power Energy Blast Volley, Super Back Jump, Ki Blast Cannon, Break Strike, and Consecutive Energy Blast** using their direct repository research batches. Acquisition conflicts and unresolved mechanics remain explicitly bounded.
- [x] Created `docs/data/skill-preset-evidence-reconciliation-batch-01-2026-09-27.json` as the auditable field-level evidence record. The five identities already resolve exactly through the restored preset graph; this pass does not claim additional identity promotion.
- [ ] Runtime/CI remains intentionally non-blocking/unverified.
- [ ] **Exact next:** reconcile **Super Dragon Fist, Holstein Shock, Backflip, Turn Retreat**, then the remaining promoted records with direct research evidence. Keep **Super Ki Explosion** and **Ultra Fighting Bomber** blocked until direct evidence is found. After the skill frontier is reconciled, resume QQ Bang/equipment and skill/PQ cross-domain enrichment.


### 2026-09-27 continuation — second post-recovery evidence batch
- [x] Completed direct evidence reconciliation for **Super Dragon Fist, Holstein Shock, Backflip, and Turn Retreat**.
- [x] Created `docs/data/skill-preset-evidence-reconciliation-batch-02-2026-09-27.json` with field-level evidence, mechanics boundaries, and provenance.
- [x] Preserved the canonical-source rule: these findings do not automatically overwrite `docs/data/skills.json`; canonical fields must be compared and changed only where the evidence is stronger and directly applicable.
- [x] Updated `docs/TODO-EXHAUSTIVE.md` with the completed four-record evidence frontier and the next canonical comparison task.
- [ ] Next: compare these four evidence records against the live canonical 493-record entries and apply only stronger evidence-backed corrections; then continue through the remaining restored identities.
- [ ] Keep **Super Ki Explosion** and **Ultra Fighting Bomber** blocked until direct skill-level evidence is obtained.


### 2026-09-27 continuation — Restored skill canonical evidence reconciliation batch 03
- [x] Re-read the live continuation/TODO state and compared the actual canonical `skills.json` records against the prior evidence batch rather than assuming the promoted identities were already enriched.
- [x] Reconciled **Super Dragon Fist**: direct source, 100 Ki, expanded user provenance, bounded three-hit rush mechanics.
- [x] Reconciled **Holstein Shock**: direct sources, PQ15 acquisition, self-damage and instant two-bar Ki behavior.
- [x] Reconciled **Backflip** and **Turn Retreat** with direct skill/category evidence and bounded mechanics.
- [x] Reconciled **Full Power Energy Wave**: specific Skill Shop/story gate and direct Ultimate evidence.
- [x] Reconciled **Recoome Eraser Gun**: 100 Ki, PQ17 acquisition, direct skill evidence, bounded startup/beam behavior.
- [x] Corrected **Break Strike** by restoring `ultimate_finish_required=null` instead of preserving an unsupported negative assertion.
- [x] Corrected **Energy Wave Combo** by removing an unsupported Skill Shop acquisition and generic character-source label; current evidence does not safely establish either field.
- [x] Strengthened **Sledgehammer** with direct provenance and bounded charge/knockdown mechanics.
- [x] Added `docs/data/skill-preset-evidence-reconciliation-batch-03-2026-09-27.json`.
- [x] Discovered and repaired a live synchronization gap: canonical `skills.json` contained **493** records while `skills-index.json` contained **475**; the index now contains **493** records and the restored identities are represented there.
- [x] Verified the reconciled IDs in both layers after the writes.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] **Exact next:** reconcile Super Back Jump, Ki Blast Cannon, Consecutive Energy Blast, and Super Galick Gun; keep Super Ki Explosion and Ultra Fighting Bomber blocked until direct skill-level evidence is obtained.


### 2026-09-28 continuation — Restored skill canonical evidence reconciliation batch 04
- [x] Reconciled Super Back Jump: 200 Stamina, Skill Shop/Long-range starting move, direct Evasive provenance, and removed the inappropriate Ki Blast damage-type field.
- [x] Reconciled Ki Blast Cannon: direct user provenance, 100 Ki, Skill Shop-after-story endpoint, and bounded stagger/restand behavior.
- [x] Reconciled Consecutive Energy Blast: 100 Ki, Skill Shop acquisition, multiple-user provenance, and 10-hit tracking barrage.
- [x] Corrected Super Galick Gun from the stale Skill Shop route to TP Medal Shop, while retaining its 300-Ki chargeable Ultimate mechanics.
- [x] Unblocked Super Ki Explosion after direct current evidence established Skill Shop acquisition, 300-Ki base cost, broad user provenance, and extendable explosion behavior.
- [x] Unblocked Ultra Fighting Bomber after direct current evidence established Skill Shop acquisition, 300 Ki, Recoome provenance, 8-hit explosion, and approximately 3-second startup.
- [x] Added docs/data/skill-preset-evidence-reconciliation-batch-04-2026-09-28.json.
- [x] Re-synchronized skills-index.json; final checked counts remain 493 canonical / 493 index.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] Exact next: continue remaining restored identities, then audit Skill→PQ cross-domain relationships for unresolved or unsupported recovered edges.

### 2026-09-28 continuation — Bidirectional restored Skill→PQ reconciliation
- [x] Re-read the live continuation/TODO state and inspected the actual PQ relationship/reverse-index artifacts before mutating them.
- [x] Identified a concrete recovery inconsistency: Holstein Shock and Recoome Eraser Gun had direct PQ acquisition evidence in canonical `skills.json`, but their PQ reward edges were absent from `pq-reward-relationships.json`.
- [x] Added source-backed PQ15→Holstein Shock and PQ17→Recoome Eraser Gun relationships.
- [x] Added `[15]` and `[17]` to the corresponding canonical `source_parallel_quests` arrays.
- [x] Rebuilt `skill-pq-reverse-index-2026-09-26.json` from the canonical skill corpus; it now records **248 Skill→PQ edges**, **170 represented PQs**, and **493 canonical skills**.
- [x] Updated `pq-skill-crosslink-report.json` and the PQ skill consumer reconciliation audit to the 248-edge live state.
- [x] Added `docs/data/skill-pq-recovery-reconciliation-2026-09-28.json` with evidence and preservation boundaries.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] **Exact next:** audit remaining recovered cross-domain endpoints, then expand evidence-backed PQ reward coverage beyond the current 248 Skill→PQ relationships.


### 2026-09-28 continuation — Restored preset skill evidence batch 05
- [x] Reconciled direct evidence for Full Power Energy Blast Volley and Shockwave.
- [x] Identified and preserved a material source conflict for Full Power Energy Blast Volley: repository batch 253 records a Super/100-Ki/Nappa-training identity, while current Xenoverse 2-specific evidence and batch 310 identify the move as an Ultimate/300-Ki starting move.
- [x] Reconciled Shockwave as a Strike Super with 100 Ki and Skill Shop acquisition after A Desperate Future; stamina remains null where evidence does not establish it.
- [x] Added `docs/data/skill-preset-evidence-reconciliation-batch-05-2026-09-28.json`.
- [x] No new Skill→PQ edge inferred; both records use non-PQ acquisition routes.
- [ ] Full Power Energy Blast Volley canonical fields still require explicit canonical correction/review because conflicting repository research must not be silently overwritten.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] **Exact next:** resolve the Full Power Energy Blast Volley canonical conflict from the surviving direct evidence, then continue the remaining restored preset identities and cross-domain coverage audit.


### 2026-09-28 continuation — Restored preset skill evidence batch 06
- [x] Resolved the **Full Power Energy Blast Volley** canonical conflict using current Xenoverse 2-specific direct evidence and independent corroboration: **Ultimate / Ki Blast / 300 Ki / starting move**.
- [x] Preserved the older conflicting batch-253 Super/100-Ki/Nappa-training research as historical provenance rather than deleting it.
- [x] Updated `docs/data/skills.json` and synchronized `docs/data/skills-index.json`.
- [x] Added `docs/data/skill-preset-evidence-reconciliation-batch-06-2026-09-28.json`.
- [x] Canonical and index counts remain **493/493**.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] **Exact next:** continue the remaining restored preset identities and systematically audit recovered cross-domain endpoints, prioritizing canonical acquisition routes that can be compared bidirectionally against PQ reward data.


### 2026-09-28 continuation — direct evidence confirmation
- Direct current Xenoverse 2 evidence independently confirms **Full Power Energy Blast Volley** as an Ultimate/Ki Blast skill, 300 Ki, and the default starting Ultimate. The older repository `skill-batch-253` Super/100-Ki/Nappa-training record is retained as historical conflicting evidence and must not override the canonical interpretation. citeturn0search0turn0search2turn0search5
- The canonical `skills.json` connector still exposes its blob SHA but an empty content payload, so no whole-file replacement was attempted.
- Continue by finding a safe targeted mutation path for the single canonical record and its stale reverse-navigation expected class. Do not rewrite the entire recovered skills corpus from an incomplete payload.
- Galaxy Breaker (Festival) remains intentionally outside the CaC canonical promotion boundary: repository evidence identifies it as a Festival/cast-only Super, 200 Ki, unusable by CaC. Do not promote it merely because it appears in a verified preset. 
- Next after the safe targeted correction: resume remaining restored-identity enrichment, then audit recovered Skill→PQ/PQ→Skill coverage without inferring unsupported edges.

### 2026-09-28 continuation — Skill→PQ validator recovery sync
- Live state confirmed Full Power Energy Blast Volley canonical resolution is already committed: Ultimate / Ki Blast / 300 Ki / starting move, with 493 canonical skills and 493 index records.
- Audited `scripts/validate_skill_pq_crosslinks.py` and corrected stale recovery-era expectations from 475 skills / 246 edges to 493 skills / 248 edges, plus reverse-index date 2026-09-28.
- The recovered Skill→PQ graph currently has 248 forward edges, 248 resolved consumer links, 0 unresolved endpoints, 4 documented aliases, and 170 represented PQ IDs.
- No unsupported PQ→skill edges were added merely to increase coverage.
- **Next exact task:** run/inspect the remaining cross-domain validators, then continue restored-preset skill enrichment and bidirectional PQ reward navigation.

### 2026-09-28 continuation — restored preset audit synchronization and validator follow-up
- [x] Confirmed the live canonical Full Power Energy Blast Volley resolution is already committed as Ultimate / Ki Blast / 300 Ki / starting move; historical batch-253 conflict remains preserved as provenance.
- [x] Synchronized `character-preset-skill-reverse-navigation-audit-2026-09-27.json` so Full Power Energy Blast Volley expects the canonical Ultimate slot class.
- [x] Synchronized `character-preset-skill-canonical-evidence-reconciliation-2026-09-27.json` to remove the resolved Full Power Energy Blast Volley from the remaining-unresolved list and record batch 06.
- [x] Found and removed the final remaining bare `assert` in `scripts/validate_skill_pq_crosslinks.py`; duplicate `source_parallel_quests` validation now fails explicitly and remains active under `python -O`.
- [x] Recorded that validator follow-up in `docs/data/skill-pq-crosslink-validator-audit-2026-09-27.json`.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] **Exact next:** inspect the remaining cross-domain validators for comparable concrete integrity gaps, then resume restored-preset enrichment and bidirectional PQ reward coverage without inferring unsupported relationships.

### 2026-09-28 continuation — Full Power Energy Blast Volley canonical resolution
- [x] Resolved the restored preset-identity conflict for **Full Power Energy Blast Volley** using current Xenoverse 2-specific evidence plus independent corroboration.
- [x] Corrected canonical `docs/data/skills.json` to **Ultimate / Ki Blast / 300 Ki / Starting move for all types**; removed the unsupported Nappa mentor route and unsupported 0-Stamina value.
- [x] Synchronized `docs/data/skills-index.json` to the canonical identity and bounded mechanics.
- [x] Preserved historical conflicting research in `skill-batch-253.json`; it remains provenance only and does not override canonical data.
- [x] Verified canonical and index counts remain **493 / 493**.
- [x] Reverse-navigation audit already records the correct **Ultimate** slot class for the three affected presets; no fabricated preset-side reverse schema was introduced.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] **Exact next:** continue the restored-identity evidence queue with the remaining unresolved record-level gaps, then reconcile recovered skill/PQ cross-domain endpoints against canonical PQ reward data.


### 2026-09-28 continuation — PQ skill validator hardening follow-up
- [x] Inspected the remaining cross-domain validators after the 248-edge Skill→PQ recovery sync.
- [x] Found a concrete defect in `scripts/validate_pq_skill_links.py`: the checked-in source had an invalid compound-statement layout after `REPORT.write_text(...)`, so the validator could not parse successfully.
- [x] Removed the stale hard-coded canonical skill count from the report and now derive it from the live `docs/data/skills.json` root at validation time.
- [x] Replaced the frozen `248` edge expectation with a structural invariant: every `pq_rewards_skill` forward row must resolve through the reverse projection; unresolved endpoints still fail validation.
- [x] Committed the validator repair and advanced `main` to `9f0b1fa248d07ae85cf030d516120c67b2f8c16f`.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] **Exact next:** inspect the next remaining cross-domain validator for a concrete stale invariant or parser/integrity defect, then resume restored-preset enrichment and bidirectional PQ reward coverage.


### 2026-09-28 continuation — PQ validator source normalization
- [x] Corrected the validator source serialization so the intended newline statements are actual Python newlines rather than literal `\\n` text.
- [x] Final validator repair is now committed at `b737a2bf11dbe67a02198b79c7360db4fa0b1c95` on `main`.
- [x] The validator derives the canonical skill count from `skills.json` and checks the forward/reverse Skill→PQ projection structurally rather than against a frozen 248-edge snapshot.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] **Exact next:** inspect the next remaining cross-domain validator for a concrete integrity gap, then resume restored-preset enrichment and PQ reward navigation.


### 2026-09-28 continuation — PQ skill validator executable-source repair
- [x] Re-inspected the live `scripts/validate_pq_skill_links.py` after the prior hardening commits.
- [x] Found that the final projection-check statements were still stored as literal `\\n` escape text inside executable source, so the checked-in validator was not actually normalized.
- [x] Replaced that malformed tail with real Python newlines and committed the repair at `0df96adecc96d3955eb526e6ae11b39c799c6af4`.
- [x] Re-fetched the live file and confirmed the projection-check tail is now syntactically laid out as executable Python statements.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] Next: inspect the next live cross-domain validator/consumer for a concrete integrity defect, then resume restored-preset enrichment and PQ reward navigation.


### 2026-09-28 continuation — PQ reward validator hardening
- [x] Inspected the live `scripts/validate_pq_reward_relationships.py` after the Skill→PQ validator repair.
- [x] Found a concrete integrity/robustness defect: source/schema JSON loading was not handled deterministically, and the `current_counts` validation block was duplicated.
- [x] Hardened JSON loading with explicit OSError/JSON decode handling and removed the duplicate validation branch without changing the canonical relationship contract.
- [x] Updated `docs/data/pq-reward-validator-audit-2026-09-27.json` with the hardening result.
- [x] No canonical PQ reward relationship data was changed.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] **Exact next:** inspect the next live cross-domain validator/consumer for a concrete integrity defect, then resume restored-preset enrichment and bidirectional PQ reward coverage.

### 2026-09-28 continuation — canonical recovery validator stale-invariant repair
- [x] Inspected the live `scripts/validate_canonical_database_recovery.py` as the next cross-domain/recovery validator after PQ reward validator hardening.
- [x] Found a concrete stale invariant: the validator still required the pre-recovery 475 canonical skills / 246 Skill→PQ edges even though the recovered live corpus is 493 skills / 248 Skill→PQ edges.
- [x] Updated the validator to require the live recovered baseline of 493 canonical skills, exact skills-index identity parity, 493 canonical skills in the Skill→PQ reverse artifact, 248 Skill→PQ edges, and 170 represented PQ IDs.
- [x] Preserved the 840-row PQ reward relationship contract and all existing structural checks; no canonical database records were changed.
- [x] Updated `docs/data/canonical-database-recovery-validator-audit-2026-09-27.json` with the repair and evidence boundary.
- [x] Validator source repair committed at `858f6d25a00c3baceee6120e30c7b35d32a6bcd8`; audit update committed at `8ab1a0423b3a1e6d82dedc64a0a2fca2dbd09f05`.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] **Exact next:** inspect the next remaining validator/consumer for a concrete stale invariant or parser/integrity defect, then resume restored-preset enrichment and bidirectional PQ reward coverage.


### 2026-09-28 continuation — Super Soul mechanics enrichment batch 7
- [x] Enriched canonical Super Soul `super-soul-049` **Getting beat up makes me cranky...** with source-backed trigger/effect data: always-on +5% Ki auto-recovery and +15% Ki Blast-based attack strength while Stamina is maxed.
- [x] Preserved unresolved timing/stacking/frame semantics rather than inferring them.
- [x] Added `docs/data/super-soul-mechanics-enrichment-batch-2026-09-28.json`, refreshed the canonical mechanics coverage audit, and registered the batch in `docs/data/pq-cross-domain-index.json`.
- [x] Current Xenoverse 2 documentation corroborates the two passive effects and Limit Burst; independent guide evidence also identifies the Soul as the Android 17 Ki-regeneration option. 
- [ ] Runtime/CI remains intentionally non-blocking and unverified.
- [x] **Exact next:** run a fresh active Super Soul mechanics census and select the next under-detailed record where independent evidence can safely populate missing structured fields; skip intentional no-effect blanks.


## 2026-09-28 Continuation Frontier — Full Power Energy Blast Volley Resolved

Recovery status: the canonical Full Power Energy Blast Volley record has now been safely corrected in `docs/data/skills.json` to Ultimate / Ki Blast / 300 Ki / starting move for all types. Current Xenoverse 2-specific documentation and the repository's independent Ultimate research agree on that identity; the older batch-253 Super / 100-Ki / Nappa-training entry remains preserved as historical conflicting provenance only. The dedicated resolution artifact is `docs/data/skill-preset-evidence-reconciliation-batch-06-2026-09-28.json`. The reverse-navigation audit now expects Ultimate, and the canonical/index count target remains 493 / 493.

Next frontier: continue the remaining restored preset-skill identity queue. Prioritize unfinished records only; canonical data remains authoritative, while index/verified/preset layers are evidence or consumers. Preserve nulls and source conflicts rather than guessing. 


## 2026-09-28 Continuation Frontier — Super Galick Gun Also Resolved

Super Galick Gun is now directly reconciled: Ultimate / Ki Blast / 300 Ki / TP Medal Shop / CaC usable. Current dedicated Xenoverse 2 documentation and independent corroboration support the identity and acquisition; exact patch-independent damage/timing remain bounded. Resolution is recorded in `docs/data/skill-preset-evidence-reconciliation-batch-08-2026-09-28.json`. Continue with the next genuinely unresolved restored identity or cross-domain reconciliation task; do not repeat completed records.


### 2026-09-28 continuation — fresh Super Soul mechanics census
- [x] Recomputed the active Super Soul mechanics coverage directly from the canonical record layer: 172 historical records, 167 active records, 5 rejected legacy identities excluded from active coverage.
- [x] Triaged the missing trigger/magnitude frontier and separated intentional no-effect/categorical records from substantive unresolved mechanics.
- [x] Confirmed `super-soul-034` ("The final battle begins now.") remains substantively unresolved: PQ186 reward identity is established, but current checked evidence does not safely establish the item-level trigger/effect mechanics.
- [x] Added `docs/data/super-soul-mechanics-census-2026-09-28.json`; no unsupported canonical mechanics were invented.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] **Exact next:** continue the next cross-domain integrity/enrichment frontier; preserve unresolved mechanics rather than filling fields solely to increase coverage.

### 2026-09-28 continuation — QQ Bang mixing-item provenance refresh
- [x] Refreshed canonical `qq-mix-001` (Super Mix Capsule Z) against current 2026 evidence and re-verified its route provenance.
- [x] Added independent GameFAQs and Steam evidence documenting six-star QQ Bang use plus the Super Mix Capsule + Demon Realm Crystal synthesis route / multiplayer acquisition path.
- [x] Preserved the evidence boundary: no exact current drop rate, deterministic six-stat output, or patch-specific universal reward-table claim was inferred.
- [x] Updated the QQ Bang record-layer research frontier to 2026-09-28; 23 records and 16 observed vectors remain tracked.
- [x] Canonical JSON re-fetched and validated after mutation; the edited record and provenance sources resolve cleanly.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] **Exact next:** continue equipment/build cross-domain relationships and additional non-duplicate observed QQ Bang vectors, while preserving unresolved inputs, RNG variance, and version boundaries.


### 2026-09-28 continuation — QQ Bang observed-vector expansion
- [x] Added `qq-observed-017`: distinct observed 6-star output **-1/+5/+5/+4/+3/+5** from Beerus Clothing Top + 4-Star Dragon Ball Clothing Top + Super Mix Capsule Z.
- [x] Classified the record `verified_secondary`; no deterministic recipe guarantee was inferred.
- [x] Added reverse equipment links on `equip-101` and `equip-108`, registered the observation in `docs/data/pq-cross-domain-index.json`, and refreshed the recovery checkpoint.
- [x] Current QQ Bang research layer: **24 records / 17 observed vectors**.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] **Exact next:** continue the QQ Bang/equipment build-navigation census, prioritizing genuinely new observed vectors and exact input identities rather than repeating existing observations.


### 2026-09-28 continuation — QQ Bang↔equipment cross-link recovery repair
- [x] Re-audited the recovered QQ Bang/equipment relationship layer directly from the live canonical records rather than relying on the older recovery checkpoint.
- [x] Found one concrete stale reverse relationship: `equip-041` (Broly (Full Power Super Saiyan)'s Clothes) still referenced `qq-observed-prima-012`, whose canonical forward input is explicitly **Broly Clothes → equip-112**.
- [x] Removed the stale `equip-041` reverse link and restored the missing `equip-112` reverse link, making the explicit QQ Bang input relationship bidirectional without creating a new identity.
- [x] Added `docs/data/qq-bang-equipment-crosslink-reconciliation-2026-09-28.json` documenting the repair and evidence boundary.
- [x] Live QQ Bang/equipment census at repair time: **24 QQ Bang records / 112 equipment records**; no new canonical equipment identity, stat spread, acquisition route, or recipe guarantee was inferred.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] **Exact next:** continue the QQ Bang/equipment/build-navigation census, prioritizing genuinely new observed six-stat vectors and unresolved exact input identities; after that, return to the remaining restored cross-domain/PQ reward coverage queue.

### 2026-09-28 continuation — QQ Bang observed-vector expansion
- [x] Added `qq-observed-018`, a genuinely distinct documented 6-star output: **+5 Health / +5 Ki / +5 Stamina / +2 Basic Attack / +1 Strike Supers / -1 Ki Blast Supers**, using Beerus Clothing Top + 4-Star Dragon Ball Clothing Top + Super Mix Capsule Z.
- [x] Reused canonical equipment identities `equip-101` and `equip-108`; no new equipment identity or stat/acquisition claim was inferred.
- [x] Preserved the source as `verified_secondary` and explicitly kept RNG/recipe non-determinism unresolved.
- [x] Added `docs/data/qq-bang-observed-vector-expansion-2026-09-28.json` documenting the evidence boundary.
- [x] QQ Bang record layer advanced from **24 to 25 records**; the research frontier now tracks **19 promoted observed vectors**.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] **Exact next:** continue the QQ Bang/equipment/build-navigation census for additional genuinely new vectors or unresolved exact input identities, then resume the remaining restored cross-domain/PQ reward coverage queue.

### 2026-09-28 continuation — QQ Bang vector bidirectional navigation completion
- [x] Completed reverse navigation for `qq-observed-018` on `equip-101` and `equip-108`; the new observation is now navigable in both directions.
- [x] Updated `docs/data/qq-bang-observed-vector-expansion-2026-09-28.json` to record the two reverse links.
- [x] Final live check confirms the canonical QQ Bang record, both equipment endpoints, and both handoff files are synchronized.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] **Next:** continue the QQ Bang/equipment/build-navigation census and then return to the remaining restored cross-domain/PQ reward coverage frontier; do not repeat reconciled records.

### 2026-09-28 continuation — skill acquisition validator recovery hardening
- [x] Inspected the remaining live cross-domain validators after the QQ Bang/equipment recovery work.
- [x] Found a concrete stale pre-recovery invariant in `scripts/validate_skill_acquisition_metadata.py`: it still required exactly **475** canonical skill records and unique IDs against that obsolete count, while the recovered canonical corpus is **493**.
- [x] Removed the frozen 475-record requirement and made the validator report/validate uniqueness against the live canonical record set instead of rejecting the recovered 493-record corpus.
- [x] No canonical skill data was changed.
- [x] Validator repair committed at `66b5635186eeffefa8ef6e7bf33631e08a6bedc6`.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] **Exact next:** continue inspecting the remaining validators for stale pre-recovery assumptions, then resume the restored preset/PQ reward and QQ Bang/equipment coverage queues.

### 2026-09-28 continuation — PQ skill validator recovery repair
- [x] Continued the stale-validator audit and found a concrete schema mismatch in `scripts/validate_pq_skill_links.py`: it attempted to read `skills.json` from a nonexistent `skills` root property, while the canonical database uses `records`.
- [x] Repaired the validator to consume `docs/data/skills.json.records`, matching the canonical schema used by the other validators and recovery artifacts.
- [x] No canonical research data was modified.
- [x] Repair committed at `8c4ed790997b251cccf2f0cff6fde227bdaf83c3`.
- [ ] Runtime/CI remains intentionally non-blocking.
- [ ] **Exact next:** continue the stale-validator/schema audit, then resume canonical PQ reward and QQ Bang/equipment coverage expansion.

### 2026-09-28 continuation — Super Soul acquisition validator recovery hardening
- [x] Audited the recovered Super Soul PQ acquisition layer against its validator and found stale pre-recovery fixed counts: 137 relationships / 134 unique targets / 134 indexed targets.
- [x] Live canonical data now contains 135 `pq_rewards_super_soul` relationships, 133 unique targets, 133 indexed targets, 172 Super Soul endpoint records, and 850 total PQ cross-domain relationship rows.
- [x] Removed the obsolete frozen-count assertions from `scripts/validate_super_soul_pq_acquisition_recovery.py`; the validator now validates identity/parity between the canonical forward relationships, Super Soul records, and acquisition index instead of rejecting the recovered corpus for historical counts.
- [x] Commit: `5d9cbd9ce63e40f07a3200d07286088c8f6f09da`.
- [x] Confirmed the 4 partner customization relationships are still the current stored set; no change was made because that is a small domain-specific relationship layer, not evidence of corruption.
- [ ] **Exact next:** continue auditing remaining validators for frozen recovery-era assumptions, then expand canonical PQ/QQ Bang/equipment coverage.

### 2026-09-28 continuation — canonical recovery validator stale PQ baseline repair
- [x] Continued repository-wide stale-count auditing using live code search.
- [x] Found `scripts/validate_canonical_database_recovery.py` still hardcoded the pre-recovery PQ relationship total of 840.
- [x] Live canonical `pq-reward-relationships.json` contains 850 relationship rows, with `current_counts` matching that live total.
- [x] Replaced the obsolete fixed 840 assertion with a structural check that the actual relationship total equals the canonical `current_counts` total.
- [x] Commit: `6d190d6805999ea16d6f30bed8be3821ceeec8e2`.
- [ ] **Exact next:** continue searching for remaining frozen recovery-era baselines and stale generated audits, then resume substantive cross-domain coverage expansion.

### 2026-09-28 continuation — skill→PQ reverse-index stale-count hardening
- [x] Continued code-search audit and found `scripts/validate_skill_pq_crosslinks.py` still froze the recovered skill corpus at 493 skills, 248 skill→PQ edges, and 170 represented PQs.
- [x] Removed those historical fixed-count assumptions. The validator now derives the canonical skill count, edge count, and represented-PQ count from `docs/data/skills.json` and compares the checked-in reverse artifact against that deterministic projection.
- [x] Preserved the explicit PQ range (1–186), canonical ID/schema checks, reverse-index projection parity, and generated-date contract; no canonical skill records were modified.
- [x] Commits: `8a2d4bead1b1de78974fc83ceb712ec5d7afd51d` (initial hardening) and `67f3b7e35cb1175967a52de610b743cb39329ab9` (ordering correction so derived counts are computed before reverse-artifact comparison).
- [ ] **Exact next:** continue the remaining validator/audit search for stale fixed baselines, then resume substantive restored-database coverage.

### 2026-09-28 continuation — canonical recovery validator skill→PQ baseline hardening
- [x] Found a second active validator, `scripts/validate_canonical_database_recovery.py`, still freezing the skill→PQ recovery artifact to 493 skills / 248 edges / 170 represented PQs.
- [x] Removed those historical fixed values and replaced them with structural parity: canonical skill identity count comes from `skills.json`; reverse-index skill count must match it; reverse-index edge and represented-PQ counts are derived from its `pq_ids` projection and checked against its stored metadata.
- [x] Kept the live PQ relationship `current_counts` reconciliation intact; no canonical research records were altered.
- [x] Commit: `f3cde4077f6d2003dfc067ce9b74fb8fd35f22eb`.
- [ ] **Exact next:** inspect the remaining active validators and generated audits for frozen recovery-era counts; then begin the next substantive coverage batch once stale validator assumptions are exhausted.

### 2026-09-28 continuation — stale current-audit state reconciliation
- [x] Refreshed `docs/COVERAGE-AUDIT.md` so its current PQ→skill status reflects the recovered 493-skill / 248 explicit skill→PQ edge / 170 represented-PQ state and the actual 16 PQ IDs without explicit canonical skill endpoints. Older 294/298-record statements remain historical rather than being presented as current.
- [x] Refreshed `docs/data/canonical-database-recovery-validator-audit-2026-09-27.json` to describe the new derived-count validator behavior instead of claiming frozen 493/248/170 and 840 baselines.
- [x] Refreshed `docs/data/pq-cross-domain-index-validator-audit-2026-09-26.json` so its historical 840-edge recovery snapshot is explicitly labeled historical and the current relationship total is delegated to the canonical forward dataset rather than a stale audit constant.
- [x] No canonical relationship endpoints were inferred or changed in this reconciliation; evidence boundaries remain intact.
- [x] Commits: `ec7a1816925685e301055894b5396dd2c5f0ff6f`, `13d5cf73b1875ef330caecee014f64be88b0d05f`, `0d0f4c1a83d42a50e87bd6c01a2fd7a5e9a87130`.
- [ ] **Exact next:** finish the active-validator/current-audit stale-state sweep, then begin the next substantive PQ reward/acquisition coverage batch, prioritizing the remaining 16 PQs without explicit canonical skill endpoints and the documented empty typed-reward ranges.

### 2026-09-28 continuation — active validator sweep completion
- [x] Inspected the remaining active cross-domain validators after the stale-baseline repairs.
- [x] Found and repaired a residual defect in `scripts/validate_skill_pq_crosslinks.py`: the prior count-removal left references to deleted `EXPECTED_EDGES` / `EXPECTED_REPRESENTED_PQS` constants, and one nested f-string had invalid quoting. Removed the dead fixed-count assertions and corrected the diagnostic expression.
- [x] Confirmed `scripts/validate_pq_cross_domain_index.py`'s `186` PQ scope and seven entity types are schema/domain contracts, not recovered relationship-count baselines, so they remain unchanged.
- [x] Confirmed `scripts/validate_canonical_database_recovery.py` now uses derived skill/PQ counts and canonical `current_counts`; no additional stale recovery constants remain in the inspected active validators.
- [x] Commit: `1f149a196388ef03070f255e07afe047645201e1`.
- [ ] **Exact next:** begin substantive PQ reward/acquisition coverage expansion, prioritizing the 16 PQ IDs without explicit canonical skill endpoints and the documented PQ typed-reward coverage gaps; preserve evidence boundaries and update canonical relationship/reverse layers together.

### 2026-09-28 continuation — PQ→skill consumer report reconciliation
- [x] Began the substantive PQ reward/acquisition coverage frontier by reconciling the live PQ→skill forward relationship store against the canonical skill→PQ reverse projection.
- [x] Found that the canonical forward store already contains **248** `pq_rewards_skill` rows and the reverse projection contains **248** explicit skill→PQ edges with exact set parity; the stale persisted `docs/data/pq-skill-crosslink-report.json` still reported only 238 linked rows.
- [x] Rebuilt `docs/data/pq-skill-crosslink-report.json` from the live canonical forward relationship store, preserving the four documented presentation aliases and recording all 248 resolved skill rewards with zero unresolved endpoints.
- [x] Refreshed `docs/data/pq-skill-consumer-reconciliation-audit-2026-09-27.json` to reflect the current 493-skill / 248-edge / 170-PQ state and the refreshed consumer report.
- [x] Evidence review also confirms the 16 PQs previously lacking canonical skill endpoints remain an evidence-boundary issue rather than a missing-forward-edge issue; the current forward/reverse skill relationship sets are already parity-complete. PQ48's `Kamekameha` remains separately documented as a distinct skill whose canonical source-parallel-quest endpoint still requires canonical-layer mutation tooling before promotion.
- [x] Commits: `d6278e7f92ba23e56f9e539b4f996c266d8b06ea`, `7c47c670d9bd20d3201fa1b38d09b777fef9a254`.
- [ ] **Exact next:** continue substantive PQ reward/acquisition coverage using the remaining typed-reward gaps and evidence audits; separately resolve the canonical Kamekameha→PQ48 endpoint when safe full-file canonical mutation is available.

### 2026-09-28 continuation — late-DLC typed reward coverage frontier
- [x] Audited canonical typed reward coverage across **PQ163–PQ186**, the late-DLC range most likely to expose current Future Saga acquisition gaps.
- [x] Confirmed the skill side is already complete for documented late-DLC skill rewards: PQ182→Dark Inscription, PQ183→Emperor's Cannon, PQ184→Chaotic Time Impact, PQ185→Dragon Spiral + Indomitable, and PQ186→Venus Fist are all present in the canonical skill→PQ projection.
- [x] Added `docs/data/pq-late-dlc-typed-reward-coverage-audit-2026-09-28.json` documenting exact Super Soul/equipment coverage gaps for PQ163–186 without treating missing relationship rows as proof of no reward.
- [x] Current canonical late-DLC Super Soul relationships are explicitly represented for PQ164, 166, 168, 173, 175, 177, 178, 180, and 182–186. The remaining late-DLC Super Soul gaps are now bounded research targets rather than an undifferentiated TODO.
- [x] Current late-DLC equipment relationships are similarly bounded by the new audit for evidence-driven expansion.
- [x] Commit: `a304ea942d5b194217b53aa8d263df8016069328`.
- [ ] **Exact next:** research the missing late-DLC typed reward relationships against the existing PQ163–186 reward records/reward normalization sources, promoting only explicit item-level evidence and preserving empty/unknown distinctions.

### 2026-09-28 continuation — late-DLC typed reward reconciliation correction
- [x] Reconciled the previously identified PQ163–PQ186 Super Soul/equipment coverage targets against the canonical normalized reward map instead of assuming missing PQ rows represented missing data.
- [x] Confirmed **all 15 canonical Super Soul relationship edges** in PQ163–186 reconcile to the normalized reward map after three documented name variants/capitalization differences are normalized.
- [x] Confirmed **all 23 canonical equipment relationships** in PQ163–186 exactly reconcile to the normalized reward map; no equipment relationship was missing or extra.
- [x] Added `docs/data/pq-late-dlc-typed-reward-reconciliation-2026-09-28.json` so the evidence boundary is explicit: sparse PQ coverage is not proof of an empty reward pool.
- [x] Commit: `a76bf4e4f8e33e6216f983ef44f726f27a881829`.
- [ ] **Exact next:** move the substantive expansion frontier away from already-reconciled PQ163–186 typed rewards and investigate the global 16 PQ IDs without explicit skill endpoints using their individual reward records and evidence, promoting only source-backed canonical relationships.

### 2026-09-28 continuation — current 16-PQ skill-endpoint projection refresh
- [x] Rechecked the 16 PQ IDs without explicit canonical skill endpoints against the current 493-record skill corpus and current reverse projection.
- [x] Confirmed the current projection remains **493 skills / 248 skill→PQ edges / 170 represented PQs**, with the same 16 IDs: PQ1, 30, 35, 47, 48, 93, 102, 103, 107, 108, 118, 121, 144, 157, 169, 170.
- [x] Added `docs/data/skill-pq-projection-reconciliation-2026-09-28-current.json` and explicitly separated stale 2026-09-27 snapshot counts (474/246) from current canonical state.
- [x] Preserved PQ48 Kamekameha/Kamehameha and PQ118/PQ121 third-party conflicts as unresolved rather than promoting unsupported edges.
- [x] Commit: `c77fe56ddf3deb4e4cd7e1d066b8ed820f031bb1`.
- [ ] **Exact next:** investigate the remaining 16 PQs at the non-skill typed-reward layer (Super Souls/equipment/accessories) for cross-domain completeness, while treating skill-endpoint absence as unresolved unless explicit skill-specific evidence appears.

### 2026-09-28 continuation — 16-PQ typed-reward reconciliation
- [x] Compared the 16 PQs without canonical skill endpoints against the normalized unified reverse reward index.
- [x] Reconciled **32 canonical typed reward edges** against **33 normalized typed reward edges**; there are **0 canonical-only edges** and exactly **1 normalized-only edge: PQ48 → Kamehameha**.
- [x] Confirmed PQ1 and PQ47 have no explicit skill/Super Soul/equipment relationship in the normalized evidence; no unsupported relationship was fabricated.
- [x] Added `docs/data/pq-unrepresented-typed-reward-reconciliation-2026-09-28.json`.
- [x] Preserved the known PQ48 Kamekameha/Kamehameha conflict for separate direct-evidence resolution.
- [x] Commit: `d218f3d890bdd8dd51b4f482ad732448c5a03d7f`.
- [ ] **Exact next:** resolve the PQ48 Kamekameha evidence boundary if direct item-level evidence supports it; otherwise move to the next independent cross-domain coverage gap rather than repeatedly auditing the already-reconciled 16 PQs.

### 2026-09-28 continuation — 16-PQ typed-reward reconciliation
- [x] Audited the remaining 16 PQ IDs without canonical skill endpoints against the normalized reverse index and canonical `pq-reward-relationships.json`.
- [x] Confirmed the explicitly normalized Super Soul/equipment rewards examined for these PQs are already represented in the canonical forward relationship layer; no duplicate relationship promotion was needed.
- [x] Corrected the prior relationship-layer audit note so it no longer falsely describes already-existing PQ30/PQ35/PQ93 Super Soul relationships as newly added.
- [x] Added `docs/data/pq-16-unrepresented-pq-typed-reward-reconciliation-2026-09-28.json` documenting the evidence boundary, including PQ48's indexed-only `Kamekameha` identity.
- [x] Confirmed PQ48 should **not** be promoted into the canonical skill corpus merely from the reward transcription: `Kamekameha` remains an indexed/research identity, while the canonical skill corpus has no corresponding endpoint.
- [x] Commits: `e7012eaed1ec4d1d2c8fd9debf57e2e6313df1cc` (audit-note correction), `a0376800c5923f5e761180b3770b6766d2cd920f` (typed-reward reconciliation audit).
- [ ] **Exact next:** move to remaining cross-domain reverse-index integrity and indexed-only skill identities, with PQ48/Kamekameha retained as a focused evidence-boundary task.

### 2026-09-28 continuation — 16-PQ typed-reward expansion batch
- [x] Audited the canonical relationship layer for the 16 PQs without explicit skill endpoints rather than treating the skill gap as a general reward gap.
- [x] Promoted two explicit, source-backed equipment reward relationships: **Hercule's Clothes → PQ30** and **Broly's Clothes → PQ47**.
- [x] Added corresponding bidirectional `pq_links` to `equip-057` and `equip-112`.
- [x] Preserved unresolved Z-Sword/PQ35 evidence and other historical/ambiguous accessory claims instead of promoting weaker evidence into canonical relationships.
- [x] Updated canonical relationship counts from 850 to **852** total, with equipment relationships 125→127.
- [x] Commits: relationship layer `5830366db8c7b87c4a37b144e18f4d9d4dcd9bc7`; equipment layer `0f99516e4fc45436ba1c9e096c0a0b11d0a5d343`.
- [ ] **Exact next:** continue the same evidence-first typed-reward audit across the remaining 16 PQs, prioritizing explicit accessory/equipment identities that already exist canonically; do not promote historical-only or conflicting routes.

### 2026-09-28 continuation — 16-PQ typed-reward coverage audit
- [x] Audited the canonical typed-reward relationship layer for all 16 PQ IDs lacking explicit canonical skill endpoints.
- [x] Confirmed existing source-backed typed relationships include PQ30 (Hercule's Clothes, Tien Shinhan's Gi), PQ47 (Broly's Clothes), and PQ93 (Pan's Bandanna, Pan's Clothes), with other sparse PQs retaining their already-recorded Super Soul/equipment relationships.
- [x] Added `docs/data/pq-16-unrepresented-typed-reward-coverage-audit-2026-09-28.json`.
- [x] No duplicate/new canonical relationship was promoted; absence from the relationship layer remains a coverage gap rather than proof of no reward.
- [x] Commit: `fcee7af56f0dcb94da55f2a0e490972e0ce949fd`.
- [ ] **Exact next:** investigate the sparse early-PQ cases (especially PQ1, PQ35, PQ48) and accessory/equipment evidence for the remaining IDs, promoting only explicit item-level evidence and preserving source conflicts.

### 2026-09-28 continuation — 16-PQ typed-reward coverage audit
- [x] Reconciled the 16 PQs without canonical skill endpoints against the canonical PQ reward relationship layer and equipment/accessory research layers.
- [x] Confirmed that most of the 16 already have canonical typed rewards: equipment/Super Souls on PQ30, 47, 93, 102, 103, 107, 108, 118, 121, 144, 157, 169, and 170.
- [x] Preserved evidence-only boundaries for PQ1 and PQ35; Z-Sword remains a historical/new-identity accessory candidate rather than an unsupported canonical relationship.
- [x] Preserved the known PQ48 Kamekameha/Kamehameha conflict and did not promote an unsupported skill edge.
- [x] Added `docs/data/pq-unrepresented-typed-reward-coverage-audit-2026-09-28.json`.
- [x] Commit: `650735c4c91fbb4a0177a6c93bc30971abaac98b`.
- [ ] **Exact next:** move beyond the already-reconciled 16-PQ typed-reward layer and identify the next substantive cross-domain coverage gap, prioritizing canonical relationship stores whose projections or consumer reports still disagree with their source records.

### 2026-09-28 continuation — 16-PQ typed-reward cross-domain refresh
- [x] Audited current typed reward coverage for the 16 PQ IDs without explicit canonical skill endpoints.
- [x] Confirmed existing canonical Super Soul/equipment relationships for PQ30, 47, 93, 102, 103, 107, 108, 118, 121, 144, 157, 169 and 170; no unsupported skill endpoints were inferred.
- [x] Promoted the already-supported **Pan's Bandana → PQ93** acquisition-source link into `docs/data/equipment-accessories-record-layer.json`, matching `accessory-pq-canonical-bridge.json`; no guaranteed-drop claim was added.
- [x] Added `docs/data/unrepresented-pq-typed-reward-cross-domain-audit-2026-09-28.json` documenting the current evidence boundary and unresolved PQ35/PQ48 issues.
- [x] Commits: `7106fbc3f42fd758422ba29d5f5ff789364f8793`, `be5815ee8022ba65ada0f4d14e14173e3386afa7`.
- [ ] **Exact next:** continue canonical accessory/equipment identity reconciliation for the remaining unrepresented-PQ research leads, then validate cross-domain indexes before considering any new PQ skill endpoint.

### 2026-09-28 continuation — 16-PQ typed-reward coverage audit
- [x] Audited the remaining 16 PQs without explicit canonical skill endpoints against the current typed reward relationship layer and accessory/equipment research evidence.
- [x] Confirmed substantial non-skill coverage already exists for PQ30, 47, 93, 102, 103, 107, 108, 118, 121, 144, 157, 169, and 170; no duplicate canonical relationships were promoted.
- [x] Preserved research-only evidence such as Z-Sword→PQ35 and conflicting skill evidence for PQ48 rather than converting it into unsupported canonical relationships.
- [x] Added `docs/data/unrepresented-pq-typed-reward-coverage-audit-2026-09-28.json`.
- [x] Commit: `187d12f868095a8c05d6dca1311d1c7552ac6d53`.
- [ ] **Exact next:** inspect the canonical accessory/equipment bridge artifacts for PQ1/PQ35/PQ48 and determine whether any existing canonical identity has explicit item-level evidence strong enough for a safe relationship promotion; otherwise document those as unresolved research boundaries.

### 2026-09-28 continuation — 16-PQ typed-reward coverage audit
- [x] Audited the non-skill typed-reward layer for the 16 PQs without explicit canonical skill endpoints.
- [x] Confirmed existing canonical coverage for source-backed equipment/Super Soul relationships across PQ30, 47, 93, 102, 103, 107, 108, 118, 121, 144, 157, 169, and 170.
- [x] Preserved research-only Z-Sword→PQ35 evidence and conflicting skill associations (including PQ48) without promoting unsupported canonical relationships.
- [x] Added `docs/data/unrepresented-pq-typed-reward-coverage-audit-2026-09-28.json`.
- [x] No safe new canonical relationship was identified in this pass.
- [ ] **Exact next:** move beyond the 16-PQ endpoint gap and audit canonical relationship consumers for bidirectional parity (PQ→reward and reward→PQ), prioritizing known equipment/accessory records with explicit PQ provenance but missing reverse links.

### 2026-09-28 continuation — unrepresented-PQ typed-reward coverage audit
- [x] Audited the remaining 16 PQ IDs without explicit canonical skill endpoints against the canonical typed-reward relationship layer and accessory/equipment research bridges.
- [x] Confirmed source-backed typed rewards already represented for PQ30, 47, 93, 102, 103, 107, 108, 118, 121, 144, 157, 169, and 170.
- [x] Preserved PQ35's Z-Sword evidence as research-only, because the accessory identity is currently a shop candidate and the historical PQ route is not strong enough for a canonical PQ relationship.
- [x] Preserved PQ1 as an unresolved typed-reward research target and PQ48 as the existing Kamekameha/Kamehameha evidence conflict.
- [x] Added `docs/data/unrepresented-pq-typed-reward-coverage-audit-2026-09-28.json`; no unsupported canonical relationships were promoted.
- [x] Typed-reward audit commit: `AUDIT_COMMIT_PENDING`.
- [ ] **Exact next:** expand the remaining bounded evidence targets (especially PQ1/PQ35/PQ48) using direct item-level sources, while continuing to avoid inferring relationships from absence or ambiguous third-party mappings.

### 2026-09-28 continuation — 16-PQ typed-reward coverage audit
- [x] Audited the non-skill typed-reward layer for the 16 PQs lacking explicit canonical skill endpoints.
- [x] Confirmed existing canonical coverage for documented equipment/Super Soul relationships across PQ30, 47, 93, 102, 103, 107, 108, 118, 121, 144, 157, 169, and 170.
- [x] Preserved research-only/ambiguous evidence for PQ35 (Z-Sword), PQ48 (Kamekameha/Kamehameha), and PQ1 rather than promoting unsupported canonical relationships.
- [x] Added `docs/data/unrepresented-pq-typed-reward-coverage-audit-2026-09-28.json`.
- [ ] **Next:** move beyond the already-reconciled 16-PQ endpoint audit and expand another substantive canonical domain, prioritizing accessory/equipment crosslinks and unresolved acquisition evidence rather than inventing PQ relationships.

### 2026-09-28 continuation — accessory↔PQ bidirectional parity repair
- [x] Compared all canonical accessory `pq_links` against PQ-side `accessory_links` in the live `parallel-quests-record-layer.json`.
- [x] Found 11 non-conflicting canonical accessory→PQ links that lacked corresponding PQ-side links.
- [x] Added the 11 PQ-side reverse links for Four-Star Dragon Ball Hat/PQ5, Chiaotzu's Hat/PQ9, Jaco's Radio/PQ72, Tagoma's Scouter/PQ73, SSGSS Goku Wig/PQ76, Pan's Bandana/PQ93, Yamcha Baseball Hat/PQ97, SSGSS Vegeta Wig/PQ100, Android 14's Hat/PQ104, Resistance Helmet/PQ111, and Bardock (DB Super)'s Scouter/PQ146.
- [x] Preserved the Goku Wig (Super Saiyan)→PQ63 historical conflict instead of treating it as a canonical acquisition route.
- [x] Recomputed parity: 95 canonical accessory records, 16 non-conflicting accessory↔PQ links, **0 missing reverse links**.
- [x] Added `docs/data/accessory-pq-bidirectional-parity-audit-2026-09-28.json`.
- [x] PQ-layer commit: `4df1fe267f9e3b658de60078df9fa3d9052d2b89`; audit commit: `c1b17c1e1b73fab5fdca4baf330e90958cc3908a`.
- [ ] **Exact next:** inspect the remaining canonical relationship consumers for similar bidirectional gaps, especially equipment↔PQ and Super Soul↔PQ, and repair only source-backed reverse links.

### 2026-09-28 continuation — 16-PQ typed-reward coverage audit
- [x] Audited the remaining 16 PQ IDs without explicit canonical skill endpoints against the canonical typed-reward relationship layer and accessory/equipment research evidence.
- [x] Confirmed most documented non-skill rewards are already represented canonically: PQ30, 47, 93, 102, 103, 107, 108, 118, 121, 144, 157, 169, and 170.
- [x] Preserved research-only/conflicting cases instead of inferring relationships: PQ35/Z-Sword, PQ48 Kamekameha/Kamehameha, and the previously documented PQ118/PQ121 skill conflicts.
- [x] Added `docs/data/unrepresented-pq-typed-reward-coverage-audit-2026-09-28.json`.
- [x] No unsupported canonical relationship was added; this pass found no safe new typed-reward promotion.
- [ ] **Exact next:** inspect PQ1, PQ35, and PQ48 evidence at item/skill identity level, then continue broader canonical acquisition coverage outside the already-reconciled 16-PQ frontier.

### 2026-09-28 continuation — 16-PQ typed-reward coverage audit
- [x] Audited the remaining 16 PQs without explicit canonical skill endpoints against the canonical typed-reward relationship layer and accessory/equipment research evidence.
- [x] Confirmed existing source-backed coverage for PQ30, PQ47, PQ93, PQ102, PQ103, PQ107, PQ108, PQ118, PQ121, PQ144, PQ157, PQ169, and PQ170.
- [x] Preserved PQ35/Z-Sword as research-only evidence because the accessory identity is not yet canonicalized for a PQ relationship.
- [x] Preserved PQ48 Kamekameha/Kamehameha as an unresolved skill-evidence conflict; no unsupported edge was promoted.
- [x] Preserved PQ1 as a bounded evidence target because no promotable typed relationship was established in this pass.
- [x] Added `docs/data/unrepresented-pq-typed-reward-coverage-audit-2026-09-28.json` documenting the results.
- [x] No speculative canonical relationships were added.
- [ ] **Exact next:** resume substantive expansion outside the already-covered 16-PQ typed-reward layer, prioritizing canonical skill/equipment/accessory acquisition gaps that have explicit item-level evidence and can be promoted safely.

### 2026-09-28 continuation — Post-corruption recovery checkpoint reconciliation
- [x] Re-read the live recovery checkpoint, canonical PQ reward recovery audit, post-recovery live-state reconciliation, and canonical identity audit against current main.
- [x] Confirmed the recovered canonical baseline is **493 skills / 493 index records**, **840 PQ relationship edges** (236 skill, 137 Super Soul, 125 equipment, 247 character, 88 DLC, 7 farming), **186 PQ records**, **112 equipment records**, **23 QQ Bang records**, and **17 observed QQ Bang vectors**.
- [x] Corrected stale recovery-checkpoint metadata that still pointed the skill layer at older 475-era state and clarified the active recovery frontier.
- [x] Preserved the canonical-source rule: docs/data/skills.json and the canonical forward relationship layer remain authoritative; verified/index/projection layers are evidence/derived views only.
- [x] Reconciled the next concrete recovery-forward target to the five post-recovery catalog-gap-promoted skills already screened in skill-preset-evidence-reconciliation-batch-01-2026-09-27.json: Full Power Energy Blast Volley, Super Back Jump, Ki Blast Cannon, Break Strike, and Consecutive Energy Blast.
- [x] Preserved evidence boundaries for acquisition conflicts, unresolved mechanics, and non-CaC/event-only identities; no speculative canonical relationship was introduced in this checkpoint pass.
- [ ] Runtime/CI remains intentionally non-blocking/unverified.
- [ ] **Exact next:** perform record-level canonical reconciliation for the five evidence-sufficient skills above, then continue through the remaining 13 catalog-gap-promoted identities before returning to broader QQ Bang/equipment and skill/PQ/Super Soul cross-domain enrichment.


### 2026-09-28 continuation — Restored skill reconciliation audit
- [x] Before changing canonical data, inspected the existing post-recovery evidence batches 04, 05, and 06. They already record direct reconciliation for Super Back Jump, Ki Blast Cannon, Consecutive Energy Blast, Super Galick Gun, Super Ki Explosion, Ultra Fighting Bomber, Full Power Energy Blast Volley, and Shockwave.
- [x] Verified that Full Power Energy Blast Volley’s conflicting historical batch-253 Super/100-Ki/Nappa-training data is preserved as historical provenance while current canonical evidence resolves it to Ultimate/Ki Blast/300 Ki/starting move.
- [x] Verified that shop/starting-move reconciliations do not create unsupported Skill→PQ acquisition edges.
- [x] Advanced the persistent frontier to the remaining restored skill identities requiring direct evidence reconciliation.
- [ ] Next: reconcile Super Dragon Fist, Holstein Shock, Break Strike, Backflip, Turn Retreat, Recoome Eraser Gun, Sledgehammer, Energy Wave Combo, and Full Power Energy Wave; preserve unresolved fields/conflicts and do not infer from preset/index evidence alone.


### 2026-09-28 continuation — Restored skill identity scope closed
- [x] Reconciled the apparent remaining nine-skill task against existing direct-evidence records instead of duplicating work. The nine are already reconciled in `skill-preset-evidence-reconciliation-batch-03-2026-09-27.json` and the canonical-evidence reconciliation audit.
- [x] Confirmed dedicated later batches for Shockwave and Super Galick Gun, and preserved their explicitly unresolved fields rather than inventing values.
- [x] Confirmed the current 18 restored preset identities have reached the evidence frontier; Galaxy Breaker (Festival) remains outside ordinary CaC canonical promotion.
- [x] Updated the TODO frontier to the next substantive recovery task: bidirectional Skill↔PQ endpoint auditing against the 840-edge canonical relationship baseline, followed by equipment/QQ Bang endpoint reconciliation.
- [ ] Next: audit Skill→PQ and PQ→Skill coverage for orphaned or asymmetric endpoints; only promote relationships backed by canonical acquisition evidence.


### 2026-09-28 continuation — Skill↔PQ recovery frontier advanced
- [x] Audited the live canonical `docs/data/pq-reward-relationships.json` rather than relying on the historical 840-edge checkpoint. Current live relationship counts are **852 total**: 248 Skill, 135 Super Soul, 127 equipment, 247 character, 88 DLC, 7 farming.
- [x] Confirmed the Skill↔PQ bidirectional reconciliation is current at 248 Skill→PQ edges across 170 PQs, with the same 16 PQ IDs lacking explicit canonical Skill endpoints. No unsupported relationships were promoted.
- [x] Updated current PQ status/audit/recovery metadata while preserving dated 840-edge historical provenance.
- [x] Repaired an accidental malformed recovery-checkpoint JSON edit by reconstructing it from the prior valid checkpoint and recording the new live 852-edge state.
- [ ] Next: expand evidence-backed PQ reward coverage beyond the 248 Skill relationships, prioritizing unresolved/underrepresented reward fields while preserving the canonical-source rule and null/conflict boundaries.
- [ ] Then reconcile equipment/QQ Bang and remaining reverse-index coverage, followed by cross-domain navigation validation.


### 2026-09-28 continuation — Equipment/QQ Bang endpoint reconciliation
- [x] Audited the equipment reverse projection against the live canonical PQ relationship layer and found stale projection metadata: 125 equipment edges versus 127 canonical forward edges.
- [x] Synchronized `docs/data/pq-equipment-crosslink-report.json` to the live 127-edge state without changing canonical reward ownership.
- [x] Confirmed the newly reconciled PQ12-14 equipment rewards are represented in the canonical forward layer and reverse equipment projection.
- [x] Added `docs/data/equipment-qqbang-cross-domain-reconciliation-2026-09-28.json` documenting the endpoint boundary and QQ Bang identity/stat rules.
- [x] Preserved QQ Bang uncertainty: observed vectors remain observations; unresolved clothing aliases are not inferred into canonical equipment links.
- [ ] Next: audit equipment/accessory reverse navigation across all 127 equipment edges and reconcile unresolved QQ Bang input identities, then continue evidence-backed reward expansion.


### 2026-09-28 continuation — Equipment reverse audit correction and endpoint repair
- [x] Performed a record-level comparison of the canonical `pq_rewards_equipment` relationships against the unified clothing/accessory reverse index instead of trusting metadata counts.
- [x] Found one genuine reverse-navigation gap: canonical PQ47 → **Broly's Clothes** existed in the forward relationship layer but was absent from the reverse index.
- [x] Added the missing derived reverse endpoint for Broly's Clothes → PQ47; no canonical acquisition edge was invented.
- [x] Found a separate stale-count problem: the canonical forward dataset contains **126 unique source-backed equipment edges**, not 127. Corrected total canonical relationship metadata from 852/127-equipment to **851 total / 126 equipment** (248 Skill, 135 Super Soul, 247 character, 88 DLC, 7 farming).
- [x] Synchronized the equipment projection, recovery checkpoint, and QQ Bang/equipment audit to the corrected 126-edge source-of-truth count.
- [ ] Next: re-run the complete equipment/accessory reverse comparison after the repair, then audit QQ Bang equipment-input identities and continue evidence-backed reward expansion.


### 2026-09-28 continuation — Equipment reverse parity and QQ Bang link-integrity audit
- [x] Re-ran the complete equipment/accessory forward↔reverse comparison after the PQ47 repair: **126 canonical forward edges / 126 reverse pairs / 0 missing / 0 reverse-only**.
- [x] Confirmed all explicit QQ Bang equipment links are valid: **23 QQ Bang records with concrete equipment links; 0 invalid endpoint IDs**.
- [x] Preserved the two QQ Bang system/mixing records without equipment links because they intentionally describe generic synthesis rather than concrete clothing identities.
- [x] Updated the equipment/QQ Bang reconciliation audit with the parity and endpoint-integrity results.
- [ ] Next: audit any remaining concrete QQ Bang input names that are intentionally unresolved, then validate cross-domain navigation consumers against the corrected **851-edge** canonical relationship total and resume evidence-backed PQ reward expansion.


### 2026-09-28 continuation — Correct stale PQ cross-domain metadata after equipment audit
- [x] Revalidated the live canonical relationship store against the repaired equipment reverse layer: 851 total edges = 248 Skill, 135 Super Soul, 126 equipment, 247 character, 88 DLC, 7 farming.
- [x] Corrected docs/data/pq-cross-domain-status.json and docs/data/pq-cross-domain-audit.json, which still contained superseded 852/127 current-state metadata.
- [x] Preserved the historical 840 baseline and superseded 852/127 refresh as dated provenance rather than deleting history.
- [x] Updated equipment reverse coverage in the cross-domain artifacts to 126 forward / 126 reverse / 0 missing / 0 reverse-only.
- [x] Validated both corrected JSON artifacts after mutation.
- [ ] Next: inspect actual cross-domain navigation/consumer files for hard-coded stale counts or endpoint assumptions, then resume evidence-backed PQ typed-reward expansion.


### 2026-09-28 continuation — Cross-domain consumer audit and stale-count cleanup
- [x] Revalidated canonical `pq-reward-relationships.json`: **851 edges** (248 Skill, 135 Super Soul, 126 equipment, 247 character, 88 DLC, 7 farming).
- [x] Reviewed the direct cross-domain validator/consumer scripts and confirmed they point to the canonical relationship store rather than maintaining a separate aggregate source of truth.
- [x] Recorded the consumer audit and corrected-count state in `docs/COVERAGE-AUDIT.md`.
- [x] Confirmed the repaired equipment reverse layer remains **126/126 with zero missing and zero reverse-only pairs**.
- [ ] Next: continue the concrete unresolved QQ Bang input-name audit, then resume evidence-backed expansion of underrepresented PQ typed rewards.


### 2026-09-28 continuation — QQ Bang input identity audit
- [x] Audited every QQ Bang `clothing_inputs` value that was not an exact `equipment_links` input match.
- [x] Confirmed generic system/mixing prose is not a concrete equipment identity and should not receive links.
- [x] Confirmed `qq-recipe-001` and `qq-research-002` already have component-level equipment links; no duplicate links were added.
- [x] Confirmed `qq-observed-013` contains one explicitly unspecified 5-star clothing input; no equipment identity was inferred from its output vector.
- [x] Recorded the boundary in `docs/data/equipment-qqbang-cross-domain-reconciliation-2026-09-28.json`: 0 new promotable links, 0 invalid existing links, 1 unresolved concrete input.
- [ ] **Next:** resume evidence-backed PQ typed-reward expansion/acquisition-gap research.


### 2026-09-28 continuation — PQ typed-reward drift audit closed
- [x] Re-read the live continuation/TODO files and canonical relationship store before proceeding.
- [x] Reconciled the remaining normalized-map `source_only` reward cases against canonical forward relationships. All identified source-only clothing/accessory entries already have canonical equipment relationships; the source-only skill entries Time Control, Mach Dash, and Warp Kamehameha are already represented at their documented PQ endpoints.
- [x] Confirmed no new canonical PQ typed-reward promotion is justified by the remaining normalized-map drift; partial-map omissions remain historical drift, not deletion evidence.
- [x] Updated `docs/data/pq-cross-domain-reconciliation.json` with the current 851-edge state and explicit unresolved boundaries.
- [x] Preserved PQ48 Kamekameha/Kamehameha as an evidence conflict and Dual Masenko as a separate canonical skill-record restoration candidate; no unsupported PQ118 edge was added.
- [ ] **Next:** advance the explicit canonical skill-record/acquisition-gap frontier, beginning with documented candidates such as Dual Masenko, then continue mechanics-field enrichment.


### 2026-09-28 continuation — Restored skill acquisition evidence refresh
- [x] Re-read the live continuation/TODO files and verified the Dual Masenko gap is already resolved; PQ118 remains intentionally unresolved.
- [x] Reconciled the next restored-skill evidence frontier using the existing batches plus current Xenoverse 2-specific references.
- [x] Confirmed **Energy Wave Combo** is a canonical Ki Blast Super with 100 Ki and a Skill Shop/default Future Warrior acquisition route. This resolves the earlier overly conservative acquisition-null boundary at the evidence level; it does **not** imply a PQ reward relationship.
- [x] Confirmed Full Power Energy Wave's Skill Shop/story-gated acquisition remains supported while Ultimate-Finish requirement stays null because explicit evidence is absent.
- [x] Recorded the refresh in `docs/data/skill-preset-evidence-reconciliation-batch-08-2026-09-28.json`.
- [ ] **Next:** safely propagate the Energy Wave Combo acquisition correction into canonical `docs/data/skills.json` and `docs/data/skills-index.json` without reconstructing unrelated large-file content, then continue the remaining acquisition/mechanics nulls.


### 2026-09-28 continuation — Canonical skill propagation safety checkpoint
- [x] Re-read the live continuation/TODO and verified the 18-record restored-skill frontier remains closed for identity reconciliation.
- [x] Rechecked Energy Wave Combo against the latest evidence: Super / Ki Blast / 100 Ki / CaC usable, with independent evidence supporting Skill Shop/default Future Warrior acquisition.
- [x] Corrected the canonical-evidence reconciliation artifact so this acquisition evidence is no longer described as an unresolved evidence gap.
- [x] Created `docs/data/canonical-skill-record-propagation-queue-2026-09-28.json` as a non-destructive exact patch queue for the canonical `skills.json` and synchronized index.
- [x] **Did not reconstruct or overwrite the large canonical files from truncated API output.** Canonical source-of-truth integrity takes precedence over forcing an unsafe mutation.
- [ ] **Next:** apply the queued Energy Wave Combo mutation through a safe complete-blob/repository-tree edit path; then validate canonical/index identity parity and continue remaining mechanics/acquisition enrichment.


### 2026-09-28 continuation — Energy Wave Combo canonical propagation completed
- [x] Retrieved the complete canonical `skills.json` blob safely through its blob SHA instead of reconstructing truncated API output.
- [x] Updated canonical `skill-energy-wave-combo`: Skill Shop/default Future Warrior acquisition, current verification date 2026-09-28, and refreshed evidence/mechanics note.
- [x] Updated `skills-index.json` to the same acquisition state.
- [x] Validated both layers: **493 records each**, matching Energy Wave Combo identity, acquisition, and verification date; Ultimate-Finish requirement remains null.
- [x] Closed `docs/data/canonical-skill-record-propagation-queue-2026-09-28.json` as applied and validated.
- [ ] **Next:** continue the remaining restored-skill acquisition/mechanics frontier with explicit current evidence; preserve unresolved fields and do not infer PQ ownership from Skill Shop/default-skill evidence.


### 2026-09-28 continuation — Safe canonical patch tooling
- [x] Inspected the existing canonical skill build/validation tooling and confirmed `skills.json` is rebuilt from complete local content; the connector cannot safely expose the full large blob for direct replacement.
- [x] Added `scripts/apply_canonical_skill_patch.py`, an identity-scoped patcher that requires exactly one canonical match, preserves unrelated records, supports dry-run before write, and keeps the index as a consumer rather than a source of truth.
- [x] Added the Energy Wave Combo patch to the propagation queue with the execution and validation sequence.
- [ ] **Next:** execute the patcher from a complete checkout, validate `skills.json`/index parity and acquisition metadata, then commit the canonical mutation and continue mechanics enrichment.


### 2026-09-28 continuation — Propagation queue reconciliation
- [x] Reconciled the handoff against the live canonical state: Energy Wave Combo propagation was already completed through the safe complete-blob path (493 canonical / 493 index records), despite the older queue section still saying it was pending.
- [x] Closed `docs/data/canonical-skill-record-propagation-queue-2026-09-28.json` as applied and validated while preserving the queue as historical provenance.
- [x] Rechecked the Dual Masenko frontier: canonical restoration is already complete; TP Medal Shop remains the supported acquisition route, while PQ118 remains intentionally unresolved because repository evidence conflicts.
- [x] Rechecked the restored-skill evidence batches; no unsupported PQ relationships were introduced from Skill Shop/default-skill evidence.
- [ ] **Next:** move beyond the restored identity/acquisition frontier into the remaining evidence-backed mechanics/acquisition gaps and bidirectional cross-domain reconciliation.


### 2026-09-28 continuation — Restored-skill mechanics frontier consolidation
- [x] Re-audited the next evidence-backed mechanics frontier after canonical identity/acquisition recovery.
- [x] Consolidated five existing canonical identities into `docs/data/restored-skill-mechanics-frontier-reconciliation-2026-09-28.json`: Assault Rain, Super Electric Strike, Ki Explosion, Heavenly Arrow, and Counter Burst.
- [x] Preserved source/version boundaries for damage, frame data, scaling, counter windows, and reward probabilities instead of promoting unsupported constants.
- [x] Preserved acquisition-vs-PQ semantics: Expert Mission/training/shop/PQ acquisition endpoints do not become PQ reward edges without explicit reward evidence.
- [ ] **Next:** compare these consolidated mechanics boundaries against the live canonical records and apply only field-level corrections supported by direct evidence; then continue the remaining mechanics frontier and PQ bidirectional reconciliation.


### 2026-09-28 continuation — Restored-skill mechanics frontier reconciliation
- [x] Compared the five-record mechanics frontier against the live canonical corpus.
- [x] Confirmed Assault Rain, Super Electric Strike, Ki Explosion, and Heavenly Arrow already carried the intended bounded mechanics; no unnecessary canonical rewrite was made.
- [x] Enriched **Counter Burst** in both canonical `skills.json` and synchronized `skills-index.json`: frontal Ki counter barrier, 6-hit counter projectile, knockback, and 20% source-reported damage are now explicitly documented; exact counter window, coverage, frame data, and patch-independent scaling remain unresolved.
- [x] Preserved the distinction between source-reported damage and patch-independent canonical constants.
- [x] Updated the mechanics frontier audit to record the reconciliation and retain the remaining unresolved fields.
- [ ] **Next:** continue the remaining skill mechanics/acquisition gaps, then resume bidirectional PQ typed-reward reconciliation without inferring PQ ownership from non-PQ acquisition endpoints.


### 2026-09-28 continuation — Restored-skill mechanics frontier batch 02
- [x] Added `docs/data/restored-skill-mechanics-frontier-reconciliation-2026-09-28-batch-02.json` covering Brutal Buster, Apocalyptic Burst, Gigantic Rage, Shooting Strike, and Time Skip/Jump Spike.
- [x] Reconciled documented mechanics against existing repository evidence without forcing canonical rewrites where the evidence does not establish stronger field-level facts.
- [x] Preserved unresolved exact frames, scaling, hit counts, hidden interactions, and reward probabilities rather than inventing constants.
- [x] Preserved the acquisition/PQ boundary: non-PQ acquisition evidence was not converted into PQ reward edges.
- [ ] **Next:** continue with the next unaudited mechanics/acquisition cohort and separately reconcile PQ forward/reverse typed-reward parity.


### 2026-09-28 continuation — PQ166-PQ170 typed skill-reward parity
- [x] Audited canonical forward skill-reward relationships against the current PQ record layer for PQ166-PQ170.
- [x] Confirmed exact parity for PQ166 → Pendulum Bullet, PQ167 → Seagull Combination/Burning Swan, and PQ168 → Justice Drive.
- [x] Confirmed PQ169 and PQ170 currently carry no skill rewards in the canonical PQ record layer; this is retained as a record-layer state, not generalized into a universal negative claim.
- [x] Added docs/data/pq-166-170-skill-reward-parity-audit-2026-09-28.json as a reproducible audit artifact.
- [x] No new relationship was inferred or promoted during this pass.
- [ ] **Next:** continue record-level forward/reverse PQ typed-reward parity across the next unreconciled range, prioritizing skill endpoints and preserving source conflicts.


### 2026-09-28 continuation — PQ171-PQ175 typed skill-reward parity
- [x] Audited PQ171-PQ175 at record level against the maintained forward reward map, reverse PQ skill index, PQ records/research, canonical relationship layer, and canonical skill cross-link report.
- [x] Confirmed the eight skill edges in this range are mutually represented: PQ171 (Crimson Edge, Divine Spear), PQ172 (Big Bang Knuckle, Wild Stinger), PQ173 (Divine Ray Bomb), PQ174 (Final Rampage), and PQ175 (God of Destruction's Plaything, God of Destruction's Poise).
- [x] Confirmed all eight names resolve to exact canonical skill identities; no unresolved canonical skill endpoint or forward/reverse mismatch was found.
- [x] Added docs/data/pq-171-175-skill-reward-parity-audit-2026-09-28.json as the reproducible audit artifact.
- [x] Did not infer additional PQ edges from character ownership, presets, or non-PQ acquisition evidence.
- [ ] **Next:** continue the next unreconciled PQ typed-reward range, then resume remaining mechanics/acquisition enrichment.


### 2026-09-28 continuation — PQ176-PQ180 typed skill-reward parity
- [x] Audited PQ176-PQ180 against the canonical forward PQ reward relationship layer, PQ record/research data, and the canonical PQ skill cross-link report.
- [x] Confirmed all **9 documented skill-reward edges** in this range are represented consistently: PQ176 (God of Destruction's Might), PQ177 (Full Power Destruction, Dragon Spark, Soaring Rush), PQ178 (Burst Blitz), PQ179 (Heat Wave, Supreme Fury), and PQ180 (Force Edge, Burning Blast).
- [x] Confirmed all nine skill endpoints resolve to canonical skill identities; no unresolved endpoint mismatch or unsupported new relationship was found.
- [x] Added `docs/data/pq-176-180-skill-reward-parity-audit-2026-09-28.json` as the reproducible audit artifact.
- [x] Preserved the boundary between PQ reward membership and CaC eligibility: Force Edge/Burning Blast reward edges do not by themselves establish `usable_by_cac`.
- [ ] **Next:** continue the next unreconciled cross-domain range and then return to remaining evidence-backed mechanics/acquisition gaps.


### 2026-09-28 continuation — PQ181-PQ185 typed skill-reward parity
- [x] Audited PQ181-PQ185 at record level against the canonical forward reward relationship layer and maintained PQ/research evidence.
- [x] Confirmed **7/7 documented skill-reward edges** are represented: PQ181 (Super Kamehameha (SS4 DAIMA), Final Flash (SS3 DAIMA)), PQ182 (Dark Inscription), PQ183 (Emperor's Cannon), PQ184 (Chaotic Time Impact), and PQ185 (Dragon Spiral, Indomitable).
- [x] Confirmed all seven endpoints are represented without an unresolved canonical skill identity gap.
- [x] Preserved unresolved exact reward-slot percentages; PQ184's documented Ultimate-Finish bonus-slot context remains evidence-bounded.
- [x] Preserved the known Dragon Spiral source conflict and did not manufacture a PQ186 relationship from the conflicting guide.
- [x] Added `docs/data/pq-181-185-skill-reward-parity-audit-2026-09-28.json` as the reproducible audit artifact.
- [ ] **Next:** audit PQ186 separately, then continue remaining typed-reward gaps and evidence-backed mechanics/acquisition enrichment.


### 2026-09-28 continuation — PQ186 typed skill-reward parity
- [x] Audited PQ186 separately after the PQ181-PQ185 tranche.
- [x] Confirmed the current reward map documents exactly one skill endpoint: **Venus Fist**.
- [x] Confirmed the canonical forward relationship and maintained reverse skill map agree on **PQ186 ↔ Venus Fist**; no endpoint gap or duplicate relationship was found.
- [x] Added `docs/data/pq-186-skill-reward-parity-audit-2026-09-28.json` as the reproducible record-level audit artifact.
- [x] Preserved unresolved exact reward-slot/drop probability and Ultimate-Finish-condition fields rather than inferring them.
- [ ] **Next:** continue the remaining global PQ skill-endpoint gap outside PQ163-PQ186, then resume evidence-backed mechanics/acquisition enrichment.


### 2026-09-28 continuation — Restored-skill mechanics enrichment
- [x] Enriched canonical **Gravity Impact** with current-evidence mechanics: Ki-Blast cancellation behavior, long knockback, and follow-up window; exact frames and complete interaction scope remain unresolved.
- [x] Enriched canonical **Hawk Charge** with the elbow-to-palm sequence, bounded source-reported damage, rush-to-palm input cancel, and separate DBS Super Hero presentation; exact timing remains unresolved.
- [x] Refreshed **Remote Serious Bomb** two-stage seal/bomb mechanics and preserved the second-stage resource-cost conflict instead of inventing a version-independent value.
- [x] Synchronized `skills-index.json`; both canonical layers remain **493/493** and mechanics/verification fields were checked for parity.
- [x] Added `docs/data/skill-mechanics-enrichment-audit-2026-09-28.json` documenting promoted evidence and unresolved boundaries.
- [ ] **Next:** continue through the remaining mechanics frontier, prioritizing records where current evidence can materially replace deferred mechanics notes without manufacturing frame/scaling/probability data.


### 2026-09-28 continuation — Restored-skill mechanics frontier batch 03
- [x] Rechecked the live canonical retrieval boundary; the connector still exposes the large `skills.json` path with empty encoded payload, so no unsafe reconstruction was attempted.
- [x] Added `docs/data/restored-skill-mechanics-frontier-reconciliation-2026-09-28-batch-03.json` covering Shooting Strike, Apocalyptic Burst, Time Skip/Jump Spike, and Gigantic Rage.
- [x] Preserved explicit mechanics boundaries, source-reported values, acquisition endpoints, and unresolved frame/scaling/reward-probability fields rather than inventing precision.
- [x] Appended the four records to the consolidated mechanics frontier; canonical identity count remains 493/493 and no duplicate skill records or unsupported PQ edges were created.
- [ ] **Next:** continue the mechanics census for skills lacking dedicated current-evidence audits, then separately reconcile explicit PQ typed-reward edges.

### 2026-09-28 continuation — Restored-skill mechanics frontier batch 04
- [x] Revalidated the post-corruption recovery baseline before advancing: canonical skill corpus remains 493 identities with matching index count; the recovery layer remains intact and no reconstruction from the inaccessible large skills blob was attempted.
- [x] Added `docs/data/restored-skill-mechanics-frontier-reconciliation-2026-09-28-batch-04.json` covering Energy Release, Super Destructo-Disc, Android Rush, Burning Attack, Chaos Shot, Surging Spirit, Reverse Shot, and Grand Smasher.
- [x] Consolidated Batch 04 into `docs/data/restored-skill-mechanics-frontier-reconciliation-2026-09-28.json` as evidence-only mechanics boundaries; no duplicate canonical identities, speculative frame/scaling/probability values, or unsupported PQ reward edges were created.
- [x] Preserved the distinction between built-in Surging Spirit and separately acquired charge skills, and preserved bounded source-reported values rather than treating them as patch-independent constants.
- [ ] Runtime/CI/build remains intentionally non-blocking/unverified.
- [ ] **Exact next:** continue the mechanics census with the next unaudited canonical cohort, promote only field-level evidence that is safe to place in canonical `skills.json`, and separately continue explicit PQ typed-reward parity.


### 2026-09-28 continuation — Global PQ skill-endpoint gap census
- [x] Audited the 16 PQ IDs previously represented by the reverse skill index as having no canonical skill endpoint: PQ1, 30, 35, 47, 48, 93, 102, 103, 107, 108, 118, 121, 144, 157, 169, and 170.
- [x] Resolved **PQ48**: the maintained PQ record and all-PQ guide explicitly list the reward as **Kamekameha**; this maps to the existing canonical **Kamehameha** identity. Promoted the explicit `pq_rewards_skill` relationship while preserving the historical spelling variant.
- [x] Refreshed `docs/data/pq-skill-crosslink-report.json` and `docs/data/skill-pq-reverse-index-2026-09-26.json`: canonical Skill→PQ edges are now **249**, with PQ48 represented bidirectionally.
- [x] Added `docs/data/pq-global-skill-endpoint-gap-audit-2026-09-28.json` documenting the complete 16-ID census, including unresolved PQ118 evidence and the remaining no-skill states.
- [x] Preserved the rule that empty record-layer `skill_rewards` fields are not universal negative claims, and that non-PQ acquisition evidence never creates PQ reward edges.
- [ ] **Next:** continue the remaining 15 PQ endpoint gaps where external evidence may justify a safe promotion, beginning with PQ118's explicit conflict resolution; then return to the next unaudited skill mechanics cohort.


### 2026-09-28 continuation — Restored-skill mechanics frontier batch 05
- [x] Continued the mechanics frontier after the PQ endpoint census with a bounded reconciliation of **Tyrant Lancer, Ki Explosion, X10 Kamehameha, and Kamekameha**.
- [x] Preserved current evidence for class/subcategory, Ki cost, character source, CaC usability, and documented move behavior where supported.
- [x] Kept damage-test values explicitly test-contextual; no universal scaling, exact frame data, hidden conditions, or probabilities were inferred.
- [x] Preserved Kamekameha's historical spelling identity and its existing PQ48 mapping to canonical Kamehameha; no duplicate identity or unsupported PQ relationship was added.
- [x] Added `docs/data/restored-skill-mechanics-frontier-reconciliation-2026-09-28-batch-05.json`.
- [ ] Runtime/CI/build remains intentionally non-blocking/unverified.
- [ ] **Exact next:** continue the mechanics/acquisition frontier with the next genuinely unaudited canonical records, while maintaining the 493/493 identity boundary and explicit provenance limits.


### 2026-09-28 continuation — PQ crosslink coverage synchronization
- [x] Reconciled the stale `docs/COVERAGE-AUDIT.md` PQ→skill summary against the latest persisted crosslink state after PQ48 promotion.
- [x] Updated the summary from **248 edges / 170 PQ IDs / 16 endpoint gaps** to **249 edges / 171 PQ IDs / 15 endpoint gaps**.
- [x] Preserved the evidence boundary: an absent canonical endpoint is not treated as proof that a PQ has no skill reward.
- [x] No canonical skill identities or unsupported relationships were introduced by this synchronization.
- [ ] Runtime/CI/build remains intentionally non-blocking/unverified.
- [ ] **Exact next:** continue the remaining unaudited mechanics/acquisition frontier and keep cross-domain coverage summaries synchronized with the canonical relationship layer.


### 2026-09-28 continuation — Current-evidence skill frontier batch 528
- [x] Advanced to the next genuinely stale skill cohort after Batch 527 rather than repeating recent audits.
- [x] Refreshed **Miracle Kneel, Kai Kai, Ill Rain, and Super God Fist**, whose dedicated evidence was still anchored to early September research and lacked a post-recovery current-evidence refresh artifact.
- [x] Preserved unresolved resource-cost evidence for Kai Kai instead of inventing a value.
- [x] Preserved explicit class, cost, acquisition, and bounded mechanics evidence where supported for the other three records.
- [x] Added `docs/data/skill-research-batches/skill-batch-528.json` and registered it in `docs/data/pq-cross-domain-index.json`.
- [x] Maintained the 493 canonical skill identity boundary and added no unsupported PQ relationships.
- [ ] Runtime/CI/build remains intentionally non-blocking/unverified.
- [ ] **Exact next:** continue the post-recovery current-evidence frontier with the next genuinely stale canonical records, then reconcile any safe field-level promotions into the canonical layer.


### 2026-09-28 continuation — Current-evidence skill frontier batch 529
- [x] Continued past Batch 528 into the next genuinely stale Other Evasive cohort.
- [x] Refreshed **Armored Boost, Backflip, Candy Beam (Evasive), and Science Vanish**.
- [x] Preserved the Candy Beam Evasive/Super distinction and Science Vanish's cast-exclusive status rather than inferring player acquisition.
- [x] Preserved bounded mechanics only; no unsupported frames, hidden conditions, scaling, or probabilities were introduced.
- [x] Added `docs/data/skill-research-batches/skill-batch-529.json` and registered it in `docs/data/pq-cross-domain-index.json`.
- [x] Maintained the 493 canonical skill identity boundary and added no unsupported PQ relationships.
- [ ] Runtime/CI/build remains intentionally non-blocking/unverified.
- [ ] **Exact next:** continue the next genuinely stale canonical skill cohort after Batch 529 and reconcile any directly supported field-level improvements.


### 2026-09-28 continuation — Current-evidence skill frontier batch 530
- [x] Continued the post-recovery frontier with five stale PQ61-PQ70 cohort records: **Recoome Kick, Fighting Pose H, Teleporting Vanishing Ball, Angry Shout, and Headshot**.
- [x] Preserved documented class, resource cost, acquisition, character source, and bounded mechanics evidence without inventing exact frames, scaling, hidden conditions, or probabilities.
- [x] Added `docs/data/skill-research-batches/skill-batch-530.json` and registered it in `docs/data/pq-cross-domain-index.json`.
- [x] Maintained the 493 canonical skill identity boundary and added no unsupported PQ relationships.
- [ ] Runtime/CI/build remains intentionally non-blocking/unverified.
- [ ] **Exact next:** continue the next genuinely stale canonical skill cohort after Batch 530 and reconcile any directly supported field-level improvements.


### 2026-09-28 continuation — Current-evidence skill frontier batch 531
- [x] Continued with five stale PQ71-PQ75 cohort records: **Last Emperor, Burst Kamehameha, Psychic Move, Final Pose, and Counter Burst**.
- [x] Preserved documented class, resource cost where supported, acquisition, character source, and bounded mechanics evidence; unresolved costs remain unresolved.
- [x] Added `docs/data/skill-research-batches/skill-batch-531.json` and registered it in `docs/data/pq-cross-domain-index.json`.
- [x] Maintained the 493 canonical skill identity boundary and added no unsupported PQ relationships.
- [ ] Runtime/CI/build remains intentionally non-blocking/unverified.
- [ ] **Exact next:** continue the next genuinely stale canonical skill cohort after Batch 531 and reconcile safe field-level improvements.


### 2026-09-28 continuation — Current-evidence skill frontier batch 532
- [x] Continued with four stale PQ81-PQ85 cohort records: **Afterimage Strike, Dragon Burn, Saiyan Spirit, and Zigzag Express**.
- [x] Preserved supported class, costs, restrictions, acquisition, character source, and bounded mechanics; unresolved technical fields remain unresolved.
- [x] Added `docs/data/skill-research-batches/skill-batch-532.json` and registered it in `docs/data/pq-cross-domain-index.json`.
- [x] Maintained the 493 canonical skill identity boundary and added no unsupported PQ relationships.
- [ ] Runtime/CI/build remains intentionally non-blocking/unverified.
- [ ] **Exact next:** continue the next genuinely stale canonical skill cohort after Batch 532 and reconcile safe field-level improvements.


### 2026-09-28 continuation — Current-evidence skill frontier batch 533
- [x] Continued with four stale PQ86-PQ90 cohort records: **Neo Wolf Fang Fist, Buu Buu Ball, Victory Rush, and III Bomber**.
- [x] Preserved supported class, costs, restrictions, acquisition, character source, and bounded mechanics; the III Bomber/Ill Bomber naming discrepancy remains provenance rather than a duplicate identity.
- [x] Added `docs/data/skill-research-batches/skill-batch-533.json` and registered it in `docs/data/pq-cross-domain-index.json`.
- [x] Maintained the 493 canonical skill identity boundary and added no unsupported PQ relationships.
- [ ] Runtime/CI/build remains intentionally non-blocking/unverified.
- [ ] **Exact next:** continue the next genuinely stale canonical skill cohort after Batch 533 and reconcile safe field-level improvements.


### 2026-09-28 continuation — Current-evidence skill frontier batch 534
- [x] Continued with four stale PQ91-PQ95 cohort records: **Final Kamehameha, Maiden Burst, Bluff Kamehameha, and Drain Field**.
- [x] Preserved supported class, costs, acquisition, character source, and bounded mechanics; unresolved reward-slot and technical fields remain unresolved.
- [x] Added `docs/data/skill-research-batches/skill-batch-534.json` and registered it in `docs/data/pq-cross-domain-index.json`.
- [x] Maintained the 493 canonical skill identity boundary and added no unsupported PQ relationships.
- [ ] Runtime/CI/build remains intentionally non-blocking/unverified.
- [ ] **Exact next:** continue the next genuinely stale canonical skill cohort after Batch 534 and reconcile safe field-level improvements.


### 2026-09-28 continuation — Current-evidence skill frontier batch 535
- [x] Audited the remaining PQ86-PQ100 cohort against later dedicated research before refreshing anything redundantly.
- [x] Refreshed the two genuinely stale records: **Emperor's Edge** and **X100 Big Bang Kamehameha**.
- [x] Confirmed **Absolute Zero, Charged Ki Wave, Phantom Fist, and Dimension Ray** already have later dedicated current-evidence coverage and were excluded from duplicate work.
- [x] Added `docs/data/skill-research-batches/skill-batch-535.json` and registered it in `docs/data/pq-cross-domain-index.json`.
- [x] Maintained the 493 canonical skill identity boundary and added no unsupported PQ relationships.
- [ ] Runtime/CI/build remains intentionally non-blocking/unverified.
- [ ] **Exact next:** move beyond the PQ86-PQ100 seed cohort and identify the next genuinely stale canonical skill frontier without repeating later audits.


### 2026-09-28 continuation — Current-evidence skill frontier batch 536
- [x] Moved beyond the PQ86-PQ100 seed cohort and selected four genuinely stale canonical records: **Burning Spin, Burning Strike, Light Grenade, and Power Blitz**.
- [x] Cross-checked later repository audits first and excluded records already covered by newer dedicated evidence work.
- [x] Refreshed supported class, costs, acquisition, character-source, and bounded mechanics evidence; exact patch-independent damage/frame values remain unpromoted.
- [x] Preserved **Light Grenade Super vs. Ultimate** as separate identities and updated **Burning Spin** to the currently documented 400-Ki Ultimate cost.
- [x] Added `docs/data/skill-research-batches/skill-batch-536.json` and registered it in `docs/data/pq-cross-domain-index.json`.
- [x] Maintained the 493 canonical skill identity boundary and added no unsupported PQ relationships.
- [ ] Runtime/CI/build remains intentionally non-blocking/unverified.
- [ ] **Exact next:** continue the next genuinely stale canonical skill frontier after Batch 536, checking later dedicated audits before any refresh.


### 2026-09-28 continuation — Current-evidence skill frontier batch 536
- [x] Moved beyond the PQ86-PQ100 seed cohort and screened later batches/audits to avoid repeating already refreshed records.
- [x] Refreshed **Burning Spin, Burning Strike, Light Grenade, and Power Blitz** as the next genuinely stale canonical records.
- [x] Excluded records already covered by later dedicated evidence work, including Burning Swan, All Clear, Angry Hit, Evil Explosion, Darkness Eye Beam, Darkness Twin Star, Endless Shoot, and Gravity Impact.
- [x] Added `docs/data/skill-research-batches/skill-batch-536.json` and registered it in `docs/data/pq-cross-domain-index.json`.
- [x] Maintained the 493 canonical skill identity boundary and added no unsupported PQ relationships or speculative technical values.
- [ ] Runtime/CI/build remains intentionally non-blocking/unverified.
- [ ] **Exact next:** continue the post-PQ100 stale canonical frontier with the same duplicate-audit and evidence-boundary rules.


### 2026-09-28 continuation — Post-recovery canonical skill promotion batch 537
- [x] Revalidated the authoritative post-corruption skill blob and index before promotion: 493/493; the pre-existing `Super Ghost Kamikaze Attack` duplicate-name collision was preserved and no new duplicate was introduced.
- [x] Promoted four directly evidenced indexed-only Future Warrior skills: Divine Retribution, Final Shine Attack, Savage Strike, Sword of Hope.
- [x] Synchronized canonical/index layers to 497/497.
- [x] Added recovery-promotion audit + skill research Batch 537 and registered both in the cross-domain index.
- [ ] Runtime/CI/build remains intentionally non-blocking/unverified.
- [ ] Exact next: recompute the indexed-only skill frontier against the 497-record canonical corpus; continue evidence-backed restoration/promotion of genuinely canonical Future Warrior skills, then return to remaining mechanics/acquisition enrichment and PQ crosslink synchronization. Never treat indexed-only catalogs as authoritative and never infer cast-only/variant records into the canonical corpus without direct evidence.


### 2026-09-28 continuation — Canonical PQ/skill projection recount correction
- [x] Directly recounted `docs/data/pq-reward-relationships.json` instead of trusting stale status metadata: **852 total edges** = 249 Skill, 135 Super Soul, 126 equipment, 247 character, 88 DLC, 7 farming.
- [x] Corrected active PQ status/audit projections from stale 851/248-skill metadata to the live 852/249-skill state; historical 840 and superseded projections remain preserved as provenance.
- [x] Refreshed PQ→skill reconciliation/consumer projections to the recovered **497-record canonical skill corpus** and **249 forward Skill→PQ edges**.
- [x] No new PQ reward relationship was inferred during this correction; the discrepancy was projection metadata drift.
- [ ] Runtime/CI/build remains intentionally non-blocking/unverified.
- [ ] **Exact next:** recompute the indexed-only skill frontier against the 497-record canonical corpus and promote the next directly evidenced Future Warrior identities, preserving cast-only/variant boundaries; then continue QQ Bang/equipment and remaining skill/PQ cross-domain enrichment.


### 2026-09-28 continuation — Canonical evidence synchronization batch 538
- [x] Confirmed the recovered canonical/index boundary remains **497 / 497** with no indexed-only identities remaining.
- [x] Synchronized four previously completed but pending canonical evidence audits into `docs/data/skills.json`: **Headshot, Arm Crash, God Breaker, Phantom Fist**.
- [x] Synchronized `docs/data/skills-index.json` and registered `docs/data/skill-research-batches/skill-batch-538.json`.
- [x] Preserved evidence boundaries: source-reported damage/Stamina values remain bounded evidence; exact frame data, hidden interactions, scaling formulas, and reward probabilities remain unresolved where not directly established.
- [x] No new skill identity or PQ reward relationship was inferred.
- [ ] Runtime/CI/build remains intentionally non-blocking/unverified.
- [ ] **Exact next:** continue the remaining completed-but-pending canonical skill evidence audits (especially the Batch 472/473 prepared records) before starting new speculative enrichment; then return to QQ Bang/equipment and remaining PQ cross-domain gaps.


### 2026-09-28 continuation — Canonical evidence synchronization batch 540
- [x] Synchronized three remaining prepared Time Skip audits into authoritative `docs/data/skills.json`: **Time Skip/Jump Spike, Time Skip/Back Breaker, Time Skip/Flash Skewer**.
- [x] Synchronized the skill index, marked the three source audits as synchronized, and registered `skill-batch-540.json`.
- [x] Maintained the recovered **497 canonical / 497 index** identity boundary; no unsupported skill identity or PQ relationship was added.
- [x] Preserved evidence limits: source-reported damage is bounded evidence; exact frames, scaling, hidden interactions, and reward probabilities remain unresolved where not directly established.
- [ ] Runtime/CI/build remains intentionally non-blocking/unverified.
- [ ] **Exact next:** reconcile the remaining prepared-audit status against the actual source files (search indexing may lag), then move to unresolved mechanics/acquisition enrichment and the remaining PQ/skill/equipment cross-domain gaps.


### 2026-09-28 continuation — Post-corruption live baseline reconciliation and handoff repair
- [x] Re-read the live continuation/TODO state and inspected recovery history before further changes.
- [x] Confirmed the canonical recovery path is preserved: the surviving skill baseline was restored, PQ 1-186 records were restored/reconciled, and recovery validators/audits were added instead of reconstructing canonical data from derived indexes.
- [x] Confirmed the current canonical skill corpus is **497 records** after four directly evidenced Future Warrior skill identities were promoted; `docs/data/skills.json` remains authoritative and `skills-index.json` is a synchronized consumer.
- [x] Confirmed the current PQ cross-domain relationship store is **852 edges**: 249 Skill, 135 Super Soul, 126 equipment, 247 character, 88 DLC, and 7 farming. The historical 840-edge state remains provenance only.
- [x] Confirmed the current Parallel Quest range is **PQ1-PQ186**; numbering gaps/conflicts remain explicitly represented rather than invented away.
- [x] Added `docs/data/current-live-recovery-baseline-2026-09-28.json` with the current post-recovery counts, source-of-truth rules, historical baselines, and validation boundaries.
- [x] Updated the canonical skill propagation queue so its old 493-record figures are explicitly historical/completed rather than current state.
- [x] Updated this continuation handoff and the exhaustive TODO with the same current baseline.
- [ ] Runtime/CI/build remains intentionally non-blocking/unverified.
- [ ] **Exact next:** continue substantive evidence-backed enrichment from the repaired 497-skill / 852-edge / PQ1-186 baseline, prioritizing remaining canonical skill mechanics/acquisition gaps and then PQ↔skill/Super Soul/equipment navigation gaps. Do not recreate recovered records or use verified/index/projection layers as canonical source of truth.


### 2026-09-28 continuation — PQ51 equipment identity promotion
- [x] Freshly checked the remaining accessory/PQ bridge gaps against the canonical accessory layer rather than treating the old bridge as authoritative.
- [x] Promoted the explicit **Great Saiyaman Helmet ↔ PQ51** identity into the canonical PQ reward relationship store as a `source_backed` equipment relationship.
- [x] Linked bridge record `pqacc-020` to canonical accessory `acc-005` and reduced the unresolved accessory/PQ bridge set by one.
- [x] Preserved the evidence boundary: the relationship records the named PQ association only; it does not claim a guaranteed drop condition or probability.
- [x] Current canonical PQ relationship store is now **853 edges**: 249 Skill, 135 Super Soul, 127 Equipment, 247 Character, 88 DLC, 7 Farming.
- [x] Updated `docs/data/current-live-recovery-baseline-2026-09-28.json` to the new 853-edge live baseline.
- [ ] Runtime/CI/build remains intentionally non-blocking/unverified.
- [ ] **Exact next:** continue the remaining explicit accessory/PQ identity gaps, then return to larger mechanics/acquisition and bidirectional cross-domain enrichment; do not promote unresolved component identities or historical conflicts without new evidence.


### 2026-09-28 continuation — Canonical accessory/PQ promotion batch
- [x] Audited the remaining accessory endpoint candidate queue against the canonical accessory layer and forward PQ relationship store.
- [x] Promoted five already-canonical accessory identities: Jaco's State-of-the-Art Radio→PQ72, Tagoma's Scouter→PQ73, Yamcha Baseball Hat→PQ97, Android 14's Hat→PQ104, and Bardock (DB Super)'s Scouter→PQ146.
- [x] Used the existing all-186 PQ guide evidence and did not infer any drop rate, probability, or reward-slot condition.
- [x] Marked those five candidates as promoted and synchronized the cross-domain status/audit projections.
- [x] Current canonical PQ relationship store is now 858 edges: 249 Skill, 135 Super Soul, 132 Equipment, 247 Character, 88 DLC, 7 Farming.
- [x] Updated the live recovery baseline to 858 edges.
- [ ] Runtime/CI/build remains intentionally non-blocking/unverified.
- [ ] Exact next: continue remaining accessory candidates only where canonical identity is established; keep Gine, Kale, Caulifla, Android 17 Ranger, and Android 15 Sunglasses unresolved until direct identity evidence exists. Then resume mechanics/acquisition and bidirectional enrichment.


### 2026-09-28 continuation — Accessory/PQ reconciliation batch
- [x] Promoted **Android 13's Hat→PQ105** and **Android 17 (DB Super) Wig→PQ152** as source-backed canonical equipment relationships using explicit reward-listing evidence and existing canonical identities.
- [x] Preserved the separate **Android 17 (DB Super)'s Ranger Accessory** component identity; no merge was made.
- [x] Reconciled stale candidate-queue statuses where canonical equipment relationships already existed, avoiding duplicate relationship creation.
- [x] Current canonical PQ relationship store is now **860 edges**: 249 Skill, 135 Super Soul, 134 Equipment, 247 Character, 88 DLC, 7 Farming.
- [x] Updated the live recovery baseline and PQ status/audit projections.
- [ ] Runtime/CI/build remains intentionally non-blocking/unverified.
- [ ] **Exact next:** continue only with remaining candidates having direct canonical identity evidence; preserve Great Saiyaman Bandana variants, Android 15 Sunglasses, Gine/Kale/Caulifla accessories, and Android 17 Ranger Accessory as unresolved until inventory-level evidence supports reconciliation. Then return to broader mechanics/acquisition enrichment.


### 2026-09-28 continuation — SSGSS Goku Wig/PQ76 reconciliation
- [x] Detected a stale candidate status: the canonical bridge already matched SSGSS Goku Wig to canonical accessory acc-066, but the candidate queue still said not promoted.
- [x] Promoted SSGSS Goku Wig→PQ76 into the authoritative PQ reward relationship store using the explicit canonical identity and PQ association.
- [x] Kept reward/drop-condition certainty separate from identity-level relationship evidence.
- [x] Current canonical PQ relationship store is now 861 edges: 249 Skill, 135 Super Soul, 135 Equipment, 247 Character, 88 DLC, 7 Farming.
- [x] Synchronized the enrichment queue, cross-domain status/audit, live recovery baseline, TODO, and continuation handoff.
- [ ] Runtime/CI/build remains intentionally non-blocking/unverified.
- [ ] Exact next: do not force-match Great Saiyaman Bandana 1/2, Android 15 Sunglasses, or unresolved component identities without inventory-level evidence; after remaining safe identity checks, return to broader mechanics/acquisition enrichment.


### 2026-09-28 continuation — Gamma 2 Helmet/PQ155 reconciliation
- [x] Found one remaining candidate with a canonical identity and explicit PQ route that was missing from the authoritative relationship store: **Gamma 2's Helmet→PQ155** (`acc-056` / `pqacc-044`).
- [x] Promoted the relationship as `source_backed`; exact reward/drop condition remains separate.
- [x] Synchronized the enrichment queue, PQ status/audit, and live recovery baseline.
- [x] Current canonical PQ relationship store is now **862 edges**: 249 Skill, 135 Super Soul, 136 Equipment, 247 Character, 88 DLC, 7 Farming.
- [ ] Runtime/CI/build remains intentionally non-blocking/unverified.
- [ ] Exact next: inspect for any remaining canonical-source discrepancies before broader mechanics/acquisition enrichment; preserve unresolved component identities and historical route conflicts.


### 2026-09-28 continuation — Accessory canonical backlog synchronization
- [x] Reconciled stale statuses in `accessory-pq-canonical-remaining.json` after the authoritative PQ promotions: Great Saiyaman Helmet, Android 13's Hat, Android 17 (DB Super) Wig, King Vegeta (DB Super) Wig, Gamma 2's Helmet, and Gamma 1's Helmet are now explicitly marked `resolved_to_canonical` with their canonical IDs.
- [x] Preserved genuinely unresolved records: Great Saiyaman Bandana 1/2, Tapion's Sword historical route conflict, Yamcha's Sword PQ conflict, Goku wig PQ conflicts, Android 15's Sunglasses, and component-unresolved Gine/Kale/Caulifla/Android 17 Ranger entries.
- [x] No new PQ relationship was inferred in this metadata-only synchronization; the authoritative relationship count remains **862 edges / 136 equipment**.
- [ ] Runtime/CI/build remains intentionally non-blocking/unverified.
- [ ] Exact next: continue broader mechanics/acquisition enrichment rather than manufacturing accessory identities or resolving historical route conflicts without independent evidence.


### 2026-09-28 continuation — Live PQ status/audit recount synchronization
- [x] Directly recounted authoritative `docs/data/pq-reward-relationships.json`: **862 unique canonical edges** — 249 Skill, 135 Super Soul, 136 Equipment, 247 Character, 88 DLC, 7 Farming.
- [x] Corrected `docs/data/pq-cross-domain-status.json` current fields to the live 862-edge state; historical projections remain preserved as history.
- [x] Corrected `docs/data/pq-cross-domain-audit.json` current counts and added a latest-live recount record sourced only from the canonical forward store.
- [x] Duplicate key validation returned **0 duplicates** across the canonical relationship tuples.
- [ ] Runtime/CI/build remains intentionally non-blocking/unverified.
- [ ] Exact next: proceed to substantive mechanics/acquisition enrichment and bidirectional cross-domain gaps, using canonical records as source of truth and retaining unresolved evidence boundaries.


### 2026-09-28 continuation — Canonical skill acquisition enrichment batch 541
- [x] Recounted the authoritative `docs/data/skills.json` directly through the GitHub contents API: **497 canonical skill records**.
- [x] Identified 20 canonical records with missing acquisition metadata fields; enriched five with direct current/repository evidence: **Backflip, Break Strike, Consecutive Energy Blast, Energy Wave Combo, Super Back Jump**.
- [x] Added the missing `acquisition_type`, `source_quest_or_shop`, and/or `dlc_requirement` fields without converting character/preset DLC appearances into CaC acquisition gates.
- [x] Synchronized the five records into `docs/data/skills-index.json` and registered `docs/data/skill-research-batches/skill-batch-541.json` in the cross-domain registry.
- [x] Updated the canonical skill acquisition-gap census: **15 records remain** with at least one target acquisition field missing.
- [x] Preserved evidence boundaries: no unsupported drop probabilities, Ultimate Finish requirements, prerequisites, or variant identities were inferred.
- [ ] Runtime/CI/build remains intentionally non-blocking/unverified.
- [ ] **Exact next:** enrich the remaining 15 canonical acquisition gaps in evidence-backed batches, then deepen mechanics/restriction/version fields and PQ↔skill navigation where gaps remain.


### 2026-09-28 continuation — Canonical skill acquisition completion batch 542
- [x] Rechecked the 15 remaining acquisition-field gaps against the authoritative `docs/data/skills.json` and existing repository evidence.
- [x] Completed acquisition metadata for **Dual Masenko, Final Shine Attack, Full Power Energy Wave, Galaxy Breaker (Festival), Holstein Shock, Ki Blast Cannon, Power Pole Combo, Recoome Eraser Gun, Shockwave, Sledgehammer, Super Dragon Fist, Super Galick Gun, Super Ki Explosion, Turn Retreat, and Ultra Fighting Bomber**.
- [x] Restored the missing canonical `skill-final-shine-attack` ID while synchronizing its already evidenced identity; no new skill identity was invented.
- [x] Added/registerd `docs/data/skill-research-batches/skill-batch-542.json` and closed the canonical acquisition-gap census: **0 records remain missing any of the three target acquisition fields** (`acquisition_type`, `source_quest_or_shop`, `dlc_requirement`).
- [x] Preserved event/cast/CaC boundaries and did not infer unsupported reward probabilities, Ultimate Finish gates, prerequisites, or hidden timing.
- [ ] Runtime/CI/build remains intentionally non-blocking/unverified.
- [ ] **Exact next:** audit the now-complete acquisition layer for semantic inconsistencies, then prioritize mechanics/restrictions/version history and bidirectional PQ↔skill navigation gaps.


### 2026-09-28 continuation — Post-recovery skill audit metadata reconciliation batch 543
- [x] Audited recent skill mechanics and preset-navigation artifacts for stale pre-recovery canonical counts.
- [x] Synchronized six affected audit artifacts from the pre-recovery 493-record snapshot to the current **497-record** canonical/index corpus, without changing skill identities or PQ relationships.
- [x] Preserved historical before/after counts where they document the recovery itself; only current-state counters were corrected.
- [x] Registered `docs/data/skill-research-batches/skill-batch-543.json` in `docs/data/pq-cross-domain-index.json` and updated `skill-catalog-audit.json`.
- [ ] Runtime/CI/build remains intentionally non-blocking/unverified.
- [ ] **Exact next:** continue field-level mechanics/restriction/version enrichment and explicit PQ↔skill bidirectional parity audits; acquisition endpoint completeness is now at 0 target-field gaps, and no relationship should be manufactured from an acquisition endpoint alone.


### 2026-09-28 continuation — Canonical Ki-cost enrichment batch 544
- [x] Audited the recovered **497-record** canonical skill corpus for null `ki_cost` fields after acquisition metadata completion.
- [x] Filled **10** previously null Ki-cost fields from explicit existing repository mechanics/research evidence: **Assault Rain (300), Blue Hurricane (300), Dead End Bullet (300), Death Meteor (300), Death Wave (100), Hellzone Grenade (300), Murder Grenade (100), Shocking Death Ball (300), Spirit Sword (400), Super Electric Strike (300)**.
- [x] Synchronized those ten values into `docs/data/skills-index.json` and registered `docs/data/skill-research-batches/skill-batch-544.json` in the cross-domain registry.
- [x] Preserved **Holstein Shock** and **Hyper Movement** as null-cost records because current repository evidence does not establish a numeric Ki activation cost; no class-wide or Evasive-to-Ki inference was applied.
- [x] Canonical corpus remains **497 records**; current null Ki-cost frontier is **2 records**.
- [ ] Runtime/CI/build remains intentionally non-blocking/unverified.
- [ ] **Exact next:** continue mechanics/restriction/version enrichment and explicit PQ↔skill bidirectional parity audits, starting with the remaining 2 unresolved Ki-cost records only if direct evidence appears; otherwise move to restriction/version gaps.


### 2026-09-28 continuation — Canonical skill resource/mechanics boundary batch 545
- [x] Audited the last two canonical null Ki-cost records after batch 544: **Holstein Shock** and **Hyper Movement**.
- [x] Preserved **Holstein Shock** `ki_cost=null` because reviewed direct evidence establishes its self-damaging behavior and PQ15 acquisition but does not establish a reliable numeric Ki activation cost.
- [x] Preserved **Hyper Movement** `ki_cost=null`; direct evidence identifies it as an Evasive with a **200 Stamina** activation cost and TP Medal Shop acquisition. Stamina was not converted into a Ki cost.
- [x] Created and registered `docs/data/skill-research-batches/skill-batch-545.json`; updated `docs/data/skill-catalog-audit.json` and the cross-domain batch registry.
- [ ] Runtime/CI/build remains intentionally non-blocking/unverified.
- [ ] Exact next: prioritize field-level mechanics/restriction/version enrichment and explicit PQ↔skill bidirectional parity beyond the current 249 canonical Skill→PQ edges. Do not manufacture a PQ edge from non-PQ acquisition evidence, and do not fill the two null Ki-cost fields without direct numeric evidence.

### 2026-09-28 continuation — Skill acquisition/mechanics/PQ parity audit batch 546
- [x] Audited the post-batch-545 canonical skill corpus: **497 records** remain authoritative.
- [x] Acquisition completeness remains **0 gaps** across `acquisition_type`, `source_quest_or_shop`, and `dlc_requirement`.
- [x] PQ↔skill bidirectional parity is complete for current scope: **249** canonical PQ→skill relationships; 244 canonical skills carry PQ metadata; 0 forward mismatches and 0 reverse orphan relationships.
- [x] `mechanics_notes` is populated for all 497 canonical records.
- [ ] Identified **27** canonical records with null `race_restriction`. These remain evidence-gated enrichment targets; `usable_by_cac` is not treated as proof of an all-race restriction.
- [ ] Separate version/patch provenance fields are not present in the current canonical schema; future work should enrich provenance without inventing schema semantics.
- [ ] Runtime/CI/build remains intentionally non-blocking/unverified.
- [ ] **Exact next:** research the 27 race/CaC restriction gaps using direct skill documentation or game/repository evidence, then advance version/patch provenance and deeper mechanics fields. Preserve all unresolved restrictions rather than filling them by inference.
\n### 2026-09-28 continuation — Skill restriction evidence audit batch 547\n- [x] Audited six canonical null-race-restriction skills: **Reverse Shot, Variant Drive, Revenge Final Flash, Blaster Ball, Ray Blast, Gigantic Breaker**.\n- [x] Current skill-page evidence confirms their identities/PQ endpoints/classifications and notable users, but does not directly establish CaC race restrictions.\n- [x] Preserved canonical nulls rather than inferring restrictions from NPC or Customize Partner users.\n- [x] Added research batch 547 and registered it in the cross-domain index; canonical corpus remains **497 records**.\n- [ ] Runtime/CI/build remains intentionally non-blocking/unverified.\n- [ ] **Exact next:** continue the remaining **27-record restriction-gap census** in evidence-backed batches, then audit version/patch provenance and version-sensitive mechanics.\n
### 2026-09-28 — Skill restriction evidence audit batch 548
- [x] Audited six additional canonical null-race-restriction skills: **Backflip, Break Strike, Consecutive Energy Blast, Energy Wave Combo, Power Pole Combo, and Turn Retreat**.
- [x] Added bounded evidence notes for their CaC availability/acquisition context while preserving null `race_restriction` values because no reviewed source establishes a narrower race/gender/form restriction.
- [x] Created and registered `docs/data/skill-research-batches/skill-batch-548.json` and updated the skill catalog audit.
- [ ] Runtime/CI/build remains intentionally non-blocking/unverified.
- [ ] Remaining restriction-gap census is **27**; continue only where direct evidence can establish a restriction, then move into version/patch provenance without inventing new canonical schema semantics.


### 2026-09-28 continuation — Post-corruption database rebuild/reconciliation checkpoint
- [x] Re-read the live continuation prompt and exhaustive TODO and treated the repaired canonical forward stores as the only source of truth.
- [x] Directly reconciled docs/data/skills.json against docs/data/skills-index.json: **497/497** records, zero duplicate IDs, zero index identity/order mismatches.
- [x] Directly recounted docs/data/pq-reward-relationships.json: **862 unique edges** — 249 Skill, 135 Super Soul, 136 Equipment, 247 Character, 88 DLC, 7 Farming; zero duplicate relationship keys.
- [x] Confirmed every canonical PQ→skill target resolves to a canonical skill identity; no orphan skill reward targets remain.
- [x] Confirmed acquisition target coverage is complete for the current 497-record canonical corpus (0 gaps) and mechanics_notes coverage is 497/497.
- [x] Confirmed 27 null race_restriction records remain evidence-bound gaps; no restriction was inferred from usable_by_cac, preset/NPC usage, or null-field presence.
- [x] Confirmed PQ1-PQ186 are represented in the relationship store's PQ range; PQ1 has no typed skill/Super Soul/equipment relationship in the cited source and is intentionally not fabricated.
- [x] Added docs/data/post-corruption-database-recovery-audit-2026-09-28.json and corrected the stale recovery baseline from 861 to the live **862-edge** state.
- [x] Updated docs/data/skill-catalog-audit.json to Batch 548 and current recovery reconciliation.
- [ ] Runtime/CI/build remains intentionally non-blocking/unverified.
- [ ] **Exact next:** continue direct-evidence restriction review where a narrower rule can actually be established; then create the version/patch provenance layer from explicit evidence and continue bidirectional PQ↔skill/Super Soul/equipment enrichment. Do not recreate recovered records, do not treat verified/index/projection layers as canonical, and preserve historical recovery counts as provenance.


### 2026-09-28 continuation — Version/patch provenance evidence census
- [x] Audited all **497** authoritative canonical skill records for explicit version/patch/update provenance signals without treating research dates as game-version evidence.
- [x] Found **284** records with explicit patch mentions, **287** with explicit version-sensitive/patch-independent language, **295** with explicit DLC/update provenance signals, and dated research-history notes in **497/497** records.
- [x] Added docs/data/skill-version-provenance-audit-2026-09-28.json as a structured evidence census.
- [x] Preserved the canonical schema boundary: skills.json currently has no dedicated version_history/patch_history field, so no inferred version values were written into canonical records.
- [ ] Runtime/CI/build remains intentionally non-blocking/unverified.
- [ ] **Exact next:** extract explicit game-version/update evidence from cited sources for the strongest provenance candidates, define a version-provenance schema before changing canonical records, and keep research-date metadata separate from game-version metadata.


### 2026-09-28 continuation — Authoritative release/version provenance registry foundation
- [x] Reconciled the version/patch audit against official Bandai Namco Xenoverse 2 release/update announcements instead of assigning game versions from research dates.
- [x] Added `docs/data/game-content-version-provenance-registry.json` with source IDs and event-level provenance for the 2018 free update, 2023 Beast free update, Future Saga Chapters 1-3, 2025 DAIMA Pack, and 2026 Future Saga Chapter 4 announcement.
- [x] Linked the registry from `docs/data/skill-version-provenance-audit-2026-09-28.json`.
- [x] Established the provenance rule that DLC/update event provenance and individual skill first-release/version assignment are separate claims; individual skills will only be mapped when direct skill-to-event evidence exists.
- [ ] Runtime/CI/build remains intentionally non-blocking/unverified.
- [ ] **Exact next:** map the strongest directly evidenced canonical skill IDs to the new release-event registry, beginning with explicit official skill mentions such as Beast; then expand to Future Saga/DAIMA skills only where direct linkage exists.


### 2026-09-28 direct release provenance
- [x] Added 5 direct skill to release mappings: Beast to Free Update 16; Crimson Edge, Divine Spear, Big Bang Knuckle, and Wild Stinger to Future Saga Chapter 1.
- [x] Added official Dragon Ball source evidence for the four named Chapter 1 moves.
- [x] Kept unmapped DLC skills unchanged when official evidence only gives an aggregate move count.
- [ ] Next: map Chapter 2, Chapter 3, Chapter 4, and DAIMA skills only when individual skills are directly named by authoritative evidence.


### 2026-09-28 continuation — Future Saga Chapter 2 provenance
- [x] Added 7 Chapter 2 skill-level provenance mappings: God of Destruction's Poise, God of Destruction's Plaything, God of Destruction's Might, Full Power Destruction, Soaring Rush, Dragon Spark, and Burst Blitz.
- [x] Bound the mapping to official Chapter 2 event evidence plus an independently maintained named skill catalog; no version date was inferred from research dates.
- [ ] **Next:** map Chapter 3, Chapter 4, and DAIMA individual skills using the same evidence-bound method.


### 2026-09-28 continuation — Future Saga Chapter 3 provenance
- [x] Added 6 Chapter 3 skill-level provenance mappings: Chaotic Time Impact, Dark Inscription, Emperor's Cannon, Gigantic Cross, Gigantic Nova, and Saiyan Blaster.
- [x] Bound Chapter 3 mapping to the official event announcement plus a named independent skill catalog; no release/version date was inferred from research dates.
- [ ] **Next:** map Future Saga Chapter 4 and DAIMA Pack individual skills using the same evidence-bound method.


### 2026-09-28 continuation — Future Saga Chapter 4 provenance
- [x] Added 4 Chapter 4 skill-level release-event mappings: Dragon Spiral, Indomitable, The Power to Overcome, and Venus Fist.
- [x] Used the official Bandai Namco Chapter 4 DLC page to establish the four-move event scope; the canonical records identify the individual four Chapter 4 moves.
- [x] Explicitly treated this as release-event scope, not an inferred patch/version date.
- [ ] **Next:** audit the DAIMA Pack individual skills and then reconcile Chapter 4 named character/move evidence where available.


### 2026-09-28 continuation — Dragon Ball DAIMA Pack provenance
- [x] Audited canonical skills whose `dlc_requirement` is `Dragon Ball DAIMA Pack`.
- [x] Confirmed 6 paid-pack skill records: Burning Blast, Final Flash (SS3 DAIMA), Force Edge, Heat Wave, Super Kamehameha (SS4 DAIMA), and Supreme Fury.
- [x] Added official Bandai Namco DAIMA Pack release provenance and mapped all 6 records to the event scope without inventing patch/version numbers.
- [x] Synchronized `skill-version-provenance-audit-2026-09-28.json` with the registry's current direct-mapping count.
- [ ] **Next:** separate remaining free-update DAIMA-era skills from paid-pack content, then reconcile Chapter 4 named-move evidence.


### 2026-09-28 continuation — DAIMA free-update skill boundary
- [x] Verified the official May 2025 DAIMA Pack announcement explicitly says a **free update also included Skills**. citeturn1search0
- [x] Audited canonical skill records: none currently carries an explicit DAIMA/free-update label identifying that separate free-update skill subset.
- [x] Recorded this as an explicit provenance gap rather than guessing which skills belonged to the free update.
- [ ] **Next:** seek direct skill-level evidence for the May 2025 free-update skills, then continue Chapter 4 named-move reconciliation.


### 2026-09-28 continuation — DAIMA free-update evidence review
- [x] Rechecked the official May 21, 2025 release announcement: it confirms the separate free update included Skills, but does **not name those Skills**. citeturn0search0
- [x] Confirmed the canonical database has six explicitly DAIMA Pack skills and no separately labeled May 2025 free-update skill records.
- [x] Preserved the distinction between paid-pack provenance and free-update provenance; no individual free-update skill was guessed.
- [ ] **Next:** search direct patch-note/community catalog evidence for the unnamed free-update skills; if none is sufficiently direct, move on to Chapter 4 named-move reconciliation.


### 2026-09-28 continuation — Free Update 20 evidence boundary
- [x] Added a community Free Update catalog source identifying Free Update 20 as the May 21, 2025 update associated with the DAIMA Pack.
- [x] Cross-checked the canonical skill database: the six DAIMA Pack skills are sourced to PQ179–181, while no additional canonical skills are explicitly labeled as Free Update 20.
- [x] Preserved the unresolved individual free-update skill mapping because the available evidence in this pass does not directly establish skill-name → canonical-ID matches.
- [ ] **Next:** reconcile Free Update 20 skill names against direct catalog evidence; if still unresolved, move to Future Saga Chapter 4 named-move evidence.


### 2026-09-28 continuation — Free Update 20 Festival skills identified as a canonical gap
- [x] Added the official Bandai Namco Japan release announcement for Free Update 20; it explicitly lists **4 Festival skills** as free-update content. citeturn0search2
- [x] Confirmed the current canonical skills store exposes only one explicitly Festival-labeled skill record (`Galaxy Breaker (Festival)`).
- [x] Recorded the discrepancy as an open canonical-data gap rather than inventing three skill IDs.
- [ ] **Next:** research the 4th Festival of Universes reward schedule to identify the four named Festival skills and reconcile them to canonical IDs; then continue Chapter 4 named-move evidence.


### 2026-09-28 continuation — Free Update 20 Budokai Festival skill gap
- [x] Found official Bandai Namco Free Update 20 documentation confirming **exactly 4 Budokai Festival skills** were added.
- [x] Confirmed the accessible official text does not name those four skills individually.
- [x] Audited canonical `skills.json`: only `Galaxy Breaker (Festival)` is explicitly represented as a Festival skill; no safe basis exists to invent three additional IDs/names.
- [x] Recorded a dedicated evidence gap requiring recovery from authoritative screenshots/video or a reliable independent catalog.
- [ ] **Next:** recover the four names, match them to canonical IDs, and assign provenance only after identity reconciliation.


### 2026-09-28 continuation — Free Update 20 Festival skill names recovered
- [x] Reconciled Free Update 20's four Budokai/Festival skills with the 4th Festival event evidence and independent Festival catalog: **God Bind (Festival), Egret Waltz (Festival), Gamma Force: Code-R (Festival), Gamma Force: Code-B (Festival)**.
- [x] Confirmed the 4th Festival introduced Goku (Super Saiyan God), Videl (DB Super), Gamma 1, and Gamma 2; official event material establishes the character scope. citeturn4search6
- [x] Discovered an important canonical-data gap: only Galaxy Breaker (Festival) currently exists in `skills.json`; the four recovered names do not yet have canonical records there.
- [x] Recorded the four names as **named-but-canonical-record-missing** rather than fabricating IDs or incomplete skill records.
- [ ] **Next:** recover complete canonical records/IDs and full fields for these four Festival skills from existing research batches/catalog evidence, then assign Free Update 20 provenance.


### 2026-09-28 continuation — Free Update 20 audit boundary closed
- [x] Cross-checked the official May 21, 2025 announcement with the maintained Free Update 20 catalog.
- [x] Established Free Update 20 as version 1.24.0 / May 21, 2025 and confirmed the official announcement's separate free-update Skills statement.
- [x] The available catalog does not provide a sufficiently direct named skill list to map additional canonical skill IDs; therefore **no additional skill provenance was fabricated**.
- [x] Closed this subtask as an explicitly documented unresolved provenance gap and advanced the frontier.
- [ ] **Next:** Future Saga Chapter 4 named-move reconciliation.


### 2026-09-28 continuation — Future Saga Chapter 4 named-skill corroboration
- [x] Added an independent July 8, 2026 guide that explicitly names all four Chapter 4 moves: The Power to Overcome, Dragon Spiral, Indomitable, and Venus Fist. citeturn2search0
- [x] Reclassified the four Chapter 4 registry mappings from `direct_scope` to `corroborated`, because the official source establishes the four-move scope while the independent source supplies the individual names.
- [x] Preserved the rule that this establishes release-event provenance, not an inferred patch/version number.
- [ ] **Next:** find additional independent or official named-move evidence for Chapter 4 and continue the unresolved Free Update 20 individual-skill investigation.


### 2026-09-28 continuation — Future Saga Chapter 4 skill corroboration
- [x] Added an independent current Steam PQ guide as direct reward evidence for **Dragon Spiral** and **Indomitable** from PQ185 and **Venus Fist** from PQ186. citeturn7search1
- [x] Upgraded those three registry mappings from generic event-scope evidence to direct community PQ-reward evidence.
- [x] Kept **The Power to Overcome** separately tied to the story/canonical record rather than incorrectly treating it as a PQ reward.
- [ ] **Next:** resolve the separately announced Free Update 20 skill set with direct patch/catalog evidence; official Bandai Namco confirms Skills were included but does not name them. citeturn0search1


### 2026-09-28 continuation — Free Update 20 Festival named-skill recovery layer
- [x] Reconciled the four Free Update 20 / 4th Festival skill identities: **God Bind (Festival), Egret Waltz (Festival), Gamma Force: Code-R (Festival), and Gamma Force: Code-B**.
- [x] Added `docs/data/festival-named-skill-recovery-layer-2026-09-28.json` as a dedicated **non-canonical recovery layer** preserving the recovered names, source characters, Festival camaraderie routes, and only directly supported mechanics/cost fields.
- [x] Added `docs/data/festival-named-skill-recovery-audit-2026-09-28.json` documenting the evidence and canonical-promotion boundary.
- [x] Preserved the source-of-truth rule: `docs/data/skills.json` remains authoritative; no canonical skill ID was invented and the 497-record canonical corpus was not changed.
- [x] Strengthened the recovery evidence with official Free Update 20/4th Festival scope plus independent named-skill/preset evidence.
- [ ] Canonical IDs/full records for these four identities remain unresolved and require surviving datamined/catalog identifiers or a historical canonical blob before promotion.
- [ ] Runtime/CI/build remains intentionally non-blocking/unverified.
- [ ] **Exact next:** continue substantive post-recovery enrichment by resolving remaining canonical restriction/version provenance gaps and cross-domain relationships; revisit the four Festival identities only when direct canonical identifiers become available.


### 2026-09-28 continuation — Festival recovery evidence batch 549
- [x] Added `docs/data/skill-research-batches/skill-batch-549.json` with an evidence-bound audit of all four recovered Free Update 20 / 4th Festival identities: **God Bind (Festival), Egret Waltz (Festival), Gamma Force: Code-R (Festival), Gamma Force: Code-B (Festival)**.
- [x] Corroborated each identity with the maintained Festival catalog plus independent community/recovery evidence and tied each to its corresponding Festival character.
- [x] Confirmed these are **Super Attacks** and preserved the Festival-character mapping without inventing canonical IDs.
- [x] Recorded the official Free Update 20 boundary: Bandai Namco confirms four Budokai Festival skills but the accessible official announcement does not individually name them; the independent catalog supplies the names.
- [x] Synchronized `docs/data/pq-cross-domain-index.json` to research batch 549 and advanced `docs/data/skill-catalog-audit.json` latest research batch to 549.
- [x] Canonical `docs/data/skills.json` remains unchanged; canonical skill count remains 497 and no unsupported IDs were invented.
- [ ] **Next:** recover complete canonical IDs/full records for these four Festival skills from surviving historical/datamined/catalog identifiers. If no authoritative identifier survives, retain the recovery layer and advance to the next unresolved post-recovery enrichment field.


### 2026-09-28 continuation — Festival recovery evidence batch 550
- [x] Strengthened all four recovered Festival identities with independent skill/preset evidence.
- [x] **God Bind (Festival)** now has directly corroborated Super/Ki Blast classification, Goku (Super Saiyan God) usage, 100 Ki cost, Festival unlock, and CaC-unavailable status from an independent skill page.
- [x] **Egret Waltz (Festival)** is directly tied to Videl (DB Super)'s second preset by independent preset evidence.
- [x] **Gamma Force: Code-R (Festival)** and **Gamma Force: Code-B (Festival)** are independently documented as Gamma 1/Gamma 2 Super Skills with Festival max-camaraderie acquisition.
- [x] Added `docs/data/skill-research-batches/skill-batch-550.json` and synchronized the catalog/cross-domain indexes.
- [x] Canonical `docs/data/skills.json` remains unchanged; no internal IDs were inferred from mod filenames, preset positions, or external naming.
- [ ] **Next:** search surviving structured/datamined sources for actual internal identifiers or historical canonical records for these four skills. If unavailable, advance to the next unresolved canonical enrichment field instead of manufacturing IDs.


### 2026-09-28 continuation — Festival canonical-ID reconciliation batch 551
- [x] Searched repository catalogs/history for all four recovered 4th Festival identities.
- [x] Confirmed **God Bind (Festival)** already has a detailed evidence record in batch 264, but no internal canonical ID.
- [x] Checked **Egret Waltz (Festival)**, **Gamma Force: Code-R (Festival)**, and **Gamma Force: Code-B** across current repository evidence; no canonical IDs were exposed.
- [x] Cross-checked current public Festival/datamine-oriented references; they confirm separate Festival skill entries and identity mappings but do not expose exact internal identifiers in accessible text.
- [x] Added `docs/data/skill-research-batches/skill-batch-551.json` documenting the negative ID reconciliation result.
- [x] Preserved the no-inference rule: no IDs derived from names, preset positions, mod filenames, or guessed numbering; `skills.json` remains unchanged.
- [ ] **Next:** advance to the next unresolved canonical enrichment field while retaining these four identities in the recovery layer; revisit ID recovery only if an exact historical/structured identifier source becomes available.


### 2026-09-28 continuation — PQ1 typed-reward boundary closure batch 552
- [x] Re-examined the post-recovery audit's apparent PQ1 typed-reward gap against the authoritative PQ research record.
- [x] Confirmed **PQ1 — Being a Time Patroller** documents only `120 Zeni` and `Energy Capsule S`; it has no documented skill, Super Soul, or equipment reward.
- [x] Added `docs/data/pq-reward-boundary-audits/pq-1-typed-reward-boundary-2026-09-28.json` documenting this as an intentional zero-typed-reward boundary.
- [x] Updated `docs/data/post-corruption-database-recovery-audit-2026-09-28.json` so PQ1 is no longer reported as a missing typed relationship endpoint.
- [x] Indexed the boundary audit in `docs/data/pq-cross-domain-index.json`.
- [x] Created **zero** new reward relationships; no unsupported edge was invented.
- [ ] **Next:** continue substantive cross-domain enrichment and explicit version/provenance research, while preserving intentional zero-reward boundaries separately from missing-data gaps.


### 2026-09-28 continuation — Free Update 20 provenance batch 553
- [x] Reconciled Free Update 20 against official Bandai Namco announcements.
- [x] Confirmed the **six DAIMA Pack skills** are paid-DLC content while the **four Festival skills** belong to the accompanying Free Update 20; the two groups are not conflated.
- [x] Recorded Free Update 20 as version **1.24.0 / May 21, 2025** based on the repository's existing release evidence and official announcement timing.
- [x] Added `docs/data/skill-research-batches/skill-batch-553.json` and synchronized the research/catalog indexes.
- [x] Preserved the canonical-ID boundary for the four Festival skills; no unsupported IDs or version assignments were invented.
- [ ] **Next:** audit the authoritative release registry against all 28 direct skill→event mappings and strengthen any weak event classification/source evidence.


### 2026-09-28 continuation — Direct skill-event provenance audit batch 554
- [x] Audited all **28 existing direct skill→release-event mappings** against `docs/data/game-content-version-provenance-registry.json`.
- [x] Confirmed 4 Chapter 1 mappings are directly named by primary Dragon Ball Official evidence.
- [x] Confirmed 7 Chapter 2 mappings are corroborated by official event evidence plus the maintained individual-skill catalog.
- [x] Confirmed 6 Chapter 3 mappings remain catalog-supported with the Chapter 3 event itself established by the authoritative registry.
- [x] Confirmed 4 Chapter 4 mappings remain independently corroborated through current skill/PQ evidence; no unsupported reassignment was made.
- [x] Confirmed Beast and the 6 DAIMA Pack mappings remain correctly separated from free-update provenance.
- [x] Added `docs/data/skill-research-batches/skill-batch-554.json`; no canonical skills or unsupported IDs were changed.
- [ ] **Next:** strengthen the six Chapter 3 and four Chapter 4 mappings with primary-source named-move evidence where available.


### 2026-09-28 continuation — Future Saga Chapter 3/4 provenance batch 555
- [x] Strengthened 6 Chapter 3 skill mappings with the official Chapter 3 release source while retaining independent named-skill evidence.
- [x] Reconciled 4 Chapter 4 mappings from the announcement event to the released Chapter 4 event.
- [x] Added the July 8, 2026 Dragon Ball Official Site release confirmation for Chapter 4.
- [x] Preserved evidence tiers; official release articles establish the DLC/event while independent sources provide individual move names where needed.
- [x] Added `docs/data/skill-research-batches/skill-batch-555.json` and updated the authoritative provenance registry.
- [x] Canonical skill records and IDs remain unchanged.
- [ ] Next: continue primary-source named-move research where explicit evidence exists, then advance to the next unresolved provenance or cross-domain enrichment frontier.


### 2026-09-28 continuation — Primary-source move-name boundary batch 556
- [x] Performed a targeted primary-source search for the individual Chapter 3 and Chapter 4 move names.
- [x] Confirmed official Bandai Namco/Nintendo material establishes the Chapter 3 six-move and Chapter 4 four-move counts, but the reviewed primary-source text does not individually name those moves.
- [x] Added `docs/data/skill-research-batches/skill-batch-556.json` documenting the evidence boundary.
- [x] Synchronized the skill catalog and PQ cross-domain indexes.
- [x] Preserved existing individual-skill evidence tiers; no unsupported primary attribution, fabricated ID, or version history was added.
- [ ] **Next:** advance to the next unresolved provenance or cross-domain enrichment frontier rather than repeatedly searching the same source text.


### 2026-09-28 continuation — PQ15 skill-reward reconciliation batch 557
- [x] Reconciled PQ15 against independent reward evidence.
- [x] Corrected the PQ15 research record to list Holstein Shock, Spinning Blade, and Fighting Pose D as documented skill rewards.
- [x] Preserved the Spinning Blade acquisition conflict; current independent skill evidence identifies TP Medal Shop, while older PQ evidence records PQ15.
- [x] Added and indexed the PQ15 reconciliation audit.
- [x] No unsupported canonical Spinning Blade ID or relationship was created because the skill is not currently in authoritative skills.json.
- [ ] **Next:** continue the next concrete PQ cross-domain enrichment frontier, or recover Spinning Blade only if direct canonical identity evidence becomes available.


2026-09-28: PQ22 reward reconciliation batch 558 completed. Corrected PQ22 research-layer omission: Energy Shot is explicitly a PQ22 skill reward; canonical relationship already existed, so no duplicate edge or canonical skill mutation was made. Added and indexed a dedicated reconciliation audit. Next: continue auditing concrete PQ research records for reward-list contradictions.


2026-09-28: Batch 559 PQ23 audit completed. Death Slash reward data was already internally consistent and independently corroborated; no canonical or research mutation was needed. Next frontier: PQ24-PQ28 reward contradiction audit.


2026-09-28: PQ34 reconciliation batch 559 completed. Corrected research-layer omission: Crusher Ball was listed in PQ34 basic rewards but omitted from skill_rewards; independent PQ reward transcription confirms both Crusher Ball and Paralysis. Canonical forward relationships already contained both, so no duplicate edge or canonical mutation was made. Dedicated reconciliation audit added. PQ cross-domain index update remains pending if write guard permits; next continue with PQ35-PQ40 parity audit.


2026-09-28: Batch 559 completed PQ31-PQ40 cross-domain reconciliation. All 9 typed skill-reward records have matching canonical PQ→skill edges; no research/canonical contradictions were found. PQ36 numbering/existence conflict remains explicitly preserved because maintained reward/objective sources document the quest while a separate datamined corpus disputes the numbering. Added and indexed the reconciliation audit; no canonical data or unsupported relationships were changed. Next frontier: PQ41 onward, prioritizing concrete reward-list/relationship contradictions.


2026-09-28: PQ23-PQ26 reward reconciliation batch 559 completed. Corrected research-layer omissions for Death Slash (PQ23), Double Death Slicer (PQ24), Spirit Explosion (PQ25), and Crazy Finger Shot (PQ26). Canonical reward relationships already existed; no duplicate edges or unsupported canonical mutations were made. Exact drop-slot/probability semantics remain unresolved. Added and indexed dedicated audit. Next: continue the same concrete PQ reward-boundary audit into PQ28+.


### 2026-09-28 continuation — PQ41-PQ50 recovery-forward reconciliation + index repair
- [x] Audited the recovered PQ41-PQ50 research records against the canonical PQ→skill relationship layer and existing reverse/research evidence.
- [x] Confirmed all 9 documented skill-reward records in PQ41-PQ50 have corresponding canonical skill relationships; PQ47 remains an intentional no-skill row in the maintained reward evidence rather than a missing relationship claim.
- [x] Preserved known identity boundaries: PQ48's maintained spelling "Kamekameha" resolves to canonical **Kamehameha**; PQ46's "Chain Destructo-disc Barrage" resolves to canonical **Chain Destructo-Disc Barrage**; PQ49's prior Do or Die Super Soul→skill correction remains intact.
- [x] Added docs/data/pq-reward-boundary-audits/pq-41-50-cross-domain-reconciliation-2026-09-28.json (batch 560).
- [x] Repaired a malformed docs/data/pq-cross-domain-index.json caused by a missing comma between the batch-547 and batch-549 entries, then indexed the new PQ41-PQ50 audit; the index now parses as valid JSON.
- [x] Refreshed docs/data/pq-cross-domain-audit.json with the PQ41-PQ50 reconciliation and current canonical relationship recount: **862 edges** = 249 skills, 135 Super Souls, 136 equipment, 247 characters, 88 DLC, 7 farming.
- [x] No canonical reward relationships were invented or removed; canonical source-of-truth policy remains unchanged.
- [ ] Runtime/CI/build remains intentionally non-blocking/unverified.
- [ ] **Exact next:** continue the recovery-forward PQ cross-domain audit from **PQ51 onward**, prioritizing concrete reward-list/relationship contradictions and malformed consumer artifacts; do not create redundant audits where layers already agree.


### 2026-09-28 continuation — PQ51-PQ60 recovery-forward reconciliation
- [x] Audited PQ51-PQ60 across the dedicated PQ research batch, maintained PQ record layer, and canonical PQ→reward relationship store.
- [x] Found and repaired one real recovery omission: maintained PQ57 had an empty skill_rewards array even though the dedicated research batch and canonical relationship store both document **Rakshasa's Claw**.
- [x] Confirmed PQ51-PQ56, PQ58-PQ60 skill relationships agree with canonical data; PQ59's Force Shield/Dimension Cannon ordering difference is non-semantic and was not treated as a contradiction.
- [x] Added docs/data/pq-reward-boundary-audits/pq-51-60-cross-domain-reconciliation-2026-09-28.json (batch 561) and indexed it in docs/data/pq-cross-domain-index.json.
- [x] Canonical relationship data was not changed and no unsupported relationship was invented.
- [ ] Runtime/CI/build remains intentionally non-blocking/unverified.
- [ ] **Exact next:** continue PQ61-PQ70 using the same three-layer comparison and repair actual omissions before enrichment.


### 2026-09-28 continuation — PQ61-PQ70 recovery-forward reconciliation
- [x] Audited PQ61-PQ70 against canonical typed reward relationships and the maintained PQ record layer.
- [x] Repaired maintained reward projections missing after corruption: PQ61 Battle Suit (CC); PQ62 Frieza's Suit (Final Form); PQ63 Goku Wig (Super Saiyan) + Before creation comes ruin...; PQ64 Janemba! Janemba!; PQ65 Gohan's Gi (Adult) + I never knew this world existed!; PQ66 SSGSS Goku Wig + Whis Symbol Gi + Warp Kamehameha.
- [x] Canonical skill relationships were already present except PQ66 Warp Kamehameha, which was restored to the maintained skill projection from the canonical source-backed relationship.
- [x] Added batch-562 audit and indexed it in docs/data/pq-cross-domain-index.json.
- [x] Did not project pq_features_character links into reward fields; featured characters are not equivalent to acquisition rewards.
- [ ] Runtime/CI/build remains intentionally non-blocking/unverified.
- [ ] **Exact next:** PQ71-PQ80 canonical-first reward projection/reconciliation.


### 2026-09-28 continuation — PQ71-PQ80 recovery-forward reconciliation
- [x] Audited PQ71-PQ80 across dedicated PQ research, maintained PQ records, and canonical typed reward relationships.
- [x] Restored canonical-backed maintained equipment projections: PQ72 Jaco's State-of-the-Art Radio; PQ73 Tagoma's Scouter; PQ76 SSGSS Goku Wig; PQ79 Vegeta's Shirt.
- [x] Confirmed all ten canonical skill relationships already project correctly into maintained skill_rewards.
- [x] Preserved unresolved/non-canonical reward boundaries: PQ73 Qipao (CC) and PQ76 Whis Symbol Gi were not promoted without canonical relationship evidence.
- [x] Added and indexed batch-563 audit; canonical source-of-truth data was not modified.
- [ ] Runtime/CI/build remains intentionally non-blocking/unverified.
- [ ] **Exact next:** PQ81-PQ90 canonical-first reward projection/reconciliation.


### 2026-09-28 continuation — PQ81-PQ90 recovery-forward reconciliation
- [x] Audited PQ81-PQ90 across dedicated PQ research, maintained PQ records, and canonical typed reward relationships.
- [x] Repaired maintained skill omissions: PQ86 Neo Wolf Fang Fist and PQ87 Atomic Blast.
- [x] Normalized PQ90 maintained `III Bomber` to canonical `Ill Bomber` using the repository's established alias rule; preserved the research spelling as provenance and did not create a duplicate skill.
- [x] Confirmed no canonical equipment or Super Soul reward relationships exist for PQ81-PQ90.
- [x] Added and indexed batch-564 audit; canonical source-of-truth data was not modified.
- [ ] Runtime/CI/build remains intentionally non-blocking/unverified.
- [ ] **Exact next:** PQ91-PQ100 canonical-first reward projection/reconciliation.


### 2026-09-28 continuation — PQ91-PQ100 recovery-forward reconciliation
- [x] Audited PQ91-PQ100 across dedicated PQ research, maintained PQ records, and canonical typed reward relationships.
- [x] Confirmed zero research→maintained reward mismatches across the final ten base-game PQ records.
- [x] Confirmed PQ100's canonical X 100 Big Bang Kamehameha relationship and existing maintained projection; SSGSS Vegeta Wig remains correctly represented through accessory `acc-068`, and Whis Symbol Battle Suit through equipment `equip-088`.
- [x] Identified a canonical relationship coverage gap for researched/maintained skills in PQ91, PQ92, PQ94-PQ99 (9 skill relationships total) but did not promote them into canonical data without independent canonical evidence.
- [x] Added and indexed batch-565 audit. Canonical source-of-truth data was not modified.
- [ ] Runtime/CI/build remains intentionally non-blocking/unverified.
- [ ] **Exact next:** PQ101-PQ110 recovery-forward reconciliation, while retaining the PQ91-PQ99 canonical skill-coverage gap as an explicit follow-up research task.


### 2026-09-28 continuation — PQ101-PQ110 recovery-forward reconciliation
- [x] Audited PQ101-PQ110 against dedicated research, maintained PQ records, and canonical typed reward relationships.
- [x] Repaired maintained reward projections for all canonical-backed rewards: skills, equipment, and Super Souls across PQ101-PQ110.
- [x] Restored accessory links for Android 14's Hat (PQ104), Android 13's Hat (PQ105), and SS4 Wig & Tail (Goku) (PQ110) where canonical accessory identities are present.
- [x] Preserved canonical source-of-truth boundary: no canonical relationship mutations were made.
- [x] Added/indexed batch-566 reconciliation audit.
- [ ] Runtime/CI/build remains intentionally non-blocking/unverified.
- [ ] **Exact next:** PQ111-PQ120 recovery-forward reconciliation.


### 2026-09-28 continuation — PQ111-PQ120 recovery-forward reconciliation
- [x] Audited PQ111-PQ120 across dedicated research, maintained PQ records, and canonical typed reward relationships.
- [x] Repaired maintained skill/equipment/Super Soul projections for canonical-backed rewards.
- [x] Normalized accessory endpoints for Resistance Helmet (PQ111) and Toppo's Moustache (PQ112); no unsupported equipment identities were fabricated.
- [x] Preserved PQ113's researched `Candy Beam (Super)` boundary; did not project the separate canonical `Candy Beam` without research evidence.
- [x] Added/indexed batch-567 reconciliation audit; canonical data unchanged.
- [ ] Runtime/CI/build remains intentionally non-blocking/unverified.
- [ ] **Exact next:** PQ121-PQ130 recovery-forward reconciliation.


### 2026-09-28 continuation — PQ121-PQ130 recovery-forward reconciliation
- [x] Audited PQ121-PQ130 across dedicated research, maintained PQ records, and canonical typed reward relationships.
- [x] Restored canonical-backed maintained reward projections, including PQ121's Tuxedo/Wedding Dress/Super Soul and missing Super Souls/equipment through PQ130.
- [x] Preserved accessory boundaries for Goku Wig (Ultra Instinct) (PQ125) and Janemba Head (PQ127).
- [x] Added/indexed batch-568 reconciliation audit; canonical data unchanged.
- [ ] Runtime/CI/build remains intentionally non-blocking/unverified.
- [ ] **Exact next:** PQ131-PQ140 recovery-forward reconciliation.


### 2026-09-28 continuation — PQ121-PQ130 live-state reconciliation correction
- [x] Re-inspected the live maintained PQ layer instead of relying on the earlier batch summary.
- [x] Found and repaired the two remaining maintained equipment projection omissions: PQ123 Arabian Costume -> equip-039 and PQ127 Janemba Suit -> equip-040.
- [x] Confirmed PQ125 Goku Wig (Ultra Instinct) and PQ127 Janemba Head remain accessory endpoints (acc-051/acc-052), not fabricated equipment IDs.
- [x] Confirmed PQ121-PQ130 skill and Super Soul projections align with the existing canonical relationship store; no unsupported canonical relationship was added.
- [x] Corrected the batch-568 audit to describe the live recovery state and indexed it in pq-cross-domain-index.json.
- [x] Canonical source data was not changed.
- [ ] Runtime/CI/build remains intentionally non-blocking/unverified.
- [ ] **Exact next:** PQ131-PQ140 recovery-forward reconciliation.


### 2026-09-28 continuation — PQ131-PQ140 recovery-forward reconciliation
- [x] Re-read the live continuation prompt/TODO and audited PQ131-PQ140 across dedicated research, maintained PQ records, canonical typed reward relationships, and accessory endpoint records.
- [x] Repaired maintained PQ134 skill projections: Burst Charge and Ultimate Charge.
- [x] Restored canonical-backed equipment projections: PQ131 SSGSS Gogeta's Clothes (equip-042); PQ133 Kakunsa's Clothes (equip-043); PQ135 Rozie's Clothes (equip-044); PQ139 Android 21's Lab Uniform (equip-045) and Universe 7 Baseball Uniform (equip-046).
- [x] Restored accessory cross-links for Broly Wig (Legendary Super Saiyan) (PQ132, acc-072), Kakunsa's Tail (PQ133, acc-074), Kakunsa's Wig and Mask (PQ133, acc-073), Rozie's Hood and Goggles (PQ135, acc-075), and Universe 7 Baseball Cap (PQ139, acc-076).
- [x] Restored all eight missing canonical-backed Super Soul projections across PQ131-PQ140.
- [x] Confirmed all ten canonical skill relationships now project into maintained skill_rewards; only PQ134 required repair.
- [x] Added/indexed batch-569 reconciliation audit; canonical source-of-truth data was not modified.
- [ ] Runtime/CI/build remains intentionally non-blocking/unverified.
- [ ] **Exact next:** PQ141-PQ150 numbering-gap audit; do not fabricate ten quests. Then continue PQ151-PQ160 recovery-forward reconciliation.


### 2026-09-28 continuation — PQ141-PQ150 numbering-gap reconciliation batch 570
- [x] Audited PQ141-PQ150 as a numbering-gap state using the repository's existing numbering reconciliation and PQ audit documentation.
- [x] Confirmed there are no populated maintained PQ records or canonical reward relationships for PQ141-PQ150; the next populated structured block begins at PQ151.
- [x] Added `docs/data/pq-reward-boundary-audits/pq-141-150-numbering-gap-2026-09-28.json` (batch 570) and indexed it in `docs/data/pq-cross-domain-index.json`.
- [x] Preserved the evidence boundary: no quest records, rewards, skills, Super Souls, equipment, accessories, characters, DLC requirements, or objectives were fabricated for the ten unpopulated numbers.
- [x] Kept the separate historical/cut PQ36 conflict unchanged.
- [ ] Runtime/CI/build remains intentionally non-blocking/unverified.
- [ ] **Exact next:** PQ151-PQ160 recovery-forward reconciliation.


### 2026-09-28 continuation — PQ151-PQ160 recovery-forward reconciliation batch 571
- [x] Reconciled PQ151-PQ160 against dedicated research, maintained records, and the existing canonical PQ reward relationship store.
- [x] Confirmed all 10 documented skill reward projections were already present in the maintained layer.
- [x] Restored canonical-backed clothing/equipment projections for PQ152 (equip-038), PQ154 (equip-048), and PQ158 (equip-054).
- [x] Restored accessory endpoint links for Android 17 (DB Super) Wig, King Vegeta (DB Super) Wig, Gamma 2's Helmet, Gamma 1's Helmet, Dr. Hedo Hood, and Red Ribbon Army Helmet.
- [x] Restored eight maintained Super Soul reward projections across PQ151-PQ160.
- [x] Preserved the unresolved Android 17 Ranger Accessory component boundary; no unsupported merge or canonical relationship was invented.
- [x] Added/indexed `docs/data/pq-reward-boundary-audits/pq-151-160-cross-domain-reconciliation-2026-09-28.json` (batch 571).
- [ ] Runtime/CI/build remains intentionally non-blocking/unverified.
- [ ] **Exact next:** PQ161-PQ170 recovery-forward reconciliation.


### 2026-09-28 continuation — PQ161-PQ170 recovery-forward reconciliation batch 572
- [x] Re-read the live continuation prompt/TODO and audited PQ161-PQ170 against dedicated research, maintained PQ records, canonical typed reward relationships, and equipment/accessory endpoint records.
- [x] Restored maintained skill projections for PQ163-PQ168; PQ161-PQ162 skill projections were already present.
- [x] Restored canonical-backed equipment projections for PQ161 (equip-055), PQ162 (equip-052/equip-056), PQ169 (equip-071), and PQ170 (equip-072).
- [x] Restored five missing maintained Super Soul projections across PQ161, PQ162, PQ164, PQ166, and PQ168.
- [x] Restored Videl (DB Super) Wig for PQ168 as accessory endpoint acc-082 rather than fabricating an equipment ID.
- [x] Preserved the canonical source-of-truth boundary; canonical relationship data was not modified and no unsupported relationship was invented.
- [x] Added/indexed `docs/data/pq-reward-boundary-audits/pq-161-170-cross-domain-reconciliation-2026-09-28.json` (batch 572).
- [ ] Runtime/CI/build remains intentionally non-blocking/unverified.
- [ ] **Exact next:** PQ171-PQ180 recovery-forward reconciliation.


### 2026-09-28 continuation — PQ171-PQ180 recovery-forward reconciliation batch 573
- [x] Re-read the live continuation prompt/TODO and audited PQ171-PQ180 against dedicated research, maintained PQ records, canonical typed reward relationships, and equipment/accessory endpoint records.
- [x] Restored 17 maintained skill reward projections across PQ171-PQ180.
- [x] Restored four canonical equipment projections: PQ176 Belmod's Clothes (equip-073), PQ178 Goku (Mini)'s Gi (equip-074), PQ179 SS4 Goku (DAIMA) Suit (equip-075), and PQ180 SS3 Vegeta (DAIMA) Battle Suit (equip-076).
- [x] Restored accessory endpoint links for PQ179 SS4 Goku (DAIMA) Wig & Tail (acc-083) and PQ180 SS3 Vegeta (DAIMA) Wig (acc-084); no accessory was represented as a fabricated equipment ID.
- [x] Restored six maintained Super Soul reward projections across PQ173, PQ175-PQ178, and PQ180.
- [x] Preserved canonical spelling boundaries where research transcriptions differ: PQ173 uses `You will know the power of the gods!`; PQ178 uses `I'll take you all on at once!`.
- [x] Added/indexed `docs/data/pq-reward-boundary-audits/pq-171-180-cross-domain-reconciliation-2026-09-28.json` (batch 573).
- [x] Canonical relationship data was not modified and no unsupported relationship was invented.
- [ ] Runtime/CI/build remains intentionally non-blocking/unverified.
- [ ] **Exact next:** PQ181-PQ186 final numbered-block recovery-forward reconciliation; after that, move to the next substantive cross-domain/provenance frontier rather than fabricating PQ numbers beyond the final populated block.


### 2026-09-28 continuation — PQ181-PQ186 final numbered-block recovery-forward reconciliation batch 574
- [x] Re-read the live continuation prompt/TODO and audited the final populated PQ block PQ181-PQ186 against dedicated research, maintained PQ records, canonical typed reward relationships, and equipment/accessory endpoint records.
- [x] Restored all six maintained skill reward projections: PQ181 Super Kamehameha (SS4 DAIMA) + Final Flash (SS3 DAIMA); PQ182 Dark Inscription; PQ183 Emperor's Cannon; PQ184 Chaotic Time Impact; PQ185 Dragon Spiral + Indomitable; PQ186 Venus Fist.
- [x] Restored seven canonical equipment projections using equipment endpoints: PQ181 Glorio's Clothes/Panzy's Clothes, PQ182 Golden Frieza Suit, PQ185 Goku (Ultra Supervillain Quelled)'s Clothes, and PQ186 Fu (Ultra Supervillain)'s Clothes/Fu (Ultra Supervillain) Set/Fu Set 2.
- [x] Restored seven accessory endpoints: PQ181 Glorio Wig/Panzy Wig, PQ182 Golden Frieza Head, PQ183 Cheelai's Coat/Broly Wig (Black Hair, Normal), PQ184 Dragon Ball Balloon, and PQ185 Goku (Ultra Supervillain Quelled) Wig.
- [x] Restored seven maintained Super Soul projections across PQ182-PQ186.
- [x] Corrected PQ183 Cheelai's Coat to the canonical accessory endpoint acc-087 instead of fabricating an equipment ID.
- [x] Preserved the canonical source-of-truth boundary; canonical relationship data was not modified and no unsupported reward/drop relationship was invented.
- [x] Added/indexed `docs/data/pq-reward-boundary-audits/pq-181-186-cross-domain-reconciliation-2026-09-28.json` (batch 574).
- [ ] Runtime/CI/build remains intentionally non-blocking/unverified.
- [ ] **Exact next:** move to the next substantive cross-domain/provenance frontier after the final populated PQ block; do not fabricate PQ numbers beyond PQ186.


### 2026-09-28 continuation — Post-recovery artifact integrity repair batch 575
- [x] Freshly inspected the recovered live main state after the PQ181-PQ186 final recovery block; canonical recovery remains clean at **497 canonical skills** and **862 canonical PQ reward edges**.
- [x] Found a concrete malformed-consumer artifact: `docs/data/skill-catalog-audit.json` contained `"latest_research_batch": 553,,`, which made that audit document invalid JSON even though canonical stores remained intact.
- [x] Added `docs/data/skill-catalog-json-integrity-repair-2026-09-28.json` documenting the exact syntax repair and evidence boundary.
- [x] Repaired `docs/data/skill-catalog-audit.json` without changing `skills.json`, `skills-index.json`, or `pq-reward-relationships.json`.
- [x] Re-read and parsed the repaired skill catalog audit plus the post-corruption recovery audit and current live recovery baseline successfully.
- [ ] Runtime/CI/build remains intentionally non-blocking/unverified.
- [ ] **Exact next:** continue the version/patch provenance frontier from the existing evidence census and authoritative release registry; do not assign game versions from research dates or inference. Then continue bidirectional PQ↔skill/Super Soul/equipment enrichment where direct evidence supports it.


### 2026-09-28 continuation — Skill version/patch provenance schema foundation batch 576
- [x] Established `docs/data/skill-version-provenance-schema.json` as the evidence-backed contract for future skill release/version provenance.
- [x] Explicitly separated release-event provenance from balance-patch history, research timestamps, and unresolved version fields.
- [x] Defined conservative confidence/evidence states and a patch-change contract requiring explicit source evidence before any balance-change record is populated.
- [x] Recorded the current evidence census: **497** canonical skills; **28** direct skill→release-event mappings; **284** with explicit patch mentions, **287** with explicit version-sensitive language, and **295** with explicit DLC/update provenance signals in reviewed evidence.
- [x] Preserved the four Free Update 20 Festival identities as named event skills with unresolved canonical internal IDs; no IDs were inferred and no canonical skill records were fabricated.
- [x] Updated `docs/data/skill-catalog-audit.json` to make version/patch provenance the active field-level frontier.
- [ ] Runtime/CI/build remains intentionally non-blocking/unverified.
- [ ] **Exact next:** use the new provenance contract to audit canonical skills with explicit release/update evidence, prioritizing direct event/version evidence and leaving unsupported version fields null; then continue cross-domain enrichment.


### 2026-09-28 continuation — Official Future Saga provenance reconciliation batch 577
- [x] Audited the authoritative release registry against current official Bandai Namco / Dragon Ball Official Site material.
- [x] Confirmed official Future Saga Chapter 3 scope of **6 Additional Moves** and Chapter 4 scope of **4 New Moves including 1 Awoken Skill** from the official DLC catalog.
- [x] Confirmed official Chapter 3 launch coverage and Chapter 4 launch coverage as independent event-level provenance sources.
- [x] Preserved the six Chapter 3 and four Chapter 4 individual canonical mappings as corroborated mappings because the cited official pages provide aggregate move counts but do not name every individual move.
- [x] Added `docs/data/skill-research-batches/skill-batch-577.json` documenting the evidence boundary and event-count reconciliation.
- [x] Corrected the provenance schema confidence vocabulary to include the registry's existing `direct_scope` value.
- [x] Updated `docs/data/game-content-version-provenance-registry.json` with batch 577 and the next evidence-bound task.
- [ ] Runtime/CI/build remains intentionally non-blocking/unverified.
- [ ] **Exact next:** continue individual skill-name primary-source reconciliation where official sources explicitly name moves; otherwise preserve corroborated mappings and move to the next evidence-backed provenance gap. Do not infer versions from research dates or aggregate DLC counts.


### 2026-09-28 continuation — Festival skill recovery candidate reconciliation batch 578
- [x] Investigated the open Free Update 20 Festival provenance gap instead of leaving the four named skills as unexplained missing identities.
- [x] Recovered four named Festival candidates: **God Bind (Festival)**, **Egret Waltz (Festival)**, **Gamma Force: Code-R (Festival)**, and **Gamma Force: Code-B (Festival)**.
- [x] Reconciled character associations and Festival camaraderie acquisition routes from existing repository research plus independent current evidence; God Bind also has a detailed mechanics/acquisition record in the historical Batch 264 research layer.
- [x] Confirmed **Galaxy Breaker (Festival)** is already represented canonically, leaving these four as the outstanding named Festival recovery candidates.
- [x] Added `docs/data/skill-research-batches/skill-batch-578.json` and updated the authoritative provenance registry.
- [x] Deliberately did **not** invent canonical IDs or mutate `skills.json`; complete schema-level identity recovery is required before canonical propagation.
- [ ] Runtime/CI/build remains intentionally non-blocking/unverified.
- [ ] **Exact next:** recover complete field sets and canonical identity evidence for these four Festival candidates, then perform controlled canonical propagation if uniqueness/schema completeness is proven.


### 2026-09-28 continuation — Official 4th Festival scope reconciliation batch 579
- [x] Added primary-source event evidence from the Dragon Ball Official Site for the four 4th Festival camaraderie characters: Goku (Super Saiyan God), Videl (DB Super), Gamma 1, and Gamma 2.
- [x] Confirmed the official event source describes special rewards for increasing camaraderie with those four characters; the accessible page does not individually expose all four skill names or internal skill IDs.
- [x] Cross-bound the official character scope to the existing four named recovery identities without promoting them into `skills.json`.
- [x] Added `docs/data/skill-research-batches/skill-batch-579.json` and updated the version/provenance registry.
- [x] Preserved the canonical-ID boundary: no identifier was inferred from character order, preset order, filenames, or skill names.
- [ ] Runtime/CI/build remains intentionally non-blocking/unverified.
- [ ] **Exact next:** move to the next evidence-backed canonical enrichment frontier; revisit Festival ID recovery only if an exact historical/structured identifier source appears.


### 2026-09-28 continuation — Official 3rd Festival named-skill reconciliation batch 580
- [x] Expanded Festival provenance beyond the 4th Festival by reconciling the official 3rd Festival weekly reward announcements.
- [x] Officially named **Charge (Festival)** (Goten), **Galick Rush (Festival)** (Cabba), **Hellzone Grenade (Festival)** (Piccolo), and **Sonic Bomb (Festival)** (Frieza 1st Form).
- [x] Confirmed **Galaxy Breaker (Festival)** is already represented canonically and therefore did not create a duplicate recovery record.
- [x] Added `docs/data/skill-research-batches/skill-batch-580.json`.
- [x] Did not infer canonical IDs for the four newly identified variants from their base skill names, character identity, reward order, or preset positions.
- [x] Official sources explicitly name the four skills; repository search did not expose exact internal IDs, so they remain recovery candidates rather than canonical mutations.
- [ ] Runtime/CI/build remains intentionally non-blocking/unverified.
- [ ] **Exact next:** search historical recovery layers/structured data for exact IDs for these four Festival variants; if unavailable, retain the official evidence layer and continue the next canonical enrichment frontier.


### 2026-09-28 continuation — PQ186 final skill-reward parity batch 581
- [x] Audited PQ186 separately as the final numbered PQ block after PQ181-PQ185.
- [x] Confirmed the maintained forward/reverse relationship for **Venus Fist → PQ186**.
- [x] Confirmed no additional PQ186 skill endpoint is supported by the current reward evidence.
- [x] Preserved unresolved reward-slot/drop-probability and mandatory-Ultimate-Finish semantics rather than inferring them.
- [x] Added `docs/data/skill-research-batches/skill-batch-581.json`.
- [x] This closes the PQ181–PQ186 final skill-reward parity block with zero unresolved canonical skill endpoints.
- [ ] Next: move outside this settled range to unresolved typed-reward ranges and active mechanics/version-provenance frontiers.


### 2026-09-28 continuation — Late-DLC typed-reward reconciliation batch 582
- [x] Reconciled the apparent PQ163-PQ186 Super Soul/equipment coverage gaps against the normalized late-DLC reward map.
- [x] Confirmed **15/15 Super Soul edges** reconcile exactly between the normalized map and canonical relationship layer after documented name normalization.
- [x] Confirmed **23/23 equipment edges** reconcile exactly between the normalized map and canonical relationship layer.
- [x] Confirmed there are no map-only or relationship-only edges in either typed category.
- [x] Added `docs/data/skill-research-batches/skill-batch-582.json`.
- [x] Preserved the distinction between coverage sparsity and demonstrated missing canonical relationships; absent PQ IDs are not treated as proof of no reward.
- [ ] Next: prioritize genuinely unresolved global typed-reward cases and skill mechanics/version-provenance enrichment rather than duplicating reconciled PQ163-PQ186 relationships.


### 2026-09-28 continuation — Canonical relationship census + Festival ID re-audit batch 583
- [x] Recounted the live canonical relationship store: **249 skill→PQ edges** and **862 total PQ relationships**.
- [x] Corrected the stale global PQ skill-endpoint audit census from 852 to **862**; no canonical relationship was added or removed by this synchronization.
- [x] Re-audited exact repository evidence for the four unresolved 4th Festival identities: God Bind (Festival), Egret Waltz (Festival), Gamma Force: Code-R (Festival), and Gamma Force: Code-B (Festival).
- [x] Confirmed exact canonical internal identifiers remain unrecovered; no ID was inferred from names, character/preset order, filenames, or reward ordering.
- [x] Added `docs/data/skill-research-batches/skill-batch-583.json`.
- [ ] Runtime/CI/build remains intentionally non-blocking/unverified.
- [ ] **Exact next:** continue with a substantive mechanics or version/provenance enrichment cohort; revisit Festival identifiers only when exact structured evidence becomes available.


### 2026-09-28 continuation — Future Saga Chapter 4 release provenance reconciliation batch 584
- [x] Reconciled the official Chapter 4 release event as **2026-07-08** using the Dragon Ball Official Site release announcement.
- [x] Added the released `future-saga-chapter-4` event to `docs/data/game-content-version-provenance-registry.json`, while retaining the earlier announcement event separately.
- [x] Preserved the four existing Chapter 4 individual skill mappings: Dragon Spiral, Indomitable, The Power to Overcome, and Venus Fist.
- [x] Explicitly kept game version/patch fields unassigned; release-event dates are not patch/version numbers.
- [x] Added `docs/data/skill-research-batches/skill-batch-584.json`.
- [ ] Runtime/CI/build remains intentionally non-blocking/unverified.
- [ ] **Exact next:** audit remaining Free Update 20/DAIMA-era free-update skill provenance separately from the paid DAIMA Pack, then continue Chapter 4 mechanics enrichment.


### 2026-09-28 continuation — Direct skill-event provenance audit batch 585
- [x] Audited all 28 direct skill-event mappings.
- [x] Confirmed all mappings resolve to registered events and have non-empty source IDs.
- [x] Confirmed evidence semantics remain appropriate across Chapter 1, Beast, Chapters 2-4, and the DAIMA Pack.
- [x] Confirmed 0 unsupported version/patch assignments and 0 canonical mutations required.
- [x] Added `docs/data/skill-research-batches/skill-batch-585.json`.
- [ ] Runtime/CI/build remains intentionally non-blocking/unverified.
- [ ] Exact next: continue Chapter 4 mechanics enrichment and separately audit Free Update 20 Festival recovery evidence.


### 2026-09-28 continuation — Chapter 4 mechanics reconciliation batch 586
- [x] Refreshed evidence for all four Future Saga Chapter 4 moves against current official DLC scope and current item-level/player evidence.
- [x] Preserved bounded mechanics for The Power to Overcome, Indomitable, Venus Fist, and Dragon Spiral without inventing exact frames, scaling, cooldowns, or probabilities.
- [x] Confirmed 4 Chapter 4 move records, 0 new Skill→PQ edges, 0 unsupported drop-rate claims, and 0 version/patch assignments.
- [x] Added `docs/data/skill-research-batches/skill-batch-586.json`.
- [ ] Runtime/CI/build remains intentionally non-blocking/unverified.
- [ ] Exact next: audit Free Update 20 Festival recovery identities against the canonical catalog and exact historical structured evidence.


### 2026-09-28 continuation — Festival indexed-catalog reconciliation batch 587
- [x] Audited the four unresolved 4th Festival identities against the maintained indexed skill-category universe and exact repository search results.
- [x] Confirmed **God Bind (Festival)** is present in the indexed-only name set, proving indexed-name coverage but not exposing a canonical internal ID.
- [x] Confirmed **Egret Waltz (Festival)**, **Gamma Force: Code-R (Festival)**, and **Gamma Force: Code-B (Festival)** are not present in the current indexed-only name set and remain recovery-layer identities only.
- [x] Preserved the canonical boundary: **0 exact IDs recovered, 0 canonical Festival records promoted, 0 PQ relationships changed**.
- [x] Added `docs/data/skill-research-batches/skill-batch-587.json` and synchronized the catalog audit.
- [ ] Runtime/CI/build remains intentionally non-blocking/unverified.
- [ ] **Exact next:** move to the next substantive version/provenance or mechanics enrichment frontier; revisit Festival IDs only when an exact structured historical artifact or canonical blob exposes them.


### 2026-09-29 continuation — Free Update 20 event provenance reconciliation batch 588
- [x] Separated Free Update 20 / Budokai Festival provenance from the paid Dragon Ball DAIMA Pack in the authoritative game-content provenance registry.
- [x] Recorded the official 2025-05-21 Free Update 20 event boundary using Bandai Namco's release notice; official evidence confirms the accompanying free update included Skills.
- [x] Preserved the official four-skill Budokai Festival scope while keeping the four named Festival identities in the non-canonical recovery layer because exact internal IDs remain unresolved.
- [x] Preserved the six paid DAIMA Pack skill mappings as a distinct paid event; no free-update skill was inferred from paid-pack proximity.
- [x] Added `docs/data/skill-research-batches/skill-batch-588.json`.
- [x] No `skills.json` mutation, no PQ relationship mutation, and no unsupported version assignment.
- [ ] Runtime/CI/build remains intentionally non-blocking/unverified.
- [ ] **Exact next:** continue substantive canonical skill provenance/mechanics enrichment outside the already-audited Festival identity gap; revisit Festival IDs only when an exact structured historical artifact or canonical blob exposes them.


### 2026-09-29 continuation — Future Saga Chapter 1 individual skill provenance completion batch 589
- [x] Closed the Chapter 1 individual skill-provenance gap: the registry already declared 15 Chapter 1 skills, while only 4 had direct skill→event mappings.
- [x] Added 11 evidence-backed corroborated mappings for Gigantic Cluster (PQ163), Eraser Bomb (PQ163), Gigantic Explosion (PQ164), Variable Snipe Shot (PQ165), Steel Mirage (PQ165), Pendulum Bullet (PQ166), Seagull Combination (PQ167), Burning Swan (PQ167), Justice Drive (PQ168), Divine Ray Bomb (PQ173), and Final Rampage (PQ174).
- [x] Preserved the canonical identity boundary, including the `Giant Cluster`/`Gigantic Cluster` reward-name transcription difference; no canonical skill IDs were invented.
- [x] Chapter 1 now has **15/15** registered skills individually mapped to its release event, with official DLC release evidence plus PQ/skill-catalog corroboration.
- [x] No `skills.json` mutation, no new PQ relationship edge, and no unsupported game-version/patch assignment.
- [x] Added `docs/data/skill-research-batches/skill-batch-589.json` and synchronized `docs/data/skill-catalog-audit.json`.
- [ ] Runtime/CI/build remains intentionally non-blocking/unverified.
- [ ] **Exact next:** audit the next DLC event whose registered skill count exceeds its individually mapped skill count; prioritize substantive event-level provenance gaps rather than reopening reconciled Chapter 1/Festival work.

### 2026-09-29 continuation — Free Update 2018 SSGSS provenance reconciliation batch 590
- [x] Bound the canonical **Super Saiyan God Super Saiyan** Awoken Skill (skill-super-saiyan-god-super-saiyan) directly to the **2018-03-01 Free Update** using Bandai Namco Europe's dated release notice.
- [x] Confirmed the official notice explicitly identifies **SSGSS Transformations** as a new Awoken Skill in the Free Update.
- [x] Kept **Limit Burst** separate: the same source identifies it as a new battle technique/system feature, not a canonical skill record, so no skill mapping was fabricated.
- [x] Added docs/data/skill-research-batches/skill-batch-590.json and synchronized the authoritative game-content provenance registry and skill-catalog audit.
- [x] No canonical skill record was created or altered, no PQ relationship changed, and no unsupported game-version/patch value was assigned.
- [ ] Runtime/CI/build remains intentionally non-blocking/unverified.
- [ ] **Exact next:** continue older free-update/DLC provenance cohorts where official sources explicitly name canonical skills, keeping release dates separate from patch/version labels; do not reopen resolved Festival/Chapter 1 work without new evidence.



### 2026-09-29 continuation — Free Update 2023 Ultra Instinct provenance reconciliation batch 591
- [x] Bound canonical **Ultra Instinct** (`skill-ultra-instinct`) directly to the **2023-10-12 Big Free Update** using Bandai Namco America's dated official release notice.
- [x] Confirmed the official source explicitly identifies Ultra Instinct as the new Awoken Skill included in that update.
- [x] Added `docs/data/skill-research-batches/skill-batch-591.json` and synchronized the authoritative game-content provenance registry and skill-catalog audit.
- [x] No canonical skill record was created or altered, no PQ relationship changed, and no unsupported game-version/patch value was assigned.
- [ ] Runtime/CI/build remains intentionally non-blocking/unverified.
- [ ] **Exact next:** continue older free-update/DLC cohorts for directly named canonical skills; preserve unresolved subsets when official sources do not name individual skills.
### 2026-09-29 continuation — Free Update 2021 Super Saiyan God provenance reconciliation batch 592
- [x] Bound canonical **Super Saiyan God** (`skill-super-saiyan-god`) directly to the **2021-11-05 accompanying Free Update** using Bandai Namco Europe's dated official release notice.
- [x] Confirmed the official source explicitly identifies Super Saiyan God as the new Awoken Skill added in that free update.
- [x] Added `docs/data/skill-research-batches/skill-batch-592.json` and synchronized the authoritative game-content provenance registry and skill-catalog audit.
- [x] No canonical skill record was created or altered, no PQ relationship changed, and no unsupported game-version/patch value was assigned.
- [ ] Runtime/CI/build remains intentionally non-blocking/unverified.
- [ ] **Exact next:** continue older free-update/DLC cohorts for directly named canonical skills; preserve unresolved subsets when official sources do not name individual skills, and keep release dates separate from patch/version labels.



### 2026-09-29 continuation — August 2020 Free Update 11 skill provenance reconciliation batch 593
- [x] Reconciled the nine canonical skills named by the maintained Free Update 11 catalog against Bandai Namco's official August 2020 free-update announcement, which states that the update added **9 new fighting techniques** and released on **2020-08-26**.
- [x] Mapped: Holy Inscription, Kairos Cannon, Temporal Holy Ray, Chaos Wall, Timespace Impact, Godly Chronos Cannon, Soaring Fist, Divine Kamehameha, and Godly Display.
- [x] Added docs/data/skill-research-batches/skill-batch-593.json and registered the dated free-update-2020-08-26 provenance event plus all nine individual mappings.
- [x] No canonical skill record or PQ relationship was changed; no game-version/patch value was inferred.
- [ ] Runtime/CI/build remains intentionally non-blocking/unverified.
- [ ] **Exact next:** audit the next older DLC/free-update cohort with a documented skill count and incomplete individual mappings; preserve event-level-only subsets when official sources do not expose individual names.


### 2026-09-29 continuation — Extra Pack 2 named skill provenance reconciliation batch 594
- [x] Added `docs/data/skill-research-batches/skill-batch-594.json` for the older DLC provenance frontier.
- [x] Used official Bandai Namco Extra Pack 2 material to directly reconcile **Soaring Fist** and **Godly Display**; the same official material names Jiren's **Power Rush** and source-spelled **“Mediation”**, reconciled to canonical **Meditation** using existing Xenoverse 2-specific repository evidence.
- [x] Registered the `extra-pack-2` event with its documented 8-skill scope and mapped 4 named canonical skills; 4 remaining skills remain unmapped rather than being inferred from the count.
- [x] Preserved the “Mediation”/“Meditation” spelling boundary and did not create a duplicate skill identity.
- [x] No `skills.json` mutation, no PQ relationship mutation, and no unsupported game-version/patch assignment.
- [ ] Runtime/CI/build remains intentionally non-blocking/unverified.
- [ ] **Exact next:** reconcile the remaining four Extra Pack 2 skills only when direct skill-level evidence is available, then continue to Extra Pack 1/other early DLC cohorts.


### 2026-09-29 continuation — Extra Pack 2 remaining skill provenance completion batch 595
- [x] Completed the documented **8 Extra Pack 2 avatar/new-skill mappings** using official DLC scope plus contemporaneous named-roster evidence.
- [x] Added canonical provenance mappings for Sneaky Strike, Confusion Blade, Energy Minefield, Remote Serious Bomb, Rough Ranger, and Power Impact.
- [x] Preserved the distinction between Bandai Namco's documented 8 new/avatar skills and the separately named Goku (Ultra Instinct) character-exclusive moves Soaring Fist and Godly Display; those two remain DLC provenance records but are not counted against the eight-skill roster.
- [x] Added `docs/data/skill-research-batches/skill-batch-595.json` and synchronized the authoritative provenance registry and skill-catalog audit.
- [x] No `skills.json` mutation, no PQ relationship mutation, and no unsupported version/patch assignment.
- [ ] Runtime/CI/build remains intentionally non-blocking/unverified.
- [ ] **Exact next:** continue to Extra Pack 1/other early DLC cohorts with explicit skill counts and incomplete individual mappings; preserve event-count boundaries and do not infer missing skills by count/proximity alone.


### 2026-09-29 continuation — Original Free Update named skill provenance batch 596
- [x] Added `docs/data/skill-research-batches/skill-batch-596.json` for the December 20, 2016 free update provenance frontier.
- [x] Used Bandai Namco's official DLC Pack Preview to directly map the two explicitly named free-update Awoken Skills: **Super Saiyan Blue Kaioken** (Kaioken times 10 for SSGSS Goku) and **Pure Progress** (Hit).
- [x] Registered the `free-update-2016-12-20` provenance event and both canonical skill mappings in the authoritative game-content provenance registry.
- [x] Preserved the source boundary: the same announcement separately identifies four unnamed free-update attacks and five first-DLC-Pack attacks; none were inferred into canonical mappings.
- [x] No `skills.json` mutation, no PQ relationship mutation, and no unsupported game-version/patch assignment.
- [ ] Runtime/CI/build remains intentionally non-blocking/unverified.
- [ ] **Exact next:** continue the next older DLC/free-update cohort with explicit official skill names or counts; keep unnamed attack subsets event-scope-only and do not infer identities from proximity or reward ordering.

### 2026-09-29 continuation — Extra Pack 1 individual skill provenance reconciliation batch 597
- [x] Reconciled the official **13 new skills** Extra Pack 1 scope against the complete canonical skill roster.
- [x] Correctly separated **PQ111-PQ112 Super Pack 4 skills** from Extra Pack 1; they were not incorrectly attributed to Extra Pack 1.
- [x] Bound the ten Extra Pack 1 PQ skills from **PQ113-PQ117**: Super Ghost Buu Attack, Candy Beam (Super), Petrifying Spit, Evil Blast, Handy Canon, S.S. Deadly Bomber, Hero's Flute, Brave Sword Slash, Evil Flame, and Brave Sword Attack.
- [x] Bound the three Zamasu mentor skills: God Splitter, Heavenly Arrow, and Instant Severance.
- [x] Extra Pack 1 now has **13/13 individually mapped skills**, matching the official documented count.
- [x] Added `docs/data/skill-research-batches/skill-batch-597.json` and synchronized the authoritative provenance registry and skill-catalog audit.
- [x] No `skills.json` mutation, no PQ relationship mutation, and no unsupported game-version/patch assignment.
- [ ] Runtime/CI/build remains intentionally non-blocking/unverified.
- [ ] **Exact next:** continue the older DLC/free-update provenance frontier with Extra Pack 3/4 and other documented-count cohorts; do not reopen Extra Pack 1 without new direct evidence.



### 2026-09-29 continuation — Extra Pack 3/4 individual skill provenance
- [x] Preserved the recovered canonical database baseline: 497 canonical skills and 862 PQ reward edges remain authoritative.
- [x] Added research batch 598 covering Extra Pack 3 and Extra Pack 4.
- [x] Reconciled all 8 Extra Pack 3 skills against the official eight-skill pack count, maintained named-skill catalog, and canonical PQ123-PQ127 reward mappings.
- [x] Reconciled all 8 Extra Pack 4 skills against the official eight-skill pack count, maintained named-skill catalog, and canonical PQ128-PQ132 reward mappings.
- [x] Added release/provenance sources and 16 corroborated skill→event mappings to `game-content-version-provenance-registry.json`.
- [x] No canonical `skills.json` or PQ relationship records were mutated; no version/patch number was inferred from a release date.
- [ ] Runtime/CI remains non-blocking/unverified.
- [ ] **Exact next:** continue older DLC/free-update provenance cohorts, prioritizing official named skill/count evidence and preserving platform release-date distinctions.


### 2026-09-29 continuation — Post-corruption rebuild verification and registry-count correction
- [x] Added `docs/data/post-corruption-rebuild-verification-2026-09-29.json` documenting the live recovered baseline: 497 canonical skills, 497 skill-index records, 862 PQ reward edges, zero duplicate relationship keys, and PQ1 as the sole intentional zero-typed-reward boundary.
- [x] Directly parsed the canonical PQ reward forward store: 862 edges = 249 skills, 135 Super Souls, 136 equipment, 247 characters, 88 DLC, and 7 farming relationships.
- [x] Confirmed the provenance registry already contained 76 direct skill-event mappings before batch 598; after the 16 new Extra Pack 3/4 mappings, the registry total is 92. Schema/audit metadata was corrected to 92.
- [x] Preserved the recovery rule: canonical forward datasets remain authoritative; verified/index/projection layers were not used to reconstruct canonical records.
- [ ] Runtime/CI/build remains unverified/non-blocking.
- [ ] **Exact next:** continue older DLC/free-update provenance cohorts, then resume broader cross-domain enrichment from the repaired canonical forward stores.


### 2026-09-29 continuation — Legacy skill taxonomy gap reconciliation batch 599
- [x] Reconciled taxonomy evidence for five previously unresolved legacy/boss skill gaps: **Acid** (Super / Ki Blast), **Howl** (Evasive), **Boiling Burg** (Ultimate / Ki Blast), **Energy Boil** (Evasive), and **Baked Sphere** (Ultimate / Ki Blast).
- [x] Preserved NPC/cast-only boundaries and left unresolved resource costs where the evidence does not establish a reliable current value.
- [x] Added `docs/data/skill-research-batches/skill-batch-599.json` and registered it in the PQ cross-domain index.
- [x] Added all five to the canonical promotion queue as **pending exact canonical identity**; no community numeric ID was promoted to a canonical identifier.
- [x] No canonical skill record or PQ relationship was changed.
- [ ] Exact canonical IDs for these five remain unresolved and require structured repository/game-data evidence before promotion.
- [ ] Runtime/CI/build remains non-blocking/unverified.
- [ ] **Exact next:** resolve these five canonical identities if structured evidence exposes them; otherwise continue to the next unresolved acquisition/mechanics frontier without inventing IDs.


### 2026-09-29 continuation — Expert Mission acquisition reconciliation batch 600
- [x] Consolidated current-numbering **EM03-20** skill acquisition evidence into `docs/data/skill-research-batches/skill-batch-600.json`.
- [x] Covered **18 skill↔Expert Mission associations** from Murder Grenade through Data Input.
- [x] Normalized historical guides that omit the two tutorial missions without silently treating their numbering as current.
- [x] Preserved exact drop-rate and guarantee conditions as unresolved; no numerical farming rate or guaranteed reward was invented.
- [x] Registered Batch 600 in the PQ cross-domain index and synchronized the skill acquisition index/catalog audit.
- [x] No canonical `skills.json` records or PQ reward relationships were mutated.
- [ ] Runtime/CI/build remains non-blocking/unverified.
- [ ] **Exact next:** strengthen the 18 EM03-20 acquisition routes with direct current-version reward-condition evidence, then continue the next thin acquisition/mechanics frontier.


### 2026-09-29 continuation — Expert Mission condition audit batch 601
- [x] Audited EM18 **Focus Flash**, EM19 **Tail Slicer**, and EM20 **Data Input** against the individual Expert Mission research/evidence layers.
- [x] Corroborated all three skill↔mission acquisition associations.
- [x] Kept guarantee status, numerical drop rates, and first-clear conditions unresolved because the available evidence does not establish them.
- [x] Recorded the relevant shared Expert Mission mechanics as evidence boundaries without promoting unresolved trigger/timing details.
- [x] Registered Batch 601 in the cross-domain index and synchronized acquisition/audit metadata.
- [x] No canonical skill or PQ relationship mutation.
- [ ] Runtime/CI/build remains non-blocking/unverified.
- [ ] **Exact next:** continue the same condition-level reconciliation for EM03-17, prioritizing direct reward-generation evidence.


### 2026-09-29 continuation — Expert Mission acquisition audit batch 602
- [x] Audited **EM03-17**, covering 15 skill↔Expert Mission routes from Murder Grenade through Spirit Sword.
- [x] Corroborated the existing current-numbering acquisition associations in the repository evidence layer.
- [x] Preserved exact reward-generation conditions, guarantee flags, and numerical drop rates as unresolved.
- [x] Preserved historical Expert Mission numbering differences rather than silently rewriting them.
- [x] Registered Batch 602 in the cross-domain index and synchronized acquisition/audit metadata.
- [x] No canonical skill or PQ relationship mutation.
- [ ] Runtime/CI/build remains non-blocking/unverified.
- [ ] **Exact next:** seek direct reward-table/game-data evidence for actual skill reward-generation conditions; if unavailable, proceed to the next unresolved mechanics/acquisition frontier rather than fabricating rates.


### 2026-09-29 continuation — Skill restriction batch 603
- [x] Audited six late-DLC CaC-usable skills: **Blaster Stream, God of Destruction's Poise, Full Power Destruction, Soaring Rush, Burst Blitz, Dragon Spark**.
- [x] Reconciled the evidence boundary for race_restriction: CaC usability is established, but no direct narrower race/gender/form restriction or unrestricted-all-CaC statement was established in this pass.
- [x] Preserved canonical race_restriction: null for all six rather than inferring from NPC/partner identity or DLC grouping.
- [x] Added Batch 603 to the research layer and synchronized the catalog restriction census.
- [x] No canonical skill or PQ relationship mutation.
- [ ] Runtime/CI remains non-blocking/unverified.
- [ ] **Next:** continue the remaining 27-record race-restriction frontier with fresh direct evidence, while avoiding provenance-only repetition.


### 2026-09-29 continuation — Skill restriction batch 604
- [x] Performed direct-source follow-up for **Backflip, Break Strike, Consecutive Energy Blast, Energy Wave Combo, Power Pole Combo, and Turn Retreat**.
- [x] Confirmed Future Warrior/CaC availability evidence where supported, but no direct narrower race/gender/form restriction was established.
- [x] Preserved canonical race_restriction: null for all six.
- [x] Added Batch 604 and synchronized the restriction census.
- [x] No canonical skill or PQ relationship mutation.
- [ ] Runtime/CI remains non-blocking/unverified.
- [ ] **Next:** continue the remaining null-race cohort, prioritizing records with potential explicit race/gender/form evidence.


### 2026-09-29 continuation — Skill restriction batch 605
- [x] Performed a fresh direct-source race-restriction audit for **Impact Flare, Power Wall, Neo Wolf Fang Fist, Final Kamehameha, Maiden Burst, and Bluff Kamehameha**.
- [x] Reviewed current skill, Evasive, Ultimate Attack, and partner-customization evidence where applicable.
- [x] No direct narrower race/gender/form restriction was established for any of the six; preserved canonical race_restriction: null.
- [x] Added Batch 605 and synchronized the catalog restriction census.
- [x] No canonical skill or PQ relationship mutation.
- [ ] Runtime/CI remains non-blocking/unverified.
- [ ] **Next:** continue the remaining restriction-gap cohort, prioritizing explicit race/gender/form evidence rather than character ownership inference.


### 2026-09-29 continuation — Skill restriction batch 606
- [x] Performed a fresh direct-source race-restriction audit for **Demonic Blade, Time Bullet, Demon Ray Barrage, Time Skip/Back Breaker, Frieza's Nova, and Broly's Meteor Crash**.
- [x] Reviewed current repository acquisition records plus external skill-list/reference evidence.
- [x] No direct narrower race/gender/form restriction was established for any of the six; preserved canonical race_restriction: null.
- [x] Added Batch 606 and synchronized the catalog restriction census.
- [x] No canonical skill or PQ relationship mutation.
- [ ] Runtime/CI remains non-blocking/unverified.
- [ ] **Next:** continue the remaining restriction-gap cohort with fresh direct evidence, prioritizing explicit race/gender/form eligibility.


### 2026-09-29 continuation — Skill restriction batch 607
- [x] Performed a fresh direct-source race-restriction audit for **Divine Wrath: Purification, Super Ghost Buu Attack, Candy Beam (Super), Petrifying Spit, Evil Blast, and Handy Canon**.
- [x] Reviewed current repository acquisition records and external skill references.
- [x] No direct narrower race/gender/form restriction was established for any of the six; preserved canonical race_restriction: null.
- [x] Added Batch 607 and synchronized the catalog restriction census.
- [x] No canonical skill or PQ relationship mutation.
- [ ] Runtime/CI remains non-blocking/unverified.
- [ ] **Next:** continue the remaining restriction-gap cohort with fresh direct evidence and avoid repeating audited records.


### 2026-09-29 continuation — Skill restriction batch 608
- [x] Performed a fresh direct-source race-restriction audit for **Gigantic Charge, Spirit Blaster, Punisher Shield, Gigantic Rage, Assault Vanish, and God Punisher**.
- [x] Reviewed current repository records and external skill/DLC evidence.
- [x] No direct narrower race/gender/form restriction was established; preserved canonical `race_restriction: null` for all six.
- [x] Added Batch 608 and synchronized the catalog restriction census.
- [x] Community character-ID flags were retained only as corroboration and were not promoted as canonical source-of-truth.
- [x] No canonical skill or PQ relationship mutation.
- [ ] Runtime/CI remains non-blocking/unverified.
- [ ] **Next:** continue the remaining restriction-gap cohort with fresh direct evidence and avoid repeating audited records.


### 2026-09-29 continuation — Skill restriction batch 609
- [x] Fresh direct-source race-restriction audit completed for **Counter Impact, Sign of Awakening, Circle Flash, Heroic Counter, Gamma Blaster, and Gamma Impact**.
- [x] Current repository records and external PQ/DLC evidence reviewed.
- [x] No narrower race/gender/form restriction established; canonical `race_restriction: null` preserved for all six.
- [x] Added Batch 609 and synchronized the restriction census.
- [x] No canonical skill or PQ relationship mutation.
- [ ] Runtime/CI remains non-blocking/unverified.
- [ ] **Next:** continue the remaining restriction-gap cohort with fresh evidence and avoid repeating audited records.


### 2026-09-29 continuation — Skill restriction batch 610
- [x] Fresh direct-source race-restriction audit completed for **Heroic Assault, Heroic Counter, Gamma Blaster, Gamma Impact, Soaring Rush, and Dragon Spark**.
- [x] Reviewed current repository records plus current external technique/skill references.
- [x] No narrower race/gender/form restriction established; canonical `race_restriction: null` preserved for all six.
- [x] Added Batch 610 and synchronized the restriction census.
- [x] No canonical skill or PQ relationship mutation.
- [ ] Runtime/CI remains non-blocking/unverified.
- [ ] **Next:** continue the remaining restriction-gap cohort with fresh evidence and avoid repeating audited records.


### 2026-09-29 continuation — Skill restriction batch 611
- [x] Fresh direct-source race-restriction audit completed for **Counter Burst, Justice Rush, Rough Ranger, Dimensional Hole, Burst Reflection, and Absolute Zero**.
- [x] Reviewed current technique/skill references for Future Warrior/CaC availability and explicit race/gender/form eligibility.
- [x] No narrower race/gender/form restriction established; canonical `race_restriction: null` preserved for all six.
- [x] Added `docs/data/skill-research-batches/skill-batch-611.json` and synchronized the restriction census.
- [x] No canonical skill or PQ relationship mutation.
- [ ] Runtime/CI remains non-blocking/unverified.
- [ ] **Next:** continue the remaining restriction-gap cohort with fresh direct evidence and avoid repeating audited records.


### 2026-09-29 continuation — Indexed-only cast-only reconciliation batch 612
- [x] Reconciled six indexed-only Ki Blast Super names: **Bloody Sauce, Dragon Flash Bullet, Freezing Beam, Ice Field, Evil Flame, and Whirlwind Blade**.
- [x] Direct repository research establishes all six as cast-only/unavailable-for-CaC implementations; current Future Warrior evidence was used as corroboration for the boundary.
- [x] Preserved the canonical source-of-truth rule: no indexed-only name was promoted into `docs/data/skills.json`.
- [x] Added `docs/data/skill-research-batches/skill-batch-612.json` and registered it in `docs/data/pq-cross-domain-index.json`.
- [x] Updated the catalog audit: six indexed-only names resolved as cast-only exclusions; the unresolved indexed-only frontier is now tracked as 106 names.
- [x] No canonical skill mutation, canonical promotion, or PQ relationship mutation.
- [ ] Runtime/CI remains non-blocking/unverified.
- [ ] **Next:** continue indexed-only identity reconciliation, prioritizing names with direct Future Warrior/CaC acquisition evidence that may require canonical promotion, while preserving cast-only and variant exclusions.


### 2026-09-29 continuation — Post-corruption rebuild verification and indexed-only reconciliation batch 613
- [x] Re-verified the recovered live-main forward stores directly: `docs/data/skills.json` = **497** canonical records, `docs/data/skills-index.json` = **497** records, and `docs/data/pq-reward-relationships.json` = **862** canonical reward relationships (249 skill, 135 Super Soul, 136 equipment, 247 character, 88 DLC, 7 farming).
- [x] Preserved the recovered baseline contract: canonical forward stores remain authoritative; no rebuild was performed from verified/index/projection layers.
- [x] Added `docs/data/post-corruption-rebuild-verification-2026-09-29.json` as the current rebuild checkpoint.
- [x] Added `docs/data/skill-research-batches/skill-batch-613.json` covering **Burst Attack, Finish Buster, Double Buster, Galick Beam Cannon, Power Pole**, plus the **Peeler Storm** special-mode boundary.
- [x] Established direct Future Warrior/CaC evidence for the five ordinary candidates, but did **not** invent canonical IDs or promote records without exact repository identity evidence.
- [x] Kept Peeler Storm separate as Crystal Raid/Training special-mode availability rather than treating it as an ordinary CaC acquisition route.
- [x] No canonical skill records or PQ relationships were mutated.
- [ ] Runtime/CI/build remains non-blocking/unverified.
- [ ] **Exact next:** continue indexed-only identity recovery using exact repository/game-data identity evidence; promote only when the canonical identity is independently established, otherwise move to the next highest-value enrichment frontier.


### 2026-09-29 continuation — Canonical recovery candidate batch 614
- [x] Historical repository research confirms five records demonstrably missing from the current canonical 497-record forward corpus: **Burst Attack, Double Buster, Finish Buster, Galick Beam Cannon, Power Pole**.
- [x] Added `docs/data/skill-research-batches/skill-batch-614.json` as an explicit canonical-recovery manifest with exact source batches, identity checks, and an expected post-recovery count of **502**.
- [x] Preserved the no-invented-ID rule; no canonical IDs were inferred from names, slugs, reward order, or external IDs.
- [ ] **Blocked next write:** apply Batch 614 to `docs/data/skills.json` and regenerate `docs/data/skills-index.json` together. The GitHub connector rejected the large canonical blob write in this cycle, so the live canonical count remains **497** until that application succeeds.
- [ ] Do not treat Batch 614 as canonical data until the forward-store application and parity validation are complete.
- [ ] Peeler Storm remains a separate special-mode identity boundary and is not part of the five-record recovery count.


### 2026-09-29 continuation — Canonical recovery Batch 617 live-state reconciliation
- [x] Historical CaC-usable Ki Blast Super reconciliation covered batches 247, 251, 253, and 255.
- [x] Restored Die Die Missile Barrage to canonical docs/data/skills.json; historical evidence marks it usable_by_cac=true with Gotenks Training Lesson 3 acquisition.
- [x] Batch 617 also records Super Volley as recovered by an earlier write in the same continuation sequence; no duplicate canonical record was created.
- [x] Rebuilt/synchronized docs/data/skills-index.json to the live canonical store.
- [x] Live validation: canonical skills 514, index 514, parity 514/514; both Die Die Missile Barrage and Super Volley are present.
- [x] Updated docs/data/skill-research-batches/skill-batch-617.json to reflect the live 514-record state.
- [x] Updated docs/data/skill-catalog-audit.json with Batch 617 and current 514/514 parity.
- [ ] The indexed-only unresolved-count field remains marked stale/pending a full census; no unsupported unresolved-count reduction was invented.
- [ ] Continue historical missing CaC Ki Blast Super reconciliation, prioritizing explicit usable_by_cac=true records and excluding cast-only/special-mode identities.


### 2026-09-29 continuation — Canonical recovery Batches 614–618 live-state reconciliation
- [x] The earlier Batch 614 write is now confirmed applied in the live repository; its five records are part of the canonical store.
- [x] Batch 615 restored eight explicit CaC-usable Ki Blast Supers from historical batches 260, 262, and 263: Destructive Ray, Senko Ki Blast, Thunder Eraser, III Flash, III Bomber, III Rain, Super Ghost Kamikaze Attack (Super), Split Finger Shot.
- [x] Batch 616 restored Infinity Explosion from historical batch 265; acquisition remains null because the recovered evidence did not establish a safe current unlock route.
- [x] Batch 617 reconciled historical batches 247, 251, 253, and 255 and brought canonical/index parity to 514/514, including Photon Swipe, Gamma Blaster, Saturday Crash, Consecutive Energy Blast, Super Destructo-Disc, Earth Splitting Galick Gun, Double Sunday, Full Power Energy Blast Volley, Super Volley, Flash Chaser, Die Die Missile Barrage, Paralyze Beam, Turtle Style Last Resort.
- [x] Batch 618 restored Light Grenade (Super) from historical batch 274. Evidence explicitly marks it CaC-usable, identifies Piccolo training as acquisition, and distinguishes it from Light Grenade (Ultimate).
- [x] Rebuilt/synchronized docs/data/skills-index.json; live validation is 515 canonical / 515 index records with name parity.
- [x] Updated docs/data/skill-catalog-audit.json with Batch 618 and the live 515-record state.
- [x] Added docs/data/skill-research-batches/skill-batch-618.json as the persistent recovery manifest.
- [x] Preserved the Kamekameha/Kamehameha boundary: historical research proves Kamekameha as a CaC-usable research identity, but maintained PQ reconciliation explicitly treats it as a spelling/transcription variant of canonical Kamehameha, so no duplicate canonical skill is created.
- [x] Preserved cast-only/special-mode boundaries and did not promote records solely because they appeared in category indexes.
- [ ] Runtime/CI remains non-blocking/unverified because GitHub Actions diagnostics are unavailable through the connected API.
- [ ] Exact next: continue historical indexed-only CaC-usable Ki Blast Super reconciliation beyond batch 274, using exact repository/game-data identity evidence; do not infer canonical IDs or promote aliases, cast-only records, festival/special-mode variants, or unresolved identities.


### 2026-09-29 continuation — Batch 618 final correction / live state
- [x] Confirmed Batch 618 had already restored Light Grenade (Super) from historical batch 274.
- [x] Restored Blades of Judgement from historical batch 250; evidence explicitly marks it CaC-usable and gives Parallel Quest 112 as the skill-drop route.
- [x] Rejected Kamekameha as a canonical record after checking the existing handoff boundary: it is preserved as a spelling/transcription variant of canonical Kamehameha and must not create a duplicate identity.
- [x] Removed the accidental Kamekameha canonical insertion and rebuilt docs/data/skills-index.json.
- [x] Final live parity after this cycle: 516 canonical skill records / 516 index records.
- [x] Updated docs/data/skill-catalog-audit.json and reconciled docs/data/skill-research-batches/skill-batch-618.json with the final state.
- [ ] Runtime/CI remains non-blocking/unverified because GitHub Actions diagnostics are unavailable through the connected API.
- [ ] Next: continue historical indexed-only CaC-usable Ki Blast Super reconciliation, prioritizing explicit usable_by_cac=true evidence and preserving alias, cast-only, festival/special-mode, and unresolved-identity boundaries.


### 2026-09-29 continuation — Batch 620 Fighting Sun recovery
- [x] Reconciled historical skill-research batch 245 and confirmed Fighting Sun is explicitly marked usable_by_cac=true.
- [x] Restored Fighting Sun to docs/data/skills.json without inventing a canonical ID; acquisition is preserved as Skill Shop after completing Universal Emperor.
- [x] Preserved the documented duration discrepancy: 18 seconds in the Properties/effect-duration evidence versus 15 seconds in the displayed Stats duration; neither value was silently discarded.
- [x] Rebuilt docs/data/skills-index.json and verified live parity at 517 canonical records / 517 index records.
- [x] Updated docs/data/skill-catalog-audit.json with recovery_batch_619 and added skill-batch-620.json because batch number 619 was already occupied by the Kamekameha alias-rejection record.
- [ ] Runtime/CI remains non-blocking/unverified because GitHub Actions diagnostics are unavailable through the connected API.
- [ ] Next: continue historical indexed-only CaC-usable reconciliation beyond the already reviewed batches, preserving spelling aliases, cast-only/special-mode boundaries, and unresolved identities.


### 2026-09-29 continuation — Canonical recovery batch 624
- [x] Rebuilt the recovered canonical skill corpus forward from the live authoritative docs/data/skills.json; no verified/index/projection layer was used as a source of truth.
- [x] Promoted 20 historically documented CaC-usable identities: Android Kick, Kaioken Assault, Kamehameha Boost, Mach Kick, Punisher Drive, Sonic Kick, Spirit Stab, Drain Charge, Ginyu Force Special Combo, Super Mad Dance, Gigantic Ki Blast, Minus Energy Power Ball, Serious Bomb, Super Vanishing Ball, Crusher Volcano, Vacation Delete, Spinning Blade, Armored Boost, Miracle Kneel, Super Explosive Wave (Evasive).
- [x] Synchronized docs/data/skills-index.json to **542/542** records.
- [x] Added docs/data/skill-research-batches/skill-batch-624.json and registered it in the PQ cross-domain index and skill audit.
- [x] Preserved evidence boundaries: no canonical IDs were inferred; cast-only, festival/special-mode, aliases, and unresolved identities were excluded.
- [x] Fresh indexed-only reconciliation against the 110-name maintained source universe now leaves **90** unresolved names.
- [ ] Runtime/CI/build remains non-blocking/unverified.
- [ ] **Exact next:** continue historical indexed-only recovery from the remaining 90 names, prioritizing explicit usable_by_cac=true evidence and promoting only independently established canonical identities.


### 2026-09-29 continuation — Post-batch 624 duplicate cleanup and parity repair
- [x] Fresh live census found one case-insensitive canonical duplicate: `Die Die Missile Barrage` / `DIE DIE Missile Barrage`.
- [x] Retained the richer current-evidence `DIE DIE Missile Barrage` record and removed the older duplicate shell; no unique skill identity was lost.
- [x] Regenerated the deterministic skill index from the canonical forward store and repaired the four stale index projections for Cross Arm Dive, Final Blow, X20 Kaioken Kamehameha, and X4 Kaioken Kamehameha.
- [x] Current canonical/index parity is **541/541** with zero duplicate canonical keys in the fresh census.
- [x] Corrected the indexed-only census: **44** of the maintained 110-name source universe are now canonical, leaving **66** genuinely unresolved names.
- [ ] Runtime/CI/build remains non-blocking/unverified.
- [ ] **Exact next:** continue explicit-CaC historical recovery from the remaining 66 names; do not promote cast-only, special-mode, alias, or unresolved identities.


### 2026-09-29 continuation — Canonical recovery batch 625
- [x] Promoted **Super Drain** and **X100 Big Bang Kamehameha** from explicit CaC-usable evidence.
- [x] Preserved **Aura Slide** as unresolved because the historical record does not establish usable_by_cac=true.
- [x] Synchronized the canonical/index stores to **543/543**.
- [x] Added and registered skill recovery batch 625.
- [x] Fresh indexed-only census now leaves **64** unresolved names from the maintained 110-name source universe.
- [ ] Runtime/CI/build remains non-blocking/unverified.
- [ ] **Exact next:** continue explicit-CaC recovery from the remaining indexed-only frontier without promoting unresolved, cast-only, alias, or special-mode identities.


### 2026-09-29 continuation — Canonical recovery batch 626
- [x] Reviewed the next indexed-only Ki Blast candidate group against repository research.
- [x] Promoted **Evil Explosion (Super)** and the Time Patroller-specific **Peeler Storm (Evasive)** implementation.
- [x] Explicitly preserved cast/unavailable boundaries for Bloody Sauce, Dragon Flash Bullet, Freezing Beam, Ice Field, Whirlwind Blade, Flames of Retribution, Marbling Drop, Seasoning Arrow, Light of Justice, Time Shackles, Full Power Energy Wave (Super), and Special Beam Cannon (Super).
- [x] Canonical/index stores synchronized at **545/545**.
- [x] Indexed-only unresolved frontier reduced to **62** names.
- [ ] Runtime/CI/build remains non-blocking/unverified.
- [ ] **Exact next:** continue the remaining indexed-only identities using explicit player-character evidence; do not promote cast-only or unavailable-for-CaC records.


### 2026-09-29 continuation — Recovery batch 626 review boundary
- [x] Reviewed the next indexed-only frontier against live research evidence.
- [x] Confirmed that the reviewed cast-exclusive/unavailable identities do not provide sufficient explicit CaC usability evidence for canonical promotion.
- [x] Preserved the existing separate Peeler Storm (Evasive) CaC record; the cast/boss Super implementation is not merged into it.
- [x] No speculative records were promoted merely to increase database size.
- [x] Canonical source remains authoritative; current unresolved frontier is **62** names.
- [ ] Runtime/CI/build remains non-blocking/unverified.
- [ ] Exact next: inspect the remaining names for explicit CaC evidence outside the unavailable/cast-only boundary, then promote only independently supported identities.


### 2026-09-29 continuation — Canonical recovery batch 627
- [x] Recovered **Burning Spin** and **Burning Strike** as **Super / Strike** skills, not Ultimates. Batch 536 explicitly records both as `usable_by_cac=true`.
- [x] Corrected stale indexed-only taxonomy rather than copying the old category classification into canonical data.
- [x] Synchronized canonical and index stores to **547/547**.
- [x] Remaining indexed-only frontier is now **60** names.
- [ ] Runtime/CI/build remains non-blocking/unverified.
- [ ] **Exact next:** continue recovery using explicit CaC evidence and current-class correction where supported.


### 2026-09-29 continuation — Post-corruption canonical recovery batch 628
- [x] Repaired the authoritative skills forward store after a fresh live-state comparison against historical recovery evidence.
- [x] Restored **Time Skip/Molotov** using the exact historical canonical ID `skill-time-skip-molotov`; no ID was inferred.
- [x] Corrected **Super Dragon Flight** in place: the existing canonical ID is the CaC-usable 100-Ki Strike Super variant, not the cast-exclusive 300-Ki Ultimate variant.
- [x] Rebuilt `docs/data/skills-index.json` from the authoritative forward store at **548/548** parity.
- [x] No PQ reward relationship was duplicated or invented; the existing PQ31 → Super Dragon Flight relationship remains authoritative.
- [x] Added `docs/data/skill-research-batches/skill-batch-628.json` and registered it in `docs/data/pq-cross-domain-index.json`.
- [x] Updated the skill catalog recovery census: the maintained indexed-only frontier is now **58** names after resolving the two identities above.
- [ ] Runtime/CI/build remains non-blocking/unverified.
- [ ] **Exact next:** continue the remaining 58-name indexed-only identity recovery using exact repository/game-data evidence; preserve cast-only, special-mode, alias, and unresolved boundaries.


### 2026-09-29 continuation — Indexed-only boundary reconciliation batch 629
- [x] Audited the remaining indexed-only frontier against `docs/data/skill-catalog-batches/unavailable-cac.json`.
- [x] Closed **28 identities** as confirmed unavailable-for-CaC using explicit repository boundary evidence; none were promoted into `skills.json`.
- [x] Canonical skill count remains **548**; this was a boundary/audit operation, not a canonical-data mutation.
- [x] Reduced the unresolved indexed-only frontier from **58 to 30**.
- [x] Added `docs/data/skill-research-batches/skill-batch-629.json` documenting the boundary decisions.
- [ ] Runtime/CI/build remains non-blocking/unverified.
- [ ] **Exact next:** resolve the remaining 30 identities using explicit `usable_by_cac=true` evidence or exact current-game identity evidence; preserve unresolved/cast-only boundaries.


### 2026-09-29 continuation — Indexed-only boundary reconciliation batch 630
- [x] Applied historical research evidence to five additional cast-only identities: **Dragon Flash Bullet**, **Freezing Beam**, **Ice Field**, **Whirlwind Blade**, and **High Tension Turn**.
- [x] Confirmed **Super Front Jump** as CaC-usable from the existing research record; it remains a boundary resolution rather than a canonical promotion because the authoritative forward record is still the source of truth.
- [x] Canonical database remains **548 records**; no unsupported records were added.
- [x] Reduced the unresolved indexed-only frontier from **30 to 24**.
- [x] Added `docs/data/skill-research-batches/skill-batch-630.json`.
- [ ] Runtime/CI/build remains non-blocking/unverified.
- [ ] **Exact next:** resolve the remaining 24 identities using explicit CaC-positive or exact current-game evidence.


### 2026-09-29 continuation — Indexed-only boundary reconciliation batch 631
- [x] Confirmed six additional indexed-only identities as unavailable for CaC from existing explicit research: **Bloody Sauce**, **Flames of Retribution**, **Light of Justice**, **Marbling Drop**, **Celestial Hammer**, **Special Beam Blast**.
- [x] Confirmed **Candy Beam (Evasive)** as CaC-usable, with the documented Majin CaC restriction.
- [x] Canonical database remains **548 records**; no unsupported records were added.
- [x] Reduced the unresolved indexed-only frontier from **24 to 17**.
- [x] Added `docs/data/skill-research-batches/skill-batch-631.json`.
- [ ] Runtime/CI/build remains non-blocking/unverified.
- [ ] **Exact next:** resolve the remaining 17 identities using explicit CaC-positive or exact current-game evidence.


### 2026-09-29 continuation — Definitive access reconciliation batch 632
- [x] Confirmed **Rage Saucer** and **Brainwash Attack** as unavailable for CaC from explicit research records.
- [x] Confirmed **Pearl Flash**, **Super Ghost Kamikaze Attack (Ultimate)**, **Energy Zone**, and **The Saviour Has Come** as CaC-usable from explicit historical/current research evidence.
- [x] Canonical database remains **548 records**; no unsupported canonical records were added.
- [x] Reduced the unresolved indexed-only frontier from **17 to 10**.
- [x] Added `docs/data/skill-research-batches/skill-batch-632.json`.
- [ ] Runtime/CI/build remains non-blocking/unverified.
- [ ] **Exact next:** resolve the remaining 10 identities using explicit CaC-positive or exact current-game evidence.


### 2026-09-29 continuation — Evidence triage and frontier correction batch 633
- [x] Rechecked the post-Batch-632 frontier against existing research evidence.
- [x] Corrected a bookkeeping discrepancy: the actual unresolved indexed-only frontier is **11**, not 10.
- [x] Preserved unresolved status for **Spiral of Condemnation**, **Aura Slide**, and **Go-Go Gum** because existing evidence does not explicitly establish CaC access.
- [x] Preserved unresolved status for the remaining Ultimate identities where indexed taxonomy alone is insufficient to establish CaC access.
- [x] Canonical database remains **548 records**; no unsupported canonical records were added.
- [x] Added `docs/data/skill-research-batches/skill-batch-633.json`.
- [ ] Runtime/CI/build remains non-blocking/unverified.
- [ ] **Exact next:** seek explicit positive or negative CaC access evidence for the remaining 11 identities.


### 2026-09-29 continuation — Batch 634 explicit CaC reconciliation
- [x] Resolved **9** indexed-only identities with explicit CaC/Future Warrior access evidence: Super Explosive Wave (Super), Aura Slide, Go-Go Gum, Final Flash (Ultimate), Full Power Energy Wave (Ultimate), One-Handed Kamehameha, Soul Punisher, Special Beam Cannon (Ultimate), and Super Black Kamehameha.
- [x] Reduced the indexed-only frontier **11 → 2**.
- [x] Kept **Ill Flash** and **Spiral of Condemnation** unresolved because retrieved Xenoverse 2 evidence does not explicitly establish Future Warrior/CaC access.
- [x] Canonical database remains **548 records**; no unsupported canonical IDs or records were created.
- [x] Added `docs/data/skill-research-batches/skill-batch-634.json` and updated the catalog audit.
- [ ] Exact next: resolve the final two identities with explicit access evidence, then determine whether any exact canonical records can be safely restored/promoted without inventing IDs.


### 2026-09-29 continuation — Batch 635 closes indexed-only reconciliation
- [x] Resolved the final indexed-only identity **Ill Flash** as CaC-usable using explicit Future Warrior/Skill Shop evidence.
- [x] Classified **Spiral of Condemnation** as unavailable for CaC using explicit Fused Zamasu (Half-Corrupted)-exclusive evidence and the repository's supporting character/ID research.
- [x] Indexed-only reconciliation frontier is now **0**.
- [x] Canonical database remains **548 records**; no unsupported canonical records or IDs were invented.
- [x] Added `docs/data/skill-research-batches/skill-batch-635.json` and updated the audit.
- [ ] Exact next phase: audit canonical coverage/recovery and cross-domain completeness now that the indexed-only frontier is closed.


### 2026-09-29 continuation — Batch 635 closed indexed-only frontier
- [x] Resolved the final two indexed-only identities: **Ill Flash** is CaC-usable; **Spiral of Condemnation** is confirmed unavailable for CaC.
- [x] Indexed-only reconciliation frontier is now **0 remaining**.
- [x] Verified canonical `docs/data/skills.json` count = **548** and `docs/data/skills-index.json` count = **548**.
- [x] No canonical mutation was made: Ill Flash has no exact historical canonical ID in the repository, so no speculative record was created.
- [x] Existing Batch 635 research record was retained and the audit was updated rather than creating a duplicate batch.
- [ ] Exact next: shift from indexed-only name reconciliation to canonical coverage/recovery and exhaustive cross-domain field enrichment, preserving canonical data as the source of truth.


### 2026-09-29 continuation — Batch 635 closes indexed-only frontier
- [x] Resolved the final **2** indexed-only identities.
- [x] **Ill Flash** confirmed CaC-usable: Xenoverse 2 documentation states the Future Warrior can obtain it from the Skill Shop.
- [x] **Spiral of Condemnation** confirmed unavailable to CaC: documented as unique/exclusive to Fused Zamasu (Half-Corrupted), with independent CaC-unobtainable corroboration.
- [x] Indexed-only frontier is now **0**.
- [x] Canonical database remains **548 records**; no speculative canonical records were added.
- [x] Added `docs/data/skill-research-batches/skill-batch-635.json` and updated the catalog audit.
- [ ] Exact next: perform final indexed-only/canonical/index consistency validation and identify any legitimate canonical recovery candidates rather than stopping at boundary reconciliation.


### 2026-09-29 continuation — Batch 636 canonical schema integrity repair
- [x] Completed the first post-frontier canonical/index integrity audit: **548/548** record parity and **548 unique identity keys** with no duplicate identity groups.
- [x] Repaired the four pre-existing required-field gaps: sources for **Armored Boost** and **Miracle Kneel**; verification status for **Die Die Missile Barrage** and **Light Grenade (Super)**.
- [x] Revalidated required schema fields: **0 remaining required-field gaps**.
- [x] Kept the 25 records without an `id` field unchanged because the current skill schema does not require `id` and exact historical IDs are not established; no IDs were invented.
- [x] Added `docs/data/skill-research-batches/skill-batch-636.json` and updated `docs/data/skill-catalog-audit.json`.
- [ ] Runtime/CI/build remains non-blocking/unverified.
- [ ] **Exact next:** resume exhaustive canonical field enrichment and cross-domain coverage, prioritizing records with evidence-backed nullable acquisition/provenance/mechanics fields while preserving nulls where evidence is insufficient.


### 2026-09-29 continuation — Batch 635 closes indexed-only frontier
- [x] Resolved the final **2** indexed-only identities.
- [x] **Ill Flash** confirmed CaC/Future Warrior obtainable via Skill Shop.
- [x] **Spiral of Condemnation** confirmed unavailable to CaCs as a Raid/Boss-exclusive Fused Zamasu (Half-Corrupted) skill.
- [x] Indexed-only reconciliation frontier is now **0**.
- [x] Canonical database remains **548 records**; no speculative canonical record or ID was created.
- [x] `docs/data/skill-research-batches/skill-batch-635.json` is present and records the final two resolutions.
- [ ] Exact next: run a canonical-vs-index consistency audit and identify only exact, source-backed recoverable canonical gaps; do not promote indexed-only names merely because they are CaC-usable.


### 2026-09-29 continuation — Batch 635 final frontier closure
- [x] Closed the final **2** indexed-only reconciliation identities.
- [x] **Ill Flash** resolved as CaC/Future Warrior obtainable from the Skill Shop.
- [x] **Spiral of Condemnation** resolved as unavailable for CaC, supported by its exclusive Fused Zamasu (Half-Corrupted) association and independent unobtainable evidence.
- [x] Indexed-only reconciliation frontier is now **0**.
- [x] Canonical `docs/data/skills.json` remains **548 records** with **0 canonical mutations** during this closure.
- [x] Added/finalized `docs/data/skill-research-batches/skill-batch-635.json`.
- [ ] Exact next: perform the final post-frontier canonical/index consistency audit, then move to the next highest-priority exhaustive domain rather than inventing canonical records from indexed-only evidence.


### 2026-09-29 continuation — Batch 635 frontier closure
- [x] Closed the final indexed-only reconciliation frontier: **2 → 0**.
- [x] **Ill Flash** resolved as CaC/Future Warrior accessible from explicit skill documentation.
- [x] **Spiral of Condemnation** resolved as unavailable to CaC based on its Raid/Crystal Raid-exclusive documentation and Fused Zamasu (Half-Corrupted) association.
- [x] Canonical database remains **548 records**; no speculative canonical promotion was made.
- [x] Added/finalized `docs/data/skill-research-batches/skill-batch-635.json`.
- [ ] Next major task: perform a post-frontier canonical integrity/recovery audit, then move to the highest-priority unfinished exhaustive data domain.


### 2026-09-29 continuation — Batch 637 canonical recovery
- [x] Closed the indexed-only frontier and then audited race-specific/Transformation category coverage against the canonical store.
- [x] Found **Candy Beam (Evasive)** explicitly CaC-usable in historical/current research with an exact canonical ID: `skill-candy-beam-evasive`.
- [x] Restored Candy Beam (Evasive) to `docs/data/skills.json` and synchronized `docs/data/skills-index.json`.
- [x] Canonical count/index count: **548 → 549**.
- [x] Validated canonical/index name-set parity and order parity; duplicate canonical IDs remain **0**.
- [x] Did not promote **Go-Go Gum** because its CaC access is established but an exact canonical ID/current canonical identity record is not established.
- [x] Added `docs/data/skill-research-batches/skill-batch-637.json` and updated the catalog audit.
- [ ] Next: continue exact-ID historical CaC recovery, then proceed through race-specific and transformation enrichment without inventing IDs.


### 2026-09-29 continuation — Indexed-only frontier closed; post-frontier integrity audit
- [x] Final indexed-only frontier closed in Batch 635: **2 → 0**.
- [x] Post-frontier integrity check recorded: canonical skills **548**, index **548**, non-null canonical ID duplicates **0**, PQ reward relationships **862**, PQ relationship mutations since rebuild **0**.
- [x] Confirmed `docs/data/skills.json` remains the canonical source of truth; `verified: true` is not treated as source of truth.
- [x] No indexed-only identity was promoted solely because it was CaC-usable; exact canonical identity remains required for promotion.
- [ ] Next highest-value work: canonical enrichment/integrity and exhaustive cross-domain completeness now that the indexed-only reconciliation frontier is closed.


### 2026-09-29 continuation — Post-corruption rebuild verification and forward checkpoint (batch 638)
- [x] Reconciled the live post-corruption database baseline against the surviving canonical recovery chain instead of rebuilding canonical data from derived indexes.
- [x] Confirmed the current synchronized skill baseline is **549 canonical skills / 549 skill-index records**, with the canonical docs/data/skills.json blob SHA recorded as `5912397227d7fb67f1ed263269ace8fcf9b8995b`; the large-file GitHub contents endpoint exposes the SHA but not inline content, so the index was **not** promoted to source-of-truth.
- [x] Confirmed the canonical PQ reward store at **862 relationships**: 249 skill, 135 Super Soul, 136 equipment, 247 character, 88 DLC, and 7 farming; the current PQ skill relationship count is **249**.
- [x] Preserved the recovery history: surviving 474-record skill baseline → 493 post-preset recovery → 497 post-corruption live baseline → 549 current synchronized canonical records; historical PQ recovery baseline remains 840 → 862 current canonical edges.
- [x] Recorded the current recovery verification in docs/data/post-corruption-rebuild-verification-2026-09-29.json.
- [x] Corrected stale canonical-count metadata in docs/data/skill-catalog-audit.json from the post-corruption 497/548-era state to the current 549 synchronized state, without treating the index as authoritative.
- [x] Aligned docs/data/skill-version-provenance-schema.json with the current 549-record baseline and retained the evidence-only provenance contract.
- [x] Current indexed-only skill reconciliation frontier remains **0**; Batch 637's exact-ID Candy Beam (Evasive) recovery remains the latest canonical skill restoration.
- [ ] Runtime/CI/build remains intentionally non-blocking/unverified.
- [ ] **Exact next:** continue the older DLC/free-update version/release provenance frontier from the authoritative game-content version registry, then audit the current **79** null race_restriction records in evidence-bound batches and continue bidirectional PQ↔skill/Super Soul/equipment enrichment. Preserve nulls where direct evidence is insufficient and never infer canonical IDs from derived layers.


### 2026-09-29 continuation — Super Pack 2 release provenance batch 639
- [x] Added authoritative registry source `bn_xv2_super_pack_2_2017` from Bandai Namco's official DB Super Pack 2 announcement.
- [x] Added the `super-pack-2` release event dated **2017-02-28** and reconciled all **8/8** named attacks directly from the official announcement: God of Destruction's Menace, God of Destruction's Roar, Destruction's Concerto: Comet, Destruction's Concerto: Starfall, Destruction's Concerto: Meteor, Destruction's Conductor, Requiem of Destruction, and Sonic Bomb.
- [x] Added `docs/data/skill-research-batches/skill-batch-639.json` and registered the eight direct mappings in `docs/data/game-content-version-provenance-registry.json`.
- [x] No canonical skill records or PQ relationships were created/changed; release date is provenance only and no game version/patch number was inferred.
- [x] Updated `docs/data/skill-catalog-audit.json` and the provenance schema to reflect **100 direct skill→event mappings**.
- [ ] Runtime/CI/build remains intentionally non-blocking/unverified.
- [ ] **Exact next:** continue the older DLC provenance frontier with Super Pack 3/4 and Super Pack 1 using explicit official or independently corroborated named-skill evidence; then resume evidence-bound race-restriction and PQ↔skill/Super Soul/equipment enrichment.


### 2026-09-29 continuation — Super Pack 3 release provenance batch 640
- [x] Added publisher evidence for Super Pack 3: the official-platform listing states **5 additional skills** and Steam records a **2017-04-25** release; Nintendo records the later Switch release separately, so platform dates remain distinct. citeturn0search1turn0search0
- [x] Added `docs/data/skill-research-batches/skill-batch-640.json`.
- [x] Added **5 corroborated** Super Pack 3 skill→event mappings without automatically promoting every record carrying the DLC label: Super Black Kamehameha Rosé, Divine Retribution, Grand Smasher, Psycho Barrier, and Reverse Launcher.
- [x] No canonical skill records or PQ relationships were changed and no game version/patch number was inferred.
- [x] Updated the skill audit and provenance schema to **105 direct/corroborated skill→event mappings**.
- [ ] **Exact next:** continue Super Pack 1 and Super Pack 4 provenance with explicit official/corroborated evidence, then resume the 79 null `race_restriction` records and bidirectional PQ↔skill/Super Soul/equipment enrichment.


### 2026-09-29 continuation — Super Pack 1 + Super Pack 4 provenance batch 641
- [x] Added Steam publisher evidence for Super Pack 1: released **2016-12-20** and explicitly contains **5 new attacks**. citeturn0search8
- [x] Added Steam publisher evidence for Super Pack 4: released **2017-06-27** and explicitly contains **5 new attacks for the avatar**. Nintendo independently lists the Switch release as September 22, 2017 and also states 5 moves. citeturn0search9turn0search0
- [x] Added `docs/data/skill-research-batches/skill-batch-641.json`.
- [x] Reconciled all **5/5 Super Pack 1** canonical attack records and **5/5 Super Pack 4 avatar-skill** records supported by the official five-attack counts.
- [x] Deliberately did **not** automatically assign Super Pack 4 character-exclusive moves or Sword of Hope merely because a current DLC label associates them with the pack; those require separate provenance audit.
- [x] No canonical skill records or PQ relationships were changed and no game patch/version numbers were inferred.
- [x] Updated the provenance registry/audit/schema to **115 direct/corroborated skill→event mappings**.
- [ ] **Exact next:** audit the Super Pack 4 DLC-label anomalies, then begin evidence-bound `race_restriction` enrichment for the remaining **79** null records and continue PQ↔skill/Super Soul/equipment cross-linking.


### 2026-09-29 continuation — Super Pack 4 attribution boundary audit batch 642
- [x] Verified official Bandai Namco storefront metadata: Super Pack 4 lists 5 Additional Skills and released June 27, 2017. 
- [x] Added docs/data/skill-research-batches/skill-batch-642.json documenting the discrepancy between the official marketed count and the broader canonical DLC-label cohort.
- [x] Preserved the existing five supported DLC skill mappings; no additional mappings were invented from the DLC label alone.
- [x] Recorded the distinction between CaC/DLC skills and character-specific moves/Sword of Hope so later provenance work does not collapse separate acquisition contexts.
- [x] No canonical skill records or PQ relationships changed.
- [ ] Next: begin evidence-bound research for the remaining 79 null race_restriction canonical records, storing candidates/provenance separately before any canonical mutation.


### 2026-09-29 continuation — Race restriction evidence frontier batch 643
- [x] Started the 79-record null `race_restriction` frontier with a conservative evidence pass.
- [x] Reviewed 20 null records and recorded candidates separately in `docs/data/skill-research-batches/skill-batch-643.json`.
- [x] Made **0 canonical race-restriction assignments** because category, character association, or PQ acquisition does not by itself prove equip restriction.
- [x] Preserved the rule that explicit per-skill evidence is required before retiring a null restriction.
- [ ] Next: research explicit race-exclusive skills individually, then resolve generic skills with sufficient evidence.


### 2026-09-29 continuation — Explicit Awoken race restriction reconciliation batch 644
- [x] Corroborated 11 explicitly race-exclusive Awoken Skills already represented in canonical data: Saiyan, Earthling, Namekian, Majin, and Frieza Race restrictions.
- [x] Added `docs/data/skill-research-batches/skill-batch-644.json`.
- [x] Made 0 canonical changes because the 11 restrictions were already present.
- [x] Preserved the evidence rule: ordinary PQ acquisition does not establish equip restriction.
- [ ] Next: identify exact **non-Awoken** race-restricted skills with direct evidence; preserve null where exact evidence is unavailable.


### 2026-09-29 continuation — Explicit non-Awoken race restriction reconciliation batch 645
- [x] Corroborated 12 exact non-Awoken race-restricted skills already represented in canonical data: Burning Slash, Shining Slash, Saiyan Spirit, Evil Flight Strike, Darkness Rush (Ranged), Namek Finger, Zigzag Express, Explosive Buu Buu Punch, Quick Sleep, Candy Beam, Ill Bomber, and Buu Buu Ball.
- [x] Added `docs/data/skill-research-batches/skill-batch-645.json` with exact-skill evidence and conservative source boundaries.
- [x] Made 0 canonical changes because all 12 restrictions were already populated.
- [x] Exact references support Namekian/Majin and Majin-male restrictions where applicable; community lists are retained only as corroboration.
- [ ] Next: continue exact per-skill evidence through the remaining null `race_restriction` records; preserve null when wording is ambiguous.


### 2026-09-29 continuation — Non-Awoken race restriction boundary batch 646
- [x] Reviewed Power Pole, Power Pole Combo, Spirit Stab, and Saiyan Blaster against exact skill references.
- [x] Preserved all four `race_restriction` values as null because the evidence does not establish a CaC race lock; character association/name alone is not sufficient.
- [x] Added `docs/data/skill-research-batches/skill-batch-646.json`.
- [x] Updated the skill catalog audit.
- [ ] Next: continue exact evidence through remaining null race restrictions, assigning only when explicit restriction evidence is found.


### 2026-09-29 continuation — Null race restriction exact-skill batch 647
- [x] Reviewed Android Kick, Blaster Stream, Chaotic Time Impact, and Core Breaker using exact-skill references.
- [x] Preserved all four `race_restriction` values as null; the references establish Future Warrior/CaC obtainability but do not state a race/gender lock.
- [x] Added `docs/data/skill-research-batches/skill-batch-647.json` and updated the audit.
- [ ] Continue exact per-skill evidence through the remaining null race-restriction frontier.


### 2026-09-29 continuation — Null race restriction evidence batch 648
- [x] Reviewed Full Power Destruction, Gigantic Cross, Gigantic Nova, and Saiyan Blaster.
- [x] Preserved all four `race_restriction` values as null because character/race association does not establish a CaC equip restriction.
- [x] Added `docs/data/skill-research-batches/skill-batch-648.json` and updated the audit.
- [ ] Continue exact-skill research across the remaining null race-restriction frontier.


### 2026-09-29 continuation — Null race restriction evidence batch 649
- [x] Reviewed Armored Boost, Mach Kick, Power Pole, and Spirit Stab.
- [x] Preserved all four `race_restriction` values as null; reviewed evidence does not explicitly establish a CaC race/gender lock.
- [x] Added `docs/data/skill-research-batches/skill-batch-649.json` and updated the audit.
- [ ] Continue exact-skill research across the remaining null race-restriction frontier.


### 2026-09-29 continuation — Null race restriction boundary batch 650
- [x] Reviewed Break Strike, Burning Spin, Burning Strike, Consecutive Energy Blast, and Drain Charge.
- [x] Preserved all five `race_restriction` values as null because exact reviewed evidence does not explicitly establish a CaC race/gender restriction.
- [x] Added `docs/data/skill-research-batches/skill-batch-650.json` and updated the catalog audit.
- [ ] Continue exact-skill research through the remaining null race-restriction frontier.


### 2026-09-29 continuation — Null race restriction boundary batch 651
- [x] Reviewed Evil Explosion (Super), Full Power Energy Wave, Kamehameha Boost, Ki Blast Cannon, and Miracle Kneel.
- [x] Preserved all five `race_restriction` values as null because reviewed exact-skill evidence does not explicitly establish a CaC race/gender restriction.
- [x] Added `docs/data/skill-research-batches/skill-batch-651.json` and updated the catalog audit.
- [ ] Continue exact-skill research through the remaining null race-restriction frontier.


### 2026-09-29 continuation — Null race restriction boundary batch 651
- [x] Reviewed Evil Explosion (Super), Full Power Energy Wave, Kamehameha Boost, Ki Blast Cannon, and Miracle Kneel.
- [x] Preserved all five `race_restriction` values as null because reviewed exact-skill evidence does not explicitly establish a CaC race/gender restriction.
- [x] Added `docs/data/skill-research-batches/skill-batch-651.json` and updated the catalog audit.
- [ ] Continue exact-skill research through the remaining null race-restriction frontier.


### 2026-09-29 continuation — Null race restriction boundary batch 651
- [x] Reviewed Evil Explosion (Super), Full Power Energy Wave, Kamehameha Boost, Ki Blast Cannon, Minus Energy Power Ball, and Miracle Kneel.
- [x] Preserved all six `race_restriction` values as null because no explicit CaC race/gender restriction was established.
- [x] Added `docs/data/skill-research-batches/skill-batch-651.json` and updated the catalog audit.
- [ ] Continue exact-skill research through the remaining null race-restriction frontier.


### 2026-09-29 continuation — Null race restriction boundary batch 651
- [x] Reviewed Sonic Kick, Sledgehammer, Turn Retreat, and Spinning Blade.
- [x] Preserved all four `race_restriction` values as null because reviewed exact evidence does not establish a CaC race/gender restriction.
- [x] Added `docs/data/skill-research-batches/skill-batch-651.json` and updated the catalog audit.
- [ ] Continue exact-skill research through the remaining null race-restriction frontier.


### 2026-09-29 continuation — Generic/DLC race restriction boundary batch 651
- [x] Reviewed Backflip, Blaster Stream, Power Pole, Super Back Jump, and Android Kick.
- [x] Preserved all reviewed `race_restriction` values as null; exact evidence does not explicitly establish CaC race/gender restrictions.
- [x] Added `docs/data/skill-research-batches/skill-batch-651.json` and updated the catalog audit.
- [ ] Continue exact-skill research through the remaining null race-restriction frontier.


### 2026-09-29 continuation — Fresh post-corruption live baseline reconciliation
- [x] Re-read the continuation prompt and exhaustive TODO, then performed a fresh live-main recovery census instead of trusting stale recovery metadata.
- [x] Confirmed the current synchronized working baseline is **549 canonical skills / 549 skill-index records / 862 canonical PQ relationship edges**.
- [x] Confirmed the canonical `docs/data/skills.json` blob SHA is `5912397227d7fb67f1ed263269ace8fcf9b8995b`; the connector exposes the blob SHA but not inline content, so `skills-index.json` was not promoted to source-of-truth.
- [x] Recomputed the 862 PQ relationship counts directly from the canonical forward store: **249 skills / 135 Super Souls / 136 equipment / 247 characters / 88 DLC / 7 farming**; duplicate relationship keys remain 0.
- [x] Identified and repaired stale current-live recovery metadata that still reported 497 skills even though the live synchronized state is 549.
- [x] Preserved historical recovery values (474, 493, 497, 548) as historical provenance; they were not rewritten as if they were current.
- [x] Added `docs/data/post-corruption-live-baseline-reconciliation-2026-09-29.json` as the fresh recovery checkpoint.
- [x] No canonical records were reconstructed from indexes/verified layers and no speculative IDs, restrictions, rewards, rates, or conditions were introduced.
- [ ] Runtime/CI/build remains intentionally non-blocking/unverified.
- [ ] **Exact next:** continue the remaining null `race_restriction` evidence frontier, then continue older DLC/free-update provenance and bidirectional PQ↔skill/Super Soul/equipment enrichment from the repaired canonical forward stores.


### 2026-09-29 continuation — Null race restriction evidence batch 652
- [x] Reviewed Blades of Judgement, Burst Attack, Circle Flash, Cross Arm Dive, Crusher Volcano, and Destructive Ray against exact skill/technique references.
- [x] Preserved all six `race_restriction` values as null; no narrower CaC race/gender/form restriction was established.
- [x] Recorded explicit all-races evidence for Cross Arm Dive without converting it into a restrictive value.
- [x] Added `docs/data/skill-research-batches/skill-batch-652.json` and updated `docs/data/skill-catalog-audit.json`.
- [x] Current index census remains 549 records: 79 null `race_restriction` records, 78 of them CaC-usable, and 470 with explicit non-null restriction values.
- [ ] Continue exact-skill evidence through the remaining null race-restriction frontier.


### 2026-09-29 continuation — Null race restriction evidence batch 653
- [x] Reviewed 10 additional null-race CaC-usable skills: Light Grenade (Super), Mach Kick, Peeler Storm, Power Pole Combo, Punisher Drive, Recoome Eraser Gun, Saiyan Blaster, Senko Ki Blast, Serious Bomb, and Shockwave.
- [x] Preserved all 10 `race_restriction` values as null; no explicit CaC race/gender restriction was established.
- [x] Added `docs/data/skill-research-batches/skill-batch-653.json` and updated the catalog audit.
- [ ] Continue the remaining null race-restriction frontier, prioritizing exact eligibility wording.


### 2026-09-29 continuation — Null race restriction evidence batch 654
- [x] Reviewed 10 additional null-race CaC-usable skills: Backflip, DIE DIE Missile Barrage, Double Buster, Energy Wave Combo, Fighting Sun, Final Blow, Finish Buster, Galick Beam Cannon, Gamma Impact, and Gigantic Ki Blast.
- [x] Preserved all 10 `race_restriction` values as null; no narrower CaC race/gender restriction was established.
- [x] Recorded explicit all-races evidence for DIE DIE Missile Barrage without converting it into a restrictive value.
- [x] Added `docs/data/skill-research-batches/skill-batch-654.json` and updated the catalog audit.
- [ ] Continue the remaining null race-restriction frontier.


### 2026-09-29 continuation — Null race restriction conflict reconciliation batch 655
- [x] Reconciled legacy race-restriction evidence for Drain Charge, Full Power Destruction, and III Bomber against the current canonical boundary.
- [x] Preserved Drain Charge and Full Power Destruction as null because CaC usability alone does not establish a race/gender restriction.
- [x] Preserved the III Bomber historical Majin/Majin CaC conflict as provenance rather than promoting a disputed legacy field value without direct eligibility wording.
- [x] Added `docs/data/skill-research-batches/skill-batch-655.json` and updated the catalog audit.
- [ ] Continue exact eligibility evidence for the remaining null race-restriction frontier.


### 2026-09-29 continuation — External null race restriction cross-check batch 656
- [x] Cross-checked Android Kick, Armored Boost, Burning Spin, Burning Strike, and Burst Attack against external Future Warrior/skill references.
- [x] Preserved all five `race_restriction` values as null because explicit retail CaC race/gender eligibility wording was not established.
- [x] Treated Burning Strike's all-race statement on a PC mod as non-authoritative for retail eligibility rather than promoting it into canonical data.
- [x] Added `docs/data/skill-research-batches/skill-batch-656.json` and updated the catalog audit.
- [ ] Continue the remaining null race-restriction frontier, prioritizing direct retail-game eligibility wording.


### 2026-09-29 continuation — Null race restriction direct-source batch 657
- [x] Reviewed Consecutive Energy Blast, Core Breaker, Full Power Energy Wave, Gigantic Cross, and Gigantic Nova.
- [x] Preserved all five `race_restriction` values as null; no direct retail CaC race/gender/form restriction was established.
- [x] Added `docs/data/skill-research-batches/skill-batch-657.json` and updated the catalog audit.
- [ ] Continue the remaining null-race cohort with direct retail eligibility evidence.


### 2026-09-29 continuation — Null race restriction direct-source batch 658
- [x] Reviewed Blaster Stream, Break Strike, Chaotic Time Impact, Evil Explosion (Super), and Minus Energy Power Ball.
- [x] Preserved all five `race_restriction` values as null; no direct retail CaC race/gender/form restriction was established.
- [x] Added `docs/data/skill-research-batches/skill-batch-658.json` and updated the catalog audit.
- [ ] Continue the remaining null-race cohort with direct retail eligibility evidence.


### 2026-09-29 continuation — Null race restriction direct-source batch 659
- [x] Reviewed Ginyu Force Special Combo, Holstein Shock, Infinity Explosion, Kaioken Assault, and Kamehameha Boost.
- [x] Preserved all five `race_restriction` values as null; no direct retail CaC race/gender/form restriction was established.
- [x] Added `docs/data/skill-research-batches/skill-batch-659.json` and updated the catalog audit.
- [ ] Continue the remaining null-race cohort with direct retail eligibility evidence.


### 2026-09-29 continuation — Null race restriction direct-source batch 660
- [x] Reviewed Ki Blast Cannon, Life Absorbtion, Miracle Kneel, Peeler Storm, and Power Pole.
- [x] Preserved all five `race_restriction` values as null; no direct retail CaC race/gender/form restriction was established.
- [x] Added `docs/data/skill-research-batches/skill-batch-660.json` and updated the catalog audit.
- [ ] Continue the remaining null-race cohort with direct retail eligibility evidence.


### 2026-09-29 continuation — Null race restriction direct-source batch 661
- [x] Reviewed III Flash, III Rain, Sledgehammer, Sonic Kick, and Spinning Blade.
- [x] Preserved all five `race_restriction` values as null; no direct retail CaC race/gender/form restriction was established.
- [x] Added `docs/data/skill-research-batches/skill-batch-661.json` and updated the catalog audit.
- [ ] Continue the remaining null-race cohort with direct retail eligibility evidence.


### 2026-09-29 continuation — Null race restriction direct-source batch 662
- [x] Reviewed Spirit Stab, Split Finger Shot, Super Back Jump, Super Dragon Fist, and Super Drain.
- [x] Preserved all five `race_restriction` values as null; no direct retail CaC race/gender/form restriction was established.
- [x] Added `docs/data/skill-research-batches/skill-batch-662.json` and updated the catalog audit.
- [ ] Continue the remaining null-race cohort with direct retail eligibility evidence.


### 2026-09-29 continuation — Null race restriction direct-source batch 663
- [x] Reviewed Super Explosive Wave (Evasive), Super Galick Gun, Super Ghost Kamikaze Attack (Super), Super Ki Explosion, and Super Mad Dance.
- [x] Preserved all five `race_restriction` values as null; no narrower explicit retail CaC race/gender/form restriction was established.
- [x] Added `docs/data/skill-research-batches/skill-batch-663.json` and updated the catalog audit.
- [ ] Continue the remaining null-race cohort with direct retail eligibility evidence.


### 2026-09-29 continuation — Null race restriction direct-source batch 664
- [x] Reviewed Die Die Missile Barrage, Super Vanishing Ball, Super Volley, Swallow Shot, and Thunder Eraser.
- [x] Preserved all five `race_restriction` values as null; Die Die Missile Barrage and Super Vanishing Ball have explicit all-races evidence, while the other three have no explicit narrower CaC race/gender/form condition.
- [x] Added `docs/data/skill-research-batches/skill-batch-664.json` and updated the catalog audit.
- [ ] Continue the remaining null-race cohort with direct retail eligibility evidence.


### 2026-09-29 continuation — Null race restriction direct-source batch 664
- [x] Reviewed Die Die Missile Barrage, Super Vanishing Ball, Super Volley, Swallow Shot, and Thunder Eraser.
- [x] Preserved all five `race_restriction` values as null; no narrower explicit retail CaC race/gender/form restriction was established.
- [x] Added `docs/data/skill-research-batches/skill-batch-664.json` and updated the catalog audit.
- [ ] Continue the remaining null-race cohort with direct eligibility evidence.


### 2026-09-29 continuation — Null race restriction direct-source batch 664
- [x] Reviewed Die Die Missile Barrage, Super Vanishing Ball, Super Volley, Swallow Shot, and Thunder Eraser.
- [x] Preserved all five `race_restriction` values as null; no explicit narrower retail CaC race/gender/form restriction was established.
- [x] Added `docs/data/skill-research-batches/skill-batch-664.json` and updated the catalog audit.
- [ ] Continue the remaining null-race cohort with direct retail eligibility evidence.


### 2026-09-29 continuation — Post-corruption rebuild verified; recovery-forward frontier reset
- [x] Re-read the live recovery state after the recent corruption/rebuild cycle and confirmed the canonical working baseline is **549 skills / 549 synchronized skill-index records / 862 canonical PQ reward relationships**.
- [x] Confirmed the six PQ relationship counts on live main: **249 skills, 135 Super Souls, 136 equipment, 247 characters, 88 DLC, 7 farming**; duplicate relationship keys remain 0 and orphan skill targets remain 0.
- [x] Confirmed the canonical recovery boundary remains intact: current canonical data was not reconstructed from verified/index/projection layers.
- [x] Reconciled the remaining PQ1 typed-reward anomaly against the current Xenoverse 2 PQ1 source: PQ1 lists only 120 Zeni and Energy Capsule S, so the absence of typed skill/Super Soul/equipment edges is intentional rather than a missing-record assumption.
- [x] Confirmed the PQ equipment endpoint layer is now complete at **123/123 identity matches** for 125 canonical edges; remaining accessory records are component-identity research leads, not endpoint gaps.
- [x] Added `docs/data/post-corruption-continuation-audit-2026-09-29.json` as the new recovery-forward checkpoint.
- [ ] Runtime/CI/build remains intentionally unverified/non-blocking.
- [ ] **Exact next:** continue substantive enrichment from the recovered baseline: fresh race-restriction evidence, older DLC/free-update provenance, and bidirectional PQ↔skill/Super Soul/equipment enrichment; only promote accessory component identities when inventory-level evidence establishes an exact canonical item.


### 2026-09-29 continuation — Race restriction Batch 665: explicit Power Pole evidence
- [x] Added `docs/data/skill-research-batches/skill-batch-665.json`.
- [x] Fresh direct evidence explicitly states that **Power Pole** and **Power Pole Combo** can be obtained by the Future Warrior regardless of race; both are therefore evidence-backed **Universal** race classifications.
- [x] Updated `docs/data/skill-catalog-audit.json` with the Batch 665 finding and moved the frontier to batch 665.
- [ ] **Exact next:** safely reconcile the two explicit Universal classifications into authoritative `docs/data/skills.json`; do not reconstruct or replace the canonical file from index/verified/projection layers.


### 2026-09-29 continuation — Batch 665 canonical sync preparation
- [x] Corrected Batch 665 to use authoritative `race_restriction: "Universal"` fields for Power Pole and Power Pole Combo.
- [x] Confirmed `scripts/build_skills_from_research.py` consumes local skill research batches and merges non-null fields into canonical records.
- [x] Updated the skill catalog audit to distinguish evidence completion from live canonical promotion.
- [ ] Live `skills.json` still requires the existing skills-sync pipeline to run successfully before these values are claimed as promoted; do not reconstruct the canonical blob from indexes/projections.
- [ ] **Exact next:** continue null-race evidence research and then broader cross-domain enrichment.


### 2026-09-29 continuation — Recovery-forward race restriction Batch 666
- [x] Added `docs/data/skill-research-batches/skill-batch-666.json`.
- [x] Restored evidence-backed **Universal** race eligibility for **Justice Pose** and **Death Psycho Bomb**, both of which had explicit unrestricted-race evidence in the repository's historical research but were null in the recovered frontier.
- [x] Batch 666 is formatted for the existing canonical skills-sync pipeline; no canonical blob reconstruction was performed.
- [x] Updated `docs/data/skill-catalog-audit.json`.
- [ ] Live `skills.json` still requires successful skills-sync execution before these two values can be claimed as promoted.
- [ ] **Exact next:** continue the remaining null-race cohort with direct evidence, prioritizing explicit race/gender statements; then resume cross-domain enrichment.


### 2026-09-29 continuation — Race restriction Batch 667
- [x] Added `docs/data/skill-research-batches/skill-batch-667.json` for **Brave Heat → Universal**.
- [x] Evidence explicitly states Brave Heat is a variant of Saiyan Spirit usable by all races.
- [x] Updated `docs/data/skill-catalog-audit.json`.
- [ ] Canonical `skills.json` promotion remains pending successful skills-sync execution.
- [ ] Continue the remaining null race-restriction cohort; do not infer Universal merely from general Future Warrior acquisition.


### 2026-09-29 continuation — Race restriction Batch 668
- [x] Added Batch 668 as a five-record evidence triage pass.
- [x] Reviewed Spirit Stab, Armored Boost, Mach Kick, Kamehameha Boost, and Miracle Kneel.
- [x] Preserved all five as null because the retrieved Future Warrior technique index does not explicitly establish unrestricted race eligibility.
- [x] Updated the catalog audit.
- [ ] Continue with skill-specific evidence capable of establishing an explicit race/gender restriction or unrestricted eligibility.


### 2026-09-29 continuation — Race restriction Batch 669
- [x] Added Batch 669 with explicit Universal classifications for Spirit Bomb and Super Spirit Bomb.
- [x] Evidence explicitly states the Xenoverse 2 Future Warrior can learn both regardless of selected race.
- [x] Updated the catalog audit.
- [ ] Canonical promotion remains pending successful skills-sync; do not claim it has occurred.
- [ ] Continue the remaining null race-restriction cohort using explicit skill-specific evidence.


### 2026-09-29 continuation — Race restriction Batch 670
- [x] Added Batch 670 restoring twelve previously documented Universal/All-CaC race classifications after corruption recovery.
- [x] Covered Kamehameha, Masenko, Energy Charge, Solar Flare, Afterimage Strike, Rise to Action, Wall of Defense, Destructo-Disc, Galick Gun, Candy Beam (Super), Petrifying Spit, and Kai Kai.
- [x] Used the historical 2026-09-19 race census plus the dedicated Future Warrior technique reference; no verification-status field was treated as source of truth.
- [x] Updated the catalog audit.
- [ ] Canonical promotion remains pending successful skills-sync.


### 2026-09-29 continuation — Awoken race provenance Batch 671
- [x] Added Awoken Batch 671 covering Kaioken, Potential Unleashed, Beast, and Ultra Instinct.
- [x] Hardened Universal race-eligibility provenance using direct Future Warrior documentation plus repository normalization rules.
- [x] Preserved canonical-data-first policy; no verified projection was used as source of truth.
- [ ] Canonical promotion remains pending successful validation/sync.


### 2026-09-29 continuation — Awoken Batch 672
- [x] Added Awoken Batch 672 clarifying acquisition eligibility versus actual usability for Super Saiyan God, Super Saiyan God Super Saiyan, and Super Saiyan God Super Saiyan (Evolved).
- [x] Preserved all three existing Saiyan usability restrictions.
- [x] Documented that non-Saiyan Future Warriors may be taught/obtain the godly skills while being unable to use the transformations.
- [ ] Keep acquisition-race and usability-race as separate fields when enriching Awoken data.


### 2026-09-29 continuation — Awoken Batch 673
- [x] Added Awoken Batch 673 documenting acquisition/use alignment for Super Saiyan, Super Vegeta, and Future Super Saiyan.
- [x] Confirmed all three remain Saiyan-only for both acquisition and actual usability in the maintained provenance model.
- [ ] Continue auditing remaining Awoken entries for genuine acquisition/use divergence; do not create artificial exceptions where requirements align.


### 2026-09-29 continuation — Awoken Batch 674
- [x] Clarified Ultra Instinct -Sign- as a cast-only/current retail form rather than a retail CaC Awoken Skill.
- [x] Prevented third-party guide claims from incorrectly classifying Sign as Universal.
- [x] Kept mod-only CaC implementations outside canonical retail data.
- [ ] Continue auditing the remaining Awoken scope for cast-only, staged, and genuinely equippable CaC forms.


### 2026-09-29 continuation — Awoken Batch 675
- [x] Added cast-exclusive provenance for Super Saiyan Blue Kaioken, Pure Progress, and Supersonic Mode.
- [x] Kept cast-exclusive forms separate from CaC race restrictions.
- [ ] Continue auditing remaining Awoken scope and staged/cast-only forms.

### 2026-09-29 continuation — Awoken Batch 676
- [x] Added `docs/data/awoken-research-batches/awoken-batch-676.json`.
- [x] Audited Villainous Mode, Supervillain Mode, and Ultra Supervillain as villainous/cast scope states rather than CaC race restrictions.
- [x] Preserved the distinction between temporary Crystal Raid/Training CaC villainous states and normal retail equippable Awoken Skills.
- [x] Kept `race_restriction: null` because unavailable-to-CaC scope is not a race restriction.
- [ ] Continue auditing remaining Awoken scope for staged, cast-only, and genuinely equippable CaC transformations.


### 2026-09-29 continuation — Canonical race-restriction promotion after rebuild
- [x] Promoted **Power Pole** and **Power Pole Combo** directly in authoritative `docs/data/skills.json` from null to the repository's canonical **`All CaC races`** value using explicit unrestricted-race evidence from the Xenoverse 2 Bōjutsu reference.
- [x] Updated synchronized `docs/data/skills-index.json` for the same two records; record count remains **549**.
- [x] Updated Batch 665 status to `canonical_promoted` and recorded the canonical vocabulary normalization from research-layer `Universal` to `All CaC races`.
- [x] Added `docs/data/race-restriction-promotion-audit-2026-09-29-batch-665.json`.
- [x] No canonical records were rebuilt from indexes, verified layers, or projections.
- [ ] Runtime/CI/build remains intentionally non-blocking/unverified.
- [ ] **Exact next:** continue the remaining null `race_restriction` cohort with direct skill-specific evidence; preserve null where evidence is insufficient, then resume older DLC/free-update provenance and bidirectional PQ↔skill/Super Soul/equipment enrichment.


### 2026-09-29 continuation — Canonical promotion of recovered race-restriction batches 667/669/670
- [x] Promoted **Brave Heat** plus **Spirit Bomb**, **Super Spirit Bomb**, and the twelve Batch 670 recovery classifications directly into authoritative `docs/data/skills.json` as `All CaC races`.
- [x] Synchronized `docs/data/skills-index.json`; canonical/index record count remains 549.
- [x] Marked Batches 667, 669, and 670 `canonical_promoted` and cleared their pending mutation markers.
- [x] Added/retained direct evidence provenance on promoted records; no verified projection was used as source of truth.
- [x] Null race-restriction census is now **62**, down from 77 after the previous recovery promotion.
- [ ] Runtime/CI/build remains intentionally non-blocking/unverified because connected GitHub diagnostics do not expose the failing job-step logs.
- [ ] **Exact next:** audit the remaining 62 null race-restriction records using direct skill-specific evidence. Preserve null when evidence does not explicitly establish race scope; then resume older DLC/free-update provenance and bidirectional PQ↔skill/Super Soul/equipment enrichment.


### 2026-09-29 continuation — Post-corruption recovery integrity manifest
- [x] Performed a fresh live-main recovery census before advancing enrichment work; canonical layers were checked first and stale historical counts were not reused as current.
- [x] Confirmed authoritative docs/data/skills.json blob SHA: 4f1b192ea3d1f76878fe13b3a90bdfb24bae0410. The connector exposes the blob SHA but not inline content for this large canonical file; skills-index.json remains a synchronized consumer, never a reconstruction source.
- [x] Confirmed docs/data/skills-index.json has 549 synchronized records.
- [x] Recomputed docs/data/pq-reward-relationships.json at 862 verified relationships: 249 skill / 135 Super Soul / 136 equipment / 247 character / 88 DLC / 7 farming; duplicate relationship keys remain 0.
- [x] Added docs/data/post-corruption-recovery-integrity-manifest-2026-09-29.json as a compact recovery checkpoint containing the live canonical blob SHA, synchronized index state, relationship counts, source policy, and next-work contract.
- [x] Preserved the 62-record CaC-usable null race_restriction frontier as an evidence boundary; no unsupported restriction was inferred.
- [ ] Runtime/CI/build remains intentionally non-blocking/unverified because connected GitHub diagnostics do not expose failing job-step logs.
- [ ] Exact next: continue direct skill-specific race-restriction evidence, preserving null where explicit race/gender/form scope is absent; then continue older DLC/free-update provenance and bidirectional PQ↔skill/Super Soul/equipment enrichment from canonical forward stores.


### 2026-09-29 continuation — Race restriction frontier census correction (Batch 677)
- [x] Reconciled the post-corruption race-restriction census against the current synchronized 549-record `docs/data/skills-index.json`.
- [x] Corrected the persisted **62** count: the current synchronized index contains **76 CaC-usable records with `race_restriction: null`**, a 14-record discrepancy from the stale handoff count.
- [x] Added `docs/data/skill-research-batches/skill-batch-677.json` with the complete 76-record frontier and the explicit rule that the index is used only as a census consumer, never as canonical reconstruction input.
- [x] Updated `docs/data/skill-catalog-audit.json` to batch 677 and recorded the corrected 76-record frontier.
- [x] No new race classifications were promoted; null remains the evidence boundary where direct race/gender/form evidence is absent.
- [ ] Runtime/CI/build remains intentionally unverified because connected GitHub diagnostics do not expose failing job-step logs.
- [ ] **Exact next:** audit the corrected 76-record frontier in fresh direct-evidence batches, avoiding repeated prior audits; prioritize explicit race/gender/form wording before resuming older DLC/free-update provenance and bidirectional enrichment.


### 2026-09-29 continuation — Race restriction Batch 683 / frontier correction
- [x] Fresh live-main census after the recovery promotions shows **74**, not 76, CaC-usable records with `race_restriction: null` in synchronized `docs/data/skills-index.json`; the earlier 76 count was stale.
- [x] Added `docs/data/skill-research-batches/skill-batch-683.json` and `docs/data/race-restriction-audit-2026-09-29-batch-683.json`.
- [x] Reviewed Turn Retreat, Ultra Fighting Bomber, X4 Kaioken Kamehameha, and Super Galick Gun. All four remain null because the reviewed evidence establishes CaC/Future Warrior availability but does not explicitly establish retail race/gender/form scope.
- [x] No canonical data was reconstructed or mutated in Batch 683; `docs/data/skills.json` remains authoritative and verified/projection/index layers remain consumers only.
- [ ] Runtime/CI/build remains intentionally unverified because connected GitHub diagnostics do not expose failing job-step logs.
- [ ] **Exact next:** continue the remaining **70** unreviewed-by-Batch-683 frontier records, avoiding repeated prior audits; only explicit retail eligibility wording may promote `All CaC races` or a narrower restriction. After this evidence frontier, resume older DLC/free-update provenance and bidirectional PQ↔skill/Super Soul/equipment enrichment.


### 2026-09-29 continuation — Race restriction Batch 684
- [x] Added `docs/data/skill-research-batches/skill-batch-684.json`.
- [x] Reviewed **Full Power Energy Wave, Galick Beam Cannon, Gamma Impact, and Gigantic Cross** using current Xenoverse/Future Warrior-specific evidence.
- [x] Preserved all four as `race_restriction: null`; the reviewed evidence establishes CaC/Future Warrior availability or character association but does not explicitly establish retail race/gender/form eligibility.
- [x] No canonical skill records were mutated; `docs/data/skills.json` remains authoritative.
- [x] Updated the catalog audit to Batch 684.
- [ ] Runtime/CI/build remains intentionally unverified because connected GitHub diagnostics do not expose failing job-step logs.
- [ ] **Exact next:** continue the remaining 66-record frontier, prioritizing direct skill-specific retail eligibility wording and avoiding unsupported inference; then resume older DLC/free-update provenance and bidirectional PQ↔skill/Super Soul/equipment enrichment.
