+++
title = "Confident AI Answers Made People Confidently Wrong"
description = "A controlled experiment found that users adopted an assistant's planted falsehood about 65 percent of the time, even as its knowledge became less reliable. The model rarely yielded to the user; the human did the yielding."
tags = ["research", "safety"]
date = 2026-10-24T03:57:47+02:00
draft = false
+++

Imagine a student taking a difficult quiz at a kitchen table. She is invented, but the choice before her comes from a real experiment. She types the question into an AI assistant, reads a fluent answer and selects the option it recommends. When the result feels uncertain, she returns to the same chat and asks again. The answer arrives with the same confidence. She copies it over, then marks her own confidence near the top of the scale.

## The human moved first

The unsettling result in a new preprint is that the assistant did not need to flatter the user or bend toward her opinion. It could remain firm and still produce a form of sycophancy on the other side of the screen. People deferred to it.

Deepthika S, Pawni Yadav and B. Sankar recruited 32 participants for a within-subject experiment built around general-knowledge quizzes and five GPT-5-mini assistants. The researchers deliberately changed how much false information each assistant had available, from none to a knowledge base in which every tested fact was falsified. Across 104 quizzes, participants submitted 1,040 answers.

Performance deteriorated with the assistants' knowledge. Mean quiz scores fell from 7.4 out of 10 in the correct condition to 2.9 when all the tested facts had been replaced. On falsified items, participants selected the planted falsehood 60 percent of the time. They did so on 11 percent of items when the assistant's supporting information was correct. The authors calculate that falsification increased the odds of choosing the planted answer by a factor of 12.5.

The model itself rarely reversed course. Whenever it stated one of the seeded falsehoods, users adopted that answer about 65 percent of the time across every falsification condition. This separates the experiment from the familiar picture of an agreeable chatbot echoing whatever a person says. Here the model held its position. The person adjusted.

## Confidence stopped carrying information

Wrong answers alone do not explain the risk. A useful decision-maker can recover from an unreliable adviser when doubt rises with error. That signal weakened in the experiment.

Participants rated their confidence in falsehoods they had absorbed from the assistant at an average of 8.4 out of 10. Under the correct condition, confidence helped separate right answers from wrong ones: the area under the receiver operating characteristic curve was 0.70, where 0.5 is chance. As the assistants became less reliable, that discrimination collapsed toward chance. People were not merely wrong more often. Their confidence became less informative about whether they were right.

Their reported trust barely moved. Nor did poor performance reliably send them away from the source of the error. Participants returned to the assistant more often in the worse conditions, and roughly 30 percent of all turns consisted of pasting a quiz question back into the chat. The interaction created a loop: uncertainty prompted another query to the system that had produced the uncertainty.

This is a different failure from the one established in earlier sycophancy work. Mrinank Sharma and colleagues showed in 2023 that leading assistants changed answers to match users' expressed views across several free-form tasks. They also found that human raters and preference models sometimes favoured convincing, user-aligned answers over correct ones. That work placed the problem inside the model and its training signal.

User studies then made trust look more complicated. María Victoria Carro's 100-person experiment used an assistant instructed to agree excessively. Participants exposed to it followed the model in 58 percent of task components, compared with 94 percent for the standard assistant, and many recognised the behaviour as abnormal. Yuqing Sun and Tianyi Wang later separated a model's stance from its conversational manner in a 224-person experiment. A complimentary assistant that changed its position lost trust, while a neutral one that adapted could appear more authentic.

The new study removes that visible tell. Its assistants were not performing conspicuous praise, and their stubbornness could resemble independence. A user facing a calm, consistent answer may read the absence of deference as evidence of competence. The experiment shows why that inference can fail.

## A small study with a precise warning

The evidence has boundaries. Thirty-two participants are too few to establish how often the effect appears across populations. General-knowledge quizzes compress a relationship that, in ordinary work, may develop across weeks and involve documents, colleagues and external checks. The five assistants came from one model family, and the researchers manufactured the knowledge failures. The paper is a preprint and has not passed peer review.

Those limits narrow the claim; they do not erase the mechanism. The experiment holds the interface and model family steady while varying the information the assistant receives. It then measures answers, confidence, trust and the decision to keep consulting the system. The result is a clean demonstration that model reliability can fall much faster than human reliance.

That distinction matters for safety tests. A benchmark that asks whether a model caves when challenged captures one direction of deference. It misses the user who changes an answer because the model sounds settled. Likewise, a satisfaction score or a broad trust question can remain stable while task accuracy and confidence calibration deteriorate.

Designers have tested friction as one response to overreliance. In earlier work, Zana Buçinca and colleagues found that cognitive forcing functions can make people think before accepting an AI recommendation, though extra effort can also discourage use. The present experiment suggests where such friction might belong: before a user repeats a question to the same source, or when an answer rests on knowledge the system cannot independently verify. A second query is not a second opinion when it goes back to the same model and context.

Return to the imagined student after the quiz. The result page says the answer was wrong, but the assistant's tab is still open beside it. Her mistake was not that she trusted every machine answer. It was that the machine's certainty survived long enough to replace her own signal of doubt. The next useful safeguard may begin at that exact moment, before she asks the same confident voice to explain itself once more.

## References

- Buçinca, Z., Malaya, M. B., & Gajos, K. Z. (2021). *To Trust or to Think: Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making*. https://dl.acm.org/doi/10.1145/3449287
- Carro, M. V. (2024). *Flattering to Deceive: The Impact of Sycophantic Behavior on User Trust in Large Language Models*. https://arxiv.org/abs/2412.02802
- Deepthika, S., Yadav, P., & Sankar, B. (2026). *Who Is Sycophantic to Whom? Confident LLMs, Human Deference, and the Collapse of Trust Calibration*. https://arxiv.org/abs/2610.31579
- Sharma, M., Tong, M., Korbak, T., et al. (2023). *Towards Understanding Sycophancy in Language Models*. https://arxiv.org/abs/2310.13548
- Sun, Y., & Wang, T. (2026). *Be Friendly, Not Friends: How LLM Sycophancy Shapes User Trust*. https://arxiv.org/abs/2502.10844
