<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/syspilot-logo-dark.svg">
    <img src="assets/syspilot-logo.svg" alt="syspilot" width="200">
  </picture>
</p>

<p align="center"><strong>Requirements Engineering that scales with AI.</strong></p>

> Your project has 5000 requirements. A change affects 5 of them.
> syspilot follows [sphinx-needs](https://sphinx-needs.readthedocs.io/) traceability links to find exactly those 5 — so your AI agent gets focused context, not the entire codebase.

## Quick Start

**Linux / Mac / GitHub Codespaces:**
```bash
mkdir -p .github/agents && curl -fsSL \
  "https://raw.githubusercontent.com/enthali/syspilot/main/.github/agents/syspilot.setup.agent.md" \
  -o .github/agents/syspilot.setup.agent.md
```

**Windows (PowerShell):**
```powershell
irm https://raw.githubusercontent.com/enthali/syspilot/main/scripts/powershell/init.ps1 | iex
```

Then open VS Code Copilot Chat and run `@syspilot.setup`.

That's it. The setup agent handles dependencies, configuration, and validation automatically.

## What You Get

Seven AI agents that work through your spec hierarchy:

| Agent | What it does |
|-------|-------------|
| `@syspilot.change` | Analyzes a change request, creates a Change Document |
| `@syspilot.implement` | Executes approved changes with traceability |
| `@syspilot.verify` | Checks implementation against the Change Document |
| `@syspilot.mece` | Finds gaps and redundancies in your specs |
| `@syspilot.trace` | Traces one item through all levels |
| `@syspilot.release` | Manages versioning and release process |
| `@syspilot.setup` | Installs/updates syspilot in your project |

## How It Works

```
User Story (WHY)  ──links──▶  Requirements (WHAT)  ──links──▶  Design Specs (HOW)
```

When you request a change, syspilot follows these links to find only the affected elements. **O(affected), not O(total).**

## Documentation

📖 **Full docs:** [enthali.github.io/syspilot](https://enthali.github.io/syspilot/index.html)

Includes methodology, naming conventions, and traceability matrices.

## Requirements

- VS Code + GitHub Copilot
- Python 3.10+

## License

Apache 2.0
