# Methodology: Specification Hierarchy & File Organization

## Overview

syspilot uses a three-level specification hierarchy based on **sphinx-needs** traceability.
Each level answers a different question and serves a different audience. This methodology
defines how specifications are structured, split into files, and traced across levels.

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
| 0 | **Why** does this matter? | Stakeholders, Product Owner | `US_` | `docs/10_userstories/` |
| 1 | **What** must the system do? | Architects, Reviewers | `REQ_` | `docs/11_requirements/` |
| 2 | **How** is it realized? | Developers, AI Agents | `SPEC_` | `docs/12_design/` |

## File Organization Principles

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

**Example themes:**

| File | Scope |
|------|-------|
| `us_installation.rst` | Bootstrap, setup, init scripts |
| `us_release.rst` | Versioning, update, rollback |
| `us_change_mgmt.rst` | Change workflow, agents, analysis |
| `us_traceability.rst` | Link discovery, MECE, verification |
| `us_process.rst` | A-SPICE alignment, methodology |
| `us_developer_experience.rst` | DX, onboarding, ergonomics |
| `us_integration.rst` | CI/CD, external tool integration |
| `us_security.rst` | Access control, credentials |

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

**Example mapping:**

```
us_installation.rst     →  req_installation.rst
us_release.rst          →  req_release.rst
us_change_mgmt.rst      →  req_change_mgmt.rst
us_traceability.rst     →  req_traceability.rst
us_process.rst          →  req_process.rst
```

For cases where a single US file produces very few REQs (2–3), it is acceptable to
merge related requirement sets — but the 1:1 default is the simplest mental model.

### Level 2 — Design Specs: Group by Technical Component

Design Specs shift from problem domain to **solution domain**. They group by
**technical component or module**, not by the User Story that motivated them.

**Splitting criteria:**
- One file per technical component, subsystem, or architectural module
- A single spec file may satisfy REQs from *multiple* User Stories
- Cross-cutting links are expected and healthy

**Example structure:**

| File | Technical Component |
|------|---------------------|
| `spec_agents.rst` | Agent framework, agent definitions |
| `spec_bootstrap.rst` | Init scripts, setup workflow |
| `spec_link_discovery.rst` | `get_need_links.py`, tracing engine |
| `spec_release.rst` | Version management, update/rollback |

**Why the shift?** At this level we describe *how the system is built*. A single
agent component might address requirements from installation, change management,
and traceability simultaneously. Forcing a 1:1 mapping with US files would create
artificial splits in cohesive technical designs.

## Cross-File Traceability

sphinx-needs resolves `:links:` directives **across all files** in the Sphinx project.
Splitting specifications into multiple files has **no impact** on traceability. The
`needtable`, `needflow`, and `needmatrix` directives aggregate from all sources.

```rst
.. req:: Bootstrap Validation
   :id: REQ_INST_BOOTSTRAP_VALIDATION
   :status: draft
   :links: US_INST_BOOTSTRAP

   .. (links to a US in a different file — works seamlessly)
```

## Directory Layout

```
docs/
├── 10_userstories/             # Level 0: WHY
│   ├── index.rst
│   ├── us_installation.rst     # Theme: setup & bootstrap
│   ├── us_release.rst          # Theme: versioning & updates
│   ├── us_change_mgmt.rst      # Theme: change workflow
│   ├── us_traceability.rst     # Theme: tracing & verification
│   └── us_process.rst          # Theme: process alignment
├── 11_requirements/            # Level 1: WHAT (mirrors Level 0)
│   ├── index.rst
│   ├── req_installation.rst    # REQs for us_installation
│   ├── req_release.rst         # REQs for us_release
│   ├── req_change_mgmt.rst     # REQs for us_change_mgmt
│   ├── req_traceability.rst    # REQs for us_traceability
│   └── req_process.rst         # REQs for us_process
├── 12_design/                  # Level 2: HOW (mirrors architecture)
│   ├── index.rst
│   ├── spec_agents.rst         # Component: agent framework
│   ├── spec_bootstrap.rst      # Component: init & setup
│   ├── spec_link_discovery.rst # Component: tracing engine
│   └── spec_release.rst        # Component: version management
```

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

File and ID naming conventions are documented in [namingconventions.md](namingconventions.md).

**File naming summary:**

| Level | Pattern | Grouping Principle |
|-------|---------|-------------------|
| Level 0 | `us_<theme>.rst` | Stakeholder theme / value stream |
| Level 1 | `req_<theme>.rst` | Matching US file (1:1) |
| Level 2 | `spec_<component>.rst` | Technical component / module |

The `<theme>` slug should be short, lowercase, and use underscores:
`installation`, `release`, `change_mgmt`, `traceability`, `process`.

**ID naming:** syspilot uses descriptive IDs (e.g., `US_CORE_SPEC_AS_CODE`)
instead of sequential numbers. See [namingconventions.md](namingconventions.md)
for the full convention.

## Summary

The fundamental insight of this methodology:

> **Levels 0–1 organize by problem domain (user goals). Level 2 organizes by
> solution domain (technical components). This asymmetry is intentional — it
> reflects the natural boundary where stakeholder needs meet system architecture.**

sphinx-needs traceability links bridge this boundary, maintaining full visibility
from *why* through *what* to *how* — regardless of how files are organized.
