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


.. req:: Single Ontology Master
   :id: SYSP_REQ_ONTOLOGY_SINGLE_MASTER
   :status: draft
   :priority: mandatory
   :tags: architecture, ontology, phase-1
   :links: SYSP_US_ONTOLOGY_SINGLE_MASTER

   **Description:**
   The sphinx-needs ``needs_from_toml`` setting SHALL point directly at
   ``.syspilot/ontology.toml``. No intermediate generated file is used.
   Sphinx-needs reads only the ``[needs]`` sections; ``[syspilot.*]`` sections
   are ignored.

   **Rationale:**
   A single-file architecture eliminates dual-file drift. There is no
   synchronisation step to forget, no stale projection to detect.

   **Acceptance Criteria:**

   * AC-1: ``docs/conf.py`` sets ``needs_from_toml`` to a path resolving to ``.syspilot/ontology.toml``.
   * AC-2: No intermediate generated file (e.g. ``docs/ubproject.toml``) exists in the project.
   * AC-3: sphinx-needs ignores ``[syspilot.*]`` sections when reading the file.


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


.. req:: Ontology Skill Content
   :id: SYSP_REQ_ONTOLOGY_SKILL
   :status: draft
   :priority: mandatory
   :tags: architecture, ontology, phase-1
   :links: SYSP_US_ONTOLOGY_SKILL

   **Description:**
   The ``syspilot.ontology`` skill SHALL document the ``ontology.toml`` schema
   structure and the governance guardrails.

   **Rationale:**
   Agents that edit the ontology need a single reference for schema and
   process rules. The skill provides this without requiring agents to read
   implementation code.

   **Acceptance Criteria:**

   * AC-1: The skill documents the ontology.toml schema (``[needs]`` sections, ``[syspilot.*]`` sections, separator convention).
   * AC-2: The skill documents how to add new types, statuses, and link types.
   * AC-3: The skill documents the additive/breaking change classification and migration-CR requirement.


.. req:: Actor Catalogue in Ontology
   :id: SYSP_REQ_ONTOLOGY_ACTOR_CATALOG
   :status: draft
   :priority: mandatory
   :tags: architecture, ontology, phase-2
   :links: SYSP_US_ONTOLOGY_ACTOR_CATALOG

   **Description:**
   The ontology SHALL declare a ``[syspilot.actors]`` section that maps every
   Need type directive to its primary owning actor. A generic agent SHALL be
   able to determine which types it owns by reading this section alone.

   **Rationale:**
   Explicit actor-to-type mapping removes hardcoded role knowledge from agent
   code and enables runtime routing decisions based on the canonical ontology.

   **Acceptance Criteria:**

   * AC-1: A ``[syspilot.actors]`` section exists in ``ontology.toml`` with one entry per Need type.
   * AC-2: Each entry maps a directive name to its primary owning actor.
   * AC-3: Adding a new type without a corresponding actor entry causes a governance violation (documented in skill).


.. req:: Type Link Relationships
   :id: SYSP_REQ_ONTOLOGY_TYPE_LINKS
   :status: draft
   :priority: mandatory
   :tags: architecture, ontology, phase-2
   :links: SYSP_US_ONTOLOGY_TYPE_LINKS

   **Description:**
   The ontology SHALL declare a ``[syspilot.type_links]`` section that defines
   the directed, typed relationships between Need types (e.g. ``req`` refines
   ``story``, ``spec`` implements ``req``).

   **Rationale:**
   The specification hierarchy is implicit in naming conventions today. An
   explicit declaration lets agents and tooling traverse the hierarchy and
   validate traceability completeness.

   **Acceptance Criteria:**

   * AC-1: A ``[syspilot.type_links]`` section exists with one entry per directed type relationship.
   * AC-2: Each entry specifies source type, target type, and relationship semantics.
   * AC-3: The declared relationships form a DAG (no cycles).


.. req:: Lifecycle Status Transitions
   :id: SYSP_REQ_ONTOLOGY_LIFECYCLE
   :status: draft
   :priority: mandatory
   :tags: architecture, ontology, phase-2
   :links: SYSP_US_ONTOLOGY_LIFECYCLE

   **Description:**
   The ontology SHALL declare a ``[syspilot.status_transitions]`` section that
   defines the allowed status transitions for each Need type. Transitions not
   explicitly listed SHALL be considered invalid.

   **Rationale:**
   Implicit lifecycle rules lead to inconsistent status progressions. A
   machine-readable state machine enables both agent self-validation and CI
   enforcement.

   **Acceptance Criteria:**

   * AC-1: A ``[syspilot.status_transitions]`` section exists with allowed transitions declared per type.
   * AC-2: Each transition entry specifies the source status, target status, and applicable type(s).
   * AC-3: A universal fallback set applies to types without type-specific overrides.
   * AC-4: The ``deprecated`` status is reachable from any other status (universal exit).


.. req:: Ontology Reference Page Generation
   :id: SYSP_REQ_ONTOLOGY_REF_PAGE
   :status: draft
   :priority: mandatory
   :tags: architecture, ontology, phase-2
   :links: SYSP_US_ONTOLOGY_REF_PAGE

   **Description:**
   The documentation build SHALL generate an ontology reference page from
   ``ontology.toml`` at build time. The page SHALL include a type catalogue
   table, a type-relationship diagram, and a lifecycle state diagram.

   **Rationale:**
   A generated page is always in sync with the canonical ontology and
   eliminates manual maintenance drift.

   **Acceptance Criteria:**

   * AC-1: The reference page is generated from ``ontology.toml`` during ``sphinx-build``.
   * AC-2: The page includes a table of all Need types with their prefix, colour, and owning actor.
   * AC-3: The page includes a Mermaid diagram showing type relationships.
   * AC-4: The page includes a Mermaid diagram showing the lifecycle state machine.
   * AC-5: Changing ``ontology.toml`` and rebuilding updates the reference page without manual edits.


.. req:: TEST Type Split
   :id: SYSP_REQ_ONTOLOGY_TYPE_SPLIT
   :status: draft
   :priority: mandatory
   :tags: architecture, ontology, phase-2
   :links: SYSP_US_ONTOLOGY_TYPE_SPLIT

   **Description:**
   The ontology SHALL split the single ``test`` type (``TEST_``) into three
   distinct types: ``uat`` (``UAT_``), ``test`` (``TEST_``), and ``unit_test``
   (``UNIT_``). The original ``TEST_`` prefix SHALL be kept as a deprecated
   alias to allow organic migration.

   **Rationale:**
   Different test granularities have different owners, workflows, and lifecycle
   expectations. Distinct types enable precise ownership, filtering, and
   reporting.

   **Acceptance Criteria:**

   * AC-1: Three distinct types exist: ``uat`` (``UAT_``), ``test`` (``TEST_``), ``unit_test`` (``UNIT_``).
   * AC-2: Each new type has a distinct colour and owning actor.
   * AC-3: ``TEST_`` is kept as a deprecated alias (existing needs continue to build without error).
   * AC-4: The actor catalogue maps ``uat`` to Test Designer, ``test`` to Test Designer, ``unit_test`` to Dev Engineer.
