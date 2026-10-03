+++
title = "Simple-WAM keeps future features without rendering video"
description = "A controlled robotics study finds that one pass over noisy future-video tokens preserves much of a world action model’s generalization advantage."
tags = ["research", "models", "agents"]
date = 2026-10-03T05:58:20+02:00
draft = false
+++

Researchers report that robot policies can retain the benefits of predicting the future without repeatedly generating clean video frames. Their Simple-WAM method gives the action model future-related features from one pass over noisy video tokens.

A world action model learns to predict both a robot’s next actions and what the scene will look like afterward. Generating that imagined video during operation is expensive. The new study separates the useful representation of the future from the costly work of turning it into a visible sequence.

**Why it matters:** Robotics researchers can use this distinction to evaluate faster policies on changed environments and unfamiliar tasks. Matching performance on familiar training-like scenes did not mean that two methods retained the same ability to adapt in the authors’ experiments.

Renping Zhou, Zanlin Ni and colleagues at Tsinghua University’s Leap Lab, the University of Science and Technology of China and Beijing Institute of Technology posted the [preprint](https://arxiv.org/abs/2609.34981) on 28 September. Its results are author-reported, and the comparisons concern a particular model setup rather than all robot policies.

## The useful step comes before a clean picture

The study compares an explicit approach, which repeatedly denoises future video while producing an action chunk, with a latent approach that drops future-video tokens during inference. The controlled comparison keeps the backbone, training data and budget matched. A structured attention mask determines whether action tokens can read the future representations.

On familiar LIBERO tasks, the explicit and latent configurations achieved reported success rates of 97.75% and 96.85%. Their separation was much larger when camera viewpoints, lighting, object arrangements and other conditions changed: 67.72% versus 53.75% on LIBERO-Plus. Using fewer demonstrations also widened the difference.

The biggest gap appeared when the researchers provided video of held-out tasks without action labels. The explicit model reached 69.90%, compared with 5.90% for the latent configuration. Neither performed strongly when it received no data about those tasks. This matters because learning from an observed operation is different from succeeding on a wholly unfamiliar task without additional information.

The team then varied how many times the explicit model’s video branch ran, without retraining it. Almost all of the advantage came from the first pass. At that point the future-video inputs were still Gaussian noise, not recognizable predicted frames. The action branch nevertheless received useful intermediate features from processing those tokens together with the current observation.

Simple-WAM preserves that first pass and reuses its features throughout action denoising. It also changes training so that fully noisy future-video inputs occur more often, matching the condition used during operation. The method leaves the action-generation steps intact and adds neither a new module nor a new loss term.

In the authors’ main evaluation, Simple-WAM scored 79.5% under environmental perturbations, against 67.7% for the explicit baseline and 53.8% for the latent one. Its reported action-chunk latency was 74.7 milliseconds on an RTX 5090, compared with 286.9 milliseconds and 62.0 milliseconds respectively. Those figures describe the tested configurations, not an end-to-end robot response time.

The real-robot experiments used an AgileX Aloha dual-arm platform. Four training tasks included stacking bowls and arranging objects in a specified order. Under changed lighting, backgrounds and layouts, Simple-WAM achieved a reported average of 69.2%, versus 25.2% for the latent baseline. These real-world scores measure the fraction of task sub-goals completed, averaged over 30 trials per task; they are not binary full-task success rates.

The central finding is therefore narrower than a claim that future prediction is unnecessary. Future-conditioned features still mattered, but clean video generation was largely dispensable in this setup. The study used a five-billion-parameter video backbone without large-scale embodied pretraining. Whether the same relationship holds for larger models or those pretrained extensively on robot experience remains the paper’s explicit open question.

## Verification

| Claim | Label | Primary source | Independent check |
|---|---|---|---|
| The preprint was first submitted on 28 September and lists the three institutions above. | VERIFIED | [arXiv record and full paper](https://arxiv.org/abs/2609.34981) | none |
| Matched configurations remain close on familiar tasks but separate under perturbations and held-out-task video. | VENDOR-REPORTED | [Tables 1–2](https://arxiv.org/abs/2609.34981) | none |
| One pass over noisy future tokens supplies useful features; Simple-WAM adjusts the training schedule accordingly. | VENDOR-REPORTED | [Sections 4–5](https://arxiv.org/abs/2609.34981) | none |
| Simple-WAM reports 79.5% perturbation performance and 74.7-millisecond action-chunk latency on an RTX 5090. | VENDOR-REPORTED | [Section 6 and Table 2](https://arxiv.org/abs/2609.34981) | none |
| Real-robot results average sub-goal completion over 30 trials per task, with the stated model-scale limitation. | VENDOR-REPORTED | [Sections 6–7 and Appendix A.3](https://arxiv.org/abs/2609.34981) | none |
