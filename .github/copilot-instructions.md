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
├── projects/                        # Jarvis project folders (role-based)
│   ├── project-manager/        # PM: planning, backlog, delegation
│   │   ├── project.yaml
│   │   └── context.md
│   ├── change-manager/         # CM: E2E change orchestration
│   │   ├── project.yaml
│   │   └── context.md
│   └── quality-manager/        # QM: independent quality checks
│       ├── project.yaml
│       └── context.md
├── syspilot/                    # syspilot family product artifacts
│   ├── version.json            # Release version
│   ├── agents/                 # Distributable agents (product)
│   ├── prompts/                # Distributable prompts
│   ├── skills/                 # Distributable skills (includes scripts)
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
│   ├── traceability/           # Cross-family traceability matrices
│   ├── changes/                # Change Documents
│   │   └── archive/            # Archived by version after release
│   ├── conf.py                 # Sphinx configuration
│   └── requirements.txt        # Python dependencies for Sphinx
└── README.md                   # Installation instructions
```

## Specification Hierarchy

```
Level 0: User Stories (WHY)     docs/syspilot/userstories/    SYSP_US_*
         │ :links:
         ▼
Level 1: Requirements (WHAT)    docs/syspilot/requirements/   SYSP_REQ_*
         │ :links:
         ▼
Level 2: Design Specs (HOW)     docs/syspilot/design/         SYSP_SPEC_*
```

## Agent System

### Managers (user-invocable)

| Agent | Persona | Purpose |
|-------|---------|--------|
| `@syspilot.pm` | Project Manager | Feature discussion, backlog, research, delegation |
| `@syspilot.cm` | Change Manager | E2E change orchestration, quality gates |
| `@syspilot.qm` | Quality Manager | Independent quality checks, MECE/Trace dispatch |
| `@syspilot.setup` | Setup Manager | Installation and updates |

### Engineers (subagents)

| Agent | Persona | Purpose |
|-------|---------|--------|
| `@syspilot.design` | System Designer | Level-by-level change analysis, RST writing |
| `@syspilot.implement` | Dev Engineer | Code implementation from specs |
| `@syspilot.uat` | Test Engineer | UAT artifact generation |
| `@syspilot.docu` | Documentation Engineer | Internal + external doc maintenance |
| `@syspilot.mece` | Quality Engineer MECE | Horizontal consistency checks |
| `@syspilot.trace` | Quality Engineer Trace | Vertical traceability checks |
| `@syspilot.release` | Release Engineer | Version, tag, release notes |

## Role-Based Development (Jarvis)

syspilot uses Jarvis as project management tool. Four manager roles, each with their own `projects/<role>/context.md`:

| Role | Folder | Responsibility |
|------|--------|---------------|
| **Project Manager** | `projects/project-manager/` | Plans features, prioritizes backlog, delegates Change Requests |
| **Change Manager** | `projects/change-manager/` | Orchestrates engineers through the change workflow |
| **Quality Manager** | `projects/quality-manager/` | Independent quality checks, dispatches MECE/Trace engineers |
| **Setup Manager** | `projects/setup-manager/` | Installation and updates, environment detection |

**Communication**: Managers communicate via Jarvis message queue (`jarvis_sendToSession` tool → `.jarvis/messages.json`). Each manager owns its `context.md` and keeps it up-to-date.

**Autonomy**: The Change Manager supports two modes: `autonomous` (proceeds without user feedback except UAT) and `user-guided` (requests user approval after each spec level).

## Sphinx-Needs Conventions

### ID Prefixes

| Type | Prefix | Example | Level |
|------|--------|---------|-------|
| User Story | `US_` | `SYSP_US_CORE_SPEC_AS_CODE` | 0 |
| Requirement | `REQ_` | `SYSP_REQ_CHG_ANALYSIS_AGENT` | 1 |
| Design Spec | `SPEC_` | `SYSP_SPEC_AGENT_WORKFLOW` | 2 |

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
python syspilot/skills/syspilot.impact-python/get_need_links.py <ID> --simple
python syspilot/skills/syspilot.impact-python/get_need_links.py <ID> --flat --depth 3
```

## Development Workflow (Dogfooding)

syspilot uses itself for development. Three core workflows:

### Change Workflow (orchestrated by Change Manager)

```
CM receives Change Request
  → System Designer (per-level: impact analysis, analyse, write RST)
  |   → Quality Eng. MECE (advisory per level)
  → Test Engineer (UAT artifacts)
  → Dev Engineer (implementation)
  → Quality Eng. MECE (final check)
  → Release Engineer
  → Documentation Engineer
```

### Quality Workflow (orchestrated by Quality Manager)

```
QM triggered (periodic, on-demand, or PM request)
  → Quality Eng. MECE (all levels)
  → Quality Eng. Trace (sample items)
  → Consolidated Report
  → Change Requests → Change Manager
```

### Release Workflow (bundles changes)

See `@syspilot.release` agent for full process. Key steps: merge to main → version bump → validate → release notes → tag & push.

### Branching Strategy

Development branch with feature branches, main = releases only. See [docs/workflows.md](../docs/workflows.md) for details.

**HARD RULE: ONLY `@syspilot.release` may commit to, merge to, or push to `main`. No exceptions.**

- If you are on `main` and need to make any change, create `feature/<name>` first
- `@syspilot.design` creates `feature/<name>` from `development`
- Feature branches are squash-merged back into `development`
- `@syspilot.setup` (update mode) creates `update/v{version}` from current branch
- All agents commit to the same feature branch
- `@syspilot.release` squash-merges `development` into `main`, bumps version, tags
- Main always equals the latest release — any non-release commit on main is a violation

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

**Skill authoring principle:** Skills describe domain knowledge, not tool syntax. Don't explain what the agent already knows (how to call a script, what `--help` does). Focus on the rules the agent *cannot* derive from the tool itself.

---

*Last updated: 2026-04-15*
