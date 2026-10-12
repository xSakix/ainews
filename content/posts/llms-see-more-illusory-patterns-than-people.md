+++
title = "LLMs see more illusory patterns than people"
description = "A preprint finds that language models infer relationships from ambiguous evidence more readily than human participants. Its controlled tests connect the effect to frequency-sensitive internal features."
tags = ["research", "models"]
date = 2026-10-12T04:01:37+02:00
draft = false
+++

Language models formed stronger false patterns than people when both were asked to infer relationships from ambiguous evidence, according to a new preprint.

The authors adapted classic psychology experiments in which the observations contain no reliable association, yet people often perceive one. They gave matched tasks to human participants and several language models, then tested whether the models linked frequent positive descriptions with majority groups or constructed causal explanations from coincidental sequences.

## Why it matters

For an analyst using a model to interpret survey comments, incident reports or customer records, fluent pattern-finding can turn an uneven sample into a confident story. The study suggests that adding more observations does not necessarily correct the problem when raw frequency itself drives the inference.

The central comparison covers two forms of illusory pattern perception. In one, a majority group appears more often and therefore accumulates more positive and negative examples even though the proportions match those of a minority group. In the other, unrelated events are arranged so that a causal sequence is tempting but unsupported.

Across the reported experiments, models were more likely than human participants to endorse the misleading association or causal account. The exact size varied by task and model, so the paper's useful result is the direction and consistency of the gap rather than a single universal percentage.

The researchers also used sparse autoencoders, tools that turn a model's dense internal activity into a smaller set of interpretable features. They report that features associated with holistic frequency perception rose with the false-pattern response, while features associated with a more analytic orientation pulled the other way. This is a correlation inside the model, not proof that either feature causes the judgment.

## The comparison is controlled but narrow

The paper's strength is its direct human comparison. Both groups receive versions of the same evidence, and the tasks descend from established demonstrations in cognitive psychology. The authors also released code, allowing other researchers to vary prompts, models and sampling settings.

The limits matter. A language model's answer is generated from training data and prompt conventions, whereas a participant's answer reflects a person in an experiment. Matching the visible task does not make those processes equivalent. The reported models and prompts are also a sample of a fast-changing population, not a fixed property of all language models.

The work nevertheless identifies a concrete failure mode: a model can treat the number of observed examples as evidence about proportions or causes. That distinction is simple enough to test in deployed systems by holding ratios constant while changing group size.

## The study also found

The false association strengthened when the evidence encouraged a holistic reading, which matters because many summarisation prompts ask for a single overall pattern. An analytic framing reduced the tendency in some conditions, suggesting that instructions can shift the response without removing the underlying sensitivity.

The preprint and its code are available now. Replications with newer models and natural operational data would show whether the laboratory effect predicts errors in real analytical work.

## Verification

| Claim | Label | Primary source | Independent check |
|---|---|---|---|
| The preprint reports stronger illusory pattern perception in tested language models than in human participants | VENDOR-REPORTED | https://arxiv.org/abs/2610.07791 | none |
| The experiments adapt classic illusory-correlation and causal-pattern tasks | VERIFIED | https://arxiv.org/abs/2610.07791 | none |
| Sparse-autoencoder features associated with frequency sensitivity and analytic orientation track the reported effect | VENDOR-REPORTED | https://arxiv.org/abs/2610.07791 | none |
| The internal-feature result is correlational rather than a causal intervention | VERIFIED | https://arxiv.org/abs/2610.07791 | none |
| The authors released code for the experiments | VERIFIED | https://arxiv.org/abs/2610.07791 | none |
