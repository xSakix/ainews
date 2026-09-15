+++
date = '2026-09-15T23:35:00+02:00'
draft = false
title = 'Strix finds GitHub token in Baseten image'
+++

After reading this, the reader knows Strix says it found a live GitHub token in a public Baseten container image, and how build history can expose secrets.

# Strix finds GitHub token in Baseten image

*The security company says it stopped after read-only checks, disclosed the issue and saw Baseten rotate the credential and restrict its registry the next day.*

Security company Strix says its autonomous testing agent found a live GitHub personal access token in the build history of a publicly downloadable Baseten container image.

In plain terms, deleting a secret from the final filesystem did not remove it from the image's historical metadata. Anyone able to pull the image could inspect the build command and potentially recover the credential.

## Why it matters

Container images are layered records of how software was assembled. A file removed in a later layer can remain in an earlier layer, and a secret placed directly in a Dockerfile command can appear in image-history fields. Scanning only the running container's visible files can therefore miss a credential that is still present in the distributed artifact.

Strix says it tested Baseten's public-facing systems as a black-box exercise. Its agent discovered a Harbor container registry that allowed anonymous pulls, downloaded an image named `baseten/baseten-app` and inspected its history. The company says one `history[].created_by` entry contained a token associated with the `basetenbot` GitHub account.

Using read-only API requests, Strix says it confirmed that the token remained active and had access to multiple repositories, including administrative or push permissions on repositories used for product, GitOps and package-distribution work. Strix says it did not clone repositories, push code or change settings and stopped after establishing scope.

The disclosure is a detailed primary account from the security vendor that found the issue. No separate Baseten post confirming the technical scope was located, so the access claims remain only partially independently verified.

## A one-day fix for a long-lived credential

Strix's timeline says the token originated in a March 2023 build and was discovered in July 2026. It reported the issue to Baseten on July 13. According to Strix, Baseten made the registry private and rotated the token on July 14, then closed remaining items by July 17.

The age matters because credential exposure is not limited to the moment an image is built. Images can be copied into caches, mirrors and developer machines. Rotation ends future use of a token, but defenders may still need to review logs for historical access and locate every copy of the artifact.

Strix credited Baseten with a rapid response and says Baseten classified the report as critical. That characterization comes through Strix's disclosure; without Baseten's own incident report, it does not establish whether the token was abused before discovery.

The direct prevention is to keep secrets out of build arguments and shell commands. Docker BuildKit secret mounts can expose a credential temporarily during a build without storing it in the resulting layer or command history. Teams should also inspect image history, scan registries, use short-lived credentials and grant only the repository permissions required for a job.

The incident also shows the limits of autonomous security tools. An agent may find and triage a flaw quickly, but authorization boundaries, minimal validation and human-controlled disclosure remain essential when a discovered token can alter source code or deployment configuration.

## Verification

1. **VERIFIED — Strix published a disclosure describing a GitHub token in a Baseten container image's build history.** This verifies the publication, not independent reproduction of access. Primary source: https://www.strix.ai/blog/baseten-harbor-github-pat-takeover
2. **PARTIALLY VERIFIED — The registry allowed anonymous pulls and the token was live with broad repository permissions.** Strix provides technical detail and screenshots, but no independent Baseten account was located. Primary disclosure: https://www.strix.ai/blog/baseten-harbor-github-pat-takeover
3. **VERIFIED — Strix says it limited validation to read-only requests and did not clone, push or change settings.** This is the researcher's stated conduct. Primary source: https://www.strix.ai/blog/baseten-harbor-github-pat-takeover
4. **PARTIALLY VERIFIED — Baseten restricted the registry and rotated the token one day after disclosure, then closed remaining issues by July 17.** The timeline is documented by Strix but not separately confirmed in a located Baseten statement. Primary disclosure: https://www.strix.ai/blog/baseten-harbor-github-pat-takeover
5. **UNVERIFIED — No unauthorized party used the token before it was rotated.** The disclosure does not establish absence of earlier access.
6. **VERIFIED — Secrets included in image layers or build commands can persist in image history; BuildKit provides secret mounts intended to avoid baking credentials into images.** Primary documentation: https://docs.docker.com/build/building/secrets/
7. **PARTIALLY VERIFIED — Automated security agents can shorten discovery and triage.** This case shows one reported success, not comparative evidence against human testing.

## Glossary candidates

- Personal access token
- Container layer
- Image history
- Harbor registry
- BuildKit secret mount

**Cold-reader sentence:** Strix says a public Baseten image exposed a live GitHub token through build metadata, showing why container history must be scanned for secrets.
