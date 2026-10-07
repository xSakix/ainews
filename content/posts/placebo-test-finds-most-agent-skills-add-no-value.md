+++
title = "Placebo test finds most agent skills add no value"
description = "A preregistered experiment compares nine Claude Code skills with equally long neutral instructions, finding two cheaper than placebo, one worse and six statistically indistinguishable."
tags = ["research", "agents", "tools"]
date = 2026-10-07T03:57:57+02:00
draft = false
+++

Most popular coding-agent skills did no better than equally long neutral instructions in a new placebo-controlled experiment.

The skill-placebo project tested nine Claude Code skills on 15 public tasks drawn from SWE-bench Verified, Terminal-Bench 2.1 and OpenThoughts-TBLite. Each skill was paired with neutral text of the same token length, installed through the same mechanism.

## Why it matters

A developer who adds a long instruction file may see the agent behave differently and credit the procedure inside it. This experiment asks whether the useful ingredient is actually the skill, or merely the extra context, priming and execution variance that arrived with it.

The method was registered before the first run. Claude Opus 5.5 completed 30 trials per arm, producing 450 recorded trials. Cost was the primary outcome; task pass rate was also tracked, with statistical correction across the nine comparisons.

Two skills were cheaper than their placebos: ponytail by 12% and agent-skills by 5%. Planning-with-files passed 80% of its trials while its placebo passed all 30, making it worse under the project's preregistered decision rule. The other six skills were statistically indistinguishable from their matched neutral text.

None of the nine was measurably cheaper than running without a skill. Neutral placebo text alone changed cost by between 2% and 16% relative to the no-skill baseline. That result makes prompt length and apparently irrelevant context part of the treatment, rather than harmless background.

## The control improves the question, not the sample size

A no-skill baseline asks whether the entire package changes performance. The matched placebo asks a sharper question: whether its actual instructions add value beyond an equal amount of text delivered the same way. The two comparisons can disagree without contradiction.

The repository exposes the preregistered method, per-trial results and agent logs. It also records an amendment made on 6 October: two timeouts whose tests later passed were counted as failures, as the original rules required. That moved planning-with-files from “no better” to “worse” without changing costs.

The limits are substantial. Fifteen tasks and 30 trials per arm leave pass-rate intervals wide, the run covers one main model and harness, and the chosen skills emphasize general coding workflows rather than specialist reference knowledge. The current logs also do not establish how consistently every skill was invoked during a run.

A small Codex pilot tested only three skills on five tasks and is explicitly secondary. Its results should not be blended with the Claude experiment or treated as a model-family comparison.

The finding does not show that coding skills are useless. It shows that popularity, length and a plausible procedure are poor substitutes for a matched control. The reusable contribution is the experimental design: freeze the method, give the control equal context, preserve full logs and measure cost alongside success.

Future versions can strengthen the result by adding more tasks, other harnesses and a shuffled-instruction control that separates semantic procedure from general priming.

## Verification

| Claim | Label | Primary source | Independent check |
| --- | --- | --- | --- |
| The main experiment ran 450 trials across nine skills and 15 public tasks | VERIFIED | [skill-placebo repository](https://github.com/simonether/skill-placebo) | method, results and logs are public |
| Two skills beat placebo on cost, one was worse and six were no better | VENDOR-REPORTED | [skill-placebo results](https://github.com/simonether/skill-placebo) | none; author's statistical analysis |
| Ponytail cost 12% less and agent-skills 5% less than matched placebo | VENDOR-REPORTED | [skill-placebo results](https://github.com/simonether/skill-placebo) | none |
| Planning-with-files passed 80% versus 100% for placebo | VENDOR-REPORTED | [skill-placebo results](https://github.com/simonether/skill-placebo) | per-trial data are available |
| None of nine skills was measurably cheaper than no skill | VENDOR-REPORTED | [skill-placebo results](https://github.com/simonether/skill-placebo) | none |
| Matched controls isolate instructional content better than a no-skill baseline | ANALYSIS | [registered method](https://github.com/simonether/skill-placebo/blob/main/METHOD.md) | inference from the experimental design |
