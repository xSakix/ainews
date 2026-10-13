+++
title = "The same attention heads change jobs with the task"
description = "A new preprint finds that a language model reorganises the influence of its attention heads when the requested task changes, even when the facts in the prompt stay fixed. Causal interventions suggest that task context helps determine what a component does, complicating attempts to give it one permanent label."
tags = ["research", "models"]
date = 2026-10-13T04:05:13+02:00
draft = false
+++

Picture an engineer at a monitor, tracing lines between hundreds of small boxes. One box receives a neat label: "country lookup." Then the instruction changes, the input facts remain the same, and the same box seems to help with something else. This engineer is invented, an illustration of the practical problem at the centre of a new study: a transformer component may not have one stable job to name.

## A map that changes with the question

Sovesh Mohapatra and Dani S. Bassett, researchers affiliated with the University of Pennsylvania and Yale University, tested how task context changes the functional organisation of attention heads in language models. Their preprint, submitted on 12 October 2026, examines five open models ranging from 1.5 billion to 14 billion parameters. It has not been peer reviewed.

The study begins with a deliberate separation. A prompt contains a small graph encoded as factual statements, while an instruction asks the model to answer one of several questions about that graph. Across conditions, the graph facts stay fixed. Only the task changes. That design lets the researchers ask whether the model runs the same internal route over identical information or reorganises the route according to what it has been asked to do.

They treat each attention head as a node in an influence network. An edge records how changing one head's output affects another head later in the model. The resulting map is functional rather than anatomical: the architecture is unchanged, but the measured pattern of influence can differ from task to task.

It does. Mohapatra and Bassett report that the networks separate by task across the tested models. Heads that occupy influential positions in one task can become less central in another. The finding shifts the interpretability question from "What does this head represent?" toward "What role does this head play in this task, within this network?"

That distinction matters because much mechanistic interpretability has searched for reusable internal parts. Eric Todd and colleagues previously identified small sets of attention heads that carry compact "function vectors" extracted from in-context examples. Roee Hendel, Mor Geva and Amir Globerson likewise showed that in-context learning can form a task vector that lets a model perform a demonstrated operation even without the demonstrations at inference time. Those results support the idea that a task can have a causal internal representation. The new paper asks how such a representation changes the relationships among components.

## The instruction can move the machinery

Correlation alone would leave an obvious doubt. A different task produces a different answer, so a different influence map might merely accompany the change. The authors therefore intervene on the model's activations.

They construct an early-layer activation edit intended to move the model from the representation of one task toward another while leaving the written prompt untouched. In experiments on Gemma and Qwen models, that edit can switch which task the model performs. The paper reports that every one of 512 prompts for which the two tasks required opposite answers switched to the target answer, while all 512 prompts for which both tasks required the same answer preserved that answer.

The intervention also makes the later influence map resemble the target task. The authors measure this with an error between network response patterns. Their task-switching edit reduced that error by 53.6 percent in Gemma and by 5 percent in Qwen. The difference in magnitude is a warning against treating the mechanism as uniform across model families, but both cases point in the same causal direction: changing the internal task context can redirect later computation.

This resembles activation steering, a broader family of methods that changes model behaviour by adding a direction to hidden activations. Alexander Matt Turner and colleagues showed that activation additions derived from contrasting prompts could alter high-level properties of generated text without further training. The new study uses an activation edit as an experimental probe. Its aim is not to ship a behavioural control, but to test whether a change in task representation precedes a change in the network of attention-head influence.

The intervention is narrow. It does not show that researchers can select any arbitrary task, edit any model reliably, or read a complete program from a graph of heads. The tasks are controlled, the models are open-weight systems of moderate size, and the causal tests focus on a particular internal contrast. The paper's strongest claim concerns context dependence inside that setting.

## From labelled parts to recruited teams

Network neuroscience supplies the authors' organising metaphor. In that field, a brain region's contribution is often studied through its place in a changing network rather than through a single isolated function. Bassett and Olaf Sporns described the approach as an effort to connect elements across scales and explain how interactions produce behaviour. Mohapatra and Bassett carry that perspective into transformer analysis.

The analogy has limits. An attention head is a designed mathematical component, not a biological region, and a transformer does not inherit the brain's anatomy or history. The useful transfer is methodological: observe a part together with the pattern of influence that recruits it.

For people who audit models, this makes a permanent label less reassuring. A head found to support a behaviour under one prompt may participate differently when instructions, examples or objectives change. Removing or suppressing that head could have effects that depend on task context. Conversely, a safety-relevant process may be distributed across different configurations even when the underlying parameters are identical.

The result also suggests a practical standard for future interpretability claims. A proposed circuit should be tested across tasks that reuse the same information, and an apparent role should survive causal intervention rather than visual inspection alone. If the circuit changes, the change is part of the mechanism to explain.

There is more work to do. The paper studies a limited family of graph-based tasks and a small set of open models. It does not establish how these response networks behave in very large proprietary systems, during long conversations or under noisy real-world instructions. It also does not settle whether the measured network captures all computation relevant to an answer. The authors present a framework for studying reconfiguration, not a finished atlas.

Return to the imagined engineer at the monitor. The label on the box is still useful, but now it needs a condition beside it: useful for this operation, under this instruction, in this company of other heads. The durable object is no longer the isolated part. It is the pattern the task calls into service.

## References

- Bassett, D. S., & Sporns, O. (2017). *Network neuroscience*. https://doi.org/10.1038/nn.4502
- Hendel, R., Geva, M., & Globerson, A. (2023). *In-Context Learning Creates Task Vectors*. https://aclanthology.org/2023.findings-emnlp.624/
- Mohapatra, S., & Bassett, D. S. (2026). *Task Context Dynamically Reconfigures Attention Head Networks in Large Language Models*. https://arxiv.org/abs/2610.13895
- Todd, E., Li, M. L., Sen Sharma, A., Mueller, A., Wallace, B. C., & Bau, D. (2024). *Function Vectors in Large Language Models*. https://openreview.net/forum?id=AwyxtyMwaG
- Turner, A. M., Thiergart, L., Leech, G., Udell, D., Vazquez, J. J., Mini, U., & MacDiarmid, M. (2024). *Activation Addition: Steering Language Models Without Optimization*. https://arxiv.org/abs/2308.10248
