+++
date = '2026-09-18T08:31:00+02:00'
draft = false
title = 'Researchers Test Coding-Agent Harnesses'
+++

After reading this, the reader knows when context management, planning and specialized tools improve coding-agent performance.

# Researchers Test Coding-Agent Harnesses

*A 176-setting study finds that harness choices depend on model strength and context budget, with no universally best configuration.*

A new preprint tests how the software around a coding model changes agent performance. Across 176 matched settings on SWE-Bench Verified and Terminal-Bench 2.1, the researchers varied context management, context budgets, planning and tool design for four models.

The central result is conditional rather than a single recipe. Context management matters most when the available context window is tight. Explicit planning helps weaker models complete tasks more accurately, while stronger models use it mainly to reduce cost. Specialized tools benefit models that struggle with shell use, but models already proficient with Bash can perform well with a simpler toolset.

## Why it matters

A coding agent is more than its language model. The harness decides which files enter context, when old observations disappear, what tools the model can call and whether it must state a plan before acting. Two products using the same underlying model can therefore produce different results and costs.

That makes model-only leaderboards incomplete for engineering decisions. A team may pay for a stronger model when better context handling would solve the actual bottleneck, or build an elaborate tool layer that adds latency without improving a model already comfortable in a terminal.

The paper evaluates five context strategies across four budgets. The authors report that context management primarily prevents overflow under constrained budgets. When there is enough room, aggressive intervention offers less value and can introduce extra transformations between the model and its original observations.

Among the tested approaches, rule-based elision followed by model-generated summarization produced the strongest efficiency. Elision removes selected low-value material according to fixed rules; summarization compresses the remaining history into a shorter representation. A more elaborate recoverable-elision design added machinery without a measured accuracy gain.

## Planning changes with model capability

The planning ablations show why a workflow feature should not be treated as universally helpful. For weaker models, requiring a plan acted as an accuracy scaffold. It encouraged task decomposition before edits began. For stronger models, planning mostly reduced cost while leaving accuracy nearly unchanged.

Tool design showed the same dependence. Predefined file and editing tools supported models that were less reliable at composing shell commands. Models with stronger Bash ability could work with a Bash-only interface at lower cost. Adding tools is therefore not automatically an upgrade; every abstraction consumes context and gives the agent another action schema to learn.

For practitioners, the study supports testing the full agent configuration. Useful experiments hold the task set and model constant while varying one harness choice at a time. Teams should record success, token use, tool failures, context overflows and wall-clock time. The best setup may differ between repository repair, terminal administration and greenfield coding.

## Limits of the study

The work is a 43-page preprint and had not undergone peer review at publication. It covers four models, two benchmarks and particular implementations of each strategy. Coding models and vendor interfaces change quickly, so the relative results may not remain stable.

Benchmarks also simplify production work. Real repositories include ambiguous requirements, private dependencies, long-running tests and organizational conventions that do not appear in every benchmark task. The paper gives evidence about mechanisms, not a permanent ranking of commercial agents.

Its durable contribution is the interaction it exposes. Context policy, planning and tools should be chosen for a model's weaknesses and the task's constraints. A harness is part of the system being evaluated, not neutral plumbing around it.

## Verification

- **Tier 0 — VERIFIED:** The preprint was submitted to arXiv on 17 September 2026 and reports 176 matched configurations across four models, SWE-Bench Verified and Terminal-Bench 2.1. Primary source: https://arxiv.org/abs/2609.20804
- **Tier 1 — AUTHOR-REPORTED:** The authors report the strongest context-management benefit under tight budgets, efficient rule-based elision plus summarization, model-dependent planning effects and model-dependent tool benefits. Same primary source.
- **Tier 2 — ANALYSIS:** Recommendations for production evaluation and telemetry are editorial analysis.

## Glossary candidates

- **Context elision:** Removing selected prior content before the model's next step.
- **Ablation:** A controlled test that removes or changes one component to measure its effect.

Cold-reader sentence: Coding-agent performance depends on matching context, planning and tools to a model's capabilities and budget.
