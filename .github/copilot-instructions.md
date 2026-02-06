# syspilot - Copilot Instructions

> **Scalable Requirements Engineering for AI-Assisted Development**

## Project Overview

syspilot is a requirements engineering toolkit that uses **sphinx-needs traceability links** to provide focused context to AI agents. Instead of scanning entire codebases, syspilot follows links from User Stories → Requirements → Design Specs to find only the affected elements.

**Key Insight**: AI agents need focused context, not the entire codebase. syspilot achieves O(affected) not O(total) complexity.

**Version**: 0.1.0-beta

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
│   ├── 10_userstories/         # Level 0: WHY (User Stories)
│   ├── 11_requirements/        # Level 1: WHAT (Requirements)
│   ├── 12_design/              # Level 2: HOW (Design Specs)
│   ├── 31_traceability/        # Traceability matrices
│   ├── 40_process/             # A-SPICE process alignment
│   ├── changes/                # Change Documents
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

syspilot uses itself for development:

1. **Change Request** → `@syspilot.change` creates Change Document
2. **Implementation** → `@syspilot.implement` executes changes
3. **Verification** → `@syspilot.verify` confirms implementation
4. **Memory Update** → `@syspilot.memory` updates this file

## Key Files

| File | Purpose |
|------|---------|
| [docs/conf.py](../docs/conf.py) | Sphinx + sphinx-needs configuration |
| [docs/requirements.txt](../docs/requirements.txt) | Python dependencies |
| [scripts/python/get_need_links.py](../scripts/python/get_need_links.py) | Link discovery utility |
| [templates/change-document.md](../templates/change-document.md) | Change Document template |
| [scripts/powershell/init.ps1](../scripts/powershell/init.ps1) | Bootstrap script |
| [docs/methodology.md](../docs/methodology.md) | File organization & methodology guide |

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
- ✅ Self-documentation with sphinx-needs (14 US, 23 REQ, 10 SPEC)
- ✅ Bootstrap scripts for Windows/Linux (minimal)
- ✅ Link discovery utility
- ✅ Install/Update workflow with backup/rollback
- ✅ Intelligent merge for user-modified agent files
- ✅ `.github/` as single source for agents/prompts
- ⏳ A-SPICE alignment documentation in progress

---

*syspilot v0.1.0-beta - Last updated: 2026-02-06*
