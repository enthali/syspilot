# Naming Conventions

## Overview

syspilot uses **descriptive, human-readable IDs** for all specification elements.
Unlike traditional sequential numbering (e.g., `REQ_001`), descriptive IDs are
self-documenting, grep-friendly, and eliminate the "insert pain" of numbered sequences.

This document covers **framework-level** naming conventions that apply across all
agent families. Family-specific conventions (themes, slug rules, examples) live in
each family's `namingconventions.md` (e.g., `docs/syspilot/namingconventions.md`).

## Why Descriptive IDs?

| Aspect | Sequential (`REQ_001`) | Descriptive (`SYSP_REQ_CORE_SPHINX_NEEDS`) |
|--------|------------------------|------------------------------------------------|
| Self-documenting | No — must look it up | Yes — readable inline |
| Insert new items | Renumber or use gaps | Just pick a name |
| Grep-friendly | Not really | `grep SPHINX_NEEDS` = instant |
| Link readability | Opaque | Clear |
| Ordering bias | Implies priority/sequence | No false hierarchy |
| Duplicate safety | Manual tracking | sphinx-needs catches at build time |

## ID Format

```
<FAMILY>_<TYPE>_<THEME>_<SHORT_SLUG>
```

- **FAMILY**: Agent family prefix (see Family Prefixes below)
- **TYPE**: The specification level (`US`, `REQ`, `SPEC`)
- **THEME**: Abbreviated domain or component identifier (2–5 chars, family-specific)
- **SHORT_SLUG**: Descriptive name in 2–4 words, UPPERCASE, underscores

### Family Prefixes

| Prefix | Scope | Description |
|--------|-------|-------------|
| `SYSP_` | syspilot family | Spec-driven development agents (change, implement, verify, etc.) |
| `SYSMLV2_` | SysMLv2 family | Model-based systems engineering agents *(planned)* |
| `INST_<FAMILY>_` | Instance | Project-specific customization (e.g., `INST_SYSP_`) |
| `COMMON_` | Shared | Cross-family shared specifications |

### Type Abbreviations

Common across all families:

| Type | Level | Directive |
|------|-------|-----------|
| `US` | 0 — User Stories | `.. story::` |
| `REQ` | 1 — Requirements | `.. req::` |
| `SPEC` | 2 — Design Specs | `.. spec::` |

### Theme Abbreviations

Themes are **family-specific**. Each family defines its own themes in
`docs/<family>/namingconventions.md`. The framework only requires themes
to be short (2–5 chars), uppercase, and consistent within the family.

## Directory Naming

| Directory | Purpose | Example |
|-----------|---------|---------|
| `<family>/` | Product artifacts (root) | `syspilot/`, `sysmlv2/` |
| `docs/<family>/` | Family specs | `docs/syspilot/userstories/` |
| `docs/inst/<family>/` | Instance specs | `docs/inst/syspilot/userstories/` |
| `docs/common/` | Shared specs | `docs/common/userstories/` |
| `.github/agents/` | Installed agents (flat) | `syspilot.design.agent.md` |

## Cross-Family Linking

sphinx-needs resolves `:links:` across **all** `.rst` files in the Sphinx project.
Families and instances can link freely:

```rst
.. story:: Release This Project
   :id: INST_SYSP_US_REL_RELEASE
   :links: SYSP_US_REL_AGENT_TEMPLATE

   .. (instance links to family product for context)
```

```rst
.. req:: Model Validation
   :id: SYSMLV2_REQ_MODEL_VALIDATION
   :links: SYSP_REQ_CORE_TRACEABILITY

   .. (SysMLv2 family links to syspilot core for shared traceability)
```

## Uniqueness

sphinx-needs enforces global uniqueness across all `.rst` files at build time.
The family prefix guarantees no collisions between families:
`SYSP_US_CORE_*` can never clash with `SYSMLV2_US_CORE_*`.

## Slug Guidelines

1. **Keep slugs short**: 2–4 words maximum
2. **Be specific**: `ANALYZE` not `DO_ANALYSIS_OF_CHANGES`
3. **Use domain language**: terms stakeholders recognize
4. **Avoid ambiguity**: `NEW_PROJECT` vs `ADOPT_EXISTING`, not `INSTALL_1`
5. **ALL CAPS**: `SYSP_US_CHG_ANALYZE` not `sysp_us_chg_analyze`
6. **Underscores only**: no hyphens, no dots

## Migration from Old IDs

When renaming IDs (e.g., `US_CORE_*` → `SYSP_US_CORE_*`):

1. Build a complete mapping table (old → new)
2. Rename `:id:` directives in specification files
3. Update all `:links:` directives referencing renamed IDs
4. Update references in agent files, scripts, release notes
5. Run `sphinx-build` to validate — it catches any missed references


