+++
title = "A Language Model Proposed Safety Proofs; Lean Checked Them"
description = "LLM2Cert uses a language model to propose stability and safety certificates, then makes SMT solvers and Lean verify every obligation. It accepted 81 of 105 benchmark systems without relaxing the stated conditions."
tags = ["research", "agents", "safety"]
date = 2026-10-27T04:12:19+01:00
draft = false
+++

Imagine an engineer watching a small autonomous aircraft return to level flight after a gust. The aircraft, the control room and the engineer are invented for this article. The question on the engineer's screen is real: can a mathematical function prove that the controller will keep the system stable, including in states that no finite simulation happened to test?

## A proposal is not a guarantee

Zhipeng Cao, Peiyang Song and seven colleagues built LLM2Cert to separate two jobs that are often blurred when language models enter formal work. A model searches for a useful mathematical certificate. Formal tools decide whether the certificate satisfies every required condition.

Their preprint applies the method to continuous- and discrete-time dynamical systems. These systems describe how a state changes, such as the motion of a robot, vehicle or aerospace platform. A Lyapunov function can certify stability by showing that a quantity decreases along the system's trajectories. A barrier function can certify safety by separating initial states from unsafe ones and showing that the system cannot cross the boundary.

Finding such a function is hard. Checking it can also be hard when the system is nonlinear or has many dimensions. Numerical methods can suffer from floating-point problems. SMT solvers can prove some formulas exactly. However, nonlinear transcendental expressions may lead to timeouts or delta-satisfiable results that do not establish the original statement. Researchers often make the task easier by excluding a region near the origin, replacing difficult terms with approximations or selecting benchmarks that suit the available solver.

LLM2Cert keeps the original target fixed. The language model may change its candidate, but it may not weaken the theorem that the candidate must satisfy.

## The checker controls the loop

The process begins with a typed description of the system, its domain, any unsafe set and the verification task. A proposal agent produces a symbolic certificate. For a controlled system, it also produces a feedback policy. Software parses the output into an expression tree and derives a list of proof obligations from the fixed theorem.

A quick screen tests the candidate on sampled states. A failure produces a counterexample that goes back to the proposal agent. Passing this screen proves nothing, because samples cannot cover a continuous state space. Every obligation still goes to a formal verifier.

A router sends compatible obligations to SMT solvers, which receive 30 seconds for each attempt. An unsatisfiable counterexample query verifies an obligation. A satisfiable query refutes the candidate and returns a counterexample. A timeout or a delta-satisfiable result remains unresolved and moves to Lean.

Lean changes the nature of the acceptance test. The system generates the theorem statement from the fixed candidate. It allows the model to write only the proof body. Lean checks each attempt in a pinned environment, and an audit rejects placeholders such as `sorry` and any axiom outside Lean's standard set. If compilation fails, the model receives the error type, its location and the remaining goal. It also receives matching declarations when an identifier is unknown. The model can try to repair the proof, but it cannot rewrite the claim.

The loop accepts a candidate only when every obligation has either an unsatisfiable verdict from an SMT solver or a proof that Lean's kernel has checked. When a candidate is refuted or remains unresolved, the system sends the evidence back to the proposal agent. The agent may then try again. The experiment allowed at most five candidate rounds and six Lean repair rounds per obligation, with a total limit of 2,400 seconds for each system.

## The benchmark was designed around harder systems

The researchers also built DynaCertBench because existing test collections reflected the limits of existing solvers. They began with 233 entries from 15 papers and BarrierBench. After removing duplicates and structurally repeated systems, 80 distinct literature-derived systems remained.

Only seven of 29 nominally high-dimensional entries survived that curation. The team therefore added extended versions and newly constructed challenges. The final benchmark contains 105 instances across stability, regions of attraction, forward-invariant sets and safety. Twenty-five instances have at least five state dimensions, up from seven in the literature-derived core.

This construction matters when reading the results. Some baseline tools support only parts of the benchmark. Their usual conditions can also include approximations that the new benchmark removes. The authors therefore report results under the original, unrelaxed targets and separate the literature, extended and new tiers.

## Formal feedback changed the result

The complete LLM2Cert system verified 81 of 105 instances, or 77.1%. A one-shot proposal verified 63. The gain from the feedback loop was 17.1 percentage points. An SMT-only version verified 57 systems, and a Lean-only version verified 60. The combination reached 66 of 80 literature-derived systems, seven of 11 extended systems and eight of 14 new systems.

The two verifiers did different work. When the researchers froze the 81 certificates from the successful full run and changed only the verification strategy, the hybrid system verified 22 certificates that an all-SMT strategy left unresolved. SMT was faster on many compatible obligations. Lean could finish exact proofs for some statements that the solvers could not settle within their limits.

The form of feedback also mattered. A generic instruction to retry repaired one of 26 failed proof obligations and completed no full system. Raw compiler diagnostics repaired 17 obligations. Structured feedback repaired 21 and completed 15 of 19 affected systems, while reducing the mean repair time to 407.42 seconds per obligation.

These results come from a preprint, and the benchmark is curated rather than representative of every control problem. The current framework focuses on deterministic systems, verifies prescribed domains instead of optimizing their size and does not yet cover the wider range of stochastic, hybrid and uncertain dynamics that real engineering may require. The accepted certificate is valid under the exact assumptions encoded in the theorem; it does not show that the system description captured every physical failure mode.

## The model searches; the kernel decides

The method extends an established pattern in which a learner proposes a candidate and a verifier checks it. Earlier systems included the SMT-based method by Daniele Ahmed, Andrea Peruffo and Alessandro Abate, as well as FOSSIL 2.0 by Alec Edwards, Peruffo and Abate. These systems alternated candidate generation with formal counterexamples. LLM2Cert uses a language model to widen the search over symbolic expressions and proof scripts. It then uses the verifier's failure messages as the next input.

Lean contributes a smaller trusted core. Leonardo de Moura and Sebastian Ullrich designed Lean 4 as both a theorem prover and a programming language. In this experiment, its kernel checks the explicit proof term. The language model's fluency does not become evidence merely because the generated text looks mathematical.

Return to the imaginary control room. The engineer does not accept a green status because the model says that it found a proof. The status changes only after every fixed obligation has evidence that the formal tools accept. The aircraft remains fictional. The division of labour is concrete: one system searches, another refuses to be persuaded.

## References

- Ahmed, D., Peruffo, A., & Abate, A. (2020). *Automated and Sound Synthesis of Lyapunov Functions with SMT Solvers*. https://arxiv.org/abs/2007.10865
- Cao, Z., Song, P., Vertovec, N., Cui, W., Yang, Z., Liu, M., Lin, L., Xue, B., & Abate, A. (2026). *LLM2Cert: LLM Synthesis of Certificates with SMT/Lean Verification*. https://arxiv.org/abs/2610.30524
- de Moura, L., & Ullrich, S. (2021). *The Lean 4 Theorem Prover and Programming Language*. https://doi.org/10.1007/978-3-030-79876-5_37
- Edwards, A., Peruffo, A., & Abate, A. (2024). *FOSSIL 2.0: Formal Certificate Synthesis for the Verification and Control of Dynamical Models*. https://arxiv.org/abs/2311.09793
- FormalCert-AI. (2026). *LLM2Cert code and experiment artifacts*. https://github.com/FormalCert-AI/llm2cert

