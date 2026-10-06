+++
title = "Reflection previews Beam before releasing its weights"
description = "The 501-billion-parameter mixture-of-experts model is available only through early access. Reflection says weights, a technical report and developer tools will follow later in October."
tags = ["models", "agents"]
date = 2026-10-06T04:09:31+02:00
draft = false
+++

Reflection AI has announced Beam, a 501-billion-parameter model for coding and agent work, but developers cannot inspect or run its weights yet.

The California AI company describes Beam as a sparse mixture-of-experts model: it stores 501 billion parameters but activates 23 billion for each token. Early access requires a sign-up, while the weights, licence, model card, technical report and developer tools remain pending.

For a developer choosing an open model, the distinction matters. An open-weight model can be tested on private workloads, modified and deployed without relying on the maker's service; an announcement and benchmark table cannot yet support those checks.

Reflection says it trained Beam on 23.8 trillion tokens and then ran more than 100 million reinforcement-learning rollouts on 10,500 NVIDIA GB300 GPUs for four weeks. Those figures describe an unusually large training run, but the company has not released the technical report needed to examine the data mix or evaluation setup.

The lab's own table gives Beam scores of 80.9 on SWE-bench Verified and 80.1 on Terminal-Bench 2.1. It also shows Beam behind Kimi K3, GLM-5.3 and Qwen 3.8-Max on most listed tests. Reflection's main comparison is efficiency: it says Beam reaches results comparable with GLM-5.2 while using three to four times less inference compute, based on its own floating-point-operation estimate.

That claim could matter more than a narrow benchmark lead for teams paying to run long agent sessions. Sparse activation reduces the computation used for each token, although the full model still requires enough memory and infrastructure to store and serve hundreds of billions of parameters.

Reflection says Beam is undergoing final safety testing. The company plans to publish the weights, technical report, model card and developer artefacts later in October 2026; it has not given a specific release day.

## Verification

| Claim | Label | Primary source | Independent check |
| --- | --- | --- | --- |
| Reflection announced Beam and opened early-access registration | VERIFIED | [Reflection announcement](https://reflection.ai/blog/introducing-beam) | none needed for the company's action |
| Beam has 501B total parameters and 23B active parameters per token | VENDOR-REPORTED | [Reflection announcement](https://reflection.ai/blog/introducing-beam) | none; weights and report are pending |
| Training used 23.8T tokens and more than 100M RL rollouts on 10,500 GB300 GPUs for four weeks | VENDOR-REPORTED | [Reflection announcement](https://reflection.ai/blog/introducing-beam) | none |
| Beam scored 80.9 on SWE-bench Verified and 80.1 on Terminal-Bench 2.1 | VENDOR-REPORTED | [Reflection announcement](https://reflection.ai/blog/introducing-beam) | none |
| Reflection estimates comparable results to GLM-5.2 at 3–4x less inference compute | VENDOR-REPORTED | [Reflection announcement](https://reflection.ai/blog/introducing-beam) | none |
| Weights, report, model card and developer artefacts are promised later in October 2026 | VERIFIED | [Reflection announcement](https://reflection.ai/blog/introducing-beam) | none needed for the stated schedule |
