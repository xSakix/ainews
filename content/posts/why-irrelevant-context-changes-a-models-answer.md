+++
title = "Why irrelevant context changes a model's answer"
description = "A new mechanistic study follows irrelevant prompt text through a language model. It finds a distinct route that can distort an answer even when the extra text supplies no competing evidence."
tags = ["research", "agents"]
date = 2026-11-06T04:12:00+01:00
draft = false
+++

Imagine an analyst asking a model for the capital of a country after a retrieval system has pasted in a paragraph about a different place. The paragraph does not contain a rival capital. It does not contradict the question. It is simply unrelated. Yet the model becomes less likely to give the answer that it already knew.

That scene is illustrative, but the failure is familiar to anyone who has built a retrieval system or a long-context agent. More context can make an answer worse. A new preprint by Dikshant Kukreja, Gautam Gupta, Avni Mittal and their colleagues tries to explain why at the level of the model's internal computation. Their answer is an “intrusion pathway”: irrelevant text is enriched, copied forward and then promoted by a small set of attention heads.

The distinction matters because most defences treat distracting context as a problem of better retrieval, stronger instructions or larger context windows. The paper asks a different question. Once irrelevant text is already in the prompt, which parts of the model let it influence the answer?

## A distractor without a false answer

The researchers begin with factual relations that open-weight models know, such as a person and an associated attribute. They construct clean prompts and several kinds of extra context: related evidence, counterfactual evidence, short irrelevant text, long irrelevant text and random text. Their canonical dataset contains 250 facts that at least three of four base models answer correctly.

This design separates contradiction from intrusion. A counterfactual passage can pull a model toward a specific wrong answer. Irrelevant prose does not need to do that. It can lower the probability of the correct answer merely by entering the computation at the wrong places.

The experiments use Llama 3.1 8B, Mistral 7B, Qwen 2.5 7B, Pythia 6.9B and GPT-2 XL, with additional larger models for one mathematics test. No model is trained. The public repository contains the scripts that build the datasets, select the implicated heads and reproduce the interventions.

The first important result is where the damage appears. Feed-forward layers enrich representations of both the subject of the question and tokens from the irrelevant passage. Some attention heads then copy material from the prefix toward the final position, where the model must predict the answer. The authors call these parroting heads. A second, sparse group of heads turns that imported material into pressure on the output distribution.

## Retrieval and intrusion are not the same circuit

The authors distinguish retrieval heads, which help move relevant evidence, from intrusion heads, which carry the unwanted effect. The sets mostly do not overlap. That makes the result more useful than a general claim that attention is noisy. A system may need the machinery that brings evidence forward while still benefiting from suppressing the separate route that promotes distractors.

The paper tests causality rather than relying only on correlations between attention patterns and errors. When the researchers replace the final residual state from a distracted run with the corresponding state from a clean run, they recover 97.6 percent of the accuracy drop. This is an oracle intervention: it requires a clean second pass, so it is not a practical production defence. It does show that the relevant damage has reached the last-token state.

They also mask selected intrusion heads. That intervention is deployable in principle because it does not require a clean reference run. The authors evaluate it on held-out relations and on several downstream tasks, including HotpotQA, PubMedQA and arithmetic datasets with distracting statements. They also test whether head sets transfer across models and between base and instruction-tuned versions.

The defence is not free. Removing attention heads can also remove useful computation, and the choice of how many heads to suppress matters. The repository therefore includes sweeps over the number of heads and the selection threshold, along with held-out stability tests. This is not a universal switch that makes context safe. It is a method for identifying a narrower trade-off.

## Why this changes context engineering

Retrieval-augmented generation often treats relevance as a search problem. A retriever ranks passages, a prompt builder chooses how many to include, and the model is expected to ignore the rest. The new work shows why that final assumption can fail. Text can influence an answer without supplying evidence and without winning a direct contest against the truth.

That makes “the answer was somewhere in the context” an incomplete diagnosis. A long prompt can contain the right document and still reduce accuracy because unrelated passages activate a separate route. The authors' downstream tests connect the circuit analysis to tasks in which models must answer questions or reason through added statements.

The work also puts a limit on a common response to context failures: telling the model to disregard irrelevant information. Instructions act through the same model that is already processing the distractor. A mechanistic intervention can test whether the harmful route remains active even when the model appears to follow the instruction.

There are important boundaries. The models are open-weight systems whose internal activations can be inspected and changed. The clearest circuit work focuses on models that are far smaller than today's largest frontier systems. The factual datasets are controlled, and the oracle recovery result cannot be deployed as written. The paper is a preprint and has not been peer reviewed.

Still, the evidence is unusually inspectable. The repository names the models, datasets, scripts, head-selection procedure and intervention sweeps. Other researchers can ask whether the same separation between retrieval and intrusion appears in different architectures, larger models and real production traces.

An illustrative engineering team could now debug a failed answer in two stages. First it would ask whether retrieval supplied the necessary evidence. Then it would ask whether irrelevant passages altered the internal route to the answer. The second question does not replace better search. It explains why better search and fewer, cleaner passages can matter even when the model seems capable of ignoring noise.

The larger lesson is simple: context is not inert storage. Every extra passage becomes part of a computation. Kukreja and colleagues have provided a map of one route through which the wrong passage can matter without ever stating a wrong answer.

## References

- Dikshant Kukreja, Gautam Gupta, Avni Mittal et al., “The Intrusion Pathway: How Non-Evidential Context Degrades Language Model Performance” — https://arxiv.org/abs/2611.07778
- Dikshant Kukreja et al., code and reproduction guide for “The Intrusion Pathway” — https://github.com/dk4248/the-intrusion-pathway
- TransformerLens contributors, “TransformerLens” — https://github.com/TransformerLensOrg/TransformerLens
- Javier Hernandez et al., relations dataset used for factual-recall experiments — https://github.com/evandez/relations
- Freda Shi et al., “GSM-IC: A Benchmark for Understanding the Effects of Irrelevant Context in Mathematical Reasoning” dataset — https://github.com/google-research-datasets/GSM-IC
