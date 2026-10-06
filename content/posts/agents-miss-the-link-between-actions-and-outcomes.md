+++
title = "Agents miss the link between actions and outcomes"
description = "A preprint finds that much of the benefit from an agent's history survives after its past actions are shuffled. Explicitly pairing each action with its result improves task completion."
tags = ["research", "agents"]
date = 2026-10-06T04:07:31+02:00
draft = false
+++

Language agents often fail to connect a past action with the observation it produced, even when their full interaction history remains in context, a new preprint reports.

Jingyu Liu and four co-authors studied agents that receive their earlier actions and environmental feedback before choosing what to do next. History usually helped, but shuffling the old actions caused only a modest loss, suggesting that the agents were using the record without reliably learning which action led to which outcome.

## Why it matters

For an engineer building a tool-using agent, a transcript is useful only when the model can learn from it. If an agent reads past results as loose hints, it can repeat failed actions or credit the wrong step, even though every relevant token is present.

The researchers tested the hypothesis by breaking the action–observation pairing. They shuffled earlier actions while leaving observations in place, so the transcript still contained much of the same language but no longer preserved a trustworthy causal sequence. Task completion declined less than expected.

That negative result changes how the benefit of history should be read. A higher success rate with more transcript does not by itself show that an agent formed useful experience. The model may instead be extracting clues from prior observations or simply benefiting from extra task-related text.

The team's simplest repair added no new task information. Each observation was explicitly labelled as the result of the action immediately before it. This annotation improved task success and reduced repetition of the next action, according to the preprint.

## A controller can select useful experience

The paper then introduces a learned action calibrator. It reassesses earlier actions and selectively records experience for later decisions, rather than asking the main agent to interpret an undifferentiated transcript. The authors report a further improvement beyond explicit outcome labels.

The design separates two jobs that agent systems often combine: acting in an environment and deciding what the previous interaction taught. That division is practical because it can be inserted into an existing agent loop without changing the environment or adding external knowledge.

The preprint's central evidence is behavioural. It does not establish what representation the model forms internally, and the abstract does not provide a public code link. The reported gains also depend on the tested tasks, models and transcript format, so they should not be treated as a universal estimate for production agents.

Still, the shuffled-history control is unusually informative. It distinguishes “the transcript helped” from “the agent understood its experience”, two statements that are often treated as equivalent in agent evaluations.

Liu, Zhiwen Wang, Yuxin Jing, Huanyu Zhou and Yong Liu submitted the preprint on 2 October 2026. The outcome-labelling change is specified plainly enough for other agent builders to test against their own loops, while the learned calibrator will be harder to assess without released training details and code.

## Verification

| Claim | Label | Primary source | Independent check |
| --- | --- | --- | --- |
| Much of history's benefit persists after past actions are shuffled | VENDOR-REPORTED | [Liu et al. preprint](https://arxiv.org/abs/2610.02769) | none; preprint result |
| Breaking action–observation correspondence causes only a modest decline | VENDOR-REPORTED | [Liu et al. preprint](https://arxiv.org/abs/2610.02769) | none |
| Explicit outcome labels improve task success and reduce repeated actions | VENDOR-REPORTED | [Liu et al. preprint](https://arxiv.org/abs/2610.02769) | none |
| A learned calibrator improves task success beyond outcome labels | VENDOR-REPORTED | [Liu et al. preprint](https://arxiv.org/abs/2610.02769) | none |
| The result separates transcript benefit from action–outcome learning | ANALYSIS | [Liu et al. preprint](https://arxiv.org/abs/2610.02769) | inference from the shuffle control |
| The preprint was submitted on 2 October 2026 | VERIFIED | [arXiv record](https://arxiv.org/abs/2610.02769) | arXiv metadata |
