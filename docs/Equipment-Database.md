---
layout: wiki
title: Equipment Database
---

# Equipment Database

This page is the canonical research index for Xenoverse 2 wearable equipment and clothing. It deliberately separates **appearance**, **equipment stat contribution**, **QQ Bang overrides**, and **Super Soul effects** so one system is not mistaken for another.

## Equipment model

The research layer treats the equipment system as several related but distinct layers:

| Layer | What it represents |
|---|---|
| Clothing/equipment piece | Individual wearable item with its own stat modifiers and appearance |
| Outfit/set | Collection of pieces that may share a visual theme or source |
| Accessory | Separate wearable cosmetic/effect item; its exact stat/effect behavior must be recorded per item |
| QQ Bang | Synthesized stat modifier that overrides the clothing contribution used for the build |
| Super Soul | Separate passive/trigger system; it is not a clothing stat modifier |

## Individual record fields

Every equipment record should preserve, where applicable:

- Stable ID
- Exact item name
- Slot
- Rarity/star information
- Health modifier
- Ki modifier
- Stamina modifier
- Basic Attack modifier
- Strike Super modifier
- Ki Blast Super modifier
- Set/outfit relationship
- Character/theme provenance
- Acquisition source
- Shop source and cost when applicable
- Parallel Quest source
- Expert Mission/raid/event source
- DLC or free-update provenance
- Mix/material relationship
- Version sensitivity
- Verification status
- Source URLs

A missing value means **not yet established**, not zero.

## Clothing vs QQ Bangs

The database must not collapse an equipment item's native stat contribution into the QQ Bang system. QQ Bang research belongs in [`QQ-Bang-Database`](QQ-Bang-Database.md), where the recipe, mixing item, observed six-stat result, and RNG uncertainty are tracked separately.

Current research describes QQ Bangs as replacing the combined clothing stat contribution, which is why builds can use clothing primarily for appearance after a suitable QQ Bang is equipped.

## Acquisition taxonomy

Use explicit acquisition labels rather than a generic "obtainable" field:

- `clothing_shop`
- `tp_medal_shop`
- `parallel_quest`
- `expert_mission`
- `raid`
- `story`
- `mentor`
- `mix_shop`
- `event`
- `dlc`
- `free_update`
- `other`
- `unknown`

When an item has both DLC ownership and an in-game unlock route, record both. DLC ownership must never replace the actual unlock condition.

## Research rules

### 1. Do not infer a complete outfit from one piece

A named costume can contain separate body, legs, hands, feet, and accessory records. Each piece should be independently catalogued when the game treats it independently.

### 2. Do not infer stats from appearance

Character-themed clothing may resemble another set without sharing its stat spread. Record observed/documented values only.

### 3. Do not turn recipe claims into guaranteed results

For mixing-related equipment, preserve the exact inputs and the observed result. Community recipes are research leads unless independently corroborated.

### 4. Preserve version differences

Post-launch updates and DLC can alter the available equipment pool. A historical acquisition route should remain historical rather than silently being presented as the current route.

### 5. Keep cosmetic and combat roles separate

An item can be visually important without being statistically important. Conversely, a stat-bearing item can matter to a build without being part of a visible outfit.

## Current coverage status

The equipment domain is an **active exhaustive research track**, not a claim that every clothing piece has already been entered.

The current structured QQ Bang layer already establishes the synthesis system, Super Mix Capsule Z research, and a community recipe family. The next equipment population pass should expand from system-level research into individual clothing/equipment records.

## High-priority population order

1. Base-game shop equipment.
2. Parallel Quest equipment pools.
3. Expert Mission rewards.
4. Raid/event equipment.
5. Mentor and story equipment.
6. DLC equipment by pack/chapter.
7. Accessories and special-effect items.
8. Historical/version-specific equipment routes.
9. Cross-links from equipment to QQ Bang recipes and Super Souls.

## Provenance standard

Official publisher/platform DLC listings establish DLC content ownership and content categories; they do not by themselves establish every individual item's in-game unlock route. For example, official Future Saga Chapter 4 documentation identifies two playable characters, one Extra Mission, two Parallel Quests, four moves including an Awoken Skill, six costumes/accessories, four Super Souls, a stage, and the Gallery of Time feature. Individual item records should therefore retain their specific acquisition evidence separately.

## Verification states

- **indexed** — item identity/source discovered but meaningful fields remain unchecked.
- **partially_verified** — core identity and some acquisition/stat fields corroborated, but important fields remain unresolved.
- **verified** — identity, core acquisition, and relevant mechanics/stat fields reconciled against sufficient evidence.

Verification is record-specific. A verified outfit source does not automatically verify every piece's stats or every historical acquisition route.

## Research targets

- Exhaustive individual equipment inventory.
- Exact six-stat modifiers for each stat-bearing piece.
- Slot/set relationships.
- Complete shop inventories and costs by progression/version.
- PQ/EM/raid reward provenance.
- DLC/free-update provenance.
- Accessory-specific effects.
- Version changes and discontinued routes.
- Equipment-to-QQ-Bang recipe cross-links.
- Equipment-to-build and Super Soul cross-links.
