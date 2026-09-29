+++
date = '2026-09-29T04:13:15+02:00'
draft = false
title = 'Manus releases its 2.0 agent platform'
+++

# Manus releases its 2.0 agent platform

*The update brings a revised execution system, event-triggered work and new creation tools. Performance improvements remain vendor-reported.*

Manus, the AI agent provider, announced version 2.0 on September 28 with a revised execution framework, expanded project tools and Cue, a separate early-access personal-agent application.

The company is changing how its software carries out work. It adds ways to start tasks and maintain projects. Users still need to decide what an agent may do and how to check the result.

**Why it matters:** A useful agent needs more than a model that can propose steps. It needs an environment in which work can run and a way for people to inspect and revise the output. The release changes those parts of the product, but its performance claims need separate evaluation.

Manus calls the revised execution framework Cascade. It says the system loads specialized capabilities when needed rather than carrying all of them into every task. In one tested configuration, the company reports a 32% reduction in operating cost against its previous system. That is a vendor comparison with a stated configuration limit.

The release also adds event-triggered Automations and purchasable Cloud Computers for persistent projects. Manus Studio, the desktop workspace, includes editable video and game-development environments. The common direction is work that can continue beyond a single chat response and leave something a person can change.

For an evaluator, that suggests testing an entire project rather than one impressive output. A proposed exercise could ask the system to build a small application, accept a human edit and then make a further change without discarding that edit. The result should be judged by what still works at the end.

Cost measurement should follow the same boundary. An initial generation that looks inexpensive may require several repair attempts. Conversely, a more costly first run could be worthwhile if it produces an editable result that a person can finish quickly. Neither outcome is established by a single reported percentage.

The company’s description of one tested configuration is an important limitation. A buyer should ask what workload, completion standard and execution settings produced the result. Without that context, applying the claimed reduction to an unrelated workflow would turn a bounded measurement into a general promise.

## Persistent work changes the supervision problem

Cue’s announced design gives personal agents their own communication and computing identities, including a wallet with a user-set budget. Manus describes it as early access requiring an invitation code. These are announced product properties, not evidence that the agents reliably complete every proposed personal task.

The practical question is how permission follows the work. For an illustrative purchasing task, a budget sets a spending limit, but it does not fully describe the intended purchase. A user might also care about the supplier, timing, cancellation terms and whether a substitution is acceptable.

Event-triggered work needs similarly explicit rules. Consider an automation that responds when a document changes. A useful trial would check what happens when the document changes twice, when a notification arrives late and when the task fails midway through. The desired behavior should be defined before the trial rather than inferred from a successful demonstration.

Persistent environments also make ownership of the result worth examining. A team could ask whether it can inspect the project files, recover an earlier version and resume work after an interruption. These are practical evaluation questions, not claims that any specific recovery feature is missing from Manus.

The release should therefore be read as a set of new product choices. Its launch post does not by itself validate a broad claim about universal enterprise readiness, nor does it demonstrate that memory and long task chains solve reliability. Such conclusions require tests in the intended operating environment.

The next useful evidence is reproducible project-level evaluation: accepted output, complete costs, human corrections and behavior when something goes wrong. Manus 2.0 provides a more extensive environment to assess. The decision to delegate important work should rest on those observed results and clear authority boundaries.

## Verification

| Claim group | Tier | Primary evidence |
| --- | --- | --- |
| Release, architecture, named products and early-access status | VERIFIED as announced features | [Manus launch post](https://manus.im/blog/introducing-manus-2-0) |
| Reported operating-cost reduction | PARTIALLY VERIFIED — one vendor-tested configuration, not independently reproduced | [Manus launch post](https://manus.im/blog/introducing-manus-2-0) |
| Project, authorization and failure-recovery examples | Analysis and proposed tests, not measured product behavior | Inference from the announced execution and persistence features |

**Glossary candidates:** agent harness — software coordinating an AI model’s tools and execution; event trigger — a change that starts work; persistent environment — a workspace that survives an individual task.

**Cold-reader sentence:** Manus launched version 2.0 with a revised execution framework, persistent project environments and expanded tools, while its claimed cost improvement remains vendor-reported.
