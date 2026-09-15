# Skills — Complete Database Master Index

This is the master index for the Xenoverse 2 skill database. The goal is to catalog **every skill entry**, not only the popular CaC moves.

## What counts as a complete record?

Each skill should ultimately have all of these fields:

- **Name**
- **Class** — Super, Ultimate, Evasive, Awoken, Counter, or other special category
- **Damage type** — Strike, Ki Blast, or utility/non-damaging
- **What it does** — practical mechanical description
- **Ki cost / Stamina cost**
- **CaC usable?**
- **Race restriction**, when applicable
- **Character/preset source**, when applicable
- **Exact unlock method**
- **PQ / Expert Mission / Mentor / Shop / Shenron / Raid source**
- **Ultimate Finish requirement**, when applicable
- **DLC requirement**, when applicable
- **Verification status and source**

The repository's structured schema supports these fields in `docs/data/skills.schema.json`.

## Current indexed scope

The current research baseline identifies **672 indexed skill records** across the following categories:

| Category | Indexed records |
|---|---:|
| Ki Blast Supers | 183 |
| Strike Supers | 130 |
| Ki Blast Ultimates | 110 |
| Strike Ultimates | 30 |
| Other Supers | 32 |
| Power Up Supers | 20 |
| Ki Blast Evasives | 23 |
| Strike Evasives | 16 |
| Other Evasives | 11 |
| Power Up Evasives | 2 |
| Other Ultimates | 3 |
| Saiyan Skills | 10 |
| Majin Skills | 10 |
| Namekian Skills | 4 |
| Frieza Race Skills | 4 |
| Human Skills | 4 |
| Unavailable for CaC | 37 |
| Counter Skills | 25 |
| Transformations | 18 |
| **Total indexed scope** | **672** |

These counts are a **coverage target**, not a claim that all 672 records have already been independently verified for mechanics and unlock methods.

## Verification levels

### Indexed

The skill is known to exist and belongs to the category, but the complete mechanical and acquisition record has not yet been independently verified.

### Partially verified

The name/type/source is supported, and at least some mechanics or acquisition details have been checked, but one or more important fields remain unresolved.

### Verified

The name, classification, mechanical behavior, costs, and acquisition route have been checked against a suitable source set. When a reward is RNG-gated, the database should record that explicitly instead of implying a guaranteed drop.

## Primary acquisition channels

1. **Mentor lessons** — signature Super and Ultimate attacks taught by instructors.
2. **Parallel Quest rewards** — many rare Supers, Ultimates, Evasives and DLC skills are reward-table drops, often on Ultimate Finish.
3. **Expert Missions** — some special skills are tied to Expert Mission reward pools.
4. **Skill Shop / TP Medal Shop / STP Medal Shop** — direct purchases and rotating availability.
5. **Shenron wishes** — a limited group of exclusive skills.
6. **Time Rifts / story progression** — especially race-specific Awoken Skills and progression-gated abilities.
7. **Raids / Festival / limited-time events** — event-exclusive rewards and rotating skill access.
8. **DLC packs** — paid-content skills and character-specific techniques.

## Important distinction: CaC skills vs. character/preset skills

A truly exhaustive database must not silently mix player-usable skills with NPC/preset-only techniques.

The database therefore keeps separate status flags for:

- CaC usable
- Race restricted
- Character/preset only
- Story/AI-only
- Raid/Crystal Raid variant
- Festival variant
- Transformation/Awoken

This matters because the same technique name can appear in multiple contexts, while the actual player-accessible version may have different acquisition rules.

## Core detailed records already researched

The repository's `Skills-Detail.md` contains detailed mentor skill research and confirmed examples including:

| Skill | What it does | Acquisition context |
|---|---|---|
| Destructo-Disc | Fast spinning energy disc with armor/guard-piercing behavior in the game's skill implementation. | Krillin mentor lesson |
| Chain Destructo-Disc | Multi-disc upgraded version of Krillin's signature technique. | Krillin mentor / Dual Ultimate path |
| Special Beam Cannon | High-damage drilling beam focused on a single target. | Piccolo mentor |
| Evil Explosion | Point-blank outward energy burst. | Piccolo mentor |
| Genocide Shell | Places a field of ki mines that detonates when enemies approach. | Nappa mentor |
| Arm Crash | Rush strike with guard/stamina-break utility. | Nappa mentor |
| Galick Gun | Fast signature ki blast beam. | Vegeta mentor |
| Final Flash | Large charged ki-blast Ultimate. | Vegeta mentor / related sources |
| Death Beam | Precise finger-fired ki blast. | Frieza mentor |
| Death Ball | Large destructive ki-blast Ultimate. | Frieza mentor |
| Masenko | Two-handed overhead ki blast. | Kid Gohan mentor |
| Instant Transmission | Teleport/evasive utility that changes position rapidly. | Goku mentor |
| Spirit Bomb | Large gathered-energy projectile/finisher. | Goku mentor / other availability varies by record |
| Body Change | Ginyu's unique body-swap Ultimate rather than a conventional damage finisher. | Ginyu mentor |
| Super Ghost Kamikaze Attack | Creates explosive ghost projectiles that pursue the target. | Gotenks / related versions |
| Meditation | Raises available maximum Ki and enables Ki regeneration while active. | PQ 122 / Extra Pack 2 |
| Burst Charge | Very fast initial Ki recovery that slows as the charge continues. | PQ 134 / Ultra Pack 1 |
| Ultimate Charge | Slower opening charge that accelerates for a large refill. | PQ 134 / Ultra Pack 1 |
| Power Rush | Extremely expensive Strike Ultimate intended for very high damage after a Stamina Break. | PQ 122 / Extra Pack 2 |
| Super Electric Strike | Wide electrical Ki Blast Ultimate suitable for grouped targets and large bosses. | Expert Mission 11 |
| Energy Zone | Creates a healing area that can restore the user and nearby allies. | Skill Shop / progression |
| Instant Rise | Fast vertical evasive escape using Stamina. | Skill Shop |

The individual records in `docs/data/skills.json` remain the machine-readable index; this page is the human-facing roadmap and quality standard.

## Research rules for the exhaustive pass

### 1. Never infer a reward location from a character association

A move used by Goku is not necessarily a Goku mentor reward. The acquisition record should name the exact source.

### 2. Distinguish guaranteed rewards from RNG drops

For PQs, Expert Missions, raids and similar activities, the database should say whether a skill is:

- guaranteed
- Ultimate-Finish reward
- random reward-table drop
- TP/STP shop rotation
- one-time reward
- event-limited

### 3. Preserve unresolved conflicts

If two reputable sources disagree on a skill name, PQ, effect, or unlock requirement, keep the conflict visible in a research note until the game data or a primary source resolves it.

### 4. Track DLC explicitly

Every DLC-exclusive skill should name the exact pack/chapter rather than simply saying "DLC".

### 5. Keep transformations separate

Awoken Skills have different unlock logic and resource behavior from ordinary Super/Ultimate/Evasive skills. They remain linked to the main skill database but receive their own detailed treatment.

## Known high-priority skill gaps

The repository's coverage audit currently identifies these major areas for expansion:

- Complete Ki Blast Super reconciliation
- Full record-level Parallel Quest skill population
- Complete Super/Ultimate/Evasive mechanical descriptions
- DLC skill population through the final Future Saga content
- Event/Festival skill variants
- Character-only and unavailable-for-CaC techniques
- Counter skill mechanics
- Exact costs for every record
- Exact Ultimate Finish flags
- Source-level cross-reference validation

## Recommended data record

Example target structure:

```json
{
  "name": "Example Skill",
  "class": "Super",
  "subcategory": "Ki Blast",
  "race_restriction": null,
  "usable_by_cac": true,
  "character_source": null,
  "dlc_requirement": null,
  "ki_cost": 100,
  "stamina_cost": 0,
  "damage_type": "Ki Blast",
  "unlock_method": "parallel_quest_drop",
  "source_quest_or_shop": "PQ ###",
  "ultimate_finish_required": true,
  "skill_description": "Practical description of what the move does.",
  "mechanics_notes": "Guard, tracking, timing, stamina-break, transformation, or special-input behavior.",
  "combo_notes": null,
  "pve_notes": null,
  "pvp_notes": null,
  "verification_status": "partially_verified",
  "last_verified": "2026-09-14",
  "sources": [
    "https://dbxv2.fandom.com/wiki/Example_Skill"
  ]
}
```

## Research sources

- Fandom skill categories: https://dbxv2.fandom.com/wiki/Category:Skills
- Fandom Ki Blast Supers: https://dbxv2.fandom.com/wiki/Category:Ki_Blast_Supers
- 2026 skills/unlock reference: https://dragonballxenoverse2.wiki/unlockables/skills/
- 2026 structured research corpus: https://github.com/Madreag/xenoverse_2_wiki

## Status

**Current state: exhaustive index target established; detailed verification is an ongoing record-by-record pass.**

The goal is not to label the database "complete" until the critical fields above have been populated and audited for all indexed records.
