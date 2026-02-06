Core Requirements
=================

Requirements for the foundational methodology and framework.

**Last Updated**: 2026-02-06


.. req:: Requirements Management with sphinx-needs
   :id: REQ_CORE_SPHINX_NEEDS
   :status: implemented
   :priority: mandatory
   :tags: core, sphinx-needs
   :links: US_CORE_SPEC_AS_CODE

   **Description:**
   syspilot SHALL manage requirements in sphinx-needs RST format.

   **Rationale:**
   sphinx-needs provides structured requirements with automatic traceability,
   validation, and documentation generation.

   **Acceptance Criteria:**

   * AC-1: Requirements stored in ``.rst`` files with sphinx-needs directives
   * AC-2: Each requirement has unique ID, status, priority, and tags
   * AC-3: sphinx-build validates requirement syntax and links
   * AC-4: HTML documentation generated from requirements


.. req:: Design Specification with Traceability
   :id: REQ_CORE_TRACEABILITY
   :status: implemented
   :priority: mandatory
   :tags: core, traceability
   :links: US_CORE_SPEC_AS_CODE, REQ_CORE_SPHINX_NEEDS

   **Description:**
   syspilot SHALL maintain design specifications linked to requirements.

   **Rationale:**
   Traceability from requirements to design ensures all requirements
   are addressed and design decisions are justified.

   **Acceptance Criteria:**

   * AC-1: Design specs use ``:links:`` to reference requirements
   * AC-2: sphinx-needs validates all links exist
   * AC-3: Traceability matrix auto-generated
   * AC-4: Orphan detection (specs without requirements, requirements without specs)


.. req:: A-SPICE Process Alignment
   :id: REQ_CORE_ASPICE
   :status: implemented
   :priority: medium
   :tags: aspice, automotive

   **Description:**
   syspilot SHOULD align with A-SPICE process areas for automotive
   software development.

   **Rationale:**
   A-SPICE alignment enables use in automotive projects with
   certification requirements.

   **Acceptance Criteria:**

   * AC-1: change agent maps to SWE.1 (Requirements Analysis)
   * AC-2: implement agent maps to SWE.2/SWE.3 (Design/Construction)
   * AC-3: verify agent maps to SWE.4 (Unit Verification)
   * AC-4: Documentation structure supports A-SPICE work products


Traceability
------------

.. needtable::
   :columns: id, title, status, tags
   :filter: id.startswith('REQ_CORE')
