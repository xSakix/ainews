+++
date = '2025-08-25T06:30:00+02:00'
draft = false
title = 'The Quiet Giant: A New AI Model from China Offers Unrivaled Power and Unsettling Risks'
+++

**A new artificial intelligence model from a Chinese startup arrived in August 2025, not with a massive publicity campaign, but with a quiet release to the developer community. The model, DeepSeek-V3.1, shows performance competitive with the most advanced proprietary systems from Western tech giants, but at a fraction of the cost. Its open-source license marks a significant shift, offering broad access. This combination of power, price, and access has the potential to reshape the AI industry, but it comes with a significant trade-off: profound risks related to data privacy, censorship, and geopolitical influence.**

This is Modra. The AI startup, DeepSeek AI, let the model’s performance serve as its own marketing. The strategy worked.

DeepSeek-V3.1 is a successor to two previous versions, merging a general-purpose AI with a reasoning-focused one into a single, unified system. Its architecture is a novel hybrid. A "non-thinking" mode provides fast, direct answers for simple conversation. For more complex tasks, a "thinking" mode engages a slower, deliberate chain-of-thought process, breaking down problems into steps before offering a solution. This allows a user to balance speed against analytical depth.

At its core, DeepSeek-V3.1 is built on a Mixture-of-Experts design. It holds a massive 671 billion parameters in total but activates only a fraction—about 37 billion—for any given task. This is the engine of its efficiency. It allows the model to command a vast reserve of knowledge without the immense computational costs of a similarly sized dense model. This innovation directly challenges the established trade-off between performance and operational cost.

### Performance at a Price

The results are potent. On several key benchmarks, the model showed highly competitive performance, especially in coding and reasoning. Vendor-reported benchmarks show its thinking mode scoring 76.3% on one programming test, ahead of some published scores for Anthropic's Claude Sonnet 4. On another benchmark measuring the ability to fix software issues, its agentic mode scored slightly higher than Google's Gemini 2.5 Pro, though such cross-lab comparisons require caution.

This performance is delivered at a substantially lower cost. Compared to major proprietary models, DeepSeek’s API can be more than 75% cheaper on input tokens and nearly 90% cheaper on output tokens.

The model is accessible through an API compatible with existing OpenAI tools, which simplifies adoption. But its true disruption lies in its license. Released under a permissive MIT license—a shift from the custom licenses of its predecessors—the model’s code and weights are freely available for anyone to download, modify, and use for commercial purposes without restriction. This allows organizations to run the model on their own servers, maintaining complete control over their data.

### A Question of Trust

This power and access, however, come with significant risks. The company’s privacy policy states that inputs from its API and services may be used to “train and improve” its technology, and the policy lacks a clear, user-facing opt-out mechanism. The policy also confirms that data is processed and stored in China. For European organizations, this raises significant compliance hurdles regarding international data transfer regulations.

The model also demonstrates clear ideological biases. The online version refuses to answer questions on politically sensitive topics related to China, such as Tiananmen Square. While self-hosting the model removes the company's application-level filters, refusal patterns can still exist within the model's weights.

Furthermore, DeepSeek’s terms of service place all legal responsibility for the model's output on the user. Unlike some Western competitors who offer copyright indemnities to paying customers, DeepSeek provides no such protection if the model generates content that infringes on intellectual property.

DeepSeek-V3.1 presents a stark choice. It offers elite performance at a radically lower cost, with the transparency and freedom of open source. It could democratize access to powerful AI and reshape the industry's economics. Yet its adoption requires a careful weighing of profound risks to data privacy, intellectual neutrality, and legal standing. The quiet launch from Beijing has created a loud and complex challenge for the rest of the world.

{{< substack >}}
