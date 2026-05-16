Skill: Impact Analysis Requirements
====================================

Requirements for the impact analysis skill.


.. req:: Impact Analysis Query
   :id: SYSP_REQ_SKILL_IMPACT_QUERY
   :status: draft
   :priority: mandatory
   :tags: agent-v2, skill, impact, traceability
   :links: SYSP_US_SKILL_IMPACT

   **Description:**
   The impact analysis skill SHALL provide dependency tree queries for
   sphinx-needs elements with configurable depth and direction.

   **Rationale:**
   Before analyzing a change, agents need to know which specification elements
   are potentially affected. The skill traverses the sphinx-needs link graph
   to produce a complete candidate list, eliminating manual search.

   **Acceptance Criteria:**

   * AC-1: Skill accepts a Need ID and returns all linked elements
   * AC-2: Depth of traversal is configurable (default: 2)
   * AC-3: Direction is configurable: ``in`` (incoming links), ``out`` (outgoing), or ``both``
   * AC-4: Output includes element ID, type, title, and status
   * AC-5: A flat mode returns just the list of IDs for easy processing


.. req:: Impact Analysis Exchangeability
   :id: SYSP_REQ_SKILL_IMPACT_EXCHANGE
   :status: draft
   :priority: mandatory
   :tags: agent-v2, skill, impact, architecture
   :links: SYSP_US_SKILL_IMPACT

   **Description:**
   The impact analysis skill SHALL be exchangeable without changing agent
   workflows. A different implementation (e.g. ubCode-based) can replace
   the Python-based skill while agents continue to use the same process.

   **Rationale:**
   Agents define stable processes; skills define exchangeable tool bindings.
   The System Designer's workflow (identify → propose → discuss → write) does
   not change when the underlying impact analysis tool changes.

   **Acceptance Criteria:**

   * AC-1: The skill interface (input: Need ID + options, output: dependency tree) is stable
   * AC-2: Agent workflow documents reference "impact analysis skill" generically, not a specific tool
   * AC-3: Swapping the skill requires only replacing the skill folder, not modifying agent definitions
   * AC-4: A skill SHALL be self-contained — all its artifacts (SKILL.md and associated scripts)
     SHALL reside in the skill folder, so that replacing the folder is the complete swap operation.
     Scripts SHALL be placed in a named subdirectory (e.g. ``scripts/``), not directly at the
     skill root
   * AC-5: The change process (Design Agent, Implement Agent) SHALL operate exclusively on the
     ``syspilot/`` and ``docs/`` directories. The ``.github/`` directory is the installed instance
     of syspilot and SHALL be maintained exclusively by the Setup Agent


.. req:: Impact Skill Group Membership
   :id: SYSP_REQ_SKILL_IMPACT_GROUP
   :status: draft
   :priority: mandatory
   :tags: agent-v2, skill, impact, architecture
   :links: SYSP_US_SKILL_IMPACT

   **Description:**
   The impact analysis skill SHALL declare ``group: impact`` in its YAML
   frontmatter. Only one skill with ``group: impact`` may be installed at
   a time (mutual exclusion). The Python-based variant
   ``syspilot.impact-python`` is the default installed variant.

   **Rationale:**
   Group membership enables substitutability — a future variant (e.g.
   ``syspilot.impact-ubcode``) can replace the Python implementation
   while agents continue to use the same impact analysis interface.

   **Acceptance Criteria:**

   * AC-1: The impact-python skill frontmatter contains ``group: impact``
   * AC-2: At most one skill with ``group: impact`` is installed at any time
   * AC-3: ``syspilot.impact-python`` is the default when no alternative is configured
   * AC-4: The impact group does not require DEFINITIONS entries — the interface is
     fixed (Need ID + options → dependency tree), not project-configurable
