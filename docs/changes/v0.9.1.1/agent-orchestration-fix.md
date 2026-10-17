# Change Document: agent-orchestration-fix

**Status**: in-progress
**Branch**: feature/agent-orchestration-fix
**Created**: 2026-09-16
**Author**: hubertusgbecker
**Operation Mode**: autonomous

---

## Summary

Restore the VS Code synchronous orchestration pipeline so every syspilot agent can be invoked only as intended and every agent that SENDs work can reach all of its declared targets through ``runSubagent``. The change corrects the product and installed agent frontmatter, removes proprietary ``model:`` pins so harness and user model choices are inherited, aligns requirements and designs with VS Code's enforced ``agents:`` allowlist, corrects the Subagent orchestration skill guidance, and installs the synchronous orchestration variant in this non-Jarvis workspace. Acceptance is demonstrated when the complete product/installed invocation and SEND-target matrix passes, no agent carries a model pin, the patch is clean, and no new documentation-build warning is introduced.

---

## Level 0: User Stories

**Status**: ✅ completed

### Impacted User Stories

| ID | Title | Impact | Notes |
|----|-------|--------|-------|
| SYSP_US_CM | Change Manager | modified | CM can SEND to its complete pipeline and readiness targets |
| SYSP_US_PM | Project Manager | modified | PM can SEND changes and releases synchronously |
| SYSP_US_QM | Quality Manager | modified | QM can SEND checks and findings synchronously |
| SYSP_US_DESIGN | System Designer | modified | Designer can SEND advisory MECE checks |
| SYSP_US_VERIFY | Verify Engineer | modified | Verify delegates traceability to Trace as required |
| SYSP_US_AGENT_ARCH | Clean Agent Architecture | modified | Invocation visibility matches agent roles |
| SYSP_US_SKILL_ORCHESTRATION | Consistent Agent Orchestration | modified | Subagent variant documents the enforced VS Code allowlist |

### New User Stories

| ID | Title | Priority |
|----|-------|----------|
| None | No new user story required | — |

### Decisions

- Decision 1: Preserve the existing Manager-to-Engineer workflow and correct its runtime declarations rather than redesigning orchestration.
- Decision 2: Treat ``agents:`` as an enforced VS Code allowlist; every actual SEND edge must be declared for both orchestration variants.
- Decision 3: Omit ``model:`` from every agent so users can select proprietary or open-source models through their harness configuration without setup/update restoring an upstream pin.

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
| SYSP_REQ_CM_FRONTMATTER | SYSP_US_CM | modified | Declares all CM SEND targets |
| SYSP_REQ_PM_FRONTMATTER | SYSP_US_PM | modified | Declares CM and Release targets |
| SYSP_REQ_QM_FRONTMATTER | SYSP_US_QM | modified | Declares MECE, Trace, and PM targets |
| SYSP_REQ_DESIGN_FRONTMATTER | SYSP_US_DESIGN | implementation aligned | Existing MECE allowlist requirement is now implemented |
| SYSP_REQ_VERIFY_FRONTMATTER | SYSP_US_VERIFY | implementation aligned | Existing Trace allowlist requirement is now implemented |

### New Requirements

| ID | Title | Links | Priority |
|----|-------|-------|----------|
| None | No new requirement required | — | — |

### Conflicts Detected

None. Existing invocation and delegation requirements remain authoritative.

### Decisions

- Decision 1: Replace Jarvis-only rationale with orchestration-variant-neutral behavior while retaining inherited tool selection.

### Horizontal Check (MECE)

- [x] No contradictions with existing Requirements
- [x] No redundancies
- [x] No new Requirements introduced

---

## Level 2: Design

**Status**: ✅ completed

### Impacted Design Elements

Found via links from Requirements above.

| ID | Linked From | Impact | Notes |
|----|-------------|--------|-------|
| SYSP_SPEC_CM_FRONTMATTER | SYSP_REQ_CM_FRONTMATTER | modified | Complete CM allowlist |
| SYSP_SPEC_PM_FRONTMATTER | SYSP_REQ_PM_FRONTMATTER | modified | Complete PM allowlist |
| SYSP_SPEC_QM_FRONTMATTER | SYSP_REQ_QM_FRONTMATTER | modified | Complete QM allowlist |
| SYSP_SPEC_DESIGN_FRONTMATTER | SYSP_REQ_DESIGN_FRONTMATTER | modified | MECE allowlist aligned |
| SYSP_SPEC_VERIFY_WORKFLOW | SYSP_REQ_VERIFY_WORKFLOW | modified | Trace delegation made explicit |
| SYSP_SPEC_VERIFY_FRONTMATTER | SYSP_REQ_VERIFY_FRONTMATTER | modified | Trace allowlist aligned |
| SYSP_SPEC_SKILL_ORCHESTRATION_VERB_MODEL_SUBAGENT | SYSP_REQ_SKILL_ORCHESTRATION_GROUP | modified | Correct VS Code allowlist semantics |

### New Design Elements

| ID | Title | Links |
|----|-------|-------|
| None | No new design element required | — |

### Conflicts Detected

None after aligning Verify's design with its existing requirement.

### Decisions

- Decision 1: Populate allowlists from actual SEND workflow edges, including completion/finding notifications.
- Decision 2: Keep leaf Engineer allowlists empty and mark all non-user entry-point agents ``user-invocable: false``.
- Decision 3: Install ``syspilot.orchestration-subagent`` and remove ``syspilot.orchestration-jarvis`` from the installed instance because this workspace has no ``.jarvis/`` directory.

### Horizontal Check (MECE)

- [x] No contradictions with existing Designs
- [x] No new SPECs introduced

---

## Final Consistency Check

**Status**: ✅ passed

### Traceability Verification

| User Story | Requirements | Design | Complete? |
|------------|--------------|--------|-----------|
| SYSP_US_CM | SYSP_REQ_CM_FRONTMATTER | SYSP_SPEC_CM_FRONTMATTER | ✅ |
| SYSP_US_PM | SYSP_REQ_PM_FRONTMATTER | SYSP_SPEC_PM_FRONTMATTER | ✅ |
| SYSP_US_QM | SYSP_REQ_QM_FRONTMATTER | SYSP_SPEC_QM_FRONTMATTER | ✅ |
| SYSP_US_DESIGN | SYSP_REQ_DESIGN_FRONTMATTER | SYSP_SPEC_DESIGN_FRONTMATTER | ✅ |
| SYSP_US_VERIFY | SYSP_REQ_VERIFY_FRONTMATTER | SYSP_SPEC_VERIFY_FRONTMATTER | ✅ |
| SYSP_US_SKILL_ORCHESTRATION | SYSP_REQ_SKILL_ORCHESTRATION_GROUP | SYSP_SPEC_SKILL_ORCHESTRATION_VERB_MODEL_SUBAGENT | ✅ |

### Artefakt-Removal-Check

*Fill in only when this CR removes an artefact (file, field, configuration key, REQ-ID).*

For each removed artefact, run a project-wide grep on all plausible name variants and classify results:

| Removed Artefact | Class (a): Code/Workflow refs | Class (b): Doc refs | Class (c): Historic Change Docs |
|------------------|-------------------------------|---------------------|---------------------------------|
| Installed Jarvis orchestration variant | Removed from ``.github/skills`` and replaced by Subagent variant | Active design retains both product variants by intent | Historical Change Documents unchanged |

- [x] All class (a) active code/workflow references fixed in this CR
- [x] All class (b) active documentation references fixed in this CR
- [x] Class (c) historical Change Documents accepted as "acceptable historic stranding" and disclosed above

### Issues Found

- [x] Focused matrix check passes for all product and installed agent copies.
- [x] Focused scan finds zero ``model:`` declarations across product and installed agent copies.
- [x] ``git diff --check`` passes.
- [x] Real Sphinx build reaches completion with only two pre-existing ``ontology-architecture`` cross-reference warnings in ``docs/methodology.md`` and ``docs/syspilot/methodology.md``; this CR introduces no warning in a changed file.
- [x] Live ``runSubagent`` proof requires a new Copilot chat because the current session's agent registry was fixed at session start with the old empty allowlist.

### Sign-off

- [x] All levels completed
- [x] All conflicts resolved
- [x] Traceability verified
- [x] Implementation complete and ready for integration

---

## QM Findings

*QM writes findings directly into this section after each review round. PM records
decisions (fix-now / defer / accept-as-is) with rationale in the same section.
Multiple review rounds are appended as sub-sections. Existing CDs without this
section are unaffected — the section is additive, never required retroactively.*

### Round 1

**Reviewed by:** QM
**Review date:** 2026-09-16

#### Findings

| # | Level | Element ID | Finding | Severity |
|---|-------|------------|---------|----------|
| 1 | Validation | Baseline docs build | Two unrelated existing missing cross-reference warnings prevent a globally clean ``-W`` build | low |

#### PM Decisions

| # | Finding # | Decision | Rationale |
|---|-----------|----------|-----------|
| 1 | 1 | defer | Existing ontology cross-reference defect is outside orchestration scope and occurs in unchanged files; track separately |

---

## Appendix: Link Discovery Results

Existing US → REQ → SPEC links listed in the Final Consistency Check resolve in the built Sphinx needs graph; no new IDs were introduced.

---

*Generated by syspilot Change Agent*
