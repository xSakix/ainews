+++
title = "METR finds Anthropic's progress doubled in pace; key proof is redacted"
description = "After eleven weeks inside Anthropic, the evaluator METR concludes that the company is improving its models at about twice its earlier rate, mostly because it uses AI to do the research. Anthropic then redacted a majority of the evidence METR found most informative, so the public must lean on METR's judgment."
tags = ["safety", "research", "policy"]
date = 2026-11-06T03:19:59+01:00
draft = false
+++

For eleven weeks, from 12 August to 29 October, a team of METR researchers worked on laptops that belonged to the company they were judging. They were 2.5 full-time equivalents, a small crew, and they logged into Anthropic's systems on Anthropic's devices, for security reasons. Anthropic gave them free tokens, which they spent on AI-assisted data analysis, and METR took no payment. They asked for data on every stage of how a model is made, and mostly got it within days. Then they wrote up what they had seen, and Anthropic decided which parts of it the public could read.

The result appeared on 5 November. METR, a nonprofit that evaluates frontier AI, says that as of October 2026 Anthropic is probably improving its models on well-specified tasks at about twice the rate it managed between March 2024 and October 2025. It attributes most of that to Anthropic's own use of AI in research. It also says Anthropic redacted "a majority of the evidence we found most informative for these conclusions". The report is thus both a measurement and a statement about what outsiders are allowed to measure.

## What METR measured

The headline number comes from Anthropic's version of the Epoch Capabilities Index, a composite of benchmark scores that METR calls AECI. Since October 2025, METR estimates, the scores of Anthropic's models have grown at 1.9 times their earlier rate, with a 95 per cent interval of 1.5 to 2.8. In METR's terms, Anthropic made in the past year about as much benchmark progress as in the two years from October 2023 to October 2025. A system card for Haiku 5.5 reported 1.7 times; METR's figure is higher mainly because it includes newer models that have not been released. Under different choices about which benchmarks and models to include, the estimate moved between 1.1 and 2.9.

METR is careful about what this does and does not show. The 1.9 figure could be an artefact of overfitting to the benchmark mix, and benchmark points lag the research that produces them. Its overall judgment, that progress on well-specified tasks runs near twice the old pace, rests on more than AECI, including redacted material. Most of the team, it says, lean that way, with "significant uncertainty and internal disagreements"; a true value of 1.3 or 3 times would not surprise them.

The cause matters as much as the size. METR says it received "convincing evidence" that the acceleration did not come from faster growth in training compute, though the details were redacted. Its guess is that perhaps 80 per cent of the current acceleration is due to AI, while the faster pace in late 2025 was likely influenced by other factors. The supporting evidence is partly soft. Interviews with researchers centred on a doubling of their own area's pace. Slack polls, in which staff vote with emoji reactions on the speedup they get from the latest model, reached 12 times in October 2026 for the most capable internal model, which METR treats as very loose evidence because the answers reflect low-effort consideration. Business Insider, reporting on the study, quotes one researcher telling METR that they are now "only bottlenecked on ideas & compute, no longer bottlenecked on code".

METR was told that the speedup comes mostly from AI assistance rather than autonomous work, though researchers described "signs of life" suggesting that autonomous contributions could arrive soon. It found no convincing bottleneck in algorithms, compute or data over the next twelve months, and says its view on bottlenecks changed several times during the study, so it holds that finding with little confidence. Its warning is that acceleration could compound.

## The redactions

Anthropic held unilateral redaction rights over everything non-public. METR kept the right to say that redactions were made and whether its findings depended on them. A table in the report lists seven kinds of evidence. Benchmark capabilities of internal models were shared and are described. Key intermediate measures, algorithmic progress estimates and measurements of research inputs were shared, mostly or fully, and are not described. Details of bottlenecks and forecasts were shared in part and are not described. Evidence of AI's contribution and staff interviews are described in part. Anthropic called the redactions "aimed at removing confidential information that could accelerate other AI developers."

METR's own verdict on its report is blunt: it "does not achieve 'transparency about evidence'", and "the public has to rely on METR's judgment much more than would be ideal, given the weight of the questions answered here." It also lists pressures on itself. Critical remarks about redactions might make other companies, or Anthropic, less willing to grant access in future. Anthropic's feedback on clarity, METR says, was in some cases "overly forceful", though it does not think the final text is significantly distorted. One team member had discussed a job at Anthropic, received an offer and declined it, and held equity in a competitor as a former employee, so a colleague checked all of that person's work. None of the team holds Anthropic equity, though one incoming staff member does.

This engagement is separate from the one Anthropic announced on 15 October, when it said it had given "employee-like access" to a team of six METR employees and listed freedom to publish among the things evaluators need. METR says the work it reports began in mid-August and did not involve unmediated access to data, documents or models.

## The risk report that METR reread

The second METR document goes back to July. Anthropic's August Risk Report said that models in use inside the company on 15 July had not crossed the early-warning threshold in its Responsible Scaling Policy for automated research, which includes a "dramatic acceleration" of progress for reasons tied to automating AI R&D. METR agrees that catastrophic risk from those models was low. It does not agree that the threshold clearly stayed uncrossed.

METR points to the phrase that the leading indicators showed acceleration "by less than a factor of 2". In the private version of the report, the figures imply 1.97, a number METR computed itself from two estimates in the private text. In its view a reader would take "less than a factor of 2" to mean meaningfully below two, and "around 2" would be more accurate. METR's own range for those indicators is 1.3 to 2.8. Both METR's researchers and Anthropic's staff lean toward the threshold not having been crossed, METR says, but it thinks crossing was plausible and that the public report "understates the level of acceleration that was occurring". Anthropic's report itself admitted lower confidence than in earlier editions, because its most concrete task-based evaluations had saturated.

## What came before

The assessment lands three days after Anthropic's amended registration statement, filed on 2 November. In it the company says that "our internal estimates and our expectations regarding future models, rather than our current models, indicate that we may imminently meet our Responsible Scaling Policy's definition of 'dramatically accelerated progress attributable to AI.'" It adds that it has not designated any current model as exceeding the threshold and that it has in the past "not identified, and may in the future not identify, a significant acceleration in our rate of development until after it has occurred." Business Insider adds a detail from METR's report: in the previous six months, Anthropic finished training three models that are not available to the public. The models that Anthropic's own researchers use to speed up their work are, in part, models that customers cannot yet use.

## Who can check the claim

Anthropic's case for the arrangement is that it cannot publish everything. In its October post, the company says some information could help malicious actors or is commercially sensitive, and compares evaluators to bank supervisors who sit inside the largest banks. METR's report shows both the value and the limit of that model. A third party looked at the real internal numbers, and its answer is less comfortable than the company's public text. The same party cannot show the public the numbers that carry its conclusions.

Imagine, for a moment, an analyst at a government office, invented for this closing, who has been asked whether frontier labs are being supervised. She opens METR's report and finds the table of seven kinds of evidence, four of them marked "No" under the public results. She can read an estimate of 1.9 with an interval of 1.5 to 2.8, and a plain statement that the underlying material was withheld. What she writes in her memo, "independent" or "partly independent", is a matter of wording. METR's text leaves that choice to her.

## References

- Anthropic. (2026). *An update on independent evaluators*. https://www.anthropic.com/news/an-update-on-independent-evaluators
- Anthropic PBC. (2026). *Amendment No. 1 to Form S-1 registration statement*. https://www.sec.gov/Archives/edgar/data/2130357/000162828026068676/anthropicpbc-sx1ax1.htm
- Coxon, J. (2026). *3 takeaways from the big AI report on Anthropic everyone is talking about*. Business Insider. https://www.businessinsider.com/anthropic-metr-ai-researchers-report-productivity-recursive-self-improvement-2026-11
- Epoch AI. (2026). *Epoch Capabilities Index (ECI)*. https://epoch.ai/eci
- METR. (2026). *METR's assessment of AI R&D acceleration at Anthropic*. https://metr.org/blog/2026-11-05-anthropic-ai-rd-acceleration-assessment/
- METR. (2026). *Review of the AI R&D section of Anthropic's August 2026 Risk Report*. https://metr.org/blog/2026-11-05-rd-section-anthropic-risk-report-august-2026-review/
