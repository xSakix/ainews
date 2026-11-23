+++
title = "An Installation Gate for Agent Skills"
description = "ClawVet scans an agent skill and its scripts before installation, then warns when an update gains access to new secrets, hosts or persistence paths. Its benchmarks show that static checks catch many attacks, while prompt injection still needs semantic review."
tags = ["agents", "safety", "tools"]
date = 2026-11-23T03:57:49+01:00
draft = false
+++

The skill looked ordinary in the staging directory. Its Markdown file described a useful shortcut, and a helper script sat beside it. Before the installer could copy either file into the agent’s working set, a separate process opened the bundle, traced a secret from an environment variable to an outbound request and returned a block.

*The scenes that open and close this article are illustrations; the people in them are invented.*

ClawVet is built for that moment. The open-source scanner examines the instructions and code inside an agent skill before installation. It runs offline by default, does not execute the bundle and can enforce its verdict through OpenClaw’s installation policy. It also records the permissions of an allowed version so that a later update cannot quietly add access to credentials or startup files without another prompt.

## Code packaged as instruction

An agent skill is neither a conventional library nor a plain document. Its main file tells a model when to use the skill and what to do. The bundle can also contain scripts, configuration, references and other assets. That combination creates a supply-chain problem with two languages: prose can redirect the agent, while code can act through the user’s account.

ClawVet treats the bundle as both. Its first pass parses the main file, code fences and files that the instructions reference. Static rules then look for remote execution, reverse shells, credential theft, miners, obfuscation and exfiltration. Tree-sitter parsers follow data through Python, JavaScript, TypeScript and shell code without running it. Other passes check undeclared programs and environment variables, risky dependency commands and names that resemble popular skills.

Six of the seven passes are static and local. The optional seventh sends the static findings and coverage gaps to an LLM chosen by the operator. A semantic judge can clear a gap only by quoting the skill, while hard security findings remain floors that the judge cannot lower. The distinction matters because a claim of “AI security scanning” can otherwise hide the fact that source code leaves the machine.

The tool reduces its findings to a score from zero to 100. Scores through 25 receive an A or B and pass. Scores from 26 through 75 produce a warning that stops an unattended installation. Scores from 76 upward block. A known command-and-control address or unreadable content blocks at any threshold.

## Permission changes, not only known patterns

Static signatures work best on an attack that already has a recognisable shape. Updates present a different problem. A useful skill can earn trust, then acquire one extra permission in a later release.

ClawVet therefore extracts capabilities: connected sites, secret environment variables, credential stores, persistence locations and proved high-risk actions. The installation gate stores that record in local state. When a release from the same owner and slug arrives, the gate compares the two. A new secret read, a persistence path or a risky destination changes the verdict to a warning and names the new permission.

That design avoids a common failure in review systems. A reviewer does not need to reread the whole package and remember what the old version could do. The question becomes narrower: why does this update need a password that the previous one never read, or a host that it never contacted?

The comparison has limits. ClawVet recognises literal paths, common placeholders and several forms of command construction, but it is not a general proof of program behaviour. Its documentation says that prose which tells an agent to fetch a page and follow the page’s instructions can escape the static analysis when no file is downloaded. Obfuscated loaders and unsupported runtime behaviour can also pass outside the rules. Complete coverage means that the scanner inspected the references it recognised within its file and directory limits; it does not certify safety.

## What the measurements say

The project reports results on a held-out subset of SkillTrustBench v1.1. The benchmark represents skills as bundles with a main instruction file and optional scripts, references, assets and agent definitions. Its 556-case leaderboard subset contains 316 malicious, 74 suspicious and 166 normal examples.

ClawVet’s static gate reached 0.660 accuracy and 0.511 macro F1 on that set. With Claude Haiku 5.5 as the optional semantic judge, accuracy rose to 0.833 and macro F1 to 0.770. Malicious recall reached 0.918. The project compares those figures with published leaderboard results of 0.775 accuracy for Cisco Skill Scanner, 0.712 for NVIDIA SkillSpector and 0.874 for Tencent A.I.G. Because the semantic configurations, prompts and implementation choices can differ, the table is evidence on one dataset rather than a universal ranking.

The gap between static and semantic results is as important as the higher score. Code analysis can prove that a credential flows into a network call. It has more trouble with a natural-language instruction whose harm depends on intent. The project’s update benchmark makes that weakness explicit: on a held-out set, its gate and permission diff stopped 95.2 percent of code-injection changes, but only 36.4 percent of prompt-injection changes.

The same benchmark measured friction. Among benign updates, 34.1 percent still stopped at some point in the combined gate and diff process, although only 5.1 percent prompted specifically because of a permission change. Across 212 unique ClawHub skills, a later ClawVet release reduced hard blocks from 79 to 37 and raised clean allows from 87 to 139. Those figures come from the project’s own corpus and labels.

Older tests show why careful labels matter. A corpus of 500 entries contained 50 skills from one malicious campaign, 400 clean skills and 50 hard negatives. Hard negatives included legitimate SSH helpers that read configuration and installers that used commands which also appear in attacks. A scanner that simply blocks every mention of a credential or shell would look safe while making ordinary work impossible.

## A gate with a defined boundary

ClawVet can run in a browser through WebAssembly, as a command-line scanner, in pre-commit checks or as a GitHub Action. Its stricter role is the installation gate. OpenClaw stages the bundle, sends metadata to the policy process and waits for one JSON verdict before committing the installation. A malformed request or scanner error fails closed.

The project advises users to install the scanner globally instead of invoking a fresh package through `npx`. That recommendation follows its own threat model: a command that fetches the newest registry release at the moment of inspection creates another unreviewed update. A global copy can be updated deliberately, and the npm attestation can be checked first.

The gate does not remove the need to inspect sensitive agent extensions. It turns that inspection into a mandatory step and leaves an auditable reason when the step stops an install. Its published limits also make the remaining choice visible: static mode keeps the bundle local and misses more semantic attacks; the optional model review reads intent better but sends selected evidence to a model endpoint.

In the staging directory, the blocked skill remained only a folder. The installer printed the secret that the script tried to read, the destination that would have received it and the rule that stopped the copy. The agent never had a chance to decide that the shortcut looked useful.

## References

- CUHK Zhuque. (2026). *SkillTrustBench*. https://huggingface.co/datasets/cuhk-zhuque/SkillTrustBench
- Shaikh, M. (2026). *ClawVet*. https://github.com/MohibShaikh/clawvet
