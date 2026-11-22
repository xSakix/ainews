+++
title = "Google cut the wait between training clusters"
description = "Google made two groups of TPUs exchange smaller updates while training a 32-billion-parameter model. Step time held under a simulated network constraint, leaving open what the method will cost across real data centres."
tags = ["research", "hardware", "models"]
date = 2026-11-22T06:29:30+01:00
draft = false
+++

Google’s engineers set a bandwidth cap between two groups of TPUs. At 10 gigabits per second, a step of ordinary data-parallel training took 55.11 seconds. The same model took 5.76 seconds per step when the groups exchanged smaller updates in the background.

The experiment, which Google published in November, tested Qwen3-32B on two TPU v5p-32 slices. The slices sat on a fast network. The team used Linux traffic control to simulate the kind of limited bandwidth that can separate two groups of accelerators. That design let it hold the hardware and model constant while changing how much data could cross the link.

## When the link sets the pace

In standard data-parallel training, each group gets a copy of the model and a different batch of training examples. After calculating gradients, which indicate how to change the model’s parameters, the groups combine them so that the copies stay in step. On a fast network, some of that exchange can overlap with computation. Once it takes longer than the computation that can hide it, the accelerators have to wait.

Google estimates that its data-parallel setup exchanged about 65.5 gigabytes across the link every step. When the link ran at full speed, the baseline needed about 5.6 seconds per step. At 30 gigabits per second, it needed 19.41 seconds. The model and the amount of work per step stayed the same. Most of the extra time went into getting the updates across.

This is the problem that Arthur Douillard and his colleagues set out to address with the original DiLoCo work. In their study of language model training on C4, the researchers had eight groups train independently for stretches and bring their updates together periodically. They reported matching fully synchronous training while exchanging 500 times less data in that particular experiment. The study used a different setup from the new MaxText benchmark, so the two traffic reductions measure different things.

## Changing when the updates travel

Original DiLoCo still had a problem at the end of each stretch. The cheaper steps ran at full speed, then the groups had to synchronise the whole model at once. At the 10-gigabit cap in Google’s new benchmark, ordinary DiLoCo averaged 7.55 seconds a step and still had a periodic pause. For a training system that stays busy most of the time, a pause at regular intervals can account for a sizeable part of the average.

The 2025 Streaming DiLoCo paper changed the schedule. Instead of sending the whole model in one operation, the groups exchange pieces in sequence. The next training steps can proceed while the transfer is in progress. The paper also explored quantising the exchanged data, which reduces the number of bits needed to represent it. The underlying distinction is between the amount of data a system sends over a run and how much it tries to send at once.

In the MaxText experiment, the team divided Qwen3-32B into 65 fragments. A group could train while host CPUs synchronised about one gigabyte of data for a fragment in the background. Across 65 steps, traffic between the slices fell from 4,258.8 gigabytes with standard data parallelism to 67 gigabytes with Streaming DiLoCo. Average step time stayed at 5.76 seconds at both 30 and 10 gigabits per second. With no bandwidth restriction, all three methods finished steps in roughly the same time.

## The experiment measured more than traffic

A model that spends less time waiting can still be worse at the end of training. Letting workers update independently changes the sequence of weights that each worker sees. Google singled out models with a mixture of experts, where a router decides which parts of the model process each token. If routers learn independently for too long, they may learn to send similar examples to different experts.

The MaxText team compared validation loss on runs of 4,000 steps for two such models, Qwen3-30B-A3B and Gemma4-26B-A4B. It reports that the streaming runs matched or slightly improved on the synchronous baseline. In the Qwen run, the team adjusted synchronisation during the first roughly 800 steps. The result tracks how well the runs predicted held-out data over the tested period. It leaves open how much tuning other models and longer runs would require.

For teams that have to secure capacity across locations, there are two separate questions. One is whether the training job can keep computing while updates travel. The other is what it costs to reach a required level of quality when the network has real latency, failures and traffic that the experiment did not reproduce. The throughput comparison used one dense model and two groups of accelerators. The quality runs answer a different question over a limited number of steps. Google gives no cost comparison or time-to-target-loss measurement for real sites.

The engineers had started by putting a cap on a link that could otherwise carry the traffic. With the cap on, they watched ordinary data parallelism spend nearly 50 extra seconds per step. Streaming DiLoCo finished a step in nearly the same time with the cap on as with it off.

## References

- Douillard, A., Feng, Q., Rusu, A. A., et al. (2023). *DiLoCo: Distributed Low-Communication Training of Language Models*. https://arxiv.org/abs/2311.08105
- Douillard, A., Donchev, Y., Rush, K., et al. (2025). *Streaming DiLoCo with overlapping communication: Towards a Distributed Free Lunch*. https://arxiv.org/abs/2501.18512
- Khatwani, M., Zuo, C., Fallen, N., et al. (2026). *Distributed LLM Training Across Metros: Streaming DiLoCo in MaxText*. https://developers.googleblog.com/distributed-llm-training-across-metros-streaming-diloco-in-maxtext/
