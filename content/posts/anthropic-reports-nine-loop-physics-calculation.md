+++
date = '2026-09-27T10:01:27+02:00'
draft = false
title = 'Anthropic Reports a Nine-Loop Physics Calculation'
+++

# Anthropic Reports a Nine-Loop Physics Calculation

*An AI-assisted calculation extends a specialized scattering result. The evidence supports progress in computational execution, with clear limits on claims of scientific invention.*

Anthropic, the developer of Claude, reported on September 25 that its Fable 5.1 model completed a nine-loop scattering calculation using established physics methods and a research computing environment.

Researchers used an AI system to carry out difficult mathematical work. The reported result extends a known calculation, and the released files let specialists inspect parts of the evidence. It does not establish that the model invented new physical laws.

**Why it matters:** Research assistance can be valuable without replacing the conceptual work of scientists. If a model reliably implements an existing method at a scale researchers have not previously completed, it may help turn a theoretical plan into a usable result. Reliability and reproducibility remain essential to that judgment.

The calculation concerns six-particle scattering in a highly symmetrical mathematical theory called planar N=4 super-Yang-Mills. A scattering amplitude is a mathematical quantity used to describe possible interactions. This particular theory is a simplified research setting, so the result should not be presented as a direct simulation of ordinary materials or an experimental discovery.

The word “loop” identifies an order in the calculation's successive corrections. Moving from eight to nine loops extends the calculation; it does not mean solving nine separate experiments. A 2023 paper by physicists Lance Dixon and Yu-Ting Liu provides the relevant eight-loop predecessor.

That earlier paper used a relationship between amplitudes and related mathematical objects to obtain its result. It matters as a baseline because the new work builds within an existing line of research. A claim of improvement should specify this problem and predecessor, rather than suggesting a general record across all physics.

The announcement describes about a week of work using known approaches. The useful question is which parts of that workflow could be repeated by another team with the same inputs and comparable resources.

## Inspecting the result is easier than reproducing it

The accompanying project page supplies computer-readable output and describes consistency checks between different representations. Those files give experts concrete material to examine. Agreement between independently constructed forms would be stronger evidence than a fluent explanation from the model alone.

However, the page explicitly says that the calculation programs are not distributed there. A reader can inspect the published outputs without necessarily being able to regenerate the entire calculation. That distinction limits what outside review can establish from this release alone.

For example, checking that two result files agree addresses a different question from checking whether the software correctly constructed both files. A shared mistake could survive a comparison if the procedures rely on the same assumption. This is a general verification concern, not evidence that these particular results contain an error.

The announcement itself restrains the interpretation. Its guest author, physicist Matt von Hippel, distinguishes implementation from a new conceptual breakthrough. Anthropic paid him and provided editorial feedback. Dixon independently checked the result and received usage credits; that validation is distinct from reproducing the complete workflow.

The strongest evidence is therefore the specific reported calculation and its inspectable artifacts. Statements that it proves autonomous scientific invention go beyond that evidence. Equally, dismissing the result because the methods were known would overlook the practical difficulty of implementing and checking a large calculation.

A useful evaluation should separate correctness, human supervision and effort. Correct output does not reveal how much expert guidance was needed. Reduced manual coding does not by itself establish a lower total research cost. Those are separate claims requiring separate records.

The next step is broader technical scrutiny and a reproducible account of the workflow. Additional code, clear inputs and independent regeneration would strengthen confidence in both the amplitude and the claimed research process. Until then, the appropriate conclusion is a reported computational advance with bounded evidence about autonomy.

## Verification

- **PARTIALLY VERIFIED — Model, researchers, duration, established methods, interpretation and disclosure:** Anthropic's account; execution was not independently reproduced here: https://www.anthropic.com/research/yes-claude-can-do-nine-loops
- **VERIFIED AS RELEASED — Output artifacts, described cross-checks and explicit absence of calculation programs on this page:** https://smsharma.io/cosmic-nine-loops/
- **VERIFIED — Eight-loop predecessor, authors and mathematical setting:** Original 2023 paper: https://arxiv.org/abs/2308.08199
- **ANALYSIS — Reproducibility, shared-error and autonomy limits:** Evaluation criteria applied to these primary sources; no error in the calculation is alleged.

## Glossary candidates

- **Scattering amplitude:** A mathematical quantity describing particle interactions.
- **Reproducibility:** The ability to regenerate a result from documented inputs and methods.

Cold-reader sentence: Anthropic reports a nine-loop physics calculation using known methods, with released outputs but incomplete evidence for reproducing the full workflow.
