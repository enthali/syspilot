Impact Analysis
===============

.. story:: Discover Ontology-Defined Impact
   :id: SYSP_US_IMPACT_QUERY
   :status: approved
   :priority: mandatory
   :tags: skill, impact, traceability
   :tracked_by: ROOT_SYSPILOT

   **As** a participant determining the scope of a Change,
   **I want** impact analysis to traverse the link types declared by the
   project's active ontology,
   **so that** affected specification candidates are discovered without
   assuming Syspilot-specific link names or overlooking customer-defined
   relationships.

   **Context:**

   Impact output informs the applicable Contract's scope and evidence. It does
   not independently decide scope or replace Contract-owned judgment.

.. ac:: Ontology-defined relationships inform Contract scope
   :id: SYSP_AC_IMPACT_QUERY_1
   :status: approved
   :validates: SYSP_US_IMPACT_QUERY

   Given an active project ontology declares standard, v2, or customer-defined
   Sphinx-Needs link options,
   When a participant queries an existing Need in either direction to a chosen
   depth,
   Then the corresponding outgoing and incoming relationships are returned
   without duplicates, and the participant records their scope disposition in
   the applicable Contract.
