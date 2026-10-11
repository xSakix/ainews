+++
title = "H2O.ai Releases H2O-Lightning-31B"
description = "The open-weight decision model answers bounded questions in one forward pass and returns probabilities. Its strongest speed and accuracy figures come from H2O.ai's own tests."
tags = ["models", "tools"]
date = 2026-10-11T04:06:06+02:00
draft = false
+++

H2O.ai has released H2O-Lightning-31B, an open-weight model built to answer bounded decision questions with probabilities instead of generating free-form prose.

The model is based on Gemma 4 31B-it and accepts text plus as many as four images. Its interface covers choices, yes-or-no questions and ordered scores, returning one result in a single forward pass. H2O.ai published the weights, model card and serving code on Hugging Face.

## Why it matters

For a developer using a large chatbot to route tickets, score records or select a tool, constrained output can remove several fragile steps: prompting for JSON, parsing it, rejecting malformed answers and asking again. A probability also exposes how close the choice was, although it is useful only when the model is calibrated for the intended data.

H2O.ai reports that the 31-billion-parameter model answered 212 of 231 public JevBench questions correctly. In its image evaluation, the fine-tuned model scored 88.4% across 1,877 questions, compared with 88.0% for the frozen Gemma base. The model card's uncertainty interval includes no improvement, so that image result does not establish a reliable gain over the base model.

The company also reports median latency of about 25 milliseconds when loading the model in FP8 on one NVIDIA H100. That figure comes from its own setup, with prefix caching disabled, and the card provides no measurement for smaller GPUs. The published bfloat16 files total about 63 GB before runtime overhead.

The release runs on unmodified vLLM 0.30.0 behind H2O.ai's `/v1/systemone` shim. Long records are not processed in full: a retrieval stage cuts them to 3,000 tokens before inference. That boundary matters because a decision can only reflect evidence the retrieval step preserves.

The weights carry Apache 2.0 alongside Google's Gemma terms. H2O.ai's notice specifically points to Gemma's prohibited-use restrictions on automated decisions that affect individual rights, so the open files do not make every deployment permissible.

H2O.ai also updated its earlier 4B sibling with revised latency measurements and a GGUF package for llama.cpp. The 31B release is available now through the Hugging Face model page; independent latency, calibration and task-quality tests have not yet been published.

## Verification

| Claim | Label | Primary source | Independent check |
|---|---|---|---|
| H2O.ai released H2O-Lightning-31B with weights, a model card and serving code | VERIFIED | https://huggingface.co/h2oai/h2o-lightning-31b | none |
| The model supports bounded text-and-image decisions and returns probabilities in one forward pass | VERIFIED | https://huggingface.co/h2oai/h2o-lightning-31b | none |
| It scored 212 of 231 JevBench items and about 25 ms median latency on one H100 | VENDOR-REPORTED | https://huggingface.co/h2oai/h2o-lightning-31b | none |
| Its image evaluation did not show a statistically reliable gain over the frozen Gemma base | VERIFIED | https://huggingface.co/h2oai/h2o-lightning-31b | none |
| Gemma terms restrict automated decisions affecting individual rights | VERIFIED | https://huggingface.co/h2oai/h2o-lightning-31b | none |
