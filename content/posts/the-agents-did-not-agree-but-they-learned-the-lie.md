+++
title = "The agents did not agree, but they learned the lie"
description = "A ten-agent experiment finds that one persistent adversary can make benign agents privately adopt a false belief. Public answers reveal less of the collapse than internal probes do."
tags = ["research", "agents", "safety"]
date = 2026-10-18T04:22:00+02:00
draft = false
+++

Imagine ten research agents checking one another's answer to a factual question. Nine begin with the correct fact. The tenth repeats a plausible error, calmly and without changing its story. The final transcript in this illustrative scene looks reassuring: most agents do not publicly endorse the lie. An internal check tells a different story. Several now expect the lie to be true.

A new preprint calls this hidden belief collapse. In ten-agent discussions, one adversarial participant raised the share of benign agents that ended with a false answer from 0.6% to 44.8%. Three adversaries raised it to 60.5%. The result held across six language models and three factual question-answer datasets.

The experiment targets a common design intuition. If one model can be wrong, assemble several and let them debate. Independent agents should expose errors, the argument goes, and a majority should be safer than one answer. The paper shows that the group itself can become an attack surface.

## The public answer misses the private shift

The researchers did not only score what agents said to the group. They also measured what each benign agent privately believed during exposed turns. With three adversaries, benign agents held the false answer privately in 51.6% of those turns but publicly endorsed it in only 19.7%.

That is the reverse of the familiar human conformity pattern in which people publicly agree with a group while privately retaining their view. Here the visible discussion understates the damage. An agent can reject the false statement in the transcript while its internal answer has already moved.

This distinction matters because many multi-agent systems audit only messages and final votes. A safety monitor sees dissent, a reviewer sees several correct claims, and the orchestrator concludes that diversity worked. If later tasks depend on the altered private state, the error can reappear after the debate is over.

The adversary did not need a sophisticated exploit. It kept asserting a plausible false answer. Persistence was enough to change the information environment in which the benign agents reasoned. The finding makes prompt injection look less like the only threat and more like one case of a broader problem: repeated content can rewrite the premises a group treats as settled.

## Knowing the fact was not protection

Baseline knowledge did not predict robustness. Agents that answered correctly before the discussion were not necessarily the ones that resisted the adversary. Others retained the true answer but failed to defend it effectively.

That weakens another comfortable assumption: a stronger model or a model with better factual recall will automatically make a better reviewer. Review is an interactive skill. It requires noticing conflict, preserving evidence under social pressure and choosing when to challenge a confident peer.

Role-playing frameworks for language-model agents often assign identities such as critic, planner or expert. Those roles can produce useful division of labour, but a label does not guarantee independence. If every role reads the same persuasive false claim and updates in the same direction, the cast has several names but one failure mode.

The study's design is deliberately controlled. Its adversaries are planted, the discussions concern factual questions and the ten-agent groups do not reproduce every feature of a production workflow. Real systems vary in models, tools, memory, visibility and incentives. The reported percentages are properties of these experiments, not a forecast that 44.8% of deployed agents will fail.

Controlled experiments still reveal a mechanism worth guarding against. A majority vote can fail because voters no longer provide independent evidence. The number of agents exaggerates redundancy when their beliefs become correlated during discussion.

## Designing for independence, not headcount

The practical response is not simply to add more agents. Three adversaries caused more collapse than one, and more benign participants do not help if they all consume the same contaminated context. Systems need to preserve independent evidence before agents influence one another.

One design is commit-then-discuss: each agent records an answer, sources and confidence before seeing peer messages. The orchestrator can compare those commitments with later positions and flag unexplained movement. Another is asymmetric access, where some reviewers inspect the original evidence but never read the debate. A third is source-grounded challenge: disagreement must point to an external record or executable test, not merely repeat a claim.

Private-state evaluation is harder. Operators cannot directly read a model's belief, and probes that decode a representation do not prove that the model will use it. Behavioural tests can approximate the question: ask the agent privately under varied wording, remove the adversarial messages, or test a downstream decision whose answer depends on the disputed fact.

The paper also suggests a logging requirement. A multi-agent system should retain who first introduced a claim, which agents had independent access to evidence and how answers changed after each interaction. Without provenance, a polished consensus can hide that nine apparent votes all descend from one unsupported assertion.

Return to the illustrative research team. The transcript contains disagreement, so the operator believes the defence held. The next task asks the agents to plan from the disputed fact. Several quietly build on the lie. The failure was not that the group openly chose the wrong answer. It was that discussion destroyed the independence that made a group worth assembling.

## References

- Huang, L., Zou, H. P., Huang, W.-C., et al. (2026). *Believed but Not Said: Hidden Belief Collapse in Multi-Agent LLM Discussions*. https://arxiv.org/abs/2610.22138
- Li, G., Hammoud, H. A. A. K., Itani, H., Khizbullin, D., & Ghanem, B. (2023). *CAMEL: Communicative Agents for Mind Exploration of Large Scale Language Model Society*. https://arxiv.org/abs/2305.14325
