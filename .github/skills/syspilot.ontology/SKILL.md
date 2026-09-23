---
name: syspilot.ontology
description: "Technical guidance for reading and editing the current Syspilot v2 ontology. USE FOR: Need types, statuses, options, named links, and strict ontology validation."
requirements: [SYSP_REQ_ONTOLOGY_SCHEMA, SYSP_REQ_ONTOLOGY_EDITING]
---

# Ontology Management

Use this skill when an applicable Contract includes reading or changing `.syspilot/ontology.toml`. The Contract owns the decision, responsibility, affected artifacts, and evidence; this skill provides the technical schema and validation procedure.

## Current V2 Schema

Sphinx-Needs reads `[needs]` directly through `needs_from_toml` in `docs/conf.py`. The sibling `[syspilot]` schema version is a descriptive baseline label, not a required graph input.

### `[needs]`

- Configuration requires explicit IDs, exports combined and per-ID JSON, and uses Graphviz flows.
- `extra_options` contains `priority`, `rationale`, and `realized_by`.
- `[[needs.types]]` defines `root`, `story`, `req`, `ac`, `vc`, and `doc`.
- `[[needs.statuses]]` defines `draft`, `open`, `approved`, `implemented`, `verified`, and `deprecated`.
- `[[needs.extra_links]]` defines `tracked_by`, `implements`, `specializes`, `validates`, `verifies`, and `includes`, including their incoming and outgoing labels.

Each type entry has `directive`, `title`, `prefix`, `color`, and `style`. Each status has `name` and `description`. Each extra link has `option`, `incoming`, and `outgoing`.

### `[syspilot]`

- `schema_version` identifies the ontology schema.

The graph uses the named, directed `[[needs.extra_links]]` definitions and exported Need links and backlinks. No Syspilot type-pair rules or status-transition metadata is required for traversal; the link definitions do not express requiredness or prove semantic correctness. Sphinx-Needs statuses remain configured under `[needs]`.

The ontology has no centralized artifact-owner or actor-name mapping. Applicable Contracts assign artifact ownership and `Current responsibility`.

## Contract-Owned Editing

1. Confirm that the applicable Contract includes the ontology change and records its owner, intended outcome, affected artifacts, and required evidence.
2. Read the complete current `.syspilot/ontology.toml`; preserve unrelated project-specific content.
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

Pristine Setup preserves an existing configured ontology. It copies the release baseline `.syspilot/ontology.toml` only when the target has no ontology. Ontology evaluation or project-specific redesign is separate Contract work; do not overwrite an existing ontology during Setup.
