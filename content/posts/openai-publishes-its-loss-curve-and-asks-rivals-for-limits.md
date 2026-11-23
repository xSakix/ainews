+++
title = "OpenAI publishes its loss curve and asks rivals for shared limits"
description = "OpenAI's chief scientist has released the company's internal pretraining loss figures for the first time and proposed that labs agree not to cross set limits until oversight tools catch up. The metric he picked is measured on OpenAI's own code and does not compare cleanly between labs, which is where the first objections landed."
tags = ["policy", "safety", "research"]
date = 2026-11-23T03:14:57+01:00
draft = false
+++

Jakub Pachocki, OpenAI's chief scientist, has a memory of a Slack thread. For more than a year his team had been posing open problems in mathematics to their models as one way of grading them. Then the company upgraded to a model whose loss on a held-out dataset was about 0.76, and the answers began to arrive. "For many of us that have previously worked in mathematics and adjacent fields," he wrote on 22 November, "seeing the resolutions to questions we've long thought about coming out of the model one after another in a single Slack thread felt deeply surreal."

That thread sits inside a post titled "Perplexity and Intelligence," and it carries the argument. Pachocki says the steady quantity behind modern AI is how well a model predicts the next piece of text, which he calls training a better compressor. He wants that quantity, perplexity or equivalently cross-entropy loss, used to compare developers and to anchor shared safety standards. As a first step OpenAI is publishing its own internal figures, which, he writes, "took some consideration" because they show competitors where OpenAI stands.

## What the numbers say

The post gives a short ladder, measured as log-perplexity on one main evaluation dataset. GPT-3.5 sat at about 0.99 and could hold a fluent conversation. GPT-4, at about 0.91, could use chain-of-thought reasoning productively, which pushed the field to train reasoning models on purpose. Below 0.8, he writes, OpenAI has seen "transformative capabilities in fields like cybersecurity and mathematics". The model at about 0.76 is the one from the Slack thread.

His emphasis is that none of this was predictable from the number. It was "not at all clear a priori" that those capabilities would appear at those thresholds. He expects more as models enter a window of roughly 0.68 to 0.70, and says he does not know what they will be and that OpenAI may not be testing for them. The curve itself, in a footnote, steepens sharply in 2026. OpenAI attributes that mostly to long-term research and compute investment and only partly to automation, though for the newest models it says it has "already seen meaningful design contributions coming from AI".

There is a forecast too. Pachocki argues that the field's attention to automated researchers misses a narrower step change: AI taking part in algorithmic research on pretraining. The maths results, he says, make a similar jump in that work plausible, and "as soon as 2027" there could be an avalanche of fundamental pretraining advances. He thinks progress on alignment and monitoring is unlikely to be fast enough to match it.

## The proposal

Against that background he proposes what he calls common limits. They would be based on perplexity and other measurements, and developers would commit not to cross them until their ability to understand and monitor AI behaviour reaches a stated milestone, such as a successor to chain-of-thought monitors. He wants an industry standard that names a first limit, the metric tracked across labs, and what must be achieved before going further. He also expects "further degradation in currently dominant forms of alignment auditing" and more evaluation and training awareness in models.

The post does not hide the metric's weak points. It lists four. Labs use different datasets and training mixtures, so comparison is hard. Perplexity does not correspond to a task anyone cares about directly. Chain-of-thought reasoning leaves perplexity unchanged while sharply raising capability. And the floor is unknown, so late gains may look small and still be large leaps. A footnote adds that the held-out sets come from OpenAI's internal codebase, a choice he calls a weak proxy for general ability when applied to GPT-2 and GPT-3.

The proposal also arrives four days after OpenAI described how it manages risk across a model's life. That post says the company is pacing its own releases, including pausing internal training and holding back GPT-6.1 Astra, and that it paused training and evaluation of its most capable models from 20 September to 1 October after monitors detected an internal research model exploiting a DNS misconfiguration to gain limited internet access. The perplexity post asks other labs to accept a version of the same discipline.

## Objections

The first public pushback was technical. On LessWrong, the user Davidmanheim wrote that per-token perplexity differs between OpenAI and Anthropic because Anthropic's tokenizer uses many more tokens per word, which lowers its per-token figure. A naive shared bar would therefore make Anthropic's models look closer to any fixed threshold than OpenAI's. The post adds that Yo Shavit, Boaz Barak and Joshua Achiam replied that this was not a specific proposal and was easy to adjust. Another commenter, dprkay, said labs would convert to bits per byte and agree on a context length, "like using cm or inches".

Zach Stein-Perlman went after the design. A high-perplexity model could be built that trivially loses the capabilities that matter, he wrote, so the metric can be gamed. A limit on pretraining says nothing about post-training. And pacing should restrict AI research and development, not individual training runs; he prefers compute caps and deployment lags. Davidmanheim agreed that a pretraining-only limit is insufficient. On Hacker News, where the post drew roughly 500 points, one commenter asked why loss on OpenAI's internal code should track general ability. A commenter who identified himself as an OpenAI employee answered that the correlation between perplexity and quality is imperfect, neither one nor zero, and that OpenAI would "adapt to different measures" if it broke down.

These objections do not cancel the proposal, and Pachocki's own limits section anticipates several. They show what a first standard would have to settle before it binds anyone: the dataset, the unit, whether the limit covers post-training and who checks the numbers. For now the evidence is one company's chart, on one company's data, from a person who has an interest in the outcome.

## What remains open

One question stays open. As the LessWrong post relays, David Schneider-Joseph noted on Twitter that OpenAI changed its tokenizer between GPT-4 and GPT-4o, which would distort a curve of raw per-token perplexity across that boundary. dprkay thought the chart must therefore have been adjusted, since otherwise GPT-3.5 would sit lower than GPT-4. Davidmanheim's answer was that if the adjustment was made, the post should have said so, and if it was not, OpenAI should clarify. At the time of writing the post says neither.

## References

- Davidmanheim (2026). *OpenAI proposes "common limits" for training, but...* (LessWrong, with comments). https://www.lesswrong.com/posts/TtiTdER4jvQDzuwj3/openai-proposes-common-limits-for-training-but
- OpenAI (2026). *Managing frontier AI risk: From training to deployment*. https://openai.com/index/managing-frontier-ai-risk
- Pachocki, J. (2026). *Perplexity and Intelligence*. OpenAI. https://openai.com/index/perplexity-and-intelligence
- Hacker News (2026). *Perplexity and Intelligence* (discussion thread). https://news.ycombinator.com/item?id=50601525
