+++
title = "PyRUA-Lean cuts robot-agent calls with executable code"
description = "The robot interface performs checks and retries inside Python before returning to the language model. The authors report better simulated success and lower token use."
tags = ["research", "agents"]
date = 2026-10-03T05:47:20+02:00
draft = false
+++

PyRUA-Lean, a robot-control interface built around executable Python, used 65% fewer input tokens than tool calling on simulated tasks both systems completed, while also improving overall success.

Ruiyang Si and colleagues at Peking University, the National University of Singapore, NVIDIA and Impossible Research changed how a language-model planner controls existing robot skills. The planner writes short programs that handle intermediate checks and retries before it needs another model call.

**Why it matters:** A robotics developer paying for a planner’s repeated observations can move routine execution into code. The study measures that trade while holding the planner and underlying robot skills constant, tying the saving to the interface rather than a stronger language model.

The [preprint](https://arxiv.org/abs/2610.01939), first submitted on 1 October, compares PyRUA-Lean with a tool-calling agent using the same GPT-6 Astra planner. Across 700 simulated task instances, reported success rose from roughly 63% to 72%, an improvement of about nine percentage points.

The percentage in the paper’s title is a relative increase. The token saving uses a different denominator: only instances that both agents solved. Keeping those two groups separate matters because a fast failed attempt and an efficiently completed task are different outcomes.

Tool calling returns control to the planner after an operation. A later action that depends on the result can require another model invocation, and images or intermediate outputs accumulate in the conversation. Each invocation can process much of that growing record again.

PyRUA-Lean instead keeps a persistent Python state. Generated code can invoke a movement, inspect its result and choose a retry before returning control. Only explicitly printed outputs and requested camera images enter the planner’s context. The program acts like a supervisor following an agreed routine while calling the specialist back for a decision that needs interpretation.

The interface composes classical robot operations and learned vision-language-action policies, which translate observations into movements. It does not replace those policies with newly trained robot skills. Both sides of the comparison use the same underlying implementations and receive the same operating guides where available.

## Fewer model calls carry most of the saving

The evaluation spans three robotics benchmark collections: LIBERO-PRO, RoboTwin 2.0 and RoboCasa365. These cover perturbed manipulation tasks, dual-arm tasks and household tasks. Each task runs under five environment seeds, producing paired instances for the two agents.

Both planners face equal limits on language-model calls and time. Those limits count planner invocations rather than individual robot operations. Code can consequently perform several dependent operations within one invocation, preserving more of the budget for later decisions.

On instances solved by both systems, the authors report 49% fewer model calls alongside the 65% reduction in cumulative input tokens. Fewer invocations account for most of the saving. Selective feedback also helps, but the study evaluates the interface as a whole rather than isolating every component’s contribution.

The benefit varies by task. Savings were smaller on atomic RoboCasa365 tasks, where a learned policy already completes much of the work and the initial prompt contributes a large share of input. PyRUA-Lean’s larger interface description offsets part of the reduction in repeated calls there.

Failures also complicate the success comparison. Among instances only PyRUA-Lean solved, some tool-calling runs exhausted their call budget while others failed before reaching it. The latter group includes scripted recovery, geometric reasoning and variation in whether a learned robot policy happened to succeed.

These are author-reported preprint results from simulation, with one run per agent on each instance and one planner family. Physical-robot behavior and repeat-run variation remain outside the evaluation. The team’s [code repository](https://github.com/DAGroup-PKU/PyRUA-Lean) accompanies the paper; its stated follow-up is to measure physical execution and recovery latency and examine reuse of validated routines across episodes.

## Verification

| Claim | Label | Primary source | Independent check |
|---|---|---|---|
| Si and collaborators’ listed affiliations and v1 submission on 1 October 2026. | VERIFIED | https://arxiv.org/abs/2610.01939 | none |
| 700 paired simulated instances; same GPT-6 Astra, primitives, policies and call/time budgets; five seeds per task. | VENDOR-REPORTED | https://arxiv.org/abs/2610.01939 | none |
| Success 63.1% to 71.7%, +8.6 percentage points or about 14% relative; shared-success episodes use 49% fewer calls and 65% fewer input tokens. | VENDOR-REPORTED | https://arxiv.org/abs/2610.01939 | none |
| Python composes operations/checks/retries in persistent state; only requested images and printed output enter context. | VERIFIED | https://arxiv.org/abs/2610.01939 | none |
| Three benchmark collections, smaller atomic-task gains, larger API description, mixed explanations of exclusive successes and study limitations. | VENDOR-REPORTED | https://arxiv.org/abs/2610.01939 | none |
| Code provided; physical latency/recovery and cross-episode routine reuse named as follow-up. | VERIFIED | https://github.com/DAGroup-PKU/PyRUA-Lean ; https://arxiv.org/abs/2610.01939 | none |
| Developer consequence and supervisor comparison explain moving repeated execution out of planner calls. | ANALYSIS | https://arxiv.org/abs/2610.01939 | none |
