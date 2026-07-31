# The Workflow-less Actor: A North Star

**Topic:** What actually steers a multi-agent change pipeline — and why it isn't the workflow prose in the agent file

## Versions

| Component | Version |
|-----------|---------|
| syspilot | 0.9.0 |
| Jarvis | async orchestration (session-to-session messaging) |

---

## The Situation

Every syspilot agent file (`syspilot.cm.agent.md`, `syspilot.qm.agent.md`, ...) carries a
Workflow section: numbered steps describing what the agent does, in what order. We wrote
these carefully, reviewed them, kept them in sync with the pipeline. And yet, watching
real Change Requests move through the system, a pattern kept repeating: **the actors
weren't following the prose. They were following the Change Document.**

This surfaced most clearly in a parallel experiment — a second, agent-file-less setup
where a Project Manager actor was bootstrapped with nothing but a name and a blank
`context.md`. No workflow spec existed anywhere for that actor. The role and
responsibility were written *into* `context.md` at the very first session, and every
subsequent actor (Change Manager, Quality Manager, ...) started the same way: an almost
empty memory file with a link to a docs page the actor itself would maintain going
forward.

By the fourth Change Request in that setup, the process had stabilized — without ever
having been specified. Actors were coordinating directly with each other on incidental
questions (an architect asking an implementer about hardware access, because only the
implementer could see it) without routing everything through a central coordinator. And
critically: **nobody could recite the workflow anymore.** It hadn't been forgotten by
neglect — it had simply stopped being the thing that mattered.

## What Actually Steers the Process

Once we looked honestly at what *was* still governing behavior, three things remained,
and none of them were prose:

**1. Ontology ownership.** Every artefact type has an "ultimate owner" — one actor
responsible for it. This one fact answers the question "who does this next?" without
any process description. It already existed in syspilot's ontology (Ontology Phase 2);
it turns out to be doing more work than we credited it for.

**2. The Contract Document.** Intent and Goal are instance-specific — they don't belong
in a governed spec at all, they belong in *this instance's* document. The document's
*structure* — which sections exist, which must be filled before the process is
considered done — carries the process implicitly. A QM Findings section that must be
completed before merge doesn't need a sentence telling anyone to get it reviewed; the
document enforces it by existing. Different instance sizes (a one-line infra fix vs. a
multi-level spec change) don't need different workflows — they need different
*document shapes*. The process is tailorable simply by tailoring the document.

The Change Document was the first instance of this, but it isn't special — it's one
member of a general pattern: **a Contract Document is a checklist owned by exactly one
actor, whose fields are the process.** Release is the second instance: a Release
Document, owned by the Release Agent, whose fields are things like "build check run",
"squash-merge to main executed", "tag pushed" — filled in by the owner as the release
actually happens, not prescribed as prose steps in a spec somewhere else. The pattern
generalizes to any workflow that has a single responsible owner and a checkable
end-state: onboarding, incident response, whatever comes next. *How* the checklist gets
filled — in what order, with what side reasoning — is left entirely to the actor's
judgment. The document only fixes *what* must end up true, not *how* it gets there.

**3. Guardrails, with a defined action at the edge.** What genuinely needs governance is
not the happy path — it's the boundary. What happens when an actor hits a decision it
can't make alone? The rule we kept coming back to, worded as sharply as we could manage:

> **Never leave the actor in the rain.**

Every boundary needs a defined next step. The *specific* guardrail (e.g. "QM signs off
directly to PM, never relayed through CM") is always better than the generic one,
because it costs nothing extra. But there's a universal fallback underneath every
specific guardrail: **escalate — never improvise.** Escalation is not the goal, it's the
safety net. Design as many specific guardrails as you can; let escalation catch
everything you didn't think of.

Ranked, the hierarchy is:

```
specific guardrail (defined action)  >  escalate (generic safety net)  >  improvise (never)
```

## What This Implies for a Coordinator Role

The clearest test case is the Change Manager. If ownership lives in the ontology and
process lives in the Change Document's structure, CM's job reduces to something almost
mechanical: **own the Change Document, read which section is next, hand it to that
section's owner.** A document custodian and baton-passer, not a choreographer.

That doesn't mean CM stops exercising judgment — the opposite. What CM keeps is exactly
the part that can't be mechanized: recognizing when a delivered result *deviates* from
what was asked and deciding whether that's an error or an improvement (see
"Deviations are discussion triggers" — a lesson from this same release cycle). What CM
sheds is the step-by-step prose describing *how* to get there.

Pushed further: if "who's next" is just a lookup over the Change Document's fill-state
and the ontology's ownership table, **that lookup itself doesn't need judgment.** It can
be a script. This is the same split we kept re-discovering this cycle in different
disguises:

- **Change Launcher** (shipped, #61) — branch creation, template copy, header pre-fill:
  deterministic, extracted into a script. The PM's job shrank to writing the Summary —
  the one part that's genuinely intent, not mechanism.
- **Ontology-as-instruction-file** (proposed, #57 follow-up) — instead of an agent
  reading the ontology at runtime, a generator bakes actor-ownership into an
  always-injected instruction file. The agent never has to remember to look; the fact
  is just there.
- **Who's-next routing** (proposed) — CM's dispatch decision, mechanized the same way.

The pattern: **wherever a step inside an actor's job is deterministic, pull it out into
a script or an injected instruction. What's left in the actor is judgment, and only
judgment.**

## What Belongs Where

This cycle also forced a cleaner separation between two things that had been living in
the same place:

- **The actor kernel** — Local Memory, Messaging (SEND/RECEIVE/RESPOND), Escalation
  behavior, and the Culture that makes the first two constructive rather than
  defensive — is method-agnostic. It describes *any* actor, in syspilot or elsewhere
  (a parallel personal-information-management use of the same kernel made this
  concrete). It belongs to the harness (Jarvis), not to syspilot.
- **The method** — how to build an ontology such that a syspilot-shaped, traceable
  system comes out the other end — is what never goes away. It's syspilot's actual
  contribution. It doesn't dissolve into the kernel; it's the thing the kernel serves.

Escalation's *behavior* (respond upward, don't improvise) is kernel. Escalation's
*topology* (which actor the chain terminates at — PM in syspilot, a human user in a
personal-assistant setting) is method. Mixing the two accidentally hardcodes one
project's shape into a supposedly generic primitive.

## Adaptability: Ship the Pattern, Not the Prescribed Process

If the Contract Document is the real mechanism, syspilot's own value to a new project
isn't "do these steps in this order" — it's "here is how to build the Contract
Document for your own process, with one owner and a checkable end-state." Concretely:
syspilot ships its own Release Document as a worked example, and an adopting project's
first real task with syspilot is writing *its own* — not adopting syspilot's verbatim.
The method (how to shape an ownership + checklist document) travels; the specific
document (syspilot's own release checklist) does not have to. This is the same
kernel-vs-method split from the previous section, applied one level down: the Contract
Document *pattern* is method: the filled-out instance is project-specific content.

## What to Watch Out For

- **The bootstrap isn't optional.** The agent-file-less experiment didn't start from a
  blank slate and immediately run unsupervised — it took several changes, actively
  supervised, before the process stabilized enough to run on its own. syspilot's
  existing actors (PM, CM, QM) have effectively already been through that phase; a
  *new* role wouldn't get to skip it just because the model is compelling.
- **Guardrails must stay legible even as workflow prose shrinks.** If the process lives
  implicitly in the Change Document's structure, the guardrails better be explicit
  *somewhere* checkable — otherwise "the actors forgot the workflow" quietly becomes
  "the actors forgot the guardrail," which is a much worse failure mode.
- **Informal cross-actor communication is fine; formal gates are not optional.**
  Actors asking each other direct questions outside the coordinator is a sign of
  health, not drift — as long as decision gates (sign-off, merge) stay on the defined
  path. The two are easy to conflate if "let the actors self-organize" is taken too
  literally.
- **Not every change earns a Contract Document.** The pattern is for workflows with
  real ownership ambiguity or a multi-step checkable end-state. A one-line, low-risk
  fix doesn't need a checklist invented for it — that's just re-introducing prescribed
  process for something too small to need one. Judgment about *when* a Contract
  Document is warranted is itself left to the actor, not mandated by the pattern.

## Open Questions

- How far can an actor's Workflow section shrink before the judgment it protects
  starts leaking out with it? We don't have the answer yet — the next experiment is to
  try stripping one real syspilot agent file down to guardrails-plus-ontology-reference
  and see whether it still holds.
- Does the Contract Document pattern hold up for a second real instance? The next test
  is reframing syspilot's own Release process as a Release Document owned by the
  Release Agent, and checking whether the release workflow prose becomes as
  dispensable as the CR workflow prose did.
