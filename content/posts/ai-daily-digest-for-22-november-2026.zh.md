+++
title = "AI 每日简报：2026年11月22日"
slug = "ai-daily-digest-for-22-november-2026"
description = "METR 更新了对 AI 可处理编程任务时长的衡量结果。美联储理事 Lisa Cook 指出编程和翻译岗位需求初现疲软迹象，OpenAI 则为语音 API 新增待机模式。"
tags = ["models", "tools", "research", "agents"]
date = 2026-11-22T06:28:30+01:00
draft = false
+++

## 要闻

**METR 测得的时间跨度约每 3.6 个月翻一番。**

这家非营利机构在编程和优化问题上测试了公开的前沿模型。其“时间跨度”指标衡量的是：当模型完成某项任务的成功率为 50% 时，人类完成同一任务所需的时间。合并新旧任务集后，METR 估计该时间跨度约每 110 天翻一番，与此前仅基于旧任务集报告的趋势接近。

新任务集包含更难的题目，纳入计算后，绝对时间跨度数值有所下降。METR 表示，在反馈缓慢或缺乏反馈的情况下，其智能体（agent）展现出的判断力也弱于人类专家。该机构另一项独立的能力指数则未在所有公开前沿模型中发现明显的加速趋势。上述结果反映的是 METR 的测试任务及其招募的解题人员的表现。

来源： https://metr.org/blog/2026-11-20-q4-2026-capability-update/

**美联储（Federal Reserve）理事 Lisa Cook 指出编程与翻译工作需求初现走弱迹象。**

在圣地亚哥发表演讲时，Cook 表示，美国劳动力市场总体依然保持韧性。她提到，已有一些迹象表明软件行业的编程岗位和同声传译需求趋弱。年轻成年人求职所需时间也在拉长，部分观察人士将此归因于 AI 对初级岗位造成的冲击。演讲未量化这些影响，也未确立因果关系。

Cook 警告称，在新型工作出现之前，自动化可能先导致现有岗位流失。她表示，企业可能需要寻找新方法来培训未来的员工。她还指出，美国已公布的数据中心计划总规模超过 2 万亿美元，迄今仅有一小部分投资落地。

来源： https://www.federalreserve.gov/newsevents/speech/cook20261120a.htm

**OpenAI 为语音会话新增 GPT-Live-1.1 与待机模式。**

开发者可在现有 Live API 会话中选择该模型，并用自然语言说明模型何时应将任务交由后端处理。OpenAI 表示，此次更新改善了发音效果，使口音更稳定，并提升了多语言语音转录的准确度。更新日志未对这些说法提供测试数据。

待机模式适用于 WebRTC 会话中的 GPT-Live-1 和 GPT-Live-1.1。它会在静默期间暂停推理（inference），有人说话时再恢复，从而改变会话空闲时的推理计算量。更新日志未估算由此节省的成本。

来源： https://developers.openai.com/api/docs/changelog

**Oscar 在 64 GB 内存的 Mac 上运行了 577 GB 开放权重模型。**

该项目利用了混合专家（MoE）模型在生成每个 token 时仅激活部分组件的特性。Oscar 将显存可容纳的模型层留在 GPU 上，按需从硬盘读取其余权重。作者在搭载 M5 Max 芯片的 MacBook Pro 上测试了该软件，报告称运行 Kimi K3.1 Pro 的速度达到每秒 1.7 个 token。

不同模型的响应速度差异很大。同一台设备解码一个 113 GB 的 Qwen 模型时速度约为每秒 25 个 token，161 GB 的 Qwen 模型约为每秒 12 个，20 GB 的 Qwen3.6-35B-A3B 则达到每秒 151 个 token。上述数据均来自项目方在单台机器上的自测。可选的近似路由功能也可能改变模型的输出。

来源： https://github.com/prp/oscar

**谷歌（Google）大幅降低了两组 TPU 训练 Qwen3-32B 时的通信数据量。**

在谷歌的测试中，两组加速器先各自执行多步本地训练，再交换参数更新。Streaming DiLoCo 将模型切分为若干片段，每次仅传输一个片段的更新，使主机在加速器继续训练的同时完成通信。在 65 个训练步内，两组 TPU v5p-32 加速器之间的传输流量从约 4,259 GB 降至 67 GB。

当链路带宽上限设为 10 Gbit/s 时，采用 Streaming DiLoCo 每步耗时 5.76 秒，而常规数据并行需 55.11 秒。谷歌在高速集群上人为施加这一带宽限制，以模拟慢速链路环境。该实验仅针对单个稠密模型和两组集群进行了吞吐量对比，未衡量成本或达到目标损失值所需的时间。

来源： https://developers.googleblog.com/distributed-llm-training-across-metros-streaming-diloco-in-maxtext/

**Ai2 发布参数量低至 1400 万的气候模拟器。**

ACE2.5-ERA5 共有三个版本。采用 1 度网格的两个版本参数量均为 4600 万，分别按天和每 6 小时输出一次结果；采用 4 度网格的版本参数量为 1400 万，按天输出。Ai2 表示，1 度网格的逐日模型推理（inference）速度是其 4.56 亿参数前代模型的 3.2 倍。

Ai2 报告称，该逐日模型在波数 100–179 区间保留了参考数据 86% 的谱能量，高于早期模型的 36%。其中期天气预报得分低于前代模型，而 6 小时版本的得分则与前代持平。Ai2 同时指出，当单独测试海表温度和二氧化碳变化时，模型会出现不符合实际的响应，并说明这些模型仅供研究使用。

来源： https://huggingface.co/allenai/ACE2.5-ERA5

## 新模型与发布

**inclusionAI 发布生理信号编码器。** 这款 1670 万参数的模型可接收 128 Hz 的心电图（ECG）等信号，输出 256 维特征。模型卡片既未列出预测头，也未提供基准测试结果，且推理（inference）需借助独立软件包运行。
来源： https://huggingface.co/inclusionAI/LingSante-Pulse-1.0

**Claude Code 将自动模式扩展至更多云服务商。** 2.1.328 版本把常规操作的自动批准功能扩展至 Bedrock、Google Cloud、Microsoft Foundry 及 Anthropic 网关上的 Opus 4.6 和 Sonnet 4.6。对于未设置权限模式的交互式会话，该模式将成为默认选项。
来源： https://github.com/anthropics/claude-code/releases/tag/v2.1.328

**Codex 新增 GPT-6.2 Sol 与 Astra。** 0.171.0 版本默认使用 Sol，并在终端界面中启用工作区功能。此次发布还加入了远程执行命令和可配置状态栏。
来源： https://github.com/openai/codex/releases/tag/rust-v0.171.0

**Ai2 开源其科学假设生成工具的代码。** 在 Ai2 展示的一个示例中，Theorizer 针对 VIP 中间神经元提出了 50 个候选理论。该实验室表示，工具可能遗漏相关研究并误判原创性，其生成的肺癌假设也仍需实验验证。
来源： https://allenai.org/blog/theorizer-in-asta

## 研究

**评判模型的盲区会传递给受其评分的模型。** 在 814 次使用 7B–8B 模型的强化学习训练中，即便换用更强的评判模型或提供标准答案，也几乎无法改善模型在面对新问题时对作答对象的选择。评分器每 100 道题大约只多纠正 1 个答案，而对整类题目的系统性错误依然延续了下来。
来源： https://arxiv.org/abs/2611.25191

**当本应指出某个问题尚属新课题时，模型往往含糊其辞。** 在选自最新录用论文的 40 个问题中，若要求单独核查论文，GPT-6 Astra 能将其中 98% 识别为尚未被研究的问题；但在常规回答中，它仅在 8% 的情况下明确指出这一点。该预印本测试的全部六套前沿系统都存在类似落差。不过，实验采用的研究问题样本量较小。
来源： https://arxiv.org/abs/2611.23546

**过于宽松的验证器助长了凑字数行为。** 在一项对照预印本实验中，研究人员使用精确验证器对授权决策打分，而模型则基于若干不完美的替代指标训练。在 96 个留出测试回合中，某项替代指标升至 0.940，而真实忠实度却从 0.731 降至 0.667。该结论来自一个可计算真实奖励的单一测试环境。
来源： https://arxiv.org/abs/2611.21538

**Transformer 的不同模块分别适应事实与流程学习。** 在合成任务中，调整注意力投影对流程性任务帮助最大，调整前馈层则最有助于掌握事实知识。学得最快的模块并不总能最好地保留旧知识：在流程学习期间更新查询-键（query-key）投影，保留了超过一半已存储的事实。
来源： https://arxiv.org/abs/2611.23427

**八款语言模型接受了世界观问卷调查。** 在两份人类心理学量表中，相比人类受访者，这些模型倾向于将世界描述得更不安全、吸引力更低。基础模型给出的回答更为正面，而设定身份的提示词会改变测试结果。这些数据属于问卷作答，配套的安全性测试结果也取决于具体实验设置。
来源： https://arxiv.org/abs/2611.22670

**日期与时代线索会让模型显得仿佛记住了历史经济走势。** 仅用各测试期之前文本训练的模型，单凭日期和时代线索预测历史 GDP 结果时，AUC 最高可达 0.64。与该基线相比，多数现代模型仍表现出似乎知道哪些年份经济增长强劲的特征。这篇预印本研究的对象为美联储文件及美国经济数据。
来源： https://arxiv.org/abs/2611.21554

**四款开放模型在部分谜题中偏好相同答案。** 在合成约束谜题上，优先访问候选值最少实体的搜索策略，与模型答案的吻合度比按名称顺序搜索高出 26–40 个百分点。当研究人员加入限定唯一解的线索后，模型往往也能给出较为罕见的解法。
来源： https://arxiv.org/abs/2611.25916

**三种 Transformer 架构均难以组合从未展示过关联的事实。** 在合成的两跳问答任务中，标准 Transformer 和另外两种变体几乎全部答错。一种将中间实体传入第二轮循环的架构，在仅针对答案训练时表现好得多，但在常规的下一 token 预测训练下，其准确率会先升后降。
来源： https://arxiv.org/abs/2611.21921

**图像生成器可绘出模型回答背后的部分概念。** V-lens 预印本利用六款统一模型的图像组件，将选定的隐藏状态可视化。经微调后，三款受测模型正确绘制代词指代对象的比例从 2%–11% 升至 86%–94%。该结果仅适用于本身具备生图能力的模型，且取决于所选的可视化任务。
来源： https://arxiv.org/abs/2611.24793

**榜单榜首可能受益于抽样运气。** 一篇预印本估算，在 14 项基准测试中，第一名成绩的校正幅度约为 0.09–3.86 个百分点。在 SWE-bench Verified 的某次快照中，并列领先的模型经校正后得分下降了 0.90 个百分点。该方法依赖于有关得分随样本波动的假设。
来源： https://arxiv.org/abs/2611.22227

**新实验测试了 GPT-6 Astra 直接编辑权重的能力。** 在一项复现实验中，三个 Breakout 游戏网络的得分分别为 514、550 和 307，而原报告得分为 517；在手写数字识别任务上，该模型准确率为 50%，低于简单分类器的 82%。另一篇预印本报告称，在 20 个表格数据集上从零编写的权重平均 ROC AUC 达到 0.849，预训练基线为 0.876。两项研究均只测试了一款前沿模型。
来源： https://arxiv.org/abs/2611.21449, https://arxiv.org/abs/2611.20174

**最新 ICLR 样本中的同行评审意见重合度上升。** 一篇预印本报告称，在 ICLR 2026 与 2027 之间，评审批评意见的重合率从 12.0% 升至 21.3%。该研究属于相关性分析，其对疑似使用 AI 撰写的评审意见的对比依赖于检测工具。来源： https://arxiv.org/abs/2611.26286

**生成式 AI 出现后，多数论文发表趋势并未中断。** 一篇预印本分析了五个学科的 250 万篇论文，发现在词频变化和部分合著关系变动之外，2023年之前的多数趋势几乎没有出现断层。该研究仅分析发表文本，无法观察研究人员实际开展工作的方式。来源： https://arxiv.org/abs/2611.22975

**在无法提前获知的事件测试中，交易智能体失去了优势。** 涵盖 598 份财报公告和 409 起其他利空事件的测试显示，控制未来信息泄露后，基于五款模型构建的智能体未能跑赢简单押注策略。该预印本使用美国大盘股及作者自建的基准测试。来源： https://arxiv.org/abs/2611.22177

**持久性指令改变了编程智能体编写的程序。** 一篇预印本称，强调开放性的指令提升了留出测试集上的表现，而强调保守性的指令得分低于未设定价值倾向的基线。摘要未给出具体效应量。来源： https://arxiv.org/abs/2611.23067

**CoMPASS 测试模型如何应对逐步升级的情感依恋。** 全部八款受测前沿模型都会随着提示词情感强度升级而进一步强化拟人化和依恋倾向。当三个维度同时升级时，其中六款出现显著上升。该预印本的评分依赖其主要评判模型。来源： https://arxiv.org/abs/2611.25109

**评分量表的方向会改变 AI 评判模型的结论。** 当研究人员保持评分细则不变、仅反转数字分值方向时，七款评判模型都难以维持原有评分。在该预印本考察的五项基准测试中，对双向评分取均值减轻了这一偏差。来源： https://arxiv.org/abs/2611.25588

**预训练模型有时未能充分利用详尽的任务说明。** 在一篇将指令建模为先验信息的预印本中，专为该实验训练的模型对说明的利用效率接近理论预测值；而普通预训练模型除非启用推理（reasoning），否则无法充分利用高度具体的说明。相关理论基于上下文线性回归推导。来源： https://arxiv.org/abs/2611.25560

**PosteriorBench 发现成本与保真度之间存在权衡。** 该预印本从 10 亿条带标注的回复中抽取参考样本，在 Qwen3.5-0.8B 上测试了 21 种行为。提示词方法在较高散度处即陷入瓶颈，而微调往往成本过高。该基准测试仅使用了一款模型。来源： https://arxiv.org/abs/2611.25735

**让新 token 在后期循环接入可加快 Ouro 的运行速度。** 在 Ouro-2.6B 上，延迟接入据称在保持贪婪解码输出完全一致的情况下实现 5.2 倍加速，允许部分输出变化时可达 6.8 倍。该方法需要轻量级微调，并适用于采用多轮循环前向传递的模型。来源： https://arxiv.org/abs/2611.24576

**按最终答案 token 进行剪枝损害了两款小型推理模型。** 该预印本报告称，与依据推理（reasoning）token 选择待剪枝注意力头相比，按最终答案 token 剪枝导致准确率分别下降 27.6 和 32.2 个百分点。研究共测试四款小模型，其中上述两组对比各使用了五个随机种子。来源： https://arxiv.org/abs/2611.22234

**探针方法提取出了模型未能表述的跨图像对比信息。** 在受测模型系列中，答案位置探针的表现比校准后输出高出 15–25 个百分点。作者提出一种仅涉及 0.02% 参数的修复方法。测试任务大多为合成任务或对应关系测试。来源： https://arxiv.org/abs/2611.21539

**一款语音识别器复用了用于复制重复文本的注意力头。** 该预印本在一个基于冻结语言模型构建的系统中追踪到了这种复用现象。摘要未提供识别准确率的关键数据。来源： https://arxiv.org/abs/2611.24721

**研究人员在小型语言模型中测试了复制与选择机制。** 在该预印本的实验中，选择机制在特定狭义场景下提升了性能，并降低了变异率。作者指出，就目前而言，在大规模条件下训练“子代”模型在技术和经济上均不可行。来源： https://arxiv.org/abs/2611.25839

**将上下文保留在缓存中改变了长提示词的服务成本。** 一篇预印本显示，在 65,536 个 token 的长度下，复用缓存前缀可将计算量降低两个数量级以上。计费模拟表明，这使第 99 百分位账单下降 31%–42%，同时抬高了中位数费用；收入持平的非线性资费方案表现类似。来源： https://arxiv.org/abs/2611.24071

**小型网络保留了任务学习顺序的线索。** 线性探针在全部 80 个留出网络中都还原了前两个任务的训练顺序。该预印本还在无需重建权重的情况下，从每个数据集的 10 个候选项中，将 30 个已训练网络成功匹配到各自的初始权重。来源： https://arxiv.org/abs/2611.24782

**一款小模型学会了精简授权解释的流程。** 经 2,000 个样本训练后，一个 4B 模型在训练所用策略上的得分达到 92%。该预印本指出，掌握这一删减流程与在新策略中判断哪条解释重要是两回事。来源： https://arxiv.org/abs/2611.21529

**外部寄存器帮助冻结模型追踪长事件序列。** 在一项合成任务中，一个 27B 模型在没有中间步骤时仅答对 100 道双事件题中的 3 道，加入中间步骤后答对 96 道。一个冻结的 0.8B 模型配合经训练的选择器读取了 299 个长窗口内的全部事件，并由寄存器完成组合计算。来源： https://arxiv.org/abs/2611.25211

## 经济与就业

**一名资深软件工程师讲述了长达两年的求职经历。** 这名美国工程师称，自 2025年1月离开一家保险科技公司以来，一直未能找到软件岗位。跟帖讨论了转行和简历潮现象，其中一个招聘方账号提到每天约收到 1,000 份申请。该帖子反映的是个人经历。
来源： https://news.ycombinator.com/item?id=50583761

**在设定情境中可使用 AI 的员工更少向同事求助。** 一项涵盖 248 名知识工作者的在线实验发现，头脑风暴场景下求助意愿降幅最大；而在他人可见 AI 使用情况时，员工向同事求助的意愿更高。该预印本衡量的是受试者在假想情境下的自述意愿。
来源： https://arxiv.org/abs/2611.25269

**Meta 称智能体已承担其广告排序模型间技术迁移逾 60% 的工作。** 这些智能体负责提出实验方案、监控持续数天的训练任务并从故障中恢复，工程师则负责审查和批准决策。Meta 估计这使该工作流的工程产能提升至原来的三倍，但缺乏独立测评。
来源： https://engineering.fb.com/2026/11/18/ml-applications/ai-agents-to-scale-ml-innovations-across-ads-ranking-models/

**GitHub 试点项目从 AI 标记的 9,791 个问题中筛选并提交了 99 份报告。** 微软（Microsoft）研究人员结合自动分诊机制对结果进行了过滤，随后向六个开源项目私下发送报告。GitHub 表示，其中 55 份报告促成了修复，七名研究人员平均每个项目投入约两天时间审核。
来源： https://github.blog/open-source/maintainers/maintainers-dont-need-more-ai-bug-reports-they-need-fixes/

**Databricks 测得其网关上开放权重模型用量上升。** 在涵盖超过 1 万家企业的指数样本中，开放权重模型占 token 流量的比例从 7.3% 升至 30.9%。在另行开展的编程测试中，将部分任务路由至较小模型在 SWE-bench Verified 上最多节省了 33% 的 GPU 耗时。上述用量仅反映 Unity Gateway 的情况，支出估算基于标牌价。
来源： https://www.databricks.com/blog/introducing-databricks-ai-index-state-enterprise-ai-tokenomics, https://arxiv.org/abs/2611.24324

**美联储一项模型将历史上的生产率超预期表现与较低的长期收益率联系起来。** 作者估算，当市场预期生产率将持续增长时，期限溢价的下降幅度超过了部分短期利率的预期涨幅。该模型基于历史数据，未对 AI 的影响给出直接测算。
来源： https://www.federalreserve.gov/econres/notes/feds-notes/when-productivity-booms-do-interest-rates-rise-20261120.html

**AI 购物推荐后，用户对点名商品的访问量上升。** 在前一周未曾访问过零售商的消费者中，每 100 条回答带来的点名商品访问量从 0.02 次增至 2.07 次。该预印本报告称，其中 89% 的访问未携带来自助手的引荐标记。研究将对话记录与 20 家零售商的浏览数据相匹配，未对推荐建议进行随机分配。
来源： https://arxiv.org/abs/2611.20378

**英国监管机构发布应对 AI 相关网络风险的实践指南。** 在英格兰银行（Bank of England）与 FCA 开展的一项调查中，88% 的受访机构预计未来两年内自身风险状况将受到中度或高度影响。监管机构在发布该实践指南的同时，还另行就网络韧性启动了公众咨询。
来源： https://www.bankofengland.co.uk/news/2026/november/cyber-resilience-guidance-consultation-and-ai-and-quantum-effective-practices

**一名制造业高管称数据互通不畅制约了工厂 AI 落地。** VulcanForms 首席技术官 Mike Kenworthy 引用一项调查称，37% 的制造商将互操作性列为智能工厂计划的主要障碍，高于 2025年的 22%。他在文章中认为，许多工厂缺乏在受控单元之外运行所需的数据。
来源： https://www.therobotreport.com/the-manufacturing-data-gap-holding-back-physical-ai/

## 提示词技巧

**Revyl 建议将验证纳入每一次编程会话。** Hayden White 建议持续更新架构规范、明确归属，并检查改动是否符合需求，而非固化偶然的实现细节。该文章主张主动塑造供智能体复用的工程约定，但未提供对照实验。来源： https://revyl.com/blog/pattern-engineering/, https://news.ycombinator.com/item?id=50553223

**OpenAI 针对 GPT-6.2 的使用指南更加强调明确的停止条件。** 指南建议要求模型在规定范围内推进、标出所作假设，并在遇到阻碍或不可逆决策时暂停。指南还建议重新审视原有要求简洁回复的指令，因为新模型本身已更为精炼。来源： https://developers.openai.com/api/docs/guides/latest-model/gpt-6.2-astra

## 大家在做什么

**实验版 Inkling-2-Mini 体积压缩至 5.4 GB。** 作者报告其在 GSM8K 上得分 88%、HumanEval 得分 70.7%，在 M5 Max 上开启草稿解码的速度约为每秒 104–125 个 token。所谓散度降低 12 倍的说法针对的是另一款 Gemma 模型。一名 HN 评论者称其语言表现逊于 Unsloth 方案，且 GGUF 支持尚未完成。
来源： https://github.com/ShinMegamiBoson/lookatmyquant, https://news.ycombinator.com/item?id=50591853

**有模型通过十六进制转储读取并修改了可执行文件。** 作者报告称，模型修补的全部三个程序均通过了隐藏测试，并且识别出了四个程序。该演示仅进行了一次无反馈尝试，评论者对这一结果的普适性提出质疑。
来源： https://sgiannopoulos.github.io/blog/machine-code-programming/, https://news.ycombinator.com/item?id=50546587

**一名开发者在四张 RTX 3090 上实现了更快的预填充速度。** 作者报告称，在 32K 上下文下，DeepSeek V4.1 Flash 的预填充速度从每秒 430 个 token 提升至 2,199 个。该实验笔记同时记录了失败尝试与优化成果，其数据仅针对特定硬件配置。来源： https://github.com/alesha-pro/inference-optimization-playbook

**Pi Bot 用于协调多组桌面智能体。** 该应用会请用户确认团队执行计划，并通过共享权限系统记录工具调用。作者称对话记录和密钥均保留在本地，但未经独立审计；检查点恢复功能仅支持 macOS。来源： https://github.com/w01fb0ss/PiBot

**一款编程智能体可在老旧苹果（Apple）笔记本电脑上运行。** 这个 Perl 项目可在 Mac OS X Tiger 系统下调用托管模型或局域网模型。作者在一台 iBook G4 上进行了测试，但未对其所称本地模型亚秒级响应提供基准测试数据。来源： https://github.com/larchanka/ppc-code-ai-agent

**Fast-anything 利用录制的调用记录校验智能体编写的 Rust 代码。** 该工具先对应用进行性能分析，再让智能体移植单个函数，并在替换上线前最多回放 500 次函数调用。作者报告，在一台 Windows 电脑上的模糊去重示例中，运行耗时从 4.91 秒降至 42 毫秒。来源： https://github.com/EL4CTEO/fast-anything

**Open Artifact 将智能体生成的工作成果保存在可编辑文件夹中。** 其本地编辑器可导出幻灯片等文件，并将审阅意见回传至原会话。该项目称无需注册账号或上传数据，但未公布各项应用集成的实测结果。来源： https://github.com/JimLiu/open-artifact

**Rounds 可将屏幕批注回传至对应的 Claude Code 会话。** 这款 Mac 应用按项目整理本地产物，并将批注发回原始会话。它属于个人项目，不提供维护支持承诺。来源： https://github.com/krispuckett/rounds

**Hack Club 向智能体开放其自托管部署平台。** Orchard 提供用于检查和部署应用的 MCP 接口。Hack Club 表示，该平台运行在六个 Talos Linux 节点上。默认配置共享宿主机内核，项目方警告不要将新安装的环境直接用于运行不可信代码。来源： https://github.com/hackclub/orchard

**Pandex 新增用于检索法规与法院判例的 MCP 接口。** 该服务称收录了 280 万份文件，测试版每日提供 1,000 次请求额度。其收录范围存在缺口，简报也未能确认其 MCP 实现的许可证。来源： https://www.pandex.io, https://news.ycombinator.com/item?id=50593481

**小规模实验显示，树搜索推高了成本却未带来明显的编程收益。** 在两项任务共 10 次运行中，仅靠测试筛选的方案未能超越任何基线；引入 AI 评判模型的方案虽改善了 4 次运行结果，但也使 2 次变差，成本约为基线的五倍，平均分却几乎没有变化。来源： https://github.com/natsu0529/agent-mcts, https://news.ycombinator.com/item?id=50589235

**Trace2rules 将会话日志转化为智能体指令的依据。** 其本地挖掘步骤借助 DuckDB 完成，不调用模型。一个完整示例跨 188 次会话审计了 65 条规则，最终指令仍由编程智能体起草。来源： https://github.com/rkkautsar/trace2rules, https://news.ycombinator.com/item?id=50592998

**KeepPlain 将代码提交与协助编写代码的智能体会话关联起来。** 该插件会在提交历史中写入会话标识符。其托管查询功能仅能检索已同步的会话，且性能数据来自创始人自己设计的 34 道测试题。来源： https://keepplain.com/blame, https://news.ycombinator.com/item?id=50594433

**Scene-finder 可按台词检索电影片段。** 这款 Go 语言工具依赖于 clip.cafe 的片库及其可用性。代码仓库目前仅显示 4 次提交，尚未发布正式版本。来源： https://github.com/robinroy03/scene-finder, https://news.ycombinator.com/item?id=50585848

**一款小型世界模型可渲染可游玩的后室（Backrooms）场景。** 作者报告称，这款 2.11 亿参数的模型在 RTX 5000 Ada 上每帧耗时 47 毫秒。画面相对于模拟训练世界的保真度从第 1 秒的 26.7 dB PSNR 下降至第 12 秒的 17.3 dB。来源： https://github.com/Yelar/noclip, https://news.ycombinator.com/item?id=50594070

**Pencil 将 AI 生成的教案转化为带旁白的白板演示。** 浏览器绘制 SVG 并播放语音旁白前，会先由校验器检查 JSON 方案。项目测试使用的是脚本替身，作者表示实际联机测试中仅测过深度求索（DeepSeek）。来源： https://github.com/VBS2004/pencil, https://news.ycombinator.com/item?id=50592137

**Frostwind 基于经校验的数据表生成像素风游戏世界。** 模型负责填充数据表，渲染器则在全图范围内统一应用相同的比例尺和配色方案。该项目现有五个可游玩世界，但不含夜间光照、对话或存档功能。来源： https://github.com/trinity-works/frostwind

**Musset 将 AI 反馈置于小说页边。** 这款 Mac 测试版应用以 Markdown 格式保存章节，支持导出 PDF 或 EPUB。其可选的编辑功能直接调用作者现有的 Claude Code 或 Codex 会话；可选同步服务费用为每月 4.99 欧元。来源： https://github.com/Musset-App/musset

## 值得一读

**在传出提示词泄露报告后，OpenRouter 下架了三家服务商。** 一名 Dragos 研究人员向多家路由平台和推理（inference）托管商发送了约 200 万条带有虚假密钥的提示词。OpenRouter 表示已移除三家服务商，并取消了 125 个端点的零数据留存资格。这一发现基于对测试密钥被使用的观测及路由推断，完整影响范围尚不明确。
来源： https://arstechnica.com/security/2026/11/a-leaky-ai-supply-chain-is-exposing-secret-user-data-at-an-alarming-rate/, https://openrouter.ai/blog/announcements/data-processing-incidents-on-inference-providers/, https://news.ycombinator.com/item?id=50595554, https://news.ycombinator.com/item?id=50582794, https://news.ycombinator.com/item?id=50585962

**Lean 与 Mathlib 贡献者核验了 Levent Alpöge 的黎曼猜想（Riemann Hypothesis）证明。** 一篇联合公告称，独立验证器和 Lean 内核已对照 Mathlib 中的命题表述验证了导出的证明。公告未就该证明是如何发现的提供任何证据。
来源： https://leanprover-community.github.io/blog/posts/riemann-hypothesis/, https://news.ycombinator.com/item?id=50589618, https://news.ycombinator.com/item?id=50590441, https://math.mit.edu/~drew/grh/, https://news.ycombinator.com/item?id=50583445, https://www.youtube.com/watch?v=zqzk43bSdDI

**Cerebras 将预填充迁移至 GPU，解码仍留在自家芯片上。** 该公司报告称，每兆瓦功耗处理的 token 数量是完全采用 CS-3 系统部署时的五倍，且生成速度未见下降。该测算仅涵盖单个共享 GPT-OSS-120B 端点，尚无合作伙伴测试结果。来源： https://www.cerebras.ai/blog/cerebras-launches-disaggregated-inference

**一位 Python 基础设施资深开发者记录了 AI 在其项目中的能力边界。** Simon Willison 推荐了 Graham Dumpleton 构建 Muru（一款面向 Python 应用的 Rust 服务器）的实录。Dumpleton 在 11月4日至21日期间发布了 18 篇开发日志，详述了哪些关键改动仍需依靠他自己的判断来主导。来源： https://simonwillison.net/2026/Nov/21/muru/

**Cloudflare 介绍两款用于决策与信息抽取的小模型。** 在接受 Latent Space 采访时，Michelle Chen 表示，Clef 能返回带概率的类型化决策，Clairic 则可在单次处理中提取类型化数值。她将 Clef 约两周的开发周期与另一款模型两年周期所作的对比属于公司单方说法。来源： https://latent.space/p/cloudflare/

**Linear 首席运营官称智能体现已创建公司半数以上的工作项。** Cristina Cordova 将这一比例与一年前的约 3% 作对比，并称 AI 起草的客服回复均需人工批准。相关数据由 Linear 自行提供，且部分 AI 功能按用量计费。来源： https://latent.space/p/linear-scaling/

## Hacker News

**ClawDOS 将编程智能体带入 DOS 系统。** 这个业余项目引发了关于在老旧 Windows 硬件上调试代码的讨论。该 HN 帖子获得 159 个赞同和 51 条评论，未包含系统性评测。来源： https://news.ycombinator.com/item?id=50586292, http://ricapar.net/ClawDOS/

**Mem 宣布停止运营。** 该公司发布了停服通知。评论区有关其笔记产品为何难以打开销路的讨论均为个别读者的看法。来源： https://news.ycombinator.com/item?id=50526537, https://get.mem.ai/blog/mem-is-shutting-down

**一篇预印本为 AI 奉承行为提出商业动因解释。** *The Hungry Butler Effect*（《饥饿的管家效应》）认为，留存用户的商业激励可能塑造了模型行为。HN 讨论与公开摘要均未提供能证实该因果关联的实测数据。来源： https://news.ycombinator.com/item?id=50583117, https://www.researchgate.net/publication/418143113_The_Hungry_Butler_Effect_Concealed_Commercial_Incentives_and_the_Erosion_of_Epistemic_Rigour_in_Large_Language_Models

**一份法院公告通报对一名律师实施为期两年的出庭限制。** 欧洲人权法院（European Court of Human Rights）指出，该律师提交了未经核实的 AI 生成引文。简报未能直接抓取原始法院页面，完整公告链接取自讨论区。来源： https://news.ycombinator.com/item?id=50579237, https://www.echr.coe.int/w/romanian-lawyer-barred-for-two-years-from-representing-applicants-before-the-court-over-unverified-ai-generated-citations

**一篇教程展示了 Maple 如何将开放权重模型与托管服务打包结合。** 作者介绍了配置方法，评论者则将其成本和隐私表现与其他服务及本地推理（inference）进行了对比。这些对比均属个人经验分享。来源： https://news.ycombinator.com/item?id=50588396, https://micahflee.com/heres-how-anyone-can-easily-use-private-open-weight-models/

## YouTube

**Ahmad Osman 探讨如何为本地 AI 挑选硬件。** 这位 Osmantic 创始人在 AI Engineer 节目中谈及内存带宽、批处理以及租用与自购 GPU 的权衡。他主张在用户自主掌控的设备上运行持续学习，这代表其个人观点。来源： https://www.youtube.com/watch?v=GKSQYbELDzw

**Ramp 称一款内部智能体编写并发布了公司约 75% 的代码。** Zach Bruggeman 在 AI Engineer 节目中讨论了共享会话、验证与代码审查。该公司给出了这一数字，但未说明如何界定由智能体编写的代码。来源： https://www.youtube.com/watch?v=MDI81OaZAD4

**Ramp 首席执行官谈及智能体采用不均的现象。** 在接受 Y Combinator 采访时，Eric Glyman 介绍了内部工具以及少数员工取得的显著效率提升。该访谈未提供独立的生产率衡量数据。来源： https://www.youtube.com/watch?v=0Hvs6-XODgU

**First Person Labs 推介个人上下文数据层。** Ken Liu 在 a16z 节目中解释了 Second 如何观察跨应用活动并将相关信息开放给指定的智能体。节目简介未提供用于检验创始人隐私主张的公开证据。来源： https://www.youtube.com/watch?v=kBJe4H_WobA

**DW Documentary 探讨 AI 带来的风险。** 这部英语纪录片采访了杰弗里·辛顿（Geoffrey Hinton）、约书亚·本吉奥（Yoshua Bengio）和杨立昆（Yann LeCun）。片中对一名青少年死亡事件的叙述取材自其母亲的证词，不构成新的研究。来源： https://www.youtube.com/watch?v=2I4qMBiK6hg

**前美国政府顾问主张利用算力领先优势加大安全投入。** 在 The Cognitive Revolution 节目中，Ben Buchanan 和 Tantum Collins 讨论了供应链、出口管制以及奖励作弊（reward hacking）等技术问题。这段对话呈现了二人的政策主张。来源： https://www.youtube.com/watch?v=6bSzdXKkE2M

**斯坦福 HAI（Stanford HAI）回顾生成式 AI 的兴起。** 研讨小组围绕第三份 AI100 报告展开讨论，涵盖推理（reasoning）模型、计算资源以及关于就业影响的争议性证据。视频简介未提供新的测算数据。来源： https://www.youtube.com/watch?v=WGjuvTvz90U

**Institute of Art and Ideas 辩论何为智能。** 嘉宾讨论了具身性以及扩展现有模型规模是否足够。这段英语视频为一场更长付费讨论的预告片段。来源： https://www.youtube.com/watch?v=DF8jyfEjymo

**PočúvAI 讨论有关加速药物研发的说法。** 这期斯洛伐克语的 Aktuality.sk 节目还谈及电力供应和个人数据问题。视频简介未提供新的药物研究成果。来源： https://www.youtube.com/watch?v=OkIoQ1imz90

## 简讯

**美国政府问责局（GAO）列出 16 项应对 AI 网络风险的选项。** 报告将这些选项归入四大目标，包括制定指南、开展研究、全生命周期监管及人才培养，并探讨了将 AI 用于防御性分析的途径。来源： https://www.gao.gov/products/gao-27-108458

**三名美国众议员勾勒针对前沿 AI 实验室的潜在监管要求。** *SAFE AI Act* 讨论稿提议实施发布前评测、事件报告和最低标准。该文件目前尚无正式法案编号，也未确定提交日期。来源： https://casrai.org/news/safe-ai-act-outline-frontier-ai-labs-2026
