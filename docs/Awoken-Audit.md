---
layout: wiki
title: Awoken Skills Audit
---

# Awoken Skills Audit

This is the dedicated verification pass for Xenoverse 2 Awoken Skills / transformations. It follows the skill-catalog pass and separates **CaC-unlockable transformations** from cast-only transformation states.

## Verification standard

Each entry should eventually record:

- Name and race restriction
- CaC availability
- Ki/stamina activation and drain behavior
- Damage/stat modifiers and notable mechanical changes
- Exact unlock path
- Required level, friendship, mentor, Time Rift, Advancement Test, Parallel Quest, wish, DLC, or TP Medal condition
- Whether the form has stages or can be chained from another Awoken
- Current-version verification date and source links

## Initial audit queue

| Awoken Skill | Scope | Primary unlock path to verify | Status |
|---|---|---|---|
| Super Saiyan | Saiyan CaC | Capsule Corporation / Vegeta chain | Research queued |
| Super Vegeta | Saiyan CaC | Capsule Corporation / Vegeta chain | Research queued |
| Future Super Saiyan | Saiyan CaC | Story / Future-related unlock path | Research queued |
| Kaioken | Any CaC | Parallel Quest reward condition | Research queued |
| Potential Unleashed | Any CaC | Advancement Test progression | Research queued |
| Turn Golden | Frieza Race CaC | Frieza's Spaceship Time Rift | Research queued |
| Purification | Majin CaC | Majin Buu's House progression | Research queued |
| Become Giant | Namekian CaC | Guru's House progression | Research queued |
| Power Pole Pro | Earthling CaC | Hercule's House progression | Research queued |
| Super Saiyan God | Saiyan CaC | Beerus / Super Saiyan God progression | Research queued |
| Super Saiyan God Super Saiyan | Saiyan CaC | Whis progression | Research queued |
| Super Saiyan God Super Saiyan (Evolved) | Saiyan CaC | Whis progression | Research queued |
| Ultra Instinct -Sign- | Cast-only form | Goku (Ultra Instinct -Sign-) preset/state; no retail CaC Awoken Skill | Scope clarified — not a CaC Awoken |
| Ultra Instinct | Any CaC | Jiren-related unlock path | Research queued |
| Beast | Any CaC | Gohan/Videl + Piccolo progression | Research queued |

## Important scope rule

Pre-transformed roster characters, enemy-only states, and mod-only forms are not counted as CaC Awoken Skills unless the game provides the form as an equippable Awoken Skill.

## Sources

- Public structured Xenoverse 2 research corpus: https://github.com/Madreag/xenoverse_2_wiki/blob/main/research/01-skills-transformations.md
- Awoken Skill guide/reference: https://dbxv2.fandom.com/wiki/Awoken_Skill

> Status intentionally starts as **Research queued**. Entries are promoted only after their unlock conditions and mechanics are independently checked.


## 2026-09-29 — Awoken race provenance Batch 671

- Added awoken-research-batches/awoken-batch-671.json.
- Hardened direct-source provenance for four Universal Awoken classifications: Kaioken, Potential Unleashed, Beast, and Ultra Instinct.
- Evidence distinguishes race eligibility from acquisition; verified projection data was not used as source of truth.
- Canonical mutation remains deferred; this is sync-ready provenance research.


## 2026-09-29 — Awoken acquisition vs usability Batch 672

- Added `awoken-research-batches/awoken-batch-672.json`.
- Documented the distinction between obtaining a Saiyan-exclusive god transformation and being able to activate/use it.
- Covered Super Saiyan God, Super Saiyan God Super Saiyan, and Super Saiyan God Super Saiyan (Evolved).
- Preserved `race_restriction: "Saiyan"` for all three; acquisition by a non-Saiyan does not establish non-Saiyan usability.
- Current Future Warrior documentation explicitly describes SSGSS and SSGSS (Evolved) as awardable regardless of selected race while remaining Saiyan-only in use; the same acquisition/use distinction is documented for SSG.
- Canonical Awoken data was not reconstructed or overwritten from projection/verified layers.


## 2026-09-29 — Awoken acquisition/use alignment Batch 673

- Added `awoken-research-batches/awoken-batch-673.json`.
- Confirmed acquisition and actual usability remain aligned for Super Saiyan, Super Vegeta, and Future Super Saiyan: all are Saiyan-restricted.
- This records an explicit alignment case so the acquisition-vs-usability distinction is not over-applied.
- Canonical data was not reconstructed or overwritten.


## 2026-09-29 — Awoken Batch 674: Ultra Instinct -Sign- scope correction

- Added `awoken-research-batches/awoken-batch-674.json`.
- Clarified that the retail CaC Awoken Skill is **Ultra Instinct**, while **Ultra Instinct -Sign-** is not a retail equippable CaC Awoken Skill.
- Prevented third-party guide wording from incorrectly creating a Universal race classification for Sign.
- CaC Ultra Instinct -Sign- implementations found in current mod references are explicitly mod-based, so they are not promoted into the retail CaC Awoken dataset.


## 2026-09-29 — Awoken Batch 675: cast-exclusive scope

- Added awoken-research-batches/awoken-batch-675.json.
- Explicitly classified Super Saiyan Blue Kaioken, Pure Progress, and Supersonic Mode as cast-exclusive and unavailable to retail CaCs.
- Kept race_restriction null for these records: cast exclusivity is a scope property, not a CaC race restriction.
- Supersonic Mode is corroborated by the official Dragon Ball announcement identifying it as Dyspo's Awoken Skill.

## 2026-09-29 — Batch 676 villainous-state scope

- Added awoken-batch-676.json.
- Audited Villainous Mode, Supervillain Mode, and Ultra Supervillain as scope states rather than CaC race restrictions.
- Crystal Raid/Training access is kept separate from a normal retail equippable Awoken Skill.
- race_restriction remains null for these unavailable-to-CaC states.
