# Mentors (Instructors)

Mentors, also called Masters or Instructors, are special NPCs who teach skills through a sequence of training missions. Mentor progression also feeds into friendship and Partner Gauge systems.

## Mentor Count — Source Reconciliation

There is a source-count discrepancy worth preserving rather than hiding:

- **Bandai Namco official website:** currently advertises **32 mentors**.
- **Community mentor catalog:** lists **33 available mentors**, including DLC.

The database therefore treats the count as a reconciliation item while keeping the individual mentor catalog separate from the marketing headline.

## How Mentor Training Works

Community documentation describes each mentor as providing **four training missions**. The lessons award mentor-specific skills, while friendship progression can unlock additional mentor benefits.

At high friendship, mentors can provide a **Dual Ultimate** and expose a **Partner Gauge**. Friendship can be raised by questing with the mentor, using Dual Ultimate attacks with them, speaking with them in Conton City, and other game-specific interactions.

Mentor availability can depend on:

- Main Story progress
- Advancement Test completion
- Level requirements
- Defeating or locating the mentor in Conton City
- Ownership of the relevant DLC
- Mentor-specific conditions such as collecting costumes

## Canonical Mentor Database

The structured mentor layer is now the source for the live mentor explorer: **33 canonical mentor identities / 133 lesson reward objects / 131 skill rewards / 1 non-skill reward / 131 mentor→skill edge rows / 130 unique canonical skill targets**. One lesson remains intentionally unresolved as a skill endpoint (Hit's Time Skip/Tremor Pulse), while Zamasu's initiation reward is explicitly typed as a Super Soul rather than treated as a missing skill. The explorer preserves these evidence boundaries and links verified lesson skills into the local skill database.

- **[Every Mentor — Live Explorer](Mentors-All.html)** — searchable canonical mentor records and lesson→skill navigation.
- **[Every Skill — Live Explorer](Skills-All.html)** — searchable canonical skill records with mentor→mentor-explorer reverse navigation.

## Cataloged Mentors

The current community catalog contains these 33 entries:

**Base / progression mentors:**
Krillin, Tien, Yamcha, Piccolo, Raditz, Gohan (Kid), Nappa, Vegeta, Zarbon, Dodoria, Captain Ginyu, Frieza (1st Form), Cooler (Final Form), Android 18, Android 16, Cell (Perfect), Lord Slug, Majin Buu, Hercule, Gohan (Adult) & Videl, Gotenks, Turles, Broly, God of Destruction Beerus, Whis, Pan, Jaco, Goku, Gohan (Future), Bardock.

**DLC mentors:**
Hit, Bojack, Zamasu.

## Representative Reward Sets

### Krillin
- Rise to Action
- Orin Combo
- Destructo-Disc
- Scatter Kamehameha
- DUAL Chain Destructo-Disc Barrage

### Vegeta
- Galick Gun
- Finish Breaker
- Flash Strike
- Final Flash
- DUAL Final Flash

### Goku
- Spirit Bomb
- Instant Transmission
- X10 Kamehameha
- Super Kamehameha
- DUAL Super Kamehameha

### Broly
- Blaster Shell
- Blaster Meteor
- Gigantic Omega
- Gigantic Meteor
- DUAL Gigantic Meteor

### Hit
- Time Skip/Flash Skewer
- Time Skip/Back Breaker
- Time Skip/Jump Spike
- Time Skip/Tremor Pulse
- Time Skip/Molotov

### Zamasu
- I'm thinking of becoming a GodTuber. (Z-Soul)
- God Splitter
- Heavenly Arrow
- Instant Severance
- DUAL Instant Severance

## Practical Tips

- Finish the full training sequence for every mentor so no lesson reward is missed.
- Use mentors during quests when possible to build friendship toward their Dual Ultimate.
- DLC mentors require the corresponding DLC and may have additional progression conditions.
- When a mentor's exact unlock condition or reward differs across platform/version, record the condition with a source instead of collapsing it into a generic rule.

## Database Roadmap

The catalog has been normalized into `docs/data/mentors-record-layer.json`, with exact lesson names/order, canonical skill IDs where verified, typed non-skill rewards, source provenance, and a dedicated cross-link report. Remaining work is field-level enrichment (for example exact unlock conditions and additional gameplay metadata) where direct evidence exists; the current explorer does not infer those fields.

**Sources:**
- [Bandai Namco — Dragon Ball Xenoverse 2 official website](https://en.bandainamcoent.eu/dragon-ball/dragon-ball-xenoverse-2)
- [Dragon Ball Xenoverse 2 Wiki — Mentors](https://dbxv2.fandom.com/wiki/Mentors)


## Canonical database navigation

- [Mentors](Mentors-All.html) — searchable mentor records and lesson navigation.
- [Skills](Skills-All.html) — canonical skill records and mentor-skill relationships.
- [Characters](Characters-All.html) — canonical character identities.

These links are navigation surfaces only; they do not establish unresolved relationships or acquisition/mechanics facts.