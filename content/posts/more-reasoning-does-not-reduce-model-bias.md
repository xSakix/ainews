+++
title = "More reasoning does not reduce model bias"
description = "A 12,350-call study found no reliable decline in six cognitive-bias measures as models consumed more reasoning tokens. One direct prompt helped with anchoring."
tags = ["research", "models"]
date = 2026-10-09T04:02:06+02:00
draft = false
+++

Giving language models more time to reason did not reliably reduce their susceptibility to cognitive-bias prompts in a new study covering seven models and 12,350 API calls.

Texas Tech University researcher Obada Kraishan varied the reasoning allowance for models from Anthropic, OpenAI, DeepSeek and Qwen, then measured how their answers changed when a decision vignette included an irrelevant anchor, frame or prior commitment. None became consistently less sensitive as its actual reasoning-token use increased.

**Why it matters:** A developer choosing a larger reasoning budget for a decision-support system pays for more computation. These results say that extra computation improved no measured bias reliably, even though reasoning models often look more deliberate to users.

## The study measured thinking that actually happened

The experiment used 30 paired vignettes covering anchoring, framing, loss aversion, escalation of commitment, availability and confirmation bias. Each pair contained the same decision-relevant information, but one version added the feature expected to shift human judgement. Ten repeated samples per condition let the author measure the change in chosen options.

The seven-model panel paired reasoning and non-reasoning versions within four families. Requested reasoning ceilings were zero, 1,024, 4,096 and 8,192 tokens, though the available cells varied by provider. Kraishan logged the tokens actually consumed because the API setting often did not translate into an equivalent amount of deliberation.

That distinction proved important. The Anthropic model increased its average reasoning use as the ceiling rose but stayed well below the larger limits. OpenAI's tested model used nearly the same amount above zero, while DeepSeek-R1 and Qwen3 sometimes exceeded a requested 1,024-token ceiling. The main analysis therefore treated realised token use as the dose.

Reasoning models were not reliably less biased than their matched comparators. The direction of the difference actually leaned toward slightly greater susceptibility in all four families, but the pooled estimate was too uncertain to support that stronger claim. More important for the experiment's central question, no model showed a statistically reliable decline as it consumed more reasoning tokens.

The finding has a narrow scope. The battery contained five items for each of six biases, all drawn from managerial decision scenarios, and some family comparisons crossed between sibling models rather than switching reasoning on and off in identical weights. It tests behaviour under controlled prompts, not the correctness of open-ended workplace decisions.

## Anchoring responded to a direct instruction

Anchoring was the only tested bias that consistently moved models in the same direction usually observed in people. A number in the prompt pulled estimates toward it across all seven models. Four other categories tended to move in the reverse direction, while availability showed no reliable effect.

For the five anchoring items, the author added one sentence requiring the model to restate the anchor before answering. Anchoring fell on every item. The aggregate result narrowly missed the study's significance threshold, so it is a promising observation rather than a confirmed mitigation, but additional reasoning alone produced no comparable reduction.

This contrast is the paper's most practical result. A targeted instruction can change which information the model processes, whereas a larger reasoning budget only gives the existing process more room. The experiment does not establish that restating numbers generalises beyond five prompts; it does show why compute settings and bias controls belong in separate evaluations.

The preprint was submitted on 7 October and has been accepted at IEEE CogMI 2026. The author released the frozen prompt battery, per-call token records and analysis code in the [Anchored Minds repository](https://github.com/obadaKraishan/anchored-minds), allowing the result to be tested on newer models and larger item sets.

## Verification

| Claim | Label | Primary source | Independent check |
|---|---|---|---|
| The study made 12,350 calls across seven models in four families | VENDOR-REPORTED | [Paper](https://arxiv.org/abs/2610.10049) | [Code and data](https://github.com/obadaKraishan/anchored-minds) |
| It used 30 vignettes spanning six cognitive biases | VENDOR-REPORTED | [Paper](https://arxiv.org/abs/2610.10049) | [Code and data](https://github.com/obadaKraishan/anchored-minds) |
| Requested ceilings and realised reasoning use diverged by provider | VENDOR-REPORTED | [Paper](https://arxiv.org/abs/2610.10049) | [Code and data](https://github.com/obadaKraishan/anchored-minds) |
| No tested model showed a reliable decline in bias magnitude as reasoning-token use increased | VENDOR-REPORTED | [Paper](https://arxiv.org/abs/2610.10049) | none |
| Reasoning models were not reliably less biased than family comparators | VENDOR-REPORTED | [Paper](https://arxiv.org/abs/2610.10049) | none |
| Anchoring moved in the human direction across all seven models | VENDOR-REPORTED | [Paper](https://arxiv.org/abs/2610.10049) | none |
| Restating the anchor reduced anchoring on all five items but missed the significance threshold | VENDOR-REPORTED | [Paper](https://arxiv.org/abs/2610.10049) | none |
| The paper was accepted at IEEE CogMI 2026 and released code and data | VERIFIED | [Paper](https://arxiv.org/abs/2610.10049) | [Repository](https://github.com/obadaKraishan/anchored-minds) |
