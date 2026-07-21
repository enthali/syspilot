Ontology Architecture Requirements
====================================

Requirements for the ontology-agnostic architecture.


.. req:: Four-Concern Separation
   :id: SYSP_REQ_ONTOLOGY_SEPARATION
   :status: draft
   :priority: mandatory
   :tags: architecture, ontology, phase-0
   :links: SYSP_US_ONTOLOGY_ARCH

   **Description:**
   The system SHALL separate Ontology, Capabilities, Actors, and Process as
   four independent concerns. Each concern SHALL be configurable without
   requiring modifications to the others.

   **Rationale:**
   Coupling these concerns forces adopters to rewrite multiple layers when
   changing one dimension (e.g. adding a Work-Product type forces changes to
   agent definitions, workflows, and tooling). Separation enables independent
   evolution and project-specific tailoring.

   **Acceptance Criteria:**

   * AC-1: Changing the set of Work-Product types does not require modifying Actor definitions or Process definitions.
   * AC-2: Changing which Actor owns a Work-Product type does not require modifying the Ontology definition or Process definition.
   * AC-3: Each concern's configuration is isolated in its own section of ``syspilot.toml`` — Ontology, Capabilities, Actors, and Process sections do not interdepend.


.. req:: Configuration Authority
   :id: SYSP_REQ_ONTOLOGY_CONFIG_AUTHORITY
   :status: draft
   :priority: mandatory
   :tags: architecture, ontology, phase-0
   :links: SYSP_US_ONTOLOGY_ARCH

   **Description:**
   ``syspilot.toml`` SHALL be the single source of truth for ontology selection
   and tailoring. All other configuration consumers (including documentation
   build configuration) SHALL derive their ontology knowledge from it.

   **Rationale:**
   A single authoritative source eliminates drift between what the ontology
   defines and what tools/agents believe the ontology to be.

   **Acceptance Criteria:**

   * AC-1: Ontology selection and tailoring parameters are defined in ``syspilot.toml``.
   * AC-2: No other file independently defines which Work-Product types are active.
   * AC-3: Consumers that need ontology information read or derive it from ``syspilot.toml``.


.. req:: Primary-Actor-Owner Invariant
   :id: SYSP_REQ_ONTOLOGY_OWNERSHIP
   :status: draft
   :priority: mandatory
   :tags: architecture, ontology, phase-0
   :links: SYSP_US_ONTOLOGY_ARCH

   **Description:**
   Every active Work-Product type SHALL have exactly one Primary-Actor-Owner.
   Multiple ownership of the same Work-Product type SHALL be forbidden. Read
   access to any Work-Product type by any Actor is unrestricted.

   **Rationale:**
   Single ownership establishes unambiguous accountability — exactly one Actor
   is responsible for creating, maintaining, and approving each Work-Product
   type. Without this invariant, conflicts and gaps emerge when multiple
   Actors believe they own (or nobody owns) a type.

   **Acceptance Criteria:**

   * AC-1: Every active Work-Product type is assigned to exactly one Actor as owner.
   * AC-2: Attempting to assign a second owner to a type is a detectable configuration error.
   * AC-3: Any Actor can read any Work-Product type regardless of ownership.


.. req:: Graph-Order Processing
   :id: SYSP_REQ_ONTOLOGY_GRAPH_ORDER
   :status: draft
   :priority: mandatory
   :tags: architecture, ontology, phase-0
   :links: SYSP_US_ONTOLOGY_ARCH

   **Description:**
   An Actor SHALL process all and only its own affected Work-Product types in
   the dependency order of the ontology graph. The system SHALL NOT assume a
   fixed numeric level sequence.

   **Rationale:**
   Real ontologies form branching directed graphs, not linear stacks. An
   Actor that owns types at multiple graph positions must process upstream
   types before downstream types to maintain consistency — but the ordering
   comes from the graph, not from a hard-coded L0/L1/L2 numbering.

   **Acceptance Criteria:**

   * AC-1: Processing order is determined by the ontology graph's dependency edges.
   * AC-2: An Actor processes only the Work-Product types it owns.
   * AC-3: The system supports branching (non-linear) ontology graphs.


.. req:: Ontology Storage
   :id: SYSP_REQ_ONTOLOGY_DIRECTORY
   :status: draft
   :priority: mandatory
   :tags: architecture, ontology, phase-0
   :links: SYSP_US_ONTOLOGY_ARCH

   **Description:**
   The system SHALL store the ontology definition in a dedicated project-local
   directory, separate from application code and build output.

   **Rationale:**
   A well-known, dedicated location enables tooling to discover the ontology
   definition without hard-coded path assumptions, and keeps ontology
   configuration separate from runtime artefacts.

   **Acceptance Criteria:**

   * AC-1: The ontology definition resides in a dedicated directory within the project.
   * AC-2: The directory is separate from application source code and build output directories.
   * AC-3: Tooling can discover the ontology definition by convention (known directory location).


.. req:: Capability Vocabulary Declaration
   :id: SYSP_REQ_ONTOLOGY_CAPABILITIES
   :status: draft
   :priority: mandatory
   :tags: architecture, ontology, phase-0
   :links: SYSP_US_ONTOLOGY_ARCH

   **Description:**
   The Capabilities concern SHALL be independently declared. A Capability is a
   named, type-agnostic operation (e.g. create, modify, review, validate,
   approve) that Actors may exercise on Work Products. The capability
   vocabulary SHALL be defined separately from Work-Product types; no
   Capability declaration depends on a specific type.

   **Rationale:**
   Decoupling capabilities from types allows the same operation vocabulary to
   be reused across different ontologies. Type-specific constraints belong to
   the Actor's ownership entry, not the capability definition itself.

   **Acceptance Criteria:**

   * AC-1: The capability vocabulary is declared independently of the ontology graph.
   * AC-2: Each capability has a unique identifier and a human-readable description.
   * AC-3: Capabilities are type-agnostic by default — constraints to specific types are expressed in the Actor's ownership entry, not in the capability declaration.


.. req:: Ontology Templates
   :id: SYSP_REQ_ONTOLOGY_TEMPLATES
   :status: draft
   :priority: mandatory
   :tags: architecture, ontology, phase-0
   :links: SYSP_US_ONTOLOGY_TEMPLATES

   **Description:**
   The system SHALL provide at least one ontology template. The
   syspilot-default template SHALL document the current User Story →
   Requirement → Design Spec ontology as a reusable configuration that
   can be applied to any new project without modification.

   **Rationale:**
   Templates lower the adoption barrier. The syspilot-default template also
   serves as schema validation — if the framework's own ontology cannot be
   expressed in it, the schema is incomplete.

   **Acceptance Criteria:**

   * AC-1: At least one ontology template is provided with the framework.
   * AC-2: The syspilot-default template expresses all Work-Product types, dependency edges, ownership assignments, and lifecycle states of the current ontology.
   * AC-3: A template is a complete, valid ontology definition — applying it requires no additional design effort.


.. req:: Ontology Generator
   :id: SYSP_REQ_ONTOLOGY_GENERATOR
   :status: draft
   :priority: mandatory
   :tags: architecture, ontology, phase-1
   :links: SYSP_US_ONTOLOGY_GENERATOR

   **Description:**
   The system SHALL provide a generator that reads ``.syspilot/ontology.toml``
   and produces ``docs/ubproject.toml`` by stripping all non-``[needs]``
   sections. The generator SHALL support a ``--compare`` mode that exits
   non-zero when the committed ``docs/ubproject.toml`` differs from a fresh
   generation.

   **Rationale:**
   The generator ensures the ubCode projection is always derivable from the
   canonical master. The compare mode provides an automated freshness check
   for the release process.

   **Acceptance Criteria:**

   * AC-1: The generator reads ``.syspilot/ontology.toml`` and writes ``docs/ubproject.toml`` containing only ``[needs]``-prefixed content.
   * AC-2: The generator preserves comments and formatting within the ``[needs]`` sections.
   * AC-3: In ``--compare`` mode, the generator exits 0 if ``docs/ubproject.toml`` matches a fresh generation, non-zero otherwise.
   * AC-4: The generator reports which sections were stripped (informational output).


.. req:: Ontology Governance
   :id: SYSP_REQ_ONTOLOGY_GOVERNANCE
   :status: draft
   :priority: mandatory
   :tags: architecture, ontology, phase-1
   :links: SYSP_US_ONTOLOGY_GOVERNANCE

   **Description:**
   ``ontology.toml`` SHALL be a guarded artifact. Every change to it SHALL be
   classified as additive or breaking. Breaking changes SHALL require a
   migration CR before they can be merged.

   **Rationale:**
   The ontology defines the vocabulary that all specs depend on. An
   uncontrolled breaking change (removing a type, renaming a status) silently
   invalidates existing specs. Classification and gate control prevent this.

   **Acceptance Criteria:**

   * AC-1: The governance rules define a classification table for additive vs. breaking changes.
   * AC-2: Breaking changes require an explicit migration CR before merge.
   * AC-3: ``sphinx-build -W`` catches type/link mismatches immediately during any CR.
   * AC-4: The Release Engineer's compare-mode check blocks release if ``docs/ubproject.toml`` is stale.


.. req:: Ontology Skill Content
   :id: SYSP_REQ_ONTOLOGY_SKILL
   :status: draft
   :priority: mandatory
   :tags: architecture, ontology, phase-1
   :links: SYSP_US_ONTOLOGY_SKILL

   **Description:**
   The ``syspilot.ontology`` skill SHALL document the ``ontology.toml`` schema
   structure, the generator invocation command, and the governance guardrails.

   **Rationale:**
   Agents that edit the ontology need a single reference for schema, tooling,
   and process rules. The skill provides this without requiring agents to read
   implementation code.

   **Acceptance Criteria:**

   * AC-1: The skill documents the ontology.toml schema (ubCode sections, syspilot sections, separator convention).
   * AC-2: The skill documents the generator command and its ``--compare`` mode.
   * AC-3: The skill documents the additive/breaking change classification and migration-CR requirement.


.. req:: Release Ontology Freshness Check
   :id: SYSP_REQ_RELEASE_ONTOLOGY_CHECK
   :status: draft
   :priority: mandatory
   :tags: architecture, ontology, phase-1
   :links: SYSP_US_ONTOLOGY_GENERATOR; SYSP_US_ONTOLOGY_GOVERNANCE; SYSP_US_RELEASE

   **Description:**
   The Release Engineer SHALL run the generator in ``--compare`` mode before
   squash-merge to main. If ``docs/ubproject.toml`` is stale relative to
   ``.syspilot/ontology.toml``, the release SHALL fail.

   **Rationale:**
   This is the last automated checkpoint before a release. It prevents
   shipping a ubCode projection that does not match the canonical ontology.

   **Acceptance Criteria:**

   * AC-1: The Release Engineer's workflow includes a compare-mode generator check before squash-merge.
   * AC-2: A stale ``docs/ubproject.toml`` causes the release to fail with a clear error message.
   * AC-3: The check runs after validation but before any merge operation.
