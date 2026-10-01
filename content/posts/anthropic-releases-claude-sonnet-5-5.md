+++
date = '2026-09-29T04:13:15+02:00'
draft = false
title = 'Anthropic releases Claude Sonnet 5.5'
description = "Anthropic keeps Sonnet’s token prices while claiming lower task costs. The useful comparison is the cost of work that passes review."
+++

Anthropic, an AI developer, released Claude Sonnet 5.5 on September 28, positioning the language model for routine coding and office work with claimed efficiency gains over Sonnet 5.

The company has updated its everyday work model. Customers pay the same advertised rates for text processing. Whether they save money depends on how much work the model needs to finish a task.

**Why it matters:** A cheaper completed task could make repeated software maintenance or document processing more economical. A faster answer that needs additional correction would offer a smaller benefit. Buyers should measure accepted results rather than output speed alone.

Anthropic lists prices of $2 per million input tokens and $10 per million output tokens. Tokens are the small units of text a model processes. The company reports output generation more than 30% faster than Sonnet 5 and up to 30% lower cost per task in its testing; these are vendor results, not independently reproduced savings.

Those measurements answer different questions. Generation speed concerns how quickly text appears. Task cost concerns the total text and activity needed to reach a result. Neither measure by itself establishes that the result is correct, and an apparently efficient run may still require a reviewer to repair its output.

A useful comparison would give both models the same maintenance request, repository and tools. Reviewers would judge the proposed changes without knowing which model wrote them. The accounting would include failed attempts and corrections, because a team pays for those attempts even when they never become accepted code.

GitHub, the software hosting company, separately announced Sonnet 5.5 in Copilot, its coding assistant. GitHub said its early testing found comparable completion of everyday tasks with fewer steps and lower token usage. That is deployment-partner evidence, rather than a substitute for testing on a customer’s own workload.

For example, fixing a clearly specified error and deciding how to redesign an unfamiliar system should be separate evaluation categories. Combining them into one average could hide an improvement in routine work alongside a regression in judgment-heavy work.

## Choose effort settings before comparing results

Anthropic itself provides a counterweight to broad superiority claims: it says Claude Opus 5.5, its higher-tier model, remains stronger on complex, open-ended work. Its benchmark discussion also warns that extra reasoning can produce unnecessary changes or timeouts. More computation is therefore not an automatic route to a better accepted answer.

For a buyer, that suggests evaluating a routing policy as well as a model. A proposed workflow might send a bounded bug fix to the less expensive option and escalate an ambiguous design decision. The escalation rule should be written in advance; otherwise a favorable comparison could simply exclude the difficult tasks after seeing the results.

Review time belongs in that calculation. The accepted patch, rather than the generated patch, should define the end of the measurement. If a faster model produces a larger patch, the engineer must still understand the changes. A measurement that ends when generation stops can miss the most expensive part of the workflow. Conversely, a concise, correct patch could save time even when the model’s own response is not the fastest.

Teams should also record their chosen reasoning effort and keep it fixed within each comparison. A high-effort configuration and a default configuration are different operating choices. Reporting only a model name makes the resulting cost comparison hard to reproduce and gives colleagues little guidance about how to obtain the same outcome.

The next useful evidence will be repeated task-level evaluations with acceptance criteria, complete cost records and human review time. Sonnet 5.5 gives teams a new candidate for that evaluation; the launch does not establish a universal replacement for every larger model.

## Verification

| Claim group | Tier | Primary evidence |
| --- | --- | --- |
| Release, positioning and listed token rates | VERIFIED | [Anthropic announcement](https://www.anthropic.com/claude-sonnet-5-5) |
| Speed, task savings, comparative strengths and effort-related failures | PARTIALLY VERIFIED — publisher evaluations, not independently reproduced here | [Anthropic performance discussion and footnotes](https://www.anthropic.com/claude-sonnet-5-5) |
| Copilot availability and partner testing | VERIFIED for announcement; PARTIALLY VERIFIED for performance | [GitHub changelog](https://github.blog/changelog/2026-09-28-claude-sonnet-5-5-in-github-copilot/) |
| Evaluation, routing and review-cost implications | Analysis; proposed tests rather than measured outcomes | Inference from the two primary sources above |
