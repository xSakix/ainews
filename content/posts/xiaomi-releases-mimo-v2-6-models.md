+++
date = '2026-09-22T04:00:20+02:00'
draft = false
title = 'Xiaomi Releases MiMo-V2.6 Models'
+++

*Xiaomi released its MiMo-V2.6 family on 21 September, pairing a large Pro model with a smaller open-weight Flash checkpoint for multimodal agent work.*

Xiaomi MiMo, the company's artificial-intelligence lab, has published Pro and Flash models that accept text, images, video and audio. Both advertise a one-million-token context window and are designed for coding and tool-using agents. The release matters because it combines a very large hosted model with downloadable weights for the smaller variant.

## Why it matters

The family gives developers two different deployment choices. MiMo-V2.6-Pro targets maximum capability through a model with more than one trillion total parameters. MiMo-V2.6-Flash uses 309 billion total parameters while activating 15 billion for each token, reducing the amount of computation used on any one step.

That design is called a mixture of experts. It resembles a large office in which only the relevant specialists are called into each meeting. The total organization can be large while the active group stays smaller. Memory, serving software and hardware requirements still matter, and “active parameters” should not be mistaken for the model's total storage footprint.

Xiaomi says the models use one reinforcement-learning run across coding, general agents, visual work and cybersecurity. Its model cards describe training across several agent harnesses so strategies can transfer to tool setups that were not present in training. This is the company's account of the method; outside evaluations have not yet tested how well the transfer holds.

## Open weights do not mean easy deployment

The Flash-RL checkpoint is available through Xiaomi's Hugging Face account, with instructions for vLLM and SGLang. Those tools can expose an OpenAI-compatible API. The model card also points to quantized versions for local runtimes, but a 309-billion-parameter model remains demanding even when only part of it runs for each token.

MiMo-V2.6-Pro is also documented on Hugging Face, while hosted providers list Pro and an UltraSpeed variant. Xiaomi says UltraSpeed comes from the same Pro checkpoint and produces roughly ten times the output speed. That speed claim should be tested on identical hardware and workloads before it guides purchasing.

The model cards emphasize a one-million-token context window. Long context can hold large repositories or tool traces, but capacity alone does not prove that the model will recall distant details or use them correctly. Teams should test retrieval accuracy at realistic document lengths, not only whether an input is accepted.

The most useful follow-up will be independent evaluation of the released checkpoints, including license review, memory requirements and task-level cost. Xiaomi has made enough material public for those tests to begin. Until they do, its benchmark rankings and speed comparisons remain vendor evidence.

## Verification

1. **VERIFIED — Xiaomi announced MiMo-V2.6-Pro and MiMo-V2.6-Flash on 21 September 2026.** Primary sources: https://mimo.xiaomi.com/mimo-v2-6 and https://x.com/XiaomiMiMo/status/2102138559952290106
2. **VERIFIED — Official model cards describe native multimodal input and a one-million-token context window.** Primary sources: https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL and https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Flash-RL
3. **VERIFIED AS A VENDOR CLAIM — Flash has 309B total and 15B active parameters; Pro is above one trillion total parameters.** Primary sources: the official Xiaomi model cards above.
4. **PARTIALLY VERIFIED — Xiaomi describes mixed-domain reinforcement learning and cross-harness transfer; independent confirmation is not yet available.** Primary source: https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL
5. **PARTIALLY VERIFIED — The UltraSpeed speed comparison is a provider and vendor claim.** Primary source: https://mimo.xiaomi.com/mimo-v2-6

## Glossary candidates

- **Open weights:** Model parameter files that users can download under stated license terms.
- **Mixture of experts:** An architecture that activates selected model components for each token.
- **Context window:** The amount of input and output a model can process in one session.

Cold-reader sentence: Xiaomi released multimodal MiMo-V2.6 models, including an open-weight Flash checkpoint, while its performance and speed claims await independent testing.
