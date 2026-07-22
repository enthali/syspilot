---
name: syspilot.orchestration-jarvis
group: orchestration
description: "Implements the SEND/RECEIVE/RESPOND orchestration vocabulary using Jarvis session-messaging tools. USE FOR: any agent that passes work to another session (SEND), obtains its triggering instructions (RECEIVE), or returns results to the initiator (RESPOND). Also use when agents need to determine whether they were triggered by a message or started directly. DO NOT USE FOR: general agent design, skill architecture rules, or spec writing."
implements: [SYSP_SPEC_SKILL_ORCHESTRATION_VERB_MODEL, SYSP_SPEC_SKILL_ORCHESTRATION_GROUP]
contract: SYSP_SPEC_SKILL_ORCHESTRATION_CONTRACT
requirements: [SYSP_REQ_SKILL_ORCHESTRATION_VERBS, SYSP_REQ_SKILL_ORCHESTRATION_GROUP]
---

# Skill: Agent Orchestration (Jarvis Variant)

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
| `SEND` | `SEND <work> to <agent>` | `jarvis_sendMessage("<session>", "<message>", "<senderSession>")` |
| `RECEIVE` | `RECEIVE` | `jarvis_receiveMessage("<destination>")` — returns the triggering message or empty |
| `RESPOND` | `RESPOND` | `jarvis_sendMessage("<originating-session>", "<result>", "<senderSession>")` — return result to sender |


