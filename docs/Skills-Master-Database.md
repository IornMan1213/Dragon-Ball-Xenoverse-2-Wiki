# Skills Master Database

Dragon Ball Xenoverse 2 has hundreds of skills across the base game and years of DLC. This page is the research hub for the complete skills project; the interactive [Skills Database](skills-database.html) is the preferred browsing experience.

> **Data policy:** a skill name or category is only treated as confirmed index data when it appears in a source category or game-data reference. Mechanics such as damage, costs, unlock requirements and combo properties are marked as verified only after a separate check. This keeps the database useful without turning guesses into facts.

## Skill Classes

| Class | Main categories | Loadout role |
|---|---|---|
| **Super** | Strike, Ki Blast, Power Up, Other | Core attacks, buffs, charges and utility |
| **Ultimate** | Strike, Ki Blast, Other | High-cost finishers and utility |
| **Evasive** | Strike, Ki Blast, Power Up, Other | Escape, repositioning and defensive tools |
| **Awoken** | Transformations / race-specific | Character transformation |

## Current Source Inventory

The Fandom Skills category currently exposes the following useful category snapshots. These are **category-member counts**, not a claim that the numbers add directly to a unique-skill total because skills can belong to multiple categories.

| Category | Indexed members | Database status |
|---|---:|---|
| Ki Blast Supers | 183 | Category indexed |
| Strike Supers | 130 | Category indexed |
| Other Supers | 32 | Category indexed |
| Power Up Supers | 20 | Category indexed |
| Ki Blast Ultimates | 110 | Category indexed |
| Strike Ultimates | 30 | Category indexed |
| Other Ultimates | 3 | Category indexed |
| Ki Blast Evasives | 23 | Category indexed |
| Strike Evasives | 16 | Category indexed |
| Other Evasives | 11 | Category indexed |
| Power Up Evasives | 2 | Category indexed |
| Saiyan Skills | 10 | Category indexed |
| Majin Skills | 10 | Category indexed |
| Unavailable for CaC | 37 | Special classification |

The interactive database links each category directly to its source so the user can inspect the full live category while the local wiki fills in individual records.

## Race / Special Categories

- **Saiyan Skills**: includes Super Saiyan, Super Saiyan God, Super Saiyan God Super Saiyan, Super Saiyan God Super Saiyan (Evolved), Future Super Saiyan, Super Vegeta, Saiyan Spirit, Burning Slash, Shining Slash and Darkness Rush (Melee) in the researched category snapshot.
- **Majin Skills**: includes Buu Buu Ball, Candy Beam (Evasive), Darkness Rush (Melee), Evil Flight Strike, Explosive Buu Buu Punch, Go-Go Gum, Ill Bomber, Majin Kamehameha, Purification and Quick Sleep.
- **Namekian / Frieza Race / Human**: these are separate race-oriented pools and should be kept as explicit tags in the eventual per-skill records rather than inferred from the skill name.
- **Unavailable for CaC**: a special classification for skills exclusive to preset/cast characters and therefore not equippable by custom characters.

## Verified Effects

The original verified-effects table remains the trusted mechanical subset. It includes entries such as Justice Combination, Spirit Sword, Giant Storm, Perfect Kamehameha, Death Ball, Big Bang Kamehameha, Heavenly Arrow, Deadly Dance, Become Giant, Turn Golden, Power Pole Pro and Counter Impact. New entries should be added only when the mechanic can be independently verified.

## Database Record Standard

Every individual skill record should eventually contain:

```text
name
class
subcategory
race_restriction
usable_by_cac
character_source
dlc_requirement
ki_cost
stamina_cost
damage_type
unlock_method
source_quest_or_shop
ultimate_finish_required
skill_description
mechanics_notes
combo_notes
pve_notes
pvp_notes
verification_status
last_verified
sources
```

This makes the wiki suitable for search, filters, build recommendations and future JSON/API export without having to rewrite the content later.

## Research Roadmap

1. Complete category-member manifests for every Super, Ultimate and Evasive subtype.
2. Normalize duplicate names that appear in more than one category.
3. Add Awoken and race-specific records.
4. Add acquisition data: mentor, PQ, Expert Mission, TP Medal Shop, Shenron, raid/event or DLC.
5. Add Ki/Stamina costs and damage type from reliable references.
6. Add individual mechanic notes for commonly used skills first.
7. Add a verification date and source to every record.
8. Generate the interactive database from the structured records rather than hand-maintaining HTML tables.

**Primary source**: Dragon Ball Xenoverse 2 Wiki on Fandom, especially the Skills category and its subcategories. Fandom's category pages identify the skill taxonomy and member lists; this project uses those pages as a reference/index while writing its own database presentation and explanatory material.

**Related**: [Interactive Skills Database](skills-database.html) · [Skills Detail](Skills-Detail.md) · [Skill Unlock Methods](Skill-Unlock-Methods.md) · [Builds](Builds.md)
