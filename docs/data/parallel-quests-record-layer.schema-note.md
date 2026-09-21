# Parallel Quest record-layer policy

The PQ record layer is the canonical 186-record endpoint layer for current player-facing PQ numbers 1-186. Every record has a deterministic ID of the form `pq-NNN`, where NNN is the zero-padded player-facing quest number.

The layer is assembled from the maintained numbered PQ record batches plus the early PQ research batches where the numbered record layer did not yet carry equivalent detail. Unresolved values remain null or empty; no record is fabricated solely to fill a field.

A record cannot be promoted to `partially_verified` or `verified` until its objectives, Ultimate Finish conditions, enemy roster, rewards, skill/equipment/Super Soul acquisition and unlock conditions have provenance.

Skill reward edges are synchronized from the maintained PQ research batches so the canonical PQ endpoint can participate in bidirectional PQ ↔ skill relationship validation. Name aliases remain explicit in the relationship validator rather than being silently renamed.

PQ 36 remains a current player-facing numbered record while the older datamined “cut quest” interpretation remains explicit historical provenance; its ID is therefore `pq-036`.
