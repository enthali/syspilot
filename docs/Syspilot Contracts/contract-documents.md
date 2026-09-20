# Contract Documents

A Contract Document is the durable, shared state of a process with a checkable end state. Its fields define what must become true; actors decide how to produce that result. Messages draw attention to the document but do not replace it.

Each process defines its canonical Contract Document template, applicability, artifact types, ownership, completion evidence, and closure conditions. A concrete process instance uses a tailored copy of that template.

## Process Definition

Every process declares:

- the positive condition under which the process applies;
- the location of its canonical template and concrete instances;
- required and tailorable artifact types;
- one owner and explicit completion evidence for every artifact type;
- process gates recorded alongside artifacts, each with exactly one owner who alone may set it;
- initial responsibility and the actor responsible for closure;
- checkable closure conditions.

Open included artifacts determine which owner needs to act. The order in which independent artifacts are completed is not prescribed by the Contract Document.

## State, Not Event Log

A Contract Document contains the currently valid state and the durable outcome. When responsibility, assumptions, blockers, or findings change, their current fields are replaced. Resolved intermediate states do not accumulate in the document; version control preserves their history for retrospective inspection.

Evidence demonstrates the outcome through inspectable artifacts, verification results, and approvals. It does not attempt to reconstruct an actor's internal reasoning or every interaction that produced the result.

## Ownership And Responsibility

Ownership is durable authority over an artifact type and its content. Responsibility is the temporary duty to maintain the handed-off Contract Document instance. Ownership does not imply exclusive write access to the Contract Document, and responsibility does not transfer authority over another owner's content.

- The process owner owns the process definition and canonical template.
- Each included artifact has exactly one owner who judges its content complete.
- Each process gate has exactly one owner, and only that owner may set it.
- The currently responsible actor keeps the document state and owned work current.
- Before a handoff, the currently responsible actor commits the completed owned artifact and current Contract Document state as one consistent version-controlled state.
- The actor then transfers responsibility to the owner of an included artifact that can progress from that state. The handoff replaces the Contract Document's current responsibility with the receiving actor.
- The actor responsible for closure receives the whole-document responsibility before closing the instance.

## Tailoring

A process describes each tailoring option at the field, row, or section of its canonical Contract template where the choice is made, together with the reason to record and the edit or delete instruction to follow. A concrete instance follows those local instructions and includes the artifacts needed to satisfy its process contract.

Tailoring changes the document shape, not the meaning of an included artifact's completion evidence.

## Contract Composition

One Contract Document may carry multiple goals and observable outcomes only when they share one responsibility, release, validation, and integration boundary.
