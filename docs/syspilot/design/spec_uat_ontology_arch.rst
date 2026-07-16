Ontology Architecture UAT Expected Outcomes
============================================

Expected outcomes specification for ``SYSP_REQ_UAT_ONTOLOGY_ARCH``.
This document is the per-scenario verification checklist a human tester runs.


.. spec:: UAT Expected Outcomes: Ontology-Agnostic Architecture (Phase 0)
   :id: SYSP_SPEC_UAT_ONTOLOGY_ARCH
   :status: draft
   :priority: mandatory
   :tags: uat, ontology, architecture, phase-0, expected-outcomes
   :links: SYSP_REQ_UAT_ONTOLOGY_ARCH

   **Definition:**

   For each scenario in ``SYSP_US_UAT_ONTOLOGY_ARCH``, the following
   outcomes SHALL be observable in the checked-out spec files. Each scenario
   is self-contained: the human tester opens the named file, locates the
   named section, and confirms the exact conditions. A check item passes
   when the stated condition is met; it fails otherwise.

   All scenarios are read-only spec-review checks. No project installation
   or runtime environment is required for AC-1 through AC-6.

   ---

   **TC-4CONCERN — Four-concern model documentation (AC-1)**

   *Precondition:* Fixture ``F-SPEC-BRANCH`` active; open
   ``docs/syspilot/design/spec_ontology_arch.rst``.

   *Action:* Locate ``SYSP_SPEC_ONTOLOGY_FOUR_CONCERNS``. Read the
   "Independence Constraint" paragraph and the ASCII diagram.

   *Expected result:*

   * [ ] The four concern names appear as bold terms: **Ontology**,
     **Capabilities**, **Actors**, **Process** — each with a distinct definition
   * [ ] An "Independence Constraint" paragraph states that changing one concern
     does not require syntactic changes to any other
   * [ ] An ASCII interface diagram shows stable-identifier arrows between the
     concerns (e.g. Ontology → type names → Actors)
   * [ ] "Process" is listed as a distinct concern separate from Actors

   *Traces to:* ``SYSP_US_ONTOLOGY_ARCH`` AC-1, ``SYSP_REQ_ONTOLOGY_SEPARATION`` AC-3

   ---

   **TC-CONFIG-AUTH — syspilot.toml is the single source of truth (AC-2)**

   *Precondition:* Fixture ``F-SPEC-BRANCH`` active; open
   ``docs/syspilot/design/spec_ontology_arch.rst``.

   *Action:* Locate ``SYSP_SPEC_ONTOLOGY_TOML_SCHEMA``. Read the opening
   sentence. Then search the entire file for any other spec element that
   designates a different file as a configuration authority for ontology
   selection.

   *Expected result:*

   * [ ] The opening sentence of ``SYSP_SPEC_ONTOLOGY_TOML_SCHEMA`` contains
     "``syspilot.toml`` is the project-level entry point"
   * [ ] The spec describes ``conf.py`` (or any other file) only as an
     "adapter/consumer" — not as an authority
   * [ ] No other spec element in this CR designates a file other than
     ``syspilot.toml`` as the configuration authority for ontology selection

   *Testability note:* The absence of contradictory authority claims is
   verifiable by reading all five SPEC elements in the file; it cannot be
   confirmed by automated tooling alone at Phase 0.

   *Traces to:* ``SYSP_US_ONTOLOGY_ARCH`` AC-4, ``SYSP_REQ_ONTOLOGY_CONFIG_AUTHORITY`` AC-1, AC-2

   ---

   **TC-OWNERSHIP — Single-owner invariant expressed in spec (AC-3)**

   *Precondition:* Fixture ``F-SPEC-BRANCH`` active; open
   ``docs/syspilot/design/spec_ontology_arch.rst``.

   *Action:* Locate ``SYSP_SPEC_ONTOLOGY_TOML_SCHEMA``. Navigate to the
   "Validation Constraints" section.

   *Expected result:*

   * [ ] A bullet point states: "Every type SHALL have exactly one ownership
     assignment (no zero, no duplicates)"
   * [ ] The word "exactly" or an equivalent unambiguous quantifier is present
   * [ ] No other validation constraint in the section contradicts or weakens
     this rule

   *Traces to:* ``SYSP_US_ONTOLOGY_ARCH`` AC-2, ``SYSP_REQ_ONTOLOGY_OWNERSHIP`` AC-1, AC-2

   ---

   **TC-GRAPH-ORDER — Graph-order processing, no L0/L1/L2 numbering (AC-4)**

   *Precondition:* Fixture ``F-SPEC-BRANCH`` active; open
   ``docs/syspilot/design/spec_ontology_arch.rst``.

   *Action:* Locate ``SYSP_SPEC_ONTOLOGY_GRAPH``. Read the "Dependency Order",
   "Branching Support", and "Processing Rule" sections.

   *Expected result:*

   * [ ] "Dependency order" is defined as topological order of the DAG
   * [ ] "Branching Support" states that branching graphs are first-class
   * [ ] "Branching" is described as non-linear (one type may have multiple
     upstream dependencies, or one upstream type may have multiple dependents)
   * [ ] No reference to L0, L1, or L2 level numbering as the ordering
     mechanism appears in the spec element
   * [ ] A concrete processing example is given (e.g. Actor owns T1, T2, T3;
     graph order determines sequence)

   *Traces to:* ``SYSP_US_ONTOLOGY_ARCH`` AC-3, ``SYSP_REQ_ONTOLOGY_GRAPH_ORDER`` AC-1, AC-3

   ---

   **TC-DIRECTORY — .syspilot/ directory convention documented (AC-5)**

   *Precondition:* Fixture ``F-SPEC-BRANCH`` active; open
   ``docs/syspilot/design/spec_ontology_arch.rst``.

   *Action:* Locate ``SYSP_SPEC_ONTOLOGY_DIRECTORY``. Read the Layout code
   block and the Discovery Convention paragraph.

   *Expected result:*

   * [ ] The Layout code block shows ``.syspilot/`` as the directory name
   * [ ] ``ontology.toml`` appears as a file inside ``.syspilot/``
   * [ ] The "Discovery Convention" paragraph states tooling looks for
     ``.syspilot/ontology.toml`` relative to the project root
   * [ ] The project root is described as being determined by the presence
     of ``syspilot.toml``
   * [ ] A "Relationship to syspilot.toml" section or equivalent links the
     directory back to the top-level configuration file

   *Traces to:* ``SYSP_US_ONTOLOGY_ARCH`` AC-4, ``SYSP_REQ_ONTOLOGY_DIRECTORY`` AC-1, AC-3

   ---

   **TC-DEFAULT-TEMPLATE — syspilot-default template is complete and self-validating (AC-6)**

   *Precondition:* Fixture ``F-SPEC-BRANCH`` active; open
   ``docs/syspilot/design/spec_ontology_arch.rst``.

   *Action:* Locate ``SYSP_SPEC_ONTOLOGY_DEFAULT_TEMPLATE``. Read the
   Work-Product Types, Dependency Edges, Ownership Assignments, and
   Validation sections.

   *Expected result:*

   * [ ] Three Work-Product types are declared: ``user_story``,
     ``requirement``, ``design_spec``
   * [ ] The dependency edge chain ``design_spec ──refines──► requirement
     ──refines──► user_story`` (or equivalent) is present
   * [ ] Ownership assignments map each type to exactly one named Actor
   * [ ] A "Validation" section explicitly states that this template, when
     loaded, SHALL pass all schema validation constraints defined in
     ``SYSP_SPEC_ONTOLOGY_TOML_SCHEMA``
   * [ ] No Work-Product type is listed without a corresponding ownership
     assignment

   *Traces to:* ``SYSP_US_ONTOLOGY_TEMPLATES`` AC-1, AC-2, AC-3,
   ``SYSP_REQ_ONTOLOGY_TEMPLATES``

   ---

   **TC-TRACE — Traceability chain and clean build (AC-7)**

   *Precondition:* Fixture ``F-BUILD-CLEAN`` — branch checked out, docs
   build environment available.

   *Action:* From the repo root, run:

   .. code-block:: shell

      cd docs
      uv run python docs-build.py clean

   Then inspect ``_build/html/schema_violations.json`` (if present).

   *Expected result:*

   * [ ] The build completes with exit code 0
   * [ ] Zero ``WARNING:`` lines appear in build output
   * [ ] ``schema_violations.json`` reports zero violations
   * [ ] Every new L2 spec element (five SYSP_SPEC_ONTOLOGY_* items) carries
     a ``:links:`` pointing to an existing L1 req in this CR
   * [ ] Every new L1 req element (six SYSP_REQ_ONTOLOGY_* items) carries a
     ``:links:`` pointing to an existing L0 user story in this CR
   * [ ] No new spec element is referenced from an index file that does not
     include its RST file in a ``toctree``

   *Traces to:* ``SYSP_US_ONTOLOGY_ARCH`` AC-1 through AC-4 (completeness
   gate), ``SYSP_US_ONTOLOGY_TEMPLATES`` AC-1 through AC-3
