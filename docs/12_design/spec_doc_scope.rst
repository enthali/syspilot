syspilot Documentation Scope
==============================

Project-specific documentation scope and per-document chapter structures for syspilot.

**Document Version**: 0.1
**Last Updated**: 2026-03-15


Document Registry
-----------------

.. spec:: syspilot Documentation Scope
   :id: SPEC_DOC_SCOPE_SYSPILOT
   :status: implemented
   :links: REQ_DOC_SCOPE, REQ_DOC_README, REQ_DOC_METHODOLOGY, REQ_DOC_NAMING, REQ_DOC_RELEASE_NOTES, REQ_DOC_PROCESS, REQ_DOC_INDEX
   :tags: documentation, scope, syspilot

   **Design:**
   Project-specific documentation scope for the syspilot project itself.
   Extends the template scope with syspilot-specific documents.

   Each document has a corresponding structure SPEC that defines its
   chapters and maps each chapter to the source specifications that
   provide the content.

   **Document Registry:**

   .. list-table::
      :header-rows: 1
      :widths: 30 35 25

      * - Document
        - Structure SPEC
        - Requirement
      * - ``README.md``
        - SPEC_DOC_README_STRUCTURE
        - REQ_DOC_README
      * - ``docs/index.rst``
        - SPEC_DOC_INDEX_STRUCTURE
        - REQ_DOC_INDEX
      * - ``docs/methodology.md``
        - SPEC_DOC_METHODOLOGY_STRUCTURE
        - REQ_DOC_METHODOLOGY
      * - ``docs/namingconventions.md``
        - SPEC_DOC_NAMING_STRUCTURE
        - REQ_DOC_NAMING
      * - ``docs/releasenotes.md``
        - SPEC_DOC_RELEASE_NOTES_STRUCTURE
        - REQ_DOC_RELEASE_NOTES
      * - ``docs/40_process/``
        - SPEC_DOC_PROCESS_STRUCTURE
        - REQ_DOC_PROCESS


Chapter Structures
------------------

.. spec:: README Chapter Structure
   :id: SPEC_DOC_README_STRUCTURE
   :status: implemented
   :links: REQ_DOC_README, SPEC_AGENT_WORKFLOW, SPEC_INST_SETUP_AGENT
   :tags: documentation, structure, readme

   **Design:**
   Chapter structure for ``README.md``.

   .. list-table::
      :header-rows: 1
      :widths: 5 20 55

      * - #
        - Chapter
        - Content Source
      * - 1
        - Logo & Tagline
        - Static branding
      * - 2
        - Quick Start
        - SPEC_INST_CURL_BOOTSTRAP (curl commands per platform)
      * - 3
        - What You Get
        - SPEC_AGENT_WORKFLOW (agent list and responsibilities)
      * - 4
        - How It Works
        - REQ_CORE_SPHINX_NEEDS, REQ_CORE_TRACEABILITY
          (three-level hierarchy, link traversal)
      * - 5
        - Documentation
        - Link to published docs (static URL)
      * - 6
        - Requirements
        - SPEC_INST_SETUP_AGENT (prerequisites)
      * - 7
        - License
        - Static (Apache 2.0)


.. spec:: Methodology Chapter Structure
   :id: SPEC_DOC_METHODOLOGY_STRUCTURE
   :status: implemented
   :links: REQ_DOC_METHODOLOGY, REQ_CORE_DOMAIN_ORG, REQ_CORE_L1_MIRROR, SPEC_DOC_STRUCTURE
   :tags: documentation, structure, methodology

   **Design:**
   Chapter structure for ``docs/methodology.md``.

   .. list-table::
      :header-rows: 1
      :widths: 5 30 55

      * - #
        - Chapter
        - Content Source
      * - 1
        - Overview
        - SPEC_DOC_STRUCTURE (three-level hierarchy overview)
      * - 2
        - The Three Levels
        - REQ_CORE_SPHINX_NEEDS, REQ_CORE_TRACEABILITY
          (level definitions, audience, ID prefixes, directories)
      * - 3
        - File Organization Principles
        - REQ_CORE_DOMAIN_ORG (domain shift rationale)
      * - 3.1
        - Level 0 — User Stories
        - REQ_CORE_DOMAIN_ORG AC-1 (theme-based splitting)
      * - 3.2
        - Level 1 — Requirements
        - REQ_CORE_L1_MIRROR (1:1 mirroring rationale)
      * - 3.3
        - Level 2 — Design Specs
        - REQ_CORE_DOMAIN_ORG AC-3, AC-4 (component splitting)
      * - 4
        - Cross-File Traceability
        - REQ_CORE_TRACEABILITY (sphinx-needs resolves across)
      * - 5
        - Directory Layout
        - SPEC_DOC_STRUCTURE (directory tree)
      * - 6
        - Scaling Guidelines
        - REQ_CORE_DOMAIN_ORG (when to split/merge files)
      * - 7
        - Naming Conventions Reference
        - Link to namingconventions.md


.. spec:: Naming Conventions Chapter Structure
   :id: SPEC_DOC_NAMING_STRUCTURE
   :status: implemented
   :links: REQ_DOC_NAMING, SPEC_DOC_STRUCTURE
   :tags: documentation, structure, naming

   **Design:**
   Chapter structure for ``docs/namingconventions.md``.

   .. list-table::
      :header-rows: 1
      :widths: 5 30 55

      * - #
        - Chapter
        - Content Source
      * - 1
        - Overview
        - Static rationale for descriptive IDs
      * - 2
        - Why Descriptive IDs
        - SPEC_DOC_STRUCTURE (comparison table)
      * - 3
        - ID Format
        - SPEC_DOC_STRUCTURE (TYPE_THEME_SLUG pattern)
      * - 3.1
        - Theme Abbreviations
        - Derived from all theme definitions across levels
      * - 3.2
        - Examples by Level
        - Derived from existing IDs in RST files
      * - 4
        - Slug Guidelines
        - Static conventions (length, casing, separators)
      * - 5
        - Cross-Level Consistency
        - REQ_CORE_DOMAIN_ORG (theme matching rules)
      * - 6
        - Uniqueness
        - REQ_CORE_SPHINX_NEEDS (build-time validation)


.. spec:: Release Notes Chapter Structure
   :id: SPEC_DOC_RELEASE_NOTES_STRUCTURE
   :status: implemented
   :links: REQ_DOC_RELEASE_NOTES, REQ_WF_RELEASE_SEQUENCE, REQ_REL_SEMVER, SPEC_REL_NOTES_STRUCTURE
   :tags: documentation, structure, release

   **Design:**
   Chapter structure for ``docs/releasenotes.md``.

   .. list-table::
      :header-rows: 1
      :widths: 5 30 55

      * - #
        - Chapter
        - Content Source
      * - 1
        - Title
        - Static ("syspilot Release Notes")
      * - 2
        - Per-Version Section (repeating, newest first)
        - Change Documents from ``docs/changes/archive/``,
          version number from REQ_REL_SEMVER format
      * - 2.1
        - Summary
        - Aggregated from Change Document summaries
      * - 2.2
        - New Features
        - Change Documents with new US/REQ/SPEC elements
      * - 2.3
        - Internal Changes
        - Change Documents with modified elements
      * - 2.4
        - Specification Counts
        - Counted from RST files at release time

   **Note:** Release notes are primarily updated during the release workflow,
   not during individual changes. The release agent ensures the structure
   stays consistent with the template above.


.. spec:: Documentation Index Structure
   :id: SPEC_DOC_INDEX_STRUCTURE
   :status: implemented
   :links: REQ_DOC_INDEX, SPEC_DOC_STRUCTURE, SPEC_AGENT_WORKFLOW
   :tags: documentation, structure, index

   **Design:**
   Chapter structure for ``docs/index.rst``.

   .. list-table::
      :header-rows: 1
      :widths: 5 30 55

      * - #
        - Chapter
        - Content Source
      * - 1
        - Welcome / Tagline
        - Static branding + value proposition
      * - 2
        - Getting Started
        - SPEC_INST_CURL_BOOTSTRAP, SPEC_INST_SETUP_AGENT
          (download, setup steps)
      * - 3
        - How It Works
        - REQ_CORE_SPHINX_NEEDS, REQ_CORE_TRACEABILITY
          (three levels, link traversal)
      * - 4
        - Your AI Team
        - SPEC_AGENT_WORKFLOW (agent table with descriptions)
      * - 5
        - FAQ
        - Derived from common questions about the toolkit
      * - 6
        - Specification Reference
        - Toctree: 10_userstories, 11_requirements, 12_design,
          31_traceability
      * - 7
        - Guides & Process
        - Toctree: methodology, namingconventions, 40_process,
          releasenotes


.. spec:: Process Documentation Structure
   :id: SPEC_DOC_PROCESS_STRUCTURE
   :status: implemented
   :links: REQ_DOC_PROCESS, SPEC_AGENT_WORKFLOW
   :tags: documentation, structure, process

   **Design:**
   Chapter structure for ``docs/40_process/``.

   **File: index.rst**

   .. list-table::
      :header-rows: 1
      :widths: 5 30 55

      * - #
        - Chapter
        - Content Source
      * - 1
        - Overview
        - Static description of process standards used
      * - 2
        - Toctree
        - Links to aspice_alignment

   **File: aspice_alignment.rst**

   .. list-table::
      :header-rows: 1
      :widths: 5 30 55

      * - #
        - Chapter
        - Content Source
      * - 1
        - Process Mapping
        - REQ_CORE_SPHINX_NEEDS (type to A-SPICE process area map)
      * - 2
        - Traceability Chain
        - REQ_CORE_TRACEABILITY (bidirectional link chain,
          current vs planned implementation status)


Traceability
------------

.. needtable::
   :columns: id, title, status, links
   :filter: id.startswith('SPEC_DOC') and ('SYSPILOT' in id or 'README' in id or 'METHODOLOGY' in id or 'NAMING' in id or 'RELEASE' in id or 'INDEX' in id or 'PROCESS' in id)
