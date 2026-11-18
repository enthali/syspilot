---
name: syspilot.contract-statistics
description: >
  Usage record of one Contract from the local Copilot session store: calls, AIU,
  tokens, active time and activity per actor, with the window start taken from
  the Contract's start gate in git history. USE FOR: the Project Manager's
  closure checkout of a Change or Release Contract, after validation.
requirements: [SYSP_REQ_CONTRACT_STATISTICS_SKILL, SYSP_REQ_CONTRACT_STATISTICS_RECORD, SYSP_REQ_CONTRACT_STATISTICS_CLOSURE]
---

# Contract Statistics

Run from the repository root:

```
python .github/skills/syspilot.contract-statistics/scripts/contract_stats.py <contract-name>
```

`<contract-name>` is the Contract file name without `.md`, for a Change or a Release. The record is written to `.syspilot/stats/<contract-name>-stat.md`. For a Release, the statistics cover the Release Contract itself, not the Changes it contains.

## Window

- **Start:** the earliest commit by author date, across all branches and following file moves, whose version of the Contract shows the start gate as approved. The gate is the row `Contract release` (Change) or `Release start` (Release) whose status starts with `approved`. Commit messages are never read.
- **End:** the time the skill runs.
- `--start` and `--end` (ISO timestamps) override either. `--contract-file` names the Contract path when the name does not locate it.
- Sessions count when they ran in this repository; the actor name is taken from `Actor "<name>"` in the session summary.

## Record

Header (window, start source, commits), usage table per actor with totals, activity table with totals, AIU by phase, a one-line `**Summary:**` under each table, and Limits. The phase split is at the first commit of the Contract that shows `Current responsibility: Quality`: before and from the first handover to Quality. With an explicit `--start`, or when Quality never held the Contract, the window is one phase.

## Failure

The skill exits non-zero with a message and writes no record when the session store `~/.copilot/session-store.db` is missing, no commit shows the gate as approved and no `--start` is given, or the window holds no usage.
