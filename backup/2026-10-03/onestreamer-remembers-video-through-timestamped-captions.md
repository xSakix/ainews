+++
title = "OneStreamer remembers video through timestamped captions"
description = "A Nanjing University-led team combines recent frames with written records of earlier events. Its tests examine whether memory can improve without sacrificing current perception."
tags = ["research", "agents"]
date = 2026-10-03T05:54:20+02:00
draft = false
+++

OneStreamer, a streaming-video model from a Nanjing University-led team, remembers earlier events through timestamped captions while retaining recent frames, improving historical answers without sacrificing current perception in the authors’ tests.

Xiangyu Zeng and collaborators teach the model to write evidence down as video arrives, before it knows which future question will need that evidence. Its later answers can combine those records with what the camera is showing now.

**Why it matters:** A developer building a live-video assistant needs the system to remember an earlier event after its frames disappear from the working context. OneStreamer separates that stored account from current visual detail, making the memory–perception trade inspectable.

The [preprint](https://arxiv.org/abs/2610.01762), first submitted on 1 October, describes a model with four billion parameters and a training dataset exceeding one million records. The team reports leading results among compared systems across eight benchmarks covering current perception, memory and the timing of responses.

That broad ranking matters less to the mechanism than a controlled comparison. The authors kept the same model checkpoint and recent visual window, then changed whether generated caption records remained available. Retaining them improved one historical-question score from about 64 to 72, while current perception stayed similar or improved slightly.

The memory contains two levels of description. Local captions record details at particular times; broader summaries describe completed events. Together they retain both the pieces a later answer may need and the larger event those pieces belong to.

A written incident log offers a useful comparison. The live view supplies the present scene, while dated notes preserve earlier evidence without occupying the screen with every old image. OneStreamer generates its own notes, however, so the accuracy of what it writes remains part of the system’s reliability.

The training pipeline imposes a timing constraint: a caption or answer must be supported by evidence already visible at that moment. Offline video annotations are converted into streaming examples with release times tied to when the relevant evidence becomes available. This prevents a training target from depending on frames that the model has not yet received.

## Memory records complement the recent visual window

The authors compare three ways of retaining evidence: all historical visual features, only recent frames, and recent frames supplemented with caption memory. Keeping every old visual feature improved some historical answers but weakened current perception compared with the recent-only setting.

Caption memory recovered historical information while preserving the short visual window. The combination beat the all-history condition on one historical metric, although another was slightly lower. That distinction grounds the conclusion in specific tests rather than treating textual memory as a universal replacement for images.

OneStreamer also learns when to record or respond. Streaming interaction contains many repeated waiting states and comparatively few output decisions. Its training method selects representative waiting and transition tokens while preserving supervision at output anchors, reducing the dominance of silence in the learning signal.

This response-timing component serves the same spine: recording evidence and using it when needed. A system that remembers correctly but responds before enough evidence arrives still fails the live interaction. The paper’s training examples therefore connect content with the moment at which it becomes justified.

The model starts from Qwen3-VL-4B-Instruct and undergoes supervised fine-tuning. In the authors’ comparison, it also exceeds the larger MOSS-VL-Realtime on the four perception-and-memory benchmarks. These remain measurements by the team that developed the model, with no independent reproduction established in the preprint.

A reported failure shows the cost of an incorrect record. OneStreamer describes a printer cover as closing when the video shows it opening, then stays silent after later frames clarify the open state. Better retention does not by itself ensure that an earlier interpretation will be corrected.

The [project page](https://mcg-nju.github.io/OneStreamer) accompanies the paper. Its demonstrated unresolved problem is therefore specific: a streaming assistant must update an account it has already emitted when new visual evidence reveals that the account was wrong.

## Verification

| Claim | Label | Primary source | Independent check |
|---|---|---|---|
| Zeng and collaborators; Nanjing University-led affiliations; v1 submitted 1 October 2026. | VERIFIED | https://arxiv.org/abs/2610.01762 | none |
| 4B parameters; >1 million training records; leads compared methods on eight benchmarks; Qwen3-VL-4B-Instruct base and supervised fine-tuning. | VENDOR-REPORTED | https://arxiv.org/abs/2610.01762 | none |
| Same-checkpoint Recent-16 caption retention raises historical ASI 63.5 to 71.6; EPM 62.0 to 62.6; current OVOBench 80.9 to 81.4 and StreamingBench 86.3 to 86.9. | VENDOR-REPORTED | https://arxiv.org/abs/2610.01762 | none |
| Local timestamped captions and completed-event summaries; causal target timing and selective state-token supervision. | VERIFIED | https://arxiv.org/abs/2610.01762 | none |
| Full visual history trades current perception for historical evidence; PHCM ASI 71.6 vs full 67.6, EPM 62.6 vs full 63.0; comparison with MOSS-VL-Realtime. | VENDOR-REPORTED | https://arxiv.org/abs/2610.01762 | none |
| Printer-opening/closing error and failure to correct are reported failure case; project accompanies paper. | VERIFIED | https://arxiv.org/abs/2610.01762 ; https://mcg-nju.github.io/OneStreamer | none |
| Developer consequence and dated-log comparison explain separating memory from current frames. | ANALYSIS | https://arxiv.org/abs/2610.01762 | none |
