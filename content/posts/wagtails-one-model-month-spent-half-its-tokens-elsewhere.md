+++
title = "Wagtail's one-model month spent half its tokens elsewhere"
description = "A plan to run September engineering on GLM 5.3 Flash consumed two billion tokens, but only half reached the target model. Prototypes, provider capacity and evaluation explain the gap."
tags = ["essays", "models", "tools"]
date = 2026-10-05T03:57:30+02:00
draft = false
+++

Thibaud Colas of the Wagtail core team tried to spend September doing engineering work with one efficient open model: GLM 5.3 Flash. His usage log records two billion tokens. Only one billion went to the chosen model.

That makes the experiment more useful than a clean success story. The target model itself cost about $68 and an estimated 4 kWh of electricity, according to Colas. The whole month's work reached roughly 35 kWh rather than the planned 10 kWh because prototypes, provider problems and deliberate model evaluation pulled traffic elsewhere.

The sharpest failure came from a “vibe-coded” prototype of Wagtail's experimental Model Context Protocol server. Colas says choosing the wrong model for that job consumed 450 million tokens, about $150 and 5 kWh almost overnight. The prototype worked, but its runaway usage shows how quickly an agentic experiment can dominate a carefully chosen budget.

Infrastructure was the second constraint. Colas reports degraded GLM 5.3 Flash performance and attributes it to limited capacity among independent inference providers. He switched work to alternatives including DeepSeek V4.1 Flash and Qwen 3.8 Flash. For a team trying to avoid the largest labs, model availability becomes part of model quality: a strong checkpoint is not a dependable production choice if the endpoint slows down under demand.

Some off-target usage was intentional. Wagtail is developing its own task benchmark, so the team needed to run a range of models rather than optimise only for everyday output. Colas now proposes reserving the one-model rule for more than half of normal production work while leaving research and development free to compare alternatives.

He remains positive about GLM 5.3 Flash. The model's long context, vision support and availability from several providers made it useful for Wagtail development, interface work, documentation and evaluation. That assessment is his experience rather than a controlled comparison.

The broader lesson is methodological. Token totals alone hide whether usage came from planned production, accidental loops or necessary evaluation. A useful operational dashboard needs at least cost, energy, model identity and task outcome. It also needs local, continuous measurement: the expensive prototype was visible only after it had already consumed a quarter of the month's total tokens.

This is one team's self-reported month, not evidence that GLM 5.3 Flash or open models generally cost a particular amount. Provider prices, energy estimates and task mixes vary. What the account establishes is a failure mode worth planning for: the model budget can be sound while the surrounding workflow defeats it.

## Verification

| Claim | Label | Primary source | Independent check |
| --- | --- | --- | --- |
| September usage totalled two billion tokens, with one billion on GLM 5.3 Flash | VERIFIED | [Wagtail account](https://wagtail.org/blog/one-month-on-glm-53-flash/) | none; author's usage dashboard |
| Target-model share cost about $68 and 4 kWh; whole month used about 35 kWh | COMMUNITY-REPORTED | [Wagtail account](https://wagtail.org/blog/one-month-on-glm-53-flash/) | none; author's estimates |
| Prototype consumed 450 million tokens, about $150 and 5 kWh | COMMUNITY-REPORTED | [Wagtail account](https://wagtail.org/blog/one-month-on-glm-53-flash/) | none; author's measurements |
| Provider capacity forced switches to other models | COMMUNITY-REPORTED | [Wagtail account](https://wagtail.org/blog/one-month-on-glm-53-flash/) | none; author's diagnosis |
| GLM 5.3 Flash was useful across Wagtail engineering tasks | OPINION | [Wagtail account](https://wagtail.org/blog/one-month-on-glm-53-flash/) | one practitioner's assessment |
| Model, cost, energy and outcome should be measured together | ANALYSIS | [Wagtail account](https://wagtail.org/blog/one-month-on-glm-53-flash/) | inference from the reported failure modes |
