# Running a Change

A Syspilot Change starts with a useful sentence: what should become true? It
does not start by assigning five agents and hoping they agree on the destination
later.

Every modification to versioned source code or documentation uses a Change
Contract. The canonical rules live in the
[Change process](Syspilot%20Processes/change.md); this guide is the human-sized
walkthrough.

## 1. Agree on the Outcome

The Project Manager creates a feature branch and a tailored Contract at
`docs/changes/<change>.md`. The opening section records:

- the goal;
- who benefits and why;
- the scope;
- the observable outcome; and
- how and when the user wants to collaborate.

Artifact work begins after the intent and outcome are approved, unless the
written collaboration agreement explicitly delegates that authority.

## 2. Let Architecture Draw the Boundary

The first handoff goes to the Architect. The Architect decides which product
model, specifications, authority boundaries, and realized artifacts are
affected.

This is the point where a request becomes a checkable change rather than a
plausible collection of edits.

## 3. Include Only the Artifacts the Change Needs

Each artifact row says whether it is included, who owns it, what completion
looks like, and its current status. Common artifacts include architecture,
implementation, acceptance tests, user documentation, quality review, and user
validation.

The owner of each artifact decides whether that artifact is complete. Current
responsibility may move between actors, but it does not grant anyone authority
to approve somebody else's work.

User documentation is included when users need a new or changed explanation.
Incoming `included_in` links on changed requirements tell the Technical Writer
which documentation surfaces deserve an impact review.

The Impact Python CLI queries a built Need by ID and follows standard links plus
every link option declared by the active project ontology. It supports incoming,
outgoing, or combined traversal to a chosen depth, so v2 typed relationships and
customer-defined relationships work without hard-coded link names.

The result is candidate scope and traceability evidence, not an independent
scope decision. The applicable Contract records the disposition of each
candidate and remains authoritative for included artifacts, responsibility, and
scope. A failed or empty query is not evidence until its ontology, built Needs
data, and other reported prerequisites are valid.

## 4. Handoff a Consistent State

Before handing off responsibility, an actor updates the owned artifact and the
Contract, commits them as one consistent state, and then messages the next
owner. The handoff identifies the Contract path, commit, completed outcome, and
remaining work. The brief gap between commit and notification is intentional:
the committed Contract stays authoritative and has one writer throughout.

There is no universal middle sequence. Open artifacts and dependencies decide
which owner receives responsibility next. Independent artifacts may be
completed in either dependency-permitted order, and bounded consultations can
happen without a handoff, but the Contract always names exactly one currently
responsible actor.

A consultant stays read-only for the Contract and versioned work artifacts and
returns advice or findings. Asking a question or escalating a concern does not
transfer Current responsibility. When no included artifact owner can make
progress, the responsible actor records an actionable blocker and escalates
instead of inventing an undeclared owner or route.

## 5. Quality Checks the Whole Outcome

Quality records one current judgment:

- `proceed` when the evidence supports validation; or
- `blocked` with a concrete required outcome for each open issue.

When Quality can proceed, it sends that judgment and its supporting evidence
directly to the Project Manager. A forwarded summary from another actor does
not establish Quality's decision. The Project Manager can then present the
verified outcome while responsibility moves directly from Quality to the User.

Resolved issues leave the open-issues table. The Contract is a dashboard, not
an attic.

## 6. The User Validates Value

Quality can show that the work is coherent and verified. Only the user can say
whether the observable outcome delivers the intended value in a user-guided
Change. After Quality can proceed, the User owns validation responsibility. The
Project Manager supports validation by presenting the observable outcome and
recording the user's decision and evidence, without becoming the validation
owner or responsibility relay.

The User communicates that decision directly to the Project Manager. A
forwarded claim does not establish the User's decision. Responsibility remains
with the User until the direct decision is recorded, then returns to the
Project Manager only for Closure.

If the user requests changes, responsibility returns to an artifact owner who
can produce the missing outcome. In autonomous work, validation may be marked
not applicable only when the recorded agreement actually grants that authority.
Unattended is different: the decision stays pending until the user returns.

## 7. The Project Manager Closes

After validation has an explicit disposition, responsibility returns to the
Project Manager for Closure. The Contract closes only when included artifacts
have terminal evidence, Quality can proceed, blockers are gone, and integration
or publication is complete or its next authorized owner is explicit.

For a live example, read
`docs/changes/documentation-foundation.md` in the repository. Then use the
canonical template in the Change process for the next real change.