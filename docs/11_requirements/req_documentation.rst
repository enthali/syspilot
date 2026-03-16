Documentation Requirements
===========================

Requirements for project documentation maintenance, scope, and per-document content.

**Last Updated**: 2026-03-15


Documentation Scope
-------------------

.. req:: Documentation Scope
   :id: REQ_DOC_SCOPE
   :status: implemented
   :priority: mandatory
   :tags: documentation, scope
   :links: US_DOC_MAINTAIN, REQ_CHG_IMPL_AGENT

   **Description:**
   syspilot SHALL define a documentation scope that identifies user-facing
   project documentation to be maintained as part of implementation artifacts.

   **Rationale:**
   Documentation is an implementation artifact like code. Per-document
   requirements and chapter-structure design specs enable any agent
   (implement, setup) to maintain documentation with full traceability.

   **Acceptance Criteria:**

   * AC-1: Documentation scope covers user-facing documentation (README, guides,
     changelog, release notes)
   * AC-2: Documentation structure and content mapping SHALL be defined
     in design specs with explicit requirement links
   * AC-3: Each project MAY customize which documents are maintained
   * AC-4: Setup agent SHALL configure documentation scope during initial setup


Per-Document Requirements
-------------------------

.. req:: README Documentation
   :id: REQ_DOC_README
   :status: implemented
   :priority: mandatory
   :tags: documentation, readme
   :links: US_DOC_MAINTAIN, REQ_INST_NEW_PROJECT, REQ_INST_ADOPT_EXISTING

   **Description:**
   The project README SHALL describe the project overview, installation
   instructions, and quickstart guide.

   **Rationale:**
   The README is the first document users encounter. It must accurately
   reflect the current state of the project.

   **Acceptance Criteria:**

   * AC-1: README contains project overview
   * AC-2: README contains installation instructions
   * AC-3: README contains quickstart or usage guide
   * AC-4: README is updated when installation process or project scope changes


.. req:: Methodology Documentation
   :id: REQ_DOC_METHODOLOGY
   :status: implemented
   :priority: mandatory
   :tags: documentation, methodology
   :links: US_DOC_MAINTAIN, REQ_CORE_DOMAIN_ORG, REQ_CORE_L1_MIRROR

   **Description:**
   The methodology document SHALL describe the file organization approach
   across specification levels.

   **Rationale:**
   Developers and agents need to understand how files are organized
   to navigate and contribute to the project correctly.

   **Acceptance Criteria:**

   * AC-1: Document describes Level 0/1 organization by problem domain
   * AC-2: Document describes Level 2 organization by solution domain
   * AC-3: Document is updated when file organization conventions change


.. req:: Naming Conventions Documentation
   :id: REQ_DOC_NAMING
   :status: implemented
   :priority: mandatory
   :tags: documentation, naming
   :links: US_DOC_MAINTAIN, REQ_CORE_DOMAIN_ORG

   **Description:**
   The naming conventions document SHALL describe the ID format, theme
   abbreviations, and slug guidelines used across all specification levels.

   **Rationale:**
   Consistent naming is critical for traceability. The document must
   reflect all current themes and naming patterns.

   **Acceptance Criteria:**

   * AC-1: Document describes ID format (<TYPE>_<THEME>_<SLUG>)
   * AC-2: Document lists all theme abbreviations with their levels
   * AC-3: Document is updated when new themes are introduced


.. req:: Release Notes Documentation
   :id: REQ_DOC_RELEASE_NOTES
   :status: implemented
   :priority: mandatory
   :tags: documentation, release
   :links: US_DOC_MAINTAIN, REQ_WF_RELEASE_SEQUENCE, REQ_REL_NOTES

   **Description:**
   The release notes document SHALL define the structure and format
   for recording release history.

   **Rationale:**
   A consistent document structure ensures release information is
   navigable and predictable. Content generation is covered by
   REQ_REL_NOTES.

   **Acceptance Criteria:**

   * AC-1: Release notes list changes per version (newest first)
   * AC-2: Release notes are updated during the release workflow


.. req:: Process Documentation
   :id: REQ_DOC_PROCESS
   :status: implemented
   :priority: high
   :tags: documentation, process
   :links: US_DOC_MAINTAIN

   **Description:**
   The process documentation SHALL describe the development process
   alignment (e.g., A-SPICE) and standards compliance.

   **Rationale:**
   Process documentation demonstrates compliance and helps new
   contributors understand the development approach.

   **Acceptance Criteria:**

   * AC-1: Process alignment is documented with traceability to standards
   * AC-2: Document is updated when workflow or process changes


.. req:: Documentation Index
   :id: REQ_DOC_INDEX
   :status: implemented
   :priority: mandatory
   :tags: documentation, index
   :links: US_DOC_MAINTAIN, REQ_DOC_SCOPE

   **Description:**
   The documentation index (docs/index.rst) SHALL serve as the entry
   point to all project documentation with working navigation.

   **Rationale:**
   The index is the root of the Sphinx documentation tree. It must
   include all sections and stay current as documentation structure evolves.

   **Acceptance Criteria:**

   * AC-1: Index includes toctree entries for all documentation sections
   * AC-2: Index is updated when documentation structure changes


Traceability
------------

.. needtable::
   :columns: id, title, status, tags
   :filter: id.startswith('REQ_DOC')
