+++
date = '2026-09-22T04:00:20+02:00'
draft = false
title = 'Kev Brings Decision Models to Local Hardware'
+++

*Jared Palmer released three small Qwen3.5-based models that answer structured decisions locally and expose probabilities instead of only a final label.*

Kev is an open project for questions such as whether to escalate a support case, which department should handle it or how strongly a text fits a rating scale. Its 0.8B, 4B and 9B models can run on common local hardware, including Apple Silicon, and use an API compatible with TypeSafe's hosted System One service.

## Why it matters

Many business workflows do not need a general chatbot. They need a repeatable decision with a confidence estimate. A compact model that runs inside an organization's network can keep source text local and may cost less to operate than a frontier model, provided its accuracy is sufficient for the specific policy.

Kev accepts one shared input and several isolated questions. It can return yes-or-no probabilities, choose among named options or place an answer on an ordered scale. The project says questions cannot read one another, reducing the chance that one requested judgment changes another. That mechanism is documented in the code and interface, although operational isolation should still be tested.

The models are built on Qwen3.5 bases and ship with training code, evaluation data and model cards. The 4B and 9B versions fit in 32GB of memory in bf16 format, according to the project's serving notes. The smallest model trades accuracy for a smaller footprint.

## The comparison needs care

The author reports that Kev-9B reached 0.852 accuracy on a held-out test of new sources. The same table gives Jev, a hosted decision model that inspired the architecture, 0.857 on a development set but no test result. These numbers are not directly interchangeable.

The repository explicitly says the Jev comparison is uncontrolled because Jev's training data are unknown. It also reports that temperature calibration reduced Kev-9B's calibration error on new sources without changing accuracy. Both findings come from project-run evaluations, and independent reproduction would make them more useful.

Calibration matters because an automated decision is easier to govern when a reported 80% confidence corresponds roughly to eight correct answers in ten similar cases. A model can choose the right label often while being dangerously overconfident on its mistakes. Kev's probability output is therefore more informative than a label alone, but only if calibration holds on the buyer's own data.

The sensible deployment path is narrow: select one decision, build a representative test set, compare errors with an existing rule or reviewer, and establish a threshold for human escalation. The model should not inherit authority merely because it can return a number.

Future evidence should include independent evaluations, domain-specific error analysis and tests for option-order sensitivity. Kev already provides a playground for permuting answer order, which makes one common failure mode visible instead of hiding it.

## Verification

1. **VERIFIED — Kev publishes 0.8B, 4B and 9B Qwen3.5-based decision models, code and evaluation material.** Primary source: https://github.com/jaredpalmer/kev
2. **VERIFIED — The API supports yes/no, choice and score questions and is compatible with TypeSafe's System One interface.** Primary source: https://github.com/jaredpalmer/kev
3. **VERIFIED AS PROJECT-REPORTED RESULTS — Accuracy, calibration and memory figures come from the project's own tests and documentation.** Primary source: https://github.com/jaredpalmer/kev
4. **VERIFIED — The project warns that its Jev comparison is not controlled because Jev's training data are unknown.** Primary source: https://github.com/jaredpalmer/kev

## Glossary candidates

- **Calibration:** How closely confidence scores match observed success rates.
- **Brier score:** A measure of error in probabilistic predictions; lower is better.
- **bf16:** A compact numerical format commonly used to run neural networks.

Cold-reader sentence: Kev packages small local models for structured decisions, with useful probability outputs but only project-run evidence of accuracy and calibration.
