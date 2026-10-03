+++
title = "Humanlike Chat adds tool use to a local texting model"
description = "Version 2.0 uses two teachers to preserve casual dialogue while improving instruction and tool behaviour. The release includes local weights and explicit tradeoffs."
tags = ["models", "agents", "projects"]
date = 2026-10-03T09:42:58+02:00
draft = false
+++

LessThanThreeAI has released Humanlike Chat 2.0, a local Qwen-based language model trained to retain a casual texting style while handling instructions and tool calls that its first version lacked.

The 27-billion-parameter model is a community adaptation of an altered Qwen3.8 base, not an official Alibaba release. Its creator, identified as codebottle, publishes a [model card and downloadable weights](https://huggingface.co/LessThanThreeAI/Qwen3.8-27B-Humanlike-Chat-GGUF) under Apache-2.0, alongside a rate-limited free endpoint.

**Why it matters:** A local-agent developer can inspect an attempt to combine a conversational voice with tool behaviour in one model. The release supplies merged quantized files and an adapter, with the creator’s own comparisons against the altered base exposing both gains and losses.

The creator’s human-message test asks a grading model to choose the real person’s reply from a pair. It mistakes the new model’s reply for the human one about 24% of the time, versus roughly 15% for official Qwen and less than 1% for the altered base. That is a judge’s preference in this test, not a measurement of human users being deceived.

Version 2.0 learns from its own generated replies. One teacher grades conversational style with a hidden instruction; another teaches instructions, tools and code using the plain base. The student never receives the hidden style instruction, so the intended voice survives without adding it to each user session.

The reported tool-selection and instruction-following scores improve over the altered base, while broad knowledge and coding scores decline. The creator also describes reduced refusals inherited from that base. These tradeoffs accompany the style gain rather than supporting a general claim of superiority over official Qwen.

The model card offers a roughly 15 GB quantized file for a 24 GB graphics card and a llama.cpp setup that enables the model’s own chat template for tool calls. Files keep the previous release’s names, so existing users must download them again to obtain 2.0; published hashes identify the new files.

## Verification

| Claim | Label | Primary source | Independent check |
|---|---|---|---|
| Version 2.0, creator codebottle/LessThanThreeAI, 27B Huihui altered Qwen3.8 base; Apache-2.0; GGUF, adapter and rate-limited endpoint offered. | VERIFIED | https://huggingface.co/LessThanThreeAI/Qwen3.8-27B-Humanlike-Chat-GGUF | none |
| ishuman judge selection: 2.0 23.5%, official Qwen 15.1%, altered base 0.3%; not a human-user deception test. | VENDOR-REPORTED | https://huggingface.co/LessThanThreeAI/Qwen3.8-27B-Humanlike-Chat-GGUF | none |
| Two-teacher on-policy distillation: style teacher has hidden instruction; plain base covers instruction/tools/code; student never sees hidden instruction. | VERIFIED | https://huggingface.co/LessThanThreeAI/Qwen3.8-27B-Humanlike-Chat-GGUF | none |
| IFBench 37.3→43.7, When2Call 48→58, BFCL irrelevance 60→78; MMLU-Pro 78.5→72.5, LiveCodeBench 56→51; reduced refusals inherited. | VENDOR-REPORTED | https://huggingface.co/LessThanThreeAI/Qwen3.8-27B-Humanlike-Chat-GGUF | none |
| IQ4_XS 15.10 GB recommended for 24 GB VRAM; --jinja enables the template and tool calls; unchanged filenames require redownload; SHA256SUMS published. | VERIFIED | https://huggingface.co/LessThanThreeAI/Qwen3.8-27B-Humanlike-Chat-GGUF | none |
| Inspectable local voice/tool tradeoff is relevant to local-agent developers. | ANALYSIS | https://huggingface.co/LessThanThreeAI/Qwen3.8-27B-Humanlike-Chat-GGUF | none |
