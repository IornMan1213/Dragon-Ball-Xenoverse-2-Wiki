---
layout: wiki
title: Canonical Accessory Database
permalink: /Accessory-Canonical-Database/
---

# Canonical Accessory Database

The canonical identity layer is the bridge between the wiki's separate accessory research tracks. An accessory is represented once here, while PQs, shops, raids, gifts, wishes, DLC, and events remain acquisition routes attached to that identity.

## Current reconciliation state

- **88 canonical identities** are currently represented in the canonical layer.
- **45 accessory → PQ research records** are available in the PQ layer.
- **51 populated Accessory Shop records** are currently present in the shop research file.
- **47 shop records** are now represented by explicit canonical IDs in the expanded canonical layer.
- Four additional shop-linked identities already existed canonically, but their exact shop record IDs remain to be attached without guessing.
- `shop-051` and `shop-052` remain unresolved data-recovery targets; they are not fabricated.
- Raid/gift and wish/special research remain separate provenance layers until each item is matched with sufficient evidence.

These counts describe the repository's research state, not the game's total accessory inventory.

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

## Accessory Shop promotion

The shop research layer has now been promoted from a candidate-only list into the canonical identity layer where the surviving source names establish distinct inventory candidates.

The promoted shop records include character headwear, eyewear, scouter variants, cosmetic weapons/props, staffs, wings, energy-device accessories, wigs, and other named accessories.

Four previously canonical identities still require exact shop-record IDs to be attached rather than guessed:

- Mr. Popo's Turban
- Saiyuki Hood
- Launch's Wig
- Spike the Devil Man's Head

The canonical layer therefore preserves the identity without inventing a route reference.

## Verification states

### Verified

Identity, acquisition, relevant conditions, and applicable alternate-route/version details have been reconciled against sufficient independent evidence.

### Partially verified

The item identity and a meaningful acquisition relationship are supported, but one or more details remain unresolved.

### Indexed

The item or relationship is catalogued as a research lead, but important acquisition or identity details remain unresolved.

The newly promoted shop identities are intentionally **partially verified**, not verified merely because their shop names are known.

## Important distinctions

- A PQ association does **not** automatically mean a reward is guaranteed on every clear.
- Ultimate Finish rewards remain distinct from ordinary-clear rewards.
- Shop inventory is not assumed to be permanently available when evidence describes rotations.
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

Current equipment research supports treating the Accessory Shop as one acquisition system among several, alongside PQs, raids, mixers, mentor-related routes, and DLC-related content.

The Time Patrol Support Pack is also a useful example of why DLC provenance and acquisition route must remain separate: its official store listing includes Frieza's Head (Final Form) and Korin Wig with Ears & Tail while noting that some included content can also be obtained through in-game conditions.

Historical accessory lists remain useful for route leads, but they are not automatically treated as current shop state. Older lists also demonstrate that some PQ accessories could later become purchasable in the Accessory Shop.

## Next reconciliation targets

1. Attach exact shop route IDs to the four existing canonical shop identities.
2. Recover the missing `shop-051` and `shop-052` records from repository history or independent evidence.
3. Match all wish/special records to canonical identities.
4. Expand canonical route references across the 45 PQ records.
5. Reconcile raid/event-only accessories and discontinued event routes.
6. Cross-check medal-shop identities without confusing TP/STP rotation with the ordinary Accessory Shop.
7. Add direct route IDs for every acquisition layer.
8. Promote identities to `verified` only after the relevant acquisition conditions are independently reconciled.

## Research caveat

The game's own Equipment Collection percentage is still a separate research problem. Current player reports continue to disagree about whether certain raid, tournament, or special-event items count toward that percentage, so the wiki does not infer collection-completion rules from the canonical inventory count.
