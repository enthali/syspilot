---
name: syspilot.ontology
description: "Ontology management for syspilot. Schema documentation for ontology.toml and governance guardrails. USE FOR: adding or modifying Work-Product types, statuses, link types; classifying ontology changes as additive or breaking."
implements: [SYSP_SPEC_ONTOLOGY_SKILL_CONTENT]
requirements: [SYSP_REQ_ONTOLOGY_SKILL]
---

# Skill: Ontology Management

## USE FOR

- Adding, modifying, or removing Work-Product types, statuses, or link types
- Understanding the ontology.toml schema structure
- Classifying ontology changes (additive vs. breaking)
- Understanding governance rules for ontology changes

## Schema: .syspilot/ontology.toml

The canonical ontology lives at `.syspilot/ontology.toml`. Sphinx-needs reads
it directly via `needs_from_toml` in `docs/conf.py`.

### Section Separator Convention

The file has two kinds of top-level sections:

1. **`[needs]` sections** — understood by sphinx-needs / ubCode.
   Sphinx-needs reads only `[needs]` and ignores sibling keys.
2. **Non-`[needs]` sections** (e.g. `[syspilot]`) — syspilot-specific metadata,
   ignored by sphinx-needs.

### ubCode Sections (under `[needs]`)

```toml
[needs]
id_required = true
build_json = true
build_json_per_id = true
flow_engine = "graphviz"
extra_options = ["priority", "rationale", "acceptance_criteria"]

[[needs.types]]
directive = "story"
title = "User Story"
prefix = "US_"
color = "#E8D5B7"
style = "node"

# ... more types ...

[[needs.statuses]]
name = "draft"
description = "Draft - Work in progress"

# ... more statuses ...

[[needs.extra_links]]
option = "defines"
incoming = "is defined by"
outgoing = "defines"
```

### syspilot Sections

```toml
[syspilot]
schema_version = "1.0"

# Future phases will add:
# [syspilot.actors]
# [syspilot.capabilities]
# [syspilot.process]
```

## How to Edit

### Adding a New Type

1. Add a `[[needs.types]]` entry to `.syspilot/ontology.toml`:
   ```toml
   [[needs.types]]
   directive = "mytype"
   title = "My Type"
   prefix = "MT_"
   color = "#AABBCC"
   style = "node"
   ```
2. Verify with `sphinx-build -W`.

### Adding a New Status

Add a `[[needs.statuses]]` entry:
```toml
[[needs.statuses]]
name = "my_status"
description = "My Status - description"
```

### Adding a New Link Type

Add a `[[needs.extra_links]]` entry:
```toml
[[needs.extra_links]]
option = "mylink"
incoming = "is linked by"
outgoing = "links to"
```

## Governance Guardrails

`ontology.toml` is a **guarded artifact**. Every change must be classified.

### Change Classification

| Change | Classification | Gate |
|--------|---------------|------|
| Add a new type | Additive | Normal CR |
| Add a new status | Additive | Normal CR |
| Add a new link type | Additive | Normal CR |
| Add a new extra_option | Additive | Normal CR |
| Add/modify `[syspilot]` metadata | Additive | Normal CR |
| Remove or rename a type | **Breaking** | Migration CR required |
| Remove or rename a status | **Breaking** | Migration CR required |
| Remove or rename a link type | **Breaking** | Migration CR required |
| Change a type's directive or prefix | **Breaking** | Migration CR required |

### Breaking Change Process

A breaking change triggers a **migration CR** that must:

1. Update all existing specs referencing the affected type/status/link.
2. Verify `sphinx-build -W` passes after migration.
3. Be merged before or atomically with the ontology change.

### Safety Net

1. **`sphinx-build -W`** (every CR) — catches type/link mismatches immediately.
2. **Governance classification** (process) — catches intent before implementation.
