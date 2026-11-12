+++
title = "Models Know Time but Misjudge Their Own Runtime"
description = "Language models answered up to 97.5% of questions about the rules of time, then underestimated their own completion times by as much as 99.5%. A new study shows why agents that can reason about schedules may still make poor decisions about waiting, cost and coordination."
tags = ["research", "agents", "models"]
date = 2026-11-12T04:18:00+01:00
draft = false
+++

Imagine an engineer who asks an agent to investigate a failed service and report how long the work will take. The agent reads the logs, lists the steps and promises an answer in ten minutes. It finishes in seconds. Later, the same agent is offered a slightly more accurate tool that requires a longer wait. It rejects the tool because it treats that wait as if it barely existed. This engineer is invented, but the two errors mirror measurements from a new study of how language models handle time.

## Rules without a clock

Ryan Liu and five colleagues at Princeton, Columbia, UC Berkeley and UCLA tested temporal competence as a chain with four links: knowledge of time, estimates of duration, human-like biases and decisions that trade time against accuracy. Their preprint, submitted on 7 November, examines Claude Opus 5, GPT-5.6 Sol and Gemini 3.7 Flash. It asks whether models can apply what they have read about time to a dimension that they do not directly experience.

That distinction matters because a language model does not sit through the interval between two calls. A timestamp can appear in its context, but the model does not feel minutes pass. Even an autonomous system usually wakes on an external schedule or event. The researchers describe time as second-hand information for a model: present in text and metadata, absent as continuous experience.

The first experiment gave the models a fair chance to show what they knew. The team drew five axioms from research on learning, skill decay, task switching, fatigue and recovery. From those axioms, it derived principles such as the cost of interruptions and the advantage of batching related work. The test used work vignettes rather than trivia. A model had to judge whether a changed sequence would make a task longer or shorter.

The results were strong. Claude scored 92.0% across the axioms and derived theorems, GPT scored 97.5%, and Gemini scored 96.3%. Their answers also remained coherent when the researchers reversed the comparisons. The errors were usually stable beliefs rather than random guesses.

This part extends a long line of work on formal temporal reasoning. James Allen's 1983 interval framework gave artificial intelligence a way to represent relations such as one event occurring before, during or after another. The new study asks a different question. A model can know these relations and still lack a reliable magnitude for how long its own work takes.

## Estimates detached from execution

For the second experiment, the researchers used software and research tasks from the Human-Calibrated Autonomy Software Tasks benchmark. HCAST contains human baselines collected from skilled workers under conditions that can be compared with agent runs. Related work by Thomas Kwa and colleagues uses these durations to express agent capability as a task-completion time horizon.

The models saw full task instructions and a description of the actor. They estimated a completion time and supplied uncertainty intervals. The researchers then compared those estimates with recorded durations for humans and agents. A separate test used 500 requests from the WildChat dataset. Each model predicted how long it would take to answer, then answered while the system recorded the actual runtime. Five repetitions per model and request produced 7,500 trials.

The central failure was self-calibration. Models underestimated their own completion times by as much as 99.5%, and they could not reliably identify which tasks would take them longer. The problem was not simply that they used human units for machine work. They also failed at relative ordering, which a scheduling system needs even when the exact number of seconds does not matter.

Human duration estimates were better, but they exposed another weakness. The wording of an event changed the model's judgement of how long it would feel. The models reproduced a known human framing bias and amplified it by as much as 1.3 times.

That result connects model behaviour with the planning fallacy studied by Roger Buehler, Dale Griffin and Michael Ross. People often predict that they will finish sooner than past experience supports, especially when they focus on a plan for the present task instead of comparable outcomes. Models can learn descriptions of that bias from text. The new paper shows that knowing about a bias does not ensure resistance to it.

## Waiting barely counted

The final experiment moved from estimates to decisions. The researchers offered choices that traded a longer wait for greater accuracy. By supplying the duration in some conditions, they could separate a bad estimate from a weak preference for saving time.

Some models treated large changes in delay as almost irrelevant. They could ignore a 1,200-fold increase in wait time when answering a user. This failure persisted even when the duration was stated, so estimation alone could not explain it. The decision policy itself did not value time consistently.

The paper does not claim that all models fail every temporal task. Its first experiment demonstrates the opposite. Nor does it establish one internal cause. The evaluation covers three model families and specific task settings, and the authors describe temporal competence through observable answers rather than a direct measure of subjective experience.

The practical risk is narrower and easier to see. An agent may choose between tools with different latencies, allocate work among other agents, estimate a bill that depends on runtime or tell a person when to return. A system that knows the rule for batching tasks can still misorder its queue. A system that explains the cost of an interruption can still promise an impossible deadline.

Time estimates should therefore be treated as predictions that need external calibration. A host can record actual durations, maintain task-specific distributions and apply deadlines outside the model. It can also expose waiting costs explicitly and test whether a choice changes when those costs grow. These controls resemble the broader lesson from agent safety: put measurable state and enforcement in the system around the model rather than relying on a correct explanation in prose.

Return to the imagined engineer after several weeks. The agent still writes a confident estimate, but the interface places it beside the median runtime from comparable jobs and a wide uncertainty range. The scheduler, not the model, decides when to abort or wait. The invented engineer has not given the agent a sense of time. The system has stopped pretending that fluency about clocks is the same as keeping one.

## References

- Allen, J. F. (1983). *Maintaining Knowledge about Temporal Intervals*. https://doi.org/10.1145/182.358434
- Buehler, R., Griffin, D., & Ross, M. (1994). *Exploring the “Planning Fallacy”: Why People Underestimate Their Task Completion Times*. https://doi.org/10.1037/0022-3514.67.3.366
- Kwa, T., et al. (2025). *Measuring AI Ability to Complete Long Software Tasks*. https://arxiv.org/abs/2503.14499
- Liu, R., Lee, D., Ai, I. S., Abdulhai, M., Dubey, R., & Griffiths, T. L. (2026). *In Search of Lost Time: Temporal Competence in Large Language Models*. https://arxiv.org/abs/2611.10536
- Rein, D., et al. (2025). *HCAST: Human-Calibrated Autonomy Software Tasks*. https://arxiv.org/abs/2503.17354
