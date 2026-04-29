---
name: syspilot.orchestration
description: "How managers invoke engineers as subagents. 'Invoke' in any syspilot agent doc means runSubagent(). The agents: list in YAML frontmatter declares which agents can be called. Managers orchestrate — engineers execute and return structured results. USE FOR: understanding agent communication, runSubagent() calls, agents: frontmatter semantics."
---

# Skill: Agent Orchestration

> Defines how syspilot managers orchestrate engineers.

## Core Principle

**Invoke = `runSubagent()`**

Whenever an agent document says "invoke", "dispatch", or "run" another agent,
this means calling `runSubagent("syspilot.<name>", ...)`.

## `agents:` Frontmatter

The `agents:` list in YAML frontmatter declares which agents this agent may
call as subagents. Only listed agents can be invoked.

```yaml
---
agents: ["syspilot.design", "syspilot.implement", "syspilot.mece"]
---
```

## Communication Pattern

1. **Manager → Engineer**: Clear assignment with input paths (Change Document,
   file paths, scope description). Always include instruction to work
   autonomously without asking questions.
2. **Engineer → Manager**: Structured result report (created files, IDs,
   build status, decisions made).
3. **Engineers are decoupled** — they don't know about each other. Only
   the manager knows the sequence.

## Who Orchestrates

| Agent | Invokes | Purpose |
|-------|---------|---------|
| `syspilot.cm` | 7 engineers | Full change workflow |
| `syspilot.qm` | mece, trace | Quality audits |
| `syspilot.design` | mece | Advisory MECE check per level |

## Completion Reporting

When an orchestrator completes a delegated task, it **SHALL** report back
to the sender via `jarvis_sendToSession`. This applies to:

- **CM → PM**: After completing a Change Request
- **QM → PM**: After completing a Quality Audit

The report **SHALL** include:
- Status (completed / blocked / failed)
- Commit hashes (if applicable)
- Summary of what was done
- Any issues or follow-up items found