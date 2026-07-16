Ontology Architecture Design
=============================

Design specifications for the ontology-agnostic architecture.


.. spec:: Four-Concern Model
   :id: SYSP_SPEC_ONTOLOGY_FOUR_CONCERNS
   :status: draft
   :tags: architecture, ontology, phase-0
   :links: SYSP_REQ_ONTOLOGY_SEPARATION

   **Definition:**

   The ontology-agnostic architecture separates four independent concerns:

   * **Ontology** — declares Work-Product types, their typed dependency edges,
     and lifecycle states. Pure structure; no assignment of who or how.
   * **Capabilities** — declares operations that can be performed on Work
     Products (create, modify, review, validate, approve, …). Operations are
     type-agnostic — they apply to any Work-Product type unless constrained.
   * **Actors** — maps Capabilities to Work-Product types and assigns ownership.
     Each Actor entry declares: which types it owns (Primary-Actor-Owner), and
     which Capabilities it may exercise on those types.
   * **Process** — defines execution order, gates, and transition rules. It
     sequences Actors and their Capabilities without redefining what types
     exist or who owns them.

   **Independence Constraint:**

   Each concern is configured in its own section/file. Changing one concern
   does not require syntactic changes to another. Cross-concern references use
   stable identifiers (type names, actor names, capability names).

   **Interfaces Between Concerns:**

   ::

      Ontology  ──(type names)──►  Actors  ──(actor+capability names)──►  Process
                                     ▲
      Capabilities ─(capability names)─┘

   Ontology defines the vocabulary of types; Capabilities defines the
   vocabulary of operations; Actors binds both; Process sequences the bindings.


.. spec:: syspilot.toml Ontology Configuration
   :id: SYSP_SPEC_ONTOLOGY_TOML_SCHEMA
   :status: draft
   :tags: architecture, ontology, phase-0
   :links: SYSP_REQ_ONTOLOGY_CONFIG_AUTHORITY, SYSP_REQ_ONTOLOGY_OWNERSHIP

   **Definition:**

   ``syspilot.toml`` is the project-level entry point. It selects the active
   ontology and provides project-specific tailoring overrides.

   **Structural Requirements for the Schema:**

   The ontology definition (whether inline or referenced) SHALL contain:

   1. **Work-Product Types** — a list of type declarations, each with:

      * A unique type identifier (string)
      * A human-readable title
      * Lifecycle states applicable to this type (list)

   2. **Dependency Edges** — a list of directed edges between types, each with:

      * Source type identifier
      * Target type identifier
      * Edge semantics (e.g. ``refines``, ``validates``, ``implements``)

   3. **Ownership Assignments** — for each active type, exactly one Actor
      identifier designated as Primary-Actor-Owner.

   4. **Capabilities** — a list of operation declarations, each with:

      * A unique capability identifier
      * A human-readable description

      (Structural definition: see ``SYSP_SPEC_ONTOLOGY_CAPABILITIES``.)

   5. **Actor–Capability Bindings** — for each Actor, the set of Capabilities
      it may exercise and on which types.

   **Validation Constraints:**

   * Every type referenced in an edge SHALL exist in the type list.
   * Every type SHALL have exactly one ownership assignment (no zero, no duplicates).
   * The dependency graph SHALL be acyclic (DAG).
   * Every Actor referenced in ownership SHALL exist in the Actor–Capability
     bindings.


.. spec:: Capability Vocabulary
   :id: SYSP_SPEC_ONTOLOGY_CAPABILITIES
   :status: draft
   :tags: architecture, ontology, phase-0
   :links: SYSP_REQ_ONTOLOGY_CAPABILITIES

   **Definition:**

   The capabilities section of the ontology definition declares the vocabulary
   of operations that Actors may exercise on Work Products.

   **Schema Structure:**

   A list of capability entries, each with:

   * ``id`` — unique string identifier for the capability (e.g. ``create``,
     ``modify``, ``review``, ``validate``, ``approve``)
   * ``description`` — human-readable explanation of what the operation does

   **Type-Agnosticism:**

   Capability declarations are type-agnostic. A capability applies to any
   Work-Product type unless constrained. Type-specific constraints (e.g.
   "Actor X may only exercise ``approve`` on ``requirement``") are expressed
   in the Actor–Capability Bindings section, not in the capability
   declaration itself.

   **Constraints:**

   * Each ``id`` SHALL be unique within the capabilities list.
   * The capabilities list is independent of the ontology graph — adding or
     removing a Work-Product type does not require changes to capability
     declarations.


.. spec:: .syspilot/ Directory Structure
   :id: SYSP_SPEC_ONTOLOGY_DIRECTORY
   :status: draft
   :tags: architecture, ontology, phase-0
   :links: SYSP_REQ_ONTOLOGY_DIRECTORY

   **Definition:**

   The ``.syspilot/`` directory at project root is the conventional location
   for ontology definitions and related configuration.

   **Layout:**

   ::

      .syspilot/
      ├── ontology.toml       # Ontology definition (types, edges, lifecycle)
      └── templates/          # (future) Additional ontology templates

   **Discovery Convention:**

   Tooling discovers the ontology by looking for ``.syspilot/ontology.toml``
   relative to the project root. The project root is determined by the
   presence of ``syspilot.toml``.

   **Relationship to syspilot.toml:**

   ``syspilot.toml`` (at project root) references or includes the ontology
   definition from ``.syspilot/ontology.toml``. The top-level file is the
   authority; the directory provides the storage location.

   **Constraints:**

   * ``.syspilot/`` SHALL NOT contain application source code or build output.
   * The directory is version-controlled alongside the project.
   * The directory name starts with a dot (hidden by convention) to avoid
     collision with project source directories.


.. spec:: Ontology Graph & Dependency Order
   :id: SYSP_SPEC_ONTOLOGY_GRAPH
   :status: draft
   :tags: architecture, ontology, phase-0
   :links: SYSP_REQ_ONTOLOGY_GRAPH_ORDER

   **Definition:**

   The ontology graph is a Directed Acyclic Graph (DAG) where:

   * **Nodes** are Work-Product types.
   * **Edges** are typed dependency relations (e.g. ``refines``,
     ``validates``), directed from downstream to upstream (a Requirement
     *refines* a User Story → edge from Requirement to User Story).

   **Dependency Order:**

   "Dependency order" means topological order of the DAG. When an Actor
   processes its owned types, it processes them in topological order — upstream
   types before downstream types.

   **Branching Support:**

   The graph may branch (one type may have multiple upstream dependencies, or
   one upstream type may have multiple downstream dependents). This is
   first-class — the system does not flatten branching graphs into a linear
   sequence.

   **Processing Rule:**

   Given Actor A owns types {T1, T2, T3} and the graph has edges
   T3 → T2 → T1 (T1 is most upstream), Actor A processes in order: T1, T2, T3.
   If T2 and T3 are independent (no edge between them), their relative order
   is unspecified (both valid topological orderings are acceptable).

   **Cycle Detection:**

   A cycle in the ontology graph is a configuration error. Tooling SHALL
   detect cycles at validation time and report them before any processing
   begins.


.. spec:: Syspilot-Default Ontology Template
   :id: SYSP_SPEC_ONTOLOGY_DEFAULT_TEMPLATE
   :status: draft
   :tags: architecture, ontology, phase-0
   :links: SYSP_REQ_ONTOLOGY_TEMPLATES

   **Definition:**

   The syspilot-default template expresses the current three-level ontology as
   a reusable configuration. It serves as both the reference implementation
   and the schema validation proof.

   **Work-Product Types:**

   * ``user_story`` — captures stakeholder intent (WHY)
   * ``requirement`` — specifies system behaviour (WHAT)
   * ``design_spec`` — defines implementation approach (HOW)

   **Dependency Edges:**

   ::

      design_spec ──refines──► requirement ──refines──► user_story

   **Lifecycle States (shared):**

   ``draft`` → ``approved`` → ``implemented`` → ``verified``

   **Ownership Assignments (syspilot-default):**

   * ``user_story`` → Actor: Project Manager
   * ``requirement`` → Actor: System Designer
   * ``design_spec`` → Actor: System Designer

   **Capabilities Exercised:**

   * Project Manager: create, modify, approve (on ``user_story``)
   * System Designer: create, modify (on ``requirement``, ``design_spec``)
   * Quality Manager: review, approve (on ``requirement``, ``design_spec``)

   **Validation:**

   This template, when loaded, SHALL pass all schema validation constraints
   defined in ``SYSP_SPEC_ONTOLOGY_TOML_SCHEMA`` — it is the proof that the
   schema can express a real ontology.
