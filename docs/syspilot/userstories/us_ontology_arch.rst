Ontology Architecture
=====================

Architecture decision: syspilot becomes ontology-agnostic.


.. story:: Ontology-Agnostic Architecture
   :id: SYSP_US_ONTOLOGY_ARCH
   :status: draft
   :priority: mandatory
   :tags: architecture, ontology, phase-0

   **As a** syspilot adopter,
   **I want** syspilot's methodology to be ontology-agnostic — separating what
   Work-Product types exist from how agents operate on them,
   **so that** I can adopt any work-product hierarchy (e.g. ASPICE, V-model,
   custom) without rewriting agents, workflows, or tooling.

   **Context:**

   syspilot currently embeds its default ontology (User Story → Requirement →
   Design Spec, L0/L1/L2) directly into agent prose, workflows, templates, and
   tools. Every migration to a different ontology requires rewriting all
   affected agents individually — a repeatable effort without a structural
   solution.

   The architecture separates four concerns:

   * **Ontology** — which Work-Product types exist, how they are linked, which
     lifecycle rules apply.
   * **Capabilities** — which operations can create, modify, check, and
     validate Work Products.
   * **Actors** — which Capabilities and Work-Product types each Actor owns.
   * **Process** — in which order Actors operate, which gates control
     transitions.

   This CR (Phase 0) documents the architecture decision and anchors the
   ontology concern in the spec tree. Subsequent phases implement it.

   **Acceptance Criteria:**

   1. Given the syspilot architecture, When I inspect its concerns, Then Ontology, Capabilities, Actors, and Process are independently defined and separately configurable.
   2. Given an active Work-Product type, When I inspect ownership, Then exactly one Actor is its Primary-Actor-Owner.
   3. Given a branching ontology graph, When an Actor processes its types, Then it follows the graph's dependency order — not a hard-coded level numbering.
   4. Given the project configuration, When I look for the single source of truth for ontology selection and tailoring, Then it is ``syspilot.toml`` — not ``conf.py`` or any agent file.
   5. Given the ontology configuration, When I look for the ontology definition, Then it is stored in a dedicated, discoverable, project-local directory (``.syspilot/``) — not scattered across agent files or ``conf.py``.


.. story:: Ontology Templates
   :id: SYSP_US_ONTOLOGY_TEMPLATES
   :status: draft
   :priority: mandatory
   :tags: architecture, ontology, phase-0

   **As a** syspilot adopter,
   **I want** ready-made ontology templates that express proven configurations,
   **so that** I can start from a working baseline instead of designing an
   ontology from scratch.

   **Context:**

   An ontology-agnostic system without examples is hard to adopt. Providing at
   least one reference template — syspilot's own current ontology (User Story →
   Requirement → Design Spec) — validates the schema and gives adopters a
   concrete starting point. Additional templates (e.g. ASPICE, V-model) can be
   contributed over time.

   **Acceptance Criteria:**

   1. Given the ontology framework, When I look for templates, Then at least one ready-made ontology template is available.
   2. Given the syspilot-default template, When I inspect it, Then it expresses the current L0/L1/L2 ontology (User Story → Requirement → Design Spec) as a reusable configuration.
   3. Given any ontology template, When I apply it to a project, Then it provides a complete, valid ontology definition that requires no additional design effort to start working.
