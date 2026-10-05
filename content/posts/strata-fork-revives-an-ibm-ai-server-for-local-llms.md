+++
title = "Strata fork revives an IBM AI server for local LLMs"
description = "A hardware-specific fork runs Qwen3.8-Flash-Next across two POWER9 processors and four V100 GPUs, showing what model-aware optimisation can recover from a 2018 system."
tags = ["projects", "hardware", "models"]
date = 2026-10-05T03:58:30+02:00
draft = false
+++

A community developer has adapted the Strata inference engine to IBM's AC922, a 2018 server whose two POWER9 processors connect directly to four 16 GB Nvidia V100 accelerators. The result is less a general replacement for llama.cpp than a case study in making an unusual machine's topology work for a modern mixture-of-experts model.

The fork runs a quantised Qwen3.8-Flash-Next, a 125-billion-parameter model whose sparse design activates only a small subset of its experts for each token. Strata keeps frequently used experts on the GPUs and the full expert set in system memory. That arrangement suits the AC922 because its CPUs and GPUs share high-bandwidth NVLink 2.0 connections rather than communicating only over ordinary PCIe.

The developer added a page-locked memory arena for each CPU socket, placed experts with awareness of the machine's non-uniform memory layout, and let an otherwise idle peer GPU fetch data across its own NVLink. Other changes include FP16 Volta tensor-core kernels, pipelined layer splitting and POWER9-specific vector and thread handling.

On four V100s, the project's own measurements peak at 7,357 tokens per second while reading a 135,000-token prompt. A 252,000-token prompt is processed at 7,089 tokens per second, taking 35.5 seconds. Greedy generation reaches 113 tokens per second on JSON, 103 on code and 84 on prose. At a reused 252,000-token context, the first follow-up token appears after 0.26 seconds and generation then runs at 60 tokens per second.

Those figures are the builder's measurements on one specialised server, not a portable benchmark. Prompt-processing speed varies substantially with prompt length, and generated text type changes decoding speed. The repository describes the fork as experimental and unsupported by upstream Strata.

Still, the project illustrates an increasingly useful approach to local inference: optimise around a particular model and a particular memory hierarchy instead of demanding that one generic engine treat every machine alike. The AC922 is old, power-hungry enterprise equipment, but its CPU-to-GPU links remain unusually capable. A model with thousands of experts gives those links useful work to do.

The code is published under Strata's MIT licence on the fork's `ac922` branch, with build, quality and benchmark notes. Some changes may eventually move upstream, but the immediate value is inspectable engineering for owners of hardware that mainstream inference projects rarely target.

## Verification

| Claim | Label | Primary source | Independent check |
| --- | --- | --- | --- |
| Fork targets an AC922 with two POWER9 CPUs, four 16 GB V100 GPUs and NVLink 2.0 | VERIFIED | [Repository](https://github.com/eelgaev/Strata-AC922) | none |
| NUMA-aware expert placement, per-socket page-locked arenas, peer-GPU fetches and Volta/POWER9 kernels | VERIFIED | [Repository](https://github.com/eelgaev/Strata-AC922) | code and technical notes present; not independently executed |
| Peak prefill 7,357 tokens/s and 7,089 tokens/s at 252,000 tokens | COMMUNITY-REPORTED | [Repository](https://github.com/eelgaev/Strata-AC922) | none; builder benchmark |
| Decode reaches 113 tokens/s on JSON and 84 on prose | COMMUNITY-REPORTED | [Repository](https://github.com/eelgaev/Strata-AC922) | none; builder benchmark |
| Fork is experimental and unsupported upstream | VERIFIED | [Repository](https://github.com/eelgaev/Strata-AC922) | explicit repository note |
| Hardware-specific inference can recover value from an older specialised memory topology | ANALYSIS | [Repository](https://github.com/eelgaev/Strata-AC922) | inference from the implementation and measurements |
