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


File Organization
-----------------

.. req:: File Organization by Domain Type
   :id: REQ_CORE_DOMAIN_ORG
   :status: implemented
   :priority: mandatory
   :tags: core, methodology, organization
   :links: US_CORE_FILE_ORG

   **Description:**
   syspilot SHALL organize specification files by domain type:

   * Level 0 (User Stories) and Level 1 (Requirements): by **problem domain**
     — one file per stakeholder theme or value stream
   * Level 2 (Design Specs): by **solution domain**
     — one file per technical component or module

   **Rationale:**
   User Stories and Requirements answer "why" and "what" from the stakeholder
   perspective, so they group naturally by user goals. Design Specs answer "how"
   from the technical perspective, so they group by architectural component.
   A single design component may address requirements from multiple themes.

   **Acceptance Criteria:**

   * AC-1: US files named ``us_<theme>.rst`` grouping by stakeholder theme
   * AC-2: REQ files named ``req_<theme>.rst`` grouping by the same themes
   * AC-3: SPEC files named ``spec_<component>.rst`` grouping by technical component
   * AC-4: A SPEC file MAY link to REQs from multiple themes


.. req:: Level 1 Mirrors Level 0 File Structure
   :id: REQ_CORE_L1_MIRROR
   :status: implemented
   :priority: mandatory
   :tags: core, methodology, organization
   :links: US_CORE_FILE_ORG, REQ_CORE_DOMAIN_ORG

   **Description:**
   syspilot SHALL maintain a 1:1 correspondence between Level 0 (User Story)
   and Level 1 (Requirement) files.

   **Rationale:**
   A User Story file defines a bounded context. Its requirements are cohesive
   and belong together. The 1:1 mapping provides a simple mental model:
   "Where are the REQs for this US file? In the matching ``req_`` file."

   **Acceptance Criteria:**

   * AC-1: For each ``us_<theme>.rst`` there SHALL be a ``req_<theme>.rst``
   * AC-2: Requirements in ``req_<theme>.rst`` SHALL link to User Stories in
     the corresponding ``us_<theme>.rst``
   * AC-3: Merging related requirement files is acceptable when a US file
     produces fewer than 3 requirements


Traceability
------------

.. needtable::
   :columns: id, title, status, tags
   :filter: id.startswith('REQ_CORE')
