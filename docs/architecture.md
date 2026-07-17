# Architecture: Product & Installation

## Overview

syspilot separates **what it delivers** from **how each project uses it**.
The Product is the distribution package; each project installs a copy and
customizes it via the agent architecture (Soul, Duties, Workflow). Agent
frontmatter no longer prescribes a `tools:` list — the VS Code tool picker
proved unstable across saves and window reloads, silently rewriting or
dropping enumerated lists independent of any syspilot action. Agents instead
inherit whatever tools are enabled on your default VS Code agent, with one
exception: the Setup Bootloader keeps an explicit `tools:` list, since its
bootstrap `agent/runSubagent` call must not depend on picker state.

| Layer | What it is | Where it lives |
|-------|-----------|----------------|
| **Product** | The generic agent toolkit — agents, skills, scripts, templates | `syspilot/` |
| **Installed Copy** | Running agents that VS Code Copilot invokes | `.github/agents/` |

The Setup Agent copies Product files into a project. Project teams then
customize project-owned agents directly. Specifications live in
`docs/syspilot/` and cover all agents at the product level.

**Required: `enthali.jarvis-core`** — Multi-agent orchestration (the `SEND` /
session-messaging mechanism agents use to hand off work to each other) depends
on the `enthali.jarvis-core` tool set being enabled on your default VS Code
agent. If it is disabled, agents do not error — they silently lose the
ability to hand off work, and a multi-agent workflow simply stalls with no
diagnostic. Verify `enthali.jarvis-core` is enabled in the Copilot Chat tool
picker before running any syspilot multi-agent workflow.


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
│   ├── syspilot.orchestration-jarvis/     #   Async variant (mutex pair)
│   └── syspilot.orchestration-subagent/   #   Sync variant (mutex pair)
├── scripts/python/                # Utility scripts
├── sphinx/                        # Build scripts (docs-build.py)
└── templates/
    └── change-document.md         # Change Document template
```

**Key properties:**

- **Language-agnostic** — No project-specific code, build commands, or test runners
- **Self-contained** — Everything needed for installation in one directory
- **Versioned** — The `version:` field in `syspilot/agents/syspilot.setup.agent.md` frontmatter tracks the release; main branch = current release
- **Single source of truth** — The Setup Agent sources all distributable files
  exclusively from `syspilot/`, never from `.github/` or project config
- **Orchestration variant selection** — `syspilot.orchestration-jarvis` (async,
  session-based) and `syspilot.orchestration-subagent` (sync, subagent-based)
  are mutually exclusive. On fresh install, the Setup Agent infers a default
  from `.jarvis/` presence, asks the user to confirm or override, and installs
  exactly one — the same mutex mechanism applies to any future Skill that
  declares a `group:` field. When the async variant is chosen, the Setup Agent
  also creates a `.jarvis/sessions/<name>/session.yaml` scaffold for every
  eligible agent.


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


## Concrete Example: The PM Agent

The Project Manager agent demonstrates the Product/Installation pattern with the
tailoring file mechanism:

**Product** (`syspilot/agents/syspilot.pm.agent.md`):
- Generic workflow skeleton — 17 steps, zero project-specific nouns
- Branch naming, change-doc location, and post-release distribution are
  deliberately absent; they live in the tailoring file
- Preflight block directs the agent to read its tailoring file before executing

**Specifications** (`docs/syspilot/design/spec_project_mgr.rst`):
- `SYSP_SPEC_PM_WORKFLOW` specifies the Preflight pattern and Tailoring Workflow
- `SYSP_SPEC_AGENT_ARCH_WORKFLOW` defines the generic Tailoring File property
  and provides the canonical preflight sentence template

**Tailoring file** (`.github/agents/syspilot.pm.tailoring.md` — created on first PM invocation):
- Instance-only; never shipped by setup, never overwritten on update
- Captures this project's bindings: branch base, change-doc path, backlog
  location, merge target, post-release mechanism
- May be empty (proceed generic), clarify a step, or override it
- Authored by PM via the Tailoring Workflow on first invocation; the file
  does not exist until PM runs for the first time in a new project


## Skill Tailoring

Skills support the same per-project override mechanism as Agents, with one
simplification: every Skill convention ships with a safe default, so there is
no RESPOND-escalation step — a project that never tailors a skill simply gets
the documented default behavior.

**Product** (`syspilot/skills/<name>/SKILL.md`):
- Defines conventions with explicit, safe defaults (e.g. the `syspilot.branching`
  skill's feature-branch retention policy defaults to retain)

**Specification** (`SYSP_SPEC_SKILL_ARCH_TAILORING`):
- Defines the generic tailoring-file contract for Skills: an optional
  `tailoring.md` file colocated with `SKILL.md`, read by any agent invoking
  that skill

**Tailoring file** (`syspilot.<skill-name>.tailoring.md` — instance-only, optional):
- May be absent entirely — the skill's documented default applies
- Never shipped by setup, never overwritten on update
- Example: a project may tailor `syspilot.branching` to delete feature
  branches after merge instead of retaining them


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

**Orphan cleanup** — The Installer removes stale files from previous syspilot versions,
but only files whose name **starts with `syspilot.`** and does **not** end with
`.tailoring.md`. Any file without a `syspilot.` prefix and all `*.tailoring.md` files
are always preserved, regardless of whether they appear in the current release.

**How to customize safely:**

1. **Use tailoring files for project-specific steps** — Each agent reads a sibling
   `syspilot.<name>.tailoring.md` file for project-specific details (paths, branch
   names, distribution targets). Edit this file freely — it is instance-only and
   never removed or overwritten by updates. If it is missing, the agent will walk
   you through creating it.

2. **Don't edit methodology agents directly** — Your changes will be overwritten on
   the next update. Instead, file a change request upstream.

3. **Customize project-owned agents via `@syspilot.design`** — This creates proper
   specs with traceability. The next update won't touch these files.

4. **Transactional rollback** — Before writing any files, the Installer creates a
   pre-install Git commit. On failure, it executes `git reset --hard` to restore the
   exact pre-install state. No partial installs persist.

---

(ontology-architecture)=
## Ontology Architecture *(Phase 0 — spec only, no runtime implementation)*

syspilot separates four concerns cleanly so that the default L0/L1/L2 hierarchy
can be replaced by any project ontology (e.g. ASPICE) without rewriting agents.

| Concern | What it defines |
|---------|----------------|
| **Ontology** | Work-Product types, typed relations, lifecycle states, ownership |
| **Capabilities** | Type-agnostic operations (create, modify, check, validate) |
| **Actors** | Which Capabilities and Work-Product types each Actor owns |
| **Process** | Execution order derived from the ontology graph; gate conditions |

### Key Invariants

- **`syspilot.toml` is the single authority** for ontology selection and tailoring.
  `conf.py` is an adapter/consumer of `syspilot.toml`, never an independent authority.
- Every active Work-Product type has exactly **one Primary-Actor-Owner**
  (1:N ownership is forbidden; read access is unrestricted).
- An Actor processes *all and only* its own affected types in the **dependency order
  of the ontology graph** — not a fixed L0/L1/L2 loop.
- Branching graphs are first-class. "Dependency order" means graph order.

### `.syspilot/` Directory Structure

The per-project `.syspilot/` directory holds all ontology and capability files:

```
.syspilot/
├── syspilot.toml           # Single authority: active ontology + tailoring
├── ontologies/
│   └── <name>/
│       └── ontology.toml  # Ontology definition (types, relations, graph)
└── capabilities/
    └── <name>.toml        # Capability declarations (optional overrides)
```

The **syspilot-default** ontology (`us → req → spec`, L0/L1/L2) ships as a
built-in template. Other ontology templates are first-class; selecting one
does not require agent changes.

*Spec elements:* `SYSP_SPEC_ONTOLOGY_FOUR_CONCERNS`, `SYSP_SPEC_ONTOLOGY_TOML_SCHEMA`,
`SYSP_SPEC_ONTOLOGY_DIRECTORY`, `SYSP_SPEC_ONTOLOGY_GRAPH`, `SYSP_SPEC_ONTOLOGY_CAPABILITIES`.

---

*For file organization details, see [methodology.md](methodology.md).
For the development process, see [workflows.md](workflows.md).*
