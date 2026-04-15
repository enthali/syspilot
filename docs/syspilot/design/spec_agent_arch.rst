Agent Architecture Design
=========================

Meta-level definitions of Soul, Duties, and Workflow concepts.


.. spec:: Soul Definition
   :id: SYSP_SPEC_AGENT_ARCH_SOUL
   :status: draft
   :tags: agent-v2, meta, architecture, soul
   :links: SYSP_REQ_AGENT_ARCH_SOUL

   **Definition:**

   The **Soul** is the immutable core identity of an agent. It defines:

   * **Character** — personality traits, disposition, attitude toward work
   * **Perspective** — how the agent views problems and what it prioritizes
   * **Guardrails** — what the agent will never do, hard boundaries
   * **Care** — what the agent cares about most deeply

   **Properties:**

   * Immutable across customizations — changing the Soul is a breaking change
   * Written in second person ("You are...")
   * Short (3–5 sentences maximum)
   * Defines identity, not tasks (tasks belong in Duties)

   **Example Pattern:**

   ::

      You are the **[Persona]** — [character description]. You [what you care about].
      You are [traits]. You never [guardrail].

   **File:** ``## Soul`` section in ``.agent.md``


.. spec:: Duties Definition
   :id: SYSP_SPEC_AGENT_ARCH_DUTIES
   :status: draft
   :tags: agent-v2, meta, architecture, duties
   :links: SYSP_REQ_AGENT_ARCH_DUTIES

   **Definition:**

   **Duties** are the enumerated tasks an agent can perform. They define:

   * **Task list** — discrete, independently addressable responsibilities
   * **Scope** — what falls within this agent's responsibility
   * **Boundaries** — what is explicitly NOT this agent's job

   **Properties:**

   * Customer-customizable — duties can be added, removed, or modified
   * Each duty is independently enableable/disableable
   * Duties do not define sequence (that's the Workflow)
   * Written as imperative descriptions

   **Customization Examples:**

   * Remove a duty: customer doesn't need safety checks
   * Add a duty: customer needs domain-specific validation
   * Modify a duty: customer uses different MECE criteria

   **File:** ``## Duties`` section in ``.agent.md``


.. spec:: Workflow Definition
   :id: SYSP_SPEC_AGENT_ARCH_WORKFLOW
   :status: draft
   :tags: agent-v2, meta, architecture, workflow
   :links: SYSP_REQ_AGENT_ARCH_WORKFLOW

   **Definition:**

   The **Workflow** defines the ordered process steps an agent follows. It defines:

   * **Steps** — numbered, sequential actions
   * **Inputs** — what the agent needs to start
   * **Outputs** — what the agent produces
   * **Decision points** — where the flow can branch

   **Properties:**

   * Customer-customizable — steps can be reordered, added, or skipped
   * Steps reference Duties (what to do) but add sequence (when to do it)
   * Written as numbered steps with clear inputs/outputs
   * Modifying the Workflow does not affect the Soul

   **Customization Examples:**

   * Reorder steps: different build sequence
   * Add a step: additional approval gate
   * Skip a step: no test generation needed

   **File:** ``## Workflow`` section in ``.agent.md``


.. spec:: Frontmatter Field Schema
   :id: SYSP_SPEC_AGENT_ARCH_FRONTMATTER
   :status: approved
   :tags: agent-v2, meta, architecture, frontmatter
   :links: SYSP_REQ_AGENT_ARCH_FRONTMATTER

   **Definition:**

   The agent frontmatter is a YAML block at the top of each ``.agent.md`` file,
   delimited by ``---``. It defines the following fields:

   * **description** (string, required) — One-sentence summary of the agent's
     purpose. Used by VS Code Copilot for agent discovery and selection.
   * **tools** (list of strings, required) — Permitted tool categories the agent
     can use (e.g., ``read``, ``edit``, ``search``, ``agent``, ``execute``).
   * **user-invocable** (boolean, required) — Whether users can invoke the agent
     directly via ``@syspilot.<name>``. Managers are ``true``; most engineers
     are ``false`` (invoked only as subagents).
   * **agents** (list of strings, required) — Subagents this agent can invoke
     via ``runSubagent()``. Empty list ``[]`` if the agent has no subagents.
   * **handover** (string, optional) — Target agent for handover delegation.
     Currently unused by all agents.

   **Example:**

   ::

      ---
      description: "Agent purpose summary."
      tools: [read, edit, search, execute]
      user-invocable: false
      agents: []
      ---
