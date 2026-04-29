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
     SHALL reside in the skill folder, so that replacing the folder is the complete swap operation
