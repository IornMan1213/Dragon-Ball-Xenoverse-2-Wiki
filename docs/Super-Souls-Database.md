---
layout: wiki
title: Super Souls Database
---

# Super Souls Database

Super Souls are equipment effects that modify combat behavior under specific conditions. Acquisition can come from Parallel Quests, Item/TP Shops, the Mixing Shop, NPCs, mentor content, and limited online events. citeturn0search3

## Database schema

Each Super Soul record should eventually contain:

| Field | Description |
|---|---|
| Name | Exact in-game name |
| Owner | Character associated with the soul, when applicable |
| Trigger | Event that activates the effect |
| Effect | Exact stat/status modification |
| Duration | Temporary effect duration, if any |
| Stack | Whether repeated activation stacks |
| Source | PQ, shop, NPC, raid, mixing, etc. |
| DLC | Required content, if any |
| Verification | Verified / indexed / needs research |

## Acquisition channels

- **Parallel Quests:** many souls are tied to specific PQ reward tables.
- **Item Shop / TP Shop:** some souls can be purchased directly.
- **Mixing Shop:** certain souls are crafted from materials.
- **NPC rewards:** some are obtained through Conton City interactions.
- **Online Raid Events:** rare souls can be limited to raid rewards. citeturn0search3

## Effect notation

The database should preserve the game's actual trigger language rather than flattening everything into a generic "damage boost" label.

Examples of useful trigger classes:

- **Always** — permanently active while equipped.
- **Battle start** — activates when the fight begins.
- **HP threshold** — activates above/below a specified HP percentage.
- **Ki/Stamina threshold** — activates at a resource threshold.
- **Awoken activation** — reacts to a particular transformation.
- **Skill activation** — responds to a specific skill type.
- **KO / revive** — triggers when the user or an ally is KO'd/revived.
- **Just Guard / Charged Ki Blast** — reacts to a specific combat event.

## Strength tiers

The wiki uses the game's letter-style effect notation as a presentation aid, but exact numerical effects should always be stored separately. The Fandom reference describes S/M/L/XL as generally corresponding to 5/10/15/20 percent, while XXL effects can vary. citeturn0search3

## Build research

A future build engine can connect Super Souls to:

- skill tags
- Awoken Skills
- race
- strike/ki specialization
- stamina strategy
- PvE/PvP mode
- trigger reliability
- DLC requirements

This makes the database useful for **build construction**, not just collection tracking.

> **Research rule:** a Super Soul's exact trigger and numerical effect should be copied into structured fields only after verification. Community recommendations belong in a separate notes field.

**Primary reference:** [Super Soul — Xenoverse 2 Wiki](https://dbxv2.fandom.com/wiki/Super_Soul).