# Expert Missions

Expert Missions (EMs) are repeatable high-difficulty encounters built around large bosses and mechanics that differ from ordinary Parallel Quests. This page is the **system index**; each mission should eventually receive its own structured record covering its boss, arena, unlock route, objectives, attacks, counterplay, rewards, drops, clear conditions, and version-sensitive behavior.

## Exhaustive Record Standard

Every EM record should capture, where evidence exists:

- canonical mission number and title
- unlock/progression requirement
- Conton City access point and replay route
- boss, forms, phases, and reinforcements
- timer and failure conditions
- player-count and offline/online behavior
- boss health/stamina and phase transitions when independently verified
- special mechanics and status effects
- named raid-style attacks and their exact behavior
- normal rewards, TP Medals, Zeni, EXP, Demon Realm Crystals, and skill drops
- first-clear rewards versus repeat rewards
- DLC/free-update provenance
- version-sensitive mechanics
- source and verification state for every important numerical or technical claim

## Unlock and Mission Count

Current reference material agrees that Expert Missions begin after the Cell portion of the story and that the Supreme Kai of Time introduces tutorial missions before the sequence expands. Current third-party references disagree on the total because they use different scopes: one current guide describes **20** missions, while another describes **17 standard/base-game** missions. The wiki will preserve that distinction until every mission is mapped by provenance rather than forcing one number into all contexts.

Sources also describe progressive mission unlocks and a consolidated replay access point after the early sequence. These progression rules belong in the individual mission records as well as the system index.

## Core Mechanics

### Brainwash Attack

A brainwash mechanic can remove affected players from the normal battlefield and place them into a separate confrontation. Each mission record should identify the boss, trigger, affected players, duration, escape/counter method, and version-specific behavior.

### Scatter Blast

Scatter-style attacks create hazardous Ki objects that can punish teams that ignore them. Record the exact boss, spawn pattern, duration, damage, destruction method, and exceptions instead of reducing the mechanic to a generic warning.

### Gigantic Ki Blast

Some bosses launch a giant Ki projectile requiring a dedicated interception/deflection interaction. Photon Swipe is commonly cited as one response, but the encyclopedia should document the actual interaction and viable alternatives per mission rather than turning a community recommendation into a mandatory rule.

### Peeler Storm

Peeler Storm produces a dangerous multi-hit field of cutting rings. Exact counter windows, immunity behavior, interruption options, and viable skills should be recorded per mission.

### Marbling Drop

Marbling Drop uses tracking projectiles. Each affected mission should document its timing, tracking behavior, damage, interruption rules, and reliable defensive interactions when independently verified.

## Offline vs Online

Expert Missions can be played without a full human team, while offline play relies on CPU allies. Online teams change practical difficulty because players can coordinate counters and revives. These observations belong in a strategy layer; canonical mission fields should describe the actual mechanics first.

## Reward Economy

| Reward category | Required documentation |
|---|---|
| TP Medals | Exact reward where verified; guaranteed vs observed must be separated |
| Zeni | Amount and conditions where verified |
| Experience | Amount/scaling where verified |
| Demon Realm Crystals | Mission, quantity/rate, and version context |
| Skills | Exact skill, mission/boss, acquisition condition, verification state |
| First-clear rewards | One-time rewards and permanent unlocks |
| Repeat rewards | Repeatable currencies/items/drops |

Current guides identify EM 16/17 as common TP Medal farming targets and EM 18 as a strong medal/crystal target. Those are **strategy observations**, not universal rankings, and should remain separate from canonical reward data.

## Cross-System Relationships

Expert Missions connect directly to:

- **TP Medals** → shops, Tosok, purchases, and other services
- **Demon Realm Crystals** → Crystal Raid and related crafting systems
- **Skills** → skill acquisition and research records
- **Story progression** → unlock sequence
- **Conton City** → rifts and replay access
- **Builds** → PvE loadouts and counter testing
- **Raids/Crystal Raids** → related economy and mechanics

## Individual Mission Record Template

```yaml
id: EM-XX
name: ""
source_type: base_game | dlc | free_update | other
unlock_method: ""
access_point: ""
bosses: []
allies: []
mission_timer: null
failure_conditions: []
objectives: []
phases: []
special_mechanics: []
raid_attacks: []
normal_rewards: []
first_clear_rewards: []
repeat_rewards: []
skill_drops: []
demon_realm_crystals: null
tp_medals: null
zeni: null
experience: null
offline_notes: ""
online_notes: ""
pve_notes: ""
known_exceptions: []
verification_status: indexed
last_verified: null
sources: []
```

The production schema should be reconciled with the repository's canonical data conventions rather than creating an incompatible parallel schema.

## Verification Rules

- Never infer a drop rate merely because a guide says a skill can drop.
- Never convert a farming recommendation into a canonical best/worst label.
- Never merge base-game and later/DLC mission counts without recording scope.
- Separate guaranteed rewards from observed/RNG rewards.
- Keep boss mechanics separate from player strategy.
- Preserve version-sensitive values and source disagreements.
- Prefer publisher material for release/DLC provenance and in-game/independent evidence for exact mechanics and rewards.
- Record known unknowns instead of inventing missing values.

## Research State

This page establishes the EM information architecture; it does **not** claim that every Expert Mission has already been exhaustively verified. The next EM data pass should build individual records and cross-link every boss, attack, reward, skill drop, currency interaction, and unlock condition.

## Research References

- [Current Expert Mission reference](https://dragonballxenoverse2.wiki/guides/expert-missions/)
- [Independent Expert Mission unlock reference](https://www.dragon-ball-xenoverse-2.wiki/fr/builds/dragon-ball-xenoverse-2-how-to-unlock-expert-missions)
