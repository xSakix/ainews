+++
title = "Gutsy ships local decision weights and evaluation code"
description = "A small Qwen fine-tune returns probabilities instead of generated text, with published tests that expose both improvements and regressions."
tags = ["projects", "models", "research"]
date = 2026-10-03T05:53:20+02:00
draft = false
+++

Gutsy, a local decision-model project by developer kouhxp, publishes compact weights and evaluation code for returning probabilities over specified answers instead of generating a text response.

A request supplies a state and typed questions, such as yes-or-no decisions or choices from a list. The runtime returns an answer distribution, including a rejection option when none of the offered choices fits the evidence.

**Why it matters:** A developer building a local classifier can inspect both the model and its uncertainty behavior rather than asking a chat model to write an answer and confidence statement. The Apache-2.0 release includes CPU-ready quantized files and training documentation.

The current model is a fine-tune of Qwen3.5-0.8B, served through llama.cpp. Its reference file is 775 MB, with a smaller 505 MB quantization also available. The runtime can encode a shared state once and reuse it for follow-up questions, reducing repeated processing of the same input.

The builder’s largest reported improvement concerns contrast pairs: nearly identical questions where a missing fact sometimes requires abstention and sometimes leaves the answer determined. On 48 held-out pairs, both answers were correct in about 42% of pairs in version 0.4, against about 10% in version 0.3. The release explains that its data audit found and removed shortcuts involving answer length and option counts.

That gain did not produce uniform improvement. On the public JevBench decision set, the reference model answered 169 of 231 items correctly, against 167 previously, while its hard-tier score declined. The model card also reports weaker calendar arithmetic and judgment of close answer pairs, with calibration becoming worse on unfamiliar hard items.

Training used about 105,000 questions, combining public datasets, generated reasoning problems and scenarios reviewed by an open teacher model. The card discloses which evaluation families had related training data and calls comparisons with other projects indicative where samples or harness versions differ.

The release provides local serving commands and a reproduction directory. Its own findings leave long policy reasoning, date calculations and long CPU inputs as weak areas, making the published failure breakdown as important as the small download.

## Verification

| Claim | Label | Primary source | Independent check |
|---|---|---|---|
| Published Apache-2.0 model/runtime/training artifacts; Qwen3.5-0.8B; Q8_0 775 MB, Q4_K_M 505 MB. | VERIFIED | https://huggingface.co/kouhxp/gutsy | none |
| Typed decision outputs, rejection distribution and state caching. | VENDOR-REPORTED | https://huggingface.co/kouhxp/gutsy | none |
| 48 contrast pairs both-correct v0.3 0.104 to v0.4 0.417; JevBench 167 to169/231; hard score59 to56/111; arithmetic/judging/calibration regressions. | VENDOR-REPORTED | https://huggingface.co/kouhxp/gutsy | none |
| 105114 training questions; open-teacher review, disclosed in-domain data and shortcut audit; comparative sample differences. | VENDOR-REPORTED | https://huggingface.co/kouhxp/gutsy | none |
| Probabilities and disclosed failures give local-classifier builders inspectable decision behavior. | ANALYSIS | https://huggingface.co/kouhxp/gutsy | none |
| Project publicly shown on dated thread. | VERIFIED | https://news.ycombinator.com/item?id=49939547 | none |
