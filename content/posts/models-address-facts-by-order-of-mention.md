+++
title = "Models address facts by order of mention"
description = "A preprint finds a shared internal direction that points language models to the first, second or later fact in a passage. Moving a question along that direction can change which fact the model retrieves."
tags = ["research", "models"]
date = 2026-10-06T04:08:31+02:00
draft = false
+++

Language models appear to locate facts in a passage partly by the order in which those facts were mentioned, according to a new interpretability study.

Yufa Zhou tested Qwen, Gemma and Llama models on short lists of factual statements followed by questions. The models' internal question states formed a repeatable pattern for the first, second and later facts, even when the names and subject matter changed.

## Why it matters

For a researcher trying to understand retrieval inside a model, the result supplies a concrete mechanism rather than another correlation between activations and answers. The same internal direction could be moved experimentally, causing a question about one fact to retrieve a different fact from the passage.

The paper calls these positions “fact addresses”. Consider a context that says Alice eats an apple and Bob eats a pear. A question about Alice and a question about Bob differ inside the model along a direction related to the facts' order of mention. When the researcher added the first-to-second direction to a question about the first fact, the model often answered with the content of the second.

That intervention is the study's strongest evidence. A classifier can discover many patterns in hidden states without showing that a model uses them. Changing the answer by changing the proposed address provides causal support for the mechanism, although the tests use controlled factual lists rather than long, natural documents.

Across 64 new word sets, the intervention selected the intended fact in about five out of six cases for Qwen, roughly half for Gemma and about one in three for Llama. The exact rates were 84.1%, 53.9% and 36.2%, respectively. Those differences show that the direction was shared across model families but was not equally reliable in each one.

## The addresses occupy a small internal space

Zhou reports that the fact addresses lie in a low-rank subspace. In plain terms, the models do not need a separate unrelated direction for every possible position; a small set of directions describes much of the ordering pattern.

The first-mentioned fact was also easier for the models to reach than later facts. That resembles a primacy effect in human recall, but the experiment does not establish that people and transformers use the same mechanism. It identifies a measurable asymmetry in the tested models.

The pattern appeared in late-middle layers and across sizes from 1.5 billion to 32 billion parameters. Checkpoints taken during training suggested that it formed early rather than arriving only after extensive instruction tuning. Code released with the preprint makes the controlled interventions inspectable.

The narrow setup is also the main limit. Lists of simple facts isolate ordering cleanly, while real prompts contain headings, repeated references, tools and conflicting statements. The paper shows that order of mention can act as an address under controlled conditions; it does not show that order dominates retrieval in ordinary agent transcripts.

Zhou submitted the preprint on 1 October 2026. The next evidence will come from reproducing the intervention on less regular documents and testing whether changing document structure changes the same internal directions.

## Verification

| Claim | Label | Primary source | Independent check |
| --- | --- | --- | --- |
| Question states are organised by fact order across Qwen, Gemma and Llama | VENDOR-REPORTED | [Zhou preprint](https://arxiv.org/abs/2610.00910) | none; preprint result |
| Adding an ordinal vector can redirect a question to another fact | VENDOR-REPORTED | [Zhou preprint](https://arxiv.org/abs/2610.00910) | none; author experiment |
| Transfer across 64 word sets reached 84.1% for Qwen, 53.9% for Gemma and 36.2% for Llama | VENDOR-REPORTED | [Zhou preprint](https://arxiv.org/abs/2610.00910) | none |
| Fact addresses occupy a low-rank subspace and favour the first fact | VENDOR-REPORTED | [Zhou preprint](https://arxiv.org/abs/2610.00910) | none |
| The pattern appears from 1.5B to 32B parameters and forms early in pretraining | VENDOR-REPORTED | [Zhou preprint](https://arxiv.org/abs/2610.00910) | none |
| Reproduction code is public | VERIFIED | [Order-of-mention repository](https://github.com/MasterZhou1/order-of-mention) | repository available |
