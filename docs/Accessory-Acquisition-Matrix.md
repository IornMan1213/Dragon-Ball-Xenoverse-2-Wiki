---
layout: wiki
title: Accessory Acquisition Matrix
permalink: /Accessory-Acquisition-Matrix/
---

# Accessory Acquisition Matrix

This page is the cross-system acquisition layer for **Dragon Ball Xenoverse 2 accessories**. It exists separately from individual PQ and shop databases so one accessory can retain multiple legitimate acquisition routes without becoming duplicate inventory entries.

## Current reconciliation coverage

The acquisition matrix tracks canonical identities across gifts, Parallel Quests, shops, raids/Crystal Raids, wishes, DLC provenance, and version-sensitive events. Negative findings are retained when a checked reward extract contains clothing, skills, Super Souls, artwork, or no accessory.

## Late-PQ reconciliation: PQ179-PQ186

| PQ | Accessory evidence | State | Notes |
|---|---|---|---|
| 179 | SS4 Goku (DAIMA) Wig & Tail | Partially verified | Accessory association retained; exact reward slot/condition still requires direct reconciliation. |
| 180 | SS3 Vegeta (DAIMA) Wig | Partially verified | Accessory association retained; exact reward slot/condition still requires direct reconciliation. |
| 181 | None promoted | Indexed negative | Checked extract identifies Glorio's Clothes, which is clothing rather than an accessory. |
| 182 | None promoted | Unresolved | Existing evidence does not safely identify an accessory reward. |
| 183 | None promoted | Unresolved | Existing evidence does not safely identify an accessory reward. |
| 184 | Dragon Ball Balloon | Partially verified | Current datamined evidence gives a 50% Ultimate Finish reward. |
| 185 | Goku (Ultra Supervillain Quelled) Wig | Partially verified | Accessory association retained; exact reward slot/condition still requires direct reconciliation. |
| 186 | None promoted | Indexed negative | Checked extract identifies clothing/set rewards, not an accessory. |

The structured source for this pass is `docs/data/pq-late-accessory-reconciliation.json`. PQ184 is the strongest late-PQ accessory record currently reconciled: the current research corpus identifies Dragon Ball Balloon at 50% on Ultimate Finish. The same source separates that accessory from Chaotic Time Impact, the Super Soul, artwork, and Super Mix Capsule rewards.

PQ182 and PQ183 are deliberately **not filled by inference**. The underlying DLC research confirms the PQ182-184 block belongs to Future Saga Chapter 3, but the accessory layer does not yet have sufficiently direct evidence to promote an accessory mapping for 182 or 183.

## Cross-route records

| Accessory | Acquisition systems currently documented | Evidence state | Important caveat |
|---|---|---|---|
| SS Rosé Wig | Character Gift — Goku; Crystal Raid / raid-related reward documentation | Partially verified | Gift reward is pool-based unless a deterministic result is independently established. |
| Golden Scouter | Character Gift — Nappa/Vegeta; Crystal Raid / raid documentation | Partially verified | Gift and raid provenance remain separate routes. |
| Golden Great Ape Wig & Tail | Character Gift — Gohan; Crystal Raid / raid documentation | Partially verified | Keep distinct from other Great Ape accessories. |
| Fused Zamasu Wig | Crystal Raid / Online Raid documentation | Partially verified | Raid availability is event-dependent. |
| Tiencha Wig | Accessory Shop; Online Raid documentation | Partially verified | Historical raid and shop routes remain separate. |
| Frieza's Head (Final Form) | Crystal Raid; Time Patrol Support Pack | Partially verified | DLC provenance does not replace the actual acquisition condition. |
| Tapion Wig | Raid/event documentation | Partially verified | Event availability is version-sensitive. |
| Janemba's Sword | Crystal Raid documentation | Partially verified | Keep distinct from Tapion's Sword. |
| Lord Zuno's Topknot Wig | Crystal Raid documentation | Partially verified | Historical/event availability requires version-aware research. |
| Universe 6 Supreme Kai's Helper's Hat | Crystal Raid documentation | Partially verified | Historical raid route; availability is event-dependent. |
| Tights Hat | Crystal Raid documentation | Partially verified | Do not infer a PQ route. |
| SS4 Wig & Tail (Goku) | PQ110 | Partially verified | PQ110's Ultimate Finish relationship is separate from DLC ownership. |
| Resistance Helmet | PQ111; DLC provenance | Partially verified | DLC ownership does not itself prove a guaranteed PQ reward. |
| Android 13's Hat | PQ105; TP Medal Shop reported | Partially verified | PQ and shop routes remain separate. |
| Android 17 (DB Super) Wig | PQ152; DLC provenance | Partially verified | Exact reward mechanics remain separate from the association. |
| King Vegeta (DB Super) Wig | PQ154; DLC provenance | Partially verified | Exact reward mechanics remain separate from the association. |
| Gamma 2's Helmet | PQ155; HERO OF JUSTICE Pack 1 | Partially verified | Current DLC and PQ evidence are cross-referenced. |
| Gamma 1's Helmet | PQ156; HERO OF JUSTICE Pack 1 | Partially verified | PQ association retained. |
| Dr. Hedo Hood | PQ159; HERO OF JUSTICE Pack 2 | Partially verified | PQ association retained. |
| Red Ribbon Army Helmet | PQ160; HERO OF JUSTICE Pack 2 | Partially verified | PQ association retained. |
| Gohan (Beast) Wig | PQ162; HERO OF JUSTICE Pack 2 | Partially verified | PQ relationship remains subject to reward-condition reconciliation. |
| Videl (DB Super) Wig | PQ168; Future Saga Chapter 1 | Partially verified | Reward-condition details remain separate. |
| Goku (Ultra Supervillain Quelled) Wig | PQ185; Future Saga Chapter 4 | Partially verified | Newest PQ route requires current-version reward reconciliation. |

## PQ157-PQ168 checked range

The dedicated reconciliation layer records each PQ in this range rather than only recording positive accessory matches. Clothing is explicitly excluded from accessory identity.

## Character Gift equipment pools

Current/historical gift documentation reports accessory routes including Goku → SS Rosé Wig, Gohan → Golden Great Ape Wig and Tail, Nappa → Golden Scouter, and Vegeta → Golden Scouter. Gift equipment is modeled as pool-based unless evidence establishes a deterministic reward.

## Raid and Crystal Raid separation

Raid documentation contains accessories including Tights Hat, Universe 6 Supreme Kai's Helper's Hat, Lord Zuno's Topknot Wig, Janemba's Sword, Frieza's Head (Final Form), Golden Great Ape Hat & Tail, Golden Scouter, Super Saiyan Rosé Wig, Fused Zamasu Wig, Tapion Wig, and Tiencha Wig. These remain event/raid provenance rather than being silently converted into PQ or shop records.

## Wish and special routes

Wish/special research is kept in `docs/data/accessory-wish-special-reconciliation.json`. These routes are distinct from ordinary PQ rewards and shop inventory. Where an item appears in both a wish route and another system, the routes remain independently documented.

## DLC provenance

DLC ownership and in-game acquisition are separate facts. A DLC pack can contain a PQ, costume/accessory, skill, or other content without that purchase itself being the item's immediate unlock condition.

## Collection percentage is a separate research problem

The wiki does not claim that every accessory in this database necessarily contributes to the same Equipment Collection percentage. The denominator, DLC/event inclusion, special-item treatment, and version differences remain separate research targets.

## Research rules

- One accessory identity gets one canonical record even when multiple acquisition routes exist.
- Each acquisition route keeps its own provenance and verification state.
- Historical conflicts remain visible until independently reconciled.
- A reward listing does not become a guaranteed-drop claim without evidence.
- Raid availability is event/version sensitive.
- Character Gift equipment can be random from a defined pool.
- DLC purchase status, PQ ownership, and actual unlock conditions are separate facts.
- Clothing is never duplicated into the accessory catalogue merely because it appears beside accessories in a reward table.
- Absence from a checked reward extract is evidence about that extract, not proof that no alternate route exists.
- Collection percentage is never inferred from an acquisition list.

## Related databases

- `docs/data/equipment-accessories-record-layer.json`
- `docs/data/accessory-acquisition-matrix.json`
- `docs/data/accessory-pq-research.json`
- `docs/data/pq-late-accessory-reconciliation.json`
- `docs/data/accessory-pq-reconciliation-157-168.json`
- `docs/data/accessory-shop-research.json`
- `docs/Accessory-PQ-Database.md`
- `docs/Accessory-Shop-Database.md`
- `docs/TP-STP-Medal-Shop-Database.md`
- `docs/Equipment-Database.md`

## Sources

- https://github.com/Madreag/xenoverse_2_wiki/blob/main/content/parallel-quests/pq-184.md
- https://github.com/Madreag/xenoverse_2_wiki/blob/main/content/dlc/future-saga-chapter-3.md
- https://github.com/Madreag/xenoverse_2_wiki/blob/main/content/game-modes/parallel-quests.md
- https://dbxv2.fandom.com/wiki/Equipment
- https://dbxv2.fandom.com/wiki/Online_Raid_Quest
- https://steamcommunity.com/sharedfiles/filedetails/?id=808851543
