> **V2 STATUS: TO BE UPDATED** - This document still describes the v1 product architecture.

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/syspilot-logo-dark.svg">
    <img src="assets/syspilot-logo.svg" alt="syspilot" width="200">
  </picture>
</p>

<p align="center"><strong>Requirements Engineering that scales with AI.</strong></p>

> **⚠️ Early Research Project** — syspilot is under active development. Feel free to use it, fork it, or just study the approach. Updates may introduce breaking changes without migration paths.

> Your project has 5000 requirements. A change affects 5 of them.
> syspilot follows [sphinx-needs](https://sphinx-needs.readthedocs.io/) traceability links to find exactly those 5 — so your AI agent gets focused context, not the entire codebase.

Cover 100% of your specs with 6x less tokens. Links are deterministic — search is probabilistic. syspilot gives your agents the map, not the flashlight. Built on [sphinx-needs](https://sphinx-needs.readthedocs.io/) by [useblocks](https://useblocks.com). Powered by [GitHub Copilot](https://github.com/features/copilot).

## Quick Start

> **V2 bootstrap is being defined.** The v1 setup-agent download has been
> removed. V2 will start from a README prompt pasted into a new Copilot session;
> that prompt creates the Syspilot Setup actor, which performs installation or
> update through a Setup Contract.

## What You Get

Four **managers** that orchestrate the work, and seven **engineers** that execute it:

| Managers | What they do |
|----------|-------------|
| `@syspilot.pm` | Plans features, manages backlog, delegates change requests |
| `@syspilot.cm` | Orchestrates engineers through the change workflow |
| `@syspilot.qm` | Runs independent quality checks |
| `@syspilot.setup` | Installs/updates syspilot in your project |

| Engineers | What they do |
|-----------|-------------|
| `@syspilot.design` | Analyzes a change request, creates a Change Document |
| `@syspilot.implement` | Executes approved changes with traceability |
| `@syspilot.uat` | Generates user acceptance test artifacts |
| `@syspilot.verify` | Validates implementation against the Change Document |
| `@syspilot.docu` | Keeps project documentation current |
| `@syspilot.mece` | Finds gaps and redundancies in your specs |
| `@syspilot.trace` | Traces one item through all levels |
| `@syspilot.release` | Manages versioning and release process |

Agents are stable processes (WHAT to do). **Skills** are exchangeable tool bindings (HOW to do it) — customize syspilot by swapping skills, not agents.

## How It Works

```
User Story (WHY)  ──links──▶  Requirements (WHAT)  ──links──▶  Design Specs (HOW)
```

When you request a change, syspilot follows these links to find only the affected elements. **O(affected), not O(total).**

## Documentation

📖 **Full docs:** [enthali.github.io/syspilot](https://enthali.github.io/syspilot/index.html)

Includes methodology, naming conventions, and traceability matrices.

## Requirements

- **VS Code** + **GitHub Copilot** (license required)
- **Python 3.10+** with `sphinx` and `sphinx-needs` pre-installed (`pip install sphinx sphinx-needs`)
- **[`enthali.jarvis-core`](https://marketplace.visualstudio.com/items?itemName=enthali.jarvis-core)** VS Code extension, installed and enabled on your default agent's tool set — required for multi-agent orchestration (agents hand off work via `SEND`/session messaging). If disabled, agents silently lose this ability instead of erroring.

> If `sphinx-needs` is missing, `@syspilot.setup` prints install instructions and stops — it does not auto-install packages.

