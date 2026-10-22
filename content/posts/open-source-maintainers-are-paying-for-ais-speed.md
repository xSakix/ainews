+++
title = "Open-source maintainers are paying for AI's speed"
description = "A Linux Foundation survey says maintainers estimate a quarter of incoming pull requests are AI slop, while contributors report halving the time they spend writing code. Curl is moving low-severity vulnerability reports into public view from 26 October, and PostgreSQL 19 slipped because AI code review found more defects than volunteers could fix."
tags = ["business", "community", "tools"]
date = 2026-10-22T03:15:11+02:00
draft = false
+++

Suppose a maintainer of a small parsing library, a man with a day job and a repository he looks after on Sunday evenings. This one is invented, a composite of the kind of person the surveys describe. He opens his inbox expecting two or three notifications. There are nineteen. Eleven are pull requests, tidy in form, each with a confident description and a green check mark. Three are reports of vulnerabilities that exist only if someone passes six options in an order nobody has ever used. He answers the first request carefully, realises halfway through that the author has not run the code, and closes the laptop with sixteen items still waiting.

His evening is made up, but the numbers that fit it were published this week. On 20 October the Linux Foundation released *Navigating Open Source Software Development in the Generative AI Era*, a survey of how maintainers and contributors are living with AI tools. It was sponsored by Red Hat, with support from Futurewei, OpenSSF and LF AI & Data. The same day, the maintainer of curl told his users that his project is near its limit. Four days earlier, a database project had explained why its next release is late. Read together, they describe a trade: AI has made writing code cheap, and the bill for checking it has gone to the people who were already working for free.

## What the survey found

The foundation reports that 59 percent of maintainers see growing contribution volume since generative AI spread, and 69 percent on large projects. Respondents estimated that a quarter of incoming pull requests are low-quality "AI slop", rising to 31 percent on large projects. Respondents also estimated that AI cut the time spent authoring code by 52 percent on average, and the foundation's summary gives time savings of 19 to 52 percent across the tasks it measured. Sixty-six percent said they put the saved time into technical debt and 63 percent into new features.

The mood is divided. Seventy-one percent of maintainers agree that generative AI lowers the barrier to taking part, yet 53 percent disagree that it has improved community trust. For highly complex work, 21 percent of respondents said AI made the task take longer. Rules lag behind use: only 35 percent of projects have a formal policy permitting generative AI, and 32 percent have no policy and no plans for one. Among contributors, 61 percent say they review and fully test AI-generated code before submitting it, and disclosure of AI help is inconsistent. The foundation says maintainer burnout is the first concern of large projects.

These are self-reported estimates. The press release and the report page do not give the sample size, so the percentages describe what respondents believe, not a count of pull requests. The foundation's own conclusion is organisational. Hilary Carter, its senior vice president of research, said projects should put "responsibility for testing and disclosure on contributors" and give maintainers "better tools to manage incoming pull requests".

## Curl runs out of room

Daniel Stenberg, who maintains curl, has been tracking the pressure since 2024. In a post on 26 January he ended the project's bug bounty, effective 31 January. The programme, run through HackerOne since 2019, had confirmed 87 vulnerabilities and paid out more than 100,000 dollars. He wrote that, before 2025, over 15 percent of submissions were confirmed vulnerabilities, and that from the start of 2025 the rate "plummeted to below 5%". He added that, by HackerOne's figures, curl's inbound volume rose sharply while that of Ruby, Node and Rails stayed flat or fell, and suspected the money was part of the reason. On pull requests he was calmer: curl could screen them with automated checks, so that nobody spends human time until a change gets "green check-marks from 200 CI jobs".

Reports were the other matter, and they did not stop when the money did. On 20 October Stenberg announced that from 26 October, vulnerability reports judged low or medium severity must be filed as public issues on GitHub. Only high and critical cases stay private. Over the last few years, he wrote, more than 90 percent of submissions could quickly be assessed as less than high. His reason was blunt: "We are struggling as a project as all key maintainers feel strained, overloaded and brought to the brink of what we can muster."

His account of the load is specific. He describes AI models that produce "crazy sequences or option combinations" which do something unexpected but are unlikely ever to occur in a real application. He also describes an army of researchers who, the moment a new set of fixes is announced, feed them to their models to look for similar mistakes. Public handling does not reduce the work per report, he admits, and it gives attackers a slightly longer window on bugs that are not yet fixed. He hopes more people can share the assessment and the writing of advisories. He called the change "our next step in a survival strategy" and added: "It might not be our last."

## When the reviewer is right

Not all of the new load is noise, and the PostgreSQL project shows the difficult version. On 9 October, core committer Peter Eisentraut of EDB published a blog post on why an unusually high number of features, about eight to ten depending on how they are counted, were reverted from PostgreSQL 19 during beta. The Register reported on 16 October that the release has moved to about 19 November and that the reverted features are likely to land in PostgreSQL 20.

Eisentraut gives several causes, and says the code may simply not have been good enough. One is the review tooling. Some reverted features had architectural defects that could not be fixed quickly in beta. But LLM-assisted review also surfaced a long tail of edge cases that in the past would have turned up over five years of fixes. With such review, he wrote, "you’re staring at a list of like forty defect reports," and "even if each of them requires only a three-line fix on average, there is a fixed overhead to dealing with each of these, and then you run out of time." The features were written before such review was useful, so the bar rose after the code was committed. He says this is not vibe coding, which was not available when the code was written.

He also notes that senior developers spent months, from April to August, on security fixes in what he calls the "Vulnpocalypse", which cut the usual beta-period review. If review tools keep improving at the current rate, he expects the situation to sort itself out in future cycles, and he suggests that AI-assisted fuzzing become part of feature development. The project is also considering an "experimental" status for new features. Nothing in his account is slop. The findings are real, and they cost the same hours to fix.

## Where the cost lands

The three accounts differ in what the tools produce. The survey counts low-quality contributions. Curl receives reports that are technically valid but trivial in practice. Postgres receives defects that are genuine and, under a fixed release date, unaffordable. In each case the part that got cheap is the generation of text and findings, and the part that stayed expensive is judgement: deciding what matters, reproducing it, writing the fix and answering the author.

None of the sources shows that the trade is a bad one overall. The survey's contributors report real savings and real reinvestment in technical debt, and Eisentraut expects a more robust database. The sources do show who carries the cost. Stenberg's steps, from ending payments to publishing lesser bugs, read as attempts to push some of it back onto the senders or out to the crowd, and the foundation's advice to make contributors responsible for testing and disclosure points the same way.

On Monday the invented maintainer reads his nineteen items again. He writes one short note to the author of the pull request, pins it above the others, and adds a line to the contributing file saying that anyone who sends code should say how it was tested. It takes four minutes. Whether that line is read, or only generated around, is the question the three projects are now testing in public.

## References

- Boysel, S., & Lai, A. (2026). *Navigating Open Source Software Development in the Generative AI Era: Challenges and Opportunities for Project Communities*. Linux Foundation Research. https://www.linuxfoundation.org/research/oss-development-gen-ai-era-2026
- Clark, L. (2026). *Postgres 19 delayed after AI reviewers find more bugs than humans can fix*. The Register. https://www.theregister.com/databases/2026/10/16/postgres-19-delayed-after-ai-reviewers-find-more-bugs-than-humans-can-fix/5303471
- Eisentraut, P. (2026). *The reverts will continue until morale improves*. https://peter.eisentraut.org/blog/2026/10/09/the-reverts-will-continue-until-morale-improves
- Kunert, P. (2026). *Swamped curl maintainers take low-level flaws public to survive vulnerability 'avalanche'*. The Register. https://www.theregister.com/security/2026/10/20/swamped-curl-maintainers-take-low-level-flaws-public-to-survive-vulnerability-avalanche/5304198
- Linux Foundation (2026). *New LF Research survey shows generative AI cuts open source coding time in half, but 25% of incoming pull requests are considered AI slop*. PR Newswire. https://www.prnewswire.com/news-releases/new-lf-research-survey-shows-generative-ai-cuts-open-source-coding-time-in-half-but-25-of-incoming-pull-requests-are-considered-ai-slop-302913843.html
- Speed, R. (2026). *AI cuts coding time, but it's also filling open source's inbox with crap*. The Register. https://www.theregister.com/ai-and-ml/2026/10/21/ai-cuts-coding-time-but-its-also-filling-open-sources-inbox-with-crap/5304389
- Stenberg, D. (2026). *Do minor curl vulnerabilities in the open*. https://daniel.haxx.se/blog/2026/10/20/do-minor-curl-vulnerabilities-in-the-open/
- Stenberg, D. (2026). *The end of the curl bug-bounty*. https://daniel.haxx.se/blog/2026/01/26/the-end-of-the-curl-bug-bounty/
