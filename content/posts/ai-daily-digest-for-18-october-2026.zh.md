+++
title = "AI 每日简报：2026年10月18日"
slug = "ai-daily-digest-for-18-october-2026"
description = "欧洲央行称，工作中使用 AI 的比例翻倍，而毕业生招聘走弱。一项多智能体研究发现，只需一个持续施压的对抗智能体，就可能让正常智能体在内部接受错误信念。"
tags = ["research", "business", "models", "safety"]
date = 2026-10-18T04:14:00+02:00
draft = false
+++

## 要闻

**欧元区工作中使用 AI 的比例翻倍，招聘计划却走弱，毕业生尤其受影响。** 欧洲央行（ECB）执行委员会成员 Philip Lane 表示，目前 52% 的劳动者在工作中使用 AI，高于 2024 年的 26%。欧洲央行另一组企业数据表明，64% 的企业以试验方式或适度使用 AI，但只有 7% 达到显著使用程度。

央行尚未看到整体就业或生产率受到重大影响。节省的时间集中在编程等专业任务上，而招聘低迷首先影响新进入劳动力市场的人。Lane 将结果描述为劳动成本与 token 价格之间的赛跑，并警告 AI 可能削弱劳动者的议价能力，降低劳动收入在总收入中的份额。

来源： https://www.ecb.europa.eu/press/key/date/2026/html/ecb.sp261013~9db9bf4fd6.en.html

**一个持续施压的对抗智能体，使正常智能体在内部持有错误信念的比例从 0.6% 升至 44.8%。** 在 10 个智能体讨论事实问题时，对抗者不断提出看似合理的错误答案。在 6 个模型、3 个问答数据集上，3 个对抗智能体将最终错误回答率推高至 60.5%。

内部结果比通常的公开从众现象更反常。有 3 个对抗者时，正常智能体在受影响轮次中有 51.6% 在内部持有错误信念，但公开赞同的比例只有 19.7%。仍保留正确认识的智能体往往无法捍卫它，初始事实知识也不能预测抵抗能力。这个结果直接挑战了“智能体群体会自然相互核查”的假设。

来源： https://arxiv.org/abs/2610.22138

**OpenCode 称，攻击者可能窃取了其托管 Console 中存储的服务商密钥。** 据公司称，此次入侵涉及正在退役的旧系统，影响了 1.4% 的 Console 用户。受影响产品是托管路由服务，并非本地编程智能体；收到通知的用户应撤销已存储的 OpenAI、Anthropic 和谷歌（Google）密钥，并检查服务商日志。

OpenCode 将事件称为“大规模蒸馏”，但尚未公布支持这一动机的证据，也未公布原因及暴露时间范围。一名 Reddit 用户称，存储的 Anthropic 密钥一夜产生了 158 美元支出。此次入侵说明，当网关持有可直接在其他服务商处消费的凭证时，用户就需要付出额外信任。

来源： https://news.ycombinator.com/item?id=50133401

**深度求索（DeepSeek）更新 V4.1 Flash，自报智能体编程得分提高，API 价格不变。** 实验室称，Terminal-Bench 4.0 得分从 31.2 升至 42.3，ProgramBench 从 20.3 升至 29.1，输出更短，任务耗时更少。采用 MIT 许可证的检查点支持 100 万 token；API 非缓存输入仍为每百万 token 0.15 美元，非高峰时段输出仍为每百万 token 0.60 美元。

一项早期独立编程测试的 30 次运行全部通过，每项任务约花费 0.045 美元，但每项任务使用约 55 万 token，而低推理强度的 Opus 5.5 约为 3 万 token。这一单项测试使实验室的效率主张更复杂：模型每 token 价格低、能力也不错，但可能消耗多得多的 token。

来源： https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017

**Xolotl 在一张 RTX 4090、系统内存和 NVMe 上运行 5520 亿参数的 DeepSeek 混合专家模型。** 这个基于 Strata 的引擎只加载每个 token 所需的专家，分布在 24 GB 显存、90 GB DDR4 内存和磁盘上。作者称，在 Ryzen 7 5700X 设备上，生成速度达到每秒 27 token，提示词处理速度每秒 180–320 token，上下文为 512K。

同一配置通过了作者的小规模测试——21 项 HumanEval 任务、10 次工具调用和 3 轮智能体缺陷修复——但这些是基于较旧量化检查点的自测结果。就可用性而言，这仍是引人注目的成果：通常需要服务器级内存的模型，通过内存层级和存储带宽与延迟之间的取舍，在消费级硬件上实现了交互运行。

来源： https://github.com/Indras-Mirror/Xolotl

## 新模型与发布

**DeepSeek 开放了自研 Search 和 Fetch API。** 从 11月1日 起，每个端点每 1000 次成功调用收费 0.75 美元；在此之前，通过 DeepSeek Harness、Claude Code 或 Codex 作为服务器端工具发起的调用仍免费。来源： https://api-docs.deepseek.com/quick_start/pricing

## 研究

**上下文学习由多种能力发展而来，并非单一能力。** 对 17 个模型的检查点分析区分了提示词控制、答案偏好、构建和迁移；在准确率高于随机水平之前，模型就已经关注与任务有关的 token。来源： https://arxiv.org/abs/2610.19113

**代码行为是否显得局部化，取决于探测方法和组件预算。** 在 10 个模型上，预算为 12 时，15 种设置中只有 1 种超过随机对照；预算为 40 时则有 6 种，推翻了此前部分关于干预一概无效的主张。来源： https://arxiv.org/abs/2610.20683

**监督训练和强化训练后，推理密度预测正确性的方式不同。** 在 60 道 GSM8K 题目的样本上，强制施加所测密度使准确率从 60.0% 降至 8.3%，而提示加缓存干预则提高了 13.3 个百分点。来源： https://arxiv.org/abs/2610.21286

**包含 65 种属性的语义表示，能解释大脑反应中共有和独有的变异。** 研究让 7 人听故事，发现具体属性与 LLaMA2-7B 的对应更强，而可解释特征保留了模型未能捕获、可预测大脑反应的信息。来源： https://arxiv.org/abs/2610.21508

**稀疏自编码器特征比随机坐标更具可加性，但仍存在相互作用。** 加入成对效应后，操控效果的排序保真度从 0.587 升至 0.779，提醒人们不要在解释时将学到的特征视为相互独立。来源： https://arxiv.org/abs/2610.21261

**自动化研究智能体定期遗忘历史后表现更好。** 在 4 项任务上，从迄今发现的最佳候选方案重新开始，相比相互通信的并行智能体最多提升 15%，相比单智能体提升 39%。来源： https://arxiv.org/abs/2610.20563

## 经济与就业

**亚马逊（Amazon）的 Atlas 系统为仓库的工会组织风险打出 100–900 分。** 内部文件列出数百项输入，包括 Reddit 帖子和调查回答，并将 16 个站点列为最高风险等级。亚马逊称，Atlas 只在站点层面运作，不监控个人观点或工会成员身份。来源： https://www.opendemocracy.net/amazon-ai-surveillance-monitor-union-activity-uk-warehouses-birmingham-coventry-atlas-sutton-coldfield/

**Gartner 估计，数据中心业主到 2030 年需要累计取得 8.5 万亿美元营收，但来自 AI 的收入最多为 3.6 万亿美元。** 美国银行（Bank of America）另称，由于 token 价格下降的影响超过用量增加，企业 AI 支出已开始下滑。这些是《财富》（Fortune）报道的分析师估计，并非经审计账目。来源： https://fortune.com/2026/10/17/ai-boom-vs-bust-bubble-warning-hyperscaler-spending-debt-coreweave-nvidia/

**银行、零售商和航空公司正在屏蔽消费端智能体，或向它们收取访问费。** 摩根大通（JPMorgan）、嘉信理财（Schwab）、亚马逊和 eBay 屏蔽智能体；达美航空（Delta）禁止自动订票，Yelp 只允许获得其数据许可的智能体进入。Meta 正逐家零售商协商访问权限。来源： https://www.theverge.com/ai-artificial-intelligence/1013195/ai-agents-blocked-web

**中国集成电路出口额增长 136%，出口量仅增长 1%。** 据《南华早报》（SCMP）报道的海关数据，9 月出口 327 亿颗，金额达 450 亿美元，说明内存短缺通过价格而非出货量推动了营收。来源： https://www.scmp.com/tech/tech-trends/article/3370858/china-chip-exports-jump-136-us45b-ai-frenzy-jacks-prices

**HUMXN 免费提供住宅维修服务，换取拍摄技术工作过程以训练机器人。** 在明尼阿波利斯、芝加哥和迈阿密，佩戴采集传感器的技术人员记录检查、工具选择和工作完成过程。公司未公布劳动者报酬条款、数据集规模或机器人部署数量。来源： https://www.tomshardware.com/tech-industry/artificial-intelligence/ai-lab-offers-free-plumbing-and-hvac-repairs-across-three-cities-to-train-ai-robots-wearable-sensors-record-video-of-repair-work-for-robotics-training-free-services-also-include-electrical-work-air-duct-cleaning-and-carpet-cleaning

## 提示词技巧

**9 条系统提示词规则，使一个模型的 Terminal-Bench 得分从 52.8% 升至 59.6%。** 规则要求智能体完成一种方案、质疑错误前提、将已核查答案视为定论，并寻求外部证据，而不是反复自我怀疑。这是 GLM-5.3-Flash 在 89 项任务上的单次运行。来源： https://old.reddit.com/r/LocalLLaMA/comments/1x8q308/followup_tested_my_9_thinking_rules_on/

## 大家在做什么

**TensorFold 在两套 DGX Spark 系统上，以每秒 56.8 token 的速度运行 DeepSeek V4.1 Flash。** 作者的 EXL3 方案在相同硬件上的文本吞吐量超过 vLLM 套件的两倍，并加入持久提示词缓存；结果来自自测。来源： https://github.com/Elevatormusic/DeepSeek-V4.1-Flash-1017-EXL3-TensorFold-2x-DGX-Spark

**Llmspeed 模拟本地模型在指定 GPU 或 Mac 上的使用感受。** 其估计混合了社区实测与推算；Hacker News 讨论串中的设备拥有者发现较大误差，且缺乏测试框架细节，因此它只能作为粗略的规划辅助工具。来源： https://llmspeed.dev/

**一个 Ternary Bonsai 智能体通过 WebGPU 完全运行在浏览器标签页中。** 这个静态 Hugging Face Space 无需服务器，提供 20 亿、40 亿、90 亿和 270 亿参数的 1.58 位模型，未提出基准成绩主张。来源： https://huggingface.co/spaces/webml-community/ternary-bonsai-2-hermes-webgpu

**Scout 将自然语言任务转为真实浏览器中的点击、输入和滚动操作。** 这个采用 Apache-2.0 许可证的智能体使用用户的模型密钥，可以在本地或 Outcrawl 付费浏览器服务上运行；README 未提供可靠性基准测试。来源： https://github.com/outcrawlai/scout

**E2E 记录已验证的智能体步骤，之后无需再次调用模型即可回放。** 常规断言验证首次运行；后续网页或移动端测试会重复使用这些操作，直到界面改变，从而降低持续发生的推理成本。来源： https://github.com/tester-army/e2e

**Reason Network 让团队成员的编程智能体点对点交换消息。** 这个 Rust 守护进程通过 MCP 提供团队会话、收件箱和状态，无需中央服务器，支持 Claude Code、Codex、Cursor 及其他智能体运行框架。来源： https://github.com/reason-machines/reason-network

## 值得一读

**Nathan Lambert 认为，Meta 和 Reflection 将西方开放模型的差距缩小了一半。** 如果不计这两次发布，他的指数仍显示有 20 多个中国开放模型领先；他同时表示，能力相当的西方模型获得了更多采用。这是有证据支持的论点，并非基准测试论文。来源： https://www.interconnects.ai/p/meta-shakes-up-the-frontiers-open

**Ben Recht 称，OpenAI 更快的傅里叶变换是在不现实的计算模型上取得的胜利。** 他认为，隐藏常数和机器假设使结果更接近钻基准测试的空子，而非加速真实 FFT；这是他的技术批评，不是正式反驳证明。来源： https://www.argmin.net/p/faster-fourier-transforms

**Sam Newman 介绍了依赖 AI 服务商的软件应如何设计灾难恢复。** 这段书摘讨论了在 GPU 短缺、服务商可用性难以预测的情况下，备份恢复、最小备用资源、温备故障切换和双活设计。来源： https://newsletter.pragmaticengineer.com/p/building-resilient-systems

## Hacker News

**亚马逊 Atlas 系统引发了有关 AI 监控劳动者的讨论。** 有劳动力分析经验的评论者称，即使输入数据能揭示员工组织工会的风险，类似系统也常以离职或敬业度工具的名义出售。这些说法属于个人经历。来源： https://news.ycombinator.com/item?id=50132278

**从业者讨论由谁核查智能体编写的代码。** 一名评论者称，破坏功能的缺陷同比增加约 40%，但功能和营收增长更快；其他人认为，这种表面生产率将质量保证成本转嫁给了用户。来源： https://news.ycombinator.com/item?id=50133713

## Reddit

**一名 OpenCode Console 用户称，泄露的存储密钥一夜产生了 158 美元支出。** 发帖者称 Anthropic 最初拒绝退款；关于受影响用户将获补偿的说法来自转述。实际应对办法是轮换密钥、设置较低支出上限并检查日志。来源： https://old.reddit.com/r/ClaudeAI/comments/1x8o35r/psa_opencode_breach_my_stored_anthropic_key_was/

**Strata 用户发现，默认设置会以质量换速度。** 在 0.1.45 之前的版本中，客户端未指定采样时可能使用贪心解码；跳过路由尾部使一名用户的速度从每秒约 72–81 token 升至 93 token，但一项已公布的分歧指标翻倍。来源： https://old.reddit.com/r/LocalLLaMA/comments/1x8m0jj/xolotl_strata_based_deepseekv41flash_552b_on_a/

## YouTube

**Featherless AI 介绍了降低推理成本的 4 种方法。** Eugene Cheah 建议测量支出、按需要选择模型规模、有计划地购买 GPU 容量，并检查 token 用量是否对应有用工作；数据来自他的公司。来源： https://www.youtube.com/watch?v=Ti-BmGU1_mQ

**Arize 为金融智能体搭建评测循环。** 在示例智能体自信地声称“116% 的分析师表示赞同”后，研讨会结合运行轨迹、代码检查、模型评判和持续集成关卡来开展评测。来源： https://www.youtube.com/watch?v=SHMCGrNJJGc

**Monzo 工程师认为，电子表格计算应由代码完成，而非交给模型。** 他们的金融智能体直播研讨会以证据、一致性、问责和核查为中心，而不是响应速度。来源： https://www.youtube.com/watch?v=e9-br9hveRI

**《纽约时报》（The New York Times）报道了拍摄技能劳动过程、用于训练机器人的劳动者。** 工人在从事体力工作时佩戴摄像头，产出旨在自动化这些工作中部分任务的数据。来源： https://www.youtube.com/watch?v=H7_KofwTsXw

## 简讯

**Anthropic 的美国法案草案规定，只有在面临超过 10 亿美元损失，或超过 50 人死亡或重伤的迫近风险时，才能封禁模型。** 据报道，文本涵盖生物武器、逃避控制和网络攻击，同时排除部分更严格州级规则的适用。来源： https://www.motherjones.com/politics/2026/10/anthropics-ai-safety-bill-has-an-alarming-threshold-for-government-action/

**遭到批评后，Meta 从新的商业抓取条款中删除了“训练”一词。** 公司称其爬虫行为没有改变；出版商指出，条款虽不再列出训练，但也没有明确禁止。来源： https://www.theverge.com/tech/1013409/meta-removes-language-that-may-have-allowed-it-to-scrape-news-sites

**供应趋紧之际，英伟达（Nvidia）否认停产 RTX 5090。** Tom's Hardware 发现，这款显卡在多家主要商店缺货，在亚马逊上的报价约为 8500 美元，但英伟达称仍在生产。来源： https://www.tomshardware.com/pc-components/gpus/nvidia-reportedly-insists-the-rtx-5090-isnt-dead-despite-severe-shortages-and-removed-listings-at-multiple-retailers-flagship-gpu-is-missing-from-nvidias-store-and-commands-usd8-500-on-amazon

**苹果（Apple）首席执行官 John Ternus 将内存芯片短缺称为“绝对是一场危机”。** 波及 AI 服务器和 GPU 的短缺如今也制约了消费设备；报道称，在美国政治压力下，苹果已测试中国内存供应商。来源： https://thenextweb.com/news/john-ternus-time-interview-memory-crisis-iphone-duo

## 后续关注

DeepSeek 将于 11月1日 开始对 Search 或 Fetch 调用收费，每 1000 次 0.75 美元。Meta 修订后的商业条款将于 10月30日 生效。
