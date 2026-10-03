+++
title = "Reka releases camera-motion models trained on games"
description = "Two small inverse-dynamics models infer movement controls from video. Reka supplies weights, scripts and real-video failure examples."
tags = ["models", "research", "tools"]
date = 2026-10-03T05:56:20+02:00
draft = false
+++

Reka, an AI model developer, released two small models that infer camera-motion controls from video, using game-generated training labels to test how well that skill transfers to real footage.

The [model repository](https://huggingface.co/RekaAI/Reka-Inverse-Dynamics-Model), created on 1 October, contains a model that reads optical flow, the movement between frames, and another that reads the frames themselves. Both estimate movement keys and camera rotation rather than describing a scene in words.

**Why it matters:** A developer studying interactive video models gets downloadable weights and inference scripts for recovering actions from recorded movement. Reka also supplies a concrete failure example, making the boundary between camera motion and actual movement visible.

Reka reports that the optical-flow model correctly identified turn direction in about 92% of 47 real-video turn clips, compared with about 51% for the raw-frame model. The flow model contains roughly 2.8 million parameters including a frozen motion extractor; the raw-frame model has roughly 9.8 million. The comparison favors the smaller model on those clips, but comes from Reka's own preliminary evaluation.

The training labels came from 4,071 recorded game plays. The game engine supplied keys, mouse movements and camera angles, avoiding manual labeling. The two models were trained on one NVIDIA L4 GPU, according to the card. The flow model produces one prediction per 17-frame window; the raw-frame model predicts at each frame.

The release includes separate settings for game footage and walking videos, plus a sample clip and expected JSON output for a smoke test. A failure video shows the camera standing still while panning: the flow model repeatedly assigns high probability to the walking key. Motion cues alone can therefore lead this model to confuse turning a stationary camera with movement.

The code and model weights use Apache 2.0. The frozen optical-flow component uses separately licensed BSD-3 weights, while the walking-video examples retain CC BY 3.0 licensing. Reka calls this a preliminary release; the repository provides both model folders, dependency versions and the failure clip for further inspection.

## Verification

| Claim | Label | Primary source | Independent check |
|---|---|---|---|
| Reka published two camera-motion models with weights, code, sample outputs and failure videos; repository creation was 1 October. | VERIFIED | [Repository and model card](https://huggingface.co/RekaAI/Reka-Inverse-Dynamics-Model) | none |
| Flow-model turn accuracy is 91.5% on 47 real-video turn clips; raw-frame accuracy is 51.1%. | VENDOR-REPORTED | [Model-card results](https://huggingface.co/RekaAI/Reka-Inverse-Dynamics-Model) | none |
| Flow has 1,795,337 trained plus 990,162 frozen parameters (2,785,499 total); raw-frame has 9,836,063. Training used 4,071 game plays and one L4 GPU. | VENDOR-REPORTED | [Architecture and training data](https://huggingface.co/RekaAI/Reka-Inverse-Dynamics-Model) | none |
| Flow predicts per 17-frame window, raw-frame per frame; configuration, JSON sample and smoke test are supplied. | VERIFIED | [Release files](https://huggingface.co/RekaAI/Reka-Inverse-Dynamics-Model) | none |
| The failure clip assigns walking-key probabilities 0.72–0.98 to a stationary camera pan, illustrating motion confusion. | VENDOR-REPORTED | [Documented failure](https://huggingface.co/RekaAI/Reka-Inverse-Dynamics-Model) | none |
| Code and weights use Apache 2.0; RAFT-small weights use BSD-3 and examples CC BY 3.0. The release is preliminary. | VERIFIED | [Licence and status](https://huggingface.co/RekaAI/Reka-Inverse-Dynamics-Model) | none |
| Inspectable weights and failure examples give interactive-video developers a starting point for action recovery. | ANALYSIS | [Release artefacts](https://huggingface.co/RekaAI/Reka-Inverse-Dynamics-Model) | none |
