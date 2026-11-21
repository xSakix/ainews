# Production log — 21 November 2026

## Research
All eight Anthropic desk briefings were present and the research status was complete. No fallback desk was needed. Desk entries had already been screened with `scripts/seen.py`; the plan merges repeated events across desks. The connected GitHub session does not expose a local checkout, so the repository scripts could not be executed again in this run; deduplication and structural validation were performed from the current files on `main`.

## Top-story selection

| Slot | Candidate | Substance | Consequence | Tension | Novelty | Fit | Total | Lens |
|---|---|---:|---:|---:|---:|---:|---:|---|
| Economy and work | Korean workers save 3.7 hours but output barely moves | 2 | 2 | 2 | 1 | 2 | 9 | Consequence |
| Economy and work | AI-linked market correction | 2 | 2 | 2 | 1 | 2 | 9 | Consequence |
| Releases | Inkling 2 Mini | 2 | 1 | 1 | 2 | 1 | 7 | Capability |
| What people are building | OpenComputer | 2 | 1 | 2 | 1 | 1 | 7 | Practice |
| Worth reading | Signal protects chats from OS-level AI assistants | 1 | 2 | 2 | 1 | 1 | 7 | Consequence |
| Next | Fed minutes on AI debt and inflation | 2 | 2 | 1 | 1 | 2 | 8 | Consequence |
| Next | Anthropic compute commitments | 2 | 2 | 1 | 1 | 2 | 8 | Consequence |
| Next | Agents rewrite their own weights | 2 | 1 | 1 | 2 | 1 | 7 | Capability |

Tension 2 — Korea: self-reported time saving in the 2026 Bank of Korea survey against the near-zero time-saved/output relationship in the bank's earlier study, both reported at https://www.koreatimes.co.kr/economy/20261117/korean-workers-embrace-ai-but-productivity-gains-remain-elusive-bok

Tension 2 — market correction: Anthropic's record IPO and AI investment optimism against the same week's fall into correction, both reported at https://www.cnbc.com/2026/11/20/sp-500-correction-market-sell-off.html

Tension 2 — OpenComputer: the project's speed and cost claims at https://github.com/diggerhq/opencomputer against objections from Cognition staff in the linked Hacker News discussion https://news.ycombinator.com/item?id=50581403

Tension 2 — Signal: OS assistants' access to screen content against Signal's end-to-end privacy guarantees, described at https://signal.org/blog/protecting-your-privacy/ and in OS integration documentation linked from that post.

No major provider released a new model or major model version today, so Releases receives one top-story slot.

The day fills five slots. The optional sixth place remains empty because the research-paper candidates cannot move up and the next eligible candidates did not outrank the selected cross-section.


## Digest
Published content/posts/ai-daily-digest-for-21-november-2026.md with five top stories and all distinct planned topics. Primary-source context for the top stories came from the Thinking Machines, Signal, OpenComputer, Korea Times and CNBC pages recorded in the completed desk briefings. Vendor benchmarks remain attributed; the GRH claims remain explicitly unverified.

## Translation notes
- Claude's article already had its Slovak twin on main.
- Skipped content/posts/ai-daily-digest-for-21-november-2026.sk.md after two validation attempts could not be completed: the connected GitHub environment did not provide a local checkout, so scripts/check_posts.py could not verify the required heading, paragraph, URL and terminology parity for this unusually long digest. No partial translation was published.
- Skipped content/posts/a-language-model-rewrote-its-own-weights-and-improved.sk.md for the same strict-validation limitation. No partial translation was published.

## LinkedIn
Not written because today's Slovak digest is not on main. Follow prompts/linkedin-run.md after the Slovak digest passes strict validation.

## Resumed Slovak and LinkedIn publication — 21 November 2026

User explicitly requested a retry of the skipped Pass 2 and Pass 3. The original skip records above describe the earlier attempt, not the final state.

### Translation notes
- Published `content/posts/ai-daily-digest-for-21-november-2026.sk.md`: connector-level comparison shows 9 headings, 120 paragraph blocks and 100 URL occurrences matching the English digest. Source URLs occur in the same multiplicities; the date and tags were copied unchanged.
- Published `content/posts/a-language-model-rewrote-its-own-weights-and-improved.sk.md`: connector-level comparison shows 5 headings, 32 paragraph blocks and 2 source URLs matching the English article. The date, tags and references were preserved.
- Claude's article and Slovak twin were already on `main`, so neither was rewritten.
- Both new Slovak files were reviewed against the confirmed Slovak translation-map forms, including Git merge terminology, agent plurals, model checkpoint, held-out evaluation and recorded reasoning traces. A targeted banned-form scan returned no matching terms.
- A Git checkout remains unavailable in this environment (GitHub host DNS resolution failed), so the local `scripts/check_posts.py --strict` checks could not be run. The parity figures above are from direct comparisons of the complete files fetched through the GitHub connector, not a claimed Python strict-check success.

### LinkedIn edition — retry
- Published `content/linkedin/2026-11-21.sk.md`: **Kórejskí pracovníci šetria s AI čas, no výkon nerastie**.
- All five top stories appear in the digest's order, with the exact source URLs for their corresponding story. The section summary contains eight bullets, one per eligible remaining digest section, with their section anchors.
- Checked title and description lengths (54 and 150 characters), share text length (551 characters), body length (569 words), story paragraph word counts, bullet length, source URL membership, and section coverage using the current GitHub files. The repository's `scripts/check_linkedin.py --strict` was not executed due to the unavailable checkout.
