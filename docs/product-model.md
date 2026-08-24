# The Syspilot Product Model

Syspilot is not a collection of elaborate chat personas. It is a small system
for keeping intent, authority, implementation, and evidence connected while AI
collaborators help with the work.

This document describes Syspilot's own product model. Treat it as a worked
example of specification-driven development, not as the only structure another
project may use. Your project can define a different ontology, different
Contracts, and additional specialist Actors while keeping the same principles
of explicit intent, authority, realization, and evidence.

## Start with the Graph

The live specification has three important layers:

```text
Graph Root -> User Stories (why) -> Requirements (what)
                                      |
                                      +-> realized_by -> the file that does it
```

Acceptance criteria ask whether the right outcome was built. Verification
criteria ask whether a requirement was implemented correctly. User
documentation has its own `doc` Needs, which point to readable documents and
declare the requirements they contain in user-oriented form.

There is no separate v2 directory full of prose design specifications. The
`realized_by` link points to the actual role card, process, skill, instruction,
or code artifact that supplies the how. Less duplicate truth means less stale
truth.

## Actors Have a Public Role and Local Memory

Every actor combines four pieces:

1. The **Jarvis Actor Kernel** supplies identity, memory, messaging,
   escalation, and collaboration culture.
2. A concise **public role card** states the actor's domain and perspective.
3. The applicable **process** assigns durable ownership of artifacts.
4. The actor-owned local **`context.md`** retains only long-lived local
  knowledge. Other actors may read it as contextual evidence, but only its
  owner may modify it.

The current base roster is deliberately compact:

| Actor | Durable area of authority |
|---|---|
| Project Manager | Strategy, intake, portfolio, and Change closure |
| Architect | Architecture, specifications, and design guidance |
| Developer | Implementation and unit verification |
| Tester | Adversarial acceptance testing |
| Quality | Independent quality judgment |
| Setup | Installation and updates |
| Release | Packaging and release delivery |
| Research | Investigation and technical due diligence |
| Technical Writer | User-facing product documentation |

The [actor registry](Syspilot%20Actors/index.md) and individual role cards are
the authority for these roles. This guide explains the model; it does not get
to quietly rewrite anyone's job description. A customer project may add a
specialist Actor when its Contracts need durable expertise that the base roster
does not provide, such as operating test hardware or a laboratory system.

## Contracts Hold the Shared State

A Contract Document is the durable state of a process. It records what must
become true, which artifacts apply, who owns them, what counts as completion,
who currently holds responsibility, and how the work closes.

That distinction matters:

- **Ownership** is lasting authority over an artifact type and its content.
- **Responsibility** is the temporary duty to keep one Contract instance and
  the currently active work consistent.
- **Messaging** gets another actor's attention. It does not replace the
  Contract or silently transfer authority.

Contracts store current truth, not a transcript. When a blocker is resolved or
responsibility changes, the current field is replaced. Git already remembers
the archaeology.

Syspilot's [Change process](Syspilot%20Processes/change.md) is the canonical
Contract definition for modifying versioned artifacts. The repository file
`docs/changes/documentation-foundation.md` is a concrete instance: it records
the real decisions, ownership, reviews, and evidence behind these guides. One
defines the reusable agreement; the other shows that agreement doing actual
work.

## The Document Drives the Work

Syspilot does not prescribe one actor sequence for every situation. Included,
open artifacts determine which owner can progress next. Independent work can
happen independently; dependent work waits for the state it needs.

The result feels less like passing a baton down a fixed line and more like
maintaining a shared control panel. Everyone can see the intended outcome, the
open work, and who currently owes the next state change.

## Product and Instance Are Different Things

Product artifacts live in their canonical repository locations: role cards,
processes, specifications, skills, instructions, and code are developed where
their owning structures place them. `.github/` contains the installed instance
used to work on this project. Setup is responsible for installing the relevant
product artifacts into a customer environment without creating a second source
of truth in the product repository.

Keeping that boundary visible makes updates safer. Project knowledge belongs
in actor memory or declared project customization, not in an accidental fork
of a generated or installed product file.

Continue with [the Change workflow](change-workflow.md) to see the model in
motion, or [Customization](customization.md) to decide where local knowledge
should live.