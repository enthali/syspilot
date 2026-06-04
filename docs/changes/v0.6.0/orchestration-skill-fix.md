# Change Document: orchestration-skill-fix

## Summary

Fix three post-merge defects found in `syspilot.orchestration-jarvis` SKILL.md after merge of `orchestration-skill-split`.

## Change Request

**Source:** PM (via Jarvis)
**Branch:** `feature/orchestration-skill-fix`

## Defects Fixed

1. **Description frontmatter** — Rewritten to Copilot discovery format with semantic trigger vocabulary, USE FOR / DO NOT USE FOR boundary, no feature prose.
2. **RESPOND logic** — Removed incorrect instruction to call `jarvis_readMessage()` inside RESPOND. RESPOND now instructs the agent to use the invocation mode already determined at RECEIVE time.
3. **Agent role descriptions removed** — "Communication Pattern" and "Completion Reporting" sections deleted from skill body. These contained Manager→Engineer, Engineer waiting for async work, and completion-reporting format — all role/topology content that violates the AC-4 no-agent-names rule. Applied to both product and instance copies.

## Files Changed

- `syspilot/skills/syspilot.orchestration-jarvis/SKILL.md` — product copy
- `.github/skills/syspilot.orchestration-jarvis/SKILL.md` — instance copy

## Spec Impact

No RST changes required. `SYSP_SPEC_SKILL_ORCHESTRATION_PATTERN` and `SYSP_SPEC_SKILL_ORCHESTRATION_MATRIX` use abstract role terms ("Manager", "Engineer") as routing-semantics vocabulary — this is acceptable at spec level and does not violate AC-4 (which restricts skill body content, not spec-level abstractions).

## Artefakt-Removal Check

Removed sections: "Communication Pattern" and "Completion Reporting"

**Grep results:**

- No references to these section headers found in active agents (`syspilot/agents/`, `.github/agents/`)
- No references in active documentation (`docs/`, `README.md`, `docs/architecture.md`, `docs/workflows.md`)
- Historic Change Documents: `docs/changes/v0.5.3/orchestration-skill-split.md` may reference these sections — acceptable historic stranding (class c), disclosed here.

**Classification:**

- (a) Active code/workflow references: none found
- (b) Active documentation references: none found
- (c) Historic Change Documents: acceptable, disclosed above

## Status

✅ Implemented, committed, pending QM check and PM merge approval.
