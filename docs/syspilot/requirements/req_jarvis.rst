Jarvis Inter-Agent Communication Requirements
==============================================

Requirements for the Jarvis inter-agent messaging mechanism.


.. req:: Jarvis Messaging Tool
   :id: SYSP_REQ_JARVIS_TOOL
   :status: draft
   :priority: mandatory
   :tags: agent-v2, infrastructure, jarvis
   :links: SYSP_US_JARVIS

   **Description:**
   The syspilot system SHALL provide a ``syspilot_jarvis_tools`` tool that
   enables manager agents to send structured messages to other agent sessions
   without requiring user mediation.

   **Acceptance Criteria:**

   * AC-1: A ``syspilot_jarvis_tools`` tool exists and exposes a
     ``jarvis_sendToSession`` function
   * AC-2: ``jarvis_sendToSession`` accepts a target session identifier and a
     structured message payload
   * AC-3: Messages sent via Jarvis are delivered to the target agent session
     without user relay
   * AC-4: The tool is declared in the ``tools:`` frontmatter of every agent
     that sends or receives Jarvis messages


.. req:: Jarvis Message Contract
   :id: SYSP_REQ_JARVIS_CONTRACT
   :status: draft
   :priority: mandatory
   :tags: agent-v2, infrastructure, jarvis
   :links: SYSP_US_JARVIS

   **Description:**
   Messages sent via Jarvis SHALL follow a defined payload structure so that
   receiving agents can reliably parse and act on them.

   **Acceptance Criteria:**

   * AC-1: Every Jarvis message includes a ``type`` field identifying the message
     category (e.g., ``change-complete``, ``findings-report``,
     ``merge-approval``, ``post-merge-confirmation``)
   * AC-2: Every Jarvis message includes a ``sender`` field identifying the
     originating agent
   * AC-3: Every Jarvis message includes a ``payload`` field containing the
     structured content specific to the message type
   * AC-4: The ``change-complete`` message type includes the Change Document
     path and a summary
   * AC-5: The ``post-merge-confirmation`` message type includes the merge
     commit hash and branch name


.. req:: Jarvis Agent Frontmatter Declarations
   :id: SYSP_REQ_JARVIS_FRONTMATTER
   :status: draft
   :priority: mandatory
   :tags: agent-v2, infrastructure, jarvis, frontmatter
   :links: SYSP_US_JARVIS, SYSP_REQ_AGENT_ARCH_FRONTMATTER

   **Description:**
   Every agent that sends or receives Jarvis messages SHALL declare
   ``syspilot_jarvis_tools`` in its ``tools:`` frontmatter field.

   **Acceptance Criteria:**

   * AC-1: ``syspilot.cm`` frontmatter includes ``syspilot_jarvis_tools``
     (sender: change-complete, post-merge-confirmation)
   * AC-2: ``syspilot.qm`` frontmatter includes ``syspilot_jarvis_tools``
     (sender: findings-report)
   * AC-3: ``syspilot.pm`` frontmatter includes ``syspilot_jarvis_tools``
     (receiver: all types, sender: merge-approval)
