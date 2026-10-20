+++
title = "Cloudflare Cut Its AI Review Bill by Fixing the Cache"
description = "Cloudflare's AI code reviewer grew more expensive as its models improved. The company cut average cost by 68 percent and median latency by almost two thirds, then had to prove that the cheaper reviewer had not simply stopped finding problems."
tags = ["agents", "tools", "business"]
date = 2026-10-20T04:05:28+02:00
draft = false
+++

Consider an engineer who exists only for this paragraph. Her merge request contains a small change to a service used around the world. She pushes it at 4:12 p.m. Seven automated reviewers wake, read the same instructions, inspect overlapping parts of the repository and send nearly three million tokens through the models before a coordinator decides what to tell her. The review arrives four minutes later. It costs more than twice what the same system cost in spring.

## The bill rose without a redesign

Cloudflare built that kind of system for its own engineers. Ryan Skidmore, a systems engineer at the company, described the original architecture in April 2026: up to seven specialist agents reviewed security, performance, code quality, documentation, releases and internal standards, while a coordinator deduplicated their findings and decided whether to approve a merge request. During its first month, Cloudflare says, it completed 131,246 review runs across 48,095 merge requests in 5,169 repositories. The average review cost $1.19.

By the end of August, the average had reached about $2.46. Cloudflare had not replaced the system with a more elaborate one. The coordinator still delegated to specialists, and the same risk tiers determined whether a change received a light or full review. The company had changed the models and allowed the conversations to grow.

The cost series moved steadily: $1.22 per review in March, $1.44 in June, $1.74 in July and $2.32 in August after adjusting for the mix of review tiers. More changes were landing in the expensive tier, but Cloudflare says model choices caused most of the increase. Moving every reviewer to Anthropic models raised a job from $1.38 to $2.03. One internal-standards reviewer rose from about 25 cents to 88 cents per run.

The models were doing more work too. Tokens per review more than tripled, from 0.91 million to 2.99 million, even as the overall cache-hit rate improved from 85.7 to 97 percent. A high percentage had hidden a larger denominator.

## The expensive prefix

Immediately before the optimisation work, output tokens represented about 23 percent of review spending. Cache writes consumed 43 percent and cache reads another 34 percent. Most money went to context already seen, or context about to be seen again.

Anthropic's prompt cache reuses matching content at the beginning of a request. Its published pricing makes the trade clear: a five-minute cache write costs 1.25 times the normal input rate, while a cache read costs one tenth. Reuse pays only when later requests begin with the same prefix before the entry expires.

Cloudflare's reviewers seemed ideal for that arrangement. Their tool definitions and agent instructions contributed 11,000 to 21,000 tokens that were identical across repositories. Yet the first request in a session found a cached prefix only 14 to 26 percent of the time.

The ordering was wrong. OpenCode v1 had placed a repository-specific environment block, including the working directory and date, in the same system block as the shared instructions. The cache breakpoint sat after both. A session in one repository could not reuse the prefix written by another because changing details appeared before the breakpoint.

Cloudflare split the system content at a marker and placed the shared material first. First-request reuse rose to between 91 and 99.5 percent after the change. The three main reviewers also started together, before one could finish writing the common prefix. The team made the second and third wait up to 20 seconds for the first response to begin, trading a small delay for about nine cents saved per reviewer.

That engineering change delivered the largest single reduction. It was still less than half the total saving.

## Models that stop sooner

Cloudflare also tested model and effort settings rather than assuming the most expensive combination was safest. Code changes accounted for 65 cents of the $1.67 reduction measured in the post; model and effort changes accounted for $1.06. Skidmore cautions that these stepwise comparisons were not a controlled experiment.

Newer models used fewer calls. In a two-and-a-half-day split test, Sonnet 5.5 cost 62 percent less per code-quality run than Sonnet 5, 58 percent less for performance and 47 percent less for security, despite identical per-token pricing. At medium effort, the code-quality agent made 1.7 model calls rather than 6.2. More than half of its runs ended after one call without opening another repository file.

That looked efficient and dangerous. A reviewer that reads less can finish cheaply because it misses the bug.

Cloudflare compared high and medium effort. High effort cost 61 percent more per code-quality run and produced 58 percent more critical or warning findings. The difference was about two cents per review. The team restored high effort for that agent while keeping other specialists at medium pending more tests.

Fewer calls shortened the wait. The median review fell from four minutes nine seconds to one minute 32 seconds. The 99th percentile dropped from 15 minutes 20 seconds to four minutes 41 seconds. Reviews lasting more than five minutes fell from 37.9 percent to 0.7 percent.

## Testing what disappeared

The raw count of severe findings fell after the changes. Code quality produced 40 percent fewer critical and warning findings; security fell 56 percent and performance 71 percent. Cloudflare tried to distinguish noise removed from problems missed.

First, it checked whether engineers changed the lines flagged by the reviewer in their next push. Before the optimisation, authors acted on 34 percent of serious code-quality findings. Afterwards they acted on 59 percent. Findings became less frequent but more likely to cause a change: 132 acted-on findings per 1,000 reviews after the changes, against 145 before, a difference Cloudflare says sits within the margin of error. Across all four reviewers, the measure rose from 229 to 321 per 1,000.

Second, models from two providers judged a blinded sample of 657 findings. A third broke disagreements. Important code-quality findings per review held near 0.3, while minor, duplicate and unverifiable findings declined. Inflated severity dropped more clearly: judges rated 0.46 critical or warning findings per review as too severe before the changes and 0.14 afterwards.

The evidence did not clear every reviewer. At medium effort, performance lost about 64 percent of important findings, equal to one missed important issue for every 24 full-tier reviews. Security lost about a quarter, though that estimate was not statistically significant. Cloudflare says its samples contained only 35 to 66 findings in each group, the post-change window lasted one day, and model judges are imperfect. An engineer changing flagged lines also proves action, not correctness.

## Cost is an evaluation result

The finished system averages 77 cents per review, down from $2.43 during its two most expensive weeks. About 40 percent of the saving came from code; the rest came from model and effort choices. Reliability improved alongside cost: reviews ending without a verdict fell from 0.79 to 0.27 percent, and security-agent retries from 3.5 to 0.04 percent.

Cloudflare's broader lesson is less tidy than “use prompt caching.” The company inspected the exact first request reaching the provider, changed the stable prefix, measured each configuration change and then evaluated the findings that vanished. A cheaper agent could mean a cleaner system, a weaker system or both in different parts of the same pipeline.

Return to the invented engineer at 4:12. The revised reviewer reaches her before she has left the merge request, having paid once for instructions its peers can reuse. It reports fewer warnings. Her job is to know whether the silence came from removing repetition or from a model that chose not to look. Cloudflare saved the money only after it built a way to tell those outcomes apart.

## References

- Anthropic. (2026). *Pricing*. https://docs.anthropic.com/en/docs/about-claude/pricing
- Skidmore, R. (2026). *Cutting our inference bill by 68% by being obsessive about optimization*. https://blog.cloudflare.com/obsessive-inference-optimization/
- Skidmore, R. (2026). *Orchestrating AI Code Review at scale*. https://blog.cloudflare.com/ai-code-review/
