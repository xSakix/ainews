+++
title = "Apple plans tighter consent for Full Disk Access"
description = "Apple says macOS will require more explicit action before apps receive broad access to personal data, citing increasingly autonomous AI agents."
tags = ["safety", "agents", "tools"]
date = 2026-10-03T05:19:20+02:00
draft = false
+++

Apple announced on 2 October that it will strengthen the process for granting Full Disk Access on macOS, warning that increasingly autonomous AI agents make this broad permission more consequential.

Full Disk Access lets an application reach data normally protected by separate privacy controls. Apple says the permission helps backup software work, but some developers use it in ways that expose files, email, messages and browsing history without users understanding the extent of access.

**Why it matters:** Developers of local AI assistants will face a more explicit consent step when requesting this permission. People exchanging messages with an app’s user also have privacy at stake: their communications can be included in the data the app reaches.

Apple’s [developer notice](https://developer.apple.com/news/?id=p6zjojqw) promises additional controls but gives no release date, macOS version or technical specification. It describes a forthcoming change, rather than a protection already available in a software update.

The announcement follows a dispute about Meta’s Muse assistant. [Ars Technica reports](https://arstechnica.com/security/2026/10/apple-changes-full-disk-access-permissions-to-curb-abuse-from-ai-agents/) that columnist Jason Aten said Muse referenced an Apple Messages exchange he believed it could not read. Meta maintains that its Messages integration requires both system-level Full Disk Access and an enabled connector inside Muse.

Security researcher Patrick Wardle told Ars that the system permission itself allows software to read message data and other accessible files. That distinguishes the operating system’s grant from an application’s own promise about when it will use the grant.

Apple names no developer in its notice. The next concrete information is the control it ships and the action it requires from users.

## Verification

| Claim | Label | Primary source | Independent check |
|---|---|---|---|
| Apple’s 2 October notice promises controls without implementation details. | VERIFIED | [Apple notice](https://developer.apple.com/news/?id=p6zjojqw) | [Ars reporting](https://arstechnica.com/security/2026/10/apple-changes-full-disk-access-permissions-to-curb-abuse-from-ai-agents/) |
| Apple attributes greater privacy risk to broad access and autonomous agents. | VENDOR-REPORTED | [Apple notice](https://developer.apple.com/news/?id=p6zjojqw) | none |
| Aten described unexpected Messages access; Meta says its integration requires both permissions. | PARTIALLY VERIFIED | [Statements reported by Ars](https://arstechnica.com/security/2026/10/apple-changes-full-disk-access-permissions-to-curb-abuse-from-ai-agents/) | Incident not independently reproduced |
| Wardle distinguishes broad operating-system access from the application’s connector setting. | PARTIALLY VERIFIED | [Wardle interview in Ars](https://arstechnica.com/security/2026/10/apple-changes-full-disk-access-permissions-to-curb-abuse-from-ai-agents/) | none |
