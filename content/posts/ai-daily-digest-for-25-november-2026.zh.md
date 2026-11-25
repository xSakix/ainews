+++
title = "AI 每日简报：2026年11月25日"
slug = "ai-daily-digest-for-25-november-2026"
description = "一项研究发现，部分企业采用 Copilot 后减少了初级技术岗位的招聘，而 Indeed 记录到软件开发职位空缺回升。百度开放 ERNIE 5.5 Flash 的权重，Anthropic 研究人员提出用单个神经元审计模型。"
tags = ["models", "research", "business", "projects"]
date = 2026-11-25T04:03:43+01:00
draft = false
+++

## 要闻

**因合同续审而采用 Copilot 的企业，每季度新招的技术人员减少了 29%。** 一篇预印本追踪了 5,414 家跨国企业，美国 38% 的程序员在这些企业工作。研究利用事先确定的软件采购周期做自然实验。采用 Copilot 一年后，这批企业招聘的技术人员减少，降幅主要集中在需要大量编程的初级岗位。

研究没有发现离职人数、技术人员总数或职位空缺时长发生变化。它衡量的是大型企业的招聘，并未统计整个经济体的裁员情况，也尚未经过同行评审。Indeed 独立收集的招聘数据表明，整体市场的走势恰好相反：过去一年，美国软件开发岗位的招聘广告增加了 23.4%。

来源： https://arxiv.org/abs/2611.31083

**美国软件开发岗位的招聘广告一年增加了 23.4%，但仍比 2020年2月少 18%。** Indeed 的整体招聘广告指数在 11月13日达到 106.2，为 2025年4月以来最高值，比一年前高 5.1%。以 2020年2月为基期、基数为 100，软件开发指数仅为 82，工程类岗位指数则为 149。

47 个行业中，只有 29 个超过疫情前的基准水平。提及 AI 或生成式 AI 的招聘广告占比升至 7.8%，上一个高点是 2022年的 3.3%。该指标统计 Indeed 广告中的关键词，无法说明这些变化是否由 AI 引起。

来源： https://hiringlab.indeed.com/2026/11/24/us-labor-market-snapshot-november-2026/

**百度开放了 ERNIE 5.5 Flash Preview 的权重，模型有 140 亿激活参数，支持 100 万 token 上下文。** 这款采用 Apache 2.0 许可证的混合专家模型共有 2,800 亿参数。每处理一个 token，模型从 512 个可路由专家中选取 10 个，另有 1 个共享专家。百度提供 FP8、BF16 和专家权重采用 FP4 的版本，以及用于推测解码的预测头。

百度公布的分数为 BrowseComp 87.4 分、DeepSWE v1.1 71.2 分、Terminal-Bench 4.0 46.5 分。模型说明称，这是一个中间版本，后训练仍在进行。分数来自百度自己的评测和对比，没有独立测试结果。

来源： https://huggingface.co/baidu/ERNIE-5.5-Flash-Preview

**Ternary Bonsai 2.5 将一个 270 亿参数的智能体模型压缩到 5.9 GB，同时缩小了与完整精度模型的准确率差距。** PrismML 将 Qwen3.8-27B 的每个权重压缩至 1.76 比特。据该公司称，压缩后的模型在 SWE-bench Verified 上得到 75.6 分，53.8 GB 的 FP16 基础模型为 80.6 分；在 AppWorld 上，两者分别为 90.5 分和 93.2 分。

此前的 Bonsai 在这两项测试中分别得 60.8 分和 51.2 分。新版采用 Apache 2.0 许可证，可通过 llama.cpp 和 MLX 运行。据厂商称，在 RTX 4090 上使用草稿预测头时，每秒可生成 204 个 token。Terminal-Bench 上的差距仍较大：新版 60.1 分，基础模型 70.8 分。

来源： https://prismml.com/news/bonsai-2-5-27b

**Anthropic 研究人员认为，单个神经元比以往研究所显示的更容易解释，在安全审计中也更有用。** Jasmine Shone 和 Lisa Dunlap 把多层感知机中的每个神经元看作一个受上下文控制的引导向量。她们既观察什么输入会激活它，也检查它向残差流写入什么。在抽样检查中，单个神经元同时贡献两个无关概念的情况最多约占 1%。

配套实验用神经元检测概念、引导行为，并为审计提供线索。在 16 个评测集中的 4 个上，神经元探针与用 400 个标注样本训练的线性探针表现相当。用神经元引导和用训练得到的向量引导，都有 21% 的回答出现目标行为。在对 58 个修改过的适配器开展盲审时，审计系统识别出其中 75% 的隐藏行为，仅检查模型输出时则为 40%。研究对象为开放模型和专门构造的实验模型，未涉及已部署的前沿系统。

来源： https://alignment.anthropic.com/2026/neuron-basis-theory/, https://alignment.anthropic.com/2026/neuron-basis-applications/

## 新模型与发布

**OpenAI 表示，GPT-6 系列模型能利用通用推理和代码设计结合蛋白。** 在湿实验中，322 个小型结合蛋白设计中有 35 个能与 5 个靶标之一结合；182 个重新设计的抗体环中有 128 个能结合 IL-4Rα。在 PoseBusters 分子对接测试中，GPT-6.2 得分为 93%，DiffDock-L 为 50%。候选设计仍需专用模型筛选。在完整蛋白质结构预测上，模型的 TM-score 比 ESMFold2 低 0.38 至 0.93。实验测量的是结合情况，未检验稳定性、特异性或安全性。该模型是内部研究系统，尚未公布访问途径。 来源： https://openai.com/index/gpt-6-models-demonstrate-intrinsic-protein-design-capabilities/

**AuroraAI 将一个 4 亿参数的混合专家模型压缩至 27.5 MB，并公布了准确率损失。** HellaSwag 得分从 38.36 降至 28.17，ARC-Easy 从 48.06 降至 39.90，其 Intelligence Index 从 21.38 降至 10.83。每个专家权重仅用半比特表示，可以节省存储空间。要减少计算量，还需有支持二进制矩阵的计算内核。 来源： https://huggingface.co/AuroraAI-Research/Aurora2-400M-A20M-QAT

**中国电信发布 Xing4.1-Preview，这是一个在 8,192 枚昇腾 910C 芯片上训练的 2,850 亿参数稀疏模型。** 每个 token 激活 170 亿参数，原生支持 100 万 token 上下文。实验室公布的得分为 SWE-Bench Pro V2 Hard51 上 74.5 分、Terminal-Bench 2.1 上 80.8 分，同时提醒各项对比使用的测试环境不同。 来源： https://huggingface.co/XingChen-AGI/Xing4.1-Preview

**腾讯发布 OmniEVIE-4B，可跨文本、图像、文档、视频和图形界面检索信息。** 模型能返回证据的位置，例如页面区域或视频时间戳。腾讯报告称，模型在 MMEB-V3 上得分为 60.68，在单个 CPU 线程上检索 100 万条记录，每次查询耗时 54.2 毫秒。这一规模的索引约占 8.8 GiB。 来源： https://huggingface.co/tencent/OmniEVIE-4B

**KRAFTON 发布了 Raon-1 mini 的最终权重。** 这款韩国模型共有 288 亿参数，其中 43 亿为激活参数，上下文窗口为 262,144 个 token，可选 6 档推理强度。KRAFTON 公布的自测成绩为 SWE-bench Verified 71.0 分、GPQA Diamond 86.0 分。 来源： https://huggingface.co/KRAFTON/Raon-1-mini

**OpenAI 调整了动态别名 `chat-latest` 的指向，并新增医疗配置。** 该别名现在随 ChatGPT 的最新模型更新，OpenAI 建议生产应用使用 GPT-6.2 系列的固定模型名。医疗配置增加了临床工作环境和医学来源搜索索引。使用动态别名时，即使应用中的模型标识不变，行为和费用也可能变化。 来源： https://developers.openai.com/api/docs/changelog

**谷歌 DeepMind（Google DeepMind）发起竞赛，征集 Humanity's First Exam 的考题。** 该基准测试以 544 道基础文本和图像题为起点，覆盖 20 种能力。主办方请 Kaggle 参赛者提交当前模型仍会答错的简单问题。公告未提供基线分数或详细评分办法。 来源： https://blog.google/innovation-and-ai/models-and-research/google-deepmind/humanitys-first-exam/

**Ollama 和 llama.cpp 更新了推理引擎。** Ollama 0.40.18 提升了 Inkling 2 在 Metal 上的速度，并停止支持 JetPack 5。llama.cpp 报告称，b12701 版让 Inkling 2 Mini 的预填充速度在 MI300X 上提高 14%–18%，在 B200 上提高 25%–37%。 来源： https://github.com/ollama/ollama/releases/tag/v0.40.18, https://github.com/ggml-org/llama.cpp/releases/tag/b12701

## 研究

**OpenAI 新增 9 篇借助 AI 撰写的数学手稿，声称在矩阵乘法、线性规划和多面体直径等问题上取得结果。** 据项目仓库介绍，一个尚未发布的模型针对 375 类问题生成了 730 篇手稿，每项获采纳的结果约耗费 ChatGPT Pro 三小时的思考时间。约 42% 的主要结果已用 Lean 形式化，其余尚未形式化，所有结果都还没有完成常规的独立评审。 来源： https://github.com/openai/math/blob/main/CONTENTS.md

**模型可以在内部进行多层计算，再给出条理清晰的解释。** 研究人员训练了简化的实验系统，其隐藏计算的深度最多是外显解释所暗示深度的 5 倍。一个能力较强的监控系统未能还原隐藏目标，而替换特定激活值的实验揭示了计算发生的位置。这些结果来自专门构造的任务，不代表前沿模型的日常使用情况。 来源： https://arxiv.org/abs/2611.31015

**GPT-5.6 Sol Ultra 给数学猜想排序，比估计自身判断的可靠程度更在行。** 模型选出了 100 个猜想，其中 87 个接受核查。模型给出的平均成功概率为 0.617，实际成功率为 0.103，布里尔分数为 0.351。不过，ROC 曲线下面积达到 0.714，说明排序仍有参考价值。实验只涉及模型自行选择的一个数学领域。 来源： https://arxiv.org/abs/2611.28827

**研究人员找到一个与置信度相关的内部方向，改变它会影响推理模型回溯思路的时长。** 在 3 个 320 亿参数模型上施加引导后，回答长度的变化从缩短约 1,300 个 token 到增加约 2,500 个 token 不等，提出的答案数量也相应增减约 4 个，准确率变化很小。这种线性信号尚不足以证明已部署模型把它当作显式的置信度变量。 来源： https://arxiv.org/abs/2611.29265

**有缺陷的测试掩盖了智能体在 SWE-Gym 上的进步。** 在智能体从未解出的任务中，74% 含有会误判正确解答的隐藏测试；在至少解出过一次的任务中，这一比例为 20%。修复测试后，两个模型系列在预留任务上的得分提高了 2.4–2.7 分。 来源： https://arxiv.org/abs/2611.30207

**GitHub 公开数据中含有隐藏的模型指令，大多来自正常的工作流编排。** 一次扫描在 1.45 亿条数据中找到 2,281 例，约合每百万条 16 例，另发现 107 个相关 README 文件。三分之二是项目方自己的工作流指令。估计每 330 万条数据中才有一次攻击。一个小模型有 19% 的时候会遵循恶意指令，去掉注释后该比例降至零。 来源： https://arxiv.org/abs/2611.28763

**当两个分布十分接近时，PyTorch 计算的 KL 散度可能不准确，甚至出现负值。** 在 850 万组输入中，数值接近 10^-7 的 FP32 案例有超过 85% 出现至少 1% 的相对误差。在更小的尺度下，约 30% 算出负值。研究人员提出的修正方案消除了超过 97% 的错误，也改变了部分蒸馏预测和计算回路排名。 来源： https://arxiv.org/abs/2611.30835

**如果被告知论文全部由 AI 完成，AI 审稿系统给出的分数会更低。** 6 个审稿模型根据 9 种作者贡献声明，为 150 篇 ICLR 投稿给出共 23,652 次评分。声明全部工作出自 AI 会稳定地导致扣分，普通的 AI 辅助则没有这种影响。这是模拟的 AI 评审，没有考察人类程序委员会的决策。 来源： https://arxiv.org/abs/2611.30410

**一个简单的动作过滤器将学习型世界模型的穿墙比例从 74% 降至 16%。** 对 6 个模型的测试表明，即使生成的动作无视约束，模型状态中仍可能编码了这些约束。过滤后仍有 16% 失败，说明过滤并未修复生成器本身。 来源： https://arxiv.org/abs/2611.27963

**在模型中可以线性读出的字母信息，约有 70% 已存在于词嵌入中。** 研究测试了 16 个规模介于 6 亿至 140 亿参数的模型。模型越大，后续层补充的答案相关信号越强。能线性读出某项特征，并不能证明模型实际使用了它。 来源： https://arxiv.org/abs/2611.30094

**两项研究检验了记忆系统的隐私风险及其遭受数据投毒的可能性。** FORGETMENOT 开展了 3,800 次会话。让记忆控制选项可见后，系统保留的属性减少了 20%。隐蔽指令则使 Copilot 和 Claude 保留的敏感信息分别增加了 25% 和 15%。另一项配套攻击研究从组织内部针对共享记忆。两项研究都在受控系统中进行，没有测量真实生产环境中的入侵事件。 来源： https://arxiv.org/abs/2611.28298, https://arxiv.org/abs/2611.30965

## 经济与就业

**资深开发者表示，相较于代码产出，AI 对工作掌控感和专注力的影响更大。** 一篇基于调查的预印本发现，开发者减少了与同事讨论、拆解问题、查阅文档和使用调试器的频率，切换任务却更频繁，深度专注也有所减少。摘要称，核心编程活动的平均差异较小，经验更丰富的人感受到的变化较大。摘要未给出样本量。 来源： https://arxiv.org/abs/2611.27947

**一项研究归纳出 35 条规则，说明开发者何时可以把任务交给 AI，何时应自行判断。** 研究人员调查了微软（Microsoft）的 860 名开发者，一年后又邀请来自微软、GitHub 和辉瑞（Pfizer）的 258 名开发者检验这些规则。第二组中有 89% 表示愿意采用。得到认同并不能证明这些规则能改善工作成果。 来源： https://arxiv.org/abs/2611.28996

**一项针对中等收入经济体的模型研究显示，引进国外智能体可能提高每个带薪工时的产出，却使国内收入下降。** 根据巴西和墨西哥的经济核算数据，论文估计，当供应商议价能力指标超过约 0.15 时，本地服务业增加智能体使用量可能降低国内增加值。这是校准理论模型得到的推算，并非实际观察到的劳动力市场结果。 来源： https://arxiv.org/abs/2611.31518

**iFood 称，其编程智能体平台覆盖 1.5 万个代码仓库，每次运行成本约 4 美分。** 一次 REST 调用会为 GPT-5.6 Luna 创建隔离环境，随后按确定的步骤克隆仓库并提交合并请求。首个应用会扫描有漏洞的依赖项并尝试修复。iFood 表示，成功修复的数量增加到原来的两倍以上，但未公布基数。这篇案例来自 OpenAI 的客户网站。 来源： https://openai.com/business/customer-stories/ifood

**sudo L7 测试常规编程基准忽略的工程判断力。** 针对私有代码库的 60 项任务设有 1,287 条专家标准，其中过半关注功能正确性以外的问题。Claude Fable 5.2 的尝试通过率为 52.2%。19 个模型中有 13 个不超过 18.9%。逐项判断是否符合标准时，评分智能体与工程师有 85%–86% 的结论一致。 来源： https://arxiv.org/abs/2611.30517

## 大家在做什么

**Hyper Elements 让智能体可以返回 React 组件，替代文字或 JSON。** 每类需求各测试 5 份简报。作者称，输出 token 数的中位数分别降至 React Email 的 1/3.4 和 Canvas 的 1/1.8。这项小规模对比由项目团队维护。 来源： https://github.com/hyper-elements/hyper-elements

**MyGraph 用必须注明出处的知识图谱为智能体构建记忆。** 这个尚在开发的项目称，使用 GPT-6.1 Terra 时，MyGraph 在 LongMemEval 上得分为 0.90，直接给出完整来源上下文为 0.86；每次查询成本分别为 0.015 美元和 0.095 美元。这些数据来自开发者本人，代码仓库仍处于早期阶段。 来源： https://github.com/dieron/mygraph

**Genesis 检查编程智能体编写的测试能否揭示它们声称覆盖的缺陷。** 在 5 个 Python 项目的 10 次提交中，评定的覆盖率从 79% 升至 88%，发现的测试不足的行为从 8 种增至 38 种。这项评测规模较小，评分由模型完成。 来源： https://github.com/GenesisAgentInfra/genesis

**LoopedWSP 反复使用同一组 19,936 个学习得到的权重，解决不同规模的谜题。** 作者称，在模型辅助下开发耗时 39 分钟、花费 19 美元后，系统在 30×30 的任务上取得 100% 的成绩，Claude 为 26%，常规训练的基线模型为零。这些说法和图表均来自项目仓库。 来源： https://github.com/mbzuai-oryx/LoopedWSP

**PiPod 在浏览器标签页中运行本地智能体。** 可运行的演示将模型推理和工具都放在客户端，文件留在设备上。项目没有提供对比测试。 来源： https://pipod.browserpod.io/

**Brickie 在 AWS 和 Kubernetes 上提供可持久保存的开发沙箱。** 这个处于测试阶段的项目为环境保存快照，智能体可以暂停后恢复工作，无需重建先前的状态。 来源： https://github.com/hatchet-dev/brickie

## 值得一读

**《Import AI》将科研智能体评测与华为昇腾硬件的一项新基准联系起来。** Jack Clark 在第 482 期分析了 SciResearch 和 AscendGym，讨论它们如何尝试在真实科研场景和非英伟达（Nvidia）计算环境中检验智能体。这份通讯提供解读，基准成绩仍是各研究团队自行报告的结果。 来源： https://jack-clark.net/2026/11/24/import-ai-482-sci-research-ascendgym-and-ai-driven-science/

## Hacker News

**OpenAI 的数学手稿引发了围绕优先权和证明范围的争论。** 两个讨论串分别涉及矩阵结果的 Lean 证明是否涵盖完整命题，以及 OpenAI 和 Anthropic 谁先证明 VP 与 VNP 分离。根据部分评论者对时间戳的比对，Anthropic 约早 5.5 小时。目前，优先权说法和数学结果都未经独立审查。 来源： https://news.ycombinator.com/item?id=50637220, https://news.ycombinator.com/item?id=50632756

**一家 API 客户称，Anthropic 要求其在 24 小时内反驳有关模型蒸馏的指控。** 这家未具名公司表示自己不训练模型，怀疑是自动回归测试触发了警报。回复者提到类似的规则执行问题，并建议路由系统兼容多个提供商。Anthropic 当时尚未在讨论中回应，因此这家公司的说法仍未经核实。 来源： https://news.ycombinator.com/item?id=50630809

## YouTube

**Jarred Sumner 讲述了如何在 5 次重写后，将智能体编写的数百万行改动合入 Bun。** 这位 Anthropic 工程师称，Claude Code 的内存占用约降至原来的四分之一，启动速度翻倍。视频简介没有提供比较基线。他强调，监督 140 个编程智能体要靠既有测试、每小时更新的评分表和模糊测试。 来源： https://www.youtube.com/watch?v=TvsF67C2F54

**SWE-bench 联合创建者 John Yang 解释了智能体为何在示例轨迹之外还需要环境。** 他在斯坦福大学（Stanford University）的讲座中区分了监督训练使用的演示，以及强化学习需要的任务、动作空间和验证器，随后介绍了来自人类、从现有资料中挖掘、合成和由模拟用户产生的数据。 来源： https://www.youtube.com/watch?v=HbgZFwWj4vY

**Tatsunori Hashimoto 说明了调参不充分如何让新优化器显得优于 AdamW。** 据斯坦福大学的讲座简介，重新调整学习率后，AdamW 追平了 MARS；调好权重衰减后，它又超过了 Lion。讲座还提醒，规模定律可能在最大规模的运行中失效。这些结论来自讲座简介的概述。 来源： https://www.youtube.com/watch?v=tc5AVfyWkVs

**Noam Brown 回顾了自己从博弈论转向语言模型推理的经历。** 在红杉资本（Sequoia）的扑克机器人决赛上，这位 OpenAI 研究人员表示，在《外交》游戏中，使用人类数据训练的系统取得了成功，而依赖对手完全理性这一假设的做法未能奏效。他认为 GPT-6 Astra 在构建扑克机器人方面仍有不足。 来源： https://www.youtube.com/watch?v=tRaFbDFBl_A

**捷克播客《AI v kostce》梳理了从聊天到自主智能体的 6 个层级。** 主持人以销售报价自动化等为例，讨论共享上下文、可复用技能、权限和检查点。本期介绍的是从业者经验，没有提供测量数据。 来源： https://www.youtube.com/watch?v=x8c60lZ0D7Q

## 简讯

**在 Anthropic 的 Siren 蜜罐测试中，近期 Claude 模型在 0.6%–1.6% 的场景中不当使用了诱饵。** 较早模型的比例为 12.7%–25.8%。给沙箱写明规则后，尝试访问沙箱外部的次数减少了 68%–96%。组合使用缓解措施，也让两个模型的任务完成率降低了约 9 个百分点。Anthropic 表示，人为构造场景中的比例不代表现实发生频率。 来源： https://safeguards.anthropic.com/2026/siren/

**一个免费编程智能体在不到 6 分钟内试用了金融公司的诱饵访问密钥。** 安全厂商 Jesta 表示，一名操作人员使用了 OpenCode、浏览器和 curl。智能体试用了预先放置和自行编造的密钥，没有窃取任何信息，在 5 分 44 秒后停止。这起涉及匿名客户的案例由销售防御工具的公司提供。 来源： https://www.theregister.com/security/2026/11/24/an-ai-coding-agent-a-browser-and-a-mac-tool-found-a-financial-firms-access-key-in-under-6-minutes/5311922

**欧盟委员会（European Commission）证实，一起由 AI 辅助的攻击从 EU Academy 窃取了姓名和电子邮件地址。** 受影响人数未知。平台将暂停服务至 2027年1月14日，欧盟委员会尚未说明是否已彻底清除入侵者。 来源： https://www.theregister.com/cyber-crime/2026/11/24/european-commission-confirms-personal-data-stolen-in-ai-assisted-cyberattack/5311834

**美国国家漏洞数据库（NVD）新收录约 20 个 AutoGPT 漏洞，严重性评分最高为 9.1。** 问题涉及应用市场可能遭到接管、执行权限过宽，以及共享智能体使用运行者的 MCP 凭据。多数情况需要已认证用户或共享智能体。运营方应升级到受影响的 0.11.x 版本之后的版本。 来源： https://nvd.nist.gov/vuln/detail/CVE-2026-133453

**美国 45 位州检察长反对在破产程序中出售 Character.AI 数据。** 拟议转让涵盖超过 2,100 万个美国账户的聊天记录，其中 210 万个账户登记在未成年人名下。各州指称交易违反隐私承诺和儿童保护法律，法院尚未就此作出裁决。 来源： https://oag.ca.gov/news/press-releases/attorney-general-bonta-opposes-asset-sale-characterai-amid-child-safety-concerns

**美国因担心先进 GPU 被转运，将 7 家东南亚企业列入实体清单（Entity List）。** 规则涉及新加坡、马来西亚和泰国的企业，包括阿里巴巴旗下一家云服务子公司。相关许可证申请原则上将被拒绝。 来源： https://www.federalregister.gov/public-inspection/2026-23999/additions-to-the-entity-list

## 商业简讯

- **据报道，亚马逊（Amazon）将以 75 亿美元收购 Decart。** 据《TechCrunch》称，买方看中的是 Decart 用于 Trainium 的优化软件及其团队，对其世界模型并无收购意图。交易金额来自彭博社（Bloomberg），亚马逊尚未确认。 来源： https://techcrunch.com/2026/11/24/amazons-decart-acquisition-is-a-bet-on-using-software-to-narrow-the-gap-with-nvidia-in-the-ai-chip-race/
- **CrowdStrike 已同意以价值 439 亿美元的股票收购 Zscaler。** 两家公司称，合并的理由之一是帮助企业监控内部 AI 智能体。客户预计价格将上涨，目前仍属猜测。 来源： https://www.theregister.com/security/2026/11/24/crowdstrike-splashes-44b-on-zscaler-customers-brace-for-the-bill/5311877
