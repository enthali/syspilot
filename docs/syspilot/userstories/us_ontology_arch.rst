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


.. story:: Single Ontology Master
   :id: SYSP_US_ONTOLOGY_SINGLE_MASTER
   :status: draft
   :priority: mandatory
   :tags: architecture, ontology, phase-1

   **As a** syspilot developer,
   **I want** ``.syspilot/ontology.toml`` to be the single canonical ontology
   source read directly by sphinx-needs,
   **so that** there is no dual-file drift risk and no synchronisation step.

   **Context:**

   Phase 0 established ``.syspilot/ontology.toml`` as the canonical master.
   Phase 1 eliminates any intermediate projection file — sphinx-needs reads
   the master directly via ``needs_from_toml``. The file contains both
   ``[needs]`` sections (sphinx-needs vocabulary) and ``[syspilot.*]`` sections
   (syspilot-only metadata, ignored by sphinx-needs).

   **Acceptance Criteria:**

   1. Given the sphinx-needs configuration, When I inspect ``docs/conf.py``, Then it points ``needs_from_toml`` directly at ``.syspilot/ontology.toml``.
   2. Given ``.syspilot/ontology.toml``, When sphinx-needs reads it, Then only the ``[needs]`` sections are consumed; ``[syspilot.*]`` sections are ignored.
   3. Given the project, When I search for an intermediate generated ontology file, Then none exists.


.. story:: Ontology Governance
   :id: SYSP_US_ONTOLOGY_GOVERNANCE
   :status: draft
   :priority: mandatory
   :tags: architecture, ontology, phase-1

   **As a** syspilot adopter,
   **I want** ``ontology.toml`` to be a governed artifact with
   additive/breaking change classification,
   **so that** accidental breaking changes are caught before they reach main.

   **Context:**

   The ontology defines the vocabulary that all specs, agents, and tools depend
   on. Removing or renaming a type, status, or link is a breaking change that
   can silently invalidate existing specs. Governance rules classify changes and
   require a migration CR for breaking ones.

   **Acceptance Criteria:**

   1. Given a proposed ontology change, When I inspect the governance rules, Then I can classify it as additive or breaking.
   2. Given a breaking ontology change, When I attempt to merge it, Then a migration CR is required before the change can proceed.
   3. Given any ontology change, When the CR runs sphinx-build -W, Then type/link mismatches are caught immediately.


.. story:: Ontology Skill
   :id: SYSP_US_ONTOLOGY_SKILL
   :status: draft
   :priority: mandatory
   :tags: architecture, ontology, phase-1

   **As a** System Designer,
   **I want** a skill that explains how to edit ``ontology.toml``,
   **so that** I can evolve the ontology correctly without reading
   implementation details.

   **Context:**

   The ``syspilot.ontology`` skill is loaded by any agent that needs to
   understand or modify the ontology. It documents the schema and the
   governance guardrails.

   **Acceptance Criteria:**

   1. Given the skill, When I read it, Then it documents the ontology.toml schema structure.
   2. Given the skill, When I propose an ontology change, Then it tells me how to classify it and what approvals are needed.
   3. Given the skill, When I need to add a new type, Then it shows me where to place the entry and how to verify it.
