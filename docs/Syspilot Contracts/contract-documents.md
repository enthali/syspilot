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

A process may declare exactly one bounded exception to this rule: a Handover log that records each responsibility transition as one append-only line. The log explains transitions; it does not replace the header. `Current responsibility` alone is authoritative, and a recipient verifies that field before acknowledging. The log accumulates no other resolved intermediate state — findings, blockers, and assumptions still follow the replace-in-place rule above.

## Ownership And Responsibility

Ownership is durable authority over an artifact type and its content. Responsibility is the temporary duty to maintain the handed-off Contract Document instance. Ownership does not imply exclusive write access to the Contract Document, and responsibility does not transfer authority over another owner's content.

- The process owner owns the process definition and canonical template.
- Each included artifact has exactly one owner who judges its content complete.
- Each process gate has exactly one owner, and only that owner may set it.
- A concrete instance states the owner of each included artifact once, in its artifact table. Section headings and process prose add no second statement of ownership, so a reader finds one owner per artifact in one place.
- When the approved intent widens after an artifact reached a terminal status, the intent returns to `draft` until it is approved again, and each owner whose terminal artifact the wider intent may affect reassesses it: the owner reopens the artifact or records in its row why the evidence still holds.
- The currently responsible actor keeps the document state and owned work current.
- Before a handoff, the currently responsible actor commits the completed owned artifact and current Contract Document state as one consistent version-controlled state.
- The actor then transfers responsibility to the owner of an included artifact that can progress from that state. The handoff replaces the Contract Document's current responsibility with the receiving actor.
- The actor responsible for closure receives the whole-document responsibility before closing the instance.

## Shared Rules Of Every Contract Kind

Every Contract kind inherits these rules, including a kind added later. A Contract kind is any process or example the registry lists other than this method. Each kind's canonical template carries the rules in its own wording where they apply, and a kind whose structure differs carries a rule in the corresponding form.

1. **Handover log.** The template carries an append-only table `Date | Time | From | To | Note`. The handing-over actor appends one line as the last act before handing over, in the same commit that changes `Current responsibility`, taking `Date` as `YYYY-MM-DD` and `Time` as `HH:MM` in 24-hour local time from the system clock at that moment. The handover goes to the next actor that follows from the logical flow of the Contract, and the header stays authoritative. A kind whose responsibility moves once carries the table too, and its single transition is its first entry.
2. **Scope change.** The template carries the scope-change rule of the previous section where the intent and the artifact rows meet.
3. **Single ownership statement.** The template names each artifact's owner once, in its owner table, and names no artifact owner in a section heading.
4. **Presenting the Contract for a User-owned gate.** In the step that asks the User to set a User-owned gate, the asking actor presents the Contract document to the User for review within that same step, because the User reviews it before deciding. Syspilot's own processes do so by opening the document in the User's editor; an adopting project names its own way.
5. **Refresh on acknowledgement.** The receiving actor re-reads its own `context.md`, its role card, and the Contract, then verifies the committed `Current responsibility` before it acknowledges. The shared Contract-handling instruction states this for every kind.

## Tailoring

A process describes each tailoring option at the field, row, or section of its canonical Contract template where the choice is made, together with the reason to record and the edit or delete instruction to follow. A concrete instance follows those local instructions and includes the artifacts needed to satisfy its process contract.

Tailoring changes the document shape, not the meaning of an included artifact's completion evidence.

## Contract Composition

One Contract Document may carry multiple goals and observable outcomes only when they share one responsibility, release, validation, and integration boundary.
