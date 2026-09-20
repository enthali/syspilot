# Contract Driven Development

Syspilot is built by separate actors — a project manager, an architect, a developer,
a tester, a quality reviewer, a release actor, a researcher and a technical writer.
Each keeps its own memory and forms its own view of the work. That separation is
deliberate: an actor that has not already convinced itself is the one most likely to
notice the thing everyone else walked past.

Separation has a price. The moment work crosses from one actor to another, everything
that was obvious to the first becomes invisible to the second. Contract Driven
Development is how Syspilot pays that price on purpose instead of discovering it
later.

## What a Contract Is

A Contract Document is one document that binds a group of actors to a single goal for
as long as that goal lasts. It writes down:

- **why the work exists** — the problem, not the solution;
- **scope** — what belongs inside the boundary, described by what it contains rather
  than by what it excludes;
- **who is involved and what they deliver** — the included artifacts, their owners,
  and the evidence that will show each one is complete;
- **who currently holds responsibility** — exactly one actor at a time;
- **verification and validation** — an independent quality judgment that the claims
  hold, and the User's confirmation that the result is what was wanted.

Two kinds are defined today. A **Change Contract** governs one bounded change to
versioned artifacts. A **Setup Contract** is bound to an exact release and governs
installing Syspilot into a project. Each process declares its own canonical template,
applicability, artifact types, ownership, and closure conditions in the
[process registry](Syspilot%20Contracts/index.md).

Releases do not yet have a process of their own. The Release actor owns packaging and
delivery, and that work currently runs under a Change Contract like any other bounded
work. A dedicated Release Contract is expected; until it exists, saying so is more
useful than implying it is already there.

They carry that content differently, and they are meant to. A Contract instance is a
tailored copy: each row offers its own choice and says what that choice obliges,
so a required artifact simply cannot be dropped and an optional one that does not
apply is marked with a reason and its empty section deleted. Every newly
introduced artifact declares exactly one owner and explicit completion evidence.
What is fixed is *what must be named*, not the shape it is named in.

## Ownership Is Per Artifact, Not Per Document

Inside a Contract, every included artifact has exactly one owner, and that owner
decides whether its content is complete. The Architect judges the specification, the
Developer judges the implementation, the Technical Writer judges the user
documentation. Nobody approves somebody else's artifact.

This matters more than it first appears. If one actor summarised everyone else's work,
that summary is where accurate statements quietly acquire inaccurate reasons. When the
actor who knows a thing is the actor who writes it down, a disagreement between two
sections stays visible instead of being smoothed away by whoever held the pen.

Current responsibility is a different thing from ownership. It is the temporary duty to
keep one Contract instance consistent, and it never transfers authority over another
owner's content. Before handing it on, the responsible actor commits its completed
artifact and the current Contract state together, then names the next owner who can
progress the work. The brief gap between commit and message is deliberate: the
committed document stays authoritative and has one writer.

Consultation stays outside that mechanism. Any actor may ask another for advice or a
factual review; the consultant remains read-only for the Contract and versioned work
artifacts and returns findings rather than edits. Questions and escalation do not move
responsibility either. When no included owner can progress, the responsible actor
records an actionable blocker and escalates it.

The boundary itself — scope, included artifacts, and the Operation Mode — is
drafted by the actor the Contract names and released by the User, in a gate that
only the User can set. Afterwards it can still change, but through an explicit
revision the User releases again, never through a quiet edit.

## How Much the User Is in the Loop

A Contract also fixes how its actors make decisions with respect to the User's
availability. It selects exactly one Operation Mode — user-guided, autonomous, or
unattended — agreed with the User before the Contract is released.

The selected mode's rule is carried in the Contract itself. The canonical
template holds all three; initialization keeps the one that was agreed and
deletes the others, so an actor reading the Contract during execution finds its
operating rule in the document already open in front of it. A link would have
been shorter. It would also have meant leaving the active Contract in order to
find out how to work inside it.

## Why a Contract Rather Than a Fixed Workflow

The obvious alternative is a standing workflow: every change goes from A to B to C,
always in that order. Syspilot tried that in v1 and moved away from it, for two
reasons.

The first is that a fixed sequence prescribes work a given change does not need. When a
rule requires a step that is plainly pointless in the case at hand, the rule does not
get followed — it gets ignored, and the habit of ignoring it spreads to the rules that
mattered.

The second is subtler. A standing workflow is itself an authority. Once it exists,
there are two documents describing who does what, and they drift apart without anyone
noticing, because nothing forces them to be read together.

So the roles were separated from the orchestration. Each
[Actor role card](Syspilot%20Actors/index.md) describes what a role durably is and may
decide. It never says when that actor participates. That is decided per goal, in the
Contract, and nowhere else.

## What a Contract Does Not Do

A Contract assigns work; it does not make the decisions inside that work. Requirements,
architecture, implementation behavior, verification verdicts, and documentation wording
stay with the actors that own them, and a Contract that tried to settle them in advance
would only be guessing.

It is also not an event log. It holds the currently valid state: when responsibility,
blockers, or findings change, the current field is replaced rather than appended to.
Git already remembers the archaeology. Completion is read from committed artifacts — a
specification diff, a test result, a documentation commit — never from the fact that a
step was expected to happen. An expected step and a finished step look identical in a
plan and nothing alike in a repository.

## The Realization Boundary

Contract Driven Development and the ontology concept are not inherently tied to any one
toolchain. Syspilot's current realization is Sphinx with Sphinx-Needs, and that is the
only supported one today. Backend neutrality is an intended direction that a future
Change must establish and verify; until then, treat the reference stack as the
supported path rather than an incidental detail.

## Where the Pieces Live

| | |
|---|---|
| The roles | [docs/Syspilot Actors/](Syspilot%20Actors/index.md) |
| The processes and their canonical templates | [docs/Syspilot Contracts/](Syspilot%20Contracts/index.md) |
| What a Contract Document must contain | [Contract Documents](Syspilot%20Contracts/contract-documents.md) |
| One bounded change | [The Change process](Syspilot%20Contracts/change.md) |
| Installing Syspilot into a project | [Pristine Setup](Syspilot%20Contracts/setup.md) |
| The method in motion | [The Change Contract](change-contract.md) |
