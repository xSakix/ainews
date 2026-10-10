+++
title = "Tencent Releases Youtu-Parsing-Omni"
description = "The 5-billion-parameter model turns documents, images, audio and video into one structured JSON format. Tencent has released weights, code and a technical report."
tags = ["models", "tools"]
date = 2026-10-10T04:02:41+02:00
draft = false
+++

Tencent's Youtu lab has released a 5-billion-parameter model that parses six kinds of media into one structured JSON format.

Youtu-Parsing-Omni accepts document pages, natural images, charts, geometry figures, audio and video. It can return text, tables, formulas, layout boxes, timestamps, speech transcripts, captions and camera-motion descriptions without switching between separate specialist models.

## Why it matters

A developer building a search or document-processing system can send mixed media through one local model and receive a predictable schema. That reduces the integration work normally required to combine optical character recognition, speech recognition and video understanding services.

Tencent has published the weights under its custom `youtu-parsing` licence, a vLLM plugin, inference examples and a technical report. The repository says evaluation code will follow, so the reported benchmark results cannot yet be reproduced from the release alone.

The model uses a common encoder for images, audio and video. For video, selected layers let each frame attend to audio from the same part of the clip. Its output schema covers both literal elements, such as text and bounding boxes, and higher-level outputs such as narratives and reports.

Tencent reports a score of 96.96 on OmniDocBench 1.6, narrowly above TeleOCR at 96.91 and PaddleOCR-VL-1.6 at 96.34 in its published table. On the broader OmniParsingBench, Tencent reports an average of 75.08, behind Gemini 3 Pro at 77.44 but ahead of the other open-weight systems it tested. These are the releaser's measurements, and the comparison depends on the benchmark configuration in the report.

The training method repeatedly turns the student model into its own next-round teacher. Content tokens and structural tokens receive different comparison signals, an attempt to preserve both what a page says and how its elements relate.

## What to watch

Independent runs will need the promised evaluation code. Commercial users also need to review the custom licence rather than assuming the permissive terms common to some open-weight releases.

## Verification

| Claim | Label | Primary source | Independent check |
|---|---|---|---|
| Tencent released Youtu-Parsing-Omni with 5B parameters, weights, code examples and a technical report | VERIFIED | https://huggingface.co/tencent/Youtu-Parsing-Omni | https://github.com/TencentYoutuResearch/Youtu-Parsing-Omni |
| The model accepts documents, images, charts, geometry, audio and video and emits one JSON schema | VENDOR-REPORTED | https://huggingface.co/tencent/Youtu-Parsing-Omni | none |
| Tencent reports 96.96 on OmniDocBench 1.6 and 75.08 on OmniParsingBench | VENDOR-REPORTED | https://huggingface.co/tencent/Youtu-Parsing-Omni | none |
| The release uses the custom youtu-parsing licence and does not yet include evaluation code | VERIFIED | https://huggingface.co/tencent/Youtu-Parsing-Omni | https://github.com/TencentYoutuResearch/Youtu-Parsing-Omni |
