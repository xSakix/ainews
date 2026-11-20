+++
title = "When Fable 5 went dark, developers' merged work barely moved"
description = "A Harvard preprint treats the 19-day suspension of Claude Fable 5 as a natural experiment. Developers who lost the model, which scored about 11 points higher on a coding benchmark than its replacement, merged pull requests at nearly the same rate, and five ordinary model upgrades showed the same flat result. The study is not peer reviewed and its measure is narrow, but it tests what a benchmark gain buys in everyday work."
tags = ["research", "tools", "essays"]
date = 2026-11-20T03:11:44+01:00
draft = false
+++
The letter reached Anthropic at 5:21 on a Friday afternoon, Eastern time, on 12 June 2026. The US government, citing national security authorities, had issued an export control directive on Fable 5 and Mythos 5, the company's newest models, which had been public for three days. The letter barred access by any foreign national, inside or outside the country. Anthropic had no reliable way to check a user's nationality in real time, so, to comply, it abruptly disabled both models for every customer. The letter, the company wrote, gave no specific details of its concern.

Developers who had spent three days with its newest model found it gone before the weekend. Most of them moved to Opus 4.8, the next model down. Nineteen days later the ban was lifted and Fable 5 came back.

## An accident that works as an experiment

Yining Hua, a researcher at Harvard, saw in those 19 days something that benchmark scores cannot offer. In a preprint posted to arXiv on 17 November, Hua argues that the suspension was a natural experiment: the same developers, working on their own projects, lost a better model and regained it, for reasons that had nothing to do with them.

The question is simple. A model company announces a coding model with a higher score on a benchmark such as SWE-Bench Pro, and buyers read the score as a promise that developers will get more done. Hua notes that no study had tested that promise on real work. The paper takes the scores from Anthropic's system cards: 80.0 percent for Fable 5 and 69.2 percent for Opus 4.8, a gap of 10.8 points.

The data come from public GitHub. Claude Code can add a co-author line to a commit, naming the model that helped write it, and some developers let that line carry over into the pull request description. Hua used it to identify which model produced each pull request. The treated group is 297 developers who opened at least one pull request naming Fable 5 in the three days it was available. The control group is 8,908 developers who used Opus 4.8 throughout and never named Fable 5. The study compares the treated developers with themselves across four phases (before release, Fable 5 available, suspended, restored) and against the control group over the same dates, a design known as difference in differences.

The outcome is the share of pull requests merged within seven days. The treatment worked as intended. In the three days of availability, 82.3 percent of the treated group's pull requests named Fable 5. During the suspension, 0.9 percent did and 74.6 percent named Opus 4.8. After restoration only 26.9 percent named Fable 5 again.

## What the merge rate did

It stayed flat. Having Fable 5 raised the seven-day merge rate by 1.4 percentage points, with a 95 percent confidence interval from minus 1.4 to plus 4.3. That interval includes zero, so the study cannot say the model changed anything. It also cannot rule out a gain of a few points, and the paper says as much: the suspension lasted only 19 days, and the first phase with Fable 5 lasted three. A placebo test, which compares the weeks before release with the suspension, when nothing changed for the treated group, came out at minus 2.6 points, with an interval from minus 6.2 to plus 1.1. That is a reminder of how much the number can move without any cause.

Hua then looked at the same question in five ordinary upgrades between Claude models in 2026, where developers chose for themselves when to switch. In that part of the study 1,208 developers and 15,442 pull requests were compared a week before and a week after each release. The newer models scored 5 to 18 points higher on SWE-Bench Pro in the six upgrades where both scores were published. The pooled change in merge rate was minus 0.9 points, from minus 1.9 to plus 0.2. All five estimates pointed down, though none of them was individually significant. Merged pull requests per week rose by 2.4 percent, with an interval from minus 4.9 to plus 10.2 percent. The upgrade analysis is observational, and the author says developers who switch early may be more skilled with new tools, which would bias results upward.

## Why a better model may not show

The ceiling is the first explanation. In the week before each upgrade, the developers who would switch had 94.5 percent of their pull requests merged within seven days, and 83.8 percent of them had every pull request merged. Little room was left for a model to improve the rate.

The second is who merges. Of 2,019 sampled pull requests, 95 percent were merged by the author, and 90 percent had no approval from any other account. The median time from opening to merging was under half an hour in every phase. A merge in this data mostly records that a developer judged the work good enough, not that a reviewer agreed. Hua concedes that if models differ mainly when someone else reviews their work, the estimates are too small.

Hua's own hypothesis is about the tasks. Developers hand agents work that an older model can already do. The paper cites Anthropic's December 2025 study of its own staff, in which more than half of 132 engineers and researchers said they could fully delegate only 0 to 20 percent of their work to Claude, and which found that they delegated tasks that are easy to check and low in stakes. If so, the hard problems that separate Fable 5 from Opus 4.8 on a benchmark are not the problems developers were handing over. Description length, the number of files mentioned and the share of new features did not change after the upgrades, which suggests developers did not give the stronger models harder work.

A second line of evidence points the same way from the benchmark side. In March 2026 METR had four active maintainers review 296 AI-written pull requests that passed the automated tests of SWE-bench Verified. Maintainer merge decisions came out about 24 percentage points lower than the benchmark's automated grader suggested. Hua adds that Fable 5 led Opus 4.8 by only 1.6 points on Terminal-Bench 2.1, largely because one in five Fable 5 runs fell back to Opus 4.8 after a safety refusal, so even the benchmark gap was not the same everywhere.

## Limits of the result

The preprint has not been peer reviewed and has a single author. Only about 1 percent of merged Claude Code pull requests name their model, though Hua reports that those that do were merged about as often as the rest, and that refitting on all pull requests of the same developers pointed the same way. The restoration phase overlapped with a holiday, with the release of Sonnet 5 and with a rule that kept Fable 5 to half of subscribers' weekly limits until 7 July. Losing Fable 5 also meant switching tools in ways that a benchmark score does not describe, so the study measures the whole experience of the model, speed and limits included, which Hua argues is what a buyer is really choosing.

None of this shows that the stronger model is no better. It shows that on one visible measure of finished work, in the pull requests where developers named their model, a gap that vendors advertise in points did not appear. Whoever pays for the top tier of a coding model, or writes a rule that judges models by their scores, now has a study to check that purchase against.

## References

- Anthropic (2026). *Redeploying Claude Fable 5*. https://www.anthropic.com/news/redeploying-fable-5
- Anthropic (2026). *Statement on the US government directive to suspend access to Fable 5 and Mythos 5*. https://www.anthropic.com/news/fable-mythos-access
- Anthropic (2025). *How AI is transforming work at Anthropic*. https://www.anthropic.com/research/how-ai-is-transforming-work-at-anthropic
- Hua, Y. (2026). *Higher-Scoring Coding Models Did Not Get More Work Done*. https://arxiv.org/abs/2611.23216
- Whitfill, P., Wu, C., Becker, J., & Rush, N. (2026). *Many SWE-bench-Passing PRs Would Not Be Merged into Main*. METR. https://metr.org/notes/2026-03-10-many-swe-bench-passing-prs-would-not-be-merged-into-main/
