---
layout: wiki
title: Canonical Accessory Database
permalink: /Accessory-Canonical-Database/
---

# Canonical Accessory Database

The canonical identity layer is the bridge between the wiki's separate accessory research tracks. An accessory is represented once here, while PQs, shops, raids, gifts, wishes, DLC, and events remain acquisition routes attached to that identity.

## Current reconciliation state

- **37 canonical identities** currently reconciled in the main identity layer.
- **45 accessory → PQ research records** are available in the PQ layer.
- **52 populated Accessory Shop records** are currently present in the shop research file; its historical description previously called this 53.
- The new **Accessory Shop → Canonical bridge** maps those populated shop records to canonical identities or marks them as new identity candidates.
- Raid/gift and wish/special research remain separate provenance layers until each item is matched with sufficient evidence.

The counts are intentionally not presented as the game's total accessory inventory. They describe the current research layers and reconciliation state.

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

## Accessory Shop bridge

`docs/data/accessory-shop-canonical-bridge.json` is the current matching layer between the Accessory Shop source data and canonical inventory identity.

The bridge deliberately does **not** manufacture canonical IDs for every shop candidate yet. A `new_identity_candidate` means the shop record is a distinct named inventory candidate that still needs to be inserted into the canonical identity layer after cross-checking PQ, raid, gift, wish, and DLC sources.

Four shop records already have canonical identities elsewhere and therefore must not be duplicated:

- Mr. Popo's Turban
- Saiyuki Hood
- Launch's Wig
- Spike the Devil Man's Head

The shop source currently has 52 populated records. The absent `shop-051` and `shop-052` IDs are not reconstructed from assumption; their contents remain a data-recovery/research task.

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
- Historical prices remain observations until current-version evidence confirms them.

## Current known naming conflicts

- **Golden Great Ape Hat & Tail / Golden Great Ape Wig & Tail** — historical terminology varies.
- **Goku's Wig** — historical PQ numbering differs between source sets.
- **Goku Wig (Super Saiyan)** — historical PQ numbering differs between source sets.
- **Yamcha's Sword** — historical sources disagree on the PQ association.
- **Power Pole / related wish terminology** — source naming requires further reconciliation.
- **Sunglasses (Turtle Hermit 1) / Turtle Hermit Sunglasses** — source naming requires inventory-level confirmation before merging.

## Source layers

- `docs/data/accessory-canonical-reconciliation.json` — canonical identity layer
- `docs/data/accessory-shop-canonical-bridge.json` — Accessory Shop → canonical matching layer
- `docs/data/accessory-pq-research.json` — PQ acquisition research
- `docs/data/accessory-shop-research.json` — standard Accessory Shop research
- `docs/data/accessory-raid-gift-reconciliation.json` — raid, Crystal Raid, and gift routes
- `docs/data/accessory-wish-special-reconciliation.json` — wishes and special routes
- `docs/data/accessory-medal-shop-reconciliation.json` — TP/STP accessory routes

## Research standard

The database is intentionally conservative. If two sources disagree, the disagreement is recorded. If a source identifies an accessory but does not establish whether the reward is guaranteed, the database records the association without inventing a drop rate.

The current Equipment source lists a broad accessory inventory and separate Accessory Shop acquisition routes, including scouter families, character headwear, wigs, and cosmetic props.

Source: https://dbxv2.fandom.com/wiki/Equipment

Historical equipment research is used for route and price leads, but those observations are not automatically treated as current shop state.

Source: https://it.scribd.com/document/741933692/Dragon-Ball-Xenoverse-2-Equipment-Guide-Outfits-and-Accessories

Current community shop schedules demonstrate that medal-shop inventory changes by rotation, so TP/STP routes remain separate from the ordinary Accessory Shop layer.

Source: https://gamefaqs.gamespot.com/boards/204216-dragon-ball-xenoverse-2/81168369

## Next reconciliation targets

1. Promote the unambiguous shop candidates into the canonical identity layer.
2. Match the four existing canonical shop identities to their shop route records.
3. Recover the missing `shop-051` and `shop-052` source records from repository history or independent evidence.
4. Match all wish/special records to canonical identities.
5. Expand the canonical layer with remaining PQ records that are currently only in the source layer.
6. Reconcile raid/event-only accessories and discontinued event routes.
7. Add direct route IDs so every acquisition record can be traced back to one canonical identity.
8. Promote identities to `verified` only after the relevant acquisition conditions are independently reconciled.
