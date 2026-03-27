# syspilot Family: Naming Conventions

This document defines naming conventions specific to the **syspilot** agent family.
For framework-level conventions (ID format, family prefixes, slug guidelines),
see [../namingconventions.md](../namingconventions.md).

## Theme Abbreviations

### Level 0 & 1 — Domain Themes

| Abbreviation | Full Name | Used at Levels |
|-------------|-----------|----------------|
| `CORE` | Core Methodology | US, REQ |
| `WF` | Workflows | US, REQ |
| `CHG` | Change Management | US, REQ |
| `TRACE` | Traceability & Quality | US, REQ |
| `INST` | Installation & Setup | US, REQ |
| `DX` | Developer Experience | US, REQ |
| `REL` | Release | US, REQ |
| `DOC` | Documentation | US, REQ |

### Level 2 — Component Themes

Level 2 (Design Specs) uses **component-based** themes instead of domain themes:

| Abbreviation | Full Name | Level |
|-------------|-----------|-------|
| `AGENT` | Agent Architecture | SPEC |
| `CHG` | Change Agent | SPEC |
| `IMPL` | Implement Agent | SPEC |
| `VERIFY` | Verify Agent | SPEC |
| `TRACE` | Traceability (MECE + Trace Agents) | SPEC |
| `MEM` | Memory Agent | SPEC |
| `DOC` | Documentation (Structure, Agent, Scope) | SPEC |
| `INST` | Installation & Setup | SPEC |
| `REL` | Release Process | SPEC |

## Examples by Level

**Level 0 — User Stories:**
```
SYSPILOT_US_CORE_SPEC_AS_CODE        # Core: manage specs as code
SYSPILOT_US_CHG_ANALYZE              # Change Mgmt: analyze changes
SYSPILOT_US_INST_BOOTSTRAP           # Installation: environment bootstrap
SYSPILOT_US_REL_CREATE               # Release: create a release
SYSPILOT_US_DX_PROJECT_MEMORY        # Dev Experience: maintain project memory
SYSPILOT_US_DOC_MAINTAIN             # Documentation: maintain project docs
```

**Level 1 — Requirements:**
```
SYSPILOT_REQ_CORE_SPHINX_NEEDS       # Core: requirements management
SYSPILOT_REQ_CHG_ANALYSIS_AGENT      # Change Mgmt: change analysis agent
SYSPILOT_REQ_INST_AUTO_SETUP         # Installation: automatic env setup
SYSPILOT_REQ_REL_SEMVER              # Release: semantic versioning
SYSPILOT_REQ_TRACE_MECE              # Traceability: MECE review
```

**Level 2 — Design Specs:**
```
SYSPILOT_SPEC_AGENT_WORKFLOW         # Agent component: four-agent workflow
SYSPILOT_SPEC_DOC_STRUCTURE          # Documentation component: structure
SYSPILOT_SPEC_INST_CURL_BOOTSTRAP    # Installation component: curl bootstrap
SYSPILOT_SPEC_REL_VERSION_FORMAT     # Release component: version format
```

## Cross-Level Consistency

The theme abbreviation in a requirement ID does **not** need to match the theme
of the linked User Story. Requirements follow the 1:1 file mapping with User Stories
(see [methodology.md](methodology.md)), but the slug describes the *requirement*,
not the parent story.

For Design Specs, the theme shifts to component names, so mismatches are expected
and healthy:

```rst
.. spec:: Setup Agent Design
   :id: SYSPILOT_SPEC_INST_SETUP_AGENT
   :links: SYSPILOT_REQ_INST_NEW_PROJECT, SYSPILOT_REQ_INST_ADOPT_EXISTING

   .. (SPEC theme is INST because it's an installation component,
       even though REQs come from multiple domains)
```
