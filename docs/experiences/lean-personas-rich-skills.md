# Lean Personas, Rich Skills

**Topic:** What a paper on expert personas taught me about how to write syspilot's agent prompts — and why it reinforces the "agents are processes, skills are knowledge" split.

## Versions

| Component | Version |
|-----------|---------|
| VS Code | 1.118 |
| Jarvis | 0.8.x |
| syspilot | 0.8.0 |
| Sphinx | 9.1.0 |
| sphinx-needs | 8.0.0 |

---

## The Read

[Expert Personas Improve LLM Alignment but Damage Accuracy: Bootstrapping Intent-Based Persona Routing with PRISM](https://arxiv.org/html/2603.18507v1)

This one is directly relevant because syspilot's agents *are* personas — "You are the Change Manager," "You are the Dev Engineer." Every agent file opens with a role identity. So a paper measuring what personas actually do to model behavior is measuring something I do on purpose, at scale, in a pipeline.

## What the Paper Shows

The headline is not "personas good" or "personas bad." It's that the persona effect is **task-type dependent**:

- Expert personas reliably **help alignment-shaped tasks** — format-following, tone, structure, intent-following, safety refusal.
- They reliably **hurt pretraining-dependent tasks** — factual recall, zero-shot math, and — notably — **coding was the single worst-hit category (−0.65).**
- **Longer personas amplify both effects.** A minimal persona ("You are a mathematician.") damages least; an elaborate one helps alignment most but hurts knowledge most.
- The effect scales with how instruction-tuned / system-prompt-optimized the model is. For reasoning-distilled models the identity itself barely matters — the gains come from the *added structured context length*, not from the "expertise."

## Where It Bites syspilot

syspilot's agents split cleanly along exactly the axis the paper cares about:

- **Alignment-shaped agents** — CM, PM, Docu, Release, MECE, Trace, Setup. Their job *is* format-following, structured output, workflow adherence, traceability discipline. This is precisely where personas help. Keep them rich.
- **Knowledge/correctness agents** — the Dev/Implement agent, and the reasoning-heavy parts of Design. This is where the warning lands hardest. A verbose "You are a senior software engineer with deep expertise in Python, Java, C++…" preamble is the exact pattern the paper measured degrading coding accuracy. The persona isn't buying correctness — the model's pretrained coding ability is — and the elaborate role text may actively distract from it.

## The Caveat That Keeps It a Hypothesis

The study is on 7–8B open models, with system-prompt personas that interact with instruction-tuning at the weights level. The frontier models I actually run are far larger and RLHF-heavy; the authors explicitly flag that 70B+ generalization is *untested*. So this is a hypothesis to probe against my own stack, not a proven law. (It also pairs naturally with the model-viability benchmark — see [Which Model Runs syspilot?](which-model-runs-syspilot.md) — because the persona effect may differ across the small local models I care about deploying.)

## Why It Reinforces the Methodology

This isn't a new principle — it's empirical support for one already in syspilot's methodology: **agents are stable processes (WHAT / procedure), skills are the exchangeable knowledge bindings (HOW).** The paper says the same thing from the other direction: for correctness work, tokens are better spent on workflow steps and spec context than on a flattering "world-class expert" identity. Keep the persona lean; push domain substance into skills and task context.

## Cheap Experiments to Try (not changes yet)

1. **Trim persona verbosity on the Dev/Implement agent** and check whether implementation quality holds or improves. The paper predicts short identity + rich *task* context beats a long "distinguished expert" preamble for correctness work.
2. **Keep rich personas on the orchestration/format agents** (CM, Docu, Release) — that's where verbosity pays off.
3. Frame correctness-critical prompts as **task + procedure heavy, identity light.** Since reasoning models gain from structured context rather than "expertise," spend the tokens on the steps and the spec, not the role.

## Where This Goes Next

A small A/B on the Implement agent's persona length is a candidate CR — but it's gated on the benchmark harness existing, because "did coding accuracy improve" needs an objective oracle to measure against. So: harness first, then run persona-length as one of the first questions it answers.
