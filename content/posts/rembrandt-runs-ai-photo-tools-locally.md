+++
title = "Rembrandt runs AI photo tools locally"
description = "The GPL desktop editor combines RAW development, masks, denoising and super-resolution without requiring an account or uploading photographs."
tags = ["projects", "tools"]
date = 2026-10-09T04:00:06+02:00
draft = false
+++

Rembrandt, a new open-source photo editor for macOS, Windows and Linux, runs its AI-assisted denoising, enlargement and masking tools on the user's device.

The GPL-licensed application is a non-destructive RAW developer and photo library rather than a pixel-painting program. It stores edits in standard XMP sidecar files, leaves original photographs unchanged and requires no account for its free local features.

**Why it matters:** Photographers can use computational editing tools without uploading private images or committing their catalogue to a subscription service. The source code and ordinary sidecar format also provide a route out if the application disappears.

Rembrandt includes subject, background, object and depth masks, GPU-based denoising, 2× and 4× super-resolution, focus restoration, HDR and panorama merging, lens corrections and batch editing. A text command such as “warmer and a bit brighter” moves the same visible controls as manual editing; the project says this feature uses a local vocabulary rather than a language model.

The editing engine is JavaScript with WebGL2 and WebGPU shaders inside a small Rust desktop shell. LibRaw handles camera files, while named open projects supply components for enlargement, denoising, lens profiles and visual masks. The project says it supports RAW files from more than 1,000 cameras.

Desktop binaries are available for Apple silicon and Intel Macs, x64 and Arm Windows systems, and x86-64 or Arm Linux. The builds are not yet code-signed, so macOS and Windows users must bypass their operating systems' first-run warnings. Users can also serve the application from a Linux or macOS computer and edit through a browser on their own network.

The repository compares Rembrandt with Lightroom and darktable, but its quality claims have not been independently tested. It also lists missing functions including tethered capture, face recognition, printing and a plugin ecosystem. Optional cloud synchronisation is paid and requires an account; the local editor does not.

The current release, build instructions and checksums are available in the [Rembrandt repository](https://github.com/thesnarkitecht/rembrandt). Its most consequential next test is sustained use on diverse RAW catalogues, where colour handling, camera compatibility and export reliability matter more than a feature checklist.

## Verification

| Claim | Label | Primary source | Independent check |
|---|---|---|---|
| Rembrandt is available for macOS, Windows and Linux under GPL-3.0-or-later | VERIFIED | [Repository](https://github.com/thesnarkitecht/rembrandt) | none |
| Local features require no account and photographs need not be uploaded | VERIFIED | [Repository](https://github.com/thesnarkitecht/rembrandt) | none |
| Edits use XMP sidecars and originals remain unchanged | VERIFIED | [Repository](https://github.com/thesnarkitecht/rembrandt) | none |
| The application includes local denoising, super-resolution and AI-assisted masks | VERIFIED | [Repository](https://github.com/thesnarkitecht/rembrandt) | none |
| The engine uses JavaScript, WebGL2/WebGPU and a Rust desktop shell | VERIFIED | [Repository](https://github.com/thesnarkitecht/rembrandt) | none |
| The project reports support for RAW files from more than 1,000 cameras | VENDOR-REPORTED | [Repository](https://github.com/thesnarkitecht/rembrandt) | none |
| Current desktop builds are not code-signed | VERIFIED | [Repository](https://github.com/thesnarkitecht/rembrandt) | none |
| Optional cloud sync is the only paid feature and needs an account | VERIFIED | [Repository](https://github.com/thesnarkitecht/rembrandt) | none |
