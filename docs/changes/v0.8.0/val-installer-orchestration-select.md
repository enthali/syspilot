# Validation Report: installer-orchestration-select

**Verification Date:** 2026-07-03
**Verified By:** Verify Engineer
**Status:** ⚠️ **PASSED WITH FINDING** (non-blocking, recommend fix-now or fast-follow)

---

## Summary

This CR implements three already-designed Installer specs (from the abandoned `session-first-orchestration` CR #35): orchestration variant selection, generic Skill mutual-exclusion, and session scaffold creation — closing GH #48 (both orchestration Skills installed) and GH #22 (no session scaffolds ever created). Implementation and UAT are correct and product/instance byte-identical. **One finding:** the fold-in fix to the "Skill Conflict Prevention" Duties bullet was applied only to the agent `.md` files, not to the underlying spec (`spec_installer.rst`), leaving the spec self-contradictory and now also out of sync with its own implementation.

---

## Key Verification Checks

| Check | Result | Evidence |
|-------|--------|----------|
| Orchestration Select Step 5 logic | ✅ PASS | Matches `SYSP_SPEC_INSTALLER_ORCHESTRATION_SELECT` exactly |
| Skill Mutex genericity | ✅ PASS | Generic mechanism; both orchestration SKILL.md files declare `group: orchestration` (product+instance) |
| Session Scaffold Step 9 | ✅ PASS | Matches `SYSP_SPEC_INSTALLER_SESSION_SCAFFOLD`; excludes Bootloader+Installer, preserves existing scaffolds/context.md, skipped for sync |
| Fold-in fix consistency | ⚠️ **FINDING** | Agent files correctly say "replace, not reject"; but `spec_installer.rst`'s own `SYSP_SPEC_INSTALLER_DUTIES` Duties bullet was NOT updated — still says "rejected with a conflict report" |
| Product/instance parity | ✅ PASS | `git diff --no-index` on both installer agent files: zero differences |
| GH #48 / GH #22 regression genuineness | ✅ PASS | Both scenarios directly target the original failure modes |
| sphinx-build -W passes clean | ✅ PASS | 0 warnings, 0 errors |

---

## Detailed Verification

### Check 1: Orchestration Select Step 5 Logic

Compared `SYSP_SPEC_INSTALLER_ORCHESTRATION_SELECT` against both installer agent files' Step 5 "Orchestration Variant Selection" subsection.

- Infer default from `.jarvis/` presence (async if present, sync otherwise) ✅
- Ask the user, offering the inferred default ✅
- Install under mutual exclusion, exactly one orchestration-group Skill afterward ✅

**Finding:** Full match, product and instance identical.

---

### Check 2: Skill Mutex Genericity

- `SYSP_SPEC_INSTALLER_SKILL_MUTEX` describes the mechanism generically: "Before writing a Skill that declares a `group:` field..." — no hardcoding to orchestration.
- Agent files' Step 5 mutex description explicitly states: "This mutual-exclusion mechanism applies generically to any Skill declaring a `group:` field, not only the orchestration Skills."
- Confirmed via grep: `syspilot/skills/syspilot.orchestration-jarvis/SKILL.md`, `syspilot/skills/syspilot.orchestration-subagent/SKILL.md`, and both `.github/skills/` counterparts all declare `group: orchestration` (4/4 files, product+instance).

**Finding:** Genericity confirmed both in spec wording and in the pre-existing Skill frontmatter the CR claims (rather than assumes) already exists.

---

### Check 3: Session Scaffold Step 9

Compared `SYSP_SPEC_INSTALLER_SESSION_SCAFFOLD` against the new Step 9 in both agent files.

- Triggered only when async variant selected; skipped entirely for sync ✅
- Excludes `syspilot.setup.agent.md` (Bootloader) and `syspilot.installer.agent.md` ✅
- Reads `name:`/`agent:` frontmatter fields to populate `session.yaml` ✅
- Existing scaffolds and `context.md` preserved — "only create what is missing" ✅

**Finding:** Full match, product and instance identical.

---

### Check 4: Fold-in Fix Consistency — ⚠️ FINDING

**Claim under test:** The corrected "Skill Conflict Prevention" Duties bullet now matches `SYSP_REQ_SETUP_SKILL_MUTEX` AC-2 (replace, not reject) and no longer contradicts Step 5.

**Agent files** (`syspilot/agents/syspilot.installer.agent.md` and `.github/agents/syspilot.installer.agent.md`, line 39):
> "If a Skill belonging to an exclusive group is being installed and a Skill of the same group already exists, the existing Skill is removed and replaced by the new one — installation always proceeds through replacement, never rejection; the replacement is reported in the run summary"

This correctly matches `SYSP_REQ_SETUP_SKILL_MUTEX` AC-2 ("removes the existing Skill before writing the new one — installation proceeds through replacement, not rejection").

**However**, `docs/syspilot/design/spec_installer.rst`'s `SYSP_SPEC_INSTALLER_DUTIES` node (line 65) still reads:
> "**Skill Conflict Prevention** — If a Skill belonging to an exclusive group is being installed and a Skill of the same group already exists, the installation is rejected with a conflict report"

**Verification of the gap:** Inspected the impl commit `41485b2` directly — it touched only `.github/agents/syspilot.installer.agent.md` and `syspilot/agents/syspilot.installer.agent.md` (2 files, per `git show 41485b2 --stat`). `docs/syspilot/design/spec_installer.rst` was **not** part of this commit or any other commit on this branch.

**Consequence:** `spec_installer.rst` now contains an internal self-contradiction between `SYSP_SPEC_INSTALLER_DUTIES` ("rejected") and `SYSP_SPEC_INSTALLER_SKILL_MUTEX` ("replace") that pre-dates this CR — but this CR's fold-in fix corrected the *implementation* to match the *correct* spec (`SYSP_SPEC_INSTALLER_SKILL_MUTEX`/`SYSP_REQ_SETUP_SKILL_MUTEX` AC-2) without also correcting the *stale* spec bullet (`SYSP_SPEC_INSTALLER_DUTIES`). The agent files are now functionally correct but no longer textually traceable to their own Duties spec bullet.

**Severity:** Medium — does not block functional correctness (the implementation is correct) and does not break sphinx-build (prose contradictions aren't schema violations), but leaves a documented spec/impl drift that a future Trace Engineer run should catch, or that should be closed now while the context is fresh.

**Recommendation:** Fix now — update `SYSP_SPEC_INSTALLER_DUTIES`'s "Skill Conflict Prevention" bullet in `docs/syspilot/design/spec_installer.rst` to match the replace-not-reject language already correctly reflected in `SYSP_SPEC_INSTALLER_SKILL_MUTEX`, `SYSP_REQ_SETUP_SKILL_MUTEX` AC-2, and both agent files. This is a small, low-risk textual fix and this CR's own commit message already correctly diagnoses the contradiction — it simply didn't reach the spec file.

---

### Check 5: Product/Instance Parity

**Method:** `git diff --no-index syspilot/agents/syspilot.installer.agent.md .github/agents/syspilot.installer.agent.md`

**Result:** No output — files are byte-identical.

---

### Check 6: GH #48 / GH #22 Regression Genuineness

**TC-IOS-GH48:** Fresh install fixture, checks exactly one orchestration variant present and the other absent, with an explicit note this fails if "both variants installed unconditionally" recurs — this is precisely GH #48's failure mode.

**TC-IOS-GH22:** Fresh install with `.jarvis/` present, checks `session.yaml` exists on disk for every eligible agent, with an explicit note this fails if "no scaffold ever created" recurs — precisely GH #22's failure mode. Correctly tests the filesystem directly rather than the live Jarvis session list, avoiding a scan-latency false-negative.

**TC-IOS-GENMUTEX:** Uses a synthetic non-orchestration group pair (Skill R1/R2, `group: reporting`) to prove the mutex mechanism generalizes beyond the orchestration case specifically — a good design choice that avoids conflating "mutex works" with "mutex works for orchestration."

**Finding:** All three scenarios are genuine, targeted regression/proof tests, not superficial checks.

---

### Check 7: Sphinx Build Validation

**Command:** `python docs-build.py` (sphinx-build -b html -W)

**Result:**
```
Schema validation completed with 0 warning(s) in 0.116 seconds. Validated 2197 needs/s.
build succeeded.
```

---

## Commits Verified

| Commit | Type | Purpose | Status |
|--------|------|---------|--------|
| `dcc9500` | UAT | 3 scenarios (general mutex, GH #48, GH #22 regressions) | ✅ Verified |
| `41485b2` | Impl | Installer agent Step 5/9 implementation (product+instance) + fold-in fix (agent files only) | ⚠️ Verified with finding |

---

## Final Verdict

⚠️ **PASSED WITH ONE MEDIUM FINDING**

All functional checks pass:
- ✅ Orchestration Select, Skill Mutex genericity, Session Scaffold all correctly implemented and product/instance-identical
- ✅ GH #48 and GH #22 regression tests are genuine
- ✅ sphinx-build -W clean

**One finding requiring CM/PM decision:** the "Skill Conflict Prevention" Duties bullet in `spec_installer.rst` (`SYSP_SPEC_INSTALLER_DUTIES`) was not updated to match the fold-in fix applied to the agent files — spec now under-describes its own corrected implementation. Given the pre-demo urgency, this does not block merge (implementation is functionally correct), but should be fixed now (single-line spec edit) or tracked as an immediate fast-follow before this drift ages into another Trace-Engineer-catches-it-later incident of the same shape as `branching-naming-fix`.

**Recommendation:** Ready for merge; recommend CM route a same-day one-line spec fix to `SYSP_SPEC_INSTALLER_DUTIES`, or explicitly accept-as-is with a backlog entry.

---

*Generated by Verify Engineer*
*Change Document: docs/changes/installer-orchestration-select.md*
*Branch: feature/installer-orchestration-select*
