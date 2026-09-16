+++
date = '2026-09-16T07:40:00+02:00'
draft = false
title = 'Salesforce launches Koa for CRM agents'
+++

After reading this, the reader knows Salesforce built Koa for CRM tool use, and it matters because enterprise agents need specialized action models.

# Salesforce launches Koa for CRM agents

*The model starts from NVIDIA Nemotron 3 Super and is post-trained on synthetic workflows. Salesforce says no customer data entered its training set.*

Salesforce and NVIDIA announced Koa on September 15, a specialized language model intended to reason through multi-step customer-relationship-management tasks and call software tools inside Agentforce.

In plain terms, Salesforce took a general open-weight model and trained it to follow the structure of business workflows. Koa is meant to do work such as routing a service case or updating a sales opportunity, where the result depends on several actions in the correct order.

## Why it matters

Enterprise agents fail differently from chatbots. A weak sentence is inconvenient; a wrong database update can damage a customer record or trigger another automated process. A model for enterprise action therefore needs to select the right tool, supply valid arguments and maintain state across several turns.

Koa is built on NVIDIA's Nemotron 3 Super 120B foundation model. Salesforce says it generated training scenarios from workflow specifications, personas and expected action sequences. The company used supervised fine-tuning followed by reinforcement learning with Group Relative Policy Optimization, or GRPO, to reward successful tool use.

Salesforce says the training corpus combined public information with synthetic scenarios and contained no customer data. That avoids one direct privacy problem, but it creates another question: whether simulated workflows capture the irregular cases, incomplete records and policy conflicts found in real organizations.

The accompanying paper is more restrained than the launch language. Its authors report that Koa improves on the Nemotron base model, performs best on multi-turn tool use, and beats one proprietary comparison. They also state that it remains below the strongest frontier models.

That limitation matters. Specialization can make a smaller or controllable model competitive on a narrow set of actions without making it generally smarter. The relevant comparison is therefore not “Koa versus every frontier model” but whether Koa completes a defined CRM workflow accurately enough, cheaply enough and within the customer's security boundary.

## Control becomes part of the product

Salesforce says it controls Koa's weights and performs post-training and inference inside its own trust boundary. It also plans to bring Nemotron-based models and accelerated computing to Missionforce, its offering for government and regulated organizations, including private-cloud and isolated deployments.

The published benchmark evidence remains vendor-produced. Salesforce says Koa made three times fewer errors on its CRM benchmark, but the company designed the training process and the evaluation. The paper provides methods and comparative results, yet independent reproduction will be needed before buyers can treat the figure as a general performance claim.

The next useful evidence will come from production: completion rates for full workflows, the frequency and cost of human correction, permission failures, recovery from changed records, and incidents caused by incorrect actions. Koa gives Salesforce a model it can tune and operate directly. It does not remove the need for authorization boundaries, audit logs and human escalation.

## Verification

1. **VERIFIED — Salesforce and NVIDIA announced Koa on September 15, 2026.** Primary source: https://www.salesforce.com/news/press-releases/2026/09/15/koa-reasoning-model/
2. **VERIFIED — Koa post-trains the open-weight Nemotron 3 Super 120B model for tool use and CRM workflows.** Primary sources: https://arxiv.org/abs/2609.15066 and https://www.salesforce.com/news/press-releases/2026/09/15/koa-reasoning-model/
3. **VERIFIED — The authors say training used public and synthetic data, not customer data.** Primary source: https://arxiv.org/abs/2609.15066
4. **VERIFIED — The paper reports gains over the base model and one proprietary baseline while remaining below the strongest frontier models.** This is author-reported benchmark evidence, not independent replication. Primary source: https://arxiv.org/abs/2609.15066
5. **VERIFIED — Salesforce says it controls the weights and keeps post-training and inference inside its trust boundary.** Primary source: https://www.salesforce.com/news/press-releases/2026/09/15/koa-reasoning-model/
6. **PARTIALLY VERIFIED — Salesforce says Koa produces three times fewer CRM-action errors.** The result is documented by the developer on a developer-created benchmark and has not been independently reproduced. Primary source: https://www.salesforce.com/news/press-releases/2026/09/15/koa-reasoning-model/

## Glossary candidates

- CRM
- Tool use
- Open-weight model
- Post-training
- GRPO
- Trust boundary

**Cold-reader sentence:** Salesforce specialized NVIDIA's Nemotron model into Koa, a controlled CRM action model trained on synthetic workflows rather than customer records.

