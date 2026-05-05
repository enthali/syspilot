# syspilot Conventions

Reference for implementers creating or customizing Agents and Skills.

---

## Agent Conventions

### Roles

Every syspilot agent belongs to one of two tiers:

| Tier | Examples | Characteristics |
|------|----------|-----------------|
| **Manager** | CM, QM, PM | User-invocable; orchestrates Engineers; knows the full workflow |
| **Engineer** | design, implement, verify, release, … | Subagent-only; executes one specialized task; decoupled from sibling Engineers |

### Frontmatter Fields

Every agent `.agent.md` file begins with a YAML frontmatter block:

```yaml
---
description: "One-sentence description shown in the agent picker"
tools: [read, edit, search, execute, ...]
model: Claude Opus 4.6 (copilot)
user-invocable: true          # true for Managers, false for Engineers
agents: ["syspilot.name"]     # Engineers this agent may invoke (empty if none)
---
```

| Field | Required | Notes |
|-------|----------|-------|
| `description` | mandatory | Shown in VS Code agent picker |
| `tools` | mandatory | Declare only tools the agent actually uses |
| `model` | recommended | Pin the model for reproducible behavior |
| `user-invocable` | mandatory | `true` = Manager, `false` = Engineer |
| `agents` | mandatory | List of subagents this agent may call; `[]` if none |

### Three-Section Structure

Every agent definition — Manager or Engineer — has exactly three sections:

| Section | Customizable? | Purpose |
|---------|---------------|---------|
| **Soul** | No | Immutable identity, character, perspective |
| **Duties** | Yes | List of discrete tasks the agent performs |
| **Workflow** | Yes | Step-by-step process the agent follows |

Customers may modify Duties and Workflow to adapt agents to their project.
The Soul must not be modified — it is the stable behavioral anchor.

### Generic Verbs

Agent documents use generic verbs. Do **not** write tool names in agent docs.

| Verb | Meaning | Blocking |
|------|---------|---------|
| `invoke <agent>` | Call agent as subagent; need the result before continuing | Yes |
| `delegate to <agent>` | Hand off to agent; continue without waiting | No (with Jarvis) |

The concrete implementation of these verbs is provided by the installed
**Orchestration Skill** (see Skill Conventions below).

---

## Skill Conventions

### What Is a Skill?

A Skill is an exchangeable specialization of an Agent. It provides concrete
tool bindings for the generic verbs an Agent uses, or project-specific
configuration values the Agent needs.

Principle: **Agents = stable processes. Skills = exchangeable tool bindings.**

### Skill File Structure

Each Skill is a self-contained folder:

```
syspilot/skills/syspilot.<name>/    ← product source (versioned, shipped)
├── SKILL.md                         # Frontmatter + instructions
└── scripts/                         # Implementation scripts (if any)
```

After setup, the Skill is installed to:

```
.github/skills/syspilot.<name>/     ← installed runtime (managed by Setup Agent)
```

### Skill Frontmatter Fields

```yaml
---
name: syspilot.<name>
description: "One-sentence description"
group: <group-name>                  # e.g. orchestration, impact, release
---
```

| Field | Required | Notes |
|-------|----------|-------|
| `name` | mandatory | Must match the folder name |
| `description` | mandatory | Shown in skill picker and documentation |
| `group` | **optional** | Required only when the Skill is part of an exchangeable family; absent for standalone Skills. Enforces Mutual Exclusion within the group. |

### Mutual Exclusion

Only **one Skill per group** may be installed at a time. Installing a second
Skill with the same `group:` value is a configuration error. The Setup Agent
checks for and rejects duplicate group installations.

### Skill Variants

Multiple variants can exist for the same group. Examples:

| Group | Variant | Description |
|-------|---------|-------------|
| `orchestration` | `syspilot.orchestration-subagent` | `invoke`/`delegate` both map to `runSubagent()` |
| `orchestration` | `syspilot.orchestration-jarvis` | `invoke` → `runSubagent()`, `delegate` → `jarvis_sendToSession()` |
| `impact` | `syspilot.impact-python` | Impact analysis via Python script |
| `impact` | `syspilot.impact-ubcode` | Impact analysis via ubCode MCP *(planned)* |
| `release` | `syspilot.release-syspilot` | Release skill for this syspilot repository |
| `release` | `syspilot.release-generic` | Generic release skill; customer fills in DEFINITIONS |

Install exactly one variant per group you need.

---

## DEFINITIONS Dictionary

### Purpose

The DEFINITIONS Dictionary is the static contract between an Agent and its
installed Skill. Agents reference configuration values by their uppercase
DEFINITION name. Skills supply the concrete values.

Uppercase signals: *"Do not guess. Use what the installed Skill says."*

### One Global Registry

There is **exactly one** DEFINITIONS Registry in syspilot —
`SYSP_SPEC_SKILL_DEFINITIONS`. Every DEFINITION is published there
exactly once as a sphinx-needs `def` need with ID `SYSP_DEF_<NAME>`.

Why global rather than per-group? Skills are loaded based on the
DEFINITIONS they declare. If two groups could declare the same DEFINITION
name, Skill resolution would be ambiguous and the wrong Skill could be
loaded. Publishing each DEFINITION as a `def` need with a unique ID makes
collisions structurally impossible — sphinx-needs rejects duplicate IDs
at build time. No manual cross-checking, no risk of registry drift.

### How a DEFINITION is published

A DEFINITION is a sphinx-needs `def` need on the Registry page:

```rst
.. def:: How the agent merges a feature branch into the development branch
   :id: SYSP_DEF_MERGE
   :status: draft
   :tags: skill-definition

   The verb the agent uses to integrate a completed feature branch.
   One Skill may resolve this to a squash-merge, another to a regular
   merge — the operational detail lives in the Skill that implements
   the group.
```

The `def` need carries only the *meaning* — one paragraph that lets a
human or LLM understand what the DEFINITION is about. The *operational*
detail (exact commands, edge cases, examples) lives in the **Skill** that
implements the group.

### Traceability Pattern (1 degree of separation)

Skills and Agents do **not** link directly to `def` needs. They link to
the **Group Contract Spec**, which in turn names its DEFINITIONS via the
`:defines:` link type:

```
SYSP_SPEC_SKILL_DEFINITIONS   ← Group Contract Spec   ← Concrete Skill Spec
   (registry of def needs)         (per group)              (per variant)
                                        ↑
                                   Agent Specs
                              (that use this group)
```

- **`def` need** — single source of truth for the DEFINITION's identity
  and meaning. Lives only on the Registry page. ID: `SYSP_DEF_<NAME>`.
- **Group Contract Spec** (`SYSP_SPEC_SKILL_<GROUP>_CONTRACT`) — declares
  which DEFINITIONS belong to this group via `:defines: SYSP_DEF_X, SYSP_DEF_Y, ...`.
  No content duplication — the contract just lists references.
- **Concrete Skill Spec** — links to its Group Contract Spec via standard
  `:links:`. Does not reference `def` needs directly.
- **Agent Spec** — links to every Group Contract Spec whose DEFINITIONS
  the Agent uses.

This keeps the Registry a 1-degree hub: following one link from a `def`
reaches all Group Contracts that define it (typically one); following one
more link reaches all Skills and Agents.

### Rules for Agent Authors

1. Use only DEFINITIONS that exist in the global Registry.
2. Write DEFINITION names in UPPERCASE wherever they appear.
3. Do not encode operational detail in the Agent — let the Skill resolve
   the DEFINITION at runtime.
4. Link your Agent Spec to the Group Contract Spec of every group whose
   DEFINITIONS you use.

### Rules for Skill Authors

1. Declare your `group:` in the Skill frontmatter.
2. Implement every DEFINITION listed in your Group Contract Spec.
3. Provide the full operational instruction in the Skill: exact commands,
   LLM-facing description of meaning, edge cases, examples.
4. Link your Skill Spec to the Group Contract Spec — not directly to a
   `def` need.
5. To introduce a new DEFINITION: add a `.. def::` need to
   `SYSP_SPEC_SKILL_DEFINITIONS` and reference it from the Group Contract
   Spec via `:defines:` — both in the same Change Request as the Skill.
6. If your proposed `SYSP_DEF_<NAME>` ID is already taken, rename it
   before merging — sphinx-needs will fail the build on a duplicate ID.

### Where to look

| Looking for… | Go to |
|--------------|-------|
| All registered DEFINITIONS (auto-generated) | `SYSP_SPEC_SKILL_DEFINITIONS` (needtable) |
| DEFINITIONS of a specific group | `SYSP_SPEC_SKILL_<GROUP>_CONTRACT` (`:defines:` field) |
| Which groups currently use DEFINITIONS | `SYSP_SPEC_SKILL_DEFINITIONS` (Group Status table) |
| The architectural rules for Skills | `SYSP_REQ_SKILL_DEFINITIONS`, `SYSP_US_SKILL_ARCH` |

---

*This document is maintained by the syspilot System Designer.
Spec anchors: `SYSP_US_SKILL_ARCH`, `SYSP_REQ_SKILL_DEFINITIONS`,
`SYSP_SPEC_SKILL_DEFINITIONS`.*

