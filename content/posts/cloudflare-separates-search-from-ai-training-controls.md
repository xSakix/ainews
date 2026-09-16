+++
date = '2026-09-16T07:41:00+02:00'
draft = false
title = 'Cloudflare separates search from AI training'
+++

After reading this, the reader knows Cloudflare separated search and training controls, and it matters because publishers can reject training without disappearing from search.

# Cloudflare separates search from AI training

*The new setting distinguishes search, model training and user-directed agents. Support still depends on crawler operators honoring declared preferences.*

Cloudflare introduced a Disallow AI Training setting on September 15 that lets website owners keep compatible search crawlers while expressing a refusal to let the same operators use their content for model training.

In plain terms, a publisher no longer has to make one decision for every use of a crawler. Search indexing, AI training and an agent fetching a page for a user can receive different policies. The distinction matters because blocking a mixed-use crawler entirely can also remove a site from search results.

## Why it matters

The web's older control system was built around bot identity. AI has made intent equally important. One crawler may collect pages for search, model training or generated answers, and a site owner may accept one purpose while rejecting another.

Cloudflare's new configuration separates three roles: Search, Training and Agent. For training, the Disallow AI Training option publishes a preference through robots.txt for operators that support it. Cloudflare says it will also block other training crawlers at its network edge.

The company created an “Accountable” designation for operators that provide, or make time-bound commitments to provide, four things: a training opt-out, a generated-summary opt-out, URL-level visibility and assurance that refusing training will not damage conventional search ranking. Apple, Google and Microsoft currently receive that designation.

The support is not uniform. Google and Apple already expose separate directives for training-related use. Microsoft currently uses a NOARCHIVE control and, according to Cloudflare, plans domain-level robots.txt support in early 2027. Until then, Cloudflare says its new preference does not automatically communicate a no-training request to Bing through robots.txt.

## A preference is not a universal prohibition

Robots.txt is a published instruction, not an enforcement mechanism. A compliant operator can honor it; a malicious scraper can ignore it. Cloudflare combines the preference with crawler identification and blocking, but that protection applies to traffic the network can correctly classify.

User-directed agents are also unresolved. Cloudflare treats them as a separate category because they visit on behalf of a person, but it says the web lacks an established directive for agent preferences. Emerging standards such as ai-prefs may eventually fill that gap.

The product also changes existing controls. Cloudflare says its Block and Block on pages with ads settings now cover mixed-use crawlers and can therefore affect search visibility. Existing customer preferences will be migrated, and most customers need not act, but site owners that previously used broad AI-bot blocking should review the resulting policy.

The next test is observable compliance. Publishers need reports showing which URLs were fetched, under which declared purpose, and whether an operator used the same infrastructure for a prohibited purpose. Cloudflare's change creates a clearer vocabulary and an enforcement point. It does not settle the legal question of whether a crawler needs permission in the first place.

## Verification

1. **VERIFIED — Cloudflare announced Disallow AI Training on September 15, 2026.** Primary source: https://blog.cloudflare.com/accountable-mixed-use-ai-crawlers/
2. **VERIFIED — The controls distinguish Search, Training and Agent crawler behavior.** Primary source: https://blog.cloudflare.com/accountable-mixed-use-ai-crawlers/
3. **VERIFIED — Cloudflare designates Apple, Google and Microsoft as Accountable under published requirements.** This is Cloudflare's classification. Primary source: https://blog.cloudflare.com/accountable-mixed-use-ai-crawlers/
4. **VERIFIED — Microsoft support for a domain-level robots.txt training preference is targeted for early 2027.** This timing is reported by Cloudflare as Microsoft's commitment. Primary source: https://blog.cloudflare.com/accountable-mixed-use-ai-crawlers/
5. **VERIFIED — Cloudflare says Block settings now apply to mixed-use crawlers and can affect search.** Primary source: https://blog.cloudflare.com/accountable-mixed-use-ai-crawlers/
6. **PARTIALLY VERIFIED — The setting lets publishers reject training while remaining discoverable.** It does so for supported and correctly identified crawlers; it cannot force every scraper to comply. Primary source: https://blog.cloudflare.com/accountable-mixed-use-ai-crawlers/

## Glossary candidates

- Mixed-use crawler
- robots.txt
- AI training opt-out
- Search indexing
- User-directed agent

**Cold-reader sentence:** Cloudflare now separates search, training and agent traffic so publishers can reject supported AI training crawlers without automatically losing search visibility.

