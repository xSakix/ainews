+++
title = "Pi Pod hosts coding-agent sessions on a private server"
description = "The AGPL project publishes mobile clients and a self-hosted sandbox service. Its separately planned hosted product is not available yet."
tags = ["projects", "agents", "tools"]
date = 2026-10-03T05:37:20+02:00
draft = false
+++

Pi Pod, a self-hosted project presented by developer Evan, runs Pi coding-agent sessions in remote sandboxes that can be reached from a terminal or phone.

Pi is a coding-agent harness, the software that connects a model to files and commands. Pi Pod adds a server-managed session layer around it, so the agent’s workspace can live on infrastructure operated by its user.

**Why it matters:** A developer moving between a computer and phone can attach to the same remote coding session while retaining control over the host. The repository publishes the session server, sandbox service and native mobile-client code together.

The architecture separates clients from execution. A command-line client and iOS and Android applications talk to a REST server and session gateway. The server manages each pod’s lifecycle and launches Pi through a small adapter inside the sandbox service on the same host.

Identity uses Zitadel, an OpenID Connect service, and the README says the application server stores no passwords. The deployment bundles Postgres with the control plane and uses one Docker Compose project for self-hosted installation and upgrades.

The documented host requirements are Linux, 8 GB of RAM, Docker with Compose, Git, OpenSSL and Node.js 22.19 or later. A published command-line package lets another machine log into that server and launch or attach to a pod; native phone clients are separate components in the source tree.

Version coordination is part of the setup. The CLI and server share one exact Pi version pin, and a client newer than its server is refused with a message directing the operator to upgrade the server first. The repository includes commands to check and update those pins.

The code is AGPL-3.0-only and copyrighted to Billzo, LLC. A paid hosted service is planned but is explicitly unavailable today; its per-user hosting, metering and billing extensions are outside this repository. The software available now is the edition users install and operate themselves.

## Verification

| Claim | Label | Primary source | Independent check |
|---|---|---|---|
| Published AGPL-3.0-only Billzo code; CLI/server/sandbox/iOS/Android components; Linux 8 GB RAM and Node22.19+ setup. | VERIFIED | https://github.com/pi-pod/pipod | none |
| Remote session gateway, same-host lifecycle, Zitadel identity/no password storage, Postgres/Compose deployment and version refusal. | VENDOR-REPORTED | https://github.com/pi-pod/pipod | none |
| Hosted service unavailable; hosted billing/metering extensions absent from this edition. | VERIFIED | https://github.com/pi-pod/pipod | none |
| Terminal and mobile clients let a developer attach to a user-operated remote workspace. | ANALYSIS | https://github.com/pi-pod/pipod | none |
| Project publicly shown on dated thread. | VERIFIED | https://news.ycombinator.com/item?id=49937304 | none |
