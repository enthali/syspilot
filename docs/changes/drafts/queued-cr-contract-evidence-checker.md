# Queued CR Draft: contract-evidence-checker

**Status**: queued (not yet branched)
**Proposed Operation Mode**: autonomous (script and tests against an existing template)
**Origin**: Research finding from an external method review (2026-11-10/11)

---

## Problem

Every artifact in a Change is checked by an algorithm and semantically:
requirements by Sphinx-Needs, code by unit and integration tests, and both by
Quality. The Change Contract is checked only semantically, although it bundles
the evidence that everything else is complete.

LLM reviewers judge meaning well and notice missing items less reliably: an
empty evidence cell, a row left at `pending`, a Handover log that disagrees with
the header, a commit or result file that does not exist. These gaps make an
outcome invalid without any check reporting it.

The Release Contract already has `scripts/check_release_record.py`, introduced
at an actor's request.

## Proposal

A record checker for Change Contracts that reads the existing Markdown tables.
The Contract stays Markdown and stays the human- and LLM-readable evidence; the
checker confirms that the evidence is complete and consistent:

- every row with `Included: yes` has a terminal status and non-empty completion evidence;
- every referenced Need ID resolves in the built `needs.json`;
- every referenced commit exists, and every referenced test result file exists for that commit;
- `Current responsibility` in the header matches the receiver of the last Handover log line;
- the Closure checklist agrees with the row statuses;
- Open Quality Issues contains `None` at closure.

The checker reports what it could not check as a limitation, as `syspilot.mece`
and `syspilot.trace` do. It runs as a pre-merge check on `development`.

The same parser can extract a small set of fields (status, current
responsibility, impacted Need IDs, dependencies) for a later portfolio view
over parallel Changes.

## Observable Outcome

- The checker passes on every closed Contract in `docs/changes/` or reports each deviation.
- Tests cover each check with a passing and a failing Contract fixture.
- Quality records the checker result in the Quality Review section.
