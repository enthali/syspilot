# Queued CR Draft: hygiene-workflow-req-links

**GH Issue**: #41
**Status**: queued (not yet branched)
**Proposed Operation Mode**: autonomous (small, mechanical, well-specified)

---

## Summary (draft)

All per-agent workflow requirements (e.g. `SYSP_REQ_PM_WORKFLOW`, `SYSP_REQ_CM_WORKFLOW`, etc.) should carry an outgoing `:links:` to `SYSP_REQ_AGENT_ARCH_WORKFLOW` to indicate they implement the agent architecture contract. Currently only frontmatter REQs do this correctly — workflow REQs don't. Discovered as an out-of-scope follow-up during the `generic-agent-workflow-pattern` CR (2026-06-29).

Motivation: same traceability-consistency principle already applied to frontmatter REQs via the `agent-spec-base-toolset-links` CR — extending it to workflow REQs closes a known gap and would let a doc-build cross-check make the gap visible going forward.

Acceptance criteria: every per-agent `SYSP_REQ_*_WORKFLOW` requirement links to `SYSP_REQ_AGENT_ARCH_WORKFLOW`; sphinx-build `-W` passes clean.

---

## Next steps once branch is safe to create

1. `git checkout experimental && git pull && git checkout -b feature/hygiene-workflow-req-links`
2. Copy `syspilot/templates/change-document.md` to `docs/changes/hygiene-workflow-req-links.md`
3. Fill header + Summary (content above) — Operation Mode: autonomous
4. Commit + push branch
5. SEND to Change Manager
