# Change Request: process-artefact-removal-grep

**Status**: merged
**Created**: 2026-05-13
**Branch**: feature/process-artefact-removal-grep
**Commit (feature)**: f496498
**Merge commit**: 8ad767c

---

## WHY

Obs-R "Stale Artefact Reference" produced 7 instances from a single origin CR in 24 hours. Each time, QM discovered remaining instances incidentally in the next CR review. A project-wide grep at artefact deletion time would have caught all 7 instances in one step.

---

## WHAT

The CM Workflow and Change Document Template shall both embed a mandatory artefact-removal check with 3-class classification of all grep results.

---

## Acceptance Criteria

- CM Workflow contains the Artefakt-Removal Rule as a mandatory step.
- Change Document Template contains a disclosure section for artefact-removal findings.
- The rule classifies findings into 3 classes: (a) code/workflow refs → fix same CR, (b) doc refs → fix same CR, (c) historic change docs → acceptable stranding + disclose.

---

## Files Changed

- `syspilot/agents/syspilot.cm.agent.md` — Artefakt-Removal Rule added after Workflow Step 11
- `syspilot/templates/change-document.md` — Artefakt-Removal-Check section updated to 3-class table + checklist

---

## Artefakt-Removal-Check

*No artefacts removed in this CR — process addition only.*

---

## Traceability

Process-only change. No spec (RST), no code, no CI changes.
