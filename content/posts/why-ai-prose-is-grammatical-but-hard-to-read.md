+++
title = "Why AI Prose Is Grammatical but Hard to Read"
description = "A new study finds that nine leading models repeatedly choose linguistic forms that require more effort to read. An experiment in fine-tuning suggests a conflict between compressed reasoning by models and language that people can easily understand."
tags = ["research", "models"]
date = 2026-10-25T04:14:11+01:00
draft = false
+++

An editor reaches the fourth line of a generated briefing and reads it twice. Every word fits, and the sentence is grammatical. Yet several nouns appear in a row without words that explain how they relate to one another. An inanimate subject is paired with a verb that normally describes a person's action, and a noun is used as a verb. The editor in this scene is fictional. The difficulty that she encounters is the subject of a real experiment.

## Why a fluent sentence can be hard to read

Thomas Hikaru Clark, Matias B. Martin and Kyle Mahowald set out to measure a problem that readers often describe as a matter of taste: recent AI writing can be difficult to understand even when it contains no obvious error. Their preprint compares text from nine frontier and near-frontier models with human writing. It also compares the model text with close paraphrases produced by translating it into Japanese and back into English.

The models repeatedly chose forms that psycholinguists associate with greater effort during reading. All nine used more uncommon sequences of words and more inanimate subjects paired with verbs that normally describe the actions of living beings. Most also placed grammatically related words further apart, used more strings of nouns to modify other nouns, and more often omitted optional connecting words from object-relative clauses. The pattern was strongest in conversations and exchanges about code, and it varied across model families.

These are not grammatical errors. English permits a phrase such as “reader-patience budget,” and a reader can work out what it means when an inanimate subject “eats” something abstract. But understanding these constructions takes effort. Unfamiliar combinations of words are harder to predict. When related words are far apart, readers must remember one part of the sentence while they wait for the other. When several nouns appear together, readers must infer relationships that the writer has left unstated.

This distinction matters because fluency alone tells us little about readability. A model can follow the rules of English syntax while choosing constructions that human speakers tend to avoid. Its prose can be grammatically correct and still require more effort to read than the idea itself requires.

## Human language reflects the needs of readers

The paper draws on decades of research into how language adapts to human limitations. Edward Gibson and colleagues describe human languages as compromises between the effort of speaking and the effort of understanding. Richard Futrell, Mahowald and Gibson studied 37 languages and found extensive evidence that grammatically related words tend to stay near one another. Keeping these words close reduces the burden on memory.

Predictability also affects how people speak and read. Roger Levy and T. Florian Jaeger proposed that speakers manage information density by keeping or dropping optional words according to what comes next. A speaker is more likely to include “that” when it helps prepare a listener for less predictable material. Nathaniel Smith and Levy later found that reading time rises roughly with a word's surprisal, a measure of how unexpected it is: less predictable words take measurably longer to read.

In this account, redundancy serves a purpose in communication. A familiar phrase, an optional connecting word or a repeated cue can give readers time to understand what they are reading. Eric Martínez and colleagues demonstrated this effect in legal language. They found that the difficulty of contracts came substantially from writing choices, including clauses inserted inside other clauses and unnecessary jargon. Specialized concepts alone did not explain that difficulty.

Clark, Martin and Mahowald ask what happens when a system that produces language does not have these human limitations. Modern models are trained on human text, but training after that initial stage increasingly rewards correct answers in mathematics, coding and reasoning. An answer can be checked for correctness at the end of a task even if the explanation that leads to it is difficult for a person to read.

## Comparing similar meanings expressed in different ways

The researchers collected model output in three settings: chat, coding and essays. They used human writing from OpenSubtitles as a baseline for conversation, Stack Exchange for technical prose and the PERSUADE 2.0 corpus for student essays. They identified difficult constructions by analysing grammatical relationships between words, a method known as dependency parsing. They added automated classification when parsing alone could not determine whether a subject was animate or whether a noun had been turned into a verb.

A comparison between model text and human writing leaves a possible objection: the two sets of texts may discuss different subjects. A technical answer naturally uses different language from a film subtitle. To address this, the team created another version of each model sentence. A translation model with 3.3 billion parameters translated the sentence into Japanese and back into English. This preserved the broad meaning while changing how it was expressed.

Most frontier models' original responses contained more rare pairs of words, or bigrams, than their translated paraphrases. They also had higher n-gram perplexity, a measure of how unpredictable their sequences of words were. Similar differences appeared in their use of inanimate subjects, verbs derived from nouns and object-relative clauses with omitted connecting words. The Llama models and the OLMo base model changed less. OLMo Think, a reasoning variant, was more similar to the frontier systems. Claude Opus 5.5 scored lower than Opus 5 on 19 of 21 comparisons. That result shows that these tendencies can also decrease as models change.

Translation into another language and back is a control, not a perfect substitute for a human rewrite. Translation systems have their own preferences. The researchers chose Japanese precisely because translation through an unrelated language tends to produce more varied paraphrases. Still, this comparison keeps meaning more consistent than a comparison between unrelated documents written by humans and models. It suggests that the difficult forms arise partly from how the model expresses an idea, rather than only from the topic.

## Penalizing length changed the model's grammar

The second experiment tested a possible mechanism. The researchers fine-tuned Qwen2.5-1.5B-Instruct to turn structured records of events into sentences. Both a shorter construction and a longer one could express the correct answer. Reinforcement learning rewarded correctness, while an adjustable penalty discouraged longer output. Some training runs also included a constraint that discouraged the model from departing too far from its original distribution of tokens.

In the runs without that constraint, any positive penalty for length led to a categorical preference for the shorter form. More than 98% of answers used the short alternative for the constructions on which the model had been trained. The preference also appeared in unseen examples of similar constructions. Without the constraint that tied it to the base model, the model extended this preference to one of four more distantly related grammatical alternatives.

The model was never instructed to omit optional words. During training, it learned that doing so saved tokens while preserving correctness on the task. Human speakers vary these choices with context. The model instead learned a general preference for compressed expression. This small experiment demonstrates how an objective that rewards efficiency can produce language that differs from human usage.

The experiment does not prove that commercial laboratories apply the same penalty for length, or that one reward explains every pattern in closed models. The authors studied English, a limited set of prompts and a subset of available systems. They could not directly observe how frontier models were trained after their initial training, and they describe their intervention as a proof of concept. Their causal claim is narrow: under a controlled reward for brevity, grammatical preferences changed in the predicted direction.

## Readability becomes a requirement for models

The study treats readability as an alignment problem: models need to produce language that meets human needs, and researchers can measure aspects of that language. A useful answer must reach a correct conclusion, but people often also need to examine how it was reached. A developer reviews an agent's explanation of a patch. A doctor reads a summary before checking the chart. An analyst uses generated research to make a decision. Dense prose can obscure uncertainty and make oversight harder even when every sentence remains technically valid.

The measurements suggest practical tests. Alongside benchmarks for task performance, model developers can track the distance between related words, uncommon sequences of words and compressed constructions. They can reward successful communication during training, rather than assuming that optimization for other goals will preserve human preferences. The improvement from one Opus generation to the next shows that these linguistic tendencies can change.

The fictional editor returns to the sentence and adds one connecting word. Then she expands the string of nouns into a clause and makes a person the subject of the action. The facts have not changed, and the passage has grown by six tokens. The model uses a little more space, but the reader needs less effort to understand it.

## References

- Clark, T. H., Martin, M. B., & Mahowald, K. (2026). *Why is AI-generated language so hard to understand?* https://arxiv.org/abs/2610.29162
- Futrell, R., Mahowald, K., & Gibson, E. (2015). *Large-scale evidence of dependency length minimization in 37 languages*. https://doi.org/10.1073/pnas.1502134112
- Gibson, E., Futrell, R., Piantadosi, S. T., Dautriche, I., Mahowald, K., Bergen, L., & Levy, R. (2019). *How efficiency shapes human language*. https://doi.org/10.1016/j.tics.2019.02.003
- Levy, R., & Jaeger, T. F. (2007). *Speakers optimize information density through syntactic reduction*. https://proceedings.neurips.cc/paper/2006/hash/c6a01432c8138d46ba39957a8250e027-Abstract.html
- Martínez, E., Mollica, F., & Gibson, E. (2022). *Poor writing, not specialized concepts, drives processing difficulty in legal language*. https://doi.org/10.1016/j.cognition.2022.105070
- Smith, N. J., & Levy, R. (2013). *The effect of word predictability on reading time is logarithmic*. https://doi.org/10.1016/j.cognition.2013.02.013
