+++
title = "A language model rewrote its own weights and improved"
description = "Researchers gave an open 27B model access to its weights, graded answers and a way to test edits, while blocking gradients and optimisers. The model raised held-out accuracy by 6.6 points and repaired a damaged copy of itself, but smaller models failed under the same conditions."
tags = ["models", "research"]
date = 2026-11-21T04:12:00+01:00
draft = false
+++

A model sat in front of a Python session with its own weights exposed. It could inspect hidden states, change selected matrices and ask a copy of itself to solve another problem. It could not calculate a gradient. Twenty forward passes and a fixed clock were all it had.

*The scenes that open and close this article are illustrations; the people in them are invented.*

Jiajun Fan and ten co-authors gave that setting to four open models in one family. The 2B model did not edit itself. The 4B and 9B models tried random changes and made themselves worse. The 27B model measured where its hidden states differed, edited along those directions and kept changes only when paired tests supported them. One edit raised its accuracy on 490 held-out problems by 6.6 percentage points.

The paper calls the method self-rewriting. Its central claim is narrow and consequential: a deployed model can make a persistent improvement to its own weights through forward-pass reasoning alone. The work is a preprint, and the authors say that it is the first demonstration of its kind.

## A model with access to itself

Training normally separates the system that searches for better weights from the model that later uses them. An optimiser calculates gradients over a loss, engineers choose data and settings, and a cluster writes the result into a new checkpoint. Inference begins after that process has stopped.

Fan and his colleagues removed the optimiser but gave the model tools. It received graded answers on practice problems, access to its weight tensors and a Python session that retained state across turns. It could run the unedited and edited model on the same problems with the same random seeds. It could also read hidden states that the model produced on texts of its choice.

The environment enforced the boundary. Gradients were disabled. Calls to optimisers, networks, new processes and model-loading functions were refused. The model could not alter the input embedding, final normalisation or output layer. It had at most 20 forward passes and 200 code executions in a session.

A paired test compared answers problem by problem. That mattered because a small aggregate gain could otherwise come from sampling noise. The framework reported how many answers changed from wrong to right, how many moved the other way and how often either version ran out of its 16,384-token budget.

In the stricter protocol, the framework also tested a proposed edit once on reserved practice problems that the model could not inspect. The model then submitted the change or withdrew it. Five of the first eight sessions withdrew. The accepted edits never lowered the accuracy of the model that remained in use.

## What the largest model changed

The 27B model did not search every parameter. It found directions in its hidden states that were associated with failures and weakened how selected output matrices wrote along those directions. The operation resembled subtracting a rank-one component from a matrix.

That intervention reduced a visible failure: some answers repeated a sentence until they exhausted the token limit. In one held-out example, the base model repeated the same sentence 549 times and never answered. The edited version completed the problem.

Across the fixed evaluation, the most successful edit produced the 6.6-point gain. Two sessions in the sequence produced improvements with paired-test probabilities below one in 100,000 under the authors' test. After the eighth session, accuracy reached 63.8%.

Each session started its investigation from the base weights, but an accepted edit replaced the model in use. The sequence therefore accumulated decisions rather than blindly stacking every proposed change. The authors report that accuracy rose or stayed level through all eight sessions.

The improvement did not require extra computation for each later answer. Once written, the change lived in the checkpoint. That distinguishes it from test-time scaling, which buys a better answer by spending more tokens or samples every time.

## Repair without the original

The team also designed a failure with a known cause. It overwrote eight consecutive rows in one multilayer-perceptron output matrix with noise scaled to 200 times the matrix's standard deviation. The damaged model solved almost nothing.

The editing model was undamaged, but it could inspect only the corrupted copy's runs and weights. It was told that some values were wrong, not where the damage sat or how it had been produced. It never read the corresponding clean values.

The 27B model located the faulty matrix and wrote replacement values of its own. A repair that it found on text mathematics carried over to six image benchmarks that the session had never seen. The repaired copy recovered 83% of the base model's pooled accuracy. On ScreenSpot-v2, it rose from zero to 89%, compared with 93% for the undamaged model.

This test avoids one easy interpretation of the main result. A model might make a narrow edit that exploits quirks in the practice problems. Repairing a deliberately damaged component and recovering performance on images shows that the model can identify and partly restore a more general function.

It does not show that a model can repair arbitrary damage. The corruption affected one constructed block, and the experiments used one model family, Qwen3.5, at four sizes. The model had graded practice answers and unusually direct access to internal tensors. Ordinary hosted assistants have none of those privileges.

## The scale boundary

The smaller models reveal the present limit. The 2B model did not treat its weights as something that it could usefully change. The 4B and 9B versions added random noise. When a test showed harm, they guessed at another intervention.

The 27B model completed a longer chain: it diagnosed a symptom, inspected activations, formed a hypothesis, changed a matrix, ran a paired test and revised its plan when the result was negative. The authors describe this as an ability that emerges with scale, but four sizes from one family cannot locate a general threshold.

A companion preprint published in the same week studied a different arrangement: an external language model chose weight edits for smaller target models. That system matched black-box search on SmolLM2 and Qwen2.5 and exceeded it on Pythia. Fan's paper moves the editor and the edited object into one model, which is the feature that supports its stronger claim.

The authors connect the result to recursive self-improvement. Their experiment remains far from an autonomous loop. People supplied the task, the failure signal, the tools, the edit constraints and the acceptance test. The sessions lasted hours on one GPU, and the strongest evidence concerns a bounded set of reasoning problems and one artificial fault.

Those boundaries are also what make the result inspectable. Every accepted change passed a paired comparison, every held-out problem stayed outside the editing session, and every smaller failure remained in the record.

Back at the Python prompt, the model used its final forward pass and left an edit on disk. The next answer needed no longer prompt and no extra sample. A few altered matrices carried the difference.

## References

- Fan, J., He, N., Yang, C., Mao, A., Zhu, X., Cheng, C., Liang, K., Shen, S., Li, Z., Guo, R., & Liu, G. (2026). *Language Models Can Rewrite Their Own Weights*. https://arxiv.org/abs/2611.21885
- Yang, C., et al. (2026). *Can an LLM Fix a Language Model Without Training It?* https://arxiv.org/abs/2611.25613
