syspilot Documentation Scope
==============================

Project-specific documentation scope and per-document chapter structures for syspilot.

**Document Version**: 0.1
**Last Updated**: 2026-03-15


Document Registry
-----------------

.. spec:: syspilot Documentation Scope
   :id: SYSPILOT_SPEC_DOC_SCOPE_SYSPILOT
   :status: implemented
   :links: SYSPILOT_REQ_DOC_SCOPE, SYSPILOT_REQ_DOC_README, SYSPILOT_REQ_DOC_METHODOLOGY, SYSPILOT_REQ_DOC_NAMING, SYSPILOT_REQ_DOC_RELEASE_NOTES, SYSPILOT_REQ_DOC_PROCESS, SYSPILOT_REQ_DOC_INDEX
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
        - SYSPILOT_SPEC_DOC_README_STRUCTURE
        - SYSPILOT_REQ_DOC_README
      * - ``docs/index.rst``
        - SYSPILOT_SPEC_DOC_INDEX_STRUCTURE
        - SYSPILOT_REQ_DOC_INDEX
      * - ``docs/methodology.md``
        - SYSPILOT_SPEC_DOC_METHODOLOGY_STRUCTURE
        - SYSPILOT_REQ_DOC_METHODOLOGY
      * - ``docs/namingconventions.md``
        - SYSPILOT_SPEC_DOC_NAMING_STRUCTURE
        - SYSPILOT_REQ_DOC_NAMING
      * - ``docs/releasenotes.md``
        - SYSPILOT_SPEC_DOC_RELEASE_NOTES_STRUCTURE
        - SYSPILOT_REQ_DOC_RELEASE_NOTES
      * - ``docs/syspilot/process/``
        - SYSPILOT_SPEC_DOC_PROCESS_STRUCTURE
        - SYSPILOT_REQ_DOC_PROCESS


Chapter Structures
------------------

.. spec:: README Chapter Structure
   :id: SYSPILOT_SPEC_DOC_README_STRUCTURE
   :status: implemented
   :links: SYSPILOT_REQ_DOC_README, SYSPILOT_SPEC_AGENT_WORKFLOW, SYSPILOT_SPEC_INST_SETUP_AGENT
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
        - SYSPILOT_SPEC_INST_CURL_BOOTSTRAP (curl commands per platform)
      * - 3
        - What You Get
        - SYSPILOT_SPEC_AGENT_WORKFLOW (agent list and responsibilities)
      * - 4
        - How It Works
        - SYSPILOT_REQ_CORE_SPHINX_NEEDS, SYSPILOT_REQ_CORE_TRACEABILITY
          (three-level hierarchy, link traversal)
      * - 5
        - Documentation
        - Link to published docs (static URL)
      * - 6
        - Requirements
        - SYSPILOT_SPEC_INST_SETUP_AGENT (prerequisites)
      * - 7
        - License
        - Static (Apache 2.0)


.. spec:: Methodology Chapter Structure
   :id: SYSPILOT_SPEC_DOC_METHODOLOGY_STRUCTURE
   :status: approved
   :links: SYSPILOT_REQ_DOC_METHODOLOGY, SYSPILOT_REQ_CORE_DOMAIN_ORG, SYSPILOT_REQ_CORE_L1_MIRROR, SYSPILOT_SPEC_DOC_STRUCTURE
   :tags: documentation, structure, methodology

   **Design:**
   The methodology is split into two levels:

   * **Framework Methodology** (``docs/methodology.md``) — Agent family concept,
     directory conventions, ID prefixes, write boundaries. Applies to all families.
   * **Family Methodology** (``docs/syspilot/methodology.md``) — syspilot-specific
     spec organization (three-level hierarchy, domain shift, theme-based splitting).
     Each family defines its own methodology.

   **Framework Methodology** — chapter structure for ``docs/methodology.md``:

   .. list-table::
      :header-rows: 1
      :widths: 5 30 55

      * - #
        - Chapter
        - Content Source
      * - 1
        - Overview
        - Spec-driven development principle
      * - 2
        - Agent Families
        - Family concept (independent agent families with own spec trees)
      * - 3
        - Repository Structure
        - Root layout: ``syspilot/``, ``docs/syspilot/``, ``docs/inst/``, ``.github/``
      * - 3.1
        - Family Directories
        - ``<family>/`` for product, ``docs/<family>/`` for specs
      * - 3.2
        - Instance Directories
        - ``docs/inst/<family>/`` for project-specific specs
      * - 3.3
        - Installation Directory
        - ``.github/agents/`` — flat, all families
      * - 4
        - ID Naming Convention
        - ``FAMILY_TYPE_THEME_SLUG`` pattern, link to namingconventions.md
      * - 5
        - Write Boundaries
        - Which agent writes where (Implement → family/, Setup → .github/)
      * - 6
        - Cross-Tree Linking
        - sphinx-needs links across families and instance trees
      * - 7
        - Family Methodology Reference
        - Link to ``docs/<family>/methodology.md``

   **syspilot Family Methodology** — chapter structure for
   ``docs/syspilot/methodology.md`` (created in Change 2):

   .. list-table::
      :header-rows: 1
      :widths: 5 30 55

      * - #
        - Chapter
        - Content Source
      * - 1
        - The Three Levels
        - SYSPILOT_REQ_CORE_SPHINX_NEEDS, SYSPILOT_REQ_CORE_TRACEABILITY
          (US → REQ → SPEC hierarchy, audience, directories)
      * - 2
        - File Organization Principles
        - SYSPILOT_REQ_CORE_DOMAIN_ORG (domain shift rationale)
      * - 2.1
        - Level 0 — User Stories
        - SYSPILOT_REQ_CORE_DOMAIN_ORG AC-1 (theme-based splitting)
      * - 2.2
        - Level 1 — Requirements
        - SYSPILOT_REQ_CORE_L1_MIRROR (1:1 mirroring rationale)
      * - 2.3
        - Level 2 — Design Specs
        - SYSPILOT_REQ_CORE_DOMAIN_ORG AC-3, AC-4 (component splitting)
      * - 3
        - Cross-File Traceability
        - SYSPILOT_REQ_CORE_TRACEABILITY (sphinx-needs resolves across)
      * - 4
        - Scaling Guidelines
        - SYSPILOT_REQ_CORE_DOMAIN_ORG (when to split/merge files)


.. spec:: Naming Conventions Chapter Structure
   :id: SYSPILOT_SPEC_DOC_NAMING_STRUCTURE
   :status: approved
   :links: SYSPILOT_REQ_DOC_NAMING, SYSPILOT_SPEC_DOC_STRUCTURE
   :tags: documentation, structure, naming

   **Design:**
   The naming conventions are split into two levels:

   * **Framework Naming** (``docs/namingconventions.md``) — ID format
     ``FAMILY_TYPE_THEME_SLUG``, family prefixes, directory naming rules.
   * **Family Naming** (``docs/syspilot/namingconventions.md``) —
     syspilot-specific themes, slug guidelines, examples.

   **Framework Naming** — chapter structure for ``docs/namingconventions.md``:

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
        - Comparison table (sequential vs descriptive)
      * - 3
        - ID Format
        - ``FAMILY_TYPE_THEME_SLUG`` pattern
      * - 3.1
        - Family Prefixes
        - ``SYSPILOT_``, ``SYSMLV2_``, ``INST_``, ``COMMON_``
      * - 3.2
        - Type Abbreviations
        - ``US``, ``REQ``, ``SPEC`` (common across families)
      * - 4
        - Directory Naming
        - ``<family>/`` for product, ``docs/<family>/`` for specs
      * - 5
        - Cross-Family Linking
        - sphinx-needs links across family boundaries
      * - 6
        - Uniqueness
        - SYSPILOT_REQ_CORE_SPHINX_NEEDS (build-time validation)

   **syspilot Family Naming** — chapter structure for
   ``docs/syspilot/namingconventions.md`` (created in Change 2):

   .. list-table::
      :header-rows: 1
      :widths: 5 30 55

      * - #
        - Chapter
        - Content Source
      * - 1
        - Theme Abbreviations
        - Problem-domain themes (CORE, CHG, INST, REL, etc.)
      * - 2
        - Component Themes (Level 2)
        - Solution-domain themes (AGENT, IMPL, VERIFY, etc.)
      * - 3
        - Slug Guidelines
        - Static conventions (length, casing, separators)
      * - 4
        - Examples by Level
        - ``SYSPILOT_US_``, ``SYSPILOT_REQ_``, ``SYSPILOT_SPEC_``
      * - 5
        - Cross-Level Consistency
        - SYSPILOT_REQ_CORE_DOMAIN_ORG (theme matching rules)


.. spec:: Release Notes Chapter Structure
   :id: SYSPILOT_SPEC_DOC_RELEASE_NOTES_STRUCTURE
   :status: implemented
   :links: SYSPILOT_REQ_DOC_RELEASE_NOTES, SYSPILOT_REQ_WF_RELEASE_SEQUENCE, SYSPILOT_REQ_REL_SEMVER, SYSPILOT_SPEC_REL_NOTES_STRUCTURE
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
          version number from SYSPILOT_REQ_REL_SEMVER format
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
   :id: SYSPILOT_SPEC_DOC_INDEX_STRUCTURE
   :status: implemented
   :links: SYSPILOT_REQ_DOC_INDEX, SYSPILOT_SPEC_DOC_STRUCTURE, SYSPILOT_SPEC_AGENT_WORKFLOW
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
        - SYSPILOT_SPEC_INST_CURL_BOOTSTRAP, SYSPILOT_SPEC_INST_SETUP_AGENT
          (download, setup steps)
      * - 3
        - How It Works
        - SYSPILOT_REQ_CORE_SPHINX_NEEDS, SYSPILOT_REQ_CORE_TRACEABILITY
          (three levels, link traversal)
      * - 4
        - Your AI Team
        - SYSPILOT_SPEC_AGENT_WORKFLOW (agent table with descriptions)
      * - 5
        - FAQ
        - Derived from common questions about the toolkit
      * - 6
        - Specification Reference
        - Toctree: syspilot/userstories, syspilot/requirements, syspilot/design,
          traceability
      * - 7
        - Guides & Process
        - Toctree: methodology, namingconventions, syspilot/process,
          releasenotes


.. spec:: Process Documentation Structure
   :id: SYSPILOT_SPEC_DOC_PROCESS_STRUCTURE
   :status: implemented
   :links: SYSPILOT_REQ_DOC_PROCESS, SYSPILOT_SPEC_AGENT_WORKFLOW
   :tags: documentation, structure, process

   **Design:**
   Chapter structure for ``docs/syspilot/process/``.

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
        - SYSPILOT_REQ_CORE_SPHINX_NEEDS (type to A-SPICE process area map)
      * - 2
        - Traceability Chain
        - SYSPILOT_REQ_CORE_TRACEABILITY (bidirectional link chain,
          current vs planned implementation status)


Traceability
------------

.. needtable::
   :columns: id, title, status, links
   :filter: id.startswith('SYSPILOT_SPEC_DOC') and ('SYSPILOT' in id or 'README' in id or 'METHODOLOGY' in id or 'NAMING' in id or 'RELEASE' in id or 'INDEX' in id or 'PROCESS' in id)
