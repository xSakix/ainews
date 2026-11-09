+++
title = "Student codebases tripled, and the comments did not"
description = "A ten-semester study of 260 capstone team repositories finds that end-of-semester code grew from about 3.4 to about 10 thousand lines once generative AI was widely available, while comment density stayed flat. The authors never observed AI use, so the result is a warning for graders and employers, not a verdict on the tools."
tags = ["research", "tools"]
date = 2026-11-09T03:16:01+01:00
draft = false
+++

Picture a course coordinator on the Friday before marks are due. She has a spreadsheet of forty-odd student teams and a habit she has kept for years: open the repository, look at how much was built and how steadily, and let that guide her sense of who worked. This year the first repository on her list holds ten thousand lines of code and three hundred commits. She scrolls through a function with deeply nested branches and finds no comment explaining any of them. The coordinator is invented, a stand-in for a problem that three researchers have now measured.

The study, "Code, Commits, and Complexity in the GenAI Era", was posted to arXiv on 5 November and accepted for the SIGCSE Technical Symposium in February 2027. Its authors are Asma Shakil and Paul Denny of the University of Auckland and Claus Brabrand of the IT University of Copenhagen. They analysed 260 team repositories from a compulsory final-year capstone course, spread over ten semesters from 2021 to 2025. End-of-semester codebases grew from a median of about 3.4 thousand lines in 2021 to 2023 to about 10 thousand in 2024 and 2025. The authors did not observe anyone using AI, and they say so repeatedly.

## One course, ten semesters

In the course, teams of five or six students build software for real external clients over thirteen weeks. The working prototype is the main thing assessed. The repositories come from the course's GitHub organisation: 302 at first, 260 after the authors removed empty, template and duplicate ones. The cohorts hold 19, 65, 57, 51 and 68 repositories for 2021 through 2025.

The authors measure each repository twice, at the mid-semester demonstration in week 7 and at the final presentation in week 13. They count lines of code with the tool tokei, mean cyclomatic complexity per function with lizard, and a lexical count of error-handling constructs. They also count commits. For each metric they test whether it rises or falls steadily across the five cohorts, correcting for the number of metrics tested.

They split the years into a period of lower and a period of higher generative AI availability, using ChatGPT's release in November 2022 as an approximate boundary. They stress that it is not sharp. GitHub Copilot became free for verified students in June 2022, and uptake afterwards was gradual. They cite a Higher Education Policy Institute survey in which the share of UK undergraduates using generative AI for assessed work rose from 53% in late 2023 to 88% in late 2024.

## What changed, and when

The median final codebase was 2.3 thousand lines in 2021, 3.7 in 2022 and 3.4 in 2023. It then jumped to 7.7 in 2024 and 11 in 2025. The mid-semester snapshot follows the same shape, from 1.4 to 1.8 thousand lines before 2024 to 4.8 thousand in 2025. The 2023 cohort, the first after ChatGPT, looks like the earlier ones, and the authors call it transitional.

Median commits per repository went from 63 in 2021 and about 100 to 112 in 2022 and 2023 to 265 in 2024 and 300 in 2025. Commits per active day rose from 3.3 to 5.4. The size of each commit barely moved: the median stayed between 38 and 65 changed lines. That cuts against a common expectation that AI-written code arrives in a few large batches. These students committed more often, in pieces about as big as before.

The most pointed result concerns what sits inside the code. Mean cyclomatic complexity rose from 1.7 in 2021 to 2.5 in 2025, and error-handling constructs per thousand lines rose from 3.7 and 4.8 in 2022 and 2023 to 12 and 13 in 2024 and 2025. Comment density, the share of lines that are comments, showed no clear trend; it was 9.2% in 2021 and 8.4% in 2025. The authors name this pattern "complexity without commentary". Later cohorts handed in code that was larger and more intricate but no better explained.

## What the authors will not claim

Shakil, Brabrand and Denny list the limits plainly. They did not observe AI use, so they report changes that coincide with greater availability, not effects. Staff, assessment criteria and project types changed over the years, the 2021 cohort and part of 2022 worked partly under COVID-19 restrictions, and the 2021 cohort has only 19 repositories. Frameworks and project templates can add boilerplate on their own. The language mix shifted toward JavaScript and TypeScript, which led from 42 to 58% of repositories in 2021 to 2023 to 71 to 74% in 2024 and 2025; restricted to the 157 repositories in those languages, all five significant trends still hold.

The metrics are proxies. The error-handling count is lexical, and cyclomatic complexity, the authors write, "relates weakly to how hard code is to understand". Because it comes from a different tool than the comment count, they ask that the complexity-without-commentary finding be read at the level of cohorts. Everything comes from one course at one institution.

## Where it sits among the evidence

The paper extends earlier work. Y. Zhang and colleagues, in a preprint from January 2026, followed an unchanged cloud-computing assignment across five semesters before ChatGPT and five after. Final submissions got longer, edits between submissions grew, and score improvement per edit shrank. The Auckland team finds a similar growth in size over a longer, team-based project, though without the same pattern in commit size.

Two other studies frame what the growth might mean. S. Peng and colleagues found in a 2023 controlled experiment that developers using GitHub Copilot finished an HTTP server task 55.8% faster. A 2026 randomised study by J. H. Shen and A. Tamkin found that developers learning a new asynchronous programming library with AI help showed worse conceptual understanding, code reading and debugging, without significant average speed gains. The Auckland authors cite that result to sharpen their concern: they write that the concern is that the extra code may be harder to inspect, and that heavy reliance on AI can impair the skills needed to review it.

For teachers the practical conclusion is about measurement. Code volume and commit counts, which an instructor might once have read as effort, have risen sharply, and a larger, more frequently committed codebase is no longer evidence of more learning. The authors suggest viva-style defences, code walkthroughs and explicit documentation requirements. Employers who read a graduate's repositories as a portfolio face the same problem.

Now imagine the coordinator again, a week later, in a room with one team. She does not open the repository. She asks a student to pick any function and explain why it branches the way it does. The invented student reads it slowly, then admits she has not seen it before. Whether the code came from a tool, a teammate or her own late night, the exchange tells the coordinator what the line count could not.

## References

- Azeem, S., Naveed, M. S., Sajid, M., & Ali, I. (2025). *AI vs. human programmers: complexity and performance in code generation*. VAWKUM Transactions on Computer Sciences, 13(1), 201-216.
- Freeman, J. (2025). *Student generative AI survey 2025*. Higher Education Policy Institute, HEPI Policy Note 61.
- Peng, S., Kalliamvakou, E., Cihon, P., & Demirer, M. (2023). *The Impact of AI on Developer Productivity: Evidence from GitHub Copilot*. https://arxiv.org/abs/2302.06590
- Shakil, A., Brabrand, C., & Denny, P. (2026). *Code, Commits, and Complexity in the GenAI Era: A Longitudinal Study of Team-Based Capstone Projects*. https://arxiv.org/abs/2611.07297
- Shen, J. H., & Tamkin, A. (2026). *How AI Impacts Skill Formation*. https://arxiv.org/abs/2601.20245
- Zhang, Y., Savelka, J., Goldstein, S., & Conway, M. (2026). *Changes in Coding Behavior and Performance Since the Introduction of LLMs*. https://arxiv.org/abs/2601.11835
