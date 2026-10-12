+++
title = "Models cannot tell when they are quantized"
description = "A preprint finds that models do not reliably report their own quantization from text behaviour. Internal probes can detect known methods, but fail to generalise to an unseen one."
tags = ["research", "models"]
date = 2026-10-12T04:00:37+02:00
draft = false
+++

Language models could not reliably say whether their weights had been quantized, even though trained probes could recover method-specific traces from their hidden states.

The preprint studies a narrow form of model self-knowledge. Researchers compressed models with several quantization methods, asked direct questions about their condition and compared their outputs with those of uncompressed versions. They then trained simple classifiers on internal activations to see whether the change existed without being available to the model's answer.

## Why it matters

For an engineer receiving a hosted or repackaged model, self-description is a poor integrity check. A model can operate through altered numerical weights without turning that internal difference into a truthful statement about its deployment.

Quantization stores weights with fewer bits so a model needs less memory and often runs faster. The process changes arithmetic throughout the network, but it need not produce an obvious textual signature. The authors report that direct self-reports and ordinary output comparisons carried almost no dependable signal about whether compression had occurred.

The picture changed when the researchers inspected hidden states. Linear probes—small classifiers trained on those internal values—separated quantized from unquantized runs and often identified the method used. The finding shows that the network contains detectable traces of its implementation even when its language interface does not expose them.

## A fingerprint is not general self-knowledge

The strongest limitation appears in the transfer test. A shared low-rank adapter learned to read several known quantization signatures, but did not reliably identify a method withheld during training. It had learned fingerprints of familiar transformations rather than a general concept of reduced numerical precision.

That distinction narrows the security conclusion. An operator with activation access may build a detector for deployment variants already represented in training data. The experiment does not establish a universal detector for arbitrary weight changes, and an API customer usually cannot read the provider's hidden states.

The authors call the mismatch anosognosia, borrowing a clinical term for lack of awareness of an impairment. The analogy is useful only at the behavioural level: the system contains evidence of a change but does not report it accurately. The paper does not show consciousness, subjective awareness or a clinical condition.

Methodologically, the study benefits from a controlled intervention. The base model and prompts can remain constant while only the weight representation changes, and the researchers can test self-report, external behaviour and hidden activity separately. Its scope remains bounded by the models, precision schemes and probe families evaluated in the preprint.

## The study also found

Different quantization methods left separable internal signatures, which may help deployment audits when a known set of variants is under consideration. Text outputs changed too little for the same task, warning against integrity tests that examine only sampled responses.

The next evidence will need to test unfamiliar compression tools and intentional evasion. The authors have established that known transformations can leave readable traces, while their own withheld-method result shows why that is not yet a general solution.

## Verification

| Claim | Label | Primary source | Independent check |
|---|---|---|---|
| Tested models did not reliably self-report whether they had been quantized | VENDOR-REPORTED | https://arxiv.org/abs/2610.06174 | none |
| Linear probes recovered method-specific information from hidden states | VENDOR-REPORTED | https://arxiv.org/abs/2610.06174 | none |
| A shared adapter failed to generalise reliably to an unseen quantization method | VENDOR-REPORTED | https://arxiv.org/abs/2610.06174 | none |
| Quantization was varied while the study compared text behaviour and internal activations | VERIFIED | https://arxiv.org/abs/2610.06174 | none |
| The paper does not establish consciousness or clinical anosognosia | ANALYSIS | https://arxiv.org/abs/2610.06174 | none |
