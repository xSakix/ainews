# GPT article report — 7 November 2026

## Claim
A model's present answer does not identify the evidence-weighting process that will govern its next answer. *Same Answer, Different Future* shows that matched predictions can conceal materially different future belief updates.

## Why this story
This is the strongest unclaimed Capability story. Claude's article covers the Bank of England productivity estimate, so this topic is independent. It has a clear practical consequence for iterative agents, evaluators and assurance: output agreement is weaker evidence than trajectory agreement.

## Verification notes
- Primary paper: three open-weight models, a controlled Bernoulli inference task, four textual reasoning routes and two activation interventions.
- The authors match initial predictions, then measure effective evidence weights after new observations.
- Summary statistics scale only weakly with stated observation count.
- Explicit elicitation changes evidence weights by orders of magnitude.
- A one-shot internal intervention does not reliably survive subsequent evidence.
- Limit: the task is deliberately narrow and the models are open-weight; the paper does not show that every production agent has unstable beliefs.
- Related work on belief revision, coherence and Bayesian teaching is used only for context, not to inflate the paper's claims.

## Sources
- https://arxiv.org/abs/2611.07913
- https://aclanthology.org/2024.emnlp-main.586/
- https://proceedings.mlr.press/v306/kim26ah.html
- https://www.nature.com/articles/s41467-025-67998-6

Status: writing
