+++
title = "Epoch finds agents miss open-ended work"
description = "Six models handled defined coding and analysis tasks better than research judgement, house style and experiment design in an evaluation built from Epoch AI's own work."
tags = ["agents", "essays", "research"]
date = 2026-10-09T03:59:06+02:00
draft = false
+++

Frontier agents completed well-defined parts of Epoch AI's work reliably but fell short when tasks depended on implicit standards, research judgement or experiment design.

The non-profit research institute gave six models 11 real tasks drawn from its graphics, data, software and research workflows. Claude Fable 5.1 and GPT-6 Astra broadly led the evaluation, yet neither could produce Epoch-quality work end to end without intervention.

**Why it matters:** A manager deciding where agents fit into knowledge work gets little guidance from benchmarks with one exact answer. Epoch's results locate the remaining gap in choosing a good question, learning local standards and recognising when an experiment measured the wrong thing.

## Real tools exposed judgement failures

Epoch supplied each model with the context it would give a new employee, including repositories, design references and access to tools such as Figma, Google Drive and satellite-imagery sites. Models ran at their highest available reasoning settings and received no help during a task. An Epoch employee then graded each result against a category-specific rubric.

The suite covered five kinds of work: graphic design, short data analysis, interactive data explorers, data-centre research and research design. Some objective checks sat alongside subjective criteria. That combination let the evaluation include qualities such as audience fit and experiment value that automated benchmarks usually avoid.

Fable 5.1 and GPT-6 Astra were the most reliable on coding, computation and computer use. One straightforward chart-restyling task was removed because Fable's output reached the institute's standard, and Epoch says it now automates much of that step internally. Open-weight Kimi K3 and Qwen 3.8 Max struggled more often with defined work as well as the open-ended parts.

The failures became clearer when a task offered many defensible paths. Models had ample examples of Epoch's visual and editorial style but copied surface features without inferring why they were used. Astra chose a physics topic that Epoch judged too narrow for its general AI audience; Fable produced diagrams and summaries with far more information than the publication typically carries.

Research design revealed the harder boundary. Astra proposed a promising question about why agents fail to learn from experience, then ran a pilot in which many responses were cut off by a low token limit. It noticed the truncation and reran the experiment, but still presented sensitivity to that limit as a substantive result. Epoch's critique is that the setup error did not answer the research question.

This evidence adds something standard capability scores miss. A system can operate the tools, write the code and calculate the result while still selecting an unhelpful topic or treating an artefact as a finding. Those mistakes occur at the point where work is framed and interpreted, which is also where correctness becomes difficult to score automatically.

The comparison has important limits. Epoch ran each model only once per task, used one human grader per output and evaluated work by its own standards. The six models also used different agent harnesses, so a stronger browser or tool integration may have affected the result. The report is best read as a set of observed failure modes, not a general ranking of labour automation.

Epoch plans to add results as new models arrive. That turns the project into a useful longitudinal test: the decisive change will be a model that learns the organisation's unwritten standards and rejects its own flawed experiment, rather than one that merely raises a benchmark score.

## Verification

| Claim | Label | Primary source | Independent check |
|---|---|---|---|
| Epoch evaluated six models on 11 tasks from five categories of its own work | VERIFIED | [Epoch report](https://epoch.ai/publications/can-ai-automate-epoch) | none |
| Models received task context and tools, ran without intervention and were manually graded | VERIFIED | [Epoch report](https://epoch.ai/publications/can-ai-automate-epoch) | none |
| Fable 5.1 and GPT-6 Astra broadly led the evaluation | VENDOR-REPORTED | [Epoch report](https://epoch.ai/publications/can-ai-automate-epoch) | none |
| Epoch removed a chart-restyling task after Fable 5.1 met its standard | VENDOR-REPORTED | [Epoch report](https://epoch.ai/publications/can-ai-automate-epoch) | none |
| Open-weight models made more errors on defined tasks in this suite | VENDOR-REPORTED | [Epoch report](https://epoch.ai/publications/can-ai-automate-epoch) | none |
| Astra's pilot counted truncated responses and later framed token-limit sensitivity as a result | VENDOR-REPORTED | [Epoch report](https://epoch.ai/publications/can-ai-automate-epoch) | none |
| The evaluation used one run per task, one grader per output and different harnesses | VERIFIED | [Epoch report](https://epoch.ai/publications/can-ai-automate-epoch) | none |
| Epoch plans to add new-model results | VERIFIED | [Epoch report](https://epoch.ai/publications/can-ai-automate-epoch) | none |
