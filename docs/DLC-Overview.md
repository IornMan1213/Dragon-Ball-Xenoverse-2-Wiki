# DLC Overview

*Dragon Ball Xenoverse 2* has received a long-running sequence of paid DLC packs and free updates. This page is the **DLC index**, not a substitute for the individual character, skill, Parallel Quest, Super Soul, costume, system, and story records that should eventually be linked here.

> **Scope rule:** DLC ownership, in-game availability, and unlock method are separate facts. A record may require a DLC pack to exist while still requiring a quest, shop rotation, story progression, wish, or other in-game condition to obtain it.

## Current DLC Status

Bandai Namco identifies **FUTURE SAGA Chapter 4** as the final DLC for Xenoverse 2. Chapter 4 launched July 8, 2026 and concludes the four-chapter FUTURE SAGA. The official DLC catalog continues to list the accumulated DLC packs and bundles.

The game's final DLC state should therefore be documented as a historical content set: **paid DLC + free updates + their in-game unlock conditions**, rather than assuming that every piece of content is obtained merely by purchasing a pack.

## Future Saga at a Glance

| Chapter | Playable characters | Parallel Quests | Moves | Super Souls | Other notable content |
|---|---:|---:|---:|---:|---|
| Chapter 1 | 5 | 12 | 15 | 5 | 3 Extra Missions, 3 costumes/accessories, 63 illustrations |
| Chapter 2 | 3 | 4 | 7 | 3 | 1 Extra Mission arc, 2 costumes/accessories, 14 illustrations |
| Chapter 3 | 2 | 3 | 6 | 3 | 1 Extra Mission arc, 5 costumes/accessories, 23 illustrations, Cheelai & Broly scenario |
| Chapter 4 | 2 | 2 | 4 | 4 | Ultra Time Patrol Battles, 6 costumes/accessories, 8 illustrations, 1 stage, Gallery of Time |

Source: Bandai Namco's official Xenoverse 2 DLC catalog.

## Chapter 1

FUTURE SAGA Chapter 1 adds five playable characters: **Vegeta (Super Saiyan God, Ultra Supervillain), Goku Black (Super Saiyan Rosé, Ultra Supervillain), Broly (Restrained), Android 18 (DB Super), and Videl (DB Super)**.

Officially listed content includes:

- 3 Extra Missions
- 12 Parallel Quests
- 15 Additional Moves
- 3 costumes/accessories
- 5 Super Souls
- 63 illustrations

Individual records should additionally document which content is immediately available, which requires clearing content, and which items/skills come from specific reward tables or shops.

## Chapter 2

FUTURE SAGA Chapter 2 adds **Jiren (Full Power, Ultra Supervillain), Belmod, and Goku (Mini)**.

Officially listed content includes:

- 1 Extra Mission arc
- 4 Parallel Quests
- 7 Additional Moves
- 2 costumes/accessories
- 3 Super Souls
- 14 illustrations

Bandai Namco notes that **Goku (Mini)'s voice-over is Japanese-only**.

## Chapter 3

FUTURE SAGA Chapter 3 adds **Golden Frieza (Ultra Supervillain)** and **Broly (DB Super)** and introduces the **Friendship Mode** system involving Cheelai and Broly.

Officially documented content includes:

- 1 Extra Mission arc
- 3 Parallel Quests
- 6 Additional Moves
- 5 costumes/accessories
- 3 Super Souls
- 23 illustrations
- Cheelai & Broly scenario content
- Friendship Mode

Bandai Namco describes Friendship Mode as a feature where players interact with Cheelai and Broly for rewards and cutscenes.

## Chapter 4 — Final Chapter

FUTURE SAGA Chapter 4 is the game's final DLC chapter. It adds two playable characters: **Goku (Ultra Supervillain Quelled)** and **Supreme Kai of Time (Ultra Supervillain)**. It also introduces **Ultra Time Patrol Battles** and the **Gallery of Time**.

Officially listed content includes:

- 1 Extra Mission
- 2 Parallel Quests
- 1 high-difficulty Ultra Time Patrol Battles quest
- 4 new moves, including 1 Awoken Skill
- 6 costumes/accessories
- 4 Super Souls
- 8 loading-screen illustrations
- 1 stage
- Gallery of Time

### Gallery of Time

The Gallery of Time is a dedicated viewing feature for the game's accumulated loading-screen illustrations and Time Patrol movies. Bandai Namco describes it as containing **over 1,000 loading-screen illustrations** in addition to Time Patrol movies.

### The Power to Overcome

Chapter 4 introduces the Awoken Skill **The Power to Overcome**. The canonical Awoken record should separately track:

- DLC ownership requirement
- exact in-game unlock condition
- race/CaC availability
- resource behavior
- activation requirements
- bonuses and penalties
- duration/stacking behavior, if applicable
- PvE/PvP behavior
- version-sensitive mechanics
- independent sources for each numerical value

The DLC page establishes its DLC relationship; it should not be used as the sole source for detailed combat mechanics.

## Other DLC Families

The official catalog groups the game's accumulated paid content into multiple lines and individual packs, including:

| DLC family / pack | Wiki treatment |
|---|---|
| Super Pass | Track every included pack and its individual content separately |
| Extra Pass | Track every included pack and its individual content separately |
| Ultra Pack Set | Track Ultra Pack 1 and 2 individually as well as the bundle |
| Legendary Pack Set | Track Legendary Pack 1 and 2 individually as well as the bundle |
| HERO OF JUSTICE Pack Set | Track both packs and movie-related content individually |
| Conton City Vote Pack | Track its characters, missions, skills, costumes, illustrations, and related systems individually |
| Legend Patrol Pack | Track its story/progression availability separately from ordinary DLC missions |
| Dragon Ball DAIMA Pack | Track its characters, Parallel Quests, skills, Super Souls, costumes/accessories, and associated free update content separately |
| FUTURE SAGA Pack Set | Treat as a bundle of Chapters 1–4; do not duplicate individual chapter ownership records |
| Individual/older packs | Preserve individual provenance even when a later bundle contains the same content |

The official catalog currently lists the **Dragon Ball DAIMA Pack**, **HERO OF JUSTICE Pack Set**, **Conton City Vote Pack**, **Legendary Pack Set**, **Ultra Pack Set**, **Extra Pass**, **Super Pass**, and the FUTURE SAGA Pack Set among the game's DLC offerings.

## Paid DLC vs Free Updates

This distinction is important for an exhaustive encyclopedia. Some post-launch additions were distributed through free updates alongside paid packs. The wiki should not attribute every item appearing in the same update window to the paid DLC.

For example, Bandai Namco's Dragon Ball DAIMA announcement explicitly separates the paid DAIMA Pack from a **free update** containing additional Raid Boss battles, costumes, Super Souls, Skills, loading screens, and lobby items.

Each future record should therefore use explicit provenance such as:

- `paid_dlc`
- `free_update`
- `base_game`
- `event`
- `shop_rotation`
- `quest_reward`
- `wish`
- `other`

when the repository's schema supports that distinction.

## DLC Content Audit Matrix

The long-term wiki goal is to account for **every individual piece of content introduced by each pack**, rather than stopping at pack-level descriptions.

| Content type | Required downstream record |
|---|---|
| Playable character | Character record, forms/presets, unlock/ownership requirement, associated skills |
| Skill / Awoken | Skill record with class, cost, mechanics, acquisition, CaC restrictions, provenance |
| Parallel Quest | PQ record with enemies, conditions, rewards, Ultimate Finish, drop provenance |
| Extra Mission | Extra Mission record with progression, objectives, rewards, story relationship |
| Super Soul | Super Soul record with effect text, trigger conditions, acquisition, DLC/free-update provenance |
| Costume / accessory | Equipment record with source, slot/type, character compatibility, acquisition |
| Illustration | Illustration/catalog record where useful, including Gallery of Time provenance |
| Stage / map area | Stage record with availability, mode use, visual/location context, related content |
| System / feature | System page explaining unlock, mechanics, progression, rewards, exceptions |
| Event / raid content | Event record with availability period, boss, rewards, rules, and recurrence information |

## Verification Policy

DLC pages establish **what the publisher says a pack contains**. They do not automatically prove every in-game acquisition condition, drop rate, damage value, or CaC restriction.

The wiki therefore keeps these evidence layers separate:

1. **Official publisher evidence** — pack identity, advertised content, release information, platform availability.
2. **In-game/canonical evidence** — actual unlock conditions, rewards, mechanics, costs, restrictions, and behavior.
3. **Structured research/datamining** — detailed reference material used to discover and cross-check content.
4. **Community testing** — useful for frame behavior, damage measurements, unusual interactions, and techniques, but labeled as such when not independently reproduced.

If sources disagree, preserve the disagreement or uncertainty rather than silently choosing the value that makes the table look complete.

## Research Checklist

For every DLC family, the eventual encyclopedia pass should answer:

- What exactly was added?
- Which platform/version received it?
- When was it released?
- Is it paid DLC, free-update content, or both?
- Which characters and forms were added?
- Which skills and Awoken Skills were added?
- Which PQs and Extra Missions were added?
- Which Super Souls were added?
- Which costumes and accessories were added?
- Which stages, systems, modes, events, raids, or features were added?
- What are the exact unlock conditions for each item?
- Are there separate ownership and in-game acquisition requirements?
- Is the content CaC-usable, character-only, race-restricted, gender-restricted, or otherwise limited?
- Does the content have normal-clear, Ultimate-Finish, first-clear, shop-rotation, wish, event, or other acquisition paths?
- Which details are version-sensitive?
- Which claims are independently verified and which remain provisional?

## Official References

- [Bandai Namco — Xenoverse 2 DLC catalog](https://www.bandainamcoent.com/games/dragon-ball-xenoverse-2/downloadable-content)
- [Bandai Namco — Future Saga Chapter 4 launch](https://www.bandainamcoent.com/news/dragon-ball-xenoverse-2-final-dlc-future-saga-chapter-4-is-available-now)
- [Bandai Namco — Future Saga Chapter 3](https://www.bandainamcoent.com/news/dragon-ball-xenoverse-2-future-saga-chapter-3-available-now)
- [Bandai Namco — Dragon Ball DAIMA Pack](https://www.bandainamcoent.com/news/dragon-ball-xenoverse-2-dragon-ball-daima-pack-now-available)
