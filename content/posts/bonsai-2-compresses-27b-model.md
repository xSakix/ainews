+++
date = '2026-09-18T05:12:00+02:00'
draft = false
title = 'Bonsai 2 Compresses a 27B Model'
+++

After reading this, the reader knows Bonsai 2 fits a 27B multimodal model into 5.9GB, with performance claims still vendor-tested.

# Bonsai 2 Compresses a 27B Model

*PrismML uses ternary weights to put a Qwen3.8-based model on consumer hardware, trading conventional precision for a much smaller footprint.*

PrismML has released Ternary Bonsai 2 27B, a compressed multimodal model based on Qwen3.8 27B. The company says the model occupies 5.9GB, supports text and images, accepts a 262,000-token context and is available under the Apache 2.0 license.

The model represents most weights using only three values: minus one, zero and plus one. It combines that ternary representation with 16-bit group scaling, producing what PrismML calls 1.76 effective bits per weight. Custom kernels then run the format on NVIDIA hardware through CUDA and on Apple devices through MLX.

## Why it matters

Model size determines where AI can run. A smaller footprint can move work from a remote service to a laptop, workstation or edge device. That can reduce network delay, keep sensitive data local and let a developer pay for hardware rather than every API call. It can also make a larger model practical in the same memory budget.

Compression normally carries a quality cost. Reducing the precision used for weights changes the numeric representation on which the model depends. The central claim behind Bonsai 2 is that ternary weights preserve enough capability to make a 27-billion-parameter class model useful while cutting memory far below a conventional full-precision implementation.

PrismML reports an aggregate score of 83.9 across reasoning, mathematics, coding, instruction following, vision and tool-use tests. Its stated Qwen3.8 27B baseline scores 85.4, which the company describes as 98.2% retention. Those figures come from PrismML's own evaluation and should not be treated as independent confirmation.

The same caution applies to speed and energy. PrismML reports up to 143 tokens per second on an NVIDIA GeForce RTX 5090 and 46.8 tokens per second on an Apple M5 Max. It also reports 0.714 milliwatt-hours per token on an RTX 4090 and says that result is 40% more efficient than an 8B full-precision model. Hardware settings, prompts, batch size and runtime design can materially change such comparisons.

## Deployment is more than a model file

The release matters partly because its weights are available, but a compressed representation needs compatible software. PrismML says Bonsai 2 runs through its custom low-bit kernels. Early community discussion on Hacker News noted that testers needed PrismML's llama.cpp fork and encountered documentation inconsistencies. That does not negate the model's size advantage, but it shows that portability depends on runtime support.

The 262K context window is also a capacity claim, not a guarantee that every device can use the full window comfortably. Long contexts require memory for the model's changing attention state in addition to the stored weights. Output speed may fall as the prompt grows, and application quality still depends on retrieval, prompting and tool design.

PrismML positions the model for local coding agents, computer use, private document analysis and hybrid systems that send only selected work to cloud models. Those are plausible uses, especially where privacy or repeated inference matters. They remain application choices rather than capabilities proved by the launch benchmarks.

The most useful next evidence will come from reproducible third-party tests using the released weights and clearly documented runtimes. Comparisons should hold prompt sets, quantization, context length, cache precision and hardware constant. They should also measure task completion, not only tokens per second.

Bonsai 2 is therefore a credible engineering release with an unusually small stated footprint. Its broader significance depends on whether outside users can reproduce the quality, speed and energy results across ordinary machines without a fragile software setup.

## Verification

- **Tier 1 — VERIFIED:** PrismML released Ternary Bonsai 2 27B on 17 September 2026 with ternary weights, FP16 group scaling, a stated 5.9GB footprint, 262K context, text-and-image support and Apache 2.0 licensing. Source: https://prismml.com/news/bonsai-2-27b
- **Tier 1 — VENDOR-REPORTED:** The 98.2% benchmark retention, throughput and energy-efficiency numbers were published by PrismML and were not independently reproduced in this review. Same source.
- **Tier 2 — REPORTED:** Hacker News participants reported runtime and documentation friction. Via: https://news.ycombinator.com/item?id=49746618
- **Tier 3 — ANALYSIS:** Privacy, cost and deployment implications are editorial analysis.

## Glossary candidates

- **Ternary weights:** Model parameters restricted to three values, commonly minus one, zero and plus one.
- **Group scaling:** A technique that stores a scaling factor for a block of compressed weights.

Cold-reader sentence: Bonsai 2 makes a 27B multimodal model unusually small, but independent tests must confirm its quality and efficiency.
