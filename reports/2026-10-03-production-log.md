# Production log — 3 October 2026

## Revised production run

This run executes the revised main prompt and editorial profile at `267b0ee` (the six-articles rule). Claude supplied all seven research desks. None was missing, so no GPT research desk was run. The seven Anthropic reports and all their sections, including substantive coverage-note pointers, were read. No legacy single-file Anthropic report was present.

The earlier 44-article edition had already been moved by the repository owner into `backup/2026-10-03/`. That directory remains a historical snapshot outside Hugo’s published content. Four previously edited article pairs were reused after source and editorial review; two pairs were newly written. The current edition contains exactly six English articles, six Slovak twins, and one bilingual digest with 57 items. This replaces the previous deferred queue: every source-qualified, unselected topic in the current Claude inputs is in the digest, not held for tomorrow. Earlier GPT-only discoveries are outside this revised input set.

Duplicate checking used existing English posts’ titles/opening paragraphs and canonical source URLs. Backup files are not live posts. A mention in an earlier research briefing alone is not a published-post duplicate under the revised main prompt; this restores several video and HN pointers that the earlier run had incorrectly excluded on briefing-only history. No matching published-post source URL was found for the current retained topics. Related discussions are merged where they describe the same artifact.

Research dates remain tied to Claude’s original desk windows, rather than extending discovery during production. Source verification read the canonical pages, papers, repositories and HN/video page records captured earlier in this conversation, with further direct retrieval for the ReaLVR PDF, Reddit retries and Backburner code. Briefing prose was never used as verification evidence.

## Shortlist and six-article selection

Five focus areas are represented; research has two articles and every other area one. Percepta is treated as a lab technical-report release, not a weight release. Its concrete evidence concerns growing memory and retrieval. Cognitive research receives preference through ReaLVR’s internal visual evidence and Cambridge’s controlled learning comparison.

| Topic | Focus area | Format | Selection reason | Rank |
|---|---|---|---|---|
| Percepta tests growing memory for long-context recall | Major releases | EXPLAINER | A lab architecture report with controlled retrieval evidence and an inspectable mechanism; strongest release candidate. | 1 |
| ReaLVR trains hidden reasoning to retain visual evidence | Research: cognition | EXPLAINER | Directly probes hidden reasoning and evidence use; controlled image edits and intervention tests support the cognitive emphasis. | 2 |
| Cambridge finds objectives outweigh distillation data source | Research: cognition | EXPLAINER | Controlled negative result separates training-answer source, objective and learning rate; practitioner-relevant cognitive/learning finding. | 3 |
| Humanlike Chat adds tool use to a local texting model | Local models and agents | NEWS BRIEF | Local downloadable weights and adapter, two-teacher recipe, explicit tool/style/knowledge tradeoffs and migration detail. | 4 |
| Pi explains its switch to MCP tools in core | Essays | NEWS BRIEF | Substantive engineering argument about tool composition, deferred discovery and execution boundaries. | 5 |
| LDraw Nova lets agents build editable LEGO models | Other tier 1: builder project | NEWS BRIEF | Inspectable code and editable construction artifacts; distinct builder use case broadens the six-area mix. | 6 |
| Box²-Bench | Research / external guidance | EXPLAINER | Strong candidate; the two research slots favour visual reasoning and the controlled distillation result. Its findings are in the digest. | digest |
| DN-MOPD | Research / learning | EXPLAINER | Strong candidate; overlaps the distillation theme while the selected research pair offers more methodological variety. Included in digest. | digest |
| Engrams | Local models and agents | NEWS BRIEF | Inspectable artifact; Humanlike offers weights and training tradeoffs, while Pi already covers agent infrastructure design. Included in digest. | digest |
| Helion vLLM backend | Essays / engineering | NEWS BRIEF | Substantive technical report, but Pi’s context/tool-composition argument better complements the selected six. Included in digest. | digest |

## Digest selection

Every row below has an opened primary source and is published in the digest. Source scope controls the wording: research results are author-reported; essays and comments are attributed arguments; video descriptions support pointers, not reviews of full talks.

| Topic | Focus area or tier | Format | Reason | Rank |
|---|---|---|---|---|
| Reka publishes camera-motion weights | Releases | DIGEST ITEM | Primary page/description read; attributed viewpoint or bounded artifact summary. Source: https://huggingface.co/RekaAI/Reka-Inverse-Dynamics-Model | digest |
| Simple-WAM keeps a future representation without video | Research | DIGEST ITEM | Primary page/description read; attributed viewpoint or bounded artifact summary. Source: https://arxiv.org/abs/2609.34981 | digest |
| DN-MOPD balances competing teachers’ feedback | Research | DIGEST ITEM | Primary page/description read; attributed viewpoint or bounded artifact summary. Source: https://arxiv.org/abs/2609.35347 | digest |
| OmniTaskonomy maps visual-generation transfer | Research | DIGEST ITEM | Primary page/description read; attributed viewpoint or bounded artifact summary. Source: https://arxiv.org/abs/2609.38079 | digest |
| Box²-Bench tests when agents resist bad guidance | Research | DIGEST ITEM | Primary page/description read; attributed viewpoint or bounded artifact summary. Source: https://arxiv.org/abs/2609.39578 | digest |
| Small judges compress the scales they are given | Research | DIGEST ITEM | Primary page/description read; attributed viewpoint or bounded artifact summary. Source: https://arxiv.org/abs/2609.38827 | digest |
| LANTERN uses model activations to rank mathematical leads | Research | DIGEST ITEM | Primary page/description read; attributed viewpoint or bounded artifact summary. Source: https://arxiv.org/abs/2609.32264 | digest |
| Unmask the State finds selective adaptation opportunities | Research | DIGEST ITEM | Primary page/description read; attributed viewpoint or bounded artifact summary. Source: https://arxiv.org/abs/2609.33355 | digest |
| EngiWorld checks engineering artifacts against constraints | Research | DIGEST ITEM | Primary page/description read; attributed viewpoint or bounded artifact summary. Source: https://arxiv.org/abs/2609.37686 | digest |
| OSWorld-Science evaluates scientific software outcomes | Research | DIGEST ITEM | Primary page/description read; attributed viewpoint or bounded artifact summary. Source: https://arxiv.org/abs/2609.39903 | digest |
| TraceDance turns deployment failures into targeted tests | Research | DIGEST ITEM | Primary page/description read; attributed viewpoint or bounded artifact summary. Source: https://arxiv.org/abs/2609.33295 | digest |
| PROWBench checks videos against program-executed events | Research | DIGEST ITEM | Primary page/description read; attributed viewpoint or bounded artifact summary. Source: https://arxiv.org/abs/2610.02205 | digest |
| OpenAI connects instructions to completion checks | Prompting techniques | DIGEST ITEM | Primary page/description read; attributed viewpoint or bounded artifact summary. Source: https://openai.com/index/practical-guide-building-gpt-6/ | digest |
| Graphene makes analytics editable by coding agents | What people are building | DIGEST ITEM | Primary page/description read; attributed viewpoint or bounded artifact summary. Source: https://github.com/graphene-data/graphene | digest |
| Engrams separates production and development isolation | What people are building | DIGEST ITEM | Primary page/description read; attributed viewpoint or bounded artifact summary. Source: https://github.com/cortexapps/engrams | digest |
| Backburner supplies phone-attention code and tests | What people are building | DIGEST ITEM | Primary page/description read; attributed viewpoint or bounded artifact summary. Source: https://github.com/StayLameBro/backburner-llama.cpp/blob/master/ggml/src/ggml-metal/phone-attn.h | digest |
| Accuretta packages a local model with a working desktop | What people are building | DIGEST ITEM | Primary page/description read; attributed viewpoint or bounded artifact summary. Source: https://github.com/mkultraware/accuretta | digest |
| messy-docs-bench grades whole-document correctness | What people are building | DIGEST ITEM | Primary page/description read; attributed viewpoint or bounded artifact summary. Source: https://github.com/TashonBraganca/messy-docs-bench | digest |
| AutoSynthData turns agent failures into training tasks | What people are building | DIGEST ITEM | Primary page/description read; attributed viewpoint or bounded artifact summary. Source: https://huggingface.co/blog/ServiceNow-AI/autosynthdata | digest |
| turbopuffer loosens the vector index’s hold on storage | Worth reading | DIGEST ITEM | Primary page/description read; attributed viewpoint or bounded artifact summary. Source: https://turbopuffer.com/blog/rip-vector-database | digest |
| Helion combines autotuning with selective dispatch | Worth reading | DIGEST ITEM | Primary page/description read; attributed viewpoint or bounded artifact summary. Source: https://pytorch.org/blog/building-a-high-performance-and-portable-vllm-linear-backend-with-helion/ | digest |
| Mollick reconsiders the need to manage agent teams | Worth reading | DIGEST ITEM | Primary page/description read; attributed viewpoint or bounded artifact summary. Source: https://www.oneusefulthing.org/p/the-dot-and-the-swarm | digest |
| Sarah asks what a self-improvement ban would cover | Worth reading | DIGEST ITEM | Primary page/description read; attributed viewpoint or bounded artifact summary. Source: https://www.lesswrong.com/posts/ZT2rKu3Z6RaargYYF/what-is-recursive-self-improvement-and-what-would-it-mean-to | digest |
| Dayen connects agent misconduct to industry incentives | Worth reading | DIGEST ITEM | Primary page/description read; attributed viewpoint or bounded artifact summary. Source: https://prospect.org/2026/09/29/artificial-intelligence-agents-openai-microsoft-sam-altman-greg-brockman-ah-nice/ | digest |
| Perone asks who will protect overlooked public systems | Worth reading | DIGEST ITEM | Primary page/description read; attributed viewpoint or bounded artifact summary. Source: https://blog.christianperone.com/2026/09/the-systems-that-no-one-will-test/ | digest |
| A teaching assistant questions the loss of programming craft | Worth reading | DIGEST ITEM | Primary page/description read; attributed viewpoint or bounded artifact summary. Source: https://mondobe.com/ai-makes-me-sad | digest |
| Housman describes AI-assisted questions during infertility | Worth reading | DIGEST ITEM | Primary page/description read; attributed viewpoint or bounded artifact summary. Source: https://www.astralcodexten.com/p/our-ai-midwife | digest |
| Kernel maintainers distinguish reports from actionable fixes | Hacker News | DIGEST ITEM | Primary page/description read; attributed viewpoint or bounded artifact summary. Source: https://news.ycombinator.com/item?id=49929391 | digest |
| Stratego readers focus on training efficiency | Hacker News | DIGEST ITEM | Primary page/description read; attributed viewpoint or bounded artifact summary. Source: https://news.ycombinator.com/item?id=49933740 | digest |
| GLM coding logs prompt questions about cost estimates | Hacker News | DIGEST ITEM | Primary page/description read; attributed viewpoint or bounded artifact summary. Source: https://news.ycombinator.com/item?id=49934620 | digest |
| DwarfStar users share local-inference modifications | Hacker News | DIGEST ITEM | Primary page/description read; attributed viewpoint or bounded artifact summary. Source: https://news.ycombinator.com/item?id=49936575 | digest |
| A painting canvas sparks disagreement over capability | Hacker News | DIGEST ITEM | Primary page/description read; attributed viewpoint or bounded artifact summary. Source: https://news.ycombinator.com/item?id=49928566 | digest |
| Hosted-site discussions divide developers | Hacker News | DIGEST ITEM | Primary page/description read; attributed viewpoint or bounded artifact summary. Source: https://news.ycombinator.com/item?id=49927747 | digest |
| A SaaS harness prediction meets practitioner resistance | Hacker News | DIGEST ITEM | Primary page/description read; attributed viewpoint or bounded artifact summary. Source: https://news.ycombinator.com/item?id=49938616 | digest |
| WoW readers ask whether the agent finished its task | Hacker News | DIGEST ITEM | Primary page/description read; attributed viewpoint or bounded artifact summary. Source: https://news.ycombinator.com/item?id=49933251 | digest |
| YC Paper Club surveys alternatives to GPU computation | YouTube | DIGEST ITEM | Primary page/description read; attributed viewpoint or bounded artifact summary. Source: https://www.youtube.com/watch?v=xc2FTBGRSJo | digest |
| Tristan Buckmaster discusses AI-written mathematics | YouTube | DIGEST ITEM | Primary page/description read; attributed viewpoint or bounded artifact summary. Source: https://www.youtube.com/watch?v=PQYFRuZ5phs | digest |
| Elie Bakouch compares agents in an optimizer speedrun | YouTube | DIGEST ITEM | Primary page/description read; attributed viewpoint or bounded artifact summary. Source: https://www.youtube.com/watch?v=oVsEddfhdxc | digest |
| Lakshya Agrawal explains reflective prompt optimisation | YouTube | DIGEST ITEM | Primary page/description read; attributed viewpoint or bounded artifact summary. Source: https://www.youtube.com/watch?v=OA-Mc60Rboo | digest |
| Hugging Face shows an always-on Pi assistant | YouTube | DIGEST ITEM | Primary page/description read; attributed viewpoint or bounded artifact summary. Source: https://www.youtube.com/watch?v=HU03WDFB_tQ | digest |
| Eric Schmidt discusses AI on Ukraine’s battlefield | YouTube | DIGEST ITEM | Primary page/description read; attributed viewpoint or bounded artifact summary. Source: https://www.youtube.com/watch?v=KgJI4Wxqqik | digest |
| Markus Gabriel discusses AI’s promises and fears | YouTube | DIGEST ITEM | Primary page/description read; attributed viewpoint or bounded artifact summary. Source: https://www.youtube.com/watch?v=uPJO4URd0w8 | digest |
| Vienna discusses human dignity in AI development | YouTube | DIGEST ITEM | Primary page/description read; attributed viewpoint or bounded artifact summary. Source: https://www.youtube.com/watch?v=8Skv9rtR_Fk | digest |
| Tom Krcha describes agents building a design tool | YouTube | DIGEST ITEM | Primary page/description read; attributed viewpoint or bounded artifact summary. Source: https://www.youtube.com/watch?v=cNlAF3USuns | digest |
| Zixuan Li explains the case for frontier open weights | YouTube | DIGEST ITEM | Primary page/description read; attributed viewpoint or bounded artifact summary. Source: https://www.youtube.com/watch?v=9JFGohx4E7U | digest |
| Weco separates harness improvement from improving itself | YouTube | DIGEST ITEM | Primary page/description read; attributed viewpoint or bounded artifact summary. Source: https://www.youtube.com/watch?v=yB6_iFGTq9k | digest |
| Stanford opens its updated transformer course | YouTube | DIGEST ITEM | Primary page/description read; attributed viewpoint or bounded artifact summary. Source: https://www.youtube.com/watch?v=114i2Kz-LZA | digest |
| Garrison Lovely challenges inevitable labour replacement | YouTube | DIGEST ITEM | Primary page/description read; attributed viewpoint or bounded artifact summary. Source: https://www.youtube.com/watch?v=PiBNrW7Q_Ws | digest |
| DeepMind explains watermarks across media and biology | YouTube | DIGEST ITEM | Primary page/description read; attributed viewpoint or bounded artifact summary. Source: https://www.youtube.com/watch?v=HIUzrxQxTtw | digest |
| Deník N contrasts American and Chinese AI politics | YouTube | DIGEST ITEM | Primary page/description read; attributed viewpoint or bounded artifact summary. Source: https://www.youtube.com/watch?v=0DcYD-l7aRk | digest |
| Georgia responds to a ballot-privacy demonstration | Tier 2 | DIGEST ITEM | Primary page/description read; attributed viewpoint or bounded artifact summary. Source: https://www.theguardian.com/us-news/2026/oct/02/midterms-ai-ballot-privacy | digest |
| Apple plans clearer Full Disk Access consent | Tier 2 | DIGEST ITEM | Primary page/description read; attributed viewpoint or bounded artifact summary. Source: https://developer.apple.com/news/?id=p6zjojqw | digest |
| Nvidia prepares a smaller-memory DGX Spark | Tier 2 | DIGEST ITEM | Primary page/description read; attributed viewpoint or bounded artifact summary. Source: https://blogs.nvidia.com/blog/local-ai-dgx-spark-64gb-sync/ | digest |
| AWS changes selected reserved GPU rates on October 7 | Tier 2 | DIGEST ITEM | Primary page/description read; attributed viewpoint or bounded artifact summary. Source: https://aws.amazon.com/ec2/capacityblocks/pricing/ | digest |
| Amazon commits funds to data-centre communities | Tier 3 — business | DIGEST ITEM | Primary-source confirmed announcement; one sentence only. | digest |
| Anthropic funds an enterprise engineering academy | Tier 3 — business | DIGEST ITEM | Primary-source confirmed announcement; one sentence only. | digest |
| Bloomberg reports a possible Clayton appointment | Tier 3 — business | DIGEST ITEM | Primary-source confirmed announcement; one sentence only. | digest |

## Merges, exclusions and source access

| Topic | Disposition | Reason |
|---|---|---|
| Percepta companion capability-growth post and Reddit thread | Merge into selected Spotlight article | Same underlying architecture; no separate general capability-growth result claimed. |
| DGX Spark release and industry coverage | One In brief item | Same hardware event; official technical scope plus independent reported price. |
| Backburner builder item and Reddit thread | One builder digest item | Canonical phone-attention header and test program recovered; social-post speed figures omitted because thread content remained unavailable. |
| Humanlike Chat Reddit announcement | Merge into selected model article | Canonical model card, weights and licence govern the claims. |
| Oracle Wisconsin grid-delay report | Drop as stale | Canonical Aterio analysis dates to September 29; separate force-majeure filing to September 24. Neither is a new October 2 underlying event. |
| Opus/Godot regression thread | Drop: source unavailable | Direct page and RSS retries return a generic Welcome to Reddit/access page, despite HTTP 200; no actual post body. Earlier JSON/web attempts also failed. |
| Search-tool decision test | Drop: source unavailable | Same actual-content failure; the briefing’s measurements were not repeated as verified results. |
| Qwen heavily quantized comparison | Drop: source unavailable | Same actual-content failure; no unverifiable anecdotes carried into digest. |
| Three-week Qwen evaluation | Drop: source unavailable | Same actual-content failure; no uninspected throughput or task scores published. |
| Self-hosting cost essay thread | Drop: source unavailable | No readable thread or recovered canonical essay in this run. |
| Micro Center export-paperwork thread | Drop: source unavailable | Retail claims could not be read or independently confirmed. |
| Unitree UnifoLM-WLA-1.0 | Drop: stale release pointer | September 28 upload is outside the release desk’s 72-hour window. |
| Microsoft FrogNano | Drop: stale release pointer | Primary card’s September 22 release date is outside the release window. |
| IBM Granite ensemble notebook pointer | Drop: unfilled source gate | HF file listing has images and .gitattributes, with no readable model card/notebook/code supporting a substantive item. |

These are final exclusions or merges, not a deferred work queue. No desk is missing. Reddit is a source-access gap, not evidence of a quiet community day; no empty Reddit section appears in the digest.

## Primary-source corrections

- Percepta’s client-rendered page initially hid its body. The linked content asset exposed the complete technical report. The selected article reports controlled 140M–670M experiments and single-record recall, not demonstrated continual-learning capability in a frontier deployment.
- ReaLVR’s PDF identifies Xi Xiao with UAB and Amazon AGI and the co-authors with Amazon AGI. The five-task average is 63.7 versus 60.4 for LVR-RL and 62.9 for ILVR; the latter wins two individual tasks. The 235B experiment has only three benchmarks, so no five-task mean is invented. The fixed-context intervention supports local dependence, not a complete causal explanation.
- Humanlike Chat’s primary card explicitly lists Apache-2.0, correcting the briefing’s unconfirmed licence. Its base is the Huihui altered model, not official Qwen. The human-message score is a model judge’s selection rate, not human-user deception. Knowledge and coding losses remain alongside style and tool gains. Unchanged filenames require redownload to obtain 2.0.
- Backburner’s initial README alone was generic upstream llama.cpp. Reading its tree exposed `phone-attn.h` and `phone-kv-test.cpp`, which confirm phone-held cache pages, partial-attention merging and a continuation-comparison test. No 29–44% speed claim is published without the originating measurement.
- Graphene’s repository is inspectable, but an open-source licence is not asserted. Accuretta is source-available with a personal-use constraint.
- Engrams’ production Firecracker design and plain-subprocess development fallback have different isolation properties.
- Georgia’s new event is the October 1 response to an August study. Recovered ballot order is not equivalent to identifying every voter; the digest avoids the misleading 1.52M-identified-voters reading.
- AWS’s canonical pricing page confirms the October 7 change, per-accelerator rates, existing-purchase price lock and unchanged On-Demand/Savings Plans/other Capacity Block prices.
- Apple gives no release date or API contract for the future Full Disk Access control.
- Clayton is a reported anticipated appointment, not a completed appointment. As a personnel move without an enacted policy change it receives one Tier 3 sentence.
- The research abstract calls the programmable-world benchmark PROWBench, while the title metadata uses ROWBench; the digest follows the abstract’s method name.
- Video metadata corrects local-date ambiguity without inventing viewing: World Science Festival’s October2 US timestamp is October3 in Bratislava; the Pi tutorial’s timestamp is October2 in Bratislava. Complete transcripts are not available, so all fifteen are digest pointers with channels and languages.

## Editing and translation

The four reused article pairs were re-edited against the current prompts. Pi’s generic procurement advice was replaced with the documented execution boundary and transcript-state behaviour. ReaLVR and Humanlike Chat were newly drafted, edited and translated. The reporting gate is one finding per article; no glossary, gate sentence, H1 or duplicated dek is published.

English article bodies use the selected brief/explainer limits. The digest can be long under the revised prompt and contains 57 items in the required section order, with the whole-digest closing parts once. Selected article topics are absent from the digest. Business has three one-sentence items. Each item has a direct source and a verification entry; video channel/description metadata is separately marked VERIFIED from the speakers’ OPINION.

Slovak preserves paragraph/heading/table structure, source URLs and their occurrence counts, figures, tags and timestamps. Product and paper names remain unchanged where used as official names. No partial translations or English-only articles are published. Unique timestamps use the current Europe/Bratislava offset, rank 1 at current time minus 60 minutes and the digest earliest.

## Validation

- Strict validation: all 14 new English/Slovak post files passed `python3 scripts/check_posts.py --strict` with zero problems.
- Full live-post validation: all 239 files passed `python3 scripts/check_posts.py` with zero problems.
- Six article body lengths, excluding front matter and verification: Percepta 629; ReaLVR 648; Cambridge 659; Humanlike 315; Pi 271; LDraw Nova 335 words. Each meets its selected format limit.
- All seven translation pairs have matching paragraph-block, heading and table-row counts. Source URLs and occurrence counts, tags and timestamps match; numeric differences are limited to Slovak formatting and sentence order. Headline and slug limits pass.
- The digest has 57 items, including three one-sentence business items; six article topics are excluded from it. No deferred queue remains.
- Unique publication timestamps use the Europe/Bratislava offset for 3 October, with rank 1 latest and the digest earliest.
- `git diff --check` passes. Only the 14 posts and two production/editor reports are included in this edition.
- Hugo is not installed in the execution environment, so the optional local Hugo build was unavailable. Repository checks passed; deployment success is not asserted.
