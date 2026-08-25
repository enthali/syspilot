---
name: syspilot.ontology
description: "Technical guidance for reading and editing the current Syspilot v2 ontology. USE FOR: Need types, statuses, options, links, type relationships, transitions, and strict ontology validation."
requirements: [SYSP_REQ_ONTOLOGY_SCHEMA, SYSP_REQ_ONTOLOGY_EDITING]
---

# Ontology Management

Use this skill when an applicable Contract includes reading or changing `.syspilot/ontology.toml`. The Contract owns the decision, responsibility, affected artifacts, and evidence; this skill provides the technical schema and validation procedure.

## Current V2 Schema

Sphinx-Needs reads `[needs]` directly through `needs_from_toml` in `docs/conf.py`. Syspilot tooling reads the sibling `[syspilot]` metadata. Preserve this separation.

### `[needs]`

- Configuration requires explicit IDs, exports combined and per-ID JSON, and uses Graphviz flows.
- `extra_options` contains `priority`, `rationale`, and `realized_by`.
- `[[needs.types]]` defines `root`, `story`, `req`, `ac`, `vc`, and `doc`.
- `[[needs.statuses]]` defines `draft`, `open`, `approved`, `implemented`, `verified`, and `deprecated`.
- `[[needs.extra_links]]` defines `tracked_by`, `implements`, `specializes`, `validates`, `verifies`, and `includes`, including their incoming and outgoing labels.

Each type entry has `directive`, `title`, `prefix`, `color`, and `style`. Each status has `name` and `description`. Each extra link has `option`, `incoming`, and `outgoing`.

### `[syspilot]`

- `schema_version` identifies the ontology schema.
- `[[syspilot.type_links]]` declares valid directed relationships with `from`, `to`, and `rel`.
- `[syspilot.status_transitions]` declares universal transitions and `universal_exit` statuses.
- `[syspilot.status_transitions.overrides.<type>]` replaces universal transitions for a specific type.

The ontology has no centralized artifact-owner or actor-name mapping. Applicable Contracts assign artifact ownership and `Current responsibility`.

## Contract-Owned Editing

1. Confirm that the applicable Contract includes the ontology change and records its owner, intended outcome, affected artifacts, and required evidence.
2. Read the complete current `.syspilot/ontology.toml`; preserve unrelated project-specific content.
3. Edit only the included current-schema surfaces:
   - Need types, statuses, or extra options under `[needs]`;
   - extra links under `[[needs.extra_links]]`;
   - relationship metadata under `[[syspilot.type_links]]`; or
   - universal, exit, or per-type transition metadata under `[syspilot.status_transitions]`.
4. Keep linked definitions coherent. For example, a `type_links.rel` value must name an existing extra link, and transition statuses must exist under `needs.statuses`.
5. Run the project's strict documentation and schema validation. For Syspilot itself:

   ```powershell
   python docs/docs-build.py clean
   python docs/test_docs_build.py -v
   git diff --check
   ```

6. Resolve every ontology or Sphinx warning before completion, then record the changed surfaces and verification evidence in the Contract.

## Setup Boundary

Pristine Setup preserves an existing configured ontology. It copies the release baseline `.syspilot/ontology.toml` only when the target has no ontology. Ontology evaluation or project-specific redesign is separate Contract work; do not overwrite an existing ontology during Setup.
