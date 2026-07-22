# Validation Report: spec-root-cause-principle

**Verification Date:** 2026-07-15
**Verified By:** Verify Engineer
**Status:** ✅ **PASSED**

---

## Summary

Formalizes a spec-root-cause-attribution principle discovered from 3/3 repeated QM review incidents: code-level defects are frequently spec-layer gaps (wrong/missing spec text, or missing cross-links hiding an affected consumer), not pure implementation slips. Adds a verification duty to QM (trace upward before classifying) and an escalation guardrail to Dev Engineer (escalate for spec correction, never patch around a spec-diverging discrepancy). All checks pass.

---

## Key Verification Checks

| Check | Result | Evidence |
|-------|--------|----------|
| Spec/impl consistency | ✅ PASS | Both agent files' new Duty bullets match `SYSP_SPEC_QM_DUTIES`/`SYSP_SPEC_IMPLEMENT_DUTIES` wording exactly |
| Product/instance parity | ✅ PASS | `git diff --no-index` on both agent files (QM, Implement): zero differences |
| Traceability chain | ✅ PASS | `SYSP_US_QM` AC-9 → `SYSP_REQ_QM_DUTIES` AC-8 → `SYSP_SPEC_QM_DUTIES`; `SYSP_US_IMPLEMENT` AC-5 → `SYSP_REQ_IMPLEMENT_DUTIES` AC-5 → `SYSP_SPEC_IMPLEMENT_DUTIES` |
| UAT regression genuineness (AC-3) | ✅ PASS | Independently verified via `git show 87a0472^:...` that the stale preservation logic genuinely existed at that historical commit |
| Pre-existing toctree warnings | ✅ PASS | Confirmed via `git log`/`git show 55164ab` — predates this branch's own commits, not introduced by this CR |
| sphinx-build -W | ✅ PASS (with disclosed pre-existing warnings) | 2 warnings present, both confirmed pre-existing and unrelated |

---

## Detailed Verification

### Check 1: Spec/Impl Consistency

| Agent | Spec Node | Agent File Bullet | Match |
|-------|-----------|---------------------|-------|
| `syspilot.qm` | `SYSP_SPEC_QM_DUTIES` — "Spec-Layer Root-Cause Attribution" | Both `syspilot/agents/syspilot.qm.agent.md` and `.github/agents/syspilot.qm.agent.md`, line 34 | ✅ Verbatim match |
| `syspilot.implement` | `SYSP_SPEC_IMPLEMENT_DUTIES` — "Spec-Divergence Escalation" | Both `syspilot/agents/syspilot.implement.agent.md` and `.github/agents/syspilot.implement.agent.md`, line 29 | ✅ Verbatim match |

**Finding:** Direct text comparison confirms word-for-word consistency between spec and both agent-file locations.

---

### Check 2: Product/Instance Parity

**Method:** `git diff --no-index` between `syspilot/agents/` and `.github/agents/` versions of both `syspilot.qm.agent.md` and `syspilot.implement.agent.md`.

**Result:** No output for either pair — byte-identical.

---

### Check 3: Traceability Chain

| Chain | US | REQ | SPEC |
|-------|----|----|------|
| QM | `SYSP_US_QM` AC-9: "QM traces the defect upward to the spec layer before classifying it as a pure implementation slip" | `SYSP_REQ_QM_DUTIES` AC-8: same content, REQ-level phrasing | `SYSP_SPEC_QM_DUTIES` "Spec-Layer Root-Cause Attribution" bullet |
| Dev Engineer | `SYSP_US_IMPLEMENT` AC-5: "the Dev Engineer escalates for spec correction instead of patching around the discrepancy" | `SYSP_REQ_IMPLEMENT_DUTIES` AC-5: same content, REQ-level phrasing | `SYSP_SPEC_IMPLEMENT_DUTIES` "Spec-Divergence Escalation" bullet |

**Finding:** Both chains are complete and semantically consistent end-to-end; no drift between levels.

---

### Check 4: UAT Regression Genuineness (AC-3 / TC-SRC-REGRESSION)

**Claim under test:** `F-INCIDENT-REPLAY` fixture genuinely replays the `installer-frontmatter-sync` incident using real repo history, not a synthesized scenario.

**Verification performed:**
1. Identified the `installer-frontmatter-sync` implementation commit (`87a0472`) referenced by that CR's Change Document (verified independently by this Verify Engineer in a prior verification pass on 2026-07-03).
2. Ran `git show 87a0472^:syspilot/agents/syspilot.installer.agent.md` — confirmed the parent commit's actual content contained the literal stale logic: *"read the current `tools:` frontmatter value from disk, fetch file from upstream, replace the upstream `tools:` line with the saved value, write the result."*
3. This matches the fixture's description exactly: *"`syspilot.installer.agent.md` Step 4 still describes the retired `tools:`-preservation logic while `SYSP_SPEC_INSTALLER_WORKFLOW` is already corrected."*

**Finding:** The regression scenario is genuine — it replays a real, independently-verifiable historical commit state, not a hypothetical. TC-SRC-REGRESSION would correctly exercise the new QM duty against real prior-incident conditions.

---

### Check 5: Pre-Existing Toctree Warnings

**Claim under test:** 2 warnings (`lean-personas-rich-skills.md`, `which-model-runs-syspilot.md` not in toctree) originate from commit `55164ab`, predating this branch, and were not introduced by any commit in this CR.

**Verification performed:**
1. `git show 55164ab --stat` — confirmed this commit added exactly these two files (`docs(experiences): add lean-personas-rich-skills and which-model-runs-syspilot field notes`).
2. `git log --oneline feature/spec-root-cause-principle -10` — confirmed `55164ab` is the `development`/branch-point commit, appearing **before** all four of this CR's own commits (`6067083`, `d2536fd`, `05edcd1`, `412245f`) in the branch's linear history.
3. Ran a forced full rebuild (`sphinx-build -W --keep-going -E`) — confirmed exactly these 2 warnings occur, both `toc.not_included`, no other warnings.

**Finding:** Confirmed pre-existing and unrelated to this CR's own changes. Correctly disclosed in the CR's own commit message rather than silently ignored.

---

### Check 6: Sphinx Build

**Command:** `sphinx-build -b html . _build/html -W --keep-going -E` (forced full rebuild)

**Result:**
```
lean-personas-rich-skills.md: WARNING: document isn't included in any toctree [toc.not_included]
which-model-runs-syspilot.md: WARNING: document isn't included in any toctree [toc.not_included]
Schema validation completed with 0 warning(s) in 0.098 seconds. Validated 2639 needs/s.
build finished with problems, 2 warnings (with warnings treated as errors).
```

**Assessment:** Both warnings are the pre-existing, disclosed, unrelated items confirmed in Check 5. No new warnings or errors introduced by this CR's own commits (`d2536fd`, `05edcd1`, `412245f`). Schema validation: 0 violations.

---

## Commits Verified

| Commit | Type | Purpose | Status |
|--------|------|---------|--------|
| `d2536fd` | Spec | New duty bullets at US/REQ/SPEC for QM + Dev Engineer | ✅ Verified |
| `05edcd1` | UAT | 3 scenarios incl. genuine regression replay | ✅ Verified |
| `412245f` | Impl | 4 agent files updated (QM + Dev Engineer, product + instance) | ✅ Verified |

---

## Final Verdict

✅ **VERIFICATION PASSED**

All key verification checks met:
- ✅ Spec/impl consistency confirmed via direct text comparison
- ✅ Product/instance byte-parity confirmed via diff
- ✅ Full traceability chain (US→REQ→SPEC) verified for both QM and Dev Engineer
- ✅ UAT regression scenario independently confirmed genuine against real commit history
- ✅ Pre-existing toctree warnings independently confirmed to predate this branch, not introduced by this CR
- ✅ No new sphinx-build warnings/errors from this CR's own commits

**Ready for merge to development.** The 2 pre-existing toctree warnings are a separate, already-disclosed housekeeping item (missing toctree entries for two experience docs) and do not block this CR.

---

*Generated by Verify Engineer*
*Change Document: docs/changes/spec-root-cause-principle.md*
*Branch: feature/spec-root-cause-principle*
