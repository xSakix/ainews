+++
title = "MASS trains one model through agent teams"
description = "Sakana AI and UC Berkeley use one model to design, execute and judge multi-agent workflows, then train that model on the best team outputs."
tags = ["research", "agents"]
date = 2026-10-12T03:58:37+02:00
draft = false
+++

Sakana AI and UC Berkeley have introduced MASS, a training method in which one model improves by designing agent teams, judging their work and learning from the best results.

The preprint targets research tasks whose answers cannot be checked with a compiler or exact solution. Instead of fixing a multi-agent workflow by hand, the same underlying model writes roles, instructions, output contracts and call order, executes the resulting team, and scores candidate answers.

## Why it matters

For a team building research agents, workflow design is usually another manual prompt-engineering project. MASS turns that design into part of training, then removes the multi-agent machinery at deployment so the improved single model can answer without paying for the whole search process.

The method has two loops. In the inner loop, a workflow optimiser proposes written team structures and an executor runs them. An evaluator chooses stronger outputs from tasks without automatic ground truth. In the outer loop, the model is fine-tuned on those selected team runs and becomes the starting point for another round.

The authors compare the process to self-play, but the opponent is not another player. The model creates increasingly demanding forms of cooperation for copies of itself, then absorbs the best behaviour into one checkpoint. Team topology is therefore temporary training scaffolding rather than a permanent serving requirement.

## Selection quality is the critical dependency

MASS relies on model-based judgment because its target research questions lack a deterministic oracle. The paper uses separate frontier models, including GPT-5.5 and Claude Opus 4.8, as withheld judges for evaluation. Sakana reports that the trained model improves its judged answer quality while using fewer output tokens than the multi-agent teams that generated its training material.

That evidence is still endogenous to language-model evaluation. A judge can prefer polished, familiar or verbose responses without measuring whether a research claim is true. Withheld judges reduce direct overfitting to one evaluator, but they do not supply factual ground truth. The result is best read as improvement under the paper's judging protocol.

The training procedure tries to limit collapse onto one lucky workflow. Each generation runs a champion tournament 18 times and retains the best 16 team traces for fine-tuning. The optimiser can change role descriptions, communication order and output formats, giving it more freedom than selecting among a few fixed prompts.

The shared-model design also constrains the claim. Executor, optimiser and evaluator are roles played by one model family rather than a market of independently specialised systems. That makes recursive improvement easier to attribute to the training loop, while leaving open whether heterogeneous teams would discover different strategies.

## The workflow disappears after training

The clearest practical feature is distillation into the base model. A deployed user does not need to replay the 18-way tournament or maintain the final team graph. The extra compute is concentrated in data generation and training, while inference uses the resulting model directly.

The paper and project description are public, allowing closer inspection of prompts and evaluation design. Independent reproduction will need to test whether the gains survive different judges, factual verification and tasks outside the authors' research set.

## Verification

| Claim | Label | Primary source | Independent check |
|---|---|---|---|
| MASS uses one model as workflow optimiser, executor and evaluator, then fine-tunes it on selected team runs | VERIFIED | https://arxiv.org/abs/2610.12176 | https://pub.sakana.ai/mass/ |
| The inner loop searches written team roles, instructions, output contracts and call order | VERIFIED | https://arxiv.org/abs/2610.12176 | https://pub.sakana.ai/mass/ |
| The authors report higher judged quality with fewer output tokens after training | VENDOR-REPORTED | https://pub.sakana.ai/mass/ | none |
| GPT-5.5 and Claude Opus 4.8 serve as withheld outside judges in the reported evaluation | VERIFIED | https://arxiv.org/abs/2610.12176 | none |
| Model-based judging does not independently establish factual correctness | ANALYSIS | https://arxiv.org/abs/2610.12176 | none |
