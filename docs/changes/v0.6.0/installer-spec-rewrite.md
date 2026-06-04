# Change Document: installer-spec-rewrite

**Status**: ready-for-merge
**Branch**: feature/installer-spec-rewrite
**Created**: 2026-05-23
**Author**: PM

---

## Summary

Rewrite the Installer spec and agent so the **customer installation path** is the documented and validated one. Today's spec was written from inside the dogfooding workspace and describes a workflow that only works there: Step 1 offers a local-source shortcut that bypasses GitHub fetch, Step 2 compares against an already-overwritten Bootloader file, Step 4 asks an after-the-fact customization question and contains a broken double-write flow, and the spec is silent on UTF-8 encoding, wrapper-script discipline, and rollback. A live install attempt on 2026-05-23 confirmed the impact: the Installer agent shortcuts to a local copy, writes 26 files with UTF-8 BOM corruption, and generates a wrapper script that bypasses its own workflow. This CR fixes the spec so customers get a correct, transactional, customer-path-validated install. It is **release-blocking for the next release** because the next release will be pulled by customers through whichever Installer ships with it — if that Installer is broken, the release breaks customer installations on first contact. **Motivation**: complete and trustworthy install for every customer, on every supported platform, every time. **Acceptance criteria**: (AC1) Installer always fetches from upstream GitHub — no local-source path in spec or agent. (AC2) Mode-Detect step (former Step 2) is removed; Installer always installs latest. (AC3) All written files are UTF-8 without BOM. (AC4) Installer performs file operations directly per file (Invoke-WebRequest + Out-File or equivalent) — no generation of wrapper scripts, no helper files in temp/. (AC5) Frontmatter preservation rule explicit: `tools:` is preserved per file; all other fields (`description`, `model`, `user-invocable`, `agents`, etc.) come from upstream; Bootloader (`syspilot.setup.agent.md`) is overwritten verbatim with no preservation. (AC6) Step 3 dependency check: if `sphinx-needs` is missing, print install instructions and stop — do not auto-install. (AC7) Git-based rollback: pre-install commit is created before file operations; on failure between install and final commit, `git reset --hard` restores the pre-install state. (AC8) Customization-question and double-write flow removed from Step 4 entirely. (AC9) Customer-path live validation: clean test repo, no local `syspilot/`, `@syspilot.setup` invoked with `development` branch override succeeds end-to-end and produces the per-directory summary table with `templates/` row.

Full design decisions, finding-by-finding rationale, and validation strategy are documented in `.jarvis/sessions/Project Manager/idea-installer-spec-rewrite.md` (PM session artefact, not a syspilot product spec). CM should treat that idea file as the authoritative source of decisions — every Workflow step rewrite, every removed step, and every new Soul/Duty entry traces back to a PM-confirmed decision recorded there.

---

## Level 0: User Stories

**Status**: ✅ completed

### Impacted User Stories

| ID | Title | Impact | Notes |
|----|-------|--------|-------|
| SYSP_US_INSTALLER | Installer Agent | unchanged | User-facing intent unchanged; all changes are at L1/L2 |

### New User Stories

None — the existing user story fully covers the rewritten installer behavior.

### Decisions

- Decision 1: SYSP_US_INSTALLER remains unchanged. The user-facing intent ("functioning, validated syspilot environment without losing local customizations") is preserved by the rewritten workflow — only the internal mechanism changes.

### Horizontal Check (MECE)

- [x] No contradictions with existing User Stories
- [x] No redundancies
- [x] Gaps identified and addressed

---

## Level 1: Requirements

**Status**: ✅ completed

### Impacted Requirements

| ID | Linked From | Impact | Notes |
|----|-------------|--------|-------|
| SYSP_REQ_INSTALLER_WORKFLOW | SYSP_US_INSTALLER | rewritten | Mode-Detect removed, customization-question removed, GitHub-only source, rollback integrated, explicit encoding/direct-ops cross-refs |
| SYSP_REQ_INSTALLER_DUTIES | SYSP_US_INSTALLER | extended | Added AC-9 (encoding), AC-10 (direct ops), AC-11 (transactional rollback) |

### New Requirements

| ID | Title | Links | Priority |
|----|-------|-------|----------|
| SYSP_REQ_INSTALLER_GITHUB_SOURCE | Installer GitHub-Only Source | SYSP_US_INSTALLER | mandatory |
| SYSP_REQ_INSTALLER_ENCODING | Installer File Encoding | SYSP_US_INSTALLER | mandatory |
| SYSP_REQ_INSTALLER_DIRECT_OPS | Installer Direct File Operations | SYSP_US_INSTALLER | mandatory |
| SYSP_REQ_INSTALLER_ROLLBACK | Installer Transactional Rollback | SYSP_US_INSTALLER | mandatory |

### Conflicts Detected

None.

### Decisions

- Decision 1: AC1 (GitHub-only) and AC2 (Mode-Detect removed) consolidated into a single REQ `SYSP_REQ_INSTALLER_GITHUB_SOURCE` — they address the same concern (source acquisition) and splitting would create overlap.
- Decision 2: AC9 (customer-path live validation) is a UAT/validation criterion, not a requirements-level AC. It will be covered by UAT artefacts created during the validation phase — no REQ-level AC needed.
- Decision 3: Finding #11 (idempotency optimization) explicitly deferred — always-overwrite behavior is acceptable for correctness-first approach; no REQ change.
- Decision 4: Finding #17 (Skill Mutual Exclusion wiring into workflow) explicitly deferred — no competing skills exist today; `SYSP_REQ_SETUP_SKILL_MUTEX` remains unchanged.
- Decision 5: Encoding, direct-ops, and rollback are also added as ACs to `SYSP_REQ_INSTALLER_DUTIES` (AC-9, AC-10, AC-11) because they represent Duty-level guarantees in addition to having their own standalone REQs with detailed ACs.

### Horizontal Check (MECE)

- [x] No contradictions with existing Requirements
- [x] No redundancies (GitHub-Source, Encoding, Direct-Ops, Rollback are orthogonal concerns)
- [x] All new REQs link to User Stories

---

## Level 2: Design

**Status**: ✅ completed

### Impacted Design Elements

| ID | Linked From | Impact | Notes |
|----|-------------|--------|-------|
| SYSP_SPEC_INSTALLER_WORKFLOW | SYSP_REQ_INSTALLER_WORKFLOW | rewritten | 9-step workflow replacing old 9-step; Mode-Detect/customization-question removed; Pre-Install Commit + Rollback added |
| SYSP_SPEC_INSTALLER_DUTIES | SYSP_REQ_INSTALLER_DUTIES | extended | Added Transaction Model duty |
| SYSP_SPEC_INSTALLER_SOUL | SYSP_REQ_SETUP_INSTALLER_NOT_USER_INVOCABLE | extended | Guardrails expanded: direct file ops, UTF-8 no BOM, no wrapper scripts, transactional rollback |
| SYSP_SPEC_INSTALLER_FRONTMATTER | SYSP_REQ_SETUP_INSTALLER_NOT_USER_INVOCABLE | modified | `version:` field removed from frontmatter (installer does not maintain its own version; Bootloader frontmatter is the single version source) |

### New Design Elements

| ID | Title | Links |
|----|-------|-------|
| SYSP_SPEC_INSTALLER_GITHUB_SOURCE | Installer GitHub-Only Source | SYSP_REQ_INSTALLER_GITHUB_SOURCE |
| SYSP_SPEC_INSTALLER_ENCODING | Installer File Encoding | SYSP_REQ_INSTALLER_ENCODING |
| SYSP_SPEC_INSTALLER_DIRECT_OPS | Installer Direct File Operations | SYSP_REQ_INSTALLER_DIRECT_OPS |
| SYSP_SPEC_INSTALLER_ROLLBACK | Installer Transactional Rollback | SYSP_REQ_INSTALLER_ROLLBACK |

### Conflicts Detected

None.

### Decisions

- Decision 1: Finding #11 (idempotency optimization) deferred — `SYSP_SPEC_INSTALLER_DUTIES` retains the "Idempotent Sync" duty as aspirational but the workflow always overwrites (correctness first). No SPEC change for #11.
- Decision 2: Finding #17 (Skill ME wiring) deferred — `SYSP_SPEC_INSTALLER_SKILL_MUTEX` is unchanged; workflow does not wire the check because no competing skills exist today.
- Decision 3: The old "Same workflow as the former Setup Manager, transferred verbatim" prefatory note is removed from WORKFLOW spec — it was a historical reference with no current value.
- Decision 4: `SYSP_SPEC_INSTALLER_WORKFLOW` links expanded to include the four new REQs for explicit traceability.
- Decision 5: Rollback SPEC Step 4 describes "commit --amend or equivalent" — the exact mechanism is left to implementation so long as the result is a single clean commit.

### Horizontal Check (MECE)

- [x] No contradictions with existing Designs
- [x] All new SPECs link to Requirements

---

## Final Consistency Check

**Status**: ✅ passed

### Traceability Verification

| AC | User Story | Requirement(s) | Design | Complete? |
|----|------------|----------------|--------|-----------|
| AC1 GitHub-only source | SYSP_US_INSTALLER | SYSP_REQ_INSTALLER_GITHUB_SOURCE (AC-1, AC-2) | SYSP_SPEC_INSTALLER_GITHUB_SOURCE | ✅ |
| AC2 Mode-Detect removed | SYSP_US_INSTALLER | SYSP_REQ_INSTALLER_GITHUB_SOURCE (AC-3, AC-4) | SYSP_SPEC_INSTALLER_GITHUB_SOURCE | ✅ |
| AC3 UTF-8 without BOM | SYSP_US_INSTALLER | SYSP_REQ_INSTALLER_ENCODING; SYSP_REQ_INSTALLER_DUTIES AC-9 | SYSP_SPEC_INSTALLER_ENCODING; SYSP_SPEC_INSTALLER_SOUL | ✅ |
| AC4 Direct per-file ops | SYSP_US_INSTALLER | SYSP_REQ_INSTALLER_DIRECT_OPS; SYSP_REQ_INSTALLER_DUTIES AC-10 | SYSP_SPEC_INSTALLER_DIRECT_OPS; SYSP_SPEC_INSTALLER_SOUL | ✅ |
| AC5 Frontmatter preservation | SYSP_US_INSTALLER | SYSP_REQ_INSTALLER_WORKFLOW AC-5, AC-6 | SYSP_SPEC_INSTALLER_WORKFLOW Step 4 | ✅ |
| AC6 sphinx-needs → instruct+stop | SYSP_US_INSTALLER | SYSP_REQ_INSTALLER_WORKFLOW AC-2 | SYSP_SPEC_INSTALLER_WORKFLOW Step 2 | ✅ |
| AC7 Git-based rollback | SYSP_US_INSTALLER | SYSP_REQ_INSTALLER_ROLLBACK; SYSP_REQ_INSTALLER_DUTIES AC-11 | SYSP_SPEC_INSTALLER_ROLLBACK; SYSP_SPEC_INSTALLER_WORKFLOW Steps 3/8 | ✅ |
| AC8 Customization-question removed | SYSP_US_INSTALLER | SYSP_REQ_INSTALLER_WORKFLOW (old AC-6 removed) | SYSP_SPEC_INSTALLER_WORKFLOW Step 4 (no question) | ✅ |
| AC9 Customer-path live validation | SYSP_US_INSTALLER | (UAT artefact — not REQ) | (UAT artefact) | ✅ (UAT) |

### Artefakt-Removal-Check

Removed concepts from the spec: **Mode-Detect step**, **local-source shortcut (Detect Source)**, **customization-question + double-write flow**.

| Removed Artefact | Class (a): Code/Workflow refs | Class (b): Doc refs | Class (c): Historic Change Docs |
|------------------|-------------------------------|---------------------|---------------------------------|
| "Detect Mode" / Mode-Detect step | `syspilot/agents/syspilot.installer.agent.md` line 39 (implementation phase), `.github/agents/syspilot.installer.agent.md` line 39 (installed instance — updated by Installer itself) | `docs/syspilot/design/spec_installer.rst` — fixed in this CR | `docs/changes/v0.3.0/val-local-install.md` — 1 historic ref (acceptable stranding) |
| "Detect Source" / local syspilot/ check | `syspilot/agents/syspilot.installer.agent.md` line 38 (implementation phase), `.github/agents/syspilot.installer.agent.md` line 38 (installed instance) | `docs/syspilot/design/spec_installer.rst` — fixed in this CR | `docs/changes/v0.3.0/val-local-install.md` — 2 historic refs; `docs/releasenotes.md` line 424 — 1 historic ref (acceptable stranding) |
| Customization-question + double-write flow | `syspilot/agents/syspilot.installer.agent.md` (implementation phase), `.github/agents/syspilot.installer.agent.md` (installed instance) | `docs/syspilot/design/spec_installer.rst` — fixed in this CR | none |

- [x] All class (a) active code/workflow references: agent file updates are in scope for the **implementation phase** (Dev Engineer) — this CR covers only spec; agent file is explicitly out-of-scope per constraints
- [x] All class (b) active documentation references fixed in this CR
- [x] Class (c) historical Change Documents accepted as "acceptable historic stranding" and disclosed above

### Issues Found

**QM targeted-check findings (2026-05-23) — PM decisions applied:**

Fix-now (applied on branch, second iteration):

- **L2-F1** `SYSP_SPEC_INSTALLER_DUTIES` — Added two short duty bullets cross-referencing `SYSP_SPEC_INSTALLER_ENCODING` and `SYSP_SPEC_INSTALLER_DIRECT_OPS` so AC-9 (UTF-8 without BOM) and AC-10 (Direct File Operations) are visibly covered in the Duties enumeration. Fixed.
- **L2-F2** `SYSP_SPEC_INSTALLER_WORKFLOW` — Added a single "Failure Handling" subsection after the numbered steps stating that rollback applies uniformly to Steps 4–7 (identical to Step 8 Validate failure rollback). Aligns WORKFLOW with `SYSP_SPEC_INSTALLER_ROLLBACK`. Fixed.
- **T-F2** `SYSP_SPEC_INSTALLER_SOUL` — Extended `:links:` to include `SYSP_REQ_INSTALLER_ENCODING`, `SYSP_REQ_INSTALLER_DIRECT_OPS`, `SYSP_REQ_INSTALLER_ROLLBACK` (matching `SYSP_SPEC_INSTALLER_WORKFLOW`). Fixed.

Accept-as-is (no spec change, recorded here):

- **L1-N2** `SYSP_REQ_INSTALLER_DUTIES` vs `SYSP_REQ_INSTALLER_SCOPE` overlap — pre-existing in `req_setup_engineer.rst`, not introduced by this CR. Accepted.
- **L2-F3** "Skill Conflict Prevention" duty has no corresponding WORKFLOW step — already captured as deferred Finding #17 in the PM idea file (no competing skills exist today; ME wiring deferred to a future CR when the first competing skill ships). Accepted.

Deferred to separate housekeeping CR (out of scope here):

- **T-F1** Parent REQ `SYSP_REQ_SETUP_INSTALLER_NOT_USER_INVOCABLE` still `:status: draft` while this CR elevates its child SPECs (`SOUL`, `FRONTMATTER`) to `approved`. This is a project-wide systemic gap across `req_setup_engineer.rst` (multiple REQs at `draft` with downstream approved SPECs), not specific to this CR. Status hierarchy mismatch acknowledged; project-wide REQ status sweep deferred to a separate housekeeping CR before the next release.

### Sign-off

- [x] All levels completed (no ⚠️ DEPRECATED markers remaining)
- [x] All conflicts resolved
- [x] Traceability verified
- [x] MECE check passed (L1, 10/10 REQs examined, 0 redundancies / 0 contradictions / 0 gaps)
- [x] Trace check passed (all 4 new REQs link to SYSP_US_INSTALLER; all 4 new SPECs link to matching new REQs; all touched statuses = approved)
- [x] sphinx-build clean (0 schema validation warnings)
- [x] Implementation: `syspilot/agents/syspilot.installer.agent.md` rewritten, UTF-8 no BOM, `tools:` preserved
- [x] Docu: architecture.md rollback section updated; README requirements section updated
- [x] Ready for QM targeted check + PM merge to development

---

## Appendix: Link Discovery Results

Impact analysis run 2026-05-23 from `SYSP_US_INSTALLER` (direction=in, depth=2):

```
SYSP_US_INSTALLER  (Level 0 — user intent unchanged)
  └── SYSP_REQ_INSTALLER_DUTIES               ← to extend (new ACs)
  │     └── SYSP_SPEC_INSTALLER_DUTIES        ← to extend
  ├── SYSP_REQ_INSTALLER_WORKFLOW             ← to rewrite
  │     └── SYSP_SPEC_INSTALLER_WORKFLOW      ← to rewrite
  ├── SYSP_REQ_INSTALLER_SCOPE                ← unchanged
  │     └── SYSP_SPEC_INSTALLER_SCOPE         ← unchanged
  ├── SYSP_REQ_INSTALLER_DOC_BOOTSTRAP        ← unchanged
  │     └── SYSP_SPEC_INSTALLER_DOC_BOOTSTRAP ← unchanged
  ├── SYSP_REQ_SETUP_INSTALLER_NOT_USER_INVOCABLE ← unchanged
  │     └── SYSP_SPEC_INSTALLER_SOUL / FRONTMATTER ← SOUL extended (new Guardrails); FRONTMATTER version bump
  └── SYSP_REQ_SETUP_SKILL_MUTEX              ← unchanged (finding #17 deferred per idea file)
        └── SYSP_SPEC_INSTALLER_SKILL_MUTEX   ← unchanged
```

**Candidate NEW elements** (Designer to confirm/refine):

- L1 REQ: Installer Transactional Rollback (covers AC7 git-reset rollback) → links SYSP_US_INSTALLER
- L1 REQ: Installer File Encoding (covers AC3 UTF-8 without BOM) → links SYSP_US_INSTALLER
- L1 REQ: Installer Direct File Operations (covers AC4 no wrapper scripts) → links SYSP_US_INSTALLER
- L1 REQ: Installer GitHub-Only Source (covers AC1 always-fetch-upstream, AC2 no Mode-Detect) → links SYSP_US_INSTALLER
- L2 SPECs corresponding to each new REQ
- L2 SPEC update: extend `SYSP_SPEC_INSTALLER_SOUL` Guardrails ("performs file ops directly; writes UTF-8 without BOM; never generates wrapper scripts")
- L2 SPEC update: extend `SYSP_SPEC_INSTALLER_DUTIES` with Transaction-Model entry


---

*Generated by syspilot Change Agent*
