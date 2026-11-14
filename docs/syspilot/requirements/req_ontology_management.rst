Ontology Management
===================

.. req:: Current Ontology Schema Guidance
   :id: SYSP_REQ_ONTOLOGY_SCHEMA
   :status: approved
   :implements: SYSP_US_ONTOLOGY_MANAGEMENT
   :realized_by: .github/skills/syspilot.ontology/SKILL.md

   The Ontology skill shall explain the current project ontology at
   ``.syspilot/ontology.toml``, including:

   - the separation between Sphinx-Needs configuration under ``[needs]`` and
     optional syspilot-specific metadata under ``[syspilot]``;
   - the configured Need types, statuses, extra options, and extra links;
   - the absence of a required Syspilot type-pair or status-transition schema;
     configured link kinds and statuses come from ``[needs]``; and
   - the absence of centralized artifact-owner or actor-name assignments,
     because applicable Contracts declare ownership and responsibility.

   The guidance shall not describe removed Need types, obsolete actors, or
   schema fields that are absent from the active project ontology.

.. vc:: Ontology guidance matches the current schema
   :id: SYSP_VC_ONTOLOGY_SCHEMA_1
   :status: approved
   :verifies: SYSP_REQ_ONTOLOGY_SCHEMA

   Every skill section and example matches ``.syspilot/ontology.toml``;
   removed types, obsolete actors and absent fields are not taught.

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
     installs the baseline ontology only when none exists;
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
   surfaces and preserves unrelated ontology content and Setup baseline behavior.

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
