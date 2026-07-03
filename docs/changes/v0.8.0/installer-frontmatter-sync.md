# Change Document: installer-frontmatter-sync

**Status**: complete
**Branch**: feature/installer-frontmatter-sync
**Created**: 2026-07-03
**Author**: PM
**Operation Mode**: autonomous

---

## Summary

**Critical, high-priority fix** — identified during a pre-demo review of the Installer (partner starts using syspilot+Jarvis Monday). `syspilot.installer.agent.md`'s Step 4 ("Install/Update") still describes the OLD frontmatter-preservation logic: "For each existing file that is NOT `syspilot.setup.agent.md`: read the current `tools:` frontmatter value from disk, fetch file from upstream, replace the upstream `tools:` line with the saved value." This is stale — the `remove-tools-frontmatter` CR (merged earlier) already stripped the `tools:` field entirely from 12 of 13 agent specs, and already corrected the design spec (`SYSP_SPEC_INSTALLER_WORKFLOW` in `spec_installer.rst`) to say "every file is written verbatim from upstream; no local field is preserved." However, the actual `syspilot.installer.agent.md` file (product source AND installed instance) was never updated to match its own already-corrected spec — the Installer that will actually run at install/update time still executes the wrong, pre-CR logic.

Root cause: `remove-tools-frontmatter`'s impact analysis did not surface the Installer's own Step 4 content as an affected consumer of the tools-frontmatter-removal change — a missing-link class of gap, same pattern as GH #46 (assume spec root cause; a missing cross-link hid an affected consumer from impact analysis).

Motivation: this is the literal agent that runs at a customer's install/update, and it currently contradicts its own already-fixed spec. High risk for the Monday demo if a fresh install or update is run.

Acceptance criteria: `syspilot.installer.agent.md` (product source and installed instance) Step 4 wording matches `SYSP_SPEC_INSTALLER_WORKFLOW`'s already-corrected content — verbatim-from-upstream for all files, no `tools:` preservation logic anywhere except the already-correct Setup Bootloader exception. sphinx-build `-W` passes clean.

---

## Level 0: User Stories

**Status**: ✅ completed (N/A)

No User Story change required — this CR is a pure implementation catch-up to an already-corrected spec (`SYSP_SPEC_INSTALLER_WORKFLOW`, corrected by the earlier `remove-tools-frontmatter` CR). No new or modified acceptance criteria at the intent level.

---

## Level 1: Requirements

**Status**: ✅ completed (N/A)

No Requirements change required — `SYSP_REQ_...` chain for the Installer's frontmatter behavior was already corrected by `remove-tools-frontmatter`. This CR only syncs the agent `.md` implementation file to match.

---

## Level 2: Design

**Status**: ✅ completed (N/A)

No Design change required — `SYSP_SPEC_INSTALLER_WORKFLOW` was already corrected by `remove-tools-frontmatter`. This CR brings `syspilot.installer.agent.md` (product + instance) into sync with that already-correct spec.

---

## Final Consistency Check

**Status**: ✅ passed

### Traceability Verification

| User Story | Requirements | Design | Complete? |
|------------|--------------|--------|-----------|
| SYSP_US_INSTALLER | SYSP_REQ_INSTALLER_WORKFLOW | SYSP_SPEC_INSTALLER_WORKFLOW | ✅ (unchanged, already correct) |

### Artefakt-Removal-Check

N/A — no artefact removed. This CR corrects stale prose in an implementation file to match an already-correct spec.

- [x] N/A

### Issues Found

- None.

### Sign-off

- [x] All levels completed (no spec change needed, disclosed as N/A)
- [x] All conflicts resolved
- [x] Traceability verified
- [x] Ready for implementation

---

## UAT

**Status**: ✅ completed

### Summary

Commit `6d3f7c2`. Single focused regression scenario (`SYSP_US_UAT_INSTALLER_FRONTMATTER_SYNC`) confirming both `syspilot.installer.agent.md` copies (product + instance) Step 4 match `SYSP_SPEC_INSTALLER_WORKFLOW`'s already-corrected wording, with no `tools:`-preservation phrasing remaining. Kept deliberately minimal given the pre-demo timeline.

### Issues Found

- None.

---

## Implementation

**Status**: ✅ completed

### Changed Files

| File | Nature |
|------|--------|
| `syspilot/agents/syspilot.installer.agent.md` | Product source — Step 4 wording synced to spec |
| `.github/agents/syspilot.installer.agent.md` | Installed instance — kept in sync |

### Issues Found

- None.

---

## Documentation

**Status**: ✅ completed (no change needed)

### Reviewed, No Change Needed

- `docs/architecture.md` — already correct (updated by the earlier `remove-tools-frontmatter` CR)
- `docs/workflows.md` — no stale Installer-specific claims found

### Issues Found

- None.

---

## QM Findings

*QM writes findings directly into this section after each review round. PM records
decisions (fix-now / defer / accept-as-is) with rationale in the same section.
Multiple review rounds are appended as sub-sections. Existing CDs without this
section are unaffected — the section is additive, never required retroactively.*

### Round 1

**Reviewed by:** Quality Manager
**Review date:** 2026-07-03
**Scope:** Full targeted check — Step 4 sync completeness, whole-file consistency, schema (urgent, pre-demo).

#### Findings

| # | Level | Element ID | Finding | Severity |
|---|-------|------------|---------|----------|
| 1 | Implementation | `syspilot/agents/syspilot.installer.agent.md`, `.github/agents/syspilot.installer.agent.md` (both product source and installed instance) | The **Duties** section retains a stale bullet: "**Local Customization Preservation** — After an update, user customizations (`tools:` fields and other local changes) are either preserved automatically or the user is explicitly informed what needs re-applying." This has zero backing in the current `SYSP_SPEC_INSTALLER_DUTIES` (verified — no such duty exists there) and directly contradicts the Step 4 workflow text in the *same file*, which this CR just corrected to state "no local field is preserved... single source of truth." This is a live, functioning agent file that will run at the partner's Monday demo — it currently instructs/implies the exact opposite of what Step 4 (right below it) says. This is precisely the "partial/incomplete sync" class of gap CM asked QM to check for. | high |

#### Validation Notes

- **Step 4 sync itself**: confirmed correct and complete. Both `syspilot/agents/syspilot.installer.agent.md` and `.github/agents/syspilot.installer.agent.md` Step 4 now reads "For each file in scope, fetch from upstream GitHub and write to `.github/<dir>/<file>`" — matches `SYSP_SPEC_INSTALLER_WORKFLOW` Step 4's corrected content; no `tools:`-preservation phrasing remains in Step 4 specifically. ✅
- **Whole-file consistency check (beyond the CR's narrow stated scope)**: This is what surfaced Finding 1 — the Duties section (a different part of the same file, not touched by this CR) still contains the pre-`remove-tools-frontmatter` preservation language. A secondary, lower-severity remnant was also noted: the spec's own `SYSP_SPEC_INSTALLER_SOUL` **Care:** line ("preserved customizations") is vague/soul-level prose that could still be read charitably (customer-owned files are preserved via orphan-cleanup scoping) — not flagged as a finding, but noted for awareness if a future CR revisits Installer prose.
- **Schema**: sphinx-needs validation — 0 warnings. ✅
- **Traceability**: `SYSP_US_INSTALLER` → `SYSP_REQ_INSTALLER_WORKFLOW` → `SYSP_SPEC_INSTALLER_WORKFLOW` chain unchanged and correct (this CR made no spec-level changes, confirmed accurate). ✅

**Verdict: 1 HIGH finding. Recommend fix-now given Monday demo — this is a two-line deletion (or rewrite) in a file already being edited by this CR, in the exact section CM asked QM to scrutinize for incomplete sync.**

#### PM Decisions

| # | Finding # | Decision | Rationale |
|---|-----------|----------|-----------|
| 1 | 1 | Fix now | The "Local Customization Preservation" Duty has zero basis in SYSP_SPEC_INSTALLER_DUTIES and directly contradicts the Step 4 text this CR just corrected — two adjacent, mutually contradictory statements in the live agent that runs Monday's demo. Trivial deletion, same branch, same file already open. |

---

### Round 2

**Reviewed by:** Quality Manager
**Review date:** 2026-07-03
**Scope:** Re-verification of Round 1 Finding 1 fix (commit `07ed7c3`) + whole-file re-scan for other contradictions (urgent, pre-demo).

#### Findings

No findings.

- **Finding 1 re-check**: The stale "Local Customization Preservation" Duties bullet is fully removed from both `syspilot/agents/syspilot.installer.agent.md` and `.github/agents/syspilot.installer.agent.md` — no replacement text, no orphaned trailing reference. The Duties list now flows directly from "Completeness and Correctness" to "Operability" with no gap or contradiction. **CLOSED.** ✅
- **Whole-file re-scan**: re-grepped both files for `tools:`, `preserv`, and related terms. Only remaining match is the `SYSP_SPEC_INSTALLER_SOUL` **Care:** line ("preserved customizations") — already noted in Round 1 as non-blocking, defensible soul-level prose (customer-owned files are preserved via orphan-cleanup scoping), not a functional contradiction with Step 4. No other contradictions found anywhere in either file. ✅
- **Schema**: sphinx-needs validation — 0 warnings, unchanged. ✅

**Verdict: CLEAN. Finding 1 resolved. No new findings. `installer-frontmatter-sync` is quality-cleared — ready for merge before the Monday demo.**

#### PM Decisions

| # | Finding # | Decision | Rationale |
|---|-----------|----------|-----------|
| — | — | — | No findings — no decisions required. |

## Appendix: Link Discovery Results

```
{paste output from get_need_links.py as needed}
```

---

*Generated by syspilot Change Agent*
