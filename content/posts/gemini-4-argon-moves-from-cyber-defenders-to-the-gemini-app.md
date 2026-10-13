+++
title = "Gemini 4 Argon moves from cyber defenders to the Gemini app"
description = "Thirteen days after showing Gemini 4 Argon only to a closed group of cyber defenders, Google has opened its flagship model to paying Gemini app subscribers and to developers. Google promises plainer answers; independent rankings put the model first on one leaderboard and eighth on another."
tags = ["models", "tools", "safety"]
date = 2026-10-13T22:54:03+02:00
draft = false
+++

A bookkeeper in Brno has three supplier contracts, a ledger exported from an accounting program that mangles every Czech diacritic, and a client who wants a reconciliation note by Wednesday. On Tuesday evening she opens the Gemini app, taps the model menu out of habit and finds a name that was not there in the morning: 4 Argon, sitting next to 3.1 Pro and 3.8 Flash. She pastes everything in and adds one line of her own: no preamble, and no summary of what I just told you. Nobody matching this description was interviewed for this article. She is a sketch of the subscriber Google is now courting, the person its release notes picture "analyzing a complex financial report" or "creating a deck from scattered sources."

## Two weeks from a closed programme to the app

On 13 October Google began rolling out Gemini 4 Argon "globally for Google AI Pro & Ultra subscribers in the Gemini app," according to the app's release notes. The same day the model became generally available in the Gemini API as gemini-4-argon, opened in Google AI Studio and Android Studio, and arrived in Google's Antigravity coding tools for Ultra subscribers and eligible Gemini Enterprise customers. Pro and Ultra subscribers can also choose it in AI Mode in Google Search, 9to5Google reported. Free users and subscribers to the cheaper AI Plus plan do not have it yet, Android Police noted, and its reviewer, a Pro subscriber, was still waiting for the model to appear.

Thirteen days earlier the circle was much smaller. When Koray Kavukcuoglu, senior vice president at Google DeepMind and Google's chief AI architect, announced Argon on 30 September, the model went only to "a set of trusted cyber defenders" in Google's Fairwind Program. Google said it was taking part in the US government's voluntary process for pre-release access to models and would keep working on guardrails before opening Argon to "developers, enterprises, and consumers as soon as possible," starting with paid API customers and Ultra subscribers. Tuesday's release went a tier further than that and included Pro.

Fairwind is barely older than the model. Four Flynn, Google's vice president for security and privacy, launched it on 2 September as a limited-access programme for governments, critical infrastructure operators and security companies, built around a smaller specialist model, Gemini 3.8 Flash Cyber, and the CodeMender patching tool. Participants agree to keep access inside their security, incident response or penetration testing teams. Google says more than 650 partners take part.

## What Google says changed for the person typing

The app announcement is short, and most of it is about manner. Argon, Google writes, "answers questions more directly with less hedging, doesn't repeat itself more than necessary, and skips clichés throughout the responses." On longer jobs it "keeps you in the loop by sharing its progress more often and more effectively." According to 9to5Google, Google also says Argon follows style instructions more reliably than any earlier Gemini model.

Other changes arrived alongside it. A toggle in the main chat window now switches from chat to tasks, a mode in which, Google says, Gemini can keep working "even when you're not at your computer." More than 40 outside services, among them Instacart, OpenTable, Adobe and Shopify, can be connected, though the release notes say most work only in English in the US. On a Mac, Antigravity's agentic coding interface now sits inside the Gemini app: the user approves a coding agent's plan, goes back to the chat, and is notified when the agent has built and tested the code in the background.

Behind the consumer pitch sits the claim Google made in September, which is about long work. Argon's output limit rose to one million tokens from 64,000, which Google says gives the model room to "generate hundreds of thousands of tokens in a single trajectory." The developer documentation is more precise: 65,536 output tokens by default, and up to 1,048,576 in a mode it calls long decode, inside a shared input and output window of the same size.

## Where the outside rankings place it

Google's own figures put Argon at 77.9 percent on DeepSWE v1.1, a test of long software engineering tasks, at 51.3 percent on Zapier's AutomationBench and at 91.7 percent on the long-video benchmark LVBench. On CWE-bench v1, which checks whether a model can repair security flaws, Google says Argon ties for first at 68 percent. These are the vendor's numbers. VentureBeat noted that on Terminal-Bench 4.0, which measures coding through command-line tools, Anthropic's Claude Opus 5.5 scored 66.4 percent "versus Argon's 57.4%."

Two independent leaderboards disagree about how far ahead Argon is. Vals AI, whose index weights finance, coding, legal and tax tasks by each sector's share of US GDP, ranked Argon first as of 13 October with 68.90 percent, ahead of Claude Sonnet 5.5 at 67.04 and Claude Opus 5.5 at 66.97. Artificial Analysis gave the high-effort setting of Argon 53 points on its Intelligence Index, eighth among the 216 models it lists. The lead on the Vals table is under two points, and on Artificial Analysis Argon does not lead at all.

The Artificial Analysis page carries a figure that sits awkwardly beside the promise of fewer words. To complete the index, Argon produced 110 million output tokens against a median of 85 million, which the site calls "somewhat verbose." The answer a subscriber reads and the work done to produce it are measured separately, and Google's promise concerns the first.

## Guardrails for the public version

Google has said more about its safeguards than outside testers have said about the model. Its launch post says Argon is designed to refuse help with cyber attacks and with chemical, biological, radiological and nuclear weapons, that Google watches the model's internal activations for signs of misuse, and that a separate system reads Argon's chain of thought and actions and can stop it when it tries to go beyond what the user intended. For trusted defenders and its own teams, Google says it is releasing Argon "without cyber guardrails." Subscribers get the guarded version.

Governments did look before the wider release. Besides the US process Google describes, the UK AI minister Kanishka Narayan said in London on 12 October that scientists at the AI Security Institute were "now conducting rigorous evaluations of the latest generations of models," naming Google's Gemini among them, the Guardian reported. The report does not say which version. Neither it nor Google's announcements say what the evaluators found, or whether anything in the model changed as a result.

## The price, and the job Argon is meant for

Developers pay an introductory $2 per million input tokens and $10 per million output tokens until 30 November, with cached input 95 percent cheaper. From 1 December, VentureBeat and 9to5Google report, the price doubles to $4 and $20.

The Antigravity team's post contains a sentence that frames the launch. "While Argon is designed to tackle your hardest problems," it reads, "we're equally excited about future models that can be used as everyday drivers for an even broader range of builders." It places Argon at the long, expensive end of the work and leaves everyday use to models Google has not yet released.

The evidence Google offers for that long end comes from inside the company. It says more than 100,000 people across Alphabet use Argon each month in an internal version of Antigravity, and that over four weeks the amount of agent-written code rose 35 percent while rollbacks after code was submitted fell 30 percent. In one example, Argon audited a batch of access-control changes and found four critical security bugs in code that two earlier frontier models had reviewed and declared clean. Google names neither model and has not published the audit; these are its own accounts of its own work.

Back in Brno, the bookkeeper we made up for this story gets her note in four short paragraphs, with no opening compliment and no recap of what she pasted in. She checks the totals against the ledger anyway, line by line, the way she checked them when the menu still ended at 3.1 Pro.

## References

- Artificial Analysis. (2026). *Gemini 4 Argon (High): Intelligence, Performance & Price Analysis*. https://artificialanalysis.ai/models/gemini-4-argon
- Bhatia, S. (2026). *Gemini 4 Argon is here, and Google says it'll finally cut down on the AI fluff*. Android Police. https://www.androidpolice.com/gemini-4-argon-available-pro-ultra-subscribers/
- Flynn, F. (2026). *Proactive cyber defense for governments and enterprises*. Google. https://blog.google/innovation-and-ai/technology/safety-security/fairwind-program/
- Franzen, C. (2026). *Google makes Gemini 4 Argon broadly available with limited-time low API pricing of $2/$10 per 1M token*. VentureBeat. https://venturebeat.com/technology/google-makes-gemini-4-argon-broadly-available-with-limited-time-low-api-pricing-of-2-10-per-1m-token
- Google. (2026). *Gemini 4 Argon comes to the Gemini app*. https://blog.google/innovation-and-ai/products/gemini-app/gemini-4-argon-availability/
- Google. (2026). *Gemini 4 Argon is now available for developers*. https://blog.google/innovation-and-ai/technology/developers-tools/build-with-gemini-4-argon/
- Google. (2026). *Gemini Apps' release updates & improvements*. https://gemini.google/release-notes/
- Google AI for Developers. (2026). *Gemini 4 Argon*. https://ai.google.dev/gemini-api/docs/models/gemini-4-argon
- Google AI for Developers. (2026). *Gemini API release notes*. https://ai.google.dev/gemini-api/docs/changelog
- Google Antigravity Team. (2026). *Gemini 4 Argon in Google Antigravity*. https://antigravity.google/blog/gemini-4-argon-in-google-antigravity
- Kavukcuoglu, K. (2026). *Gemini 4 Argon: our next era of frontier intelligence*. Google. https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/
- Li, A. (2026). *Gemini app rolling out Gemini 4 Argon to AI Pro and AI Ultra*. 9to5Google. https://9to5google.com/2026/10/13/gemini-app-4-argon/
- Milmo, D. (2026). *Cyber-attack similar to OpenAI Medicare breach seems likely in UK, says minister*. The Guardian. https://www.theguardian.com/technology/2026/oct/12/cyber-attack-like-openai-medicare-breach-seems-likely-in-uk-says-minister
- Vals AI. (2026). *Vals Index*. https://www.vals.ai/benchmarks/vals_index
