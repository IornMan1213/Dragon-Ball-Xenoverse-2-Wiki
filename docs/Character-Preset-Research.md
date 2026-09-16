# Character Preset Research

This is the dedicated research layer for **character presets**. A preset is not automatically a new character identity: it is a documented playable configuration belonging to a character unless the source/game represents the form or variant as a separate roster identity.

## Why this layer exists

Character coverage was previously vulnerable to a common database error: treating a character's roster entry as if it documented every preset. Xenoverse 2 has many characters with multiple preset loadouts, costume variations, transformations, Super Souls, and special/event configurations. Those relationships need their own audit layer.

## Evidence status

| Status | Meaning |
|---|---|
| `indexed` | Preset is discovered from a roster/source listing but its loadout or acquisition is not adequately reconciled. |
| `partially_verified` | Identity and some loadout/acquisition facts are corroborated, but historical or complete preset details remain open. |
| `verified` | Preset identity, loadout, and relevant acquisition/availability facts have been reconciled against sufficient evidence. |

A community video or guide can establish that a preset exists and provide a useful lead, but it is not automatically sufficient evidence for every unlock condition, historical date, shop route, or gameplay statistic.

## Current high-value preset findings

A current community reference provides a broad preset inventory and explicitly separates many preset numbers from distinct roster identities. Its timestamped chapter list is useful for **coverage discovery**, including Goku presets 2–18, multiple Vegeta/Gohan/Piccolo/Frieza presets, special Super Saiyan Blue configurations, GT presets, Festival-related records, Partner Customization keys, and later DLC characters. citeturn0youtube12

The same source also demonstrates why the wiki must not flatten all forms into ordinary preset rows: it separately identifies records such as Goku (Ultra Instinct), Super Saiyan 4 Goku, Super Saiyan God Goku, Goku (Mini), Orange Piccolo, Power Awakening Piccolo, Gohan Beast, and other DLC/event identities. citeturn0youtube12

A second historical community guide from 2022 is useful as a **versioned source**, because its preset inventory differs from the later inventory. For example, it documents earlier preset numbering and older DLC coverage. This should be preserved as historical evidence rather than silently overwritten by the newer list. citeturn0youtube13

## Canonical rules for preset records

### 1. Do not infer numbering across forms

`Goku Preset 15` and `Super Saiyan God Goku` must not be assumed to be the same database identity merely because a source lists them near one another. The source/game's actual roster representation controls the relationship.

### 2. Do not copy a base character's properties into every preset

A base character being a mentor does not prove that every separately represented form is a mentor. Likewise, Partner Customization availability must be recorded per eligible partner identity.

### 3. Preserve preset loadouts exactly when sourced

A documented preset should preserve its sourced Super/Ultimate/Awoken/Evasive/skill configuration. Do not turn a representative loadout into a claim that the skills are exclusive to that character.

### 4. Separate acquisition from presence

A guide showing a preset in the roster does not, by itself, establish whether it came from story progression, a Parallel Quest, a DLC purchase, Festival progression, a Raid key, a gift, a wish, or another route.

### 5. Preserve historical differences

Preset inventories have changed as DLC and free updates were released. A 2022 inventory and a 2026 inventory are separate observations. Historical availability should remain queryable instead of being rewritten as current fact.

## High-connectivity preset audit targets

The next detailed pass should prioritize:

1. **Goku** — base presets, Super Saiyan God, SSGSS variants, GT/SS4, Ultra Instinct variants, Mini, Festival and custom-partner records.
2. **Vegeta** — base presets, Super Saiyan God, SSGSS/Evolved, SS4, GT, DAIMA, Ultra Supervillain and partner records.
3. **Gohan** — Kid, Teen, Adult, Future, Super Hero, Beast and Great Saiyaman relationships.
4. **Piccolo** — base, Power Awakening and Orange Piccolo.
5. **Frieza** — 1st Form, Final Form, Full Power, Golden and Supervillain variants.
6. **Broly** — original Broly, Super Broly, Restrained, Full Power and Supervillain records.
7. **Gogeta/Vegito** — fusion/form identities versus ordinary preset variations.
8. **Future Trunks** — original/Future Trunks, DBS Future Trunks, GT-related and special/customization records.
9. **Jiren/Hit/Toppo** — base, transformed and Supervillain/Ultra Supervillain identities.
10. **DLC/event characters** — Festival, Crystal Raid and Partner Customization records.

## Source-provenance policy

Each future preset record should retain:

- source URL;
- source type (`official`, `wiki`, `community`, `video`, `datamine`, or other documented category);
- observation date/version when known;
- exact preset/form name;
- loadout evidence;
- acquisition evidence;
- verification state;
- unresolved conflicts.

## Known unresolved questions

- Complete current preset counts for every canonical character.
- Exact preset-by-preset unlock routes where guides only demonstrate roster presence.
- Historical changes to preset numbering after DLC/free updates.
- Complete Festival preset inventory and its progression requirements.
- Complete Partner Customization preset inventory and key/DLC relationships.
- Whether certain special/event configurations should be modeled as presets, separate character identities, or both.
- Complete reconciliation of preset skills with the canonical skills database.

## Next pass

Build machine-readable preset records from the highest-connectivity characters first, then reconcile those records against the canonical character layer, skill database, PQ database, DLC layer, Partner Customization keys, and historical-version records. No missing field should be filled by inference.
