+++
title = "4MT-VLM shows vision models lose places after rotation"
description = "A preprint adapts a clinical spatial-memory test for 16 vision-language models. All of them can recognise a landscape from the angle they studied, but most fall to guessing once the camera moves."
tags = ["research", "models"]
date = 2026-10-06T04:02:31+02:00
draft = false
+++

Vision-language models recognise a landscape from the angle they first saw it, but most cannot pick it out once the camera moves, according to 4MT-VLM, a new benchmark adapted from a clinical test of spatial memory.

Markus Frey of Fraunhofer IAIS, a German applied-research institute, gave 16 open and closed models the puzzle used on human patients: study a computer-rendered landscape of four peaks, then find it among four similar landscapes shown from a new angle. A human volunteer solved about four in five rotated trials. Most models did no better than a guess.

## Why it matters

A robotics engineer who uses a vision-language model as the eyes of a mobile robot needs exactly this skill: recognising a room after the robot has turned around. The preprint finds that neither larger models nor more detailed instructions supply it.

## Recognition holds, rotation fails

The benchmark adapts the Four Mountains Test, which clinicians use because scores fall with damage to the hippocampus and in early Alzheimer's disease. Colours, textures and lighting change between the study image and the test images on every trial, so even a trial with no rotation cannot be solved by matching pixels. Frey treats accuracy on those unrotated trials as a check that a model can identify the place at all.

The models pass that check and then fail the rotation. OpenAI's GPT-5.6 Luna answered every unrotated trial correctly but only 31 percent of rotated ones, where guessing scores one in four. Pooled across all 16 models, the worst angle was 135 degrees, where accuracy fell clearly below chance.

A half-turn of 180 degrees, the largest change, scored better than 135 degrees. Frey reads that as a sign the models use an image shortcut, such as comparing against a mirror image of the scene, and do not rotate an internal map. The human comparison comes from a single participant, enough to show the task is solvable but not to give a human average.

## Bigger models recognise more, rotate no better

Scale improved recognition and left rotation where it was. In Alibaba's Qwen2.5-VL family, from 3 billion to 72 billion parameters, unrotated accuracy rose from 30 to 75 percent while rotated accuracy stayed at or below chance. The InternVL3.5 family repeated the pattern from 1 billion to 38 billion parameters. Across 14 open-weight models up to 235 billion parameters, none answered more than 31 percent of rotated trials correctly, and a "thinking" variant scored the same as its standard sibling.

Instructions did not close the gap. Frey ran Qwen2.5-VL-32B under six prompts, including explicit procedures such as imagining the layout from directly above or anchoring on the most distinctive peak. All six left it below chance.

## Spacing the wrong answers exposes a coarse map

The most informative experiment changed only the wrong answers. Frey measured, in metres, how far two landscapes' peaks sit from each other after the best possible rotation, then redrew the three decoys from more distant layouts while keeping the target and the angles identical.

Moving the nearest decoy from about 7 metres to about 31 metres away lifted Google's Gemini 3.8 Flash from 39 to 85 percent on rotated trials and GPT-5.6 Luna from 31 to 55 percent. No open model improved by a statistically meaningful amount.

That is the paper's evidence that frontier models hold some sense of layout, only at low resolution. A model with no map could not gain from spacing the decoys, and a model with a human-grade map would not need 30 metres of separation. The effect resembles recognising your town from an aircraft window but not your street.

The errors point the same way. A person who answers wrongly tends to choose the decoy whose layout is closest to the target. The models' wrong answers were spread almost evenly across near and far decoys, as if layout played no part in the choice.

## A synthetic, single-author test

The landscapes are synthetic renders, and Frey notes that pretraining on similar rendered scenes could favour some models. Closed models' parameter counts are undisclosed, so the scaling evidence rests on open models alone. The preprint, posted to arXiv on 30 September 2026, has one author and links no code or dataset.

Frey says more human participants are being tested, which will give the volunteer's 82 percent score on rotated trials a proper comparison group.

## Verification

| Claim | Label | Primary source | Independent check |
| --- | --- | --- | --- |
| 4MT-VLM adapts the Four Mountains Test; 500 trials over 100 generated landscapes, 16 models tested | VERIFIED | [Frey preprint](https://arxiv.org/abs/2609.39238) | none; author's own benchmark |
| Appearance is resampled between study and test images at every angle | VERIFIED | [Frey preprint](https://arxiv.org/abs/2609.39238) | none; method description |
| One human participant answered 100% of unrotated and 82% of rotated trials | VENDOR-REPORTED | [Frey preprint](https://arxiv.org/abs/2609.39238) | none; one participant only |
| GPT-5.6 Luna: 100% unrotated, 31% rotated; chance is 25% | VENDOR-REPORTED | [Frey preprint](https://arxiv.org/abs/2609.39238) | none |
| Pooled accuracy at 135 degrees is 15.0% (48/320), below chance; 23% at 180 degrees | VENDOR-REPORTED | [Frey preprint](https://arxiv.org/abs/2609.39238) | none |
| Models use an image shortcut such as mirror matching | ANALYSIS | [Frey preprint](https://arxiv.org/abs/2609.39238) | author's interpretation of the 135/180-degree pattern |
| Qwen2.5-VL 3B to 72B: unrotated 30% to 75%, rotated 29%, 31%, 18%, 20% | VENDOR-REPORTED | [Frey preprint](https://arxiv.org/abs/2609.39238) | none |
| No open-weight model (1B to 235B) exceeds 31% rotated; thinking variant matches instruct at 19% rotated | VENDOR-REPORTED | [Frey preprint](https://arxiv.org/abs/2609.39238) | none |
| Six instruction styles leave Qwen2.5-VL-32B at 13.8% to 23.8%, all below chance | VENDOR-REPORTED | [Frey preprint](https://arxiv.org/abs/2609.39238) | none |
| Median nearest-decoy distance 6.8 m to 31.4 m: Gemini 3.8 Flash 39% to 85%, GPT-5.6 Luna 31% to 55% | VENDOR-REPORTED | [Frey preprint](https://arxiv.org/abs/2609.39238) | none |
| No open model changes significantly with wider decoy spacing | VENDOR-REPORTED | [Frey preprint](https://arxiv.org/abs/2609.39238) | none |
| Model errors split 30/37/33 across nearest, middle and farthest decoys; the human chose the nearest in 10 of 14 errors | VENDOR-REPORTED | [Frey preprint](https://arxiv.org/abs/2609.39238) | none |
| Frontier models hold a coarse layout representation | ANALYSIS | [Frey preprint](https://arxiv.org/abs/2609.39238) | inference from the decoy-spacing result |
| Single-author preprint posted 30 September 2026; author at Fraunhofer IAIS; no code or data linked | VERIFIED | [arXiv record](https://arxiv.org/abs/2609.39238) | arXiv metadata and author e-mail domain |
| More human participants are being evaluated | VENDOR-REPORTED | [Frey preprint](https://arxiv.org/abs/2609.39238) | none |
