+++
title = "Better Leads Went to Humans, and They Closed Fewer"
description = "A preprint on a Chinese insurance brokerage finds that after an AI voice agent took the weakest sales leads, human agents got far better ones early in the day, yet closed fewer of them. The authors blame what the agents expected to come next, and warn that routing work to AI changes how people treat the work left."
tags = ["research", "business"]
date = 2026-10-20T03:12:18+02:00
draft = false
+++

The woman in this scene does not exist. She is a sketch built from the rules of a real call centre, and everything she does is something its rules allow. It is nine in the morning at an online insurance brokerage, and her headset clicks. The system hands her the first lead of the day without asking. It is a man who got as far as the payment screen the night before, then closed the page. She can work him, or she can send him back to the shared queue for someone else. She would earn nothing if a colleague sold him the policy, and the queue holds a dozen more like him.

She sends him back. It will not count against her.

## What the brokerage changed

The call centre is real, though its name is not. The authors of a new preprint call it Platform X, a pseudonym kept under a non-disclosure agreement. It is a licensed online brokerage, founded in 2017, that sells health, critical-illness, accident and life policies for dozens of insurers. Its agents phone people who abandoned a purchase partway through, roughly ten thousand calls on a working day in the sample studied. A customer who reached the payment screen is a hot lead. One who left earlier is a cold lead.

Until 2024, hot and cold leads sat in one queue, and the system gave the next lead to whichever agent was free. On 28 August 2024 the firm changed the routing. An AI voice agent, which had been calling in the evenings since December 2023 and in a backup role by day since June 2024, now took cold leads by default. Humans kept priority on hot ones. The AI's share of cold leads rose from under 25 percent to above 60. Management's reasoning, as the paper reports it, was plain: an AI that costs almost nothing per call can work leads that were often unprofitable for people, and humans are freed for the leads that pay.

The paper, by Xinyu Fu, Shulong Luo, Narayan Ramasubbu, Peng Shen, Xincheng Wang and Yucheng Wang, has not been peer reviewed and rests on this one firm. Its design is a regression discontinuity in time: it compares calls in the 60 days before the switch with the 60 days after, 409,622 handled by humans and 157,468 by the AI, across about 13,000 agent-days. The authors say pay, scripts, training, evaluation and hiring did not change, and that the number of calls per agent-day did not jump at the cutoff.

## Better work, worse results

The routing did what management wanted. On an agent's first three calls of the day, the chance that the lead was hot rose by 23.4 percentage points. The gain faded through the shift and reached zero in the final calls.

Conversion moved the other way. On those first three calls, the share of leads that agents closed fell by 4.5 percentage points, and by 2.5 on the next three. In the middle of the day it was unchanged, and at the very end it rose by 3.4 points. Sales fell most where the leads improved most.

Agents did two things differently, according to the authors. They sent the lead back to the queue more often, by 8.1 percentage points on the first three calls, and on calls they kept they spoke for about 13 percent less time. Agents earn a modest base salary plus commission that makes up most of their take-home pay, and returning a lead carried no penalty and did not enter their evaluations. Neither the commission rates nor the reward for a sale changed.

## The theory of the next lead

Earlier accounts of AI at work, as the authors summarise them, expect gains from sorting tasks between people and machines by comparative advantage, as Acemoglu and Restrepo argued in 2019, or from AI that helps the worker, as in the customer-support study by Brynjolfsson, Li and Raymond. Neither predicts that handing humans better work would lower their results. The authors turn instead to an idea from the economics of job search, in which a searcher compares what is in hand with what is likely to turn up. Stigler wrote about the economics of information in 1961, McCall about search in 1970, and Lippman and McCall surveyed the field in 1976. Applied to the call centre, the logic is that an agent who expects a good lead next is less willing to labour over a mediocre one now. The AI had raised the agent's expectations of the whole queue. The effect should be strongest early in the day, when many leads remain, and it was.

The authors also tested rivals. One was that agents simply slowed down, with longer gaps between calls. They report no such gap at the early positions. Others covered shifts in the mix of customers and in the workforce, and learning on the job. They find the reservation-value account fits best, with a caveat of their own: the reallocation and call-length measures explain only a modest share of the drop in conversion, so the "conduct" effect is better read as everything agents did differently, not as proof of those two behaviours alone.

## Counting what was gained

The accounting is where the paper turns uncomfortable. In the authors' model, the better ordering of hot leads lifts the yield on them by 0.58 percent, while the change in conduct cuts it by 17.6 percent, about thirty times as much. Conversion on hot leads fell from 4.4 to 3.7 percent. Across all human calls it fell from 3.2 to 2.9. The authors summarise the day-level effect on human performance as close to zero, set against that fall on the hot leads themselves.

The firm's totals look better than they are. Humans made 31.8 percent fewer calls after the switch, and the AI made about four and a half times as many. Conversions per 50 human calls rose 6.3 percent, but the paper says this comes from reassigning volume, since the denominator shrank faster than the numerator. Per day, humans lost 50.5 hot-lead conversions and the AI recovered 7.7 on cold leads, a ratio of about seven to one. These are the authors' calculations on their own data, and they put the pattern down to the routing rather than a verdict on the firm's decision.

The authors do not conclude that firms should hand humans worse work or take the AI out. They suggest staggering the release of hot leads through the day, or mixing in lower-value work, so that the agent's next call does not look so much better than the one in hand. In their model, restoring the pre-expansion rhythm of hot leads would raise conversions per call by about 13.5 percent, with an interval of 10.5 to 16.6. That figure comes from a calibration, not an experiment, and the authors list the open questions themselves: whether the effect holds with a thin queue, in claims processing or content moderation, or where workers cannot return tasks.

## The ordinary morning

Back to the sketch of the woman at her desk, still invented. By ten she has returned four leads and kept two, and both calls ended sooner than she would have let them a year ago. In the sketch she does not feel lazy. She feels she is waiting for the good one, because the last hour has shown her how many there are. The paper cannot say what any agent was thinking. It can say only that, across the calls it measured, the best leads of the day were the ones most easily let go.

## References

- Acemoglu, D., & Restrepo, P. (2019). Artificial intelligence, automation, and work. In A. Agrawal, J. Gans, & A. Goldfarb (Eds.), *The Economics of Artificial Intelligence: An Agenda* (pp. 197-236). University of Chicago Press.
- Brynjolfsson, E., Li, D., & Raymond, L. (2025). *Generative AI at Work*. Quarterly Journal of Economics, 140(2), 889-942.
- Fu, X., Luo, S., Ramasubbu, N., Shen, P., Wang, X., & Wang, Y. (2026). *When Better Opportunities Backfire: Service Worker Responses to Parallel AI Deployment in Customer Acquisition*. https://arxiv.org/abs/2610.25603
- Lippman, S. A., & McCall, J. J. (1976). *The Economics of Job Search: A Survey*. Economic Inquiry, 14(2), 155-189.
- McCall, J. J. (1970). *Economics of Information and Job Search*. Quarterly Journal of Economics, 84(1), 113-126.
- Stigler, G. J. (1961). *The Economics of Information*. Journal of Political Economy, 69(3), 213-225.
