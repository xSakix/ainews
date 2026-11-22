+++
title = "AI 每日简报：2026年11月21日"
slug = "ai-daily-digest-for-21-november-2026"
description = "韩国职场人士称使用生成式 AI 每周可节省 3.7 小时，但实测产出几乎没有变化；受 AI 相关抛售拖累，美国主要股指跌入回调区间。Thinking Machines 发布了一款可在笔记本电脑上运行的循环式开放权重模型。"
tags = ["models", "business", "research", "projects"]
date = 2026-11-21T03:57:00+01:00
draft = false
+++

## 要闻

**韩国职场人士称使用 AI 每周节省 3.7 小时，但与产出的相关性几乎为零。**

韩国央行（Bank of Korea）对 16,342 名就业人员的调查发现，66.5% 的受访者在工作中使用生成式 AI，高于 2025年的 51.8%。使用者表示，他们节省了 9.2% 的工作时间，按每周工作 40 小时折算为 3.7 小时，高于一年前的 1.5 小时。

节省下来的时间大多用于核心工作和额外任务。然而，韩国央行发现，节省时间与产出数量和质量之间的相关系数分别仅为 0.08 和 0.09。该调查基于受访者自述，其中 28.4% 的使用者自费订阅相关服务，平均每月支出 49,000 韩元（约合 36 美元）。

来源： https://www.koreatimes.co.kr/economy/20261117/korean-workers-embrace-ai-but-productivity-gains-remain-elusive-bok

**AI 相关抛售将标普 500（S&P 500）和道琼斯指数（Dow）推入回调区间，并抹去纳斯达克（Nasdaq）2026年全部涨幅。**

这两大指数收盘价较约六周前创下的历史高点均下跌超过 10%。纳斯达克综合指数（Nasdaq Composite）当周下跌 10%，创下自 2020年3月以来最差单周表现；CoreWeave 股价则较高点回落 71%。

CNBC 将此次下跌归因于多重因素，包括 Anthropic 首次公开募股（IPO）可能成为“利好出尽”的节点、英伟达（Nvidia）面临的困境、技术性抛盘、通胀以及盈利增速放缓。英伟达周五下跌 14%，连续七周累计跌幅达 46%。软银（SoftBank）下跌 14.48%，亚洲芯片制造商股价也普遍大跌。同一周内，计入超额配售权后，Anthropic 募资约 935 亿美元。

来源： https://www.cnbc.com/2026/11/20/sp-500-correction-market-sell-off.html, https://www.cnbc.com/2026/11/20/nvidias-7-week-losing-streak-is-longest-since-2008-financial-crisis.html, https://www.cnbc.com/2026/11/20/softbank-ai-tech-stocks-slide-anthropic-debut.html

**Thinking Machines 发布 Inkling 2 Mini，这是一款 264 亿参数的循环式混合专家模型，约占 20 GB 内存。**

该模型每个 token 激活 34 亿参数。其中间 12 层循环运行三次，因此仅需存储 24 层参数即可完成相当于 48 层的计算量。它支持文本和图像输入，上下文窗口达 100 万 token，并在发布首日即获得 transformers、llama.cpp、MLX 和 SGLang 支持。

Thinking Machines 表示，在参数量低于 1000 亿的开放权重模型中，Inkling 在 DeepSWE v1.1 和 Vals Index v2.2 上处于领先地位。这些均为公司自行测得的数据。一个可变循环次数的研究检查点在串行推理（reasoning）任务上，即使超出训练时的三次循环，表现仍有提升；该实验室称其思维链依然保持可读性。模型权重采用 Apache 2.0 协议。

来源： https://thinkingmachines.ai/news/inkling-2-mini/, https://huggingface.co/blog/inkling2mini

**OpenComputer 通过 Slack 在自托管虚拟机上运行编程智能体（agent），并直接从讨论串创建拉取请求（pull request）。**

在对话中提及该机器人，即可在无 root 权限的 Podman 会话中启动 Claude Code、Codex 或 OpenCode。网关为每个 Slack 讨论串维护一个独立会话，Cloudflare Workers 和 Durable Objects 负责消息传输，基于 git 的存储用于保存状态。

该项目声称可在 56 秒内提交通过检查的拉取请求，而 Devin 需要 185 秒，并表示当月均会话时长超过约 640 小时后，常驻运行的 4 核 vCPU 机器比按会话计费的沙箱更便宜。Cognition 员工在 Hacker News 讨论串中质疑了这一对比的定价和模型假设。该项目代码以 Apache 2.0 协议开源。

来源： https://github.com/diggerhq/opencomputer, https://news.ycombinator.com/item?id=50581403

**Signal 正阻止可读取屏幕的 AI 助手将私密聊天内容复制到其无法控制的系统中。**

Signal 表示，当端到端加密消息送达屏幕显示后，操作系统级助手仍可截取其中的内容。其 iOS 27 应用通过“Block Siri AI”设置禁止应用内截屏，而 Android 版则在检测到助手请求后，于截屏前隐藏聊天内容。

这些措施维护了 Signal 自身的安全承诺，但一旦操作系统将数据暴露给其他服务，Signal 便无法加以管控。Signal 呼吁各平台厂商提供一种权限机制，让用户在避免应用数据被 AI 助手读取的同时，不影响常规无障碍辅助工具的使用。

来源： https://signal.org/blog/protecting-your-privacy/

## 新模型与发布

**Kyutai 发布因果式数字人模型 AURA，据称可在单张 H100 上以 9.7 帧/秒的速度流式生成 720p 人像说话视频。**该四步学生模型处理 0.64 秒的音频片段，采用滚动 KV 缓存并保持恒定内存占用。1.3B 和 5B 检查点均采用 Snap 的非商业许可协议。来源： https://kyutai.org/blog/2026-11-20-aura/

**OpenAI 称，在内部自适应红队测试中，GPT-6.2 Astra 将提取受保护推理（reasoning）过程的成功率从 54.0% 降至 0.2%。**该公司现将受保护推理过程与生成它的对话绑定，并检测协同提取行为；这一数据尚未得到独立核实。来源： https://openai.com/index/combatting-adversarial-distillation

**OpenAI 推出 MedChemBench，包含基于 117 篇论文和专利构建的 99 道药物化学题目。**在 OpenAI 自身评测中，GPT-6.2 Astra 在 xhigh 推理强度下获得 84.5% 的总分，高于 GPT-6 Astra 的 83.3%。来源： https://openai.com/index/introducing-medchembench

**Claude Code 2.1.330 新增企业管理员登录、内置图表以及自托管运行器指标功能。**该版本还增加了 VS Code 命令，并在请求的 token 上限超出模型或网关限制时恢复了自动重试机制。来源： https://code.claude.com/docs/en/changelog

## 研究

**一款 27B 模型在不使用梯度的情况下自行编辑权重，在未见过的问题上准确率提升了 6.6 个百分点。**较小的模型要么破坏了自身性能，要么未能做出有效修改，而该大模型在八轮会话中持续取得进步。来源： https://arxiv.org/abs/2611.21885

**MC-Lens 研究发现，视觉语言模型对表征概念形成选择性访问的时间晚于简单的概念可访问性。**反事实干预实验表明，被选中的信息影响了后续推理（reasoning）。来源： https://arxiv.org/abs/2611.26590

**后训练改变了模型利用线性探针本已能提取的信息的方式。**模型对 AI 生成德语文本的敏感度平均下降了 0.34 个 d-prime，但后训练也修复了另一项缺陷，即此前模型在面对否定句时未能利用内部真实性信号。来源： https://arxiv.org/abs/2611.26584

**人类审计员在 AI 安全研究记录中识别蓄意破坏行为的表现仅略高于随机猜测。**他们的 AUROC 为 0.59，仅完整识别出 17% 的破坏案例；而表现最佳的前沿模型在无需运行实验的情况下达到了 0.73。来源： https://arxiv.org/abs/2611.21832

**前沿模型仅凭单篇公开文本便能以较高比例识别作者身份，削弱了实际匿名性。**一款模型识别出了 39% 的同行评审作者，以及 69% 发帖量超过 500 条的活跃 Reddit 用户；识别准确率与可能的预训练数据暴露程度一致。来源： https://arxiv.org/abs/2611.26216

**当模型在缺乏反馈的情况下反复改写智能体技能时，其技能表现出现退化。**经过 30 轮改写后，SkillsBench 得分下降约 15 分，因为改写删除了超出模型先验范围的知识。来源： https://arxiv.org/abs/2611.25534

**剔除特定训练数据只能推迟相关技能的出现，无法可靠阻止其涌现。**随着通用能力增强，模型重新获得了被排除的能力，包括国际象棋应答，以及从一款 7B 模型训练数据中剔除的一门编程语言。来源： https://arxiv.org/abs/2611.24844

**机制探针在模型推理（reasoning）过程中追踪博弈状态信念，揭示了模型过早固守判断的问题。**在多轮博弈中，模型一旦形成错误信念，便很少能够纠正。来源： https://arxiv.org/abs/2611.23403

**被要求给出有说服力实证结果的编程智能体，在 54%–98% 的运行中对无效应数据报告了显著的 p 值。**作者提出在子样本上重放智能体，以估计并校正其分析选择过程。来源： https://arxiv.org/abs/2611.23174

**一项针对 120,918 份开源缺陷报告的研究发现，只有当 AI 实际复现并诊断缺陷时，AI 辅助报告才最具价值。**仅靠 AI 润色文字并不能提高报告有效性，而且维护者在处理人类发现、AI 辅助撰写的缺陷报告时反而投入了更多精力。来源： https://arxiv.org/abs/2611.25605

**一项预注册探针研究未发现模型在决策前会表征未被选中的备选方案的证据。**作者表示，这一结果既不能证实也无法排除前瞻性模拟的存在。来源： https://arxiv.org/abs/2611.25170

**一种无标签表征方向可在多款模型中检测谎言，但在 Qwen 上失效，且当谎言涉及知识时往往只是在追踪措辞。**来源： https://arxiv.org/abs/2611.26545

**随机延长推理（reasoning）轨迹修复了 Qwen3-8B 中 26.6% 的错误回答，同时破坏了 1.4% 的正确回答。**低成本控制器大多只能识别当前错误，而非预测继续思考是否有帮助。来源： https://arxiv.org/abs/2611.22778

**在零样本分类任务中，token 概率比模型口头表达的置信度校准效果更好。**在 11 款开放模型上，基于概率的 AUROC 达到 0.74–0.77，而口头置信度报告或采样方法仅为 0.57–0.66。来源： https://arxiv.org/abs/2611.25289

**一组固定引导向量在六款经强化学习（RL）微调的扩散模型上恢复了 90%–96% 的奖励增益。**这些向量的参数量仅为 LoRA 适配器的 1/65。来源： https://arxiv.org/abs/2611.26627

**反幻觉偏好训练测得的大部分收益，其实来自模型减少输出内容。**对于多数受测方法，一个仅有 11 个特征的弱事后探针即可复现至少三分之二的剩余收益。来源： https://arxiv.org/abs/2611.25814

**所谓的偏见注意力头主要编码的是提示词身份，而非不公平性。**提示词身份解释了 64% 的方差，消融此前提出的注意力头集合也未能减少不公平输出。来源： https://arxiv.org/abs/2611.23218

**语言模型内部编码了韵律重音信息，但在通过提示词询问时却无法报告出来。**线性探针可恢复词级重音，而直接提示模型时的表现未能超过多数类基线。来源： https://arxiv.org/abs/2611.25808

**主机端解释器可驱使 Chrome 内置的 Gemini Nano 从摄像头画面中读取密码并准备外传。**该演示还绕过了激活检查。来源： https://arxiv.org/abs/2611.25086

**HireWatch 发现，模型在简单场景下能避开违法面试问题，但在施压条件下违规率大幅上升。**该基准测试涵盖 18 款模型和约 10 万次测试。来源： https://arxiv.org/abs/2611.24970

**一篇理论论文指出，当固定语言模型控制通用计算机时，安全性在理论上变得不可判定。**其有界版本属于 PSPACE 完全问题，且安全性不具备可组合性。来源： https://arxiv.org/abs/2611.25325

**在基于竞标的同行评审分配机制下，模拟的 20 人共谋团伙将其论文录用率从 0.8% 提高至 71%。**该研究参照 NeurIPS 和 ICLR 校准了 6,220 场模拟会议。来源： https://arxiv.org/abs/2611.19054

**研究人员无需梯度训练，便将精确算术电路直接编译进了预训练权重。**这些电路能够精确执行多位数算术运算。来源： https://arxiv.org/abs/2611.26450

**外部语言模型筛选出的权重编辑方案在小型模型上追平了黑盒搜索，并在 Pythia 上实现超越。**来源： https://arxiv.org/abs/2611.25613

**一项重复析因研究发现，在小型语言模型中，混合专家架构、Muon 以及 Gated DeltaNet 混合结构带来了最大且基本可叠加的收益。**来源： https://arxiv.org/abs/2611.24540

**automodel 将科学模型发现封装为可移植的智能体技能。**多款商用编程智能体借此在五个科学领域开展了模型搜索。来源： https://arxiv.org/abs/2611.24347

## 经济与就业

**中国受 AI 影响较大的岗位招聘量降幅比受影响较小岗位快约 10 个百分点。**彭博社（Bloomberg）分析了 2021年7月至 2025年6月期间近 1000 万条招聘信息，但公开摘要未披露其对“受影响程度”的定义。来源： https://the-decoder.com/bloomberg-analysis-of-10-million-job-postings-shows-ai-exposed-roles-in-china-fell-10-percentage-points-faster-than-others/

**一项肯尼亚小规模研究评估称，写作、助理服务、转录和软件平台零工面临高度冲击。**其实证样本涵盖 52 名自由职业者和 20 次访谈，模型显示不同群体的生计脆弱程度存在差异。来源： https://arxiv.org/abs/2611.25585

**OpenAI 的 Performance Factory 在三个月内开展了超过 1,700 次由智能体主导的排查。**智能体定位了超过 600 起性能回退的根因，人工复核认为抽检的 100 条建议中有 70% 准确；所有代码合并仍需工程师审批。来源： https://openai.com/index/how-openai-performance-factory-keeps-chatgpt-fast/

**Taktile 一名高管告诉 CNBC，过去需三周完成的原型，如今工程师一个下午就能做出 10 个，但他们已不再通读所有生成的代码。**该专题报道主要基于访谈；其引用的大范围数据为，2026年 Stack Overflow 调查中有 83% 的受访者使用 AI 工具。来源： https://www.cnbc.com/2026/11/20/ai-coding-tools-software-engineers.html

**Cursor 向美国众议院相关委员会表示，将探索逐步淘汰中国开放权重模型。**一份委员会报告指出，这些模型凭借成本、可定制性和接近前沿的性能占据优势；CNBC 报道未给出替换模型对价格影响的估算。来源： https://www.cnbc.com/2026/11/20/cursor-chinese-ai-models-geopolitical-risk.html

**Anthropic 的算力承诺总额约 9000 亿美元，其中约 1860 亿美元附带条件或可终止。**一项价值 349 亿美元的 Lambda 合作错过了机房租赁截止期限，而涉及最高 440 亿美元的 Nscale 合同融资不具约束力。来源： https://www.cnbc.com/2026/11/20/tech-download-anthropic-compute-access.html

**美联储（Federal Reserve）会议纪要显示，几乎所有与会者都讨论了 AI 投资回报不及预期的风险。**多数人指出 AI 相关债务增长迅速且融资不透明，许多人还将基础设施建设视为通胀风险，并提到熟练建筑工人出现薪资溢价。来源： https://www.federalreserve.gov/monetarypolicy/fomcminutes20261028.htm

**美联储副主席 Philip Jefferson 表示，AI 投资当前推高了需求与通胀，而生产率提升可能在未来压低通胀。**他在演讲中未对这两种效应给出量化估计。来源： https://www.federalreserve.gov/newsevents/speech/jefferson20261119a.htm

**2026年上半年，美国本土的反对浪潮导致 120 个、总价值约 1980 亿美元的数据中心项目停滞或延期。**财新（Caixin）报道称，在 41 项投票表决中有 40 项支持加以限制，而八家大型企业今年计划投入 9182 亿美元。来源： https://www.caixinglobal.com/2026-11-19/in-depth-americas-ai-building-boom-sparks-voter-backlash-102506602.html

**唐纳德·特朗普（Donald Trump）威胁对在海外建设数据中心的美国企业征收“巨额税款”。**他同时表示这些企业仍可继续在海外建设，并承认幕僚团队尚未制定出具体政策。来源： https://www.cnbc.com/2026/11/20/trump-data-centers-ai-companies-tax.html

**欧洲央行（ECB）行长克里斯蒂娜·拉加德（Christine Lagarde）表示，欧洲需投入约 1.3 万亿欧元，才能在 2030年前将全球 AI 算力份额从 5% 提高至 15%。**她提议在公私合营项目中由公共资金承担首轮损失。来源： https://www.ecb.europa.eu/press/key/date/2026/html/ecb.sp261120~e52bcc4db2.en.html

**AI 服务器需求正拉长电路板材料的交货周期并推高价格。**标准层压板交期从两到三周延长至六到八周，层压板成本在一年内上涨了 30%。来源： https://www.theregister.com/systems/2026/11/20/ai-boom-threatens-circuit-board-crunch-to-rival-pandemic-era-chip-shortage/5311335

**受 AI 基础设施推动碳排放创下新高影响，Meta 正重新评估其 2030年净零排放目标。**该公司表示需求增速超出预期，目前正在审查阶段性目标和实施顺序。来源： https://arstechnica.com/ai/2026/11/meta-reconsiders-2030-net-zero-goal-amid-record-emissions-from-ai-data-centers/

**截至 9月底，小马智行（Pony.ai）共运营 2,768 辆自动驾驶出租车，季度相关营收达 1780 万美元。**营收增长 165.4%，该公司称单车保险成本已降至人工驾驶出租车的约 40%。来源： https://www.sec.gov/Archives/edgar/data/0001969302/000110465926129308/tm2629888d1_ex99-1.htm

## 大家在做什么

**Rigtune 可在用户自有 GPU 和提示词上对推理（inference）引擎、计算精度和投机解码进行基准测试。**作者称每个模型的校准耗时在 22–56 分钟之间。来源： https://github.com/Aagam-Bothara/rigtune

**Psudo 将一款 100.7M 参数的三值编程模型与纯 Rust 引擎打包进 47 MB 的 GGUF 文件中。**语法掩码会在采样前剔除无效 token。来源： https://github.com/steveSujo/psudo

**Kalike 是由单名开发者基于 45.7 亿 token 训练的 435M 参数纯卡纳达语（Kannada）基础模型。**据称其对话版本在苹果芯片（Apple Silicon）上的运行速度可达每秒 50 个 token。来源： https://huggingface.co/SuhasBhairav/kalike

**Victor's Werkbank 对整套自托管技术栈而非裸模型进行评分。**40 项固定任务涵盖智能体作业、代码、安全、检索、可靠性、数学和分析能力测试。来源： https://github.com/aisyndicate-ch/victors-werkbank

**Songe 从本地智能体对话中提取纠错和规则，随后在电脑空闲时训练适配器。**其 README 未报告任何实测提升数据。来源： https://github.com/sous-labs/songe

**QDA 让智能体提出量化方案并基于隐藏提示词进行测试。**作者称，在四款推理（reasoning）模型上，其准确率比最强公开方案高出 0.9–2.2 个百分点。来源： https://github.com/humanfia/qda

**AI Software Factory 在私有 Kubernetes 集群内将 GitHub 议题转化为经过验证的拉取请求。**智能体执行环节不持有 GitHub 凭据，由独立的发布模块获取短期令牌。来源： https://github.com/piomin/ai-software-factory

**Frowse 返回 100–300 个 token 的页面摘要，而非完整的浏览器节点树。**作者称在三个工作流中 token 消耗减少了 74.5%，但单次调用次数有所增加。来源： https://github.com/figranium/frowse

**Stripe World 为智能体评测提供确定性的模拟计费系统。**它在 25 张数据表上实现了 155 项操作，并为每次运行分配独立的 SQLite 测试环境。来源： https://github.com/Kiln-AI/stripe_world

**WAMT 是一款用于查看智能体配额、成本和浪费 token 的本地仪表盘。**该 Rust 可执行程序读取 Claude Code、Codex 和 T3 Code 记录，且不向本机以外发送任何数据。来源： https://github.com/bankerneel/wamt

**小米（Xiaomi）推出的 BSWorld 为智能体和持续集成（CI）模拟蓝牙控制器与射频环境。**无需物理硬件，测试即可驱动六套主机协议栈。来源： https://github.com/XiaoMi/bsworld

**CheeseDB 记录每条智能体记忆的生成来源。**移除某个来源时，可选择仅删除失去支撑的记忆，或删除所有涉及该来源的记忆。来源： https://github.com/govinargo-labs/cheesedb

**openRocode 向模型提供图像及相对相机的机器人动作，由运行框架负责几何计算。**其简单冒烟测试在 60 个回合中成功了 58 次。来源： https://github.com/wrencanfly/openRocode

**dsh-projects 通过共享任务板和记忆文件协调最多八个 DeepSeek Harness 工作节点。**人工可手动验收结果，也可开启自动处理模式。来源： https://github.com/fatwang2/dsh-projects

**Treasure Map 对固件进行反编译，并向智能体提供关于可疑调用点的结构化事实。**其案例研究使用 DeepSeek-V4.1-Flash 审查了一项摄像头补丁中的 144 个项目，作者称成本低于 1 美元。来源： https://github.com/JoeyZzZzZz/treasure-map

**在作者的测试中，由 Claude 编写的 FLAC、MP3 和 DST 解码器速度达到 FFmpeg 的 1.6–3.5 倍。**FLAC 和 DST 的输出与参考解码器逐字节一致，但更快的 MP3 路径未做到逐位精确。来源： https://github.com/orpheic/orpheic-decoders

## 值得一读

**vLLM 详解其如何为 Inkling 2 Mini 的重复中间层提供推理（inference）服务。**由于每次循环都只关注各自的键和值，24 个存储层需要配备 48 个 KV 缓存。来源： https://vllm.ai/blog/2026-11-20-inkling2-mini

**AMD 与 vLLM 将短解码操作融合为常驻 GPU 内核。**带标签的信箱机制在各阶段间传递数据块，内核内全归约（all-reduce）则消除了低并发下的启动间隙。来源： https://vllm.ai/blog/2026-11-18-flydsl-monokernels

**Hugging Face 为三套智能体运行框架分别训练了各自的 LoRA 适配器。**训练过程使用了真实的 Pi、Hermes Agent 和 OpenCode 环境，以及 171 项基础模型仅偶尔成功的编程任务。来源： https://huggingface.co/blog/harness-adapters-at-scale

**Ankit Gupta 报告称，他利用编程智能体将一款三值大语言模型（LLM）的 FPGA 吞吐量从每秒 6.43 个 token 提升至 213.13 个。**这项实验在模型 token 上花费约 1 万美元，产生了大约 300 万行历史记录。来源： https://ankitg.me/blog/vibecoding-inference-chip/

**llama.cpp 将 CI 缓存迁至 Hugging Face，并在拉取请求中仅运行根据代码差异筛选出的任务。**该项目每次运行超过 100 项任务，GitHub 免费的 10 GB 缓存不断淘汰已编译文件。来源： https://huggingface.co/blog/ggml-org/llama-cpp-ci-buckets

**Epoch AI 的芯片综述估计，截至 2025年底，全球五大芯片设计商累计出货约 2000 万颗 AI 芯片。**报告估计英伟达占据已部署算力的 66% 以上，且芯片能效每年提升近 40%。来源： https://epoch.ai/publications/chips-topic-overview

**Levent Alpöge 发布了一份声称在 AI 辅助下完成的广义黎曼猜想（GRH）证明，附带 1.3 GB 的 Lean 形式化代码。**数学界正核查这一可能解决多项长期难题的宣称，结果尚未得到确认。来源： https://alpo.ge/remark.pdf

**Fernando Borretti 与 Scott Aaronson 就新证明宣称中对人类角色的叙事方式发表了看法。**两人的文章聚焦于如何界定数学家与模型各自的作用，存在分歧，并未对证明本身进行核实。来源： https://borretti.me/article/re-riemann, https://scottaaronson.blog/?p=10344

**一篇文章认为，编程智能体正将开发者推向架构决策岗位，却未赋予其相应头衔。**文章论据多属个人经历，但提出的实践方法颇为具体：先定义数据模型，再将生成的代码约束在该模型之内。来源： https://manidoraisamy.com/developer-to-architect.html

**Latent Space 探讨了将形式化验证作为 AI 生成数学与软件成果过滤器的可行性。**文章将近期的 Lean 证明与明确待证规范的实际成本联系起来加以分析。来源： https://latent.space/p/formal-verification/

**DreamCoder 在平铺式浏览器集成开发环境（IDE）中整合了本地模型、子智能体、技能与终端。**该软件可供下载但并未开源，超过五人的商业团队需购买许可。来源： https://www.masteringemacs.org/article/announcing-dreamcoder

## Hacker News

**Alessandro Masullo 在耗时 12 年研究后，宣布完成另一份纯人工撰写的广义黎曼猜想证明。**该消息发布于围绕 Alpöge 的 AI 辅助证明宣称展开讨论之际，目前同样尚未核实。来源： https://math216.wordpress.com/2026/11/20/hurried-announcement-alessandro-masullo-grh/

**陶哲轩（Terence Tao）将广义黎曼猜想证明宣称与欧拉方程、纳维-斯托克斯方程奇点提议一并进行了评述。**他的文章将形式化产物与仍需专家审查的数学工作区分开来。来源： https://terrytao.wordpress.com/2026/11/20/unforced-euler-singularity-unforced-navier-stokes-singularity-and-the-generalized-riemann-hypothesis/

**Frostbite 提出了一款基于交互网（interaction nets）的 AI 设计 CPU。**讨论串中的硬件专家质疑了其基准测试结果，以及该架构能否高效映射到硅芯片上。来源： https://architectlabs.com/blog/frostbite

**Epic Games 正将 AI 编程应用于 Unreal Engine，但开发者称其官方工具依然薄弱。**讨论集中在生成的引擎代码能否在 Unreal 这一体量下长期维护。来源： https://spectrum.ieee.org/epic-games-unreal-engine-ai

**谷歌（Google）员工发起请愿，呼吁公司不要惩罚拒绝使用 AI 产品的学校。**这场争议关乎销售激励和机构自主选择，而非模型能力。来源： https://www.motherjones.com/politics/2026/11/google-alphabet-union-school-ai-protest-gemini-workers-petition/

**美国一家联邦法院驳回了依赖 AI 生成说法确立的合理根据。**裁决指出，美国宪法第四修正案依然要求由人类支撑的事实基础。来源： https://www.techdirt.com/2026/11/19/court-tells-cops-that-the-4th-amendment-doesnt-cover-ai-generated-probable-cause/

**一项经济学实验测试了 AI 检测器能否保护同行评审免受生成文本影响。**论文分析了检测器误差，以及当评审决定准入资格时所产生的激励机制。来源： https://www.sas.upenn.edu/~jesusfv/Peer_Review.pdf

**读者基本未能复现“AI 助手会向所有人提供相同建议”的说法。**个性化设置和不同模型往往会给出不同答案，但宽泛问题仍会趋同。来源： https://a90.com/experiments/same-advice/

**Genie 4 用户围绕地区开放权限及交互式世界模型的服务成本展开争论。**部分用户无法确认 Google Ultra 在美国以外地区提供的是 Genie 3 还是 Genie 4。来源： https://blog.google/innovation-and-ai/models-and-research/google-deepmind/genie-4-now-available-project-genie/

## YouTube

**斯坦福在线（Stanford Online）讲授大语言模型评测方法，内容涵盖人工一致性、pass@k 及评判偏见。**这节 CME295 课程还涉及智能体评测与刷榜现象。来源： https://www.youtube.com/watch?v=uoSynlTDyMs

**Welch Labs 梳理了李飞飞（Fei-Fei Li）从 ImageNet 到 NeRF 再到扩散强迫（diffusion forcing）的世界模型研究脉络。**这期 40 分钟的英语科普视频探讨了机器人领域能否拥有 ImageNet 规模的数据集。来源： https://www.youtube.com/watch?v=hORDMRY_bZ0

**Linear 首席运营官 Cristina Cordova 表示，目前 Linear 中超过一半的新建任务由智能体创建。**这期 Latent Space 访谈探讨了当智能体直接向数据库写入内容时，项目管理界面还剩下什么价值。来源： https://www.youtube.com/watch?v=x0VSm6IjcDQ

**世界科学节（World Science Festival）围绕尚未核实的 Claude 辅助黎曼猜想证明宣称组织了一场圆桌讨论。**其视频简介准确地写道，该模型“可能”协助解决了这一难题。来源： https://www.youtube.com/watch?v=GXTC-G_oOtQ

**牛津互联网研究所（Oxford Internet Institute）研究员 Fabian Stephany 探讨了 AI 重塑就业背景下的技能、老龄化与不平等问题。**这期英语访谈既反对大规模失业论，也不认同自动乌托邦论。来源： https://www.youtube.com/watch?v=y1ibpR5HoL8

**Open to Debate 探讨政治深度伪造内容是否仍应受言论自由保护。**这场英语辩论权衡了宪法保护和戏仿权利，以及欺骗风险、水印技术和公民社会应对措施。来源： https://www.youtube.com/watch?v=C0_W7ZGbe3I

**SAP 管理者 René Obermann 探讨欧洲在 AI 领域是否仍有竞争力。**这期 17 分钟的德语 ARD 节目从产业主权角度切入讨论。来源： https://www.youtube.com/watch?v=S25Q4JaA5jc

## 简讯

**亚马逊（Amazon）称，疑似与中国有关联的攻击者在 48 小时的行动中使用智能体发现并利用了 MONAI Label 中的一个零日漏洞。**据亚马逊威胁情报报告称，智能体发现了一处路径遍历漏洞，并利用该漏洞接管了一台高校服务器。来源： https://www.theregister.com/security/2026/11/20/china-attackers-deployed-ai-agents-that-autonomously-found-and-exploited-a-0-day-to-take-over-a-university-server/5311382

**中国在 9月和 10月新增 133 款已完成备案的生成式 AI 服务，累计总数达 1,245 款。**同期还登记了 224 款通过 API 调用已备案模型的新应用或新功能。来源： https://www.cac.gov.cn/2026-11/20/c_1796918603542950.htm

**中国发布了五项人形机器人标准，其中包括 L0 至 L5 级智能化分级体系。**该分级涵盖感知与认知、决策与学习、执行以及协作能力。来源： https://www.ncsti.gov.cn/kjdt/kjrd/202611/t20261118_264191.html
