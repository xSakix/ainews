+++
title = "Planning agents acted before checking whether they could"
description = "A formal test found older language-model agents solved fewer tasks when acting than when writing complete plans. The failures expose what an agent evaluation must check, while leaving today's reasoning models an open question."
tags = ["research", "agents", "safety"]
date = 2026-10-21T05:28:36+02:00
draft = false
+++

A red block sits under a blue one. At a teaching bench, a student reads the assistant's instruction to lift the red block and pauses, because the blue block has nowhere to go. This is a fictional classroom moment, built from the rules of a planning task. The instruction sounds ordinary. The state of the little world makes it impossible.

## Every action has a precondition

That distinction drives a preprint published on 15 October by Oriol Miro-Lopez-Feliu and colleagues at the Barcelona Supercomputing Center, the Universitat Politècnica de Catalunya, the University of Amsterdam and Safe AI Netherlands. They ask whether the systems called planning agents can actually satisfy the conditions attached to their actions.

Their strongest offline configuration solved 31 of 40 solvable problems. Their strongest interactive agent solved 16. Both used GPT-4o. Writing the whole plan before acting worked substantially better in these tests than choosing successive actions through tools.

The experiment concerns four older, non-reasoning models: GPT-4o, GPT-4o-mini, Gemini 2.0 Flash and Flash-Lite. The authors chose them deliberately because the prompting methods under examination were developed for that class of model. The results do not establish the failure rate of current frontier reasoning systems.

What makes the study useful is the judge. Each natural-language task rests on a hidden model written in PDDL, a language used in automated planning. That model defines which actions are available, their prerequisites and how they change the world. A validator can therefore check the route to the goal, rather than accept a persuasive explanation of arrival.

The suite contains 50 tasks across five domains, including block manipulation, transport and two new domains. Forty tasks have solutions; ten do not. A system can fail by making an illegal move, stopping before the goal or failing to recognise that no sequence of allowed moves can succeed. Those outcomes are recorded separately.

## The opportunity to look went unused

In the offline condition, the model receives a complete description and returns a plan. The interactive condition lets it inspect the task, list objects, read the action catalogue and query the current state. It then chooses what to do next.

Inspection does not change the world. An applicable action does. An action whose prerequisites are false ends the episode immediately. This is a deliberate safety assumption: the experiment treats an invalid commitment as something the agent cannot simply undo and retry.

The researchers gave agents enough calls to retrieve the task, inspect the state before every step of an optimal plan and submit a result. They also show that a successful offline plan could fit within the interactive budget. Access to tools did not intrinsically require a worse result.

Yet only 7.3% of actions were preceded by a fresh state query. In 58% of episodes where agents took any action, they never queried the state at all. They often committed using a picture of the world they had not checked.

Precondition violations ended roughly two-thirds of solvable interactive episodes. The authors interpret the pattern as consistent with overconfident commitment, but distinguish interpretation from proof. Rare inspection explains why agents failed to exploit information; it does not, by itself, fully explain why they fell below offline planners that never inspected anything.

This precision matters. A benchmark can locate a failure without proving the psychological explanation suggested by its name.

## More deliberation did not provide a reliable repair

The team compared six offline prompting strategies and three interactive architectures. The latter included a basic ReAct loop, a version with reflective memory and a version in which another model call criticised proposed actions.

Neither addition improved success over ReAct for any tested model. The critic saw the same history as the actor and could not query the world independently. Rejecting a proposed action consumed a call, so criticism also created another way to run out of budget.

Offline, chain-of-thought and Plan-and-Solve helped some models. GPT-4o rose from 57.5% with direct prompting to 77.5% with chain-of-thought. But none of the within-model improvements survived correction for multiple comparisons. With only 40 solvable tasks, the study could reliably detect only large differences; the authors do not equate an inconclusive statistical test with proof of no benefit.

Some expensive strategies were less ambiguous about their cost. Self-Refine used about five times as many tokens as direct prompting, and Tree of Thoughts about 22 times. The extra computation did not produce a corresponding general improvement in success.

The unsolvable tasks revealed a different weakness. Across 360 episodes involving impossible goals, systems recognised impossibility only 32 times. False declarations of impossibility were almost absent on solvable tasks. These models tended to keep attempting the assignment even when the correct answer was to stop.

## A boundary earlier planning research already identified

The work extends a longstanding effort to distinguish planning from plausible recollection. PlanBench, introduced by Karthik Valmeekam and colleagues and published in the NeurIPS 2023 datasets track, builds on domains from automated planning so evaluations can test actions and changes systematically. Familiar everyday instructions alone make it difficult to tell whether a model has worked out a valid sequence.

Subbarao Kambhampati and colleagues' 2024 LLM-Modulo position paper proposes combining language models with external, model-based verifiers. The language model can contribute candidate solutions and knowledge; a separate checking system carries responsibility for correctness. Their proposal includes interaction between the two components, rather than a single unchecked answer at the end.

The new study reaches a compatible engineering recommendation: intercept inapplicable actions with a validator. It does not demonstrate that adding such a gate makes these agents successful. Turning a fatal mistake into recoverable feedback would change the experiment, and whether the agent then recovers remains an open question.

The limits are substantial. Each configuration ran once. The worlds are deterministic, fully observable and single-agent. Some methods were adapted: reflective memory operated within one episode, and the critic had no tools. Real applications may allow recovery, while newer reasoning models may use inspection differently. Those differences need testing rather than extrapolation from this score.

At the fictional teaching bench, the student sets the instruction aside and checks what is on top of the red block. The task has not become harder. One prerequisite has become visible. Before the next instruction moves anything, she wants the system to check it too.

## References

- Kambhampati, S., Valmeekam, K., Guan, L., Verma, M., Stechly, K., Bhambri, S., Saldyt, L. P., & B Murthy, A. (2024). *Position: LLMs Can’t Plan, But Can Help Planning in LLM-Modulo Frameworks*. https://proceedings.mlr.press/v235/kambhampati24a.html
- Miro-Lopez-Feliu, O., Miró López-Feliu, O., Gimenez-Abalos, V., Vazquez-Salceda, J., Carballo Araruna, V., & Alvarez-Napagao, S. (2026). *Testing the Planning Claims of LLM-Based Agents against Formal Semantics*. https://arxiv.org/abs/2610.22469
- Valmeekam, K., Marquez, M., Olmo, A., Sreedharan, S., & Kambhampati, S. (2023). *PlanBench: An Extensible Benchmark for Evaluating Large Language Models on Planning and Reasoning about Change*. https://arxiv.org/abs/2206.10498
