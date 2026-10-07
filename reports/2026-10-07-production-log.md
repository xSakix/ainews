# Production log — 7 October 2026

All seven Claude desk briefings are present and report completed coverage, so no research desk was repeated. Deduplication compared titles, source URLs and openings with existing English posts; no selected event has an earlier article. Repeated release, community and essay coverage was merged by underlying event.

The plan selects six stories across five focus areas. EmbeddingGemma 2 and Mistral Large 4 are the two strongest lab releases, though the Mistral article must centre on the live preview because its weights are still promised rather than released. The VLM paper supplies the cognitive-research slot, OpenTPU is an inspectable local hardware stack, skill-placebo is the day's clearest context-instruction measurement, and Manifold's routing study provides a substantive technical deep dive. Performance claims from labs, repositories and the Manifold study remain attributed to their publishers.

The release announcements and inspectable artefacts support NEWS BRIEFs. The VLM and skill-placebo studies need EXPLAINERS because their methods and limitations decide the meaning of the results. The Manifold article reports the author's argument and measurements as a NEWS BRIEF. Business items remain confined to the digest.

Publishing proceeds one file at a time, with strict validation and an atomic fast-forward commit to `main` after each completed file.

## Google releases EmbeddingGemma 2 for multimodal search

NEWS BRIEF. Opened Google's announcement and checked the released weight repository. The article centres on the modular shared embedding space, separates availability from Google's benchmark and RAM measurements, and keeps those measurements VENDOR-REPORTED. Strict check passed.

## Mistral previews Large 4 before releasing its weights

NEWS BRIEF. Opened Mistral's announcement and model documentation. The two sources disagree on total and active parameter counts, so the article reports both rather than resolving them by assumption. The live API and 27 October weight date are VERIFIED; performance remains VENDOR-REPORTED. Strict check passed.

## Vision models split objects from abstract relations

EXPLAINER. Read the arXiv record and the study's reported behavioral, representational and ablation findings. The causal spine is the transfer from heads found on the relational task to ARC-AGI-1. The human-development comparison is bounded as analogy, and all experimental results remain VENDOR-REPORTED preprint findings. Strict check passed.

## OpenTPU runs local models on a $300 FPGA card

NEWS BRIEF. Inspected the repository README, measurement tables, method notes, architecture map and licence. The article treats the published stack as the news and narrows the “developed by AI” framing. Every throughput and bandwidth result remains VENDOR-REPORTED pending independent hardware reproduction. Strict check passed.
