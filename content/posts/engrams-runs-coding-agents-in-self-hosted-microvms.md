+++
title = "Engrams runs coding agents in self-hosted microVMs"
description = "Cortex publishes an agent orchestrator that snapshots idle sessions, with Firecracker isolation in production and explicit development fallbacks."
tags = ["projects", "agents", "tools"]
date = 2026-10-03T05:42:20+02:00
draft = false
+++

Engrams, a self-hosted orchestrator published by Cortex Applications, runs coding-agent sessions in Firecracker microVMs and restores saved sessions when new prompts arrive.

A session combines a Linux container image with an agent harness, the software that runs model calls and tools. The host supplies the runtime and captures memory and disk state when the agent becomes idle, preserving the workspace between periods of execution.

**Why it matters:** An engineer operating a coding-agent service can host the session state and isolation layer in their own cloud account. The project includes the dashboard, command-line client and deployment definitions, rather than only a sandbox library.

Cortex reports restoration in under 100 milliseconds on the same host, one to two seconds on a different host and under a second from cold without prewarming. Its README also illustrates storage deduplication with a thousand sessions based on one shared image; both speed and capacity figures are the company’s own claims.

The storage design uses immutable chunks addressed by their content hashes. Base-image chunks are shared, while a snapshot writes changed chunks and records a manifest pointing to them. A restored session fetches disk data and memory pages as needed instead of first copying an entire image.

Production deployment uses Kubernetes, a dedicated host fleet with nested virtualization, and two Helm releases for the control plane and hosts. Terraform examples target Google Cloud and AWS, with their object stores and secret managers supplying shared state and credentials. Host agents connect outward to the coordinator, avoiding an inbound control port.

Isolation depends on the selected environment. Production uses Linux KVM and Firecracker; the Apple Silicon development backend uses Apple’s virtualization framework. Elsewhere, the quick-start can run plain subprocesses without isolation. The README explicitly separates that development setup from its production topology.

The main code is AGPL-3.0, with selected custom-harness SDK crates under Apache-2.0. Claude Code and Codex harnesses ship with the project, while users provide model access. Cortex calls it an unfinished 0.x release with changing interfaces and a maintained Firecracker fork—concrete maintenance obligations for the self-hosted operator.

## Verification

| Claim | Label | Primary source | Independent check |
|---|---|---|---|
| Cortex source, AGPL-3.0 plus Apache-2.0 SDK crates, Firecracker/KVM production, harness/image deployment and 0.x/fork status. | VERIFIED | https://github.com/cortexapps/engrams | none |
| Restoration under100 ms same host,1–2 s other host,under1 s cold;1000 sessions4 GiB base about100 GiB storage rather than4 TiB. | VENDOR-REPORTED | https://github.com/cortexapps/engrams | none |
| Hash-addressed snapshots/lazy reads, cloud deployment/outbound hosts, Apple development VM and subprocess fallback without isolation. | VENDOR-REPORTED | https://github.com/cortexapps/engrams | none |
| Self-hosted code gives an operator control over session state and deployment boundaries. | ANALYSIS | https://github.com/cortexapps/engrams | none |
| Project publicly shown on dated thread. | VERIFIED | https://news.ycombinator.com/item?id=49927208 | none |
