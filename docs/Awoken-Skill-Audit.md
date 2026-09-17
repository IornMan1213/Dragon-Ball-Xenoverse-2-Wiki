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

The initial roster covers 18 canonical CaC Awoken records when staged forms are grouped into their parent transformations:

- Saiyan: Super Saiyan 1–3, Super Vegeta 1–2, Future Super Saiyan, Super Saiyan God, Super Saiyan God Super Saiyan, Super Saiyan God Super Saiyan (Evolved).
- Universal: Kaioken (including x3/x20 stages), Potential Unleashed, Beast, Ultra Instinct.
- Frieza Race: Turn Golden.
- Majin: Purification.
- Namekian: Become Giant.
- Earthling: Power Pole Pro.
- Universal/DLC: The Power to Overcome.

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

The classification pass confirms **18 canonical CaC Awoken records**. Staged transformations are intentionally grouped rather than counted as separate records:

- Super Saiyan → Super Saiyan 2 → Super Saiyan 3
- Super Vegeta → Super Vegeta 2
- Kaioken → Kaioken x3 → Kaioken x20

The current seeded `skills.json` reports a **Transformations category count of 18**, matching this canonical roster. The file remains a seeded index, so category membership itself is not treated as proof of mechanics or acquisition.

### Explicitly excluded from the CaC roster

- Pure Progress — Hit's cast transformation.
- Supersonic Mode — Dyspo's cast transformation.
- Super Saiyan Blue Kaioken — Goku's cast transformation rather than a separate CaC Awoken skill.
- Supervillain / Ultra Supervillain states — enemy/story states.
- SS4 / SS4 Limit Breaker — not a standard selectable CaC Awoken skill in the current game.
- Orange Piccolo — cast-character transformation; the CaC transformation introduced alongside that era is Beast.

Current 2026 independent material likewise presents the same 18-form CaC roster, including the three-stage Super Saiyan chain, both Super Vegeta stages, Kaioken stages, racial forms, and The Power to Overcome.

## Coverage status

**Structured Awoken audit coverage: 18 canonical CaC transformation records.**

Classification is now audited. Mechanics and acquisition are researched separately, with unresolved fields retained as unresolved. The next promotion step is to reconcile these research batches against the canonical skill records and only promote fields that have sufficient evidence.

## Primary research corpus

- Structured transformation research: https://github.com/Madreag/xenoverse_2_wiki/blob/main/research/01-skills-transformations.md
- Transformation overview: https://dragonballxenoverse2.wiki/guides/transformations/
- Unlock checklist: https://dragonballxenoverse2.wiki/guides/how-to-unlock-all-awoken-skills/
- Official Bandai Namco Ultra Instinct update: https://www.bandainamcoent.com/news/dragon-ball-xenoverse-2-free-update-october-12-2023
