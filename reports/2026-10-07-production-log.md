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

## Placebo test finds most agent skills add no value

EXPLAINER. Inspected the preregistration, result table, amendments and stated limitations in the public repository. The matched-control design is the spine. The article separates the 450-trial Claude study from the small Codex pilot and avoids generalizing beyond the tested tasks, model and harness. Strict check passed.

## Manifold finds malware judgments use moral routing

NEWS BRIEF. Read Manifold's full method, routing distances, workspace-lens contrast, route transplant and pruning results. The article treats the route transplant as the strongest evidence and preserves the distinction between a consulted path and the location of a decision. Results remain VENDOR-REPORTED company research. Strict check passed.

## Digest

Matched each planned item to its desk entry by direct URL, removed all six article topics and merged repeated release or community discussion. Vendor, preprint and forum claims remain attributed; videos name their language and are limited to their official descriptions. Business coverage stays in the final section. Strict check passed.

Translation notes: google-releases-embeddinggemma-2.sk.md — paragraph, heading, URL, figure, date, tag and verification-row fidelity reviewed; required heading IDs preserved. Strict twin check passed.

Translation notes: mistral-previews-large-4-before-releasing-weights.sk.md — paragraph, heading, URL, figure, date, tag and verification-row fidelity reviewed; conflicting parameter figures preserved; required heading IDs preserved. Strict twin check passed.

Translation notes: vision-models-split-objects-from-relations.sk.md — paragraph, heading, URL, figure, date, tag and verification-row fidelity reviewed; required heading IDs preserved. Strict twin check passed.

Translation notes: opentpu-runs-local-models-on-a-300-dollar-fpga.sk.md — paragraph, heading, URL, figure, unit, date, tag and verification-row fidelity reviewed; required heading IDs preserved. Strict twin check passed.

Translation notes: placebo-test-finds-most-agent-skills-add-no-value.sk.md — paragraph, heading, URL, figure, date, tag and verification-row fidelity reviewed; matched-control distinctions and required heading IDs preserved. Strict twin check passed.
