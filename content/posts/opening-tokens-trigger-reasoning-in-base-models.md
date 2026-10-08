+++
title = "Opening tokens trigger reasoning in base models"
description = "A preprint finds that a few fixed words at the start of an answer can recover much of the reasoning performance usually associated with reinforcement learning."
tags = ["research", "models"]
date = 2026-10-08T03:57:31+02:00
draft = false
+++

Specific opening words pushed base language models into markedly better mathematical reasoning, according to a preprint that traces the effect back to patterns in their training data.

The six-author study tested whether the first tokens of a model's answer act as a cue for the style of text that follows. Fixing a short opening before generation raised accuracy without changing model weights, suggesting that some apparent reasoning gains come from selecting behaviour already learned during pre-training.

For anyone writing prompts, the finding changes the role of a phrase such as “think step by step.” Its words need not contain an instruction that the model understands as a person would. The phrase can instead point the model toward regions of its learned text distribution where worked solutions and extended reasoning are common.

## A small cue produced a large measured change

The researchers tested base versions of several open models on mathematics and coding. On 500 competition-style mathematics problems, forcing OLMo-3-7B to begin with a period, a blank line and “Okay” raised its one-attempt accuracy from 42% to 78%. Beginning Qwen3-14B with “Alright,” raised its score from 72% to 87%.

Those exact results come from the authors' experiments in an arXiv preprint and have not been independently reproduced. They also depend on the named models, benchmark and decoding setup. The paper's central evidence is broader than one prompt, however: different starts repeatedly induced different reasoning behaviour, and reinforcement learning made the successful starts more likely to occur naturally.

That distinction helps explain why post-trained “thinking” models can outperform their base models even when pre-training already supplied the underlying skills. Reinforcement learning may teach the model when to enter a useful mode and how to remain there, while the opening cue manually selects part of that behaviour.

The result also separates two questions that benchmark scores usually combine: whether a model contains a reasoning procedure, and whether ordinary generation activates it at the right moment. A cue can improve the second without adding the first. That makes prompt sensitivity part of the measured capability rather than mere noise around it, especially when two evaluators use different answer prefixes or chat templates for the same base model.

## Training-data edits changed what the cue meant

The strongest causal test altered the training association itself. The team made an arbitrary word, “chicken,” into an effective reasoning cue through targeted data interventions, and also weakened an existing cue. A related intervention made “Think duck duck goose” work like “Think step by step.”

This is more revealing than finding a lucky string by prompt search. If changing the examples connected to a token changes the behaviour that token evokes, the cue effect is tied to learned associations rather than a special semantic property of “Okay” or “Alright.” Internal representations prompted by different cues also correlated with different kinds of documents in the training set.

The method does not turn prompting into a universal substitute for reinforcement learning. A fixed opening has to be discovered for a model and task, and its success on math or code says little about reliability elsewhere. The paper's safety case study found that cues could also select different refusal and compliance patterns, making the same sensitivity relevant to safeguards.

The safety result points in both directions. A refusal benchmark can change when a seemingly harmless opening steers generation toward another class of training examples, while an attack can exploit that pathway. Evaluations therefore need to record the exact response prefix and chat template, not only the user prompt and model name.

Sophie L. Wang, Amil Dravid, Rulin Shao, Kevin Farhat, Sewon Min and Alexei A. Efros submitted the work on 5 October and released code with the preprint. Independent replications will be able to test whether the cue effects survive changes in model family, benchmark and sampling settings.

## Verification

| Claim | Label | Primary source | Independent check |
|---|---|---|---|
| Fixed opening-token cues made base models competitive with reinforcement-learning-trained counterparts on math and coding | VENDOR-REPORTED | [Wang et al. preprint](https://arxiv.org/abs/2610.06851) | none |
| The “Okay” cue raised OLMo-3-7B from 42% to 78% on MATH-500 pass@1 | VENDOR-REPORTED | [Wang et al. preprint](https://arxiv.org/abs/2610.06851) | none |
| The “Alright,” cue raised Qwen3-14B from 72% to 87% on MATH-500 pass@1 | VENDOR-REPORTED | [Wang et al. preprint](https://arxiv.org/abs/2610.06851) | none |
| Reinforcement learning made successful cues more likely and fixed cues recovered much of its performance gain | VENDOR-REPORTED | [Wang et al. preprint](https://arxiv.org/abs/2610.06851) | none |
| Causal data interventions made arbitrary phrases effective and removed existing cue effects | VENDOR-REPORTED | [Wang et al. preprint](https://arxiv.org/abs/2610.06851) | [Released code](https://github.com/sophie-xh-wang/reasoning-by-cue) |
| The preprint was submitted on 5 October 2026 by six authors | VERIFIED | [arXiv record](https://arxiv.org/abs/2610.06851) | none |
