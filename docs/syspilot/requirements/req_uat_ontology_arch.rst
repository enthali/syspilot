Ontology Architecture UAT Test Data
=====================================

Test data requirements for ``SYSP_US_UAT_ONTOLOGY_ARCH``.


.. req:: UAT Test Data: Ontology-Agnostic Architecture (Phase 0)
   :id: SYSP_REQ_UAT_ONTOLOGY_ARCH
   :status: draft
   :priority: mandatory
   :tags: uat, ontology, architecture, phase-0, test-data
   :links: SYSP_US_UAT_ONTOLOGY_ARCH

   **Description:**

   To run the scenarios in ``SYSP_US_UAT_ONTOLOGY_ARCH``, the following
   artifacts and reference data SHALL be available to the human tester.
   All scenarios are read-only spec-review checks; no project installation
   or runtime environment is required.

   **Primary Artifacts Under Test:**

   .. list-table:: Artifacts Under Test
      :header-rows: 1
      :widths: 40 30 30

      * - Artifact
        - Location
        - Relevance
      * - ``spec_ontology_arch.rst``
        - ``docs/syspilot/design/``
        - All five SPEC elements (AC-1 through AC-6)
      * - ``req_ontology_arch.rst``
        - ``docs/syspilot/requirements/``
        - Six REQ elements (AC-7 traceability)
      * - ``us_ontology_arch.rst``
        - ``docs/syspilot/userstories/``
        - Two US elements (AC-7 traceability)

   **Fixtures:**

   .. list-table:: Fixtures
      :header-rows: 1
      :widths: 22 38 40

      * - Fixture
        - State
        - Used By
      * - ``F-SPEC-BRANCH``
        - Branch ``feature/ontology-architecture-decision`` checked out
          locally; ``spec_ontology_arch.rst`` present and readable
        - AC-1 through AC-6
      * - ``F-BUILD-CLEAN``
        - Running ``cd docs && uv run python docs-build.py clean``
          from the repo root returns exit code 0 with no ``WARNING``
          lines and the ``_build/html/schema_violations.json`` reports
          no violations
        - AC-7

   **Reference Data:**

   * Exact section names to locate within ``spec_ontology_arch.rst``:

     * AC-1: "Independence Constraint" paragraph and the ASCII interface diagram inside ``SYSP_SPEC_ONTOLOGY_FOUR_CONCERNS``
     * AC-2: Opening sentence of ``SYSP_SPEC_ONTOLOGY_TOML_SCHEMA`` ("``syspilot.toml`` is the project-level entry point")
     * AC-3: "Validation Constraints" bullet list inside ``SYSP_SPEC_ONTOLOGY_TOML_SCHEMA``
     * AC-4: "Dependency Order" and "Branching Support" paragraphs inside ``SYSP_SPEC_ONTOLOGY_GRAPH``
     * AC-5: "Layout" code block and "Discovery Convention" paragraph inside ``SYSP_SPEC_ONTOLOGY_DIRECTORY``
     * AC-6: "Work-Product Types", "Dependency Edges", and "Validation" paragraphs inside ``SYSP_SPEC_ONTOLOGY_DEFAULT_TEMPLATE``

   **Build Command (AC-7):**

   .. code-block:: shell

      cd docs
      uv run python docs-build.py clean

   A clean run produces no ``WARNING:`` lines. Check
   ``_build/html/schema_violations.json`` for any schema violations.

   **Tooling:**

   No additional tooling beyond a text editor and the standard sphinx build
   is required for any scenario in this chain.
