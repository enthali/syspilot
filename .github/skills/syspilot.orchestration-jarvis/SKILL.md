---
name: syspilot.orchestration-jarvis
group: orchestration
description: "Implements the INVOKE/SEND/RECEIVE/RESPOND orchestration vocabulary using runSubagent() and Jarvis messaging tools. USE FOR: any agent that calls subagents (INVOKE), sends messages to other sessions (SEND), checks its inbox (RECEIVE), or returns results to callers (RESPOND). Also use when agents need to determine whether they were triggered by a message or invoked directly. DO NOT USE FOR: general agent design, skill architecture rules, or spec writing."
---

# Skill: Agent Orchestration (Jarvis Variant)

> **Implements**: SYSP_SPEC_SKILL_ORCHESTRATION_VERB_MODEL, SYSP_SPEC_SKILL_ORCHESTRATION_GROUP
> **Group Contract**: SYSP_SPEC_SKILL_ORCHESTRATION_CONTRACT
> **Requirements**: SYSP_REQ_SKILL_ORCHESTRATION_INVOKE, SYSP_REQ_SKILL_ORCHESTRATION_GROUP

## DEFINITIONS

| Term | Semantics |
|------|-----------|
| `INVOKE` | Synchronous call. Caller blocks until callee returns a structured result. |
| `SEND` | Deliver a message to another session. Non-blocking cross-session communication. |
| `RECEIVE` | Check inbox for pending messages. Returns the next pending message or indicates none available. |
| `RESPOND` | Deliver result to caller. Auto-detects invocation mode and routes accordingly (see below). Terminal workflow step. |

## Verb Mappings

| Verb | Syntax | Concrete Tool Call |
|------|--------|--------------------|
| `INVOKE` | `INVOKE <agent>` | `runSubagent("syspilot.<agent>", "<prompt>")` |
| `SEND` | `SEND <message> to <session>` | `jarvis_sendToSession("<session>", "<message>")` |
| `RECEIVE` | `RECEIVE` | `jarvis_readMessage()` — returns next pending message or empty |
| `RESPOND` | `RESPOND` | Mode-detection logic (see below) |

## RESPOND: Delivering Your Result

RESPOND is the terminal step. How you deliver depends on how you were invoked:

- **If you received your instructions via RECEIVE** (a message was present when you checked your inbox at workflow start): deliver your result via SEND to the originating sender.
- **If you were invoked directly** (no pending message was found via RECEIVE at workflow start): emit the result as direct structured output — `runSubagent()` captures this as its return value.

Do not call `jarvis_readMessage()` inside RESPOND. The invocation mode is already known from the RECEIVE call at workflow start.

## `agents:` Frontmatter

The `agents:` list in YAML frontmatter declares which agents this agent may
call as subagents via INVOKE. Only listed agents can be invoked.

```yaml
---
agents: ["syspilot.design", "syspilot.implement", "syspilot.mece"]
---
```
