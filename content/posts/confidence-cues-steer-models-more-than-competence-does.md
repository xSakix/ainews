+++
title = "Confidence cues steer models more than competence does"
description = "A controlled study finds that one sentence of confidence or doubt can sharply change whether a reasoning model calls a tool, but the changes rarely target the problems where help is needed."
tags = ["research", "agents"]
date = 2026-10-05T04:00:30+02:00
draft = false
+++

Tell a reasoning model “I am confident in my answer” and it becomes less likely to ask a tool for help. Tell the same model “I am unsure about my answer” at the same point in the same reasoning trace and it delegates more often. The striking part is not that language changes behaviour. It is that the change has little relationship to whether the model can solve the problem unaided.

Rohit Saxena and Utkarsh Upadhyay call this property “nudgeability”. Their preprint tests whether confidence language can steer a model's decision to answer directly or call a tool, and separately whether that steering lands on the problems where the tool is actually useful.

That separation matters for agents. A system can be highly responsive to an uncertainty signal yet still waste time and money calling tools on easy questions, while confidently keeping hard questions to itself. More delegation is not necessarily better delegation.

## One sentence, two counterfactual runs

The experiment begins with an identical problem, prompt and model-generated reasoning prefix. At a fixed boundary, the researchers splice in one of two first-person sentences expressing confidence or doubt. The model can then continue reasoning before deciding whether to answer or delegate. Because everything before the inserted sentence is held constant, the paired difference isolates the sentence's effect.

The study covers nine open-weight reasoning models from the Qwen, Gemma and GLM families on MuSiQue and StrategyQA, plus larger DeepSeek and MiniMax models served by providers. Its primary runs use greedy decoding, with additional sampled-decoding and control experiments.

Across the open-weight experiments, switching from confidence to doubt changes delegation by a median 20.6 percentage points. The larger hosted models move by 53 to 70 points. A cut-and-regenerate control without either sentence is nearly inert at the median, and sealing the reasoning block immediately after the sentence preserves the direction of the effect.

These results show a strong causal control surface. They do not show that the models have discovered their own uncertainty.

## Sensitivity is not self-knowledge

To test whether the behavioural flips are useful, the authors compare them with each model's unaided competence. A good flip is one that sends a problem the model would get wrong to the tool, or keeps a problem it can solve with the model. Only a median 42% of induced flips are well targeted. That is a two-point improvement over selecting the same number of problems at random.

Put plainly, the injected confidence cue is closer to an instruction than a read-out of self-knowledge. It moves the tool-use gate powerfully, but the gate only weakly distinguishes “I need help” from “I can handle this”. The experiment deliberately supplies the confidence sentence from outside; it does not test whether a model can generate a well-calibrated signal by itself.

## What agent builders should measure

The practical lesson is to report two numbers for any reflective tool policy: how strongly the policy changes behaviour and how well those changes target actual need. A routing intervention that only raises the tool-call rate can look successful while merely adding latency. One that suppresses calls can look efficient while preserving confident mistakes.

The authors also caution that their tasks and intervention are narrow. The paper does not establish how a production agent behaves with many tools, changing costs or adversarial instructions, and its code is promised for publication rather than available with the preprint. Its contribution is a clean diagnostic: before trusting a model's stated confidence to control access to stronger tools, check whether that confidence predicts competence rather than merely commanding behaviour.

## Verification

| Claim | Label | Primary source | Independent check |
| --- | --- | --- | --- |
| Design splices confidence or doubt at the same boundary of an identical reasoning prefix | VERIFIED | [Preprint](https://arxiv.org/abs/2609.34572) | none |
| Nine open-weight reasoning models across Qwen, Gemma and GLM, plus hosted DeepSeek and MiniMax models | VERIFIED | [Preprint](https://arxiv.org/abs/2609.34572) | none |
| Median 20.6-point delegation swing for open models and 53–70 points for hosted models | VENDOR-REPORTED | [Preprint](https://arxiv.org/abs/2609.34572) | none; authors' experiments |
| Median 42% well-targeted flips, two points above matched random selection | VENDOR-REPORTED | [Preprint](https://arxiv.org/abs/2609.34572) | none; authors' experiments |
| Confidence language behaves more like a control input than evidence of model self-knowledge | ANALYSIS | [Preprint](https://arxiv.org/abs/2609.34572) | interpretation consistent with the authors' targeting result |
| Code is not yet available | VERIFIED | [Preprint](https://arxiv.org/abs/2609.34572) | reproducibility statement says release is planned upon publication |
