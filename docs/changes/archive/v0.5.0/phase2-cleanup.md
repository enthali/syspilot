# Change Document: phase2-cleanup

**Status**: draft
**Branch**: feature/agent-architecture-v2
**Created**: 2026-04-11
**Author**: System Designer
**Parent**: agent-architecture-v2 (Phase 1)

---

## Summary

Phase 2 cleanup of the Agent Architecture v2 migration. Removes all superseded
`SYSPILOT_` RST files (27 files across 3 levels), updates toctree index files,
re-creates the orchestration skill, and cleans dangling `SYSPILOT_` ID references
from documentation. No new specs are created — this is purely a deletion and
reference-cleanup task. The 36 new `SYSP_` files from Phase 1 remain untouched.

---

## Task 1: Delete Old SYSPILOT_ RST Files

These files have been superseded by the `SYSP_` equivalents created in Phase 1.

### Level 0 — User Stories (8 files)

| File | IDs contained | Superseded by |
|------|---------------|---------------|
| `docs/syspilot/userstories/us_core.rst` | `SYSPILOT_US_CORE_*` | `SYSP_` agent-specific US files |
| `docs/syspilot/userstories/us_workflows.rst` | `SYSPILOT_US_WF_*` | `SYSP_` agent-specific US files |
| `docs/syspilot/userstories/us_change_mgmt.rst` | `SYSPILOT_US_CHG_*` | `SYSP_` agent-specific US files |
| `docs/syspilot/userstories/us_traceability.rst` | `SYSPILOT_US_TRACE_*` | `SYSP_` agent-specific US files |
| `docs/syspilot/userstories/us_installation.rst` | `SYSPILOT_US_INST_*` | `SYSP_` agent-specific US files |
| `docs/syspilot/userstories/us_release.rst` | `SYSPILOT_US_REL_*` | `SYSP_` agent-specific US files |
| `docs/syspilot/userstories/us_developer_experience.rst` | `SYSPILOT_US_DX_*` | `SYSP_` agent-specific US files |
| `docs/syspilot/userstories/us_documentation.rst` | `SYSPILOT_US_DOC_*` | `SYSP_` agent-specific US files |

### Level 1 — Requirements (8 files)

| File | IDs contained | Superseded by |
|------|---------------|---------------|
| `docs/syspilot/requirements/req_core.rst` | `SYSPILOT_REQ_CORE_*` | `SYSP_` agent-specific REQ files |
| `docs/syspilot/requirements/req_workflows.rst` | `SYSPILOT_REQ_WF_*` | `SYSP_` agent-specific REQ files |
| `docs/syspilot/requirements/req_change_mgmt.rst` | `SYSPILOT_REQ_CHG_*` | `SYSP_` agent-specific REQ files |
| `docs/syspilot/requirements/req_traceability.rst` | `SYSPILOT_REQ_TRACE_*` | `SYSP_` agent-specific REQ files |
| `docs/syspilot/requirements/req_installation.rst` | `SYSPILOT_REQ_INST_*` | `SYSP_` agent-specific REQ files |
| `docs/syspilot/requirements/req_release.rst` | `SYSPILOT_REQ_REL_*` | `SYSP_` agent-specific REQ files |
| `docs/syspilot/requirements/req_developer_experience.rst` | `SYSPILOT_REQ_DX_*` | `SYSP_` agent-specific REQ files |
| `docs/syspilot/requirements/req_documentation.rst` | `SYSPILOT_REQ_DOC_*` | `SYSP_` agent-specific REQ files |

### Level 2 — Design Specs (11 files)

| File | IDs contained | Superseded by |
|------|---------------|---------------|
| `docs/syspilot/design/spec_agent_framework.rst` | `SYSPILOT_SPEC_AGENT_*` | `spec_agent_arch.rst` |
| `docs/syspilot/design/spec_change.rst` | `SYSPILOT_SPEC_CHG_*` | `spec_system_designer.rst` |
| `docs/syspilot/design/spec_implement.rst` | `SYSPILOT_SPEC_IMPL_*` | `spec_dev_engineer.rst` |
| `docs/syspilot/design/spec_verify.rst` | `SYSPILOT_SPEC_VERIFY_*` | `spec_quality_mece.rst`, `spec_quality_trace.rst` |
| `docs/syspilot/design/spec_traceability.rst` | `SYSPILOT_SPEC_TRACE_*` | `spec_quality_trace.rst` |
| `docs/syspilot/design/spec_memory.rst` | `SYSPILOT_SPEC_MEM_*` | N/A (functionality folded into agent specs) |
| `docs/syspilot/design/spec_setup.rst` | `SYSPILOT_SPEC_INST_*` | `spec_setup_engineer.rst` |
| `docs/syspilot/design/spec_doc_structure.rst` | `SYSPILOT_SPEC_DOC_*` | `spec_docu_engineer.rst` |
| `docs/syspilot/design/spec_doc_scope_template.rst` | `SYSPILOT_SPEC_DOC_*` | `spec_docu_engineer.rst` |
| `docs/syspilot/design/spec_doc_scope.rst` | `SYSPILOT_SPEC_DOC_*` | `spec_docu_engineer.rst` |
| `docs/syspilot/design/spec_release.rst` | `SYSPILOT_SPEC_REL_*` | `spec_release_engineer.rst` |

**Total: 27 files to delete**

---

## Task 2: Update Toctree Index Files

Remove deleted file entries from the `.. toctree::` directive in each index.

### `docs/syspilot/userstories/index.rst`

**Remove** these toctree entries:
```
us_core
us_workflows
us_change_mgmt
us_traceability
us_installation
us_release
us_developer_experience
us_documentation
```

**Keep** these toctree entries:
```
us_agent_arch
us_project_mgr
us_change_mgr
us_quality_mgr
us_system_designer
us_dev_engineer
us_test_engineer
us_docu_engineer
us_quality_mece
us_quality_trace
us_release_engineer
us_setup_engineer
```

### `docs/syspilot/requirements/index.rst`

**Remove** these toctree entries:
```
req_core
req_workflows
req_change_mgmt
req_traceability
req_installation
req_release
req_developer_experience
req_documentation
```

**Keep** these toctree entries:
```
req_agent_arch
req_project_mgr
req_change_mgr
req_quality_mgr
req_system_designer
req_dev_engineer
req_test_engineer
req_docu_engineer
req_quality_mece
req_quality_trace
req_release_engineer
req_setup_engineer
```

Also update the hierarchy comment in the Overview section: replace `SYSPILOT_US_*`,
`SYSPILOT_REQ_*`, `SYSPILOT_SPEC_*` with `SYSP_US_*`, `SYSP_REQ_*`, `SYSP_SPEC_*`.

### `docs/syspilot/design/index.rst`

**Remove** these toctree entries:
```
spec_agent_framework
spec_change
spec_implement
spec_verify
spec_traceability
spec_memory
spec_setup
spec_doc_structure
spec_doc_scope_template
spec_doc_scope
spec_release
```

**Keep** these toctree entries:
```
spec_agent_arch
spec_project_mgr
spec_change_mgr
spec_quality_mgr
spec_system_designer
spec_dev_engineer
spec_test_engineer
spec_docu_engineer
spec_quality_mece
spec_quality_trace
spec_release_engineer
spec_setup_engineer
```

---

## Task 3: Re-add Orchestration Skill

Create two copies of the orchestration skill (product + installed):

### Files to CREATE

| File | Purpose |
|------|---------|
| `.github/skills/syspilot.orchestration/SKILL.md` | Installed copy (active in workspace) |
| `syspilot/skills/syspilot.orchestration/SKILL.md` | Product copy (distributable) |

### Content Requirements

The orchestration skill SHALL define:

1. **Agent frontmatter semantics** — how `.agent.md` YAML frontmatter declares
   capabilities, tool restrictions, and subagent relationships
2. **Communication pattern** — "Invoke" in any syspilot agent doc means
   `runSubagent()` (not Jarvis messaging, not direct user invocation)
3. **Orchestration hierarchy** — who orchestrates whom:
   - Managers (PM, CM, QM) invoke Engineers as subagents
   - Engineers do NOT invoke other engineers
   - Engineers do NOT invoke managers
4. **runSubagent() conventions** — how to pass context, receive results,
   handle failures

---

## Task 4: Clean Dangling SYSPILOT_ References

Update documentation files that still reference old `SYSPILOT_` IDs.

### Files to UPDATE

| File | What to change |
|------|---------------|
| `.github/copilot-instructions.md` | Update ID examples in Specification Hierarchy and Sphinx-Needs Conventions sections from `SYSPILOT_*` to `SYSP_*` |
| `docs/architecture.md` | Update Mermaid diagram and examples referencing `SYSPILOT_REQ_REL_*`, `SYSPILOT_SPEC_REL_*` |
| `docs/methodology.md` | Update ID examples: `SYSPILOT_US_CORE_SPEC_AS_CODE` → `SYSP_` equivalent |
| `docs/namingconventions.md` | Update all `SYSPILOT_*` example IDs to `SYSP_*` equivalents |
| `docs/workflows.md` | Update `SYSPILOT_REQ_INST_LOCAL_SOURCE` example reference |
| `docs/syspilot/methodology.md` | Update prefix table: `SYSPILOT_US_`, `SYSPILOT_REQ_`, `SYSPILOT_SPEC_` → `SYSP_US_`, `SYSP_REQ_`, `SYSP_SPEC_` |
| `docs/syspilot/namingconventions.md` | Update all `SYSPILOT_*` example IDs to `SYSP_*` equivalents |
| `docs/releasenotes.md` | **Do NOT change** — historical references are intentional |

### Note on Instance Specs

`docs/inst/syspilot/` files may contain `:links:` to old `SYSPILOT_` IDs. These
links will break once the old RST files are deleted. Instance spec links should be
updated to point to the new `SYSP_` equivalents, or instance specs should be
regenerated as a separate follow-up task.

---

## Task 5: Validate

After all changes:

1. Run `cd docs && uv run sphinx-build -b html . _build/html` — must pass with **0 errors**
2. Verify no orphaned toctree warnings
3. Verify no broken `:links:` (needs IDs referencing deleted `SYSPILOT_` elements)

---

## Files Summary

### Files to DELETE (27)

```
docs/syspilot/userstories/us_change_mgmt.rst
docs/syspilot/userstories/us_core.rst
docs/syspilot/userstories/us_developer_experience.rst
docs/syspilot/userstories/us_documentation.rst
docs/syspilot/userstories/us_installation.rst
docs/syspilot/userstories/us_release.rst
docs/syspilot/userstories/us_traceability.rst
docs/syspilot/userstories/us_workflows.rst
docs/syspilot/requirements/req_change_mgmt.rst
docs/syspilot/requirements/req_core.rst
docs/syspilot/requirements/req_developer_experience.rst
docs/syspilot/requirements/req_documentation.rst
docs/syspilot/requirements/req_installation.rst
docs/syspilot/requirements/req_release.rst
docs/syspilot/requirements/req_traceability.rst
docs/syspilot/requirements/req_workflows.rst
docs/syspilot/design/spec_agent_framework.rst
docs/syspilot/design/spec_change.rst
docs/syspilot/design/spec_doc_scope.rst
docs/syspilot/design/spec_doc_scope_template.rst
docs/syspilot/design/spec_doc_structure.rst
docs/syspilot/design/spec_implement.rst
docs/syspilot/design/spec_memory.rst
docs/syspilot/design/spec_release.rst
docs/syspilot/design/spec_setup.rst
docs/syspilot/design/spec_traceability.rst
docs/syspilot/design/spec_verify.rst
```

### Files to CREATE (2)

```
.github/skills/syspilot.orchestration/SKILL.md
syspilot/skills/syspilot.orchestration/SKILL.md
```

### Files to UPDATE (9)

```
docs/syspilot/userstories/index.rst          (remove 8 toctree entries)
docs/syspilot/requirements/index.rst         (remove 8 toctree entries + update hierarchy comment)
docs/syspilot/design/index.rst               (remove 11 toctree entries)
.github/copilot-instructions.md              (update SYSPILOT_ → SYSP_ examples)
docs/architecture.md                         (update SYSPILOT_ → SYSP_ examples)
docs/methodology.md                          (update SYSPILOT_ → SYSP_ examples)
docs/namingconventions.md                    (update SYSPILOT_ → SYSP_ examples)
docs/workflows.md                            (update SYSPILOT_ → SYSP_ example)
docs/syspilot/methodology.md                (update SYSPILOT_ → SYSP_ prefix table)
docs/syspilot/namingconventions.md           (update SYSPILOT_ → SYSP_ examples)
```

### Files to KEEP (do NOT touch)

```
All SYSP_ files (36 RST files)
docs/inst/**                                 (instance specs)
docs/traceability/**
docs/syspilot/process/**
docs/methodology.md                          (update refs only, preserve content)
docs/namingconventions.md                    (update refs only, preserve content)
docs/releasenotes.md                         (historical refs — do NOT change)
```

---

*Generated by syspilot System Designer*
