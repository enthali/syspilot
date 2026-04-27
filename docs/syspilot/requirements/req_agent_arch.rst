Agent Architecture Requirements
================================

Meta-level requirements defining the Soul/Duties/Workflow structure.


.. req:: Agent Soul Definition
   :id: SYSP_REQ_AGENT_ARCH_SOUL
   :status: draft
   :priority: mandatory
   :tags: agent-v2, meta, architecture, soul
   :links: SYSP_US_AGENT_ARCH

   **Description:**
   Every syspilot agent SHALL have a **Soul** section that defines the agent's
   immutable identity, character, and perspective.

   **Rationale:**
   The Soul anchors an agent's behavior. It defines what the agent cares about
   and how it approaches problems. Customers cannot modify the Soul — it is the
   stable foundation that ensures consistent agent behavior across projects.

   **Acceptance Criteria:**

   * AC-1: Every agent definition contains a Soul section
   * AC-2: The Soul section defines character traits and perspective
   * AC-3: The Soul section is marked as immutable (not customer-customizable)
   * AC-4: Removing or modifying the Soul is a breaking change


.. req:: Agent Duties Definition
   :id: SYSP_REQ_AGENT_ARCH_DUTIES
   :status: draft
   :priority: mandatory
   :tags: agent-v2, meta, architecture, duties
   :links: SYSP_US_AGENT_ARCH

   **Description:**
   Every syspilot agent SHALL have a **Duties** section listing its individual
   tasks. Duties are customer-customizable.

   **Rationale:**
   Duties define what an agent does. Customers can add, remove, or modify
   individual duties to adapt agents to their project needs (e.g., skip
   safety checks if not required, add domain-specific validations).

   **Acceptance Criteria:**

   * AC-1: Every agent definition contains a Duties section
   * AC-2: Duties are listed as discrete, independently addressable tasks
   * AC-3: Customers can add, remove, or modify individual duties
   * AC-4: Adding or removing a duty does not affect the Soul


.. req:: Agent Workflow Definition
   :id: SYSP_REQ_AGENT_ARCH_WORKFLOW
   :status: draft
   :priority: mandatory
   :tags: agent-v2, meta, architecture, workflow
   :links: SYSP_US_AGENT_ARCH

   **Description:**
   Every syspilot agent SHALL have a **Workflow** section defining its process
   steps. Workflows are customer-customizable.

   **Rationale:**
   Workflows define the sequence of actions an agent takes. Customers can
   reorder steps, add validations, or skip steps to match their process
   (e.g., different build order, additional approval gates).

   **Acceptance Criteria:**

   * AC-1: Every agent definition contains a Workflow section
   * AC-2: Workflow steps are ordered and numbered
   * AC-3: Customers can reorder, add, or skip steps
   * AC-4: Modifying the workflow does not affect the Soul


.. req:: Agent Frontmatter Definition
   :id: SYSP_REQ_AGENT_ARCH_FRONTMATTER
   :status: approved
   :priority: mandatory
   :tags: agent-v2, meta, architecture, frontmatter
   :links: SYSP_US_AGENT_ARCH

   **Description:**
   Every agent SHALL have YAML **Agent Frontmatter** defining its technical configuration.
   The frontmatter specifies how VS Code Copilot discovers, categorizes, and
   constrains the agent.

   **Rationale:**
   Frontmatter is the machine-readable contract between an agent and the VS Code
   Copilot runtime. It determines discoverability (description), permissions (tools),
   invocation mode (user-invocable), orchestration capabilities (agents), and
   delegation targets (handover).

   **Acceptance Criteria:**

   * AC-1: Every agent definition contains a YAML frontmatter block (``---`` delimited)
   * AC-2: Frontmatter includes a ``description`` field (string)
   * AC-3: Frontmatter includes a ``tools`` field (list of permitted tool categories)
   * AC-4: Frontmatter includes a ``user-invocable`` field (boolean)
   * AC-5: Frontmatter includes an ``agents`` field (list of callable subagents)
   * AC-6: Frontmatter may include a ``handover`` field (string, optional)


.. req:: Agent Prompt File
   :id: SYSP_REQ_AGENT_ARCH_PROMPT
   :status: draft
   :priority: mandatory
   :tags: agent-v2, meta, architecture, prompt
   :links: SYSP_US_AGENT_ARCH

   **Description:**
   Every user-invocable agent SHALL have a prompt file that enables direct user
   invocation via VS Code Copilot's prompt mechanism.

   **Rationale:**
   Prompt files (``*.prompt.md``) are the user-facing entry points for agents.
   They allow users to invoke agents directly via the VS Code chat panel. Only
   user-invocable agents (managers) need prompt files — engineers are invoked
   via ``runSubagent()`` and do not have prompts.

   **Acceptance Criteria:**

   * AC-1: Every agent with ``user-invocable: true`` has a corresponding prompt file
   * AC-2: Engineers (``user-invocable: false``) do NOT have prompt files
   * AC-3: The prompt file name follows the pattern ``syspilot.<name>.prompt.md``
   * AC-4: The prompt file references the agent it belongs to
