# The Change Contract

A Syspilot Change starts with a useful sentence: what should become true? It does
not start by assigning eight actors and hoping they agree on the destination
later.

Every modification to versioned source code or documentation uses a Change
Contract. The canonical rules live in the
[Change process](Syspilot%20Contracts/change.md); this guide is the human-sized
walkthrough.

The sections below follow the order a Change usually takes. Usually is the
operative word. Nothing here is a fixed relay: the open artifacts decide who can
move next, and a Change that needs less simply visits fewer of these sections.

```{mermaid}
flowchart LR
    PM["Project Manager<br/>intent and outcome"] --> ARCH["Architect<br/>specification"]
    ARCH --> DEV["Developer<br/>implementation"]
    DEV --> TW["Technical Writer<br/>user documentation"]
    TW --> TEST["Tester<br/>acceptance"]
    TEST --> QA["Quality<br/>judgment"]
    QA --> USER["User<br/>validation"]
    USER --> CLOSE["Project Manager<br/>closure"]
    TW -.->|"consultation"| ARCH
```

That is one real Change, and the order its open artifacts happened to require.
A Change that touches no user-facing surface never reaches the Technical Writer;
one that needs no new specification can start at the Developer. The dashed arrow
is a consultation — it returns findings and moves no responsibility at all.

## Agree on the Outcome

The Project Manager creates the Change's feature branch from `development` and a
tailored Contract at `docs/changes/<change>.md`. The opening section records:

- the goal;
- who benefits and why;
- the scope;
- the observable outcome; and
- how and when the user wants to collaborate.

The Contract also selects one Operation Mode — user-guided, autonomous, or
unattended — agreed with the User beforehand, and keeps that mode's rule in its
own text rather than pointing elsewhere. It records the User's release exactly
once, in a `Contract release` gate that only the User may set. Artifact work
starts when that gate reads `approved`, and nothing else starts it: a settled
intent is not an authorization to begin.

## Draw the Boundary

The first handoff goes to the Architect. The Architect decides which product
model, specifications, authority boundaries, and realized artifacts are
affected.

This is the point where a request becomes a checkable change rather than a
plausible collection of edits.

## Include Only What the Change Needs

Each artifact row says whether it is included, who owns it, what completion
looks like, and its current status. Common artifacts include architecture,
implementation, acceptance tests, user documentation, quality review, user
validation, and version control.

Version control is an artifact like any other, which is what keeps the branch
out of the prose. The Project Manager owns it, its evidence is the branch name
and integration state, and a Change that needs no branch marks the row as not
included instead of inventing a placeholder.

The same table carries process gates alongside artifacts — the User's release of
the Contract is one. Each gate has exactly one owner, and only that owner may
set it. An authorization stated in a row with a visible owner cannot later be
asserted in prose by whoever happened to be holding the pen.

An optional artifact that does not apply is marked `not applicable` with a
reason, and its now-empty owner section is deleted in the same step. The row
itself says so, next to the choice, rather than in a rule somewhere else —
because the moment you are deciding is the moment you need to be told what the
decision obliges you to do. Required artifacts offer no such option. An empty
section under a heading tells a reader nothing
except that somebody may have forgotten it.

The owner of each artifact decides whether that artifact is complete. Current
responsibility may move between actors, but it never lets one actor approve
somebody else's work. Otherwise a review would measure nothing more than how
convincing the last writer was.

User documentation is included when users need a new or changed explanation.
Incoming `included_in` links on changed requirements tell the Technical Writer
which documentation surfaces deserve an impact review.

Impact Python answers the same question for the rest of the graph. It queries a
built Need by ID and follows standard links plus every link option the active
ontology declares, incoming or outgoing, to a chosen depth — so project-defined
relationships work without hard-coded names. What comes back is a list of
candidates and the evidence behind them. The Contract still decides what is in
scope, and a query that failed or returned nothing proves nothing until its
ontology, built data, and other prerequisites are valid.

## Hand Off a Consistent State

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

## Quality Checks the Whole Outcome

Quality records one current judgment:

- `proceed` when the evidence supports validation; or
- `blocked` with a concrete required outcome for each open issue.

That judgment is not a general impression. Quality starts from the objects the
Contract records as impacted and applies two named methods to them.

**Horizontal coverage** compares each impacted object with its peers of the same
type — Requirement against Requirement, Story against Story — looking for
overlap, duplicated obligation, contradiction, missing coverage, and
responsibility boundaries that collide. The peer set is a deliberate choice and
is reported: either the peers in the same document, or every peer of that type.

**Relationship analysis** walks the object's declared relationships to a chosen
depth and reports observed named links in their direction, targets that do not
resolve, and objects with no observed links in the selected neighborhood. It
cannot infer which links ought to exist, whether the graph is complete, or
whether a same-type link points to the semantically right neighbor. Reviewing
the meaning and coverage of those relationships remains a human judgment.

Both methods are read-only, and both record their scope, evidence, findings, and
limits — including what they could not check. A method that reports nothing
because its data was missing is not the same as a method that looked and found
nothing, and a reviewer has to be able to tell those two apart.

When Quality can proceed, it sends that judgment and its supporting evidence
directly to the Project Manager. A forwarded summary from another actor does
not establish Quality's decision. The Project Manager can then present the
verified outcome while responsibility moves directly from Quality to the User.

Resolved issues leave the open-issues table. The Contract is a dashboard, not
an attic.

## The User Validates Value

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
can produce the missing outcome. Validation can be marked `not applicable` only
when the User explicitly delegates it and that delegation is recorded in the
validation row itself. No Operation Mode does this on its own: autonomous
governs how actors decide within authority they already hold, and it cannot hand
over authority that belongs to the User. Unattended does not waive anything
either — the decision stays pending until the user returns.

## The Project Manager Closes

After validation has an explicit disposition, responsibility returns to the
Project Manager for Closure. The Contract closes only when included artifacts
have terminal evidence, Quality can proceed, blockers are gone, and integration
or publication is complete or its next authorized owner is explicit.

A closed Contract is worth more than a finished one. It is the record a future
reader consults when they need to know why the system looks the way it does.

The Contracts in `docs/changes/` are real instances rather than tidy examples,
which is why they stay in the repository instead of the rendered documentation.
Open one there to see the shape of actual work, then start the next change from
the canonical template in the Change process.