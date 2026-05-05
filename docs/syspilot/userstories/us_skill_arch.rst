Skill Architecture
==================

Meta-level definition of the Skill structure and its exchangeability model.


.. story:: Skill Architecture
   :id: SYSP_US_SKILL_ARCH
   :status: draft
   :priority: mandatory
   :tags: agent-v2, skill, architecture
   :links: SYSP_US_AGENT_ARCH

   **As a** syspilot user,
   **I want** a clean, consistent Skill structure where every Skill
   carries the LLM instructions needed to perform a capability and may
   optionally be exchangeable via a group,
   **so that** Skills are predictable to author, easy to consume by Agents,
   and replaceable without changing the Agent.

   **Context:**

   A Skill is a self-contained, LLM-facing instruction unit. It packages
   the *how* of a capability — the rules, commands, and edge cases — so
   that an Agent can stay generic. Agents say *what* they want
   (``invoke``, ``delegate to``); Skills say *how* it is done.

   Skills follow a consistent inner structure analogous to (but simpler
   than) the Agent Soul/Duties/Workflow model. A Skill has no identity
   ("Soul") and no list of independent tasks ("Duties") — a Skill is a
   tool that gets called. What it has:

   * **Frontmatter** — machine-readable metadata: ``name``, ``description``,
     and (optional) ``group``, ``tools``, ``triggers``
   * **Instructions** — the LLM-facing body: how to perform the capability,
     what tools to use, what the expected outcome is
   * **Rules** — hard constraints, edge cases, and explicit "don'ts"

   Two further properties are *optional*:

   * **Group membership** — a Skill MAY declare a ``group:`` field if it is
     part of an exchangeable family (e.g. orchestration variants). Without
     a group, a Skill is standalone and not exchanged at runtime.
   * **DEFINITIONS implementation** — a Skill that belongs to a group MAY
     implement the DEFINITIONS of that group (see ``SYSP_US_DOC_CONVENTIONS``
     and ``SYSP_REQ_SKILL_DEFINITIONS``).

   Standalone Skills (no group, no DEFINITIONS) are valid and common
   today — e.g. ``syspilot.impact-python``, ``syspilot.branching``,
   ``syspilot.ask-questions``.

   **Acceptance Criteria — Inner Structure (mandatory for every Skill):**

   1. Given any Skill, When I read it, Then it has a Frontmatter block
      with at least ``name`` and ``description``
   2. Given any Skill, When I read it, Then it has an Instructions section
      that tells the LLM how to perform the capability
   3. Given any Skill, When I read it, Then it has a Rules section listing
      hard constraints (or explicitly states "no special rules")
   4. Given any Skill, When I read its Frontmatter, Then ``group`` is
      either present (group member) or absent (standalone)

   **Acceptance Criteria — Group + DEFINITIONS (optional):**

   5. Given a Skill declares a ``group``, When another Skill of the same
      group is installed, Then only one of them may be active at a time
      (Mutual Exclusion enforced by the Setup Agent)
   6. Given a Skill declares a ``group`` and that group has DEFINITIONS,
      When the Skill is installed, Then it implements every DEFINITION of
      its group's contract
   7. Given a Skill is removed and replaced by another Skill of the same
      group, Then the Agent that uses the group continues to function
      without modification
