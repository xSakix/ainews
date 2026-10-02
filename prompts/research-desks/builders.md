# Desk: What people are building

Desk name for the header: `What people are building`
Output file: `reports/YYYY-MM-DD-briefing-builders.md`

## Scope

Things individuals, researchers and small teams have built and shown: open-source projects, Show HN launches, notable GitHub repositories, Hugging Face Spaces, local-model setups, agents, developer tools, experiments and demos. The item must show the thing itself — code, a working demo, or a detailed write-up of how it was built.

Out of scope: launches by funded companies that are mainly marketing (waitlists, landing pages, "contact sales"), which belong to the releases or industry desk, and lab releases, which belong to the releases desk.

## Window

The project was launched, released or first shown within the past 7 days, and it appears in no earlier briefing or post. A new version of an older project qualifies when the release itself is in the window; say what changed.

## Where to look

- Show HN: `https://hn.algolia.com/api/v1/search_by_date?tags=show_hn&hitsPerPage=100`, or `https://news.ycombinator.com/show`.
- Hacker News front page: `https://hn.algolia.com/api/v1/search?tags=front_page`.
- GitHub trending: `https://github.com/trending?since=daily` and `?since=weekly`, also filtered by language (Python, TypeScript, Rust). If it does not load, use the GitHub search API for new repositories with many stars (`https://api.github.com/search/repositories?q=created:>YYYY-MM-DD+topic:llm&sort=stars`, also `topic:agents`, `topic:ai`), or projects linked from Hacker News and Reddit.
- Hugging Face trending Spaces: `https://huggingface.co/spaces?sort=trending`, or `https://huggingface.co/api/spaces?sort=trendingScore&limit=100`.
- r/LocalLLaMA and r/MachineLearning ([P] posts): `https://old.reddit.com/r/LocalLLaMA/top/?t=week`. If Reddit refuses the request, use the subreddit's RSS feed or a search for recent posts.
- Lobsters: `https://lobste.rs/t/ai`.

## What to report

For each item, the summary says what it does, who built it and what is interesting about how it is built (model used, architecture, stack, cost, a clever trick). Then add one line:
`Built by: [person or team] · Artefacts: [code (licence) / demo / write-up] · Signal: [stars, points or upvotes]`

Stars and points are a signal of attention, not of quality; never present them as proof that something works. Performance claims are the builder's own.

## Sections

1. Open-source projects and tools
2. Agents and automation
3. Local and on-device AI
4. Experiments, demos and write-ups
