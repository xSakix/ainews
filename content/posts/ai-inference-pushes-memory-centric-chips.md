+++
date = '2026-09-15T23:30:00+02:00'
draft = false
title = 'AI inference pushes memory-centric chips'
+++

After reading this, the reader knows growing inference demand is pushing chip designers toward faster memory movement and specialized prefill and decode hardware.

# AI inference pushes memory-centric chips

*An IEEE Spectrum survey shows vendors stacking memory with compute, using on-chip SRAM and splitting language-model serving across different processors.*

AI hardware designers are reorganizing systems around memory bandwidth as inference becomes a larger share of data-center work, according to an IEEE Spectrum analysis published September 15.

In plain terms, generating a model response requires moving enormous amounts of data repeatedly. A processor can perform arithmetic quickly and still sit idle while it waits for model weights or conversation context to arrive from memory.

## Why it matters

Training made GPUs the center of the AI boom because many calculations can run in parallel. Inference has a different rhythm. The prefill phase reads a prompt and can process many tokens together. The decode phase produces the answer one token at a time, repeatedly reading model weights and a growing key-value cache.

That sequential decode work can be limited by memory bandwidth rather than raw arithmetic. IEEE cited research finding Nvidia H100 GPUs idle for 50% to 80% of the time in tested open-model workloads. The range comes from particular models and configurations, so it should not be generalized to every deployment, but it illustrates why vendors are changing the data path.

One response is to place memory closer to compute. d-Matrix says its Raptor design stacks an accelerator die directly on DRAM, shortening the connection. Majestic Labs proposes a longer proprietary link to a memory-aggregation chip, allowing a rack to draw on commodity DRAM beyond the physical edge around a processor where high-bandwidth memory normally sits.

These are vendor designs and projections. Their practical value depends on latency, power, software support, manufacturing yield and real application throughput. Capacity or bandwidth figures alone do not establish lower total cost.

## Prefill and decode may split apart

Another approach assigns the two inference phases to different chips. Nvidia says its Rubin GPUs can handle context processing while the Groq 3 language-processing unit performs parts of token generation using 500 megabytes of on-die SRAM. AWS has announced a pairing in which Trainium handles prefill and Cerebras wafer-scale systems handle decode.

The split reflects different strengths. Prefill benefits from parallel compute; decode benefits from quick access to weights. Cerebras places 44 gigabytes of SRAM on its wafer-scale chip, while Groq's design arranges SRAM and compute for predictable data movement. Keeping more data close to arithmetic can reduce waiting, though multi-chip systems add scheduling and networking complexity.

Software is changing alongside hardware. Quantization stores model numbers in fewer bits, reducing memory use and movement at the possible cost of accuracy. Nvidia promotes its NVFP4 format, while AMD, Intel, Qualcomm and others support MXFP4. Vendor benchmarks show large speed gains with small losses on selected tests, but buyers need evaluations on their own models and quality thresholds.

The survey does not identify one winner. It shows a market testing stacked memory, commodity DRAM, on-chip SRAM, wafer-scale processors, new numeric formats and application-specific silicon at the same time. Some products are shipping; others remain planned or depend on company performance claims.

The useful next comparison is end-to-end: tokens per second at a stated latency and quality, measured with power, utilization and total system cost. Inference hardware will be judged as a system, not by a single chip specification.

## Verification

1. **VERIFIED — IEEE Spectrum published its inference-hardware survey on September 15, 2026.** Source: https://spectrum.ieee.org/inference-hardware-revolution
2. **VERIFIED — LLM inference separates into a parallel prefill phase and sequential decode phase that repeatedly reads weights and the KV cache.** Primary research is linked in the IEEE survey; source: https://spectrum.ieee.org/inference-hardware-revolution
3. **PARTIALLY VERIFIED — Tested H100 workloads left processors idle 50% to 80% of the time.** IEEE cites a research paper for selected open-model configurations; the result is not universal. Via: https://spectrum.ieee.org/inference-hardware-revolution
4. **VERIFIED — d-Matrix describes Raptor as stacking compute with DRAM, while Majestic proposes memory aggregation over a longer link.** Primary company pages are linked from: https://spectrum.ieee.org/inference-hardware-revolution
5. **VERIFIED — Nvidia documents Groq 3 LPU and its use alongside Rubin systems; AWS announced a Trainium and Cerebras inference partnership.** Primary sources: https://www.nvidia.com/ and https://www.aboutamazon.com/
6. **PARTIALLY VERIFIED — Cerebras WSE-3 contains 44 GB of on-wafer SRAM and is intended for memory-intensive inference.** The specifications are company-reported and linked through the IEEE analysis. Via: https://spectrum.ieee.org/inference-hardware-revolution
7. **PARTIALLY VERIFIED — Four-bit formats can raise inference performance with limited quality loss.** The outcome depends on the model and benchmark; cited gains are vendor measurements. Primary references are linked from: https://spectrum.ieee.org/inference-hardware-revolution

## Glossary candidates

- Prefill
- Decode
- KV cache
- Memory bandwidth
- Quantization

**Cold-reader sentence:** Inference is driving chipmakers to move memory closer to compute and divide prompt processing from token generation across specialized hardware.
