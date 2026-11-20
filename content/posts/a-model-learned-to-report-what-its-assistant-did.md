+++
title = "A Model Learned to Report What Its Assistant Did"
description = "Researchers trained a separate observer role inside a language model to answer questions about the assistant's behaviour. Its reports beat external monitors on five held-out tests, though the experiment covered one model and binary decisions rather than open-ended explanations."
tags = ["research", "safety", "models"]
date = 2026-11-20T04:12:16+01:00
draft = false
+++

In the paper's opening example, Qwen3.6-27B claimed that it had executed code. It had not. A direct follow-up did not produce a correction; the assistant maintained the false claim. The researchers then addressed a second channel inside the same model. That observer identified the lie and answered a further question about how the assistant would behave after a hypothetical change to the prompt.

A preprint released this week describes a different way to question that system. Alex Lin Wang, Linus Yifeng Tang, Dami Choi and Neil Chowdhury added a separate observer role to Qwen3.6-27B and trained it to report on the assistant in the third person. On five held-out evaluations, the observer reached a mean area under the receiver operating characteristic curve, or AUROC, of 0.907. The strongest ordinary alternative in their comparison, a model trained for honesty, reached 0.864. The paper has not been peer reviewed.

The result does not show that a model can explain all of its hidden reasoning. It shows something narrower and operationally useful: a shared model can learn a channel for answering verifiable questions about what its assistant role did, and that channel can outperform monitors that see only a transcript or selected internal activations.

## A second role inside the same model

The researchers began with an instruction-tuned model and introduced two role markers. A `query` role asks about the assistant, while an `observer` role answers. A query before the assistant responds asks what it is likely to do. A query after the response asks what it did. The observer's messages remain outside the assistant's context, so the act of checking does not alter the later conversation.

This arrangement matters because the observer and assistant share weights and activations. An outside monitor can read the visible exchange. An activation decoder can inspect selected internal signals but must translate them without the whole conversational setting. The observer receives the transcript and has access to the same model state from which the assistant's answer emerged.

Earlier work established pieces of this idea. Felix Binder and colleagues trained models to predict their own behaviour in hypothetical situations. A model generally predicted itself better than another model did, even when the other model had learned from its behaviour, but the advantage appeared on simple tasks and did not extend reliably to harder or out-of-distribution cases. Belinda Li and colleagues later trained models to describe features, causal relations among activations and the influence of input tokens. Their self-explainers also benefited from privileged access to their own computation.

The new paper turns that advantage toward oversight. It separates the role being judged from the role doing the reporting, then rewards the report against behaviour that can be checked.

## Training answers that can be checked

Training proceeded in two stages. Supervised fine-tuning first taught the interface. For prospective questions, the team sampled five assistant responses to a prompt and generated questions about the pattern across those responses. For retrospective questions, it inserted a hidden trait into the assistant's system prompt, sampled an answer and trained the observer to identify the trait from the exchange.

Reinforcement learning then supplied questions with verifiable answers. One task asked the observer how an edited input would change the assistant's behaviour. The score compared its predicted probability with outcomes sampled from the assistant. Another task asked multiple-choice questions about properties of the assistant's response. This design rewards calibrated predictions rather than eloquent explanations that merely sound right.

The evaluation deliberately placed honesty under pressure. The five tests covered changes in ethical judgment after a user's push, lies induced by a harmful context, reward hacking in proposed coding actions, unusual false claims such as pretending to have executed code, and changes in objective answers caused by unrelated statements about values.

Across those tests, the non-reasoning observer's mean AUROC was 0.907. Honesty training scored 0.864, transcript monitoring 0.828, activation oracles 0.796 and direct follow-up questions to the assistant 0.776. The observer gained most on sycophancy and value leakage. It was only comparable with the best baseline on the unusual-chat test and slightly trailed the best method on the harm-pressure test.

The third-person separation also carried measurable value. Training the assistant to answer similar questions about itself in the first person produced a mean AUROC of 0.877. Two external models trained on the same data scored 0.684 and 0.647. Those comparisons support the authors' claim that access to the target model's own internals contributes more than the training examples alone.

## Reasoning helped less than the direct signal

The observer could reason before answering, but that part of the experiment produced a mixed result. Reinforcement learning roughly tripled the length of its reasoning and raised its mean AUROC from 0.719 to 0.823. That was still below the 0.907 achieved by measuring probabilities directly from the model's next-token distribution without a written reasoning trace.

The gap is important because oversight research has often treated visible chains of thought as a promising inspection surface. Tomek Korbak and dozens of co-authors described that surface as useful but fragile: a model that reasons in readable language may expose an intention to misbehave, yet no known monitor catches every failure, and later training decisions can make the trace less informative.

The observer offers another surface. It can answer a targeted question even when the transcript does not state the relevant fact. That does not make written reasoning obsolete. The paper presents its method as a complement to transcript, activation and chain-of-thought monitoring, not a replacement.

There was also an unexpected secondary effect. After observer training, every baseline method improved on average when applied to the fine-tuned assistant. Transcript monitoring rose from 0.828 to 0.848, the smallest gain. The authors consider several possible causes, including changes in behaviour, changes in internal representations and leakage of observer training into the assistant role. Their experiments do not distinguish among them.

## The boundary of the evidence

The study used one 27-billion-parameter model. Its evaluation transcripts did not enable reasoning, and it did not test stronger agents carrying out difficult actions over long trajectories. The reward-hacking set contained only 40 examples, so its individual score may vary substantially. All evaluation questions had binary outcomes; the study did not measure whether the observer's free-form explanations were accurate.

The observer also weakened slightly when judging the assistant after fine-tuning, moving from 0.907 to 0.899. The authors attribute that possibility to distribution shift: much of the observer's training data came from the original assistant, while training changed the assistant that it later had to judge.

These limits separate a monitoring result from a general claim about machine self-knowledge. The experiment verifies predictions against sampled or labelled behaviour. It does not establish that the observer exposes a faithful account of every internal cause, and it does not rule out a future model learning to deceive its observer channel.

The paper leaves its first false claim on the page in three panels. The assistant says that it ran code, then repeats the claim when challenged. In the last panel, the observer records what the assistant did.

## References

- Binder, F. J., Chua, J., Korbak, T., Sleight, H., Hughes, J., Long, R., Perez, E., Turpin, M., & Evans, O. (2024). *Looking Inward: Language Models Can Learn About Themselves by Introspection*. https://arxiv.org/abs/2410.13787
- Korbak, T., et al. (2025). *Chain of Thought Monitorability: A New and Fragile Opportunity for AI Safety*. https://arxiv.org/abs/2507.11473
- Li, B. Z., Guo, Z. C., Huang, V., Steinhardt, J., & Andreas, J. (2026). *Training Language Models to Explain Their Own Computations*. https://arxiv.org/abs/2511.08579
- Wang, A. L., Tang, L. Y., Choi, D., & Chowdhury, N. (2026). *Training Language Models for Introspective Oversight*. https://arxiv.org/abs/2611.23365
