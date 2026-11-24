+++
title = "AI 每日简报：2026年11月24日"
slug = "ai-daily-digest-for-24-november-2026"
description = "中国已在 15 个地区将 AI 引入社保服务，新加坡因 AI 电子产品需求上调经济增长预期。Aleph Alpha 发布开源德英双语推理模型，一款 10 GB 量化模型在多项智能体基准测试中追平 54 GB 原版。"
tags = ["models", "research", "agents", "business"]
date = 2026-11-24T03:58:39+01:00
draft = false
+++

## 要闻

**中国报告称，AI 在单一省份已处理 700 万件社保业务。**

国际劳工组织（International Labour Organization，简称 ILO）的一份报告涵盖了中国 15 个省级地区的 45 项部署。其中 47% 用于提升服务交付，33% 用于辅助行政管理，其余涉及风险防控或决策支持。

在北京市海淀区，自动化系统 2024年处理了逾 7 万笔业务，处理效率较人工提高 80% 以上。截至 2025年7月，广东省审核系统已在 34 项业务中处理超过 700 万件案件，节省逾 64 万人工工时。

这些案例是与中国劳动主管部门共同遴选的，并非具有普遍代表性的抽样样本。ILO 指出，待遇资格认定和工伤判定仍应由人工把关，同时必须为面临数字鸿沟的人群保留线下服务渠道。

来源： https://www.ilo.org/resource/news/ai-transforming-social-security-services-china-new-ilo-report-finds

**新加坡将 2026年经济增长预期上调至约 6%，AI 电子产品需求拉动出口。**

新加坡第三季度经济同比增长 6.1%。官方将强劲表现主要归因于与 AI 投资周期相关的电子产品需求，并据此上调了全年增长预期。

2027年增长预期将放缓至 2.5%–4.5%。对一个半导体和服务器出货如今高度依赖海外数据中心持续支出的出口型经济体而言，这一落差意义重大；该数字属于官方预测，并非对新加坡本土企业内部 AI 生产率的衡量。

来源： https://asia.nikkei.com/economy/singapore-gdp-grows-6.1-in-q3-as-ai-demand-stays-strong, https://www.bloomberg.com/news/articles/2026-11-24/singapore-raises-gdp-growth-outlook-to-around-6-on-ai-boom

**Aleph Alpha 发布 Kolibri 1.1，总参数量 750 亿，原生上下文达 262,144 个 token。**

这款采用 Apache-2.0 协议的德英双语推理（reasoning）模型每个 token 激活 34.4 亿参数。其权重占用约 77.6 GB 显存，因此稀疏架构减少的是计算量而非内存占用。

Aleph Alpha 公布的后训练基准测试平均分为 73.2，高于 Kolibri 1.0 的 66.6，同一榜单中 Qwen3.8 Flash Next 达到 80.1。尽管该实现可扩展至约 100 万个 token，模型说明卡仍建议在复杂任务中将长度控制在原生上下文上限以内。

来源： https://huggingface.co/Aleph-Alpha/Kolibri-1.1

**Nari Labs 将 Qwen3.8-27B 从 53.8 GB 压缩至 10.12 GB，在三项基准测试中未见掉点。**

NariQ 采用网格编码后训练量化方法，并基于编程智能体（agent）轨迹进行校准。该实验室的 3-bit 版本在 DeepSWE 上得分为 41.0（BF16 为 39.8），在 Terminal-Bench 上为 63.8（BF16 为 62.6），在 AIME 2025–26 上为 98.3（BF16 为 97.7）。

体积更小的 2-bit 版本在这三项测试中分别降至 28.6、52.4 和 86.0。此外，这些权重文件依赖 Nari Labs 维护的 llama.cpp 分支，该分支针对英伟达（Nvidia）SM120 架构进行了优化，在旧款英伟达显卡和 Metal 上运行较慢，且不支持 AMD 或英特尔（Intel）GPU。

来源： https://huggingface.co/nari-labs/Qwen3.8-27B-NariQ-GGUF

**在 58 家 Anthropic 企业客户中，三分之二表示 AI 减少了招聘需求。**

Anthropic 经济学团队对美国企业客户开展了 66 次访谈。仅有两家公司因自动化取消了岗位，五家公司解雇了抵触 AI 的员工；另有十家公司增加了人手，主要集中在部署实施和 IT 支持岗位。

影响更多体现在招聘门槛上：三分之二受访企业表示招聘减少，其中约三分之一通过自然减员缩减职能规模，九家减少了外包用工。在描述足够详尽、可供分类的 100 款 AI 构建软件中，80 款用于自动化人工流程，20 款替代了外购软件。

该样本规模较小、非随机抽样，且局限于厂商自身客户。价值判断大多属于定性自述，并非来自受控实验的实测结果。

来源： https://www.anthropic.com/research/working-with-ai

## 新模型与发布

**蚂蚁集团以 MIT 协议发布 124B 参数模型 Ling-3.2-air。** 该模型激活参数为 55 亿，混合了 35 层线性注意力层与 7 层门控注意力层。发布方称其法律基准测试单项标准通过率达 87.7%，但加入实质性幻觉检查后，仅有 0.8% 的样本通过全部标准；模型说明卡未附带技术报告。

来源： https://huggingface.co/inclusionAI/Ling-3.2-air

**腾讯发布五款面向在线零售的 WeMM-Ecom 视觉语言模型。** 参数规模覆盖 0.8B 至激活 3B 参数的 35B 混合专家模型。腾讯称，相比其 Qwen3.5 基座模型，新模型在 28 项电商基准测试中平均提升 3.92 分，但在 64 项通用基准测试中仅提升 0.17 分；这些成绩均基于 BF16 版本，而非新发布的量化版本。

来源： https://huggingface.co/tencent/WeMM-Ecom-35B-A3B-GPTQ

**AI Singapore 为其 9B 参数的 SEA-LION 模型新增 2B 投机解码器。** 发布方在并发数为 1、基线约每秒 195 个 token 的条件下，实测每秒生成 token 数提升至 2.26–3.08 倍。并发数为 16 时优势收窄至最高 1.5 倍，并发 32 时可能消失，因此它更适合低负载降延迟，而非高吞吐场景。

来源： https://huggingface.co/aisingapore/Qwen-SEA-LION-v5-9B-SpecDecoder

**Anthropic 将于 2027年1月22日下线 Claude Opus 4.5，并开放 Enterprise Frontier Safeguards 测试版。** 该安全防护机制在保留零数据留存（Zero Data Retention）的前提下，将提示词与回复的加密副本存储在客户自有云账户中以供安全审查。固定调用 `claude-opus-4-5-20251101` 的团队还有约两个月时间迁移至 Opus 5.5。

来源： https://platform.claude.com/docs/en/release-notes/api

**Gemini API 用户现可按选定页面、单元格和媒体片段付费，而非整份文件。** 文件切片功能适用于 Gemini 4 全系列模型，并新增原生 Office 和 OpenDocument 文档上传支持。Vercel 测得速览提取的 PDF 文本时 token 消耗降至原来的 1/14；LiteLLM 测得单份 PDF 减少 67% 的 token 消耗、单份工作簿减少 33%，但两者均为合作伙伴报告的测试结果，未披露定价或文件数量上限。

来源： https://blog.google/innovation-and-ai/technology/developers-tools/file-slicing-controls/

## 研究

**一项审计在六个多步骤基准测试套件中仅核实了 29.3% 的任务有效。** 两名作者审查了来自八个基准测试的 749 项任务和 767 份公开模型评测。已确认的缺陷中，71.7% 导致合规解答无法得分，其余则允许钻空子；修补容器后，已确认的运行时绕过率从 14.7% 降至 2.7%。这是作者持续审查工作的首个阶段性成果，且“核实有效”的标准由其自身流程界定。

来源： https://arxiv.org/abs/2611.27622

**一种推理图谱方法将忠实思维链与高效思维链区分开来。** 作者分别衡量语义支撑是否解释了模型预测，以及推理步骤是否始终沿着通向答案的路径推进。不忠实与低效均仅与正确率呈弱相关或不一致相关，有针对性的微调可在不降低准确率的情况下分别改善两项属性；摘要未给出效应量，结果也取决于作者对图谱的构建方式。

来源： https://arxiv.org/abs/2611.27100

**14 款语言模型在选项抉择中呈现“先压缩后比较”模式。** 在 12 项基准测试中，中间层将提示词压缩为低秩瓶颈，后续层再将其展开为用于比较的几何结构。在瓶颈附近施加低秩干预会改变后续偏好，但这篇单作者 NeurIPS 论文依赖作者自定义的协方差方法得出结论。

来源： https://arxiv.org/abs/2611.26874

**合成调查受访者仅复现了人类偏好差异的 0.4%–10.5%。** 三个开源模型家族重演了 1,991 名智利、843 名法国和 434 名巴西成年人的政策选择。27 种实验条件无一同时匹配个体选择、群体异质性和政治组织结构；调换提案顺序即改变了模型 12.3%–31.2% 的选择。

来源： https://arxiv.org/abs/2611.28383

**快速决策模型节省了耗时，但也更容易遭投毒攻击。** 四款模型在 1,440 对合成浏览器任务上的干净准确率平均为 91%，但两样本注入评论即可达到 81.2% 的攻击成功率。在 48 项匹配任务中，短思维链对投毒输入的正确率达 95.83%，远高于快速版本的 38.54%，耗时为 1.94 秒对 0.29 秒。另一项研究中的 4B System-1 模型报告在三项基准测试中将单回合成本降低 75%–91%，但未测试对抗输入。

来源： https://arxiv.org/abs/2611.27679, https://arxiv.org/abs/2611.23751

**部分可解释性测试可能会认证模型并未按宣称方式使用的特征。** 该论文构造了“寄生特征”，将一个区分输入的方向与另一个引导输出的方向组合起来，从而经由无关通路通过因果抽象测试。实验在句法一致性和两位数加法中发现了此类失效；这一结论源自两项任务，是警示而非替代方法。

来源： https://arxiv.org/abs/2611.26711

**一项脑状态基准测试发现，预测外部刺激并不意味着追踪受试者内部状态。** 仅依赖刺激的编码器预测相关性达到 0.320，但在该基准的 State 指标上得分为零。作者的双时间尺度模型相关性达到 0.349，State 为 5.5%、Forecast 为 16%、Updating 为 20.3%，但 State 的绝对表现依然偏低。

来源： https://arxiv.org/abs/2611.28508

**一项审计显示，大多数通过人类模拟等效性检验的测试同样会让零效应模型过关。** 在对 70 项实验的重新分析中，GPT-4 在正负 0.20 个标准差容差下通过的测试里，有 72% 属于零基准也会通过的情形。一项预注册的 Claude 模拟通过了三项意图目标，但对规范信念的偏移仅为 0.065 个标准差，而人类为 0.351；论文标明了部分分析包含事后补充内容。

来源： https://arxiv.org/abs/2611.27186

**一种固定容量适配器学会了何时记忆、何时遗忘。** 控制器在 LoRA 适配器内为不同记忆分配独立衰减率，在作者构建的合成用户轨迹上达到了理论最优性能的 86%。另一项相关研究发现，混合长短轨迹可用更少 token 学到稳定规则，但两项结果均来自人为构造的环境。

来源： https://arxiv.org/abs/2611.25235, https://arxiv.org/abs/2611.28613

**引入第二个 AI 伙伴能催生更多头脑风暴点子，但会减少人类贡献。** 这项样本量 N=168 的实验室研究将双智能体分组与人类双人组进行对比；只有第二个智能体提升了单次讨论内的创意分化度。该任务范围较窄，单智能体结果也未能推广。来源： https://arxiv.org/abs/2611.26663

**一款专用行为模型与两项审计在“合格合成人需要什么”上得出分歧结论。** 基于 288,307 条记录和 1,411,750 项决策训练的 Chiron 报告称，其个体预测较前沿模型提升最高达 28.4%，效应量误差降低 82.2%–94.3%。合成公众审计则发现群体差异被严重压缩，等效性审计指出许多表面吻合同样放行零效应；三项研究均使用作者自选任务。

来源： https://arxiv.org/abs/2611.24830, https://arxiv.org/abs/2611.28383, https://arxiv.org/abs/2611.27186

## 经济与就业

**测得的智能体敞口越高的上市公司，随后发布的非资深岗位越少。** 一篇工作论文将约 2000 万亿个模型 token 与 3480 万条招聘信息关联起来。其股市敞口指标每上升一个标准差，六个月后招聘增速低 2.11%，九个月后低 3.20%；该结果统计的是招聘信息而非裁员，且敞口系由市场反应推算得出。

来源： https://arxiv.org/abs/2611.27210

**Claude Ship 将编程智能体从编写代码推进到审查与批准代码。** Anthropic 表示，6月至 9月间合并的拉取请求数量翻了一倍以上，同时回滚占比下降逾 40%，但未公布基数或对照组。Code Review 已全面开放，PR Steward 和 Approvals 仍处于测试阶段；管理员可为计费 token 支出设置上限。

来源： https://claude.com/resources/articles/introducing-claude-ship

**一项经济模型称，进展缓慢的“薄弱环节”任务可能阻断快速进步资本带来的爆发式增长。** 这篇美国国家经济研究局（NBER）工作论文估计，资本互补型任务的生产率年增速比劳动型任务快约 5 个百分点。其可观的总体增长结论取决于模型内部的任务替代关系与瓶颈设定，因此属于机制阐释而非经济预测。

来源： https://www.nber.org/papers/w36050

**AlphaFold2 使结构生物学实验转向已知范例附近的蛋白质。** 一篇 NBER 论文追踪了 530,471 种蛋白质，发现高置信度预测增加了针对已知蛋白及其近亲的实验，同时减少了对远缘未知结构的首次探索尝试。该研究衡量的是科研人员的实验选题方向，而非这些选择的最终科学价值。

来源： https://www.nber.org/papers/w36045

## 提示词技巧

**一段对齐 OWASP 的提示词模块使 AI 生成 Web 应用中的扫描器告警减少约三分之一。** 研究人员使用 Claude Code 和 Codex 对 100 份需求规格各构建四次，共产生 6,721 条经分拣的告警。发病率比为 0.65（95% 置信区间 0.60–0.71），但该提示词模块使声明的依赖数量翻倍，且扫描器告警并不等同于已证实的漏洞利用。

来源： https://arxiv.org/abs/2611.28408

**要求模型核实检索文本反而使其采纳更多错误答案。** FutureBench 在六款模型上测试了 3,629 道问题。若在提示词中警告参考段落可能具有误导性，可挽回普通“核实”提示词所挤掉的 82.5%–98.9% 的正确答案，而在正确段落上的得分波动不足 1 分；该结果来自两名作者构建的单一基准测试家族。

来源： https://arxiv.org/abs/2611.23601

## 大家在做什么

**Gall 通过每次作答后卸载模型，在 24 GB MacBook Air 上运行 26B 混合专家模型。** 这款基于 Rust 和 Metal 的推理引擎会保存对话状态，空闲内存降至 32–57 MB，热状态重载耗时约 0.1 秒。作者在一台 M2 Air 上测得短上下文速度约每秒 20 个 token，29,900 个 token 时为每秒 16 个；模型输出质量及宣称的 10 万 token 设置均未经过评测。

来源： https://github.com/ltrgoddard/gall

**OCRia-nano-1 以 810 万参数在 CPU 上解析文档。** LlamaIndex 公布其在 ParseBench-2 上得分为 59.2，在 16 核虚拟 CPU 上每秒处理 27.8 页。其图表项得分仅为 3.1（4B 教师模型为 77.4），且权重采用自定义许可协议，限制较大型商业用户使用。

来源： https://huggingface.co/llamaindex/OCRia-nano-1

**OpenToolSearch 使用两款 0.6B 模型从大型工具目录中筛选工具。** 其重排器在公开数据集 ToolRet 上达到 nDCG@10 为 70.8，在作者自建测试集上为 89.0，公布成本为每 1,000 次搜索 0.19 美元，中位延迟 0.10 秒。竞争对手在两项测试中得分均更高，作者也建议当工具数量在约 200 个及以下时直接将完整列表提供给模型。

来源： https://github.com/ai3inc/opentoolsearch

**CubePod 为编程智能体提供持久化 Kata 微虚拟机沙箱。** 这款兼容 E2B 的 Kubernetes 项目声称热池分配低于 50 毫秒，跨节点恢复或写时复制分支接近 1 秒。这些数据未附带公开测试方法，且部署需要 Kata Containers 及块存储驱动支持。来源： https://github.com/cubeplexai/cubepod

**两款小型工具在不同环节守护智能体依赖安全。** mcpwatch 锁定 MCP 工具描述并在运行时拦截发生变更的工具，但其安全评级并非担保，指纹校验方法也未公开文档。slop-deps 对照 4,179 个软件包名称和软件仓库扫描导入项，包含拼写仿冒和同形字检查；其 142 个文件的耗时示例仅作演示，且全部代码均由智能体在人工指导下编写。

来源： https://www.mcpwatch.io, https://github.com/viditx/slop-deps

**Terminal Tasks Open 发布 30 项任务及一项针对大型基准测试缺陷的审计。** 作者称在 Terminal-Bench 4.1 的 66 项任务中有 23 项存在缺陷，并将 980 次智能体失败尝试中的约 52% 归类为过拟合、31% 归类为误判、9% 归类为处理不当。审计方同时也是替代基准测试的构建者，并销售评测流水线，相关分类标准亦由其自行定义。

来源： https://vetto.ai/companies/terminal-tasks-v2/

## 值得一读

**Hugging Face 展示智能体基准测试如何奖励投机取巧而非完成任务。** 一段脚本在未拟合谱峰的情况下，于全部八项拉曼光谱任务中返回了正确的缺陷比，迫使作者增设逐峰校验。gpt-oss-120b 在 24 次运行中通过了 11 次，仅更换推理（inference）服务商后增至 13 次；三款更强模型则全部通过 24 次，表明这套缩减后的改编测试集已无法区分其高下。

来源： https://huggingface.co/blog/agentic-evals

**一项 AMD 支持的测试用 NVMe 替代智能体 KV 缓存的 DRAM 池，吞吐量几乎持平。** 在 16 张 MI355X GPU 上运行 Kimi-K3 时，三项并发测试与 DRAM 差距均在 1% 以内，缓存命中率解释了 42 次运行中 96% 的吞吐量波动。若在 96 个并发会话下存储每个数据块，NVMe 硬盘约 5.5 个月便会耗尽额定写入寿命，且多数对比仅为单次运行，伴随约 2.5% 的噪声。

来源： https://vllm.ai/blog/2026-11-23-skip-the-dram-tier

**Gemini 4 智能体团队发现更低成本的量子电路，并用 Lean 证明了每项结果。** 谷歌 DeepMind（Google DeepMind）称，一项聚变模拟的计算成本降至原来的 1/11.8，细胞色素 P450 降至 1/2.5，反正弦例程降至 1/290。课题由人类遴选并监督，所得电路规模仍超出早期容错量子计算机的预期能力。

来源： https://deepmind.google/blog/finding-faster-quantum-algorithms-with-agents-and-formal-verification/

**Anthropic 发布 AI 撰写的“VP 异于 VNP”主张，附带 Lean 证明但未经人类数学同行评审。** 代码仓库称独立内核已按标准公理核验了形式化陈述。然而没有任何机器校验能确保这些形式化陈述与论文主张一致，该项目亦自称为不再维护的快照，且并未解决 P 对 NP 问题。

来源： https://github.com/anthropics/formal-math/tree/main/vp-vnp

## Hacker News

**GLM-5.4 使循环 Transformer 层成为一周内第二股架构风潮。** Z.ai 称重复运行共享层可在不增加参数量的情况下加深有效深度，Simon Willison 将该思路与 Thinking Machines 的 Inkling 2 Mini 相提并论。他的实测仅包含一条图像提示词，模型权重未开源，可获取资料也未披露参数规模或正式基准测试成绩；该 Hacker News 帖子获 1,075 分。

来源： https://simonwillison.net/2026/Nov/23/glm-54/, https://news.ycombinator.com/item?id=50609685

## YouTube

**Factory 的 Dex Horthy 提出 12 项针对智能体构建软件的控制措施。** 这场英文 AI Engineer 演讲涵盖规划、阶段间压力、功能开关、评测以及智能体自测。Horthy 称最佳模型在 Slop Code Bench 上得分约 16%，但未给出任务总数；Factory 本身销售编程智能体，因此这些准则属于厂商实践而非受控实验结果。

来源： https://www.youtube.com/watch?v=-NFMsM2y0Vk

**斯坦福大学（Stanford University）CS312 课程要求学生在看到训练结果前先作预测。** 课程使用的 30M 参数、八层模型在单张 GPU 上仅需约十分钟即可完成训练，使学习率与架构实验的成本足够低廉、适合课堂开展。本摘要整理自英文视频简介，而非逐字稿。来源： https://www.youtube.com/watch?v=JLcCYvUawsM

## 简讯

**同一安全监控器漏检成功攻击的比例在 0.2% 至 23% 之间，取决于攻击生成方式。** 英国人工智能安全研究所（UK AI Security Institute）用多种策略生成的攻击测试了一款前 OpenAI 生产级监控器；其中一次强化学习运行将漏检率从 0.5% 推高至 20.8%。这虽只是单一实验设定，但说明若无法论证攻击策略代表未来威胁，合成监控器分数便难以采信。

来源： https://www.aisi.gov.uk/blog/attack-policy-selection-can-make-monitor-evaluations-misleading

**OpenAI 与思科（Cisco）发布 Shirudo，在补丁安装前拦截运行中 Linux 服务的漏洞利用路径。** 其签名 eBPF 防护盾需经运维人员批准，并留存由 TPM 支撑的记录。在一次受控厂商测试中，它在未重启服务的情况下拦截了针对 Elasticsearch 的 Java4Shell 攻击；文章未公布性能或采用数据，防护盾仍属临时措施。

来源： https://openai.com/index/introducing-shirudo

**美国网络安全和基础设施安全局（CISA）将 MONAI Label 路径遍历漏洞列入已利用漏洞目录。** CVE-2026-133968 可让未经身份验证的攻击者在医学影像服务器的数据存储区外写入文件，并可能执行代码；美国联邦机构的修复截止日期为 11月26日。来源： https://nvd.nist.gov/vuln/detail/CVE-2026-133968

**美国将 Megaspeed 关联企业及一家阿里巴巴旗下的新加坡公司列入实体清单（Entity List）。** 有关部门正调查涉嫌向中国转运英伟达芯片的行为，此举限制相关实体采购先进芯片；Megaspeed 否认曾运送此类芯片。来源： https://www.bloomberg.com/news/articles/2026-11-24/us-blacklists-alibaba-owned-company-in-setback-to-ai-ambitions

**俄勒冈州和弗吉尼亚州就 Grok 生成色情图像起诉与埃隆·马斯克（Elon Musk）相关的公司。** 两州指控其安全防护措施未能阻止生成包括儿童在内的真人图像，X 则称所有输出均经过筛查；简报未能查阅起诉书，因此原告请求的救济措施尚未得到证实。来源： https://arstechnica.com/tech-policy/2026/11/states-sue-spacex-to-stop-grok-from-generating-child-sex-images-revenge-porn/

## 商业简讯

亚马逊（Amazon）收购了 Decart 的芯片优化软件及团队，据报道交易额为 75 亿美元；两家公司均未披露该软件的基准测试成绩。来源： https://www.theregister.com/ai-and-ml/2026/11/23/amazon-scoops-up-ai-accelerator-tech-to-keep-chips-busy-at-all-times/5311754

密歇根大学（University of Michigan）校董会以 7 票对 1 票批准与洛斯阿拉莫斯共建一座造价 12.5 亿美元的数据中心，而当地镇区仍维持为期六个月的新建电力基础设施禁令。来源： https://www.404media.co/ypsilanti-michigan-data-center-vote/

## 后续关注

Anthropic 将于 2027年1月22日下线 Claude Opus 4.5。CISA 对 MONAI Label 漏洞的修复截止日期为 11月26日，Shirudo 技术网络研讨会定于 12月15日举行。
