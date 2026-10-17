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
   :status: approved
   :priority: mandatory
   :tags: agent-v2, meta, architecture, frontmatter
   :links: SYSP_US_AGENT_ARCH, SYSP_US_HARNESS_PORTABILITY

   **Description:**
   Every agent SHALL have YAML **Agent Frontmatter** defining its technical configuration.
   The source frontmatter specifies how VS Code Copilot discovers, categorizes,
   and constrains the agent. A deterministic harness adapter MAY transform
   frontmatter fields required by another harness while preserving the agent's
   Soul, Duties, and Workflow body unchanged.

   **Rationale:**
   The Frontmatter is the machine-readable contract between an agent and its
   harness runtime. It determines discoverability and invocation mode.
   Frontmatter deliberately does NOT prescribe a ``tools:`` list: the VS Code custom-agent
   tool picker has proven unstable in practice, silently rewriting or dropping
   enumerated tool lists independent of any syspilot action. Prescribing an
   exact list in spec fights a mechanism syspilot does not control. Agents
   instead inherit whichever tools are enabled on the user's default VS Code
   agent — one place for the user to manage, no drift to maintain in specs.

   **Acceptance Criteria:**

   * AC-1: Every agent definition contains a YAML frontmatter block (``---`` delimited)
   * AC-2: Frontmatter includes a ``description`` field (string)
   * AC-3: Every source agent declares no ``tools:`` field — the agent inherits
     enabled tools or receives only harness-required deterministic capability
     mapping during adaptation
   * AC-4: Frontmatter includes a ``user-invocable`` field (boolean)
   * AC-5: Setup declares no Installer subagent target; installation control
     flow uses direct deterministic runtime execution
   * AC-6: Frontmatter may include a ``handover`` field (string, optional)
   * AC-7: No agent requires session-identity frontmatter for installation
   * AC-8: Manager and Engineer invocation visibility follows the source role
     and the selected harness's native representation
   * AC-9: Setup and the optional Installer documentation surface carry no
     bootstrap or session-actor identity
   * AC-10: Setup has execution capability but no ``agent/runSubagent`` or
     equivalent Installer-agent dependency
   * AC-11: Given a harness other than VS Code Copilot Chat, When an agent
     is installed there, Then only the frontmatter/structural adapter
     differs — the agent's Soul, Duties, and Workflow content is unchanged
   * AC-12: Given Claude Code is selected, When agents are installed, Then
         the harness exposes native, discoverable Manager and Engineer roles
         and records independent production evidence for that harness. Given
         Qoder is selected, When agents are installed, Then the harness
         receives the staged, checksummed package archive as its
         experimental-tier evidence; live native discoverability for Qoder
         is deferred future scope and is not required for this change.
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

   Because VS Code detects any ``.md`` file placed in ``.github/agents/`` as a
   selectable custom agent, every tailoring file SHALL begin with YAML
   frontmatter declaring ``user-invocable: false`` and
   ``disable-model-invocation: true``, so it is colocated with its agent for
   the Installer's orphan-cleanup exemption without appearing in the agent
   picker or being invocable as a subagent.

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
