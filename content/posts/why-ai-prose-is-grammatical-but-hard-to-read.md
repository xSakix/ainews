+++
title = "Why AI Prose Is Grammatical but Hard to Read"
description = "A new study finds that nine leading models repeatedly choose linguistic forms associated with greater reading effort. Its fine-tuning experiment points to a conflict between dense machine reasoning and language built for human comprehension."
tags = ["research", "models"]
date = 2026-10-25T04:14:11+01:00
draft = false
+++

An editor reaches the fourth line of a generated briefing and reads it twice. Every word belongs. The sentence is grammatical. Still, its nouns have piled into a block, a thing that cannot act has been made the actor, and the verb was once a noun. The editor in this scene is fictional. The small resistance in the sentence is the subject of a real experiment.

## The strain inside a fluent sentence

Thomas Hikaru Clark, Matias B. Martin and Kyle Mahowald set out to measure a complaint that usually ends as taste: recent AI writing can be difficult to understand even when it contains no obvious error. Their preprint compares text from nine frontier and near-frontier models with human writing and with close paraphrases created by translating the model text into Japanese and back into English.

The models repeatedly chose forms that psycholinguists associate with greater processing effort. All nine used more low-frequency word sequences and paired more inanimate subjects with verbs associated with animate actors. Most produced longer syntactic dependencies, more stacked nouns and more object-relative clauses with an optional connecting word removed. The pattern was strongest in conversations and code-related exchanges, and it varied across model families.

These are not grammar mistakes. English permits a phrase such as “reader-patience budget,” and a reader can recover the meaning of an inanimate subject that “eats” something abstract. The cost arrives during comprehension. Unfamiliar word combinations are harder to predict. Long dependencies ask working memory to hold one part of a sentence until its partner arrives. Dense noun groups require the reader to infer relationships that the writer has left unstated.

The distinction matters because fluency has become a weak test of readability. A model can obey English syntax while choosing constructions that human speakers tend to avoid. Its prose can pass a grammatical inspection and still make the reader spend more effort than the idea requires.

## Human language carries its readers

The paper rests on decades of work about how language adapts to the limits of people. Edward Gibson and colleagues describe human languages as compromises between the effort of speaking and the effort of understanding. Across 37 languages, Richard Futrell, Mahowald and Gibson found large-scale evidence that words with a syntactic relationship tend to stay near each other. Shorter dependencies reduce the burden on memory.

Predictability creates another pressure. Roger Levy and T. Florian Jaeger proposed that speakers manage information density by retaining or dropping optional words according to what comes next. A speaker is more likely to include “that” when it helps prepare a listener for less predictable material. Nathaniel Smith and Levy later found that reading time rises roughly with a word's surprisal: uncommon continuations impose a measurable cost.

That work treats redundancy as part of communication, not waste. A familiar phrase, an optional connector or a repeated cue can give the mind time to keep up. Eric Martínez and colleagues demonstrated the consequence in legal language. The difficulty of contracts came substantially from writing choices such as centre-embedded clauses and unnecessary jargon, rather than from specialized concepts alone.

Clark, Martin and Mahowald ask what happens when the producer of language does not share those human constraints. Modern models are trained on human text, but post-training increasingly rewards correct answers in mathematics, coding and reasoning. Success may be verified at the end of a task. The route to that answer does not always need to be comfortable for a person to read.

## A parallel corpus separates meaning from form

The researchers collected model output in three settings: chat, coding and essays. Human baselines came from OpenSubtitles for conversation, Stack Exchange for technical prose and the PERSUADE 2.0 corpus of student essays. They identified difficult constructions with dependency parsing, supplemented by automated classification where a parse alone could not decide whether a subject was animate or a noun had been turned into a verb.

Comparing model text with human corpora leaves a possible objection. The subjects may differ, and a technical answer naturally uses different language from a film subtitle. The team therefore built a parallel control. Each model sentence went through a 3.3-billion-parameter translation model into Japanese and back into English, preserving the broad meaning while changing the expression.

Most frontier models' original responses contained more rare bigrams and higher n-gram perplexity than their translated paraphrases. Similar shifts appeared for inanimate subjects, noun-derived verbs and reduced object-relative clauses. The Llama models and the OLMo base model changed less. OLMo Think, a reasoning variant, looked more like the frontier systems. Claude Opus 5.5 scored lower than Opus 5 on 19 of 21 comparisons, evidence that these tendencies can move in the other direction as models change.

The round trip is a control, not a perfect human rewrite. Translation systems have their own preferences, and Japanese was chosen precisely because an unrelated pivot language tends to produce more varied paraphrases. Yet the comparison holds meaning closer than a simple contrast between unrelated human and model documents. It suggests that the difficult forms come from the model's manner of expression, not only from the topic.

## The length penalty changed the grammar

The second experiment tested a mechanism. The researchers fine-tuned Qwen2.5-1.5B-Instruct to convert structured event records into sentences. Both a shorter and a longer construction could express the right answer. Reinforcement learning rewarded correctness while an adjustable penalty charged for length. Some runs also used a constraint that discouraged the fine-tuned model from moving too far from its original token distribution.

Any positive length penalty pushed the unconstrained runs toward a categorical preference for the shorter form. On the trained constructions, more than 98% of answers used the short alternative. The preference transferred to unseen examples of similar constructions. It reached one of four more distant grammatical alternatives when the model had no constraint tying it to the base model.

The model was never told to omit optional words. It discovered that choice as a way to save tokens while preserving task correctness. Human speakers vary those same choices with context. The model instead learned a broad compression preference, a small demonstration of how an objective aimed at efficiency can alter language away from human use.

This experiment does not prove that commercial laboratories apply the same length penalty, or that one reward explains every pattern in closed models. The authors studied English, a limited set of prompts and a subset of available systems. They could not observe frontier post-training directly and describe the intervention as a proof of concept. The causal claim is narrow: under a controlled reward for brevity, grammatical preferences changed in the predicted direction.

## Readability becomes a model requirement

The study reframes readability as an alignment problem with measurable targets. A useful answer must reach a correct conclusion, but human work often depends on inspecting the route. A developer reviews an agent's patch explanation. A doctor reads a summary before checking the chart. An analyst turns generated research into a decision. Dense prose can hide uncertainty and raise the cost of oversight even when every sentence remains technically valid.

The measurements also suggest practical tests. Model developers can track dependency length, low-frequency sequences and compressed constructions alongside task benchmarks. Training can reward successful communication rather than assuming that human preference will survive optimization for other goals. The improvement from one Opus generation to the next shows that the linguistic profile is not fixed.

The fictional editor returns to the sentence and adds one connecting word. Then she breaks the noun stack into a clause and gives the action to a person. The facts have not changed, and the passage has grown by six tokens. What changed is where the cost sits: the machine saved less space, and the reader carried less weight.

## References

- Clark, T. H., Martin, M. B., & Mahowald, K. (2026). *Why is AI-generated language so hard to understand?* https://arxiv.org/abs/2610.29162
- Futrell, R., Mahowald, K., & Gibson, E. (2015). *Large-scale evidence of dependency length minimization in 37 languages*. https://doi.org/10.1073/pnas.1502134112
- Gibson, E., Futrell, R., Piantadosi, S. T., Dautriche, I., Mahowald, K., Bergen, L., & Levy, R. (2019). *How efficiency shapes human language*. https://doi.org/10.1016/j.tics.2019.02.003
- Levy, R., & Jaeger, T. F. (2007). *Speakers optimize information density through syntactic reduction*. https://proceedings.neurips.cc/paper/2006/hash/c6a01432c8138d46ba39957a8250e027-Abstract.html
- Martínez, E., Mollica, F., & Gibson, E. (2022). *Poor writing, not specialized concepts, drives processing difficulty in legal language*. https://doi.org/10.1016/j.cognition.2022.105070
- Smith, N. J., & Levy, R. (2013). *The effect of word predictability on reading time is logarithmic*. https://doi.org/10.1016/j.cognition.2013.02.013
