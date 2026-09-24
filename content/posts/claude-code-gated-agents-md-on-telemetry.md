+++
date = '2026-09-24T03:58:09+02:00'
draft = false
title = 'Claude Code Gated AGENTS.md on Telemetry'
+++

*A developer found that Claude Code could silently skip local AGENTS.md instructions when telemetry or nonessential network traffic was disabled.*

Developer Przemek Szypowicz reproduced the behavior in Claude Code versions 2.1.277 through 2.1.280. The coding agent’s support for an AGENTS.md project-instruction file was controlled by a remote feature flag. When privacy settings blocked that flag, the local file was not loaded and Claude Code displayed no warning.

## Why it matters

Project instructions tell a coding agent how to build, test and edit a repository. If the agent silently misses them, it can use the wrong commands, ignore architectural boundaries or produce changes that violate team rules. The failure is especially confusing because the file is local and appears unrelated to telemetry.

Szypowicz tested an otherwise empty directory containing an AGENTS.md file with a canary word. He asked Claude Code to report that word without directly reading files. With either `DISABLE_TELEMETRY` or `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` present, the word did not reach the model. Clearing both settings allowed the remote flag to resolve and the file to load on a later session.

Inspection of the bundled plugin showed why. The AGENTS.md loader was off by default and checked a remote flag named `tengu_agents_md_mod`. When the client could not fetch the flag, the fallback was false. A network-dependent rollout mechanism therefore controlled whether a purely local instruction source existed from the agent’s perspective.

The problem also affected environments that route model calls through Amazon Bedrock, Google Vertex AI or third-party gateways, according to the report and linked issue. Those configurations often block nonessential traffic by design. Teams choosing them for governance could receive different instruction behavior without a visible configuration difference inside the repository.

## Workaround and reported fix

The demonstrated workaround is a one-line CLAUDE.md file that imports AGENTS.md with `@AGENTS.md`. Szypowicz found that this import continued to work while nonessential traffic was disabled because CLAUDE.md loading did not depend on the same flag. The workaround adds another repository file but restores deterministic behavior.

A comment linked from the report says Claude Code 2.1.281 changes the fallback so AGENTS.md support does not depend on the remote switch in the same way. This run did not reproduce the behavior on that release, so the fix is treated as reported rather than independently confirmed.

The design lesson reaches beyond one product. Agent configuration should be observable. A command-line tool can print which instruction files it loaded, which skills it found and which optional features were unavailable. That turns a hidden behavioral difference into a diagnosable state.

Teams using coding agents should add a small startup or continuous-integration check that asks the agent to repeat a harmless canary from project instructions. They should also pin known-good versions when instruction loading is operationally important. Prompt quality cannot compensate for a prompt that never reaches the model.

The next useful confirmation is a public release note and independent test of the changed fallback across direct, Bedrock, Vertex and gateway configurations.

## Verification

1. **VERIFIED AS A REPRODUCIBLE AUTHOR REPORT — Claude Code 2.1.277–2.1.280 skipped AGENTS.md in the documented test when telemetry or nonessential traffic was disabled.** Primary source: https://blog.szypowi.cz/p/claude-code-reads-agents.md-only-when-telemetry-is-on/
2. **VERIFIED AS CODE INSPECTION — The bundled loader used a remote feature flag with a false fallback.** Primary source: the technical report above.
3. **VERIFIED AS AN AUTHOR-REPORTED WORKAROUND — Importing AGENTS.md from CLAUDE.md worked in the reported test.** Primary source: the technical report above.
4. **PARTIALLY VERIFIED — A linked Anthropic issue comment reports a fix in version 2.1.281; this run did not reproduce it independently.** Via: https://github.com/anthropics/claude-code/issues/95690

## Glossary candidates

- **Feature flag:** A switch that enables or disables software behavior without changing the installed code.
- **Telemetry:** Diagnostic or usage data sent from software to its operator.
- **Canary:** A harmless test value used to show whether a path is working.

Cold-reader sentence: Claude Code’s AGENTS.md loader depended on a remote flag, so privacy settings could silently remove project instructions; a later version reportedly changes the fallback.
