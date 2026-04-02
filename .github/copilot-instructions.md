# syspilot - Copilot Instructions

> **Scalable Requirements Engineering for AI-Assisted Development**

## Project Overview

syspilot is a requirements engineering toolkit that uses **sphinx-needs traceability links** to provide focused context to AI agents. Instead of scanning entire codebases, syspilot follows links from User Stories → Requirements → Design Specs to find only the affected elements.

**Key Insight**: AI agents need focused context, not the entire codebase. syspilot achieves O(affected) not O(total) complexity.

**Principle**: Spec-driven development for everything — not just the product, but also processes, methods, and tools. Every decision is traceable through User Stories → Requirements → Design Specs.

## Tech Stack

- **Documentation**: Sphinx with sphinx-needs extension
- **Markup**: reStructuredText (RST) + Markdown (MyST)
- **Diagrams**: Mermaid via sphinxcontrib-mermaid (client-side rendering)
- **Python Runner**: uv (Astral's fast Python package manager)
- **Theme**: Furo
- **Process Alignment**: Optional (see `docs/syspilot/process/`)

## Project Structure

```
syspilot/                            # Repository root (also the product dir)
├── .github/
│   ├── agents/                 # Installed agent files (*.agent.md)
│   ├── prompts/                # Prompt configuration files (*.prompt.md)
│   ├── skills/                 # Shared skill files (*/SKILL.md)
│   └── copilot-instructions.md # This file
├── scripts/
│   └── python/
│       └── get_need_links.py   # Link discovery utility (consumer copy)
├── syspilot/                    # syspilot family product artifacts
│   ├── version.json            # Release version
│   ├── agents/                 # Distributable agents (product)
│   ├── prompts/                # Distributable prompts
│   ├── skills/                 # Distributable skills
│   ├── scripts/python/         # Distributable scripts
│   ├── sphinx/                 # Sphinx build script templates
│   └── templates/              # Document templates
│       └── change-document.md  # Change Document template
├── docs/
│   ├── methodology.md          # Framework methodology
│   ├── architecture.md         # Product/Instance concept
│   ├── workflows.md            # Workflows & branching strategy
│   ├── namingconventions.md    # Framework naming conventions
│   ├── releasenotes.md         # Release notes (newest first)
│   ├── syspilot/               # syspilot family specs (product-level)
│   │   ├── userstories/        # Level 0: WHY (User Stories)
│   │   ├── requirements/       # Level 1: WHAT (Requirements)
│   │   ├── design/             # Level 2: HOW (Design Specs)
│   │   ├── process/            # A-SPICE process alignment
│   │   ├── methodology.md      # Family-specific methodology
│   │   └── namingconventions.md # Family-specific naming
│   ├── inst/syspilot/          # Instance-level specs (project-specific)
│   │   ├── userstories/        # Instance User Stories
│   │   ├── requirements/       # Instance Requirements
│   │   └── design/             # Instance Design Specs
│   ├── traceability/           # Cross-family traceability matrices
│   ├── changes/                # Change Documents
│   │   └── archive/            # Archived by version after release
│   ├── conf.py                 # Sphinx configuration
│   └── requirements.txt        # Python dependencies for Sphinx
└── README.md                   # Installation instructions
```

## Specification Hierarchy

```
Level 0: User Stories (WHY)     docs/syspilot/userstories/    SYSPILOT_US_*
         │ :links:
         ▼
Level 1: Requirements (WHAT)    docs/syspilot/requirements/   SYSPILOT_REQ_*
         │ :links:
         ▼
Level 2: Design Specs (HOW)     docs/syspilot/design/         SYSPILOT_SPEC_*

Instance specs (project-specific)  docs/inst/syspilot/           INST_SYSPILOT_*
```

## Agent System

| Agent | Purpose |
|-------|---------|
| `@syspilot.setup` | Install/update syspilot in a project |
| `@syspilot.change` | Analyze change requests level-by-level |
| `@syspilot.implement` | Execute approved changes with traceability |
| `@syspilot.verify` | Verify implementation matches Change Document |
| `@syspilot.mece` | Check one level for MECE properties |
| `@syspilot.trace` | Trace one item through all levels |
| `@syspilot.memory` | Keep copilot-instructions.md up-to-date |

## Sphinx-Needs Conventions

### ID Prefixes

| Type | Prefix | Example | Level |
|------|--------|---------|-------|
| User Story | `US_` | `SYSPILOT_US_CORE_SPEC_AS_CODE` | 0 |
| Requirement | `REQ_` | `SYSPILOT_REQ_CHG_ANALYSIS_AGENT` | 1 |
| Design Spec | `SPEC_` | `SYSPILOT_SPEC_AGENT_WORKFLOW` | 2 |
| Instance | `INST_` | `INST_SYSPILOT_SPEC_REL_AGENT_CONFIG` | 0–2 |

### Theme Abbreviations

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

Level 2 uses component-based themes: `AGENT`, `CHG`, `IMPL`, `VERIFY`, `MECE`, `TRACE`, `MEM`, `DOC`, `INST`, `REL`.

See [docs/namingconventions.md](../docs/namingconventions.md) for full conventions.

## Development Commands

```powershell
# Build documentation (from docs/ directory)
cd docs
uv run sphinx-build -b html . _build/html

# Query sphinx-needs links
python scripts/python/get_need_links.py <ID> --simple
python scripts/python/get_need_links.py <ID> --flat --depth 3
```

## Development Workflow (Dogfooding)

syspilot uses itself for development. Three core workflows:

### Change Workflow (per change)

1. **@syspilot.change** → Analyze request, create Change Document (US → REQ → SPEC)
2. **@syspilot.implement** → Execute approved changes from Change Document
3. **@syspilot.verify** → Validate implementation against Change Document
4. **@syspilot.memory** → Update copilot-instructions.md
6. **Next** → Either start a new change (@change) or proceed to release (@release)

**Agent Handoff Chain:**

```
change → implement → verify → memory → change / release
    ↑                                │
    └────────────────────────────────┘ (next change)
```

### Quality Workflow (independent, any time)

- **@syspilot.mece** → Horizontal consistency check on one level
- **@syspilot.trace** → Vertical traceability check for one element
- Both are read-only; findings trigger a change workflow

### Release Workflow (bundles changes)

See `@syspilot.release` agent for full process. Key steps: merge to main → version bump → validate → release notes → tag & push.

### Branching Strategy

Chained feature branches, main = releases only. See [docs/workflows.md](../docs/workflows.md) for details.

- `@syspilot.change` creates `feature/<name>` from latest feature branch (not main)
- `@syspilot.setup` (update mode) creates `update/v{version}` from current branch
- All agents commit to the same feature branch
- Squash merge to main only during `@syspilot.release`
- Main always equals the latest release

## Patterns & Conventions

### File Organization (see [docs/methodology.md](../docs/methodology.md))

Levels 0–1 organize by **problem domain** (stakeholder themes). Level 2 organizes by **solution domain** (technical components). This asymmetry is intentional.

### File Naming

- Agents: `syspilot.<name>.agent.md`
- Prompts: `syspilot.<name>.prompt.md`
- Skills: `.github/skills/syspilot.<name>/SKILL.md` (folder-based, YAML frontmatter with `name`/`description`)
- User Stories: `us_<theme>.rst` (one per stakeholder theme)
- Requirements: `req_<theme>.rst` (mirrors matching `us_` file)
- Design Specs: `spec_<component>.rst` (one per technical component)
- Change Documents: `docs/changes/<name>.md`
- Validation Reports: `docs/changes/val-<name>.md`

### Sphinx-Needs Authoring

Follow the conventions visible in existing RST files. Key points:
- Always include `:id:`, `:status:`, `:links:` (where applicable)
- Use `SHALL` for mandatory requirements
- Include **Acceptance Criteria** in requirements
- See [docs/namingconventions.md](../docs/namingconventions.md) for ID naming rules

## Agent Interaction

Skill files use VS Code standard format (`.github/skills/<name>/SKILL.md` with YAML
frontmatter). Copilot discovers and invokes skills automatically based on the `description`
field — no manual references needed.

---

*Last updated: 2026-04-03*
