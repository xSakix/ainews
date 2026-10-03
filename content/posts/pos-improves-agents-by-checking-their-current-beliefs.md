+++
title = "PoS improves agents by checking their current beliefs"
description = "The framework tracks what an agent believes, what remains unknown and whether actions make progress. Its benchmark gains come from maintaining that state, rather than retaining more history."
tags = ["research", "agents"]
date = 2026-10-03T05:49:20+02:00
draft = false
+++

PoS, a framework from Nankai University, Alibaba Group and Tsinghua University, improves long-running agents by maintaining and checking an explicit account of the current world rather than relying on accumulated conversation history.

Yu Luo and colleagues organize that account around what the agent knows, what it still needs to learn and what it still needs to accomplish. They check proposed updates against evidence and redirect the agent when its activity stops producing progress.

**Why it matters:** A developer diagnosing a stalled agent can inspect the working assumptions driving its next action. PoS makes those assumptions an editable record, allowing the system to repair a mistaken state or stop repeating an unproductive investigation.

The [preprint](https://arxiv.org/abs/2610.01415), first submitted on 1 October, reports the highest overall performance among compared methods on four benchmarks with each of three language-model backbones. The comparisons cover goal-directed execution and evidence-seeking diagnosis, two tasks in which remembering a past observation is different from knowing what is currently true.

A history records the sequence of actions and observations. A current-state record reconciles that sequence: an object may have moved, an earlier hypothesis may have been ruled out, or a requirement may already have been met. Retaining more history still leaves the agent to reconstruct those relationships at every decision.

PoS maintains entities, their states and their relationships alongside unfinished requirements. It distinguishes missing information from an unfinished action. That separation matters because a diagnosis needs a discriminating observation, whereas an execution task may need a concrete change in the environment.

The framework resembles a maintained case board rather than a box of interview transcripts. New evidence updates the board, unresolved questions remain visible and incompatible entries can be challenged. The underlying language model still supplies the interpretation, so the board’s contents require validation.

After each action, the task agent proposes an update. A checking component reviews new or modified entries for contradictions within the record and against available observations. The task agent then revises the proposal before committing the updated state. A belief can therefore be rejected even when it sounds plausible in isolation.

## Recovery distinguishes uncertainty from unfinished work

PoS also selects an active unresolved requirement to guide the next action while retaining the wider task context. It monitors whether requirements persist, whether recent steps make progress and whether the same relevant world state keeps recurring.

Those signals identify stalled activity that the paper calls belief trapping. Recovery depends on both the pattern of stagnation and the type of unresolved requirement. An agent circling around a diagnostic uncertainty needs evidence that separates explanations; repeating an ineffective operation calls for a change in execution.

A reported incident-diagnosis example illustrates the distinction. The agent could not tell whether slow inventory requests arose from database waiting or processing inside the Java virtual machine. After detecting stagnation, PoS directed it toward discriminating evidence; CPU observations combined with earlier garbage-collection evidence supported a revised diagnosis.

The experiments use Qwen3.7-Plus, Kimi-K3 and GLM-5.3 consistently across each framework’s model-based components. Baselines include complete raw history, compressed memory, hierarchical memory and another explicitly maintained task-state harness. PoS led all twelve benchmark–backbone combinations in the authors’ main table.

Removing update validation or stagnation recovery reduced performance. The effects differed between execution and diagnosis, supporting the authors’ claim that the components address different failures. Compression-based alternatives also sometimes scored below raw history, demonstrating that organizing context can lose information as well as reduce repetition.

The improvement has a cost: maintaining and validating the state adds work, and the authors acknowledge dependence on task and domain knowledge. Correct context cannot supply a missing operational skill or medical understanding. Their clinical benchmark is an agent diagnosis evaluation, not evidence of clinical deployment.

The results remain author-reported and the manuscript is a preprint. The team supplies [code](https://github.com/luoyu100/PoS) and a [project description](https://luoyu100.github.io/projects/progression-of-states/project/). Its own failure analysis leaves a concrete boundary: some agents acquired correct evidence and still misinterpreted it because they lacked the knowledge needed to act on that evidence.

## Verification

| Claim | Label | Primary source | Independent check |
|---|---|---|---|
| Luo and coauthors’ Nankai/Alibaba/Tsinghua affiliations; v1 submitted 1 October 2026. | VERIFIED | https://arxiv.org/abs/2610.01415 | none |
| Highest main-table performance across four benchmarks and Qwen3.7-Plus, Kimi-K3, GLM-5.3; twelve combinations. | VENDOR-REPORTED | https://arxiv.org/abs/2610.01415 | none |
| Explicit entities/states/relations, information/action gaps, validated updates, active gap and stagnation/recurrence recovery describe the method. | VERIFIED | https://arxiv.org/abs/2610.01415 | none |
| Reported inventory-service example uses CPU/garbage-collection evidence to distinguish JVM processing from database waiting. | VENDOR-REPORTED | https://arxiv.org/abs/2610.01415 | none |
| Baseline types, model consistency, removal-test effects and occasional raw-history advantage. | VENDOR-REPORTED | https://arxiv.org/abs/2610.01415 | none |
| Maintenance costs, domain-knowledge dependency and clinical interpretation failures are stated limitations. | VERIFIED | https://arxiv.org/abs/2610.01415 | none |
| Code and project pages supplied. | VERIFIED | https://github.com/luoyu100/PoS ; https://luoyu100.github.io/projects/progression-of-states/project/ | none |
| Developer consequence and case-board analogy explain inspectable current assumptions. | ANALYSIS | https://arxiv.org/abs/2610.01415 | none |
