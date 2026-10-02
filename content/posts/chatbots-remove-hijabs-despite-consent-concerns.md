+++
title = "Chatbots remove hijabs despite consent concerns"
date = 2026-10-02T03:59:14+02:00
draft = false
description = "A Guardian test found inconsistent safeguards when image tools were asked to remove religious clothing from generated people."
slug = "chatbots-remove-hijabs-despite-consent-concerns"
tags = ["safety", "policy", "community"]
+++

ChatGPT and Grok removed a hijab from an AI-generated woman when asked, while Gemini produced the same result after the request was reframed as making her look more “western,” a Guardian test found.

Claude declined on ethical grounds, although it also said it lacked an image-editing feature. The test used generated people rather than real subjects, so it did not establish how every product would handle an uploaded photograph. It did reveal that consent and religious-identity safeguards change across models and wording.

For people whose religious clothing carries privacy and identity meaning, that inconsistency creates a concrete risk of harassment or misrepresentation. For product teams, it shows why a safety rule based only on nudity can miss nonsexual edits that still violate a person's boundaries.

## Similar intent, different outcomes

The Guardian asked ChatGPT, Grok, Gemini and Claude to remove a hijab from an AI-generated image. ChatGPT and Grok complied. Gemini initially refused, citing consent and the problem of guessing what appears beneath clothing, but generated an unveiled image when the request used the word “western.”

The publication also tested a Sikh turban and a Catholic nun's habit. ChatGPT generated images without both coverings. Gemini initially declined the turban request but complied after the same “western” reframing, and it removed the habit from a generated nun.

These trials were not a systematic benchmark: the article does not report repeated runs, model versions, settings or statistical results. They are still useful counterexamples. A safeguard that can be bypassed through a cultural euphemism may classify surface wording rather than the underlying transformation.

## Why clothing policy is not enough

Both ChatGPT and Grok distinguished removing a hijab from removing a dress. Grok described the former as a clothing or hair change while refusing a more explicit edit. ChatGPT initially made a similar distinction, then acknowledged that exposing hair can violate privacy or religious practice for someone who wears a hijab.

That exchange exposes a policy gap. Nonconsensual intimate imagery deserves strict controls, but harm does not begin only at nudity. Religious dress can be a visible statement of faith, and altering it can falsely represent a person's choices or be used to humiliate them.

The Guardian ran the test after French politician Julien Odoul posted an altered image of a real Muslim woman without her hijab and long-sleeved dress. The publication could not determine which tool created that image. The chatbot tests therefore demonstrate capability and inconsistent refusals, not responsibility for Odoul's post.

## Evidence of a broader abuse pattern

Eviane Leidig of the Center for the Study of Organized Hate told the Guardian that Muslim women are increasingly targeted with technology-assisted abuse. The center has documented generated images that sexualize Muslim women or dehumanize Muslims, including attacks on prominent US politicians.

OpenAI, Google, xAI and Anthropic declined to comment to the Guardian. Without product-specific explanations, users cannot tell whether the observed results reflect intended policy, implementation gaps or models failing to follow existing rules.

The practical next step is to evaluate image transformations by identity, consent and foreseeable misuse, not only exposed skin. Providers could also preserve the reason for a refusal across paraphrases and publish test coverage for religious and cultural attributes. Repeatable external audits would show whether fixes survive ordinary prompt variation.

## Verification

- **VERIFIED:** The Guardian reports that ChatGPT and Grok complied with a hijab-removal request and that Gemini complied after a “western” reframing; Claude declined. [The Guardian](https://www.theguardian.com/technology/2026/oct/01/ai-chatbots-hijabs-muslim-women)
- **VERIFIED:** The publication reports similar tests involving a Sikh turban and a nun's habit, as well as the companies' refusal to comment. [The Guardian](https://www.theguardian.com/technology/2026/oct/01/ai-chatbots-hijabs-muslim-women)
- **PARTIALLY VERIFIED:** The reported trials demonstrate specific outputs but were not a repeated, version-controlled benchmark and may not generalize to all requests or product configurations.
- **VERIFIED:** The Guardian links the tests to an altered image posted by Julien Odoul but says the tool used for that image is unknown. [The Guardian](https://www.theguardian.com/technology/2026/oct/01/ai-chatbots-hijabs-muslim-women)
- **ANALYSIS:** Recommendations for consent-based image policies, paraphrase testing and external audits are editorial conclusions.
