# Desk: Research papers

Desk name for the header: `Research papers`
Output file: `reports/YYYY-MM-DD-briefing-papers.md`

## Scope

New research worth a deep dive: papers on arXiv and elsewhere, lab research posts, technical reports and datasets. Pick what a technical reader would want explained — a new method, a surprising result, a careful negative result, an interpretability or evaluation insight, a new dataset or benchmark that changes how something is measured. Skip incremental leaderboard gains and surveys with no new finding.

Any institution qualifies: universities, big labs, small labs, independent researchers, in any country.

## Window

The paper's first version (v1) was submitted within the past 7 days, and the paper appears in no earlier briefing or post.

Why 7 days and not 24 hours: arXiv announces papers in batches at 20:00 US Eastern time, Sunday to Thursday, and nothing on Friday or Saturday. A paper's v1 date is its submission time, usually 6 to 30 hours before it becomes public, and up to three days before on a weekend. Papers also gain attention over several days on Hugging Face Daily Papers, Hacker News and in lab posts. A 24-hour window therefore rejects almost every paper, and every paper on Saturday, Sunday and Monday mornings.

## Where to look

Check these directly; do not rely on web search to find new papers (see "Go to the sources" in `prompts/research-prompt.md`).

- arXiv listings: `https://arxiv.org/list/<category>/new` for today's batch and `https://arxiv.org/list/<category>/pastweek?show=2000` for the week, for cs.CL, cs.LG, cs.AI, cs.CV, cs.MA, cs.CR, cs.RO and stat.ML.
- arXiv API, sorted by submission date: `https://export.arxiv.org/api/query?search_query=cat:cs.CL&sortBy=submittedDate&sortOrder=descending&max_results=200` (change the category as needed).
- Hugging Face Daily Papers: `https://huggingface.co/papers`, or `https://huggingface.co/api/daily_papers?date=YYYY-MM-DD` for each day in the window. Community upvotes are a signal of interest, not of quality.
- alphaXiv (`https://www.alphaxiv.org/`) for papers with active discussion.
- Lab research pages: Anthropic, OpenAI, Google DeepMind, Meta FAIR, Microsoft Research, NVIDIA Research, Apple Machine Learning Research, Allen Institute for AI, and the GitHub or Hugging Face pages of Qwen, DeepSeek, Moonshot and other labs, whose technical reports often appear there first.
- Papers discussed on Hacker News and r/MachineLearning in the window.
- Conference proceedings (OpenReview, ACL Anthology, PMLR) only when a conference publishes in the window.

## Reading the date, and when arxiv.org does not load

- Open `https://arxiv.org/abs/<id>`. "Submitted on" next to [v1] is the date that counts.
- If arxiv.org does not load, use arXiv's own mirror `https://export.arxiv.org/abs/<id>`, or the API `https://export.arxiv.org/api/query?id_list=<id>`: its `<published>` element is v1's submission time, and it also lists the title, authors, abstract and categories. The PDF is at `https://arxiv.org/pdf/<id>`.
- These are arXiv's own servers, so they are primary sources. Always cite `https://arxiv.org/abs/<id>` in the briefing, whichever server you read.
- `https://huggingface.co/papers/<id>` and Semantic Scholar mirror the metadata; use them only as a pointer when all arXiv servers fail, and say so in the coverage note.

## What to report

Aim for 5–10 papers. For each item, the summary states the one finding in plain words and why it is interesting. Then add one line:
`Authors: [lead institution(s)] · First submitted: [v1 date] · Artefacts: [code / data / weights / none]`

Prefer papers with released code, data or weights: the reader can inspect them, and the writer can explain them.

## Sections

1. Papers worth a deep dive — ranked; these are the article candidates.
2. Also notable — one line each.
