+++
date = '2026-09-20T04:05:00+02:00'
draft = false
title = 'DraftKings Reportedly Targeted Likely Losses'
+++

After reading this, the reader knows what the New York Times reported, why loss prediction raises a distinct governance issue and what evidence is still missing.

# DraftKings Reportedly Targeted Likely Losses

*A newspaper report says the sportsbook used machine learning to find customers expected to lose and direct offers toward them; primary documentation was not available.*

DraftKings reportedly used a machine-learning model to identify gamblers expected to lose money and target them with promotional offers. The claim comes from a 19 September New York Times report.

No public company document, model card or regulator filing confirming the described targeting system was located during this review. DraftKings' precise criteria, deployment dates, safeguards and response to the allegations therefore cannot be independently established from primary sources here.

That missing evidence changes how the story should be stated. It is accurate to say the Times reported the practice. It is not yet accurate to present every detail of the system as independently verified fact.

## Why it matters

Prediction is common in online commerce. Companies estimate whether a customer will leave, click, buy or respond to a discount. Gambling creates a sharper problem because the target outcome may be the customer's financial loss, and some users are vulnerable to compulsive behavior.

A model optimized to find likely losers can turn ordinary personalization into risk selection. If a promotion is sent because the recipient is expected to lose, the system's success for the operator may be directly opposed to the customer's welfare. That is different from recommending a film or predicting which shoes someone prefers.

The key governance question is the objective function. A model can use similar behavioral data for opposite purposes: detecting signs of harm and slowing a user's activity, or identifying the same susceptibility and increasing engagement. Accuracy alone says nothing about whether the deployment is responsible.

Regulators and auditors would need more than the model's name. They would need its target variable, features, training period, decision thresholds and how promotions changed after a score. They would also need to know whether risk indicators were excluded from marketing systems, whether vulnerable users could be suppressed from campaigns and how staff monitored outcomes.

## What evidence would settle the claim

The strongest evidence would include internal policy documents, source records, regulator findings or sworn testimony describing the model and its use. Aggregate numbers could show how many people were scored, how many received offers and whether the targeted group lost more than a valid comparison group.

Independent reviewers should also examine false positives and feedback loops. A person who responds to an offer may generate more betting data, which can make the system more confident and trigger further promotions. Without constraints, the model can help create the pattern it claims merely to predict.

Safeguards should be testable. Useful controls could include separating responsible-gaming and marketing data, prohibiting promotions above risk thresholds, logging every model-driven offer and allowing compliance teams to reproduce why a person was selected. External audits should test actual outcomes, not only policy language.

The story also illustrates a limitation of public AI debate. Attention often centers on hypothetical future systems, while narrow predictive models already shape credit, insurance, employment and gambling decisions. Their risks come from incentives, data and deployment rules as much as from model capability.

DraftKings should have an opportunity to provide documentation and context, and regulators should distinguish an allegation from a completed finding. At the same time, a system that predicts who is likely to lose deserves scrutiny precisely because the commercial and consumer objectives can diverge so clearly.

Until primary evidence is available, the central claim remains reported rather than independently verified. The policy lesson is firmer: high-impact personalization should be evaluated by what the model is optimizing and whom its successful predictions benefit.

## Verification

- **Tier 3 — UNVERIFIED:** The New York Times reportedly says DraftKings used machine learning to identify customers expected to lose and target them with offers. Via: https://www.nytimes.com/2026/09/19/business/draftkings-ai.html
- **Tier 3 — UNVERIFIED:** No primary company document or regulator finding confirming the reported deployment was located during this review.
- **Tier 2 — ANALYSIS:** Discussion of objective functions, feedback loops, audit evidence and safeguards is editorial analysis and does not establish DraftKings' actual implementation.

## Glossary candidates

- **Objective function:** The result a model is trained or tuned to optimize.
- **Feedback loop:** A cycle in which a prediction changes behavior and creates new data that reinforces later predictions.

Cold-reader sentence: DraftKings reportedly targeted people predicted to lose, but the deployment details remain unconfirmed without primary company or regulator records.
