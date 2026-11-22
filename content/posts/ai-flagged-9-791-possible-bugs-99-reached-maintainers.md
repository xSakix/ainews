+++
title = "AI flagged 9,791 possible bugs; 99 reached maintainers"
description = "A GitHub and Microsoft pilot scanned six open-source projects with AI and sent maintainers only what survived triage and hand review. Fifty-five of the 99 reports have been fixed, and the pilot shows who paid for the filtering."
tags = ["safety", "community", "tools"]
date = 2026-11-22T03:14:11+01:00
draft = false
+++

ImageMagick is looked after by two people. In the pilot they received 22 security reports, and one of them looked like a kind they had seen before. Its summary showed that it was not, and it pointed to the exact lines of code. The maintainers pushed a fix in 15 minutes. Normally, an ImageMagick maintainer said afterwards, a security advisory takes "around 30 minutes to 1 hour on average to read, understand, and make a fix".

That is a small saving, told by the people who gained it. It sits at the end of a pipeline that began with something far larger.

## What the pilot did

On 17 November, GitHub's Ashley Wolf and Gregg Cochran described a pilot run with Microsoft on six open-source projects: AutoGPT, Caddy, Express, FastMCP, ImageMagick and Netty. Microsoft's scanning system, Codename MDASH, working with its MAI Cyber model, went through each codebase and suggested fixes for what it found. The results graphic gives the number of possible issues flagged across the six projects as 9,791.

None of those went straight to a maintainer. An AI triage agent built by GitHub Security Lab removed duplicates, checked validity and kept the high-impact bugs. Researchers from Microsoft's FORGE Lab then checked each remaining finding by hand; seven of them spent about two days per project on that work. What reached the maintainers, through GitHub's private vulnerability reporting, was 99 reports, each with a proof of concept and a suggested fix. That is about one report for every hundred raw findings.

The maintainers decided what to fix and when. As of 15 November they had fixed 55 of the reports, and 14 of those fixes were already in a release. Caddy's maintainers fixed all 22 of theirs within a week. AutoGPT's had just shipped a new check, and it was broken; the report landed three days later and pointed at the right line, and they wrote a fix within a day and had it in production in under a week.

## The flood this answers

The pilot responds to something maintainers have described for two years. In a post of 26 January, Daniel Stenberg, who leads curl, announced that the project's bug bounty would stop on 31 January. He wrote that the programme's decline began slowly in the second half of 2024 and "accelerated badly in 2025", with an "explosion in AI slop reports". Before 2025, he said, more than 15 percent of submissions ended up as confirmed vulnerabilities. In 2025 the rate fell below 5 percent: "Not even one in twenty was real."

The bounty had paid more than $100,000 for 87 confirmed vulnerabilities over almost seven years, and Stenberg called it a success until the noise arrived. He ended the payments to remove the incentive to submit "made up lies", and told reporters to use GitHub's private vulnerability reporting, the same channel the pilot used. HackerOne's figures for the past year, which he published, showed curl's inbound volume rising sharply while Ruby, Node and Rails stayed flat or fell slightly. He called the reason a matter for further speculation.

GitHub's post cites Christian Grobmeier, a maintainer of Log4j, on the stakes: the AI defending open source has to be better than the AI attacking it. Its own diagnosis is that AI has made finding potential vulnerabilities "fast and cheap", while fixing them still takes human judgment, and in open source that judgment belongs to maintainers. A Netty maintainer put it in their own words: "Finding vulnerabilities is no longer our bottleneck. Fixing them is the hard part."

## What the filter cost

The pilot's numbers show where the cost went. The model produced thousands of candidates at a price the post does not give. Getting from there to 99 took an AI triage agent and then a team of seven researchers working about two days on each project. GitHub says plainly that "the pilot worked because people did careful work at every step, and that work doesn't scale yet."

So the burden did not vanish; it moved. Before, a maintainer read a scanner's output and decided what was real. In the pilot, a Microsoft team read it first and sent the maintainer only what had passed. GitHub's stated rule for anyone who points an AI at someone else's code follows from that: check every finding against what the project already knows and against its security policy, report it privately, include a suggested fix, and let the maintainers set the pace.

There are reasons to read the result with care, and GitHub gives several of them. Six projects is, in its words, "a small sample". All six are alumni of the GitHub Secure Open Source Fund, which gives each project $10,000 and security training, so they were already close to the company that is now offering them more. The lessons come from what those projects chose to share. The fix rate, 55 of 99, is a count at one date and says nothing about the 44 reports still open or how long they will take. The post also does not say how many of the 9,791 were false, how many were duplicates, or how many real bugs the triage may have discarded.

## Where it goes next

GitHub says it will offer every alumni project AI security scans with findings checked before they are reported, and give alumni GitHub Copilot Max. It will build the pilot's lessons into private vulnerability reporting and security advisories. It adds that maintainers also need to run CI tests on private forks and to have access to cyber-capable models, so that they can test a proof of concept before and after a fix.

The model behind the scans is changing as well. On the day of GitHub's post, Microsoft announced MAI Cyber 2 Flash; the pilot ran on the earlier model. Microsoft says the new one scores 92.3 percent on the CyberGym-E2E benchmark, against 91.5 percent for GPT-6 Astra, at less than 2 percent of the cost per task, on company-run tests that left out 92 of 905 tasks. It will be exclusive to Microsoft's security products, MDASH included, from mid-December. Cheaper scanning means more findings. The pilot's arithmetic says each further hundred of them still needs a person to read it.

The AutoGPT maintainer's remark, printed near the end of GitHub's post, points the same way: features are easier and easier to ship, and in future maintaining software "will probably come down to who cares enough to manage the security." For the ImageMagick team, the pilot came down to 22 reports, one that looked familiar, and a quarter of an hour.

## References

- Microsoft AI. (2026). *Introducing MAI Cyber 2 Flash: Leading security. Lower cost*. https://microsoft.ai/news/introducing-mai-cyber-2-flash/
- Stenberg, D. (2026). *The end of the curl bug-bounty*. https://daniel.haxx.se/blog/2026/01/26/the-end-of-the-curl-bug-bounty/
- Wolf, A., & Cochran, G. (2026). *Maintainers don't need more AI bug reports. They need fixes.* GitHub Blog. https://github.blog/open-source/maintainers/maintainers-dont-need-more-ai-bug-reports-they-need-fixes/
