+++
title = "A model cannot tell which question will change its mind"
description = "A new study finds that language models cannot reliably name the cruxes that drive their conclusions. Finding them requires many rollouts, not one confident explanation."
tags = ["research", "models"]
date = 2026-10-17T04:18:00+02:00
draft = false
+++

Imagine an analyst asking a model whether a proposed software migration should proceed. The model says yes and offers three reasons. Asked what fact could reverse its recommendation, it points to database throughput. In this illustrative case, repeated runs reveal that throughput barely matters. The recommendation flips when the model changes its assumption about rollback time, a factor it never named.

A new preprint turns that mismatch into a measurable object. Its authors call the decisive sub-question a crux: a point on which a model's own reasoning paths disagree and whose answer can change the final conclusion. They ask whether a language model can identify those cruxes before it reasons, or after it has produced one chain of thought. It generally cannot.

The result cuts against a comfortable habit in human-AI work. We often ask a model to explain what matters, then use that explanation to decide what to verify. If the explanation does not track the variables that actually control the model's answer, the verification budget goes to the wrong place.

## From explanation to behavioural test

The paper does not define a crux as whatever a model calls important. It looks across many rollouts of the same problem. Different samples expose disagreements in intermediate answers; the researchers then test whether resolving one of those disagreements would change the conclusion.

That definition makes the claim behavioural. A sub-question matters because the model's output moves when its answer moves, not because the model writes a persuasive paragraph about it. The distinction resembles stress-testing a program rather than accepting its comments as documentation.

The authors compare three routes. An a-priori route asks the model to predict its cruxes before solving the problem. A single-rollout route lets it reason once and then identify the crucial points. A many-rollout route searches for disagreements across sampled solutions and measures which ones can flip the final result.

The first route had little relation to the factors that later proved decisive. One completed chain of thought did not fix the problem. Only the repeated-rollout procedure reliably surfaced useful cruxes.

This is not merely another finding that explanations can be wrong. The model is being asked for something narrower and more operational: which missing answer would change its own mind. Failure there means a system can sound calibrated while directing an operator away from the test that matters.

## Why one chain is not enough

One reasoning trace shows one route through a problem. It does not reveal the routes the model might take under sampling, nor the assumptions that vary between them. A factor can look central in the visible trace yet be stable across all runs. Another can appear as a minor detail but split the sampled conclusions.

Repeated sampling has long been used to improve answer accuracy through self-consistency: generate several reasoning paths and select the answer that appears most often. The crux method uses variation differently. Disagreement is not noise to average away. It is evidence about the decision boundary.

The cost is obvious. Generating and judging many solutions can be far more expensive than asking once. The researchers replace an LLM judge with a reranker and report making the procedure about 86 times cheaper. That reduction turns a research instrument into something closer to a practical diagnostic, but it does not make it free. A high-stakes decision may justify the extra inference; an ordinary chat response may not.

The method also depends on the sampled rollouts exploring meaningful alternatives. If every run repeats the same hidden assumption, no disagreement exposes it. A discovered crux belongs to this model, prompt and sampling procedure. It is not automatically the objectively decisive fact in the outside world.

## What changes for agents and reviewers

Agent systems increasingly ask one model to plan and another to review. A planner may list “key uncertainties”; a reviewer may check them and approve the result. The paper suggests that this neat division can inherit the planner's blind spots. A self-reported uncertainty is not the same as a behavioural crux.

For expensive or consequential tasks, a stronger workflow would sample several plans, locate the disagreements that alter the recommendation, and spend tools or human attention there. In software work, the crux might be whether a migration can roll back under load. In research, it might be whether one cited result applies to the present population. In an investment memo, it might be an assumption about refinancing rather than the market-size estimate that dominates the prose.

The finding also sharpens the meaning of model self-knowledge. A system can state a conclusion, describe a plausible route and name what it believes matters while remaining unable to predict what actually controls its own future outputs. Fluent introspection is not reliable introspection.

That does not make explanations useless. They can expose premises, communicate a proposed argument and help a person notice missing evidence. The paper shows why an explanation should be treated as another model output to test, not privileged access to the mechanism that produced the answer.

Return to the illustrative migration decision. The analyst could spend a day benchmarking throughput and still leave the recommendation unstable. Several sampled plans would reveal that rollback time is where the model divides. The useful question is no longer “What do you think matters?” It is “Across the ways you might reason, which answer actually changes the result?”

## References

- Reber et al. (2026). *Can LLMs Anticipate Their Cruxes?* https://arxiv.org/abs/2610.21006
- Wang, X., et al. (2023). *Self-Consistency Improves Chain of Thought Reasoning in Language Models*. https://arxiv.org/abs/2303.08896
