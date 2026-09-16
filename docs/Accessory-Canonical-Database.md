---
layout: wiki
title: Canonical Accessory Database
permalink: /Accessory-Canonical-Database/
---

# Canonical Accessory Database

The canonical identity layer is the bridge between the wiki's separate accessory research tracks. An accessory is represented once here, while PQs, shops, raids, gifts, wishes, DLC, and events remain acquisition routes attached to that identity.

## Current reconciliation state

- **37 canonical identities** currently reconciled in this layer.
- **45 accessory → PQ research records** are available in the PQ layer.
- **53 Accessory Shop research records** remain a broader source layer and still require direct identity matching.
- Raid/gift and wish/special research remain separate provenance layers until each item is matched with sufficient evidence.

The count is intentionally not presented as a claim that the game contains only 37 accessories. This is a **reconciled subset**, not a final inventory count.

## Why this layer exists

Large Xenoverse 2 equipment lists often mix inventory identity, acquisition method, historical terminology, DLC ownership, and shop rotation into one table. That creates duplicate-looking entries and makes alternate acquisition routes difficult to follow.

This database separates those concepts:

| Layer | Meaning |
| --- | --- |
| Canonical identity | The inventory item itself |
| Alias | Historical or alternate name for the same item when supported |
| Acquisition route | A way the player can obtain the item |
| Provenance | DLC, update, raid, event, or historical context |
| Verification status | How completely the identity and route have been reconciled |

## Verification states

### Verified

Identity, acquisition, relevant conditions, and applicable alternate-route/version details have been reconciled against sufficient independent evidence.

### Partially verified

The item identity and a meaningful acquisition relationship are supported, but one or more details remain unresolved.

### Indexed

The item or relationship is catalogued as a research lead, but important acquisition or identity details remain unresolved.

## Important distinctions

- A PQ association does **not** automatically mean a reward is guaranteed on every clear.
- Ultimate Finish rewards remain distinct from ordinary-clear rewards.
- Shop inventory is not assumed to be permanently available when the evidence describes rotations.
- Raid history is preserved separately from current availability.
- Character gifts are not merged into raid routes merely because the same accessory appears in both systems.
- Clothing and accessories are not merged because they appear in the same reward table.
- DLC ownership and the in-game acquisition condition are separate facts.
- Historical naming conflicts remain visible instead of being silently rewritten.

## Current known naming conflicts

- **Golden Great Ape Hat & Tail / Golden Great Ape Wig & Tail** — historical terminology varies.
- **Goku's Wig** — historical PQ numbering differs between source sets.
- **Goku Wig (Super Saiyan)** — historical PQ numbering differs between source sets.
- **Yamcha's Sword** — historical sources disagree on the PQ association.
- **Power Pole / related wish terminology** — source naming requires further reconciliation.

## Source layers

- `docs/data/accessory-canonical-reconciliation.json` — canonical identity layer
- `docs/data/accessory-pq-research.json` — PQ acquisition research
- `docs/data/accessory-shop-research.json` — standard Accessory Shop research
- `docs/data/accessory-raid-gift-reconciliation.json` — raid, Crystal Raid, and gift routes
- `docs/data/accessory-wish-special-reconciliation.json` — wishes and special routes
- `docs/data/accessory-medal-shop-reconciliation.json` — TP/STP accessory routes

## Research standard

The database is intentionally conservative. If two sources disagree, the disagreement is recorded. If a source identifies an accessory but does not establish whether the reward is guaranteed, the database records the association without inventing a drop rate.

Current official DLC documentation confirms that Xenoverse 2 continues to distribute costumes/accessories through DLC alongside Parallel Quests and that some DLC content is obtained by clearing in-game conditions. urlOfficial Dragon Ball Xenoverse 2 DLC pagehttps://en.bandainamcoent.eu/dragon-ball/dragon-ball-xenoverse-2/dlc

The current 186-PQ research guide also demonstrates why the canonical layer is necessary: late PQs can provide both costume pieces and accessory items, and those need to remain separate inventory identities. urlAll 186 Parallel Quests guidehttps://steamcommunity.com/sharedfiles/filedetails/?id=808851543

## Next reconciliation targets

1. Match the 53 standard shop records to canonical identities.
2. Match all wish/special records to canonical identities.
3. Expand the canonical layer with the remaining PQ records that are currently only in the source layer.
4. Reconcile raid/event-only accessories and discontinued event routes.
5. Add direct route IDs so every acquisition record can be traced back to one canonical identity.
6. Promote identities to `verified` only after the relevant acquisition conditions are independently reconciled.
