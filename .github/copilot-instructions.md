# syspilot - Copilot Instructions

> **Scalable Requirements Engineering for AI-Assisted Development**

## Project Overview

syspilot is a requirements engineering toolkit that uses **sphinx-needs traceability links** to provide focused context to AI agents. Instead of scanning entire codebases, syspilot follows links from User Stories → Requirements → Design Specs to find only the affected elements.

**Key Insight**: AI agents need focused context, not the entire codebase. syspilot achieves O(affected) not O(total) complexity.

**Version**: 0.1.0-rc.3

## Tech Stack

- **Documentation**: Sphinx with sphinx-needs extension
- **Markup**: reStructuredText (RST)
- **Python Runner**: uv (Astral's fast Python package manager)
- **Theme**: Furo
- **Process Alignment**: Optional (see `docs/40_process/`)

## Project Structure

```
syspilot/
├── .github/
│   ├── agents/                 # Agent definition files (*.agent.md)
│   ├── prompts/                # Prompt configuration files (*.prompt.md)
│   ├── skills/                 # Shared skill files (*.skill.md)
│   └── copilot-instructions.md # This file
├── scripts/
│   ├── powershell/init.ps1     # Bootstrap script (Windows)
│   ├── bash/init.sh            # Bootstrap script (Linux/Mac)
│   └── python/
│       └── get_need_links.py   # Link discovery utility
├── templates/
│   ├── change-document.md      # Change Document template
│   └── sphinx/                 # Sphinx build script templates
├── docs/                        # Self-documentation (dogfooding)
│   ├── methodology.md          # File organization & methodology guide
│   ├── namingconventions.md    # ID naming conventions
│   ├── releasenotes.md         # Release notes (newest first)
│   ├── 10_userstories/         # Level 0: WHY (User Stories)
│   ├── 11_requirements/        # Level 1: WHAT (Requirements)
│   ├── 12_design/              # Level 2: HOW (Design Specs)
│   ├── 31_traceability/        # Traceability matrices
│   ├── 40_process/             # A-SPICE process alignment
│   ├── changes/                # Change Documents (deleted after release)
│   ├── conf.py                 # Sphinx configuration
│   └── requirements.txt        # Python dependencies for Sphinx
└── version.json                # Release version info
```

## Specification Hierarchy

```
Level 0: User Stories (WHY)     docs/10_userstories/    US_*
         │ :links:
         ▼
Level 1: Requirements (WHAT)    docs/11_requirements/   REQ_*
         │ :links:
         ▼
Level 2: Design Specs (HOW)     docs/12_design/         SPEC_*
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
| User Story | `US_` | `US_CORE_SPEC_AS_CODE` | 0 |
| Requirement | `REQ_` | `REQ_CHG_ANALYSIS_AGENT` | 1 |
| Design Spec | `SPEC_` | `SPEC_AGENT_WORKFLOW` | 2 |

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
5. **Next** → Either start a new change (@change) or proceed to release (@release)

**Agent Handoff Chain:**

```
change → implement → verify → memory → change / release
    ↑                            │
    └────────────────────────────┘ (next change)
```

### Quality Workflow (independent, any time)

- **@syspilot.mece** → Horizontal consistency check on one level
- **@syspilot.trace** → Vertical traceability check for one element
- Both are read-only; findings trigger a change workflow

### Release Workflow (bundles changes)

See `@syspilot.release` agent for full process. Key steps: merge to main → version bump → validate → release notes → tag & push.

## Patterns & Conventions

### File Organization (see [docs/methodology.md](../docs/methodology.md))

Levels 0–1 organize by **problem domain** (stakeholder themes). Level 2 organizes by **solution domain** (technical components). This asymmetry is intentional.

### File Naming

- Agents: `syspilot.<name>.agent.md`
- Prompts: `syspilot.<name>.prompt.md`
- Skills: `syspilot.<name>.skill.md` (shared patterns, e.g., `syspilot.ask-questions.skill.md`)
- User Stories: `us_<theme>.rst` (one per stakeholder theme)
- Requirements: `req_<theme>.rst` (mirrors matching `us_` file)
- Design Specs: `spec_<component>.rst` (one per technical component)
- Change Documents: `docs/changes/<name>.md`

### Sphinx-Needs Authoring

Follow the conventions visible in existing RST files. Key points:
- Always include `:id:`, `:status:`, `:links:` (where applicable)
- Use `SHALL` for mandatory requirements
- Include **Acceptance Criteria** in requirements
- See [docs/namingconventions.md](../docs/namingconventions.md) for ID naming rules

## Agent Interaction

When presenting choices to the user during agent sessions,
read and follow `.github/skills/syspilot.ask-questions.skill.md`.

---

*syspilot v0.1.0-rc.3 - Last updated: 2026-02-11*
