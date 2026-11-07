+++
title = "The same answer can hide a different belief"
description = "A new paper shows that language models can make identical predictions while assigning radically different weight to the next piece of evidence. For agents, evaluators and high-stakes systems, matching outputs are not enough."
tags = ["research", "models", "agents"]
date = 2026-11-07T04:18:00+01:00
draft = false
+++

Imagine two risk models that both put the chance of a supplier failing at 30%. A procurement team would normally treat them as interchangeable. Then a late-payment report arrives. One model moves to 35%; the other jumps to 70%. The opening is illustrative, but the failure it describes is the subject of a new preprint: the same answer now can conceal a different answer to the next question.

*Same Answer, Different Future*, by researchers from UC Berkeley and Google DeepMind, studies what language models do after their present predictions have been made to match. Its central result is simple and uncomfortable. Agreement at one point in time does not imply agreement about how evidence should change that prediction. An evaluator that checks only the current answer can therefore certify systems whose future behaviour is materially different.

## Matching the prediction, changing the route

The authors use a controlled Bernoulli task. A model sees a sequence of binary observations and predicts the probability of the next one. Because the correct update is mathematically clear, the experiment can separate the answer a model states from the weight it gives to additional evidence.

Across three open-weight models, the researchers create matched initial predictions through four textual routes and two activation interventions. The routes can make the model arrive at the same probability while carrying different descriptions of the observations, summaries or assumptions. The internal interventions alter activations directly. After the initial outputs match, the models receive the same new observations.

Their updates diverge.

The paper measures an “effective evidence weight”: how much a model's prediction moves in response to new data. Models with the same starting probability can behave as though they had seen very different amounts of prior evidence. A model that acts highly certain will move little; one that treats its current answer as lightly supported will move much more. The visible number does not reveal which state the model is in.

This is not just a wording effect. The authors report that summaries scale only weakly with the number of observations they claim to represent. Telling a model that a statistic summarises a large sample does not reliably give that statistic the inertia a Bayesian observer would assign it. Conversely, explicitly eliciting a model's reasoning can change its effective evidence weights by orders of magnitude. Asking for more explanation is not always a passive measurement; it can change the process being measured.

## Why one-shot steering is fragile

The activation experiments make the result especially relevant to model control. A targeted intervention can move an immediate prediction to the desired value. But after the model receives new evidence, the effect often fades. The intervention aligned the displayed state without necessarily changing the update rule that produced it.

That distinction matters for any system that acts over time. A customer-service agent may agree with a refund policy in a test and then interpret an ambiguous message differently in production. A trading model may share a risk estimate with its replacement but react more strongly to the next market signal. A medical assistant may match a calibrated probability on a benchmark yet update inconsistently when a new symptom is added.

None of those failures is demonstrated by this paper. Its task is deliberately narrow, and controlled probability estimation is far simpler than medicine, markets or customer support. The examples are consequences to test, not claims the authors have already proved. The experiment does establish the missing property: identical present outputs do not identify identical future trajectories.

## Evaluation needs trajectories

Most model evaluations are snapshots. They present an input, record an output and score it against a reference or a judge. Calibration tests improve on raw accuracy by asking whether 70% predictions are right about 70% of the time. Yet even a calibrated snapshot can hide the dynamics exposed here. Two systems can be equally accurate and equally calibrated over one distribution while responding differently when evidence arrives sequentially.

Earlier work on language-model belief revision has already shown that models can update inconsistently when facts conflict or context changes. Research on probabilistic coherence asks whether a collection of stated beliefs obeys basic mathematical constraints. The new paper adds a temporal dimension: even when the current belief is held fixed, the path by which it was induced affects what comes next.

A stronger evaluation would therefore test update curves. It would give models the same initial evidence through different representations, match their stated predictions, and then feed identical additional observations. The score would cover not only the final answer but also sensitivity to sample size, order, framing and elicitation. For an agent, the equivalent test would replay a task with the same operational state reached through different histories.

This is also a reason to preserve provenance. If an application stores only the latest model summary, it may discard information needed to interpret future updates. A structured record of observations, their sources and the transformation that produced the summary gives the next inference step something firmer than a sentence asserting confidence. Memory systems should not merely remember conclusions; they should retain enough evidence structure to make those conclusions revisable in a predictable way.

## What builders can do now

The paper does not offer a universal correction, but it suggests three practical safeguards.

First, test sequences rather than isolated turns. Add follow-up evidence after a model passes the initial case and compare how much its answer moves across equivalent prompts.

Second, do not assume that a verbal confidence statement represents a sample size. If the number of observations matters, keep it as structured data and compute straightforward updates outside the model where possible.

Third, treat elicitation and activation steering as interventions, not transparent windows. A chain-of-thought request, a summary prompt or an internal edit can alter later behaviour. The relevant question is not only whether the immediate answer improved, but whether the change persists under new information.

Related work on Bayesian teaching offers a useful contrast. A good teacher selects examples with an understanding of how a learner will update. A system whose update rule changes with representation makes that teaching problem harder: the same example can carry different force depending on the hidden route to the learner's present answer.

## The next report

Return to the two supplier-risk models. The procurement team now knows that 30% is not a complete state description. Before approving either model, it replays the late-payment report after several equivalent histories and plots the full update curve. This closing scene is illustrative too. Its discipline is not.

For systems that make one prediction and stop, snapshot agreement may be enough. Agents rarely stop. They remember, receive evidence, revise plans and act again. Once a model has a future, the quality of its next update belongs in the evaluation of its answer today.

## References

- *Same Answer, Different Future: Language Models Hide Their Belief Updating* — https://arxiv.org/abs/2611.07913
- *Belief Revision in Large Language Models* — https://aclanthology.org/2024.emnlp-main.586/
- *From Drift to Coherence: Probabilistic Beliefs in Language Models* — https://proceedings.mlr.press/v306/kim26ah.html
- *Bayesian teaching and learning with language models* — https://www.nature.com/articles/s41467-025-67998-6
