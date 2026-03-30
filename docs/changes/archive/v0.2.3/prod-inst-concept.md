# Change Document: prod-inst-concept

**Status**: approved
**Branch**: feature/product-instance
**Created**: 2026-03-20
**Author**: Georg Doll
**Sequence**: 1 of 3

---

## Summary

Establish the Agent Family Framework architecture. Specifications are organized
around agent families (syspilot, sysmlv2, ...) with independent spec trees,
release cycles, and instance customizations. Framework-level docs (methodology,
naming conventions) are separated from family-specific docs. The spec-driven
development principle is codified.

---

## Decisions (evolved through discussion)

1. **Agent Families**: Independent groups of agents with own spec trees and releases
2. **Family-based naming**: `SYSPILOT_US_*`, `SYSMLV2_US_*`, `INST_SYSPILOT_US_*`
3. **Product directory**: `syspilot/` at root (rename from `templates/`)
4. **Spec structure**: `docs/syspilot/`, `docs/inst/syspilot/`, `docs/common/`
5. **Two-level docs**: Framework methodology (root) + Family methodology (per family)
6. **Write boundaries**: Implement → `<family>/`, Setup → `.github/`
7. **Open source**: Customers see both family specs AND instance specs as reference
8. **Spec-driven principle**: Everything is specified — product, process, and tools
9. **Installation flat**: `.github/agents/` contains all families, prefixed by family name

## Files Changed

- `docs/methodology.md` — Rewritten as Framework Methodology (families, structure, boundaries)
- `docs/namingconventions.md` — Rewritten as Framework Naming (FAMILY_TYPE_THEME_SLUG)
- `docs/12_design/spec_doc_scope.rst` — SPEC_DOC_METHODOLOGY_STRUCTURE and SPEC_DOC_NAMING_STRUCTURE split into framework/family levels
- `.github/copilot-instructions.md` — Added spec-driven principle
- `docs/changes/prod-inst-concept.md` — This file

## Blocks

- Change 2 (prod-inst-migrate): Rename directories, rename IDs, fix all references
- Change 3 (prod-inst-instance): Build instance tree, demonstrate the pattern
