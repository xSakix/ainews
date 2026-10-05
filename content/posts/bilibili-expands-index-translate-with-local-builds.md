+++
title = "bilibili expands Index-Translate with local builds"
description = "The open translation family now has GGUF, FP8 and NVFP4 packages, a free compatible API and four public benchmarks. Its performance numbers remain the developer's own."
tags = ["models", "tools"]
date = 2026-10-05T04:01:30+02:00
draft = false
+++

bilibili added official quantised builds, a free public interface and four evaluation sets to Index-Translate on 3 and 4 October, turning its recently released translation models into a more practical package for local and hosted use.

The family translates text across 150 languages and accepts instructions about terminology, formatting and style. Its ordinary text models come in 2-billion, 9-billion and preview 35-billion-parameter sizes. The largest is a mixture-of-experts model that activates about 3 billion parameters for each token.

The important change for local users is packaging. GGUF versions now target llama.cpp, while FP8 builds target vLLM and NVFP4 builds target newer Blackwell GPUs. The project publishes those formats across the text, syllable-controlled and long-document lines. Its speech models also have quantised packages, although the GGUF repositories contain only their text-model backbones rather than the complete speech pipeline.

The new hosted endpoint exposes the 35B-A3B preview through an interface compatible with OpenAI's chat API. That gives developers a way to test the model without first arranging suitable hardware. The repository labels the endpoint free, but it does not promise a service level or long-term pricing.

Index-Translate is more than a sentence translator. The client can preserve JSON and markdown structure, enforce a glossary and request a particular tone. Related packages translate speech, aim for a requested syllable count for dubbing, or carry context across a long document. These features address the awkward parts of production translation that a generic “translate this” prompt tends to miss.

bilibili also released instTrans, MEME, SandGlass and NativeLong benchmark material with evaluation scripts. That makes the test design inspectable, but the published scores are still the developer's own measurements. In the technical report, the preview model records 0.8794 on FLORES COMET-22 and 76.76 on the WMT26 judge. The latter uses GPT-5.6-Sol as evaluator, so it should not be read as an independent human comparison.

The original model family arrived on 30 September; this is not a new foundation-model launch. The news is that, within four days, it gained the deployment formats, test endpoint and evaluation artefacts needed to move from a model announcement toward something developers can actually try.

## Verification

| Claim | Label | Primary source | Independent check |
| --- | --- | --- | --- |
| Public API and four benchmarks released 4 October; quantised builds released 3 October | VERIFIED | [Project repository](https://github.com/bilibili/Index-Translate) | none |
| Text models cover 150 languages and support terminology, formatting and style constraints | VERIFIED | [Project repository](https://github.com/bilibili/Index-Translate) | [Model card](https://huggingface.co/IndexTeam/Index-Translate-35B-A3B-preview) |
| GGUF, FP8 and NVFP4 packages and their documented runtime targets | VERIFIED | [Project repository](https://github.com/bilibili/Index-Translate) | individual package links listed in the repository |
| Preview model has 35B total and about 3B active parameters | VERIFIED | [Model card](https://huggingface.co/IndexTeam/Index-Translate-35B-A3B-preview) | none |
| FLORES COMET-22 0.8794 and WMT26 judge 76.76 | VENDOR-REPORTED | [Technical report](https://arxiv.org/abs/2609.40181) | none; report uses GPT-5.6-Sol as judge for WMT26 |
| New packaging makes the family more practical to test locally or through a hosted endpoint | ANALYSIS | [Project repository](https://github.com/bilibili/Index-Translate) | inference from released artefacts; endpoint durability not established |
