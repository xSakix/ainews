+++
date = '2026-09-19T04:00:00+02:00'
draft = false
title = 'Claude Code Adds AGENTS.md Support'
+++

After reading this, the reader knows how Claude Code now discovers shared repository instructions and where the fallback is unavailable.

# Claude Code Adds AGENTS.md Support

*Anthropic's coding agent now reads a cross-tool instruction file when its own project file is absent, reducing one source of repository-specific duplication.*

Anthropic has added `AGENTS.md` support to Claude Code version 2.1.277. When a repository contains no `CLAUDE.md`, the coding agent now reads `AGENTS.md` as its project instruction file.

In plain terms, a team can place build commands, testing rules and repository conventions in one file that several supporting agents understand. Claude Code still gives its native file priority. The new behavior is a fallback, not an automatic merge of both files.

## Why it matters

Coding agents need more than source code. They must know which formatter to run, which directories are generated, how tests are divided and what local conventions should not be inferred from examples. Teams commonly store that operational context in a repository-level instruction file.

Vendor-specific filenames create maintenance debt. A repository can end up with several near-identical files whose contents drift. One agent receives a new security restriction while another keeps following an old command. A shared convention makes the instructions easier to review alongside code changes.

The change also improves portability at a practical layer. Switching coding tools does not make their models or execution policies equivalent, but it lets a repository carry a common starting document. That can reduce setup work in projects where developers use different assistants locally and in continuous integration.

The exact precedence rule is important. Claude Code reads `AGENTS.md` only when `CLAUDE.md` is missing. Teams that already maintain both files should not assume edits to the shared file will affect Claude Code. They must remove the native file, synchronize the two documents or deliberately keep separate instructions.

## A common file is not a common security model

Instruction portability does not standardize permissions. Coding agents still differ in how they approve shell commands, access networks, load nested files and protect secrets. A command that is harmless inside one sandbox may have broader effects in another environment.

Repositories should therefore keep shared instructions focused on project facts and verifiable procedures. Examples include the package manager, supported runtime, test commands and directories that must not be edited. Access policy and deployment credentials should remain controlled by the execution environment rather than trusted to prose alone.

Nested repositories introduce another question: which instruction file applies at each path? The changelog entry establishes the top-level fallback but does not document a new cross-vendor specification for merging or scoping multiple files. Teams should test behavior before relying on directory-specific overrides.

Anthropic also says the feature is not yet available when Claude Code runs through Amazon Bedrock, Google Vertex AI or Microsoft Foundry. Organizations using those managed providers should treat support as deployment-dependent rather than a property of the repository itself.

The useful next step is a small compatibility test. Put one harmless, visible rule in `AGENTS.md`, open the project with each supported agent and confirm that the rule appears in its loaded instructions. Repeat after adding a native instruction file to confirm precedence.

This is a modest product change, but it addresses a real coordination problem. Repository instructions work best when they are versioned, reviewable and shared. The fallback moves Claude Code closer to that model without pretending that all coding agents behave the same way.

## Verification

- **Tier 0 — VERIFIED:** Anthropic's Claude Code changelog dated 18 September 2026 says version 2.1.277 reads `AGENTS.md` when no `CLAUDE.md` exists. Primary source: https://code.claude.com/docs/en/changelog
- **Tier 0 — VERIFIED:** Anthropic says the feature is not yet available on Amazon Bedrock, Google Vertex AI or Microsoft Foundry. Same primary source.
- **Tier 2 — ANALYSIS:** Portability, maintenance and security implications are editorial analysis.

## Glossary candidates

- **Repository instruction file:** Versioned guidance that tells an agent how to work inside a codebase.
- **Fallback:** A secondary source used only when the preferred source is absent.

Cold-reader sentence: Claude Code now reads AGENTS.md when CLAUDE.md is absent, making shared repository guidance easier while preserving vendor-specific precedence.
