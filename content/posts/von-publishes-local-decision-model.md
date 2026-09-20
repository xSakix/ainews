+++
date = '2026-09-20T04:05:00+02:00'
draft = false
title = 'Von Publishes a Local Decision Model'
+++

After reading this, the reader knows what Von does, how its published results compare with Jev and which claims still need independent testing.

# Von Publishes a Local Decision Model

*The 395-million-parameter model scores bounded choices locally instead of generating prose, but its own published table does not support every launch claim.*

An independent developer has released Von-1.0, an Apache-2.0 model for making bounded decisions from text. It is presented as a local alternative to proprietary decision APIs such as TypeSafe's Jev.

Von is not a small chatbot. It uses a bidirectional ModernBERT-large encoder to score supplied options without generating an answer token by token. An application can ask it to route a support ticket, judge whether a condition is true or assign an ordinal score. The result is a permitted value plus probabilities rather than free-form prose.

## Why it matters

Many software teams currently use general language models for classification. They request JSON, wait for a generated response, validate the schema and retry when the output is malformed. A decision model can remove the generation and parsing steps because the answer space is fixed before inference begins.

That narrower contract can be useful when a workflow needs one of five queues, a yes-or-no risk flag or a score on a known scale. It does not make the decision correct. The model can still choose the wrong option, express misleading confidence or fail when real inputs differ from its training data.

The model card lists a 395-million-parameter encoder, an 8,192-token context and a training corpus of 250,000 balanced examples drawn from established natural-language-inference datasets. It says the model was trained with a combined cross-entropy and Brier-score objective intended to improve both classification accuracy and probability calibration.

Published latency ranges depend heavily on hardware. Von's card reports about 62 milliseconds on Apple GPU hardware and about 300 milliseconds on CPU for its benchmark setup. A launch post says the model can run with 1–2 GB of memory and does not require a GPU. Those figures make local evaluation plausible, but they do not guarantee the same speed inside a production service.

## The benchmark needs careful reading

The model card reports 93.0% macro accuracy and 92.3% micro accuracy across eight tasks and 78 cases. In the same table, hosted Jev scores 97.2% and 97.4%, respectively. Von beats the open GLiNER2 baseline in that comparison, but it does not beat Jev overall.

This matters because the accompanying Reddit launch post says Von beats Jev in all benchmarks. The detailed task table shows a more mixed result: Von leads on incident severity, ties on several tasks and trails Jev on others. The card is the better source because it exposes per-task numbers and a reproducible model artifact.

The evaluation remains small. Seventy-eight cases cannot establish reliability across languages, organizations or changing business policies. The benchmark also compares local hardware latency with a remote API, so network and service overhead are mixed with model computation.

The useful next step is not another aggregate leaderboard. Teams should test Von against their own labeled decisions, include an abstain or escalation path, measure calibration after deployment and track errors by category. They should also compare total operating cost, not describe self-hosted inference as literally free.

Von adds a testable option to a rapidly growing category of specialized decision models. Its strongest contribution is the open checkpoint and bounded interface. Its strongest performance claims remain developer-reported and should be reproduced before the model controls consequential workflows.

## Verification

- **Tier 0 — VERIFIED:** Von-1.0's model card and weights are public under Apache 2.0. Primary source: https://huggingface.co/wfzyx/von-1.0
- **Tier 0 — VERIFIED:** The card specifies a 395M ModernBERT encoder, 8,192-token context and reported CPU and Apple-GPU latency. Same primary source.
- **Tier 1 — DEVELOPER-REPORTED:** Accuracy, calibration, memory and speed figures were published by the developer and were not independently reproduced here. Same primary source; launch context: https://www.reddit.com/r/LocalLLM/comments/1wkrrlp/von_opensource_395m_system_one_model/
- **Tier 0 — VERIFIED:** The published aggregate table places Von below Jev and above GLiNER2 on that 78-case suite. Same primary source.
- **Tier 2 — ANALYSIS:** Production-fit and evaluation recommendations are editorial analysis.

## Glossary candidates

- **Brier score:** A measure of how close predicted probabilities are to actual outcomes.
- **Non-autoregressive model:** A model that produces scores without generating an output sequence one token at a time.

Cold-reader sentence: Von is an open local model for bounded decisions, but its broad performance claims exceed what its small published benchmark demonstrates.
