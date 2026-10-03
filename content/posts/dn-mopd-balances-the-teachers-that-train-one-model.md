+++
title = "DN-MOPD balances the teachers that train one model"
description = "A multi-teacher distillation study finds that instruction-following feedback can dominate mathematics feedback. Rescaling that feedback improves the combined student across tested model sizes."
tags = ["research", "agents"]
date = 2026-10-03T05:52:20+02:00
draft = false
+++

DN-MOPD, a training method led by Nanyang Technological University researchers, improves multi-teacher model distillation by balancing the strength of each specialist’s feedback instead of only choosing which specialist teaches.

Xin Li and colleagues from Nanyang Technological University, Yale University and the University of Manchester combine mathematics, coding and instruction-following specialists into one student model. Their diagnosis is that equal treatment of prompts can still produce unequal influence on the shared parameters.

**Why it matters:** A post-training engineer merging specialist models needs each skill to survive the combination. This study makes the strength of feedback an explicit variable, explaining why correctly routing a mathematics problem to its mathematics teacher can still transfer little mathematics ability.

The [preprint](https://arxiv.org/abs/2609.35347), first submitted on 28 September, studies Qwen3.5 models at three sizes. Standard multi-teacher distillation failed to beat the best single-teacher student at any size and retained only a small fraction of the mathematics specialist’s improvement under one evaluated answer budget.

The student generates its own answer, and the teacher for that prompt’s domain supplies feedback on each token. That is on-policy distillation: instruction targets are applied to answers produced by the current learner, rather than exclusively to a fixed collection of teacher-written answers.

Routing identifies the relevant teacher. It does not set how strongly that teacher’s feedback changes the student. Instruction-following feedback had a much wider spread than mathematics feedback, and in the initial four-billion-parameter student it contributed nearly all of the combined update under equal weights.

The mechanism resembles a committee whose members have equally many turns but different microphone volumes. Giving the mathematics teacher its allotted prompts cannot balance the outcome when another teacher’s feedback arrives at a much greater scale. DN-MOPD adjusts that scale while keeping the teacher assignments.

The method measures the spread of feedback separately for each domain in the current batch. A bounded multiplier brings those signals toward a common scale while preserving their direction. It requires neither another teacher call nor a learned routing model; it changes how existing signals count.

## Turning down one teacher restores the others’ influence

The authors compare independently trained specialist pools at nine, four and two billion parameters. Teachers and students have matching sizes within each pool. The main comparisons share specialists, starting student weights and prompts, helping separate feedback balancing from a different training corpus or a stronger teacher.

Across six public benchmarks, DN-MOPD improves the average over ordinary domain-routed distillation at every size. The pattern holds across three random student seeds and two answer-length limits. The reported average gains are roughly one to three percentage points, with mathematics supplying the largest recovery.

The controls clarify what produces the improvement. Increasing mathematics feedback alone does less than limiting the oversized instruction-following signal. Fixed domain weights near the values measured by DN-MOPD also perform comparably, suggesting that much of the benefit comes from correcting the imbalance rather than requiring elaborate dynamic routing.

This evidence narrows the claim. DN-MOPD offers a way to identify and control feedback scale, while comparable fixed weights show that the measured balance can sometimes be implemented more simply. Choosing a teacher and calibrating its influence are distinct decisions in the same training process.

The paper also tests whether adding early imitation of teacher answers restores the lost specialist ability. That intervention does not replace the need to control the feedback imbalance. The central issue remains how multiple domain signals update the same student, rather than whether each domain has an available expert.

The measurements are author-reported preprint results limited to the studied Qwen3.5 specialist pools and tasks. Some comparisons against the strongest single-teacher student have uncertainty intervals that include no improvement, even though the averages favor DN-MOPD. The repeat-seed results support the comparison with ordinary multi-teacher routing more directly.

The authors provide a [project page](https://lixin.ai/DN-MOPD) and [code](https://github.com/LiXin97/DN-MOPD). Their control experiments leave a practical conclusion: the training signal from an instruction-following specialist can overwhelm other specialists even when the prompt-routing rule is correct.

## Verification

| Claim | Label | Primary source | Independent check |
|---|---|---|---|
| Li and collaborators’ NTU/Yale/Manchester affiliations; v1 28 September 2026. | VERIFIED | https://arxiv.org/abs/2609.35347 | none |
| Qwen3.5 9B/4B/2B specialist pools; matching sizes and shared initialization/prompts; six benchmarks, three seeds, 8K/16K evaluation budgets. | VENDOR-REPORTED | https://arxiv.org/abs/2609.35347 | none |
| Ordinary MOPD fails to beat strongest single-teacher student; retains 14–32% mathematics gain at8K and no gain at16K. | VENDOR-REPORTED | https://arxiv.org/abs/2609.35347 | none |
| Initial4B instruction-following contributes94% combined gradient; feedback spread2.3–4.4× pooled scale. | VENDOR-REPORTED | https://arxiv.org/abs/2609.35347 | none |
| Domain-spread normalization uses bounded sign-preserving multipliers, no added teacher/call/router. | VERIFIED | https://arxiv.org/abs/2609.35347 | none |
| Mean improvements1.17–2.36points at16K,2.47–3.08at8K; fixed weights comparable; downweighting instruction-following key; early imitation control; single-teacher uncertainty caveat. | VENDOR-REPORTED | https://arxiv.org/abs/2609.35347 | none |
| Project and code offered. | VERIFIED | https://lixin.ai/DN-MOPD ; https://github.com/LiXin97/DN-MOPD | none |
| Engineer consequence and microphone analogy explain unequal feedback influence despite routing. | ANALYSIS | https://arxiv.org/abs/2609.35347 | none |
