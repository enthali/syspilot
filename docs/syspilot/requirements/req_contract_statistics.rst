Contract Statistics
===================

.. req:: Contract Statistics Skill
   :id: SYSP_REQ_CONTRACT_STATISTICS_SKILL
   :status: approved
   :implements: SYSP_US_CONTRACT_STATISTICS
   :realized_by: .github/skills/syspilot.contract-statistics/scripts/contract_stats.py

   The skill ``syspilot.contract-statistics`` shall take a Contract name and
   write the Contract's usage record, for any Contract kind. It shall read the
   local Copilot session store read-only and attribute each model call to the
   Actor whose session made it, within a window of the Contract.

   The window shall start at the first commit, in the history of the Contract's
   file across all branches and following renames, whose version of the file
   shows the User's start gate as ``approved``. That gate is the row
   ``Contract release`` in a Change Contract and ``Release start`` in a Release
   Contract; the rule reads the row's status and never a commit message. The
   window shall end when the skill runs, which the Project Manager does at
   checkout. Explicit start and end times shall override both.

   The Contract name shall be a plain file name; a name with a path separator
   or a parent reference is rejected, so the record cannot leave
   ``.syspilot/stats/``.

   The skill shall fail explicitly, producing no record, when the session
   store is missing, when no start gate is found and no start time is given, or
   when the window holds no usage. For a Release Contract the figures cover the
   release Contract itself, not the Changes the release contains.

.. vc:: The window start is found from the gate, not from a message
   :id: SYSP_VC_CONTRACT_STATISTICS_SKILL_1
   :status: approved
   :verifies: SYSP_REQ_CONTRACT_STATISTICS_SKILL

   For a Change Contract and a Release Contract whose commit messages contain
   no release wording, the window starts at the first commit whose file version
   shows the gate ``approved``, including after the file was moved.

.. vc:: Explicit times produce the validated figures
   :id: SYSP_VC_CONTRACT_STATISTICS_SKILL_2
   :status: approved
   :verifies: SYSP_REQ_CONTRACT_STATISTICS_SKILL

   For ``ontology-example``-era data, the start 2026-11-16 22:03:00Z and end
   2026-11-16 22:12:00Z give 79 calls and 158.4 AIU, the figures the Project
   Manager validated against the session store.

.. vc:: Missing inputs fail without a record
   :id: SYSP_VC_CONTRACT_STATISTICS_SKILL_3
   :status: approved
   :verifies: SYSP_REQ_CONTRACT_STATISTICS_SKILL

   A missing session store, a Contract without a start gate and without a
   given start, an empty window, and a name that is not a plain file name each
   end with a non-zero exit and a message
   naming the cause; no record is written.

.. req:: Contract Statistics Record
   :id: SYSP_REQ_CONTRACT_STATISTICS_RECORD
   :status: approved
   :implements: SYSP_US_CONTRACT_STATISTICS
   :realized_by: .github/skills/syspilot.contract-statistics/SKILL.md

   The record shall be ``.syspilot/stats/<contract>-stat.md`` and contain:

   - a header with the window and how its start was found, the commits in the
     window, the extraction time and the definition of the credit;
   - a usage table with one row per Actor and a total row: calls, model time,
     active time, AIU, premium requests, input tokens, cached share, cache
     write tokens, output tokens, reasoning tokens, and model with reasoning
     effort;
   - an activity table with one row per Actor and a total row: turns, files
     changed and sub-agent calls;
   - an AIU split by phase, before and from the first commit whose Contract
     file shows Quality as ``Current responsibility`` (one phase when Quality
     never held it or the start is explicit), and one generated summary line
     under each table; and
   - the limits of the figures.

   AIU is the credit. The record shall state that per-Actor commit counts,
   tool calls and tool durations are not available from the session store, and
   that the figures are usage, not a judgment of the work.

.. vc:: The record holds the specified tables and limits
   :id: SYSP_VC_CONTRACT_STATISTICS_RECORD_1
   :status: approved
   :verifies: SYSP_REQ_CONTRACT_STATISTICS_RECORD

   A generated record has the header fields, both tables with total rows, the
   phase split, a summary line under each table, and the stated limits.

.. req:: Contract Statistics At Closure
   :id: SYSP_REQ_CONTRACT_STATISTICS_CLOSURE
   :status: approved
   :implements: SYSP_US_CONTRACT_STATISTICS
   :realized_by: docs/Syspilot Contracts/change.md

   The Closure checklist of the canonical Change and Release Contracts, and of
   their Example counterparts that carry such a checklist, shall contain an
   item for running the statistics skill at checkout, by the Project Manager,
   after validation. It is a checkout step, not an artifact or gate row, and
   the Contract shall hold no statistics evidence.

.. vc:: Closure checklists name the statistics step
   :id: SYSP_VC_CONTRACT_STATISTICS_CLOSURE_1
   :status: approved
   :verifies: SYSP_REQ_CONTRACT_STATISTICS_CLOSURE

   The Change and Release templates and their Example counterparts each
   contain the checklist item, and no artifact row or Contract field records
   statistics.

.. req:: Setup Prepares Contract Statistics
   :id: SYSP_REQ_SETUP_STATISTICS
   :status: approved
   :implements: SYSP_US_CONTRACT_STATISTICS
   :realized_by: docs/Syspilot Contracts/setup.md

   Setup shall install the skill with the other release skills, create
   ``.syspilot/stats/``, and add that folder to the project's ``.gitignore``.
   The ignore entry is an additive edit under Setup's rule for such edits: it
   never overwrites the file and never duplicates an existing entry. The
   ignored folder is Setup's own and does not trigger the blocker for ignored
   generated destinations.

.. vc:: Setup prepares the ignored statistics folder
   :id: SYSP_VC_SETUP_STATISTICS_1
   :status: approved
   :verifies: SYSP_REQ_SETUP_STATISTICS

   A fresh Setup installs the skill and creates the folder with its ignore
   entry; a second run, and a ``.gitignore`` that already holds the entry,
   change nothing, and other content of that file stays as it was.
