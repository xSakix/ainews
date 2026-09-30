+++
title = "OpenAI releases GPT-6.1 Sol"
description = "OpenAI's new mid-tier model costs one-fifth as much as GPT-6 Astra at standard API rates. Its performance and safety comparisons remain company-run evaluations."
tags = ["models", "business", "safety"]
date = 2026-09-30T04:04:34+02:00
draft = false
+++

OpenAI released GPT-6.1 Sol on September 29, pricing the model at $2 per million input tokens and $10 per million output tokens through its API.

The company positions the model between its existing GPT-6 Sol and flagship GPT-6 Astra. OpenAI says the new version approaches Astra on coding, computer-use and professional-work evaluations while charging one-fifth of Astra's standard input and output prices.

**Why it matters:** Developers running agents repeatedly pay for long prompts, tool results and generated output. A lower price at near-flagship capability can change which model they leave active for routine work and which tasks still justify Astra.

GPT-6.1 Sol is available through the API as `gpt-6.1-sol` and to Plus, Pro, Business, Enterprise and Education customers in ChatGPT Work and Codex. It is not yet available in the general Chat interface. Cached input costs $0.10 per million tokens, while an Ultrafast version with faster generation is due in the coming days.

OpenAI's headline evidence comes from its own evaluation environment. On DeepSWE 1.1, the company says GPT-6.1 Sol matched Astra while costing about one-fifth as much per task. On OSWorld's offline computer-use set, it finished within roughly two percentage points of Astra at maximum reasoning effort while costing about one-seventh as much per task.

The scientific-work comparison leaves a clearer separation. OpenAI reports that Astra scored 68.1% on Terminal-Bench Science 0.1 and remained the strongest model it tested. GPT-6.1 Sol cost $5.47 per task at maximum effort in that evaluation, compared with $23.80 for Astra.

OpenAI also published a safety addendum. It classifies GPT-6.1 Sol as Critical for cybersecurity and High for biological and chemical capability under the company's Preparedness Framework, applying the same safeguard stack used for Astra. The document says the model made no attempts to bypass an automated action reviewer in a challenging internal test.

Those results remain vendor measurements. OpenAI notes that its research environment and API can differ from production ChatGPT, and the difficult factuality prompts were selected from conversations where users had already flagged errors. Independent testing will be needed to establish how the model behaves across ordinary workloads and competing agent harnesses.

The next release milestone is Ultrafast availability. Developers can already compare the standard model's actual task cost and latency with Sol and Astra using the same prompts; OpenAI has not yet published a launch date or separate price for GPT-6.1 Sol Ultrafast.

## Verification

| Claim | Label | Primary source | Independent check |
| --- | --- | --- | --- |
| OpenAI released GPT-6.1 Sol on September 29 | VERIFIED | [OpenAI announcement](https://openai.com/index/introducing-gpt-6-1-sol/) | [Associated Press](https://apnews.com/article/77b6b8888145869206996d7509d24256) reports the launch |
| API pricing is $2 input, $0.10 cached input and $10 output per million tokens | VERIFIED | [OpenAI pricing and availability](https://openai.com/index/introducing-gpt-6-1-sol/) | Public API documentation lists the model |
| The model approaches or matches Astra on named company evaluations | VENDOR-REPORTED | [OpenAI evaluation results](https://openai.com/index/introducing-gpt-6-1-sol/) | No independent reproduction located |
| Astra scored 68.1% on Terminal-Bench Science in OpenAI's comparison | VENDOR-REPORTED | [OpenAI evaluation results](https://openai.com/index/introducing-gpt-6-1-sol/) | No independent reproduction located |
| OpenAI classifies the model as Critical for cyber and High for biological and chemical capability | VERIFIED | [System-card addendum](https://deploymentsafety.openai.com/gpt-6-1-sol/respecting-auto-review) | Classification is OpenAI's own framework decision |
| Ultrafast is planned but lacks a published launch date and price | VERIFIED | [OpenAI availability section](https://openai.com/index/introducing-gpt-6-1-sol/) | DevDay recap says it is coming soon |
