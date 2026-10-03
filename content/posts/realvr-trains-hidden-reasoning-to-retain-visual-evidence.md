+++
title = "ReaLVR trains hidden reasoning to retain visual evidence"
description = "A visual-reasoning study targets the information held between seeing an image and answering a question. Its training method makes those hidden states more sensitive to relevant image changes."
tags = ["research", "models"]
date = 2026-10-03T09:44:58+02:00
draft = false
+++

ReaLVR teaches a vision-language model’s hidden reasoning steps to retain the image evidence needed for its answer, improving accuracy across the model families tested by its authors.

Xi Xiao of the University of Alabama at Birmingham and Amazon AGI, with colleagues at Amazon AGI, examines models that reason through internal numerical states instead of written steps. Their 28 September [preprint](https://arxiv.org/abs/2609.34563) asks whether those states actually preserve the visual detail that determines an answer.

**Why it matters:** A researcher developing visual reasoning cannot tell from a correct final answer alone whether the model used the decisive image evidence. ReaLVR connects training feedback to that evidence inside the model, making the intermediate computation itself part of the learning target.

The authors’ clearest diagnosis comes from edited images. Changes to colour, object presence, shape or relative position changed the correct answer in roughly four out of five paired examples, but the baseline changed its prediction in only about 6–13% of them. Much of its internal reasoning remained insensitive to the relevant change.

The baseline first learns with visual targets supplied during training. Later, it generates its own hidden states and receives rewards for its final answer. The authors argue that this transition leaves too little guidance about which image information those self-generated states should preserve.

ReaLVR supplies two comparisons during training. One contrasts the relevant part of the image with visual information from mismatched examples. The other contrasts how a correct answer and the model’s own wrong answers draw on the hidden states. Together, they specify what information to retain and where to strengthen its representation.

The mechanism resembles improving a person’s working notes while checking a diagram: feedback identifies both the detail that belongs in the notes and the note the final conclusion actually relies on. The model’s notes are numerical states, however, so this comparison describes their role rather than a readable internal monologue.

The answer comparisons happen after the hidden sequence has been generated. They guide training; the system does not receive the correct answer before constructing its reasoning at inference. The authors keep the architecture and inference procedure unchanged, concentrating the intervention on how the existing model learns.

## Accuracy and internal dependence improve together

ReaLVR reaches about 64% average accuracy across five visual benchmarks on Qwen2.5-VL-7B. The ordinary reinforcement-trained latent-reasoning baseline reaches about 60%, while the strongest competing latent method averages about 63%. These are the authors’ three-seed comparisons, covering visual discrimination, spatial reasoning and high-resolution image tasks.

The strongest average does not mean a win on every task. A competing method scores better on two of the five benchmarks, which limits the claim to the combined result. The comparisons also separate gains over a simpler baseline from the smaller improvement over a stronger competitor.

The researchers test whether the improved hidden states influence the answer. Replacing the most answer-attended states while holding the surrounding context fixed produces a larger drop in correct-answer probability with ReaLVR than with the baseline. That intervention supports local dependence on the selected states, beyond an attention visualisation alone.

The broader evaluation spans six backbones across three model families. It includes a model with 235 billion total parameters, where the authors report improvements on the three benchmarks evaluated. They omit the two high-resolution tests at that size, so its results cannot be compared as the same five-task average.

The training target is less precise when the data lack marked image regions: ReaLVR then uses a whole-image target. Its tests also retain a preset number of hidden reasoning steps. Those constraints leave questions about how well the method selects evidence without detailed annotations and adjusts effort to each question.

The work is an author-reported preprint, with no independent reproduction established here. Its next stated directions are finer evidence targets from weaker supervision and a reasoning budget that adapts to the question, extending the same link between the image, intermediate computation and answer.

## Verification

| Claim | Label | Primary source | Independent check |
|---|---|---|---|
| Xi Xiao: UAB/Amazon AGI; co-authors Amazon AGI; v1 28 September 2026. | VERIFIED | https://arxiv.org/abs/2609.34563 | none |
| Correct answer changes in 81.45–86.33% of edited pairs; LVR prediction changes in 5.66–13.09%; four edit types, 512 pairs each. | VENDOR-REPORTED | https://arxiv.org/abs/2609.34563 | none |
| Training uses correct/wrong answer readout contrast and relevant/mismatched visual evidence; hidden states generated before answer branches; architecture and inference unchanged. | VERIFIED | https://arxiv.org/abs/2609.34563 | none |
| Qwen2.5-VL-7B five-task means: ReaLVR 63.7, LVR-RL 60.4, ILVR 62.9; three seeds; ILVR wins BLINK and HR-8K. | VENDOR-REPORTED | https://arxiv.org/abs/2609.34563 | none |
| Fixed-context top-eight-token replacement lowers correct-answer probability by 4 points in LVR and 11 points in ReaLVR; local intervention, not full causal identification. | VENDOR-REPORTED | https://arxiv.org/abs/2609.34563 | none |
| Six backbones/three families; 235B covers three benchmarks only; whole-image fallback without region labels; fixed latent budget; weaker supervision and adaptive budget future work. | VERIFIED | https://arxiv.org/abs/2609.34563 | none |
| Researcher consequence and working-notes analogy interpret the documented training mechanism. | ANALYSIS | https://arxiv.org/abs/2609.34563 | none |
