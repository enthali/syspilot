# Change Request: bootloader-schema-v2

**Status**: designed
**Created**: 2026-05-12
**Author**: PM

---

## WHY

The Setup Bootloader's current design has two misalignments discovered during live testing:

1. **Soul/Guardrail contradiction**: The Bootloader's Soul states "You do not perform any installation yourself" and its Guardrail says "Never install files directly." This is factually wrong — the Bootloader does install files: it writes the Installer agent to disk before invoking it. The current wording creates an inconsistency between the documented behavior and the actual expected behavior.

2. **Schema inflexibility**: `bootstrap.json` currently uses an `entry_point` field that encodes exactly one file path. This cannot accommodate future additions (e.g., supporting scripts, additional bootstrap files) without changing the Bootloader itself. A `files[]` array with explicit `source`/`destination` per entry would make the manifest extensible without requiring a Bootloader update.

The Bootloader's value proposition is that it is the **stable, never-changing** entry point. Its schema must support that promise.

---

## WHAT

- `bootstrap.json` shall use a `files[]` array where each entry has a `source` (repo-relative path) and a `destination` (workspace-relative target folder). The current `entry_point` field is removed.
- The Bootloader's Soul and Guardrail shall correctly reflect that it installs exactly the files listed in `bootstrap.json` — no more, no less.
- The Bootloader's Workflow shall iterate over `files[]`, fetch each file from upstream, and write it to the specified destination.
- The Bootloader's Workflow shall derive the Installer agent name from the written `.agent.md` file and invoke it via `runSubagent()`.
- All affected specs (US, REQ, SPEC for setup/bootloader) shall be updated to match.

---

## Acceptance Criteria

- A user running the Setup Bootloader successfully installs syspilot.
- `bootstrap.json` contains a `files[]` array with `source` and `destination` per entry; no `entry_point` field exists.
- The Bootloader's Soul and Guardrail contain no contradiction with its actual installation behavior.
- Adding a new file to `bootstrap.json` does not require any change to the Bootloader agent itself.
