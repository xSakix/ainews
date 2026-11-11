+++
title = "Token Spend Tracks Who Uses Agents, Not What Gets Shipped"
description = "A JetBrains study links five weeks of coding-agent token use to the commits of 404 engineers. Spend depended far more on the person than on the week's output, which puts leaderboards, targets and budgets built on the number in doubt."
tags = ["business", "research", "agents"]
date = 2026-11-11T03:23:00+01:00
draft = false
+++

Suppose a head of platform engineering opens the monthly invoice from her AI vendor on a Monday morning. The line for coding agents has grown again, and she has been asked to explain it by Wednesday. She builds the obvious chart: spend per engineer on one axis, merged work on the other. She expects a rising line. What she gets looks like a scatter of confetti. Two engineers with the same output differ in spend by a factor she cannot explain, and the heaviest user is not the one whose work she would single out. This is an invented scene, a way to see the problem before the numbers arrive.

The numbers now exist. On 10 November, a team from JetBrains, Carnegie Mellon University and the University of California, Irvine posted a preprint called "The AI Era's Lines of Code?", which asks what an engineer's token spend actually measures. The authors are Shyam Agarwal, Olga Lvova, Agnia Sergeyuk, Anastasiia Serova, Timofey Bryksin, Thomas Zimmermann and Bogdan Vasilescu. Their answer, reached on one company's data, is that it measures how much a person works through agents, and says little about what that person produces. The paper has not been peer reviewed.

## A metric adopted before it was tested

Companies began using token spend as a management number before anyone had studied it, and the authors say so. They cite a leaderboard that a Meta employee built so that colleagues could compete to be the company's top token user; Fortune reported in April that it was taken down two days after the press wrote about it. They cite executives at Nvidia and Meta saying a good engineer should use tokens worth a large share of their salary, Salesforce setting minimum monthly spending targets, and analytics vendors that divide token cost by merged pull requests and call the ratio a return on investment.

Doubt has grown since. The paper reports that Uber spent its 2026 budget for AI coding tools in four months, and that its chief operating officer said the link between token spend and shipped features "is not there yet". A critic quoted in the paper called token spend "the lines-of-code metric of the AI era: easy to measure, easy to game, and disconnected from actual productivity." Meta has since told engineers that token counts will not be used to evaluate their impact, and Amazon shut down a usage leaderboard and called token usage a "deeply flawed" measure, according to the authors' account of press reports. The open question was whether the criticism held up when someone joined the usage logs to real output.

## What the telemetry shows

JetBrains, which builds software development tools and had about 2,600 employees at the time, runs an internal gateway that logs every coding-agent call. The researchers took the five complete weeks from 29 June to 2 August 2026 and matched each engineer's weekly tokens to that engineer's commits. The panel covers 404 engineers; the logs hold 3.1 million agent calls. A separate anonymous company survey drew 412 employees.

Within each band of weekly commit counts, the engineer-week at the 90th percentile of spend used between 39 and 240 times the tokens of the one at the 10th. Following the same person from week to week gave a flatter picture than the authors expected. A week with twice an engineer's usual commits cost about 20 percent more tokens. Run the other way, a week with twice the usual tokens came with only about 10 percent more commits. If output rose in proportion to spend, both figures would be close to 100 percent, and the authors reject proportionality at every time unit they tried.

Much of the variation sits with the person. Who the engineer was accounted for 79 percent of the variation in weekly tokens, and the heaviest third of users consumed 79 percent of all tokens. The people who spent the most stayed the same people across the five weeks. Commits, lines changed and two further activity measures together explained 38 percent of the differences between engineers and 13 percent of the week-to-week differences within one. Role and team, taken alone, predicted spend worse than simply using the average.

The paper then asks where the surplus goes. Weeks with no commit at all account for only 4 percent of tokens, but the authors estimate, from the best-fitting curves, that up to about two fifths of spend does not move with the week's commits. They call that an upper bound, since it includes the fixed cost of using an agent at all and the spend behind commits written by hand. They also note that most tokens are context re-sent on every turn, and that a new frontier model arrived in the third week and took 45 percent of all spend within two weeks.

## The work that never becomes a commit

The survey explains part of the gap. Of the technical respondents' 197 evaluations of the two coding agents, 167 answered the questions about the past week. In 91 percent of those, respondents said the tool had saved them time, a median of 10 hours. They used the agents for coding in 63 percent of evaluations and for at least one other activity in 89 percent: analysing data, brainstorming, researching a topic, planning, learning, writing. Respondents who used the agent only for coding reported a median of 3 hours saved; those who reported two or more non-coding uses reported 10.

Some of the value is work that would not otherwise exist. Asked about the agent's main benefit, 31 percent of 74 substantive answers named speed on usual tasks and 30 percent named work in unfamiliar code, domains or technologies; one respondent wrote, "I can try things that I was scared to try." Of 44 descriptions of work done only because the agent existed, 36 percent involved an unfamiliar codebase, language or stack. The survey also records costs. The most common was wrong or low-quality output, named in 49 percent of answers, and 31 percent of technical agent users reported higher cognitive load. The authors add that self-reports can overstate gains, and cite a 2025 randomised trial in which experienced open-source developers took 19 percent longer with AI tools while believing they were faster.

## What it means for targets, budgets and caps

The authors do not conclude that agents are a poor investment. Their conclusion concerns the measuring stick. If the within-engineer association were causal, doubling an engineer's spend through a target would raise commits by about 10 percent, with a range of 2 to 25 percent. They recommend against judging engineers by spend and against expecting targets to lift output much. Dividing spend by output misleads in its own way, because tokens per commit fall mechanically as commits rise, so an engineer looks more efficient in a busy week.

Caps get the least comfortable treatment. A cap bites mostly on the heaviest users, whose share of spend not tied to output is the lowest of the three groups at 36 percent, against 51 and 52 percent for the others. Because they spend most of the tokens, they also hold most of the untied spend, so a cap removes spend that serves output along with spend that does not, and the token count cannot say which is which. Before capping, the authors suggest compressing or managing context, caching repeated context and routing routine calls to cheaper models, and measuring billed cost rather than tokens, since trimming context can raise the bill when the agent re-reads what was removed.

Two limits matter. JetBrains builds AI coding tools, so some metered use may be testing of its own agents, and its engineers work on established codebases. Use was voluntary, with no target, so spending differences partly reflect personal choice. Commits also miss review and design work. The authors stress that these are associations from one company over five weeks.

A second study, from a partly overlapping set of authors, shows what happens when a target is imposed. Using 802 developers and 196,212 pull requests, it examines a mid-sized company whose chief technology officer set a goal in June 2025 of doubling merged pull requests per engineer with AI. The company reached the target only in the tenth month, and the cost fell on code review, where the load per reviewer doubled.

## Counting the right thing

The JetBrains authors propose two repairs. Gateways should record which issue or task each agent session served, so that spend can be joined to outcomes rather than only to commits. And the field needs validated measures of the value of agent-assisted work; the authors know of none. Until then, they say, spend suits resource accounting and little else. For adoption, they suggest reporting the weekly headcount of users beside a count that does not grow with context size, such as the share of engineers who use agents on most working days.

Back in the invented office, the head of platform engineering does not cut anyone's budget on Wednesday. She asks the gateway team to add one field, the ticket each session belongs to, and tells her finance partner that the confetti chart is the finding. The invoice will still arrive on the first of the month. What it counts is how often her engineers reach for the agent. Whether that was worth the money is a separate question, and the invoice has no line for it.

## References

- Agarwal, S., Lvova, O., Sergeyuk, A., Serova, A., Bryksin, T., Zimmermann, T., & Vasilescu, B. (2026). *The AI Era's Lines of Code? A Case Study on What an Engineer's Token Spend Measures*. https://arxiv.org/abs/2611.13396
- Arar, A. B. (2026). *Tokenmaxxing and the search for AI metrics that matter*. LeadDev. https://leaddev.com/ai/tokenmaxxing-and-the-search-for-ai-metrics-that-matter
- Becker, J., Rush, N., Barnes, E., & Rein, D. (2025). *Measuring the impact of early-2025 AI on experienced open-source developer productivity*. https://arxiv.org/abs/2507.09089
- Bharade, A. (2026). *Uber's COO says it's getting harder to justify the money spent on AI tokenmaxxing*. Business Insider, via Yahoo Finance. https://finance.yahoo.com/sectors/technology/articles/ubers-coo-says-getting-harder-050841491.html
- Cooter, M. (2026). *Meta minimizes role of token maxing in employee evaluations*. CIO. https://www.cio.com/article/4218661/meta-minimizes-role-of-token-maxing-in-employee-evaluations-2.html
- He, H., Agarwal, S., Denisov-Blanch, Y., Azaletskiy, P., Koyejo, S., & Vasilescu, B. (2026). *AI Writes Faster Than Humans Can Review: A Longitudinal Study of an Enterprise 2x Mandate*. https://arxiv.org/abs/2607.01904
- Munis, J. (2026). *A Meta employee created a dashboard so coworkers can compete to be the company's No. 1 AI token user*. Fortune. https://fortune.com/2026/04/09/meta-killed-employee-ai-token-dashboard/
- Palmer, A. (2026). *Amazon's anti-tokenmaxxing memo says engineers should be pickier about using AI*. CNBC. https://www.cnbc.com/2026/10/27/amazon-ai-coding-tokenmaxxing.html
