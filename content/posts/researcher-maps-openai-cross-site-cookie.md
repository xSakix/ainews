+++
date = '2026-09-21T04:05:00+02:00'
draft = false
title = "Researcher Maps OpenAI's Cross-Site Cookie"
+++

After reading this, the reader knows what browser traffic the researcher observed, what OpenAI discloses and which account-linkage claim remains inferred.

# Researcher Maps OpenAI's Cross-Site Cookie

*An independent test found one OpenAI identifier on advertiser-page requests, while the crucial server-side account join was not directly observed.*

Security researcher Lucian Buchodi has documented an OpenAI advertising identifier moving from ChatGPT to third-party websites that load OpenAI's advertising code.

The identifier is stored in a cookie named `__obi`. Buchodi reports that OpenAI's synchronization endpoint set the cookie for the `.openai.com` domain with the `SameSite=None` and `Secure` attributes. On Chrome for Android, the browser then attached that cookie to requests for OpenAI's advertising script and event collector when participating merchant pages loaded.

OpenAI's cookie policy, updated on 10 September, confirms that `__obi` is an OpenAI cookie with a one-year duration on `chatgpt.com` and `openai.com`. The policy classifies it as analytics rather than marketing. It describes analytics cookies generally as tools for understanding service performance and use, but it does not explain this cross-site flow.

## Why it matters

Advertising pixels normally help platforms measure whether an ad led to a visit or purchase. A stable platform identifier can make that measurement more accurate across sites. The privacy issue is whether people understand that an analytics choice inside a conversational product may also enable browser requests from unrelated commercial pages to carry the same identifier.

Buchodi's capture found `__obi` on the request that fetched OpenAI's advertising script, on conversion-event requests and on a nominal no-credentials path. He also observed the same value across multiple advertisers. In the broader dataset he examined, page URLs were reduced to origin and path rather than including query strings, but some paths themselves exposed sensitive context.

The advertising software also collected values from form fields, rendered page text and tag-manager data, according to the analysis. Email addresses, phone numbers and names were hashed before transmission; location fields such as city and postal code could travel in clear text. A configured denylist excluded several sensitive categories.

## The limit of the evidence

The strongest headline version goes beyond what was observed. Buchodi saw synchronization tokens carrying an account subject and later saw the cookie accompany advertiser-page events. He did not watch OpenAI resolve a third-party event to a named ChatGPT account on its servers. He describes that join as an inference from the system's design.

The test also has platform limits. It was reproduced on Chrome for Android. Desktop Chrome was not tested, and WebKit's third-party-cookie controls prevent the described mechanism on iOS browsers. Buchodi says roughly one in five ChatGPT sessions in his test produced a synchronization token, so the flow was not universal.

OpenAI Support acknowledged the researcher's questions and said the observations would be reviewed internally, according to the post, but did not answer why `__obi` is classified as analytics or how consent choices apply. OpenAI has not publicly confirmed the inferred account-resolution step.

The evidence supports a narrow conclusion: an OpenAI identifier associated with synchronization traffic was repeatedly sent from advertiser sites on the tested browser. It supports scrutiny of consent and classification. It does not by itself prove that every event was joined to a named account or used to personalize ChatGPT.

## Verification

- **Tier 0 — VERIFIED:** OpenAI lists `__obi` as a one-year analytics cookie on `chatgpt.com` and `openai.com`. Primary source: https://openai.com/policies/cookie-policy/
- **Tier 1 — RESEARCHER-REPORTED:** Cookie attributes, captured requests, payload fields and observed reach come from Buchodi's independent analysis. Source: https://www.buchodi.com/chatgpt-now-knows-what-you-do-on-other-websites-via-ad-collector/
- **Tier 3 — UNVERIFIED:** Server-side resolution of advertiser events to a named ChatGPT account was inferred, not observed or confirmed by OpenAI. Same source.
- **Tier 1 — RESEARCHER-REPORTED:** The Android, iOS, desktop and gating limitations are stated by the researcher. Same source.
- **Tier 2 — ANALYSIS:** Consent and product implications are editorial analysis.

## Glossary candidates

- **Advertising pixel:** Code loaded on a page to report visits or conversions to an advertising platform.
- **SameSite:** A cookie setting that controls whether browsers attach the cookie to cross-site requests.

Cold-reader sentence: A researcher saw OpenAI's `__obi` identifier cross advertiser sites, but did not directly observe OpenAI join those events to named accounts.
