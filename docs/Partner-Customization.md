# Partner Customization

Partner Customization is a separate character-configuration system in Dragon Ball Xenoverse 2. It should not be conflated with ordinary CaC customization or with mentor availability.

## How the system works

Partner Customization allows eligible characters to receive alternate skill sets, stats, Super Souls, and costume configurations. The system is accessed through Partner Customization robots in the game's hub areas.

Bandai Namco's official announcement states that players must obtain Customize Unlock Keys from Raid Boss Battles to unlock additional partner characters for customization.

Source: https://www.bandainamcoent.com/news/dbx2-free-big-update

## Customization Unlock Keys

There are 20 documented Customization Unlock Keys. The complete mapping is maintained in:

- `docs/data/partner-customization-key-record-layer.json`
- `docs/data/partner-customization-key-reconciliation.json`

| Key | Partner | DLC / ownership note | Status |
|---:|---|---|---|
| 1 | Goku (Super Saiyan 4) | Free | partially_verified |
| 2 | Vegeta (Super Saiyan 4) | Free | partially_verified |
| 3 | Future Trunks | Free | partially_verified |
| 4 | SSGSS Vegito | Super Pack 4 | partially_verified |
| 5 | SSGSS Gogeta | Extra Pack 4 | partially_verified |
| 6 | Tapion | Extra Pack 1 | partially_verified |
| 7 | Rosé Goku Black | Super Pack 3 | partially_verified |
| 8 | Android 17 (DB Super) | Extra Pack 2 | partially_verified |
| 9 | Janemba | Free | partially_verified |
| 10 | Broly (Full Power Super Saiyan) | Extra Pack 4 | partially_verified |
| 11 | Goku (GT) | Free | partially_verified |
| 12 | Omega Shenron | Free | partially_verified |
| 13 | Majin Buu (Gohan Absorbed) | Extra Pack 1 | partially_verified |
| 14 | Jiren | Extra Pack 2 | partially_verified |
| 15 | Kefla (Super Saiyan) | Extra Pack 3 | partially_verified |
| 16 | Goku (Super Saiyan God) | Free | partially_verified |
| 17 | Gogeta (Super Saiyan 4) | Free | partially_verified |
| 18 | Vegeta (Super Saiyan God) | Ultra Pack 1 | partially_verified |
| 19 | Super Baby 2 | Extra Pack 3 | partially_verified |
| 20 | Goku Black | Pre-order Bonus | partially_verified |

Complete mapping source: https://dbxv2.fandom.com/wiki/Customization_Key

## Key ownership versus DLC ownership

A Customization Unlock Key and the character's DLC ownership are separate facts.

Obtaining a key does **not** by itself establish ownership of DLC containing the corresponding character. Community documentation specifically reports that some keys can be obtained while the associated DLC character remains unavailable until the required content is owned.

The research database therefore keeps key acquisition, partner unlock, and DLC ownership as separate fields.

## What a key unlocks

Community documentation reports that the initial key unlock covers the partner's base skills, balanced stat configuration, and assigned Super Soul. Additional customization options can require TP Medals.

Exact TP Medal costs and complete unlock trees are not yet fully reconciled, so this repository does not invent those values.

## Raid acquisition

Customize Unlock Keys are associated with Online Raid / Raid Boss Battle rewards. A key drop is not guaranteed from every raid round. The repository deliberately does not record a fabricated universal drop percentage.

Official source: https://www.bandainamcoent.com/news/dbx2-free-big-update

Community source: https://dbxv2.fandom.com/wiki/Customization_Key

## Historical update groups

Community references report three historical groups:

- Keys 1–10: 1.15-era update.
- Keys 11–15: 1.17-era update.
- Keys 16–20: 1.19-era update.

These are retained as historical/community evidence until primary patch documentation is reconciled.

## Research status

The current key list is **partially_verified**. The 1–20 mapping is consistent across multiple references, while exact primary-source DLC associations, historical raid rotations, and complete TP Medal unlock trees remain research targets.

## Research targets

1. Reconcile every partner with the canonical character ID.
2. Verify every DLC ownership requirement against official DLC documentation.
3. Record raid/reward history for each key where evidence exists.
4. Catalogue each partner's TP Medal skill, costume, stat, and Super Soul unlock tree.
5. Preserve historical differences rather than replacing them with current-only data.

## Sources

- https://www.bandainamcoent.com/news/dbx2-free-big-update
- https://dbxv2.fandom.com/wiki/Customization_Key
- https://dbxv2.fandom.com/wiki/Partner_Customization
- https://dragonball.fandom.com/wiki/Future_Warrior_(Xenoverse_2)
