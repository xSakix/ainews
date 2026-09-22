+++
date = '2026-09-22T04:00:20+02:00'
draft = false
title = 'SpaceXAI Releases Grok 4.7'
+++

*SpaceXAI released Grok 4.7 on 21 September for coding and professional knowledge work, with API access starting at $2 per million input tokens.*

SpaceXAI, the company that develops Grok, has introduced a larger model with longer reinforcement learning and a new safeguard system. The release is available through the Grok API, Grok Build, Cursor and other model platforms. Developers now have another frontier-priced option, but the evidence published with the launch comes mainly from the vendor.

## Why it matters

The practical change is not a single benchmark win. Grok 4.7 combines a relatively low advertised API price with support for multi-hour coding and office tasks. That makes it relevant to teams choosing a model for agents that must work through repositories, terminals or document-heavy assignments rather than answer one prompt.

SpaceXAI lists standard pricing of $2 per million input tokens and $6 per million output tokens, the same rates it gives for Grok 4.6. A faster variant is advertised at twice the output speed and twice the price. Price comparisons still depend on how many tokens and retries a task consumes, so a cheaper token does not necessarily mean a cheaper completed job.

The company says Grok 4.7 uses a larger base model than Grok 4.6 and received a longer reinforcement-learning run weighted toward tasks that take hours. It also says the model checks its own work more carefully and understands the Grok Bot harness natively. Those descriptions explain the intended design, but they do not independently establish reliability.

## What the published tests show

SpaceXAI reports 46.3% on CursorBench 4.0, a long-running software-engineering test, compared with 40.4% for Grok 4.6. It also reports 38.0% on Terminal-Bench 4.0 and 1,657 points on AA Briefcase 1.1. The comparison table includes competing models, but SpaceXAI published the numbers and did not provide an independent audit with the announcement.

Safety claims require the same caution. The company says only 3.3% of risky dual-use prompts passed through on its HackerBench 0.3 test and calls this its best jailbreak resistance so far. It also says selected security partners will receive invite-only red-team access. These are useful disclosures about intended controls; they are not a substitute for external evaluation or production incident data.

The release therefore changes the available market before it settles the ranking. A procurement team can test Grok 4.7 now, but should reproduce its own workloads, count end-to-end cost and examine refusal behavior on both benign and risky tasks.

The next useful information will come from independent coding-agent runs and comparisons using identical harnesses. Model performance can change when tools, context management and retry policies change, so tests that hold those factors constant will be more informative than headline tables.

## Verification

1. **VERIFIED — SpaceXAI announced Grok 4.7 on 21 September 2026 and made it available through its API and named platforms.** Primary source: https://x.ai/news/grok-4-7
2. **VERIFIED AS A VENDOR CLAIM — SpaceXAI says the model has a larger base, longer reinforcement learning and stronger self-checking.** Primary source: https://x.ai/news/grok-4-7
3. **VERIFIED AS VENDOR-REPORTED RESULTS — The benchmark scores and 3.3% risky-prompt figure are reported by SpaceXAI, not independently confirmed here.** Primary source: https://x.ai/news/grok-4-7
4. **VERIFIED — Standard API pricing starts at $2 per million input tokens and $6 per million output tokens.** Primary source: https://x.ai/news/grok-4-7

## Glossary candidates

- **Reinforcement learning:** Training that improves behavior using feedback or rewards.
- **Harness:** Software that supplies tools, context and control logic around a model.
- **Dual use:** Work that can support legitimate or harmful purposes.

Cold-reader sentence: SpaceXAI released Grok 4.7 with lower-cost API access, vendor-reported coding gains and a safeguard system that still needs independent testing.
