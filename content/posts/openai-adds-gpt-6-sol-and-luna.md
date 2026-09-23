+++
date = '2026-09-23T03:59:46+02:00'
draft = false
title = 'OpenAI Adds GPT-6 Sol and Luna'
+++

*OpenAI added two GPT-6 API tiers, giving developers a lower-cost Sol model and a very inexpensive Luna option for high-volume workloads.*

OpenAI's API page now lists GPT-6 Sol and GPT-6 Luna alongside the higher-priced GPT-6 Astra. Sol costs $2 per million input tokens and $10 per million output tokens. Luna costs $0.10 per million input tokens and $0.50 per million output tokens. Both list a 1.05-million-token context window and a maximum output of 128,000 tokens.

## Why it matters

The release turns the GPT-6 family into a price ladder rather than a single frontier product. Astra remains the expensive option at $10 per million input tokens and $50 per million output tokens. Sol is one fifth of those prices, while Luna is one hundredth of Astra's input price. That gives teams a clearer way to route work by difficulty instead of using one model for every request.

Routing can change the economics of agents. A workflow might reserve Astra for difficult planning, use Sol for most coding or analysis, and send classification, extraction or simple drafting to Luna. The savings are only real if the lower tier completes the task reliably. Failed attempts, retries and human review can erase a headline token discount.

OpenAI lists the same context and maximum-output sizes for all three models on its API overview. A large context window means the system can accept a substantial prompt, but it does not guarantee that every detail will be used correctly. Long-context performance depends on retrieval, ordering and the task itself. Developers should test the portions of the window they actually need rather than treating the maximum as a quality promise.

Launch coverage also described performance improvements and price cuts relative to GPT-5.6 models. The primary OpenAI page confirms current prices and specifications, but it does not show enough methodology on that page to validate every comparative claim. This article therefore treats current availability, price and context limits as verified and leaves broader quality claims to controlled tests.

The pricing also intensifies competition on completed-task cost. Anthropic launched Opus 5.5 the same day with lower prices and claims of reduced token use. A model can be more expensive per token yet cheaper for a job if it finishes in fewer turns. Conversely, a cheap model may dominate repetitive, bounded tasks even when it loses harder benchmarks.

Procurement teams should build a representative evaluation set and record success rate, latency, tokens, retries and reviewer corrections. They should also pin model versions where possible because routing aliases and behavior can change. Sensitive deployments need the usual checks for retention, regional processing and tool permissions independent of the model tier.

The next meaningful evidence will be reproducible comparisons using identical agent harnesses. Until then, Sol and Luna clearly expand the available price range, but they do not by themselves settle which model is cheapest for a finished, accepted result.

## Verification

1. **VERIFIED — OpenAI's API page lists GPT-6 Sol and GPT-6 Luna.** Primary source: https://openai.com/api/
2. **VERIFIED — Sol is priced at $2 per million input tokens and $10 per million output tokens.** Primary source: https://openai.com/api/
3. **VERIFIED — Luna is priced at $0.10 per million input tokens and $0.50 per million output tokens.** Primary source: https://openai.com/api/
4. **VERIFIED — Both models list a 1.05-million-token context and 128,000-token maximum output.** Primary source: https://openai.com/api/
5. **UNVERIFIED HERE — Broad comparative quality claims were not reproduced independently.** Via: https://techcrunch.com/2026/09/22/openai-launches-gpt-6-sol-and-luna/

## Glossary candidates

- **Context window:** The amount of input and prior conversation a model can consider at once.
- **Routing:** Sending different tasks to different models based on cost or difficulty.
- **Completed-task cost:** Total expense required to produce an accepted result, including retries.

Cold-reader sentence: OpenAI's Sol and Luna expand GPT-6 into lower price tiers, but teams still need workload tests to measure true completed-task cost.
