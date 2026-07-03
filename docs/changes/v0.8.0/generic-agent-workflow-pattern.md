# Change Document: generic-agent-workflow-pattern

**Status**: cleared
**Branch**: feature/generic-agent-workflow-pattern
**Created**: 2026-06-26
**Author**: PM
**Operation Mode**: user-guided

---

## Summary

Today every syspilot agent embeds project-specific details (paths, commands, distribution targets) directly in its workflow steps, causing CI breaks and drift whenever syspilot is installed in a new project. This change makes each agent's workflow skeleton fully project-neutral and ships it as product; project-specific details live in a sibling tailoring file (`syspilot.<name>.tailoring.md`) stored next to the agent, never shipped by setup. An agent reads its tailoring file for project-specific steps; if it is missing, the agent RESPONDs to PM, who reads the agent's generic workflow, interviews the user, and authors the file. The tailoring file may be empty (proceed generic), clarify a step, or override it. The Project Manager is converted first as the pilot and gains a 4th workflow (Tailoring). Acceptance criteria: the PM workflow skeleton contains zero project-specific nouns; a missing `syspilot.pm.tailoring.md` triggers the PM Tailoring workflow; no Sphinx PROC hierarchy and no skill are introduced — just the per-agent sentence + RESPOND-to-PM mechanism.

---

## Level 0: User Stories

**Status**: ✅ completed

### Impacted User Stories

| ID | Title | Impact | Notes |
|----|-------|--------|-------|
| SYSP_US_AGENT_ARCH | Clean Agent Architecture | modified | Added AC 6: workflow bindings in process spec, not hardcoded |
| SYSP_US_PM | Project Manager Agent | not modified | Intent unchanged; generic skeleton is L1/L2 concern |

### New User Stories

| ID | Title | Priority |
|----|-------|----------|
| SYSP_US_CUSTOM_AGENT_WORKFLOWS | Custom Agent Workflow Bindings | mandatory |

### Decisions

- Decision 1: PM user story unchanged at L0 — the WHAT stays the same, only the HOW (L1/L2) changes
- Decision 2: New US links to SYSP_US_AGENT_ARCH (it extends the architecture, not a specific agent)

### Horizontal Check (MECE)

- [x] No contradictions with existing User Stories
- [x] No redundancies
- [x] Gaps identified and addressed

---

## Level 1: Requirements

**Status**: ✅ completed

### Impacted Requirements

Found via links from User Stories above.

| ID | Linked From | Impact | Notes |
|----|-------------|--------|-------|
| SYSP_REQ_AGENT_ARCH_WORKFLOW | SYSP_US_AGENT_ARCH | modified | Added AC-6: bindings from tailoring file |
| SYSP_REQ_PM_DUTIES | SYSP_US_PM | modified | Genericised: branch names via syspilot.branching skill, post-release via tailoring |
| SYSP_REQ_PM_WORKFLOW | SYSP_US_PM | modified | Link to SYSP_REQ_AGENT_ARCH_WORKFLOW + SYSP_REQ_SKILL_BRANCHING_CHAINED; AC-6 references branching skill; AC-9 for tailoring file |

### New Requirements

| ID | Title | Links | Priority |
|----|-------|-------|----------|
| SYSP_REQ_AGENT_WORKFLOW_BINDING | Agent Workflow Binding Contract | SYSP_US_CUSTOM_AGENT_WORKFLOWS; SYSP_REQ_AGENT_ARCH_WORKFLOW | mandatory |

### Conflicts Detected

- none

### Decisions

- Decision 1: "merge into development" in SYSP_REQ_PM_WORKFLOW AC-6 replaced with reference to SYSP_REQ_SKILL_BRANCHING_CHAINED — branch name is a branching strategy binding, not a PM workflow concern
- Decision 2: SEND/CM/Release Agent/Setup Agent remain in SYSP_REQ_PM_WORKFLOW — these are syspilot orchestration method, not project-specific bindings
- Decision 3: GH issue #41 filed for follow-up: all per-agent workflow REQs should link to SYSP_REQ_AGENT_ARCH_WORKFLOW (out of scope this CR)

### Horizontal Check (MECE)

- [x] No contradictions with existing Requirements
- [x] No redundancies
- [x] All new REQs link to User Stories

---

## Level 2: Design

**Status**: ✅ completed

### Impacted Design Elements

Found via links from Requirements above.

| ID | Linked From | Impact | Notes |
|----|-------------|--------|-------|
| SYSP_SPEC_AGENT_ARCH_WORKFLOW | SYSP_REQ_AGENT_ARCH_WORKFLOW | modified | Added Tailoring File property |
| SYSP_SPEC_PM_DUTIES | SYSP_REQ_PM_DUTIES | modified | Genericised: syspilot.branching skill refs, post-release distribution via tailoring; status approved→draft |
| SYSP_SPEC_PM_WORKFLOW | SYSP_REQ_PM_WORKFLOW | modified | Preflight + 2-workflow structure (Main lifecycle + Tailoring); steps 7/8/merge via branching skill; GH #42 filed |

### New Design Elements

| ID | Title | Links |
|----|-------|-------|
| (none) | Tailoring captured in instance ``*.tailoring.md`` files — not Sphinx-needs elements | — |

### Conflicts Detected

- none

### Decisions

- Decision 1: Docs location stays fixed — not configurable (avoids forcing a doc-location skill on every agent)
- Decision 2: semver is the generic default; CalVer demoted to optional binding
- Decision 3: experimental branch lane is syspilot-only — lives in PROC spec, not the generic skeleton
- Decision 4: Release step 5 kept as generic "post-release distribution"; binding resolves to self-install (syspilot) or no-op/marketplace (Jarvis) — step always accounted for
- Decision 5: No PROC_* Sphinx hierarchy — tailoring is a sibling ``syspilot.<name>.tailoring.md`` file per agent, like session context.md promoted to official name
- Decision 6: No tailoring skill — one sentence per agent + RESPOND-to-PM; PM reads agent name, interviews, authors file
- Decision 7: PM gains a 4th workflow (Tailoring) — detect missing file → interview → author; serves any agent that rolls up

### Horizontal Check (MECE)

- [x] No contradictions with existing Designs
- [x] All new SPECs link to Requirements

---

## Final Consistency Check

**Status**: ✅ passed

### Traceability Verification

| User Story | Requirements | Design | Complete? |
|------------|--------------|--------|-----------|
| SYSP_US_CUSTOM_AGENT_WORKFLOWS | SYSP_REQ_AGENT_WORKFLOW_BINDING | SYSP_SPEC_AGENT_ARCH_WORKFLOW (property) | ✅ |
| SYSP_US_AGENT_ARCH (+AC6) | SYSP_REQ_AGENT_ARCH_WORKFLOW (+AC6) | SYSP_SPEC_AGENT_ARCH_WORKFLOW (+Tailoring File) | ✅ |
| SYSP_US_PM (unchanged) | SYSP_REQ_PM_DUTIES, SYSP_REQ_PM_WORKFLOW | SYSP_SPEC_PM_DUTIES, SYSP_SPEC_PM_WORKFLOW | ✅ |

### Artefakt-Removal-Check

| Removed Artefact | Class (a): Code/Workflow refs | Class (b): Doc refs | Class (c): Historic Change Docs |
|------------------|-------------------------------|---------------------|---------------------------------|
| `spec_proc_pm_workflow.rst` (PROC_SPEC_WORKFLOW_PM_AGENT) | none — file was created and deleted within this CR, never referenced externally | none | none — created and removed in same CR, no stranding |
| `PROC_SPEC_PM_PROJECT_WORKFLOW` (renamed then dropped) | none | none | none — never committed to a stable branch |

- [x] All class (a) active code/workflow references fixed in this CR
- [x] All class (b) active documentation references fixed in this CR
- [x] Class (c) historical Change Documents: none (PROC IDs never appeared in any other change document)

### Issues Found

- none

### Sign-off

- [x] All levels completed (no ⚠️ DEPRECATED markers remaining)
- [x] All conflicts resolved
- [x] Traceability verified
- [x] Ready for implementation

---

## QM Findings

### Round 1

**Reviewed by:** MECE Engineer + Trace Engineer
**Review date:** 2026-06-29

#### Findings

| # | Level | Element ID | Finding | Severity |
|---|-------|------------|---------|----------|
| 1 | L2 | `SYSP_SPEC_AGENT_ARCH_WORKFLOW` | No `:links: SYSP_REQ_AGENT_WORKFLOW_BINDING` — US→REQ→SPEC chain broken (Trace DEF-1) | high |
| 2 | L1 | `SYSP_REQ_PM_WORKFLOW` AC-9 | "branch naming patterns" listed as tailoring concern — contradicts AC-6 which assigns it to the branching skill (MECE L1-C1 / L2-C1) | high |
| 3 | L0 | `SYSP_US_AGENT_ARCH` AC-6 | "referenced process specification" — terminology contradicts CR Decision 5 (no PROC_*); should say "sibling tailoring file" (MECE L0-C1) | high |
| 4 | L1 | `SYSP_REQ_PM_DUTIES` AC-8 + `SYSP_REQ_PM_WORKFLOW` AC-8 | Post-release distribution in both Duties and Workflow — architecture rule violation: one behavioural item, one home (MECE L1-MX1) | high |
| 5 | L1 | `SYSP_REQ_PM_DUTIES` AC-7/9 + `SYSP_REQ_PM_WORKFLOW` AC-5 | QM decision + recording in both Duties and Workflow — same architecture violation (MECE L1-MX2) | high |
| 6 | L1/L2 | `SYSP_REQ_PM_DUTIES`, `SYSP_REQ_PM_WORKFLOW`, `SYSP_SPEC_PM_WORKFLOW` | Missing `:links: SYSP_REQ_AGENT_WORKFLOW_BINDING` — tailoring changes untraceable to binding contract (MECE L1-G2 / Trace DEF-2) | medium |
| 7 | L2 | `SYSP_SPEC_AGENT_ARCH_WORKFLOW` | "RESPOND to PM" self-referential when PM is the agent — no carve-out for PM (MECE L2-G3) | medium |
| 8 | L0 | `SYSP_US_CUSTOM_AGENT_WORKFLOWS` AC-1 | AC-1 says the invoked agent does the interview; L1 assigns it to PM — responsibility inconsistency across levels (MECE L0-G1) | medium |
| 9 | L0 | `SYSP_US_CUSTOM_AGENT_WORKFLOWS` | Empty-file AC missing at L0 — covered at L1 but no L0 mandate (MECE L0-G2) | low |
| 10 | L1 | `SYSP_REQ_AGENT_WORKFLOW_BINDING` AC-1 | "Customizable agents" not enumerated — scope open by design (MECE L1-G1) | low |
| 11 | L2 | `SYSP_SPEC_AGENT_ARCH_WORKFLOW` | No canonical preflight sentence template — implementers have no form to follow (MECE L2-G1) | medium |
| 12 | L2 | `SYSP_SPEC_PM_WORKFLOW` step 11 | Backlog location introduced at L2 without upstream AC — scope creep (MECE L2-G2) | medium |
| 13 | L1/L2 | `SYSP_REQ_AGENT_ARCH_WORKFLOW` AC-6, `SYSP_SPEC_PM_WORKFLOW` Preflight | Minor redundancies — same rule stated twice; no single source of truth (MECE L1-R1 / L2-R1) | low |

#### PM Decisions

| # | Finding # | Decision | Rationale |
|---|-----------|----------|-----------|
| 1 | 1 | fix-now | Critical traceability gap — SPEC_AGENT_ARCH_WORKFLOW already implements the binding pattern; missing link makes it invisible. Add `SYSP_REQ_AGENT_WORKFLOW_BINDING` to links. |
| 2 | 2 | fix-now | Branch naming is a branching skill concern, not a tailoring file concern. Remove from AC-9; SPEC step 7 is already correct. |
| 3 | 3 | fix-now | "Process specification" contradicts CR Decision 5 (no PROC_*). Replace with "sibling tailoring file". |
| 4 | 4 | fix-now | Architecture rule is clear: one behavioural item, one home. Post-release distribution stays in Duties only; SPEC step 17 is a correct execution step and is not affected. |
| 5 | 5 | fix-now | Same architecture rule. QM decision accountability stays in Duties only; WORKFLOW AC-5 replaced with a trigger-only statement. |
| 6 | 6 | fix-now | Traceability links added to PM Duties REQ, PM Workflow REQ, and PM Workflow SPEC. |
| 7 | 7 | fix-now | PM self-reference is a genuine gap. Added carve-out: "or, if the agent is PM, runs its own Tailoring Workflow directly". |
| 8 | 8 | fix-now | AC-1 reworded: the invoked agent RESPONDs to PM; PM does the interview and authoring. This is PM's defined responsibility (Tailoring Workflow). |
| 9 | 9 | defer | Empty-file behavior is specified at L1 (SYSP_REQ_AGENT_WORKFLOW_BINDING AC-4). Adding a formal L0 AC is low priority; no user-facing gap. |
| 10 | 10 | defer | Scope enumeration by design: agents are added incrementally via subsequent CRs. No value in listing the set now. |
| 11 | 11 | fix-now | Added Implementation Template property to SYSP_SPEC_AGENT_ARCH_WORKFLOW. Gives implementers a canonical preflight sentence form. |
| 12 | 12 | fix-now | Backlog ownership added to SYSP_US_PM (AC-9) and SYSP_REQ_PM_WORKFLOW (AC-10) — provides upstream mandate for the tailoring-file backlog location in SPEC step 11. |
| 13 | 13 | fix-now | AC-6 in SYSP_REQ_AGENT_ARCH_WORKFLOW demoted to a cross-reference pointer to SYSP_REQ_AGENT_WORKFLOW_BINDING. Preflight in SYSP_SPEC_PM_WORKFLOW cross-references SYSP_SPEC_AGENT_ARCH_WORKFLOW. |

### Round 2

**Reviewed by:** Quality Manager
**Review date:** 2026-06-29
**Scope:** Fresh independent targeted check of Round 1 fixes and declared branch changes.

#### Findings

| # | Level | Element ID / Artefact | Finding | Severity |
|---|-------|------------------------|---------|----------|
| 1 | L1/L2/Implementation | `SYSP_REQ_AGENT_WORKFLOW_BINDING` AC-2; `SYSP_SPEC_INSTALLER_WORKFLOW`; `.github/agents/syspilot.pm.tailoring.md` | Tailoring files are promised to survive setup updates, but Installer orphan cleanup still removes any file in `.github/agents/` that has no corresponding source file. Because `*.tailoring.md` is intentionally instance-only and absent from `syspilot/agents/`, the next setup/update can delete the PM tailoring file instead of preserving it. | high |
| 2 | L1/L2/Implementation | `SYSP_REQ_PM_WORKFLOW` AC-6/AC-9; `SYSP_SPEC_PM_WORKFLOW` step 7/13; `.github/agents/syspilot.pm.tailoring.md` | Branch base, branch naming, and merge target are duplicated in the PM tailoring file even though Round 1 fixed the specs to make branch naming and merge policy a `syspilot.branching` skill concern. This creates a stale second source of truth and currently conflicts with the installed branching skill (`development`/`feature/<name>` vs tailoring `experimental`/`feature/<slug>`/`fix/<slug>`). | high |

#### PM Decisions

| # | Finding # | Decision | Rationale |
|---|-----------|----------|-----------|
| 1 | 1 | defer | Installer orphan-cleanup scoping (syspilot.* only vs all files) is a separate installer concern; tailoring files are re-creatable via the Tailoring Workflow so deletion is recoverable. Filed as GH issue for installer-scoping CR. |
| 2 | 2 | fix-now | Delete `.github/agents/syspilot.pm.tailoring.md` from this branch. The file was created prematurely — per UAT scenario 2 and the Tailoring Workflow, it is authored on first PM invocation, not at install/CR time. Branch naming entries in the tailoring file are redundant with the branching skill and create a conflicting second source of truth. |

#### Validation Notes

- Generated needs trace export confirms the Round 1 link fixes are present for the declared changed elements.
- Schema validation completed with 0 schema warnings.
- Full docs build currently exits failed because `html_static_path` references missing `_static`; this warning is outside the changed files and appears pre-existing for this CR.

### Round 3

**Reviewed by:** Quality Manager
**Review date:** 2026-06-29
**Scope:** Confirm R2-2 fix (commit 39ee8ec) is clean; check for new issues introduced by deletion.

#### Findings

| # | Level | Element ID / Artefact | Finding | Severity |
|---|-------|------------------------|---------|----------|
| 1 | Docs | `docs/releasenotes.md` (Unreleased section) | Release notes say `` `syspilot.pm.tailoring.md` added as the syspilot dogfooding instance: `experimental` branch base… ``. The file was deleted in commit 39ee8ec. The shipped state is NO tailoring file; users reading the release notes will incorrectly expect to find the file in `.github/agents/`. | medium |
| 2 | Docs | `docs/architecture.md` (Concrete Example section) | The "Tailoring file" sub-section describes the file with illustrative content and correctly states "Authored by PM via the Tailoring Workflow on first invocation", but the heading and preceding bullets describe an existing file. No actual change needed if the last bullet is understood as the lifecycle statement; however a one-line clarification ("will be created on first PM invocation") would remove ambiguity. | low |

#### PM Decisions

| # | Finding # | Decision | Rationale |
|---|-----------|----------|-----------|
| 1 | 1 | fix-now | Factual inaccuracy corrected: release note reworded to state the file is authored on first PM invocation, not committed to the repo. One-liner, no spec impact. |
| 2 | 2 | fix-now | Architecture example heading updated to "(created on first PM invocation)"; added clarifying last bullet. Removes ambiguity at zero risk. |

#### R2-2 Fix Verification

- Commit 39ee8ec deleted `.github/agents/syspilot.pm.tailoring.md` cleanly (30 lines removed, no residual references in committed files).
- Deletion is correct per Tailoring Workflow design: the file is authored on first PM invocation, not during a CR.
- UAT scenario 2 (missing tailoring file triggers Tailoring Workflow) is now satisfiable in the installed worktree.
- No new L0 or L1 spec issues introduced.

---

## Appendix: Link Discovery Results

```
{paste output from get_need_links.py as needed}
```

---

*Generated by syspilot Change Agent*
