+++
title = "Basalt Specialises Qwen Inference for Blackwell"
description = "The MIT-licensed engine narrows its target to one Qwen model and NVIDIA's newest consumer GPUs. It can spill mixture-of-experts weights into system memory or a second card."
tags = ["models", "tools", "projects"]
date = 2026-10-10T03:59:41+02:00
draft = false
+++

Basalt is a new local inference engine built for one model family and one GPU generation: Qwen3.8-Flash-Next on NVIDIA Blackwell cards.

The MIT-licensed project forks the broader Strata engine and removes other targets. Its central trade is specialisation: experts that do not fit in video memory can remain in system RAM or on a second GPU, while the dense parts of the mixture-of-experts model stay close to the main card.

## Why it matters

A local-model developer with an RTX 50-series workstation gets an engine shaped around that hardware instead of a general runtime carrying many compatibility paths. The same narrow design also excludes older NVIDIA and non-NVIDIA systems.

Basalt packages the model into one memory-mappable file containing weights, tokenizer, chat template, speculative-decoding head, expert layout and optional vision components. Conversion repacks existing weights rather than retraining them. Ready-made packs are available separately on Hugging Face.

The included server implements OpenAI- and Anthropic-compatible interfaces and can serve as many as eight concurrent requests. Context is divided among active slots by default, so four slots under a 262,144-token maximum receive 65,536 tokens each. Operators can instead allocate the full context to every slot at a corresponding memory cost.

The runtime requires Linux on x86-64, CUDA 13 and a Blackwell GPU with compute capability 12.0. Its image path has a separate encoder written for Qwen's vision tower, with a CPU fallback. The repository also includes parity tests, a quality gate based on perplexity and divergence, and benchmark fixtures.

The project's author reports hundreds of generated tokens per second on a mixed RTX 5090 and 5060 Ti setup, depending on prompt type and quantisation. Those figures are self-measured and have not been independently reproduced. More important than the peak number is the engineering choice behind it: a large sparse model can run on a workstation by streaming only the experts needed at each step.

## What to watch

Independent tests need to compare quality as well as speed across the supplied quantisations. The repository also warns that its default server settings are untuned, so published results need a complete configuration to be comparable.

## Verification

| Claim | Label | Primary source | Independent check |
|---|---|---|---|
| Basalt is an MIT-licensed Qwen3.8-Flash-Next engine for Linux and NVIDIA Blackwell | VERIFIED | https://github.com/jesdga95/basalt | none |
| The engine can place experts in system RAM or on a second GPU | VERIFIED | https://github.com/jesdga95/basalt | none |
| The server offers OpenAI- and Anthropic-compatible APIs with up to eight concurrent slots | VERIFIED | https://github.com/jesdga95/basalt | none |
| The author reports hundreds of generated tokens per second on an RTX 5090 and 5060 Ti pair | VENDOR-REPORTED | https://github.com/jesdga95/basalt | none |
| Specialisation removes compatibility paths in exchange for tighter hardware optimisation | ANALYSIS | https://github.com/jesdga95/basalt | none |
