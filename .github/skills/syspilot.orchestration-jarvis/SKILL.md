---
name: syspilot.orchestration-jarvis
group: orchestration
description: "Implements the SEND/RECEIVE/RESPOND orchestration vocabulary using Jarvis session-messaging tools. USE FOR: any agent that passes work to another session (SEND), obtains its triggering instructions (RECEIVE), or returns results to the initiator (RESPOND). Also use when agents need to determine whether they were triggered by a message or started directly. DO NOT USE FOR: general agent design, skill architecture rules, or spec writing."
---

# Skill: Agent Orchestration (Jarvis Variant)

> **Implements**: SYSP_SPEC_SKILL_ORCHESTRATION_VERB_MODEL, SYSP_SPEC_SKILL_ORCHESTRATION_GROUP
> **Group Contract**: SYSP_SPEC_SKILL_ORCHESTRATION_CONTRACT
> **Requirements**: SYSP_REQ_SKILL_ORCHESTRATION_VERBS, SYSP_REQ_SKILL_ORCHESTRATION_GROUP

This is the **asynchronous** variant: SEND/RECEIVE map to Jarvis session
messaging. It runs each orchestrating agent as its own persistent session.

## DEFINITIONS

| Term | Semantics |
|------|-----------|
| `SEND` | Pass work to another agent. The installed variant decides whether this is asynchronous message delivery or a synchronous call. |
| `RECEIVE` | Obtain the instructions that triggered this run — a pending inbox message or the task the agent was started with. |
| `RESPOND` | Deliver result to the initiator. The only mode-dependent verb: routes the result back accordingly (see below). Terminal workflow step. |

## Verb Mappings

| Verb | Syntax | Concrete Tool Call |
|------|--------|--------------------|
| `SEND` | `SEND <work> to <agent>` | `jarvis_sendToSession("<session>", "<message>")` |
| `RECEIVE` | `RECEIVE` | `jarvis_readMessage()` — returns the triggering message or empty |
| `RESPOND` | `RESPOND` | Mode-detection logic (see below) |

## RESPOND: Delivering Your Result

RESPOND is the terminal step. How you deliver depends on how you were triggered:

- **If you received your instructions via RECEIVE** (a message was present when you checked your inbox at workflow start): deliver your result via SEND to the originating sender.
- **If you were started directly** (no pending message was found via RECEIVE at workflow start): emit the result as direct structured output — `runSubagent()` captures this as its return value.

Do not call `jarvis_readMessage()` inside RESPOND. The invocation mode is already known from the RECEIVE call at workflow start.

## `agents:` Frontmatter

The `agents:` field is an optional documentation field listing typical SEND
targets. It does not constrain which sessions an agent may SEND to at runtime.
In the session model any session can SEND to any other session by name.

The field is retained only on the Setup Bootloader (which uses it to declare
its synchronous `runSubagent` target `syspilot.installer` — a call outside
the orchestration contract). All other agents omit `agents:` or leave it empty.

```yaml
---
# example: Setup Bootloader only
agents: ["syspilot.installer"]
---
```
