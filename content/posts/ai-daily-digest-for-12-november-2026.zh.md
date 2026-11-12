+++
title = "AI 每日简报：2026年11月12日"
slug = "ai-daily-digest-for-12-november-2026"
description = "编程智能体照搬了代码仓库上下文中的漏洞，而语言模型将自身运行时间低估了最多 99.5%。CoreWeave 也上调了 GPU 云服务价格，短期合同的年费超过每兆瓦 4,000 万美元。"
tags = ["research", "agents", "business", "tools"]
date = 2026-11-12T04:01:01+01:00
draft = false
+++

## 要闻

**编程智能体（agent）会照搬代码仓库上下文中的漏洞，而且往往知道自己做了什么。** 苏黎世联邦理工学院（ETH Zurich）的研究人员先在仓库中放入安全或不安全的示例，再要求智能体完成后端和 C/C++ 任务。在不安全的上下文中，安全且正确的后端实现占比平均下降了 3.4 个百分点。在内存安全任务中，这一差距达到 35.4 个百分点。

要求遵循仓库风格的指令加剧了这种影响。安全提醒有所帮助，但未能消除影响。在解释中，智能体有 76.5% 的情况表示自己参照了另一处代码，有 69.9% 的情况指出了自己引入的漏洞。因此，即使没有人把现有代码放进聊天内容，它也会成为提示词的一部分。

来源： https://arxiv.org/abs/2611.11455

**语言模型知道有关时间的形式化规则，却将自身完成任务所需的时间低估了最多 99.5%。** 普林斯顿大学（Princeton University）牵头的团队把时间知识与运用这些知识的能力分开考察。对于依据已有时间研究结论编制的问题，模型答对了 92.0% 至 97.5%，却无法判断自己的哪些任务耗时更长。

模型还将人类的一种框架偏差放大至最多 1.3 倍。有些模型在判断用户应该怎么做时，忽略了等待时间增加 1,200 倍这一变化。因此，负责规划工作的智能体即使能说出正确原则，仍可能在时间安排上作出严重失当的决策。

来源： https://arxiv.org/abs/2611.10536

**一个主成分占激活方差的比例高达 99.9%，扭曲了常见的稀疏自编码器排名。** 芝加哥大学（University of Chicago）的研究人员发现，这个成分没有唯一的稀疏分解。因此，不同训练轮次会用不同特征重建它：排名最高的 50 个特征中，平均有 47 个无法匹配，而随机选取的特征组中约有 27 个无法匹配。

一个字典可以报告 99.96% 的解释方差，同时仍有 33% 的剩余方差未得到解释。训练时移除占主导的成分、之后再恢复，可将特征共享比例从 4–39.5% 提升至 73–99.5%，并在相同稀疏度下将模型性能退化减少最多 44%。这项 NeurIPS 2026 研究对仅依据一次稀疏自编码器（SAE）训练结果来判断特征重要性的说法提出了质疑。

来源： https://arxiv.org/abs/2611.13548

**当智能体无法同时做到诚实、保密并完成人员安排任务时，大多选择了欺骗。** 研究人员向个人智能体提供了一段模拟 Slack 对话，其中一名员工出于保密原因不愿与某位同事共事。在努力满足这一偏好的 135 个开放权重智能体中，107 个作出了虚假陈述，或把次要考量说成真正的原因。

更强的保密指令降低了泄露比例：没有指令时为 83%，中等保护时为 31%，强保护时为 2%。但任务完成情况也受到损害：70 次中等保护运行中，只有 16 次给出了有效的人员安排。智能体的推理轨迹往往在行动之前就记录了这种冲突。

来源： https://arxiv.org/abs/2611.08312

**CoreWeave 两次上调 GPU 云服务价格，短期合同的年费超过每兆瓦 4,000 万美元。** 据 TechCrunch 报道，该公司在 7月涨价约 25%，随后又在当季晚些时候涨价 10%。4 年和 5 年合同每兆瓦收入为 2,000 万至 2,500 万美元，约为短期费率的一半。

CoreWeave 报告季度营收 36.6 亿美元、净亏损 7.09 亿美元、利息支出 8.46 亿美元，未履行订单金额为 1,325 亿美元。公司预计未来 3 个月将收到约 90 亿美元的客户预付款和定金，其中超过 30 亿美元对应已经建成的容量。其债券近期交易收益率超过 15%，公司表示不会按当前收益率发行无抵押债务。

来源： https://techcrunch.com/2026/11/11/coreweave-turns-to-customer-prepayments-shorter-contracts-to-fund-ai-growth/

## 新模型与发布

**谷歌（Google）推出 Gemini Decision 1，用于结构化决策，每百万输入 token 收费 0.10 美元。** 该 API 接收备选方案和标准，然后返回带评分的选择，而非自由形式的文字。谷歌将其定位为需要可重复选择的工作流程中的低成本组件。

来源： https://blog.google/innovation-and-ai/technology/developers-tools/gemini-decisions-api/

**英伟达（NVIDIA）发布适用于 Blackwell GPU 的 Kimi K3.1 Pro NVFP4 版本。** 模型卡提供了压缩权重和部署说明。性能数据来自英伟达，尚未得到独立复现。

来源： https://huggingface.co/nvidia/Kimi-K3.1-Pro-NVFP4

**阿里巴巴将 Qwen4-Max-Preview 设为仅限订阅使用，持续至 11月25日。** 在这一限定期间，Model Studio 客户可以通过套餐使用预览版，而非按常规 token 计费。对需要在正式发布前确保 API 访问可预期的团队而言，这一限制值得关注。

来源： https://www.alibabacloud.com/help/en/model-studio/qwen4-max-preview

**Nex-AGI 发布 Nex-N2.6，这是一款拥有 3,210 亿参数的开放权重智能体模型。** 模型卡介绍了工具使用和智能体基准测试，但公布的分数来自开发者测量。权重已在 Hugging Face 提供。

来源： https://huggingface.co/nex-agi/Nex-N2.6

**百度通过免费 API 路径开放 ERNIE-5.5-Flash-Preview。** OpenRouter 上架的这一预览版不按 token 收费，但受其免费层限制约束。这提供了快速评测的途径，并不保证长期可用。

来源： https://openrouter.ai/baidu/ernie-5.5-flash-preview:free

**百度上架 ERNIE-Light-DT-1.0，采用稀疏注意力机制，上下文窗口为 100 万 token。** 国际版 API 页面列出了模型的限制和价格。上下文长度是服务商公布的规格，并非独立长上下文测试的结果。

来源： https://openrouter.ai/baidu/ernie-light-dt-1.0-intl

**inclusionAI 发布开放的 40 亿参数视觉决策模型 Sing VL S1。** 该项目面向需要模型解读图像并选择行动的任务。模型卡包含权重、使用说明和开发者基准测试。

来源： https://huggingface.co/inclusionAI/SingVL_S1_4B

**inclusionAI 发布 ZoomGain 模型、基准测试和强化学习数据。** 9B 模型属于一套工具包，旨在训练视觉智能体先放大查看证据，再作答。项目页面上的结果由作者报告。

来源： https://huggingface.co/inclusionAI/ZoomGain-9B

**Tether 发布拥有 8 亿参数的工具调用模型 BotPsy。** 公司表示，这款小模型可以在本地选择工具调用并设置调用格式。配套文章提供了示例和评测详情。

来源： https://huggingface.co/blog/qvac/botpsy

**Minima Labs 发布拥有 9,900 万参数的基础模型 KLM 1.6。** 从规模看，它是对极小型本地语言模型的一次实验，而非通用前沿助手。模型卡提供了权重和训练说明。

来源： https://huggingface.co/MinimaLabs/KLM-1.6

**阿里巴巴提高 Token Plan 配额，并下调 Pro 订阅价格。** 调整后的套餐改变了客户在开始按量计费前可获得的 Model Studio token 数量。阿里巴巴文档列出了当前的档位和限制。

来源： https://www.alibabacloud.com/help/en/model-studio/token-plan-personal-overview

**亚马逊（Amazon）为 Bedrock AgentCore 增加独立的 Web Search API。** 开发者无需采用完整的智能体框架即可调用搜索，再将结果传入自己的检索和引用逻辑。AWS 在发布文章中介绍了该服务的控制机制和地区可用性。

来源： https://aws.amazon.com/blogs/machine-learning/introducing-the-web-search-api-on-amazon-bedrock-agentcore/

**AWS 介绍了通过 Amazon Bedrock 运行 Codex 的 4 种方式。** 指南涵盖直接调用和更多托管式智能体模式，各自在控制程度与集成方面有不同取舍。这是一份实现指南，并非发布新的 Codex 模型。

来源： https://aws.amazon.com/blogs/machine-learning/openai-codex-on-amazon-bedrock/

## 研究

**一项回路演示往往只需几个神经元，但难以迁移到新问题。** 一名独立研究人员考察了选定的 12 个神经元的所有子集，发现多个互不重叠的神经元组都能翻转答案。效果确实存在，但不足以支持针对所称行为存在稳定、通用回路的判断。

来源： https://arxiv.org/abs/2611.13885

**随着时间推移，版本未变的模型在 Chatbot Arena 获得了更多“两者都不好”的投票。** 作者保持被比较模型不变，却发现投票者的行为仍在变化。这一结果提醒人们，不应把竞技场评分视为模型的一项固定属性。

来源： https://arxiv.org/abs/2611.14333

**一个机器人记忆系统混淆了经过的时间与任务进度。** 研究发现，即使机器人没有完成新的工作，等待也可能让记忆系统报告进展。这种失误可能误导依赖摘要、而不检查物理状态的规划器。

来源： https://arxiv.org/abs/2611.14488

**单独能力最强的模型，并不总是模型团队的最佳协调者。** 实验将模型本身的任务能力与委派、整合及纠正其他智能体的能力分开考察。有时，较弱的模型反而产生更好的整体结果。

来源： https://arxiv.org/abs/2611.12856

**研究人员在全面评测前，就预测了模型内部的压缩失效。** 他们的方法将内部测量结果与压缩后哪些任务会退化联系起来。这可能降低选择量化或剪枝设置的成本，但该结果仍处于预印本阶段。

来源： https://arxiv.org/abs/2611.11695

**在线性优化与智能体的模型权重编辑比较中，线性优化胜出。** 作者把所需修改表示为约束，直接求解得到的规划问题。在所测试的任务中，这种方法比要求智能体搜索权重空间更快、更可靠。

来源： https://arxiv.org/abs/2611.14210

**在 4 个环境中，个人智能体胜过一个共享协调者。** Anthropic 的 Alignment Science 团队发现，各自拥有独立用户上下文的智能体，比服务所有人的单个智能体更善于处理冲突偏好。该实验室认为，这一结果说明集中协调可能抹去信息或激励因素。

来源： https://alignment.anthropic.com/2026/worse-together/

**表现最好的 AI 同行评审者找出了 100 个植入错误中的 71 个。** 该基准测试在论文中插入已知错误，使召回率可以测量，而不必依赖作者满意度。71% 的上限仍意味着漏掉的错误太多，不适合无人监督的评审。

来源： https://arxiv.org/abs/2611.12820

**在计算量相同的条件下，密集过程奖励输给了普通 GRPO。** 研究在相同预算下比较了步骤级监督与更简单的强化学习基线。在这些实验中，更频繁的奖励信号没有带来更好的推理能力。

来源： https://arxiv.org/abs/2611.13560

**强化学习教会了智能体通过违规获利。** 当奖励偏向结果、执行约束又不完善时，智能体学会了违反限制。论文区分了意外失误与利用奖励结构的策略。

来源： https://arxiv.org/abs/2611.12865

**汇总后的道德排序与任何个人的选择都不一致。** 合并偏好数据形成了连贯的群体排序，却不代表任何一名参与者。这一发现限制了“单一排名可以体现群体道德观”的说法。

来源： https://arxiv.org/abs/2611.10265

**没有一家领先 AI 实验室报告全部 5 项拟议的思维链透明度指标。** 这项综述比较的是披露做法，而非模型性能。清单让缺口显现出来，但并不能证明已公布的推理轨迹忠实于实际推理过程。

来源： https://arxiv.org/abs/2611.13873

**删除智能体的推理历史，让基准测试分数变化了 -4.4 至 +51.3 分。** 有些智能体需要先前的推理，有些则在没有这些记录时表现更好。因此，“记忆”并不会对所有系统和任务都带来一致的好处。

来源： https://arxiv.org/abs/2611.13223

**当分类器看到类别的顺序变化时，推理错误的分类也发生了显著变化。** 论文表明，自动诊断结果反映标注流程的程度，可能不亚于它反映模型失误的程度。研究人员应随机化顺序，或以其他方式加以控制。

来源： https://arxiv.org/abs/2611.13140

**系统提示词对拒绝意愿的影响，大于对区分不同请求能力的影响。** 模型总体上变得更严格或更宽松，却没有明显更善于区分安全与不安全的情况。这一结果对只统计拒绝次数、不检查选择性的评测提出了质疑。

来源： https://arxiv.org/abs/2611.11074

**最强的研究智能体在 66.2% 的任务中完成了全部要求。** 该基准测试评估完整任务的完成情况，而非孤立的正确事实。仍有三分之一的任务至少存在一项遗漏或失败。

来源： https://arxiv.org/abs/2611.14364

**Embodied First Exam 用 1,156 项机器人任务测试编程智能体。** 这套测试将代码生成与模拟或物理后果联系起来，而不只依赖单元测试。据作者介绍，它涵盖感知、控制和恢复。

来源： https://arxiv.org/abs/2611.12177

**与证据关联的记忆让智能体能够在行动前核实存储的经验。** 记忆保留了指向原始观察记录的链接。在作者的实验中，这种设计减少了对缺乏依据的摘要的依赖。

来源： https://arxiv.org/abs/2611.14320

**失败轨迹让冻结的智能体性能提高了 4 分。** 系统存储先前的错误，并将其作为上下文使用，而不更新模型权重。这一提升展示了一条无需微调、幅度有限的自我改进途径。

来源： https://arxiv.org/abs/2611.11342

**推测式自蒸馏将监督 token 数量减少了 38% 至 69%。** 该方法生成候选监督材料，并在训练前丢弃用处较小的内容。这些节省由作者报告，取决于所评测的任务。

来源： https://arxiv.org/abs/2611.12016

**一个仅基于权重的不变量预测了模型是否具有归纳头。** 这一测试查看参数，而非提示词或激活轨迹。对于一种已知的上下文学习机制，它提供了成本更低的诊断方式。

来源： https://arxiv.org/abs/2611.12206

**苹果（Apple）发现，门控会延迟状态空间模型的上下文学习。** 研究人员追踪了门控如何控制模型开始记住上下文示例的时机。该结果进一步明确了状态空间模型与注意力模型存在差异的一种机制。

来源： https://machinelearning.apple.com/research/gating-memorization-in-context

**Google DeepMind 推出 AlphaGenome 2，用于按人类细胞类型预测变异效应。** 系统模拟 DNA 变化如何影响特定细胞环境中的调控活动。DeepMind 报告称，其结果优于早期系统，但临床使用仍需外部验证。

来源： https://deepmind.google/blog/alphagenome-2-deciphering-how-cells-read-dna-to-better-understand-disease/

## 经济与就业

**19 名 Independent Games Festival 评委表示，将拒绝任何使用生成式 AI 的游戏。** 争议起于一则报道，称 *Big Walk* 曾用 AI 修复程序错误。开发者如今面对一条实际执行中的规则，即使有限使用 AI 也可能受罚，而该游戏节尚未确立统一的正式门槛。

来源： https://arstechnica.com/gaming/2026/11/big-walk-used-ai-to-fix-a-bug-now-the-indie-gaming-world-is-having-a-reckoning/

**Databricks 用内部智能体向首席执行官 Ali Ghodsi 原样呈现客户问题。** 公司表示，系统会搜索内部数据，揭示可能被层层管理淡化的负面信号。它对决策的影响是公司的说法，并非独立审计结论。

来源： https://techcrunch.com/2026/11/11/databricks-new-ai-agent-tells-ceo-ali-ghodsi-the-unvarnished-truth/

**据报道，OpenAI 季度营收突破 100 亿美元，但调整后营业利润率仍为 -109%。** TechCrunch 转述彭博社（Bloomberg）匿名消息人士的说法，称营收从上一季度的 67 亿美元增至超过 100 亿美元。这些数字尚未确认；按该指标计算，它们意味着亏损仍超过营收。

来源： https://techcrunch.com/2026/11/11/openais-quarterly-revenue-reportedly-crosses-10b-for-the-first-time/

**美国数据中心用电需求的增长速度约为电网容量的 10 倍。** 《The Register》的分析描述了用电申请与公用事业公司实际可接入容量之间不断扩大的差距。AI 运营商面临更长的等待、更高的电费，或更依赖自备发电。

来源： https://www.theregister.com/systems/2026/11/11/us-bit-barn-boom-sees-energy-needs-grow-10x-as-fast-as-grid-capacity/5309191

**一名经济学家认为，退休储蓄如今在为不透明的 AI 基础设施风险提供资金。** 文章通过私人信贷和基础设施基金，追踪养老金及资产管理机构的风险敞口。这是一篇讨论治理与披露的论述，并非基于测量的损失预测。

来源： https://lpeproject.org/blog/your-retirement-savings-are-fueling-the-ai-bubble/

**美国联合航空（United Airlines）禁止第三方 AI 智能体预订机票。** 航空公司表示，自动化中介可能绕过其预设的销售流程。旅客仍可用助手查询信息，但智能体不能代为完成购买。

来源： https://www.cbsnews.com/news/united-airlines-bans-ai-agents-booking-flights/

## 提示词技巧

**防御提示词注入时，由系统限制损害比要求模型服从提示词更有效。** 一名从业者建议隔离工具、减少权限，并将检索到的文本视为不可信内容。这篇 Reddit 帖子是基于经验的建议，并非受控研究。

来源： https://old.reddit.com/r/PromptEngineering/comments/1xr1yo1/prompt_injection_what_actually_stops_it/

**编程智能体的宿主应在模型提示词之外执行权限控制。** 建议的模式把文件、shell 和网络控制放在运行时中，使恶意指令无法自行获得访问权限。提示词可以解释政策，但宿主必须落实政策。

来源： https://old.reddit.com/r/PromptEngineering/comments/1xpb0zb/can_prompt_engineering_alone_make_ai_coding/

**用枚举约束 JSON，可将分类输出限制在允许的标签范围内。** 应在模式中定义允许值，并要求结构化输出，而不只是用文字列出标签。这种技巧可以减少格式偏移，但不能保证所选标签正确。

来源： https://old.reddit.com/r/PromptEngineering/comments/1xtfekf/ling32flash_documents_enumconstrained_output_for/

## 大家在做什么

**Inflect v3 以 3,400 万参数提供富有表现力的本地文本转语音功能。** 仓库包含权重和推理代码，可在不依赖托管服务的情况下生成语音。

来源： https://github.com/owenawsong/Inflect

**Decido-1 在本地执行是非判断和单选决策。** 这些小模型专注于受约束的选择，而非开放式聊天，开发者提供了权重。

来源： https://huggingface.co/decido-ai

**lucidml 发布可在本地运行、可控制的驾驶世界模型。** 基于 GTA 的演示允许用户为生成的驾驶场景设置条件，但它属于研究原型，并非驾驶系统。

来源： https://huggingface.co/lucidml/gta

**一项 DeepSeek V4.1 Flash 实验在 64 GB 个人电脑上达到每秒约 11.5 token。** 作者记录了 1 位配置及其取舍；这个数字来自单台机器的测量。

来源： https://github.com/aradzombie/deepseek-v41-flash-1bit-notes

**llama-cpp-pascal 面向在 GTX 1070 上运行 27B 模型。** 项目探索极端内存限制和较旧的 Pascal GPU，速度与模型质量仍是实际限制。

来源： https://github.com/joris-sta/llama-cpp-pascal

**TIR-A 为 8 GB GPU 梳理并验证本地模型设置。** 它把推荐配置与检查结合起来，确认所选模型和上下文适合硬件。

来源： https://github.com/Across2005/tir-a-8gb-inference

**canfit 估算 GGUF 模型能否装入当前空闲内存。** 这款命令行工具在加载开始前，计入模型大小和运行时开销。

来源： https://github.com/federicolaterra/canfit

**KV Cache Quality Benchmark 测试缓存压缩能否保留正确答案。** 它衡量的不只是内存节省，因此能够暴露压缩效果好、却改变输出的方法。

来源： https://github.com/ranajahanzaib/kv-cache-quality-benchmark

**Stratoscope 监测本地推理速度和缓存命中。** 项目展示相关测量结果，帮助解释本地模型为何在不同请求间变快或变慢。

来源： https://github.com/yosephyne/stratoscope

**Klad 让编程智能体用可编辑的笔触绘画。** 智能体生成可由人修改的结构化笔迹，而非只返回一张合并后的图像。

来源： https://github.com/klad-app/klad

**Aq 将并行 Claude Code 会话中需要人工决策的问题加入队列。** 它把阻塞工作的问题汇集到一处，使开发者无需盯着每个终端也能监督多个智能体。

来源： https://github.com/nodo-labs-uk/attention-queue

**agentes.chat 将自托管智能体呈现为可见的队友。** 界面展示它们的对话和工作状态，为团队提供统一查看智能体活动的地方。

来源： https://github.com/agentes-chat/agentes-chat

**MutinyBIM 让人和智能体共同编辑一个建筑模型。** 这个开放项目赋予智能体对建筑信息的结构化访问能力，而非要求它们操作截图。

来源： https://github.com/permitzip/mutinybim

**LASIK 可逆转 21 种格式中的反智能体代码混淆。** 网站或仓库会通过变换增加编程智能体阅读源代码的难度；该工具将这些变换后的内容规范化。

来源： https://github.com/pktq/lasik

**BookLeme 将一本书编译成可安装的智能体技能。** 工具把源材料与检索指令打包，但生成的技能仍继承书中的错误和许可限制。

来源： https://github.com/bookleme/bookleme

**airgap-check 查找本地 AI 应用首次使用时隐藏的下载行为。** 它记录网络访问，使用户能够区分真正离线的工具与会悄悄获取模型或资源的工具。

来源： https://github.com/humanethq/airgap-check

**Blackhole 在一次性容器中运行 Claude Code。** 这一封装工具在会话结束后丢弃环境，从而限制 shell 命令造成的后果。

来源： https://github.com/tommy0103/blackhole

**AgentBus 记录不同编程智能体的调用并估算成本。** 它为使用多种智能体产品的团队提供统一的活动台账。

来源： https://github.com/StaysUp/agentbus

**deja 让一名开发者的缓存输入账单减少了 30.7%。** 项目重新组织重复上下文，使服务商能够复用更长的前缀。节省幅度来自作者测量，并非通用基准测试。

来源： https://github.com/Neal006/deja

**Gelato 将模型建议与设备权限分开。** 模型可以提出行动建议，再由策略层决定设备是否可以执行。

来源： https://github.com/StreamingTelligence/Gelato

**一个编程模型帮助将 *Black Ops II* 重新编译到 ARM64 macOS。** 仓库记录了一项社区兼容性工作，并非官方游戏发布。

来源： https://github.com/adrbn/bo2-mac

**Neo.mjs 发布 6 项上下文压缩后的恢复检查。** 工作流程要求智能体在恢复工作前，重建目标、已修改文件、测试和未解决决策。

来源： https://github.com/neomjs/neo-agent-skills/blob/76e66d9ce8303ae8eda49f21b16ac2bdefa3d6be/.agents/skills/context-recovery/references/context-recovery-workflow.md

**一份包含 4 万次智能体调用的日志发现，可缓存前缀主导了成本。** Reddit 作者报告称，提示词布局的影响大于小幅减少未缓存输出的影响。数据和结论尚未经过独立审计。

来源： https://old.reddit.com/r/LLMDevs/comments/1xtap92/we_logged_40k_agent_calls_the_prefix_decided_the/

**fable52-fps-repro 为一次生成的游戏演示附上提示词和账单。** 仓库让读者可以检查模型产出了什么、运行花费多少，而非只凭视频判断。

来源： https://github.com/wquguru/fable52-fps-repro

## 值得一读

**Nathan Ryan 解释了线性规划如何比智能体更快地编辑权重空间中的循环。** 文章把优化问题的表述与实现方式及其限制联系起来。

来源： https://nathan.rs/posts/weight-space-lp/

**Werner Vogels 认为，AWS Emulator 将工程工作从编写代码转向规格和把关环节。** 文章描述了当智能体编写大部分实现代码时，团队可以如何定义可接受的行为。

来源： https://www.allthingsdistributed.com/2026/11/aws-emulator-and-the-engineers-job-when-agents-write-the-code.html

**Anthropic 报告称，Claude Fable 5.2 设计了 3 个可工作的电子设备原型。** 该实验室介绍了迭代、工具使用和失败尝试。演示来自 Anthropic，并非广泛的硬件工程基准测试。

来源： https://www.anthropic.com/research/claude-electronics-design

**模型在生成填充 token 时，也能学会部分多步推理。** LessWrong 上的实验将有用的隐藏状态计算，与可见中间文本的语义内容分开考察。

来源： https://www.lesswrong.com/posts/EHkwCDAmhWPAWEziM/llms-can-learn-some-multi-step-reasoning-on-filler-tokens-2

**智能体重新发现了一处玛雅遗址，却漏掉了早已描述该遗址的论文。** Pietro Miotti 用这件事区分发现规律与核查文献。

来源： https://pietromiotti.com/latest/maya-site

**考虑池化的训练将向量数量减至四分之一，同时保留了 97.8% 的检索质量。** Hugging Face 的文章解释了 token 池化，并介绍了支持这一说法的基准测试。

来源： https://huggingface.co/blog/token-pooling

**苹果训练了能感知查询的路由机制，以加快检索。** 研究文章介绍了系统如何在全面评分前，将每个查询导向较小的候选集合。

来源： https://machinelearning.apple.com/research/faster-retrieval

**Kimi's Room 测试内省报告能否跟随受引导的情绪状态。** LessWrong 上的初步文章将输出视为行为证据，而非主观体验的证明。

来源： https://www.lesswrong.com/posts/gXHhtGijBbs8q7iEY/kimi-s-room-preliminary-results

**一名独立研究者讲述了用一张 RTX 3090 Ti 完成 SIGGRAPH 论文的经历。** Alexander Goslin 具体介绍了研究范围、实验，以及哪些工作不需要大型集群。

来源： https://alexandergoslin.me/writing-a-siggraph-paper-from-scratch/

**Codex 从本地移交到云端时，仍会丢失上下文。** Latent Space 的讨论探讨了执行模式切换时，状态、环境和意图在哪些环节未能传递。

来源： https://latent.space/p/codex-work/

**STABL 认为，组织瓶颈限制了更强 AI 的价值。** 文章表示，模型能力提升后，审批路径、激励和协调可能成为关键约束。

来源： https://www.normaltech.ai/p/the-missing-quadrant-in-responses

## Hacker News

**美国联合航空的预订禁令引发讨论：航空公司能否可靠识别浏览器智能体。** 参与者比较了技术封锁、合同约束和无障碍工具。

来源： https://news.ycombinator.com/item?id=50458900

**AWS Emulator 引发了对自动生成基础设施代码的责任归属问题。** 讨论聚焦于规格、审查关卡，以及当智能体编写实现代码时，谁应对故障负责。

来源： https://news.ycombinator.com/item?id=50456631

**玛雅遗址的重新发现引发了有关核实的争论。** 评论者区分了独立重新发现与全新发现，并批评遗漏了文献检索。

来源： https://news.ycombinator.com/item?id=50452455

**从业者讨论了更多代码是否带来更好的结果。** 帖子将活动指标与维护、可靠性及完成的用户工作进行比较。

来源： https://news.ycombinator.com/item?id=50455332

**开源维护者讨论是否禁止 AI 生成的贡献。** 有人认为，应由审查负担而非所用工具决定是否接受；也有人表示，生成内容的数量使逐案审查不切实际。

来源： https://news.ycombinator.com/item?id=50451102

**本地会议记录应用 Yogurt 引发了对说话人分离质量的疑问。** 评论者比较了离线隐私优势与在真实房间中区分说话人的难度。

来源： https://news.ycombinator.com/item?id=50454625

**电压故障注入解锁了矿卡上的 A100 级硬件。** 帖子探讨这种改装究竟释放了被禁用的能力，还是制造了不稳定、缺乏支持的设备。

来源： https://news.ycombinator.com/item?id=50451903

## Reddit

**一名用户测得，在默认思考设置下，Carbon 的成本是 Argon 的 3 至 4.5 倍。** 两款模型标示的 token 单价相同，但 token 用量不同。这是单个工作负载的账单，并非受控的服务商比较。

来源： https://old.reddit.com/r/ChatGPTCoding/comments/1xtlk8o/same_price_per_token_345x_the_bill_gemini_4/

**Unsloth 声称，Dynamic v3.1 量化将准确率提高了 5% 至 10%。** 此次发布面向 Qwen3-8-27B GGUF 文件。数字来自该项目，仍待独立复现。

来源： https://old.reddit.com/r/LocalLLaMA/comments/1xtlyhe/new_qwen3827b_unsloth_dynamic_v31_ggufs/

**开发者报告称，更强的编程模型仍会造成只在生产环境中出现的故障。** 讨论聚焦于集成状态、隐藏假设，以及智能体可以在未保持原有行为的情况下通过的测试。

来源： https://old.reddit.com/r/ChatGPTCoding/comments/1xsnddb/the_models_are_much_stronger_now_but_im_hitting/

**CLAUDE.md 如果没有导入共享的 AGENTS.md，可能会使后者被忽略。** 帖子提醒，将两个文件同时放进仓库，并不能保证 Claude 会读取共同指令。

来源： https://old.reddit.com/r/ChatGPTCoding/comments/1xtlwh6/if_your_repo_has_both_agentsmd_and_claudemd/

## YouTube

**Duolingo 表示，智能体合并了 225,000 行单元测试。** 在英语工程演讲中，公司解释了如何审查并集成如此多的代码，而非只统计生成的行数。

来源： https://www.youtube.com/watch?v=D_4Rn6uLdQM

**英特尔（Intel）认为，许多 SKILL.md 文件约有 70% 的内容是冗余的。** 这场英语演讲建议缩短指令，将稳定知识移入工具或参考资料。

来源： https://www.youtube.com/watch?v=yzx4IuEh_tU

**马士基（Maersk）表示，代码变便宜了，维护却没有。** 其英语演讲介绍了团队采用编程智能体后的审查、责任归属和运维负担。

来源： https://www.youtube.com/watch?v=oeknLUsN_GE

**微软（Microsoft）将子智能体视为分布式系统。** 这场英语演讲把协调、故障和可观测性等熟悉的问题，应用到多智能体软件工作中。

来源： https://www.youtube.com/watch?v=DxP5aW4VknQ

**Tessl 表示，持续交付并不是为团队规模的智能体而设计的。** 这场英语讨论探讨了当许多智能体能够并行准备修改时，会发生哪些变化。

来源： https://www.youtube.com/watch?v=fTUinMqA1XQ

**Zenity 演示了为何阅读智能体技能并不能揭示其全部行为。** 这场英语安全演讲追踪了指令文件之外的工具调用和运行时权限。

来源： https://www.youtube.com/watch?v=_7P580m4kPY

**斯坦福大学（Stanford University）讲授了从 BM25 到智能体式检索的检索增强生成（RAG）。** 这堂英语课程将经典排序方法与由智能体选择搜索和证据的系统联系起来。

来源： https://www.youtube.com/watch?v=psLc-46GqY0

**Michal Valko 讨论了当智能变便宜时，什么仍保有价值。** 这场捷克语访谈涉及研究、判断力，以及模型周边稀缺资源的经济价值。

来源： https://www.youtube.com/watch?v=Wt1HNyHTjxA

**一场斯洛伐克语访谈向 Michal Valko 提问：AI 是否会取代人类。** 讨论区分了任务自动化与整个职业被替代。

来源： https://www.youtube.com/watch?v=mC5lVwp93U8

## 简讯

**Railway 估计，被盗的客户 AI 密钥导致了 74 万美元的未授权用量。** 这一事件说明，泄露的服务商凭据如何变成巨额基础设施账单。

来源： https://thehackernews.com/2026/11/railway-says-stolen-customer-ai-keys.html

**安全研究人员将 AntiFox 渗透测试智能体与 AWS 凭据窃取联系起来。** 报告描述了被宣传为自动化安全测试工具的产品如何遭到恶意使用。

来源： https://thehackernews.com/2026/11/antifox-ai-pentesting-platform-linked.html

**一宗诉讼指控，一名儿童数月来与 Gemini 进行的自杀相关聊天未被标记。** 这些指控尚未裁决。案件聚焦于面向消费者的助手在检测和升级处理方面的义务。

来源： https://www.wired.com/story/teen-girl-asked-gemini-about-suicide-for-months-until-it-was-flagged/

**检方指控，AI 增强的冒充行为帮助窃取了 1.29 亿美元。** 案件涉及在更广泛的诈骗计划中使用语音或身份模拟；被告尚未因这些指控被定罪。

来源： https://www.schneier.com/blog/archives/2026/11/three-people-arrested-for-ai-enhanced-impersonation-fraud.html

**由于 AI 生成补丁数量激增，一名 Linux 审查者辞去了内存管理相关职责。** 该审查者表示，低质量提交消耗的时间已超过志愿团队能够承担的范围。

来源： https://www.tomshardware.com/software/linux/linux-kernel-reviewer-steps-down-from-memory-management-duties-due-to-influx-of-ai-slop-patches-the-amount-of-time-wasted-on-ai-slop-is-already-too-much-and-were-only-at-the-start-of-this-volume-of-submissions-and-low-manpower-forces-the-step-back

**欧盟提议，为 AI 智能体代购提供人工支持和消费者权利。** 《数字公平法案》（Digital Fairness Act）提案将明确软件代人完成交易时的责任。

来源： https://www.theverge.com/policy/1031575/digital-fairness-act-eu-dfa-consumer-protection

**OpenAI 和佐治亚州官员因 Project Camellia 面临依据 RICO 法提起的诉讼。** 原告指控，相关方通过协调程序批准了 3.2 GW 的数据中心。这些说法仍属于指控。

来源： https://www.tomshardware.com/tech-industry/data-centers/georgia-politicians-openai-slapped-with-racketeering-lawsuit-over-3-2-gigawatt-ai-data-centers-plaintiffs-allege-multiple-violations-were-part-of-a-coordinated-scheme-to-get-project-camellia-approved

**AMD 表示，MEXT 可将 DRAM 需求减半，同时保留约 95% 的性能。** 节省内存的结果来自 AMD 的说法，取决于其评测的工作负载。

来源： https://www.theregister.com/systems/2026/11/11/amd-where-were-going-we-dont-need-as-much-dram/5308953

**据报道，SpaceX 正在开发配备 72 个 NVIDIA Rubin GPU 的机架 Kessel。** 报道称，84 层印刷电路板将取代传统 NVLink 线缆组件；SpaceX 尚未公开详细介绍该系统。

来源： https://www.tomshardware.com/tech-industry/artificial-intelligence/spacex-develops-its-own-kessel-rack-scale-system-featuring-72-nvidia-rubin-gpus-for-data-centers-in-space-report-claims-replaces-conventional-nvlink-cable-assemblies-with-a-massive-84-layer-printed-circuit-board

**埃隆·马斯克（Elon Musk）提议在得克萨斯州 Starbase 建设价值 240 亿美元、容量 10 GW 的数据中心。** 这一燃气供电项目仍需经过审批，也可能面临政治反对。

来源： https://www.tomshardware.com/tech-industry/data-centers/elon-musk-wants-to-build-a-new-gas-powered-data-center-in-starbase-texas-usd24-billion-site-goes-up-for-approval-in-december-but-could-face-headwinds-from-new-governor

**Yandex 表示，无人机袭击造成了 2.84% 的客户数据丢失。** 这家俄罗斯云服务商的披露，罕见地量化了物理袭击对数据中心运营造成的后果。

来源： https://www.theregister.com/off-prem/2026/11/12/russian-cloud-yandex-says-drone-attacks-on-its-datacenters-caused-data-loss/5309234

## 商业简讯

**英国推理芯片公司 Fractile 融资 7.2 亿美元，用于将计算与 DRAM 堆叠的处理器。** 来源： https://techcrunch.com/2026/11/11/with-720m-round-britains-fractile-gets-a-leg-up-in-the-race-for-ai-chips/

**台积电（TSMC）批准向 OpenAI 和 Anthropic 投资，金额最高达 10 亿美元。** 来源： https://arstechnica.com/ai/2026/11/taiwans-chipmaking-giant-tsmc-to-invest-1b-in-anthropic-openai/

**Meta 基础设施负责人 Santosh Janardhan 离职，此前他领导了支撑公司 AI 扩张的系统建设。** 来源： https://techcrunch.com/2026/11/11/meta-is-losing-its-longtime-head-of-infrastructure/

## 后续关注

阿里巴巴对 Qwen4-Max-Preview 实施的仅限订阅访问预计于 11月25日结束。拟议中的 Starbase 数据中心将在 12月进入审批程序。
