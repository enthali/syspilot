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
     and outcome of a process instance rather than an event log, with exactly
     one bounded exception a process may declare: an append-only Handover log
     that records each responsibility transition as one line, explains
     transitions without replacing the header, and accumulates no other
     resolved intermediate state;
   - how inspectable artifacts, verification results, and approvals demonstrate
     the current outcome;
   - the distinction between durable artifact ownership and temporary
     responsibility for the Contract Document instance, including a committed
     consistent state before responsibility transfers to an owner whose
     included artifact can progress;
   - that a concrete instance states each included artifact's owner once, in
     its artifact table, with no second statement of ownership in section
     headings or process prose;
   - that a widening of the approved intent returns the intent to ``draft``
     until it is approved again, and that each owner whose terminal artifact
     the wider intent may affect reopens it or records why its evidence still
     holds;
   - shared rules that every Contract kind carries in its canonical template,
     including a kind added later: a Handover log with date as ``YYYY-MM-DD`` and
     time as ``HH:MM`` in 24-hour local time, both taken from the system clock,
     and a handover to the next actor that follows from the logical flow
     of the Contract, the scope-change rule, the single statement of artifact
     ownership, the presentation of the Contract to the User in the step that
     asks for a User-owned gate, and the receiving actor's refresh before it
     acknowledges, where a kind whose structure differs carries a rule in the
     corresponding form;
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
   individual process that uses it. Confirm that the one declared exception to
   the state-not-log rule is bounded to a single append-only Handover log,
   that the header's `Current responsibility` field stays authoritative over
   it, and that findings, blockers, and assumptions remain subject to the
   replace-in-place rule. Confirm that an instance names each artifact's owner
   only in its artifact table, and that a widened intent returns to ``draft``
   and triggers an owner reassessment of terminal artifacts. Confirm that the
   method lists the five shared rules once, that every process and example the
   registry lists carries each of them in its template, and that a Contract
   kind lacking a shared rule is detectable by a requirement test over the
   registry's listed kinds.