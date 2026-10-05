+++
title = "Examples amplify a symbolic circuit already in models"
description = "An interpretability study finds the same abstraction, induction and retrieval pathway before few-shot accuracy rises, suggesting demonstrations energise existing machinery instead of building a new algorithm."
tags = ["research", "models"]
date = 2026-10-05T03:59:30+02:00
draft = false
+++

When a language model learns a pattern from several examples in its prompt, it can look as though it has assembled a new procedure on the fly. A mechanistic study by independent researcher Melissa Wessel offers a different account for one family of symbolic tasks: the procedure is already present in the model, and examples progressively strengthen the signal flowing through it.

The preprint follows a three-stage circuit across prompts containing from zero to ten demonstrations. It finds the same core route when accuracy is poor and when it is nearly perfect. The heads do not suddenly appear as the model “gets” the pattern. Their causal contribution grows.

This is a narrow experiment, not a general theory of learning in context. But it turns an appealing metaphor—examples awaken latent machinery—into something researchers can intervene on and test.

## From tokens to variables and back

The task uses abstract three-token patterns such as ABA or ABB. Tokens are arbitrary, preventing the model from relying on their ordinary meaning. It must infer which position should be copied into the answer.

Prior work identified three stages. Symbolic-abstraction heads translate concrete tokens into variables. Symbolic-induction heads operate over that abstract pattern. Retrieval heads convert the predicted variable back into the required token. Wessel traces this structure in Gemma 2-2B, Llama 3.1-8B and Qwen 3-4B while changing only the number of demonstrations.

In Gemma 2-2B, accuracy begins at 17% with one example, reaches 93% with four and 99% with ten. Yet causal mediation analysis already detects the three stages at one example. The important heads mostly persist across adjacent prompt lengths, while an individual head's causal contribution grows by as much as eightfold between one and ten examples.

The interpretation is quantitative rather than architectural: additional examples turn up an existing pathway instead of recruiting a wholly different one.

## Moving the signal across prompts

Detection alone can mistake correlation for mechanism, so the paper also moves internal activations between runs. Patching ten-example activations into a one-example prompt raises Gemma's accuracy from 17% to 88%. At zero examples, patching the induction and retrieval stages raises one pattern's accuracy from 1% to 56%; random non-circuit heads leave it below 1%.

The most vivid intervention uses a “function vector”, a fixed activation assembled from heads identified by the causal analysis. Injecting it at zero examples raises accuracy from 1% to 86% on the ABA rule. When the downstream retrieval heads are ablated, that rescue falls to 13%.

That dependency is the key. The vector does not act as a free-standing answer or a generic jolt to the network. It can largely substitute for the induction stage only because the later retrieval machinery remains available to read its output.

## A useful result with a small domain

The study makes in-context learning look less like writing a fresh program during inference and more like supplying an input to a program embedded during training. If that view generalises, a model's few-shot limits would depend on which circuits its weights contain and whether a prompt can access them.

The paper does not show that all demonstrations work this way. Its central task is essentially a small relational table with a copy operation. A letter-string analogy check finds a similar topology, but it is not repeated across every model or with the full patching programme. The analysis method also selects components that distinguish two rules, so it may miss shared infrastructure.

The result is strongest as a concrete mechanism for one simple capability: examples can amplify a stable symbolic pathway long before behaviour reveals that the pathway is there.

## Verification

| Claim | Label | Primary source | Independent check |
| --- | --- | --- | --- |
| Study traces abstraction, induction and retrieval stages across Gemma 2-2B, Llama 3.1-8B and Qwen 3-4B | VERIFIED | [Preprint](https://arxiv.org/abs/2609.36265) | none |
| Gemma accuracy rises from 17% at one example to 99% at ten; per-head contribution grows up to eightfold | VENDOR-REPORTED | [Preprint](https://arxiv.org/abs/2609.36265) | none; author's experiments |
| Ten-example activation patches raise one-example accuracy to 88%, and zero-example patches raise 1% to 56% | VENDOR-REPORTED | [Preprint](https://arxiv.org/abs/2609.36265) | none; author's experiments |
| Function-vector injection raises zero-example ABA accuracy from 1% to 86%, falling to 13% after retrieval ablation | VENDOR-REPORTED | [Preprint](https://arxiv.org/abs/2609.36265) | none; author's experiments |
| Demonstrations amplify a pre-existing circuit rather than construct a new one for these tasks | ANALYSIS | [Preprint](https://arxiv.org/abs/2609.36265) | the paper's interpretation of causal interventions |
| Generalisation to richer abstract reasoning remains open | VERIFIED | [Preprint](https://arxiv.org/abs/2609.36265) | stated limitation |
