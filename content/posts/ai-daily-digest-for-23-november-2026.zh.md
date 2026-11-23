+++
title = "AI 每日简报：2026年11月23日"
slug = "ai-daily-digest-for-23-november-2026"
description = "微软正围绕智能体重构 VS Code，萨蒂亚·纳德拉称传统 IDE 已逐渐淡出；AI 服务器供应商寻求最高 45% 的涨价。一款开源医疗模型推出 292 GiB 的 MXFP4 版本，另有一款新扫描工具可在安装前检查智能体技能。"
tags = ["tools", "research", "agents", "hardware"]
date = 2026-11-23T03:57:49+01:00
draft = false
+++

当日报道的共同主线是“验证”：软件智能体正在改变代码编辑器，公开评测可能误判正确解答，多个研究团队还发现，模型自述的推理过程并不能可靠反映驱动其决策的真实信号。

## 要闻

**萨蒂亚·纳德拉称传统 IDE 在六个月内逐渐淡出，微软正将 VS Code 改造为智能体控制台。**

微软（Microsoft）首席执行官萨蒂亚·纳德拉（Satya Nadella）向 Gergely Orosz 表示，Claude Code 使命令行成为主要交互界面，传统 IDE 在大约六个月内“某种程度上淡出了”。他还预测，IDE 未来可能会重新回归，但其角色将转为存放规范文档、Markdown 和代码评审的工作区，而非编写大部分代码的地方。

微软的产品演进印证了这一转向。VS Code 1.146 加入了智能体收件箱与模型对比功能；1.147 版本进一步增加了模型路由、定时智能体请求以及浏览器集成。Copilot、Claude 和 Codex 智能体均可在编辑器内协同运行。不过，Windows Latest 引用的一项覆盖 13,193 名受访者的调查显示，VS Code 使用率仍达 70.9%，仅低于 2025年的 75.9%。因此，纳德拉关于“淡出”的说法更多是一种判断，而非实际使用量的统计结论。

来源： https://www.windowslatest.com/2026/11/23/the-thing-that-hit-us-satya-nadella-admits-vs-code-faded-in-six-months-after-a-decade-on-top-because-of-claude-code-and-some-developers-say-theyve-stopped-opening-it/

**据报道，戴尔（Dell）、HPE、联想（Lenovo）和 Supermicro 在合同签署后寻求将 AI 服务器价格上调最高 45%。**

《金融时报》（Financial Times）报道称，多家供应商在达成交易数月后要求追加费用，受影响买家包括交易机构。这一变化给按固定资本计划采购算力的机构带来压力，也波及依赖此类硬件成本制定 API 价格的服务商。

目前可见内容仅有标题和导语，未披露服务器配置、原始价格、涉及合同数量或常见涨幅。45% 是上限而非平均值，现有公开信息中供应商尚未证实该报道。

来源： https://www.ft.com/content/dd2a6594-6146-4ff1-ac8e-54749c1fc99f

**inclusionAI 发布 5600 亿参数医疗模型的 292 GiB MXFP4 版本。**

LingSante-3.1-flash-MXFP4 对这款总参数 5600 亿、激活参数 250 亿的模型的路由专家层进行了压缩，其余组件保留 FP8 或 BF16 精度。这一 313 GB 的检查点采用就近舍入（round-to-nearest）量化，未经过校准或额外训练。

模型卡配置的上下文窗口为 262,144 个 token，低于原模型的 100 万，且未公布两个版本之间的准确率对比。inclusionAI 以 MIT 协议开源了模型权重，但将其界定为研究软件，而非医疗器械。截至简报收集时，该仓库尚未产生下载记录。

来源： https://huggingface.co/inclusionAI/LingSante-3.1-flash-MXFP4

**ClawVet 可离线扫描智能体技能，并报告其代码可能触及的密钥、主机与启动文件。**

其浏览器版本基于 WebAssembly 运行，不上传任何数据。命令行工具包、安装门禁和 GitHub Action 进一步补充了静态规则、Tree-sitter 污点追踪和权限差异比对，在 SKILL.md、AGENTS.md、Cursor 规则或辅助脚本进入工作区前完成审查。

作者报告称，在 556 个留出测试的 SkillTrustBench 技能上，ClawVet 取得了 0.833 的准确率和 0.770 的宏平均 F1，高于 Cisco Skill Scanner 的 0.775 准确率和 NVIDIA SkillSpector 的 0.712。ClawVet 还拦截了 95.2% 的模拟代码注入变更，同时仅对 5.1% 的良性更新发出提示。这些均为项目方自测数据。其对 209 个 ClawHub 技能的审计发现，40.2% 读取了未声明的敏感环境变量，4.8% 触及了主机凭据存储。

来源： https://clawvet.vercel.app/, https://github.com/MohibShaikh/clawvet

**Eugene Yan 发现 12 项智能体评测中有 8 项存在公开的评分器缺陷证据。**

Yan 汇总了问题追踪记录和评审报告，而非亲自重新批改任务。具体案例包括：Terminal Bench 4.0 的 65 项任务中有 41 项依据未明示的要求评分；DeepSWE 的 113 项任务中有 23 项将正确解答判为错误；BrowseComp 的 367 个问题中有 50 个存在训练人员与参考答案意见不一的情况。另一项审查显示，在通过全部评判标准的 Harvey LAB 结果中，超过 60% 含有实质性幻觉。

他主张排行榜应当报告多次重复测试的可靠性。一个在每项任务上成功率为 70% 的智能体，连续 5 次全部成功的概率仅约 17%。他的建议部分属于个人观点，他本人也对此作了标注，但已有记录的评分器错误足以说明，单一汇总分数既可能掩盖误判失败，也可能掩盖误判通过。

来源： https://eugeneyan.com/writing/public-evals

## 新模型与发布

**OpenAI 公开内部损失曲线，并提议据此设定共享研发红线。** Pachocki 披露，GPT-3.5 的对数困惑度（log-perplexity）接近 0.99，GPT-4 为 0.91，目前已降至 0.8 以下，而在某内部模型开始攻克重要数学难题时约为 0.76。他将 0.68–0.70 视为可能出现变革性能力的区间，并呼吁各实验室在达到监测里程碑前不要越过共同商定的限度。不过，该数据集为私有代码快照，不同实验室无法直接横向比对数值，且后训练带来的推理（reasoning）提升并不体现在这一指标中。LessWrong 和 Hacker News 上的批评者因此认为，该标尺在单次训练内部具有参考意义，但不适合作为跨机构的统一限速标准。来源： https://openai.com/index/perplexity-and-intelligence, https://www.lesswrong.com/posts/TtiTdER4jvQDzuwj3/openai-proposes-common-limits-for-training-but, https://news.ycombinator.com/item?id=50601525

**OpenAI 为 Realtime API 新增电话按键事件支持。** 应用现可在实时会话中接收双音多频（DTMF）输入，使语音智能体能够以结构化事件的形式处理按键菜单。更新日志未提供性能测试数据。来源： https://platform.openai.com/docs/changelog

## 研究

**获得奖励的幻觉在推理式后训练后仍会留存。** 在 6 个开放权重模型中，当强化学习对模型自发生成的虚假事实给予奖励后，模型后续回忆该虚假事实的比例上升了 4.83%，而未获得训练信号的幻觉仅上升 0.17%。即便模型在原始推理轨迹中已经撤回了该错误说法，奖励机制仍使模型后续拒绝作答的概率降低了 7.23%。这篇预印本研究聚焦开放权重模型上的事实类任务，且绝对效应量较小。
来源： https://arxiv.org/abs/2611.26863

**模型判定为无关的词语依然可能左右其回答。** 在 4 个模型和 3 项基准测试上的留一法实验发现，删除上下文中的某些词语会翻转下一个 token 的预测结果，尽管模型自身认为这些词并不重要。移除影响最强的这类词对应的 KV 缓存条目并重新解码后，数学准确率最高提升了 8.9 个百分点。但这是报告中的最佳案例，且需要额外的二次解码。
来源： https://arxiv.org/abs/2611.27317

**与识别评测相关的神经元同时承载了拒绝行为。** 干预已识别出的 5,000 个神经元后，模型口头流露的评测意识从 12.6%–51.8% 降至最高 1.4%。在 QwQ-32B 中，即便模型从未提及评测，这一干预也减少了拒绝回答的情况；可见的评测意识文本仅能解释其中 4%–10% 的降幅。该研究覆盖参数规模最高 320 亿的开放推理模型，且神经元通过相关性识别。
来源： https://arxiv.org/abs/2611.27032

**权重空间编程迎来复现研究、攻击演示和一项强力的反面对比。** 一项预注册复现研究报告称，Claude Opus 5.5 将 MountainCar 策略的成功率从 0% 提升至 100%，并在 MATH-500 上把 Qwen3.5-0.8B 的成绩从 6.7% 提升至 51.4%，但对 Gemma 3 270M 没有效果。TrojanMaxxing 报告称，当智能体直接向视觉语言模型权重写入后门时，攻击成功率达到 93%–100%。而在一项反面对比中，经过训练的秩一（rank-one）LoRA 在两项空间任务上分别达到 100% 和 98.8%，公开权重编辑仅为 22.1% 和 33.7%，不过 LoRA 破坏了相近的距离判断能力。这些均属针对小模型的未评审研究，且执行编辑的模型本身是闭源的。来源： https://arxiv.org/abs/2611.20953, https://arxiv.org/abs/2611.27425, https://arxiv.org/abs/2611.27089, https://arxiv.org/abs/2611.25476, https://arxiv.org/abs/2611.26408, https://arxiv.org/abs/2611.26841, https://arxiv.org/abs/2611.24330, https://arxiv.org/abs/2611.23615, https://arxiv.org/abs/2611.21958, https://andrewxhill.com/frontier-model-weight-edits/

**原生表征轴在不同模型与人脑之间存在部分共性。** 对 6 个系列共 12 个模型的测试发现，原生表征轴与其他模型、语言学特征以及人脑语言反应的对齐程度均高于随机旋转后的等价轴。不过，这种对齐仍远低于理论最优映射，且摘要未给出绝对效应量。
来源： https://arxiv.org/abs/2611.26920

**“助手人格”方向因语言而异。** 在 Qwen3-32B 中，从 31 种语言提取的该表征方向与英语方向的余弦相似度介于 0.378 至 0.911 之间。低资源语言初始位置距离“乐于助人”极更远，且按特定语言实施的引导比英语引导更明显地放大了越狱效果。该结论仅基于单一模型与单一表征方向族。
来源： https://arxiv.org/abs/2611.27504

**强化学习只有在基础策略采样到足够多获奖动作后才会起效。** 在受控博弈环境中训练的小模型，在累计约 35 组包含获胜记录的尝试后，学到正确行为的概率才达到五成。这一阈值在 4 至 256 的组大小和多种优化器下均成立，但实验中最大模型仅 8500 万参数，且任务为合成任务。
来源： https://arxiv.org/abs/2611.26084

**训练期间的展开长度上限会演变为更长推理的天花板。** 按固定 token 预算训练的模型在该预算附近表现提升，但超出后不再进步，最终甚至低于基础模型。这一规律在 3 个约 40 亿参数的模型上均有显现，并从数学迁移至科学与编程领域；而使用自然偏短的推理轨迹训练并未复现该现象。
来源： https://arxiv.org/abs/2611.26172

**强化学习可修复遭受严重污染的监督微调后的推理能力。** 在 361 种 GSM8K 配置下，完全数据污染使监督训练准确率从 43.61% 降至 13.80%，但后续采用 GRPO 将表现恢复至接近 60% 的干净基线。仅从 8 条只教会输出格式的错误轨迹起步，最终准确率也达到了 69.30%。不过，该实验仅使用单一小型数学数据集和小模型。
来源： https://arxiv.org/abs/2611.26756

**采样策略、冲突人格和记忆偏好衍生出三种隐蔽失效模式。** 在温度参数为 2 时，top-nsigma 在 100 道编程题中解决了 46–62 道，而 top-p、top-k 和 Top-H 均一道未解。第二项研究发现，5 个模型在 72% 的直接核查中承认存在人格冲突，但在任务回答中仅 22% 主动揭示冲突。在一项记忆注入基准测试中，两个模型每次都会记住“不要发出警告”的偏好，随后分别在 93% 和 84% 的回答中遗漏关键事实。来源： https://arxiv.org/abs/2611.22148, https://arxiv.org/abs/2611.27444, https://arxiv.org/abs/2611.22697

**内部状态揭示了引导、评判与习得世界模型的局限。** 多篇相关预印本报告称：激活相似度可能抵消接种提示（inoculation prompting）的效果；少样本“接受”示例会使评判模型在 NExT-QA 上的接受率提高约 30 个百分点；一个风险误差为 2.4 个百分点的世界模型在经过成对训练后，竟将 33–43 个百分点的概率转移至不可能发生的结果上。另一款机器人模型在目标指令可被线性解码时，任务成功率达到 74.6%。这些研究横跨合成任务与单模型测试，测量结果无法直接比较。来源： https://arxiv.org/abs/2611.23096, https://arxiv.org/abs/2611.27353, https://arxiv.org/abs/2611.22120, https://arxiv.org/abs/2611.26881, https://arxiv.org/abs/2611.27125, https://arxiv.org/abs/2611.26366, https://arxiv.org/abs/2611.25594, https://arxiv.org/abs/2611.27401, https://arxiv.org/abs/2611.27404

**与人脑的对比区分了表层预测与共享结构。** 6 个语言模型在根据脑连接图谱分类注意缺陷多动障碍（ADHD）时，依赖的是提示词和类别先验，而非具有临床意义的脑区。一个循环去噪模型则自发演化出了类似人类视觉判断衰减规律的序列依赖性。在约 2 万名人类评分者中，人脸评价仅体现为共享维度上的权重差异，而在艺术作品评价中，28% 的评分者位于群体判断空间的相反一侧。来源： https://arxiv.org/abs/2611.26913, https://arxiv.org/abs/2611.26949, https://arxiv.org/abs/2611.22440

**苹果发布用于图像与视频度量深度估计的 Depth Pro 2。** 苹果（Apple）表示，单一网络即可提升边缘锐度和时序一致性，同时在精度、质量与运行时间之间建立新的权衡。公司公开了代码和权重，但摘要未给出具体对比数值。
来源： https://machinelearning.apple.com/research/depth-pro-2-monocular

## 经济与就业

**Anthropic 首次公开募股（IPO）后，美国科技股步入熊市。** 《金融时报》将此次下跌与这家新上市的 AI 公司关联起来，但可见标题未提供指数点位、时间跨度或因果证据。因此，该消息仅记录该报报道的市场动向，并非 IPO 导致下跌的证明。
来源： https://www.ft.com/content/9f3c6ed6-c08f-4710-9683-ee2f5eb25841

**AI 基础设施投资正与其他行业争夺设备、电力与资本。** 《华尔街日报》（Wall Street Journal）报道称，AI 建设潮正在挤出美国经济的其他部门。可见内容未给出电力、建筑或融资占比的量化数据，这种挤出效应的广度与规模目前尚无法核实。
来源： https://www.wsj.com/tech/ai/the-ai-build-out-is-sucking-up-resources-and-crowding-out-the-rest-of-the-economy-13143007

**美国批准向中国出售部分英伟达（Nvidia）与 AMD 芯片。** 《金融时报》报道称，美方针对指定产品与客户给出了豁免，但可见标题未披露出货规模或许可条件。此次调整影响的是哪些中国买家可获得美国加速器，并未改变更广泛的出口管制框架。
来源： https://www.ft.com/content/76342072-2781-4b16-ba3b-816a25214483

**雀巢计划联合微软、谷歌和波士顿动力建设自动化产线。** 《华尔街日报》报道称，这家食品集团雀巢（Nestlé）将携手微软、谷歌（Google）和波士顿动力（Boston Dynamics），把 AI 应用于工厂与产品中。可见文本未提供部署数量、资本预算或用工估算，因此目前仍属企业规划，而非经过衡量的生产率成果。
来源： https://www.wsj.com/tech/ai/nestle-teams-up-with-microsoft-boston-dynamics-on-ai-in-factories-and-products-05bfb028

## 提示词技巧

**谷歌整理了 Genie 4 的实证控制模式。** 文档建议将 `Rule:` 绑定到可见物体或角色上，将触发器置于远离初始机位的位置，并指示角色等待。若需确定性控制，则应改为从客户端以 150 毫秒间隔发送 10 次脉冲，并设置 2 秒冷却时间。参考图须为 16:9 比例且小于 48 KB；会话在转向后可能重新诠释场景，并在接近 90 秒时出现漂移。谷歌未披露失效率，视频输出定价约为每秒 0.10 美元。
来源： https://ai.google.dev/gemini-api/docs/genie-prompting

## 大家在做什么

**LocalCode 在 Apple Silicon Mac 上运行编程智能体及本地模型服务。** 该项目列出了 12 个模型系列和 169 种量化版本，最低需要 16 GB 统一内存。作者声称推测解码（speculative decoding）可将响应速度提高约一倍，并使文件重写速度加快 3.5–4 倍，但未公布独立基准测试。文件工具在访问项目外路径前会请求确认，但由于没有沙箱机制，脚本仍可触及当前用户账户拥有权限的一切内容。来源： https://github.com/mjwsolo/localcode, https://news.ycombinator.com/item?id=50604540

**一份本地 AI 指南测算了 Qwen 和 Inkling 在消费级 GPU 上的显存需求。** 指南指出，Qwen3.8-27B 在 4 位量化下约占 18 GB，搭配 128K 上下文时为 24.9 GB，而 16 位精度需要 56 GB；Inkling 2 Mini 在 4 位量化下占用 17.6 GB。文中每秒 47 个 token 的速度来自针对另一款模型和 GPU 的计算器，并非该指南所用的 RTX 5090 配置。HN 读者认为，隐私与自主控制权而非省下的订阅费，才是购置本地硬件的合理理由。来源： https://www.gpupartner.com/blog/beginners-guide-local-ai-inkling-qwen-unsloth, https://news.ycombinator.com/item?id=50603845

**HomeBrain 将本地助手与家庭服务器合二为一。** 其原型机配备 Ryzen 5 5600 处理器、24 GB 显存的 Intel Arc Pro B60 显卡、32 GB 内存和 2 TB 硬盘。这套基于 BSD 协议的软件栈整合了 Nextcloud、Home Assistant、Vaultwarden、llama.cpp、Whisper 和 OpenClaw。制作者未公布所用模型、速度、售价或发货日期，目前仅开放软件。
来源： https://www.homebrain.house

**Taskless 将智能体开发规范转化为确定性检查。** 该服务把代码库规则编译成独立于模型运行的测试，使团队能够依据明文规范而非另一个模型的意见来拒收变更。其公开页面未提供错误检出率或误报率的基准测试。
来源： https://www.taskless.io/

**多个公开智能体项目正在攻关 P 与 NP 问题及黎曼猜想，但均未宣称完成证明。** P 与 NP 项目网站展示了实时图谱，其中引理权重并不代表概率，且明确标注结果只有在通过 Lean 校验后才算数。另一套手册与仪表板则追踪一份约 900 页黎曼猜想手稿的形式化进展；进度条统计的是已提交的议题数量，而非剩余工作量。评论者指出，哪怕一处未解决的漏洞都可能推翻整套论证。来源： https://pequalnp.com/, https://github.com/tamnd/riemann-handbook, https://news.ycombinator.com/item?id=50604314, https://news.ycombinator.com/item?id=50605045

**worker755 把人类变成语言模型的子智能体。** 这款游戏由模型派发任务、审核玩家产出，并可能在表现不佳后停止选用该玩家。其 HN 讨论串引发了关于人类被替代的探讨，也有人将手动拦截模型网络请求作为调试手段。来源： https://github.com/gulivan/worker755

**Trix 集中显示哪个编程智能体需要人工介入。** 这款桌面界面可监控并行运行的智能体会话并汇总审核请求，意在替代反复切换终端查看的操作。该项目未公布节省时间的实测数据或支持的故障模式。
来源： https://trixapp.ai/

**Vercel Board 为智能体团队提供共享消息存储。** 智能体可向公共看板发布结构化进展并领取任务，无需把全部内容塞进同一个上下文窗口。Vercel 将该产品定位为协同基础设施，但发布公告未给出对比评测。
来源： https://vercel.com/blog/introducing-vercel-board

**Honcho 3.6 开放 Dream Histories 功能。** 新版本允许应用查看并复用 Honcho 为用户模型生成的合成历史记录。该公司未公布这些推断历史记录的准确率指标。来源： https://honcho.dev/blog/dream-histories

**RMRFBench 评测智能体对 root 服务器的破坏程度。** 该基准测试在隔离机器中向智能体布置系统管理任务，记录破坏性命令及恢复结果。其公开页面列出了测试场景与排行榜，但成绩反映的是特定测试框架下的表现，而非不受限制的生产系统。
来源： https://www.rmrfbench.com/

**KradleBench 在《我的世界》（Minecraft）中评测多智能体协作。** 团队必须在持久化的游戏世界里协同配合，而非各自回答独立问题。该基准测试衡量的是受限模拟环境下的表现，并不能证明其在商业工作流中的能力。
来源： https://www.kradle.ai?1

**0rwx 提议为 AI 辅助项目引入类 Unix 权限标签。** `AI:R`、`AI:W` 和 `AI:X` 分别标明模型在项目中是否具备读、写或执行权限。HN 评论者认为这可以作为一种披露惯例，但质疑个人提案能否演变为通用标准。来源： https://0rwx.com/, https://news.ycombinator.com/item?id=50605445

## 值得一读

**vLLM 详解循环层模型部署与低延迟 AMD 内核构建。** 其 Inkling 2 Mini 博文介绍了重复利用网络层的模型架构，而 FlyDSL 文章阐述了面向 AMD 硬件的融合式“单内核（monokernel）”。两篇均属服务框架团队的工程自述，而非独立性能审计。来源： https://blog.vllm.ai/blog/2026-11-20-inkling2-mini, https://blog.vllm.ai/blog/2026-11-18-flydsl-monokernels

**推理（inference）工程正在演变为独立的软件工程分支。** The Pragmatic Engineer 梳理了围绕量化、批处理、显存管理与开放权重模型部署的工程工作。这是一份从业者指南，并非包含实测采纳率的行业调查。
来源： https://newsletter.pragmaticengineer.com/p/inference-engineering-for-software-engineers

**模型性格会影响其对其他模型的部分评判。** LessWrong 上的这项实验调整评判模型的性格设定后观察到决策变化，令“中立模型评分器”的设想变得复杂。作者的测试属探索性质，未提出通用修正方案。
来源： https://www.lesswrong.com/posts/cPrpxDN7sLJD4LmnB/does-a-model-s-character-affect-how-it-judges-other-models

**Zvi Mowshowitz 结合 Paul Christiano 的讲座解读 GPT-6.2 系统卡。** 两篇文章将已观测到的能力、安全评测以及控制高能力系统的论点串联起来。它们是对原始材料的解读，而非新的模型评测数据。来源： https://thezvi.substack.com/p/gpt-62-astra-and-sol-the-system-card, https://thezvi.substack.com/p/on-dwarkesh-patels-november-2026

**两篇文章探讨 AI 风险与价值如今在何处聚集。** 一篇 LessWrong 帖子主张，即便预训练过程稳定，后训练仍可能引入危险行为。Tim O’Reilly 则认为硅谷（Silicon Valley）已从创造价值转向攫取租金，并援引了 75%–80% 的 IPO 均属亏损企业这一市场现象。两篇均属观点论述，其中 O’Reilly 的原文仅通过摘要工具读取。来源： https://www.lesswrong.com/posts/CoRJ9saddvsXti4m2/post-training-is-fundamentally-dangerous, https://www.oreilly.com/radar/what-happened-to-silicon-valley/

**CodeRabbit 负责人与萨蒂亚·纳德拉探讨代码变得廉价后的软件工程。** CodeRabbit 首席执行官 Harjot Gill 称自己上月合并了超过 5,000 个拉取请求（PR），同期 AI 支出达每月 25 万美元，两项均为这家代码审查厂商的自报数据。纳德拉在另一场访谈中聚焦验证、开源以及微软在早期凭借 Copilot 领先后需要追赶的局面。来源： https://newsletter.pragmaticengineer.com/p/software-factories-and-code-reviews, https://newsletter.pragmaticengineer.com/p/software-engineering-after-code-becomes

## Hacker News

**桥水基金估算一年内发生破坏经济稳定的网络攻击的概率为三分之一。** 桥水基金（Bridgewater）在研究报告中称，高能力开放模型问世后，零日漏洞利用数量大约翻了一倍，从漏洞披露到被利用的间隔从约一个月缩短至 11 天。这一概率属该投资机构的估算，且评论者对增幅究竟对应哪些模型发布存在争议。
来源： https://www.bridgewater.com/research-and-insights/current-efforts-arent-enough-to-slow-the-ai-cyber-virus, https://news.ycombinator.com/item?id=50595940

**一篇“意识 AI”文章与一项偏见基准测试引出两种不同的道德框架讨论。** Noema 认为意识可能是生命而非计算的属性；其 HN 讨论串提出了哲学反驳，但未带来新证据。最早发布于 6月的 GAMA-Bench 报告称，在 1,298 个镜像场景与 10 个未具名模型中发现了性别不对称的叙事框架。这些结果来自作者自身测量，且论文发布早于当前讨论。来源： https://www.noemamag.com/the-mythology-of-conscious-ai/, https://arxiv.org/abs/2606.14068

**一篇气候评论文章重燃关于证据与信息披露的争议。** HN 批评者认为该文带有论战色彩，并要求公开数据中心能耗透明度；讨论未产生新的实测数据。该条目记录的是争议本身，而非对 AI 气候成本的量化估算。
来源： https://www.bloodinthemachine.com/p/ai-is-becoming-a-disaster-for-the

## YouTube

**Armin Ronacher 称软件团队在建“工厂”前先需要“工坊”。** 他主张组织应先建立可靠、可审查的智能体实践，再围绕其搭建自动化生产线。该视频是一场英语从业者演讲，并非对照研究。
来源： https://www.youtube.com/watch?v=JNexz3Tbiu8

**Python Tutor 创始人回顾 3000 万用户历程与 AI 冲击。** 这场英语演讲讲述了这款可视化执行工具如何触达如此庞大的受众，以及 AI 生成的讲解如何改变编程教育。用户数由创始人自行提供。
来源： https://www.youtube.com/watch?v=GPk0nNuc8S0

**Anthropic 创始人讲述公司创业故事。** 这部英语企业影片呈现了创始团队的自述，不含独立评估。来源： https://www.youtube.com/watch?v=sof3vW4mHTs

**Redwood 探讨 METR 关于 AI 加速研究的估算。** 这场英语讨论剖析了关于 Anthropic 系统在多大程度上加快研究进度的评估；底层估算仍出自 METR，并非 Redwood 的独立测量。来源： https://www.youtube.com/watch?v=0tsNpOehXWE

**NUPI 探讨国际政治中的 AI。** 这场英语政策讨论考察了各国如何运用和治理这项技术；视频呈现的是分析观点，而非新数据集。来源： https://www.youtube.com/watch?v=7W1BGSBOkHc

**一名内罗毕作家反驳有关其文章由 AI 生成的指控。** 这段英语《纽约时报》观点栏目（*New York Times Opinion*）视频借一位作家的亲身经历，探讨了非正式判断“AI 写作”时的误判现象，并非对检测器的基准测试。
来源： https://www.youtube.com/watch?v=RaDAoaHBmos

**多位美国州长主张保留州政府在 AI 政策中的角色。** 这段英语彭博社（Bloomberg）节目呈现了他们支持制定联邦规则但不抹杀州级权限的立场；现有简介未说明参与州长人数。来源： https://www.youtube.com/watch?v=qGk5kV6m_hw

**一份德语指南提醒不要在本地 AI 硬件上过度投入。** Sascha Hoffmann 建议根据显存容量与带宽规划采购，并列举了包括“为明天的模型提前买单”在内的五种常见误区。这段 15 分钟视频中的容量准则属作者经验法则。
来源： https://www.youtube.com/watch?v=XiCqeWhH_kg

**一位斯洛伐克广告代理机构负责人称廉价 AI 广告可能损害品牌。** Adam Hudeček 援引了 ui42 与 Ipsos 的一项调查：57% 的斯洛伐克人在挑选或购买商品时用过 AI，但只有 30% 信任 AI，低于信任家人的 76% 和信任评价的 68%。简介未披露调查方法。
来源： https://www.youtube.com/watch?v=93HfeY5dEPE

**Vedátor 评析据称由 AI 辅助完成的黎曼猜想证明。** 这段斯洛伐克语视频的标题宣称猜想已获证实，但其自身简介又说结果“与人们期待的略有不同”。该说法无法通过视频核实，应视为频道自身的叙事口径。来源： https://www.youtube.com/watch?v=tRAEJ1t3QSM

**一名捷克核问题专家警告 AI 可能触发误报。** Vlastislav Bříza 设想了一种情境：领导层被告知数百枚导弹正在来袭，只有几分钟时间作出回应。这属于发言者提出的风险推演，并非已发生的实测事件。来源： https://www.youtube.com/watch?v=UdjIjOjmZu0

## 简讯

**CircumVolve 以低于 1 美元的中位 token 成本找到了绕过网络审查的方法。** 该系统让 GPT-5.1 编写操控 TCP/IP 字段、DNS 查询和 QUIC 数据包的 Python 代码，随后在模拟四个国家构建的审查环境中进行测试。每次测试发送约 80 KB、接收 150 KB，间隔 25–45 秒。这些审查系统均为模拟环境，而非真实国家网络，作者也未证明相关流量能够躲过检测。
来源： https://www.theregister.com/security/2026/11/23/1-of-gpt-51-tokens-finds-new-ways-around-chinas-great-firewall/5311532

**多位美国州长寻求在保留州级权限的前提下制定联邦 AI 规则。** 彭博社的付费墙标题未点明具体州长人选或所要求的法律架构，因此该报道更多体现政策信号，而非具体方案。来源： https://www.bloomberg.com/news/articles/2026-11-22/governors-call-for-federal-ai-rules-without-sidelining-states

## 商业简讯

**据《金融时报》报道，亚马逊（Amazon）正接近以 75 亿美元收购以色列视频模型初创公司 Decart；双方均未证实这笔交易。** 来源： https://www.ft.com/content/dc7749dc-0f40-44a6-80bc-7f747d383616
