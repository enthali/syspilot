Skill: Impact Analysis Design
=============================

Design specifications for the impact analysis skill.


.. spec:: Impact Analysis Query Interface
   :id: SYSP_SPEC_SKILL_IMPACT_QUERY
   :status: draft
   :tags: agent-v2, skill, impact, query
   :links: SYSP_REQ_SKILL_IMPACT_QUERY

   **Definition:**

   The impact analysis skill queries sphinx-needs dependency trees to discover
   affected specification elements before writing changes. It traverses
   traceability links by ID, configurable depth and direction.

   **Tool:** ``syspilot/skills/syspilot.impact-python/get_need_links.py``

   **Data Source:** ``docs/_build/html/needs.json`` (requires prior ``sphinx-build``)

   **Domain Rules:**

   1. **Search from consumer elements, not from new elements.** A newly created
      element has no incoming links. Run the query from each consumer US/REQ
      that the new element satisfies.
   2. **Use direction ``in`` for level transitions.** ``in`` = "who links to me"
      = "who implements me". REQs link to USes, SPECs link to REQs. So searching
      a US with ``--direction in`` yields its REQ candidates.
   3. **Depth 1 for level transitions, depth 2 for Level 2 cross-checks.**
      Depth 2 at Level 2 catches second-order consumers (e.g. documentation
      SPECs that aggregate workflow SPECs).
   4. **Raw output at Level 0, assessment at Level 1/2.** At Level 0 the agent
      presents candidates without verdicts. Assessment (affected / not affected)
      happens when writing the next level.


.. spec:: Impact Analysis Exchangeability
   :id: SYSP_SPEC_SKILL_IMPACT_EXCHANGE
   :status: draft
   :tags: agent-v2, skill, impact, exchange
   :links: SYSP_REQ_SKILL_IMPACT_EXCHANGE

   **Definition:**

   The impact analysis capability is packaged as a **skill** (SKILL.md), not
   hardcoded into agent workflows. This follows the architectural principle:

      *Agents = stable processes, Skills = exchangeable tool bindings*

   **Skill File Structure:**

   ::

      .github/skills/syspilot.impact-python/
      ├── SKILL.md               # YAML frontmatter + instructions
      └── get_need_links.py      # Python implementation (skill-owned artifact)

   A skill is self-contained: all its artifacts (SKILL.md and associated scripts)
   reside in the skill folder. Replacing the folder is the complete swap operation.

   **Frontmatter:**

   .. code-block:: yaml

      ---
      name: syspilot.impact-python
      description: >
        Impact analysis using sphinx-needs dependency trees.
        Discovers affected specification elements by traversing
        traceability links. USE FOR: change scoping, blast radius
        analysis, element discovery before spec writing.
      ---

   **Exchange Contract:**

   To replace the Python implementation with a different backend:

   1. Create a new skill folder (e.g. ``syspilot.impact-graphql/``) containing
      ``SKILL.md`` and any scripts or assets the new implementation requires
   2. Provide the same capability: query by ID, depth, direction
   3. Return structured output (JSON or equivalent)
   4. Update the skill ``description`` so Copilot discovers it

   No agent code changes required — agents discover skills by description,
   not by hardcoded script paths.

   **Product Copy:**

   The skill is also distributed as a product artifact at
   ``syspilot/skills/syspilot.impact-python/SKILL.md``.
