Contract Handling
=================

.. req:: Contract Responsibility Handling
   :id: SYSP_REQ_CONTRACT_HANDLING
   :status: approved
   :implements: SYSP_US_CONTRACT_DOCUMENTS
   :specializes: SYSP_REQ_CONTRACT_DOCUMENTS
   :realized_by: .github/instructions/syspilot.contract-handling.instructions.md

   Every actor working with a Contract Document shall receive one concise,
   workspace-shared instruction that:

   - treats ``Current responsibility`` as the temporary authority to maintain
     the Contract instance without changing durable artifact ownership;
   - after completing its work, selects the next logical included artifact
     owner whose work can progress the Contract;
   - updates Contract status, artifact evidence, and ``Current
     responsibility``, then commits the Contract and related artifacts as one
     consistent state before notifying the receiving owner through ``SEND``,
     intentionally prioritizing single-writer, consistent Contract state over
     uninterrupted handoff communication and accepting the resulting brief
     notification gap;
   - identifies the Contract path, committed state, completed outcome, and
     remaining work in the handoff notification without redefining the Actor
     Kernel's messaging transport;
   - allows every actor to request advice or review from another actor at any
     time without transferring ``Current responsibility``; during that
     consultation, the consulting actor remains read-only with respect to the
     Contract and versioned work artifacts and returns only advice or findings;
   - does not transfer ``Current responsibility`` for questions or escalation;
     and
   - records an actionable blocker and escalates when no included artifact
     owner can progress the Contract.

.. vc:: Contract responsibility produces a committed direct handoff
   :id: SYSP_VC_CONTRACT_HANDLING_1
   :status: approved
   :verifies: SYSP_REQ_CONTRACT_HANDLING

    Inspect the workspace-shared Contract-handling instruction and exercise a completed handoff, a consultation, and a blocked Contract. Confirm that the completed handoff updates evidence, status, and ``Current responsibility`` in one committed state before ``SEND`` notifies the next logical owner; the deliberate notification gap preserves single-writer, consistent Contract state; consultation is available between any actors without transferring responsibility or allowing the consulting actor to modify the Contract or versioned work artifacts; and an unprogressable Contract records and escalates its blocker.