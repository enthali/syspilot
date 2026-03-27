# Change Document: prod-inst-migrate

**Status**: draft
**Branch**: feature/product-instance
**Created**: 2026-03-20
**Updated**: 2026-03-27
**Author**: Georg Doll
**Sequence**: 2 of 3

---

## Summary

Migrate existing spec tree to the Agent Family Framework structure defined in Change 1.
All 130 existing specs become syspilot family product specs. Pure structural migration —
no new specs created, no semantic changes. Sphinx must build with 0 errors after migration.

---

## Decisions

1. `docs/31_traceability/` → `docs/traceability/` (framework-level, cross-family)
2. `docs/40_process/` → `docs/syspilot/process/` (family-specific)
3. Syspilot-specific methodology content splits into `docs/syspilot/methodology.md`
4. Syspilot-specific naming content splits into `docs/syspilot/namingconventions.md`
5. `docs/releasenotes.md` stays at framework level (shared across families)
6. `docs/changes/` stays at framework level

## Directory Renames

| Current | New | Notes |
|---------|-----|-------|
| `templates/` | `syspilot/` | Product root |
| `docs/10_userstories/` | `docs/syspilot/userstories/` | Level 0 specs |
| `docs/11_requirements/` | `docs/syspilot/requirements/` | Level 1 specs |
| `docs/12_design/` | `docs/syspilot/design/` | Level 2 specs |
| `docs/31_traceability/` | `docs/traceability/` | Framework level |
| `docs/40_process/` | `docs/syspilot/process/` | Family specific |

## ID Renames (all 130 IDs)

All existing IDs get `SYSPILOT_` prefix:

| Pattern | Count | Example |
|---------|-------|---------|
| `US_*` → `SYSPILOT_US_*` | 27 | `US_CORE_SPEC_AS_CODE` → `SYSPILOT_US_CORE_SPEC_AS_CODE` |
| `REQ_*` → `SYSPILOT_REQ_*` | 51 | `REQ_CHG_ANALYSIS_AGENT` → `SYSPILOT_REQ_CHG_ANALYSIS_AGENT` |
| `SPEC_*` → `SYSPILOT_SPEC_*` | 52 | `SPEC_AGENT_WORKFLOW` → `SYSPILOT_SPEC_AGENT_WORKFLOW` |

## Reference Updates

- All `:links:` directives in all RST files
- All `:id:` directives in all RST files
- `docs/index.rst` — toctree paths
- `docs/conf.py` — exclude patterns
- All sub-`index.rst` files — toctree paths
- Agent files in `syspilot/agents/` (was `templates/agents/`)
- Agent files in `.github/agents/` 
- Skill files in `syspilot/skills/` and `.github/skills/`
- `.github/copilot-instructions.md` — example IDs, directory paths
- `scripts/python/get_need_links.py` — if it references IDs

## Content Splits

### docs/methodology.md → docs/syspilot/methodology.md

Framework methodology.md keeps:
- Overview (agent families, spec-driven principle)
- Repository Structure (family dirs, doc structure, installation)
- ID Naming Convention (overview, reference to namingconventions.md)
- Write Boundaries table
- Cross-Tree Linking

Syspilot family methodology.md gets:
- Three-level hierarchy (US → REQ → SPEC)
- Domain shift at Level 2 (problem domain → solution domain)
- Theme-based file splitting rules
- Level 0/1/2 organization details
- Scaling guidelines

### docs/namingconventions.md → docs/syspilot/namingconventions.md

Framework namingconventions.md keeps:
- ID Format (`FAMILY_TYPE_THEME_SLUG`)
- Family Prefixes table
- Type Abbreviations
- Slug Guidelines
- Uniqueness rules
- Cross-Family Linking

Syspilot family namingconventions.md gets:
- Theme Abbreviations (CORE, WF, CHG, TRACE, INST, DX, REL, DOC)
- Level 2 component themes (AGENT, CHG, IMPL, VERIFY, MECE, TRACE, MEM, DOC, INST, REL)
- Cross-level theme matching rules
- Examples specific to syspilot

## Execution Order

1. Rename directories (git mv)
2. Rename all IDs in RST files (`:id:` and `:links:`)
3. Create `docs/syspilot/methodology.md` and `docs/syspilot/namingconventions.md`
4. Update framework docs (methodology.md, namingconventions.md)
5. Update `docs/index.rst` toctree paths
6. Update all sub-`index.rst` files
7. Update `docs/conf.py`
8. Update agent/skill files (ID references)
9. Update `.github/copilot-instructions.md`
10. Sphinx build validation — 0 errors, 0 warnings

## Dependencies

- prod-inst-concept (Change 1) — naming decisions ✅ approved

## Blocks

- prod-inst-instance (Change 3)
