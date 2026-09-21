# AI Continuation Prompt — Efficiency Addendum

> **Purpose:** This addendum is an append-only operating protocol for free/web-client AI sessions. It is intended to be read together with `docs/AI-CONTINUATION-PROMPT.md` and does not replace or delete any instruction in that file.

## Free/web-client execution protocol

1. **Start with a live census, not historical notes.** Read the handoff, then inspect the current canonical files and compute the smallest relevant counts before choosing work. Historical counts are context only.
2. **Choose one bounded batch per cycle.** Prefer 4–12 closely related records or one deterministic validator/producer invariant. Do not spend a whole context window re-reading unrelated history.
3. **Use a two-pass workflow.** First inspect and research; second edit, validate, and document. Do not mix speculative research with writes.
4. **Prefer repository evidence first.** Search canonical data, schemas, validators, research batches, reverse indexes, and existing source URLs before using web research. Reuse already-verified sources instead of repeatedly rediscovering them.
5. **Research only the fields in scope.** Do not rewrite a whole record or normalize unrelated fields during a bounded pass. Preserve existing values, provenance, conflicts, and `null` where evidence is insufficient.
6. **Keep browser-context work compact.** When web research is needed, search exact record names plus `Xenoverse 2`, inspect a small number of authoritative/independent sources, and record the result immediately. Avoid opening long pages or repeating searches that cannot change the classification.
7. **Stop researching a record when the evidence threshold is reached.** Either make an evidence-backed change or record an evidence boundary/conflict; do not continue browsing merely to force a non-null value.
8. **Batch related writes atomically.** Update the canonical layer, generated/index projection, audit/coverage file, and changelog only when required by the repository contract. Keep a bounded batch internally consistent before committing.
9. **Validate after every write.** Parse changed JSON, recompute the relevant census, compare canonical/index parity, search changed files for internal citation artifacts, and inspect applicable Actions. Never claim CI success when no run/status is exposed.
10. **Use a compact end-of-cycle record.** Before finishing, append a dated entry containing: scope, records/files changed, evidence used, evidence limits, validation result, CI result or unavailable status, current live counts, commit(s), and the exact next batch.
11. **Avoid context waste.** Do not quote or duplicate large historical sections in responses. Refer to file paths, record names, counts, and commit IDs. Re-fetch only the exact files needed for the current batch.
12. **If tools or context are limited, preserve state rather than guessing.** Make a smaller safe batch, update the handoff with the blocked action and next exact step, and stop cleanly.

## Append-only protection

- Never delete, rewrite, summarize away, reorder, or truncate any existing content in `docs/AI-CONTINUATION-PROMPT.md`.
- Add new cycle entries only at the end of that file, preserving all historical notes even when counts are stale; clearly label newer live counts as superseding them.
- If an edit tool cannot safely append while preserving the complete existing file, do not overwrite the file. Create a separate addendum or report the limitation instead.
- Do not “clean up” old wording, old counts, formatting, source conflicts, or historical mistakes by removal. Add a correction or clarification below the existing entry.

## Recommended batch template

```text
### YYYY-MM-DD cycle update — [short scope]
- Live census before editing: [counts].
- Bounded batch: [records/files].
- Research/evidence: [sources and what they establish].
- Changes: [precise fields/files].
- Evidence limits/conflicts preserved: [details].
- Validation: [parse/census/parity/artifact results].
- CI: [run/status result, or explicitly unavailable].
- Commits: [IDs].
- Live census after editing: [counts].
- Exact next batch: [specific records/files and method].
```

## Priority tie-breaker for efficient progress

When several tasks are available, choose the highest-impact task that is: (a) directly supported by existing repository evidence, (b) bounded enough to validate in one web-client session, (c) useful to more than one database or reverse link, and (d) unlikely to require broad schema migration. Prefer fixing a deterministic producer/validator/index mismatch over adding low-confidence descriptive prose.
