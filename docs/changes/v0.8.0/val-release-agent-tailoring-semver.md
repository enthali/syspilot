# Validation Report: release-agent-tailoring-semver

**Verification Date:** 2026-07-02
**Verified By:** Verify Engineer
**Status:** ✅ **PASSED**

---

## Summary

The "release-agent-tailoring-semver" CR gives the Release Engineer the same Tailoring Workflow pattern already used by PM, correcting the GH #44 incident where syspilot's hardcoded CalVer scheme silently applied to a customer project (Jarvis) requiring semver. The CR also introduces a generic Skill Tailoring architecture, applies it concretely to the branching skill (feature-branch retention, default: retain), fixes two stale attribution rows in the branching Permissions table, and reverts syspilot's own project to semver. All verification checks pass; two scope-bleed incidents during development were correctly identified and discarded before commit, leaving no trace in the CR's history.

---

## Key Verification Checks

| Check | Result | Evidence |
|-------|--------|----------|
| Release Engineer spec/impl consistency | ✅ PASS | Archive-based version source, validate-first ordering, branching-skill delegation identical in spec and both agent files |
| Tailoring Workflow parity vs PM pattern | ✅ PASS | Release Engineer's RESPOND-to-PM escalation matches PM's own documented Tailoring Workflow trigger condition |
| syspilot's own tailoring (semver) | ✅ PASS | `.github/agents/syspilot.release.tailoring.md` specifies semver, correct write-target |
| Skill Tailoring architecture genericity | ✅ PASS | `SYSP_SPEC_SKILL_ARCH_TAILORING` names no specific Skill except in illustrative example |
| Branching skill fixes | ✅ PASS | Hard Rule, Permissions row, retention section, "Workflow Sequence" removal all confirmed |
| UAT AC-5 (GH #44 regression test) | ✅ PASS | TC-RTS-ISOLATION scenario would have caught the original defect |
| No scope-bleed files in CR commits | ✅ PASS | 0 matches for pm.agent.md / pm.tailoring.md / setup.agent.md across all 4 CR commits |
| sphinx-build -W passes clean | ✅ PASS | 0 warnings, 0 errors |

---

## Detailed Verification

### Check 1: Release Engineer Spec/Implementation Consistency

Compared `SYSP_SPEC_RELEASE_WORKFLOW` (docs/syspilot/design/spec_release_engineer.rst) against both `syspilot/agents/syspilot.release.agent.md` and `.github/agents/syspilot.release.agent.md`.

| Aspect | Spec | Product Agent File | Instance Agent File | Match |
|--------|------|---------------------|----------------------|-------|
| Version source-of-truth | Latest `docs/changes/<version>/` archive folder, explicitly not syspilot's own framework version | Identical wording | Identical wording | ✅ |
| Validation ordering | Step 2, before any archival/version-bump | Step 2, before any archival/version-bump | Step 2, before any archival/version-bump | ✅ |
| Merge/back-merge/retention delegation | Steps 7/9/10 delegate to `syspilot.branching` skill, mechanics "not restated here" | Identical delegation language | Identical delegation language | ✅ |
| Preflight tailoring read | Reads `syspilot.release.tailoring.md`; RESPOND to PM if missing | Identical | Identical | ✅ |

**Finding:** Full three-way consistency (spec ↔ product ↔ instance). No drift detected.

---

### Check 2: Tailoring Workflow Parity

Compared Release Engineer's Preflight escalation against PM's own documented Tailoring Workflow trigger (`docs/syspilot/design/spec_project_mgr.rst`).

- PM's `SYSP_SPEC_PM_WORKFLOW` states its own Tailoring Workflow is "triggered when PM's tailoring file is missing, **or when any agent RESPONDs that its tailoring file is missing**."
- Release Engineer's Preflight: "If the file is missing, RESPOND to PM that tailoring is needed."

**Finding:** Exact parity — Release Engineer's escalation is precisely the mechanism PM's own spec documents as the trigger for non-PM agents. No mismatch.

---

### Check 3: syspilot's Own Tailoring File

**File:** `.github/agents/syspilot.release.tailoring.md`

- Confirmed present.
- States "syspilot uses **Semantic Versioning (semver)**: `MAJOR.MINOR.PATCH`" with bump-selection guidance (MAJOR/MINOR/PATCH).
- Version Write-Target section correctly identifies `version:` field in `syspilot/agents/syspilot.setup.agent.md` as the write-target, with an explicit note explaining why this file's dual role (installed-version marker + syspilot's own release marker) is a special case for the syspilot repo itself.

**Finding:** Matches TC-RTS-SYSPILOT-SEMVER expected outcome exactly.

---

### Check 4: Skill Tailoring Architecture Genericity

**File:** `docs/syspilot/design/spec_skill_arch.rst`, node `SYSP_SPEC_SKILL_ARCH_TAILORING`.

- All subsections (File, Format, Behavior, Instance-only, Difference from Agent tailoring) describe the contract generically ("a Skill", "the Skill's documented conventions").
- The only occurrence of `syspilot.branching` is in the illustrative file-path example (`.github/skills/syspilot.branching/tailoring.md`), clearly an example, not a rule-defining reference.
- Applied concretely and correctly to `SYSP_SPEC_SKILL_BRANCHING_RETENTION` (docs/syspilot/design/spec_skill_branching.rst), which links back to `SYSP_SPEC_SKILL_ARCH_TAILORING` and states the retention default (retain) with a tailoring override example.

**Finding:** Architecture is genuinely generic; concrete application is correctly scoped to the branching skill only. Matches TC-RTS-SKILLTAILORING-GENERIC.

---

### Check 5: Branching Skill Fixes

Compared `SYSP_SPEC_SKILL_BRANCHING_PERMISSIONS` / `SYSP_SPEC_SKILL_BRANCHING_STRATEGY` / `SYSP_SPEC_SKILL_BRANCHING_RETENTION` against both `syspilot/skills/syspilot.branching/SKILL.md` and `.github/skills/syspilot.branching/SKILL.md`.

| Item | Spec | Product SKILL.md | Instance SKILL.md | Match |
|------|------|-------------------|---------------------|-------|
| Hard Rule (branch from `development`) | "create a `feature/<name>` branch from `development` first" | Identical wording | Identical wording | ✅ |
| Permissions: `@syspilot.pm` creates feature branches | Fixed (was `@syspilot.design`) | Correct | Correct | ✅ |
| Permissions: `@syspilot.installer` row | Pre-install/final-commit description, no dedicated branch | Correct | Correct | ✅ |
| "Workflow Sequence" section | Removed | Absent (confirmed no such heading) | Absent (confirmed no such heading) | ✅ |
| Feature-branch retention default | Retain (new section) | Present, matches spec | Present, matches spec | ✅ |

**Note (non-blocking, pre-disclosed):** The "Branch Naming Conventions" table in both SKILL.md files still attributes `update/v{version}` to `@syspilot.setup`. This row was **not** in scope for this CR — the Change Document explicitly flags this as a known stale item recommended for a follow-up Trace/MECE audit, not fixed here. Verified this matches the CD's own disclosure; not a defect in this CR's deliverable.

**Finding:** All in-scope fixes verified present and product/instance-synchronized. The one remaining stale row is correctly disclosed as out-of-scope, not silently missed.

---

### Check 6: UAT AC-5 — GH #44 Regression Test

**Scenario:** TC-RTS-ISOLATION (docs/syspilot/design/spec_uat_release_agent_tailoring_semver.rst)

- Uses two independent fixtures: Project A (tailored semver) and Project B (tailored CalVer).
- Checks: Project A's version follows semver and never contains a CalVer-shaped string; Project B's version follows CalVer and never contains a semver-shaped string; neither project's tailoring file changes as a side effect of releasing the other.

**Finding:** This scenario directly targets the original incident's failure mode — a scheme from one project silently leaking into another. The second check item ("Project A's version marker, tag, and archive folder name never contain a CalVer-shaped string") would have caught the original GH #44 defect had it existed beforehand. Confirmed genuine regression coverage, not a superficial test.

---

### Check 7: No Scope-Bleed Files in CR Commits

**Method:** Ran `git show --name-only` on all four CR commits (`31c13e3`, `3a9f228`, `7e6f073`, `04d78ce`) and searched for `pm.agent`, `pm.tailoring`, `setup.agent`.

**Result:** Zero matches. None of the flagged files (`.github/agents/syspilot.pm.agent.md`, `.github/agents/syspilot.pm.tailoring.md`, `.github/agents/syspilot.setup.agent.md`, or their `syspilot/agents/` product counterparts) appear in any commit on this branch's own CR history.

**Finding:** Both disclosed scope-bleed incidents were correctly discarded via `git restore` before committing, exactly as the Change Document states. No committed history is affected.

---

### Check 8: Sphinx Build Validation

**Command:** `python docs-build.py` (sphinx-build -b html -W)

**Result:**
```
Schema validation completed with 0 warning(s) in 0.079 seconds. Validated 3101 needs/s.
build succeeded.
```

**Metrics:** Warnings: 0 | Errors: 0 | Schema violations: 0

---

## Commits Verified

| Commit | Type | Purpose | Status |
|--------|------|---------|--------|
| `31c13e3` | Spec | Release Engineer tailoring redesign + generic Skill Tailoring architecture (L0/L1/L2) | ✅ Verified |
| `3a9f228` | UAT | 7 executable scenarios including GH #44 regression test | ✅ Verified |
| `7e6f073` | Impl | Release Engineer + branching skill (product+instance), new tailoring file | ✅ Verified |
| `04d78ce` | Docs | Disclosed second discarded scope-bleed in Change Document | ✅ Verified |

---

## Issues Noted (Carried Forward, Not Blocking)

- **Stale `update/v{version}` naming row:** Both `SKILL.md` copies and `SYSP_REQ_SKILL_BRANCHING_NAMING` still attribute the `update/v{version}` branch pattern to `@syspilot.setup`, which appears vestigial given this CR's own Permissions-table correction (`@syspilot.installer`, no dedicated branch). Explicitly flagged in the Change Document as out of scope; recommend routing to a follow-up Trace/MECE audit as the CD itself proposes.
- **Two scope-bleed incidents during development** (unrelated PM/tailoring "Parallel CR Drafting" changes, and a stray Setup Bootloader `name:` field addition) were correctly caught and discarded before commit — confirmed via commit-level `git show` inspection, not merely trusting the Change Document's narrative.

Neither item blocks this CR's verification.

---

## Final Verdict

✅ **VERIFICATION PASSED**

All key verification checks met:
- ✅ Release Engineer spec/implementation consistency (product + instance)
- ✅ Tailoring Workflow parity with PM's established pattern
- ✅ syspilot's own tailoring file specifies semver correctly
- ✅ Skill Tailoring architecture is genuinely generic, applied correctly to branching
- ✅ Branching skill fixes (Hard Rule, Permissions, retention, Workflow Sequence removal) confirmed in spec and both SKILL.md copies
- ✅ UAT AC-5 genuinely covers the GH #44 regression scenario
- ✅ No scope-bleed files present in any CR commit
- ✅ sphinx-build -W passes clean

**Ready for merge to development.**

---

*Generated by Verify Engineer*
*Change Document: docs/changes/release-agent-tailoring-semver.md*
*Branch: feature/release-agent-tailoring-semver*
