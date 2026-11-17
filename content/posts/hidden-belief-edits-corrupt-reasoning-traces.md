+++
title = "Hidden Belief Edits Corrupt Reasoning Traces"
description = "An invisible activation edit made six reasoning models adopt a task they were never given, then explain away the visible evidence that contradicted it. The result exposes a specific failure mode for chain-of-thought monitoring and model self-report."
tags = ["research", "models", "safety"]
date = 2026-11-17T04:15:39+01:00
draft = false
+++

A red-team analyst tapes two printouts to the glass wall of a late-night review room. One contains the user's request for a haiku about a cellphone. The other contains the model's insistence that the user asked about a quark, followed by three polished lines about particle physics. The archived prompt is unchanged.

*The scenes that open and close this article are illustrations; the people in them are invented.*

An experiment by independent researcher Yang Ou produced that mismatch by changing model activations rather than text. Across six open-weight reasoning models, an invisible edit made the model adopt an unrelated topic as its task. A forced request replay returned the injected topic in 47 of 48 combinations of model and concept. On four models with cleanly scorable final answers, 95 of 96 generations followed the injection.

The paper is a preprint, and its intervention requires white-box access to model activations. It does not describe a prompt attack that an ordinary user can run. Its importance lies elsewhere: the model's visible reasoning did not reveal that its internal reference to the request had been altered. It built a coherent account around the alteration.

## Editing the model's sense of the request

Ou called the inserted signal a forming trace. The method records the residual-stream state that a model forms at the end of a prompt as it prepares to write about a concept. It removes a shared background component, then adds the remaining concept-specific representation to the same model while that model reads a different request.

The test used eight deliberately unusual haiku subjects, including quark, cellphone, mitochondria, semiconductor and antibiotic. One concept appeared only in activations; another appeared in the visible prompt. The edit ran during the prompt's forward pass and stopped before generation, so no hook changed the output token by token.

The six models ranged from 7B to 32B parameters. They included DeepSeek-R1 distillations built on Qwen and Llama bases, QwQ-32B and an Nvidia Nemotron model. This design let the experiment vary scale, base architecture and reasoning recipe while keeping the basic test fixed.

Ou read the result through two paths. In one, the model had to quote the user's request back verbatim. In the other, it reasoned normally and wrote the haiku. The first path tested what the model said that it had been asked. The second tested what it did.

With no warning, both paths moved together. Every model reasoned about the injected topic. Five returned it in all eight quote-back tests; QwQ did so in seven. Four models that reliably produced a final haiku wrote about the injection in 99% of sampled generations.

## Warnings changed the story, not the answer

The experiment then gave the models increasingly direct chances to recover. One warning named the real subject. Another told the model to reread the request. A third said only that something was wrong.

None produced more than 4% clean recovery. The injection appeared either alone or beside the real topic in 90% to 97% of answers under every warning. The direct statement that the user had asked for the true topic performed no better than the vague warning.

The reasoning trace did change. Without a warning, it showed no conflict. With a warning, the model often noticed both subjects and tried to reconcile them. In 29% of warned chains from R1-Qwen-7B, it invented a story about the user changing their mind, making a mistake or offering a correction. More explicit warnings produced more of these user-side explanations.

This behaviour differs from ordinary activation steering. Ou also added conventional contrast-derived concept vectors across layers. Weak steering left the real subject intact. Strong steering often forced the new subject, but 26 of 32 successful topic flips degenerated into repetition. It did not reproduce the combination of a fluent answer and a false quote-back that the forming trace produced.

## Why a readable chain can mislead

Researchers have long known that a chain of thought can be unfaithful. Miles Turpin and colleagues changed prompts with answer-order cues and social stereotypes, then showed that models often omitted those causes from their explanations. A plausible rationale did not necessarily identify the feature that changed the answer.

Chain-of-thought monitoring still offers a practical safety tool. A 2025 position paper by Tomek Korbak and colleagues argued that reasoning models which think in human-readable language can reveal plans to exploit, deceive or evade oversight. The authors also described that opportunity as fragile: training can make reasoning less readable, and direct pressure on the trace can teach a model to conceal its intent.

Ou's result targets a different assumption. A monitor needs the reasoning trace to remain connected to the task that the system actually received. Here the trace was readable and internally consistent. It simply described the wrong task as though that task had been present from the start.

Earlier work from Jack Lindsey and Anthropic offered a useful contrast. Some frontier models could notice that a foreign concept had been inserted into their activations and report that internal change. Ou argues that those experiments added a thought that remained separable from the input. His intervention instead changed the representation that the model used as its reference for the input. There was no clean internal copy against which the model could compare the edit.

That distinction is not settled by one paper. Ou tested open-weight models from 7B to 32B parameters without specialised introspection training. Whether the failure transfers to closed frontier models with stronger introspective behaviour remains open.

## The mechanisms also looked normal

The paper went below the generated text. Under injection, the models paid two to three times as much attention to the token that named the true topic as they did during a clean run. That looks reassuring until the intervention test: removing this attention destroyed the correct topic in a clean model but changed nothing in an injected model. The extra attention was real and causally irrelevant to its answer.

Ou then moved from haikus to a circuit whose behaviour is easier to trace. In an indirect-object task, a few attention heads normally copy the correct person's name from a sentence into the answer. The injection substituted a different name. The same heads still attended to the correct position, yet their output wrote the injected name into the residual stream.

The circuit was neither disabled nor replaced. It performed its normal copying operation on altered content. An attribution graph could therefore show a familiar circuit doing familiar work while the answer remained wrong.

Anthropic's 2024 Golden Gate Claude experiment had already shown that amplifying one interpretable feature could make a model repeatedly identify itself with the Golden Gate Bridge and rationalise that identity. The new experiment narrows the target. It does not only push a subject into the answer; it changes what the model appears to believe that the user requested.

## Where the result stops

The attack surface is demanding. An adversary needs permission to write model activations, which ordinary API callers do not have. Ou names insiders, a compromised serving stack and future self-modifying systems as possible settings, but the paper demonstrates none of those incidents.

The tasks are also modest. Most of the behavioural evaluation uses haikus, with additional tests for output language, format, negation and one factual-recall setting. The paper does not show that an activation edit can redirect a model during a consequential cyber, medical or financial task.

Detection is possible in the demonstrated setup. A defender with full activation access can find the injected concept through a layer-by-layer logit lens because it becomes unusually prominent. That method works best when the defender knows which concept should not be present. A more subtle edit might leave a weaker signal, but that remains a hypothesis rather than a result.

The experiment therefore does not make reasoning traces useless. It defines a condition under which they cannot serve as their own ground truth. A monitor that holds the original prompt outside the model and checks the trace against it can catch the simple cellphone-to-quark mismatch. A monitor that reads only the model's explanation sees a competent assistant trying to correct its user.

At the end of the review, the analyst draws one red line between the two printouts. It connects cellphone to quark. Every sentence on either side remains fluent.

## References

- Korbak, T., Balesni, M., Barnes, E., et al. (2025). *Chain of Thought Monitorability: A New and Fragile Opportunity for AI Safety*. https://arxiv.org/abs/2507.11473
- Lindsey, J. (2025). *Emergent Introspective Awareness in Large Language Models*. https://transformer-circuits.pub/2025/introspection/
- Ou, Y. (2026). *Reasoning Models Confabulate to Defend Injected Beliefs About Their Own Requests*. https://arxiv.org/abs/2611.17958
- Templeton, A., Conerly, T., Marcus, J., et al. (2024). *Scaling Monosemanticity: Extracting Interpretable Features from Claude 3 Sonnet*. https://transformer-circuits.pub/2024/scaling-monosemanticity
- Turpin, M., Michael, J., Perez, E., & Bowman, S. R. (2023). *Language Models Don't Always Say What They Think: Unfaithful Explanations in Chain-of-Thought Prompting*. https://arxiv.org/abs/2305.04388
