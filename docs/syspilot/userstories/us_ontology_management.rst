Ontology Management
===================

.. story:: Safe Project Ontology Maintenance
   :id: SYSP_US_ONTOLOGY_MANAGEMENT
   :status: approved
   :priority: mandatory
   :tags: skill, ontology, schema
   :tracked_by: ROOT_SYSPILOT

   **As** a participant maintaining a syspilot project ontology,
   **I want** current technical guidance for understanding, editing, and
   validating the ontology schema,
   **so that** an ontology decision recorded in the applicable Contract can be
   realized without introducing invalid Needs configuration or stale process
   governance.

   **Context:**

   The Ontology skill explains and applies the technical schema. The applicable
   Contract owns the decision, responsibility, scope, and evidence for each
   ontology change.

.. ac:: A Contract-owned ontology decision is safely realized
   :id: SYSP_AC_ONTOLOGY_MANAGEMENT_1
   :status: approved
   :validates: SYSP_US_ONTOLOGY_MANAGEMENT

   Given an applicable Contract records an ontology decision and responsibility,
   When the responsible participant uses the Ontology skill to inspect or edit
   the project ontology,
   Then the guidance matches the current v2 schema, the resulting documentation
   build validates the configuration strictly, and the skill does not introduce
   a separate governance authority.
