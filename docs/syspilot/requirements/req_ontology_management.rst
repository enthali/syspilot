Ontology Management
===================

.. req:: Current V2 Ontology Schema Guidance
   :id: SYSP_REQ_ONTOLOGY_SCHEMA
   :status: approved
   :implements: SYSP_US_ONTOLOGY_MANAGEMENT
   :realized_by: .github/skills/syspilot.ontology/SKILL.md

   The Ontology skill shall explain the current project ontology at
   ``.syspilot/ontology.toml``, including:

   - the separation between Sphinx-Needs configuration under ``[needs]`` and
     syspilot-specific metadata under ``[syspilot]``;
   - the v2 Need types, statuses, extra options, and extra links;
   - the v2 ``type_links`` relationships and status-transition metadata; and
   - the absence of centralized artifact-owner or actor-name assignments,
     because applicable Contracts declare ownership and responsibility.

   The guidance shall not describe removed Need types, obsolete actors, or
   schema fields that are absent from the current v2 ontology.

.. vc:: Ontology guidance matches the current schema
   :id: SYSP_VC_ONTOLOGY_SCHEMA_1
   :status: approved
   :verifies: SYSP_REQ_ONTOLOGY_SCHEMA

   Compare the realized Ontology skill with ``.syspilot/ontology.toml`` and
   confirm that every described section and example exists in the v2 schema,
   removed v1 types and actor ownership are absent, and ownership is assigned to
   applicable Contracts rather than the ontology.

.. req:: Contract-Owned Ontology Editing And Validation
   :id: SYSP_REQ_ONTOLOGY_EDITING
   :status: approved
   :implements: SYSP_US_ONTOLOGY_MANAGEMENT
   :realized_by: .github/skills/syspilot.ontology/SKILL.md

   When an applicable Contract includes an ontology change, the Ontology skill
   shall provide technical instructions to:

   - edit Need types, statuses, extra options, extra links, type relationships,
     or status transitions represented by the current schema;
   - preserve unrelated existing project ontology content and Setup's rule that
     installs the baseline ontology only when none exists;
   - record the decision, responsibility, affected artifacts, and evidence in
     the applicable Contract rather than defining separate CR or migration
     governance in the skill; and
   - run the project's strict documentation and schema validation after the
     edit and resolve ontology warnings before completion.

   Establishing a project-specific ontology immediately after Setup is outside
   this capability unless a future Contract explicitly includes that work.

.. vc:: Contract-owned ontology edits validate strictly
   :id: SYSP_VC_ONTOLOGY_EDITING_1
   :status: approved
   :verifies: SYSP_REQ_ONTOLOGY_EDITING

   Inspect the realized skill and exercise a representative Contract-owned
   ontology edit. Confirm that the instructions cover only current schema
   surfaces, preserve unrelated content and Setup baseline behavior, place
   governance and evidence in the Contract, contain no separate CR or migration
   gate, and require a strict documentation build with zero schema warnings.
