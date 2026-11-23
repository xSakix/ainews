+++
title = "厚重思考的轻盈化"
slug = "the-lightness-of-heavy-thought"
description = "Google DeepMind 发布中型模型 Gemini 4 Neon，旨在以远低于旗舰兄弟模型的时间与成本，承担前沿级软件工程、科学研究与网络防御任务。它的到来标志着人工智能领域一次更为克制的转向：从单纯追求庞大规模，转向有节制的日常执行。"
tags = ["models", "agents", "business", "safety"]
date = 2026-11-19T06:58:00+01:00
draft = false
+++

**Google DeepMind 发布中型模型 Gemini 4 Neon，旨在以远低于旗舰兄弟模型的时间与成本，承担前沿级软件工程、科学研究与网络防御任务。它的到来标志着人工智能领域一次更为克制的转向：从单纯追求庞大规模，转向有节制的日常执行。**

上周二晚上十一点，厨房餐桌早已凉透，我最终放弃了核对那张电费账单。台灯旁摊着地区电力公司发来的 4 份 PDF、两份扫描的电表读数，以及一张死活对不上秋季突发附加费的电子表格。我把这团乱麻丢给一款旗舰推理模型，在暖气片于暗处咔哒作响的间隙盯着光标闪烁。三分钟过去，四分钟过去。最终返回的答复详尽、礼貌，却与眼下的场景完全不成比例——就像为了把一只挎包送到城另一头而调来一台货运机车。等它思考完毕，我自己早已忘了原本的思路，只得合上笔记本电脑。

## 中间地带的架构

这种微小却熟悉的摩擦——聪明到足以解开难题的模型，与快到足以融入日常工作的模型之间的距离——正是谷歌（Google）在 2026年11月18日着手填补的领域。在一份由 Google DeepMind 高级副总裁兼谷歌首席 AI 架构师 Koray Kavukcuoglu 署名的公告中，公司正式推出 Gemini 4 Neon。在不断扩展的 Gemini 4“元素周期表”中，Neon 有意占据正中位置。Gemini 4 Carbon 仍是面向最漫长、最棘手项目的重型载具；Gemini 4 Hydrogen 负责敏捷的常规执行。Neon 由 Carbon 衍生而来，意在衔接二者，为复杂且高频的工作提供深度多步推理，同时压缩等待时间与账单开销。

其经济账一目了然。谷歌为 Neon 定价每百万输入 token 3 美元——缓存输入降至 0.15 美元，相当于 95% 的折扣——每百万输出 token 15 美元，并统一配备 100 万 token 的上下文窗口，可同时处理文本、电子表格、PDF、音频和视频。发布当天，该模型同步登陆 Google AI Studio 和 Android Studio 中的 Gemini API、面向企业用户的 Gemini、Google Antigravity 的付费 Pro 与 Ultra 订阅层，以及 Gemini 应用的下拉菜单。

独立评测机构的数据显示，减重并未牺牲判断力。在 Artificial Analysis Intelligence Index 上，运行于最高推理设置的 Neon 拿下 61 分，总榜位列第三，仅落后于体量更大、速度更慢的模型。在 Vals Index 上，它以 70.9% 排名第二，稳稳落在成本与准确率的帕累托前沿上，并在 Legal Research Bench 和 Tax Agent Bench 两项榜单夺得第一。在 Surge AI 覆盖金融、会计与电子表格建模的评测中，它在大多数类别位居榜首，在 Chartography 上解读高密度专业图表的准确率为 73.5%，在 Agents' Last Exam v1.1 上以 75.8% 追平领先系统。在 Zapier 的 AutomationBench 上，它以 56.3% 名列第一。在基于超过 4,200 次真实智能体（agent）会话构建的新榜单 Agent Arena Index 上，Neon 首次亮相便以 1336 分位居全球第二，并在衡量模型吸收人工中途纠偏能力的可控性（steerability）指标上排名第二。

检验持续判断力最奇特的考场，或许是 Andon Labs 的 Vending-Bench 2。这项为期一年的模拟测试要求自主智能体管理库存、与对抗性供应商讨价还价、支付日常费用，在保持逻辑连贯的前提下设法将 500 美元做成盈利的自动售货机生意。Neon 以 16,843 美元的余额拿下总榜第一。在较为安静的数学与技术研究领域，它在 Terminal-Bench Science 取得 70.5%，在 RiemannBench 达到 84.0%，在 HLE-Diamond 录得 71.3%，均处于领先。

早期企业测试者谈论这一变化时，较少纠结于榜单小数点，而更看重模型的“脾性”。Glean 的 AI 产品负责人 Thai Tran 报告称，Neon 在整体职场任务质量上追平甚至超过 Carbon，同时速度达到三倍，成本仅为 60%。Micro1 的 Brandon Valafar 看到它登顶公司内部的 Medical Index 与生命科学评测。Quadrillion 首席科学家 Trenton Chang 给出了更犀利的区分：新手研究员会照单执行交给它的任何实验，优秀的研究员则会不断追问“为什么”。Neon 是其团队观察到的首个在无人监督下跨越失败运行、主动寻找新信号并重新设计建模策略的模型，而不是在糟糕结果面前轻易认输。Cartwheel 联合创始人兼首席科学家 Andrew Carr 称它在机器学习工程与架构设计方面是位扎实的搭档，既能吸收反馈，也尊重既有成果。

## 代码、智能体集群与可控算力

软件工程已成为自主智能体的真正试金石，一次草率修改就可能波及上百个文件。谷歌打造 Neon 的目标，是让它经得起漫长且密集调用工具的会话——既可独立作业，也能在 Google Antigravity 中充当沉稳的编排者，调度并行运行的 Hydrogen 子智能体。落到实践中，这意味着减少冗余的文件读取、边推进边汇报进度，以及在压缩长上下文窗口时不至于忘记最初打开代码库的初衷。

在 Artificial Analysis Coding Agent Index 上，Neon 以 58.6 分位居总榜第一，并在 Terminal-Bench 4.1 取得 65.2%，在默认高推理设置下的 FrontierCode 2.0 取得 46.2%。在 SWE-sweep 上，它在 mini-SWE 测试框架下以 12.8% 领跑，而在 Google Antigravity 内部成绩暴涨逾三倍，达到创纪录的 39.0%——这充分说明当代智能体的表现有多大程度取决于模型权重之外的脚手架设计。

为了展示这些百分比在实战中的模样，谷歌演示了 Neon 驱动智能体集群完成近乎炫技的复杂任务。在 Antigravity 内，Neon 利用勃朗峰（Mont Blanc）与霞慕尼（Chamonix）的真实高程数据，从零编写了一款第一人称 WebGL2 自由式滑雪模拟器——包含超过 10,200 行自定义着色器代码、120 Hz 滑雪物理引擎、动态刻雪轨迹、板状雪崩与空间音频，且未借助任何预制素材。另一个集群调取档案照片，在交互式三维空间里重建了艾伦·图灵（Alan Turing）1936年在剑桥大学国王学院（King's College, Cambridge）的 X.8 书房，窗外可见国王学院礼拜堂，书桌上则摆着一台运转中的通用图灵机。第三个集群把单张照片转译成包含 10 万个单元格的 Google Sheets 表格，既不嵌入图片也不用 Apps Script，仅靠超过 50 万条实时电子表格公式完成边缘检测、三维深度映射，并在六种交互模式下重新打光。

在绚丽演示之下，是一枚务实的调节旋钮。Neon 开放了四个思考挡位——low、standard、默认的 high 以及 xhigh——让工程团队按问题分量灵活分配 token 开销。在默认 high 挡位下，Neon 的单任务成本较 Carbon 降低 32%，在 Vals Index 和 Agent Arena 上比顶尖竞品前沿模型便宜约 50% 至 80%。即便在最棘手的科学与工程问题上推至 xhigh 挡位，其单任务成本仍比运行于上限的竞品模型低 36% 以上。

## 防御中的克制与纪律

更快的速度与更低的成本伴随一个阴暗推论：对建设者而言更便宜的工具，对攻击者同样更具诱惑。谷歌直面这一张力，推出了专门变体 Gemini 4 Neon for cyber，并将在未来数日内通过 Fairwind Program 向经审核的安全团队开放。

在整个防御生命周期中，该模型刷新了多项最佳成绩，预算却大约只有更大规模竞品的一半。在 AutoBaxBench 高难度层级生成安全 Web 后端时，它达到 76%。在 WebExploitBench v1.2 的主动渗透测试中，它以竞品大模型一半的成本取得 51.26%。在 SEC-bench Pro 既有代码库漏洞挖掘中，它达到 90.5%，同时将单项挑战成本减半。在 ExploitGym 验证漏洞是否真正可利用时，它仅用 Carbon 一半的 token 就追平前沿水准。在 Collinear 的 CWE-bench v2 上修补漏洞根因时，它达到 70.7%，比 Carbon 高出 3.4 个百分点。Thoughtful Lab 创始人 Karina Nguyen 报告称，在他们的网络安全评测中，Neon 仅消耗极少 token，就发现了其他模型漏掉的隐蔽漏洞。

同样值得关注的，是谷歌如何衡量“克制”。一个偷工减料或虚构测试通过结果的快速智能体，比慢速模型更危险。在 Google Antigravity 内部测试中，Neon 创下了公司迄今最低的编造率。在 Terminal-Bench 4.0 上，它与 Carbon 一样保持 0% 作弊率；在谷歌的编程作弊测试集中，它仅在 2.45% 的任务中走了捷径，为整个 Gemini 4 系列最低。其智能体式安全评测录得 0.09% 的错位行动率和 99.2% 的智能体诚实度通过率；对过度拒绝的收敛，使其在 Terminal-Bench 4.0 上仅拒绝了 1.98% 的正当任务，在 Terminal-Bench Science 上为 0%。在各个算力挡位上，服务不足（under-service）下降了 43% 至 56%，越界操作（overreach）减少了 15% 至 35%。针对隐藏在网页、邮件或代码库中的间接提示词注入攻击，在最高思考挡位配合实时安全防护措施下，Neon 在 Gray Swan 基准测试中录得 0.0% 的攻击成功率。

然而，任何诚实的报道都必须在新闻稿止步之处停下来审视。基准测试是洁净室，真实的互联网却是废品场。在受限评测中取得 0% 的攻击成功率，只能说明谷歌的监测器与护栏守住了 Gray Swan 设计的场景，并不能证明一段藏在冷门开源依赖包里的精巧载荷永远不会在凌晨 3 点溜过无人值守的智能体。在旧金山（San Francisco）模拟自动售货机生意里赚到 1.6 万美元，也不意味着企业财务团队从此可以不再核对报表附注。真正检验 Neon 的，终究要看六个月后新鲜感褪去、日志越积越长时的安静可靠，而不仅是发布日的漂亮图表。

## 回到书桌前

对 Gemini 应用里的普通订阅用户而言，它的价值远没有三维剑桥书房那么富于戏剧性。Neon 从 Gmail 和 Docs 提取上下文，解析杂乱的收据与密集财务表格，跨供应商执行实时网页核查，并在不至于一下午就耗尽用量额度的前提下完成多步琐事。

今天清晨，窗外街道尚未完全苏醒，我在厨房餐桌上重新打开那 4 份电力账单 PDF，连同扫描的电表照片一起拖进提示词窗口。这一次，没有守着闪烁光标的漫长等待。几秒之内，模型便锁定了 9月一笔重复计收的配电费，对照地下室电表照片上横印的精确千瓦时读数完成了交叉核验，并起草了一封简短、不带情绪的账单申诉信。那一刻既不显得充满未来感，也谈不上宏大。它更像是按下电灯开关，灯泡随即亮起。或许比起任何排行榜桂冠，这才是 Gemini 4 Neon 背后真正的新闻：前沿智能终于不再要求满屋子的人停下手里的事，静静看它思考。

## 参考文献

Kavukcuoglu, Koray. Introducing Gemini 4 Neon. [https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/)

Google DeepMind. Gemini 4 Neon Model Card. [https://deepmind.google/models/model-cards/gemini-4-neon/](https://deepmind.google/models/model-cards/gemini-4-neon/)

Google DeepMind. Gemini 4 Neon Model Evaluation Methodology. [https://deepmind.google/models/evals-methodology/gemini-4-neon/](https://deepmind.google/models/evals-methodology/gemini-4-neon/)

Artificial Analysis. Google continues to accelerate its release cadence with Gemini 4. [https://artificialanalysis.ai/articles/gemini-4-neon-intelligence-gain](https://artificialanalysis.ai/articles/gemini-4-neon-intelligence-gain)

Vals AI. Vals AI: AI Benchmarks for Real-World Tasks. [https://www.vals.ai/home](https://www.vals.ai/home)

Vals AI. Vals Legal Index Leaderboard and Methodology. [https://www.vals.ai/benchmarks/legal_index](https://www.vals.ai/benchmarks/legal_index)

Andon Labs. Vending-Bench 2. [https://andonlabs.com/evals/vending-bench-2](https://andonlabs.com/evals/vending-bench-2)
