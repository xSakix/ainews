# Editorial profile — what AI News Daily covers and how stories are ranked

AI News Daily is written first for its publisher: a technical reader with twenty years in AI who wants to know what was released, what was discovered, what people are building and what the community is arguing about. Search visibility is a welcome side effect, never a reason to select or rank a story.

The research desks use this profile to decide what to look for. Triage (`prompts/main-prompt.md`, Task B) uses it to rank. When this file and another prompt disagree about what to cover or how to rank it, this file wins.

## Interest tiers

### Tier 1 — the reason the site exists

1. **Releases from AI labs, major and minor, anywhere in the world.** New models and open weights, technical reports, model cards, notable version updates and API changes. Cover the United States, Europe, China and the rest of the world with equal care; a release from a small lab or a non-English lab counts as much as one from a household name if the work is interesting.
2. **New research worth a deep dive.** Papers (arXiv and elsewhere), lab research posts, technical reports and datasets with a finding that can be explained: a new method, a surprising result, a careful negative result, an interpretability or evaluation insight.
3. **What people are building.** Open-source projects, Show HN launches, notable GitHub repositories, Hugging Face Spaces, local-model setups, agents and tools built by individuals and small teams, with the code or a working demo available.
4. **Technical writing and essays.** Deep dives, engineering write-ups, post-mortems, benchmark investigations, and essays with a substantive argument about how AI works or is built.
5. **Community discussion.** Hacker News, Reddit and similar threads where practitioners share measurements, experience or informed disagreement.
6. **Talks and discussions on video.** Lectures, conference talks, long interviews and debates — on AI engineering and building with AI, and on what AI means for society, politics, the economy, science and philosophy. In English, German, Czech and Slovak.

### Tier 2 — keep the reader in the loop

- Developer tools, agent frameworks, inference engines and infrastructure software.
- Hardware, when the story carries technical detail (specifications, benchmarks, availability), not only orders and revenue.
- Safety and security incidents, vulnerabilities and red-team results, especially with technical detail.
- Policy and regulation that changes what can be built, released or used (open-weight rules, the EU AI Act, export controls, court rulings on training data).

### Tier 3 — business, kept to a minimum

Funding rounds, valuations, investments, IPOs and filings, acquisitions and mergers, partnerships and enterprise deals, earnings and revenue figures, executive moves, stock moves, consulting surveys and market reports, data-centre spending.

Tier 3 never becomes an article. It may appear as a one-line item in the digest's "Business, briefly" section, at most five items a day, and only when it involves a lab, model or tool the site covers.

**Exception:** a business event moves up to tier 1 or 2 when it directly changes what the reader can use or study — an open model relicensed or withdrawn, an open-source project shut down or forked after an acquisition, a lab closing, an API discontinued or repriced. Write it about that consequence, not about the money.

## Ranking

Rank topics in this order:

1. **Tier.** Every tier 1 topic ranks above every tier 2 topic.
2. **Substance.** Within a tier, prefer the topic with more to explain and more that can be inspected: released weights, code, a paper or technical report, data, a reproducible measurement. A release with a technical report outranks a release with only a blog post.
3. **Novelty and consequence.** Then prefer what is genuinely new and what changes what practitioners can do.

Keep the mix varied: when material exists, the day's articles should include at least one lab release, one research paper and one community-built project. No single lab or category should take every slot.

The 🚨 marker in briefings flags magnitude, not interest. It does not decide rank.

## Volume

There is no fixed article limit. Write every tier 1 and tier 2 topic that has enough substance and sourcing for an article; the rest go to the digest. Volume follows what happened: a quiet day produces a short edition, a busy day a long one. If a run cannot finish everything, publish in rank order and log what was cut and why.
