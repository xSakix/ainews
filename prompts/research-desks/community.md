# Desk: Community

Desk name for the header: `Community`
Output file: `reports/YYYY-MM-DD-briefing-community.md`

## Scope

What practitioners are discussing: threads on Hacker News and Reddit where people share measurements, hands-on experience, rebuttals or informed disagreement. Skip memes, drama and pure hype. YouTube has its own desk (`prompts/research-desks/youtube.md`).

Overlap with other desks is fine: a Show HN thread can appear here for its discussion and on the builders desk for the project. Triage merges duplicates.

## Window

Threads from the past 7 days with active discussion in the past 24 hours.

## Where to look

- Hacker News front page: `https://hn.algolia.com/api/v1/search?tags=front_page`; recent AI stories by points: `https://hn.algolia.com/api/v1/search?query=AI&tags=story&numericFilters=created_at_i>UNIX_TIME`.
- Reddit: r/LocalLLaMA and r/MachineLearning (`https://old.reddit.com/r/LocalLLaMA/top/?t=day`, `?t=week`). Other subreddits (r/StableDiffusion, r/ClaudeAI, r/OpenAI and similar) only for a thread with real technical substance. If Reddit refuses the request, use the subreddit's RSS feed or a search for recent posts.

## What to report

For each item, the summary says what the discussion is about and what it adds: a measurement, an experience report, a correction, a strong counter-argument. Then add one line:
`Signal: [points and comments, or upvotes]`

Community claims are the posters' own; label speculation and unverified claims as such.

## Sections

1. Hacker News
2. Reddit
