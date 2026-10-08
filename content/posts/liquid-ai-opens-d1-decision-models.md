+++
title = "Liquid AI opens d1 decision models"
description = "The 3.1-billion-parameter d1-3B and experimental 600-million-parameter d1-omni answer structured questions in one forward pass, with weights available for local deployment."
tags = ["models", "projects"]
date = 2026-10-08T03:58:31+02:00
draft = false
+++

Liquid AI released open weights for two d1 models on 7 October, bringing its fast, structured decision system to local devices after an API-only introduction.

The models answer yes-or-no, multiple-choice and scored questions in one forward pass instead of generating a sequence of tokens. The 3.1-billion-parameter d1-3B accepts text and images; the experimental d1-omni-600M accepts text with either images or up to 30 seconds of audio.

The design gives developers a compact component for routing, moderation, classification or ranking when a free-form response is unnecessary. One input state can carry several named questions, and the model returns the corresponding decisions together, avoiding the latency and variable wording of token generation.

Liquid reports that d1-3B answered a single question in 8 milliseconds on an RTX 4090, 30 milliseconds on an Apple M5 Pro and 50 milliseconds on a Jetson Orin Nano. Those are the company's own measurements. Its published table also gives d1-3B a mean score of 82.9 across seven public text datasets, while the smaller model scored 78.4.

The two releases serve different hardware. d1-3B uses Liquid's decoder-only vision-language model as its base and has a 32,768-token context window. d1-omni-600M combines a bidirectional text encoder with separate vision and audio encoders, with a 16,384-token context window. Liquid describes the smaller model as an early research release and does not publish latency measurements for it.

Both repositories use the LFM Open License rather than a standard permissive software licence. Loading the models currently requires Transformers 5.14 or later and executes repository-supplied Python through `trust_remote_code=True`, a setting that warrants reviewing the downloaded code before use.

The weights, model cards and demo are available now on Hugging Face. Liquid also provides GGUF and weight-activation 8-bit variants, which make d1-3B easier to test on constrained machines while its decision API is still new.

## Verification

| Claim | Label | Primary source | Independent check |
|---|---|---|---|
| Liquid AI released d1-3B and d1-omni-600M weights on 7 October 2026 | VERIFIED | [Liquid AI release](https://huggingface.co/blog/LiquidAI/open-d1) | [d1-3B model card](https://huggingface.co/LiquidAI/d1-3B) |
| d1 models answer structured questions in one forward pass without generating output tokens | VERIFIED | [Liquid AI release](https://huggingface.co/blog/LiquidAI/open-d1) | none |
| d1-3B accepts text and images; d1-omni-600M accepts text with images or audio | VERIFIED | [Liquid AI release](https://huggingface.co/blog/LiquidAI/open-d1) | [d1-omni-600M model card](https://huggingface.co/LiquidAI/d1-omni-600M) |
| Liquid reports 8 ms on RTX 4090, 30 ms on Apple M5 Pro and 50 ms on Jetson Orin Nano | VENDOR-REPORTED | [Liquid AI release](https://huggingface.co/blog/LiquidAI/open-d1) | none |
| Liquid reports mean text-benchmark scores of 82.9 for d1-3B and 78.4 for d1-omni-600M | VENDOR-REPORTED | [Liquid AI release](https://huggingface.co/blog/LiquidAI/open-d1) | none |
| Loading requires Transformers 5.14 or later and `trust_remote_code=True` | VERIFIED | [Liquid AI release](https://huggingface.co/blog/LiquidAI/open-d1) | [d1-3B model card](https://huggingface.co/LiquidAI/d1-3B) |
