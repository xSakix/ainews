+++
title = "Vision models can reason about beliefs after they see clearly"
description = "Seven vision-language models lost more than 20 points when false-belief problems moved from text to images. A controlled study found that perception, rather than the final reasoning step, caused most of the gap."
tags = ["research", "models"]
date = 2026-11-10T04:04:14+01:00
draft = false
+++

Picture a child watching a short scene on a screen. A red ball sits in a drawer. One character leaves, and another moves the ball into a box. When the first character returns, the child knows that the character will search the drawer. Now replace the child with a vision-language model. The model can explain false belief in text, but the moving object on the screen changes its answer. This scene is illustrative; it describes the kind of task that a new study isolates.

## The visual gap

Mohamed Rayan Barhdadi, Syed Talal Wasim, Juergen Gall and their colleagues tested seven vision-language models on false-belief problems. Their preprint, accepted to the NeurIPS 2026 Evaluations and Datasets track, reports more than 159,000 API calls across a five-condition protocol. Models that approached human-level performance on text versions lost more than 20 percentage points when the same underlying problem appeared visually.

False-belief tests have a long history in psychology. They ask whether a subject can separate reality from another person's knowledge of reality. In the standard pattern, an object moves while a character is absent. The correct answer requires the subject to predict what the character believes, even though the subject knows where the object actually is.

Recent language models often perform well on textual versions. Michal Kosinski evaluated eleven language models on forty bespoke false-belief tasks and reported that a 2023 version of GPT-4 solved 75 percent of them. A separate comparison by James Strachan and colleagues found that some language models reached or exceeded human performance on several theory-of-mind tests. Both papers also warned that a correct answer does not establish that a model reasons about minds in the same way that a person does. Memorised patterns, task structure and language cues remain alternative explanations.

The visual setting adds another dependency. Before a model can reason about what a character believes, it must identify the characters, objects, locations and changes that determine that belief. A wrong answer could therefore come from social reasoning, from perception or from the connection between them. A single score cannot tell those failures apart.

## Five views of the same problem

Barhdadi and colleagues designed five conditions that preserve the reasoning target while changing the quality and form of the perceptual evidence. The important intervention supplied models with ground-truth descriptions of the scene. With that scaffold, much of the text-to-image gap disappeared. The same repair did not occur when automatic parsers generated the descriptions, even when those parsers included frontier vision-language models.

That contrast locates the immediate bottleneck. The models could often use an accurate symbolic account of the scene to infer the absent character's belief. They failed when they had to produce that account from pixels themselves. Better prompting at the final question would not recover information that the visual front end had already missed or distorted.

The error pattern supports the same conclusion. Sixty percent of false-belief failures showed reality bias: the model answered with the object's actual location instead of the location that the absent character would remember. This resembles a failure to keep two representations separate. One describes the current scene; the other describes the scene that the character last observed.

Reality bias can look like a failure of social reasoning because the final answer ignores the character's perspective. The controlled conditions show that the model may never have constructed a usable account of that perspective. If a parser says that a character saw the move, or misses the moment when the character left, the later reasoning step receives the wrong problem.

The authors' ground-truth scaffold is diagnostic rather than a deployable solution. Real systems rarely receive perfect scene descriptions. An assistant that watches a workplace, a robot that acts around people or a tutoring system that follows a demonstration must decide which events each person witnessed. Those systems cannot assume that a human has already converted the video into the exact facts that matter.

## A benchmark for the boundary

Earlier visual theory-of-mind benchmarks already showed that multimodal systems struggle with intentions, beliefs and misleading displays. The new protocol adds a sharper separation between seeing and inferring. It asks whether the model can solve the reasoning problem when perception is held constant and then measures what happens as the perceptual support changes.

That separation matters for engineering. A team that observes a false-belief error might add longer reasoning traces or a larger language model. The study suggests a different first test: give the system a verified scene representation. If the answer becomes correct, the work should move toward object tracking, event parsing and perspective-specific memory. If the error remains, then the belief-reasoning component needs attention.

The result also limits broad claims about machine social intelligence. Text benchmarks can establish that a model maps a written scenario to an expected answer. They do not establish that the system can recover the relevant scenario from a changing physical world. A model that discusses another person's belief after reading a clean paragraph has completed only the second half of the job.

The paper provides code and data, which makes its conditions available for extension. The reported seven-model comparison is still a bounded laboratory test. It does not measure every visual model, every kind of social inference or performance in uncontrolled video. The preprint has not been peer reviewed through a journal, although its conference-track acceptance supplies a formal venue.

Return to the illustrative child and the moving ball. An engineer gives the model one extra line: the first character left before the ball moved. The model now predicts the drawer. Its reasoning looks better, although the reasoning machinery may not have changed at all. The missing piece was the event that the model failed to see.

## References

- Barhdadi, M. R., Wasim, S. T., Gall, J., Serpedin, E., & Kurban, H. (2026). *Perception, Not Reasoning, Limits Visual Theory of Mind*. https://arxiv.org/abs/2611.10694
- Kosinski, M. (2024). *Evaluating large language models in theory of mind tasks*. https://doi.org/10.1073/pnas.2405460121
- Strachan, J. W. A., Albergo, D., Borghini, G., Pansardi, O., Scaliti, E., Gupta, S., Saxena, K., Rufo, A., Panzeri, S., Manzi, G., Graziano, M. S. A., & Becchio, C. (2024). *Testing theory of mind in large language models and humans*. https://doi.org/10.1038/s41562-024-01882-z
