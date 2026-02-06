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
- **Process Alignment**: Automotive SPICE (A-SPICE)

## Project Structure

```
syspilot/
├── .github/
│   ├── agents/                 # Agent definition files (*.agent.md)
│   ├── prompts/                # Prompt configuration files (*.prompt.md)
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
│   │   ├── us_core.rst         # Core methodology stories
│   │   ├── us_workflows.rst    # Workflow orchestration stories
│   │   ├── us_change_mgmt.rst  # Change management stories
│   │   ├── us_traceability.rst # Traceability & quality stories
│   │   ├── us_installation.rst # Installation stories
│   │   ├── us_release.rst      # Release stories
│   │   └── us_developer_experience.rst
│   ├── 11_requirements/        # Level 1: WHAT (Requirements)
│   │   └── req_<theme>.rst     # 1:1 mapping with us_<theme>.rst
│   ├── 12_design/              # Level 2: HOW (Design Specs)
│   │   ├── spec_agent_framework.rst  # Shared agent workflow & prompts
│   │   ├── spec_change.rst           # Change Agent design
│   │   ├── spec_implement.rst        # Implement Agent design
│   │   ├── spec_verify.rst           # Verify Agent design
│   │   ├── spec_traceability.rst     # MECE + Trace Agents
│   │   ├── spec_memory.rst           # Memory Agent design
│   │   ├── spec_setup.rst            # Setup Agent design
│   │   ├── spec_doc_structure.rst    # Documentation structure
│   │   └── spec_release.rst          # Release pipeline
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

### Directive Format

```rst
.. req:: Requirement Title
   :id: REQ_FEATURE_001
   :status: draft
   :priority: mandatory
   :links: US_FEATURE_001

   The system SHALL do something specific.

   **Acceptance Criteria:**
   - Criterion 1
   - Criterion 2
```

### Status Values

- `draft` - Initial creation
- `in-review` - Under review
- `approved` - Approved for implementation
- `implemented` - Code complete
- `verified` - Tests passing

## Development Commands

### Build Documentation

```powershell
# Using build script (recommended)
.\docs\build.ps1

# Clean build
.\docs\build.ps1 -Clean

# Direct uv command (from docs/ directory)
cd docs
uv run sphinx-build -b html . _build/html
```

### Query Sphinx-Needs Links

```powershell
# Get links for a specific ID
python scripts/python/get_need_links.py US_CORE_SPEC_AS_CODE --simple

# Trace with depth
python scripts/python/get_need_links.py REQ_CHG_ANALYSIS_AGENT --depth 2

# Flat list of all impacted IDs
python scripts/python/get_need_links.py US_CORE_SPEC_AS_CODE --flat --depth 3
```

## Installation Workflow

syspilot uses a two-step installation:

### Step 1: Init Script (minimal)

```powershell
# From your project directory, run syspilot's init script
C:\path\to\syspilot\scripts\powershell\init.ps1
```

This only copies `syspilot.setup.agent.md` to `.github/agents/`.

### Step 2: Setup Agent (interactive)

Open VS Code, start GitHub Copilot Chat, select `@syspilot.setup`.

The agent handles:
- Dependency installation (sphinx, sphinx-needs, furo, myst-parser)
- Copying remaining agents and prompts
- VS Code configuration
- Validation

### Update Process

Updates use backup/rollback:
1. `.syspilot/` → `.syspilot_backup/`
2. Download latest release
3. Intelligent merge for modified agent files
4. Success: delete backup / Failure: rollback

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

1. **Merge** feature branch to main (squash)
2. **Version** → Determine version, update `version.json`
3. **Validate** → `sphinx-build`, schema validation
4. **Release Notes** → Prepend to `docs/releasenotes.md`
5. **Clean up** → Delete processed Change Documents
6. **Tag & Push** → Annotated tag triggers GitHub Actions
7. **Next** → Start a new change workflow (@change) or end

## Key Files

| File | Purpose |
|------|---------|
| [docs/conf.py](../docs/conf.py) | Sphinx + sphinx-needs configuration |
| [docs/requirements.txt](../docs/requirements.txt) | Python dependencies |
| [scripts/python/get_need_links.py](../scripts/python/get_need_links.py) | Link discovery utility |
| [templates/change-document.md](../templates/change-document.md) | Change Document template |
| [scripts/powershell/init.ps1](../scripts/powershell/init.ps1) | Bootstrap script |
| [docs/methodology.md](../docs/methodology.md) | File organization & methodology guide |
| [docs/namingconventions.md](../docs/namingconventions.md) | ID naming conventions |
| [docs/releasenotes.md](../docs/releasenotes.md) | Release notes (newest first) |

## Dependencies

From `docs/requirements.txt`:

```
sphinx>=7.0.0
sphinx-needs>=2.0.0
furo>=2024.0.0
myst-parser>=2.0.0
graphviz>=0.20.0
```

**Note**: No `pyproject.toml` yet - dependencies managed via `docs/requirements.txt` and `uv run`.

## Patterns & Conventions

### File Organization (see [docs/methodology.md](../docs/methodology.md))

Levels 0–1 organize by **problem domain** (stakeholder themes). Level 2 organizes by **solution domain** (technical components). This asymmetry is intentional.

- **Level 0 — User Stories**: one `us_<theme>.rst` per stakeholder theme/value stream
- **Level 1 — Requirements**: one `req_<theme>.rst` per US file (1:1 mapping)
- **Level 2 — Design Specs**: one `spec_<component>.rst` per technical component (independent of US structure)

### File Naming

- Agents: `syspilot.<name>.agent.md`
- Prompts: `syspilot.<name>.prompt.md`
- User Stories: `us_<theme>.rst` (one per stakeholder theme)
- Requirements: `req_<theme>.rst` (mirrors matching `us_` file)
- Design Specs: `spec_<component>.rst` (one per technical component)

### RST Formatting

- Use `.. <directive>::` for sphinx-needs elements
- Always include `:id:`, `:status:`, `:links:` (where applicable)
- Use `SHALL` for mandatory requirements
- Include **Acceptance Criteria** in requirements

### Change Documents

- Stored in `docs/changes/<name>.md`
- Track status per level (⏳ not started | 🔄 in progress | ✅ completed)
- Include horizontal MECE checks

## Current State

- ✅ Core agent system implemented (7 agents)
- ✅ Self-documentation with sphinx-needs (18 US, 28 REQ, 36 SPEC)
- ✅ L2 design specs split by component (9 spec files)
- ✅ File organization methodology formalized in spec chain
- ✅ Core workflows (change, quality, release) formalized in spec chain
- ✅ Bootstrap scripts for Windows/Linux (minimal)
- ✅ Link discovery utility
- ✅ Install/Update workflow with backup/rollback
- ✅ Intelligent merge for user-modified agent files
- ✅ `.github/` as single source for agents/prompts
- ⏳ A-SPICE alignment documentation in progress

---

*syspilot v0.1.0-rc.3 - Last updated: 2026-02-06*
