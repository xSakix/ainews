+++
title = "The Shortcut Inside a Model's Theory of Mind"
description = "Language models looked capable of following beliefs inside beliefs. HopToM shows that many benchmark questions let them answer by taking a shallower route, then offers a cheaper way to reason through the full chain."
tags = ["research", "agents"]
date = 2026-10-15T04:05:30+02:00
draft = false
+++

Imagine an operations room after a handover. Ana moved the key to the blue drawer. Boris saw her. Cara saw Boris leave before the move, while David only heard Cara describe what she thought Boris knew. Now an assistant must answer a narrow question: where does David think Cara believes Boris will look?

Ana, Boris, Cara and David are invented. The confusion is not. Agents that negotiate, teach, coordinate or act for people must separate the world from each person's view of it. A new preprint argues that the tests used to measure this skill have often made the puzzle easier than their labels suggest.

## A fourth-order question with a second-order exit

Theory of mind is the ability to reason about another person's knowledge, intentions or beliefs. Its higher-order form nests those perspectives: Alice believes that Bob thinks Carol knows something. Researchers have used such stories to ask whether language models can track several minds at once.

The new study, *Beyond Belief Nesting*, begins with a distinction that sounds technical and changes the result. The number of names or belief verbs in a question does not necessarily equal the amount of nested reasoning required to answer it. A nominally fourth-order question may depend on evidence that separates only two perspectives. The model can ignore the rest of the chain and still receive credit.

Shanshan You and colleagues call this order inflation. They define effective order by counting the distinct events needed to support successive belief prefixes. A test reaches full order only when every layer of the question depends on evidence that rules out a shallower solution.

That correction matters because earlier benchmarks established an appealing progression. HI-TOM, published in 2023, generated stories with increasingly nested beliefs and found that model performance declined as order rose. More recent methods then improved results by building explicit perspectives. RecToM recursively transforms a story through each character's point of view and reported perfect accuracy on HI-TOM with GPT-5.4 and Qwen3.5. The score looked like progress on deep social reasoning.

HopToM asks whether the test itself still permitted a shortcut.

## The fall after shortcuts disappear

The researchers built certified full-order questions and paired them with controls for lower-order alternatives. Under direct prompting, average accuracy across four frontier models dropped from 73.5 percent at first order to 20.0 percent at fourth order. Human participants also found the deeper questions difficult.

The decline alone does not prove that models lack a theory of mind. It shows that success on easier benchmark constructions cannot establish the stronger claim. A model may answer correctly because the story contains a clue close to the requested fact, because one person's perspective never diverges from reality, or because intermediate beliefs do not affect the answer.

The team then intervened on the evidence in the stories. A recurring error pattern followed support for shallower belief prefixes: models answered as though they had stopped at an earlier person's perspective. That result ties the failures to the structure of the reasoning problem rather than only to longer prompts or more names.

The finding also fits a broader change in theory-of-mind evaluation. OmniToM does not accept a final answer as the whole test. It asks models to extract explicit belief propositions and label their order, truth status, access to knowledge and mental source. Across its 895 stories and 22,343 labelled propositions, the authors found a bottleneck in turning narrative facts into actor-specific beliefs. A model may know every event in a story and still assign one event to the wrong mind.

## Write the perspectives once

HopToM does more than lower a score. The paper introduces HopTrace, an inference-time procedure that converts each interaction into a perspective record once. A deterministic resolver then follows those records through a nested query.

This approach avoids repeatedly asking a model to reconstruct the entire chain. On the benchmark's certified narrative questions, HopTrace improved fourth-order accuracy by 22.0 percentage points and fifth-order accuracy by 38.5 points over strong prompting baselines. It used 20 to 39 times fewer tokens than multi-call methods.

The combination is unusual. Reasoning aids often trade cost for accuracy by sampling more answers, asking several agents or producing longer chains of thought. HopTrace instead gives the model a representation that resembles an audit trail: who observed which event, what each participant could infer and which perspective the next hop must inherit.

That does not settle whether the model understands minds in a human sense. It changes the engineering question. An agent may not need a general faculty called theory of mind if its harness can maintain explicit, inspectable perspective records. The records can also reveal where the chain broke, which a correct final answer cannot.

## What the benchmark now demands

Higher-order belief tasks sit near practical failures in multi-agent systems. An assistant scheduling a meeting must distinguish what the organiser knows from what each attendee has received. A support agent must separate a customer's claim from an internal note and from another agent's summary. A negotiating agent must track beliefs that are incomplete, stale or deliberately asymmetric.

In each case, shallow agreement can hide a dangerous mistake. Several agents may produce accurate answers on average while sharing the same blind spot. Another preprint released this week, *Smart Alone, Blind Together*, argues that correlated errors decide whether a theory-of-mind module is safe for a team. Accuracy by itself cannot certify coordination when every participant fails on the same perspective boundary.

HopToM therefore changes what a convincing result should contain. The question must force every claimed order of reasoning. The evaluation should expose intermediate perspectives. Comparisons should include token cost, because a method that opens dozens of model calls may be unusable inside a working agent. Human difficulty should remain visible too: fourth- and fifth-order beliefs are hard cognitive work, not a routine language exercise.

The paper is a preprint. Its results need replication across more models, settings and natural interactions. Certified synthetic questions can isolate a mechanism, but real conversations contain ambiguity, deception and missing evidence that a generated story can control away.

Return to the imagined operations room. A capable assistant should not guess which drawer a character will name because the latest sentence mentions blue. It should preserve the view from each chair and show how the answer crossed from one mind to the next. The new benchmark makes every one of those crossings count.

## References

- Bawatneh, A., Sapkota, S., Bedi, A. S., Karmaker, S., & Shah, M. (2026). *OmniToM: Benchmarking Theory of Mind in LLMs via Explicit Belief Modeling*. https://arxiv.org/abs/2605.26322
- Beaumaster, S., & Schrater, P. (2026). *Smart Alone, Blind Together: Why Accuracy Fails to Certify Theory of Mind in Multi-Agent Teams*. https://arxiv.org/abs/2610.19051
- He, Y., Wu, Y., Jia, Y., Mihalcea, R., Chen, Y., & Deng, N. (2023). *HI-TOM: A Benchmark for Evaluating Higher-Order Theory of Mind Reasoning in Large Language Models*. https://arxiv.org/abs/2310.16755
- Lei, C., Hu, G., Yang, M., Jiang, Y., & Lipovetzky, N. (2026). *Mind the Perspective: Let's Reason Recursively for Theory of Mind*. https://arxiv.org/abs/2606.11724
- You, S., Wang, Z., Liu, H., Liu, Y., He, Y., Hao, X., & Wang, L. (2026). *Beyond Belief Nesting: Rethinking Higher-Order Theory of Mind in Large Language Models*. https://arxiv.org/abs/2610.17777
