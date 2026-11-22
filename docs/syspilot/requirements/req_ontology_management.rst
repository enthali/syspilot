Ontology Management
===================

.. req:: Current Ontology Schema Guidance
   :id: SYSP_REQ_ONTOLOGY_SCHEMA
   :status: approved
   :implements: SYSP_US_ONTOLOGY_MANAGEMENT
   :realized_by: .github/skills/syspilot.ontology/SKILL.md

   The Ontology skill shall explain the active project ontology, the one
   bound through ``needs_from_toml``, without naming a fixed path or a fixed
   type list, including:

   - the separation between Sphinx-Needs configuration under ``[needs]`` and
     optional syspilot-specific metadata under ``[syspilot]``;
   - the configured Need types, statuses, extra options, and extra links;
   - the absence of a required Syspilot type-pair or status-transition schema
     under ``[syspilot]``; configured link kinds and statuses come from
     ``[needs]``; and
   - the absence of centralized artifact-owner or actor-name assignments,
     because applicable Contracts declare ownership and responsibility.

   The guidance shall not describe removed Need types, obsolete actors, or
   schema fields that are absent from the active project ontology.

.. vc:: Ontology guidance matches the current schema
   :id: SYSP_VC_ONTOLOGY_SCHEMA_1
   :status: approved
   :verifies: SYSP_REQ_ONTOLOGY_SCHEMA

   Every skill section and example holds for both Syspilot's own ontology and
   the Example Ontology, or names the bound ontology as its source; removed
   types, obsolete actors and absent fields are not taught.

.. vc:: Ontology guidance leaves governance with Contracts
   :id: SYSP_VC_ONTOLOGY_SCHEMA_2
   :status: approved
   :verifies: SYSP_REQ_ONTOLOGY_SCHEMA

   Guidance distinguishes ``[needs]`` configuration from optional metadata;
   neither mandatory graph/transition metadata nor centralized actor ownership
   is introduced.

.. req:: Contract-Owned Ontology Editing And Validation
   :id: SYSP_REQ_ONTOLOGY_EDITING
   :status: approved
   :implements: SYSP_US_ONTOLOGY_MANAGEMENT
   :realized_by: .github/skills/syspilot.ontology/SKILL.md

   When an applicable Contract includes an ontology change, the Ontology skill
   shall provide technical instructions to:

   - edit Need types, statuses, extra options, extra links, and other
     project-configured Sphinx-Needs options represented by the current schema,
     without requiring Syspilot graph or transition metadata;
   - preserve unrelated existing project ontology content and Setup's rule that
     installs the Example Ontology only when none exists;
   - record the decision, responsibility, affected artifacts, and evidence in
     the applicable Contract rather than defining separate CR or migration
     governance in the skill; and
   - run the project's strict documentation and schema validation after the
     edit and resolve ontology warnings before completion.

   Establishing a project-specific ontology immediately after Setup is outside
   this capability unless a future Contract explicitly includes that work.

.. vc:: Contract-owned ontology edits preserve unrelated configuration
   :id: SYSP_VC_ONTOLOGY_EDITING_1
   :status: approved
   :verifies: SYSP_REQ_ONTOLOGY_EDITING

   A representative edit changes only Contract-included current-schema
   surfaces and preserves unrelated ontology content and Setup's install-only-when-absent behavior.

.. vc:: Ontology editing records governance in the Contract
   :id: SYSP_VC_ONTOLOGY_EDITING_2
   :status: approved
   :verifies: SYSP_REQ_ONTOLOGY_EDITING

   Skill instructions record decision, responsibility, affected artifacts and
   evidence in the applicable Contract, with no separate CR or migration gate.

.. vc:: Ontology editing requires strict validation
   :id: SYSP_VC_ONTOLOGY_EDITING_3
   :status: approved
   :verifies: SYSP_REQ_ONTOLOGY_EDITING

   The edit's documentation and schema validation report zero warnings before
   completion.

.. vc:: Post-Setup ontology establishment needs explicit scope
   :id: SYSP_VC_ONTOLOGY_EDITING_4
   :status: approved
   :verifies: SYSP_REQ_ONTOLOGY_EDITING

   Establishing a project-specific ontology immediately after Setup is included
   only by explicit Contract scope, not assumed from the editing capability.

.. req:: Ontologies Live With The Specifications
   :id: SYSP_REQ_ONTOLOGY_LOCATION
   :status: approved
   :implements: SYSP_US_ONTOLOGY_MANAGEMENT
   :realized_by: docs/conf.py

   Each ontology shall be a folder ``docs/<Name> Ontology/`` that holds its
   ``ontology.toml`` and a reader-oriented ``ontology.md``:

   - Syspilot's own ontology is ``docs/Syspilot Ontology/``; ``docs/conf.py``
     binds its ``ontology.toml`` through ``needs_from_toml``;
   - the documentation build does not write ``docs/Syspilot Ontology/ontology.md``;
     it is a tracked, hand-maintained page beside ``ontology.toml``, like the
     Example Ontology's, with the type catalogue and a Mermaid link diagram
     whose nodes are the configured types and whose edges are written in the
     page, because ``[[needs.extra_links]]`` does not name endpoint types and
     Syspilot defines no type-pair rule; ``ontology.toml`` carries no diagram
     metadata and ``.gitignore`` does not exclude the page;
   - an installed project's ``ontology.md`` is hand-written prose seeded from
     the Example Ontology; and
   - Syspilot's repository tracks no file under ``.syspilot/`` and holds no
     ontology there, because that folder is untracked local state: in an
     installed project the baseline and Setup records, and in a working
     checkout the statistics records.

.. vc:: Syspilot binds its ontology in the specification tree
   :id: SYSP_VC_ONTOLOGY_LOCATION_1
   :status: approved
   :verifies: SYSP_REQ_ONTOLOGY_LOCATION

   The strict documentation build passes with ``needs_from_toml`` naming
   ``docs/Syspilot Ontology/ontology.toml``, and no tracked file remains at
   ``.syspilot/ontology.toml`` or ``docs/ontology-reference.md``.

.. vc:: The tracked ontology page follows the ontology
   :id: SYSP_VC_ONTOLOGY_LOCATION_2
   :status: approved
   :verifies: SYSP_REQ_ONTOLOGY_LOCATION

   ``docs/Syspilot Ontology/ontology.md`` is tracked, is not ignored, lists
   every configured Need type and every configured link of
   ``docs/Syspilot Ontology/ontology.toml``, and a strict build leaves it
   unchanged; ``docs/conf.py`` contains no hook that writes it.

.. vc:: The link diagram matches the ontology and the graph
   :id: SYSP_VC_ONTOLOGY_LOCATION_3
   :status: approved
   :verifies: SYSP_REQ_ONTOLOGY_LOCATION

   The page's Mermaid diagram has one node per configured type; every edge
   names a configured link and configured types, every configured link has an
   edge, and the edges equal the (type, link, type) triples observed in the
   built Needs data. ``ontology.toml`` holds no ``[[syspilot.diagram_edges]]``.

.. req:: Mandatory Link Obligations Fail The Strict Build
   :id: SYSP_REQ_ONTOLOGY_LINK_OBLIGATIONS
   :status: approved
   :implements: SYSP_US_ONTOLOGY_MANAGEMENT

   The strict documentation build of Syspilot's own documentation and of a
   project seeded with the Example Ontology shall fail, naming the offending
   Need and the missing link, when a Need lacks one of these links:

   - a ``story`` has an incoming ``validates`` from an ``ac`` and an incoming
     ``implements`` from a ``req``;
   - a ``req`` has an incoming ``verifies`` from a ``vc`` and an outgoing
     ``implements`` to a ``story``; and
   - a ``design`` (Example Ontology only) has an incoming ``verifies`` from a
     ``vc`` and an outgoing ``details`` to a ``req``.

   ``doc`` to ``req`` via ``includes`` and ``req`` to ``req`` via ``specializes``
   stay optional. The obligations apply to the Syspilot ontology and the
   Example Ontology; an existing project ontology is user-owned and gains no
   obligation from installing Syspilot. The checks establish that the minimum
   links exist with the named endpoint types, not that they are semantically
   right.

.. vc:: A model lacking a mandatory link fails the strict build
   :id: SYSP_VC_ONTOLOGY_LINK_OBLIGATIONS_1
   :status: approved
   :verifies: SYSP_REQ_ONTOLOGY_LINK_OBLIGATIONS

   For each obligation, a model that omits the link fails the strict build
   with a message naming the Need and the link; the same model with the link
   present builds with zero warnings.

.. vc:: Existing intended builds satisfy the obligations
   :id: SYSP_VC_ONTOLOGY_LINK_OBLIGATIONS_2
   :status: approved
   :verifies: SYSP_REQ_ONTOLOGY_LINK_OBLIGATIONS

   Syspilot's own documentation and the seeded Example Ontology project build
   with zero warnings, and a project with its own ontology gains no obligation.
