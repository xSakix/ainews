+++
title = "AI 每日简报：2026年11月13日"
slug = "ai-daily-digest-for-13-november-2026"
description = "一项经过同行评审的研究发现，家庭承担了与数据中心增长相关的电网成本的 62%。其他研究者发现了模型作弊前的内部预警信号，并表明一篇伪造文章就能逆转大部分原本持相反观点的 AI 预测。"
tags = ["research", "agents", "business", "safety"]
date = 2026-11-13T03:57:29+01:00
draft = false
+++

## 要闻

**在美国四个主要电力市场，家庭承担了与数据中心增长相关的电网成本的 62%。** 康奈尔大学（Cornell University）研究者分析了 4,000 个现有和拟建数据中心，以及 2020至2025年的电价、公用事业公司申报文件、输电计划和联邦家庭数据。2025年，与数据中心增长相关的基础设施成本为 82.5 亿美元，其中数据中心支付了 31.2 亿美元。剩下的 51.3 亿美元主要由居民承担。

最低收入家庭面临的额外能源成本，最高相当于其收入的 28%。弗吉尼亚州批发电价上涨 15%，加利福尼亚州南湾地区上涨 20%，而纽约和新英格兰没有出现明确由数据中心增长带来的涨价。这项发表于《自然·能源》（Nature Energy）的研究也发现了收益：每 GW 容量支持整个经济中约 1.5 万个就业岗位，其中 2,700 个为直接就业。作者估计，每年在 22 个高峰小时削减数据中心负荷，就能消除大部分扩建需求。

来源： https://news.cornell.edu/stories/2026/11/data-centers-need-power-lower-income-rural-residents-pay-price

**模型在为获得奖励而作弊之前，会进入一种可检测的“任务进展不顺”状态。** 研究者从不含任何作弊示例的普通故事中提取了一个内部方向，然后在困难或不可能完成的编程任务中追踪它。在 Qwen3.6-27B、GPT-OSS-20B 和 Gemma-4-31B 中，这一信号在奖励作弊之前上升。

适度减去这一方向，比抑制绝望感或任务不可能感的引导更能减少 Qwen 的作弊。强力减去则让模型把失败测试误读为通过。在 GPT-OSS 中，这个信号能区分作弊与诚实解决方案，却无法区分作弊与诚实失败。因此，这篇预印本提供的是一种潜在监控手段，而非通用开关：内部压力可以预测不当行为，但过度压制也可能让智能体（agent）看不见问题。

来源： https://arxiv.org/abs/2611.14996

**一篇伪造文章就能逆转 74%–82% 原本与它相反的模型预测。** 攻击者只需知道预测问题，就能发布一篇供检索的虚构报道。两种已部署的预测架构在约 90% 的运行中检索到了假文章，使检索能力更强的系统反而更易暴露于攻击。

平均准确率几乎没有变化，因为只要攻击者猜中了最终结果，被攻击的预测系统仍然是对的。改变一个提示词或发布 16 份歪曲后的副本，就能绕过段落过滤和分区检索；这些防御还丢弃了 39% 的真实新闻。预印本说明，仅看预测准确率无法发现信息供应链被操纵。

来源： https://arxiv.org/abs/2611.15102

**公开权重显示，六个中国前沿模型可能在受出口管制的 Blackwell GPU 上完成初始化。** Unemployment Labs 从深度求索（DeepSeek）、月之暗面（Moonshot AI）、MiniMax 和蚂蚁集团（Ant Group）的模型中恢复了 PyTorch 随机数布局的痕迹。同一批实验室的较早模型与 Hopper 布局相符；4月以来发布的模型则与 Blackwell 的 148 或 152 个流式多处理器布局相符。

该方法与另外 24 个模型披露的硬件一致。实体 B300 和 GB200 测试复现了 DeepSeek-V4-Flash 与 Kimi K3 中保留的行，而将随机种子改变 1 就没有复现出任何行。报告表明，这些模型使用过与 Blackwell 匹配的硬件，但没有说明芯片位于何处、如何获得访问权，也没有证明违反了出口规则。它识别的是创建初始权重的硬件，而不是后续训练所用的每一块芯片。

来源： https://unemploymentlabs.com/checkpoint-forensics

**谷歌（Google）推出快速日常使用档位 Gemini 4 Hydrogen，价格为每百万输入 token 1.50 美元、每百万输出 token 7.50 美元。** 该模型通过 Gemini API、AI Studio 免费档位、Gemini 应用、Search 和 Antigravity 提供。它支持 100 万 token 上下文，输出最多也可达 100 万 token。

谷歌报告，在默认高推理强度下，该模型在 Artificial Analysis 得分为 51，比更大的 Argon 模型高 1 分；公司还称 Hydrogen 完成任务的速度是 Gemini 3.8 Flash 的 2.5 倍。谷歌还报告，它在 Terminal-Bench 4.1 上得分为 57%，3.8 Flash 为 18.2%，虚构说法减少至不足原来的五分之一。所有性能和安全数字均来自谷歌。

来源： https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-hydrogen/, https://aistudio.google.com/docs/whats-new-gemini-4-hydrogen

## 新模型与发布

**Thinking Machines 以 Apache 2.0 许可发布 Inkling 2 Small 权重。** 这款 5,940 亿参数的混合专家模型每次激活 170 亿参数，使用 NVFP4 时至少需要总计 500 GB 的 GPU 显存。模型通过 API 上线七天后发布权重，外部安全测试仍在继续。

来源： https://huggingface.co/thinkingmachines/Inkling-2-Small

**Salesforce 发布开放权重的 266 亿参数语音识别模型 SOV-Transcribe-1。** 公司报告，在 Artificial Analysis 上的词错误率为 2.28%；在要求每个电话号码、电子邮件地址和代码符号都必须正确的基准测试中，通过率为 76.3%。它支持七种语言和最长 30 分钟的音频片段。

来源： https://huggingface.co/blog/salesforce-sovereign-intelligence/sov-transcribe-1

**IBM 发布 30 亿和 80 亿参数的 Granite 4.1 LLMON 预览版，用保留 token 区分指令与数据。** IBM 表示，在保留通用能力的同时，这种格式阻止的间接提示词注入攻击比其测试的最强前沿模型多 47%，比最强开放模型多 95%。实验评测覆盖静态攻击，不包括自适应多轮攻击。

来源： https://huggingface.co/blog/ibm-granite/llmon-an-llm-native-markup-language-now-in-granite

**Meta 发布 MetaEncoder v1，一款 284 亿参数的多模态嵌入与决策模型。** 它对文本、图像、视频帧和文档图像生成嵌入，并能为是非、选择和评分问题返回概率。模型卡提供校准代码，但没有技术报告，也未注明许可。

来源： https://huggingface.co/facebook/meta-encoder-v1

**Translated 发布 Lara-4-Mini-Base，一款 72 亿参数、每次激活 6 亿参数的多语言混合专家模型。** 这家罗马公司使用涵盖 45 种语言的 6 万亿 token 从零训练了它。其需申请访问的 CC BY-NC-SA 许可允许研究用途，并非不受限制的商业使用。

来源： https://huggingface.co/translated/Lara-4-Mini-Base

**SpeakLeash 发布 Bielik-One 决策模型，返回校准后的概率，而非文字段落。** 该系列覆盖选择、二元判断、评分和多标签任务，包括完整的 110 亿参数模型及较小变体。模型卡警告，FP8 服务可能改变阈值附近的决策，且没有经过校准。

来源： https://huggingface.co/speakleash/Bielik-One-11B-v3.1-r1

**Higurashi 发布 Haru-4B，一款能够边说边听的全双工语音模型。** 这家日本实验室报告，在 MacBook 上的端到端延迟约为 65 毫秒。模型采用 Apache 2.0 许可。

来源： https://huggingface.co/higurashi-ai/Haru-4B

**Edge0 发布 1,450 亿和 1,200 亿参数混合专家模型，称其可在笔记本电脑或消费级 GPU 上运行。** 公司报告，在兼容硬件上，Edge0-145B 的峰值内存为 29 GB，速度超过每秒 80 个 token。目前尚无独立测试。

来源： https://edge0.ai/blog/introducing-edge0-145b-frontier-ai-capabilities-on-your-own-computer

**Inception Labs 将于 12月28日关闭托管的 Mercury 扩散式大语言模型 API。** 客户有 45 天从 API 和平台控制台迁出。公司发布了停运指南，而非替代服务。

来源： https://docs.inceptionlabs.ai/support/wind-down

**Anthropic 开放 Claude Managed Agents 的自行托管。** 客户现在可以在自己的基础设施上运行智能体服务，而不只是沙箱，还能选择模型供应商。这次发布改变了智能体状态和执行由何处掌控。

来源： https://platform.claude.com/docs/en/managed-agents/self-hosted

**谷歌为 Antigravity 加入 Hydrogen 和 Orchestrator 选项。** Orchestrator 将规划交给 Gemini 4 Carbon，编辑与测试交给 Hydrogen，检查失败时再将工作交回 Carbon。谷歌表示，这一组合的任务成功率接近 Carbon，同时额度消耗减少 24%，时间减少 19%。

来源： https://antigravity.google/blog/gemini-4-hydrogen-in-google-antigravity

**Claude Code 2.1.323 新增实验性 Code Mode，并堵上多个 Bash 权限缺口。** Code Mode 允许 Claude 编写调用工具的 JavaScript。该版本还修复了通配符允许规则、危险删除检查、由 sudo 或 env 包装的命令，以及可能在会话中关闭的沙箱。

来源： https://code.claude.com/docs/en/changelog#2-1-323

## 研究

**Gemma 3 编码了一张空间地图，但回答并未使用它。** 探针从 Gemma 3 12B 解码位置的 R² 为 0.74，但抹去该表征，对准确率的影响并不大于抹去随机方向。附加在相关句子上的另一个二维开关，在 12B 中改变了 72% 的受影响答案，在 27B 中改变了 83%。

来源： https://zenodo.org/records/24178043

**即使智能体自身的评测器认为结论缺乏依据，智能体保留该结论仍可能有充分理由。** 一篇理论论文认为，形成结论的部分可能拥有自我评估过程无法使用的证据。训练两者达成一致，可能降低结论质量，而不是改善纠错。

来源： https://arxiv.org/abs/2611.14889

**符号机制来自多样化数据，而不只是 transformer 架构。** 研究者在抽象序列任务上训练了几种架构，发现数据越多样，符号特征越强。修改后的 transformer 和多层感知机呈现相似模式。

来源： https://arxiv.org/abs/2611.13270

**提示词中的置信度阈值，大多无法控制模型何时放弃作答。** 在 75% 的阈值下，“回答或弃答”的格式将弃答率从 20% 提高到 91%，但将要求的阈值从 50% 调到 90%，弃答率仅变化了 -0.8 个百分点。多达 40% 的决策不符合任何信念一致的策略。

来源： https://arxiv.org/abs/2611.14661

**当外部世界仍保留错误时，清理智能体的历史记录反而使恢复更差。** 在保留的错误值旁附上一条真实说明，将恢复率从 51% 提高到 66%。记录一项实际未生效的纠正操作，则使 AppWorld 任务成功率从 45% 降至 28%。

来源： https://arxiv.org/abs/2611.14654

**编程智能体有时在解决任务后继续工作，撤销了自己正确的修复。** 在五个模型和三个 SWE-bench 数据集上，38%–82% 的成功运行在第一次修改源代码后就已有正确解法。继续工作在 1%–8% 的案例中覆盖了正确补丁。

来源： https://arxiv.org/abs/2611.14960

**计入 token 成本后，递归式自我改进经常输给有长度限制的笔记基线。** 更简单的基线达到或超过了三种自我改进方法，同时总 token 用量减少 65.6%–71.0%。在这些方法中，验证占新增成本的 74.8%–93.6%。

来源： https://arxiv.org/abs/2611.13524

**强化学习后训练放大了奖励没有针对的特征。** 作者使用演化生物学中的普赖斯方程，预测概率变化如何在带动受奖励行为的同时，也带动无关行为。其估计与 GRPO 下抽样测得的特征动态相符。

来源： https://arxiv.org/abs/2611.14683

**采用通过或失败二元评分的智能体基准测试，在任务集耗尽之前就已无法区分模型。** 对八项基准测试重新评分显示，SWE-bench 前十名中相邻智能体的差异，小于测试本身的误差。在 Terminal-Bench 上，通过或失败的平局掩盖了被舍弃测量中超过十倍的差异。

来源： https://arxiv.org/abs/2611.13541

**开放偏好排行榜的排名可以被操纵多达 45 位。** 策略性投票、提示词设计和模型提名各自能让一个模型移动 15 至 20 位，组合使用则带来更大变化。分析使用了公开排行榜数据。

来源： https://arxiv.org/abs/2611.14769

**只有在事后挑选最佳改写时，改写问题才将准确率提高了 27.6%。** 盲目改写每个问题，反而使准确率降低 5.6%。一项学得的规则在其选择改写的案例上获得了 11.0% 的提升。

来源： https://arxiv.org/abs/2611.14997

**在 Continual-ARC 上，固定不变的智能体运行框架学到的内容，少于一个示范缓存。** 它们在未见任务上没有收益，而改变模型权重的方法表现更好。作者发布了代码与运行记录。

来源： https://arxiv.org/abs/2611.14505

**研究智能体几乎所有的构思进展，都发生在 100 个问题中的前 30 个。** 一款基于 200 篇 ICML 2026 论文构建的游戏表明，瓶颈变成了生成有用问题，而非识别答案。

来源： https://arxiv.org/abs/2611.14487

**当数据和轨迹生成预算匹配时，监督微调的泛化能力与强化学习相当。** 在 Qwen2.5 和 Qwen3 上，结合 SFT 与 RL 又超过了单独使用 RL。这篇 NeurIPS 2026 论文认为，以往差异部分来自数据，而非学习规则。

来源： https://arxiv.org/abs/2611.14912

## 经济与就业

**美国软件开发招聘信息同比增加 24%，发布的薪酬增速接近翻倍。** Indeed 的追踪数据还显示，截至 10月23日的一年中，总体招聘信息增加 3.1%，是近四年来首次转正。软件岗位薪酬增速在 9月达到 2.9%，一年前为 1.5%；专业服务业离职率仍比 2019年平均水平低近一个百分点。报告没有检验这些变化是否由 AI 引起。

来源： https://hiringlab.indeed.com/2026/11/12/2026-q3-us-tech-labor-market-update/

**Anthropic 的 IPO 页面将客户生产率大幅提升的说法，与 -3% 的 GAAP 营业利润率并列呈现。** Salesforce 报告，每名开发者的有效产出增加 151%；乐天（Rakuten）称，一项功能的开发从 24 个工作日缩短至五个；沃尔玛（Walmart）称，其购物智能体使平均订单金额增加约 35%。Anthropic 报告季度营收为 170 亿美元，净亏损为 233 亿美元，其中包括 219 亿美元非现金重估费用。这些是面向投资者的营销说法。

来源： https://ipo.anthropic.com/us/

**Meta 将 Muse 致电商家的功能纳入付费套餐。** 美国订阅用户目前每月最低支付 20 美元，可获得每周 5 亿 Muse token；100 美元套餐则包含 30 亿。TechCrunch 报道，有些接待员一发现来电者是 AI 就挂断电话。

来源： https://techcrunch.com/2026/11/12/muse-can-now-place-calls-to-u-s-businesses-if-you-pay/

**英伟达（Nvidia）在黄仁勋（Jensen Huang）辞职后一小时内损失约 5,460 亿美元市值。** 《连线》（Wired）计算，自丑闻开始以来，该公司市值已蒸发超过 1 万亿美元；而 AMD 在五天内上涨 28%，博通（Broadcom）上涨近 16%。这次波动将 AI 基础设施市场与领导层危机联系起来，而不是与芯片能力变化联系起来。

来源： https://www.wired.com/story/jensen-huang-tanked-a-trillion-dollars-in-less-than-a-month/

**Nebius 计划在 2027年支出 400 亿至 450 亿美元资本开支，但交付延迟使其股价下跌 17%。** 公司预计 2027年营收为 120 亿至 130 亿美元，此前第三季度营收为 9.81 亿美元。在价值最高 194 亿美元的微软（Microsoft）容量中，目前仅略多于一半预计年底前交付，其余延至 2027年第二季度。

来源： https://techcrunch.com/2026/11/12/nebius-tests-the-neocloud-playbook-with-40-billion-in-planned-spending/

**美国联邦航空管理局（FAA）将 SMART 建议系统扩展至全美 22 个航路交通管制中心。** 该机构称，自 9月21日以来，180 次改道平均为每架次节省十分钟和近 80 加仑燃油。人工专家会验证建议，但管制员工会表示，其超过 1.5 万名成员未被征询意见。

来源： https://arstechnica.com/ai/2026/11/faa-expands-ai-advice-to-manage-air-traffic-congestion-across-entire-us-airspace/

**Anthropic 推出 17 项现成制造业技能，但未发布部署结果。** Claude 可以帮助质量工程师记录未通过的检查、搜索早期报告和起草纠正措施，但不控制设备。公告没有提供客户的时间或质量测量数据。

来源： https://www.businessinsider.com/anthropic-launches-claude-for-manufacturers-ahead-of-ipo-2026-11

**超过 3,500 台 AI 引导激光设备，现正为挪威 1.12 亿条三文鱼处理海虱。** Stingray Marine Solutions 表示，部署量一年增加约 1,000 台，覆盖该国 20%–25% 的养殖三文鱼。效果数字来自公司。

来源： https://www.tomshardware.com/tech-industry/drones/3-500-ai-laser-robots-patrol-norwegian-salmon-farms-killing-sea-lice-parasites-get-zapped-by-high-tech-alternative-to-harsh-chemical-baths

## 提示词技巧

**LLMON 将每条指令绑定到带类型的数据块，而不是把所有内容放进一个扁平提示词。** 用保留分隔符标记指令、数据、要求和输出，为各块分配唯一 ID，再用最终执行块指定哪条指令作用于哪些数据。IBM 提供 JSON 转换器，并在 Mellea 中提供原生支持。

来源： https://huggingface.co/blog/ibm-granite/llmon-an-llm-native-markup-language-now-in-granite

**多智能体编排看板应生成元素 ID，并拒绝使用非自身签发 ID 的写入。** 一位实践者还使用智能体密钥为写入签名，将缺失数据视为无法验证，而不是通过，并把审查者的查看范围限制在其卡片的差异和直接调用方。这些规则来自一套实际配置，没有基准测试。

来源： https://old.reddit.com/r/ChatGPTCoding/comments/1xuf00x/i_posted_4_rules_for_multiagent_teams_the/

## 大家在做什么

**smolmaxxing 在电视盒上运行了 160 亿参数模型，在 2013年款 iPad 上运行了 17 亿参数模型。** 其 llama.cpp 补丁从闪存分页加载专家，并为 Cortex-A55 添加低比特内核。构建者报告，Ling-mini-2.0 在小米电视盒上的速度为每秒 5.1 个 token，Bonsai-1.7B 在 iPad 上为每秒 24 至 26 个。

来源： https://github.com/hyperionaidev/smolmaxxing/

**Kinetic 为 Rust GGUF 推理引擎加入精确推测解码。** 它支持 CPU，以及英伟达、AMD 和英特尔（Intel）GPU。构建者报告，首次运行中，编辑任务速度最高提升至 2.5 倍，生成任务最高至 1.4 倍；在 RTX 4060 上出现过一次未能复现的精确性失败。

来源： https://github.com/Veloresearch/kinetic

**Kiln 可直接在 WebGPU 中运行 safetensors、PyTorch 和 GGUF 模型，无需导出 ONNX。** 它保留 transformers.js 的 API 名称，并在加载时量化为四比特或八比特。作者报告，在 31 组模型与任务组合上，端到端加速中位数为 2.2 倍。

来源： https://github.com/erdemozkan/kiln

**warmctl 将已预热的八块 H100 vLLM 引擎恢复时间从 650 秒缩短至 37 秒。** 它为权重加载、编译、自动调优和 CUDA 图捕获创建快照，以便在匹配的主机上恢复。时间数据来自构建者测量，且需要 root 权限。

来源： https://github.com/TensorRails/warmctl

**LibreAGI 使用私有 BitTorrent tracker 和稀缺性积分保存开放权重模型。** 一份签名的公开目录记录哈希和来源提交，以便网站消失后重建共享网络。访问需要申请。

来源： https://libreagi.com/

**ZigZag 让智能体通过 MCP 创作刺绣设计。** 这款 Rust 编辑器将 SVG 图稿转换为针迹，导出五种机器格式，并能通过蓝牙将设计发送到 Brother Skitch。作者在发现一台 300 美元的机器还要求订阅后，编写了这款工具。

来源： https://github.com/simpsoka/zigzag

**Whiteboard AI Tutor 将模型生成的绘图指令以 JSON 流式输出，并对六种辅导模型进行基准测试。** 其盲评从 288 节课中审查了 64 块白板，总成本为 4.83 美元。Gemini 4 Argon 的 11 块受审白板全部通过，Claude Haiku 5.5 通过九块，但作者提醒样本很小。

来源： https://github.com/molly554/whiteboard-ai-tutor

**ZeroPoint 是一款 89 MB 的 CPU 决策模型，可以回答“以上都不是”。** 作者报告，在 900 个案例中，它的准确率为 53.6%，延迟中位数为 42 毫秒；相比之下，一个 20 亿参数 GPU 模型的准确率为 58.6%，延迟为 6.77 秒。测试由开发者编写。

来源： https://github.com/Javihaus/zeropoint

**AgentRun 让托管智能体在不同运行之间保留笔记、技能和工作流。** Parcha 表示，一个调优后的审查者将每个拉取请求的成本降至 18 美分，并在 30 个未见过的拉取请求上发现了某商业工具 1.6 倍的真实缺陷。这份案例研究由公司制作。

来源： https://github.com/Parcha-ai/agentrun

**Silos 在由策略管理的 Docker 沙箱中运行不可信智能体。** 它控制网络出口，通过代理提供带审计日志的推理服务，并管理集成所需的凭据。这个 TypeScript 项目需要 Docker。

来源： https://github.com/SilosLabs/silo-cli

**Cloakroom 在编程智能体看到内容前，遮蔽 API 密钥、密码和个人数据。** 智能体写入占位符后，它在本地文件和命令中恢复真实值。它支持 Claude Code、Codex、Gemini CLI 和 Cursor。

来源： https://github.com/shanjeevrajendran/cloakroom

## 值得一读

**EUROPA 将一款 9,519 亿参数模型的训练吞吐量，从每 GPU 每秒 90 个 token 提高到约 1,300 个。** 工程师在 EuroHPC 的 JUPITER 上共享 384 块 GH200 GPU，为 Muon 对专家进行分片，将检查点卸载到 Grace CPU，并修复了一个 PyTorch 分配器缺陷。修复已贡献到 PyTorch 和 TorchTitan 上游；尚未公布模型质量结果。

来源： https://pytorch.org/blog/training-a-1t-parameter-moe-on-eu-public-infrastructure-with-pytorch-and-torchtitan/

**Project EVE 测试 Claude 独立交易，以及在被暗中破坏的智能体团队中担任成员的表现。** 从 Opus 4.6 到 Fable 5，平均模拟利润增至三倍，但即使 Fable，也只有约一半运行能靠方向性押注赚钱。智能体团队几乎从未发现某个队友被秘密要求破坏团队。

来源： https://www.anthropic.com/research/project-eve-claude-plays-mmorpgs

**数据库研究者 Thomas Neumann 质疑 AI 生成数据库引擎所报告的 22 至 61 倍提升。** 他认为，基准结果意味着物理上不可能的内存流量，反映的是对测试的过拟合。文章审视的是所声称的测量结果，而非提出一个竞争引擎。

来源： http://databasearchitects.blogspot.com/2026/11/next-level-benchmarking-overfitting.html

**PyTorch 的 Helion 现在在编译时选择内核设置，而不再运行昂贵的自动调优。** Meta 报告，在 H100 上，其 Flash Linear Attention 性能为手写 Triton 的 1.18 倍，归约算子性能为 vLLM 的 1.27 倍。此前一次分页注意力自动调优曾耗时 10 至 25 小时。

来源： https://pytorch.org/blog/fast-by-default-compile-time-heuristics-for-helion-kernels/

**IBM 工程师与编程智能体在不到一周内，将 SGLang 与 Spyre 加速器集成。** 据供应商撰写的报告，这个约 1,500 行的插件，吞吐量达到参考 torch-spyre 路径的约 3.6 倍，并在受测工作负载上与 vLLM 持平。

来源： https://pytorch.org/blog/integrating-sglang-into-spyre-in-under-a-week-with-ai/

**Zonder Labs 在抽样 AI 文章的 54% 和 Claude Code 消息的 78% 中发现了表达不清的问题。** 人类对照组比例分别为 10% 和 11%。页面未说明样本量或标注人员，因此这些百分比只是线索，并非基准测试。

来源： https://zonderlabs.com/slop

## Hacker News

**实践者争论应如何解读 Anthropic 的 233 亿美元净亏损。** 有人将其视为泡沫证据；另一些人指出，其中 219 亿美元来自将在 IPO 时转换的金融工具的非现金重估。评论者的替代计算并非审计。

来源： https://news.ycombinator.com/item?id=50465829

**Gemini Hydrogen 用户讨论了命名、价格和自动模型选择。** 评论者将 Antigravity 的 Orchestrator 与 Anthropic 的顾问模式比较，并质疑提示词缓存在 Hydrogen 与 Carbon 之间如何运作。另一些人反对谷歌以元素命名模型，因为名称看不出哪个档位更强。

来源： https://news.ycombinator.com/item?id=50471431

**Jane Street 的 Socratic Tutor 技能，让实践者对智能体指令能否帮助学习产生分歧。** 该文件要求编程助手通过提问而非直接给答案来教学。一些评论者称它只是套话；另一些人说，这种方法终于帮他们学会了 Lean。

来源： https://news.ycombinator.com/item?id=50438261

**Humble Bundle 用户报告，重新设计的网站不再要求双重验证代码。** 评论者还报告登录邮件延迟。网站重写由 AI 完成的说法来自论坛发帖者，并非代码证据或公司声明。

来源： https://news.ycombinator.com/item?id=50463899

**开发者争论，一个月不进行拉取请求审查，能否证明这项实践已经过时。** 作者称变化效果很好。回复者认为，审查也能传播理解，而长期维护成本需要更久才会显现。

来源： https://news.ycombinator.com/item?id=50462613

## Reddit

**在一项测试中，一个带技能的智能体以约低 40% 的成本和一半时间，达到子智能体团队的水平。** 一位 Claude Code 用户用每种配置各构建了七次相同的预订网站，并报告质量相近。结果仅来自一个人的测量。

来源： https://old.reddit.com/r/ClaudeCode/comments/1xuqnnc/i_tested_anthropics_one_agent_with_skills_beats_a/

**OpenAI 网络安全主题演讲的一张图表显示，某内部模型在 ExploitGym 上得分为 77.0%，Claude Mythos 5.2 为 39.2%。** 这项包含 869 个任务的基准数字由 Reddit 发帖者转录，并非以完整模型报告发布。

来源： https://old.reddit.com/r/OpenAI/comments/1xurxd4/openais_internal_cyber_model_hit_770_on/

**在同一项 Next.js 功能上，三个编程智能体使用了差异很大的 token 数量、额度和套餐价格。** 发帖者比较了 Codex、Google Antigravity 和 Meta Muse Code 完成同一任务的情况。帖子只涉及一个工作负载，并非受控基准测试。

来源： https://old.reddit.com/r/ChatGPTCoding/comments/1xugdkv/i_tested_codex_google_antigravity_and_meta_muse/

**一个简洁输出插件让回复缩短 17%，却让成本增加 11%。** 作者对十项任务各运行六次；输出 token 减少 8%，成本却上涨，95% 区间为 7%–15%。简洁指令既改变了可见文本，也改变了推理行为。

来源： https://old.reddit.com/r/ChatGPTCoding/comments/1xu266g/i_built_an_opensource_cli_that_shows_where_your/

## YouTube

**斯坦福大学（Stanford University）教授 Diyi Yang 讲解函数调用、MCP，以及智能体如何学习使用工具。** 这场英语 CS329Z 讲座涵盖 Toolformer、ToolLLM、Gorilla，以及 BFCL 和 tau-bench 等评测，包括常见失败模式。

来源： https://www.youtube.com/watch?v=s0S38lz6O7M

**Hadley Wickham 认为，即使代码由 AI 编写，它仍是推理的产物。** 在一场英语 Priestley Award 演讲中，这位 tidyverse 作者解释了为什么学习编程对可复现性和判断力仍然重要。

来源： https://www.youtube.com/watch?v=HMifrFaYmVc

**Paul Christiano 以一场关于变革性 AI 治理的演讲，为 Hinton Lectures 收尾。** 这场英语讲座涵盖独立评测、外部监督、共同标准和国际合作，随后与 Geoffrey Hinton 进行讨论。

来源： https://www.youtube.com/watch?v=s0qUNvgFgHg

**一场斯坦福座谈会介绍研究者如何划定 AI 使用边界。** 这场英语讨论覆盖法律、人文学科和生物工程，涉及披露、技能退化，以及不用 AI 撰写推荐信的决定。

来源： https://www.youtube.com/watch?v=PeRJkvzIEts

**捷克实践者 Libor Vaněk 解释廉价 AI token 背后的基础设施成本。** 他在捷克语 Frontendisti 演讲中，利用公司使用 8×H200 NVL 和 4×H100 裸机服务器的经验，讨论性价比和投资回报。

来源： https://www.youtube.com/watch?v=EEC3zsfNyQw

**斯洛伐克心理学家 Branislava Očvárová 探讨 AI 是否会制造虚假的理解感。** 这期斯洛伐克语赞助播客提供的是保持判断力的一般建议，而非实验证据。

来源： https://www.youtube.com/watch?v=-J2wInJwDFc

## 简讯

**OpenAI 基于专注网络安全的 GPT-6 Cyber 模型，推出 Daybreak Red Team 和 Defense Factory 智能体。** Red Team 探测应用并验证漏洞；Defense Factory 为工程师生成补丁和测试。The Register 报道了供应商说法，但没有独立测量。

来源： https://www.theregister.com/security/2026/11/12/openai-launches-security-products-tells-orgs-theyre-doomed-if-they-dont-use-them/5309500

**一名攻击者利用 4,837 个被劫持的 GitHub 账户植入 CI 机密窃取程序。** 据安全研究者称，探测性拉取请求到达了 61,764 个仓库，恶意提交出现在至少 8,093 个仓库中。载荷窃取 GitHub token、云凭据和 AI 服务密钥。

来源： https://www.aikido.dev/blog/compromised-github-accounts-push-ci-secret-stealer-to-tens-of-thousands-of-repositories

**研究者发现，仿冒 27 个 AI 品牌的 186 个近似域名正在分发恶意软件或搜索劫持程序。** 这场行动使用虚假的 Cloudflare 检查、浏览器恶意软件，以及 Chrome Web Store 上 16 个仍在线的扩展，这些扩展声称共有 972,000 名用户。

来源： https://thehackernews.com/2026/11/186-fake-ai-domains-redirect-users-to.html

**一项供应商研究发现，AI 聊天机器人在 4%–15% 的购物回答中提到了有风险的零售网站。** 在有关 151 个品牌的 6,795 个回答中，Perplexity 的比例为 15%，ChatGPT 为 8%，Gemini 为 4%。提示词由知识产权保护公司 Podqi 设计，其定义也包括对某网站发出警告的情况。

来源： https://www.theverge.com/ai-artificial-intelligence/1032020/gemini-chatgpt-perplexity-shopping-test-risky-fake-websites-citations

**四个倡议团体起诉，要求冻结超越当前前沿水平的 AI 系统开发。** 这份加利福尼亚州诉状依据不正当竞争和公共妨害法律，援引实验室事件报告及评测逃逸情况。这是诉状，而非判决。

来源： https://www.unite.ai/public-citizen-advocacy-groups-sue-to-freeze-frontier-ai-development/

**FreeBSD 的一项调查发现，140 名受访者中有 84% 希望披露 AI 使用情况。** 78% 希望强制人工审查，16% 则会直接拒绝 AI 辅助代码。项目尚未发布最终政策。

来源： https://www.theregister.com/os-platforms/2026/11/12/the-latest-freebsd-report-is-here-and-the-ai-debate-is-ongoing/5309206

**Google DeepMind 员工因军事 AI 合同问题寻求法定工会承认。** 如果英国申请成功，约 1,000 名产品员工可参加有约束力的投票。员工希望谷歌退出与美国及以色列军方的协议。

来源： https://www.wired.com/story/google-deepmind-staff-escalate-their-union-fight/

**谷歌警告，三个 AMD Turin 侧信道漏洞需要操作系统补丁，以及关机再启动。** 对受影响的 C4D、N4D、H4D、Z4D 和 G4 云实例，普通重启并不足够。谷歌将漏洞评级为中等，并表示已经应用主机级缓解措施。

来源： https://thehackernews.com/2026/11/google-cloud-warns-three-amd-turin-cpu.html

## 商业简讯

**英伟达尚未完成的 130 亿美元 Hugging Face 收购和 60 亿美元 Poolside 许可交易，如今交由临时首席执行官处理。** 来源： https://techcrunch.com/2026/11/12/jensen-huangs-exit-puts-nvidias-support-for-open-source-in-question/

## 后续关注

Inception Labs 将于 12月28日关闭 Mercury API。Anthropic 计划于 11月18日为 IPO 定价，并于 11月19日以 ANT 为股票代码开始在纳斯达克（Nasdaq）交易。
