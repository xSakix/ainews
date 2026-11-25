+++
title = "Study finds Copilot adoption cut junior coding hires"
description = "A preprint following 5,414 large firms reports that Copilot adoption lowered quarterly technical hiring by 29 percent at firms pushed to adopt by their contract review, with junior coding roles hit hardest and no rise in layoffs. It covers 2023 to mid-2025, firms and not the whole market, and has not been peer reviewed."
tags = ["business", "research", "tools"]
date = 2026-11-25T03:12:29+01:00
draft = false
+++
In the autumn of 2023, the director of platform engineering at a large insurer sits through the renewal meeting for the company's GitHub contract. The legal, security and finance people are already on the call, because the meeting was set years ago and happens every year. The account representative has added a line to the order sheet for Copilot, the coding assistant. Nobody has to open a separate purchase request, wait in a queue for a security review or find a budget code. The director looks at her hiring plan for the next four quarters, which still has seven graduate positions on it, and tells the finance lead to approve the line.

*The scenes that open and close this article are illustrations; the people in them are invented.*

What happened to plans like hers is the subject of a preprint posted to arXiv on 23 November 2026. Lindsey Raymond of MIT and Eleanor Dillon of Microsoft Research followed 5,414 large companies, which together employ 45 million people and account for 38 percent of the US programming workforce. Copilot adoption, they report, reduced quarterly technical hiring by 29 percent at the firms that adopted because their review came up. Hiring of junior software engineers fell by about 40 percent. The paper has not been peer reviewed, and the authors state that their views are their own and not those of their employers.

## Why the meeting is the experiment

Firms that adopt a coding assistant early are not like firms that adopt it late. In this sample they were already hiring more before Copilot launched, and they were larger, more technical and had older workforces. Comparing adopters with non-adopters would therefore mix the effect of the tool with the character of the firm.

The authors use the renewal meeting to separate the two. All the firms already bought GitHub's enterprise product and met its sales staff on a fixed schedule set before Copilot existed. Before the launch, the share of firms that raised their licence counts rose from about 10 percent to about 40 percent in the two months around a review, which shows how strongly purchases cluster at these meetings. After Copilot's enterprise launch in January 2023, a firm whose scheduled review came earlier was more likely to adopt earlier. One year after the review, those firms were 20 percentage points more likely to have adopted than firms whose review had not yet come.

The authors then compare hiring at firms that had reached their review with hiring at firms that had not. Reviews before the launch had no effect on technical hiring, and reviews after it had none on hiring of non-technical professionals such as accountants. Those two checks speak to the objection that the meetings coincide with budget cycles or hiring freezes. Their data come from Revelio Labs, which builds employment histories from public professional profiles and job postings, and from GitHub's own records of who adopted Copilot and when.

## What changed at the firms that adopted

At firms that reached their review, monthly technical hiring was 7.6 percent lower than at firms that had not. Scaled to the firms that adopted because of the review, the authors estimate a 29 percent drop in quarterly technical hiring. Against a baseline of roughly 55 technical hires per firm per quarter, that means about 39. The average firm in the sample has 8,284 employees, so the change amounts to less than 0.2 percent of headcount per quarter.

Nobody was let go. Separations did not change, and neither did total technical headcount over the first year. Open technical postings fell by 14 percent, while the time a posting stayed open did not change, which the authors read as firms opening fewer positions and not struggling to fill them.

The fall was not spread evenly. Using pre-2023 job descriptions, the authors scored how much of each role is coding. Junior hiring dropped in the roles with the most coding, and the effect at the other end of the scale was zero: hiring of experienced software engineers and of systems and infrastructure engineers did not move. Before Copilot, 72 percent of junior technical hires went into code-heavy roles, and the authors estimate that adoption lowers this to 52 percent. Experienced hires kept their numbers but changed in kind. New experienced software engineers had about 1.3 more years of potential experience and were 4.7 percentage points more likely to hold a master's or doctorate, and external hiring into those roles fell by about 13 percent while internal fills held. The authors also looked for work moving to India, the main offshore hub, and found none; if anything, hiring there slowed more.

The result runs against a finding the authors cite from experiments, where novices gain the most from AI help on individual tasks. A bigger gain for the person did not mean more demand for the person's position.

## How much of the slump is Copilot

Technical hiring was falling before any of this reached the sample. Average quarterly technical hires across the firms dropped 29 percent from 2022 to 2024, from 55.3 to 39.2. That the figure equals the treatment effect is a coincidence of the numbers, and the two should not be confused. At firms that never adopted Copilot, the monthly hiring rate fell from 2.7 to 1.8 percent over the same three years.

The authors attribute part of the slump to the tool and give three estimates that depend on what one assumes. If the review effect applies to every firm, Copilot accounts for 10 percent of the decline. If it applies only to firms like the compliers, 19 percent. If every adopter, roughly half the sample by 2024, reacted as the compliers did, 51 percent. They call these illustrative, and they say the design cannot tell which factors produced the rest, naming monetary tightening, the correction of pandemic-era overhiring and changes in the tax treatment of software research.

They add a warning about other studies. Comparisons across occupations that differ in AI exposure, they argue, pick up a downturn in technical work generally, which by their estimate explains at least half of the post-2022 drop.

## Where the study stops

The estimates describe firms, not the labour market. A candidate not hired by an insurer may be hired by a smaller company, and a firm that expands at a rival's expense may flatter the result. The window is the first year after each review, between 2023 and mid-2025, when Copilot was the dominant enterprise assistant and before the enterprise versions of Cursor and Claude Code appeared. The firms are big, old and mostly American or European, and the 29 percent is the effect on firms induced to adopt by their review, not on every adopter.

It joins a thread that has run through recent weeks. A preprint of 20 November by Borri, Cheremukhin, Liu and Tsyvinski linked firms' exposure to agent use to fewer non-senior postings, measuring postings and not hires. A Stanford study of ADP payroll data, revised on 12 August, found employment of 22- to 25-year-olds in AI-exposed jobs 19 percent below trend, with no such gap for older workers. Indeed's hiring snapshot of 24 November puts its software development index at 82, against 100 in February 2020. Those sources use postings, payroll and keyword counts. This one adds the adoption record and a reason for the timing, which is what lets it speak of cause.

Back at the insurer, a year on, the director opens the same plan. The seven graduate positions have become three. In their place stands one opening for someone with five years behind them, and the person who fills it holds a master's degree.

## References

- Borri, N., Cheremukhin, A., Liu, Y., & Tsyvinski, A. (2026). *The Rise of Agents and the Labor Market*. arXiv:2611.27210. https://arxiv.org/abs/2611.27210
- Brynjolfsson, E., Chandar, B., & Chen, R. (2026). *Canaries in the Coal Mine? Six Facts about the Recent Employment Effects of Artificial Intelligence*. Stanford Digital Economy Lab. https://digitaleconomy.stanford.edu/publications/canaries-in-the-coal-mine/
- Indeed Hiring Lab (2026). *US Labor Market Snapshot, November 2026*. https://hiringlab.indeed.com/2026/11/24/us-labor-market-snapshot-november-2026/
- Raymond, L., & Dillon, E. (2026). *AI-Assisted Programming and Labor Demand*. arXiv:2611.31083. https://arxiv.org/abs/2611.31083
