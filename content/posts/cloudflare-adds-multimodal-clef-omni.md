+++
title = "Cloudflare adds multimodal Clef-omni"
description = "The new classifier keeps Qwen3-Omni's image, audio and video inputs while returning typed answers instead of generated prose. Cloudflare also cut Clef-flash's price and context window."
tags = ["models", "tools"]
date = 2026-10-12T04:02:37+02:00
draft = false
+++

Cloudflare has released Clef-omni, a multimodal classifier that accepts text, images, audio and video but returns typed answers rather than generated prose.

The model extends the Clef classification family with Qwen3-Omni as its base. Cloudflare froze that base, trained lightweight adapters and added a head that maps an input directly to a user-defined label schema in one forward pass.

## Why it matters

For a developer sorting support messages, inspecting product photos or routing short clips, Clef-omni offers a single classification interface across several media types. That can remove a separate transcription or captioning stage, although Cloudflare has not published independent end-to-end comparisons against such pipelines.

Cloudflare says Clef-omni is a 30-billion-parameter mixture-of-experts model that activates about 3 billion parameters for an input. In the company's Workers AI measurements, text classification took about 130 milliseconds, images about 150 milliseconds and a 21-second video with audio about 1.5 seconds. Those timings are vendor tests and will vary with input size, queueing and deployment.

The benchmark picture is mixed rather than uniformly better. Cloudflare's table puts the older dense Clef ahead on several text tasks, while Clef-omni edges it on the BANKING77 intent dataset, 94.8% to 94.2%. The new model's practical distinction is its range of inputs, not a general claim to higher text accuracy.

Cloudflare also changed the terms for Clef-flash. Its listed input price fell from $0.09 to $0.038 per million tokens, while its context window fell from 64,000 to 24,000 tokens. Clef remains $0.24 per million input tokens and Clef-omni launches at $0.15.

The Clef-omni weights are available under Apache 2.0 on Hugging Face. The model card lists about 35.3 billion total parameters and says the current custom loader needs roughly 64 GB of BF16 memory on an H200-class GPU. Cloudflare says SGLang support is planned, but gives no release date.

## What to watch

The open weights make independent latency, calibration and accuracy tests possible now. Support in a mainstream serving engine will matter for teams that want to run the model outside Workers AI without maintaining Cloudflare's custom loader.

## Verification

| Claim | Label | Primary source | Independent check |
|---|---|---|---|
| Cloudflare released Clef-omni with text, image, audio and video inputs and typed classification outputs | VERIFIED | https://blog.cloudflare.com/clef-faster-cheaper-multimodal/ | https://huggingface.co/Cloudflare/clef-omni |
| Cloudflare reports about 130 ms for text, 150 ms for images and 1.5 s for a 21-second audiovisual clip | VENDOR-REPORTED | https://blog.cloudflare.com/clef-faster-cheaper-multimodal/ | none |
| Cloudflare's table reports 94.8% on BANKING77 for Clef-omni and 94.2% for Clef | VENDOR-REPORTED | https://blog.cloudflare.com/clef-faster-cheaper-multimodal/ | none |
| Clef-flash now costs $0.038 per million input tokens and has a 24,000-token context window | VERIFIED | https://blog.cloudflare.com/clef-faster-cheaper-multimodal/ | none |
| Apache-2.0 weights and a custom loader are available; SGLang support is planned | VERIFIED | https://huggingface.co/Cloudflare/clef-omni | https://blog.cloudflare.com/clef-faster-cheaper-multimodal/ |
