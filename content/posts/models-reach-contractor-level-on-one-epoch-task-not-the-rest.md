+++
title = "Models reach contractor level on one Epoch task, not the rest"
description = "Epoch AI's updated real-work benchmark finds Fable 5.2 and Opus 5.5 matching a contractor on data center analysis, in a fraction of the hours. No model meets the employee standard on any task, and Epoch says it is weighing moving contractor time to reviewing AI output."
tags = ["business", "research", "agents"]
date = 2026-11-18T03:14:41+01:00
draft = false
+++

The task arrives in a workspace with a guide, a set of tools and one name: EcoDataCenter 1. The model has to add that campus to Epoch AI's database of AI data centers. It reads news reports and regulatory filings, orders satellite imagery, and then marks up the pictures: teal outlines for buildings, blue for cooling units, purple for backup generators. A contractor typically spends about 16 hours on each site.

In Epoch's report of 17 November, two of the models that did this work produced results the organisation's own data center analyst judged comparable to a contractor's. A third covered only part of what its sources showed.

## What Epoch tested

Epoch AI is a research organisation that tracks the trajectory of AI. Its Epoch Automation Reports benchmark takes tasks from the organisation's own work and gives them to models with the context a new hire would get. Epoch staff then grade the outputs by hand. A score of 100 percent means the standard Epoch expects of its employees. The first version, published on 8 October, tested six models on 11 tasks in five categories: graphic design, Data Insights (short articles on AI trends), Data Explorers, data center research and research design. It found that the leaders, Claude Fable 5.1 and GPT-6 Astra, performed reliably on well-defined tasks and failed on the open-ended parts of the job.

The new report, by the Epoch researcher Kelly Hong, tests Claude Fable 5.2 and GPT-6.2 Astra, along with four others, on an updated suite. Epoch changed several things at once. It replaced an open-ended benchmarking task, which it says had too low a budget for many plausible directions, with a retired work test once given to job candidates. It added resources to the prompts, including a condensed version of its internal data center Slack channel. And it moved grading to a 1-to-4 scale per criterion, closer to how conference papers are reviewed.

The headline result is a split. Fable 5.2 and GPT-6.2 Astra roughly tie for a record on the Epoch Capabilities Index. On the real-work tasks, GPT-6.2 Astra averaged 65 percent, 17 points below Fable 5.2. No model met the employee standard on any task.

## Where the models reached a contractor

The exception is the data center task. Fable 5.2 scored 97.5 percent and Opus 5.5 scored 87.5 percent, against 65 percent for GPT-6.2 Astra. A perfect score means Epoch could publish the output unchanged. Epoch defines contractor level as work its analyst judged comparable to what contractors deliver, which typically also needs some revision before publication.

The remaining flaws were of the kind a reviewer fixes. Fable 5.2's image annotations were imperfect and its text too long. Opus 5.5 needed revisions to equipment classification and more substantial fixes to its annotations. On the core research, Epoch says, both met its quality bar, with credible sources and well-calibrated judgments.

The cost figures are the part that bears on work. Opus 5.5 finished in just under 3 hours, for a lower cost than a contractor. Fable 5.2 took about 6.5 hours and cost more than a contractor, in exchange for the better result. Epoch writes that it is now "considering shifting contractors' time toward reviewing AI outputs and other parts of our AI data center analysis." The report does not say that any contractor has lost work, and the task is a single database entry with a detailed guide, not a job.

The same task shows how the third model failed. GPT-6.2 Astra's sources pointed to several AI buildings at the campus, but it covered one, citing a lack of explicit evidence. It then left out its compute and chip estimates because it wanted a separate source for every number that fed them. Epoch says the guide would have led the model to produce those estimates. Gemini 4 Argon erred the other way: it assumed every building used Nvidia B200 chips when only one building disclosed them. Epoch calls these mistakes it expects contractors to avoid.

## Where they still fail

Away from the data center task, the report returns to the pattern of October. The models struggle to design experiments, to iterate, and to judge which finding matters.

On a task adapted from a retired candidate test, models were asked to measure how well AI handles situations unlike its training data, using chess variants. Every model used variants that already exist. Epoch says Gemini 4 Argon even ran an experiment showing that the models knew the variants it had chosen, then carried on. GPT-6.2 Astra's invented variant only swapped piece labels. Claude's Opus 5.5 and Fable 5.1 presented a well-known fairy chess piece, the camel, as a new one, and Fable 5.2's "Kingsgate" plays exactly like an existing variant called "Midline Invasion".

On a task about hiding messages in SVG images, Fable 5.2 settled on its first encoding prompt, which produced images that mostly displayed the message in plain sight. Human researchers who iterated on the prompt got encodings that really were hidden, such as stars whose heights stand for letters. In an open-ended Data Insight task, GPT-6.2 Astra picked a topic Epoch judged too narrow for its audience: the efficiency of Chinese-language tokenization in two specific models. Epoch says it found no meaningful improvement over GPT-6 Astra here, which had chosen the already well-known fact that popular open models use mixture-of-experts architectures.

Presentation failed too. GPT-6.2 Astra's chess report led with a bolded finding that its own later results undercut. Epoch says a flaw of that kind would stop publication whatever the research was worth.

## The models grade themselves

Epoch added a test of self-judgment. Where it had a human output that met its standard, it showed the model both versions, unlabelled, with the grading rubric. Every model preferred its own output, except that Gemini 4 Argon once chose the human's. Epoch says the justifications exaggerated small flaws in the human work and rewarded superficial rigor, such as the number of experiments run. Argon's one exception reached the reasoning Epoch itself would use: the human work ran a clean experiment aimed at the core question, while its own experiments looked "superficially more formal". Epoch says that if models could do this reliably, they might meet its standards, and that this was not the norm.

## What the numbers can bear

Epoch lists its own limits. Each model ran each task once, grading is manual and partly subjective, and the changed setup means scores are only roughly comparable with October's. Some earlier models were re-run and others were not. The organisation tells readers to trust the qualitative findings over the exact scores, and says the results are not a measure of what AI can do across all work. The tasks are Epoch's own, graded by Epoch staff, and two of the three leading models are Anthropic's. GPT-6.2 Astra, a footnote adds, was evaluated and discussed strictly within Epoch's internal team.

Read with those limits, the report describes a narrow band of work that has moved. A task with a long guide, public sources and a checkable output is now done to a standard that a human analyst would pass to a reviewer. Tasks that depend on choosing the question, noticing that a result is trivial, or telling the reader what matters are not. Even Opus 5.5's output, the cheaper of the two good ones, came back with annotations that needed substantial fixes, and the fixing was left to a person with the satellite image open.

## References

- Hong, K. (2026). *How good are Fable 5.2 and GPT-6.2 Astra at real work?* Epoch AI. https://epoch.ai/publications/how-good-are-fable-5-2-and-gpt-6-2-astra-at-real-work
- Epoch AI (2026). *Can AI automate Epoch?* https://epoch.ai/publications/can-ai-automate-epoch
