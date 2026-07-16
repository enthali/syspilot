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
   * AC-3: Each of the four concerns has its own configuration surface.


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
