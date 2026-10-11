+++
title = "Nish Tahir Recalibrates a Small Decision Model"
description = "A runnable experiment turns Qwen3-1.7B into a single-pass classifier, then shows that its confidence is too high. Temperature scaling improves the probabilities."
tags = ["models", "research", "essays"]
date = 2026-10-11T04:01:06+02:00
draft = false
+++

Independent engineer Nish Tahir has published a runnable experiment that turns Qwen3-1.7B into a single-pass decision model and then measures how poorly its confidence matches its accuracy.

The method limits the model's output vocabulary to answer tokens A through E and reads their probabilities after one forward pass. On CommonsenseQA, Tahir reports 59.4% accuracy for the base model and 62.4% after a short fine-tuning run.

## Why it matters

A developer building a router or risk score needs to know more than which option won. If a model says 95% but is right only seven times in ten, thresholds based on that number will behave unpredictably. Tahir's experiment shows the complete path from logits to a measured calibration problem, using a model small enough to reproduce.

The accuracy gain is not the most informative result. Answers assigned between 90% and 100% confidence were correct only about 70% of the time. In the 80% to 90% band, accuracy was roughly 40%. The model therefore separated choices well enough to beat chance, while expressing far more certainty than its results justified.

Tahir applies temperature scaling to correct the probabilities. The method learns one scalar on held-out examples and divides the logits by it before the softmax operation. Raising the temperature flattens an overconfident distribution without changing which answer has the highest score.

That makes temperature scaling a calibration step, not a capability upgrade. It cannot repair wrong rankings or teach missing knowledge. Its value is that a reported 70% can become closer to seven correct cases in ten on data resembling the calibration set.

The write-up includes a compact PyTorch implementation and interactive demonstrations. It also exposes a design choice hidden by many decision-model products: the answer schema must be known in advance and mapped cleanly to a small set of tokens. A task with ambiguous labels, missing options or several valid answers breaks that simplicity.

The results come from one small model, one benchmark and the author's own training setup. CommonsenseQA multiple-choice questions do not reproduce document routing, fraud review or tool selection, and calibration can drift when the input distribution changes. Each deployment would need its own held-out data and periodic checks.

The article is useful precisely because it reports that weakness instead of presenting the confidence output as trustworthy by construction. The code and demonstrations are available now, giving practitioners a short baseline against which to test larger specialised decision models.

## Verification

| Claim | Label | Primary source | Independent check |
|---|---|---|---|
| The experiment restricts Qwen3-1.7B to answer tokens A through E and reads one forward pass | VERIFIED | https://nishtahir.com/build-your-own-decision-model/ | none |
| The base model scored 59.4% and the quickly fine-tuned model 62.4% on CommonsenseQA | VENDOR-REPORTED | https://nishtahir.com/build-your-own-decision-model/ | none |
| The 90% to 100% confidence bin was correct about 70% of the time | VENDOR-REPORTED | https://nishtahir.com/build-your-own-decision-model/ | none |
| The 80% to 90% confidence bin was correct about 40% of the time | VENDOR-REPORTED | https://nishtahir.com/build-your-own-decision-model/ | none |
| Temperature scaling changes probability sharpness without changing the top-ranked answer | VERIFIED | https://nishtahir.com/build-your-own-decision-model/ | none |
