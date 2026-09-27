---
layout: wiki
title: Accessory Shop Database
---

# Accessory Shop Database

A structured research index for accessories reported through the **Conton City Accessory Shop**.

This page intentionally separates **shop identity**, **historical price evidence**, **progression availability**, and **current-version verification**. A price from an older guide is not treated as a permanent game constant.

## Current research layer

The machine-readable inventory is stored in:

`docs/data/accessory-shop-research.json`

The current population contains **49 unique shop-route records** after duplicate-name cleanup, covering:

- Scouters and New/Old Model Scouters
- Headwear and character hats
- Wigs
- Eyewear
- Weapon-like cosmetic accessories
- Staffs and wings
- Special accessories

Historical accessory references document shop prices ranging from inexpensive early accessories to high-cost items such as Angel Halo and Z-Sword. They also show that some accessories have alternate PQ, TP Medal Shop, wish, raid, or event routes.

## Research rules

### Price is version-sensitive

A recorded Zeni or TP Medal price is treated as an observation unless current-version evidence confirms it. Shop inventories have changed as Xenoverse 2 received updates and DLC.

### Shop route does not exclude alternate routes

An accessory can be sold in the shop while also appearing as a quest, event, raid, wish, or gift reward. Each route should remain separately documented.

### Cosmetic does not mean unimportant

Accessories generally belong to the cosmetic equipment layer, but the database still records their exact type and relationships because accessories are part of the game's collectible equipment ecosystem.

### Gender/race restrictions are evidence fields

Restrictions are not inferred from character appearance. If a source reports a restriction, it remains marked as reported until reconciled with current-game evidence.

### Duplicate names are not separate inventory records

Repeated historical listings for the same accessory are consolidated into one canonical shop record. Alternate acquisition routes remain attached to that record rather than creating fake duplicate inventory entries.

### TP/STP-only inventory stays separate

Accessories documented specifically as TP/STP Medal Shop rotations are maintained in the separate medal-shop research layer. They are not silently reclassified as ordinary Accessory Shop inventory.

## Initial shop families

| Family | Examples | Research status |
|---|---|---|
| Scouters | Old Model, standard, New Model | Partially verified |
| Headwear | King Kai, Krillin, Ox-King, Chiaotzu, Pikkon | Partially verified |
| Wigs | Hercule, Yajirobe, Chiaotzu | Partially verified |
| Eyewear | Tournament Announcer, King Kai, Cell Game Commentator, Turtle Hermit | Partially verified |
| Cosmetic weapons | Z-Sword, Ninja Katana, Yajirobe's Katana, Ox-King's Axe | Partially verified |
| Staffs/wings | Turtle Hermit's Staff, Korin's Staff, Angel Wings, King Kai's Wings | Partially verified |
| Special | Energy Absorber, Energy Meter | Partially verified |

## Cross-reference targets

The shop layer will eventually cross-link every accessory to:

1. Its master accessory record.
2. Its exact PQ or event alternative, when applicable.
3. TP/STP Medal Shop alternatives.
4. Character Gift routes.
5. Raid and Crystal Raid provenance.
6. DLC/free-update provenance.
7. Collection-percentage behavior.
8. Historical/discontinued availability.

## Sources

- https://dbxv2.fandom.com/wiki/Equipment
- https://enjoi7.sakura.ne.jp/db_newproject2/ac.html
- https://it.scribd.com/document/741933692/Dragon-Ball-Xenoverse-2-Equipment-Guide-Outfits-and-Accessories
- https://www.gameskinny.com/tips/dragon-ball-xenoverse-guide-equipment-and-accessory-list/
