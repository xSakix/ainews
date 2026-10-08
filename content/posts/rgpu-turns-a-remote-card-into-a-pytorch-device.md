+++
title = "rGPU turns a remote card into a PyTorch device"
description = "The Apache-licensed project keeps Python and model code on a client machine while tensors and CUDA operations run on a remote NVIDIA GPU."
tags = ["projects", "hardware", "tools"]
date = 2026-10-08T03:55:31+02:00
draft = false
+++

Open-source project rGPU lets a PyTorch program keep running on a laptop while its tensors and operations live on a remote NVIDIA GPU.

The Apache-licensed system exposes two paths. New PyTorch code can select `device="rgpu"`, while a broader CUDA shim intercepts calls from existing Linux binaries and forwards them to a server over a network connection.

For a developer with a Mac or a modest workstation and an idle GPU box elsewhere, that split preserves the local coding environment without moving the whole application into a cloud notebook or remote shell. The client can create a tensor on the remote device with ordinary PyTorch syntax, and the supplied launcher establishes an SSH tunnel to the server.

The simple device path sends PyTorch operations over TCP. The compatibility path implements shims for the CUDA driver and runtime as well as cuBLAS, cuBLASLt and cuDNN, aiming to run stock CUDA PyTorch binaries. The repository describes the shim as having a larger compatibility surface, so support will depend on which library calls an application uses.

rGPU includes a nanoGPT training example, operation and configuration references, performance notes and tests across its Python and C++ components. Experimental JAX work is present in the repository but is not listed as a supported product path.

Network security is the main operational constraint. Neither protocol authenticates or encrypts its own traffic. The documentation tells users to keep the operation server bound to localhost and connect through SSH; the CUDA server listens on all IPv4 interfaces, so port 9713 must also be restricted by host or cloud firewall rules.

The project turns remote acceleration into a device choice rather than a separate execution environment, but its performance and compatibility claims currently come from its maintainer's documentation. The code, tests and engineering records are available for inspection, and the project has no tagged release listed on its GitHub page yet.

## Verification

| Claim | Label | Primary source | Independent check |
|---|---|---|---|
| rGPU keeps an application on the client while tensors and GPU work run on a remote NVIDIA machine | VERIFIED | [rGPU repository](https://github.com/ymcrcat/rgpu) | none |
| The project offers a PyTorch `rgpu` device and a CUDA compatibility shim | VERIFIED | [rGPU repository](https://github.com/ymcrcat/rgpu) | none |
| The shim covers the CUDA driver, CUDA Runtime, cuBLAS, cuBLASLt and cuDNN interfaces | VERIFIED | [rGPU repository](https://github.com/ymcrcat/rgpu) | none |
| Neither protocol supplies authentication or encryption; the documentation prescribes SSH and firewall restrictions | VERIFIED | [rGPU repository](https://github.com/ymcrcat/rgpu) | none |
| The repository includes tests, a nanoGPT example and experimental JAX work | VERIFIED | [rGPU repository](https://github.com/ymcrcat/rgpu) | none |
| Compatibility and performance characteristics are documented by the project maintainer | VENDOR-REPORTED | [rGPU repository](https://github.com/ymcrcat/rgpu) | none |
