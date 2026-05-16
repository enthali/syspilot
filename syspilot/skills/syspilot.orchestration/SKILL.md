---
name: syspilot.orchestration
group: orchestration
description: "How managers orchestrate engineers using the INVOKE/DELEGATE/REPLY verb model. Verbs are tool-agnostic — this sync variant maps them to runSubagent(). The agents: list in YAML frontmatter declares which agents can be called. USE FOR: understanding agent communication, INVOKE/DELEGATE/REPLY semantics, runSubagent() calls, agents: frontmatter semantics."
---

# Skill: Agent Orchestration (Sync Variant)

> **Implements**: SYSP_SPEC_SKILL_ORCHESTRATION_VERB_MODEL, SYSP_SPEC_SKILL_ORCHESTRATION_GROUP
> **Requirements**: SYSP_REQ_SKILL_ORCHESTRATION_INVOKE, SYSP_REQ_SKILL_ORCHESTRATION_GROUP

## Instructions

## The Three Verbs

Orchestration uses three tool-agnostic verbs. Agents write these verbs in
their workflows; the installed orchestration skill maps them to runtime calls.

### INVOKE

Synchronous call — the manager blocks until the engineer returns a result.

Use when the manager needs the result before proceeding to the next step.

### DELEGATE

Hand-off of a task to another agent. In async variants, the caller continues
working while the delegate executes. **In this sync variant, DELEGATE
collapses to INVOKE** — there is no async execution.

Use when the intent is "hand this off", even though sync execution blocks.

### REPLY

The engineer returns its result to whoever called it. **REPLY is
runtime-conditional** — the agent checks how it was called:

- **If called via `runSubagent()` (sync):** Summarize findings as the final
  message. `runSubagent()` captures this as its return value.
- **If called via `jarvis_sendToSession` (async/inter-session):** Send the
  result back via `jarvis_sendToSession` to the originating session.

Every engineer workflow MUST end with REPLY.

## Sync-Variant Verb Mapping

| Verb | Syntax | Concrete Mapping |
|------|--------|------------------|
| `INVOKE` | `INVOKE <agent>` | `runSubagent("syspilot.<agent>", "<prompt>")` |
| `DELEGATE` | `DELEGATE <task> to <agent>` | Collapses to INVOKE (no async in sync variant) |
| `REPLY` | `REPLY` | Prompt-Reminder: summarize findings as final message |

## `agents:` Frontmatter

The `agents:` list in YAML frontmatter declares which agents this agent may
call as subagents. Only listed agents can be invoked.

```yaml
---
agents: ["syspilot.design", "syspilot.implement", "syspilot.mece"]
---
```

## Communication Pattern

1. **Manager → Engineer (INVOKE / DELEGATE)**: Clear assignment with input
   paths (Change Document, file paths, scope description). Always include
   instruction to work autonomously without asking questions.
2. **Engineer → Manager (REPLY)**: Structured result report (created files,
   IDs, build status, decisions made).
3. **Engineers are decoupled** — they don't know about each other. Only
   the manager knows the sequence.

## Who Orchestrates

| Agent | Invokes | Purpose |
|-------|---------|---------|
| `syspilot.cm` | change, implement, uat, verify, mece, trace, release, docu | Full change workflow |
| `syspilot.qm` | mece, trace | Quality audits |
| `syspilot.design` | mece | Advisory MECE check per level |

## Completion Reporting

When an orchestrator completes a delegated task, it **SHALL** report back
to the sender. The delivery mechanism depends on the context:

- **In-session (engineer → manager):** Direct return value via REPLY
- **Inter-session (manager → manager):** `jarvis_sendToSession`

This applies to:
- **CM → PM**: After completing a Change Request
- **QM → PM**: After completing a Quality Audit
- **Any engineer → orchestrating manager**: After completing a delegated task

The report **SHALL** include:
- Status (completed / blocked / failed)
- Commit hashes (if applicable)
- Summary of what was done
- Any issues or follow-up items found

## Rules

* Only agents listed in `agents:` frontmatter MAY be invoked — calling an unlisted agent MUST NOT happen.
* Every engineer workflow MUST end with REPLY.
* REPLY delivery is runtime-conditional: `runSubagent()` return value (sync) or `jarvis_sendToSession` (async).
* Orchestrators (CM, QM) SHALL send completion reports. MUST NOT silently drop results.
* Report SHALL include: status, commit hashes (if applicable), summary, any issues or follow-up items.
* Only one skill with `group: orchestration` may be installed at a time.