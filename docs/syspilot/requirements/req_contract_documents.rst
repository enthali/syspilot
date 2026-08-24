Contract Documents
==================

.. req:: Contract Document Method
   :id: SYSP_REQ_CONTRACT_DOCUMENTS
   :status: approved
   :implements: SYSP_US_CONTRACT_DOCUMENTS
   :realized_by: docs/Syspilot Processes/contract-documents.md

   A Contract Document method shall define:

   - how a process declares applicability, canonical and concrete document
     locations, artifact types, ownership, completion evidence, initial and
     closure responsibility, and closure conditions;
   - the nature of a Contract Document as the durable, currently valid state
     and outcome of a process instance rather than an event log;
   - how inspectable artifacts, verification results, and approvals demonstrate
     the current outcome;
   - how the collaboration mode establishes expectations for user agreement,
     availability, questions, and assumptions;
   - the distinction between durable artifact ownership and temporary
     responsibility for the Contract Document instance, including a committed
     consistent state before responsibility transfers to an owner whose
     included artifact can progress;
   - how a concrete process instance may tailor its artifact set while
     preserving ownership and completion semantics.

.. vc:: Contract Document method defines its stable contract
   :id: SYSP_VC_CONTRACT_DOCUMENTS_1
   :status: approved
   :verifies: SYSP_REQ_CONTRACT_DOCUMENTS

   Confirm that the realized method defines process structure, durable state
   and evidence, collaboration mode, ownership and responsibility, consistent
   handoff commits, and tailoring.