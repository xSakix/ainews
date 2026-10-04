+++
title = "Zou team traces how models report internal changes"
description = "A controlled preprint separates detecting an activation change from reporting its location. The experiment uses fixed input text and scores answers without an AI judge."
tags = ["research", "safety"]
date = 2026-10-04T09:26:37+02:00
draft = false
+++

Jiahong Zou's team has identified two groups of attention heads that help language models report a deliberately injected internal change: one controls reporting, and another helps locate the change.

The preprint, submitted on 28 September, studies a narrow form of introspection. The researchers alter a model's hidden activations while keeping the visible prompt identical, then ask the model to name the affected position or say that nothing changed.

For an engineer studying activation steering, the result provides a concrete place to investigate whether a model registered the intervention. Steering changes a model's internal representations to influence its output; this experiment examines the machinery that turns such a change into an explicit report.

Zou and co-authors list affiliations at Shandong University, Tsinghua University, Northeastern University and the University of Hong Kong. They test instruction-tuned models from the Qwen, Llama and Gemma families, with the scoring performed directly from model output scores instead of by a separate language-model judge.

Each prompt contains ten candidate token positions. An injected concept vector changes the hidden state at one position, or a clean comparison run changes nothing. The vector is constructed from the difference between activations elicited by a concept and an average over vocabulary words.

The model chooses among position labels and a no-change response. Scoring uses the first output position, before generated explanatory text can supply extra evidence. The researchers also vary the labels between digits, letters and words, and shuffle their order to check whether a fixed label association explains success.

All three models locate changes above the paper's random-position baseline, but results depend substantially on the label format. The authors choose injection settings on separate calibration data and retain concepts that work best there. Their test therefore measures performance within a screened concept pool, rather than sensitivity to any arbitrary internal change.

## Detecting a change and naming its position come apart

The central evidence comes from replacing selected attention-head outputs with outputs from a paired run. An attention head moves information between token positions; replacing its output lets the researchers test its contribution to the answer.

Middle-layer heads influence whether a position is reported at all. The authors call these gate heads. A small group in a later layer helps choose which position to report, earning the name router heads.

Intervening on the gate heads can suppress a position report even when the router heads still carry location information. Conversely, replacing router outputs with clean-run outputs reduces location accuracy. Redirecting their attention helps test the link between where they look and the position selected.

That separation is the paper's strongest finding. Information about an intervention can remain inside the model while the answer reports no intervention. A model's verbal report is therefore the end of a specific reporting mechanism, not a complete inventory of the information in its hidden state.

The authors limit their analysis to six task variants, one selected injection layer and strength per model, and models no larger than 12 billion parameters. They explicitly study functional reporting and make no claim about consciousness or subjective experience.

Free-form and unprompted reports remain outside the tested task. The paper identifies those as follow-up work, along with other types of perturbation and the role of components that process information within each position. The authors have released code, data splits and scripts for reproducing the figures and tables.

## Verification

| Claim | Label | Primary source | Independent check |
| --- | --- | --- | --- |
| Preprint submitted 28 September; authors and listed university affiliations | VERIFIED | [Source](https://arxiv.org/abs/2609.35108) | none; publication is a preprint |
| Qwen3-4B-IT, LLaMA-3.1-8B-IT and Gemma-3-12B-IT; fixed text, ten candidate positions, concept-vector injection or clean control; direct first-output scoring | VENDOR-REPORTED | [Source](https://arxiv.org/abs/2609.35108) | none; authors' methods |
| Separate calibration; top 300 concepts split into disjoint groups; six label settings and shuffled labels; performance exceeds 10% position baseline but varies by label | VENDOR-REPORTED | [Source](https://arxiv.org/abs/2609.35108) | none; methods and Table 1 |
| Gate heads affect whether to report; later router heads affect location; patching and attention-redirection interventions support separation | VENDOR-REPORTED | [Source](https://arxiv.org/abs/2609.35108) | none; authors' causal experiments |
| Internal location information can persist when no position is reported; relevance to monitoring steering interventions | ANALYSIS | [Source](https://arxiv.org/abs/2609.35108) | Inference from gate/router interventions; not a deployed monitoring result |
| Scope limitations; functional rather than experiential introspection; follow-up questions; code and reproduction scripts released | VERIFIED | [Source](https://arxiv.org/abs/2609.35108) | none; paper's stated scope and repository link |
