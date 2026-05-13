# Architecture: Product & Installation

## Overview

syspilot separates **what it delivers** from **how each project uses it**.
The Product is the distribution package; each project installs a copy and
customizes it via the agent architecture (Soul, Duties, Workflow, Frontmatter).

| Layer | What it is | Where it lives |
|-------|-----------|----------------|
| **Product** | The generic agent toolkit — agents, skills, scripts, templates | `syspilot/` |
| **Installed Copy** | Running agents that VS Code Copilot invokes | `.github/agents/` |

The Setup Agent copies Product files into a project. Project teams then
customize project-owned agents directly. Specifications live in
`docs/syspilot/` and cover all agents at the product level.


## Why the Separation?

Three problems drove this design:

1. **Reusability** — The same agents work across many projects. A change management
   agent doesn't need to know your CI/CD setup. By keeping agents generic in the
   Product, they can be installed in any project without modification.

2. **Update safety** — When syspilot releases a new version, methodology agents
   (design, uat, mece, trace, docu) are replaced automatically. Project-owned
   agents (release, implement) are never overwritten.

3. **Clear ownership** — Every file has an explicit owner (methodology or project).
   This eliminates guesswork about what's safe to edit and what will
   be overwritten on the next update.


## What is Product?

The **Product** is everything in the `syspilot/` directory at the repository root.
It's the distribution package — what gets installed into target projects.

```
syspilot/                          # The Product
├── agents/                        # Generic agent templates
│   ├── syspilot.design.agent.md
│   ├── syspilot.uat.agent.md
│   ├── syspilot.implement.agent.md  # ← Generic skeleton
│   └── ...
├── prompts/                       # Prompt configurations
├── skills/                        # Shared skills (folder-based)
│   ├── syspilot.ask-questions/    #   Each skill has SKILL.md with YAML frontmatter
│   ├── syspilot.branching/
│   ├── syspilot.impact-python/
│   └── syspilot.orchestration/
├── scripts/python/                # Utility scripts
├── sphinx/                        # Build scripts (build.ps1, build.sh)
└── templates/
    └── change-document.md         # Change Document template
```

**Key properties:**

- **Language-agnostic** — No project-specific code, build commands, or test runners
- **Self-contained** — Everything needed for installation in one directory
- **Versioned** — The `version:` field in `syspilot/agents/syspilot.setup.agent.md` frontmatter tracks the release; main branch = current release
- **Single source of truth** — The Setup Agent sources all distributable files
  exclusively from `syspilot/`, never from `.github/` or project config


## How Installation Works

```{mermaid}
flowchart TD
    P["<b>Product</b> (syspilot/)<br/>Generic agents, skills, templates"]
    G["<b>.github/agents/</b> (Installed copy)<br/>Running agents that Copilot invokes"]
    S["<b>docs/syspilot/</b><br/>Product-level specifications<br/>(US → REQ → SPEC)"]

    P -- "Setup Agent installs<br/>Product → .github/" --> G
    S -- "Specifications describe<br/>agent architecture" --> G
```

The flow:

1. **Setup Agent** reads from `syspilot/` (Product) and copies files to `.github/`
2. **Project team** customizes project-owned agents (release, implement) directly
3. **Specifications** in `docs/syspilot/` document the agent architecture
   with full traceability (US → REQ → SPEC)
4. **sphinx-needs** resolves `:links:` across the spec hierarchy, enabling impact analysis


## Concrete Example: The Release Agent

The Release Agent demonstrates the Product/Installation pattern:

**Product** (`syspilot/agents/syspilot.release.agent.md`):
- Generic release workflow: version bump → validate → release notes → tag → publish
- No hardcoded paths, tag formats, or validation commands
- Contains `TODO` placeholders where project configuration is needed

**Specifications** (`docs/syspilot/design/spec_release_engineer.rst`):
- `SYSP_SPEC_RELEASE_FRONTMATTER` documents the exact frontmatter configuration
- `SYSP_SPEC_RELEASE_*` specs define Soul, Duties, and Workflow

**Installed copy** (`.github/agents/syspilot.release.agent.md`):
- The Product template, customized by the project team
- Contains the actual configuration values
- Never overwritten by updates (project-owned)


## Update Safety

syspilot separates **Agents** (stable processes — WHAT to do) from **Skills**
(exchangeable tool bindings — HOW to do it). Agents define workflow steps;
skills encapsulate domain knowledge that agents invoke. Customize syspilot
by swapping skills, not agents.

syspilot defines three ownership categories that determine what happens on update:

| Category | What | On Update |
|----------|------|-----------|
| **Methodology-owned** | design, uat, verify, mece, trace, docu agents; skills; scripts; build files | **Replaced** — always get the latest version |
| **Project-owned** | release, implement agents and prompts | **Never touched** — copied once on install, then yours |
| **User-owned** | Your specs, change docs, copilot-instructions.md | **Never touched** — Setup Agent ignores these entirely |

**How to customize safely:**

1. **Don't edit methodology agents directly** — Your changes will be overwritten on
   the next update. Instead, file a change request upstream.

2. **Customize project-owned agents via `@syspilot.design`** — This creates proper
   specs with traceability. The next update won't touch these files.

3. **Git is your backup** — No special rollback mechanism needed. If an update
   breaks something, `git diff` shows exactly what changed.

---

*For file organization details, see [methodology.md](methodology.md).
For the development process, see [workflows.md](workflows.md).*
