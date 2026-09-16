+++
date = '2026-09-16T07:47:00+02:00'
draft = false
title = 'Researchers redirect RL toward harder problems'
+++

After reading this, the reader knows standard RL may favor easier examples, and it matters because average gains can hide failure on hard problems.

# Researchers redirect RL toward harder problems

*Never Give Up keeps sampling a problem until it finds a correct answer, shifting reinforcement-learning compute away from examples the model already solves.*

Researchers led by Michael Noukhovitch published a technical explainer on September 15 for Never Give Up, an adaptive sampling method designed to make reinforcement learning spend more effort on difficult language-model tasks.

In plain terms, ordinary training can repeatedly reward a model for improving answers it already gets partly right. The hardest examples may generate no successful attempt and therefore little useful learning signal. Never Give Up, or NGU, keeps trying those examples until it obtains a correct sample.

## Why it matters

An average benchmark score can rise while the capability a developer cares about remains unchanged. In the researchers' math experiment, reinforcement learning improved easier and medium examples much more than questions the starting model could not solve in 32 attempts.

The authors call this uneven improvement the Matthew Effect: examples that already produce some success receive more useful reinforcement, while zero-success examples remain starved of signal. The term describes a training dynamic, not a claim that every hard problem can be solved by sampling longer.

NGU changes allocation rather than inventing a new reward. It draws fewer samples once an easy problem yields a correct answer and continues generating on harder problems. An asynchronous training system allows workers to finish at different times without forcing every problem to use the same sample budget.

The paper reports improved performance per unit of compute on Deepscaler, a math benchmark. On Manufactoria, a coding task with tests of varying difficulty, the authors report that standard GRPO failed to solve full problems while NGU progressed toward harder tests.

## Harder sampling has costs

The method depends on recognizing a correct result. That makes it best suited to domains such as mathematics and code where a verifier can cheaply test an answer. Tasks judged by human preference or ambiguous real-world outcomes do not provide the same clean stopping rule.

Repeated sampling can also chase impossible, mislabeled or out-of-distribution examples. A production system needs limits so one problem cannot consume unbounded compute. The paper examines off-policy learning because slow, difficult samples may arrive after the model has already changed.

The evidence is promising but bounded. The authors evaluated selected math and coding settings, and the paper was posted to arXiv without peer-review status stated on its page. Independent reproduction across models, reward systems and larger training runs will determine whether the allocation rule generalizes.

The practical lesson is immediate even before NGU is adopted: aggregate evaluation should be split by initial difficulty. If gains come mostly from tasks the base model already solved sometimes, a higher average may exaggerate progress on genuinely new reasoning.

## Verification

1. **VERIFIED — The authors published the NGU explainer on September 15, 2026; the paper was submitted to arXiv on September 11.** Primary sources: https://mnoukhov.github.io/posts/ngu/ and https://arxiv.org/abs/2609.13443
2. **VERIFIED — The paper defines a Matthew Effect in which RL improves easy problems more than initially unsolved hard problems.** Primary source: https://arxiv.org/abs/2609.13443
3. **VERIFIED — NGU samples a problem until it obtains a correct answer and uses asynchronous RL to vary compute allocation.** Primary source: https://arxiv.org/abs/2609.13443
4. **PARTIALLY VERIFIED — NGU improves performance per compute on Deepscaler and solves harder Manufactoria tests.** These are author-reported experiments awaiting independent replication. Primary source: https://arxiv.org/abs/2609.13443
5. **VERIFIED — The method requires a correctness signal for its stopping rule.** This follows from the published sampling mechanism. Primary source: https://arxiv.org/abs/2609.13443
6. **UNVERIFIED — NGU will generalize to larger models and non-verifiable tasks.** The published evidence does not establish that broader claim.

## Glossary candidates

- Reinforcement learning
- Adaptive sampling
- Matthew Effect
- GRPO
- Verifiable reward
- Asynchronous training

**Cold-reader sentence:** Never Give Up reallocates reinforcement-learning samples toward initially unsolved problems so average gains do not come mainly from already-easy examples.
