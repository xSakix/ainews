+++
title = "EasyCommand runs English-to-Bash locally"
description = "The open-source command-line tool embeds llama.cpp and ships two small fine-tuned models. Its author also released the 401,975-pair training set and benchmark code."
tags = ["projects", "models", "tools"]
date = 2026-10-06T04:06:31+02:00
draft = false
+++

EasyCommand turns English requests into Bash commands with a small model that runs on a CPU, keeping the prompt and proposed command on the user's machine.

Developer Max Trivedi released the `ec` command-line application, two model families and a dataset of 401,975 deduplicated request-and-command pairs. The application embeds llama.cpp, previews its proposed command and can ask for confirmation before execution.

For a developer who needs an occasional shell reminder, local execution removes an API call from a sensitive part of the workflow. The trade-off is direct responsibility: the project warns that a plausible command can still be wrong and recommends starting in preview mode.

The released models start from Qwen2.5-Coder-1.5B-Instruct and Qwen3-0.6B. Both come as GGUF files for local inference, merged BF16 checkpoints and LoRA adapters for further training. The models and dataset use the Apache 2.0 licence; the application and benchmark code use MIT.

Trivedi says the 1.5-billion-parameter model solved 212 of 300 items in an updated version of the ALFA English-to-shell benchmark, compared with 191 for the earlier nl2sh system. That is an author-run comparison with different model prompts and settings, not an independent leaderboard result.

The release is unusually useful because it includes the failed edges as well as the model. Trivedi says the flat dataset does not reproduce the historical weighting used during training and has no official test split. He recommends holding out whole task families instead of randomly separating paraphrases, which could otherwise leak nearly identical commands into training and evaluation.

The target is GNU/Linux Bash rather than every shell or operating system. EasyCommand's repository is public now, and the author is asking users to contribute tests that expose unreliable transfer and missing command coverage.

## Verification

| Claim | Label | Primary source | Independent check |
| --- | --- | --- | --- |
| EasyCommand runs locally, embeds llama.cpp and previews commands before execution | VERIFIED | [Project write-up](https://dirac.run/posts/easycommand) | [public repository](https://github.com/dirac-run/ec) |
| The release includes 401,975 deduplicated English/Bash pairs | VERIFIED | [Project write-up](https://dirac.run/posts/easycommand) | dataset linked from repository |
| Models derive from Qwen2.5-Coder-1.5B and Qwen3-0.6B | VERIFIED | [Project write-up](https://dirac.run/posts/easycommand) | model artefacts linked from repository |
| The 1.5B model scored 212/300 versus nl2sh's 191/300 | VENDOR-REPORTED | [Project write-up](https://dirac.run/posts/easycommand) | none; author-run benchmark |
| Models and data are Apache-2.0; application and benchmark code are MIT | VERIFIED | [Project write-up](https://dirac.run/posts/easycommand) | repository licence files |
| The dataset has no official test split and does not preserve historical weighting | VENDOR-REPORTED | [Project write-up](https://dirac.run/posts/easycommand) | author disclosure |
