---
name: syspilot.ontology
description: "Ontology management for syspilot. Schema documentation for ontology.toml, generator invocation, and governance guardrails. USE FOR: adding or modifying Work-Product types, statuses, link types; running the ubproject.toml generator; classifying ontology changes as additive or breaking."
---

# Skill: Ontology Management

## USE FOR

- Adding, modifying, or removing Work-Product types, statuses, or link types
- Understanding the ontology.toml schema structure
- Running the generator to produce docs/ubproject.toml
- Classifying ontology changes (additive vs. breaking)
- Understanding governance rules for ontology changes

## Schema: .syspilot/ontology.toml

The canonical ontology master lives at `.syspilot/ontology.toml`. It is a
superset of `docs/ubproject.toml` — containing both ubCode-understood sections
and syspilot-specific metadata.

### Section Separator Convention

The file has two kinds of top-level sections:

1. **`[needs]` sections** — passed through to `docs/ubproject.toml` verbatim.
   These are understood by sphinx-needs / ubCode.
2. **Non-`[needs]` sections** (e.g. `[syspilot]`) — stripped by the generator.
   These contain syspilot-specific metadata.

The generator strips everything whose top-level key is NOT `needs`.

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
2. Run the generator (see below).
3. Verify with `sphinx-build -W`.

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

## Generator

**Location:** `syspilot/sphinx/generate_ubproject.py`

### Normal Mode

```shell
python syspilot/sphinx/generate_ubproject.py
```

Reads `.syspilot/ontology.toml`, strips non-`[needs]` sections, writes
`docs/ubproject.toml`.

### Compare Mode

```shell
python syspilot/sphinx/generate_ubproject.py --compare
```

Compares a fresh generation against the committed `docs/ubproject.toml`.

- **Exit 0:** up-to-date (no changes needed)
- **Exit 1:** stale (diff printed to stderr)
- **Exit 2:** input file missing or invalid

The Release Engineer runs `--compare` before squash-merge. A non-zero exit
blocks the release.

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

### Safety Nets

1. **`sphinx-build -W`** (every CR) — catches type/link mismatches immediately.
2. **Generator `--compare`** (release gate) — catches stale projections.
3. **Governance classification** (process) — catches intent before implementation.
