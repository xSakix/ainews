+++
title = "A Novelty Judge Changed Its Mind With the Prompt"
description = "Ai2 tested language models that judge whether research ideas are new. One model's accuracy fell from 93.5% to 40.9% after a small prompt change, exposing how fragile automated novelty scores can be."
tags = ["research", "models"]
date = 2026-10-28T04:11:25+01:00
draft = false
+++

Picture a machine-learning researcher at the end of a long review session. Two proposed ideas sit side by side on her screen. A model has marked the first one as novel. She shortens the instruction above the same pair, runs it again and watches the mark move to the second idea. The researcher is invented. The reversal is not: Ai2 measured it across a benchmark built to test automated judges of scientific novelty.

## The verdict moved before the evidence did

Ai2's study, released with code and data, tested six language models as novelty judges. The researchers varied the prompt, the reasoning budget, the retrieved literature, the format of the ideas and the way they combined multiple calls. The underlying ideas stayed fixed.

The sharpest result came from GPT-5.4. In one prompt, the model was told that reviewers had found exactly one idea in each pair to be novel and was asked to identify it. In a simpler prompt, it was merely asked which idea was novel. Accuracy on the same human-versus-generated pairs fell from 93.5% to 40.9%. The model changed more than half its verdicts.

The wording mattered less on pairs containing only human-authored ideas. There, the same prompt change moved accuracy by about seven percentage points. A judge can therefore appear stable on conventional academic material and behave differently on the generated ideas it is increasingly asked to evaluate. Even the human-only set was not immune: Claude Opus 4.6 moved by 21 points under the prompt change.

There was no prompt that improved every judge. Removing a warning against treating incremental work as novel helped some models and hurt others. When the team compared ideas from two AI generators, changing the prompt altered roughly a quarter to a third of verdicts on average across the six judges. That instability can be measured without first deciding which generator is better.

## Reviews became the benchmark

Novelty is difficult to benchmark because it is not a property that can be read from an answer key. A research idea is new only in relation to earlier work, and experts can disagree about how much difference counts. Ai2 therefore did not use paper acceptance as a stand-in. It mined ICLR 2026 peer reviews for passages in which reviewers explicitly praised or disputed a contribution's originality.

The process produced 154 high-novelty human ideas from accepted papers in the top-rated 10% of their research areas. Each had positive reviewer evidence for novelty and no reviewer dispute. The lower-novelty pool contained 145 ideas from rejected papers in the bottom 10% whose reviews raised originality concerns without positive novelty evidence. In a check of 50 extracted review passages, an annotator agreed with the assigned polarity in 47 cases. None of the three disagreements would have changed whether a reviewer counted as praising or disputing novelty.

This human-only collection tests whether a judge can separate contributions with stronger and weaker review evidence. A second collection addresses a central use case for automated science: judging ideas written by a model. The team paired the 154 validated human ideas with 154 ideas from a simple generator. It received a research area and an instruction to propose something novel, without literature search, tools, iteration or feedback.

The label for those generated ideas is deliberately weaker. The researchers assumed that the simple generator's output was less novel than a contribution from a top-rated paper whose reviewers had endorsed its originality. No expert judged every pair. As a check, one expert reviewed 30 pairs, weighted towards examples the strongest judge had missed, and preferred the human idea every time. The team also rewrote the generated and human ideas into the same structure to reduce the chance that style gave away their origin.

## More machinery did not produce a firmer answer

The study also tested a familiar response to uncertain model judgements: give the judge more search, more reasoning or a system designed for the task. None delivered a general cure.

An agentic GPT-5.6 Sol judge received an extra-high reasoning budget and live iterative search limited to arXiv. It reached 0.78 macro-F1 on the human-plus-generated task. A standard Claude Opus 4.6 setup with five retrieved abstracts reached 0.89 and cost roughly one-tenth as much per decision at the API prices used in the study. The comparison does not prove that search is useless. It shows that additional machinery does not guarantee a better novelty judgement.

Purpose-built systems also trailed a simpler baseline. A low-reasoning Claude Opus 4.6 prompt, decided by majority vote across three calls, reached 0.854 macro-F1 for a total evaluation cost of $2.59. Idea Novelty Checker, which retrieves and reranks literature, scored 0.642 for $30.66. The novelty evaluator in Sakana AI's AI Scientist, which searches Semantic Scholar iteratively, scored 0.772 for $82.05. All three figures come from Ai2's implementation and pricing assumptions, so they compare these tested configurations rather than every possible use of the systems.

Earlier systems explain why researchers reach for these designs. Scideator helps scientists recombine facets of papers into new proposals and uses literature retrieval to assess overlap. Idea Novelty Checker narrows a broad literature search through embedding filters and facet-based reranking. AI Scientist treats novelty checking as one stage in a larger automated research loop. Each grounds its judgement in prior work instead of relying on a model's memory alone.

Ai2's result shifts the burden of proof. A high score from one judge, prompt and reasoning setting says little about whether the verdict will survive another reasonable setup. The authors recommend testing judges on the kinds of generated ideas they will actually see, measuring sensitivity across prompts and models, and updating benchmarks as the literature changes.

## A score needs its own review

Return to the imagined researcher. She does not choose the verdict that she prefers. She keeps both outputs, records both prompts and reads the related papers herself. The model can still help sort a growing pile of proposals, but its number is now one piece of evidence rather than the final gate.

The mark moved between two ideas, but the more important change was the confidence attached to it. When a few words can move the answer, the judgement needs a review as much as the research idea does.

## References

- Ai2. (2026). *Can we trust LLMs to judge whether a research idea is novel?* https://allenai.org/blog/novelty-bench
- Lu, C., Lu, C., Lange, R. T., Foerster, J. N., Clune, J., & Ha, D. (2024). *The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery*. https://arxiv.org/abs/2408.06292
- Radensky, M., Shahid, S., Fok, R., Siangliulue, P., Hope, T., & Weld, D. S. (2024). *Scideator: Human-LLM Scientific Idea Generation Grounded in Research-Paper Facet Recombination*. https://arxiv.org/abs/2409.14634
- Shahid, S., Radensky, M., Fok, R., Siangliulue, P., Weld, D. S., & Hope, T. (2025). *Literature-Grounded Novelty Assessment of Scientific Ideas*. https://arxiv.org/abs/2506.22026
- Sternlicht, N., Shahid, S., Jansen, P., Weld, D. S., Siangliulue, P., & Hope, T. (2026). *Old Ideas, Novel Problems: The Instability of LLM-Based Novelty Evaluation*. https://arxiv.org/abs/2610.02022
