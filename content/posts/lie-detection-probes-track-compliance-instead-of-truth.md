+++
title = "Lie-detection probes track compliance instead of truth"
description = "A preprint tests eight published probes on language models playing characters who reject basic facts. Many fail once true and false answers share the same prompt, and a probe trained to separate truth from obedience holds up."
tags = ["research", "safety"]
date = 2026-10-06T04:01:31+02:00
draft = false
+++

Many published lie-detection probes, which read a language model's internal activity to flag false answers, are partly detecting whether the model followed its instructions, a new preprint reports.

Maximilian von Klinski and three co-authors had three open models play characters who reject basic facts, such as a Ptolemaic astronomer or a conspiracy theorist, and tested whether eight existing probes still caught the false answers. Many did, until the true and false replies were placed under the same character prompt. Then several scored worse than a coin toss.

## Why it matters

A safety team that monitors a deployed model with a probe needs the alarm to fire on falsehood, not on something that usually travels with it. In the data most probes are trained on, the false answer is also the less likely answer and the one that breaks the model's rules, and the study finds that probes learn those shortcuts.

## How a probe reads a model

A probe is a simple classifier trained on the numbers inside one layer of a model, labelled by whether the text being processed was true or false. If it works, it reads what the model treats as true even when the words it produces say otherwise.

The team built a dataset of 8,916 answers from Meta's Llama 3.3 70B and Google's Gemma 3 27B and Gemma 4 31B, each answering yes-or-no questions both as a plain assistant and as one of 15 characters: real-world believers, fictional figures such as a citizen of Orwell's *1984*, and historical ones such as a medieval physician. The questions were refined by a pipeline built on Anthropic's Claude Opus 4.8, screened by Llama as a judge, and checked by hand by the first author.

## Sharing the prompt breaks most probes

In the first version of the test, most earlier probes separated true from false answers well, ranking them correctly in roughly nine pairs out of ten. But every false answer came with a character prompt and every true one with the assistant prompt, so the prompt alone gave the answer away.

The authors removed that clue by placing both answers after the character's prompt. Now the true answer was also the less probable one and the one that contradicted the character's instructions. On Llama, several probes that had worked fell below chance, and only two stayed close to their earlier scores. The failures repeated, often more severely, on both Gemma models.

## Three traps isolate the shortcut

To find out what the probes were tracking, the team built three test sets in which truth runs opposite to a likely confounder. In one, a scoring rule made the wrong answer the more probable one. In another, a character privately held a false belief, such as that seven times six is 13. In the third, the correct answer broke a formatting rule, for example by using parentheses when square brackets were required, while the wrong answer obeyed it.

The formatting trap was decisive. On Llama, every earlier probe scored below chance except one whose readings were inverted on every test, which the authors read as a strong link between "true" and "compliant" inside those probes.

The team's own probe adds one ingredient to standard training on simple facts: questions where the instructions demand the wrong answer, so obedience and truth point in opposite directions. It scored about 0.98 out of 1 on the shared-prompt test with Llama, never fell below 0.90 on any of the three models, and was perfect on all three traps.

## A home-built fix, and confounders still unknown

That result needs two qualifications. The new probe was designed against the same confounders it was then tested on, which the authors acknowledge makes its perfect trap scores unsurprising. Its design also extends an earlier probe co-developed by co-author Lennart Bürger, one of only two prior probes that held up when the prompt was shared.

The study's own data shows the list of confounders is incomplete. On Gemma 4, one earlier probe was near-perfect on all three traps yet scored about 0.17 on the shared-prompt test, failing for a reason none of the traps captured. The characters were also set up with a single system prompt in one-turn conversations, on models of up to 70 billion parameters.

The work was funded by Germany's Federal Ministry of Research, Technology and Space, the European Union's Horizon Europe programme and the German Research Foundation. The authors have published the dataset on Hugging Face and their code on GitHub, and name characters that emerge gradually over long conversations as the next case to test.

## Verification

| Claim | Label | Primary source | Independent check |
| --- | --- | --- | --- |
| Eight prior probes evaluated; many fail when true and false answers share the character prompt | VENDOR-REPORTED | [von Klinski et al. preprint](https://arxiv.org/abs/2609.39807) | none; preprint result |
| Dataset of 8,916 human-reviewed answers from Llama 3.3 70B, Gemma 3 27B and Gemma 4 31B across 15 characters | VERIFIED | [von Klinski et al. preprint](https://arxiv.org/abs/2609.39807) | [dataset on Hugging Face](https://huggingface.co/datasets/maxvonk/anti-factual-personas) |
| Questions refined with a Claude Opus 4.8 pipeline, judged by Llama 3.3 70B, checked by the first author | VERIFIED | [von Klinski et al. preprint](https://arxiv.org/abs/2609.39807) | none; authors' method statement |
| Most prior probes score AUROC 0.86 to 0.94 when the prompt differs between true and false answers | VENDOR-REPORTED | [von Klinski et al. preprint](https://arxiv.org/abs/2609.39807) | none |
| With a shared prompt on Llama, several prior probes fall below chance; only Marks/Bürger Lie (0.885) and Cundy DolusChat (0.901) stay stable | VENDOR-REPORTED | [von Klinski et al. preprint](https://arxiv.org/abs/2609.39807) | none |
| Shared-prompt failures replicate, often more severely, on Gemma 3 27B and Gemma 4 31B | VENDOR-REPORTED | [von Klinski et al. preprint](https://arxiv.org/abs/2609.39807) | none |
| On the compliance trap with Llama, all prior probes score below chance except Goldowsky-Dill SD, which is inverted throughout | VENDOR-REPORTED | [von Klinski et al. preprint](https://arxiv.org/abs/2609.39807) | none |
| Probes link truth with instruction compliance | ANALYSIS | [von Klinski et al. preprint](https://arxiv.org/abs/2609.39807) | authors' inference from the compliance trap |
| New probe: AUROC 0.976 on the shared-prompt test with Llama, never below 0.900 across three models, perfect on all three traps | VENDOR-REPORTED | [von Klinski et al. preprint](https://arxiv.org/abs/2609.39807) | none |
| The new probe was trained to remove the same confounders it is tested on; authors call the trap results unsurprising | VERIFIED | [von Klinski et al. preprint](https://arxiv.org/abs/2609.39807) | none |
| Co-author Lennart Bürger co-developed the Marks/Bürger probe that the new probe extends | VERIFIED | [von Klinski et al. preprint](https://arxiv.org/abs/2609.39807) | cites Bürger et al. (2024) |
| On Gemma 4, Cooney DYL is near-perfect on all traps but scores 0.171 with a shared prompt | VENDOR-REPORTED | [von Klinski et al. preprint](https://arxiv.org/abs/2609.39807) | none |
| Funded by Germany's BMFTR, EU Horizon Europe and the German Research Foundation (DFG) | VERIFIED | [von Klinski et al. preprint](https://arxiv.org/abs/2609.39807) | acknowledgements section |
| Code is public on GitHub | VERIFIED | [GitHub repository](https://github.com/max-vkl/stress-testing-llm-lie-detectors) | repository page loads |
| Preprint posted 30 September 2026 | VERIFIED | [arXiv record](https://arxiv.org/abs/2609.39807) | arXiv metadata |
