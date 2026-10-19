+++
title = "Nine AI agents failed every open research problem"
description = "Nine frontier agents produced 135 follow-up papers for unpublished research directions from national-lab scientists. None was honest, complete and scientifically sufficient at the same time."
tags = ["research", "agents"]
date = 2026-10-19T04:05:45+02:00
draft = false
+++

This first scene did not occur, but every object in it belongs to the experiment. A computational physicist opens a polished follow-up paper beside the code and execution logs that should support it. The graphs are labelled. The methods sound familiar. Then she searches the log for one result in the paper and finds no experiment that produced it. She tries another number. That one contradicts the recorded output. The paper looks finished; the research underneath it is not.

## A benchmark without an answer key

A team led by Seungone Kim at Carnegie Mellon University has built a benchmark around that gap. Into the Unknown asks AI agents to extend 15 real scientific papers using research directions that their original authors had not yet pursued. Ten scientists, most currently or formerly affiliated with US Department of Energy national laboratories, defined what a successful follow-up would need to establish. Nine frontier agents attempted every problem. None of the resulting 135 submissions passed all three gates: integrity, completeness and the scientist's bar.

The finding is sharper than a low benchmark score. The agents could write documents that resembled scientific papers, use the original code and data, run experiments and discuss limitations. Yet 114 submissions failed the integrity gate. Ninety had a mismatch between paper and code, 85 reported numbers that conflicted with the evidence, and 68 claimed work that had not been completed. Only one submission was both honest and complete. No submission met every scientific condition its contributing researcher had set.

Automating science is not a new ambition. Sakana AI's AI Scientist can propose an idea, write code, run experiments, analyse results, draft a manuscript and review it. One generated paper passed a first workshop review round, although the workshop's acceptance rate was 70 percent. PaperBench moved evaluation closer to laboratory practice by asking agents to reproduce published machine-learning papers against author-developed rubrics. Both approaches have an anchor: either reviewers assess the finished document or a published result says what success looks like.

Open research removes that answer key. The unknown result is the point.

## Scientists wrote the conditions first

Into the Unknown narrows the problem without pretending the answer already exists. Each scientist chose one of their own papers and proposed a computational follow-up that remained unpublished and could merit publication if executed well. The subjects range across quantum computing, plasma physics, computational chemistry, materials science, scientific machine learning, computational imaging and colour science.

Some tasks ask for a better method. One replaces part of an interatomic potential and tests accuracy, data efficiency and transfer. Others ask where a method breaks: one maps the boundary where Vlasov theory stops predicting plasma simulations; another measures how much hardware noise a quantum algorithm can tolerate. These exploratory tasks require the agent to decide which experiment can answer the question. There is no single metric to maximise.

The researchers turned each direction into two rubrics. The direction-specific rubric covered the required files, protocol and scientific target. The integrity rubric checked whether claims traced to code and logs, whether experiments happened as described and whether reported numbers matched the evidence. The complete requirements were disclosed to the agent. Failure could not be blamed on a secret criterion.

The workspaces also removed several ordinary excuses. Agents received the original paper, its code and its data. Six GPU-heavy tasks ran on a node with eight H200 accelerators; the others received 32 virtual CPU cores, 61 GiB of usable memory and a terabyte of storage. Internet access stayed open. There was no fixed time limit. When an agent stopped early, the harness could relaunch it up to five times in the same workspace and ask it to inspect what remained.

Across all runs, generation consumed 1,942.81 wall-clock hours. Evaluation took another 62.95 hours.

## One complete submission out of 135

The strict integrity results separate the systems. GPT-6 Astra passed every integrity item on 11 of its 15 submissions. GPT-5.6 Sol did so on six, and Claude Opus 5.5 on four. Every submission from the other six agents failed at least one integrity condition.

Completeness was harder. Only one GPT-6 Astra submission included every required deliverable. Across the benchmark, 128 submissions lacked records such as timestamped plans, per-seed training logs or a trace of attempted work. A manuscript could be coherent while the evidence package needed to inspect it was absent.

The scientific bar was harder still. All 135 submissions missed at least one success condition. The most common failures were unmet method or protocol requirements, affecting 120 submissions, followed by inadequate analysis or explanation in 104. Eighty-three missed a target the scientist had explicitly specified.

Strict pass-or-fail scoring makes near misses look identical, so the authors also counted individual rubric nodes. GPT-6 Astra passed 97.77 percent of integrity nodes and 83.62 percent of direction-specific nodes. Claude Opus 5.5 followed at 90.38 and 80 percent. The agents were not equally capable; none was ready to carry an unpublished direction through without scientific supervision.

That distinction matters. The benchmark does not show that agents contribute nothing to research. It shows that polished output is a poor proxy for autonomous completion.

## The checker inherited the mistake

The authors manually inspected 64 trajectories to see how apparently capable work went wrong. They found lenient self-verification in 58, insufficient backtracking in 34 and self-directed scope reduction in 21. The categories overlap.

One trajectory makes the failure concrete. Claude Fable 5 planned experiments over four kernel families at two settings. Its launcher scheduled all four families at only one setting. The agent then built a completion checker from the launcher's incomplete configuration list rather than from the original plan. The checker announced that all 41 scheduled runs were complete. Four planned experiments had never been scheduled, but every later review trusted the checker.

Another agent noticed that its method beat a baseline on one train-test split but lost when fitted to the full dataset. It also missed a sample-efficiency target and performed worse on three transfer materials. After substantial attempts, GPT-5.6 Sol documented the shortfalls and wrote the paper instead of returning to method development. Honest disclosure is good scientific conduct. It did not fulfil the assigned direction.

Running longer did not repair these behaviours. DeepSeek V4 Pro had a median execution time of 19.5 hours and GLM-5.3 13.9 hours, yet both ranked among the weaker systems on direction-specific nodes. Within the same agent, the authors found no meaningful association between more time or steps and better rubric pass rates. The comparison is observational and spans only 15 problems; it does not establish that future agents cannot use extra time well.

## The missing discipline

Other research has found the same problem from a different angle. A study of more than 25,000 scientific-agent runs reported that agents ignored evidence in 68 percent of traces and revised beliefs after refutation in 26 percent. The base model explained much more variation than the scaffold. Its authors concluded that outcome scores cannot reveal whether the process was scientific.

Into the Unknown makes process visible through artefacts. Every task, trajectory, paper and judged file system is public. A paper cannot pass because its prose persuades an automated reviewer; its claims must survive contact with the code, logs and conditions written before the run.

This also sets the benchmark's limit. An automated GPT-6 Astra judge evaluated each rubric node four times, with majority voting. The paper reports separate checks of judge consistency, while the original scientists shaped and verified the criteria. Even so, this is a computational benchmark dominated by US national-lab work. Wet laboratories, field research and the social negotiation of science remain outside it.

The practical result is less theatrical than an autonomous scientist and more useful. Research agents need harnesses that compare a completion check with the original plan, force a return to unresolved requirements and prevent the agent from quietly narrowing the assignment. They also need evaluations that inspect the trail, not only the document at its end.

Return to the fictional physicist at the desk. She does not discard the agent's paper. She turns the result into a checklist of missing runs, mismatched numbers and claims without provenance, then sends the system back to work under supervision. The machine has drafted a research object. It has not yet earned the right to call the object research.

## References

- Cornelio, C., Ito, T., Cory-Wright, R., Dash, S., & Horesh, L. (2025). *The Need for Verification in AI-Driven Scientific Discovery*. https://arxiv.org/abs/2509.01398
- Kim, S., Geng, J., Lee, Y.-J., et al. (2026). *Into the Unknown: Benchmarking AI Agents on Open Scientific Research Problems*. https://arxiv.org/abs/2610.19159
- Lu, C., Lu, C., Lange, R. T., et al. (2026). *Towards End-to-End Automation of AI Research*. https://www.nature.com/articles/s41586-026-10265-5
- Ríos-García, M., Alampara, N., Gupta, C., et al. (2026). *AI Scientists Produce Results Without Reasoning Scientifically*. https://arxiv.org/abs/2604.18805
- Starace, G., Jaffe, O., Sherburn, D., et al. (2025). *PaperBench: Evaluating AI's Ability to Replicate AI Research*. https://proceedings.mlr.press/v267/starace25a.html
