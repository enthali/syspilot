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
   Every syspilot agent SHALL have a **Duties** section that answers the
   question: *What is this agent accountable for?* Duties enumerate the
   agent's responsibilities and expected outcomes — not the steps taken to
   achieve them. Duties are customer-customizable.

   **Rationale:**
   Duties establish accountability: they define what an agent owns and is
   responsible for delivering. This is a conceptually distinct question from
   *how* the agent works. By restricting Duties to outcomes and
   responsibilities, any given behavioural item has exactly one correct
   home — either accountability (Duties) or execution sequence (Workflow) —
   eliminating structural pressure to duplicate content across both sections.

   **Acceptance Criteria:**

   * AC-1: Every agent definition contains a Duties section
   * AC-2: Duties are listed as discrete, independently addressable responsibilities or outcomes
   * AC-3: Customers can add, remove, or modify individual duties
   * AC-4: Adding or removing a duty does not affect the Soul
   * AC-5: A single behavioural item SHALL appear in exactly one of Duties or
     Workflow — never both


.. req:: Agent Workflow Definition
   :id: SYSP_REQ_AGENT_ARCH_WORKFLOW
   :status: draft
   :priority: mandatory
   :tags: agent-v2, meta, architecture, workflow
   :links: SYSP_US_AGENT_ARCH

   **Description:**
   Every syspilot agent SHALL have a **Workflow** section that answers the
   question: *How does this agent execute its work?* The Workflow defines the
   ordered sequence of execution steps the agent follows — not what the agent
   is accountable for. Workflows are customer-customizable.

   **Rationale:**
   Workflow establishes execution sequence: it describes the concrete steps an
   agent takes and in what order. This is a conceptually distinct question from
   *what* the agent is responsible for. By restricting Workflow to execution
   steps, any given behavioural item has exactly one correct home — either
   execution sequence (Workflow) or accountability (Duties) — eliminating
   structural pressure to duplicate content across both sections.

   **Acceptance Criteria:**

   * AC-1: Every agent definition contains a Workflow section
   * AC-2: Workflow steps are ordered, numbered, and describe execution actions
   * AC-3: Customers can reorder, add, or skip steps
   * AC-4: Modifying the workflow does not affect the Soul
   * AC-5: A single behavioural item SHALL appear in exactly one of Workflow or
     Duties — never both
   * AC-6: Project-specific bindings in workflow steps are governed by
     ``SYSP_REQ_AGENT_WORKFLOW_BINDING`` — see that requirement for the
     full tailoring file contract


.. req:: Agent Frontmatter Definition
   :id: SYSP_REQ_AGENT_ARCH_FRONTMATTER
   :status: draft
   :priority: mandatory
   :tags: agent-v2, meta, architecture, frontmatter
   :links: SYSP_US_AGENT_ARCH

   **Description:**
   Every agent SHALL have YAML **Agent Frontmatter** defining its technical configuration.
   The frontmatter specifies how VS Code Copilot discovers, categorizes, and
   constrains the agent. Every agent except the Setup Bootloader and the Installer
   SHALL additionally carry session-identity fields and be user-invocable, so that
   the asynchronous orchestration variant can run each agent as its own session.

   **Rationale:**
   Frontmatter is the machine-readable contract between an agent and the VS Code
   Copilot runtime. It determines discoverability (description), invocation mode
   (user-invocable), and session identity. The session-identity fields give each
   agent a stable name under which a session can be addressed; the Setup
   Bootloader and the Installer are excluded because they are the bootstrap
   layer and never run as a session. The ``agents:`` field is retained
   only on the Setup Bootloader (which lists ``syspilot.installer`` — a real
   synchronous ``runSubagent`` call outside the orchestration contract); all
   other session-capable agents omit ``agents:``. Frontmatter deliberately does
   NOT prescribe a ``tools:`` list for most agents: the VS Code custom-agent
   tool picker has proven unstable in practice, silently rewriting or dropping
   enumerated tool lists independent of any syspilot action. Prescribing an
   exact list in spec fights a mechanism syspilot does not control. Agents
   instead inherit whichever tools are enabled on the user's default VS Code
   agent — one place for the user to manage, no drift to maintain in specs.
   The sole exception is the Setup Bootloader: its one synchronous
   ``agent/runSubagent`` call to the Installer is a structural bootstrap
   mechanism, not a customization surface, so it carries an explicit,
   hardcoded ``tools:`` list.

   **Acceptance Criteria:**

   * AC-1: Every agent definition contains a YAML frontmatter block (``---`` delimited)
   * AC-2: Frontmatter includes a ``description`` field (string)
   * AC-3: Every agent except the Setup Bootloader declares no ``tools:``
     field — the agent inherits whatever tools are enabled on the user's
     default VS Code agent
   * AC-4: Frontmatter includes a ``user-invocable`` field (boolean)
   * AC-5: The Setup Bootloader MAY include an ``agents`` field listing its synchronous subagent targets (``syspilot.installer``); all other agents omit ``agents:`` — in the session model the field enforces nothing at runtime
   * AC-6: Frontmatter may include a ``handover`` field (string, optional)
   * AC-7: Every agent except the Setup Bootloader and the Installer carries session-identity frontmatter (a human-readable session name and an agent identifier)
   * AC-8: Every agent except the Setup Bootloader and the Installer declares ``user-invocable: true``
   * AC-9: The Setup Bootloader and the Installer carry no session-identity fields — they are the bootstrap layer and never run as a session
   * AC-10: The Setup Bootloader is the sole agent carrying an explicit
     ``tools:`` field; it includes ``agent/runSubagent`` (its one structural
     dependency, not shared by any other agent) alongside its other required
     tools


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


.. req:: Agent Workflow Binding Contract
   :id: SYSP_REQ_AGENT_WORKFLOW_BINDING
   :status: draft
   :priority: mandatory
   :tags: agent-v2, meta, architecture, workflow, process
   :links: SYSP_US_CUSTOM_AGENT_WORKFLOWS; SYSP_REQ_AGENT_ARCH_WORKFLOW

   **Description:**
   Every agent whose workflow may need project-specific tailoring SHALL include
   a sentence directing it to read a sibling tailoring file
   (``syspilot.<name>.tailoring.md``) stored next to the agent. The tailoring
   file may be empty (proceed generic), clarify a step, or override a step. If
   the file is missing, the agent RESPONDs to PM that tailoring is needed; PM
   reads the agent's generic workflow, interviews the user, and authors the
   tailoring file. The file is instance-only: setup ships ``*.agent.md`` and
   never ``*.tailoring.md``, so product updates never overwrite it.

   **Rationale:**
   Separating generic method (in the agent, product) from project-specific
   detail (in the tailoring file, instance) lets the same agent run across
   projects without modification. RESPOND-on-missing makes the gap
   self-diagnosing: any agent — user-facing or engineer subagent — bubbles up
   to PM, who is the one user-facing agent able to interview and author the
   file. No skill or spec hierarchy is required.

   **Acceptance Criteria:**

   * AC-1: Each customizable agent includes a sentence directing it to read ``syspilot.<name>.tailoring.md`` — 1:1 with the agent
   * AC-2: The tailoring file is instance-only and lives next to the agent; setup ships ``*.agent.md`` only and never overwrites ``*.tailoring.md``
   * AC-3: A missing tailoring file causes the agent to RESPOND to PM that tailoring is needed; PM interviews the user and authors the file — the agent does not proceed with assumptions
   * AC-4: An empty tailoring file means "nothing to tailor — proceed generic"; agents with no project-specific steps need no tailoring
   * AC-5: The generic workflow skeleton in the agent file contains zero project-specific nouns — every sentence passes the test: "would this be true, unchanged, for a different project?"
