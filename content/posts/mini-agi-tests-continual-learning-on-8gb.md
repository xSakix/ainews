+++
date = '2026-09-22T04:00:20+02:00'
draft = false
title = 'Mini-AGI Tests Continual Learning on 8GB'
+++

*An open experiment called mini-AGI trains a byte-level language model on one 8GB GPU and keeps updating it as it reads, while warning that it remains a toy.*

Mini-AGI is a research repository, not a frontier assistant. Its author is testing whether a small model can keep learning from one stream of data without erasing earlier knowledge. The system stores expert weights as files, pages selected parts through memory and grows or removes capacity during training.

## Why it matters

Most downloadable language models are trained elsewhere and then frozen. Fine-tuning can adapt them, but repeated updates may cause catastrophic forgetting, where learning new material damages older capabilities. A model that learns continuously on modest hardware could support private, personal systems if the method remains stable at larger scale.

The project uses bytes rather than a fixed word-piece tokenizer. Text passes through two dense blocks and a recurrent block that can run repeatedly, selecting groups of experts at each step. A learned halting mechanism stops easy characters earlier and spends more computation on harder ones.

Weights and optimizer state live across disk, system memory and graphics memory. Before a chunk is processed, the system chooses a working set of experts for the GPU. This allows the total pool to exceed graphics memory, although frequent movement can reduce speed and disk capacity is not a substitute for compute.

## The experiment is deliberately limited

The author says the current model is toy-level and that trained weights are not yet published because the first corpus pass is still running. That warning is important. The repository demonstrates an architecture and training process; it does not provide a capable general assistant for download.

The central forgetting test reports that lowering the shared trunk's learning rate to one tenth of the experts' rate retained 99.84% of progress against chance after a focused chess-data probe. The project also says only part of the expert pool received gradients during that probe. These are project-run measurements on its own setup, not independent evidence that the method solves continual learning generally.

The repository also corrects one of its earlier interpretations. It says the expert pool alone did not prevent forgetting; slowing updates to the shared trunk produced most of the effect. That self-correction strengthens the documentation because it separates a measured result from the original narrative.

An 8GB requirement makes reproduction more accessible than large-model training, but the experiment still needs time, data preparation and careful monitoring. Its byte-level design may also behave differently from tokenized models commonly used in production.

The next useful milestones are published weights, repeat runs with controlled seeds and evaluations on held-out tasks beyond the project's corpus. Independent attempts should test whether learning a new domain preserves old performance and whether the same behavior holds as the expert pool grows.

## Verification

1. **VERIFIED — Mini-AGI describes a byte-level continual-learning model targeted at one 8GB CUDA GPU.** Primary source: https://github.com/volotat/mini-AGI/
2. **VERIFIED — The repository says the model is toy-level and its weights are not yet published.** Primary source: https://github.com/volotat/mini-AGI/
3. **VERIFIED AS PROJECT-REPORTED RESULTS — The 99.84% retention figure and gradient observations come from the author's tests.** Primary source: https://github.com/volotat/mini-AGI/
4. **VERIFIED — The project says a slower shared-trunk learning rate, not the expert pool alone, produced most of the anti-forgetting effect.** Primary source: https://github.com/volotat/mini-AGI/

## Glossary candidates

- **Continual learning:** Updating a model over time as new data arrives.
- **Catastrophic forgetting:** Loss of earlier skills after training on new material.
- **Working set:** The subset of model weights loaded for current computation.

Cold-reader sentence: Mini-AGI demonstrates continual-learning mechanisms on an 8GB GPU, but it remains a toy experiment with unpublished weights and self-reported results.
