# Naming Conventions

## Overview

syspilot uses **descriptive, human-readable IDs** for all specification elements.
Unlike traditional sequential numbering (e.g., `REQ_001`), descriptive IDs are
self-documenting, grep-friendly, and eliminate the "insert pain" of numbered sequences.

## Why Descriptive IDs?

| Aspect | Sequential (`US_CORE_001`) | Descriptive (`US_CORE_SPEC_AS_CODE`) |
|--------|--------------------------|--------------------------------------|
| Self-documenting | No — must look it up | Yes — readable inline |
| Insert new items | Renumber or use gaps | Just pick a name |
| Grep-friendly | Not really | `grep SPEC_AS_CODE` = instant |
| Link readability | `:links: US_CORE_001` — opaque | `:links: US_CORE_SPEC_AS_CODE` — clear |
| Ordering bias | Implies priority/sequence | No false hierarchy |
| Duplicate safety | Manual tracking | sphinx-needs catches at build time |

**The only trade-off** is length, but with short slugs (2–4 words) this is very manageable.

## ID Format

```
<TYPE>_<THEME>_<SHORT_SLUG>
```

- **TYPE**: The specification level prefix (`US`, `REQ`, `SPEC`)
- **THEME**: Abbreviated domain/component identifier (2–5 chars)
- **SHORT_SLUG**: Descriptive name in 2–4 words, UPPERCASE, underscores

### Theme Abbreviations

| Abbreviation | Full Name | Used at Levels |
|-------------|-----------|----------------|
| `CORE` | Core Methodology | US, REQ |
| `CHG` | Change Management | US, REQ |
| `TRACE` | Traceability & Quality | US, REQ |
| `INST` | Installation & Setup | US, REQ |
| `DX` | Developer Experience | US, REQ |
| `REL` | Release | US, REQ |

Level 2 (Design Specs) uses **component-based** themes instead of domain themes:

| Abbreviation | Full Name | Level |
|-------------|-----------|-------|
| `AGENT` | Agent Architecture | SPEC |
| `DOC` | Documentation Structure | SPEC |
| `INST` | Installation Scripts | SPEC |
| `REL` | Release Process | SPEC |

### Examples by Level

**Level 0 — User Stories:**
```
US_CORE_SPEC_AS_CODE        # Core: manage specs as code
US_CHG_ANALYZE              # Change Mgmt: analyze changes
US_INST_BOOTSTRAP           # Installation: environment bootstrap
US_REL_CREATE               # Release: create a release
US_DX_PROJECT_MEMORY        # Dev Experience: maintain project memory
```

**Level 1 — Requirements:**
```
REQ_CORE_SPHINX_NEEDS       # Core: requirements management with sphinx-needs
REQ_CHG_ANALYSIS_AGENT      # Change Mgmt: change analysis agent
REQ_INST_AUTO_SETUP         # Installation: automatic environment setup
REQ_REL_SEMVER              # Release: semantic versioning
REQ_TRACE_MECE              # Traceability: MECE review
```

**Level 2 — Design Specs:**
```
SPEC_AGENT_WORKFLOW         # Agent component: four-agent workflow
SPEC_DOC_STRUCTURE          # Documentation component: sphinx-needs structure
SPEC_INST_INIT_SCRIPTS      # Installation component: init scripts
SPEC_REL_VERSION_FORMAT     # Release component: version format
```

## Slug Guidelines

1. **Keep slugs short**: 2–4 words maximum
2. **Be specific**: `ANALYZE` not `DO_ANALYSIS_OF_CHANGES`
3. **Use domain language**: terms stakeholders recognize
4. **Avoid ambiguity**: `NEW_PROJECT` vs `ADOPT_EXISTING`, not `INSTALL_1` vs `INSTALL_2`
5. **ALL CAPS**: `US_CHG_ANALYZE` not `US_chg_analyze`
6. **Underscores only**: no hyphens, no dots

## Cross-Level Consistency

The theme abbreviation in a requirement ID does **not** need to match the theme
of the linked User Story. Requirements follow the 1:1 file mapping with User Stories
(see [methodology.md](methodology.md)), but the slug describes the *requirement*,
not the parent story.

```rst
.. req:: Change Analysis Agent
   :id: REQ_CHG_ANALYSIS_AGENT
   :links: US_CHG_ANALYZE

   .. (theme CHG matches because the REQ and US are in the same domain)
```

For Design Specs, the theme shifts to component names, so mismatches are expected
and healthy:

```rst
.. spec:: Setup Agent Design
   :id: SPEC_INST_SETUP_AGENT
   :links: REQ_INST_NEW_PROJECT, REQ_INST_ADOPT_EXISTING, REQ_INST_SPHINX_NEEDS_DEP

   .. (SPEC theme is INST because it's an installation component,
       even though REQs come from multiple domains)
```

## Uniqueness

sphinx-needs enforces global uniqueness across all `.rst` files at build time.
If two items share an ID, the build fails with an explicit error. This makes
descriptive IDs **safer** than sequential numbers (where duplicates across files
are easy to create accidentally).

## Migration from Sequential IDs

When renaming from sequential to descriptive IDs:

1. Build a complete mapping table (old → new)
2. Rename `:id:` directives in specification files
3. Update all `:links:` directives referencing renamed IDs
4. Update references in agent files, scripts, release notes
5. Run `sphinx-build` to validate — it will catch any missed references
