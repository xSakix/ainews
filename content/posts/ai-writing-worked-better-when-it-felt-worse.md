+++
title = "AI Writing Worked Better When It Felt Worse"
description = "A randomized experiment found that workers produced better briefs after an AI interface made them define the goal and divide the task. They also judged the tool less helpful, exposing a flaw in how teams evaluate AI products."
tags = ["research", "tools"]
date = 2026-10-23T04:10:11+02:00
draft = false
+++

Picture a policy analyst at the end of a long afternoon. She has an executive brief to write and a chat box that could produce a draft in seconds. Then the software slows her down. Before it will write, it asks who must read the brief, what that reader should do, how much detail belongs in the answer and which parts of the job should be handled separately. The analyst in this scene is invented. The delay is not: it is the central mechanism in a new experiment on what happens when an AI writing tool refuses to make thinking disappear.

## A writing tool that asks first

The preprint, posted on 22 October by Viktor Kewenig, Lev Tankelevitch, Sean Rintel, Advait Sarkar and Abigail Sellen of Microsoft Research, reports a randomized experiment with 297 US-based, English-first-language workers recruited through Prolific. Together they wrote 594 professional briefs. One group used a standard chat-and-canvas interface connected to GPT-5.3. The other saw dynamically generated controls that made them specify their goal and break the task into parts before the model drafted.

The scaffold asked for such things as the intended message, target reader, desired outcome, scope and depth. It then generated task-specific controls for analysis, structure and critical considerations. Participants could revise those controls in natural language. The interface did not replace chat; it inserted a planning layer before the familiar act of asking a model to write.

That extra layer improved the work. In the first task, when the scaffold was present, the researchers' automated judge found a statistically reliable advantage in the seven-part composite score. Human raters examining a 107-essay benchmark also found a larger composite advantage. The gains were not confined to tidier formatting: the automated scoring removed headings, emphasis and list markers before judging, and its strongest effects concerned argument quality, evidence credibility and attention to impact.

The stranger result arrived in the second task. Both groups now used the ordinary interface. People who had previously encountered the scaffold still wrote better briefs. Their prompts also stated goals more clearly and decomposed work more deliberately, according to blinded coding of the full prompt sequences. A short intervention appeared to change what people asked the AI to do after the intervention vanished.

## The uncomfortable signal

The participants did not reward the interface for this improvement. Those who used the scaffold rated the AI as less helpful and felt less in control. Their average workload score while the scaffold was active was 4.71, compared with 3.96 for the control group. When both groups moved to the unscaffolded second task, that workload difference was small and not statistically reliable.

The discomfort matters because ease is one of the most visible signals available to a product team. A feature that adds clicks, questions or decisions can look like a regression in a usability test. The experiment suggests that this signal can point in the wrong direction. The smoother experience may remove the mental work that helps a person frame the problem, decide what success means and notice what the model has left out.

Earlier research had already exposed parts of this conflict. Shakked Noy and Whitney Zhang found that ChatGPT could reduce completion time and improve quality on professional writing tasks. Zana Buçinca and colleagues found that cognitive forcing functions could reduce overreliance on AI advice, even though users did not always prefer the most effective intervention. In classrooms, Louis Deslauriers and colleagues showed that students in active-learning sessions learned more while feeling that they had learned less than peers in fluent lectures.

AI can sharpen the contradiction because it offers both assistance and offloading through the same box. A worker may experience the disappearance of effort as evidence that the tool helped. Yet effort is also how people establish goals, test arguments and build a memory of the material. Hamsa Bastani and colleagues illustrated the risk in a randomized study of high-school mathematics: access to a general GPT-4 tutor raised performance during assisted practice, but students later performed worse on an unassisted exam. A guarded tutor avoided most of that damage, though it did not produce an exam advantage over the no-AI control.

## Better work, narrow evidence

Kewenig and colleagues also tested memory. Three days after the writing session, 159 participants returned for a voluntary follow-up. Among those respondents, 64.6 per cent of the scaffolded group recalled the topic of the first task, compared with 45.6 per cent of controls. For the second, unscaffolded task, the figures were 54.4 and 38.0 per cent. An analysis that imputed missing outcomes preserved a positive association.

Those numbers need restraint. Nearly half the cohort supplied no scored recall response, the confidence intervals were wide, and the test credited any correct identification of the topic. It did not establish deep understanding. The experiment was not preregistered, used one-shot online writing tasks and measured transfer only to the next task. It cannot show that a week of prompts will become a durable professional skill.

The quality measure also deserves care. The primary judge was GPT-5.4, calibrated against human ratings. Its agreement with the human benchmark was moderate, and it compressed the range of scores people gave. The human subset supported the direction of the main result, but the two approaches emphasized different strengths. The authors therefore treat the quality scores alongside the prompting, self-report and recall evidence rather than as a verdict on their own.

There is another unresolved design question. The treatment combined goal specification with task decomposition, so the experiment cannot say which component did the work. It also lacked a static checklist condition. A simpler form might preserve some benefit without the same cognitive load. Only a longer workplace study could show whether repeated scaffolding becomes habit, becomes nuisance, or helps some workers while obstructing others.

## Friction whose value can be seen

The useful lesson is narrower than “make AI harder to use.” Most friction is merely friction. A slow response, an arbitrary form or an extra confirmation box does not create judgment. The intervention in this study targeted two specific acts that ordinary chat interfaces invite users to skip: naming the outcome and structuring the path toward it.

That distinction will become more important as AI products move from drafting sentences to carrying out whole sequences of work. When a system can plan, search and act before a person sees the intermediate steps, a pleasant experience may be one in which the user supplies less of the intent and understands less of the result. Teams will need measures beyond satisfaction: output quality, later performance, error detection and what users can explain after the tool closes.

Return to the imaginary analyst as she reviews the generated brief. The extra questions have cost her several minutes. She is still irritated by them. But when her director asks why the recommendation fits this audience, she can answer without reopening the chat. The interface felt worse because the tool left part of the work with her. That retained work may be the feature.

## References

- Bastani, H., Bastani, O., Sungu, A., Ge, H., Kabakcı, Ö., & Mariman, R. (2025). *Generative AI without guardrails can harm learning: Evidence from high school mathematics*. https://www.pnas.org/doi/10.1073/pnas.2422633122
- Buçinca, Z., Malaya, M. B., & Gajos, K. Z. (2021). *To Trust or to Think: Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making*. https://dl.acm.org/doi/10.1145/3449287
- Deslauriers, L., McCarty, L. S., Miller, K., Callaghan, K., & Kestin, G. (2019). *Measuring actual learning versus feeling of learning in response to being actively engaged in the classroom*. https://www.pnas.org/doi/10.1073/pnas.1821936116
- Kewenig, V., Tankelevitch, L., Rintel, S., Sarkar, A., & Sellen, A. (2026). *Metacognitive Scaffolds Create Productive Friction for AI-Assisted Knowledge Work*. https://arxiv.org/abs/2610.30945
- Noy, S., & Zhang, W. (2023). *Experimental evidence on the productivity effects of generative artificial intelligence*. https://www.science.org/doi/10.1126/science.adh2586
