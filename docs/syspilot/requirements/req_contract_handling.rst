Contract Handling
=================

.. req:: Contract Responsibility Handling
   :id: SYSP_REQ_CONTRACT_HANDLING
   :status: approved
   :implements: SYSP_US_CONTRACT_DOCUMENTS
   :specializes: SYSP_REQ_CONTRACT_DOCUMENTS
   :realized_by: .github/instructions/syspilot.contract-handling.instructions.md

   Every actor shall receive one concise workspace-shared instruction that:

   - treats ``Current responsibility`` as temporary Contract authority,
     preserving durable artifact ownership;
   - selects the next logical included owner able to progress the Contract;
   - commits Contract status, evidence, responsibility and owned artifacts as
     one consistent state before notification;
   - names the Contract path and the committed state in the ``HANDOFF`` message
     and nothing else, leaving outcome in the last log line and work in open rows;
   - requires, before starting received work, receiver refresh of its own
     ``context.md``, role card and
     Contract, then verification that the named commit's header names itself,
     before ``ACK``; mismatch requires escalation instead;
   - permits ``CONSULT`` and ``CONSULTRESPOND`` between any actors without
     responsibility transfer or consultation writes to Contract/versioned artifacts;
   - keeps notes and messages short, factual and direct, without recited
     evidence or instructions to the next artifact's owner; and
   - records an actionable blocker and escalates when no included owner can
     progress; questions and escalation transfer no responsibility.

   ``HANDOFF`` and ``CONSULT`` shall use the Kernel's ``SEND``;
   ``ACK`` and ``CONSULTRESPOND`` shall use ``RESPOND``. The instruction shall
   not redefine transport. Committed single-writer consistency takes priority
   over uninterrupted communication; the brief notification gap is accepted.

.. vc:: Handoff refers to an already committed consistent state
   :id: SYSP_VC_CONTRACT_HANDLING_1
   :status: approved
   :verifies: SYSP_REQ_CONTRACT_HANDLING

   A completed handoff names only the Contract path and commit; that commit
   contains the status, evidence, owned work and next responsibility.

.. vc:: Acknowledgement verifies the receiver's current authority
   :id: SYSP_VC_CONTRACT_HANDLING_2
   :status: approved
   :verifies: SYSP_REQ_CONTRACT_HANDLING

   Receiver evidence shows context, role and Contract refresh before header
   verification. A matching committed header permits ACK; a mismatch escalates.

.. vc:: Consultation returns advice without state transfer
   :id: SYSP_VC_CONTRACT_HANDLING_3
   :status: approved
   :verifies: SYSP_REQ_CONTRACT_HANDLING

   A consultation returns advice/findings without changing responsibility or
   versioned artifacts, using Kernel SEND/RESPOND rather than a new transport.

.. vc:: An unprogressable Contract escalates an actionable blocker
   :id: SYSP_VC_CONTRACT_HANDLING_4
   :status: approved
   :verifies: SYSP_REQ_CONTRACT_HANDLING

   A blocked Contract names the needed action and escalation; questions and
   escalation transfer no responsibility.

.. vc:: Handoff communication leaves detail in the Contract
   :id: SYSP_VC_CONTRACT_HANDLING_5
   :status: approved
   :verifies: SYSP_REQ_CONTRACT_HANDLING

   Notes and messages contain short facts and decisions, not repeated evidence
   or owner instructions; the last log line and open rows carry outcome and work.

.. vc:: Handoff policy accepts the notification gap
   :id: SYSP_VC_CONTRACT_HANDLING_6
   :status: approved
   :verifies: SYSP_REQ_CONTRACT_HANDLING

   The instruction explicitly prioritizes committed single-writer consistency
   over uninterrupted notification, rather than authorizing a second writer.
