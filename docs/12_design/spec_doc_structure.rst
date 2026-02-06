Documentation Structure Design
===============================

Design specifications for the sphinx-needs documentation structure and conventions.

**Document Version**: 0.2
**Last Updated**: 2026-02-06


.. spec:: sphinx-needs Documentation Structure
   :id: SPEC_DOC_STRUCTURE
   :status: implemented
   :links: REQ_CORE_SPHINX_NEEDS, REQ_CORE_TRACEABILITY, REQ_CORE_DOMAIN_ORG, REQ_CORE_L1_MIRROR
   :tags: sphinx-needs, structure

   **Design:**
   Documentation organized in numbered folders following a three-level hierarchy.

   **Directory Structure:**

   ::

      docs/
      ├── conf.py                    # sphinx-needs configuration
      ├── index.rst                  # Main index
      ├── methodology.md             # File organization guide
      ├── namingconventions.md       # ID naming conventions
      ├── 10_userstories/
      │   ├── index.rst              # User Stories overview
      │   ├── us_core.rst            # Core stories
      │   ├── us_change_mgmt.rst     # Change management stories
      │   └── us_<theme>.rst         # Theme-based stories
      ├── 11_requirements/
      │   ├── index.rst              # Requirements overview
      │   ├── req_core.rst           # Core requirements
      │   ├── req_change_mgmt.rst    # Change management requirements
      │   └── req_<theme>.rst        # Theme-based requirements (1:1 with US)
      ├── 12_design/
      │   ├── index.rst              # Design overview
      │   └── spec_<component>.rst   # Component designs
      └── 31_traceability/
          └── index.rst              # Auto-generated traceability

   **Naming Conventions:**

   * User Stories: ``US_<THEME>_<SLUG>`` (e.g., ``US_CORE_SPEC_AS_CODE``)
   * Requirements: ``REQ_<THEME>_<SLUG>`` (e.g., ``REQ_CHG_ANALYSIS_AGENT``)
   * Designs: ``SPEC_<COMPONENT>_<SLUG>`` (e.g., ``SPEC_AGENT_WORKFLOW``)

   See ``docs/namingconventions.md`` for full convention.

   **File Organization by Domain Type:**

   Levels 0–1 are organized by **problem domain** (stakeholder themes).
   Level 2 is organized by **solution domain** (technical components).

   * **Level 0 — User Stories**: One ``us_<theme>.rst`` per stakeholder theme
     or value stream. Themes cluster by *user goal*, not by technical component.
     Examples: ``us_installation.rst``, ``us_change_mgmt.rst``, ``us_release.rst``.

   * **Level 1 — Requirements**: One ``req_<theme>.rst`` per US file (1:1 mapping).
     Each requirement file contains all requirements derived from the User Stories
     in the corresponding ``us_<theme>.rst``. This provides natural scoping,
     reviewable file sizes, and a simple mental model.

   * **Level 2 — Design Specs**: One ``spec_<component>.rst`` per technical
     component or module. A single spec file MAY satisfy requirements from
     multiple User Story themes. Cross-cutting links are expected.

   This asymmetry between Level 1 (mirrors Level 0) and Level 2 (mirrors
   architecture) is intentional. It reflects the natural boundary where the
   problem domain meets the solution domain.


Traceability
------------

.. needtable::
   :columns: id, title, status, links
   :filter: id.startswith('SPEC_DOC')
