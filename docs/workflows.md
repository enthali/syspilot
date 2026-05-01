# Workflows: The syspilot Process

## Overview

syspilot is a **process framework** for spec-driven development. It defines three
workflows that cover the full lifecycle of specifications and code:

| Workflow | Purpose | Agents | When to use |
|----------|---------|--------|-------------|
| **Change** | Evolve specs and code | design → implement → uat → verify → docu | Every feature, fix, or refactor |
| **Quality** | Check specification health | mece, trace | Any time, independently |
| **Release** | Bundle and publish | release | After changes are merged |

### Manager Orchestration

Three managers orchestrate the engineers:

| Manager | Role | Responsibility |
|---------|------|---------------|
| `@syspilot.pm` | Project Manager | Plans features, prioritizes backlog, delegates Change Requests to CM |
| `@syspilot.cm` | Change Manager | Orchestrates engineers through the Change Workflow (autonomous or user-guided) |
| `@syspilot.qm` | Quality Manager | Dispatches `@syspilot.mece` and `@syspilot.trace`, consolidates findings |

**Change Modes:** The Change Manager supports two modes:
- **autonomous** — proceeds without user feedback except for UAT
- **user-guided** — requests user approval after each spec level

Each workflow is a defined sequence of agent invocations. You always know which
agent to call next.


## The Change Workflow

The Change Workflow is the primary development loop. Every change — from a new
feature to a bug fix — follows this sequence:

```{mermaid}
flowchart LR
    design --> implement --> uat --> verify --> docu
    docu --> next["Next change or<br/>release workflow"]
    design -.-> next
```

### @syspilot.design — Analyze

**Input:** A change request (GitHub issue, verbal description, or idea)

**What it does:**
1. Creates a **Change Document** in `docs/changes/`
2. Analyzes impact **level by level** — at each level, runs **impact analysis**
   (via `syspilot.impact-python` skill) to discover affected elements through
   sphinx-needs traceability links before identifying changes:
   - **Level 0 (User Stories):** Which user goals are affected? New scenarios?
   - **Level 1 (Requirements):** Which requirements change? New acceptance criteria?
   - **Level 2 (Design Specs):** Which technical specs need updating?
3. Asks for your approval at each level before proceeding
4. Performs horizontal consistency checks (MECE) at each level

**Output:** An approved Change Document with all affected IDs listed

**Key principle:** The Design Agent never modifies code — it only analyzes and
documents. This separation ensures thorough analysis before implementation.

### @syspilot.implement — Execute

**Input:** An approved Change Document

**What it does:**
1. Reads the Change Document and all linked specs
2. Writes the RST specification changes (US, REQ, SPEC files)
3. Implements code changes with traceability comments
4. Verifies every acceptance criterion is covered before proceeding
5. Runs tests (if applicable)
6. Updates user-facing documentation
7. Commits with traceability references

**Output:** A commit (or series of commits) implementing all specified changes

**Key principle:** The Implement Agent follows the Change Document exactly.
It doesn't make design decisions — those were made during analysis.

### @syspilot.uat — User Acceptance Test

**Input:** The same Change Document, after implementation

**What it does:**
1. Generates user acceptance test artifacts from the Change Document
2. Checks acceptance criteria coverage
3. Produces test stories and scenarios

**Output:** UAT artifacts for user review

### @syspilot.verify — Validate

**Input:** The same Change Document, after UAT

**What it does:**
1. Reads the Change Document and checks every requirement against the implementation
2. Verifies traceability: US → REQ → SPEC → Code
3. Validates that acceptance criteria are met
4. Runs the Sphinx build to check for broken links
5. Updates spec statuses from `approved` → `implemented`
6. Creates a validation report in `docs/changes/val-<name>.md`

**Output:** A validation report confirming (or flagging issues with) the implementation

### @syspilot.docu — Update Documentation

**Input:** Completed and verified changes

**What it does:**
1. Reviews what changed in the codebase
2. Updates `copilot-instructions.md`, manager context files, and external docs as needed
3. Keeps documentation concise — removes outdated info, adds new patterns

**Output:** Updated documentation (or confirmation that no update is needed)

**Key principle:** Documentation is the last step because it captures the *result*
of the full change cycle, not intermediate states.


## The Quality Workflow

Quality checks run independently — no Change Document needed. They're read-only
analyses that identify issues in your specifications.

```{mermaid}
flowchart TD
    mece --> f1{"Findings?"}
    trace --> f2{"Findings?"}
    f1 --> fix["Start a change<br/>workflow to fix"]
    f2 --> fix
```

### @syspilot.mece — Horizontal Check

**What it does:** Analyzes **one specification level** for:
- **Mutually Exclusive** — No overlapping or contradictory specs
- **Collectively Exhaustive** — No gaps in coverage

**When to use:**
- Before a release, to validate spec quality
- After a large change, to check consistency
- When you suspect redundancies or gaps

**Example:** `@syspilot.mece` on Level 1 (Requirements) might find that two
requirements define conflicting behavior for the same feature.

### @syspilot.trace — Vertical Check

**What it does:** Traces **one specification element** through all levels:
- Up: Which User Stories does this requirement serve?
- Down: Which Design Specs implement this requirement? Which code?

**When to use:**
- To verify a specific item has complete coverage
- To understand the full context of a spec element
- To find "orphan" specs that aren't linked to anything

**Example:** `@syspilot.trace SYSP_REQ_INST_LOCAL_SOURCE` shows the User
Stories above, the Design Specs below, and the code that implements it.


## The Release Workflow

The Release Workflow bundles completed changes into a versioned release.
It runs after one or more Change Workflows have been merged to main.

```{mermaid}
flowchart LR
    V["Version<br/>bump"] --> Val["Validate<br/>(build)"] --> N["Notes<br/>(generate)"] --> P["Publish<br/>(tag+push)"]
```

**`@syspilot.release`** handles the full process:

1. **Version bump** — Update `syspilot/version.json` with the new version and update the `version:` field in `syspilot/agents/syspilot.setup.agent.md` frontmatter
2. **Validate** — Run Sphinx build, check for broken links and schema violations
3. **Release notes** — Generate `docs/releasenotes.md` from Change Documents
4. **Archive** — Move Change Documents to `docs/changes/archive/<version>/`
5. **Publish** — Create Git tag and GitHub Release

**When to use:** After all planned changes for a version are merged and verified.


## Branching Strategy

syspilot uses a permanent `development` integration branch with short-lived feature branches:

```{mermaid}
gitGraph
    commit id: "v0.2.3" tag: "v0.2.3"
    branch development
    checkout development
    commit id: "dev-start"
    branch feature/CR7
    checkout feature/CR7
    commit id: "CR7: specs"
    commit id: "CR7: implement"
    commit id: "CR7: verify"
    checkout development
    merge feature/CR7 id: "squash CR7"
    branch feature/CR8
    checkout feature/CR8
    commit id: "CR8: specs"
    commit id: "CR8: implement"
    commit id: "CR8: verify"
    checkout development
    merge feature/CR8 id: "squash CR8"
    checkout main
    merge development id: "v0.2.4" tag: "v0.2.4"
```

**Rules:**

| Rule | What | Why |
|------|------|-----|
| **One branch per change** | `@syspilot.design` creates `feature/<name>` from `development` | Isolates each change for independent review |
| **Development as integration** | All feature branches squash-merge into `development` | Permanent integration branch for all work |
| **Squash-merge everywhere** | Feature→development and development→main use squash-merge | Clean history on both branches |
| **Main = releases only** | Squash merge to main happens only during `@syspilot.release` | Main always equals the latest release |
| **Tag on main** | Release creates `v{version}` tag on the squash merge commit | Tags mark published releases |

**Workflow:**

1. `@syspilot.design` → creates `feature/<name>` branch from `development`
2. `@syspilot.implement` → commits code on the same branch
3. `@syspilot.uat` → generates UAT artifacts on the same branch
4. `@syspilot.verify` → commits validation report on the same branch
5. `@syspilot.docu` → commits documentation updates on the same branch
6. **Complete** → squash-merge feature branch into ``development``
6. `@syspilot.release` → squash-merge `development` into main, bump version, tag


## When to Use Which Agent

| Situation | Agent | Notes |
|-----------|-------|-------|
| New feature request | `@syspilot.design` | Always start here |
| Bug fix | `@syspilot.design` | Even bugs go through the analysis |
| Refactoring | `@syspilot.design` | Ensures specs stay aligned |
| Change Document is approved | `@syspilot.implement` | Follows the design agent |
| Implementation is done | `@syspilot.uat` | Follows the implement agent |
| "Are my specs consistent?" | `@syspilot.mece` | Independent, any time |
| "Is this requirement fully covered?" | `@syspilot.trace` | Independent, any time |
| All changes merged, ready to ship | `@syspilot.release` | After change workflows |
| Setting up syspilot in a project | `@syspilot.setup` | One-time or update |


## Workflow Diagram

The complete agent interaction model:

```{mermaid}
flowchart LR
    A["Issue / Idea"] --> change

    subgraph CW ["Change Workflow (loop)"]
        change --> implement --> uat
        uat -- "fix & retry" --> change
    end

    uat --> docu
    docu --> decision{"Another change?"}
    decision -- yes --> change
    decision -- no --> release["Release workflow"]

    subgraph QW ["Quality (any time)"]
        mece --> findings1{"findings?"}
        trace --> findings2{"findings?"}
    end

    findings1 -- yes --> change
    findings2 -- yes --> change
```

---

*For the Product/Instance architecture, see [architecture.md](architecture.md).
For file organization details, see [methodology.md](methodology.md).*
