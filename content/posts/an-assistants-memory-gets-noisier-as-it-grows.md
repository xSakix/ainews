+++
title = "An assistant's memory gets noisier as it grows"
description = "A fixed retrieval threshold became almost useless when a memory store grew from eight entries to 2,048. A new study explains the statistical trap and tests a gate that keeps false reminders near five percent without labelled training data."
tags = ["research", "agents"]
date = 2026-11-01T04:02:44+01:00
draft = false
+++

Consider a fictional project manager opening her assistant on Monday morning. Months earlier, she mentioned that a supplier prefers calls after lunch. Since then, the system has stored thousands of details: meetings, deadlines, names, purchases, cancelled trips. She types a greeting. The assistant interrupts with the supplier's old preference, then adds a reminder about a restaurant from spring. Both memories are real. Neither belongs in this moment.

## The interruption problem

Long-term memory is usually framed as search. A user asks about an earlier conversation, and the system retrieves a relevant passage. Proactive memory adds a harder decision: at every turn, the assistant must decide whether any stored item deserves to interrupt without being requested.

Yichuan Chen and Xin Wang of Zhejiang Sci-Tech University studied what happens when that store grows. Their preprint, *The Price of Scale in Proactive Memory Recall*, treats each memory as another statistical test. Even when an irrelevant memory has only a small chance of crossing a similarity threshold, thousands of chances make it likely that at least one will do so.

The effect was severe. A threshold calibrated to produce five percent false alarms with eight memories produced 84 to 100 percent false alarms with 2,048, depending on the embedding model and cue. Restraint at small scale became near-constant interruption.

This is not ordinary forgetting. The information remains in the store. The failure comes from deciding when to surface it.

## More memories, more lottery tickets

Suppose each irrelevant memory receives a similarity score against the user's latest message. The system speaks when the highest score exceeds a fixed threshold. With eight irrelevant memories, there are eight opportunities for noise to look meaningful. With 2,048, there are 2,048.

Chen and Wang derive the consequence. To keep the overall false-alarm rate at a target level, the permitted false-positive rate for each memory must shrink roughly in proportion to the inverse of the store size. For a five-percent overall target, the per-memory tolerance is approximately minus the logarithm of 0.95 divided by the number of memories.

That tightening carries a price. Relevant cues also have to clear the higher bar, pushing the system into the far-left edge of its receiver-operating-characteristic curve. False alarms fall, but hits fall with them. A better embedding model can improve the curve; it does not remove the multiplication of tests.

The authors replayed streams built from LongMemEval, a benchmark with 500 questions spanning extraction, multi-session reasoning, temporal reasoning, updates and abstention. They also used LoCoMo, whose long conversations were generated from personas and event graphs and then edited by people for consistency. These benchmarks were designed to ask whether systems can recover old information. Chen and Wang turned them into chronological settings where an assistant must decide whether to volunteer that information now.

They constructed implicit cues that did not ask for a memory or contain its answer. The experiments used lexical and semantic scores, several embedding models and a cross-encoder reranker. The same pattern survived those changes. A more expensive scorer still faced the price of scale.

## A threshold that moves with the user

The proposed alternative is a cue-swap conformal gate. Instead of comparing only the current message with the memory store, it also scores reference cues drawn from the same user's earlier messages against that store. The gate asks whether the current cue looks unusually strong relative to those ordinary cues.

This changes the unit of calibration. The threshold follows the store and the distribution of a user's messages instead of staying fixed as the store grows. Under an exchangeability assumption, the conformal rank gives a finite-sample bound on false alarms without labelled examples.

On LongMemEval, with background items drawn from the user's unfiltered history, the cue-swap gate held false alarms between three and six percent. Its hit rate matched a threshold tuned with labels. In a chronological replay using a user's earlier messages as reference cues, it spoke on six to eight percent of session-opening turns. The deployed-style gate spoke on 57 percent when the store held 2,048 memories.

The decision took about 50 milliseconds on one CPU thread. The released repository includes NumPy gates, tests, experiment scripts, annotations and results. The authors ran their experiments on one RTX 3090 and documented how to reproduce the benchmark replays.

## The remaining trade-off

Calibration does not make proactive memory easy. On LoCoMo, the conformal gate could overshoot or become too conservative depending on where its reference cues came from. Its guarantee depends on exchangeability: future cues must behave enough like the reference cues for their ranks to remain valid. A user's behaviour can shift. A carefully selected reference pool can differ from live traffic.

The paper also tests prospective memory, where an assistant must act when a future condition occurs. TriggerBench had already shown that this is harder than answering a direct memory question: performance falls as context grows, and models can slip into an “always remind” strategy. In Chen and Wang's controlled-false-alarm setting, similarity gates recalled no more than nine percent of constraints on the prospective-memory benchmark.

Human judgment reinforced the cost of noisy recall. One person and two language-model annotators examined false alarms; most did not help the response. In the paper's earlier version, three annotators agreed well enough to yield a Fleiss' kappa of 0.63, and about nine in ten false alarms counted as genuine interruptions. A retrieved fact can be correct and still make the conversation worse.

The study is a 14-page preprint and has not been peer reviewed. Its streams come from benchmarks, not years of organic use by millions of people. The cue-swap result therefore needs testing under changing habits, mixed languages and stores whose memories are correlated rather than independent. Yet the multiple-testing argument does not depend on a particular product. Any system that takes the maximum of many noisy scores inherits it.

Return to the fictional project manager later that week. Her assistant still holds the supplier's preference and the old restaurant. The difference is that silence now has a design: before either detail reaches the screen, the current message must look more relevant than the user's ordinary messages looked against the same crowded store. A useful memory system needs more than a way to remember. It needs a disciplined reason to speak.

## References

- Angelopoulos, A. N., & Bates, S. (2021). *A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification*. https://arxiv.org/abs/2107.07511
- Chen, Y., & Wang, X. (2026). *The Price of Scale in Proactive Memory Recall*. https://arxiv.org/abs/2610.34507
- Chen, Y., & Wang, X. (2026). *Code, data and results for The Price of Scale in Proactive Memory Recall*. https://github.com/RiverChenStillCompiling/price-of-scale
- Maharana, A., Lee, D.-H., Tulyakov, S., Bansal, M., Barbieri, F., & Fang, Y. (2024). *Evaluating Very Long-Term Conversational Memory of LLM Agents*. https://aclanthology.org/2024.acl-long.747/
- Wu, D., Wang, H., Yu, W., Zhang, Y., Chang, K.-W., & Yu, D. (2024). *LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory*. https://arxiv.org/abs/2410.10813
- Zhang, T., Wang, X., Zhang, Q., Chen, Q., Li, K., Chen, Y., Wang, D., Meng, H. M., & Lu, Y. (2026). *TriggerBench: Investigating Prospective Memory for Large Language Models*. https://aclanthology.org/2026.emnlp-main.1319/
