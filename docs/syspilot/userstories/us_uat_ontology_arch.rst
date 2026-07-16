Ontology Architecture UAT
=========================

User Acceptance Test Story for the ``ontology-architecture-decision`` change
request — verifying that the Phase 0 architecture documentation is complete,
internally consistent, and correctly linked before any implementation begins.


.. story:: UAT: Ontology-Agnostic Architecture (Phase 0 Spec Review)
   :id: SYSP_US_UAT_ONTOLOGY_ARCH
   :status: draft
   :priority: mandatory
   :tags: uat, ontology, architecture, phase-0
   :links: SYSP_US_ONTOLOGY_ARCH, SYSP_US_ONTOLOGY_TEMPLATES

   **As a** syspilot Test Designer,
   **I want** self-contained test scenarios that let a human verify the
   Phase 0 architecture documentation expresses all five key invariants clearly
   and without contradiction, and that the new spec elements form a complete,
   clean traceability chain,
   **so that** the architecture decision is reviewable, auditable, and ready
   to anchor the subsequent implementation phases.

   **Context:**

   Phase 0 is pure architecture documentation — no code, no agent changes.
   All UAT scenarios in this chain are spec-review scenarios: a human opens
   the referenced file, reads the referenced section, and confirms the stated
   condition. No runtime environment is required.

   **Artifacts Under Test:**

   * ``docs/syspilot/design/spec_ontology_arch.rst`` — all five spec elements:
     ``SYSP_SPEC_ONTOLOGY_FOUR_CONCERNS``, ``SYSP_SPEC_ONTOLOGY_TOML_SCHEMA``,
     ``SYSP_SPEC_ONTOLOGY_DIRECTORY``, ``SYSP_SPEC_ONTOLOGY_GRAPH``,
     ``SYSP_SPEC_ONTOLOGY_DEFAULT_TEMPLATE``
   * ``docs/syspilot/requirements/req_ontology_arch.rst`` — six REQ elements
   * ``docs/syspilot/userstories/us_ontology_arch.rst`` — two US elements
   * sphinx-build -W output — traceability and build gate

   **Acceptance Criteria:**

   1. Given the spec element ``SYSP_SPEC_ONTOLOGY_FOUR_CONCERNS``, When I read it, Then it names and defines all four concerns (Ontology, Capabilities, Actors, Process), states the Independence Constraint explicitly, and shows stable-identifier interfaces between the concerns.
   2. Given the spec element ``SYSP_SPEC_ONTOLOGY_TOML_SCHEMA``, When I inspect its authority statement, Then ``syspilot.toml`` is unambiguously designated as the project-level entry point and single source of truth — no other file is designated as a configuration authority for ontology selection in any spec element of this CR.
   3. Given the spec element ``SYSP_SPEC_ONTOLOGY_TOML_SCHEMA``, When I read the Validation Constraints section, Then the constraint "every type SHALL have exactly one ownership assignment (no zero, no duplicates)" is present and unambiguous.
   4. Given the spec element ``SYSP_SPEC_ONTOLOGY_GRAPH``, When I read the Dependency Order and Branching Support sections, Then processing order is defined as topological order of the DAG, branching is explicitly first-class, and no reference to L0/L1/L2 numbering appears as the ordering mechanism.
   5. Given the spec element ``SYSP_SPEC_ONTOLOGY_DIRECTORY``, When I read the Layout and Discovery Convention sections, Then the directory path ``.syspilot/`` is named, ``ontology.toml`` is the file inside it, and discovery is described as resolving ``.syspilot/ontology.toml`` relative to the project root (anchored by ``syspilot.toml``).
   6. Given the spec element ``SYSP_SPEC_ONTOLOGY_DEFAULT_TEMPLATE``, When I inspect it, Then it declares three Work-Product types (user_story, requirement, design_spec), defines the dependency-edge chain design_spec → requirement → user_story, and explicitly states that this template SHALL pass all schema validation constraints in ``SYSP_SPEC_ONTOLOGY_TOML_SCHEMA``.
   7. Given all new spec elements (L0, L1, L2), When I check traceability links and run ``sphinx-build -W``, Then every L2 spec links to at least one L1 req, every L1 req links to at least one L0 US, and the build completes with zero warnings.

   **Testability Note:**

   AC-1 through AC-6 are read-only spec-review checks — no runtime environment
   is needed. AC-7 requires running ``sphinx-build -W`` (command given in
   ``SYSP_REQ_UAT_ONTOLOGY_ARCH``).

   **Traceability:**

   Test data is defined in ``SYSP_REQ_UAT_ONTOLOGY_ARCH``; expected outcomes
   in ``SYSP_SPEC_UAT_ONTOLOGY_ARCH``.
