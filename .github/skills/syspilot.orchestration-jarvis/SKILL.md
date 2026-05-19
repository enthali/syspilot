---
name: syspilot.orchestration-jarvis
group: orchestration
description: "Implements INVOKE/SEND/RECEIVE/RESPOND using runSubagent() and Jarvis messaging tools. Enables parallel Change Manager sessions via async inter-session communication. USE FOR: understanding agent communication patterns, INVOKE/SEND/RECEIVE/RESPOND semantics, Jarvis-backed session messaging."
---

# Skill: Agent Orchestration (Jarvis Variant)

> **Implements**: SYSP_SPEC_SKILL_ORCHESTRATION_VERB_MODEL, SYSP_SPEC_SKILL_ORCHESTRATION_GROUP
> **Group Contract**: SYSP_SPEC_SKILL_ORCHESTRATION_CONTRACT
> **Requirements**: SYSP_REQ_SKILL_ORCHESTRATION_INVOKE, SYSP_REQ_SKILL_ORCHESTRATION_GROUP

## DEFINITIONS

| Term | Semantics |
|------|-----------|
| `INVOKE` | Synchronous call. Caller blocks until callee returns a structured result. Used for same-session manager-to-engineer calls. |
| `SEND` | Deliver a message to another session. Non-blocking cross-session communication. Used for manager-to-manager handoff. |
| `RECEIVE` | Check inbox for pending messages. Returns the next pending message or indicates no messages available. Used by agents waiting for async work assignments. |
| `RESPOND` | Deliver result to caller. Auto-detects invocation mode and routes accordingly (see below). Terminal workflow step. |

## Verb Mappings

| Verb | Syntax | Concrete Tool Call |
|------|--------|--------------------|
| `INVOKE` | `INVOKE <agent>` | `runSubagent("syspilot.<agent>", "<prompt>")` |
| `SEND` | `SEND <message> to <session>` | `jarvis_sendToSession("<session>", "<message>")` |
| `RECEIVE` | `RECEIVE` | `jarvis_readMessage()` — returns next pending message or empty |
| `RESPOND` | `RESPOND` | Mode-detection logic (see below) |

## RESPOND: Invocation-Mode Detection

RESPOND auto-detects how the agent was invoked and routes the result accordingly:

1. Call `jarvis_readMessage()` to check if a pending message triggered this run
2. **If a triggering message is found** (sender context present): deliver the result via `jarvis_sendToSession` to the originating session
3. **If no triggering message**: output the result directly as structured final message (captured by `runSubagent()` return value)

Agents always call `RESPOND` — the detection logic is internal to this skill. Agents do not branch on invocation mode.

## Communication Pattern

**Manager → Engineer (INVOKE):**
- Assign work with input paths, instruction to work autonomously, expected output format
- Caller blocks until the engineer's RESPOND delivers the structured result

**Manager → Manager (SEND):**
- Deliver message to a named session
- Caller continues immediately (non-blocking)

**Engineer waiting for async work (RECEIVE):**
- First step in the workflow: call RECEIVE
- If a message is found, proceed with the work described in the message
- The RESPOND at the end routes back to the sender automatically

**Completion Reporting:**
- Status: `completed` / `blocked` / `failed`
- Commits: list of commit hashes with messages (if applicable)
- Summary: brief description of what was done
- Issues: list of problems or follow-up items (empty if none)

## `agents:` Frontmatter

The `agents:` list in YAML frontmatter declares which agents this agent may
call as subagents via INVOKE. Only listed agents can be invoked.

```yaml
---
agents: ["syspilot.design", "syspilot.implement", "syspilot.mece"]
---
```
