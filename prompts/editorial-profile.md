# Editorial profile — what AI News Daily covers and how stories are ranked

AI News Daily is written first for its publisher: a technical reader with twenty years in AI who wants to know what was released, what was discovered, what people are building and what the community is arguing about. Search visibility is a welcome side effect, never a reason to select or rank a story.

The research desks use this profile to decide what to look for. Triage (`prompts/main-prompt.md`, Task B) uses it to rank. When this file and another prompt disagree about what to cover or how to rank it, this file wins.

## Interest tiers

### Tier 1 — the reason the site exists

1. **Releases from AI labs, major and minor, anywhere in the world.** New models and open weights, technical reports, model cards, notable version updates and API changes. Cover the United States, Europe, China and the rest of the world with equal care; a release from a small lab or a non-English lab counts as much as one from a household name if the work is interesting.
2. **New research worth a deep dive, especially on the cognitive side.** Papers (arXiv and elsewhere), lab research posts, technical reports and datasets with a finding that can be explained. Most wanted: how models reason, plan, remember, learn and represent knowledge; metacognition, self-knowledge and calibration; theory of mind and cognitive biases in models; comparisons with human cognition and neuroscience; interpretability of what happens inside a model while it thinks. Also welcome: a new method, a surprising result, a careful negative result, an evaluation insight.
3. **Local models and agents, and what people are building.** Running models on your own hardware (inference engines, quantisation, small and on-device models, local agent setups), plus open-source projects, Show HN launches, notable repositories and agents built by individuals and small teams, with the code or a working demo available.
4. **New prompting and context techniques.** New ways to instruct models and agents: prompt patterns, context engineering, agent instructions and skills, prompting guides from labs that change practice, and papers on prompting — with enough detail to try them.
5. **Technical writing and essays.** Deep dives, engineering write-ups, post-mortems, benchmark investigations, and essays with a substantive argument about how AI works or is built.
6. **Community discussion.** Hacker News, Reddit and similar threads where practitioners share measurements, experience or informed disagreement.
7. **Talks and discussions on video.** Lectures, conference talks, long interviews and debates — on AI engineering and building with AI, and on what AI means for society, politics, the economy, science and philosophy. In English, German, Czech and Slovak.

### Tier 2 — keep the reader in the loop

- Developer tools, agent frameworks, inference engines and infrastructure software.
- Hardware, when the story carries technical detail (specifications, benchmarks, availability), not only orders and revenue.
- Safety and security incidents, vulnerabilities and red-team results, especially with technical detail.
- Policy and regulation that changes what can be built, released or used (open-weight rules, the EU AI Act, export controls, court rulings on training data).

### Tier 3 — business, kept to a minimum

Funding rounds, valuations, investments, IPOs and filings, acquisitions and mergers, partnerships and enterprise deals, earnings and revenue figures, executive moves, stock moves, consulting surveys and market reports, data-centre spending.

Tier 3 never becomes an article. It may appear as a one-line item in the digest's "Business, briefly" section, at most five items a day, and only when it involves a lab, model or tool the site covers.

**Exception:** a business event moves up to tier 1 or 2 when it directly changes what the reader can use or study — an open model relicensed or withdrawn, an open-source project shut down or forked after an acquisition, a lab closing, an API discontinued or repriced. Write it about that consequence, not about the money.

## The six articles

Each day has **six articles** and **one digest**. The articles are the best six topics of the day from these focus areas:

1. **Major releases** — a significant new model, open weights or technical report from any lab, in any region.
2. **Research, especially the cognitive side** — see tier 1, item 2. A cognitive-side paper beats an otherwise equal paper on another subject.
3. **Essays** — a substantive argument or deep dive about how AI works, is built or is used.
4. **Local models and agents** — running models and agents on your own hardware.
5. **Prompting and context techniques** — a new technique the reader could try.
6. **Other tier 1 topics** — a project people built, a talk with a transcript, a community measurement.

How to choose:

- Take at most two articles from one focus area, and cover at least four areas when the day's material allows.
- Within an area, prefer substance: released weights, code, a paper, data, a reproducible measurement — something the reader can inspect. Then novelty, then consequence for practitioners.
- Write six only if six topics pass the writer's gate. Never pad with a weak topic; five strong articles beat six with a filler.
- Tier 2 topics become articles only when no focus-area topic of similar substance is left. Tier 3 never does.

The 🚨 marker in briefings flags magnitude, not interest. It does not decide what becomes an article.

## The digest

Everything else that has a primary source goes into the day's single digest, which can be long. Nothing that passed triage is held back for later: a topic that missed the six articles is a digest item today. Merge duplicates, and keep each item short.
