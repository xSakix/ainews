+++
title = "A 27B Agent Model Fits in 10 GB"
description = "Nari Labs compressed Qwen3.8-27B from 53.8 GB to 10.12 GB and matched its BF16 source on several long agent benchmarks. The result depends on agent-generated calibration data and a specialised inference fork, which limits where the smaller files can run."
tags = ["models", "agents", "research", "hardware"]
date = 2026-11-24T04:21:00+01:00
draft = false
+++

The download finished on a workstation with 16 gigabytes of graphics memory. A 27-billion-parameter model that normally needed 53.8 gigabytes sat in one 10.12-gigabyte file. The engineer started a coding agent and watched it call tools, read the results and continue instead of failing halfway through the job.

*The scenes that open and close this article are illustrations; the people in them are invented.*

Nari Labs released three compressed versions of Alibaba's Qwen3.8-27B on 20 November. Its three-bit and 2.5-bit files matched the original BF16 model on the laboratory's tests of long coding and terminal tasks. The two-bit file did not. The release offers a practical claim and a methodological one: a model can lose almost four-fifths of its weight storage without losing the behaviour that agents need, provided that the compression process learns from agent work rather than ordinary text.

## The wrong text for the job

Quantization replaces the high-precision numbers in a model's weights with smaller representations. Fewer bits reduce memory and bandwidth, which can turn a model that needs a server into one that fits on a workstation. The cost is approximation. Each compressed weight departs from the original, and the errors can accumulate as the model generates a long answer or moves through many steps.

Most calibration sets consist of short passages from the web. A quantizer uses those passages to learn which errors matter and how to distribute a limited set of numerical values. Doyeob Kim, the NariQ report's sole author, argues that this data does not represent the work of a coding agent. An agent may operate across more than 100,000 tokens, alternate between reasoning and tool calls, and react to terminal output over many turns.

That mismatch appears in existing results. According to Kim's paper, previous quantizations of Qwen3.8-27B at three bits or less can match BF16 on the short mathematics problems in AIME while solving no more than 72 percent as many DeepSWE tasks. A model that recalls facts and completes isolated calculations may still drift during a long exchange with a software repository.

NariQ changes the calibration material. It records tokens that the full BF16 model generated during agent sessions, then uses those traces to guide the choice of compressed weights. The model sees the kind of sequence that it will later have to survive: plans, tool requests, observations and revisions.

## Trellises and traces

The numerical machinery builds on QTIP, a 2024 method by James Tseng and colleagues. QTIP uses trellis-coded quantization and an incoherence transform to assign groups of weights to compact codewords. The trellis searches among possible sequences instead of rounding every weight independently.

NariQ joins that machinery with calibration from the target activity. The distinction matters because a quantizer can preserve average next-token probability while damaging a small set of decisions that control whether an agent recovers from a failed command. Long tasks repeatedly expose those decisions.

The published files cover three, 2.5 and two bits per weight. They retain Qwen3.8-27B's vision tower and key-value cache at BF16, so the headline bit width describes the language-model weights rather than every byte that inference consumes. The base model is a dense vision-language model with 64 layers and a native context length of 262,144 tokens. It supports adjustable reasoning effort and preserves reasoning content across turns by default.

Nari Labs evaluated the compressed files beside the 53.8-gigabyte BF16 checkpoint. On DeepSWE v1.1, which contains 113 tasks run three times, BF16 scored 39.8 pass@1. The three-bit file scored 41.0 and the 2.5-bit file 41.9. Terminal-Bench 2.1 produced 62.6 for BF16, 63.8 for three bits and 60.2 for 2.5 bits.

The pattern continued on the AIME 2025 and 2026 mathematics sets. BF16 scored 97.7, the three-bit build 98.3 and the 2.5-bit build 96.5. RealWorldQA, a vision benchmark, put BF16 and three-bit level at 82.4. Small differences of this size do not prove that compression improves the model; repeated sampling can move an agent benchmark. They do support the narrower conclusion that the two larger NariQ files did not measurably fall behind in these tests.

## The two-bit boundary

The smallest file shows where the claim stops. At two bits per weight, DeepSWE fell to 28.6, Terminal-Bench to 52.4 and AIME to 86.0. Compression crossed a threshold where calibration could no longer recover the source model's behaviour.

The benchmark set also belongs to the developer. Nari Labs chose the model, calibration traces, implementation and evaluation settings. The report has one author and has not been peer reviewed. Independent runs on different agents, repositories and hardware would test whether the parity travels beyond the published table.

There is another boundary between a small file and an accessible model. NariQ requires the company's fork of llama.cpp because the weight format and kernels are not in the standard project. Stock llama.cpp, Ollama and LM Studio cannot load the files. The fork is tuned for Nvidia's SM120 architecture. Nari Labs says it runs more slowly on Ampere, Ada and Hopper cards, does not support AMD or Intel GPUs, and remains slow on Apple Metal.

That qualification changes the meaning of “local.” Ten gigabytes puts the weights inside the memory budget of many consumer graphics cards, but the software path does not yet serve many of those cards well. Qwen's uncompressed model card, by contrast, lists established serving frameworks such as Transformers, vLLM and SGLang. The NariQ files trade that broad compatibility for their size.

## What the file measures

The work suggests a different way to judge low-bit models. Perplexity and short exams are convenient because they are cheap and repeatable. They do not exercise the loops that make an agent useful: retaining a goal, choosing tools, reading errors and trying again. Calibration data can carry the same blind spot as an evaluation.

NariQ does not make a 27B model universally cheap. The full context still consumes key-value memory, the vision encoder remains at high precision, and inference speed depends on kernels for a specific device. It does show that weight storage and agent competence need not decline together at three or 2.5 bits on the tasks that were tested.

Back at the workstation, the agent reached the end of its terminal task. The 10.12-gigabyte file had fit from the start. Whether the next machine can run it depends less on the file than on the name printed on its graphics chip.

## References

- Kim, D. (2026). *NariQ: Sub-3-Bit Quantization for Long-Horizon Agentic Tasks*. https://arxiv.org/abs/2611.26157
- Nari Labs (2026). *Qwen3.8-27B-NariQ-GGUF model card*. https://huggingface.co/nari-labs/Qwen3.8-27B-NariQ-GGUF
- Qwen Team (2026). *Qwen3.8-27B model card*. https://huggingface.co/Qwen/Qwen3.8-27B
- Tseng, J., et al. (2024). *QTIP: Quantization with Trellises and Incoherence Processing*. https://arxiv.org/abs/2406.11235
