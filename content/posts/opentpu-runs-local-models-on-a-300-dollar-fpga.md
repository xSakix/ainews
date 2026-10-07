+++
title = "OpenTPU runs local models on a $300 FPGA card"
description = "The Apache-licensed project publishes its accelerator design, compiler, simulator and host tools, with measured throughput showing a small, memory-bound system rather than a GPU replacement."
tags = ["hardware", "projects", "models"]
date = 2026-10-07T03:58:57+02:00
draft = false
+++

OpenTPU has published an end-to-end AI accelerator stack that runs modern language models on a roughly $300 Kintex-7 FPGA card.

The Apache-2.0 repository includes SystemVerilog hardware, an instruction set, a bit-exact simulator, a kernel language and compiler, profiling tools and host software. Its value is inspectability: the same small codebase reaches from Python model kernels to the signals on a physical PCIe board.

## Why it matters

A developer learning inference hardware can trace where every cycle and memory transfer goes without needing a datacentre accelerator. The resulting machine is slow beside current GPUs, but its constraints make the bottleneck unusually visible.

OpenTPU reports 30.7 generated tokens per second for a four-bit Qwen3-0.6B model and 82.1 for LFM2.5-230M, including host overhead. Larger dense models slow to 12.03 tokens per second for Qwen3.5-2B and 3.75 for Gemma 4 E4B in the listed configurations.

The card reaches 82% to 94% of its two DDR3 channels' 17.1 GB/s peak while decoding. That makes memory bandwidth, rather than matrix arithmetic, the limiting resource. A four-column systolic unit helps prompt processing more than token-by-token generation.

Models larger than the card's 4 GiB can stream mixture-of-experts weights from host storage. The repository reports 10.6 tokens per second for LFM2.5-8B-A1B and 3.95 for Qwen3.5-35B-A3B, with the latter moving 153 MB per token across PCIe. These are the project's own measurements, but the scripts, dated builds and measurement conditions are public.

The “developed by AI” description needs care. A human-directed agent workflow produced much of the design and optimization, according to the project, but that does not show an autonomous system deciding to create its own hardware. The concrete result is the released stack and the bit-for-bit agreement reported between the board and simulator.

The next tests are straightforward: reproduce the published bitstreams on the same board, compare power and latency with inexpensive GPUs, and see whether outside contributors can change the architecture without breaking simulator equivalence.

## Verification

| Claim | Label | Primary source | Independent check |
| --- | --- | --- | --- |
| OpenTPU publishes hardware, ISA, simulator, compiler and host tools under Apache-2.0 | VERIFIED | [OpenTPU repository](https://github.com/FeSens/openTPU) | files and licence are accessible |
| Qwen3-0.6B reaches 30.7 wall tokens/s and LFM2.5-230M reaches 82.1 in four-bit configurations | VENDOR-REPORTED | [OpenTPU measurements](https://github.com/FeSens/openTPU) | none |
| Decode uses 82% to 94% of a 17.1 GB/s DDR3 peak | VENDOR-REPORTED | [OpenTPU measurements](https://github.com/FeSens/openTPU) | none |
| Qwen3.5-35B-A3B reaches 3.95 tokens/s while streaming 153 MB per token | VENDOR-REPORTED | [OpenTPU measurements](https://github.com/FeSens/openTPU) | none |
| The card reproduces simulator tokens bit for bit | VENDOR-REPORTED | [OpenTPU repository](https://github.com/FeSens/openTPU) | public tests exist; no independent hardware reproduction found |
| “Developed by AI” does not establish autonomous hardware development | ANALYSIS | [OpenTPU repository](https://github.com/FeSens/openTPU) | distinction follows the documented human-directed workflow |
