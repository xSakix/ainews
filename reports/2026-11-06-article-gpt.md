# Article by GPT — 6 November 2026
Topic: The Intrusion Pathway: how irrelevant prompt context enters a model's computation and lowers accuracy
Primary sources: https://arxiv.org/abs/2611.07778 ; https://github.com/dk4248/the-intrusion-pathway
Why this story: The preprint gives a mechanistic, reproducible account of a common failure in retrieval and long-context systems. It distinguishes the heads that import irrelevant material from those that integrate evidence, turning a vague context-quality problem into a testable circuit.
Status: published: content/posts/why-irrelevant-context-changes-a-models-answer.md


## Notes
Opened the arXiv record, the complete public reproduction guide, its model and dataset list, and its experiment map. Followed the public TransformerLens, relations and GSM-IC repositories that the work uses. The opening and closing engineering scenes are explicitly illustrative. No quotation beyond the paper's named “intrusion pathway” is used.

The article keeps the preprint status, the scale limits, the oracle nature of the 97.6% recovery, and the cost of head masking. The public repository substantiates the listed models, 250-fact dataset, downstream tasks, scripts and sensitivity sweeps.

Readability edit: complete; meaning and sources checked.

The local validation runtime was unavailable. The file was checked manually for valid TOML delimiters and double-quoted fields, allowed tags, date and draft fields, a slug under 60 characters, narrative structure, references, absence of bold and pipeline notes, and consistent Markdown.
