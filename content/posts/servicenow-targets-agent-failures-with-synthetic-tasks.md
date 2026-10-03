+++
title = "ServiceNow targets agent failures with synthetic tasks"
description = "AutoSynthData validates executable tasks and adjusts the curriculum to a target model’s weaknesses."
tags = ["essays", "research", "agents"]
date = 2026-10-03T05:51:20+02:00
draft = false
+++

ServiceNow's CoreAI team describes a synthetic-data pipeline that generates training tasks from an agent's observed weaknesses, then checks whether those tasks and their success criteria work in the environment.

The October 2 engineering article introduces AutoSynthData. A stronger teacher model helps identify tasks the target model struggles with; new examples are then generated to exercise those capabilities rather than copying the evaluation prompts.

**Why it matters:** An engineer training an enterprise agent needs examples that are difficult, realistic and actually solvable. A plausible request is poor training material if the required tool is missing or the verifier rewards the wrong outcome.

The pipeline separates a task's environment specification, user request and verifier. It executes intended solutions to check that they succeed, then tests incorrect outcomes to see whether the verifier rejects them. Failed candidates enter a bounded repair loop before acceptance or rejection.

The team also reviews whole batches for repetition and gaps. Its expansion stage creates variants from vetted original tasks, but does not let those variants seed further expansion. That rule is intended to keep generation anchored rather than allowing errors to propagate through successive generations.

The authors report gains in two EnterpriseOps Gym domains using Gemma-4-26B-A4B-it as the target. In the Hybrid domain, with Qwen3.8-27B as teacher, first-attempt success improved by about 7 percentage points. In ITSM, with DeepSeek-V4.1-Flash, it rose from about 19% to 27%. These are the team's own results in the environments used for generation and evaluation.

The engineering lesson is to improve the task and the checker together. A model trained to satisfy a defective verifier can become better at the wrong job. ServiceNow says it plans to investigate this moving curriculum beyond supervised fine-tuning.

## Verification

| Claim | Label | Primary source | Independent check |
|---|---|---|---|
| October 2 article; CoreAI authors Esakkiraja, Radhakrishna, Akhiyarov and Davasam. | VERIFIED | https://huggingface.co/blog/ServiceNow-AI/autosynthdata | None; attributed primary account. |
| Capability cards, separate task components, positive/negative verification, repair, batch review and no recursive multiplication. | VENDOR-REPORTED | https://huggingface.co/blog/ServiceNow-AI/autosynthdata | None; attributed primary account. |
| Gemma target, Qwen teacher Hybrid +7.2pp; DeepSeek teacher ITSM 18.77% to 27.18%; same-environment experiments. | VENDOR-REPORTED | https://huggingface.co/blog/ServiceNow-AI/autosynthdata | None; attributed primary account. |
| Defective verifiers can reward the wrong objective; future work beyond SFT planned. | ANALYSIS | https://huggingface.co/blog/ServiceNow-AI/autosynthdata | None; attributed primary account. |
