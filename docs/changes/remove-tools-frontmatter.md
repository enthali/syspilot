# Change Document: remove-tools-frontmatter

**Status**: complete
**Branch**: feature/remove-tools-frontmatter
**Created**: 2026-07-01
**Author**: PM
**Operation Mode**: user-guided

---

## Summary

Remove the `tools:` frontmatter field entirely from all syspilot agent specs, and retire the central `SYSP_SPEC_AGENT_BASE_TOOLSET` spec (and its references in every per-agent `SYSP_SPEC_*_FRONTMATTER` spec) that currently prescribes a common base toolset. Motivation: the VS Code custom-agent tool picker has proven unstable in practice — enumerated and categorized tool lists in agent frontmatter get silently rewritten, dropped, or left unchanged across saves and window reloads, independent of any syspilot action. Maintaining a prescribed toolset in agent specs no longer reflects a controllable reality. Instead, agents should inherit whatever tools are enabled on the user's default agent in VS Code — one place for the user to manage, no drift to maintain in specs. Acceptance criteria: no syspilot agent spec or installed agent file contains a `tools:` frontmatter key; agents function correctly using the default agent's tool selection; the user is clearly informed (via documentation and/or an Installer check) that `enthali.jarvis-core` must be enabled on their default agent for syspilot orchestration to work, since without it agents silently lose orchestration capability rather than failing loudly.

---

## Level 0: User Stories

**Status**: ✅ completed

### Impacted User Stories

| ID | Title | Impact | Notes |
|----|-------|--------|-------|
| SYSP_US_AGENT_ARCH | Clean Agent Architecture | modified | AC-6 rewritten: no `tools:` field prescribed (except Setup Bootloader); agent inherits the user's default VS Code agent tool selection |
| SYSP_US_DOC_EXTERNAL | External Documentation | modified | New AC-6: documentation must state `enthali.jarvis-core` must be enabled on the user's default agent for orchestration to work |

### New User Stories

None.

### Decisions

- Root cause: the VS Code custom-agent tool picker is unstable in practice — it silently rewrites/drops enumerated tool lists independent of any syspilot action. Prescribing an exact `tools:` list in spec fights a mechanism syspilot does not control.
- Resolution: retire the prescriptive base-toolset model. Agents inherit whatever tools are enabled on the user's default VS Code agent — one place for the user to manage, no drift to maintain in specs.
- **Judgment call (flagged):** the Setup Bootloader is the sole exception and keeps an explicit `tools:` field. Its single synchronous `agent/runSubagent` call to the Installer is a structural bootstrap mechanism, not a customization surface — if that tool isn't enabled by default, the install/update entry point breaks outright. This mirrors the existing precedent that the Bootloader/Installer are already treated as exceptions to the session-identity model.

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
| SYSP_REQ_AGENT_ARCH_FRONTMATTER | SYSP_US_AGENT_ARCH | modified | AC-3 rewritten (no `tools:` except Setup); removed old AC-10/AC-11/AC-12 (base toolset, no-memory, runSubagent-Setup-only — folded into new AC-10); rationale explains VS Code picker instability |
| SYSP_REQ_CM_FRONTMATTER | SYSP_US_CM | modified | AC-3: no `tools:` field |
| SYSP_REQ_QM_FRONTMATTER | SYSP_US_QM | modified | AC-3: no `tools:` field |
| SYSP_REQ_PM_FRONTMATTER | SYSP_US_PM | modified | AC-3: no `tools:` field |

### New Requirements

None.

### Conflicts Detected

None.

### Decisions

- `SYSP_REQ_SETUP_FRONTMATTER` AC-3 (explicit tools list including `agent/runSubagent`) required **no change** — it was already the Setup Bootloader's own hardcoded list, independent of the base-toolset mechanism being retired.
- `SYSP_REQ_SETUP_INSTALLER_NOT_USER_INVOCABLE` (Installer L1) never referenced `tools:` — no change needed.

### Horizontal Check (MECE)

- [x] No contradictions with existing Requirements
- [x] No redundancies
- [x] All modified REQs link to their User Story

---

## Level 2: Design

**Status**: ✅ completed

### Impacted Design Elements

| ID | Linked From | Impact | Notes |
|----|-------------|--------|-------|
| SYSP_SPEC_AGENT_ARCH_FRONTMATTER | SYSP_REQ_AGENT_ARCH_FRONTMATTER | modified | `tools` field redefined as optional/Setup-only; example and constraint text updated |
| SYSP_SPEC_CM_FRONTMATTER | SYSP_REQ_CM_FRONTMATTER | modified | `tools:` line + base-toolset link removed |
| SYSP_SPEC_PM_FRONTMATTER | SYSP_REQ_PM_FRONTMATTER | modified | `tools:` line + base-toolset link removed |
| SYSP_SPEC_QM_FRONTMATTER | SYSP_REQ_QM_FRONTMATTER | modified | `tools:` line + base-toolset link removed |
| SYSP_SPEC_DESIGN_FRONTMATTER | SYSP_REQ_DESIGN_FRONTMATTER | modified | `tools:` line + base-toolset link removed |
| SYSP_SPEC_IMPLEMENT_FRONTMATTER | SYSP_REQ_IMPLEMENT_FRONTMATTER | modified | `tools:` line + base-toolset link removed |
| SYSP_SPEC_DOCU_FRONTMATTER | — | modified | `tools:` line + base-toolset link removed |
| SYSP_SPEC_UAT_FRONTMATTER | — | modified | `tools:` line + base-toolset link removed |
| SYSP_SPEC_MECE_FRONTMATTER | — | modified | `tools:` line + base-toolset link removed |
| SYSP_SPEC_TRACE_FRONTMATTER | — | modified | `tools:` line + base-toolset link removed |
| SYSP_SPEC_VERIFY_FRONTMATTER | — | modified | `tools:` line + base-toolset link removed |
| SYSP_SPEC_RELEASE_FRONTMATTER | — | modified | `tools:` line + base-toolset link removed |
| SYSP_SPEC_INSTALLER_FRONTMATTER | — | modified | `tools:` line + base-toolset link removed |
| SYSP_SPEC_SETUP_FRONTMATTER | — | modified | `tools:` rewritten as explicit hardcoded list (its sole exception); base-toolset link removed |

### Removed Design Elements

| ID | Title | Reason |
|----|-------|--------|
| SYSP_SPEC_AGENT_BASE_TOOLSET | Agent Base Toolset | Retired — the prescriptive base-toolset model is replaced by inheritance from the user's default VS Code agent |

### Conflicts Detected

None.

### Decisions

- The Setup Bootloader's frontmatter spec now carries the same explicit tool list as its own L1 req (`SYSP_REQ_SETUP_FRONTMATTER` AC-3) directly, rather than referencing a shared base-toolset spec — it never depended on the base toolset content, only borrowed its wording.

### Horizontal Check (MECE)

- [x] No contradictions with existing Designs
- [x] All modified specs trace to their Requirements
- [x] No dangling `:links:` to the removed spec (verified via grep — zero `:links:` directives referenced it; remaining prose mentions are in historic UAT test artifacts, see Artefakt-Removal-Check)

---

## Final Consistency Check

**Status**: ✅ passed

### Traceability Verification

| User Story | Requirements | Design | Complete? |
|------------|--------------|--------|-----------|
| SYSP_US_AGENT_ARCH | SYSP_REQ_AGENT_ARCH_FRONTMATTER | SYSP_SPEC_AGENT_ARCH_FRONTMATTER + 13 per-agent frontmatter specs | ✅ |
| SYSP_US_DOC_EXTERNAL | — (documentation content updated downstream at Document stage) | — | ✅ |

sphinx-build `-W` passes clean (EXIT=0) — all RST valid, all traceability links resolve, no dangling references to the removed spec.

### Artefakt-Removal-Check

**Removed artefact:** `SYSP_SPEC_AGENT_BASE_TOOLSET` (spec node) and the `tools:` frontmatter field prescription across all agent specs except Setup.

| Removed Artefact | Class (a): Code/Workflow refs | Class (b): Doc refs | Class (c): Historic Change Docs |
|------------------|-------------------------------|---------------------|---------------------------------|
| `SYSP_SPEC_AGENT_BASE_TOOLSET` | None found (grep: zero `:links:` directives reference it after this CR) | None found in docs/architecture.md, README, workflows.md as a `:links:` reference | Historic Change Documents (`product-owns-tool-lists.md`, `agent-spec-base-toolset-links.md`) reference it in prose — acceptable historic stranding |
| `tools:` frontmatter prescription | Closed by Dev Engineer (commit `81b5e3a`) — 12 non-Setup agent files (product + instance) stripped | Closed by Documentation Engineer (commit `5e0bb23`) — `docs/architecture.md` + `README.md` updated | — |

- [x] Class (a) for `SYSP_SPEC_AGENT_BASE_TOOLSET` — none found
- [x] Class (b) doc refs — closed (`docs/architecture.md`, `README.md` updated by Documentation Engineer)
- [x] Class (c) historical Change Documents accepted as "acceptable historic stranding"

### Issues Found

- **Stale UAT test artifacts** — resolved: `us_uat_product_owns_tool_lists.rst` (+ req/spec) chain deprecated/superseded per-scenario by Test Designer (commit `b98cc84`); new `SYSP_US_UAT_REMOVE_TOOLS_FRONTMATTER` chain added.
- **Implementation scope** — resolved: `.agent.md` product + instance files stripped of `tools:` (except Setup Bootloader) by Dev Engineer (commit `81b5e3a`).

### Sign-off

- [x] All levels completed (no ⚠️ DEPRECATED markers remaining)
- [x] All conflicts resolved
- [x] Traceability verified
- [x] Ready for implementation

---

## UAT

**Status**: ✅ completed

### Summary

Commit `b98cc84`. Stale `product-owns-tool-lists` UAT chain deprecated/superseded per-scenario (not wholesale) — `SYSP_US_UAT_AGENT_BASE_TOOLSET` chain fully deprecated; `SYSP_US_UAT_INSTALLER_TOOL_OWNERSHIP` AC-3 superseded, AC-1/2/4 kept valid. New `SYSP_US_UAT_REMOVE_TOOLS_FRONTMATTER` chain added with 5 scenarios (TC-RT-NOTOOLS, TC-RT-SETUP, TC-RT-UPDATE, TC-RT-DOCTESTABILITY [testability-limited, disclosed], TC-RT-DOCPRESENCE [closed after Documentation stage]).

### Issues Found

- None outstanding — TC-RT-DOCPRESENCE forward dependency closed by Documentation Engineer.

---

## Implementation

**Status**: ✅ completed

### Summary

Commit `81b5e3a`. `tools:` line removed from 12 non-Setup agent files in both `syspilot/agents/` (product) and `.github/agents/` (instance) = 24 files. Setup Bootloader (both locations) verified untouched — retains explicit `tools:` list including `agent/runSubagent`.

### Issues Found

- None.

---

## Documentation

**Status**: ✅ completed

### Changed Files

| File | Nature |
|------|--------|
| `docs/architecture.md` | Replaced stale base-toolset-model prose with accurate description; added "Required: `enthali.jarvis-core`" guidance (silent-failure mode disclosed) |
| `README.md` | Added `enthali.jarvis-core` requirement bullet at install-time visibility |

### Reviewed, No Change Needed

- `docs/workflows.md` — no `tools:`/base-toolset prescription language present
- `docs/methodology.md` — no `tools:` frontmatter model references

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
**Review date:** 2026-07-02
**Scope:** Full targeted check — L0/L1/L2, retirement of `SYSP_SPEC_AGENT_BASE_TOOLSET`, 24 agent file changes, UAT chain, schema, reversal consistency.

#### Findings

| # | Level | Element ID | Finding | Severity |
|---|-------|------------|---------|----------|
| 1 | L1 | `SYSP_REQ_CM_FRONTMATTER`, `SYSP_REQ_QM_FRONTMATTER` | Rationale prose (newly written by this CR) refers to session-messaging tools as ``jarvis-core_*`` (underscore, no namespace). The actual, verified tool ID format used across all product agent files is `enthali.jarvis-core/<toolname>` (namespace+slash) — this exact underscore-vs-slash mismatch was raised and fixed in `product-owns-tool-lists` Round 1/2. Reintroducing the wrong notation in new prose, even outside a functional `tools:` list, reintroduces the same documentation inconsistency and risks propagating the wrong format if a future `tools:` field is ever reinstated for these agents. | low |
| 2 | L2 | `SYSP_SPEC_INSTALLER_WORKFLOW` Step 4 | Prose still states "All frontmatter fields (including ``tools:``) come from upstream; no local field is preserved" as if `tools:` were a common example field. Since this CR removes `tools:` from 12 of 13 agents, the field is no longer representative of the general case (only Setup carries it now). Not incorrect — verbatim-write behavior is unaffected and still true — but the illustrative example is stale relative to the new model. | low |

#### Validation Notes

- **Retirement of `SYSP_SPEC_AGENT_BASE_TOOLSET`**: confirmed fully removed from the needs graph. Zero `:links:` directives reference it anywhere in the current (non-deprecated) spec tree. All remaining prose mentions are confined to the explicitly-deprecated UAT chain (`us_uat_product_owns_tool_lists.rst` + req/spec), correctly disclosed via a superseded-note at the top of that file. ✅
- **L0**: `SYSP_US_AGENT_ARCH` AC-6 correctly rewritten (no `tools:` field, inherits default agent). New `SYSP_US_DOC_EXTERNAL` AC-6 correctly requires documenting the `enthali.jarvis-core` dependency. ✅
- **L1**: `SYSP_REQ_AGENT_ARCH_FRONTMATTER` AC-3/AC-10 correctly collapse the old base-toolset/no-memory/runSubagent-Setup-only ACs; rationale clearly documents the VS Code tool-picker instability root cause. `SYSP_REQ_CM_FRONTMATTER`, `SYSP_REQ_PM_FRONTMATTER`, `SYSP_REQ_QM_FRONTMATTER` AC-3 all correctly state no `tools:` field (see Finding 1 for a prose-only issue). ✅
- **L2**: All 13 `SYSP_SPEC_*_FRONTMATTER` specs verified — 12 have the `tools:` bullet and base-toolset link fully removed; `SYSP_SPEC_SETUP_FRONTMATTER` correctly retains an explicit hardcoded list including `agent/runSubagent` as the sole documented exception. `SYSP_SPEC_AGENT_ARCH_FRONTMATTER` schema/example/constraint text is fully consistent with the new model. ✅
- **Implementation**: Verified 13 total product agent files (`syspilot/agents/`) and 13 installed files (`.github/agents/`) — exactly 1 (`syspilot.setup.agent.md`) carries a `tools:` line in both locations; the other 12 × 2 = 24 files have it removed, matching the CR's stated file count. ✅
- **UAT chain**: New `SYSP_US_UAT_REMOVE_TOOLS_FRONTMATTER` correctly links to both `SYSP_US_AGENT_ARCH` and `SYSP_US_DOC_EXTERNAL`; full REQ→SPEC trace chain resolves. Deprecated chain (`SYSP_US_UAT_AGENT_BASE_TOOLSET` full deprecation, `SYSP_US_UAT_INSTALLER_TOOL_OWNERSHIP` AC-3 superseded) carries explicit, unambiguous status notes — no silent removal. Testability-limited claim (tool-inheritance functional behavior) is explicitly disclosed as a documentation/design-record check rather than glossed over as a runtime test. ✅
- **Reversal consistency**: This CR reverses `product-owns-tool-lists` and `agent-spec-base-toolset-links` (both previously merged, both QM-cleared). No contradictory prose or orphaned trace links found from either merged CR outside the explicitly-deprecated UAT files. ✅
- **Schema**: sphinx-needs validation — 0 warnings. ✅
- **Judgment call assessment**: The Setup Bootloader exception (sole agent keeping explicit `tools:` including `agent/runSubagent`) is consistently documented across L0 (`SYSP_US_AGENT_ARCH` rationale via `SYSP_REQ_AGENT_ARCH_FRONTMATTER` AC-10), L1, and L2 (`SYSP_SPEC_SETUP_FRONTMATTER`, `SYSP_SPEC_AGENT_ARCH_FRONTMATTER` constraint). This is not scope creep — it is the same bootstrap-layer exception pattern already established for session-identity fields elsewhere in the spec (Bootloader/Installer exclusions). Judgment call is sound.

#### PM Decisions

| # | Finding # | Decision | Rationale |
|---|-----------|----------|-----------|
| 1 | 1 | Fix now | This exact `jarvis-core_*` vs. `enthali.jarvis-core/<toolname>` mismatch was already found and corrected once before, in `product-owns-tool-lists` Round 1/2. Letting it recur in new prose risks the same confusion resurfacing later. Low effort, same branch — fix immediately rather than defer. |
| 2 | 2 | Fix now | The `SYSP_SPEC_INSTALLER_WORKFLOW` Step 4 example is now stale relative to the model this CR introduces (only 1 of 13 agents retains `tools:`). Not functionally incorrect, but leaving a misleading illustrative example in a spec this CR directly touches creates unnecessary confusion for the next reader. Cheap fix, same branch. |
| — | Setup Bootloader `tools:` exception | Approved (permanent) | QM confirmed the exception is consistently documented across all three levels and consistent with the existing Bootloader/Installer bootstrap-layer exception pattern. Sound, not scope creep. |

Both fixes sent back to CM for the same branch; awaiting re-verification and Round 2 QM report before merge.

---

### Round 2

**Reviewed by:** Quality Manager
**Review date:** 2026-07-02
**Scope:** Re-verification of both Round 1 fix-now findings (commit `71c19d3`) + schema re-check.

#### Findings

| # | Level | Element ID | Finding | Severity |
|---|-------|------------|---------|----------|
| 3 | L2 | `SYSP_SPEC_INSTALLER_WORKFLOW` Step 4 | Finding 2's fix replaced the stale `tools:` example correctly, but the added parenthetical — "The Setup Bootloader's `tools:` field is the sole exception to 'no local field is preserved' — it is a hardcoded, agent-specific field... not a common field subject to this general rule" — is logically inconsistent with the surrounding text. Step 4 states every file is "written verbatim from upstream; no local field is preserved" for **all** files including Setup's — there is no local-preservation carve-out for Setup anywhere else in the spec (`SYSP_SPEC_SETUP_FRONTMATTER` defines Setup's `tools:` as a hardcoded **product**-defined list fetched from upstream like any other field, not a customer-local override that survives updates). Calling it "the sole exception to no local field is preserved" implies a customer could locally customize Setup's `tools:` and have that survive an update — which contradicts the verbatim-overwrite model this CR and the Installer spec establish everywhere else. The fix corrects the staleness (Finding 2) but introduces new, confusing wording that misstates the actual behavior. | low |

#### Validation Notes

- **Finding 1 re-check**: `SYSP_REQ_CM_FRONTMATTER` and `SYSP_REQ_QM_FRONTMATTER` now both correctly read ``enthali.jarvis-core/*`` — matches the verified format used across all product agent files. **CLOSED.** ✅
- **Finding 2 re-check**: `SYSP_SPEC_INSTALLER_WORKFLOW` Step 4 illustrative example replaced with `description`, `user-invocable` (both genuinely common fields) — staleness issue resolved. However, the added exception clause about Setup's `tools:` field introduces a new wording defect — see Finding 3 above. **PARTIALLY CLOSED** (staleness fixed; new clarity issue found).
- **Schema**: sphinx-needs validation — 0 warnings, unchanged. ✅

**Verdict:** Finding 1 fully resolved. Finding 2's underlying staleness is resolved, but the fix introduces a new low-severity wording finding (Finding 3) requiring a further correction — e.g. replacing the parenthetical with something like: "The Setup Bootloader's ``tools:`` field is likewise written verbatim from upstream on every update — it is simply the one agent whose frontmatter includes this field at all, per SYSP_SPEC_SETUP_FRONTMATTER."

#### PM Decisions

| # | Finding # | Decision | Rationale |
|---|-----------|----------|-----------|
| 1 | 3 | Fix now | The parenthetical misstates Setup's `tools:` handling as a local-preservation exception, implying a customer-local override survives updates — contradicts the verbatim-overwrite model established everywhere else in the spec. Apply QM's suggested correction (or equivalent) clarifying Setup's `tools:` is written verbatim from upstream like every other field, and is simply the one agent whose frontmatter includes this field at all. |

---

### Round 3

**Reviewed by:** Quality Manager
**Review date:** 2026-07-02
**Scope:** Re-verification of Round 2 Finding 3 fix (commit `c1ce08a`) + schema re-check.

#### Findings

No findings.

- **Finding 3 re-check**: `SYSP_SPEC_INSTALLER_WORKFLOW` Step 4 now reads: "The Setup Bootloader's ``tools:`` field is likewise written verbatim from upstream on every update — it is simply the one agent whose frontmatter includes this field at all, per SYSP_SPEC_SETUP_FRONTMATTER." This is logically consistent with the surrounding verbatim-overwrite rule and correctly implements QM's suggested correction. **CLOSED.** ✅
- **Schema**: sphinx-needs validation — 0 warnings, unchanged. ✅

**Verdict: CLEAN. All three findings across Rounds 1–2 are now resolved. No open findings remain.**

#### PM Decisions

| # | Finding # | Decision | Rationale |
|---|-----------|----------|-----------|
| — | — | — | No findings — no decisions required. |

---

## Appendix: Link Discovery Results

```
{paste output from get_need_links.py as needed}
```

---

*Generated by syspilot Change Agent*
