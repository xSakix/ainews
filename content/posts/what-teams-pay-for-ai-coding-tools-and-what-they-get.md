+++
title = "What teams pay for AI coding tools, and what they get"
description = "Gergely Orosz asked 27 engineering workplaces what they spend on AI per developer. The answers run from under $300 to $3,000 a month, and output rose in some places and barely moved in others. The subsidies behind many bills are ending as 2027 budgets are set."
tags = ["business", "tools"]
date = 2026-10-23T03:21:44+02:00
draft = false
+++

The person in this paragraph is a composite, put together from the kinds of answers a survey of engineering teams produced. Call her the finance partner for a software division, and give her a Tuesday in late October with a blank column in a spreadsheet headed "AI tooling, 2027". Her engineering director has told her that the bills have been rising all year. She has the invoices from three vendors, a Slack message saying that some people use a company card, and a question she cannot answer from any of them: how much is normal? She types a figure into the first cell, deletes it, and types a lower one.

Gergely Orosz, who writes The Pragmatic Engineer, received nearly that question from a reader and went looking for an answer. In an issue published on 20 October he reports talking to engineering leaders and senior engineers at 27 workplaces, and collecting aggregate figures from two vendors of code-review tools, CodeRabbit and Gitar. The sample is self-selected and most companies are anonymous. It is not a controlled study. It is, for now, one of the few places where real numbers sit next to each other.

## The spread is wide, and size does not explain it

Orosz's first finding is that company size and spend are unrelated. A two-person .NET agency in Europe, Ix Technologies, spends $3,000 per developer per month, mostly on Claude Opus and GitHub Copilot. A publicly traded company with 1,500 engineers limits each developer to $150.

Between them sit caps. Orosz writes that caps are normal at medium and high spenders, with extra spend needing a justification, and that most people say the caps are easily avoided. A hospitality company with about 200 engineers defaults to $1,500 a month. A publicly traded SaaS company with about 600 engineers budgets $1,200, though a staff engineer there says fewer than 5% of developers reach it. An AI software company of about 100 staff gives $2,000 and runs a public Slack channel that names people nearing their limit. Its engineers describe the cap as a hard one, since an increase requires running a diagnostic skill that hunts for wasted loops and then asking a manager.

The steepest curve belongs to a quant trading firm with about 2,000 developers. Its monthly AI spend rose from $500,000 in January to $8 million in September, or $1,600 per developer, up from about $80. The biggest spenders are not developers but traders, and an engineer there says the firm is learning "the importance of rate limiting for traders who accidentally run expensive queries without realizing it." It sets a limit of $25,000 per employee. Its logic is that trading profits can absorb the cost, and a desk that makes more money is not asked to justify its tooling.

## Output rose in places, and barely moved in others

Orosz chose pull-request throughput as the measure because most companies already have it and developers have not yet learned to game it. The vendor data point up. CodeRabbit sees weekly pull requests per developer 113% higher than a year ago, and a fixed group of 20,000 developers shows a 128% rise. Gitar reports that teams it classes as AI-native ship more than 60 pull requests per developer per week.

The company accounts are more mixed. The Ix cofounder says they went from one or two pull requests a day to ten or more, and that two people now do work that would have taken five to seven. A multinational team lead counts 1.5 pull requests per developer per week in January and about 4 now, though he warns that one engineer's jump skews the average. That team also closes three times as many user stories a month as last year. At a company of 5,000 employees, by contrast, the number of pull requests is flat and each carries three times as many lines of code.

The SaaS engineer with the $1,200 budget describes the most careful picture. The volume of pull requests is up, but the velocity of merged ones has not changed much, because human reviewers still catch changes that are not needed or are ten times bigger than they should be. Triage of customer issues, which once took a day, now takes minutes plus up to an hour of checking. Research into why code was written a certain way and proof-of-concept prototypes also shrank from days to hours. "When the team cares about the quality in production code and wants to keep it like before AI," the engineer says, "then actual development speed had not increased much."

## Bills have fallen, for now

Two other findings bear on the spreadsheet. Spend peaked in June and July and has roughly halved for companies on API plans, which Orosz attributes to a mix of Opus 5.5 and a move to open models. A hospitality engineer who spent $2,200 in September on Opus 5 expects to halve it with the newer model.

The second finding cuts the other way. Several companies told Orosz their subsidised subscriptions are ending, and that they must either optimise costs or see bills rise five to ten times. Few can say what they get for the money. The article's own summary is that return on investment is a question few companies seem able to answer.

## The pattern of the past three weeks

The same pressure shows in other sources. On 3 October the developer Simon Willison argued that usage-priced services need hard spending caps by default, because coding agents make it easy to launch things that bill by the hour. He noted that AWS had begun releasing a spend limit that pauses a project for the month, and that Google Cloud had launched Spend Caps in July.

On 21 October the analyst firm Forrester published its predictions. It expects AI to take 20% of business technology spend next year. Only 22% of AI decision-makers report a positive effect on EBITDA over the past twelve months, and Forrester expects more than half of CIOs to miss their AI return targets in 2027. It also predicts that open-weight models will carry half of enterprise AI tokens but account for only 5% of spend. The same day, Peter Steinberger of OpenAI told a conference audience that he had spent around $10 million in tokens the previous month, adding: "not all of that is useful." The Register reports that the bill came out of investors' pockets.

On 22 October IBM's chief executive, Arvind Krishna, gave the buyer's side of the argument on an earnings call. He said open-weight models cost "anywhere from 25 percent to 10 percent of the token cost of the frontier models" and are "90 percent as effective", and that most businesses can run them in two or three racks. IBM sells hardware and software for exactly that, so the claim comes from a seller. His own caveat is that companies often lack the kernel, network and caching engineers to make it work.

## What a single number would hide

Taken together, the sources give the finance partner no figure she can type with confidence, and they explain why. The firm that spends $1,600 per developer measures return in trading profit. The one that spends $150 per developer may be doing the same work with a cheaper model or a different habit. Pull requests, the metric Orosz chose, rise sharply in the vendors' aggregate and stay flat at a team whose reviewers insist on the old standard. Each company is counting something different as worth paying for.

Back in her spreadsheet, the finance partner leaves the cell as a range and adds a second column she did not plan: the date each subscription's introductory price ends. Then she writes a question for the engineering director, and it is not about price. It asks which of last quarter's merged changes would not have existed without the tools, and who decided they were wanted.

## References

- Forrester (2026). *AI will eat a fifth of tech budgets in 2027, but don't expect it to pay for itself* (reported by The Register). https://www.theregister.com/ai-and-ml/2026/10/21/ai-will-eat-a-fifth-of-tech-budgets-in-2027-but-dont-expect-it-to-pay-for-itself/5304466
- Orosz, G. (2026). *What's the ROI of software engineers' spending on AI?* The Pragmatic Engineer. https://newsletter.pragmaticengineer.com/p/whats-the-roi-of-software-engineers
- Sharwood, S. (2026). *IBM CEO says open weight models are now irresistibly good and cheap on-prem*. The Register. https://www.theregister.com/systems/2026/10/22/ibm-ceo-says-open-weight-models-are-now-irresistibly-good-and-cheap-on-prem/5304640
- The Register (2026). *OpenClaw creator says he spent $10 million in tokens last month*. https://www.theregister.com/ai-and-ml/2026/10/21/openclaw-creator-says-he-spent-10-million-in-tokens-last-month/5304573
- Willison, S. (2026). *We're going to need default hard budget caps on pretty much everything*. https://simonwillison.net/2026/Oct/3/default-hard-budget-caps/
