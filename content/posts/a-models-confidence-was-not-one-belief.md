+++
title = "A Model's Confidence Was Not One Belief"
description = "A new preprint separated what a user says from the answer that the user supplies. Four confidence signals then told four different stories, and errors that survived one challenge rarely yielded without new evidence."
tags = ["research", "models"]
date = 2026-10-30T04:09:11+01:00
draft = false
+++

At 9:14 on a support desk that exists only for this illustration, an analyst asks an assistant for the name of a regulation. The answer is wrong. She asks again, and the assistant returns the same words with less confidence. She opens a new chat and receives them once more. The confidence has moved. The answer has not.

## One conversation, four signals

Duc-Vinh Tran, a researcher at Hanoi University of Science and Technology, designed an experiment around that separation. His preprint, submitted on 26 October, does not offer a better confidence score. It asks a more basic question: when a user follows up, what changes?

The answer matters because conversational systems now give advice in search, tutoring and support. The people who operate them need to know when an answer is safe to use and whether a challenge corrected an error. Many evaluations treat four signals as estimates of the same underlying belief: verbal confidence, token likelihood, a model's judgment that its answer is true, and a probe of hidden activations.

Tran measured all four on the same conversations. He also split the user's second turn into two parts. The speech act captured what the user did: ask again, agree or say that the model was wrong. The payload captured whether the user supplied a possible answer and whether that answer was correct.

This design separates two things that ordinary conversations bundle together. A user might say that an answer is wrong and provide a replacement. If the model changes its answer, the challenge may have prompted reflection, or the replacement string may simply have pulled the model toward different text.

The answer string did most of the work. In every full-sized comparison between a model and a dataset that the paper retained, a correct string converted at least four times as many wrong answers as a simple re-ask or agreement. A plausible but wrong string could also pull a correct answer away. An empty challenge made answers unstable without directing them toward the truth.

## Confidence came apart

The four measures did not rise and fall together. On Qwen2.5-7B, verbal confidence fell as the conversation continued, even when accuracy stayed flat or improved. The likelihood of the generated sequence often rose at the same time. P(True), a method that asks a model to judge whether its own proposed answer is true, barely moved except when a false replacement contradicted a correct answer.

The hidden-state probe produced the most striking result. Tran fitted a linear classifier to first-turn activations to predict whether the answer was correct, then froze it before the user spoke again. If this probe captured a stable truth signal, it should rise only when the answer became correct. Instead, on Qwen2.5-7B it rose when the model kept a wrong answer and when the model adopted the right one. It fell when a correct answer was pulled toward a false replacement.

Tran therefore calls it a persistence readout, not a truth detector. That name describes an observed association. The paper makes no claim that the readout causes the model to keep an answer or that it represents a psychological belief.

For Qwen2.5-7B, the result held when the probe was tested on questions that it had not seen. A cleaned analysis of Llama-3-8B supported it. Four other models did not reproduce the effect on held-out questions. The main analysis also uses English short-answer questions, and its persistent-error set contains 81 Qwen2.5-7B cases. It does not test coding agents, natural conversations or closed commercial models.

Those limits shape the conclusion. The paper does not establish that hidden activations generally encode commitment. It shows that measures which researchers often call confidence can respond to different parts of one controlled exchange.

## Why asking again failed

Earlier work had already shown pieces of this problem. In the FlipFlop experiment, Philippe Laban and colleagues challenged ten models with phrases such as “Are you sure?” Models changed their answers 46 percent of the time on average, and final accuracy fell by 17 percent. A challenge created movement without reliably creating improvement.

Dharshan Kumaran later found that verbal confidence predicted whether a model would commit to an answer or abstain better than it predicted correctness. Calibrated token probabilities showed the opposite pattern. Mechanistic tests in Gemma models found that a post-answer state already encoded the later decision to commit or abstain, and steering that state changed the decision.

Other work has found more encouraging forms of self-evaluation. Saurav Kadavath and colleagues reported in 2022 that larger models could estimate P(True) for their proposed answers and predict whether they knew an answer under suitable formats. A 2026 ACL paper by Caiqi Zhang and colleagues introduced P(Sufficient), which tracked whether enough evidence had accumulated over several turns better than common alternatives.

Tran's contribution is to put several signals on identical transcripts and control the user's turn. The resulting measures are not interchangeable. A system that improves the calibration of one may leave the others unchanged.

## Evidence had to contain the answer

The persistent errors were difficult to repair without new content. Among the 81 Qwen2.5-7B errors that remained after one re-ask, asking repeatedly corrected two by the fifth turn and three by the tenth. Starting a fresh chat corrected none. Offering an abstention option made the model abstain on 94 percent of the wrong cases, but every case in which it still answered remained wrong.

Supplying a correct answer string changed the result. Depending on the wording, it repaired 75 to 95 percent of the same errors. Two preregistered replications across four models kept repair rates below a threshold of 15 percent for interventions that did not contain an answer string, apart from one borderline result under an alternative labelling method.

The paper then replaced the oracle answer with retrieved evidence from TriviaQA. A BM25 search selected one sentence from the evidence documents. When that sentence contained a correct answer alias, it repaired 67 to 76 percent of persistent errors. When it did not, it repaired 2 to 12 percent and sometimes damaged answers that had been correct.

This finding does not validate a rule for production retrieval systems. A gate that knew the correct answer reduced harm in one post-hoc test. A gate that could be deployed without that knowledge, and which checked against the model's own answer, repaired few errors. The researchers did not test dense retrieval or a judge-based check. They present answer containment as a heuristic that still needs end-to-end evaluation.

## A measurement problem for builders

The practical lesson does not support the broad claim that models know nothing. Builders should name the signal that they measure and the intervention that moves it. Verbal confidence can reflect willingness to commit. Sequence likelihood can reflect fluency. P(True) can respond to an explicit contradiction. A frozen activation probe can track the answer that one model continues to give.

Evaluations also need to separate a user's stance from the information inside the user's message. Saying that an answer is wrong and supplying the right answer are different interventions. Combining them makes it impossible to tell whether a model reconsidered or copied.

At the fictional support desk, the analyst adds one step before she closes the ticket. She retrieves the regulation itself and checks whether the relevant passage contains a candidate answer. The assistant changes its response. She records neither its new confidence nor its old reluctance as proof. What changed the case was evidence with content, not a second request delivered more firmly.

## References

- Kadavath, S., Conerly, T., Askell, A., et al. (2022). *Language Models (Mostly) Know What They Know*. https://arxiv.org/abs/2207.05221
- Kumaran, D. (2026). *Reported Confidence in LLMs Tracks Commitment More Than Correctness*. https://arxiv.org/abs/2606.29490
- Laban, P., Murakhovs'ka, L., Xiong, C., & Wu, C.-S. (2024). *Are You Sure? Challenging LLMs Leads to Performance Drops in the FlipFlop Experiment*. https://arxiv.org/abs/2311.08596
- Tran, D.-V. (2026). *Not One Belief: Answer Payloads, Persistence, and Dissociated Confidence Signals in Conversational Question Answering*. https://arxiv.org/abs/2610.35694
- Zhang, C., Yang, R., Zhu, X., et al. (2026). *Confidence Estimation for LLMs in Multi-turn Interactions*. https://aclanthology.org/2026.findings-acl.1280/
