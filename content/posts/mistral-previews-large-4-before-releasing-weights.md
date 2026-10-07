+++
title = "Mistral previews Large 4 before releasing its weights"
description = "Mistral has opened API access to its one-trillion-parameter multimodal model and set 27 October for the open-weight release, leaving architecture and benchmark claims provisional."
tags = ["models", "business"]
date = 2026-10-07T04:00:57+02:00
draft = false
+++

Mistral has opened a public API preview of Mistral Large 4, while scheduling the model's downloadable weights for 27 October.

The French company describes the model as a multimodal mixture of experts trained from scratch in its European data centres. It accepts text and images, supports more than 160 languages and has a one-million-token context window.

## Why it matters

An organisation considering a self-hosted European model can test Large 4 now, but it cannot yet inspect or deploy the promised weights. That gap makes this a preview with a dated delivery commitment, rather than a completed open-weight release.

Mistral's announcement lists one trillion total parameters and 49 billion active for each token. Its documentation instead lists 1.05 trillion total, 52 billion active and a 1.6-billion-parameter vision encoder. The difference may reflect rounding or a changed configuration, but Mistral has not published a technical report that reconciles the figures.

The company is emphasizing cybersecurity. It reports 82% on the reproduce-then-patch portion of CyberGym-E2E, 93% on Cybench and 61.7% on DeepSWE v1.1. Some evaluations name external providers, but the assembled comparison and most headline claims appear in Mistral's own release materials.

Before the weights arrive, Mistral says cybersecurity specialists and public authorities will test a version with reduced moderation. The company argues that ordinary safety refusals can suppress defensive work, a trade-off that this preview is designed to probe.

API pricing starts at $1.36 per million input tokens and $4.18 per million output tokens. Reasoning and non-reasoning modes are available through Mistral Studio, while the licence and final deployment requirements will remain unknown until the weight release.

The decisive event is 27 October. A model card, technical report, licence and downloadable files will show whether the public artefact matches the preview's scale and capabilities.

## Verification

| Claim | Label | Primary source | Independent check |
| --- | --- | --- | --- |
| Mistral opened a Large 4 API preview and scheduled weights for 27 October | VERIFIED | [Mistral announcement](https://mistral.ai/news/mistral-large-4/) | [Mistral documentation](https://docs.mistral.ai/models/mistral-large-4) |
| The announcement lists 1T total and 49B active parameters | VERIFIED | [Mistral announcement](https://mistral.ai/news/mistral-large-4/) | documentation lists different figures |
| The documentation lists 1.05T total, 52B active and a 1.6B vision encoder | VERIFIED | [Mistral documentation](https://docs.mistral.ai/models/mistral-large-4) | none |
| The model scored 82% on CyberGym-E2E reproduce-then-patch, 93% on Cybench and 61.7% on DeepSWE v1.1 | VENDOR-REPORTED | [Mistral announcement](https://mistral.ai/news/mistral-large-4/) | named evaluators do not independently verify the whole comparison |
| API pricing is $1.36 input and $4.18 output per million tokens | VERIFIED | [Mistral documentation](https://docs.mistral.ai/models/mistral-large-4) | live documentation |
