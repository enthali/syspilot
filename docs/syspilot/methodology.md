# syspilot Family: Methodology

This document describes the specification methodology for the **syspilot** agent family.
For the framework-level methodology (families, repository structure, write boundaries),
see [../methodology.md](../methodology.md).

## The Three Levels

```
Level 0: User Stories  (WHY)   → Stakeholder perspective
         │ :links:
         ▼
Level 1: Requirements  (WHAT)  → System behavior
         │ :links:
         ▼
Level 2: Design Specs  (HOW)   → Technical solution
```

| Level | Question | Audience | ID Prefix | Directory |
|-------|----------|----------|-----------|-----------|
| 0 | **Why** does this matter? | Stakeholders, Product Owner | `SYSP_US_` | `docs/syspilot/userstories/` |
| 1 | **What** must the system do? | Architects, Reviewers | `SYSP_REQ_` | `docs/syspilot/requirements/` |
| 2 | **How** is it realized? | Developers, AI Agents | `SYSP_SPEC_` | `docs/syspilot/design/` |

## File Organization

### Key Insight: The Domain Shift

Levels 0 and 1 are organized by **problem domain** — they cluster around user goals
and stakeholder concerns. Level 2 shifts to **solution domain** — it clusters around
technical components and architecture.

This asymmetry between Level 1 (mirrors Level 0) and Level 2 (mirrors architecture)
is **intentional by design**. It reflects the natural boundary where the *problem domain*
meets the *solution domain*.

### Level 0 — User Stories: Split by Stakeholder Theme

User Stories group by **domain/theme** — areas of stakeholder concern or value streams.

**Splitting criteria:**
- One file per coherent theme or domain area
- Group by *stakeholder goal*, not by technical component
- Typical file contains 2–8 User Stories

**Current themes:**

| File | Scope |
|------|-------|
| `us_core.rst` | Core methodology, spec-as-code |
| `us_workflows.rst` | End-to-end workflow orchestration |
| `us_change_mgmt.rst` | Change workflow, agents, analysis |
| `us_traceability.rst` | Link discovery, MECE, verification |
| `us_installation.rst` | Bootstrap, setup, init scripts |
| `us_release.rst` | Versioning, update, rollback |
| `us_developer_experience.rst` | DX, onboarding, ergonomics |
| `us_documentation.rst` | Documentation maintenance |

**Guideline:** When identifying themes, ask *"What value does the user get?"* not
*"What component does this touch?"*

### Level 1 — Requirements: Mirror the User Story Files

Requirements files have a **1:1 correspondence** with User Story files.

**Splitting criteria:**
- One `req_<domain>.rst` for each `us_<domain>.rst`
- Contains all requirements linked to the User Stories in the matching file
- Typical file contains 5–20 requirements

**Rationale:**
- **Natural scoping** — a US file defines a bounded context, so its REQs are cohesive
- **Reviewable size** — keeps files manageable for human review
- **Parallel work** — different contributors can own different domains
- **Clear naming** — `req_installation.rst` maps to `us_installation.rst`

### Level 2 — Design Specs: Group by Technical Component

Design Specs shift from problem domain to **solution domain**. They group by
**technical component or module**, not by the User Story that motivated them.

**Splitting criteria:**
- One file per technical component, subsystem, or architectural module
- A single spec file may satisfy REQs from *multiple* User Stories
- Cross-cutting links are expected and healthy

**Current components:**

| File | Technical Component |
|------|---------------------|
| `spec_agent_framework.rst` | Shared workflow, prompt-agent separation |
| `spec_change.rst` | Change Agent (level processing, change doc, navigation) |
| `spec_implement.rst` | Implement Agent (quality gates, traceability) |
| `spec_verify.rst` | Verify Agent (categories, report, status lifecycle) |
| `spec_traceability.rst` | MECE Agent + Trace Agent (horizontal & vertical) |
| `spec_memory.rst` | Memory Agent (update process, content categories) |
| `spec_setup.rst` | Setup Agent (init, ownership, update, auto-detect) |
| `spec_doc_structure.rst` | sphinx-needs documentation structure |
| `spec_doc_scope.rst` | Documentation scope (project-specific, chapter structures) |
| `spec_release.rst` | Release pipeline (versioning, CI/CD, GitHub Pages) |

**Why the shift?** At this level we describe *how the system is built*. A single
agent component might address requirements from installation, change management,
and traceability simultaneously. Forcing a 1:1 mapping with US files would create
artificial splits in cohesive technical designs.

## Scaling Guidelines

| Scale | User Stories | Requirements | Design Specs |
|-------|-------------|--------------|--------------|
| Small (< 10 US) | 1–3 files | 1–3 files | 1–3 files |
| Medium (10–50 US) | 5–10 files | 5–10 files | 5–15 files |
| Large (50+ US) | 10–20 files | 10–20 files | 15–30 files |

**When to split an existing file:**
- More than ~10 User Stories in one file
- More than ~20 Requirements in one file
- More than ~15 Design Specs in one file
- When two clearly distinct themes share a file

**When NOT to split:**
- Fewer than 3 items — keep in a shared file
- Items are tightly cohesive and always reviewed together

## Naming Conventions

syspilot-specific naming conventions (themes, examples) are documented in
[namingconventions.md](namingconventions.md).
