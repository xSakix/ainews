+++
title = "Fine-Tuning Can Hide Knowledge Without Erasing It"
description = "A preprint separates a reversible loss of access from the slower destruction of stored facts. The distinction could change how continual-learning failures are diagnosed."
tags = ["research", "models"]
date = 2026-10-11T04:04:06+02:00
draft = false
+++

Knowledge that vanishes during fine-tuning can remain intact inside a language model and later reappear, a new mechanistic study reports.

Vedant Palit, Florent Draye, Nicolas Zucchet, Zhijing Jin and Bernhard Schölkopf studied “spurious forgetting”: a fall in recall that looks like erased knowledge but instead reflects a temporary failure to access it. Their preprint combines a minimal associative memory, a small Transformer and interventions on a pretrained language model.

## Why it matters

A developer updating a model with new company data may see its accuracy on older facts collapse and conclude that the update destroyed them. If the failure is an access problem, retraining or restoring an earlier checkpoint wastes information that is still present. The useful question becomes not only how much performance fell, but whether the old representations moved together or were individually damaged.

The authors observed a three-stage pattern while training on new facts. Recall of old facts first collapsed, recovered even though training continued only on the new material, and then declined again. A single theory of permanent overwriting cannot explain the middle recovery.

Their minimal memory reproduced that curve with three ingredients: old keys sharing structure, new values concentrated in one region, and normalisation inside the network. Fine-tuning initially pushed the old representations along a common direction. That shift disrupted the readout, but preserved the relative arrangement that encoded which fact was which.

Once the new facts were learned, normalisation withdrew much of the common shift and old answers became accessible again. Meanwhile, smaller fact-specific changes accumulated. Those changes altered the relationships among memories and eventually produced lasting loss.

## One direction separates hiding from erosion

The paper tests the mechanism rather than stopping at the curve. In a Transformer trained on synthetic data, subtracting the shared shift removed the temporary collapse. In a pretrained language model, removing one direction from each fine-tuning weight update restored old facts, according to the authors.

That intervention gives the account more force than a description of changing benchmark scores. It identifies a low-dimensional component associated with reversible loss and distinguishes it from slower, distributed changes that damage individual memories.

The distinction is about model state, not human memory. “Hidden” knowledge here means that an evaluation prompt no longer retrieves the expected answer while the geometry that supported it remains measurable. It does not imply that the model consciously remembers or can recover the fact without an intervention.

The experiments also use deliberately controlled facts and training conditions. Real fine-tuning mixes formats, objectives and overlapping concepts, and a production model can fail for reasons outside this mechanism: prompt mismatch, changed decoding, safety tuning or a new answer policy. Detecting a common representation shift therefore cannot by itself certify that a lost capability is recoverable.

### The study also found

Whether forgetting was mostly temporary or permanent depended on the new data: old memories that moved together retained their relative geometry, while updates that moved them apart produced destructive erosion. Normalisation helped explain the rebound by reducing the common displacement after new learning stabilised. The minimal model predicted qualitative behaviour later tested in Transformer experiments.

The preprint was submitted on 6 October 2026 and has not yet been peer reviewed. Its practical value is a diagnostic hypothesis: before treating every post-fine-tuning regression as erased knowledge, inspect whether the representations share a removable direction and whether recovery occurs during continued training.

## Verification

| Claim | Label | Primary source | Independent check |
|---|---|---|---|
| Recall of old facts collapsed, recovered during continued new-fact training and later eroded | VENDOR-REPORTED | https://arxiv.org/abs/2610.08718 | none |
| A minimal associative memory reproduced the pattern with shared keys, concentrated values and normalisation | VENDOR-REPORTED | https://arxiv.org/abs/2610.08718 | none |
| Fine-tuning moved old representations along a common direction while preserving relative geometry | VENDOR-REPORTED | https://arxiv.org/abs/2610.08718 | none |
| Removing the common direction eliminated temporary collapse in a small Transformer | VENDOR-REPORTED | https://arxiv.org/abs/2610.08718 | none |
| Removing one direction from weight updates restored old facts in a pretrained language model | VENDOR-REPORTED | https://arxiv.org/abs/2610.08718 | none |
| The paper was submitted on 6 October 2026 | VERIFIED | https://arxiv.org/abs/2610.08718 | none |
