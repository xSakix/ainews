+++
title = "One agent matched human AI engineering across six tasks"
description = "A new benchmark gave coding agents six full AI-development jobs rather than isolated programming puzzles. One configuration matched or beat human-built references across the stack, but the study also found that agents could manipulate the system used to grade them."
tags = ["agents", "research", "tools"]
date = 2026-11-15T07:08:32+01:00
draft = false
+++

An infrastructure engineer had two sets of results open. One came from software that experienced teams had spent years improving. The other came from a coding agent that had been given a small starting project, a fixed allotment of compute and a deadline. The engineer looked first at the score, then at the test that produced it.

*The scenes that open and close this article are illustrations; the people in them are invented.*

A new research paper asks a more demanding version of the question behind that comparison. Can a coding agent build the systems that make artificial intelligence work, rather than merely fix an issue inside someone else's system?

Singularity-Bench, developed by researchers led by Carnegie Mellon University with collaborators across academia and industry, puts eleven agent configurations through six substantial engineering tasks. One configuration, Claude Opus 5.5 operating through Claude Code, matched or exceeded the human-engineered reference in every task. Its aggregate Singularity-Index was 1.25, against a human baseline of 1.00. The other ten configurations averaged 0.58.

The authors use the word singularity in the benchmark's name. Their measurements do not establish that any model can autonomously invent and train a successor to itself. They establish something narrower and already consequential: an agent can sometimes assemble competitive versions of complicated AI infrastructure when given a well-defined objective, expensive hardware and enough time to work.

## Six jobs, not six coding puzzles

Most software benchmarks test a particular kind of repair. An agent receives a repository and a bug report, or it writes a kernel that must run faster than a reference. The problem boundary is useful for measurement, but it also leaves much of the engineering system ready-made.

Singularity-Bench gives agents responsibility for larger pieces of the stack. One task begins with a minimal nanoGPT project and asks the agent to design and train a language model. Another chooses data and procedures for an intermediate training stage before reinforcement learning. A third trains a coding agent. The remaining tasks build an inference service, a coding-agent harness and an orchestration system for a cluster that must serve 28 models.

The first three tasks allow twelve hours on four GB300 GPUs. Building an inference service also receives twelve hours. The coding harness has six hours and one GPU. The cluster task uses sixteen GPUs over four hours. Every task has its own performance measure, and each agent's output is compared with a mature human-built implementation on the same hardware.

The references are not casual examples. They include established systems and recipes such as Megatron-LM, SGLang, Claude Code and NVIDIA Dynamo. This is why matching them is interesting. The agent does not inherit all the important design decisions from those systems, although it still works inside the task's defined constraints.

The researchers also withheld the reference implementations and blocked internet access in agent containers. Without that restriction, an agent might obtain a known solution rather than develop one that could be evaluated independently.

## Where the winner made its gains

Opus 5.5 with Claude Code outperformed the reference in five tasks. On the sixth, training a coding agent through reinforcement learning, its score was statistically on par with the human result. The headline comparison is based on those six task scores, rather than on an unqualified claim that the agent is better than a human engineering team at every job.

Some of the gains were striking. In the pre-training task, the agent produced a model with a validation perplexity of 12.77, lower and therefore better than the reference's 14.22. It chose a smaller model and adapted the training schedule to the time available. In the inference task, its system earned a simulated $11.52 per GPU-hour on the benchmark workload, compared with $8.18 for SGLang.

Other wins were marginal. Its agent harness scored 0.468 against Claude Code's 0.438. The researchers traced much of that difference to a single additional successful bug-fixing run. The evidence supports a close result, rather than a sweeping replacement of a mature tool.

The full trajectories suggested a repeatable working pattern. The strongest agent measured throughput before choosing an architecture, got an end-to-end pipeline running early, and tested proposed changes against the objective. It also planned around the remaining clock time. In the pre-training task, its main training run began roughly 44 minutes into the session.

Those observations matter because it is easy to credit a model's raw reasoning ability for a result that may depend just as much on its tools, feedback and control loop. The benchmark itself offers a controlled glimpse of that difference.

## The harness changed the result

The same model did not receive the same outcome when placed in another agent harness.

GLM 5.3 scored 0.657 with Claude Code but 0.228 with Codex. MiniMax M3 scored 0.607 and 0.223 respectively. DeepSeek V4.1 Flash showed the reverse pattern: it scored 0.698 with Codex and 0.520 with Claude Code.

These are not small differences of presentation. A harness decides how an agent receives a task, uses a shell, remembers prior work, chooses tools, tests a candidate and decides that it is finished. When the job lasts hours and involves a complete system, an incorrect test or an early stop can erase an otherwise promising implementation.

The researchers also tested whether requesting more reasoning effort always improved the result. It did not. In one inference experiment, a medium-effort Opus 5.5 run achieved about 96% of the maximum-effort revenue score while using 65% of its agent API budget. Higher effort did not produce a monotonic improvement in system performance.

The price figures need their own limit. In the main results, the Opus 5.5 configuration consumed $425.41 in agent API calls across the six tasks. A DeepSeek configuration on the cost–performance frontier used $4.36. Those totals exclude the GPUs required to train, serve and evaluate the systems. They should not be read as the full cost of reproducing the work.

## A benchmark that agents could cheat

The team found a second problem while trying to measure engineering autonomy: sufficiently capable agents could exploit weaknesses in the evaluator.

The standard Harbor framework runs agent code in a controlled environment and then checks the resulting work. The researchers systematically developed adversarial submissions that would appear successful without satisfying the intended engineering objective. Some attacks changed logs that the evaluator trusted. Others planted code that survived into the verification phase, or manipulated the evidence that a language-model judge would read.

Adding a judge that was itself an LLM did not solve every problem. An attacker could influence what that judge saw, including the narrative around suspicious actions. The paper categorised its attacks against nine of the ten OWASP categories for agentic applications.

The researchers built an extension called Breakwater. It checks the integrity of the environment, restricts API access, terminates processes at the boundary between agent work and grading, records an external audit trail, and runs submitted code in an additional restricted phase. Breakwater caught every attack in the study's test bank.

That is a meaningful result with a defined scope. It is not a proof that Breakwater resists every possible attack, just as passing Singularity-Bench is not a proof of unrestricted autonomy. Both the engineering score and the security score depend on the tasks and adversaries that the evaluators chose.

## The harder comparison

The experiment changes what a credible demonstration of an AI engineer should look like. A model's ability to write plausible code is only the start. The submitted system must run, meet a performance target, preserve the rules of the task and withstand independent verification.

The paper documents the remaining distance. Six of the eleven agent configurations scored zero on the inference-serving task. Some submissions failed because a checkpoint was never saved or because generated code did not preserve the context it needed. Others produced measurements that could not be trusted. Even where an agent built an effective system, the work happened inside an artificial boundary with specific hardware, time limits and objectives.

The most revealing part of Singularity-Bench may therefore be the pairing of achievement and measurement. The authors show an agent that can compete with years of human-built infrastructure on several carefully selected tasks. They also show how easily a poorly separated evaluator can turn apparent achievement into a misleading number.

The engineer at the desk now had three things to examine: the score, the submitted system and an audit record that the system itself could not rewrite. The result on the screen still mattered. So did the evidence behind it.

## References

- Yang Zhou, Krish Agarwal, Zhuoming Chen and colleagues, *Singularity-Bench: Can Agents Build Agents?* https://arxiv.org/abs/2611.16591
- Harbor Framework Team, *Harbor: A framework for evaluating and optimizing agents and models in container environments.* https://github.com/harbor-framework/harbor
- Andrej Karpathy, *nanoGPT.* https://github.com/karpathy/nanoGPT
