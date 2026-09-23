+++
date = '2026-09-23T03:59:46+02:00'
draft = false
title = 'Anthropic Launches Claude Opus 5.5'
+++

*Anthropic released Claude Opus 5.5 with lower prices, faster output and vendor-reported gains in coding, computer use and long-running work.*

Anthropic introduced Claude Opus 5.5 on 22 September as the first model in its Claude 5.5 family. The company positions it between two familiar demands: frontier capability and a production bill that can survive sustained agent use. Its central claim is not simply that the model scores higher. Anthropic says Opus 5.5 performs at roughly the level of Fable 5.1 on most work while costing 40% less than Opus 5 on typical workloads.

## Why it matters

Agent economics depend on more than a price printed beside a model name. A coding agent may read large caches, make repeated tool calls and generate many tokens before it finishes. Anthropic has therefore cut several parts of the bill: input tokens cost $4 per million, output tokens $20 per million and cache reads $0.20 per million. The company says default workloads cost 40% less overall and output arrives more than 30% faster than with Opus 5.

Those figures could matter more than a narrow benchmark lead. A model that reaches the same result with fewer steps can reduce latency and cost at once. Early customers quoted by Anthropic describe fewer turns, less rework and longer unattended runs. They are useful accounts of intended use, but they are testimonials selected for a launch and should not be mistaken for a controlled market-wide study.

Anthropic's own table reports 66.4% on Terminal-Bench 4.0, 54.4% on FrontierCode and 81.8% on a partial OSWorld 2.0 evaluation. The company also says Opus 5.5 completes long code migrations and audits more efficiently than its predecessors. Evaluation settings differ across models, and some competing scores are reported by their vendors. That makes the table evidence about Anthropic's testing, not a permanent universal ranking.

Safety is unusually prominent in the release. Anthropic says external evaluators including METR and Frontier Design tested the model before release. Its automated behavioral audit found fewer irreversible or out-of-bounds actions, and its prompt-injection results matched or improved on Opus 5. The model also uses an action-screening classifier and an auditable sandbox in Claude Code. A system card supplies more detail, though real production incidents remain the harder test.

The launch follows Anthropic's public call to slow the pace of frontier development. The company says Opus 5.5 is comparable to Claude Mythos 5.1 in biology and cybersecurity and is deploying similar safeguards. Vetted organizations can seek special access for life-sciences and cybersecurity work. That framing separates raw capability from permission to use the most sensitive parts of it.

For buyers, the right comparison is a workload trial using the same repository, tools, retry rules and quality bar. Token prices alone cannot show whether a model will finish with less supervision. The most credible follow-up will be independent evaluations that publish prompts, harness settings, total cost and error analysis.

## Verification

1. **VERIFIED — Anthropic announced Claude Opus 5.5 on 22 September 2026.** Primary source: https://www.anthropic.com/claude-opus-5-5
2. **VERIFIED — Standard prices are $4 per million input tokens, $20 per million output tokens and $0.20 per million cache-read tokens.** Primary source: https://www.anthropic.com/claude-opus-5-5
3. **VERIFIED AS VENDOR CLAIMS — The 40% workload saving, speed gain and benchmark scores were published by Anthropic.** Primary source: https://www.anthropic.com/claude-opus-5-5
4. **VERIFIED — Anthropic names external pre-release evaluators and provides a system card.** Primary source: https://www.anthropic.com/claude-opus-5-5

## Glossary candidates

- **Cache read:** Reusing stored prompt context instead of processing it again.
- **Prompt injection:** Instructions in untrusted content that try to redirect an AI system.
- **Harness:** Software that supplies tools, context and control logic around a model.

Cold-reader sentence: Claude Opus 5.5 targets long-running agent work with lower prices and stronger vendor-reported results that still need independent testing.
