# Editorial audit — 29 September 2026

## Scope and output

Controlling files: `prompts/main-prompt.md`, `prompts/research-prompt.md` and `prompts/article-writer-prompt.md`, read from live `main`. The first prompt delegates selection and requires one article per eligible distinct news event plus one combined community digest. No AGENTS.md was present in the recursive repository tree.

Review base: `0bfb44464adcff66287dcb6751d6efd6ed195380`. News window: September 28 02:57 UTC–September 29 02:57 UTC. Community window: seven days. Date-only announcements are identified as such; an exact publication hour cannot be inferred from the date alone.

The output comprises **16 individual explainers, one seven-item community digest, today's briefing and this audit**. Twelve of the explainers recover the previously prepared September 28 Gemini supplement, which had not reached main; four address additional developments found in current research. The two supplemental reports are also preserved. There are **21 new Markdown files** in the complete change.

Fifteen explainers have directly retrieved or indexed primary-source support for their central announcement. The OpenAI release-decision article is explicitly **reported coverage**, with the independently unretrieved primary statement and underlying tests marked UNVERIFIED. It is not counted as independently primary-verified. No benchmark, safety claim or acquisition benefit is described as experimentally reproduced here.

## Repository reconciliation

Read today's `2026-09-29-ai-briefing-anthropic.md`, yesterday's Gemini and Anthropic inputs, the September 28 briefing and audit, and the existing September 28 digest. Inspected the recursive live tree and searched repository contents for the new events and community source titles. Earlier checks for the twelve recovered stories are documented in `2026-09-28-gemini-editorial-review.md`.

Today's searches found no existing post for Heidi II, Lenovo Googlebook, Robotiq.ai, GPT-6.1 Astra, ImaJev, the current reward-hacking discussion, Glyph's essay, Ewerlöf's essay or Newport's current investigation essay. The architecture query found older general discussions, not this event. A transient search-rate limit on Googlebook was retried successfully. Existing NYC legislation coverage and the new subpoena are distinct events; existing Muse/Shopify partnership coverage and the checkout API release are also distinct.

The source reports remain unchanged. The previous day's digest remains unchanged. Publication timestamps for all new posts use actual current time minus one hour, as instructed.

## Today's Anthropic companion: every entry reconciled

| Entry | Decision and correction |
| --- | --- |
| Sonnet 5.5 | Publish recovered explainer once. Use official announcement and GitHub partner release; preserve evaluator attribution. |
| Jeff | Publish recovered explainer. Correct the companion's claim of training in approximately 30 ms: the milliseconds describe inference, not training. Repository limitations prevent a blanket parity claim. |
| Opus 5.5 prompting guide | Do not call it a new release. Primary documentation was read, but its publication/update time within the 24-hour window was not established. Discussion popularity is insufficient to date the document. |
| MicroLLM Lab | Exclude as fresh release. The project had already surfaced September 21; no distinct current release was verified. |
| AMD/World Labs | Publish once. AMD's September 28 release supplies the announced consideration and conditional closing, correcting the implication that terms could not be stated. |
| MongoDB/Meta | Publish once from both employers' announcements. Avoid interpreting a personnel move as proof of a broader talent-market price. |
| Research section marked quiet | Do not repeat the universal claim that no lab published research. The independently verified CASP report and Wolfram essay are covered in their appropriate categories; no new arXiv paper is fabricated to fill a quota. |
| NVIDIA safety platform | Publish once, combining OpenShell and Sentry. Distinguish the existing runtime from today's platform announcement. Omit unsupported universal-containment and participant-count claims. |
| HN satire | Retain as satire discussion; do not repeat fictional incidents or quotations as facts. |
| HN coding | Retain and merge with the architecture discussion. Author's essay is dated September 26, within the community window. |
| HN architecture | Merge with coding item. Identify competing professional arguments rather than declare a consensus or measured effect. |
| HN Newport | Retain as a September 28 opinion calling for scrutiny, not a newly opened official investigation. |
| HN serious AI product | Retain as a September 27 design proposal. Do not endorse universal claims about all products. |
| Reddit NVIDIA competitive-coding model | Hold as insufficiently established new development. Hugging Face's repository metadata says last updated September 17, contradicting an inferred overnight model release; direct thread metadata/content were insufficient to establish a substantive new event. |
| Reddit Qwen/Sonnet comparison | Omit from digest under the rule removing overlap with the Sonnet individual article. The retrieved post is a contributor's comparison and personal experience, not an independently controlled benchmark. |
| Reddit reward hacking | Retain current discussion of the September 18 Handshake audit. Correct its characterization as general daily-user observations; do not re-date the underlying research. |
| Reddit ImaJev | Retain creator discussion; verify metadata through the creator's Hugging Face repository. Benchmark rankings remain author claims, not independent reproduction. |
| Reddit functional gradient descent | Retain author acceptance discussion. Primary submission record is June 15, not September; a co-author's recent acceptance post supplies current context. |
| YouTube CNBC / GGzPtkYiYis | Hold. Direct retrieval throttled; current upload metadata/content not independently established. Topic also overlaps the platform article. |
| YouTube CNN / aaopxmz-fwU | Hold. Retrieval failed; no verified current upload and no reconstructed quotation. |
| YouTube CBS News / _DUqL7dbXg8 | Hold. Retrieval failed; no verified current upload/content. |
| YouTube CBS Mornings / 3534g3dA2bs | Hold. Retrieval failed; no verified current upload/content. |
| YouTube Higgsfield / UQDM-ZigvGo | Hold. Indexed publisher title/description establishes the video, but an exact eligible upload date was not independently verified. No view count is reproduced. |

The companion contains seven news entries and fifteen community/video entries; the separate “quiet” research claim is audited as an additional editorial assertion. Eight retained community inputs become seven digest items after merging the two coding discussions.

## Additional research and evidence

- **Heidi II:** September 28 primary launch post, plus region-specific rollout notice. Publish announced administrative scope and review conditions. Exclude untested clinical-benefit claims. The regional page's September 29 date is separate from the September 28 release date. Sources: https://www.heidihealth.com/blog/heidi-ii and https://www.heidihealth.com/en-za/blog/heidi-ii-is-here
- **Lenovo Googlebook:** September 28 primary release and footnotes. Publish announcement and future availability; distinguish laboratory battery claims from measured user experience and preserve internet/language/geography qualifications. Source: https://news.lenovo.com/pressroom/press-releases/first-googlebook-premium-ai-experiences-sleek-lightweight-design/
- **HCLSoftware/Robotiq.ai:** September 28 primary acquisition-intent release. Publish intended integration and expected November closing, not a completed acquisition. Omit price rather than infer it from inconsistent secondary descriptions. Source: https://www.hcltech.com/en-us/press-releases/hclsoftware-acquire-robotiqai-strengthening-enterprise-agentic-automation
- **OpenAI release decision:** Multiple current outlets report a withheld model and reproduce an attributed company statement. The explainer uses “reportedly,” attributes the account, and explicitly marks the original statement and test record as independently unretrieved. No internal failure rate, causal mechanism or global model comparison is invented. Secondary links appear only as “via” evidence for the attributed original statement, not as primary verification. Sources: https://www.cbsnews.com/news/openai-halts-gpt-astra-safety-concerns/ and https://www.reuters.com/business/openai-shelves-new-ai-model-after-internal-safety-tests-wsj-reports-2026-09-28/
- **AutoTrust JEV-27B:** Do not promote the September 28 syndicated release into a first launch. The creator's own announcement is dated September 27. No distinct technical advance in the current window was established. Primary earlier announcement: https://huggingface.co/blog/autotrust/autotrustjev-27b-fast-calibrated-decisions-and-ful
- **Anthropic prospectus reporting:** Identified current reporting, but no directly inspectable primary filing was retrieved in this review. Financial figures and risk interpretations are held rather than synthesized from secondary summaries.
- **UNCTAD access reporting:** The underlying independent investigation already appears in the September 28 digest. No separate newly verified incident is asserted from renewed coverage.

The seven additional topics recovered from Gemini beyond the five shared with today's companion are ElevenLabs, Shopify checkout, Lenfest, the NYC subpoena, CASP, Wolfram and Manus. Their corrections and sources are documented in the preserved supplemental review and each article's verification appendix.

## Verification limits

Several direct page opens failed. Where search returned the original publisher's indexed text, it was used as primary text, with company claims still attributed. Source dates were checked separately from crawler freshness. An indexed result's “today” crawl label alone was not treated as a publication date. Hugging Face's connected metadata tool supplied the NVIDIA and ImaJev repository dates; models were not downloaded or benchmarked.

Disconfirmation checks considered stale project announcements, preprint submission dates, rollout exclusions, product footnotes, future acquisition closings, missing evaluation details and differences between statements and measured outcomes. No new request for comment was sent and no response was invented. Proposed acceptance tests in the articles are editorial analysis, not claims that those tests were performed.

## Validation

All 17 new posts have parseable TOML front matter, `draft = false`, and publication timestamps set to current time minus one hour. All sixteen individual explainers have 600–800-word bodies, titles no longer than 60 characters, ledes below 35 words, a plain second paragraph, an early why-it-matters passage, a mid-article subheading, verification material, glossary candidates and cold-reader sentences of at most 30 words. The community digest has separate Hacker News, Reddit and YouTube sections and seven non-duplicate items.

The briefing's 32 NotebookLM URLs are unique and ordered by appearance. Local relative links are checked against the live repository tree plus new files. Only this run's 21 new files are selected; existing content and the companion report are preserved. The main branch is rechecked before the fast-forward update.
