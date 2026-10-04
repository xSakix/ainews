+++
title = "Aleph Alpha releases open-weight Kolibri"
description = "The German-English reasoning model ships with Apache-2.0 weights and serving instructions. Its small active parameter count still leaves a large memory requirement."
tags = ["models", "tools"]
date = 2026-10-04T09:27:37+02:00
draft = false
+++

Aleph Alpha, a German AI developer, released Kolibri on 3 October, making a German-English reasoning model available as downloadable weights under the Apache 2.0 licence.

Kolibri uses a mixture of experts: each token activates a small part of a much larger network. The model card documents reasoning controls, tool calling and a server interface compatible with OpenAI's chat API.

For a developer handling German documents, the release offers an inspectable model that can run on infrastructure they control. Aleph Alpha deliberately concentrates on German and English, including a tokenizer designed for German word structure, instead of broad multilingual coverage.

The memory requirement is substantial. Kolibri activates about 3.5 billion parameters per token, but its roughly 78 billion parameters still need to be stored. The FP8 checkpoint occupies about 78 GB; the card lists two 80 GB A100 GPUs or a single H200 among the minimum configurations.

Aleph Alpha says it validated contexts of about one million tokens, while recommending a quarter of that for efficient serving and complex tasks. Its native long-context training length is the smaller figure. The distinction is useful when planning deployment: the largest accepted input is a documented extension, with a separate recommendation for everyday use.

The company's own tests show uneven strengths. Kolibri scores highly on competition mathematics, while Qwen3.8 27B leads it on the card's overall English and German measures. These are Aleph Alpha's evaluations of both models, rather than an independent comparison.

Serving requires Aleph Alpha's inference package, which provides a Kolibri plugin for vLLM. The card includes commands for enabling reasoning and tool-call parsing, and lets callers select low, medium or high reasoning effort or disable it. It describes human-reviewed assistants and document workflows as intended uses. The FP8 checkpoint and a separate BF16 checkpoint are available now.

## Verification

| Claim | Label | Primary source | Independent check |
| --- | --- | --- | --- |
| Release on 3 October; German-English focus; downloadable Apache-2.0 weights | VERIFIED | [Source](https://huggingface.co/Aleph-Alpha/Kolibri-1) | none |
| 78,103,074,560 total and 3,457,573,120 active parameters; approximately 78 GB FP8 footprint; documented GPU configurations | VENDOR-REPORTED | [Source](https://huggingface.co/Aleph-Alpha/Kolibri-1) | none |
| Native context 262,144; validated extension 1,048,576; recommendation at most 262,144 | VENDOR-REPORTED | [Source](https://huggingface.co/Aleph-Alpha/Kolibri-1) | none |
| Overall EN/DE: Kolibri 75.5/70.8, Qwen3.8 27B 80.2/79.9; AIME 2025 EN 96.9 | VENDOR-REPORTED | [Source](https://huggingface.co/Aleph-Alpha/Kolibri-1) | none; all models evaluated by Aleph Alpha |
| Tokenizer design; vLLM plugin, reasoning controls, tool parser and OpenAI-compatible API; human-reviewed intended uses; BF16 checkpoint | VERIFIED | [Source](https://huggingface.co/Aleph-Alpha/Kolibri-1) | none; documented interfaces and intended uses, not execution tests |
| Local deployment gives German-document developers control over infrastructure | ANALYSIS | [Source](https://huggingface.co/Aleph-Alpha/Kolibri-1) | Inference from downloadable weights and serving documentation |
