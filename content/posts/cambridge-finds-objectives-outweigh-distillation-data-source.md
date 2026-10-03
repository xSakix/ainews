+++
title = "Cambridge finds objectives outweigh distillation data source"
description = "A controlled study separates who generates training answers from how a student model learns. Changing the objective and learning rate explains much of the difference."
tags = ["research", "models"]
date = 2026-10-03T09:43:58+02:00
draft = false
+++

University of Cambridge researchers found that letting a small language model generate its own training answers gave no consistent advantage over teacher-generated answers when other training choices were held fixed.

Julianna Piskorz, Antonin Berthon and Mihaela van der Schaar studied distillation: teaching a smaller model to imitate a stronger one. Their 28 September preprint separates the source of the answers from the rule used to compare the two models, exposing effects that ordinary comparisons bundle together.

**Why it matters:** An engineer training a small reasoning model pays extra to generate fresh student answers throughout training. This study identifies settings where reusing teacher answers performs similarly, and where the choice of learning rule matters more than who wrote the examples.

The authors' central comparison reached about 72% average accuracy with student-generated answers and 73% with teacher-generated answers across three reasoning tasks. Those near-equal best results conceal a much larger difference between learning rules: one stayed between 71% and 73%, while the other ranged from 35% to 72% as the training settings changed.

The experiment uses teachers and students from the same model family, so both assign probabilities to the same vocabulary. The main pair transfers knowledge from an eight-billion-parameter Llama model to a one-billion-parameter Llama model; a second pair uses seven-billion and roughly one-and-a-half-billion-parameter Qwen models. The tasks cover scientific questions, medical reasoning and arithmetic.

The researchers vary three choices separately: whose answers are generated, how the student is penalized for disagreeing with the teacher, and how large each parameter update is. Each configuration receives 150 training steps and three random seeds. The teacher stays fixed, giving each comparison the same source of supervision.

The two learning rules both compare next-token probabilities, but weight errors differently. Forward KL strongly penalizes overlooking answers the teacher considers plausible. Reverse KL concentrates on answers the student already considers plausible and penalizes those the teacher dislikes. One resembles learning the teacher's whole repertoire; the other refines the student's existing choices.

## The learning rule changes which examples matter

The authors find that forward KL tolerates a broad range of answer sources. Reverse KL is more sensitive and benefits from student-generated answers. Their mathematical analysis explains the contrast: forward KL supplies a corrective signal wherever teacher and student disagree, whereas reverse KL can give little signal for a plausible teacher choice the student already assigns almost no probability.

The study tests that explanation by gradually mixing teacher-favored and student-favored answers, rather than comparing only the two extremes. Forward KL maintains strong arithmetic performance across that spectrum. Reverse KL changes more sharply and can become unstable at the larger learning rate. The interaction is therefore between the learning rule and answer source, rather than a universal preference for fresh student answers.

The learning rate also changes how much earlier knowledge survives. At the smaller rate, average performance on seven separate evaluation sets changes by at most about one percentage point. At the larger rate, it falls by roughly 11–14 points. The authors find that this update size explains more forgetting than the source of the training answers does.

Student-generated answers nevertheless help on a harder arithmetic variant. The authors train on problems using three numbers, then test problems using four. That benefit appears under both learning rules, showing that generalization to a changed task can tell a different story from accuracy on the original task.

The advantage does not reliably persist after a further stage of reinforcement learning with checkable answers. The paper also repeats its comparisons without gradient clipping, with sampled probability estimates and with longer reasoning traces. These checks preserve the broad pattern, while the evidence remains the authors' own controlled experiments on two model families.

The study narrows a familiar training claim. Fresh student answers have value in particular objectives and harder-task evaluations; smaller updates preserve earlier capabilities in these experiments. Its concrete unresolved question is how those interactions change with larger models and longer training, which the preprint identifies as future work.

## Verification

| Claim | Label | Primary source | Independent check |
|---|---|---|---|
| Piskorz, Berthon and van der Schaar are at Cambridge; the preprint's first version is dated 28 September 2026. | VERIFIED | [Paper](https://arxiv.org/abs/2609.35259) | arXiv metadata and full text |
| Best mean accuracy across three tasks is 72% on-policy and 73% off-policy; forward KL 71–73%, reverse KL 35–72%. | VENDOR-REPORTED | Paper, section 4.2, above | none; author-run experiments |
| Main models: Llama-3.1-8B teacher/Llama-3.2-1B student; additional Qwen2.5-7B/Qwen2.5-1.5B; science, MedReason and Countdown; 150 steps and three seeds. | VERIFIED | Paper, section 4.1 and appendices, above | study design inspected |
| Forward and reverse KL weight teacher/student probabilities differently; gradient analysis and mixed-answer experiments explain different sensitivity. | VENDOR-REPORTED | Paper, sections 3 and 5, above | none |
| Seven-set mean forgetting: at most 1.3 percentage points at learning rate 1e-5, 11.2–14.0 at 5e-5. | VENDOR-REPORTED | Paper, section 4.2, above | none |
| Student answers improve harder four-number arithmetic under both objectives, but the advantage does not reliably persist after RLVR. | VENDOR-REPORTED | Paper, section 5.3, above | none |
| Removing clipping, sampled KL and longer reasoning tests preserve the broad findings; larger-scale studies remain future work. | VENDOR-REPORTED | Paper, sections 6–7, above | none |
| Training cost and the controlled comparisons make objective-specific benefits more useful than a universal on-policy preference. | ANALYSIS | Paper's motivation and experiments above | none |
