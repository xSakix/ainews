+++
date = '2026-09-29T04:13:15+02:00'
draft = false
title = 'Firelex publishes Jeff decision models'
description = "The small open-weight models choose among supplied options. Their developer’s benchmark shows useful specialization and clear limits."
+++

Firelex, the developer account publishing Jeff, updated the project’s decision-model release and benchmark documentation on September 28, describing fast local classification from a single model evaluation.

Jeff takes a situation and a list of possible answers. It scores the choices instead of writing a response. Developers can use that narrower output to test routing and classification inside their applications.

**Why it matters:** Some software decisions need a label rather than a paragraph. A small local classifier could simplify that step and reduce its delay, provided the application still handles uncertain or incorrect decisions. The release is not evidence that a small model replaces general-purpose reasoning.

The project offers fine-tunes of Qwen3.5 and Gemma 4, existing model families, and uses the request format of Jev, a separate decision-model service. Compatibility describes the interface. It does not mean the independent Jeff project is the same service or has the same capabilities.

The developer reports median Jeff 0.8B inference times of 22 milliseconds on an RTX PRO 6000 graphics processor and 28 milliseconds on an Apple M4 Max using MLX, a local machine-learning framework. The timing sample contains 200 questions of roughly 200 tokens each. These are author measurements on specified hardware, not a promise for every deployment.

Its benchmark table covers 4,599 questions across five tasks. The reported aggregate accuracy is 79.1% for Jeff 0.8B, compared with 84.9% for AutoJev 27B. The README explicitly warns that the larger system’s reasoning is stronger and that some rival results use different published samples.

That directly limits the tempting claim that the tiny model matches the larger system overall. A win on an individual classification task can be useful without proving general parity. Combining unlike test samples also prevents a clean controlled comparison, even when the numbers appear together in one table.

For an application owner, the next step would be to test the actual labels and mistakes that matter. Misrouting an ordinary support ticket and misclassifying an urgent escalation need different treatment. An overall accuracy score can obscure that distinction, so a useful evaluation should preserve the results by category.

## A fast choice is still a choice that needs checking

Jeff returns scores for supplied options without generating an explanatory answer. In the project’s game examples, the model receives a textual state and descriptions of legal moves. This tests selection from prepared alternatives; it should not be presented as evidence of unrestricted visual game understanding or autonomous planning.

The distinction is practical. Suppose an application describes several actions and leaves out the safe action. A classifier can rank the supplied options, but the surrounding program still owns the list. The application should therefore define when to request clarification or decline to act instead of treating the highest score as sufficient authorization.

A probability output also invites a separate test. An evaluator could group decisions by confidence and check whether those groups are correct as often as the scores suggest. That would assess calibration on the deployment data rather than assuming that a useful benchmark average guarantees trustworthy confidence estimates.

The repository makes code available under the MIT license and describes model weights under Apache 2.0. It cautions that training datasets retain their individual licenses. Downloadable weights and executable examples help developers inspect the system, but the licenses for all ingredients should not be collapsed into one blanket description.

The strongest next evidence would be independently repeated measurements using identical questions, hardware and scoring rules, followed by a small application-specific trial. Jeff is worth evaluating as a specialized decision component. Its release is most informative when the narrow interface, latency conditions and reasoning limitations remain visible alongside its speed.

## Verification

| Claim group | Tier | Primary evidence |
| --- | --- | --- |
| September 28 documentation update | VERIFIED | [Dated repository commit](https://github.com/firelex/jeff/commit/985797fa2040d1c7a14822a96123c055800d5d09) |
| Architecture, interface, families, examples and licensing | VERIFIED as documented project properties | [Jeff repository](https://github.com/firelex/jeff) |
| Latency, samples and accuracy comparisons | PARTIALLY VERIFIED — author-reported, different comparator samples | [Benchmark and limitations in README](https://github.com/firelex/jeff) |
| Calibration, escalation and application examples | Analysis and proposed tests | Inference from the documented input/output contract |
