# Translation maps

One file per edition: `<lang>.yaml` (`sk` exists; `nl`, `fr`, `de`, `es` and `zh` have none yet). A translator prompt loads its own language's map and no other; an edition without a map is translated exactly as before.

| File | Read by |
|---|---|
| `sk.yaml` | `prompts/translator-prompt.md` (Slovak: the production run, `prompts/main-prompt.md` Pass 2, and Claude's own Slovak twin, `prompts/article-run.md` step 7) |

## Sections (the same in every language)

| Section | Binds the translator as | Entry fields |
|---|---|---|
| `terms` | binding if `confirmed`, advisory if `needs_review` | `en`, `target`, `avoid`, `note`, `status`, `evidence` |
| `keep_in_english` | binding if `confirmed`, advisory if `needs_review` | `term`, `note`, `status`, `evidence` |
| `idioms` | binding for the listed phrases | `en`, `target`, `avoid`, `note`, `status`, `evidence` |
| `patterns` | guidance | `id`, `en`, `target`, `before`, `after`, `note`, `status`, `evidence` |
| `style` | guidance | lists of rules under `headlines`, `numbers`, `currency`, `dates`, `names`, `register` |

`status` is `confirmed` or `needs_review`. A `confirmed` entry binds the translator. A `needs_review` entry is advisory: the translator prefers it but may use an established alternative, until a native editor confirms it or removes it. `evidence` lists audit finding IDs (for Slovak: `docs/sk-translation-audit/report.md`) and may be empty only when the note says that the entry rests on usage.

`en` is always the English source term and `target` the rendering in the map's language, so every language's map has the same shape. Keep the section and field names unchanged.

## Changing a map

`scripts/check_posts.py` enforces a small part of the Slovak map on its own: the list `SK_AVOID` holds the `avoid` forms that are wrong in every sense, and a Slovak twin that contains one fails the strict check. When a `confirmed` entry with such an unambiguous `avoid` form is added to `sk.yaml`, add its pattern there too. Forms that are correct in another sense („politika“, „zisk“, „stopa“) stay out of the script and with the translator.

Only a person edits a map. A translator run that meets a term the map lacks logs it as `Term not in map: …` (see the prompt), and a person adds it here.
