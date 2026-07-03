---
name: syspilot.orchestration-subagent
group: orchestration
description: "Implements the SEND/RECEIVE/RESPOND orchestration vocabulary synchronously using runSubagent() only — no session-messaging infrastructure required. USE FOR: any agent that passes work to another agent (SEND), obtains its triggering instructions (RECEIVE), or returns results to the initiator (RESPOND). This is the graceful-degradation variant for workspaces without Jarvis. DO NOT USE FOR: general agent design, skill architecture rules, or spec writing."
---

# Skill: Agent Orchestration (Subagent Variant)

> **Implements**: SYSP_SPEC_SKILL_ORCHESTRATION_VERB_MODEL_SUBAGENT, SYSP_SPEC_SKILL_ORCHESTRATION_GROUP
> **Group Contract**: SYSP_SPEC_SKILL_ORCHESTRATION_CONTRACT
> **Requirements**: SYSP_REQ_SKILL_ORCHESTRATION_VERBS, SYSP_REQ_SKILL_ORCHESTRATION_GROUP

This is the **synchronous** variant: every verb maps to `runSubagent()`. It
requires no session-messaging infrastructure and is the graceful-degradation
path for workspaces without Jarvis. Agent documents are identical to the
asynchronous variant — only the mapping below differs.

## DEFINITIONS

| Term | Semantics |
|------|-----------|
| `SEND` | Pass work to another agent. The installed variant decides whether this is asynchronous message delivery or a synchronous call. |
| `RECEIVE` | Obtain the instructions that triggered this run — a pending inbox message or the task the agent was started with. |
| `RESPOND` | Deliver result to the initiator. The only mode-dependent verb: routes the result back accordingly (see below). Terminal workflow step. |

## Verb Mappings

| Verb | Syntax | Concrete Tool Call |
|------|--------|--------------------|
| `SEND` | `SEND <work> to <agent>` | `runSubagent("syspilot.<agent>", "<task>")` — blocks until the callee returns |
| `RECEIVE` | `RECEIVE` | The task/prompt this agent was started with (the `runSubagent` argument) — no inbox poll |
| `RESPOND` | `RESPOND` | The agent's normal output, captured as the `runSubagent` return value |

## RECEIVE: Obtaining Your Assignment

In the synchronous variant there is no inbox. Your assignment is the task you
were started with — the prompt passed into `runSubagent`. RECEIVE is therefore
a no-op that simply reads those starting instructions.

## RESPOND: Delivering Your Result

RESPOND is the terminal step. In this variant it is always plain output: emit
your structured result as your final message. The calling `runSubagent`
captures it as the return value. There is no active send-back and no inbox.

## `agents:` Frontmatter

The `agents:` field is an optional documentation field listing typical SEND
targets. It does not constrain which agents an agent may SEND to at runtime.

The field is retained only on the Setup Bootloader (which uses it to declare
its synchronous `runSubagent` target `syspilot.installer` — a call outside
the orchestration contract). All other agents omit `agents:` or leave it empty.

```yaml
---
# example: Setup Bootloader only
agents: ["syspilot.installer"]
---
```

## Rules

- Only one skill with `group: orchestration` may be installed at a time
  (mutual exclusion, enforced by the Setup Agent).
- This variant has no session concept: each SEND is a nested synchronous
  call. Deep nesting is bounded by the platform's subagent limits.
