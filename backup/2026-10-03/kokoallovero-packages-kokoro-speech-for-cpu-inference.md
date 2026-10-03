+++
title = "Kokoallovero packages Kokoro speech for CPU inference"
description = "A C++ implementation bundles English pronunciation tools with Kokoro-82M and reports roughly twice PyTorch’s synthesis speed on two Intel CPUs."
tags = ["projects", "models", "tools"]
date = 2026-10-03T05:46:20+02:00
draft = false
+++

Kokoallovero, a C++ speech-synthesis project by developer RobViren, packages the Kokoro-82M voice model with English pronunciation tools for CPU-only use.

The developer wanted a voice interface for Claude Code that could be copied between machines without a Python installation or a separate pronunciation engine. The result turns text into 24 kHz audio using bundled assets and processor-specific vector operations.

**Why it matters:** A developer building a local voice application gets speech synthesis and text-to-pronunciation processing in one deployable package. The project’s optional embedded build includes the assets in a single executable of about 350 MB.

RobViren reports approximately twice PyTorch’s synthesis speed on two Intel processors. The comparison uses the same short sentence and voice with four synthesis threads: about 470 milliseconds against 916 on an i7-14700F, and about 902 against 1,770 on an i7-7700. Those timings cover synthesis, rather than the complete text-normalization and playback path.

The implementation uses Google Highway, a library that selects vector-instruction implementations at runtime. Its kernels were tuned and tested on AVX2, with AVX-512 disabled by default. An ARM build is documented, but the developer says its speed remains untuned and the audio comparison was made under emulation.

The pronunciation pipeline has a different openness boundary from the engine. The source includes tools for exporting Kokoro weights and training a pronunciation guesser, while the lexicon database, tagger corpus and guesser’s training lexicon are private. The shipped binary assets therefore support running the package without fully reproducing those training inputs.

Building requires CMake and a C++ compiler; the asset-embedding option needs GCC 15 or later. Dependencies and missing weights are fetched during configuration, and the documentation says runtime use requires no downloads. The repository carries an Apache-2.0 licence.

RobViren says text normalization still needs improvement and describes the current package as sufficient for the intended voice-interface work. The release includes the benchmark script and repeatable synthesis command, giving other users the concrete baseline behind its CPU speed claim.

## Verification

| Claim | Label | Primary source | Independent check |
|---|---|---|---|
| Developer, Apache-2.0 C++ source, Kokoro-82M, English-only G2P, 24 kHz output, optional approximately 350 MB embedded binary, CMake/GCC requirements. | VERIFIED | https://github.com/RobViren/kokoallovero | none |
| Synthesis-only four-thread timings: i7-14700F 470/916 ms (1.95x); i7-7700 902/1770 ms (1.96x), one 6.6-second sentence, af_heart voice. | VENDOR-REPORTED | https://github.com/RobViren/kokoallovero | none |
| Highway dispatch; AVX2 tuning, AVX-512 default off; ARM untuned/emulated; pronunciation data private; runtime downloads unnecessary. | VENDOR-REPORTED | https://github.com/RobViren/kokoallovero | none |
| Bundling reduces deployment components for a local voice developer. | ANALYSIS | https://github.com/RobViren/kokoallovero | none |
| Project publicly shown on dated thread. | VERIFIED | https://news.ycombinator.com/item?id=49937676 | none |
