---
layout: wiki
title: Awoken Skill Audit
---

# Awoken Skill Audit

This is the dedicated verification pass for **CaC Awoken skills / transformations**. It is separate from the general skill catalog because Awoken skills have race eligibility, transformation-specific resource systems, staged forms, and mechanics that are easy to misclassify.

## Verification rules

- Distinguish CaC Awoken skills from cast-character transformations and enemy-only modes.
- Preserve race restrictions and DLC requirements.
- Record activation/resource costs only when supported by the current research corpus.
- Keep version-sensitive mechanics explicitly attributed rather than presenting historical values as timeless.
- Do not infer unlock requirements from a character merely appearing with a transformation.
- Conflicting mechanics remain documented until independently reconciled.

## Batch 1 — Core CaC transformations

Structured in `docs/data/awoken-research-batches/awoken-batch-01.json`.

The initial audit used an **18-record convention**, but the later canonical integrity pass found that this convention was internally inconsistent: the roster names 20 CaC Awoken forms when every staged form (SS2/SS3, Super Vegeta 2, Kaioken x3/x20) is represented individually alongside the later Power to Overcome. This is now explicitly corrected rather than perpetuated.

Current CaC Awoken forms represented individually are:

- Saiyan: Super Saiyan 1–3, Super Vegeta 1–2, Future Super Saiyan, Super Saiyan God, Super Saiyan God Super Saiyan, Super Saiyan God Super Saiyan (Evolved).
- Universal: Kaioken, Kaioken x3, Kaioken x20, Potential Unleashed, Beast, Ultra Instinct.
- Frieza Race: Turn Golden.
- Majin: Purification.
- Namekian: Become Giant.
- Earthling: Power Pole Pro.
- Universal/DLC: The Power to Overcome.

That is **20 individual forms**. The older "18 transformations" target was therefore stale and is no longer treated as authoritative.

The audit deliberately does **not** treat Pure Progress, Supersonic Mode, Super Saiyan Blue Kaioken, Super/Ultra Supervillain states, SS4 variants, or cast-exclusive forms as standard CaC Awoken skills.

## Batch 2 — Current-version corrections

Structured in `docs/data/awoken-research-batches/awoken-batch-02-corrections.json`.

Key corrections include the current Ultra Instinct 500-Ki requirement with no Ki consumed on activation, Power Pole Pro's zero-Ki activation, and the unresolved two-stage resource details of The Power to Overcome.

## Batch 3 — Acquisition audit

Structured in `docs/data/awoken-research-batches/awoken-batch-03-acquisition-audit.json`.

Acquisition routes were checked separately from mechanics. Unsupported exact levels, PQ numbers, Ultimate Finish percentages, and historical requirements remain qualified rather than being inferred.

## Batch 4 — Mechanics audit

Structured in `docs/data/awoken-research-batches/awoken-batch-04-mechanics-audit.json`.

Current-version mechanics were cross-checked against the consolidated Awoken tables and an independent technical research corpus. Version-sensitive disagreements remain explicitly represented. The Power to Overcome is still partially verified because its exact cooldown/resource transition is not independently settled.

## Batch 5 — Classification and completeness audit

Structured in `docs/data/awoken-research-batches/awoken-batch-05-classification-audit.json`.

The classification pass originally recorded 18 canonical CaC Awoken records. The subsequent canonical integrity pass found that this count was incorrect once every staged form was counted individually and The Power to Overcome was included.

## Batch 6 — Acquisition reconciliation

Structured in `docs/data/awoken-research-batches/awoken-batch-06-acquisition-reconciliation.json`.

Acquisition metadata was reconciled without inventing disputed level gates, friendship thresholds, PQ numbers, or Ultimate Finish requirements.

## Batch 7 — Canonical roster correction

Structured in `docs/data/awoken-research-batches/awoken-batch-07-canonical-roster-correction.json`.

The canonical integrity audit identified a stale Transformation-category index containing cast/enemy-only entries while omitting several CaC stages and The Power to Overcome. The stale seeded entries were Pure Progress, Super Saiyan Blue Kaioken, and Supersonic Mode. Missing entries included Super Saiyan 3, Super Vegeta 2, Kaioken x3, Kaioken x20, and The Power to Overcome.

The correction establishes the current **20-form individual CaC roster** and explicitly records that the previous 18-count convention was erroneous.

## Canonical normalization

`scripts/normalize_awoken_transformation_category.py` now rebuilds only the `Awoken / Transformation` membership records from the audited roster after the general catalog build. Detailed mechanics and acquisition data remain in the researched Awoken records and promotion layer.

`scripts/validate_awoken_integrity.py` separately verifies that promoted Awoken fields are not silently lost during future catalog regeneration.

## Coverage status

**Structured Awoken audit coverage: 20 individual CaC transformation forms.**

Mechanics, acquisition, and classification are audited separately. Unresolved fields remain unresolved. The canonical sync now normalizes the Transformation category after rebuilding the general skill catalog, preventing stale cast-only transformation entries from displacing current CaC Awoken forms.

## Primary research corpus

- Structured transformation research: https://github.com/Madreag/xenoverse_2_wiki/blob/main/research/01-skills-transformations.md
- Transformation overview: https://dragonballxenoverse2.wiki/guides/transformations/
- Unlock checklist: https://dragonballxenoverse2.wiki/guides/how-to-unlock-all-awoken-skills/
- Official Bandai Namco Ultra Instinct update: https://www.bandainamcoent.com/news/dragon-ball-xenoverse-2-free-update-october-12-2023
