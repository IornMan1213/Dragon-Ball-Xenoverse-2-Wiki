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

## DLC → Character Identity Navigation

The resolved DLC headline-character labels below link into the local character search surface through the maintained DLC identity bridge. Unresolved variants remain explicitly unresolved and are not mapped to a nearby character identity.

| DLC headline-character label | Canonical character destination | Resolution |
|---|---|---|
| Goku Black (Super Saiyan Rosé), Ultra Supervillain | [Goku Black (Super Saiyan Rosé) Ultra Supervillain]({{ "/Characters-All/" | relative_url }}?q=Goku%20Black%20(Super%20Saiyan%20Ros%C3%A9)%20Ultra%20Supervillain) | explicit_alias |
| Vegeta (Super Saiyan God) Ultra Supervillain | [Vegeta (Super Saiyan God) Ultra Supervillain]({{ "/Characters-All/" | relative_url }}?q=Vegeta%20(Super%20Saiyan%20God)%20Ultra%20Supervillain) | exact |
| Broly (Restrained) | [Broly (Restrained)]({{ "/Characters-All/" | relative_url }}?q=Broly%20(Restrained)) | exact |
| Videl (DB Super) | [Videl (DB Super)]({{ "/Characters-All/" | relative_url }}?q=Videl%20(DB%20Super)) | exact |
| Android 18 (DB Super) | [Android 18 (DB Super)]({{ "/Characters-All/" | relative_url }}?q=Android%2018%20(DB%20Super)) | exact |
| Jiren (Full Power, Ultra Supervillain) | [Jiren (Full Power) Ultra Supervillain]({{ "/Characters-All/" | relative_url }}?q=Jiren%20(Full%20Power)%20Ultra%20Supervillain) | explicit_alias |
| Belmod | [God of Destruction Belmod]({{ "/Characters-All/" | relative_url }}?q=God%20of%20Destruction%20Belmod) | explicit_alias |
| Goku (Mini) | [Goku (Mini)]({{ "/Characters-All/" | relative_url }}?q=Goku%20(Mini)) | exact |
| Supreme Kai of Time (Ultra Supervillain) | [Supreme Kai of Time (Ultra Supervillain)]({{ "/Characters-All/" | relative_url }}?q=Supreme%20Kai%20of%20Time%20(Ultra%20Supervillain)) | publisher_confirmed_identity |
| Goku (Ultra Supervillain Quelled) | [Goku (Ultra Supervillain Quelled)]({{ "/Characters-All/" | relative_url }}?q=Goku%20(Ultra%20Supervillain%20Quelled)) | publisher_confirmed_identity |
| Super Saiyan 4 Goku (DAIMA) | [SS4 Goku (DAIMA)]({{ "/Characters-All/" | relative_url }}?q=SS4%20Goku%20(DAIMA)) | explicit_alias |
| Super Saiyan 3 Vegeta (DAIMA) | [SS3 Vegeta (DAIMA)]({{ "/Characters-All/" | relative_url }}?q=SS3%20Vegeta%20(DAIMA)) | explicit_alias |
| Gohan (Beast) | [Gohan (Beast)]({{ "/Characters-All/" | relative_url }}?q=Gohan%20(Beast)) | exact |
| Piccolo (Power Awakening) | [Piccolo (Power Awakening)]({{ "/Characters-All/" | relative_url }}?q=Piccolo%20(Power%20Awakening)) | exact |
| Orange Piccolo | [Orange Piccolo]({{ "/Characters-All/" | relative_url }}?q=Orange%20Piccolo) | exact |

> This is presentation navigation only. The bridge does not create DLC ownership or character relationships.

## Canonical DLC → PQ Reverse Navigation

The canonical DLC identity layer is also exposed here as a player-facing reverse-navigation index. Each entry links directly back into the local PQ explorer using its query contract; these links are derived from `docs/data/dlc/pq-reverse-index.json` and do not create new relationships.

| DLC identity | Canonical PQs |
|---|---|
| Super Pack 1 | [PQ 101]({{ "/Parallel-Quests-All/" | relative_url }}?q=PQ%20101), [PQ 102]({{ "/Parallel-Quests-All/" | relative_url }}?q=PQ%20102), [PQ 103]({{ "/Parallel-Quests-All/" | relative_url }}?q=PQ%20103) |
| Super Pack 2 | [PQ 104]({{ "/Parallel-Quests-All/" | relative_url }}?q=PQ%20104), [PQ 105]({{ "/Parallel-Quests-All/" | relative_url }}?q=PQ%20105), [PQ 106]({{ "/Parallel-Quests-All/" | relative_url }}?q=PQ%20106) |
| Super Pack 3 | [PQ 107]({{ "/Parallel-Quests-All/" | relative_url }}?q=PQ%20107), [PQ 108]({{ "/Parallel-Quests-All/" | relative_url }}?q=PQ%20108), [PQ 109]({{ "/Parallel-Quests-All/" | relative_url }}?q=PQ%20109) |
| Super Pack 4 | [PQ 110]({{ "/Parallel-Quests-All/" | relative_url }}?q=PQ%20110), [PQ 111]({{ "/Parallel-Quests-All/" | relative_url }}?q=PQ%20111), [PQ 112]({{ "/Parallel-Quests-All/" | relative_url }}?q=PQ%20112) |
| Extra Pack 1 | [PQ 113]({{ "/Parallel-Quests-All/" | relative_url }}?q=PQ%20113), [PQ 114]({{ "/Parallel-Quests-All/" | relative_url }}?q=PQ%20114), [PQ 115]({{ "/Parallel-Quests-All/" | relative_url }}?q=PQ%20115), [PQ 116]({{ "/Parallel-Quests-All/" | relative_url }}?q=PQ%20116), [PQ 117]({{ "/Parallel-Quests-All/" | relative_url }}?q=PQ%20117) |
| Extra Pack 2 | [PQ 118]({{ "/Parallel-Quests-All/" | relative_url }}?q=PQ%20118), [PQ 119]({{ "/Parallel-Quests-All/" | relative_url }}?q=PQ%20119), [PQ 120]({{ "/Parallel-Quests-All/" | relative_url }}?q=PQ%20120), [PQ 121]({{ "/Parallel-Quests-All/" | relative_url }}?q=PQ%20121), [PQ 122]({{ "/Parallel-Quests-All/" | relative_url }}?q=PQ%20122) |
| Extra Pack 3 | [PQ 123]({{ "/Parallel-Quests-All/" | relative_url }}?q=PQ%20123), [PQ 124]({{ "/Parallel-Quests-All/" | relative_url }}?q=PQ%20124), [PQ 125]({{ "/Parallel-Quests-All/" | relative_url }}?q=PQ%20125), [PQ 126]({{ "/Parallel-Quests-All/" | relative_url }}?q=PQ%20126), [PQ 127]({{ "/Parallel-Quests-All/" | relative_url }}?q=PQ%20127) |
| Extra Pack 4 | [PQ 128]({{ "/Parallel-Quests-All/" | relative_url }}?q=PQ%20128), [PQ 129]({{ "/Parallel-Quests-All/" | relative_url }}?q=PQ%20129), [PQ 130]({{ "/Parallel-Quests-All/" | relative_url }}?q=PQ%20130), [PQ 131]({{ "/Parallel-Quests-All/" | relative_url }}?q=PQ%20131), [PQ 132]({{ "/Parallel-Quests-All/" | relative_url }}?q=PQ%20132) |
| Ultra Pack 1 | [PQ 133]({{ "/Parallel-Quests-All/" | relative_url }}?q=PQ%20133), [PQ 134]({{ "/Parallel-Quests-All/" | relative_url }}?q=PQ%20134), [PQ 135]({{ "/Parallel-Quests-All/" | relative_url }}?q=PQ%20135), [PQ 136]({{ "/Parallel-Quests-All/" | relative_url }}?q=PQ%20136), [PQ 137]({{ "/Parallel-Quests-All/" | relative_url }}?q=PQ%20137) |
| Ultra Pack 2 | [PQ 138]({{ "/Parallel-Quests-All/" | relative_url }}?q=PQ%20138), [PQ 139]({{ "/Parallel-Quests-All/" | relative_url }}?q=PQ%20139), [PQ 140]({{ "/Parallel-Quests-All/" | relative_url }}?q=PQ%20140), [PQ 141]({{ "/Parallel-Quests-All/" | relative_url }}?q=PQ%20141), [PQ 142]({{ "/Parallel-Quests-All/" | relative_url }}?q=PQ%20142), [PQ 143]({{ "/Parallel-Quests-All/" | relative_url }}?q=PQ%20143) |
| Legendary Pack 1 | [PQ 144]({{ "/Parallel-Quests-All/" | relative_url }}?q=PQ%20144), [PQ 145]({{ "/Parallel-Quests-All/" | relative_url }}?q=PQ%20145), [PQ 146]({{ "/Parallel-Quests-All/" | relative_url }}?q=PQ%20146) |
| Legendary Pack 2 | [PQ 147]({{ "/Parallel-Quests-All/" | relative_url }}?q=PQ%20147), [PQ 148]({{ "/Parallel-Quests-All/" | relative_url }}?q=PQ%20148), [PQ 149]({{ "/Parallel-Quests-All/" | relative_url }}?q=PQ%20149), [PQ 150]({{ "/Parallel-Quests-All/" | relative_url }}?q=PQ%20150) |
| Hero of Justice Pack 1 | [PQ 155]({{ "/Parallel-Quests-All/" | relative_url }}?q=PQ%20155), [PQ 156]({{ "/Parallel-Quests-All/" | relative_url }}?q=PQ%20156), [PQ 157]({{ "/Parallel-Quests-All/" | relative_url }}?q=PQ%20157), [PQ 158]({{ "/Parallel-Quests-All/" | relative_url }}?q=PQ%20158) |
| Hero of Justice Pack 2 | [PQ 159]({{ "/Parallel-Quests-All/" | relative_url }}?q=PQ%20159), [PQ 160]({{ "/Parallel-Quests-All/" | relative_url }}?q=PQ%20160), [PQ 161]({{ "/Parallel-Quests-All/" | relative_url }}?q=PQ%20161), [PQ 162]({{ "/Parallel-Quests-All/" | relative_url }}?q=PQ%20162) |
| Conton City Vote Pack | [PQ 151]({{ "/Parallel-Quests-All/" | relative_url }}?q=PQ%20151), [PQ 152]({{ "/Parallel-Quests-All/" | relative_url }}?q=PQ%20152), [PQ 153]({{ "/Parallel-Quests-All/" | relative_url }}?q=PQ%20153), [PQ 154]({{ "/Parallel-Quests-All/" | relative_url }}?q=PQ%20154) |
| Dragon Ball DAIMA Pack | [PQ 179]({{ "/Parallel-Quests-All/" | relative_url }}?q=PQ%20179), [PQ 180]({{ "/Parallel-Quests-All/" | relative_url }}?q=PQ%20180), [PQ 181]({{ "/Parallel-Quests-All/" | relative_url }}?q=PQ%20181) |
| Future Saga Chapter 1 | [PQ 163]({{ "/Parallel-Quests-All/" | relative_url }}?q=PQ%20163), [PQ 164]({{ "/Parallel-Quests-All/" | relative_url }}?q=PQ%20164), [PQ 165]({{ "/Parallel-Quests-All/" | relative_url }}?q=PQ%20165), [PQ 166]({{ "/Parallel-Quests-All/" | relative_url }}?q=PQ%20166), [PQ 167]({{ "/Parallel-Quests-All/" | relative_url }}?q=PQ%20167), [PQ 168]({{ "/Parallel-Quests-All/" | relative_url }}?q=PQ%20168), [PQ 169]({{ "/Parallel-Quests-All/" | relative_url }}?q=PQ%20169), [PQ 170]({{ "/Parallel-Quests-All/" | relative_url }}?q=PQ%20170), [PQ 171]({{ "/Parallel-Quests-All/" | relative_url }}?q=PQ%20171), [PQ 172]({{ "/Parallel-Quests-All/" | relative_url }}?q=PQ%20172), [PQ 173]({{ "/Parallel-Quests-All/" | relative_url }}?q=PQ%20173), [PQ 174]({{ "/Parallel-Quests-All/" | relative_url }}?q=PQ%20174) |
| Future Saga Chapter 2 | [PQ 175]({{ "/Parallel-Quests-All/" | relative_url }}?q=PQ%20175), [PQ 176]({{ "/Parallel-Quests-All/" | relative_url }}?q=PQ%20176), [PQ 177]({{ "/Parallel-Quests-All/" | relative_url }}?q=PQ%20177), [PQ 178]({{ "/Parallel-Quests-All/" | relative_url }}?q=PQ%20178) |
| Future Saga Chapter 3 | [PQ 182]({{ "/Parallel-Quests-All/" | relative_url }}?q=PQ%20182), [PQ 183]({{ "/Parallel-Quests-All/" | relative_url }}?q=PQ%20183), [PQ 184]({{ "/Parallel-Quests-All/" | relative_url }}?q=PQ%20184) |
| Future Saga Chapter 4 | [PQ 185]({{ "/Parallel-Quests-All/" | relative_url }}?q=PQ%20185), [PQ 186]({{ "/Parallel-Quests-All/" | relative_url }}?q=PQ%20186) |

> This presentation is a navigation consumer, not a second source of truth. If a reverse-index membership is uncertain, the canonical relationship layer and its provenance remain authoritative.


## Canonical DLC Identity Navigation

The machine-readable DLC relationship layer is backed by a standalone canonical identity projection for the **20 DLC targets currently used by canonical PQ relationships**. This projection preserves pack-versus-chapter granularity and does not create additional PQ relationships.

- [Canonical DLC identity records](./data/dlc/canonical-dlc-identity.json)
- [PQ → DLC reverse index](./data/dlc/pq-reverse-index.json)
- [DLC reverse-navigation audit](./data/dlc/pq-reverse-navigation-audit.json)

- [Future Saga content map](./data/future-saga-content-map.json)
- [DLC presentation consumer audit](./data/dlc/dlc-presentation-consumer-audit.json)

The canonical relationship layer remains authoritative. The identity projection exists to make existing `pq_requires_dlc` targets navigable and validator-resolvable; it is not a replacement for the official DLC baseline or a source for new relationships.
