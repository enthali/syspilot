# Architecture: Product & Instance

## Overview

syspilot separates **what it delivers** from **how each project uses it**.
This two-layer model keeps the toolkit reusable and updatable while giving
every project full control over its own configuration.

| Layer | What it is | Where it lives |
|-------|-----------|----------------|
| **Product** | The generic agent toolkit — agents, skills, scripts, templates | `syspilot/` |
| **Instance** | Project-specific configuration — customized agents, specs, decisions | `docs/inst/syspilot/` |

Think of it like an operating system: the Product is the OS distribution,
the Instance is your personal configuration. Updates replace the OS,
your configuration stays untouched.


## Why the Separation?

Three problems drove this design:

1. **Reusability** — The same agents work across many projects. A change management
   agent doesn't need to know your CI/CD setup. By keeping agents generic in the
   Product, they can be installed in any project without modification.

2. **Update safety** — When syspilot releases a new version, methodology agents
   (change, verify, mece, trace, memory) are replaced automatically. If your
   project-specific configuration lived in those files, it would be overwritten.
   The separation ensures updates never touch your customizations.

3. **Clear ownership** — Every file has an explicit owner (methodology, project,
   or user). This eliminates guesswork about what's safe to edit and what will
   be overwritten on the next update.


## What is Product?

The **Product** is everything in the `syspilot/` directory at the repository root.
It's the distribution package — what gets installed into target projects.

```
syspilot/                          # The Product
├── version.json                   # Release version (e.g., "0.2.3")
├── agents/                        # Generic agent templates
│   ├── syspilot.change.agent.md
│   ├── syspilot.verify.agent.md
│   ├── syspilot.implement.agent.md  # ← Generic skeleton
│   └── ...
├── prompts/                       # Prompt configurations
├── skills/                        # Shared skills
├── scripts/python/                # Utility scripts
├── sphinx/                        # Build scripts (build.ps1, build.sh)
└── templates/
    └── change-document.md         # Change Document template
```

**Key properties:**

- **Language-agnostic** — No project-specific code, build commands, or test runners
- **Self-contained** — Everything needed for installation in one directory
- **Versioned** — `version.json` tracks the release; main branch = current release
- **Single source of truth** — The Setup Agent sources all distributable files
  exclusively from `syspilot/`, never from `.github/` or project config


## What is Instance?

The **Instance** is the project-specific layer that customizes the Product
for a particular project. It lives in `docs/inst/syspilot/`.

```
docs/inst/syspilot/                # The Instance
├── userstories/
│   ├── us_release.rst             # Project-specific release stories
│   └── us_implement.rst           # Project-specific implement stories
├── requirements/
│   ├── req_release.rst            # Project-specific release requirements
│   └── req_implement.rst          # Project-specific implement requirements
└── design/
    ├── spec_release.rst           # Release Agent configuration
    └── spec_implement.rst         # Implement Agent configuration
```

**Key properties:**

- **Project-specific** — Contains decisions, configurations, and customizations
  that are unique to this project
- **Links to Product** — Instance specs reference Product specs via sphinx-needs
  `:links:` directives, creating traceable connections
- **Survives updates** — The Setup Agent never touches `docs/inst/`
- **Follows the same hierarchy** — User Stories → Requirements → Design,
  just scoped to this project

The Instance is where you answer questions like:
- *Where is our version file?* → `syspilot/version.json`
- *What tag format do we use?* → `v{version}`
- *What pre-release checks do we run?* → Sphinx build + link check


## How They Relate

```{mermaid}
flowchart TD
    P["<b>Product</b> (syspilot/)<br/>Generic agents, skills, templates<br/>syspilot.release.agent.md — generic skeleton<br/>syspilot.implement.agent.md — generic skeleton"]
    G["<b>.github/agents/</b> (Installed copy)<br/>Running agents that Copilot invokes"]
    I["<b>Instance</b> (docs/inst/syspilot/)<br/>Project-specific specs with :links: to Product specs<br/>INST_SYSPILOT_SPEC_REL_AGENT_CONFIG<br/>→ links to SYSPILOT_REQ_REL_*, SYSPILOT_SPEC_REL_*"]

    P -- "Setup Agent installs<br/>Product → .github/" --> G
    G -- "Instance specs configure<br/>how installed agents behave" --> I
```

The flow:

1. **Setup Agent** reads from `syspilot/` (Product) and copies files to `.github/`
2. **Project team** customizes project-owned agents (release, implement) via
   `@syspilot.change`
3. **Instance specs** in `docs/inst/syspilot/` document those customizations
   with full traceability back to Product specs
4. **sphinx-needs** resolves `:links:` across both trees, enabling impact analysis


## Concrete Example: The Release Agent

The Release Agent demonstrates the Product/Instance pattern clearly:

**Product** (`syspilot/agents/syspilot.release.agent.md`):
- Generic release workflow: version bump → validate → release notes → tag → publish
- No hardcoded paths, tag formats, or validation commands
- Contains `TODO` placeholders where project configuration is needed

**Instance** (`docs/inst/syspilot/design/spec_release.rst`):
- Defines `INST_SYSPILOT_SPEC_REL_AGENT_CONFIG` with a configuration table:

| Decision | Value |
|----------|-------|
| Version file | `syspilot/version.json` |
| Tag format | `v{version}` |
| Release notes | `docs/releasenotes.md` |
| Pre-release validation | Sphinx build, link check |

**Installed copy** (`.github/agents/syspilot.release.agent.md`):
- The Product template, customized by the project team
- Contains the actual configuration values from the Instance spec
- Never overwritten by updates (project-owned)

When `@syspilot.change` analyzes a change that affects the release process, it
follows the links from `INST_SYSPILOT_SPEC_REL_AGENT_CONFIG` back to the Product
specs to understand the full impact.


## Update Safety

syspilot defines three ownership categories that determine what happens on update:

| Category | What | On Update |
|----------|------|-----------|
| **Methodology-owned** | change, verify, mece, trace, memory agents; skills; scripts; build files | **Replaced** — always get the latest version |
| **Project-owned** | release, implement agents and prompts | **Never touched** — copied once on install, then yours |
| **User-owned** | Your specs, change docs, copilot-instructions.md | **Never touched** — Setup Agent ignores these entirely |

**How to customize safely:**

1. **Don't edit methodology agents directly** — Your changes will be overwritten on
   the next update. Instead, file a change request upstream or use Instance specs.

2. **Customize project-owned agents via `@syspilot.change`** — This creates proper
   Instance specs with traceability. The next update won't touch these files.

3. **Use Instance specs for project decisions** — Put your configuration in
   `docs/inst/syspilot/` with `:links:` to the Product specs. When the Product
   changes, impact analysis will flag your Instance specs for review.

4. **Git is your backup** — No special rollback mechanism needed. If an update
   breaks something, `git diff` shows exactly what changed.

---

*For file organization details, see [methodology.md](methodology.md).
For the development process, see [workflows.md](workflows.md).*
