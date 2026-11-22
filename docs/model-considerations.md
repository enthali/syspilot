# Model Considerations

**Considerations updated:** 2026-11-20  
**Owner:** Technical Writer  
**Next monthly review:** 2026-12-20

Choose a model for the work an actor does, not simply the highest score on a
leaderboard. This guide explains the trade-offs and offers a dated starting
choice for the nine Syspilot actors, not a requirement to use these models or
proof that they fit every project task. Availability, prices, reasoning
settings, and observed cache reuse can change the choice.

The Technical Writer maintains this document and refreshes it monthly. Any
refresh that changes a model choice is agreed with the User before the Admin
adds or updates the agent files' `model:` lines. Editing this document does not
switch a running session's model.

## Default Selection Principles

- **Cognitive and orchestration tier (`Min Index ~55–60`, `CR 10, CW 0`):** Roles
  that resolve open-ended ambiguity, define specification boundaries, maintain
  shared process and tooling, or run sustained multi-turn sessions benefit from
  strong reasoning and zero cache-write cost (`Gemini 4 Carbon`, Index **60**).
- **Dissimilar review (`Min Index ~50`, `CR 10`):** Quality intentionally uses a
  different model family (`GPT-6.2 Sol`, OpenAI, Index **57**) from both
  specification/documentation (`Gemini 4`, Google) and implementation/testing
  (`MAI Code 2`, Microsoft) to reduce correlated blind spots (`GPT-6.1 Terra`,
  Index **51**, is the lower-cost fallback). Reassess family separation if the
  reviewed roles move to the same vendor family.
- **Structured execution tier (`Min Index ~50`, `CR 5, CW 0`):** Roles that
  turn a settled specification or checklist into code, requirement tests, or
  release operations across many tool calls run cheaply on **`MAI Code 2`**
  (`powerful` category, `CR 5, CW 0` during its 50% promo until `2027-05-18`),
  with **`GPT-6.1 Terra`** (Index **51**, `CR 5, CW 125`) as the benchmarked
  fallback when the promotion ends or when a task needs a benchmarked alternative.
- **Expository writing tier (`Min Index ~54–55`, `CR 7.5, CW 0`):** User-facing
  prose needs clear, natural writing and strict fidelity to authoritative
  sources (`Gemini 4 Hydrogen`, Index **54**, `CW 0`).
- **Subagent and bounded-task floor (`Min Index ~35`, `CR 1, CW 0`):** Short,
  cold-cache `explore` and `task` helper runs are dominated by initial cache
  writes and log output; **`MAI Code 2 Flash`** (`CR 1, CW 0`, 50% promo until
  `2027-05-18`) is the primary choice, with **`Claude Haiku 5.5`** (Index **36**)
  as the benchmarked fallback. Where Contracts, ontology checks, and automated
  tests guard the outcome, small well-bounded tasks can drop to this floor,
  escalating unresolved reasoning rather than retrying a cheap model.
- **Context discipline:** Keep sessions within default context where long-context
  surcharges apply: cached metadata doubles rates on `GPT-6/6.1/6.2` and
  quintuples them on `Haiku 5.5`, while `Gemini 4`, `MAI Code 2`, and `Claude
  Sonnet/Opus 5.5` list no separate long-context surcharge.

## Actor Model Mapping

`Min Index` is a soft selection floor for future re-mapping when cheaper models
cross that threshold, not a hard qualification gate. Index scores come from the
[Artificial Analysis leaderboard](https://artificialanalysis.ai/leaderboards/models)
on the date above; check the tested effort span when comparing runs.

| Actor | Min Index | Starting Model (Index) | Task Profile, Fallback, and Selection Rationale |
|---|---:|---|---|
| **Research** | ~60 *(task-dep.)* | `Gemini 4 Carbon` (**60**) | **Open-ended investigation and feasibility spikes:** Explores unfamiliar APIs, external ecosystems, and uncertain evidence before a specification exists (`~60` floor for open spikes; smaller models suffice for simple lookups). |
| **Architect** | ~55 | `Gemini 4 Carbon` (**60**) | **System design and formal specification:** Translates intent into user stories, requirements, architecture decisions, and ontology links; `Carbon` (**60**) matches `Sonnet 5.5`'s `CR 10` without `CW 250` (`Claude Sonnet 5.5` [**55**] is a capable alternative). |
| **Admin** | ~55 | `Gemini 4 Carbon` (**60**) | **Infrastructure, tooling, and process maintenance:** Maintains CI/CD, build scripts, skills, and shared agent configuration. Low token volume with wide project impact; `CW 0` keeps short infrastructure sessions cheap. |
| **Project Manager** | ~55 | `Claude Sonnet 5.5` (**55**) | **Interactive user dialogue, scope, and closure:** Primary synchronous partner for the User; prioritizes responsive turn latency and readable scoping (`Gemini 4 Carbon` [**60**, `CW 0`] is the lower-cost alternative when slower turn latency is acceptable). |
| **Quality** | ~50 | `GPT-6.2 Sol` (**57**) | **Independent cross-family review:** Audits specification, implementation, test evidence, and MECE/Trace analyses from a third vendor family (OpenAI) distinct from Google and Microsoft; compact review sessions keep `CW 250` overhead low (**fallback:** `GPT-6.1 Terra` [**51**]). |
| **Technical Writer** | ~54–55 | `Gemini 4 Hydrogen` (**54**) | **Audience-focused documentation and example sync:** Maintains guides, README, and documentation ownership links with strict fidelity to source owners at `CR 7.5, CW 0` (**fallback:** `Claude Sonnet 5.5` [**55**] or `Gemini 4 Carbon` [**60**]). |
| **Developer** | ~50 | `MAI Code 2` *(n/a, `powerful`)* | **Spec-driven implementation and unit verification:** Realizes settled specifications and unit tests across high file/diff volume at `CR 5, CW 0` (**fallback:** `GPT-6.1 Terra` [**51**]; escalate to `GPT-6.2 Sol` [**57**] or `Gemini 4 Carbon` [**60**] for complex concurrency or subtle stateful bugs). |
| **Tester** | ~50 | `MAI Code 2` *(n/a, `powerful`)* | **Adversarial requirement-based testing:** Designs and runs black-box tests from the specification to expose loopholes and edge cases; `CR 5, CW 0` keeps iterative test runs cheap (**fallback:** `GPT-6.1 Terra` [**51**]). |
| **Release** | ~50 | `MAI Code 2` *(n/a, `powerful`)* | **Methodical preflight, packaging, and publication:** Executes multi-step release checklists, archive checks, and release records across large cached contexts at `CR 5, CW 0` (**fallback:** `GPT-6.1 Terra` [**51**]). |
| *Subagents (`explore` / `task`)* | ~35 | `MAI Code 2 Flash` *(n/a, `lightweight`)* | **Short cold-cache helper runs:** Read-only searches and build/test command runners (1–4 turns), where `CW 0` and no long-context surcharge beat `CW 12.5` (**fallback:** `Claude Haiku 5.5` [**36**]). |

## Copilot Model Reference and Workload Cost

Rates are **Copilot Credits per 1M tokens** (not API dollar prices), read from
VS Code's cached `copilot` vendor metadata on 2026-11-20. The table is sorted
primarily by Copilot `Input` credits descending and secondarily by `AA Index`
descending, which orders capability tiers monotonically while slotting
unbenchmarked `MAI` models into their capability band. Bold rows mark primary
starting choices.

*Excluded from this active current-generation list: warning-flagged models with
planned deprecation notices (`MAI-Code-1.1-Flash`, `Gemini 3.8 Flash`, `Gemini
4 Argon`, `Kimi K3`) and deprecated, superseded, or unpriced routing entries
(`Claude Haiku 4.5`, `Claude Sonnet 5`, `GPT-4o mini`, `GPT-5.3-Codex`,
`GPT-5.4 nano`, `GPT-5.6 Luna/Sol`, `GPT-6 Sol/Astra`, `GPT-6.1 Sol`, `Auto`).*

| Model | GH Category | AA Index (Max) | Effort Span | Input | Output | Cache Read | Cache Write | Long-Context / Promo Note |
|---|---|---:|---:|---:|---:|---:|---:|---|
| GPT-6.2 Astra | `powerful` | 62 | 46–62 | 800 | 4000 | 40 | 1000 | 2× (`CR 80, CW 2000`) |
| Claude Opus 5.5 | `powerful` | 59 | 35–59 | 400 | 2000 | 20 | 500 | none |
| Gemini 4 Neon | `versatile` | 61 | 44–61 | 300 | 1500 | 15 | 0 | none |
| **Gemini 4 Carbon** | **`powerful`** | **60** | **54–60** | **200** | **1000** | **10** | **0** | **none** |
| **GPT-6.2 Sol** | **`powerful`** | **57** | **41–57** | **200** | **1000** | **10** | **250** | **2× (`CR 20, CW 500`)** |
| **Claude Sonnet 5.5** | **`versatile`** | **55** | **26–55** | **200** | **1000** | **10** | **250** | **none** |
| **Gemini 4 Hydrogen** | **`versatile`** | **54** | **27–54** | **150** | **750** | **7.5** | **0** | **none** |
| GPT-6.1 Terra *(fallback)* | `versatile` | 51 | 29–51 | 100 | 500 | 5 | 125 | 2× (`CR 10, CW 250`) |
| **MAI Code 2** | **`powerful`** | **n/a** | **–** | **100** | **500** | **5** | **0** | **none (50% promo until 2027-05-18 UTC; base In 200)** |
| Claude Haiku 5.5 *(fallback)* | `lightweight` | 36 | 19–36 | 10 | 50 | 1 | 12.5 | 5× (`CR 5, CW 62.5`) |
| GPT-6 Luna | `lightweight` | 28 | 9–28 | 10 | 50 | 1 | 12.5 | 2× (`CR 2, CW 25`) |
| **MAI Code 2 Flash** | **`lightweight`** | **n/a** | **–** | **10** | **50** | **1** | **0** | **none (50% promo until 2027-05-18 UTC; base In 20)** |

Promotional rates above already include the 50% discount; do not halve them
again or assume they hold past `2027-05-18`.

Estimate workload cost from the project's observed token buckets (if a usage
report bundles cached tokens inside total input, subtract them first):

```text
credits = (uncached_input * input_rate
         + cache_read * cache_read_rate
         + cache_write * cache_write_rate
         + output * output_rate) / 1,000,000
```

For illustration only — **not a measured project average** — 970,000 cache-read,
20,000 cache-write, 10,000 uncached input, and 2,500 output tokens (97% cache
read) cost **14.2** credits on `Carbon`, **19.2** on `Sonnet 5.5` or `GPT-6.2
Sol`, **7.1** on `MAI Code 2`, and **9.6** on `GPT-6.1 Terra`. Check your own
cache share, output volume, and long-context threshold before switching.

## Monthly Refresh: Steps 1 to 3

1. **Read Copilot credits and filter active models:** Query VS Code's SQLite
   database (`%APPDATA%\Code\User\globalStorage\state.vscdb` on default Windows
   installs; profiles and other OSes vary) **read-only** on `ItemTable` where
   `key = 'chat.cachedLanguageModels.v2'`. Filter `metadata` to `vendor ==
   "copilot"` (other vendors repeat display names with rounded numbers), read
   `name`, `category`, `inputCost`, `outputCost`, `cacheCost`, `cacheWriteCost`,
   `longContext*Cost`, and `promo`, and **exclude warning-flagged models**
   (`statusIcon.id == "warning"` or deprecation notices in `tooltip`) as well as
   deprecated/superseded generations and unpriced routing entries (`Auto`).
   *Fallback:* if the database or cost fields cannot be read, report what is
   missing, never substitute provider API dollar prices for Copilot Credits,
   keep the last dated table marked stale, and ask the User before proposing any
   change on incomplete data.
2. **Fetch benchmark scores and check project usage:** Read
   [leaderboards/models](https://artificialanalysis.ai/leaderboards/models) and
   [models/releases](https://artificialanalysis.ai/models/releases) (plus
   individual model pages when needed) for maximum Index scores, effort spans,
   and retirement warnings. Leave unbenchmarked models as `n/a`, sort the active
   table by `Input` credits descending then `AA Index` descending, and check
   cost against the project's observed token buckets (for example from
   `.syspilot/stats/` where available).
3. **Re-map roles, agree changes, and update agent files:** Match the refreshed
   table against the selection principles and role profiles above, keeping
   Quality on a separate vendor family from the roles it reviews. Agree every
   changed model choice with the User; only then hand the agreed changes to the
   Admin to add or update `model:` in `.github/agents/*.agent.md` using the
   environment's model completions (see the
   [VS Code model-preference reference](https://code.visualstudio.com/docs/agents/reference/custom-agent-file-reference#_model-preferences)),
   and verify effective selection on the next session start. Maintain a monthly
   heartbeat via the available scheduling facility, or tell the User and agree a
   manual reminder if scheduling is unavailable.

## Adoption During Setup

Setup asks the User whether to adopt this guide. Only on yes does it place
`docs/model-considerations.md` into the project's documentation and message the
Technical Writer to run steps 1 to 3 and set a monthly heartbeat. Setup changes
no `model:` line on any agent file, and adoption does not pre-approve later
model switches (the choice and delivery status are recorded in
`.syspilot/setup-contract.md`).
