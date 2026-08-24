# Syspilot Architect — Context

My public-facing role is documented in [docs/Syspilot Actors/Syspilot Architect.md](../../../../docs/Syspilot%20Actors/Syspilot%20Architect.md). I keep it current whenever my responsibilities change.
I read [docs/Syspilot Processes/index.md](../../../../docs/Syspilot%20Processes/index.md) at the start of every session to check for processes that apply to my work. For changes to the registry, I contact the Syspilot Project Manager.

Standing context that survives session loss. Lean by design.

## Decision
- v2 ontology uses `root, story, req, ac, vc, doc` (no `spec`/`impl`); REQ implements US directly; HOW uses `realized_by`; Technical Writer-owned DOC Needs aggregate into the documentation ownership map and link to REQs through `includes` / `included_in`. No `[syspilot.actors]` table — ownership is per-process (AD-6), not central.
- v2 actor specs use one shared Actor Model US/REQ for common structure and kernel boundary, plus one concrete US/REQ chain per Syspilot actor.

## Next
- Architecture work-in-progress tracked in [memory/kanban.md](memory/kanban.md).
