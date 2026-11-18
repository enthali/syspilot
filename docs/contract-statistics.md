# Contract Statistics

The `syspilot.contract-statistics` skill records actor usage during a Contract's
time window. The Project Manager runs it at checkout, after validation, as a
closure step for Change and Release Contracts. It is not another artifact or
gate, and the statistics are not copied into the Contract.

For a Release, the window covers running the Release Contract itself, not an
aggregate of the Changes it publishes.

## Run It

From the repository root:

```powershell
python .github\skills\syspilot.contract-statistics\scripts\contract_stats.py <contract-name>
```

Replace `<contract-name>` with the Contract file name without `.md`, for example
`impact-artifact-list`. The command reads the local Copilot session store at
`~/.copilot/session-store.db` without changing it and writes:

```text
.syspilot/stats/<contract-name>-stat.md
```

The record is local working output. Setup installs the skill, creates the folder,
and adds its Git ignore entry additively without overwriting existing content
or duplicating an existing entry. An existing ignore rule that already covers
the folder is sufficient. The deliberately ignored statistics folder does not
trigger Setup's blocker for ignored generated destinations.

## Choose the Window

By default, the start is the earliest commit by author date in the Contract
file's history whose version shows its start gate as approved. The search spans
all branches and follows file moves; it reads the gate row, not commit-message
wording. The recognized gates are `Contract release` for a Change and
`Release start` for a Release. The end is the time the command runs.

Use `--start` or `--end` with an ISO timestamp to override either boundary;
include `Z` or a UTC offset to make the timezone explicit. A timestamp without
either is read as UTC, not local time. For example, using a sample Contract name:

```powershell
python .github\skills\syspilot.contract-statistics\scripts\contract_stats.py sample-contract --start 2026-11-16T22:03:00Z --end 2026-11-16T22:12:00Z
```

`--contract-file` supplies the Contract's repository-relative path when its name
does not locate it. Other Contract kinds can use an explicit start when they
have no recognized start gate. `--repo` selects the repository root, and
`--store` selects a different local session-store file.

A rerun replaces the record for that Contract name. Without an explicit end,
it also extends the window to the new run time.

## Read the Record

The header identifies the window, its start source, extraction time, commit
count and credit definition. AIU is the credit: recorded nano-AIU divided by
one billion. Premium requests are a separate sum of request multipliers.

- **Usage per actor:** calls, model time, active time, AIU, premium requests,
  input tokens, cached share, cache write tokens, output tokens, reasoning
  tokens, and model with reasoning effort; a total row follows.
- **Activity per actor:** turns, files changed and sub-agent calls, with totals.
- **AIU by phase:** before and from the first commit that names Quality as
  current responsibility. If Quality never held the Contract, or `--start`
  is explicit, the report uses one whole-window phase.

Each table has a generated one-line summary. Model time comes from recorded call
durations. Active time approximates actor runtime using short gaps between
calls and includes tool and wait time; it is not wall-clock project duration.

Sessions are selected by repository and time, not by whether their content is
about this Contract. Parallel unrelated work in the same repository is included.
Actor names come from session summaries; unrecognized names remain visible as
unnamed sessions. The figures describe usage, not the quality of an actor's work.

Per-actor commit counts, tool-call counts and tool durations are not available
from the local store. The header's commit count is a repository-history figure,
not an attribution to actors.

## If It Fails

The command exits non-zero with a diagnostic and writes no record when the
store is missing, no approved start gate is found without an explicit start,
or the window contains no usage. Check the named input or boundary rather than
treating a missing record as zero usage.
