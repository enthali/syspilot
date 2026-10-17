# Change Document: hide-tailoring-files-from-picker

**Status**: ✅ completed
**Branch**: feature/hide-tailoring-files-from-picker
**Created**: 2026-09-16
**Author**: hubertusgbecker
**Operation Mode**: autonomous

---

## Summary

VS Code detects any `.md` file placed in `.github/agents/` as a selectable custom agent (per VS Code's own documentation). Because `syspilot.<name>.tailoring.md` files are deliberately colocated with their agent in that same directory (so the Installer's orphan-cleanup exemption can protect them), the two existing instance tailoring files (`syspilot.pm.tailoring.md`, `syspilot.release.tailoring.md`) were surfacing in the agent picker as plain, frontmatter-less agents. This CR adds a `user-invocable: false` / `disable-model-invocation: true` frontmatter block to both existing tailoring files and codifies this requirement in the generic tailoring contract (`SYSP_REQ_AGENT_WORKFLOW_BINDING`, the Tailoring File bullet in `spec_agent_arch.rst`, and PM's own Author step) so every tailoring file PM authors in the future is hidden from the picker by construction. Acceptance is demonstrated when both existing tailoring files carry the frontmatter, the generic contract mandates it for future files, and the Sphinx build shows no new warning.

---

## Level 0: User Stories

**Status**: ✅ completed

### Impacted User Stories

| ID | Title | Impact | Notes |
|----|-------|--------|-------|
| SYSP_US_CUSTOM_AGENT_WORKFLOWS | Custom Agent Workflow Tailoring | modified | Added AC-4: tailoring file frontmatter hides it from the VS Code agent picker |

### New User Stories

| ID | Title | Priority |
|----|-------|----------|
| None | No new user story required | — |

### Decisions

- Decision 1: Root cause is VS Code's documented "any `.md` in `.github/agents/` is a custom agent" behavior colliding with the tailoring file's required colocation for Installer orphan-cleanup — fix via frontmatter, not relocation, since relocation would break the orphan-cleanup contract.

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
| SYSP_REQ_AGENT_WORKFLOW_BINDING | SYSP_US_CUSTOM_AGENT_WORKFLOWS | modified | Mandates `user-invocable: false` / `disable-model-invocation: true` frontmatter on every tailoring file |

### New Requirements

| ID | Title | Links | Priority |
|----|-------|-------|----------|
| None | No new requirement required | — | — |

### Conflicts Detected

None.

### Decisions

- Decision 1: Extend the existing binding-contract requirement rather than create a new one — this is a refinement of how the file must present itself, not a new capability.

### Horizontal Check (MECE)

- [x] No contradictions with existing Requirements
- [x] No redundancies
- [x] No new REQs introduced

---

## Level 2: Design

**Status**: ✅ completed

### Impacted Design Elements

| ID | Linked From | Impact | Notes |
|----|-------------|--------|-------|
| SYSP_SPEC_AGENT_ARCH_WORKFLOW (Tailoring File bullet) | SYSP_REQ_AGENT_WORKFLOW_BINDING | modified | Implementation Template now includes the frontmatter block |

### New Design Elements

| ID | Title | Links |
|----|-------|-------|
| None | No new design element required | — |

### Conflicts Detected

None.

### Decisions

- Decision 1: PM's Author step (product and installed `syspilot.pm.agent.md`) now writes the frontmatter block as part of authoring any future tailoring file.
- Decision 2: The two existing instance tailoring files were corrected directly rather than waiting for the next `@syspilot.setup` run, since setup never touches `*.tailoring.md` files.

### Horizontal Check (MECE)

- [x] No contradictions with existing Designs
- [x] No new SPECs introduced

---

## Final Consistency Check

**Status**: ✅ passed

### Traceability Verification

| User Story | Requirements | Design | Complete? |
|------------|--------------|--------|-----------|
| SYSP_US_CUSTOM_AGENT_WORKFLOWS | SYSP_REQ_AGENT_WORKFLOW_BINDING | SYSP_SPEC_AGENT_ARCH_WORKFLOW | ✅ |

### Artefakt-Removal-Check

Not applicable — this CR adds frontmatter, it removes no artefact.

### Issues Found

- [x] Found and fixed a pre-existing RST indentation regression in `spec_uat_installer_spec_rewrite.rst` (introduced by the prior `agent-orchestration-fix` CR, T-5/TC-3 sections under-indented by one space), which was breaking sphinx-needs ID parsing. Confirmed via full `-W` Sphinx build: 3 warnings before the fix, 2 (both pre-existing, unrelated `ontology-architecture` cross-reference warnings) after.
- [x] `git diff --check` passes.

### Sign-off

- [x] All levels completed
- [x] All conflicts resolved
- [x] Traceability verified
- [x] Implementation complete and ready for integration

---

## QM Findings

Not yet reviewed by QM.

---

## Appendix: Link Discovery Results

```
No new IDs introduced; existing SYSP_US_CUSTOM_AGENT_WORKFLOWS -> SYSP_REQ_AGENT_WORKFLOW_BINDING link unchanged.
```

---

*Generated by syspilot Change Agent*
