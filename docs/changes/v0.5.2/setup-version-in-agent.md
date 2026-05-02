# Change Document: setup-version-in-agent

**Status**: approved
**Branch**: feature/setup-version-in-agent
**Created**: 2026-04-29
**Author**: Project Manager

---

## Summary

Replace the `.syspilot/version.json` marker file in target projects with a
`version:` field in the Setup Agent's YAML frontmatter. The installed version
is tracked inside `syspilot/agents/syspilot.setup.agent.md` itself — the most
visible artifact. Mode detection (fresh install vs. update) compares the
`version:` frontmatter field against `syspilot/version.json` of the source.

---

## Motivation

- `.syspilot/version.json` is an invisible extra artefact — easy to get out of
  sync when files are copied manually or by `@syspilot.setup`
- The setup agent is always present after installation — it is the natural place
  to carry the version
- Discovered during post-v0.5.1 self-install test preparation

---

## Scope

### Level 0: User Stories

No new User Stories required. The change affects only implementation details
of the Setup Engineer role.

**Impacted:**

| ID | Title | Impact |
|----|-------|--------|
| (Setup-related US) | Setup Engineer user stories | Review only — no text change expected |

---

### Level 1: Requirements

**Impacted:**

| ID | File | Impact |
|----|------|--------|
| SYSP_REQ_INST_* | `docs/syspilot/requirements/req_setup_engineer.rst` | Review mode-detection AC |

---

### Level 2: Design

**Impacted:**

| ID | File | Impact |
|----|------|--------|
| SPEC_SETUP_* | `docs/syspilot/design/spec_setup_engineer.rst` | Replace `.syspilot/version.json` with frontmatter version field |

---

### Implementation

| File | Change |
|------|--------|
| `syspilot/agents/syspilot.setup.agent.md` | Add `version: x.y.z` to YAML frontmatter; update Mode Detection step to read own frontmatter instead of `.syspilot/version.json` |
| `docs/workflows.md` | Update version-tracking description |

---

## Acceptance Criteria

- AC-1: `syspilot/agents/syspilot.setup.agent.md` has `version: 0.5.1` in frontmatter
- AC-2: Setup Agent Mode Detection reads version from own frontmatter (not `.syspilot/version.json`)
- AC-3: `spec_setup_engineer.rst` reflects the new mechanism
- AC-4: No reference to `.syspilot/version.json` remains in agent or spec (only historical mentions in releasenotes/changelog are acceptable)
- AC-5: Sphinx build passes

---

## Out of Scope

- Self-install as Release Workflow step (separate backlog item)
- `release.yml` references to `syspilot/version.json` (that is the source version file, correct and unchanged)
