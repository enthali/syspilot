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
   * Defines identity, not responsibilities or execution steps (accountability belongs in Duties; execution steps belong in Workflow)

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

   **Duties** answer the question *What is this agent accountable for?*
   They enumerate the agent's responsibilities and expected outcomes. They define:

   * **Accountability** — what the agent owns and is responsible for delivering
   * **Scope** — what falls within this agent's responsibility
   * **Boundaries** — what is explicitly NOT this agent's job

   **Properties:**

   * Every agent definition SHALL contain a Duties section
   * Customer-customizable — duties can be added, removed, or modified
   * Each duty is independently enableable/disableable
   * Adding or removing a duty does not affect the Soul
   * Written as short, unordered responsibility statements
   * **Mutual Exclusion** — A single behavioural item SHALL appear in exactly
     one of Duties or Workflow — never both. If an item describes an outcome
     or accountability, it belongs in Duties. If it describes a step in the
     execution sequence, it belongs in Workflow.

   **Customization Examples:**

   * Remove a duty: customer doesn't need safety checks
   * Add a duty: customer needs domain-specific validation
   * Modify a duty: customer uses different MECE criteria

   **File:** ``## Duties`` section in ``.agent.md``


.. spec:: Workflow Definition
   :id: SYSP_SPEC_AGENT_ARCH_WORKFLOW
   :status: draft
   :tags: agent-v2, meta, architecture, workflow
   :links: SYSP_REQ_AGENT_ARCH_WORKFLOW; SYSP_REQ_AGENT_WORKFLOW_BINDING

   **Definition:**

   The **Workflow** answers the question *How does this agent execute its work?*
   It defines the ordered sequence of execution steps the agent follows. It defines:

   * **Steps** — numbered, sequential execution actions
   * **Inputs** — what the agent needs to start
   * **Outputs** — what the agent produces
   * **Decision points** — where the flow can branch

   **Properties:**

   * Every agent definition SHALL contain a Workflow section
   * Customer-customizable — steps can be reordered, added, or skipped
   * Written as numbered steps with clear inputs/outputs
   * Modifying the Workflow does not affect the Soul
   * **Mutual Exclusion** — A single behavioural item SHALL appear in exactly
     one of Workflow or Duties — never both. If an item describes a step in
     the execution sequence, it belongs in Workflow. If it describes an outcome
     or accountability, it belongs in Duties.
   * **Tailoring File** — When a workflow step requires project-specific
     information (paths, branch names, commands, distribution targets), the
     skeleton directs the agent to read a sibling tailoring file
     (``syspilot.<name>.tailoring.md``) rather than embedding the value. The
     skeleton itself contains zero project-specific nouns. The file may be
     empty (proceed generic), clarify, or override. If missing, the agent
     RESPONDs to PM (or, if the agent *is* PM, runs its own Tailoring Workflow
     directly), who interviews the user and authors it. Because VS Code
     detects any ``.md`` file in ``.github/agents/`` as a selectable custom
     agent, every tailoring file begins with its own frontmatter block
     (``user-invocable: false``, ``disable-model-invocation: true``) so it
     never appears in the agent picker or accepts subagent invocation despite
     living next to its agent.

   * **Implementation Template** — Every customizable agent's Workflow section
     SHALL begin with a Preflight sentence of the form:

     *"Before executing, read* ``syspilot.<name>.tailoring.md`` *for any
     project-specific clarifications or overrides. If the file is missing,
     RESPOND to PM that tailoring is needed (or, if this agent is PM, run the
     Tailoring Workflow directly). If empty, proceed generic."*

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

   The **Agent Frontmatter** is a YAML block at the top of each ``.agent.md`` file,
   delimited by ``---``. It defines the following fields:

   * **description** (string, required) — One-sentence summary of the agent's
     purpose. Used by VS Code Copilot for agent discovery and selection.
   * **tools** (list of strings, optional) — Omitted from source agents. When
     omitted, the agent inherits whatever tools are enabled on the user's
     default VS Code agent; a harness adapter may emit only native capability
     metadata required for the role.
   * **user-invocable** (boolean, required) — Whether users can invoke the agent
     directly via ``@syspilot.<name>``. Every agent except the Setup Bootloader
     and the Installer is ``true``; the Bootloader and Installer are the
     bootstrap layer.
   * **agents** (list of strings, required) — Agents this agent may SEND work to.
     Empty list ``[]`` if the agent has no SEND targets.
   * **name** (string, optional) — Human-readable agent name where consumed by
     a harness; it is not an installation-time session identity.
   * **agent** (string, optional) — Agent identifier where consumed by a
     harness; the Installer does not materialize sessions or actors from it.
   * **handover** (string, optional) — Target agent for handover delegation.
     Currently unused by all agents.
   * **version** (string, optional, default: absent) — The installed syspilot
     version string (e.g. ``0.5.1``). Only ``syspilot.setup.agent.md`` uses
     this field; all other agents omit it.

   **Example (orchestrating agent):**

   ::

      ---
      description: "Agent purpose summary."
      user-invocable: true
      agents: []
      name: Project Manager
      agent: syspilot.pm
      ---

   **Constraint:** Setup declares no Installer subagent and no
   ``agent/runSubagent`` dependency. It directly executes the deterministic
   local runtime. The Installer creates no sessions or actors from frontmatter.


.. spec:: Prompt File Definition
   :id: SYSP_SPEC_AGENT_ARCH_PROMPT
   :status: draft
   :tags: agent-v2, meta, architecture, prompt
   :links: SYSP_REQ_AGENT_ARCH_PROMPT; SYSP_REQ_PM_PROMPT; SYSP_REQ_CM_PROMPT; SYSP_REQ_QM_PROMPT; SYSP_REQ_SETUP_PROMPT

   **Definition:**

   A **Prompt file** is the user-facing entry point for invoking an agent directly
   via VS Code Copilot's chat panel.

   **File format:**

   * File name: ``syspilot.<name>.prompt.md``
   * Location: ``syspilot/prompts/`` (product) or ``.github/prompts/`` (instance)
   * Minimal **Prompt Frontmatter**: ``agent: syspilot.<name>``

   **Scope:**

   * Only user-invocable agents (managers) have prompt files
   * Engineers are invoked via ``runSubagent()`` and do NOT need prompt files
   * The prompt file references the agent it belongs to via the ``agent`` field

   **Example:**

   ::

      ---
      agent: "syspilot.pm"
      ---
      [Prompt content for the Project Manager]

   **Current prompt files:**

   * ``syspilot.pm.prompt.md`` — Project Manager
   * ``syspilot.cm.prompt.md`` — Change Manager
   * ``syspilot.qm.prompt.md`` — Quality Manager
   * ``syspilot.setup.prompt.md`` — Setup Manager
