# Change Document: installer-orchestration-select

**Status**: complete
**Branch**: feature/installer-orchestration-select
**Created**: 2026-07-03
**Author**: PM
**Operation Mode**: autonomous

---

## Summary

Implement three already-designed but never-implemented Installer specs, all introduced by the `session-first-orchestration` CR (#35, commit `17c3874`), which completed only Design (L0/L1/L2) and was never carried through UAT/Implementation/Verification/Documentation:

1. **`SYSP_SPEC_INSTALLER_ORCHESTRATION_SELECT`** — the Installer should infer a default orchestration variant from `.jarvis/` presence, ask the user which variant to install, then install exactly the chosen one.
2. **`SYSP_SPEC_INSTALLER_SKILL_MUTEX`** — enforce mutual exclusion for any Skill declaring a `group:` field: replace any existing Skill of the same group rather than letting both coexist.
3. **`SYSP_SPEC_INSTALLER_SESSION_SCAFFOLD`** — when the async variant is selected, create a `.jarvis/sessions/<name>/session.yaml` scaffold for every eligible agent (excluding Bootloader and Installer itself).

Motivation: without this, the Installer currently installs BOTH orchestration Skills on every fresh install (GH #48, discovered ahead of a Monday partner demo), and never creates Jarvis session scaffolds (GH #22). None of this is a coding bug — the specs already fully describe the correct behavior; it was simply never implemented after the specs were written.

Acceptance criteria: a fresh install infers a sensible default variant from `.jarvis/` presence, asks the user to confirm/override, installs exactly one orchestration-group Skill (mutex enforced for any future group-based Skill conflicts too, not just orchestration), and — when the async variant is chosen — creates session scaffolds for every eligible agent. sphinx-build `-W` passes clean. Closes GH #48 and GH #22.

---

## Level 0: User Stories

**Status**: ✅ completed (N/A)

No User Story change required. `SYSP_US_INSTALLER` already covers orchestration variant selection and session scaffolding at the intent level, authored during the abandoned `session-first-orchestration` CR #35. This CR only carries the already-approved intent through Implementation.

---

## Level 1: Requirements

**Status**: ✅ completed (N/A)

No Requirements change required. `SYSP_REQ_SETUP_SKILL_MUTEX`, and the Installer requirements covering orchestration selection and session scaffolding, already exist from CR #35 and were never modified by this CR.

---

## Level 2: Design

**Status**: ✅ completed (N/A)

No Design change required. `SYSP_SPEC_INSTALLER_ORCHESTRATION_SELECT`, `SYSP_SPEC_INSTALLER_SKILL_MUTEX`, and `SYSP_SPEC_INSTALLER_SESSION_SCAFFOLD` already exist in `docs/syspilot/design/spec_installer.rst`, fully wired with `:links:`, from CR #35. This CR implements them; it does not design them.

---

## Final Consistency Check

**Status**: ✅ passed

### Traceability Verification

| User Story | Requirements | Design | Complete? |
|------------|--------------|--------|-----------|
| SYSP_US_INSTALLER | SYSP_REQ_SETUP_SKILL_MUTEX, SYSP_REQ_INSTALLER_WORKFLOW | SYSP_SPEC_INSTALLER_ORCHESTRATION_SELECT, SYSP_SPEC_INSTALLER_SKILL_MUTEX, SYSP_SPEC_INSTALLER_SESSION_SCAFFOLD | ✅ (unchanged, pre-existing from CR #35) |

### Artefakt-Removal-Check

N/A — no artefact removed.

- [x] N/A

### Issues Found

- **Medium finding (Verify Engineer) — resolved:** `SYSP_SPEC_INSTALLER_DUTIES`'s "Skill Conflict Prevention" bullet said installation "is rejected with a conflict report" — contradicted `SYSP_SPEC_INSTALLER_SKILL_MUTEX` (replace, not reject) and the corrected agent files. PM decided fix-now; System Designer corrected the wording to "the existing Skill is replaced by the new one, and the run summary names the replaced Skill" (commit `40e86ab`).

### Sign-off

- [x] All levels completed (N/A — no spec change needed, disclosed above)
- [x] All conflicts resolved (pending PM decision on the one disclosed finding)
- [x] Traceability verified
- [x] Ready for implementation

---

## UAT

**Status**: ✅ completed

### Summary

Commit `dcc9500`. `SYSP_US_UAT_INSTALLER_ORCHESTRATION_SELECT` (+ req/spec) — 3 scenarios: general mutex genericity proof (non-orchestration `group:` pair), GH #48 regression (exactly one variant installed), GH #22 regression (session scaffolds exist on disk). Cross-references the existing `SYSP_US_UAT_INSTALLER_SESSION_FIRST` chain (from abandoned CR #35, now finally executable) rather than duplicating its scenarios.

### Issues Found

- None.

---

## Implementation

**Status**: ✅ completed

### Changed Files

| File | Nature |
|------|--------|
| `syspilot/agents/syspilot.installer.agent.md` | Product source — Step 5 (variant select + skill mutex), new Step 9 (session scaffolds), fold-in fix to stale Duties bullet |
| `.github/agents/syspilot.installer.agent.md` | Installed instance — byte-identical to product source |

### Issues Found

- See Final Consistency Check — medium finding on incomplete fold-in fix (spec not updated to match), routed to PM.

---

## Documentation

**Status**: ✅ completed

### Changed Files

| File | Nature |
|------|--------|
| `docs/architecture.md` | Fixed pre-existing incomplete Skills file-tree listing (missing `syspilot.orchestration-subagent/`); added "Orchestration variant selection" key-property bullet |
| `docs/methodology.md` | Same file-tree fix |

### Reviewed, No Change Needed

- `docs/workflows.md` — no Installer/Setup Agent workflow description exists to update

### Issues Found

- None.

---

## QM Findings

*QM writes findings directly into this section after each review round. PM records
decisions (fix-now / defer / accept-as-is) with rationale in the same section.
Multiple review rounds are appended as sub-sections. Existing CDs without this
section are unaffected — the section is additive, never required retroactively.*

### Round 1

**Reviewed by:** QM
**Review date:** 2026-07-03

#### Findings

None. Independently verified (not relying on the CD narrative alone):

- **No-spec-change premise** — `git diff experimental...feature/installer-orchestration-select -- docs/syspilot/design/spec_installer.rst` shows exactly one hunk: the disclosed "Skill Conflict Prevention" wording fix. `SYSP_SPEC_INSTALLER_ORCHESTRATION_SELECT`, `SYSP_SPEC_INSTALLER_SKILL_MUTEX`, `SYSP_SPEC_INSTALLER_SESSION_SCAFFOLD` are otherwise untouched, confirming they genuinely pre-existed from CR #35.
- **Fix-now correction consistency** — `SYSP_SPEC_INSTALLER_DUTIES`'s corrected "Skill Conflict Prevention" wording (replace, not reject) is consistent with `SYSP_SPEC_INSTALLER_SKILL_MUTEX`'s "Replace" step and with both installer agent files' Duties bullet and Step 5 mutex text; `syspilot/agents/syspilot.installer.agent.md` and `.github/agents/syspilot.installer.agent.md` confirmed byte-identical via `Compare-Object`.
- **GH #48 / GH #22 regression genuineness** — independently confirmed by diffing the pre-CR installer agent file (`git show 57f9a1c:syspilot/agents/syspilot.installer.agent.md`) against terms `orchestration-jarvis|orchestration-subagent|Session Scaffolds|jarvis/sessions`: zero matches, i.e. the pre-CR Installer had no variant-selection or session-scaffold logic at all — the two regressions genuinely existed.
- **UAT cross-reference approach** — reviewed both `SYSP_US_UAT_INSTALLER_ORCHESTRATION_SELECT` (3 new scenarios: general non-orchestration mutex proof, GH #48 regression, GH #22 regression) and the existing `SYSP_US_UAT_INSTALLER_SESSION_FIRST` (5 scenarios: session-path, sync-fallback, mutex-by-replacement, update-preservation, bootstrap-exception). No overlap and no coverage gap — the new chain adds exactly what the old, design-only chain could not previously exercise (general mutex genericity + explicit regression framing).
- **Documentation** — `docs/architecture.md` / `docs/methodology.md` diffs (verified via `Compare-Object` after `git show`, since `git diff` with commit-range args produced no output in this shell session) confirm only the disclosed tree-listing fix and one new "Orchestration variant selection" bullet, accurate against the specs.
- **Traceability** — spot-checked via `needs.json`: all new (`SYSP_US/REQ/SPEC_UAT_INSTALLER_ORCHESTRATION_SELECT`) and referenced pre-existing (`SYSP_SPEC_INSTALLER_ORCHESTRATION_SELECT/SKILL_MUTEX/SESSION_SCAFFOLD`, `SYSP_REQ_SETUP_SKILL_MUTEX`, `SYSP_REQ_INSTALLER_ORCHESTRATION_SELECT/SESSION_SCAFFOLD`) elements have complete, correct links.
- **Schema** — `docs-build.py clean` → "Schema validation completed with 0 warning(s)".

**Verdict:** Clean. No findings raised.

#### PM Decisions

N/A — no findings to decide on.

---

## Appendix: Link Discovery Results

```
{paste output from get_need_links.py as needed}
```

---

*Generated by syspilot Change Agent*
