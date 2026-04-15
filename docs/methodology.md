# Methodology: Agent Family Framework

## Overview

syspilot follows **spec-driven development** — not just for the product, but also for
processes, methods, and tools. Every decision is traceable through specifications.

Specifications are organized around **agent families** — independent groups of agents
with their own spec trees, release cycles, and domain knowledge. Each family has
a **product** (what it delivers) and each project has an **instance** (how it's used).

## Agent Families

An agent family is a cohesive set of agents, skills, and specifications that address
a specific domain. Families are independent but can share common infrastructure.

| Family | Domain | Agents |
|--------|--------|--------|
| `syspilot` | Spec-driven development (US → REQ → SPEC) | design, implement, uat, verify, release, setup, mece, trace, docu |
| `sysmlv2` | Model-based systems engineering | *(planned)* |
| `common` | Cross-family shared skills | *(as needed)* |

Each family defines its own:
- **Methodology** — how specs are structured within the family
- **Naming conventions** — themes, slug rules, examples
- **Agent templates** — the product artifacts
- **Spec tree** — US → REQ → SPEC (or whatever levels the family uses)

## Repository Structure

### Family Directories (Product)

Each family has a root directory containing its distributable artifacts:

```
syspilot/                       # syspilot family product
├── agents/                     #   Agent templates → .github/agents/
├── prompts/                    #   Prompt configs → .github/prompts/
├── skills/                     #   Shared skills → .github/skills/
│   ├── syspilot.ask-questions/ #     Folder-based, YAML frontmatter
│   ├── syspilot.branching/
│   ├── syspilot.impact-python/
│   └── syspilot.orchestration/
├── scripts/python/             #   Utilities → .syspilot/scripts/
├── sphinx/                     #   Build scripts → docs/
├── templates/                  #   Document templates → .syspilot/templates/
│   └── change-document.md      #   Change doc template
└── version.json                #   Release version

sysmlv2/                        # SysMLv2 family product (future)
├── agents/
├── skills/
└── version.json
```

### Documentation Structure (Specs)

Specs live under `docs/`, grouped by family:

```
docs/
├── syspilot/                   # syspilot family specs
│   ├── userstories/            #   Level 0: WHY
│   ├── requirements/           #   Level 1: WHAT
│   ├── design/                 #   Level 2: HOW
│   ├── methodology.md          #   Family-specific methodology
│   └── namingconventions.md    #   Family-specific naming
│
├── sysmlv2/                    # SysMLv2 family specs (future)
│   ├── userstories/
│   ├── requirements/
│   ├── design/
│   └── methodology.md
│
├── inst/                       # Instance specs (project-specific)
│   ├── syspilot/               #   syspilot instance
│   │   ├── userstories/        #     e.g. "how we release"
│   │   ├── requirements/
│   │   └── design/
│   └── sysmlv2/                #   SysMLv2 instance (future)
│       ├── userstories/
│       ├── requirements/
│       └── design/
│
├── common/                     # Shared specs (optional, cross-family)
│   ├── userstories/
│   ├── requirements/
│   └── design/
│
├── traceability/               # Cross-tree traceability matrices
├── changes/                    # Change Documents
│   └── archive/                #   Archived by version after release
├── methodology.md              # THIS FILE (framework-level)
├── namingconventions.md        # Framework naming conventions
└── releasenotes.md             # Release notes (newest first)
```

### Installation Directory

All installed agents live flat in `.github/agents/`, regardless of family:

```
.github/agents/
├── syspilot.design.agent.md    # syspilot family
├── syspilot.release.agent.md
├── sysmlv2.model.agent.md      # SysMLv2 family (future)
└── ...
```

The agent filename prefix (`syspilot.`, `sysmlv2.`) identifies the family.

## ID Naming Convention

IDs follow the pattern `FAMILY_TYPE_THEME_SLUG`:

```
SYSP_US_CORE_SPEC_AS_CODE          # syspilot family, User Story
SYSMLV2_REQ_MODEL_VALIDATION        # SysMLv2 family, Requirement
INST_SYSP_US_REL_RELEASE            # Instance, syspilot family
COMMON_SPEC_TOOL_INTEGRATION        # Common, shared across families
```

See [namingconventions.md](namingconventions.md) for full rules.

## Write Boundaries

Each agent has a defined scope of what it may write:

| Agent | Writes to | Never writes to |
|-------|-----------|-----------------|
| System Designer (`design`) | Family specs OR Instance specs | — |
| Implement Agent | `<family>/` (product artifacts) | `.github/agents/` |
| Setup Agent | `.github/` (installation) | `<family>/` |
| Release Agent | `docs/`, version files | `.github/agents/` |
| Test Engineer (`uat`) | Status updates in specs | — |
| Documentation Engineer (`docu`) | `.github/copilot-instructions.md`, `docs/` | `<family>/` |

The **Setup Agent** is the only agent that syncs `<family>/` → `.github/`.

## Agents and Skills

**Agents are stable, universal processes** (WHAT to do). They define the workflow
steps — analyze, implement, verify, document — independent of any specific tooling.

**Skills are exchangeable tool bindings** (HOW to do it). They encapsulate domain
knowledge and tool-specific behavior that agents invoke. Skills are folder-based
(`.github/skills/<name>/SKILL.md`) with YAML frontmatter declaring `name` and
`description`. Copilot discovers and invokes them automatically.

**Customization principle:** Customers customize syspilot by swapping or adding
Skills, not by modifying Agents. An agent’s process stays the same across projects;
the skills it calls adapt to the project’s tools and domain.

sphinx-needs resolves `:links:` directives across **all files** in the Sphinx project.
Families and instances can link freely to each other:

```
Instance                    Family Product            Family Product
INST_SYSP_US_RELEASE ──→ SYSP_US_REL_AGENT ──→ SYSP_REQ_REL_PROCESS_DOC
```

The System Designer follows these links to provide context from product specs when
analyzing instance changes — the same mechanism used for any change analysis.

## Family Methodology Reference

Each family defines its own methodology in `docs/<family>/methodology.md`:

- **syspilot**: Three-level hierarchy (US → REQ → SPEC), domain shift at Level 2,
  theme-based file splitting. See `docs/syspilot/methodology.md`.
- **sysmlv2**: *(to be defined)*

sphinx-needs traceability links bridge this boundary, maintaining full visibility
from *why* through *what* to *how* — regardless of how files are organized.

---

*For the Product/Instance concept, see [architecture.md](architecture.md).
For the development process, see [workflows.md](workflows.md).*
