# Production log — 20 November 2026

All eight Claude research desks completed. No fallback research was required.

## Selection scores

| Candidate | Substance | Consequence | Tension | Novelty | Fit | Total | Lens |
|---|---:|---:|---:|---:|---:|---:|---|
| Fable 5 natural experiment | 2 | 2 | 2 | 1 | 2 | 9 | Consequence |
| Introspective oversight | 2 | 1 | 1 | 2 | 2 | 8 | Capability |
| Resolution Hypothesis | 2 | 1 | 1 | 2 | 2 | 8 | Practice |
| Prime Intellect model substitution | 2 | 2 | 1 | 2 | 1 | 8 | Consequence |
| VLM planning circuit | 2 | 1 | 1 | 2 | 2 | 8 | Capability |
| Chinese automakers scale back humanoids | 1 | 2 | 2 | 1 | 2 | 8 | Consequence |
| Natural-language activation readouts | 2 | 1 | 1 | 1 | 2 | 7 | Capability |
| Directly set MNIST weights | 2 | 1 | 1 | 2 | 1 | 7 | Practice |

## Tension 2 sources

- Fable 5: an 11-point SWE-Bench Pro advantage reported in the paper versus no measurable change in merged pull requests in its natural experiment: https://arxiv.org/abs/2611.23216 ; https://www.anthropic.com/news/fable-mythos-access
- Chinese humanoids: 2025 production-line announcements versus 2026 removals for cost and reliability, reported together by Caixin: https://www.caixinglobal.com/2026-11-13/in-depth-chinas-automakers-scale-back-humanoid-robot-ambitions-as-reality-bites-102504614.html

Balance moved the VLM planning circuit above the humanoid item so the five leads span Capability, Practice and Consequence without giving one lens more than two positions. Claude's claimed Fable story remains in the digest as required.

## Deduplication and verification

- Ran `scripts/seen.py` on 148 source URLs and `scripts/seen.py --titles 14`.
- Dropped the already published Claude black-hole research item. Kept the OpenAI changelog because gpt-live-1.1 and standby mode are material developments after earlier uses of the same rolling URL.
- Merged duplicate Muse, local-voice, safeguards, IPO and outage items across desks; dropped weak, purely speculative and headline-only items.

## Digest

- Published `content/posts/ai-daily-digest-for-20-november-2026.md` with five top stories and every item in the fixed plan.
- Opened the primary sources for the Fable 5 natural experiment, introspective oversight, the Resolution Hypothesis, Prime Intellect's model-substitution advisory and the Qwen3-VL planning circuit.
- Vendor, builder, community and single-author measurements remain attributed; the unavailable independent verification is stated where it changes the claim.

## Slovak editions

- content/posts/a-model-learned-to-report-what-its-assistant-did.sk.md: ok: 5 headings, 20 paragraphs, 4 list items and 4 source URLs match a-model-learned-to-report-what-its-assistant-did.md
- Term not in map: activation oracle → veštec založený na aktiváciách (a-model-learned-to-report-what-its-assistant-did)
- content/posts/ai-daily-digest-for-20-november-2026.sk.md: ok: 10 headings, 140 paragraphs and 65 source URLs match ai-daily-digest-for-20-november-2026.md
- Term not in map: activation oracle → veštec založený na aktiváciách (ai-daily-digest-for-20-november-2026)

## LinkedIn edition

content/linkedin/2026-11-20.sk.md: Silnejší programátorský model nezvýšil počet zlúčení. Všetkých päť hlavných správ v poradí digestu a päť ďalších položiek.

## Slovak translation-map revision — 20 November 2026

- Revisited today's Slovak digest and both article twins using `prompts/translation-maps/sk.yaml` (version 5), particularly its confirmed Git/GitHub vocabulary and the prohibition on literal verb translations. The observer article required no targeted changes.
- Corrected Git-specific `merge` / `merged` / `merge rate` throughout the Slovak digest and the Fable 5 article: `mergovať`, `mergnutý`, `miera mergovania` rather than `zlúčiť`, `zlúčenie`. Existing English source files were left unchanged.
- Rewrote the already-published LinkedIn edition to use terminology consistent with the revised Slovak digest; retained its metadata, source URLs and five-story order.
- Independent connector-based comparison: all three Slovak posts retain their English counterparts' heading counts, paragraph-block counts and source URLs. The repository's strict Python check scripts were not run because a Git checkout could not be accessed in this runtime (GitHub DNS resolution failure); this is not a strict-check pass.

## Retrospective editorial reselection — 20 November 2026

The publisher explicitly requested regeneration of this date under the revised `prompts/editorial-profile.md` and `prompts/linkedin-edition-prompt.md`. This supersedes the original top-story ranking above, without altering the English or Slovak narrative articles. It preserves all 65 digest source URLs and stories, moving four previous research leads to `Research` and the Prime Intellect incident to `In brief`.

### Revised slots and comparative scores

| Slot | Candidate | Substance | Consequence | Tension | Novelty | Fit | Total | Lens |
|---|---|---:|---:|---:|---:|---:|---:|---|
| Economy and work, lead | Indeed's diverging senior/entry-level hiring | 1 | 2 | 1 | 2 | 2 | 8 | Consequence |
| Economy and work | Chinese automakers' abandoned humanoid trials | 1 | 2 | 1 | 1 | 2 | 7 | Consequence |
| Releases | Microsoft MAI Code 2 and Flash | 2 | 1 | 1 | 2 | 1 | 7 | Capability |
| What people are building | Weight-Space Playground | 2 | 1 | 1 | 2 | 1 | 7 | Practice |
| Worth reading | Julián Posada on expert AI gig workers | 1 | 2 | 1 | 1 | 2 | 7 | Consequence |
| Releases | Microsoft MAI Realtime 1 | 1 | 1 | 0 | 1 | 1 | 4 | Capability |
| Next candidate | Starbright browser speech model | 2 | 1 | 0 | 1 | 1 | 5 | Practice |
| Next candidate | Nadella's eleven-developer software factory | 1 | 1 | 1 | 1 | 1 | 5 | Consequence |
| Next candidate | Prime Intellect model substitution | 1 | 1 | 1 | 1 | 1 | 5 | Consequence |

Microsoft, a major provider, announced new models on this date; the revised profile therefore calls for two release slots. All four mandatory section categories are represented, with two economy-and-work leads. No research paper occupies a top slot. No candidate received Tension 2 because a separately verifiable pair of source URLs had not been established for the comparison.

### Republished files and checks

- Rebuilt `content/posts/ai-daily-digest-for-20-november-2026.md` and its Slovak twin with six top stories, no duplicate source item, unchanged timestamps and all 65 original source URLs. The new selection preserves the previous reporting, moving items rather than silently dropping them.
- Rewrote `content/linkedin/2026-11-20.sk.md` from the revised Slovak digest (explicit user-requested rewrite). It now has six lead-story blocks and eight linked summaries, one for each eligible remaining digest section.
- Connector-level comparisons confirmed matching counts of sections, paragraphs, story headlines and source URLs across the English and Slovak digests. LinkedIn text was checked for story and section coverage, URLs, headline lengths, description length, share-post length, story-paragraph lengths and bullet lengths.
- The repository's Python strict checks (`scripts/check_posts.py`, `scripts/check_linkedin.py`) were not executed, so this is not a strict-check pass; source pages were not independently refetched for this retrospective selection. The published originals and their citations were reused.
