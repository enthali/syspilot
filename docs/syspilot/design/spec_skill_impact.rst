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

   **Tool:** ``.github/skills/syspilot.impact-python/scripts/get_need_links.py``

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

   Two locations exist — product source and installed runtime:

   ::

      syspilot/skills/syspilot.impact-python/   ← product source (distributed, versioned)
      ├── SKILL.md               # YAML frontmatter + instructions
      └── scripts/               # Named subdirectory for implementation scripts
          └── get_need_links.py  # Python implementation (skill-owned artifact)

      .github/skills/syspilot.impact-python/    ← installed runtime (what agents use)
      ├── SKILL.md
      └── scripts/
          └── get_need_links.py

   ``syspilot/skills/`` is the product source for distribution and versioning.
   ``.github/skills/`` is the installed instance — the only path visible to
   Copilot agents at runtime. Agents SHALL reference ``.github/skills/`` paths;
   the product source path is invisible to them.

   A skill is self-contained: all its artifacts (SKILL.md and associated scripts)
   reside in the skill folder. Scripts SHALL be placed in a named subdirectory
   (e.g. ``scripts/``), not directly at the skill root. Replacing the folder is
   the complete swap operation.

   **Change Process Scope:**

   The change process (Design Agent, Implement Agent) operates exclusively on
   ``syspilot/`` and ``docs/``. The ``.github/`` directory holds the **installed
   instance** of syspilot and is exclusively maintained by the Setup Agent.
   Change agents SHALL NOT modify any files under ``.github/``.

   The installed instance (maintained by Setup Agent only) is what agents
   read at runtime::

      .github/skills/syspilot.impact-python/    ← installed runtime (agents read this)
      ├── SKILL.md
      └── scripts/
          └── get_need_links.py

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

   1. Create a new skill folder (e.g. ``syspilot.impact-graphql/``) under
      ``syspilot/skills/``, with ``SKILL.md`` in the root and scripts in a
      named subdirectory (e.g. ``scripts/``)
   2. Provide the same capability: query by ID, depth, direction
   3. Return structured output (JSON or equivalent)
   4. Update the skill ``description`` so Copilot discovers it
   5. Run Setup Agent to install the new skill to
      ``.github/skills/syspilot.impact-graphql/scripts/`` — that is the path
      agents will invoke at runtime

   No agent code changes required — agents discover skills by description.
   The installed path (``.github/skills/<name>/scripts/``) is the runtime
   entry point; the product source (``syspilot/skills/``) is invisible to agents.


.. spec:: Impact Skill Group Membership
   :id: SYSP_SPEC_SKILL_IMPACT_GROUP
   :status: draft
   :tags: agent-v2, skill, impact, architecture
   :links: SYSP_REQ_SKILL_IMPACT_GROUP; SYSP_SPEC_SKILL_ARCH_FRONTMATTER

   **Definition:**

   The impact-python skill SHALL carry the following frontmatter field:

   .. code-block:: yaml

      group: impact

   **Mutual Exclusion:** The Setup Agent enforces that at most one skill
   with ``group: impact`` is installed. If a new variant (e.g.
   ``syspilot.impact-ubcode``) is installed, the previous one is removed.

   **Default Variant:** ``syspilot.impact-python`` is the default. It is
   installed by the Setup Agent unless an alternative is explicitly
   configured.

   **DEFINITIONS:** The ``impact`` group does not use DEFINITIONS.
   The interface is fixed (Need ID + query options → dependency tree);
   no project-specific configuration is required.
