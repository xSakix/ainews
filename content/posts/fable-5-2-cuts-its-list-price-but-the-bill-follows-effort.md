+++
title = "Fable 5.2 cuts its list price, but the bill follows effort"
description = "Anthropic lowered the price of Claude Fable 5.2 by a fifth, yet an independent index measured the highest cost per task of 73 models at maximum effort. The gap comes down to how many tokens the model spends, and Anthropic's own charts say the effort setting decides it."
tags = ["models", "business"]
date = 2026-11-10T03:25:07+01:00
draft = false
+++

This Monday is made up, assembled from launch documents and not from anyone's diary. A platform lead at a mid-sized software company reads that Anthropic has cut the price of its top model by a fifth. She does what the announcement invites. She changes the model name in her team's agent configuration, sets the effort parameter to its highest value and leaves forty repository audits running overnight. By morning the batch has finished, and the only thing she wants to open is the invoice. It does not look like the headline she read.

The headline was accurate. On 9 November Anthropic released Claude Fable 5.2 and its twin, Claude Mythos 5.2, at $8 per million input tokens and $40 per million output tokens, down from $10 and $50 for the 5.1 versions. The independent number that arrived the same day is also accurate. Artificial Analysis, which publishes a cross-vendor intelligence index, ran Fable 5.2 at its maximum setting and put it first of 74 models on intelligence, with a score of 65, and 73rd of 73 on cost, at $26.54 per index task. The two figures describe one model. What separates them is how many tokens it spends.

## What the price sheet says

Anthropic's documentation lists the new rates plainly. Cache reads cost $0.20 per million tokens, batch processing is half the base price, and an optional fast mode that generates up to 2.5 times faster costs $16 for input and $80 for output. The company also says the model produces output up to 30% faster than Fable 5.1. TechCrunch notes that Fable is now cheaper than its main rival, and Fortune puts Fable 5.2 20% under OpenAI's GPT-6 Astra, which lists at $10 and $50, with cached input at 20 cents against Astra's one dollar.

Mythos 5.2 carries the same price. Anthropic calls the two models the same underlying model; Fable ships with cyber and biology safeguards and is open to every customer, while Mythos goes to organisations accepted into the company's Cyber Verification and Life Sciences Verification Programs. The price is shared. The access is not.

## What the index measured

Artificial Analysis computes cost per task from input, cache-hit, cache-write, reasoning and answer-token prices, divided by the number of tasks and weighted across the nine evaluations in its index. On that basis Fable 5.2 at maximum effort generated 275 million output tokens, where the median for comparable models is 72.8 million. It took 46.4 minutes per task, against a median of 12.7, and 216 seconds to the first answer token. The site's own summary calls the model "particularly expensive" and "very verbose".

The arithmetic is short. The listed output price is $40 against a median of $10, four times as much, and the token count is about 3.8 times the median. A bill is price multiplied by volume, and Fable 5.2 sits high on both at this setting. The limits are worth stating: these are Artificial Analysis's tasks, not the reader's, and the figure belongs to one effort level.

## The dial Anthropic points to

Anthropic does not dispute that effort matters. Its launch page says the default in Claude apps and Claude Code is Medium, and that at Medium Fable 5.2 completes hard tasks with fewer tokens than 5.1. In early testing on FrontierCode 2.0, a benchmark of whether a model's code changes would be merged by open-source maintainers, Fable 5.2 at High effort scored 45.3% against 45.5% for Opus 5.5 at Max, for roughly half the cost per task. On Perplexity's WANDR data-collection benchmark, Medium effort matches Opus 5.5's best score for about 40% of the cost. On Humanity's Last Exam, Low effort does so for less than a tenth. At Xhigh effort the model reaches 49.1% on FrontierCode, the highest score of any released model Anthropic tested.

All of these are the vendor's charts from early testing. They show that the same model sits at very different points on a cost curve depending on one parameter, which is the reading the independent number also supports. The documentation is blunt about where Fable belongs: for most workloads, start with the latest Opus model, and move to Fable when evals on Opus at higher effort still fail to "meet your requirements".

## How the bill got here

Anthropic has framed pricing this way before. Its Claude Opus 5.5 announcement of 22 September said the model performs at the level of Fable 5.1 on most work and costs 40% less than Opus 5 on typical workloads. The per-token price was 20% lower, at $4 and $20 per million, and the company said the rest of the saving came from using fewer tokens per task. A bill, in Anthropic's own account, is a rate times a count.

Gergely Orosz, who writes The Pragmatic Engineer, gave the effect some texture in an issue of 20 October. He spoke to people at 27 workplaces about AI spending per developer, a self-selected sample, mostly anonymous. He reports that spending peaked in June and July and has roughly halved for companies on API plans, with a mix of Opus 5.5 and open models given as the reason at most of them. One engineer spent $2,200 in September on Opus 5 and expects half that with Opus 5.5. Orosz also heard that several firms' subsidised subscriptions are ending, which could raise their bills five to ten times.

Fable 5.2 arrives into that arithmetic. A buyer who moved to Opus 5.5 to halve the invoice now has a higher tier whose per-token price fell and whose per-task cost depends on a setting most people do not touch.

## Launch offers and who pays for the trial

For the first week, the price does not bite for subscribers. Anthropic's help centre says Pro plans and standard Team seats get all Fable models included in their weekly limits from 9 to 16 November, up to 50% of those limits, plus one limit reset. Max and Ultra plans get one to three resets, depending on how long the account has been paid, and unused resets lapse on 8 March 2027. The offers are written for subscription plans, and the page says nothing of API accounts.

## The invoice, again

Back in the made-up Monday, the lead looks at the audit batch and sees nothing wrong with the findings. What she lacks is a comparison. The next test she writes is dull: the same forty repositories at High effort, then at Medium, with the cost and the number of accepted findings beside each. Whether the cheaper runs find enough is a question no launch page can settle for her team, and the documentation she read says as much. The model is priced by the million tokens. Her review will be priced by the repository.

## References

- Anthropic (2026). *Introducing Claude Fable 5.2 and Claude Mythos 5.2*. https://www.anthropic.com/claude-fable-and-mythos-5-2
- Anthropic (2026). *Introducing Claude Opus 5.5*. https://www.anthropic.com/news/claude-opus-5-5
- Anthropic (2026). *Claude Fable 5.2 launch offers*. Claude Help Center. https://support.claude.com/en/articles/17506494-claude-fable-5-2-launch-offers
- Anthropic (2026). *What's new in Claude Fable 5.2*. Claude Platform Docs. https://platform.claude.com/docs/en/models/fable-5-2/whats-new-fable-5-2
- Artificial Analysis (2026). *Claude Fable 5.2 (Max): Intelligence, Performance & Price Analysis*. https://artificialanalysis.ai/models/claude-fable-5-2
- Brandom, R. (2026). *Anthropic releases new Mythos and Fable models amid RSI concerns*. TechCrunch. https://techcrunch.com/2026/11/09/anthropic-releases-new-mythos-and-fable-models-amid-rsi-concerns/
- Forlini, E. (2026). *Anthropic debuts Claude Fable, Mythos 5.2 models, priced 20% below OpenAI's GPT-6 Astra*. Fortune. https://fortune.com/2026/11/09/anthropic-debuts-updated-claude-fable-and-mythos-models-undercutting-price-of-openais-gpt-6-astra-by-up-to-80/
- Orosz, G. (2026). *What's the ROI of software engineers' spending on AI?* The Pragmatic Engineer. https://newsletter.pragmaticengineer.com/p/whats-the-roi-of-software-engineers
