+++
title = "Firms most exposed to AI agents post fewer junior jobs"
description = "A new economics preprint links two quadrillion tokens of real AI use to 34.8 million job postings and finds that listed firms most exposed to agents later advertised fewer jobs, mainly non-senior ones. It measures postings, not layoffs, and it infers exposure from stock prices."
tags = ["research", "agents", "business"]
date = 2026-11-24T03:11:30+01:00
draft = false
+++
On a Monday morning in the autumn of 2025, a talent lead at a regional health-services company opens the dashboard of requisitions. She has done this every week for six years. Three analyst roles that once reopened as soon as someone was promoted sit closed. The senior roles, for people who already know how the company works, are open as always. Nobody has told her to stop hiring juniors. The numbers simply stop being asked for.

*The scenes that open and close this article are illustrations; the people in them are invented.*

Whether that pattern holds across companies is the question of a working paper posted to arXiv on 20 November 2026. Nicola Borri of Luiss University, Anton Cheremukhin of the Federal Reserve Bank of Dallas, Yukun Liu of the University of Rochester and Aleh Tsyvinski of Yale and the National Bureau of Economic Research ask whether firms more exposed to AI agents have since advertised fewer jobs. Their answer is yes, and the cut falls mainly on non-senior jobs. The authors state that their views are not those of the Dallas Fed or the Federal Reserve System, and the paper has not been peer reviewed.

## Counting agents through tokens

The authors say earlier evidence came from single companies: Perplexity, OpenAI's Codex, Anthropic's Claude Code, and Anthropic's own report on employment inside the company. Their data are wider. OpenRouter, a service that routes requests to hundreds of models, gave them anonymised records of about two quadrillion tokens of paid use across more than 400 models. That is roughly 2 percent of global token consumption.

They define an agentic token as one that belongs to a response ending in a call to an external tool, such as a database query, a code run or a file write. By that definition 1.1 quadrillion of the tokens are agentic. From June to September 2025 the agentic share of OpenRouter traffic stayed between 8.2 and 8.7 percent. Anthropic released Claude Code 2.0 on 29 September 2025. The share then rose every month, to 21.5 percent in December 2025 and 76.8 percent in the first 27 days of September 2026, when agents accounted for most of the tokens on the platform.

## Exposure inferred from stock prices

A firm does not report how much of the agent wave it is exposed to, so the authors infer it. For each listed US company they measure how its stock return moves with the weekly growth of agentic tokens, a quantity they call the agentic beta. A high beta marks a firm whose market value rises and falls with agent usage. They check the measure against what firms later say: a one-standard-deviation higher beta goes with a 1.39 percentage point higher chance of mentioning AI agents in an SEC filing over the next six months, and 1.46 points for an earnings call.

The labour side comes from Lightcast, which collects postings from company career pages and job boards. The authors matched 34.8 million postings, about 18 percent of Lightcast's total, to 1,784 listed parent companies.

## What the postings show

A firm one standard deviation higher in agentic beta posted 2.11 percent less growth in jobs over the next six months and 3.20 percent less over nine. A skeptic would say that firms whose prospects were already dimming could have been the ones the market tied to agents. To meet that, the authors run an event study around the Claude Code 2.0 release. They fix each firm's beta at its September 2025 value and compare growth after the release. They find no relation between exposure and posting growth before it. After it, firms with higher exposure grew postings more slowly in every month from October 2025, and the six-month figure was 4.73 percent lower per standard deviation. This rests on an assumption the authors state: that without the release, high-exposure and low-exposure firms would have grown alike once industry and firm traits are accounted for.

The drop sits in the lower ranks. For senior positions, and for jobs asking six or more years of experience, the estimates are statistically insignificant. For non-senior jobs and for jobs asking less than six years, they are negative and significant at the 5 percent level, as are the gaps between the groups. Postings that expect workers to use AI tools responded little, while postings without that expectation fell. Advertised wages did not fall. Broad AI use told a different story: once agentic exposure is controlled for, a firm's exposure to total AI token use has no significant link to later postings. The effect also shows up with exposure measured through closed-weight frontier models, and much less with open-weight ones.

The negative sign appeared in all five Fama-French industry groups, and the Health group had the largest estimate. Occupation-level exposure scores, including the ones from Eloundou and colleagues, Webb, and Anthropic's own Economic Index, had limited power to predict which firms would post less once firm traits were included.

## Where it stops

The paper measures advertising, not employment. A firm can post less and fire nobody; it can also fill jobs without posting them. The sample is listed US companies, and exposure rests on stock-return co-movement and on a 2 percent slice of global tokens. The paper shows that exposure predicts lower posting growth; it does not show what any single firm decided.

Its direction matches other work from this year, on different data. Anthropic's economists reported in October that junior technical hires at their own company fell from 27 percent to 9 percent of hires, while the share of junior employees in its technical departments fell from 21 to 14 percent since early 2025. Stanford researchers using ADP payroll records through June 2026 found no sign of widespread job displacement, but employment of workers aged 22 to 25 in AI-exposed occupations stood 19 percent below where it would have been had it kept pace with less-exposed peers, with no comparable gap for experienced workers. The three sources are one company, one payroll sample and one set of postings, and the pattern they share is a thinner bottom rung.

Back at her dashboard a year later, the talent lead has filled two of the senior roles. The analyst requisitions are still closed, and nobody has asked her to reopen them.

## References

- Borri, N., Cheremukhin, A., Liu, Y., & Tsyvinski, A. (2026). *The Rise of Agents and the Labor Market*. arXiv:2611.27210. https://arxiv.org/abs/2611.27210
- Brynjolfsson, E., Chandar, B., & Chen, R. (2026, revised 12 August). *Canaries in the Coal Mine? Six Facts about the Recent Employment Effects of Artificial Intelligence*. Stanford Digital Economy Lab. https://digitaleconomy.stanford.edu/publications/canaries-in-the-coal-mine/
- Wilmers, N., Catipon, R., Massenkoff, M., & McCrory, P. (2026). *How employment is changing at Anthropic*. The Anthropic Institute. https://www.anthropic.com/research/employment-at-anthropic
