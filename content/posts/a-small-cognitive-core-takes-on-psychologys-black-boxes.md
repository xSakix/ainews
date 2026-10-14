+++
title = "A small cognitive core takes on psychology's black boxes"
description = "Two researchers combined a few established ideas about memory, context and prediction error into one model of human choice. CORE beat matched neural predictors across 137 experiments while keeping its internal operations open to inspection."
tags = ["research", "models"]
date = 2026-10-14T04:02:33+02:00
draft = false
+++

Imagine a participant sitting alone in a psychology lab. A symbol appears, then another. She guesses which door hides a reward, remembers the last surprise and slowly changes her strategy. This participant is invented, but each small act belongs to the experimental record behind a new model that tries to explain millions of such choices without hiding the explanation inside a neural network.

## Many experiments, one account

Marcel Binz and Eric Schulz of the Institute for Human-Centered AI at Helmholtz Munich have built COntextual Retrieval and Encoding, or CORE. Their preprint joins a small set of established cognitive principles in one computational model, then fits it jointly to 7,036,442 human choices from 137 experiments and 80,452 experimental sessions.

The ambition is larger than predicting one task. Psychology has accumulated accounts of association, prediction error, hierarchical representation, memory retrieval and forgetting, often tested in separate experimental traditions. CORE asks how much of the behavioural record those ideas can explain when they must work together under one set of mechanisms.

Its structure is a hierarchy of episodic memories. Prediction errors are written into those memories. Context governs what gets encoded, which memories are retrieved and how they fade. These operations are expressed as components whose roles a researcher can inspect rather than as an unrestricted sequence model trained only to minimise error.

The authors compare CORE with a transformer of matched configuration and with Centaur, a foundation model of human cognition introduced by a large collaboration led by Binz. Centaur fine-tuned a language model on Psych-101, a dataset covering more than ten million choices in 160 experiments. It demonstrated that one large predictive system could generalise across cover stories, task modifications and unfamiliar domains. It also raised the familiar price of foundation models: prediction became broad, while the learned mechanism remained difficult to state as a psychological theory.

CORE reverses that trade. In the new paper, it records a lower predictive negative log-likelihood than the matched transformer, 262,572 against 329,043. Against Centaur the comparison is 262,572 against 389,151. CORE performs better than the transformer in all 62 studies used for that study-level comparison and better than Centaur in 47.

These figures do not mean that CORE has captured the human mind. They compare predictions inside a particular assembled experimental corpus. They do show that an interpretable model was not forced to sacrifice predictive reach merely because its parts had psychological meanings.

## What the model remembers

The hierarchy matters because a choice can depend on events at different scales. A recent error may change the next response. A run of related trials may establish a local situation. A shift in the experiment can make older experience less relevant even when it remains stored.

CORE handles those effects through context-sensitive encoding and retrieval. Prediction errors update memory instead of simply changing a single value estimate. The model can retrieve an episode when the current situation resembles it, while its forgetting process discounts experience as context moves away.

That design produces internal traces familiar from established theories. The authors report signatures of Bayesian learning in CORE's latent variables: its updating responds to uncertainty in ways associated with probabilistic inference. They also find event-segmentation signatures, meaning the model's internal organisation reflects boundaries between situations rather than treating the full stream as uniform.

The result extends a research programme the same authors have pursued from the opposite direction. In 2023, Binz and Schulz showed that language models fine-tuned on psychology experiments could outperform traditional cognitive models in two decision domains and carry information about individual participants. Their work on meta-learned cognition argued that learning algorithms could approximate Bayes-optimal behaviour while incorporating limited computation and other realistic constraints.

Those systems asked how far general machine-learning machinery could travel toward human behaviour. CORE asks how far a compact psychological theory can travel toward the predictive range of machine learning. The two directions now meet on some of the same data.

## Reproducing effects instead of naming them

Prediction is only part of the test. The authors simulate CORE in the experimental conditions and ask whether it reproduces the behavioural effects that the studies reported. It recovers 75% of them.

This is a stricter demand than matching an average choice rate. An effect can involve adaptation, bias, order, uncertainty or a change after a contextual boundary. Reproducing it requires the model's behaviour to move in the relevant direction when the experimental manipulation changes.

The missing quarter matters as much as the successful three quarters. A unified model becomes scientifically useful when its failures identify where the proposed core is incomplete. A black-box predictor can absorb another pattern without telling researchers which theory changed. An interpretable system forces a clearer choice: revise retrieval, add a mechanism, alter the hierarchy or accept that the phenomenon falls outside the account.

The paper's breadth also creates risks. Experiments differ in their instructions, response formats, participant populations and analytical conventions. Joint fitting can favour mechanisms that explain common structures while smoothing over unusual ones. A total likelihood can conceal a weak account of a small but important domain. The authors therefore report study-level comparisons and simulated effects, not only one aggregate score.

CORE is also a preprint. Its claims, implementation choices and dataset harmonisation have not completed peer review. The corpus is large by the standards of experimental psychology but remains a selected record of tasks that can be represented and fitted together. Human life outside a laboratory includes language, social relationships, emotion and embodied action that are not compressed into seven million discrete choices.

## A theory that can be wrong

The model's main contribution may be methodological. Cognitive science has often had to choose between a transparent model that explains one paradigm and a general predictor that says little about mechanism. CORE supplies evidence that this boundary can move.

That does not eliminate neural or foundation models. Centaur establishes a strong predictive baseline and can generalise through natural-language task descriptions. A compact model can use such systems as rivals, data generators or discovery tools. The important distinction is what claim each supports. A predictor shows that behaviour can be anticipated. A cognitive theory states the operations it believes produced it.

Because CORE states those operations, researchers can intervene on them. They can remove contextual forgetting, flatten the memory hierarchy or change how prediction errors are written, then identify which experiments fail. They can also add a proposed principle and test whether it earns its place across the full record rather than improving one hand-picked task.

Return to the imagined participant facing two doors. Her next choice can now be predicted by a large opaque model or reconstructed through a memory of surprises, arranged by context and allowed to fade. The first may be right. The second gives the scientist something else: a precise account that the next experiment can prove wrong.

## References

- Binz, M., Dasgupta, I., Jagadish, A., Botvinick, M., Wang, J. X., & Schulz, E. (2023). *Meta-Learned Models of Cognition*. https://arxiv.org/abs/2304.06729
- Binz, M., et al. (2024). *Centaur: a foundation model of human cognition*. https://arxiv.org/abs/2410.20268
- Binz, M., & Schulz, E. (2023). *Turning large language models into cognitive models*. https://arxiv.org/abs/2306.03917
- Binz, M., & Schulz, E. (2026). *A small cognitive core explains human behavior at scale*. https://arxiv.org/abs/2610.13603
