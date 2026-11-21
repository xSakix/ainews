# Plan: acting on the November 2026 UX review

The review's diagnosis holds: the content is strong and the packaging is a
default PaperMod blog. This plan maps each recommendation to the files that
change, says what was verified against a local build (Hugo 0.148.2, the CI
version) and orders the work so the cheapest, most visible fixes ship first.

## What the build confirmed

| Review claim | Found in the build | Where it comes from |
|---|---|---|
| Logo announced as "logo AI News Daily" | `<img alt aria-label=logo>` on every page | `themes/PaperMod/layouts/partials/header.html:63,66` |
| `<li>\|</li>` inside the language list | Yes | same file, line 103 |
| No active-language state | The current edition is not in the list at all; the list holds the other six | `site.Home.Translations` excludes the current one |
| Header links go to edition home pages even when the post has a translation | Yes; the post's own translations sit in the post meta line | header uses `site.Home.Translations` |
| Generic `Next »` | `Next » AI Daily Digest for 21 November 2026` | theme `post_nav_links.html` |
| `cnbc.com, cnbc.com, cnbc.com` | Yes: the render hook turns bare URLs into the bare host | `layouts/_default/_markup/render-link.html` |
| Digest never links the day's own articles | Yes: the digest is written before GPT's article exists, and the prompts never ask for it | `prompts/digest-writer-prompt.md`, `prompts/main-prompt.md` |
| Search index is a "future" problem | **Already a problem**: `/index.json` is 3.5 MB (1.16 MB gzipped) for 406 English posts; `/sk/index.json` is 2.5 MB. The service worker also caches it for offline use. | `outputs.home` includes `JSON`; `static/sw.js:53` |
| "Invented people" line where no people appear | The fixed line is in 8 English articles (and their translations); 21 Nov's has no human in its scene | `prompts/article-writer-prompt.md:34` |
| Model byline missing | No `writer` field; but `reports/YYYY-MM-DD-article-{claude,gpt}.md` record the author of every article since 12 Oct (79 files) | `prompts/article-run.md` |

Not verifiable from the repo: Cloudflare's build command (needed for Pagefind).

## Decisions (21 November 2026)

1. **No public error-report channel.** A GitHub issue form was tried and removed: a public form linked from every page invites spam, exposes reporters, and becomes a prompt-injection path the moment an AI run reads issues. The About pages now say only that corrections are made in the article itself.
2. **Source labels improve through the prompt** (item 11, option b).
3. **Invented opening scenes stay** (item 10 goes ahead as written).
4. **The label stays "AI-generated".** Context is added next to it, never in its place; "primary-source checked" appears only where the pipeline guarantees it.
5. **The Substack is retired.** Done: removed from the social icons of all seven editions, the follow box, the About pages and schema.org `sameAs` (now the GitHub repo). Without it there is no email subscription, so the homepage call to action (item 3) is RSS and "Install the app" until an email channel exists.

## Phase 1: templates and copy (no pipeline change, applies to the whole archive)

Every new string goes through `i18n/*.yaml` so all seven editions get it.

### 1. Digest jump bar (review #1)
- Override `layouts/partials/toc.html` (or add a partial called from an overridden `single.html`): for digests (`File.ContentBaseName` starts with `ai-daily-digest-for-`), render the H2s (`Top stories · Releases · Research · Economy and work · What people are building · Worth reading · Hacker News · YouTube · In brief`) as a horizontal, scrollable chip bar that sticks under the header on scroll. Use the anchor IDs Hugo generates; no JS needed (`position: sticky`).
- Add an item count per section (count of `<strong>` leads under each H2, computed from `.Fragments` and content) so readers see "Research (14)".
- Articles keep no TOC; they are 6–7 minutes.
- CSS in `assets/css/extended/custom.css`; 44 px touch height.

### 2. Homepage as "Today's issue" (review #2, first half)
- `layouts/_default/list.html` already pins the newest digest. Extend it: collect the posts whose date (Europe/Bratislava day) equals the digest's day and that are not digests; render a "Today's issue" block with the digest as the lead card and the day's articles as two cards side by side (stacked on phones), each with its byline from item 9.
- Below it, group the rest of the feed under day headings (`Thursday 20 November`), digest first in each day. Pagination stays at 12 entries; a day split across pages repeats its heading.
- Same ordering for `/archives/`: override the theme's `archives.html` to sort each day digest first, then articles.

### 3. Hero copy and subscribe CTA (review #3)
- `hugo.toml` `homeInfoParams.Content` per edition. Proposed English:
  > Source-checked AI news for technical readers, every morning. Clarity, not persuasion.
  >
  > **[Follow by RSS](/index.xml)** · [Install the app](/install/) · [How we work](/about/) · [Archive](/archives/)
- The category list moves to the About page (it is already in the `description` meta). The Claude/GPT promise moves to the "Today's issue" block, where the bylines now fulfil it.
- Style the follow link as a button in `custom.css`. Translate for the six other editions.

### 4. Header and language switcher (review #6)
- Copy `themes/PaperMod/layouts/partials/header.html` to `layouts/partials/header.html` and:
  - drop `aria-label="logo"` (keep `alt=""`);
  - remove the `<li>|</li>`; draw the separator with a CSS border;
  - replace the six links with a `<details>` dropdown: summary `EN ▾`, list of native names, current edition included with `aria-current="page"`;
  - on a post page, link each edition to the post's translation when it exists; editions without one link to their home page and say so ("Deutsch — not yet translated"), via i18n.
- Re-run `scripts/test_pwa_browser.cjs` (it walks every edition) after the change.

### 5. End-of-article navigation (review: CRO)
- Override `post_nav_links.html` for posts in `mainSections`: on an article, "Today's digest" and "Today's other article"; on a digest, the day's two articles. Fall back to the theme's chronological links only for days without an issue (older posts).

### 6. Digest links to its own articles (review #2, second half)
- In `render-link.html`: when the page is a digest, build (once per page, with `partialCached` keyed on the date) a map of source URL → same-day article, from the URLs in each article's `## References`. When a digest link's destination is in the map, append ` · <a href=…>Read our full story</a>` after the link (once per item).
- Retroactive for every digest, no prompt change, and it survives the digest being written before the GPT article exists, because the site is rebuilt on every push.
- Translations: the map is built per language from the article's twin, so the Slovak digest links the Slovak article when it exists and the English one otherwise.

### 7. Report an error (review: CRO) — dropped
- Not implemented; see decision 1. Revisit only with a private channel (e.g. a corrections mailbox) that no pipeline run reads unattended.

### 8. About page: verification note (review: CRO)
- Rewrite `content/about*.md` "Verification labels": say what replaced the table on 12 October (source links inline on every item, quoted vendor/preprint qualifiers in the text) and keep the label definitions for the archived articles. Seven files.

## Phase 2: front matter and pipeline

### 9. Model byline and a better disclosure line (review #4, Trust)
- New front matter field `writer = "claude" | "gpt"` on articles (not digests).
- `prompts/article-run.md`: each writer sets its key. Translators copy it unchanged (add to the "keep" list in the seven translator prompts); `scripts/check_posts.py`: allowed values, and equality with the English twin, like `tags` and `date`.
- Backfill script: read `Status: published: content/posts/<slug>.md` from `reports/*-article-{claude,gpt}.md` and add the field to `<slug>.md` and every `<slug>.<lang>.md`. Articles before 12 October stay without a byline.
- Render in an overridden `post_meta.html` and on homepage cards: `AI-generated · Written by Claude · How we work` (link to `/about/#ai-disclosure`). Keep `params.author = "AI-generated"` for `<meta>` and schema.org.

### 10. The illustration line (review #4)
- Replace the fixed sentence in the body with a front matter flag `illustrativeScenes = true`, rendered by the template as a small note under the perex from i18n. One wording per language, owned by the template, not the model.
- Two variants: `people` ("…the people in them are invented") and `setting` ("The scenes that open and close this article are illustrations."), so a scene without people does not mention them.
- Update `prompts/article-writer-prompt.md` §"Invent a scene", the seven translator prompts (drop the fixed-line rule) and `check_posts.py` (reject the old sentence in new posts; require the flag when it is absent and the notes say "invented").
- Migrate the 8 English articles and their translations with a script.

### 11. Source labels (review #5, decision 2: prompt change)
- `prompts/digest-writer-prompt.md`: replace "bare URLs" with descriptive Markdown links, `Sources: [CNBC: S&P 500 correction](url), [CNBC: Nvidia's losing streak](url)`. Text is `Publisher: subject` in a few words; papers use `arXiv 2611.21885`, repositories `owner/repo`, discussions `HN discussion`. Same in `prompts/main-prompt.md` where it restates the rule.
- Seven translator prompts: translate the subject, keep the publisher name and the URL unchanged.
- `scripts/check_posts.py`: keeps comparing URLs between twins; in `--strict` mode, flag a new digest whose source link text equals the bare URL or the bare host.
- `layouts/_default/_markup/render-link.html` needs no change: it only shortens links whose text is the URL itself, so old digests keep their host labels and new ones show the written text.
- `prompts/linkedin-edition-prompt.md` and `scripts/check_linkedin.py`: check they do not assume bare URLs in the Slovak digest.

### 12. Headline consistency (review: IA)
- `prompts/article-writer-prompt.md` title rule: sentence case, names the actor and the claim, no metaphor-only titles.
- `check_posts.py --strict`: warn when more than half the words after the first are capitalised (excluding known proper nouns is not needed for a warning).
- Optional backfill of Title Case titles in older posts; URLs come from file names, so retitling does not break links.

## Phase 3: search and browsing

### 13. Pagefind (review #8)
- Run `npx -y pagefind@<pinned> --site public` after `hugo` in the Cloudflare build command (a dashboard change) and in `.github/workflows/check-site.yml`. Pagefind indexes each `<html lang>` separately, so the seven editions keep separate results.
- Override `layouts/_default/search.html` to load Pagefind UI; mark article bodies with `data-pagefind-body`, and record `format` (digest/article) and `writer` as Pagefind filters.
- Remove `JSON` from `outputs.home` and the `index.json` branch in `static/sw.js`; offline search goes away, or the service worker caches Pagefind's chunks on demand. Update `scripts/test_sw.cjs` and `test_pwa_browser.cjs`.
- Effect: the search page fetches a few kB of index chunks per query instead of 1.16 MB up front.

### 14. Digest vs. article facet (review: IA)
- No front matter needed: digests are recognised by file name. Add `/digests/` and `/articles/` pages (content files with a layout that filters `site.RegularPages`), linked from the Archive page and the menu.
- On tag pages, add two filter chips ("Digests", "Articles") that toggle a `data-format` attribute on each entry with a few lines of JS; without JS, all entries show.

## Order of work and size

| Step | Items | Size | Depends on |
|---|---|---|---|
| A | 4 (header a11y), 1 (jump bar), 3 (hero + CTA) | about a day, mostly i18n | none |
| B | 2 (today's issue), 5 (end nav), 6 (digest → article links) | 1–2 days | none |
| C | 9 (byline + backfill), 8 | 1 day | none |
| D | 10, 11, 12 | 1–2 days | none |
| E | 13 (Pagefind), 14 | 1–2 days | Cloudflare build access |

Each step ends with `hugo --minify --panicOnWarning`, `scripts/check_posts.py`, `scripts/check_pwa.py`, `scripts/test_pwa_browser.cjs`, and a phone-width (375 px) screenshot of the home page, a digest and an article in English and one translated edition.
