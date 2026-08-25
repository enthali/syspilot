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
applicability, artifacts, owners, evidence, collaboration agreement, and
closure conditions.

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

### 4. Add Specialist Actors

The eight persistent Syspilot actors are a reusable base roster, not a closed
cast. Add a
project-owned specialist Actor when work needs durable expertise, authority,
memory, and a perspective that none of the base roles should pretend to have.

For example, a Test Hardware Actor could own safe operation of a rig and the
evidence it produces. Project Contracts can then include that artifact and
owner like any other. Keep the role concise, connect it to the actor kernel and
process registry, and make its ownership boundaries explicit.

## Tune Knowledge and Tools

After the four structural levels are clear, local memory and skills refine how
actors work within them.

## Put Knowledge in the Right Place

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