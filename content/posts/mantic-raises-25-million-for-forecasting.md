+++
date = '2026-09-19T04:00:00+02:00'
draft = false
title = 'Mantic Raises $25 Million for AI Forecasting'
+++

After reading this, the reader knows what Mantic says it predicts, who funded it and why its performance claim needs scrutiny.

# Mantic Raises $25 Million for AI Forecasting

*The London startup says its system beat human forecasters in a recent tournament, attracting a seed round led by Radical Ventures.*

Mantic has raised $25 million in seed funding to develop AI systems that assign probabilities to political, economic and cultural events, according to Reuters. Radical Ventures led the round at an undisclosed valuation.

In plain terms, Mantic adapts existing frontier models for forecasting rather than building a general-purpose foundation model. It tests predictions against historical outcomes, grades the results and changes the system to improve later forecasts.

## Why it matters

Organizations routinely make decisions under uncertainty, from inventory planning to policy analysis. A system that produces calibrated probabilities can be more useful than a confident narrative because decision-makers can compare the forecast with risk thresholds and update it as evidence changes.

Forecasting is also unusually measurable. A prediction made before an event can be scored after the outcome is known. Repeated questions allow evaluators to test whether events assigned 70% probability happen about seven times out of ten. That creates a clearer feedback loop than many open-ended business AI tasks.

Reuters reported that Mantic outperformed human participants in the Summer 2026 Metaculus Cup, an online tournament whose questions covered several domains. The public tournament page confirms that the competition closed and winners were announced, but the accessible page did not expose enough leaderboard detail to reproduce the comparative claim for this article.

The company told Reuters that it avoided following the human consensus on some questions. One example involved Colombia's presidential election: Mantic reportedly assigned the eventual winner a higher probability than the crowd did. Individual successes are illustrative, but they do not establish overall calibration or robustness.

## A leaderboard is not a deployment

Forecasting tournaments define questions, deadlines and resolution criteria in advance. Real customers may ask ambiguous questions whose outcomes are delayed or difficult to score. A model can also perform well on a broad average while failing on the low-frequency events that matter most to a specific organization.

Useful evaluation therefore needs more than a rank. Customers should inspect the number of questions, scoring rule, comparison group and whether the system was tuned after seeing similar historical tasks. They should also test performance on a held-out period that the developer could not use for iteration.

The funding participants reported by Reuters include Microsoft's venture fund M12, Thinking Machines Lab and Balderton Capital. Mantic was co-founded in 2024 by Toby Shevlane, a former Google DeepMind researcher, and Ben Day. Reuters said companies and government agencies have shown interest, but Mantic did not name customers.

No public company announcement documenting the round was located during verification. The funding details and quoted performance description therefore remain reported information rather than independently verified primary claims. The Metaculus tournament page provides a primary record that the competition existed, not the full evidence needed to validate Mantic's rank.

The next useful disclosure would be a reproducible evaluation containing forecasts, timestamps, scoring rules and baselines. Commercial results should also state where human review changed a forecast and how often the system abstained.

Mantic's round shows investors treating probabilistic forecasting as a distinct AI product category. Its durable value will depend on calibration outside tournaments and on whether customers can audit how a probability was produced.

## Verification

- **Tier 3 — UNVERIFIED AGAINST PUBLIC PRIMARY:** Reuters reported the $25 million seed round, its investors and Mantic's operating description after interviews with the company and investor. No public Mantic announcement was located. Via: https://www.reuters.com/technology/ai-startup-mantic-raises-25-million-superhuman-forecasting-2026-09-18/
- **Tier 0 — VERIFIED:** Metaculus maintains a public page for the closed Summer 2026 Cup and says winners were announced. Primary source: https://www.metaculus.com/tournament/metaculus-cup-summer-2026/
- **Tier 3 — UNVERIFIED AGAINST ACCESSIBLE PRIMARY DATA:** Mantic's reported performance relative to human participants could not be reproduced from the accessible tournament page. Via: Reuters article above.
- **Tier 2 — ANALYSIS:** Evaluation and deployment guidance is editorial analysis.

## Glossary candidates

- **Calibration:** Agreement between forecast probabilities and observed outcome frequencies.
- **Scoring rule:** A formula that rewards accurate probability forecasts and penalizes inaccurate ones.

Cold-reader sentence: Mantic reportedly raised $25 million after a strong forecasting tournament, but its comparative performance needs reproducible primary data.
