# Change Document: product-owns-tool-lists

**Status**: in-progress
**Branch**: feature/product-owns-tool-lists
**Created**: 2026-06-24
**Author**: PM
**Operation Mode**: user-guided

---

## Summary

The `tools:` frontmatter field in agent files is currently treated as a user customization point — the Installer preserves whatever `tools:` value is on disk during updates, overwriting the upstream value. This made sense when tool lists were per-installation tuning, but it causes two practical failures: (1) product-side tool fixes (like removing `agent/runSubagent` from non-setup agents) never reach installed instances, and (2) the preservation logic is fragile and has failed repeatedly. This CR transfers ownership of `tools:` to the syspilot product: the Installer removes the `tools:` preservation step and overwrites `tools:` from upstream like every other frontmatter field. The `syspilot/agents/` product files become the single source of truth for tool lists, and the installed `.github/agents/` files are synced to match on every install/update. The Installer spec (`SYSP_SPEC_INSTALLER_WORKFLOW`) and Installer agent duty (`Local Customization Preservation`) are updated accordingly. Acceptance: Installer spec no longer mentions `tools:` preservation; product agent files have correct tool lists; sphinx-build -W passes clean.

---

## Level 0: User Stories

**Status**: ⏳ not started | 🔄 in progress | ✅ completed

### Impacted User Stories

| ID | Title | Impact | Notes |
## Level 0: User Stories

**Status**: ✅ completed

### Impacted User Stories

| ID | Title | Impact | Notes |
|----|-------|--------|-------|
| SYSP_US_INSTALLER | Installer Agent | modified | Removed `tools:` preservation duty + AC; reframed skill-mutex duty; renumbered ACs |
| SYSP_US_AGENT_ARCH | Clean Agent Architecture | modified | Added AC-6: tool permissions are product-defined and uniform except documented per-agent additions |

### New User Stories

None.

### Decisions

- `tools:` ownership moves from "user customization preserved by Installer" to product-owned, overwritten on every install/update.
- Tool-list correctness is a specification concern (frontmatter spec), not an implementation detail — the spec is the single source of truth.

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
| SYSP_REQ_INSTALLER_DUTIES | SYSP_US_INSTALLER | modified | Removed `tools:` preservation AC; renumbered AC-3…AC-11 → AC-2…AC-10 |
| SYSP_REQ_INSTALLER_WORKFLOW | SYSP_US_INSTALLER | modified | Replaced `tools:` read/replace AC-5 with verbatim-copy; removed Bootloader-exception AC-6; renumbered |
| SYSP_REQ_AGENT_ARCH_FRONTMATTER | SYSP_US_AGENT_ARCH | modified | AC-3 reworded to concrete tool IDs; added AC-10 (common base toolset + enumerated deltas), AC-11 (no workspace memory), AC-12 (`agent/runSubagent` Setup-only) |
| SYSP_REQ_CM_FRONTMATTER | SYSP_US_CM | modified | Drop subagent `agents:` + `runSubagent`/`syspilot_jarvis_tools`; base toolset; SENDs via sessions |
| SYSP_REQ_QM_FRONTMATTER | SYSP_US_QM | modified | Same reconciliation as CM |
| SYSP_REQ_PM_FRONTMATTER | SYSP_US_PM | modified | Drop `agents:`/`runSubagent`/`syspilot_jarvis_tools`/`github`; base toolset; SENDs to CM session |

### New Requirements

None.

### Conflicts Detected

- ⚠️ Manager frontmatter reqs (CM/QM/PM) required `agent/runSubagent` + populated `agents:`, contradicting the parent `SYSP_REQ_AGENT_ARCH_FRONTMATTER` AC-5 ("all other agents omit `agents:`") and deployed reality (all non-Setup agents have `agents: []`).
  - Resolution: Reconciled — managers SEND via sessions; only the Setup Bootloader keeps populated `agents:` + `runSubagent`.

### Decisions

- All agents receive the full Jarvis tool set (revisit later if it causes issues).
- No `vscode/resolveMemoryFileUri` (workspace memory) for any agent.
- `agent/runSubagent` granted only to the Setup Bootloader.
- Jarvis tools renamed to the marketplace prefix `jarvis-core_*` (legacy `enthali.jarvis/` retired).

### Horizontal Check (MECE)

- [x] No contradictions with existing Requirements
- [x] No redundancies
- [x] All modified REQs link to User Stories

---

## Level 2: Design

**Status**: ✅ completed

### Impacted Design Elements

| ID | Linked From | Impact | Notes |
|----|-------------|--------|-------|
| SYSP_SPEC_INSTALLER_DUTIES | SYSP_REQ_INSTALLER_DUTIES | modified | Removed "Local Customization Preservation" duty; → draft |
| SYSP_SPEC_INSTALLER_WORKFLOW | SYSP_REQ_INSTALLER_WORKFLOW | modified | Step 4 collapsed to verbatim copy from upstream |
| SYSP_SPEC_INSTALLER_ENCODING | SYSP_REQ_INSTALLER_ENCODING | modified | Removed stale `tools:` re-injection example |
| SYSP_SPEC_AGENT_ARCH_FRONTMATTER | SYSP_REQ_AGENT_ARCH_FRONTMATTER | modified | `tools` field redefined to concrete IDs referencing base toolset; example updated |
| SYSP_SPEC_CM_FRONTMATTER | SYSP_REQ_CM_FRONTMATTER | modified | Base toolset; `agents: []`; → draft |
| SYSP_SPEC_PM_FRONTMATTER | SYSP_REQ_PM_FRONTMATTER | modified | Base toolset; `agents: []`; → draft |
| SYSP_SPEC_QM_FRONTMATTER | SYSP_REQ_QM_FRONTMATTER | modified | Base toolset; `agents: []`; → draft |
| SYSP_SPEC_DESIGN_FRONTMATTER | SYSP_REQ_DESIGN_FRONTMATTER | modified | Base toolset; `agents: []`; → draft |
| SYSP_SPEC_IMPLEMENT_FRONTMATTER | SYSP_REQ_IMPLEMENT_FRONTMATTER | modified | Base toolset; → draft |
| SYSP_SPEC_DOCU_FRONTMATTER | — | modified | Base toolset; → draft |
| SYSP_SPEC_UAT_FRONTMATTER | — | modified | Base toolset; → draft |
| SYSP_SPEC_MECE_FRONTMATTER | — | modified | Base toolset; → draft |
| SYSP_SPEC_TRACE_FRONTMATTER | — | modified | Base toolset; → draft |
| SYSP_SPEC_VERIFY_FRONTMATTER | — | modified | Base toolset; `agents: []`; → draft |
| SYSP_SPEC_RELEASE_FRONTMATTER | — | modified | Base toolset; → draft |
| SYSP_SPEC_SETUP_FRONTMATTER | — | modified | Base toolset + `agent/runSubagent`; → draft |
| SYSP_SPEC_INSTALLER_FRONTMATTER | — | modified | Base toolset; → draft |

### New Design Elements

| ID | Title | Links |
|----|-------|-------|
| SYSP_SPEC_AGENT_BASE_TOOLSET | Agent Base Toolset | SYSP_REQ_AGENT_ARCH_FRONTMATTER |

### Conflicts Detected

None new at L2 (manager `agents:`/`runSubagent` contradiction was resolved at L1 and propagated here).

### Decisions

- One `SYSP_SPEC_AGENT_BASE_TOOLSET` holds the literal concrete tool-ID list once; each agent's `tools:` = base toolset (+ documented additions).
- `context7` included in the base toolset for all agents (harmless, simplifies frontmatter management).
- Only per-agent addition anywhere: `agent/runSubagent` on Setup.

### Horizontal Check (MECE)

- [x] No contradictions with existing Designs
- [x] New SPEC links to its Requirement
- [x] All frontmatter specs reference the single base-toolset source

---

## Final Consistency Check

**Status**: ✅ passed

### Traceability Verification

| User Story | Requirements | Design | Complete? |
|------------|--------------|--------|-----------|
| SYSP_US_INSTALLER | SYSP_REQ_INSTALLER_DUTIES, SYSP_REQ_INSTALLER_WORKFLOW | SYSP_SPEC_INSTALLER_DUTIES, SYSP_SPEC_INSTALLER_WORKFLOW, SYSP_SPEC_INSTALLER_ENCODING | ✅ |
| SYSP_US_AGENT_ARCH | SYSP_REQ_AGENT_ARCH_FRONTMATTER | SYSP_SPEC_AGENT_ARCH_FRONTMATTER, SYSP_SPEC_AGENT_BASE_TOOLSET, + 14 agent frontmatter specs | ✅ |

sphinx-build `-W` passes clean (EXIT=0) — all RST valid, all traceability links resolve.

### Artefakt-Removal-Check

| Removed Artefact | Class (a): Code/Workflow refs | Class (b): Doc refs | Class (c): Historic Change Docs |
|------------------|-------------------------------|---------------------|---------------------------------|
| `tools:` preservation (Installer behaviour) | Installer spec/req/story updated in this CR | none outside spec set | Not surveyed — historic stranding acceptable |
| `syspilot_jarvis_tools` (tool name) | Replaced by `jarvis-core_*` in spec set | none | Historic CDs may reference — acceptable |
| `enthali.jarvis/` (legacy prefix) | Replaced by `jarvis-core_*` in base toolset | none | Acceptable historic stranding |

**Note:** The agent `.agent.md` product files (`syspilot/agents/`) and deployed `.github/agents/` files still carry the old bloated lists / legacy Jarvis names. Regenerating them to match the new specs is the **Dev Engineer's** implementation task (CR Acceptance Criterion 2), not a spec change.

- [x] All class (a) active code/workflow references fixed in this CR (spec layer)
- [x] All class (b) active documentation references fixed in this CR
- [x] Class (c) historical Change Documents accepted as "acceptable historic stranding"

### Issues Found

- None blocking. Agent file regeneration handed to Dev Engineer.
- **Scope bleed (System Designer):** `.github/agents/syspilot.design.agent.md` was modified by System Designer (expanded tool list). This is an installed-instance file, not a product spec file — discarded by CM per standing protocol. Dev Engineer will update `syspilot/agents/` from the new specs; Installer syncs to `.github/agents/`.

### Sign-off

- [x] All levels completed (no ⚠️ DEPRECATED markers remaining)
- [x] All conflicts resolved
- [x] Traceability verified
- [x] Ready for implementation

---

## QM Findings

*QM writes findings directly into this section after each review round. PM records
decisions (fix-now / defer / accept-as-is) with rationale in the same section.
Multiple review rounds are appended as sub-sections. Existing CDs without this
section are unaffected — the section is additive, never required retroactively.*

### Round 1

**Reviewed by:** Quality Manager
**Review date:** 2026-06-30
**Scope:** Full targeted check — L0, L1, L2, trace, schema, and implementation compliance.

#### Findings

| # | Level | Element ID | Finding | Severity |
|---|-------|------------|---------|----------|
| 1 | L2 | `SYSP_SPEC_AGENT_BASE_TOOLSET` | Code block specifies Jarvis tool IDs as `jarvis-core_createSession` etc. (underscore notation, no namespace prefix), but all 13 product agent files (`syspilot/agents/`) and all installed `.github/agents/` files use `enthali.jarvis-core/createSession` (namespace+slash format, which is the actual VS Code MCP extension tool ID). The CR's explicit goal was to make this spec the single source of truth for tool lists; the spec currently documents non-functional tool IDs. The CD "Decisions" section also states "`jarvis-core_*`" which matches the spec error. | high |

#### Validation Notes

- L0: `SYSP_US_INSTALLER` and `SYSP_US_AGENT_ARCH` content and ACs are correct and consistent.
- L1: All six declared L1 elements present with correct trace links. No contradictions or gaps detected. `SYSP_REQ_INSTALLER_WORKFLOW` AC-5 correctly mandates verbatim copy from upstream.
- L2: `SYSP_SPEC_INSTALLER_WORKFLOW` step 4 correctly implements verbatim-from-upstream. `SYSP_SPEC_INSTALLER_DUTIES` "Local Customization Preservation" duty removed correctly. All 13 agent frontmatter specs present and reference `SYSP_SPEC_AGENT_BASE_TOOLSET`.
- Implementation: `vscode/resolveMemoryFileUri` absent from all 13 product agents (Rule 2 ✅). `agent/runSubagent` only in `syspilot.setup.agent.md` (Rule 3 ✅). `syspilot/agents/` and `.github/agents/` in sync ✅.
- Schema: 0 sphinx-needs schema warnings. All declared trace links resolve.

#### PM Decisions

| # | Finding # | Decision | Rationale |
|---|-----------|----------|-----------|
| 1 | 1 | fix-now | Spec is the SSOT for tool IDs. Having the wrong format in the spec directly contradicts the CR's goal. Fixed `SYSP_SPEC_AGENT_BASE_TOOLSET` code block to use `enthali.jarvis-core/` prefix (namespace+slash, matching actual VS Code MCP tool IDs) and updated Rule 4 accordingly. |

### Round 2

**Reviewed by:** Quality Manager
**Review date:** 2026-06-30
**Scope:** `SYSP_SPEC_AGENT_BASE_TOOLSET` only — re-check of Round 1 Finding #1 fix.

#### Findings

No findings. The fix is correct and complete.

- Code block now uses `enthali.jarvis-core/<toolname>` format (namespace+slash) for all 11 Jarvis tool IDs — matching the actual VS Code MCP extension tool ID format used in all 13 product agent files ✅
- Rule 4 prose updated to state `enthali.jarvis-core/<toolname>` and `The legacy enthali.jarvis/ prefix is not used.` ✅
- Spec tool IDs match `syspilot/agents/` and `.github/agents/` agent frontmatter verbatim ✅

**Verdict: Round 1 Finding #1 CLOSED. SYSP_SPEC_AGENT_BASE_TOOLSET is clean.**

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
