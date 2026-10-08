+++
title = "Anthropic launches Claude Haiku 5.5"
description = "The small Claude model adds adaptive thinking and a two-tier token price. Anthropic positions it for summaries, browser work and narrowly scoped subagents."
tags = ["models", "agents"]
date = 2026-10-08T03:59:31+02:00
draft = false
+++

Anthropic released Claude Haiku 5.5 on 7 October, cutting the effective price of its small-model tier while adding a one-million-token context window and adjustable reasoning effort.

The API model is built for frequent, narrowly scoped work such as classification, summarisation, database queries and subagent tasks. It is available through Anthropic and the major cloud platforms under the model ID `claude-haiku-5-5`.

For developers paying per task, the price change is the immediate consequence. Prompts up to 100,000 tokens cost $0.10 per million input tokens and $0.50 per million output tokens. Longer prompts cost $0.50 and $2.50 respectively. Anthropic says the resulting average cost is about 75% below Haiku 4.5 after accounting for the new model's slightly different tokenizer.

Haiku 5.5 is the first Haiku model with adaptive thinking and an effort control. That also creates a migration issue: requests using the older manual `budget_tokens` setting return an HTTP 400 error. Applications moving from Haiku 4.5 need to remove that setting and retest token use as well as output quality.

Anthropic's own evaluations put Haiku 5.5 at 72.4% on the offline portion of a computer-use benchmark, compared with 15.7% for Haiku 4.5. The comparison is vendor-run, and Anthropic still directs complex coding work to Sonnet 5.5 or Opus 5.5. Haiku's intended role is the cheaper supporting model that handles short, repeated operations around a larger model.

The release also halves Sonnet 5.5 cache-read pricing to $0.10 per million tokens. Anthropic says cache reads make up enough agent traffic for the change to reduce the cost of most Sonnet 5.5 agent tasks by about 20%.

Max and Team subscribers are due to receive monthly API credits during the week of the launch. Anthropic's Python and TypeScript SDKs are also gaining beta classes for browser and computer use, the two speed-sensitive workloads the company highlights for Haiku 5.5.

## Verification

| Claim | Label | Primary source | Independent check |
|---|---|---|---|
| Anthropic released Claude Haiku 5.5 on 7 October 2026 with adaptive thinking, a 1M-token context window and 128K maximum output | VERIFIED | [Anthropic launch](https://www.anthropic.com/claude-haiku-5-5) | none |
| Prompts up to 100K tokens cost $0.10 input and $0.50 output per million tokens; longer prompts cost $0.50 and $2.50 | VERIFIED | [Anthropic launch](https://www.anthropic.com/claude-haiku-5-5) | none |
| Anthropic says average cost is about 75% below Haiku 4.5 | VENDOR-REPORTED | [Anthropic launch](https://www.anthropic.com/claude-haiku-5-5) | none |
| Anthropic reports 72.4% on the OSWorld 2.1 offline subset, versus 15.7% for Haiku 4.5 | VENDOR-REPORTED | [Anthropic launch](https://www.anthropic.com/claude-haiku-5-5) | none |
| Manual `budget_tokens` requests return HTTP 400 during migration | VERIFIED | [Claude release notes](https://platform.claude.com/docs/en/release-notes/overview) | none |
| Sonnet 5.5 cache reads now cost $0.10 per million tokens and Anthropic estimates about 20% lower agent-task costs | VENDOR-REPORTED | [Anthropic launch](https://www.anthropic.com/claude-haiku-5-5) | none |
