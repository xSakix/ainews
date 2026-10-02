# Production Log — 2 October 2026

## Inputs

- Controlling specification: `prompts/main-prompt.md`
- Research specification: `prompts/research-prompt.md`
- Companion report: `reports/2026-10-02-ai-briefing-anthropic.md`
- Existing English post titles and opening paragraphs were checked before selection.

## Output

- New research briefing: 1
- English standalone articles: 6
- English daily digest: 1
- Slovak twins: 7
- Total new posts: 14
- Unique URLs in the research briefing NotebookLM list: 29

## Article selection

1. OpenAI warns more than 100 organizations — material update to prior incident coverage; independent reporting and investigation available.
2. SoftBank completes $30 billion OpenAI investment — transaction above the major-deal threshold; company filing and Reuters confirmation available.
3. California subpoenas OpenAI — new regulatory action; official state release and Reuters confirmation available.
4. Bull doubles French supercomputer output — on-site Reuters reporting with executive interviews and concrete capacity figures.
5. BearingPoint finds AI value stalls before scale — primary study material plus independent coverage; survey limitations disclosed.
6. Chatbots remove hijabs despite consent concerns — original Guardian testing with company responses and outside expert context.

## Digest selection

Cloudflare Clef, Pi 1.0/Pi Durable, Turbo Harness, three Hacker News discussions, three Reddit items and three videos were consolidated into one article. Vendor claims, community interpretation, pull-request status and speculation are labeled explicitly.

## Exclusions and corrections

- Broadcom/Anthropic $42 billion loan: retained in the briefing but not published as a post because the cited confidential prospectus was not available as a primary source.
- Congressional letters about Chinese access: retained in the briefing but not published because the underlying letters were not public.
- Synopsys/OpenAI chip-system story: excluded as an out-of-window continuation of a 30 September announcement.
- K2 Horizon: treated only as a newly scheduled AMA; the older model release was not presented as new.
- Gemini 4: retained only as explicitly unverified video speculation.
- OpenAI notices: distinguished from earlier repository articles by focusing on the new count above 100 and the independent Asymmetric investigation.

## Verification and language parity

- Every standalone article ends with a claim-level verification appendix.
- English labels use the permitted closed set; Slovak labels use the specified Slovak set.
- Each English post has one Slovak twin with matching date, tags, URLs, headings and verification-item order.
- Front matter uses TOML with double-quoted strings, unique ASCII slugs and 2–4 tags.
- Dates are ranked one minute apart; the digest has the earliest timestamp.
