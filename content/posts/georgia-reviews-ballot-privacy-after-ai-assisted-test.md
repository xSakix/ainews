+++
title = "Georgia reviews ballot privacy after AI-assisted test"
description = "An emergency election-board meeting addressed a privacy weakness investigated by Princeton researcher Max Springer. Recovering ballot order and identifying voters are different results."
tags = ["policy", "safety", "agents"]
date = 2026-10-03T05:18:20+02:00
draft = false
+++

Georgia’s election board met on 1 October to address a ballot-privacy weakness examined with AI coding tools, The Guardian reported on 2 October.

Max Springer, a postdoctoral researcher at Princeton’s Center for Information Technology Policy, described the underlying experiment in August. He used an agent that writes and runs code to analyse public records from Georgia’s May primary election, applying a previously disclosed weakness in ballot anonymisation.

**Why it matters:** An election administrator releasing records needs to preserve public scrutiny without exposing how an individual voted. The state’s response addresses that tension: information useful for checking the count can also connect a ballot to its owner when combined with other records.

Springer reported recovering the casting order of roughly 99% of in-person ballots in the counties where reconstruction worked. That figure measures recovered order, not identified voters. His analysis covered 139 counties, with order reconstruction successful in 114.

Public voting lists and ballot records alone produced unique matches for about 1% of the early in-person voters analysed, he wrote. More precise matching required additional scanner audit logs and voter check-in records; the distinction limits how the statewide result can be interpreted.

Ballot records omit voters’ names, but their identifiers were intended to obscure the sequence in which ballots entered a scanner. Springer described an algorithm whose apparent randomness could be reversed. Combining the recovered sequence with other records created the privacy risk.

Springer said the agent built his analysis pipeline within hours using a $20 subscription. He applied an existing disclosure rather than discovering a new vulnerability, and presented the experiment as a warning about the speed of exploitation.

Brad Raffensperger, Georgia’s secretary of state, ordered ballot identifiers removed from publicly released tabulation data, according to The Guardian. The board also debated changing ballot handling before early voting.

## Verification

| Claim | Label | Primary source | Independent check |
|---|---|---|---|
| Georgia’s board met on 1 October; Raffensperger ordered public-release identifier redaction; ballot-handling changes were debated. | PARTIALLY VERIFIED | https://www.theguardian.com/us-news/2026/oct/02/midterms-ai-ballot-privacy | Guardian reporting and attributed official statements; meeting record unavailable. |
| Springer’s August 3 account concerns the May 2026 primary and an existing anonymisation vulnerability, using a coding agent and public records. | VERIFIED | https://blog.citp.princeton.edu/2026/08/03/an-algorithmic-failure-beneath-the-secret-ballot/ | none |
| Springer reports recovered order for 1.52 million ballots, 98.9% of in-person ballots in the 114 of 139 counties where reconstruction succeeded. This is not a statewide voter-identification rate. | VENDOR-REPORTED | https://blog.citp.princeton.edu/2026/08/03/an-algorithmic-failure-beneath-the-secret-ballot/ | none |
| Public files alone yielded unique matches for approximately 1% of early in-person voters analysed; further matching used scanner audit and check-in records. | VENDOR-REPORTED | https://blog.citp.princeton.edu/2026/08/03/an-algorithmic-failure-beneath-the-secret-ballot/ | none |
| Identifiers’ reversible ordering creates a privacy risk when combined with other records; Springer reports hours of work with a $20 coding-agent subscription. | VENDOR-REPORTED | https://blog.citp.princeton.edu/2026/08/03/an-algorithmic-failure-beneath-the-secret-ballot/ | none |
| Election administrators face competing requirements for public scrutiny and voter privacy. | ANALYSIS | https://blog.citp.princeton.edu/2026/08/03/an-algorithmic-failure-beneath-the-secret-ballot/ | none |
