# syspilot

**Scalable Requirements Engineering for AI-Assisted Development**

> The key insight: AI agents need focused context, not the entire codebase. syspilot uses [sphinx-needs](https://sphinx-needs.readthedocs.io/) links to navigate from high-level User Stories down to only the affected Requirements and Design elements. This makes it scale to large projects.

## The Problem

AI coding assistants struggle with large projects because they can't process everything at once. When you ask for a change, which of your 500 requirements are affected? Which design specs need updates?

## The Solution

syspilot uses **traceability links** to find exactly what's needed:

```
User Story (few)
     │ linked to
     ▼
Requirements (subset)     ← Only the affected ones!
     │ linked to  
     ▼
Design Specs (subset)     ← Only the affected ones!
     │
     ▼
Focused Implementation
```

Instead of scanning everything, syspilot follows the links. A project with 1000 requirements might only have 5 affected by your change. That's the context the AI needs.

---

## Quick Start

### 1. Download Release

Go to [Releases](https://github.com/enthali/syspilot/releases) and download the latest `Source code (zip)`.

### 2. Extract Anywhere

Extract the ZIP to any location on your system. The release contains a versioned folder structure:

```
syspilot-0.1.0-beta.3/
├── .github/agents/      # Agent definitions
├── scripts/             # Installation scripts
├── templates/           # Document templates
├── docs/                # Documentation
└── version.json         # Version info
```

**Note:** syspilot automatically detects its location via `version.json` - no manual configuration needed!

### 3. Run Init Script

Navigate to the init script inside the extracted folder and run it:

```powershell
# Windows (from your project directory)
C:\path\to\syspilot-0.1.0-beta.3\scripts\powershell\init.ps1

# Linux/Mac (from your project directory)
/path/to/syspilot-0.1.0-beta.3/scripts/bash/init.sh
```

This copies the **Setup Agent** to `.github/agents/` in your project.

### 4. Start Setup Agent

Open VS Code Copilot Chat and type:

```
@syspilot.setup
```

The Setup Agent will:
- **Auto-detect** syspilot location (via `version.json`)
- Copy remaining agents and prompts to your project
- Check and install dependencies (sphinx, sphinx-needs, etc.)
- Validate installation with sphinx-build
- Confirm success

**No manual path configuration needed!** The agent finds syspilot automatically.

## How It Works

### Link-Based Context Discovery

When you request a change, syspilot:

1. Identifies affected User Stories (Level 0)
2. Follows `:links:` to find affected Requirements (Level 1)
3. Follows `:links:` to find affected Design Specs (Level 2)
4. Works only with this focused subset

This is why it scales: **O(affected) not O(total)**.

### Specification Hierarchy

```
┌─────────────────────────────────────────────────────────────────┐
│  Level 0: User Stories (WHY)                                    │
│  "As a user, I want X so that Y"                                │
└──────────────────────────┬──────────────────────────────────────┘
                           │ :links:
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│  Level 1: Requirements (WHAT)                                   │
│  "System SHALL do X" + Acceptance Criteria                      │
└──────────────────────────┬──────────────────────────────────────┘
                           │ :links:
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│  Level 2: Design/Specs (HOW)                                    │
│  Technical design, architecture, interfaces                     │
└─────────────────────────────────────────────────────────────────┘
```

## Agents

| Agent | Purpose |
|-------|---------|
| `@syspilot.change` | Analyze change requests level-by-level, create Change Documents |
| `@syspilot.implement` | Execute approved changes with full traceability |
| `@syspilot.verify` | Verify implementation matches the Change Document |
| `@syspilot.mece` | Check one level for MECE properties (redundancies, gaps) |
| `@syspilot.trace` | Trace one item through all levels |
| `@syspilot.memory` | Keep copilot-instructions.md up-to-date |
| `@syspilot.setup` | Install/update syspilot in a project |

## Workflow

```
User Request
     │
     ▼
┌─────────────┐
│   change    │ ──→ Change Document (US + REQ + SPEC changes)
└─────────────┘      Only affected elements, found via links
     │
     ▼ (approved)
┌─────────────┐
│  implement  │ ──→ Docs + Code + Tests with traceability
└─────────────┘
     │
     ▼
┌─────────────┐
│   verify    │ ──→ Verification Report
└─────────────┘
```

## Project Structure

When installed in your project:

```
your-project/
├── .github/
│   ├── agents/                  # ← Agents deployed here
│   │   ├── syspilot.change.agent.md
│   │   ├── syspilot.implement.agent.md
│   │   └── ...
│   └── copilot-instructions.md  # Project memory
└── docs/                        # ← Your documentation
    ├── 10_userstories/          # User Stories (WHY)
    ├── 11_requirements/         # Requirements (WHAT)
    ├── 12_design/               # Design Specs (HOW)
    ├── conf.py                  # Sphinx configuration
    └── requirements.txt         # Python dependencies

# syspilot source (extracted anywhere)
C:\Downloads\syspilot-0.1.0-beta.3\  # ← Or any other location
    ├── .github/agents/          # Source agent files
    ├── scripts/                 # Installation scripts
    ├── templates/               # Templates
    └── version.json             # Auto-detection marker
```

## Requirements

- **VS Code** with GitHub Copilot extension
- **Python 3.10+**
- **sphinx-needs** in your project

## Why sphinx-needs?

[sphinx-needs](https://sphinx-needs.readthedocs.io/) provides:
- Structured requirements in RST format
- `:links:` directive for traceability
- JSON export for tooling (`needs_id/*.json`)
- Validation of links and IDs

syspilot reads the JSON output to discover what's linked to what.

## License

Apache 2.0

## Contributing

Contributions welcome! Use the syspilot workflow:

1. `@syspilot.change` - Create a Change Document
2. `@syspilot.implement` - Implement the change
3. `@syspilot.verify` - Verify the implementation
4. Submit a Pull Request

---

*syspilot - Focused context for scalable AI-assisted development*
