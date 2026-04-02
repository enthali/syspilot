# Workflows: The syspilot Process

## Overview

syspilot is a **process framework** for spec-driven development. It defines three
workflows that cover the full lifecycle of specifications and code:

| Workflow | Purpose | Agents | When to use |
|----------|---------|--------|-------------|
| **Change** | Evolve specs and code | change → implement → verify → memory | Every feature, fix, or refactor |
| **Quality** | Check specification health | mece, trace | Any time, independently |
| **Release** | Bundle and publish | release | After changes are merged |

Each workflow is a defined sequence of agent invocations. You always know which
agent to call next.


## The Change Workflow

The Change Workflow is the primary development loop. Every change — from a new
feature to a bug fix — follows this sequence:

```{mermaid}
flowchart LR
    change --> implement --> verify --> memory
    memory --> next["Next change or<br/>release workflow"]
    change -.-> next
```

### @syspilot.change — Analyze

**Input:** A change request (GitHub issue, verbal description, or idea)

**What it does:**
1. Creates a **Change Document** in `docs/changes/`
2. Analyzes impact **level by level**:
   - **Level 0 (User Stories):** Which user goals are affected? New scenarios?
   - **Level 1 (Requirements):** Which requirements change? New acceptance criteria?
   - **Level 2 (Design Specs):** Which technical specs need updating?
3. Asks for your approval at each level before proceeding
4. Performs horizontal consistency checks (MECE) at each level

**Output:** An approved Change Document with all affected IDs listed

**Key principle:** The Change Agent never modifies code — it only analyzes and
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

### @syspilot.verify — Validate

**Input:** The same Change Document, after implementation

**What it does:**
1. Reads the Change Document and checks every requirement against the implementation
2. Verifies traceability: US → REQ → SPEC → Code
3. Validates that acceptance criteria are met
4. Runs the Sphinx build to check for broken links
5. Updates spec statuses from `approved` → `implemented`
6. Creates a validation report in `docs/changes/val-<name>.md`

**Output:** A validation report confirming (or flagging issues with) the implementation

### @syspilot.memory — Update Context

**Input:** Completed and verified changes

**What it does:**
1. Reviews what changed in the codebase
2. Determines if `copilot-instructions.md` needs updating
3. Updates project structure, conventions, or workflow descriptions as needed
4. Keeps the file concise — removes outdated info, adds new patterns

**Output:** Updated `copilot-instructions.md` (or confirmation that no update is needed)

**Key principle:** Memory is the last step because it captures the *result*
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

**Example:** `@syspilot.trace SYSPILOT_REQ_INST_LOCAL_SOURCE` shows the User
Stories above, the Design Specs below, and the code that implements it.


## The Release Workflow

The Release Workflow bundles completed changes into a versioned release.
It runs after one or more Change Workflows have been merged to main.

```{mermaid}
flowchart LR
    V["Version<br/>bump"] --> Val["Validate<br/>(build)"] --> N["Notes<br/>(generate)"] --> P["Publish<br/>(tag+push)"]
```

**`@syspilot.release`** handles the full process:

1. **Version bump** — Update `syspilot/version.json` with the new version
2. **Validate** — Run Sphinx build, check for broken links and schema violations
3. **Release notes** — Generate `docs/releasenotes.md` from Change Documents
4. **Archive** — Move Change Documents to `docs/changes/archive/<version>/`
5. **Publish** — Create Git tag and GitHub Release

**When to use:** After all planned changes for a version are merged and verified.


## Branching Strategy

syspilot uses chained feature branches with a release-only main:

```{mermaid}
gitGraph
    commit id: "v0.2.3"
    branch feature/local-install
    commit id: "change + specs"
    commit id: "implement"
    commit id: "verify"
    branch feature/concept-docs
    commit id: "change + specs "
    commit id: "implement "
    commit id: "verify "
    checkout main
    merge feature/concept-docs id: "squash merge (release)" type: HIGHLIGHT tag: "v0.2.4"
```

**Rules:**

| Rule | What | Why |
|------|------|-----|
| **One branch per change** | `@syspilot.change` creates `feature/<name>` | Isolates each change for independent review |
| **Chain from previous** | New branch starts from the latest feature branch, not main | Builds on previous work without merging first |
| **All work on branch** | Specs, code, tests, docs — everything commits to the feature branch | Clean history, easy to revert |
| **Main = releases only** | Squash merge to main happens only during `@syspilot.release` | Main always equals the latest release |
| **Tag on main** | Release creates `v{version}` tag on the squash merge commit | Tags mark published releases |

**Workflow:**

1. `@syspilot.change` → creates `feature/<name>` branch (from latest feature branch or main)
2. `@syspilot.implement` → commits code on the same branch
3. `@syspilot.verify` → commits validation report on the same branch
4. `@syspilot.memory` → commits copilot-instructions updates on the same branch
5. **Next change?** → branch again from the current feature branch
6. `@syspilot.release` → squash merge to main, bump version, tag


## When to Use Which Agent

| Situation | Agent | Notes |
|-----------|-------|-------|
| New feature request | `@syspilot.change` | Always start here |
| Bug fix | `@syspilot.change` | Even bugs go through the analysis |
| Refactoring | `@syspilot.change` | Ensures specs stay aligned |
| Change Document is approved | `@syspilot.implement` | Follows the change agent |
| Implementation is done | `@syspilot.verify` | Follows the implement agent |
| Verification passed | `@syspilot.memory` | Follows the verify agent |
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
        change --> implement --> verify
        verify -- "fix & retry" --> change
    end

    verify --> memory
    memory --> decision{"Another change?"}
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
