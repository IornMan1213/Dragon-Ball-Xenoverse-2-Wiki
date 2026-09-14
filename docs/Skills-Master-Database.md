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

The live category links remain available from the interactive database. The repository now also has a machine-readable `docs/data/skills.json` seed and a JSON Schema at `docs/data/skills.schema.json` so the project can grow into a real data source rather than a collection of hand-written HTML tables.

## Structured Data Pipeline

The canonical record shape is designed around four layers:

1. **Identity** — name, class and subcategory.
2. **Availability** — race restriction, CaC availability, character source and DLC requirement.
3. **Acquisition / mechanics** — costs, unlock source, finish requirements and mechanics.
4. **Verification** — status, date and source URLs.

Current records deliberately use `verification_status: indexed` when only category membership has been established. A record should move to `partially_verified` or `verified` only after the relevant mechanics/acquisition fields are checked.

### Local data files

- `docs/data/skills.json` — current hand-curated seed used by the browser database.
- `docs/data/skills.schema.json` — machine-readable record contract.
- `scripts/sync_skills.py` — reproducible indexer for Fandom category pages. It is intentionally conservative and records category membership before mechanics.

The sync script is the foundation for the next pass: generate the complete category-member manifest, normalize duplicate memberships, then enrich records without losing the original source trail.

## Race / Special Categories

- **Saiyan Skills**: includes Super Saiyan, Super Saiyan God, Super Saiyan God Super Saiyan, Super Saiyan God Super Saiyan (Evolved), Future Super Saiyan, Super Vegeta, Saiyan Spirit, Burning Slash, Shining Slash and Darkness Rush (Melee) in the researched category snapshot.
- **Majin Skills**: includes Buu Buu Ball, Candy Beam (Evasive), Darkness Rush (Melee), Evil Flight Strike, Explosive Buu Buu Punch, Go-Go Gum, Ill Bomber, Majin Kamehameha, Purification and Quick Sleep.
- **Namekian / Frieza Race / Human**: these are separate race-oriented pools and should be kept as explicit tags in the eventual per-skill records rather than inferred from the skill name.
- **Unavailable for CaC**: a special classification for skills exclusive to preset/cast characters and therefore not equippable by custom characters.

## Verification Queue

The first enrichment pass should prioritize skills that players commonly search for, then expand outward:

| Priority | Data to verify | Why it matters |
|---|---|---|
| 1 | Unlock method + source mission/shop | Makes the database actionable |
| 2 | Ki/Stamina cost | Enables build and loadout comparisons |
| 3 | Skill behavior/mechanics | Makes entries useful beyond names |
| 4 | CaC/race availability | Prevents unusable build recommendations |
| 5 | DLC / event requirements | Helps players locate missing content |
| 6 | PvE/PvP notes | Adds practical context without pretending there is one universal tier list |

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

1. Generate complete category-member manifests for every Super, Ultimate, Evasive and race/special subtype.
2. Normalize duplicate names that appear in more than one category.
3. Add Awoken and race-specific records.
4. Add acquisition data: mentor, PQ, Expert Mission, TP Medal Shop, Shenron, raid/event or DLC.
5. Add Ki/Stamina costs and damage type from reliable references.
6. Add individual mechanic notes for commonly used skills first.
7. Add a verification date and source to every record.
8. Generate all interactive views and exports from the structured records instead of hand-maintaining duplicate tables.

**Primary source**: Dragon Ball Xenoverse 2 Wiki on Fandom, especially the Skills category and its subcategories. Fandom's category pages identify the skill taxonomy and member lists; this project uses those pages as a reference/index while writing its own database presentation and explanatory material.

**Related**: [Interactive Skills Database](skills-database.html) · [Skills Detail](Skills-Detail.md) · [Skill Unlock Methods](Skill-Unlock-Methods.md) · [Builds](Builds.md)
