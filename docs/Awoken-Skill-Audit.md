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

The initial roster covers:

- Saiyan: Super Saiyan 1–3, Super Vegeta 1–2, Future Super Saiyan, Super Saiyan God, Super Saiyan Blue, Super Saiyan Blue Evolved.
- Universal: Kaioken, Potential Unleashed, Beast, Ultra Instinct.
- Frieza Race: Turn Golden.
- Majin: Purification.
- Namekian: Become Giant.
- Earthling: Power Pole Pro.
- Future Saga Chapter 4: The Power to Overcome.

The first pass deliberately does **not** treat Pure Progress, Supersonic Mode, Super Saiyan Blue Kaioken, Ultra Supervillain states, or cast-only transformations as CaC Awoken skills.

## Research notes

The current external research corpus identifies the core CaC roster and separates player transformations from cast-only states. A 2026 transformation guide independently lists the major CaC forms and their unlock families, while Bandai Namco's October 2023 announcement independently confirms Ultra Instinct as an Awoken Skill. citeturn0search1turn0search7

`The Power to Overcome` remains partially verified because its detailed two-stage resource/cooldown mechanics require a dedicated reconciliation pass; unsupported numeric values are intentionally null.

## Coverage status

**Structured Awoken audit coverage: 18 transformation records.**

The next pass will reconcile exact mechanics and unlock requirements, then separately audit any cast-exclusive or potentially misclassified transformation records before promotion to fully verified status.

## Primary research corpus

- Structured transformation research: https://github.com/Madreag/xenoverse_2_wiki/blob/main/research/01-skills-transformations.md
- Transformation overview: https://dragonballxenoverse2.wiki/guides/transformations/
- Unlock checklist: https://dragonballxenoverse2.wiki/guides/how-to-unlock-all-awoken-skills/
- Official Bandai Namco update: https://www.bandainamcoent.com/news/dragon-ball-xenoverse-2-free-update-october-12-2023
