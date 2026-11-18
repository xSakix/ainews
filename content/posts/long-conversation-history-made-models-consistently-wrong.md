+++
title = "Long Conversation History Made Models Consistently Wrong"
description = "A 100-turn study found that full chat history drove state-tracking accuracy from about 60 percent to 10 percent. Verified summaries preserved the answers, while common monitors often made the failing system look stable."
tags = ["research", "models"]
date = 2026-11-18T04:00:29+01:00
draft = false
+++

Marta checks the inventory assistant before the morning shift. The dashboard is green. Its answers agree with one another, its language is calm, and the warehouse totals have barely moved across the last five questions. Then she compares one number with the ledger. The assistant has carried the same mistake through every answer.

*The scenes that open and close this article are illustrations; the people in them are invented.*

A preprint by Ali Şenol of Tarsus University tests that quiet failure. In 100-turn conversations about changing budgets, inventories, laboratory containers and project milestones, model accuracy fell from about 60 percent to about 10 percent within twenty turns when the full transcript stayed in context. A solver-verified state summary kept accuracy more than 50 percentage points higher. The usual signs of orderly reasoning did not give a reliable warning.

## The transcript becomes part of the problem

Long conversations ask a model to do two jobs at once. It must solve the current problem, and it must decide what to retain from everything that it and the user said before. The second job becomes harder when the state changes, an earlier fact is corrected, or the model has already made an error.

Prior work had isolated part of this problem. In *LLMs Get Lost in Multi-Turn Conversation*, Philippe Laban and his co-authors divided complete tasks into pieces that arrived over several turns. Models often committed to an answer too early. Their performance fell even though the underlying problem had not changed. That study used tasks derived from GSM8K, the dataset of 8,500 grade-school maths problems that Karl Cobbe and colleagues introduced in 2021.

Şenol asked a narrower causal question first: does keeping the model's own replies make the final answer worse? He selected 48 divided maths tasks with four to nine turns. GPT-4o-mini, Llama 4 Scout and Mistral 7B each saw two versions. One version kept the dialogue. The other rebuilt a fresh prompt from the information that the user had supplied and left out the assistant's earlier answers.

All 11,382 model calls finished. GPT-4o-mini solved 33 of 48 tasks with its own replies in view and 43 with a fresh prefix, a fall of 21 percentage points. Mistral 7B fell from 17 correct tasks to three, or 29 points. Llama 4 Scout moved in the same direction, but its ten-point difference did not reach the study's statistical threshold.

Mistral's error had a visible form. With its earlier answers present, it often reached the last turn and still said that it needed more information. The fresh prompt contained the same facts and produced an answer.

## A hundred turns with an exact ledger

The first experiment ended after at most nine turns. It also could not separate a harder late question from damage caused by a longer conversation. Şenol therefore built CDR-Stream, a benchmark in which every turn updates a state and asks a question with an exact answer.

The benchmark covers four kinds of state: a budget ledger, warehouse inventory, a laboratory protocol and a chain of project milestones. A user message may add a delivery, correct an earlier entry or move a quantity between locations. It may include distracting sentences. The question asks for a sum, a difference, a count above a threshold, a maximum, a hypothetical result or a share.

An exact solver produces the correct answer for every turn. A twelve-level ladder changes one source of difficulty at a time, such as the number of events or the complexity of an update. The study calibrated that ladder separately for each model, then froze the settings. This choice makes the experiment useful for measuring decline inside a model, but it means that its raw scores should not rank the models against one another.

GPT-4o-mini, Llama 3 70B and Gemma 3 12B each received thirty 100-turn dialogues. In one arm, the prompt held the full conversation. In the other, it held a verified summary of the current state and the new user turn. Both arms used the same instructions and answer format.

The full-history curves nearly overlapped. Accuracy began around 0.6 in the first five turns, fell to roughly 0.3 over turns six through twenty, and settled between 0.08 and 0.11 for the remaining eighty turns. Even when the questions stayed in the easiest regime, full-history accuracy after turn twenty ranged from 0.10 to 0.14.

The verified summary changed the result. On those same easy conversations, it held accuracy between 0.82 and 0.86. Across all five difficulty patterns, the average advantage was 0.521 for GPT-4o-mini, 0.545 for Llama 3 and 0.588 for Gemma 3. When a sequence returned from hard questions to easy ones, summary-based performance recovered. Full-history performance did not.

## A stable answer can be a stable mistake

An operator does not have the exact solver that the experiment used. A deployed system needs a signal that says when its current answer has stopped tracking reality. The study tested several candidates: consistency across sampled answers, logical coherence, semantic similarity, a paired readiness measure and standard detectors for changes in a stream.

None gave a robust warning across models. In the shorter maths experiment, the measured quality signals had no statistically detectable association with final failure after the analysis controlled for turn, revealed information and context length. One signal covered only 29 source tasks, so the paper does not claim that every small association has been ruled out.

The hundred-turn study produced a more troubling pattern. Consistency and coherence moved far less than accuracy. Stability rose because the models repeated similar wrong answers. A monitor that rewards agreement could therefore become more confident as the underlying state estimate deteriorates.

Şenol fixes the scope of that conclusion carefully. Both studies use arithmetic and exact state tracking, which make correctness observable but do not represent every open-ended conversation. The model sets differ between the two experiments, and they do not include the strongest current frontier systems. Gemma 4 31B was too accurate for the planned difficulty ladder, so a valid test would require harder tasks rather than more repetitions of these ones.

The long experiment also lacks a user-only comparison. It therefore measures the full-history failure but cannot assign a precise share to the assistant's previous replies, the length of the context or the growing burden of state. Repeat-based monitoring was complete only for GPT-4o-mini. Several monitoring analyses were exploratory rather than part of the frozen confirmatory tests.

## State belongs outside the transcript

The intervention in the paper is modest. It does not give the model a better memory. It removes the need to reconstruct the present from the whole conversation by supplying a compact state that an external program has checked.

That architecture separates evidence from narration. The transcript can remain available for an audit, while the active prompt receives the current ledger, inventory or task state. Şenol also proposes checks across separate sessions and counterfactual re-queries, because a detector inside one deteriorating stream may never get a clean baseline.

The paper leaves a difficult engineering problem. Its summaries came from an exact solver. Most real systems do not have one, and a model that writes its own state file can preserve an error as efficiently as it preserves a fact. The open question is how a system can maintain and verify that external state without quietly turning the summary into another untrusted reply.

Marta opens the state file beside the chat. One warehouse transfer appears there once, with its source event and correction. The transcript still contains the assistant's five matching answers. She leaves them in the archive and sends the checked ledger with the next question.

## References

- Cobbe, K., et al. (2021). *Training Verifiers to Solve Math Word Problems*. https://arxiv.org/abs/2110.14168
- Laban, P., Hayashi, H., Zhou, Y., & Neville, J. (2026). *LLMs Get Lost in Multi-Turn Conversation*. https://arxiv.org/abs/2505.06120
- Şenol, A. (2026). *The Silent Cost of Conversation History in LLM Reasoning*. https://arxiv.org/abs/2611.20071
