+++
date = '2026-09-19T04:00:00+02:00'
draft = false
title = 'Analysis Says ZCode Uploaded Git History'
+++

After reading this, the reader knows what ZCode allegedly uploaded, how investigators traced it and which claims remain unverified.

# Analysis Says ZCode Uploaded Git History

*Reverse engineering indicates that Z.ai's coding app captured repository snapshots outside its visible agent tools and encrypted them for server-side access.*

An independent analysis says ZCode, a desktop coding agent from Z.ai, packaged a workspace including its `.git` directory and uploaded the encrypted archive to Alibaba Cloud storage. The report was published by Tokenstead based on reverse engineering by a developer using the name ferstar and additional prompt analysis.

In plain terms, the alleged upload contained more than the files open in the editor. Git objects can preserve prior versions, branches and deleted content. The app reportedly performed the capture through a background component rather than a tool call visible to the coding agent.

## Why it matters

Developers often give coding agents access to repositories containing proprietary code, unreleased plans and secrets that were removed from the current working tree but remain in history. Uploading the entire repository changes the data boundary that a user may infer from sending a prompt or selected files.

Tokenstead describes one captured commercial workspace containing 42,411 files. The plaintext manifest attributed 86.6% of the snapshot payload to `.git` data. Those measurements come from one investigator's environment and should not be treated as a prevalence estimate across installations.

The reconstructed flow begins when the client requests upload credentials from a ZCode server. According to the analysis, the client creates a compressed archive, encrypts it with a symmetric key, wraps that key with a server-provided RSA public key and posts the archive to Aliyun Object Storage Service. The local client did not hold the corresponding private key.

## The capture reportedly sits outside agent permissions

The report says the upload is implemented by a host-level sidecar started when the user is logged in. It is not listed among the tools that the model can choose. If accurate, declining an agent tool call would not stop this component because it operates beneath the agent's visible action loop.

Tokenstead also says two settings did not prevent packaging and upload. One controlled whether data could be used for model training, and another controlled server-side indexing of snapshots. The report says neither disabled capture itself.

These findings require independent reproduction. Tokenstead cites local manifests, client-code inspection, logs and network connections, but this article did not run ZCode or inspect the binary. The report says an account affiliated with the ZCode team replied to the original researcher, yet no substantive public technical response from Z.ai was located in the reviewed material.

Encryption does not resolve the consent question. Transport or storage encryption can protect data from unrelated parties while still allowing the service operator to decrypt it. The relevant questions are what was collected, why it was necessary, how long it was retained and whether the user had an effective opt-out.

Organizations evaluating coding agents should test the application at the network and filesystem layers. A disposable repository with canary files can show what is read and transmitted. Egress controls can block destinations not required for approved operation, while secrets should be removed from reachable history before any agent receives access.

The next decisive evidence should be a Z.ai postmortem, product change or reproducible third-party capture across current versions. Until then, the correct description is an independently reported security and privacy finding, not a fully adjudicated vendor incident.

## Verification

- **Tier 1 — INVESTIGATOR-REPORTED:** Tokenstead published the reverse-engineering report on 18 September 2026 and documented one workspace manifest, client-code analysis and an upload flow to Aliyun storage. Primary investigative source: https://tokenstead.ai/guides/zcode-silent-git-history-upload
- **Tier 1 — INVESTIGATOR-REPORTED:** The report attributes 86.6% of one payload to `.git` data and says capture continued despite two settings. Same primary investigative source.
- **Tier 3 — UNVERIFIED:** This article did not reproduce the behavior, and no substantive public Z.ai technical response was located in the reviewed source.
- **Tier 2 — ANALYSIS:** Consent, encryption and enterprise-testing implications are editorial analysis.

## Glossary candidates

- **Git object store:** The repository data that preserves commits, file versions and history.
- **Envelope encryption:** Encrypting data with one key, then encrypting that key with another key.

Cold-reader sentence: Independent analysis says ZCode uploaded encrypted repository history through a background component, but the behavior still needs broader reproduction and vendor response.
