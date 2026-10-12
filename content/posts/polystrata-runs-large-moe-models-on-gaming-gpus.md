+++
title = "PolyStrata runs large MoE models on gaming GPUs"
description = "The open-source runner keeps selected model experts in system memory and moves them to a consumer GPU as needed. Its one-click package exposes local OpenAI- and Anthropic-compatible APIs."
tags = ["projects", "models", "hardware"]
date = 2026-10-12T03:57:37+02:00
draft = false
+++

PolyStrata has released an open-source runner that uses system memory to serve mixture-of-experts models too large to fit entirely on a gaming GPU.

The one-click package wraps the Strata runtime and targets Nvidia and AMD cards with at least 12 GB of video memory. It ships an image-capable Qwen3.8-Flash-Next setup and experimental support for several larger sparse models, while exposing OpenAI- and Anthropic-compatible endpoints on the local machine.

## Why it matters

For a developer with a workstation rather than a server, PolyStrata turns spare system RAM into a larger model pool. Only the experts needed for the current token are moved through the GPU, trading data movement and memory capacity against the cost of multi-GPU hardware.

Mixture-of-experts models contain many specialised parameter blocks but activate only a subset at each step. PolyStrata keeps those blocks in host memory and schedules active ones onto the accelerator. The technique does not shrink the model file: the README says experimental GLM 5.3 Flash builds still require roughly 79 to 114 GB, depending on quantization.

The project's own RTX 5070 measurements range from about 94 generated tokens per second at its smallest two-bit setting to 53 at a larger three-bit setting. It reports prompt-processing rates between roughly 1,620 and 2,650 tokens per second at a 32,000-token context. These are builder benchmarks, not independent measurements, and quality differs between quantization levels.

PolyStrata also documents Claude Code driving a Qwen3.6 35B sparse model at three-bit precision on an 8 GB laptop GPU. A warm-start option reads the system prompt before the interactive session, reducing the delay before the first answer. Actual usability will depend on RAM bandwidth, model routing and how much context changes between turns.

The repository is licensed under MIT and provides local endpoints compatible with existing agent clients. That lowers integration work, while giving local applications access to files and tools under the user's own permissions. It also means the operator, rather than a hosted provider, owns model updates, network exposure and log handling.

## What to watch

Independent tests should compare identical models and quantization settings with established CPU-offload runtimes. The project's current value is inspectable code and a practical packaging layer; its headline speeds remain author-reported until reproduced across more hardware.

## Verification

| Claim | Label | Primary source | Independent check |
|---|---|---|---|
| PolyStrata released an MIT-licensed local runner for sparse models on consumer GPUs | VERIFIED | https://github.com/VecSzn/PolyStrata | none |
| The package exposes OpenAI- and Anthropic-compatible local APIs | VERIFIED | https://github.com/VecSzn/PolyStrata | none |
| The README reports 53–94 generated tokens per second on an RTX 5070 across selected quantizations | VENDOR-REPORTED | https://github.com/VecSzn/PolyStrata | none |
| Experimental GLM 5.3 Flash files require roughly 79–114 GB depending on quantization | VERIFIED | https://github.com/VecSzn/PolyStrata | none |
| Host-memory expert loading trades capacity against transfer and memory-bandwidth costs | ANALYSIS | https://github.com/VecSzn/PolyStrata | none |
