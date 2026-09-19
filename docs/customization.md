# Customizing Syspilot

Good customization teaches Syspilot about your project. Risky customization
quietly forks the product and leaves the next update holding a tiny fire
extinguisher.

The useful question is not "Which file can I edit?" It is "How does this project
work, what does it know, what must it explain, and which specialists does it
need?"

## Four Levels of Project Customization

### 1. Define Project Contracts

Contracts are the main way a project customizes actor behavior. A project can
define Contract X for one outcome and Contract Y for another, each with its own
applicability, artifacts, owners, evidence, operation mode, and closure
conditions.

Tell the actors which Contract is active and the document supplies the shared
state and work agreement. The same base actors can therefore behave differently
in different projects without forking their public roles. A Contract coordinates
declared authority; it does not silently grant an actor ownership or expertise
that the project has never assigned.

### 2. Design the Project Ontology

The ontology defines what the project can trace: artifact types, statuses,
relationships, and structural rules. Syspilot currently realizes its own
ontology with Sphinx-Needs and `.syspilot/ontology.toml`. This is the currently
supported realization.

The file separates Sphinx-Needs configuration under `[needs]` from Syspilot
metadata under `[syspilot]`. It defines current Need types, statuses, options,
typed relationships, and status transitions. It does not assign artifacts to
actors: the applicable Contract declares ownership, Current responsibility,
decisions, and evidence for each change.

This is the one level worth slowing down for. The ontology decides what the
project is able to say about its artifacts, including the ones already written.
Changing it is never a local edit — it reaches backwards through everything the
project has recorded so far.

Treat ontology editing as technical Contract work. Preserve unrelated project
content, change only schema surfaces represented by the current file, and run
the strict documentation and schema build afterward. Resolve every ontology
warning before completing the artifact. Pristine Setup preserves an existing
ontology or installs the baseline when none exists; it does not evaluate or
redesign that ontology. At handoff, the Project Manager explains the selected
ontology's artifact types, statuses, and relationships and asks the User whether
it fits. Acceptance continues normal intake without an ontology Change. A
requested adjustment starts a normal Change before modification, with the
Ontology skill used only as technical guidance inside that Change.

A project can model different elements within this realization. Backend
neutrality is an intended direction, but another backend is not currently a
supported Syspilot capability; a future Change must establish and verify it.
Whatever the realization, actors need explicit relationships and a validated
model instead of reconstructing structure from prose and search results.

### 3. Build the Documentation Matrix

Each project decides which independently maintained user-facing documents it
needs. In the current Sphinx-Needs implementation, one `doc` Need represents
each surface, `realized_by` points to the readable document, and `includes`
declares the requirements that document contains in user-oriented form.

That collection is the project's documentation matrix. When a requirement
changes, incoming `included_in` links expose the guides that deserve an impact
review. The Technical Writer can establish the same pattern in a customer
project without putting Needs markup into the user-facing prose.

A document that no requirement points at is a document nobody thinks of when the
truth underneath it moves. That is how guides quietly go stale while everyone
assumes somebody is watching them.

### 4. Add Specialist Actors

The eight persistent Syspilot actors are a reusable base roster, not a closed
cast. Add a project-owned specialist Actor when work needs durable expertise,
authority, memory, and a perspective that none of the base roles should pretend
to have.

For example, a Test Hardware Actor could own safe operation of a rig and the
evidence it produces. Project Contracts can then include that artifact and
owner like any other. Keep the role concise, connect it to the actor kernel and
process registry, and make its ownership boundaries explicit.

## Put Knowledge in the Right Place

Once the four structural levels are in place, local memory and skills decide how
actors work inside them.

| Kind of knowledge | Best home |
|---|---|
| A durable fact one actor needs | That actor's `.jarvis/actors/<name>/context.md` |
| Shared product behavior | An approved specification and its realized artifact |
| Process state for one piece of work | The active Contract Document |
| Tool-specific operating procedure | A skill or instruction owned as a product artifact |
| A hypothesis or observed pattern | Research or a Field Note until it earns stronger status |

Actor memory is not a diary. Keep decisions, findings, constraints, and next
actions that will still matter in a future session. Replace stale entries and
let Git preserve the history.

Whether that memory is versioned with the project or kept private is a project
decision, not a default. Setup resolves it with you during installation, because
the answer determines who gets to read an actor's working notes later.

### Prefer Memory over Persona Forks

An actor's public role should stay lean and reusable. Project-specific facts
belong in local actor memory, linked back to the public role and applicable
process. That gives the actor continuity without duplicating its entire
definition.

Do not edit another actor's memory. Read it for context if needed, then message
the owner when you need action, clarification, or a decision.

### Skills Carry Tool-Specific Behavior

Actors describe stable responsibility. Skills bind that responsibility to a
tool or environment. When a different tool needs a different procedure, prefer
a focused skill variant over a second almost-identical actor.

Changes to shared product skills or base roles are product changes. Changes to
a customer's Contracts, ontology, documentation matrix, or specialist Actors
are project changes. Run either through the applicable project Contract so
ownership, impact, and update behavior stay visible.

The distinction is not paperwork. It decides who has to agree before the change
lands, and whether the next update will quietly take it away again.

## Build a Learning Organization, Not a Memory Heap

Syspilot can improve through two complementary loops:

1. **Explicit learning:** A durable lesson is reviewed and placed in the actor
   memory, skill, process, or specification that should change future behavior.
2. **Organizational learning:** Repeated actor interactions expose structural
   gaps. A missing owner, recurring clarification, or useful new role becomes a
   candidate product change.

The Field Notes provide evidence that these patterns have appeared in practice.
They are valuable precisely because they show the system in the field. They are
not automatically current architecture, though. Before promoting an insight,
check it against today's actor model and make the authority transition explicit.

## A Small Customization Checklist

Before changing anything, ask:

- Is this project knowledge, process state, or product behavior?
- Does the project need a new Contract, ontology element, document surface, or
  specialist Actor?
- Who owns it?
- Will it still matter in two weeks?
- Could an update overwrite this location?
- Does another actor need to review the factual claim?
- Should this be a local memory update or a proper Change?

That short pause prevents most customization debt. For installation and update
boundaries, continue with [Operations](operations.md).