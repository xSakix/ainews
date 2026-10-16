+++
title = "The answer was still inside the model"
description = "A study of 15 language models finds that many working-memory failures happen after the right item is selected. The models retain decodable information but fail to report it."
tags = ["research", "models"]
date = 2026-10-16T04:07:00+02:00
draft = false
+++

Imagine a model shown a short list of symbols, then distracted by a second list before it must name the original target. It answers with the distractor. The obvious diagnosis is that the first symbol has vanished. In this illustrative scene, however, an internal probe can still read the target almost perfectly. The answer was not erased. Something went wrong between holding it and saying it.

That distinction drives a new preprint on working memory in language models. Its authors tested 15 models ranging from 70 million to 14 billion parameters on tasks designed to create interference. They found that attention heads often selected the correct target even when the model's final answer was wrong. Simple probes could decode the target from hidden states with near-perfect accuracy on many failures.

The result challenges a familiar shortcut in model evaluation: treating a wrong output as evidence that the underlying information is absent. The paper instead separates three operations that a single accuracy score collapses—selecting a relevant item, preserving its identity and reading it out as an answer.

## A controlled memory problem

Working memory is not long-term storage. It is the temporary ability to hold information in a usable state while other material competes for attention. Human experiments often reveal that the item remains partly available even when a participant reports the wrong one. Similar interference can make two memories hard to distinguish without destroying either.

The researchers constructed tasks that let them vary the target, the competing items and their positions. They then looked inside the models at the points where the target should be selected and carried forward. The models covered several scales and families, which matters because a pattern in one checkpoint can be an architectural accident rather than a general mechanism.

On correct trials, the expected story held: attention focused on the target and the final layers produced the right token. On many incorrect trials, the first half of that story still held. Target-selecting heads attended to the right position. Hidden-state probes retained enough information to identify the target. Yet the output reflected a competitor.

A probe is evidence of decodability, not of use. A classifier trained after the fact may extract information that the model's own computation cannot access. The authors therefore went beyond reading states and intervened on them.

## Turning down the competitors

The key causal test suppressed representations of non-target identity. That intervention improved sensitivity, measured as d-prime, in the direction predicted by an interference account. Weakening the competitors made the stored target easier for the model to report.

This does not mean every memory error is a readout error. Models can fail to encode an item, lose it, or select the wrong location. The paper's claim is narrower: a meaningful share of failures occur while target information remains internally available, and confusion among similar representations can block the final answer.

The distinction matters for engineering. Adding more context or repeating the target attacks a storage problem. It may do little when the model already holds the target but cannot separate it from competing content. A system facing that second problem may need different prompts, intermediate structure or architectural changes that sharpen identity at readout.

It also matters for interpretation. Transformer attention, introduced as a mechanism for relating positions in a sequence, is often inspected as if attention to the right token settled what the model knows. Here, attention can point to the target and still fail to deliver the correct output. Conversely, a wrong answer does not imply that attention missed.

## A human resemblance with limits

The authors frame the interference pattern as human-like, but the comparison is functional rather than biological. A transformer does not need a human memory system to display the same behavioural split between availability and report. Similar errors can emerge from very different machinery.

Scale also does not dissolve the problem. Testing models up to 14 billion parameters shows that the effect survives beyond tiny experimental networks, but it does not establish the same result in frontier systems with much larger parameter counts or proprietary post-training. The tasks are deliberately controlled. Real conversations mix retrieval, instruction following, planning and generation in ways that make the source of one failure harder to isolate.

Still, controlled tasks are the point. They let researchers change one competitor, observe one representation and test one intervention. The paper offers a method for asking a better question after a model is wrong: was the information never encoded, was it lost, or was it present but inaccessible to the output process?

Return to the illustrative symbol task. The model gives the wrong item, and an evaluator marks a failure. That verdict is correct at the product boundary. Internally, though, the system may have done most of the work. The next advance may not come from giving it a larger memory. It may come from teaching it how to read what it already kept.

## References

- Vaswani, A., et al. (2017). *Attention Is All You Need*. https://arxiv.org/abs/1706.03762
- *Working Memory Readout Bottlenecks in Language Models* (2026). https://arxiv.org/abs/2610.21176
