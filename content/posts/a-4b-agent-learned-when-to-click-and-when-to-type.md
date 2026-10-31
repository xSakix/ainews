+++
title = "A 4B agent learned when to click and when to type"
description = "Microsoft's Mage-VL-Cowork combines screen actions and a persistent terminal in one open model. Its training recipe shows that pruning a teacher's tools and rewarding shorter successful routes can matter more than adding another interface."
tags = ["models", "agents", "research"]
date = 2026-10-31T04:03:07+01:00
draft = false
+++

Picture an analyst facing a spreadsheet with two banners to merge, a chart to add and an `.xlsx` file to preserve. This analyst is imaginary, but the choice is real: drag through the menus one cell at a time, or open a shell and edit the workbook through Python. A capable computer agent should know which route fits the job before the first click.

## One policy, two ways to act

Microsoft's Mage team has released Mage-VL-Cowork, an Apache-2.0 model with 4.74 billion parameters that can act through a graphical desktop or a persistent Bash and Python environment. It does not hand the decision to an outside router. On each turn, the same vision-language policy decides whether the task calls for one of 11 screen actions or a terminal command.

The distinction sounds small. It changes how an agent spends its context and how directly it can verify its work. A screenshot can consume thousands of tokens, while a long sequence of mouse actions can imitate badly what a software library does exactly. Yet the terminal cannot see an unsaved canvas, a dialog box or an application's temporary state. The model needs both channels and a habit of choosing between them.

The Mage team reports 66.04 percent on OSWorld-Verified, averaged over two runs of 361 tasks with a limit of 50 steps. The two runs scored 65.33 and 66.75 percent. Human performance in the team's comparison table is 72.4 percent; GPT-5.4-mini scores 69.6 percent in one run under the same task and step limits. ScaleCUA-Qwen3.5-9B leads the open-weight comparison at 68.7 percent. Mage-VL-Cowork's claim is therefore narrower than overall leadership: the team reports the best score among 4B models.

Those are Microsoft's measurements and have not been independently reproduced. The repository includes the evaluation tasks, agent code and launch scripts, which makes the claim more testable than a model-card number alone.

## The teacher had to lose tools

The training work began upstream of the model. A strong teacher given every available interface did not automatically produce clean examples. Overlapping routes split the supervision: an accessibility tree, direct desktop automation and visual clicking could all solve the same step in different ways.

The team compared two teacher setups on 672 held-out multi-application tasks. Its chosen harness gave GPT-5.4 graphical and coding tools, removed overlapping utilities such as `xdotool` and accessibility dumps, and preinstalled libraries for spreadsheets, documents, presentations, PDFs and images. That teacher succeeded on 92.0 percent of tasks in 25 steps on average. An accessibility-augmented harness reached 89.6 percent in 35.33 steps.

The difference grew after distillation. A 4B student trained from the pruned harness reached 37.6 percent, against 25.1 percent for the student trained from the larger tool set. Mean steps fell from 39.40 to 30.91. The same research team supplied both results. Even so, the comparison identifies a useful failure mode: a frontier model can absorb redundant choices by spending more steps, while a small student inherits the confusion.

The data pipeline followed the same preference for reusable structure. Mage-CUA-Forge generated 293,806 tasks across 6,915 atomic skills and retained 318,837 hybrid trajectories. Instead of asking an agent to construct every environment from scratch, the system built reusable workflows and application-specific preparers once per skill. With the same generation model, the team reports that tokens per task fell from 1.276 million to 85,000 and recurring cost fell from $0.906 to $0.158.

This is synthetic training data at industrial scale. Its value depends on the preparers, task specifications and rubrics being right. The repository says 38.24 percent of the generated tasks span multiple applications and that the trajectories divide roughly 68 percent graphical actions to 32 percent terminal actions.

## Specialise first, then unify

Mage-VL-Cowork starts from an intermediate Mage-VL checkpoint, rather than a model already specialised for graphical control or coding. Training proceeds through five stages: visual grounding, multi-step graphical work, coding and terminal work, hybrid supervised fine-tuning, and online reinforcement learning.

That order matters. The model first learns two competent channels and only then learns to route between them. The hybrid supervised stage scored 55.84 percent on OSWorld-Verified. Online reinforcement learning lifted the score to 66.04 percent while reducing mean model calls from 21.57 to 18.77 and output tokens per task from 7,374 to 5,499.

The reward did not merely make the agent try longer. It made successful routes shorter. The team used verifiable task rewards across 1,988 tasks, with 768 episode slots per update. The reinforcement-learning stage consumed more nominal compute than any other single stage even though it represented only 3.5 percent of the training schedule by the team's accounting.

Long desktop sessions create another problem. Screenshots can fill the context before the work ends. Mage-VL-Cowork keeps the three newest screenshots and four complete assistant responses, then collapses older turns into one-line action summaries. The policy retains recent visual changes and a compressed record of earlier work.

The active context is 32,768 tokens, although the architecture supports more. At each step the model emits reasoning, a short action summary and a tool call. That format lets earlier reasoning disappear while the action record remains.

## Where the benchmark ends

OSWorld was designed to test agents across real applications and operating-system tasks rather than isolated websites. The verified task set improves the reliability of its graders, but a benchmark still fixes the operating environment, installed software and success checks. It cannot show what happens when an agent meets a personal password store, an unpredictable network or a document containing hostile instructions.

Microsoft's own deployment guidance reflects that gap. The model can execute arbitrary shell commands and manipulate a desktop, so the team recommends disposable virtual machines or containers, no personal credentials, restricted outbound networking and human confirmation before irreversible actions. The model is released for research, not product deployment.

Its 4B size also does not mean that the complete system is light. The team reports 7.79 zettaFLOPs of nominal language-model training compute across the five stages, using 32 NVIDIA B200 GPUs and 1,120 CPU sandbox slots for reinforcement learning. Serving the BF16 checkpoint requires about 9.48 GB for the two weight shards, before runtime memory and the desktop environment.

The release is strongest as a training argument. Its designers narrowed the teacher's choices, constructed tasks around reusable skills and trained each action channel separately. Only then did they reward the model for completing verifiable work with fewer calls.

Return to the imagined analyst. The chart still belongs in the graphical application, where its appearance can be seen. The cell merge belongs in Python, where the file structure can be changed and checked precisely. The important action happens before either tool opens: the model chooses a route, and that choice is now part of the policy that anyone can inspect.

## References

- Microsoft Mage Team. (2026). *Mage: A Lightweight, Research-Friendly Multimodal Model Family*. https://github.com/microsoft/Mage
- Microsoft Mage Team. (2026). *Mage-VL-Cowork: A Full Training Recipe to Learn Hybrid Computer Use from Evolved Harnesses*. https://github.com/microsoft/Mage/blob/main/assets/mage_vl_cowork_tech_report.pdf
- Microsoft. (2026). *Mage-VL-Cowork model card*. https://huggingface.co/microsoft/Mage-VL-Cowork
- Xie, T., et al. (2024). *OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments*. https://arxiv.org/abs/2404.07972
- Yang, S., et al. (2026). *Mage-VL: An Efficient Codec-Native Streaming Multimodal Foundation Model*. https://arxiv.org/abs/2607.24904
