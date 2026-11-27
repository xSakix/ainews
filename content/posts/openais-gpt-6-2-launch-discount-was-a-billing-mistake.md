+++
title = "OpenAI's GPT-6.2 launch discount was a billing mistake"
description = "OpenAI says it incorrectly discounted plan usage of GPT-6.2 Astra and Sol for nine days, so subscribers now reach their limits 40 and 25 percent faster. The correction lands beside an independent measurement that the models reason less, and shows how little of a flat-rate plan can be checked from the outside."
tags = ["business", "tools"]
date = 2026-11-27T03:17:17+01:00
draft = false
+++

Under a post from an OpenAI engineer, a Hacker News thread filled with people reading their usage meters. A commenter who goes by seviu wrote that "yesterday evening I had close to 90% quota left, and today I woke up to find it all gone." He was on the Pro plan and had not left an agent running overnight. Another, ragequittah, remembered the week before in the opposite terms: "6 hours of Astra would be 3%."

Between those two readings sits the post itself, and a change in how a flat-rate plan counts a day of work.

## The correction

At 02:50 UTC on 26 November, Thibault Sottiaux, who works on Codex and ChatGPT at OpenAI, wrote on X: "We made a billing mistake at launch of GPT-6.2 that incorrectly discounted GPT-6.2 Astra and Sol usage for most users." The fix, he said, means that "the same work will use more of your plan’s usage allowance". Compared with the week before, subscribers "will reach your limits 40% faster on GPT-6.2 Astra and 25% faster on Sol." He added that the models should still go further than GPT-6 Astra and GPT-6.1 Sol, that other models were not affected, and that OpenAI would not charge for the difference on past usage. As an apology, everyone on Go, Plus, Pro and Business would get one banked reset.

The numbers need translating. If an allowance drains 40 percent faster, a subscriber gets about 29 percent fewer tasks out of it, since one divided by 1.4 is 0.71. A 25 percent faster drain means 20 percent fewer. That is arithmetic on OpenAI's wording, and the company has not published the underlying rate.

The launch was nine days old. OpenAI introduced GPT-6.2 Astra and Sol on 17 November, the date GitHub gave when it added them to Copilot. The announcement sold the pair partly on economy: both models "deliver better results on demanding tasks with fewer output tokens, so you can get more done within your usage limits", and Sol "lets you complete more tasks on the same paid plan." In the API, Astra's token prices were cut 20 percent, to $8 per million input tokens and $40 per million output tokens, the same list price Anthropic had set for Claude Fable 5.2 on 9 November. Sol kept GPT-6.1 Sol's $2 and $10.

The API prices are not what changed. A paid ChatGPT plan is billed in a different currency, a share of an allowance, and the rate at which a task consumes it is set inside OpenAI. OpenAI's pricing page, read on 27 November, lists credits per million tokens: 200 for Astra input and 1,000 for output, a fifth below GPT-6 Astra's 250 and 1,250, and unchanged 50 and 250 for Sol. It also gives Plus subscribers an estimate of 6 to 50 local Codex messages per five-hour window on GPT-6.2 Astra, and 17 to 180 on Sol, against 5 to 45 for GPT-6 Astra and 15 to 160 for GPT-6.1 Sol. The page calls these estimates "not fixed message limits". It says that "Pro plans currently have no five-hour limit" and that weekly limits may also apply.

A range of 6 to 50 cannot confirm or refute a 40 percent claim, and the page does not say whether its table was updated after the correction. The overnight loss that seviu describes is one account, unconfirmed, and could have come from the change or from a weekly cap.

## What the thread argued about

The post, quoted in a headline as a usage cut, drew 468 points on Hacker News. Readers split on what it meant. Some took the "billing mistake" at face value. One commenter wrote that they had spent hours on Astra 6.2 and still seen 100 percent on the meter, and went looking for a broken widget. Others read the correction as a price rise delivered through a bug fix, and some said they had cancelled or were weighing Anthropic and Google. Another noted that the email OpenAI first sent was short, and a follow-up had to explain it. Every one of these is a user's account, not a measurement.

The thread also carried a memory of a back-and-forth. One long-time user of both OpenAI and Anthropic accounts said that OpenAI's allowances had felt limitless, with a constant flow of resets, that Opus 5.5 then gave more usage, and that OpenAI responded by reducing its allowances. A different commenter replied that the balance between the two vendors had alternated since the category began and would do so again. Both accounts are recollection, and neither is a record of what any plan delivered.

## A second reading of the same models

On 26 November, a few hours after Sottiaux's post, the developer behind Agent Duel, a head-to-head evaluation, published a post titled "OpenAI may be in cost control mode". Agent Duel is built on the coding agent OpenCode; it pits models against each other on real work and ranks them with Elo scores. Its author reports that against opponents in the same battles, Astra 6.2 and Sol 6.2 spent fewer output tokens and fewer reasoning tokens per task than their predecessors. The p-values he gives for output tokens are 0.0055 for Sol and 0.022 for Astra; for reasoning tokens, 0.00013 for Sol and 0.0064 for Astra. His conclusion is that the models "appear to be cost tuned", to the point of being "underthinking outliers".

The word "cost" belongs to the author. The data show less reasoning, not why. OpenAI's launch post lists fewer output tokens as a feature, and says Astra gained 6.2 points on its internal GDPval v2 benchmark while using 22 percent fewer output tokens than GPT-6 Astra. The same measurement can support an efficiency story or a savings story, and only OpenAI knows which it is. Nor does a lower token count explain the billing error, which concerned how tokens are charged against an allowance.

The leaderboard itself, generated at 03:00 UTC on 27 November, is not decisive either. GPT-6.2 Astra sits fifth with an Elo of 1007 and an interval of plus or minus 61, at $2.33 per task and 2.6 minutes; Sol is twelfth at 937, $0.43 and 1.7 minutes. Claude Fable 5.2 leads at 1069 and $3.49, and Claude Opus 5.5 follows at 1060 and $1.63. The intervals overlap widely, and Astra's plausible rank runs from second to eleventh.

## What a subscriber can check

Price and bill have parted before. On 9 November Anthropic cut Fable 5.2 to $8 and $40 per million tokens, a fifth below its predecessor, and Artificial Analysis still lists the model last on cost among the models it ranks, at $26.54 per task on its Intelligence Index, because the bill follows the tokens a model chooses to spend. The OpenAI episode adds a layer. For a subscriber, the tokens a model spends, the rate at which they are charged against an allowance and the size of the allowance are three numbers the vendor sets, and one of them, the charging rate, is what OpenAI says it got wrong during the first nine days.

Outsiders can measure the first, as Agent Duel did. The other two they can only read off a meter. The pricing page offers one sentence to a person looking at an empty one: "Tasks that look similar can consume different amounts of your allowance."

## References

- Agent Duel (2026). *Agent Duel Leaderboard*, generated 27 November 2026. https://agentduel.com/leaderboard
- Anthropic (2026). *Introducing Claude Fable 5.2 and Claude Mythos 5.2*. https://www.anthropic.com/claude-fable-and-mythos-5-2
- Artificial Analysis (2026). *Claude Fable 5.2 (Max): Intelligence, Performance & Price Analysis*. https://artificialanalysis.ai/models/claude-fable-5-2
- GitHub (2026). *OpenAI's GPT-6.2 Astra and GPT-6.2 Sol now available*. GitHub Changelog, 17 November. https://github.blog/changelog/2026-11-17-openais-gpt-6-2-astra-and-gpt-6-2-sol-now-available
- Hacker News (2026). *OpenAI cuts GPT-6.2 usage: Astra hits limits 40% faster, Sol 25% faster*. https://news.ycombinator.com/item?id=50651117
- micjm (2026). *OpenAI may be in cost control mode*. https://micjm.com/blog/openai-is-in-cost-control-mode/
- OpenAI (2026). *Introducing GPT-6.2 Astra and Sol*. https://openai.com/index/introducing-gpt-6-2-astra-sol
- OpenAI (2026). *Pricing*. ChatGPT Learn. https://learn.chatgpt.com/docs/pricing
- Sottiaux, T. (2026). Post on X about the GPT-6.2 billing mistake, 26 November. https://x.com/thsottiaux/status/2125784147889393806
