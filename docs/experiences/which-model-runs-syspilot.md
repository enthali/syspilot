# Which Model Runs syspilot?

**Topic:** What I've learned about model viability, cost, and running the whole agent workflow on cheap — ideally local — models, and how I plan to benchmark it.

## Versions

| Component | Version |
|-----------|---------|
| VS Code | 1.118 |
| Jarvis | 0.8.x |
| syspilot | 0.8.0 |
| Sphinx | 9.1.0 |
| sphinx-needs | 8.0.0 |

---

## The Question

syspilot runs a whole family of agents in sequence — Change Manager, Designer, Developer, MECE, Trace, QM, Docu, Release. Each one is a session driving a model. The obvious question a real user asks: *which model do I need, and what does it cost me per change?*

The lazy answer is "use the best frontier model everywhere." That answer kills adoption. If the only way to run syspilot is to burn frontier tokens on every mechanical trace check, then it's a toy for people with unlimited budgets. The interesting answer is: **stay model-agnostic, route each agent to the cheapest model that can still do its job, and reserve the strong models for the few steps that genuinely need reasoning.**

## What I Observed

**Viability tracks the "Agentic" score, not the headline coding/intelligence score.** Watching the QM loop across models, the pattern is consistent:

- Qwen3.6 35B A3B (agentic 21) — runs, but weakest; needs extra loops
- Nemotron 3 Ultra 550B (agentic 27) — barely gets through
- Qwen3.6 27B (agentic 27) — runs the full workflow with no drama
- Sonnet 5 (agentic 47) — flawless
- Haiku — intermittently struggles

The models that fail don't fail at *coding* — they fail at *being an agent*: following the workflow, calling the right tool, not derailing at a handoff. The headline coding/intelligence numbers mislead. The agentic benchmark predicts whether a model can even run the loop.

**Pass/fail is almost a useless metric here.** The QM loop is self-correcting. A viable model always converges eventually. So the real signals aren't "did it pass" but:

1. **Viability** — can the model run the full workflow at all without derailing? (This is what cheap models fail. Some can't even get through the first agent.)
2. **Efficiency** — for viable models: how many loops to converge, how much wall-clock, how much money. A strong model converges in fewer loops; Qwen ~35B is viable but adds a couple loops and runs slower — yet costs a fraction.

**Cheapest sticker price ≠ cheapest completed task.** Qwen 35B is the cheapest per token (~10× under Sonnet), but a "barely viable" model derails, hits loop caps, and needs babysitting — every extra loop erases the savings. My working hypothesis: **Qwen 27B is the robust sweet spot** — near-35B cost, meaningfully higher reliability, fewer restarts. Sonnet earns its 10× only on the reasoning-critical step (design decomposition) where one-loop convergence is worth it.

## The Local-First Thesis

Once a single ~27B model is viable, something bigger opens up. It runs locally — Qwen 27B on an AMD 395+ at ~20 t/s, sometimes beating cloud latency.

The economics are decisive. Local marginal cost is basically electricity — ≈€0 per loop once the hardware is sunk. A €13k RTX6000 Blackwell at 140 t/s is worth roughly 13,000 Qwen change-loops on OpenRouter. And here's the key insight: **syspilot's binding metric is convergence (loops), not throughput (tokens/sec).** The workflow is async, background, self-correcting — it can afford to be slow. 20 t/s for free beats 140 t/s for €13k.

Capex-only, no per-token meter, no data leaving the building — that's also the pitch for the market frontier-cloud tools structurally *cannot* serve: airgapped, regulated, defense, IP-sensitive. Single-local-model viability isn't just a cost optimization; for that segment it's feasibility-at-all.

So the design target is explicit: **one viable ~27B model, sequential agents, modest throughput.** Cloud and parallel setups are upside, not the baseline.

## The Blocker

There's one gate in front of all of this: the GH Copilot session timeout kills runs during cold KV/weight load. You can't generate local benchmark data until it's fixed. Likely fixes, cheap to costly:

1. Warm/prime the model outside the timed turn
2. Keep the model resident (keep-alive) so you pay KV load once per session, not per agent hop — biggest win for a multi-agent flow
3. Timeout config / own the harness — which is also the concrete argument for eventually moving off Copilot

Prove buckets 1–2 before reaching for 3.

## The Benchmark Plan

I don't want to act on any of the routing or model-choice claims above until I have data. So the next real investment is a benchmark harness, not more speculation.

**Fair comparison is non-negotiable:** one frozen start-state, one fixed change request, fed identically to every model. Enforce a loop cap (hitting it = efficiency failure, distinct from viability failure). Repeat runs per cell because sampling is nondeterministic.

**Two-tier measurement:** Copilot is a viability + loops + wall-clock tier only — its token model is opaque, so it can't give real cost. OpenRouter (and local) give real tokens, cost, and time. Report them in separate columns; don't fake comparability. As a cross-tier proxy, loops-to-converge × wall-clock transfers across tiers (3 loops / 40 min is expensive everywhere).

**Free telemetry already exists** — no new instrumentation needed to *diagnose* failures:

- The Jarvis message log shows the agentic flow, orchestration hops, and where a session stalled
- The Change Document git history shows where agents struggled (section churn, QM loop rounds as commits)
- Each agent's context.md before/after shows its conclusions and any drift

That turns "model X failed" into "derailed at the design→implement handoff, thrashed the spec file" — which tells me whether the fix is a prompt change, a task split, or rejecting the model.

**Apply routing discipline to the benchmark itself.** You run models you'd never deploy, so the benchmark's own cost is dominated by expensive models. Cheap/target models (Qwen 27B/35B, Nemotron) get full OpenRouter runs. Frontier models get viability + loops only via local/Copilot, with at most one OpenRouter full run as a calibration anchor. Prove the harness on the cheapest viable model first — don't debug plumbing with Sonnet money.

### Candidate benchmarks

- **esp32-distance** (leading, C / ESP32 firmware, QEMU emulation): task = add a temperature sensor from a user story; oracle = QEMU + acceptance script = *objective, executable* pass/fail. That objective oracle is its key advantage. Design musts: freeze the baseline as an immutable tag (syspilot already upgraded, feature absent — not a moving `main`); the syspilot upgrade and the feature-add are two separate tasks, so bake the upgrade into the baseline and measure only the add; pin the exact user-story text and feed it verbatim; keep the acceptance script model-blind (assert behavior, not implementation shape); make QEMU timing deterministic (a flaky oracle is worse than none).
- **jarvis** (second, TypeScript VS Code extension): complements esp32 with a different language and a software-architecture change shape. The pair becomes a go/nogo on agentic capability across two languages and two problem shapes.

## What This Is Not

This isn't a hobby compromise. The constraint profile — spare-time, hard spend limit, "move all I can to local" — *is* the target-user profile. SMB, regulated, and embedded shops can't burn frontier tokens either. Cheap-and-local-first is the product thesis, not a limitation.

## Where This Goes Next

1. Fix the Copilot timeout (the critical path — nothing local happens until this works)
2. Build the harness on esp32-distance, prove it stable on Qwen 27B
3. Add jarvis as the second problem shape
4. Only then spend OpenRouter dollars where the cost number actually informs a decision
