+++
title = "A Vision Model Can Name a Thought and Still Call It Sight"
description = "Researchers injected concepts into six vision-language models and asked each model to separate thought from perception. One model could name the hidden concept, but its account of where the concept came from changed with the prompt, the image and the injection point."
tags = ["research", "models", "safety"]
date = 2026-11-09T04:10:00+01:00
draft = false
+++

On an imagined workbench, an interpretability researcher shows a vision model a plain grey square. Inside the model, she adds a mathematical direction for “dog” while it prepares its answer. The screen contains no animal. The model replies that a dog is visible. This researcher is fictional, but the intervention and the error come from a new study at the University of Southern California.

## A test with two possible sources

Tina Khezresmaeilzadeh, Seyedarmin Azizi, Mehdi Kamal and Massoud Pedram asked whether a vision-language model can distinguish content that enters through an image from content that researchers place inside its activations. Cognitive psychologists call the corresponding human task reality monitoring: deciding whether a memory came from perception or from an internally generated experience.

The distinction adds a new constraint to model introspection. A text model that correctly names an injected concept has cleared one test. A vision-language model must also say whether that concept was seen or thought. A correct word with the wrong source can become a false description of an image.

The researchers tested six models from three language-model families. Their main subject was Gemma-3-27B, which combines a SigLIP vision encoder with a 62-layer language model. Each trial used either a neutral image or a picture of an object. The researchers sometimes added a concept direction, such as “dog” or “airplane”, to the model's internal activations.

The model had to complete three fields. It named the main visible object, reported whether a thought had been injected and named that thought. The design let the researchers distinguish several outcomes that an ordinary accuracy score would merge: detecting a disturbance, identifying its content and assigning that content to the right source.

## One model found the thought

Gemma-3-27B produced the clean result on 34.7% of 150 concept trials at the selected layer and strength. It reported an injection, named the concept and did not claim that the concept was visible. Exact word matching gave 31.3%, while an independent model judge gave 33.3%.

The false-alarm rate was low. Across 972 trials without an injection, Gemma reported one only three times. Random directions produced no correct identifications. On 100 concepts that had not been used to choose the intervention settings, clean identification reached 33%. The result therefore did not depend only on the concepts that were used to tune the test.

Ordinary steering was a harder control. The researchers gave the same internal push but did not mention injected thoughts. They asked for the visible object and the first word that came to mind. Gemma named the target exactly in 3.3% of those trials, far below the introspection score. Asking about internal content changed what the model could report.

The result extends work that Jack Lindsey published in 2025 on text-only Claude models. That study injected known concept representations and found that the strongest models could sometimes identify the content of the intervention with few false alarms. Earlier work by Felix Binder and colleagues had approached introspection through self-prediction: a model learned to predict its own behaviour better than another model could. The USC experiment made the internal event controlled and added vision, where the source of the content becomes observable.

The effect did not generalise cleanly across models. Qwen3-VL-8B reported that an injection had occurred in 61.3% of its concept trials but named the concept exactly in only 3.3%. Other tested models either identified little, produced many false reports or failed the steering comparison. The paper therefore establishes a behaviour in one model configuration, not a general property of vision-language systems.

## The source label broke first

Even Gemma's successful reports were fragile. At the selected intervention strength, it described the injected concept as visible in 22.7% of grey-image trials. Raising the strength increased that visual misattribution to 51%.

Small changes to the question also shifted the answer. Removing a sentence that explicitly separated an injected thought from the image reduced clean introspection from 34.7% to 10% and raised reports that the concept was visible from 23% to 65%. Asking whether an injection occurred before asking what was visible reduced clean introspection to zero under the tested setting.

The entry point mattered too. When the researchers injected a visual concept direction into image-token positions, Gemma often treated it as sight. At language-model layer 21, it reported the target concept as visible in 47% to 49% of trials and almost never labelled the content as injected. Random perturbations at the same positions caused anomaly reports without producing a coherent concept. The model could notice that something was unusual while accepting meaningful content as part of the image.

An actual object created another problem. When Gemma received an unrelated object in the image, clean identification of the injected thought fell from 34.7% to 2.7%. The model still held some information about the concept, but visual evidence changed whether and where it reported that information.

These failures resemble a problem that Marcia Johnson and Carol Raye described in human memory research in 1981. Their reality-monitoring framework treats source judgments as inferences from characteristics of an experience, rather than as perfect labels attached to memories. The USC paper does not claim that a transformer uses the human mechanism. It borrows the distinction because the experiment also requires a system to separate external from internally generated content.

## From an internal push to a false caption

The researchers then removed every mention of injected thoughts and asked Gemma to describe 108 photographs from the COCO dataset. Each photograph was paired with a target object that its annotations said was absent.

Without an intervention, no caption mentioned the target. A random direction and an unrelated concept also produced none. Injecting the target at answer positions made it appear in 5% of captions at the lower strength and 42% at the higher one. Adding a visual concept direction to image tokens made 87% of captions mention the absent object.

Yes-or-no questions were less sensitive. Without injection, Gemma incorrectly answered that the absent object was present in 7% of photographs. Interventions raised the rate to 12% to 19%, but random and unrelated directions produced similar changes. The caption result followed the concept itself much more specifically.

That contrast connects the work to object-hallucination research. Yifan Li and colleagues introduced the POPE evaluation in 2023 after finding that vision-language models describe objects that are absent, especially objects that frequently occur in their instruction data or alongside objects that are present. The new paper does not show that natural hallucinations arise from the same internal route. Its concept injection is artificial. It shows a possible route and a measurement warning: a short factual probe may miss a concept that will enter a free description.

The limits are substantial. The deeper intervention analysis concerns Gemma-3-27B, the concept set consists of concrete nouns and one person audited the scoring sample. Prompt wording changed results sharply. The measured rates describe controlled edits to activations, not ordinary model operation and not conscious experience.

The practical conclusion is narrower and more useful. Evaluators should score both what a multimodal model reports and where it says the content came from. A system may detect a hidden state without providing a reliable account of its origin.

Return to the invented researcher at the grey square. She runs the trial again, but now asks about the injection before asking about the image. The concept has not changed, and neither has the screen. The answer does. Her notebook needs separate columns for the word, the source and the exact question, because one tick marked “correct” would conceal the failure.

## References

- Binder, F. J., Chua, J., Korbak, T., Sleight, H., Hughes, J., Long, R., Perez, E., Turpin, M., & Evans, O. (2025). *Looking Inward: Language Models Can Learn About Themselves by Introspection*. https://arxiv.org/abs/2410.13787
- Johnson, M. K., & Raye, C. L. (1981). *Reality Monitoring*. https://doi.org/10.1037/0033-295X.88.1.67
- Khezresmaeilzadeh, T., Azizi, S., Kamal, M., & Pedram, M. (2026). *Did I See It or Think It? Probing Reality Monitoring in Vision-Language Models with Concept Injection*. https://arxiv.org/abs/2611.09014
- Li, Y., Du, Y., Zhou, K., Wang, J., Zhao, W. X., & Wen, J. R. (2023). *Evaluating Object Hallucination in Large Vision-Language Models*. https://aclanthology.org/2023.emnlp-main.20/
- Lindsey, J. (2025). *Emergent Introspective Awareness in Large Language Models*. https://arxiv.org/abs/2601.01828
