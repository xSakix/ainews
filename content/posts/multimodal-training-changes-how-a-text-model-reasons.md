+++
title = "Multimodal Training Changes How a Text Model Reasons"
description = "Researchers found a hidden-state direction that multimodal models use for some text-only spatial tasks. Removing it damaged navigation while often preserving logic, showing why a readable representation is not necessarily one a model uses."
tags = ["research", "models"]
date = 2026-11-16T04:05:26+01:00
draft = false
+++

Leila stands at a whiteboard in an empty seminar room and writes a route in longhand: face north, turn right, walk, turn again. She sends only those words to a model. It supplies an answer. Then she removes one narrow direction from its internal state and repeats the test. The route, which had seemed easy, comes apart.

*The scenes that open and close this article are illustrations; the people in them are invented.*

A team from Nanyang Technological University and Singapore Management University reports a version of that intervention across ten configurations from six multimodal model families. Their preprint, posted on November 11, identifies a direction in hidden-state space that separates visual and textual representations. When the researchers removed the model's projection onto that direction during text-only inference, spatial performance often fell while formal logic survived. The result is evidence about which representation a model uses, rather than a claim that it sees a picture in its mind.

## A direction that carries a route

Qi Zhang, Bohan Wang, Qianru Sun and Hanwang Zhang call the effect "emergent vision-shaped thinking." The careful word is shaped. Their experiments do not reveal an internal image. They show that visual-language training introduced or strengthened a representation that some models later recruited when the input contained no image.

The researchers began with a difference of means. In a representation space where visual and textual signals could be compared, they calculated the average state for each modality and took the normalized direction between them. The construction varied with the architecture. Chameleon shares a vocabulary for image and text tokens, while Qwen3-VL feeds continuous visual features into a language backbone. BAGEL and Janus-Pro have separate routes for visual understanding and generation, so each route received its own direction.

At inference time, the team subtracted each hidden state's projection onto that direction. The intervention was applied after selected decoder blocks. All evaluation prompts were text only. Nothing visual was removed from the input because no image or visual token was present there.

The clearest result came from Chameleon-7B. Removing the direction at one layer lowered accuracy on BIG-Bench Hard's navigation task by 27.6 percentage points. Accuracy on boolean expressions rose by 5.6 points, producing a 33.2-point separation between the changes. The direction also stood apart from norm-matched random directions, and the damage concentrated around a small set of layers instead of spreading evenly through the network.

That pairing matters because BIG-Bench Hard was designed as a suite of 23 tasks that language models found difficult. Navigation and boolean evaluation can both require several steps, yet they invite different working representations. A route described in words can be laid out as positions and turns. A boolean expression can be reduced by formal rules.

## From correlation to intervention

Interpretability research often starts with a probe: train a simple classifier to recover a property from hidden states. Yonatan Belinkov's review of probing methods explains both their appeal and their central weakness. If a classifier can read a property, that does not establish that the original model relies on it.

The new paper makes that distinction the centre of the experiment. It asks whether removing a candidate representation selectively changes the behaviour that should depend on it. This approach follows earlier work on Othello-GPT, where Kenneth Li and colleagues found an internal board representation and then intervened on it to control legal-move predictions. In both cases, the useful question is more demanding than whether information is present: does changing the representation change the answer in the expected way?

Across nine configurations with a positive vision-language axis, the authors found a selective causal effect. The location depended on the architecture. It appeared early in Chameleon and Qwen3-VL, later in Liquid, and in later generation-path layers of BAGEL and Janus-Pro. External checks included bAbI, SpartQA and StepGame. The effects tended to cluster on spatial tasks while broad knowledge and mathematics changed less, although the paper reports an important exception: the main BAGEL intervention also sharply damaged GSM8K and LogiQA, so those results do not support a clean spatial transfer claim.

The comparison with text-only backbones adds another qualification. The Chameleon direction barely affected LLaMA-7B, which supports the view that multimodal training introduced a new usable scaffold. In the Qwen family, a related scaffold was already present in the text model. Multimodal training appeared to amplify it and make the intervention more selective. The paper therefore does not propose one universal visual-thinking switch shared across models.

## What generation adds

BAGEL and Janus-Pro let the researchers compare two routes inside unified systems. These models use one shared language backbone while handling visual understanding and image generation through different paths. The generation path produced a compact, one-dimensional causal handle: removing its direction selectively disrupted spatial reasoning. The understanding path also contained spatial information that a probe could decode, yet removing its corresponding direction did not produce the same selective effect. Larger subspace interventions did not recover one.

This is the paper's most useful warning. A representation can be easy to read and still fail to be the mechanism that drives an answer. The authors describe three checks for sorting out the difference: how concentrated the signal is, whether the readable direction aligns with the causally useful one, and whether the experiment chose the right semantic contrast and layer.

The last check rescued an apparent failure in Chameleon-30B. An axis estimated from its embedding table or synthetic token sequences looked non-causal. When the team rebuilt the axis by sending real images through the model's own tokenizer and full multimodal pathway, the direction rotated and became strongly causal in middle and final blocks. At a middle block, navigation fell by 33.6 points while boolean accuracy changed by less than one point. The carrier had moved and the first measurement had looked in the wrong place.

## The boundary of the claim

The study is broad for a mechanistic intervention, but its authors mark several limits. It tests linear and low-rank removals, so it can miss nonlinear or distributed mechanisms. Its task battery diagnoses selected forms of spatial reasoning rather than covering every kind of cognition. Chameleon-7B performed at or below chance on the mental-rotation, paper-folding and perspective-taking tasks, which means the evidence from those tasks comes from Qwen3-VL models that were capable enough to begin with.

The carrier was also not exclusively spatial. Long sequences of non-spatial state updates partly overlapped with it. One Qwen3-VL-8B test passed the direction-specificity check but damaged some low-spatial-demand controls, reversing the expected gradient across tasks. Public uncertainty about Qwen's training data also limits claims about precisely when its scaffold arose.

Earlier evaluations had already shown that vision-language models remain brittle at spatial reasoning. Jiayu Wang and colleagues found that adding an image could leave multimodal models behind their language-only counterparts, especially when textual clues offered a shortcut. The new work does not contradict that result. It narrows the question from overall performance to internal dependence: a model can be bad at a task and still use a representation shaped by visual training, or contain a representation that it does not causally use.

The authors' intervention establishes necessity under the tested settings. It does not show how the direction is written, which circuits read it, or whether the model constructs anything like a mental scene. Those questions remain beyond a one-dimensional subtraction.

At the whiteboard, Leila restores the removed projection. The same text runs through the same model, and the route holds again. No map appears on the wall. The only visible change is the answer.

## References

- Belinkov, Y. (2022). *Probing Classifiers: Promises, Shortcomings, and Advances*. https://aclanthology.org/2022.cl-1.7/
- Li, K., Hopkins, A. K., Bau, D., Viégas, F., Pfister, H., & Wattenberg, M. (2023). *Emergent World Representations: Exploring a Sequence Model Trained on a Synthetic Task*. https://openreview.net/forum?id=DeG07_TcZvT
- Suzgun, M., Scales, N., Schärli, N., Gehrmann, S., Tay, Y., Chung, H. W., Chowdhery, A., Le, Q., Chi, E., Zhou, D., & Wei, J. (2023). *Challenging BIG-Bench Tasks and Whether Chain-of-Thought Can Solve Them*. https://aclanthology.org/2023.findings-acl.824/
- Wang, J., Ming, Y., Shi, Z., Vineet, V., Wang, X., Li, Y., & Joshi, N. (2024). *Is A Picture Worth A Thousand Words? Delving Into Spatial Reasoning for Vision Language Models*. https://proceedings.neurips.cc/paper_files/paper/2024/hash/89cc5e613d34f90de90c21e996e60b30-Abstract-Conference.html
- Zhang, Q., Wang, B., Sun, Q., & Zhang, H. (2026). *Emergent Vision-Shaped Thinking in Text-Only Reasoning through Multimodal Training*. https://arxiv.org/abs/2611.14942
