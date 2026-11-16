Ontology Management
===================

.. req:: Current Ontology Schema Guidance
   :id: SYSP_REQ_ONTOLOGY_SCHEMA
   :status: approved
   :implements: SYSP_US_ONTOLOGY_MANAGEMENT
   :realized_by: .github/skills/syspilot.ontology/SKILL.md

   The Ontology skill shall explain the active project ontology, the one
   bound through ``needs_from_toml``, without naming a fixed path or a fixed
   type list, including:

   - the separation between Sphinx-Needs configuration under ``[needs]`` and
     optional syspilot-specific metadata under ``[syspilot]``;
   - the configured Need types, statuses, extra options, and extra links;
   - the absence of a required Syspilot type-pair or status-transition schema;
     the optional ``[[syspilot.diagram_edges]]`` entries only feed the
     generated link diagram and neither constrain nor validate links;
     configured link kinds and statuses come from ``[needs]``; and
   - the absence of centralized artifact-owner or actor-name assignments,
     because applicable Contracts declare ownership and responsibility.

   The guidance shall not describe removed Need types, obsolete actors, or
   schema fields that are absent from the active project ontology.

.. vc:: Ontology guidance matches the current schema
   :id: SYSP_VC_ONTOLOGY_SCHEMA_1
   :status: approved
   :verifies: SYSP_REQ_ONTOLOGY_SCHEMA

   Every skill section and example holds for both Syspilot's own ontology and
   the Example Ontology, or names the bound ontology as its source; removed
   types, obsolete actors and absent fields are not taught.

.. vc:: Ontology guidance leaves governance with Contracts
   :id: SYSP_VC_ONTOLOGY_SCHEMA_2
   :status: approved
   :verifies: SYSP_REQ_ONTOLOGY_SCHEMA

   Guidance distinguishes ``[needs]`` configuration from optional metadata;
   neither mandatory graph/transition metadata nor centralized actor ownership
   is introduced.

.. req:: Contract-Owned Ontology Editing And Validation
   :id: SYSP_REQ_ONTOLOGY_EDITING
   :status: approved
   :implements: SYSP_US_ONTOLOGY_MANAGEMENT
   :realized_by: .github/skills/syspilot.ontology/SKILL.md

   When an applicable Contract includes an ontology change, the Ontology skill
   shall provide technical instructions to:

   - edit Need types, statuses, extra options, extra links, and other
     project-configured Sphinx-Needs options represented by the current schema,
     without requiring Syspilot graph or transition metadata;
   - preserve unrelated existing project ontology content and Setup's rule that
     installs the Example Ontology only when none exists;
   - record the decision, responsibility, affected artifacts, and evidence in
     the applicable Contract rather than defining separate CR or migration
     governance in the skill; and
   - run the project's strict documentation and schema validation after the
     edit and resolve ontology warnings before completion.

   Establishing a project-specific ontology immediately after Setup is outside
   this capability unless a future Contract explicitly includes that work.

.. vc:: Contract-owned ontology edits preserve unrelated configuration
   :id: SYSP_VC_ONTOLOGY_EDITING_1
   :status: approved
   :verifies: SYSP_REQ_ONTOLOGY_EDITING

   A representative edit changes only Contract-included current-schema
   surfaces and preserves unrelated ontology content and Setup's install-only-when-absent behavior.

.. vc:: Ontology editing records governance in the Contract
   :id: SYSP_VC_ONTOLOGY_EDITING_2
   :status: approved
   :verifies: SYSP_REQ_ONTOLOGY_EDITING

   Skill instructions record decision, responsibility, affected artifacts and
   evidence in the applicable Contract, with no separate CR or migration gate.

.. vc:: Ontology editing requires strict validation
   :id: SYSP_VC_ONTOLOGY_EDITING_3
   :status: approved
   :verifies: SYSP_REQ_ONTOLOGY_EDITING

   The edit's documentation and schema validation report zero warnings before
   completion.

.. vc:: Post-Setup ontology establishment needs explicit scope
   :id: SYSP_VC_ONTOLOGY_EDITING_4
   :status: approved
   :verifies: SYSP_REQ_ONTOLOGY_EDITING

   Establishing a project-specific ontology immediately after Setup is included
   only by explicit Contract scope, not assumed from the editing capability.

.. req:: Ontologies Live With The Specifications
   :id: SYSP_REQ_ONTOLOGY_LOCATION
   :status: approved
   :implements: SYSP_US_ONTOLOGY_MANAGEMENT
   :realized_by: docs/conf.py

   Each ontology shall be a folder ``docs/<Name> Ontology/`` that holds its
   ``ontology.toml`` and a reader-oriented ``ontology.md``:

   - Syspilot's own ontology is ``docs/Syspilot Ontology/``; ``docs/conf.py``
     binds its ``ontology.toml`` through ``needs_from_toml``;
   - the documentation build generates ``docs/Syspilot Ontology/ontology.md``
     from that ``ontology.toml`` on every run, so the page cannot drift from
     the ontology; it carries the type catalogue and a Mermaid link diagram
     whose nodes are the configured types and whose edges are the descriptive
     ``[[syspilot.diagram_edges]]`` entries (``link``, ``from``, ``to``) of
     that file, because ``[[needs.extra_links]]`` does not name endpoint
     types and Syspilot defines no type-pair rule;
   - an installed project's ``ontology.md`` is hand-written prose seeded from
     the Example Ontology; and
   - Syspilot's repository has no ``.syspilot/`` folder, because that folder
     in an installed project holds only the baseline and Setup records.

.. vc:: Syspilot binds its ontology in the specification tree
   :id: SYSP_VC_ONTOLOGY_LOCATION_1
   :status: approved
   :verifies: SYSP_REQ_ONTOLOGY_LOCATION

   The strict documentation build passes with ``needs_from_toml`` naming
   ``docs/Syspilot Ontology/ontology.toml``, and no tracked file remains at
   ``.syspilot/ontology.toml`` or ``docs/ontology-reference.md``.

.. vc:: The generated ontology page follows the ontology
   :id: SYSP_VC_ONTOLOGY_LOCATION_2
   :status: approved
   :verifies: SYSP_REQ_ONTOLOGY_LOCATION

   After a build, ``docs/Syspilot Ontology/ontology.md`` lists every configured
   Need type of ``docs/Syspilot Ontology/ontology.toml`` and is not tracked.

.. vc:: The generated link diagram matches the ontology and the graph
   :id: SYSP_VC_ONTOLOGY_LOCATION_3
   :status: approved
   :verifies: SYSP_REQ_ONTOLOGY_LOCATION

   The generated Mermaid diagram has one node per configured type and one edge
   per ``[[syspilot.diagram_edges]]`` entry; every entry names a configured
   link and configured types, every configured link has an edge, and every
   (type, link, type) triple observed in the built Needs data has an edge.
