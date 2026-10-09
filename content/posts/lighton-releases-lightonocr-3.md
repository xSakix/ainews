+++
title = "LightOn releases LightOnOCR-3"
description = "The Apache-2.0 model family combines transcription, layout boxes, image descriptions and chart extraction in models small enough to run locally."
tags = ["models", "tools"]
date = 2026-10-09T04:04:06+02:00
draft = false
+++

French AI company LightOn has released LightOnOCR-3, a family of open-weight document models that can return text, page structure, image descriptions and chart data in one pass.

The family comes in 0.8-billion, 1-billion and 4-billion-parameter versions under the Apache 2.0 licence. An empty prompt produces a conventional transcription; the prompt `grounding` adds labelled regions with coordinates, describes images and turns charts into HTML tables.

**Why it matters:** A developer building a private document pipeline can inspect and run these models locally instead of sending pages to a hosted service or joining separate systems for OCR, layout detection and chart extraction.

LightOn kept its previous architecture for the 1B model, making that variant a direct upgrade for existing LightOnOCR-2 deployments. The smaller and larger versions use the Qwen3.5 vision-language architecture. LightOn also published conversion and visualisation utilities, model weights and the scripts it used to reproduce its benchmark scores.

The strongest headline result comes from LightOn's own testing. Its 4B model scored 86.3 on the 512-page olmOCR benchmark, 1.3 points behind the 35.1B-parameter Infinity Parser Pro and half a point ahead of another 4B model, Chandra 2. The comparison is useful because the company ran the models under a common serving setup, but it is still a vendor evaluation and output normalisation can materially change OCR scores.

The model's structured output is deliberately compact. LightOn said the 0.8B and 4B versions generated 9% to 14% fewer tokens than two competing parsers on the same pages while also returning boxes and image descriptions. At each model's preferred benchmark resolution, the 1B version had the lowest reported single-page latency at 2.7 seconds on an NVIDIA H100.

The training account is unusually detailed for a release post. LightOn describes how it combined several detectors, rejected ambiguous page annotations and used a large vision model to label figures. It also says the benchmark repository contains its post-processing rules, which matter because equivalent footnotes or formulas can receive different edit-distance scores depending on their formatting.

All three weights, a demo and the supporting code are available now through [LightOn's release post](https://huggingface.co/blog/lightonai/lightonocr-3). Independent tests will need to establish how reliably chart values and boxes hold up on documents outside LightOn's evaluation sets.

## Verification

| Claim | Label | Primary source | Independent check |
|---|---|---|---|
| LightOn released three LightOnOCR-3 variants under Apache 2.0 | VERIFIED | [Release post](https://huggingface.co/blog/lightonai/lightonocr-3) | [4B model card](https://huggingface.co/lightonai/LightOnOCR-3-4B) |
| Grounding mode returns labelled boxes, image descriptions and chart tables | VERIFIED | [Release post](https://huggingface.co/blog/lightonai/lightonocr-3) | none |
| The 1B model keeps the previous architecture; 0.8B and 4B use Qwen3.5 VLM | VERIFIED | [Release post](https://huggingface.co/blog/lightonai/lightonocr-3) | none |
| LightOn published weights, utilities and benchmark-reproduction scripts | VERIFIED | [Release post](https://huggingface.co/blog/lightonai/lightonocr-3) | [4B model card](https://huggingface.co/lightonai/LightOnOCR-3-4B) |
| The 4B model scored 86.3 on olmOCR-Bench | VENDOR-REPORTED | [Release post](https://huggingface.co/blog/lightonai/lightonocr-3) | none |
| Selected models produced 9% to 14% fewer tokens than named competitors | VENDOR-REPORTED | [Release post](https://huggingface.co/blog/lightonai/lightonocr-3) | none |
| The 1B model had 2.7-second single-page latency on an H100 | VENDOR-REPORTED | [Release post](https://huggingface.co/blog/lightonai/lightonocr-3) | none |
