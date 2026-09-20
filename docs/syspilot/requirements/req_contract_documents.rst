Contract Documents
==================

.. req:: Contract Document Method
   :id: SYSP_REQ_CONTRACT_DOCUMENTS
   :status: approved
   :implements: SYSP_US_CONTRACT_DOCUMENTS
   :realized_by: docs/Syspilot Contracts/contract-documents.md

   A Contract Document method shall define:

   - how a process declares applicability, canonical and concrete document
     locations, artifact types, ownership, completion evidence, initial and
     closure responsibility, and closure conditions;
   - the nature of a Contract Document as the durable, currently valid state
     and outcome of a process instance rather than an event log;
   - how inspectable artifacts, verification results, and approvals demonstrate
     the current outcome;
   - the distinction between durable artifact ownership and temporary
     responsibility for the Contract Document instance, including a committed
     consistent state before responsibility transfers to an owner whose
     included artifact can progress;
   - process gates that a Contract Document records alongside its artifacts,
     each carrying exactly one owner who alone may set it, so that an
     authorization such as a release is stated once with its owner visible;
   - that each tailoring option is described at the section of the process
     Contract template where that choice is made, so that an author meets the
     option and its editing instruction at the point of use rather than in a
     central list; and
   - that one Contract Document may carry multiple goals and observable
     outcomes only when they share one responsibility, release, validation, and
     integration boundary, which governs Contract composition rather than
     tailoring.

.. vc:: Contract Document method defines its stable contract
   :id: SYSP_VC_CONTRACT_DOCUMENTS_1
   :status: approved
   :verifies: SYSP_REQ_CONTRACT_DOCUMENTS

   Confirm that the realized method defines process structure, durable state
   and evidence, ownership and responsibility, consistent handoff commits, and
   the rule that a tailoring option is described where its choice is made.
   Confirm that it defines process gates whose owner alone may set them, states
   the multiple-goal boundary as a Contract composition invariant rather than a
   tailoring option, carries no central list of tailoring options, and defines
   no collaboration or operation mode, because mode behavior belongs to the
   individual process that uses it.