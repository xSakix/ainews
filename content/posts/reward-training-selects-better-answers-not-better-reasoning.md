+++
title = "Reward training selects better answers, not better reasoning"
description = "A new study followed every checkpoint in a small model's reinforcement training. Accuracy improved, but the model did not develop a sharper internal representation of reasoning errors; it became better at selecting solutions that it already knew."
tags = ["research", "models"]
date = 2026-11-08T04:18:00+01:00
draft = false
+++

Picture a student who can solve a mathematics problem one time in two. A tutor rewards every correct answer and says nothing about the steps. After weeks of practice, the student answers correctly more often. The tempting conclusion is that the student learned better mathematics. In this imagined classroom, however, a closer test finds the same catalogue of good and bad approaches as before. The student has become better at choosing from it.

## Following the whole training run

That distinction drives *RLVR Sharpens the Pencil, Not the Mind*, a new preprint by Shreeyam Bangera and Manya Gupta. The researchers follow OLMo-2-1B through 13 checkpoints of reinforcement learning with verifiable rewards, or RLVR. Instead of comparing only the model before and after training, they inspect what changes along the way.

RLVR became prominent because a correct answer to a mathematics or coding problem can be checked automatically. A training system samples solutions, assigns rewards and raises the probability of behaviour that earned them. DeepSeek-R1 showed how far this approach could go: its R1-Zero model developed stronger mathematical and coding performance through reinforcement learning without a preliminary supervised fine-tuning stage.

The visible performance gains created a harder question. Does reward training teach a model new reasoning skills, or does it make existing skills easier to reach? The second explanation is known as sharpening. A pretrained model may already contain a good solution path, but assign it too little probability to use on the first attempt.

Bangera and Gupta use the openness of OLMo to test that claim across the training trajectory. Ai2 publishes intermediate checkpoints from the one-billion-parameter model's RLVR run. The authors evaluate those checkpoints on GSM8K, a dataset of 8,500 grade-school word problems introduced by Karl Cobbe and colleagues.

## More reliable access to old solutions

First-attempt accuracy rises from 58.0% at the start of the run to 61.3% at the end. The increase is real but modest. The more revealing measurement comes from asking the model the same problem 256 times and checking whether any sample contains a correct solution. That solution coverage starts at 94.5% and ends at 96.9%.

The base model could therefore produce a valid answer for almost every problem before RLVR. Training made those valid paths more likely to appear on the first attempt. It did not open a large new region of problems that the model could solve only afterwards.

Solution coverage cannot reveal what the model represents internally. A model might already sample the right answer occasionally and still learn a better concept of reasoning during training. The researchers test this possibility by inserting three kinds of mistake into problem-solving traces. They then train linear probes on model activations to identify the errors.

Probe performance stays between 0.798 and 0.840 AUROC across all 13 checkpoints. The variation is smaller than the confidence interval. On this test, the model does not become better at internally distinguishing sound reasoning from a planted mistake.

One internal signal does change clearly. A probe can distinguish early from late checkpoints with 0.93 AUROC at the final-answer token. Applied to tokens in the reasoning steps, the same probe performs near chance. Training appears to reorganise the decision at the end of the solution more than the representations used while constructing it.

## What the result does and does not show

The paper's title draws a sharp line, but its experiment is narrow. It studies one one-billion-parameter model family, one mathematics benchmark and one RLVR run. Linear probes can miss information that exists in a form they cannot decode. GSM8K rewards a short final answer and does not represent the open-ended tasks for which correctness is difficult to verify.

The authors also do not show that RLVR never creates new reasoning skills. Their evidence supports a more limited claim: in this training run, the observed gain is better explained by improved selection of existing solution paths than by a sharper internal representation of the tested errors.

That qualification matters because RLVR is often described through its outward behaviour. A model produces longer chains, tries alternative approaches and reaches more correct answers. Those changes can look like new understanding. The checkpoint analysis shows that an output can improve even when a probe of the reasoning process stays almost still.

The finding also clarifies why sampling remains useful after reinforcement training. If a model's knowledge covers more solutions than its first answer reveals, then repeated attempts expose capability that a single pass misses. RLVR changes the probability distribution over those attempts. It does not make pass-at-one accuracy a complete measure of what the model knows.

## Training for the process

Verifiable final answers are attractive because they are cheap and objective. A number is either correct or it is not. A program passes its tests or fails them. The reward does not need to say which reasoning step helped, which shortcut will fail elsewhere or whether the model recognised its own mistake.

Training a better error representation would require a signal closer to the process. That could mean verified intermediate steps, adversarially planted mistakes, process supervision or tasks that reward calibrated self-correction. Each option costs more than checking a final answer, and each introduces its own judgment problem.

The paper does not prescribe one of these methods. It supplies a diagnostic that future work can reuse: preserve intermediate checkpoints, measure solution coverage rather than only first attempts, and probe the tokens where reasoning occurs separately from the token that commits to an answer. A before-and-after score loses the path that explains the gain.

This lesson reaches beyond mathematics. Agents receive rewards for completed tickets, passing tests or successful tool calls. If training mainly improves selection among existing behaviours, the agent may look more capable without becoming better at recognising a flawed plan. Evaluation then needs both outcomes and process-level failure tests.

Return to the invented student after another week. The correct answers arrive faster now, and the tutor's chart rises. Before moving to harder material, the tutor places one plausible mistake in a worked solution and asks the student to find it. The pause that follows measures something the reward chart did not.

## References

- Ai2. (2025). *OLMo-2-0425-1B-SFT model card*. https://huggingface.co/allenai/OLMo-2-0425-1B-SFT
- Bangera, S., & Gupta, M. (2026). *RLVR Sharpens the Pencil, Not the Mind*. https://arxiv.org/abs/2611.02574
- Cobbe, K., Kosaraju, V., Bavarian, M., et al. (2021). *Training Verifiers to Solve Math Word Problems*. https://arxiv.org/abs/2110.14168
- DeepSeek-AI. (2025). *DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning*. https://arxiv.org/abs/2501.12948
