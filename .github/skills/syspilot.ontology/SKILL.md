---
name: syspilot.ontology
description: "Technical guidance for reading and editing the active project ontology. USE FOR: Need types, statuses, options, named links, and strict ontology validation."
requirements: [SYSP_REQ_ONTOLOGY_SCHEMA, SYSP_REQ_ONTOLOGY_EDITING]
---

# Ontology Management

Use this skill when an applicable Contract includes reading or changing the active ontology, the TOML file that `needs_from_toml` in the project's `docs/conf.py` binds. Syspilot's own is `docs/Syspilot Ontology/ontology.toml`; a project that adopted the Example Ontology has `docs/<Project name> Ontology/ontology.toml`. The Contract owns the decision, responsibility, affected artifacts, and evidence; this skill provides the technical schema and validation procedure.

## Current Schema

Sphinx-Needs reads `[needs]` directly through `needs_from_toml` in `docs/conf.py`. The sibling `[syspilot]` schema version is a descriptive baseline label, not a required graph input.

### `[needs]`

- Configuration requires explicit IDs, exports combined and per-ID JSON, and uses Graphviz flows.
- `extra_options` lists the project's additional Need options.
- `[[needs.types]]` defines the Need types.
- `[[needs.statuses]]` defines the allowed statuses.
- `[[needs.extra_links]]` defines the named links, including their incoming and outgoing labels.

Read the type, status, option, and link names from the active file; they differ between ontologies. Syspilot's own has `root`, `story`, `req`, `ac`, `vc`, and `doc`; the Example Ontology adds `design`, which links to a `req` through `details`.

Each type entry has `directive`, `title`, `prefix`, `color`, and `style`. Each status has `name` and `description`. Each extra link has `option`, `incoming`, and `outgoing`.

### `[syspilot]`

- `schema_version` identifies the ontology schema.

The graph uses the named, directed `[[needs.extra_links]]` definitions and exported Need links and backlinks. No Syspilot type-pair rules or status-transition metadata is required for traversal; the link definitions do not express requiredness or prove semantic correctness. Sphinx-Needs statuses remain configured under `[needs]`.

The ontology has no centralized artifact-owner or actor-name mapping. Applicable Contracts assign artifact ownership and `Current responsibility`.

## Contract-Owned Editing

1. Confirm that the applicable Contract includes the ontology change and records its owner, intended outcome, affected artifacts, and required evidence.
2. Locate the active ontology through `needs_from_toml` and read the complete file; preserve unrelated project-specific content.
3. Edit only the included current-schema surfaces: Need types, statuses, and extra options under `[needs]`, or named directed links under `[[needs.extra_links]]`. Preserve the descriptive `[syspilot]` schema version unless the Contract includes changing it.
4. Keep link option names and incoming/outgoing labels coherent with the Needs that use them. Changing a link kind can affect existing Needs and their backlinks.
5. Run the project's strict documentation and schema validation. For Syspilot itself:

   ```powershell
   python docs/docs-build.py clean
   python docs/test_docs_build.py -v
   git diff --check
   ```

6. Resolve every ontology or Sphinx warning before completion, then record the changed surfaces and verification evidence in the Contract.

## Setup Boundary

Pristine Setup preserves an existing configured ontology. It copies the Example Ontology folder to `docs/<Project name> Ontology/` only when the target has no ontology. Ontology evaluation or project-specific redesign is separate Contract work; do not overwrite an existing ontology during Setup.
