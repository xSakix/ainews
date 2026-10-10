+++
title = "Model Self-Reports Leave an Internal Signature"
description = "A controlled study finds that faithful reports about learned preferences reuse more of the computation behind a model's decisions. The result suggests a white-box test for grounding, within narrow limits."
tags = ["research", "models"]
date = 2026-10-10T04:01:41+02:00
draft = false
+++

Models that accurately described their own learned preferences reused more of the internal computation behind their decisions than models that confabulated, a new preprint reports.

David Atkinson and David Bau at Northeastern University, with Dillon Plunkett of Eleos AI Research, created fictional characters with hidden preferences and trained Qwen3 models to choose on their behalf. The models were never trained to explain those preferences, which let the team ask whether accurate self-report could emerge on its own.

## Why it matters

An interpretability researcher evaluating a model's claim about its own state usually faces a circular problem: the statement sounds plausible, but the state itself may be impossible to check. This experiment supplies known ground truth and finds a structural difference between reports that match it and reports that do not.

The fictional preferences were simple five-number rules over features such as distance from a city centre and room size. A model saw pairs of options and learned which one its assigned character would choose. Separate prompts then asked it to output the character's preference weights as numbers.

Accurate reports eventually emerged in some runs even though the training data contained only decisions. That matters because the model could not merely imitate an explanation shown during training; it had to turn the decision rule it had learned into language.

## The same weights support choosing and reporting

The authors then used attribution patching, a method that estimates which adapter components contribute to a specific output. They compared the pattern used to make a choice with the pattern used to report the hidden preference.

Faithful adapters had an average similarity of 0.34 between those patterns, against 0.08 for unfaithful adapters. The authors' uncertainty interval for the difference excluded zero. In plain terms, accurate reporters tended to rely on more of the same added circuitry for acting and describing what guided the action.

Layer experiments pointed in the same direction. A 14-billion-parameter Qwen3 model trained across all 40 layers learned the decisions but reported its preferences poorly. Restricting training to roughly the first quarter to half of the network produced markedly more faithful reports, while training only later layers did not reproduce the effect. The authors interpret this as preference information moving to layers where existing verbalisation mechanisms can reach it.

The evidence is mechanistic rather than behavioural: the test does not need to understand the report's wording. In principle, the same comparison could work on an obfuscated report or an unfamiliar language, provided the relevant internal components are accessible.

### The study also found

Larger Qwen3 models more often learned faithful self-report than smaller variants, although some smaller models developed negatively correlated reports despite strong decisions. A replication with Gemma 4 found both high- and low-faithfulness adapters among the larger configurations. Within one shared model, the relationship between attribution similarity and faithfulness across characters was positive but weak.

The result does not yield an introspection detector for deployed models. The preference rules were constructed, linear and only five-dimensional; the experiments modified lightweight adapters rather than full model weights; and similarity scores for faithful and unfaithful groups overlapped. High similarity supported faithfulness in this setting, but a low score did not prove deception or confabulation.

The preprint was submitted on 5 October 2026. Its clearest next step is testing whether the same internal reuse appears when models report on richer learned strategies whose ground truth is still independently measurable.

## Verification

| Claim | Label | Primary source | Independent check |
|---|---|---|---|
| The study trained LoRA adapters on hidden linear preferences and observed accurate self-report without self-report supervision | VENDOR-REPORTED | https://arxiv.org/abs/2610.07186 | none |
| Faithful adapters averaged 0.34 attribution similarity versus 0.08 for unfaithful adapters | VENDOR-REPORTED | https://arxiv.org/abs/2610.07186 | none |
| Early-layer-only training improved self-report in Qwen3-14B while late-layer-only training did not | VENDOR-REPORTED | https://arxiv.org/abs/2610.07186 | none |
| The method separates groups with overlapping scores and was tested on adapters in a controlled setting | VERIFIED | https://arxiv.org/abs/2610.07186 | none |
| The paper was submitted on 5 October 2026 by Atkinson, Plunkett and Bau | VERIFIED | https://arxiv.org/abs/2610.07186 | none |
