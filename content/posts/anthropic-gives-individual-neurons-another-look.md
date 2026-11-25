+++
title = "Anthropic Gives Individual Neurons Another Look"
description = "Anthropic researchers argue that a model's individual neurons are more readable than earlier work suggested. Their tests turn neurons into zero-shot detectors, steering directions and clues for finding hidden behaviour, though the evidence comes from open models and controlled model organisms."
tags = ["research", "safety", "models"]
date = 2026-11-25T04:03:43+01:00
draft = false
+++

An auditor opens two copies of a language model. One is the familiar base model. The other carries a small adapter whose purpose is hidden. Instead of asking the modified model to reveal itself, the auditor looks down a list of neurons and asks which ones changed their habits.

*The scenes that open and close this article are illustrations; the people in them are invented.*

That is the practical bet behind two reports published by Anthropic researchers Jasmine Shone and Lisa Dunlap. They argue that individual neurons, long treated as unreliable units of meaning, can expose what fine-tuning added to a model. In a blind test on 68 LoRA adapters, their neuron-assisted auditor named the hidden behaviour in 75% of the 58 adapters that contained one. Looking only at model outputs reached 40%.

The work reopens an old question in interpretability. Researchers once hoped that inspecting single neurons would reveal a model's concepts. Evidence of polysemanticity, changing representations across layers and distributed factual recall pushed much of the field toward learned features, probes and residual-stream directions. Shone and Dunlap do not claim that those problems vanished. They change the object being interpreted.

## What a neuron writes

An MLP neuron has two relevant parts. Its activation decides how strongly it fires in a particular context. Its output vector determines what direction it adds to the residual stream. The output vector is fixed, although the activation can be positive or negative.

The researchers therefore describe a neuron as a context-gated steering vector. Earlier work often asked what text makes a neuron activate. Their method also asks what the neuron writes when it does. They use a vocabulary readout called the J-lens to identify tokens that an output vector makes more likely, then combine that information with the neuron's top activation contexts.

One neuron in Llama 3.1 8B Instruct illustrates the distinction. It contributes the token “John” in prompts about John the Ripper and the author of the fourth Gospel. An activation-only description misses that shared output. The same vector can also carry different meanings under positive and negative activation, so the sign matters.

The team tested its interpretations through interventions. It removed neuron activations, injected output vectors at other layers and used them to steer behaviour. In its sampled census, a neuron contributed two unrelated concepts to the residual stream in about 1% or fewer of cases. Output vectors also kept roughly the same meaning across most layers.

Those findings do not say that neurons fire for only one kind of text. A neuron can activate in many contexts. The narrower claim concerns what it contributes to the model's next computation. That distinction lets the authors preserve evidence of messy activation while arguing that the written direction remains readable.

## Distributed facts can still be legible

Factual recall presents a second objection. Editing one neuron rarely deletes one fact because the model stores knowledge along many paths. The Anthropic work agrees with the distributed part. When the researchers changed enough neurons to make a model answer a factual question incorrectly, the affected neurons usually represented concepts connected to that fact.

Distribution, in other words, did not make the paths arbitrary. Several interpretable contributions could jointly support one answer. This matters because interpretability tools often face a choice between simple units that seem too crude and learned feature dictionaries that require extra training and introduce their own choices.

Sparse autoencoders became a prominent answer to that problem. They learn a larger set of sparse features from model activations, with the aim of separating concepts that ordinary neurons combine. Anthropic's own earlier work used those features to map activations in Claude. Shone and Dunlap do not reject sparse autoencoders. Their comparisons ask whether a model's existing neurons can serve some of the same practical purposes without first training another representation.

## From descriptions to safety tools

The second report tests three uses: detection, steering and auditing. For detection, the team selected neurons from their activation examples, automated descriptions and output readouts. The resulting neuron probes beat text search on most of the evaluation sets and matched linear probes trained on 400 labelled examples on four of 16 sets. For retrieval, they beat text search on 11 of 17 harmful-content topics.

That is not a general victory over trained classifiers. The report says trained probes usually perform better. The useful comparison is zero-shot: the neuron method needs no labelled training set for the target concept. It may help an investigator start an audit before collecting examples.

For steering, the researchers used neuron output vectors to push a chatbot toward a target behaviour. Neurons chosen from their readouts and activation descriptions produced that behaviour in 21% of responses. Trained steering vectors achieved the same rate. The result is modest in absolute terms, but it tests whether the neuron's fixed output has causal force rather than merely correlating with a concept.

The audit experiment then compares a fine-tuned model with its base version. The team examined model organisms of backdoors, emergent misalignment and subliminal learning. Fine-tuning tended to increase activation of neurons whose existing output vectors already pointed toward the new behaviour. The adapter often reused directions present in the base model rather than inventing a completely new internal vocabulary.

That pattern gave the auditor something to inspect. By steering along update directions and reading neurons aligned with them, the Claude-based audit named three-quarters of the hidden behaviours. Output sampling alone missed most of them.

## Unlearning that hides an answer

The authors also applied their method to 23 public checkpoints trained to forget hazardous cybersecurity knowledge from WMDP. The benchmark contains 1,987 multiple-choice questions whose answers could support cyberattacks. An unlearning method is meant to remove access to the underlying information while preserving unrelated ability.

Fourteen of the 23 checkpoints still ranked the correct answer first under cloze scoring for most questions that the base model had answered correctly. Their visible multiple-choice accuracy could fall while a different readout continued to recover the answer. The researchers interpret this as evidence that many methods hid the knowledge behind a learned response mechanism rather than removing it.

This result has a narrow boundary. WMDP is a benchmark, and cloze scoring is one probe of retained knowledge. A model that ranks a token correctly has not necessarily preserved every operational skill associated with it. Still, the experiment shows why one behavioural score cannot establish that information disappeared.

## A basis, not a complete map

The two reports work mainly with open-weight models whose neurons and fine-tuned checkpoints can be compared directly. The hidden behaviours are controlled model organisms. Real deployments combine larger models, tool use, system prompts and safeguards that may obscure the same signals.

Neuron descriptions also depend on examples and readouts. A legible output vector does not guarantee that an auditor will find the right neuron, and the zero-shot detectors usually trail supervised probes. The authors present neurons as useful units of analysis, not as a complete account of cognition.

The practical contribution is a cheaper first pass. A fixed output vector comes with the model. It can be read, moved, suppressed and compared before an auditor trains a feature dictionary or assembles a labelled set.

Back at the two model copies, the auditor reaches the neurons whose activation rose after fine-tuning. Their output vectors already pointed toward the adapter's concealed behaviour before the adapter existed. The change lies less in a new concept than in when the model chooses to use an old direction.

## References

- Jasmine Shone and Lisa Dunlap, “Returning to the Neuron Basis for Interpretability, Part 1: Answering Three Objections” — https://alignment.anthropic.com/2026/neuron-basis-theory/
- Jasmine Shone and Lisa Dunlap, “Returning to the Neuron Basis for Interpretability, Part 2: Using Neurons For Safety Applications” — https://alignment.anthropic.com/2026/neuron-basis-applications/
- Trenton Bricken et al., “Towards Monosemanticity: Decomposing Language Models With Dictionary Learning” — https://transformer-circuits.pub/2023/monosemantic-features/index.html
- Nicholas Carlini et al., “WMDP: Measuring and Reducing Malicious Use With Unlearning” — https://arxiv.org/abs/2403.03218
