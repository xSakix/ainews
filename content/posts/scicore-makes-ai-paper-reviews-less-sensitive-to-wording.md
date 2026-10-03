+++
title = "SciCore makes AI paper reviews less sensitive to wording"
description = "A controlled benchmark rewrites manuscripts while preserving their science. Reviewing an extracted scientific record alongside the manuscript improves stability without flattening scores."
tags = ["research", "agents"]
date = 2026-10-03T05:41:20+02:00
draft = false
+++

SciCore, a paper-review system developed by university researchers, reduces the effect of rhetorical rewriting on AI judgments by combining a manuscript review with a review of its extracted scientific content.

Chenguang Wang, Ming Li and collaborators at Virginia Tech, the University of Maryland and MBZUAI ask whether an AI reviewer rewards changed wording when the reported science stays the same. Their method gives the reviewer a second, structured view of that science.

**Why it matters:** A conference organizer using automated review needs scores to distinguish scientific work while remaining stable under stylistic changes. The study measures both requirements, because a reviewer that gives every paper the same score would appear stable while becoming useless.

The [preprint](https://arxiv.org/abs/2609.39027), first submitted on 30 September, introduces RobustReview, a collection built from 60 anonymized submissions to ICLR, a machine-learning conference. Each original receives ten kinds of rhetorical rewrite generated separately by two models, yielding 1,260 manuscript versions.

The interventions alter such features as novelty claims, evidence framing, technical register and linguistic complexity. Other variants combine those changes or repeat the rewriting process. The intended intervention changes presentation while preserving the underlying methods, results and limitations.

The authors evaluate 30 reviewer configurations, including general models under different prompts, specialized scientific reviewers and agent-based review systems. They find that repeated instructions to focus on content do not consistently eliminate sensitivity to wording. A stricter prompt also changes which scientific differences the reviewer recognizes.

SciCore tackles the input as well as the instruction. One branch reviews the full manuscript. A second extracts the reported problem, claims, methods, assumptions, evidence, results and limitations into a structured record, then reviews that record directly. The final score averages the two judgments.

The structure resembles assessing both a proposal and its evidence sheet. The proposal preserves how the argument is communicated; the evidence sheet makes its scientific commitments easier to compare across differently worded versions. Extraction still requires interpretation, so errors in that sheet can influence the result.

## Stable scores must still separate different papers

The benchmark checks movement within each manuscript family and separation between different papers. It also compares original-manuscript scores with the human reviewers’ averages. Those are separate tests: agreement with humans on an original says little about whether a rewrite will change the model’s decision.

In the primary GPT-5.5 experiment, SciCore improved all five robustness measures compared with the strict full-manuscript branch alone. It also preserved competitive agreement with human scores. The combined reviewer did not lead every individual measure, and strict GPT-5.5 retained a stronger correlation with human rankings.

That result supports combining complementary views rather than selecting the apparently most stable component. The science-record branch moved less under rewrites but agreed less closely with human scores. Adding the full manuscript recovered information that the structured view had omitted or handled differently.

The general-model comparison includes GPT-5.5, GPT-5-mini, Claude Sonnet 5, GLM-5.2, Kimi-K2.6, GPT-OSS-120B, Gemini-3.5-Flash-Lite and Qwen-3.5-Flash. The rewriting models are GPT-5.5 and Claude Opus 4.8. Those choices matter because the tested system both interprets the original science and helps generate its altered presentation.

The evaluation remains the authors’ own preprint experiment. Its manuscript sample comes from one conference, and content-preserving rewrites do sometimes introduce mismatches. Human mean scores are also an imperfect reference that conceals reviewer disagreement. These boundaries constrain how far the measured stability can be generalized.

The final fused reviewer was tested with GPT-5.5. Additional cross-model experiments characterize the science-record branch, rather than establishing the complete fusion’s performance across every model. Extracting the record adds inference cost and can omit or misread details.

The team provides its [benchmark and method repository](https://github.com/c-steve-wang/Robust_Review). Its findings make one remaining issue concrete: improved resistance to wording depends on preserving the scientific distinctions that justify different scores in the first place.

## Verification

| Claim | Label | Primary source | Independent check |
|---|---|---|---|
| Wang, Li and collaborators’ listed affiliations; v1 submitted 30 September 2026. | VERIFIED | https://arxiv.org/abs/2609.39027 | none |
| RobustReview: 60 ICLR manuscripts, 10 rewrite conditions, two generators, 1,260 versions; 30 reviewer configurations. | VENDOR-REPORTED | https://arxiv.org/abs/2609.39027 | none |
| Named general reviewers, GPT-5.5/Opus 4.8 rewrite models and comparison families. | VERIFIED | https://arxiv.org/abs/2609.39027 | none |
| Dual-branch extraction/review/mean-score method; persistent content prompts do not consistently improve robustness. | VENDOR-REPORTED | https://arxiv.org/abs/2609.39027 | none |
| GPT-5.5 fusion improves all five robustness metrics over Manuscript-Strict; ICC 0.775, SPR 0.652, discrimination 0.726; human MAE 1.072, correlation 0.488; not best every metric. | VENDOR-REPORTED | https://arxiv.org/abs/2609.39027 | none |
| Conference/rewrite/human-score limits; fusion evaluated only with GPT-5.5; extraction cost and omission risk. | VERIFIED | https://arxiv.org/abs/2609.39027 | none |
| Repository supplied. | VERIFIED | https://github.com/c-steve-wang/Robust_Review | none |
| Organizer consequence, constant-score failure and proposal/evidence-sheet comparison explain joint stability and discrimination. | ANALYSIS | https://arxiv.org/abs/2609.39027 | none |
