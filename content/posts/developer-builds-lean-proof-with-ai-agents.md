+++
date = '2026-09-19T04:00:00+02:00'
draft = false
title = 'Developer Builds a Lean Proof With AI Agents'
+++

After reading this, the reader knows how Dan Abramov used AI and Lean to produce a proof that still needs mathematical review.

# Developer Builds a Lean Proof With AI Agents

*A month-long experiment produced a machine-checked certificate for Conway's refinement conjecture after repeated hallucinations, dead ends and workflow resets.*

Software developer Dan Abramov has published a detailed account of using ChatGPT, Claude and the Lean proof assistant to construct a proposed proof of Conway's refinement conjecture. He says the final statement compiles in Lean and passed mechanical registry checks.

In plain terms, the computer has verified that the submitted proof follows from its encoded assumptions under Lean's rules. Mathematicians have not yet independently confirmed that the formal statement captures the intended conjecture or that the surrounding interpretation is correct.

## Why it matters

AI mathematics announcements often compress the work into a result: a model solved a problem. Abramov's account exposes the process. Models produced plausible but false arguments, invented terminology, certified work that later failed and expanded unfinished ideas into large documents. Progress came from repeatedly deleting weak work and moving formal verification closer to each new claim.

The conjecture concerns omnific integers, part of John Conway's surreal-number system. It asks whether two equal products can be refined into four factors that recombine to produce both original factorizations. Abramov began without expertise in the area and selected the problem through a conversation with Claude.

Early attempts asked models to attack the problem directly. Abramov says the output often sounded sophisticated without providing reliable mathematics. Later he created multiple agent roles: mathematical explorers, a skeptical reviewer, a coordinator and a Lean formalizer. That workflow generated many notes but initially let unverified claims accumulate faster than formal checking.

## Verification had to follow the ideas closely

The project improved after Abramov separated established prerequisites from experimental results and required standalone Lean statements to import only the community Mathlib library. A second file linked each statement to its proof, while audits checked for extra axioms and prohibited dependencies.

He also contacted mathematicians about errors the agents believed they had found in published work. Some were real; others were misunderstandings. That feedback helped distinguish useful model criticism from confident noise.

The decisive workflow kept mathematical agents slightly ahead while Lean closed the gap within hours. When formalization fell far behind, the project accumulated conditional statements and private terminology that looked like progress but could not support the target theorem.

Abramov reports that the final target now compiles as a standalone proof certificate. He published an interactive dependency map and invited review. He also states clearly that mathematicians have not independently verified the proof, so the appropriate description is a proposed Lean-checked proof rather than a settled mathematical result.

Lean reduces one class of uncertainty: it checks whether a formal term satisfies a formal statement without using unproved assumptions outside the accepted base. It does not decide whether the chosen statement is the historically intended conjecture, whether definitions match the literature or whether the proof communicates useful understanding.

The experiment offers a practical lesson for AI-assisted research. Independent model votes did not create trust when the sessions shared mistaken premises. Reliable progress required small claims, formal checks, separated workspaces, visible dependency structure and human feedback from the field.

The next evidence should come from specialists reviewing the formal statement, dependencies and mathematical significance. If they confirm it, the contribution will include both the proof and an unusually candid record of how much verification work separated a plausible draft from a checkable artifact.

## Verification

- **Tier 1 — AUTHOR-REPORTED:** Abramov says the project produced a Lean-checked standalone proof certificate for Conway's refinement conjecture after roughly one month. Primary source: https://overreacted.io/how-i-vibed-a-proof-of-conways-conjecture/
- **Tier 1 — AUTHOR-REPORTED:** The account documents multi-agent roles, failed proofs, invented terminology, separated formalization tracks and mechanical audits. Same primary source.
- **Tier 1 — PARTIALLY VERIFIED:** Abramov links public Lean code and registry checks, but says mathematicians have not independently verified the proof. Same primary source and linked artifacts.
- **Tier 2 — ANALYSIS:** Distinctions between formal checking, interpretation and workflow lessons are editorial analysis.

## Glossary candidates

- **Lean:** A proof assistant that checks formal mathematical statements and proofs.
- **Proof certificate:** A machine-checkable object showing that a formal statement follows from accepted definitions and assumptions.

Cold-reader sentence: Dan Abramov produced a Lean-checked proposed proof with AI agents, but independent mathematicians still need to validate its statement and significance.
