# Change Request: docs-version-json-cleanup

**Status**: merged
**Created**: 2026-05-13
**Branch**: feature/docs-version-json-cleanup
**Commit (feature)**: ebdc961
**Merge commit**: 9604a0b

---

## WHY

`docs/architecture.md` and `docs/workflows.md` still referenced `version.json` as an active artefact. The file was intentionally removed in v0.5.3 when the version source was moved to the Setup Agent frontmatter. The stale documentation misleads users and LLMs into believing `version.json` is still part of the product.

---

## WHAT

All references to `version.json` as an active artefact in `docs/architecture.md` and `docs/workflows.md` shall be removed or updated to reflect the current version source: the `version:` field in `syspilot/agents/syspilot.setup.agent.md` frontmatter.

---

## Acceptance Criteria

- `version.json` does not appear as an active artefact in `docs/architecture.md`.
- `docs/workflows.md` version bump step references only the Setup Agent frontmatter.

---

## Files Changed

- `docs/architecture.md` — removed `version.json` from product directory tree; updated "Versioned" property
- `docs/methodology.md` — removed `version.json` from syspilot and sysmlv2 product trees
- `docs/workflows.md` — updated release version bump step

---

## Traceability

Documentation-only fix. No spec or code changes.
