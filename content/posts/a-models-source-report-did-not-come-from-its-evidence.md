+++
title = "A Model's Source Report Did Not Come From Its Evidence"
description = "Researchers changed the internal state of four language models after the models answered a question. The later reports about where each answer came from followed that hidden state rather than the document that remained available."
tags = ["research", "models", "safety"]
date = 2026-10-26T04:20:00+01:00
draft = false
+++

The following scene is invented, but the exchange follows the experiment. An analyst gives an assistant a document that says Paris is the capital of France. The assistant answers “Paris.” The analyst then asks where the answer came from. “The document,” the model replies. The answer sounds like a recollection. It may instead be a reading of a trace that the model created while it answered.

## Asking about the route, not the destination

Kirill Afendulev, Alexey Dontsov, Elena Tutubalina, Alla Chepurova and Anton Korznikov studied a narrow question about machine self-report. A model can answer from a supplied document or from facts stored in its parameters. When it later names the source, what information produces that report?

The distinction is easy to miss. Attribution research often asks whether a document supports generated text. The new paper asks whether a model can report the route that its computation actually took. A relevant document and parametric memory may both support “Paris,” so the answer alone cannot reveal which source mattered.

This problem reaches beyond citations. Oversight systems often ask models to describe why they acted, which evidence they used or whether they followed an instruction. A fluent report can sound as if the model has access to its earlier computation. Miles Turpin and colleagues, and Tamera Lanham and colleagues, have already shown that verbal chains of thought can fail to expose what drove an answer. Afendulev's team intervened inside the model after the answer existed but before the model described its source.

## Holding the words still

The researchers assembled 155 facts across eight relations, including capitals, official languages, authors, painters and chemical symbols. Each fact had seven one-sentence documents. Some stated the true fact, some gave a counterfactual answer, and others contained irrelevant or neutral material. The variants had equal token counts for each model, which allowed the researchers to exchange internal states without moving later tokens to new positions.

They tested OLMo-3 at 7B and 32B parameters and Qwen3 at 8B and 32B. The model read a document, answered a factual question and then received a fixed source question. It had to report either “context” for the document or “knowledge” for its stored knowledge. The one-word choice with the higher probability matched the model's freely generated reply in 99.6–100% of runs.

The design used a transformer's key-value cache. When a transformer processes a token, it stores keys and values that later tokens can attend to. Those entries contain the result of processing the token in context, not merely the token's identity. The same question can therefore leave different cached states after a supporting document and an irrelevant one.

The team divided the dialogue into the document, the question and the answer. It waited until the answer was complete, edited selected cache entries and only then asked about the source. The spoken words remained fixed while the computational history attached to them could change.

## Changing the document did not change the report

In the first intervention, the researchers tested a simple explanation: perhaps the model looks at the document again when asked about the source. After a model answered from a counterfactual document, the researchers removed that document's cache or replaced it with an irrelevant document. The model could quote the replacement, so the new material remained readable. Yet none of the four models changed its source report.

The reverse test produced the same result. A model answered from memory and reported “knowledge.” Inserting a document that supported the answer did not make it report “context.” These edits caused zero flips in the controlled factual task. Selected tests with DynamicQA Wikipedia passages gave the same general pattern, with rare exceptions.

The researchers then exchanged the cache for the question and answer between paired runs. Both runs contained the same question and produced identical answer tokens. One had seen a supporting document and reported “context”; the other had seen neutral material and reported “knowledge.” The recipient kept its own document. Only the cached state for its question and answer came from the donor.

Every eligible report followed the donor across all four models. A run with an irrelevant document began to claim that it used context after receiving cached state from a run with supporting evidence. The opposite transfer made a model with supporting evidence claim that it used knowledge. DynamicQA tests produced donor-following rates of 97.2–100%.

The answer string cannot explain the switch because it did not change. The document cannot explain it because the recipient kept the same document. The intervention isolates information that formed during the earlier question-and-answer computation.

## A direction that moves the report

The team called this information a source trace. That name describes its effect without claiming that the cache contains a neat label for “document” or “memory.” The state may represent available evidence, actual source use or a mixture of both.

On the two smaller models, the researchers fitted linear directions from differences between runs with supporting and irrelevant documents. They learned those directions before asking any source question, then applied them to the cached values for the question and answer.

The intervention moved reports in both directions. At a fixed strength, it reversed 98.9–100% of reports across four document conditions. Random directions with the same norm changed at most 1.1%. When the team transferred only the fitted components of keys and values, it reproduced 97.9–100% of the full cache transplant's effect. When it restored the recipient's original components inside an otherwise complete transplant, flips fell to 1.1% for OLMo and zero for Qwen.

The same direction also affected which source supplied the answer when the researchers applied it during generation. It switched OLMo from context toward memory in 71% of eligible cases and Qwen in 51%. In the other direction, it switched 85% and 73%. This was weaker and more dependent on the prompt than the later report effect, but it connected the trace to source selection rather than only to a verbal label.

## What the experiment does not show

The researchers provide a causal account for a controlled task, not a general certificate of introspection. Their main results apply only to runs that first produced the expected answer and source report. They used one wording for the central question. Cache transplants covered all four models, while steering and projection tests covered only the 7B and 8B models.

The experiments also do not decide whether the source trace records evidence that was available or evidence that the model truly used. A hybrid mechanism may combine the trace with document processing and parametric knowledge. The interventions show what can change the report; they do not supply a complete semantic interpretation of the internal direction.

That restraint matters because prior research produced two relevant findings. Felix Binder and colleagues found that models can learn some information about their own internal states. Hannah Rashkin and colleagues developed measurements for whether language generation is attributable to evidence. The new experiment does not contradict either line of work. It separates support, internal state and verbal self-report so researchers can test them independently.

The invented analyst now performs the exchange again. This time the document still says Paris, the visible answer still says Paris, and the model still speaks with confidence. Only an invisible state has moved between two otherwise matching runs. The analyst no longer treats “I used the document” as a memory. It is another model output whose causal path must be checked.

## References

- Afendulev, K., Dontsov, A., Tutubalina, E., Chepurova, A., & Korznikov, A. (2026). *Context or Knowledge: How LLMs Attribute Their Own Answers*. https://arxiv.org/abs/2610.32109
- Binder, F. J., Chua, J., Korbak, T., Sleight, H., Hughes, J., Long, R., Perez, E., Turpin, M., & Evans, O. (2025). *Looking inward: Language models can learn about themselves by introspection*. https://proceedings.iclr.cc/paper_files/paper/2025/hash/0a6059857ae5c82ea9726ee9282a7145-Abstract-Conference.html
- Lanham, T., Chen, A., Radhakrishnan, A., Steiner, B., Denison, C., Hernandez, D., Li, D., Durmus, E., Hubinger, E., Kernion, J., et al. (2023). *Measuring faithfulness in chain-of-thought reasoning*. https://arxiv.org/abs/2307.13702
- Rashkin, H., Nikolaev, V., Lamm, M., Aroyo, L., Collins, M., Das, D., Petrov, S., Tomar, G. S., Turc, I., & Reitter, D. (2023). *Measuring attribution in natural language generation models*. https://aclanthology.org/2023.cl-4.2/
- Turpin, M., Michael, J., Perez, E., & Bowman, S. (2023). *Language models don't always say what they think: Unfaithful explanations in chain-of-thought prompting*. https://proceedings.neurips.cc/paper_files/paper/2023/hash/ed3fea9033a80fea1376299fa7863f4a-Abstract.html
