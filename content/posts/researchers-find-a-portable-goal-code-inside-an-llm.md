+++
title = "Researchers Find a Portable Goal Code Inside an LLM"
description = "A new preprint traces an LLM's next coding objective to a sparse group of attention heads, reads it in plain language and moves it between programming languages. The result is causal evidence from a controlled setting, not proof that every agent has a stable inner intention."
tags = ["research", "models", "agents"]
date = 2026-11-14T04:08:30+01:00
draft = false
+++

Take a fictional developer named Mara at the point where a generated function has finished counting capitalised words and is about to check for palindromes. The cursor rests after an equals sign. No comparison has appeared, no string has been reversed, and no output token says what comes next. Mara would like to pause the model there and ask a simple question: what are you trying to do now? The scene is illustrative. A new experiment turns that question into something researchers can test inside a model.

## A goal before the code

Arnab Sen Sharma and nine colleagues at Northeastern University, Parallax, the University of Copenhagen and the University of Oxford report that the next sub-goal of a coding model can be localised to a sparse group of attention heads. Their preprint, released on 12 November, goes further than finding a correlation. The researchers decode the representation into natural language, transplant it into another programming language and intervene on it to change what the model writes.

The work asks a narrow version of a broad and loaded question: do language models have goals? The authors avoid treating fluent behaviour as evidence of intention. They define a goal as an internal state that appears before an action, can be realised through different means and persists while the action is carried out. That operational definition produces three tests: pre-commitment, plasticity and persistence.

The controlled task makes those tests possible. Prompts asked a model to complete two to four independent operations over integers, strings or lists. An operation might count capitalised words, find a range or check whether any word is a palindrome. The researchers used 253 specifications and examined four positions before each next operation began, giving 1,012 observations in each evaluation configuration.

Most of the paper's main results use Qwen-2.5-Coder-32B-Instruct, a 64-layer model. A sparse-selection procedure identified 122 attention heads concentrated between layers 28 and 55. The procedure rewarded heads whose output could be moved from a source prompt in one programming language to a destination prompt in another and cause the source operation to begin. Choosing different languages mattered: a representation of palindrome checking had to survive changes in syntax, variable names and concrete tokens.

## Reading the hidden instruction

To make the representation legible, the team built a probe called GoalScope from the outputs of those selected heads. It sums what the heads write into the model's residual stream at a chosen token, then injects that vector into a separate run of the same model. The second run receives a fixed request to describe the operation. Its text prompt contains no information from the original coding problem, so the injected activation is the only route by which the original context can reach the answer.

This method extends Patchscopes, a framework introduced by Asma Ghandeharioun and colleagues for placing a hidden representation into a prompt where a language model can explain it. It also follows earlier work from several of the same researchers. Function Vectors showed that a compact sum of attention-head outputs could carry an input-output function and trigger that function in a new context. General Filter Heads later isolated a portable representation of predicates used to filter lists. The new paper moves from a single operation towards the changing next step of a multi-operation task.

The goal readout became useful before the model emitted the implementation. At the end of the preceding line, GoalScope descriptions agreed with a non-trivial part of the upcoming behaviour about 60% of the time. At the indentation point, three tokens before implementation, the reported score exceeded 90%. When moved into a C++ context, the encoding triggered the corresponding operation 96% of the time at one pivot position; the mean across pivot positions was about 87%.

Those results support pre-commitment and plasticity. They say the selected activity carries information about what to do before the relevant code appears, and that the information is not just a cached sequence of Python tokens. The destination model produces a route suited to its new context.

The causal tests sharpen that claim. When the researchers preserved the selected heads' access to the next task while blocking roughly 93% of later attention heads from that span, the model largely retained its ability to implement the operation. Blinding only the 122 selected heads left room for compensation through redundant paths, but blinding a broader set of 250 sharply reduced performance. The authors describe this as a causal bottleneck with redundancy rather than a single indispensable switch.

## A goal reconstructed at every step

Persistence creates a mechanical puzzle. An autoregressive transformer does not have a recurrent state that can simply be handed from one generated token to the next forever. Attention can read an earlier position, but moving a newly computed state forward consumes layers. In this model the goal became verbalizable only after about layer 40, leaving too little depth to carry the same state through operations that last more than 30 tokens.

The authors propose a different mechanism. The model repeatedly rereads the task specification, examines the completed code visible in its context and reconstructs the pending operation. They call this non-recurrent goal-seeking. The apparent continuity belongs to repeated computation, not to one internal object travelling untouched across the sequence.

Targeted transplants supported that account. The researchers changed the key-value states that the goal heads read from the task span while leaving other heads on the destination prompt. The model then implemented the source prompt's next operation in the destination programming language about 94% of the time, and GoalScope's description shifted with it about 90% of the time. In a separate intervention, replacing the heads' query states transferred information about completed work and changed which remaining sub-task the model selected.

That distinction matters for oversight. A monitor might be able to read a pending operation before it appears in output, and an intervention might redirect it. Yet the representation is assembled from the specification and visible progress. Change either source and the apparent goal can change too.

## The limits of a readable goal

The paper does not establish a universal goal centre. Its central dataset consists of enumerated coding operations, most main-text measurements come from one code-tuned model, and an LLM judge scores whether generated descriptions and implementations agree. The authors test other model families and some natural-language settings in appendices, but they list model and task coverage as limitations.

The strongest caution appears when the path is disturbed. The model kept a recognisable encoding during ordinary execution, yet it often failed to recover from a planted false start. Qwen-2.5-Coder-32B-Instruct adapted in about 97% of aligned cases, 63% of easy perturbations and only 15% of hard ones. Other tested models showed the same decline. A readable objective did not guarantee successful pursuit.

Return to Mara at the waiting cursor. In this invented closing scene, her debugger displays a tentative note: checking whether any word is a palindrome. She treats it as a forecast tied to this prompt and this point in the code, not as a confession from a machine. Then she inserts a misleading prefix. The note still names the task, while the generated code wanders. The new research gives her a window onto the model's next operation. It also shows why seeing a goal and trusting its execution remain different jobs.

## References

- Ghandeharioun, A., Caciularu, A., Pearce, A., Dixon, L., & Geva, M. (2024). *Patchscopes: A Unifying Framework for Inspecting Hidden Representations of Language Models*. https://arxiv.org/abs/2401.06102
- Sen Sharma, A., Rogers, G., Shapira, N., & Bau, D. (2026). *LLMs Process Lists With General Filter Heads*. https://arxiv.org/abs/2510.26784
- Sen Sharma, A., Todd, E., Feucht, S., Arditi, A., Gandikota, R., Shapira, N., Sarti, G., Fierro, C., Schut, L., & Bau, D. (2026). *Goal Encoding in LLMs*. https://arxiv.org/abs/2611.17297
- Todd, E., Li, M. L., Sen Sharma, A., Mueller, A., Wallace, B. C., & Bau, D. (2024). *Function Vectors in Large Language Models*. https://arxiv.org/abs/2310.15213
