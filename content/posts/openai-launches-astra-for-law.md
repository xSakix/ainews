+++
date = '2026-09-18T05:12:00+02:00'
draft = false
title = 'OpenAI Launches Astra for Law'
+++

After reading this, the reader knows OpenAI built a legal version of GPT-6 Astra, and professional review remains essential.

# OpenAI Launches Astra for Law

*The system combines a frontier model with a large US legal index, specialized instructions and controls for confidential work.*

OpenAI has introduced Astra for Law, a configuration of GPT-6 Astra intended for legal research, analysis and writing. It adds a search index covering more than 230 million URLs of US case law, statutes, regulations, court rules and administrative decisions.

The offering will first reach selected law firms through a Trusted Access program in ChatGPT and Codex. OpenAI says an API version called `gpt-6-astra-law` is coming soon. Legal technology companies Harvey and Legora are among the customers expected to build on it.

## Why it matters

General web search is a poor substitute for legal research. Lawyers must find controlling authority, distinguish binding rulings from persuasive material and trace an answer to exact passages. A dedicated index can narrow that retrieval problem and make the model's work easier to inspect.

OpenAI says its index incorporates CourtListener data from the nonprofit Free Law Project, whose collection covers more than 99.9% of published US precedential case law. It also says the corpus is updated daily. Coverage does not by itself guarantee that a model selects the right authority or applies it correctly, but it gives reviewers a clearer path back to sources.

In OpenAI's evaluation on 200 questions from a private validation set of Vals AI's Legal Research Bench, Astra for Law passed the overall correctness check on 54.0% of questions. GPT-6 Astra with web search scored 38.7% at the same highest reasoning setting. OpenAI also reports 24% more reference cases found on case-law questions and up to 54% more relevant passages retrieved from correct opinions.

These are vendor-run results on a private set. The improvement is meaningful if reproducible, but 54% correctness is not a level at which unreviewed legal advice would be acceptable. The benchmark also cannot represent every jurisdiction, procedural posture, changing rule or firm-specific standard.

## Building around firm knowledge

OpenAI presents Astra for Law as a foundation rather than a finished law practice. Firms can connect their own precedents, permissions and review processes. The launch includes 26 partner-built plugins for systems including iManage, Intapp, DeepJudge and Thomson Reuters products, plus nine community plugins and 47 adaptable skills.

Selected firms have already built workflow-specific applications. OpenAI says Sullivan & Cromwell created an agreement analyzer, Ropes & Gray built a diligence system and Cooley built a tool for preparing public-company filings. The important design choice is that lawyers define which sources, methods and controls belong in a workflow.

Confidentiality remains central. OpenAI says eligible firms receive zero data retention on the API and that ChatGPT Enterprise use is excluded from human review by default. The company is working with Latham & Watkins on information permissions, ethical walls, client instructions and firm oversight.

Those controls must be tested in practice. Legal organizations need clear access rules, matter separation, audit records and a process for correcting output before it reaches a client or court. A model's citation can be precise yet still support the wrong proposition, omit contrary authority or rely on law that has changed.

Astra for Law signals a shift from generic assistants to systems that combine a general model with a domain index, instructions and institutional controls. Its value will depend less on fluent drafting than on whether it improves source discovery while preserving professional judgment and accountability.

## Verification

- **Tier 1 — VERIFIED:** OpenAI announced Astra for Law on 17 September 2026, combining GPT-6 Astra with a legal search index and specialized instructions. Source: https://openai.com/index/astra-for-law/
- **Tier 1 — VERIFIED:** OpenAI describes more than 230 million indexed URLs, initial Trusted Access, future API availability and specific privacy controls. Same source.
- **Tier 1 — VENDOR-REPORTED:** The 54.0% correctness score, 38.7% baseline and retrieval improvements are OpenAI's evaluation results on a private validation set. Same source.
- **Tier 2 — ANALYSIS:** Discussion of liability, review and operational controls is editorial analysis.

## Glossary candidates

- **Precedential case law:** Court decisions that establish rules later courts may be required to follow.
- **Ethical wall:** Controls that prevent information from crossing between people or matters with conflicting duties.

Cold-reader sentence: Astra for Law improves legal retrieval by combining GPT-6 Astra with a specialized index, but lawyers must verify every material conclusion.
