# Editorial profile — what AI News Daily covers and how stories are ranked

AI News Daily is written for two readers. The first is its publisher: a technical reader with twenty years in AI who wants to know what was released, what was discovered, what people are building and what the community is arguing about. The second is the reader of the Slovak LinkedIn newsletter "Svet AI tvorený AI": a professional who follows AI for work (a developer, a manager, an analyst) and wants to know what AI is doing to their work, their tools, their industry and their bills. Both distrust hype and both want evidence. Search visibility is a welcome side effect, never a reason to select or rank a story.

The research desks use this profile to decide what to look for. The production run (`prompts/main-prompt.md`, Task B) uses it to plan the digest, and both writers use it to choose their article (`prompts/article-run.md`). When this file and another prompt disagree about what to cover or how to rank it, this file wins.

Why the profile reads this way: `reports/2026-10-15-linkedin-theme-analysis.md`. The newsletter's best-performing stories were about consequence (markets, prices, jobs, skills, access to frontier models, robots in factories), each with one tension and one number that lands, while the digest's top stories were almost all papers and releases.

## Three lenses

Every topic is seen through one main lens. The lenses keep the day's selection balanced.

- **Capability**: what AI can now do and how it works. Releases, research, evaluations, interpretability.
- **Practice**: how people build and use it. Local models, agents, projects, tools, prompting and context techniques, engineering write-ups.
- **Consequence**: what it changes for people, companies and societies. Economy and work, pricing, who gets access to frontier capability, safety incidents, policy, deployment in the physical economy.

## Interest tiers

### Tier 1 — the reason the site exists

1. **Releases from AI labs, major and minor, anywhere in the world.** *(Capability)* New models and open weights, technical reports, model cards, notable version updates and API changes. Cover the United States, Europe, China and the rest of the world with equal care; a release from a small lab or a non-English lab counts as much as one from a household name if the work is interesting.
2. **New research worth a deep dive, especially on the cognitive side.** *(Capability)* Papers (arXiv and elsewhere), lab research posts, technical reports and datasets with a finding that can be explained. Most wanted: how models reason, plan, remember, learn and represent knowledge; metacognition, self-knowledge and calibration; theory of mind and cognitive biases in models; comparisons with human cognition and neuroscience; interpretability of what happens inside a model while it thinks. Also welcome: a new method, a surprising result, a careful negative result, an evaluation insight.
3. **AI economy and work.** *(Consequence)* What AI does to jobs, skills and professions, above all the software profession; how teams and companies reorganise around agents; what AI tools cost and how their pricing changes; which industries and companies gain or lose because of an AI capability (a market move with a stated cause, a product category displaced); the scale and limits of AI infrastructure spending; AI deployed in the physical economy (robots in factories, autonomous logistics) with numbers on what works. It needs evidence: a study or official statistic with its method, a price sheet or billing change, a filing or earnings line about AI, a company's own account of how it works, a measured deployment. Opinion pieces count only when they carry such evidence.
4. **Frontier capability and who gets it.** *(Consequence)* A frontier model's system card, safety incidents during its testing, restricted or staged access, and the argument over who it is built for. The release itself is Capability; this item is about what the release changes and for whom.
5. **Local models and agents, and what people are building.** *(Practice)* Running models on your own hardware (inference engines, quantisation, small and on-device models, local agent setups), plus open-source projects, Show HN launches, notable repositories and agents built by individuals and small teams, with the code or a working demo available.
6. **New prompting and context techniques.** *(Practice)* New ways to instruct models and agents: prompt patterns, context engineering, agent instructions and skills, prompting guides from labs that change practice, and papers on prompting — with enough detail to try them.
7. **Technical writing and essays.** *(Practice, or the lens of their subject)* Deep dives, engineering write-ups, post-mortems, benchmark investigations, and essays with a substantive argument about how AI works, is built, is used or changes work.
8. **Community discussion.** Hacker News, Reddit and similar threads where practitioners share measurements, experience or informed disagreement — including about their jobs, their bills and their teams.
9. **Talks and discussions on video.** Lectures, conference talks, long interviews and debates — on AI engineering and building with AI, and on what AI means for society, politics, the economy, science and philosophy. In English, German, Czech and Slovak.

### Tier 2 — keep the reader in the loop

- Developer tools, agent frameworks, inference engines and infrastructure software. *(Practice)*
- Hardware, when the story carries technical detail (specifications, benchmarks, availability), not only orders and revenue. *(Capability)*
- Safety and security incidents, vulnerabilities and red-team results, especially with technical detail. *(Consequence)*
- Policy and regulation that changes what can be built, released or used (open-weight rules, the EU AI Act, export controls, court rulings on training data). *(Consequence)*

### Tier 3 — business, kept to a minimum

Funding rounds, valuations, investments, IPOs and filings, acquisitions and mergers, partnerships and enterprise deals, executive moves, consulting surveys without a published method, and revenue figures that say nothing about how AI is used.

Tier 3 never becomes an article or a top story. It may appear as a one-line item in the digest's "Business, briefly" section, at most five items a day, and only when it involves a lab, model or tool the site covers.

**Moving up.** A business event leaves tier 3 when it carries a consequence the reader can feel, and is then written about that consequence, not about the money:

- it changes what the reader can use or study (an open model relicensed or withdrawn, an open-source project shut down or forked after an acquisition, a lab closing, an API discontinued) — tier 1 or 2 by subject;
- it changes what AI costs, how people work or which companies and jobs are affected (a tool repriced, a market move attributed to an AI release, layoffs or hiring explicitly tied to AI, infrastructure spending at a scale that changes the market, an AI-native company's growth with its own figures and what it sells) — tier 1, item 3.

A revenue or valuation number stays a claim of whoever states it, and a market move needs a source that names its cause.

## The digest — the main product

Each day has **one digest** and **two articles**. The digest is the main product: everything that passed triage and has a primary source goes into it, and it can be long. Nothing is held back for a later day. Merge duplicates; keep each item short and specific.

### Choosing the top stories

The digest opens with three to five top stories. Choose them by score, then balance.

**1. Gate.** A candidate needs a primary source with specifics (substance at least 1, below). Tier 3 never qualifies.

**2. Score** each candidate from 0 to 2 on five criteria:

| Criterion | 2 | 1 | 0 |
|---|---|---|---|
| **Substance** — what the reader can inspect | weights, code, a paper, data, a filing, a price sheet, an official statistic, a reproducible measurement | a primary statement with concrete figures or terms | claims without detail |
| **Consequence** — whose work, money or options change | many readers' work, tools, bills, jobs or companies | one group of practitioners | a curiosity |
| **Tension** — a gap the facts show | promise against measured reality, capability against access, one group's gain against another's loss, a result that overturns an accepted belief | a clear contrast with the state before | none |
| **Novelty** | first of its kind, or overturns a prior result | a notable step | incremental |
| **Fit** — the two core interests | cognitive-side research, or economy and work (tier 1, items 2 and 3) | any other tier 1 | tier 2 |

Tension must be in the sources, never added by the writer: a vendor's claim against an independent measurement, a study's finding against the common assumption, a price before and after. A story with no such gap scores 0 here and is no worse for it.

**3. Rank** by total (0 to 10). Break ties by substance, then consequence.

**4. Balance**, adjusting the ranking only as far as needed:

- the top stories span at least two of the three lenses;
- when a Consequence topic scores 6 or more, at least one Consequence topic is a top story;
- no lens holds more than three top stories;
- tier 2 topics become top stories only when no tier 1 topic within one point of them is left.

**5. Lead.** The first top story is the highest-scoring one after balancing. When two are within one point, lead with the one whose consequence reaches more readers: the lead becomes the title of the Slovak LinkedIn edition.

The 🚨 marker in briefings flags magnitude, not interest. It does not decide what becomes a top story.

The production run writes each top story's scores, total and lens to the production log, so the publisher can see why a story was chosen and adjust this profile.

## The two articles

Two articles sit on top of the digest, one written by Claude and one by GPT (`prompts/article-run.md`). Each tells one story of the day in full, as a narrative dispatch with a reference list (`prompts/article-writer-prompt.md`). The article is there to give the reader what the digest cannot: the people behind the work, the background, the reasoning, and why it matters beyond the day. A story earns an article when it has:

- **Substance to explain**: a finding, a method, an argument, a working system or a documented change in how people work or what they pay, with a primary source deep enough to write 900 to 1,500 words from without padding, and sources behind it to draw background from;
- **A human element**: the people who made it and why, or the people it affects, real or pictured in an illustrative scene;
- **Significance beyond the day**: it changes how the reader understands, builds, uses or earns a living with AI;
- **A tension** the sources show (the same criterion as for the top stories), which gives the narrative its line.

**The lenses split between the writers.** Claude's article prefers a Consequence story; GPT's prefers a Capability or Practice story. Each writer falls back to the other lenses when no story in its own lens qualifies, and the two writers never choose the same story.

**A Consequence article may tell an arc.** Economy and work stories rarely happen in one day. Today's event is the hook; the article may draw on the events of the past 60 days on the same thread (earlier posts in `content/posts/` and their primary sources) to show where it is going, with every earlier event dated and sourced.

Research on how models think, a substantial essay, a release with a technical report, a project with a builder's story, a labour study with its data, a repricing that changes what a profession pays, and a frontier release told through what it changes make good articles. A vendor announcement with nothing to inspect, a funding round or a thread with no new evidence does not. A day without a story worth a full article has fewer articles; never write one to fill the slot.
