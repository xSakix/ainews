# Editorial audit — 28 September 2026

Controlling specifications: `prompts/main-prompt.md`, `prompts/research-prompt.md` and `prompts/article-writer-prompt.md`, read from `main`. Inputs were fresh research and `reports/2026-09-28-ai-briefing-anthropic.md`. The companion was treated as a lead list, not independent verification.

News cutoff: 28 September 2026, 03:00:29 UTC; preceding 24 hours for sections 1–5 and YouTube, up to seven days for community discussions. Dates on current coverage did not reset underlying release dates.

## Published output

- Three individual explainers: NaiveAI's model, Tiny AI Arena's scoring change and the attributed corporate open-model report.
- One combined digest with nine retained community items: four Hacker News, four Reddit and one YouTube.
- Briefing with 19 unique source URLs, in item order.

## Companion reconciliation

| Lead | Decision and evidence |
| --- | --- |
| Open-weight corporate adoption | Retained as attributed reporting; underlying adoption scale and executive-mention count remain unverified. FT full text was access-restricted; PYMNTS supplied the secondary account. |
| Frontier token share and effective price | Excluded from the current-news bullet. Traced to Ramp's 9 September publication, which explicitly says open-model adoption was not driving its observed shift. Older counterevidence is labeled as background in the explainer. |
| OpenAI development pause | Duplicate of `openai-pauses-work-after-dns-sandbox-escape.md`; no new article. |
| Tiny AI Arena | Retained once under agents. Primary repository inspection found a concrete 27 September scoring change; article avoids treating gameplay as general intelligence measurement. |
| Authors Guild filings | Retained in digest as a current discussion of a 21 September claimant statement; allegations are not described as judicial findings. |
| Ember-1 | Retained in digest; primary publication is 23 September. The vendor's 40% token claim is attributed, not changed into an independently verified saving or today's launch. |
| Slop UI essay | Retained as design opinion. Primary indexed text supported the summary; direct page retrieval failed. |
| “There are no rogue AI agents” | Not repeated. Its operator-responsibility argument overlaps the 25 September digest's responsibility discussion, and underlying incidents have individual coverage. The essay supplied no separate new incident in this review. |
| UNCTAD investigation | Retained in digest. Original analysis dated 26 September concerns April–June traffic; investigator attribution and limitations are explicit. This is distinct from prior Hugging Face and Australian-portal stories. |
| Naive-N0.5-Flash | Promoted to individual coverage. Initial GitHub commit dated 27 September, 15:57 UTC; repository checks verified the publication and documented specifications. |
| Qwen/Jev competitor | Retained with correction: Alibaba Cloud documents `decision-model-preview`, with a 25 September update and a lifecycle listing for 24 September. “Rushed” and comparative superiority are not established. |
| Qwen Warcraft | Retained as a creator demonstration. Directly read post says no visual input; custom tools provide game state and actions. |
| Logit penalties | Retained as a limited user experiment, with the author's one-model/one-test caveat. |
| Machine-learning research priorities | Retained as discussion, not evidence that research fields are obsolete. |
| Jubilee/Andrew Yang | Retained from publisher-supplied episode metadata dated 27 September, 12:00 UTC, corroborated by current participant promotion. No full-video quotations or audience counts. |
| GreatScott video | Held: direct video retrieval failed; a mirror of a current promotional post was insufficient to verify upload metadata and project results. |
| CBS, Fox and Podcast Gold videos | Held: video pages failed or were throttled, and searches did not establish the required metadata/content. No claims copied solely from the companion. |

## Additional exclusions from fresh searches

- **MiniCPM5-2B:** the official repository changelog dates release to 7 September, despite 27 September secondary coverage. https://github.com/OpenBMB/MiniCPM/blob/main/README.md
- **Google video co-director:** the primary blog predates the strict window; a new secondary summary is not a new research release. https://research.google/blog/coherent-long-form-video-generation/
- **Previously covered OpenAI incidents, Meta Muse distribution and bilateral AI talks:** recent repository posts already cover the underlying developments.

## Verification limits

GitHub records were directly inspected through the connected account. Several public web pages failed direct retrieval; indexed primary text was used where available and explicitly identified where material. The Reddit posts were read through the current Reddit pages; output uses the required old.reddit.com links. Hacker News permalinks were preserved, but direct thread loading was unreliable, so no vote counts or unsupported commenter consensus is asserted.

No model performance or game history was independently rerun. Vendor benchmarks, researcher attribution, claimant allegations and user experiments retain their respective qualifications. Suggested evaluation protocols are editorial analysis.

The new business article uses Ramp's older primary analysis only as labeled explanatory counterevidence. It is excluded from the strict-window briefing URL list. Primary source: https://ramp.com/data/ai-index-sept-2026

## Checks

TOML front matter, `draft = false`, title length, explainer word counts, required verification/glossary/cold-reader sections, cold-reader sentence length, and ordered unique briefing URLs were checked before commit. Existing `main` filenames, recent reports and community digests were checked for overlapping events. Only the six new files from this run are included in the commit.
