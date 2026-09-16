---
layout: wiki
title: QQ Bang Database
---

# QQ Bang Database

QQ Bangs are synthesized stat modifiers created at the Capsule Corporation Clothing Mixing Shop. They replace the stat contribution of the four main clothing pieces, letting a CaC keep a chosen stat profile while using clothing primarily for appearance. citeturn0search1turn0search0

## Core attributes

Every QQ Bang record should track the six core CaC attributes:

- Health
- Ki
- Stamina
- Basic Attack
- Strike Supers
- Ki Blast Supers

Each field can receive a positive, neutral, or negative modifier. The exact resulting spread is recipe- and RNG-dependent, so a recipe should never be treated as a guaranteed stat outcome. citeturn0search1turn0search8

## Database fields

| Field | Description |
|---|---|
| ID | Stable database identifier |
| Stars | Quality/rating of the QQ Bang |
| Health | Observed modifier |
| Ki | Observed modifier |
| Stamina | Observed modifier |
| Basic Attack | Observed modifier |
| Strike Supers | Observed modifier |
| Ki Blast Supers | Observed modifier |
| Clothing inputs | Exact clothing pieces used |
| Mixing item | Capsule/material used |
| Mixing location | NPC/shop used for synthesis |
| Result | Observed six-stat output |
| Build tags | Searchable build archetypes |
| RNG notes | Variance and reproducibility notes |
| Verification | `indexed`, `partially_verified`, or `verified` |

## Synthesis workflow

1. Reach the Capsule Corporation Clothing Mixing Shop.
2. Select two clothing pieces as synthesis inputs.
3. Select the mixing item.
4. Pay the required mixing cost shown by the game.
5. Record the resulting QQ Bang's star rating and all six stat modifiers.
6. Preserve the exact inputs and mixing item with the result.

Older and current community references agree that the system produces variable results and that material quality can influence the potential result without guaranteeing a specific spread. citeturn0search1turn0search8

## Six-star research

Super Mix Capsule Z is widely documented as a high-tier mixing item used for six-star QQ Bang attempts. Community guides commonly use Multiplayer Parallel Quest Tour runs to farm it, while exact current drop behavior remains a research field rather than a hard-coded guarantee. citeturn0youtube24turn0reddit29

The wiki therefore records **how a result was produced** separately from **what result was actually observed**.

## Recipe research

The database should preserve recipe families rather than presenting one community recipe as universally deterministic. Frequently discussed inputs include Battle Suit (Bardock), Beerus clothing, Light Heart Suit combinations, and other high-quality clothing. citeturn0youtube24turn0reddit30

### Current structured research layer

Machine-readable QQ Bang system research is stored in:

`docs/data/qq-bangs-record-layer.json`

Current records cover the synthesis system, Super Mix Capsule Z research, and a documented Bardock/Beerus recipe family. These are **research records**, not a claim that every possible QQ Bang has been catalogued.

## Build archetype tags

The eventual searchable catalogue should support:

- Strike-focused
- Ki Blast-focused
- Basic Attack
- Hybrid
- Ki + Stamina
- Health + Stamina
- Defensive
- General-purpose
- PvE-oriented
- PvP-oriented

These tags describe how a recorded stat spread is commonly used; they are not substitutes for the raw six-stat values.

## Verification standard

A specific QQ Bang should be promoted to **verified** only when its exact six-stat result, star rating, inputs, and mixing item are sufficiently corroborated. Community screenshots and recipes are valuable research leads, but an expected result must not be written as an observed result.

## Research gaps

- Complete inventory of documented QQ Bang recipes and recipe families.
- Six-stat outputs for each reproducible recipe/result combination.
- Six-star material and mixing-item behavior by version.
- Clothing rarity/quality effects on result distributions.
- Exact current acquisition paths for Super Mix Capsule Z and related mixing materials.
- Version differences in stat caps and QQ Bang behavior.
- Cross-links from QQ Bangs into build, attribute, Super Soul, skill, and equipment records.

**Primary references:** [GameSkinny QQ Bang guide](https://www.gameskinny.com/tips/dragon-ball-xenoverse-2-qq-bangs-guide/), the current Madreag gear/QQ Bang research corpus, and community synthesis reports.
