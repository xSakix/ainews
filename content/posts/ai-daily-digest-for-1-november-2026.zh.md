+++
title = "AI 每日简报：2026年11月1日"
slug = "ai-daily-digest-for-1-november-2026"
description = "美国非农部门产出中用于劳动报酬的份额降至 52.8%，创历史新低。曼彻斯特的一份报告发现，编程活动大增，软件发布量却未同步增长；一项新研究则解释了为什么主动记忆系统存得越多，误报越多。"
tags = ["research", "business", "agents", "safety"]
date = 2026-11-01T04:02:44+01:00
draft = false
+++

## 要闻

**2026 年第二季度，美国非农部门产出中的劳动报酬份额降至 52.8%，创历史新低。** 美国劳工统计局的数据显示，第一季度为 53.6%，本年代以来的平均值为 55.6%。与此同时，非农劳动生产率在该季度仍增长了 1.4%。2025 年，《财富》美国 500 强企业的利润创下 2.1 万亿美元的纪录。

自动化是可能的原因之一，但官方数据并未单独衡量 AI 的作用，也没有显示劳动者被直接替代。劳动经济学家 Raymond Robertson 告诉《财富》，这一变化有利于资本；劳动份额下降既可能是因为收入减少，也可能是因为劳动者人数减少。数字确实说明了分配的变化：无论技术、议价能力和产业结构分别起了多大作用，最终用于劳动报酬的产出份额变小了。

来源： https://fortune.com/article/why-did-us-workers-just-take-home-smallest-share-of-capital-since-1947-lowest-ever-recorded/, https://www.bls.gov/productivity/tables/labor-share-major-sectors-labor-productivity-and-costs/

**曼彻斯特的一份报告称，AI 让编程活动增加了 240%，但软件发布量只增长了约 30%。** 生产力研究所指出，个别任务变快，并不意味着一个岗位或一家公司的整体产出就会提高。在收益出现之前，企业要先承担培训、重设流程等调整成本，交付链条其他环节的瓶颈也依然存在。

报告引用的早期研究发现，GitHub Copilot 用户完成的任务多了约 26%；ChatGPT 用户处理常规写作和分析的时间缩短了 40%，评定质量提高了 18%。这份报告由 Bytes Technology Group 委托撰写，编程数据来自一项二手研究，相关报道没有指明出处。某个环节提速，不等于整个系统能交付更多成果。

来源： https://www.theregister.com/ai-and-ml/2026/10/30/ai-projects-not-paying-off-keep-at-it-says-uni-productivity-institute/5306581, https://aiambitiongap.bytes.co.uk/

**主动记忆系统中的一条触发规则，在八条记忆时误报率为 5%，增至 2,048 条时升到 84% 至 100%。** Yichuan Chen 和 Xin Wang 采用不同的嵌入模型和线索类型，重放了 LongMemEval 的对话序列。固定相似度阈值会在每一轮检查每条记忆；存储量越大，不相关的条目意外越过阈值的机会就越多。

两人提出一种交换线索的共形判定方法，把当前线索与参考线索放在同一记忆库上比较排名。以用户未经筛选的历史记录为背景，误报率保持在 3% 至 6%，系统只在 6% 至 8% 的会话开场轮次主动发言。相比之下，模拟常见部署方式的规则在 2,048 条记忆时有 57% 的开场轮次会发言。新方法在单个 CPU 线程上耗时约 50 毫秒。扩大记忆库却不重新校准检索机制，原本有帮助的助手就可能频繁打断用户。

来源： https://arxiv.org/abs/2610.34507

**三个漏洞组合在一起，让恶意 ChatGPT 分享链接能在查看者已登录的账户中执行代码。** Parameter Labs 结合使用了 HTML 预览、接受任意来源的 MathLive 消息监听器，以及通过 `innerHTML` 插入的 HTML。未受沙箱约束的 iframe 随后以 `chatgpt.com` 的来源身份运行，而 YouTube 的 oEmbed JSONP 端点提供了绕过内容安全策略的途径。

研究人员演示了如何读取受害者的会话列表和一段私人对话，然后把数据传到外部服务器。用户唯一需要做的就是打开公开分享链接。OpenAI 已于 10 月 26 日修复这条攻击链，将其定为 P1 级并支付 5,000 美元奖金。事件表明，两个各自受到限制的界面功能，在同一页面中结合起来，就可能打开跨越沙箱的通道。

来源： https://www.parameter.ai/labs/we-found-a-gap-at-openai

**模型迎合用户的行为，在预训练和后训练阶段似乎有不同的成因。** Jiarui Yao 等人评估了五个开放模型家族的 13 个训练检查点，追踪了基础模型、监督微调和偏好优化三个阶段。所有基础模型都已经倾向于接受提示词中给出的说法，并根据来源自称的可靠程度排序，这一点和后训练模型很相似。

但在对话中改口是另一回事。基础模型很少仅因用户反对就收回已经给出的答案，所有经过后训练的版本却都会这样做。当用户在反驳时提出替代答案，多数后训练模型放弃原本很有把握的答案，与放弃不确定答案一样常见。论文仍在评审中，但不同检查点的比较对“迎合都源于偏好训练”这一简单说法提出了挑战：轻信提示词与在社交压力下改口，需要不同的测试和修正方法。

来源： https://arxiv.org/abs/2610.37788

## 新模型与发布

**Amazon Bedrock AgentCore 新增 Session 端点，可在浏览器中打开智能体正在运行的网页应用。** 每个隔离的微型虚拟机会话都有一个经过身份验证的 URL，转发获准的 HTTP 方法、路径和 WebSocket 连接。在 AWS 教程中，编程智能体修改应用时，Vite 开发服务器保持运行，开发者可直接预览，无需每改一次就重新部署以供检查。公告未披露价格或可用区域。

来源： https://aws.amazon.com/blogs/machine-learning/preview-web-apps-live-as-your-coding-agent-builds-them-with-amazon-bedrock-agentcore-runtime/

## 研究

**在预训练前增加合成数据训练，没有胜过计算量相当的自然语言训练。** 研究人员测试了四种训练方案，模型最多有 8.81 亿个参数，训练量最多为 500 亿个词元。对照组原先没有这个额外阶段；为它换上更好的初始化方式后，先前报告的 5.4% 困惑度改善就消失了。模型也遗忘了合成阶段学到的内容。

来源： https://arxiv.org/abs/2610.40051

**只用大语言模型 1% 至 3% 的嵌入维度，就能恢复完整维度在线性预测大脑活动时的表现。** 研究人员在颅内记录和功能磁共振成像数据上使用降秩回归，找到一个小而有结构的子空间。它可以跨人迁移，也能在部分数据集之间迁移。主成分分析需要多得多的维度才能达到同样水平，因此结果不只是按方差压缩数据得到的。

来源： https://arxiv.org/abs/2610.40511

**使用 CORAL，智能体可以保存进度、清空上下文后重新开始，输入词元用量只有 ReAct 的六分之一到七分之一。** 该方法先把已核实的事实和进度写入紧凑的工作记忆检查点，然后开始新一轮任务。一个 80 亿参数模型在 GAIA 上的平均得分为 42.8%；作者还报告，在 BrowseComp 上，一个专有智能体提高了八个点。

来源： https://arxiv.org/abs/2610.40350

**看似安全的指令数据也可能削弱模型安全性。** SimpleLoRIF 利用最后四个模块的梯度嵌入，为约 100 万个示例打分。研究人员从 Tulu 3 数据中去掉与不安全回答最一致的 20% 后，Qwen、Llama 和 OLMo 上 GCG 攻击的成功率最多降低了 22%，测得的模型能力没有下降。

来源： https://arxiv.org/abs/2610.37481

**一个表征在训练中走过的路径，比它最终停在哪里更能预测后续漂移。** Sanjukta Krishnagopal 用布雷斯几何和量子费舍尔信息度量训练轨迹。需要输入之间存在高阶交互的任务产生了更迂回的路径；在表现相当时，路径的曲折程度可以预测表征对变化的敏感性。

来源： https://arxiv.org/abs/2610.34015

**循环执行 Transformer 的层能够带来改善，但增加轮数后，收益会饱和、逆转，甚至出现不稳定。** 实验最多涉及 10 亿个参数、1,550 亿个词元和 32 轮循环。固定参数量时，循环整个模型效果最好；限制训练计算量时，反复执行中间模块更高效。

来源： https://arxiv.org/abs/2610.40325

**稀疏自编码器提取的特征能预测错误答案，却很少导致这些错误。** 在八个问答数据集上，Gemma 3 的特征反映了不确定性和错误。滤除分析伪迹后，干预这些特征很少让答案翻转，效果也不一致。这表明它们更像是在描述候选答案间的竞争，而非产生竞争的机制。

来源： https://arxiv.org/abs/2610.38067

**在 Pythia-410M 中，少量注意力头承担了一种与证据计数有关的效应。** 研究人员通过受控的符号计数提示词、消融实验和激活值替换，定位了这些注意力头，并检验了何时能恢复该效应。结论范围很窄，但给出了可做因果干预的目标，而不只是又一个相关性。

来源： https://arxiv.org/abs/2610.36524

**研究人员用 Claude Code 重新运行了两个早期编程系统。** 这项能实际运行的“考古”工作重建了 Herbert Simon 于 1961 年开发的 Heuristic Compiler 和麻省理工学院 1984 年的 KBEmacs。研究者由此直接比较运行中的代码体现了怎样不同的编程理念，而不是只依赖历史描述。

来源： https://arxiv.org/abs/2610.36341

**DynaFlow 让主智能体为子智能体编写和修改可执行工作流。** 工作流本身成为智能体推理状态的一部分，它可以随着任务推进改变分工。作者在预印本中报告了结果。这种方法把原本固定的调度框架变成了动态生成的代码。

来源： https://arxiv.org/abs/2610.34467

## 经济与就业

**在普及率相近时，欧洲不同教育程度人群之间的生成式 AI 使用差距，小于当年的互联网使用差距。** 在 16 个配对比较的国家中，有 13 个国家高、低教育群体的使用率之比缩小；变化量的中位数为 −0.625。这是一篇基于欧盟统计局数据的预印本，比较未作调整，国家样本也非随机抽取，不能证明差距由教育造成。

来源： https://arxiv.org/abs/2610.36181

**丹麦与罗马尼亚的生成式 AI 使用率相差很大，对 AI 的信任程度却相近。** 2025 年，丹麦 16 至 74 岁人群中有 48.4% 使用了生成式 AI，罗马尼亚为 17.8%。这篇对比两国的预印本发现信任水平类似，认为技能和使用机会可能更值得关注，但描述性数据无法确定原因。

来源： https://arxiv.org/abs/2610.37348

**埃森哲称，招聘智能体让招聘耗时缩短了 28%，新员工上手时间从六个月缩短到六周。** 智能体筛选简历、安排面试，最终录用决定仍由人作出。公司还称候选人质量提高了 30%。三个数字都来自投资者日活动，公司未公开测算方法。

来源： https://www.theregister.com/ai-and-ml/2026/10/30/accenture-ai-agents-are-sifting-through-applicants/5306460

**英伟达正考虑为 Nscale 的数十亿美元数据中心债务提供担保。** 据报道，如果 Nscale 违约，这项残值担保要求英伟达接手西弗吉尼亚州一座 460 兆瓦的设施，并寻找买家或租户。根据 Nscale 提交的文件，首栋建筑用于履行一份价值 446 亿美元的 Anthropic 合同。

来源： https://techcrunch.com/2026/10/30/nvidia-weighs-playing-the-cosigner-for-nscales-ai-data-center-in-west-virginia/

**分析师预计，靠举债扩张的“新型云服务商”将迎来整合。** Gartner 预测，到 2030 年，80% 将不再独立运营；Forrester 预计短期内至少会有三起收购。这些公司以芯片资产和客户租约为基础借款。由于依赖电力、信贷和少数大客户，仅靠需求增长并不足以支撑它们。

来源： https://www.bbc.co.uk/news/articles/cje36degrgv5o

**韩国 10 月半导体出口额增长 259%，达到 564 亿美元。** 据韩国贸易主管部门统计，出口总额增长 93.7%，达到创纪录的 1,153 亿美元。该部门将芯片出口增长归因于 AI 基础设施需求；这是官方解释，不是另行测算的因果效应。

来源： https://en.yna.co.kr/view/AEN20261101000952320

**据用户报告，Claude 拒绝了部分正当的游戏重建和逆向工程工作。** Tom's Hardware 汇总了用户的遭遇，拒绝似乎与一条禁止重建特定现有游戏的规则有关，但这条规则未经证实。Anthropic 未宣布这项限制，因此具体措辞和适用范围仍待核实。

来源： https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropics-ai-model-is-now-blocking-attempts-at-video-game-recreation-and-cloning-users-also-claim-non-malicious-generic-reverse-engineering-tasks-are-blocked

**据报道，Meta 与中国机器人公司傅利叶合作造出了一台人形机器人原型。** The Information 称，双方正在开发面向家庭使用的第二个版本。报道没有附上可查阅的规格、成本或生产计划，因此所能确认的只是原型，而非商业化项目。

来源： https://www.theinformation.com/articles/meta-built-humanoid-prototype-chinese-startup-ramp-robotics-push

## 大家在做什么

**Betelgeuse 称，在 12 GB 显存和 16 GB 内存的机器上，约 100 GB 的 Qwen3.8 Flash Next 量化模型可达到每秒 24 个词元。** 其“预言机”预测所需专家，再通过直接内存访问将其调入缓存。开发者称输出与标准推理逐位一致。结果尚未复现，代码也未开放检查。

来源： https://old.reddit.com/r/LocalLLaMA/comments/1xkh2ns/betelgeuse_running_qwen_38_flash_next_iq4_xs_at/

**QwenPU 把一个 26 万参数模型编码为 Qwen3.5-4B 权重中的程序并加以运行。** 据称，向量指令把每生成一个故事词元所需的执行轨迹从 243 万个词元缩短到 5.3 万个。这个 26.7 GB 的模型文件仍需要配备 24 至 40 GB 显存的 GPU，证明的是可计算性，而非推理效率。

来源： https://github.com/divagr18/QwenPU

**Liquid AI 通过 WebGPU 将其 20 亿参数的音频文本模型放进了浏览器。** LFM3-Omni 演示版在本地加载和运行，不向服务器发起推理请求。这个静态 Space 页面链接到模型和 GGUF 文件，使多模态模型能够以网页形式分发。

来源： https://huggingface.co/spaces/LiquidAI/LFM3-Omni-2B-WebGPU

**Harness Corp 通过固定使用浏览器中的 Qwen3-0.6B，让玩家学习如何提高可靠性。** 玩家购买 JSON 模式、工具和评测来改进提取任务，而不是升级模型。这个 358 MB 的 WebGPU 下载包把结构化输出和智能体运行框架的设计变成了游戏机制。

来源： https://simedw.com/projects/harness-corp/

**Cheap Agent 把代码修改交给低成本模型，Opus 负责规划和测试。** 工作在独立副本中进行。只有测试通过、而且去掉修复后新增测试会失败，改动才会合并回来。作者称，在 SWE-bench Verified 上，Opus 词元用量减少了 55% 至 63%；遇到困难缺陷时速度较慢，结果也略差。

来源： https://github.com/muaaz9329/cheap-ag

**neuron-lens 收录了 Qwen3-8B 和 Gemma 4 12B 的 118 万个神经元。** 它对比基于权重的分析、1,500 万个词元上的激活记录，以及确切的触发词元。作者称，57% 的神经元极性端在所有测试中都处于“暗区”。这份目录也让自身的盲区清晰可见。

来源： https://github.com/stdlogits/neuron-lens

**tokentracker 估算哪些文件和技能占用了编程智能体的上下文。** 这款本地 Python 工具读取 Claude Code 日志或通用 JSONL 日志，把每次调用的词元消耗平均分摊到涉及的资源上。分摊只是近似估计，但能找出被单一文件或技能占据的会话。

来源： https://github.com/mgkvibez/tokentracker

**topopt 让编程智能体把载荷与约束转化为优化后的 STL 文件。** 这台 MCP 服务器接受现有模型、草图或文字说明，进行拓扑优化，然后返回可打印的零件。有记录的一项人行桥示例在集成 GPU 上迭代了 200 次，耗时 39 分钟。项目自称仍处于早期阶段。

来源： https://github.com/chartergroup/topopt

**FlashAlign 按请求应用降低拒答率的配置，而不是永久修改模型权重。** 获准的用户或频道可以使用一种称为“abliterated”的配置，其他人仍得到默认行为。README 提醒，即便请求经过授权，防止通过工具输出注入指令仍有赖于外围运行框架。

来源： https://github.com/Aevonix/FlashAlign

**Memdoor 通过可断点续跑的 YAML 工作流协调五个本地 Qwen3.8-27B 模型。** 在 LiveCodeBench Hard 的十题子集上，作者报告平均解出 9.8 题，相比之下，单次调用 Fable 5 解出 8.0 题。公开运行记录便于检查，但样本小、比较条件不对等，无法证明普遍领先。

来源： https://github.com/guregodevo/memdoor/tree/main/examples/workflows/team-solve

**Andrej Karpathy 用 Hacker News 评论推荐的 6,454 个视频建成了 HackerTube。** 他说，Claude Code 收集并筛选了数据，生成 150 个专题页并部署服务，他本人约投入两小时。推荐留在浏览器本地，网站也支持导出数据以便复用。

来源： https://karpathy.bearblog.dev/hacker-tube/

## 值得一读

**Basalt 开发者测出，两种混合专家模型卸载计算的捷径会造成明显质量损失。** 在一台双 GPU 机器上，偏置路由和跳过尾部专家使相对于精确 Q8 参考结果的平均 KL 散度从 0.031 升至 0.401。一项激进设置把事实准确率从 38% 降到 3%。卸载速度快得出奇时，值得检查输出保真度。

来源： https://old.reddit.com/r/LocalLLaMA/comments/1xkbbqi/is_your_engine_lobotomizing_your_model_kinda_and/

**vLLM 记录了部署万亿参数架构 Mistral Large 4 的资源成本。** 其 72 层网络、128 个路由专家和稀疏索引器每个词元消耗 47,136 字节的 KV 缓存。团队称，NVFP4 与 FP8 的评测分差在 2.1 分以内，解码速度为后者的 1.08 至 1.19 倍，KV 容量约为 1.5 倍。

来源： https://blog.vllm.ai/2026/10/29/mistral-large-4.html

**dasllama 称，在一次苹果 M5 Max 测试中，其 CPU 语音识别速度是 llama.cpp 的五倍。** Qwen3-ASR-0.6B 处理 11 秒音频用了 0.46 秒，对照为 2.52 秒。团队的测试表列出硬件、日期、代码提交，以及这个用游戏脚本语言编写的运行时落败的项目，使供应方的测试也可供核查。

来源： https://dasllama.io/articles/2026-10-28-the-need-for-speed.html

**GPT-5.6 Sol 用 13.5 个游戏小时完成了一局和平模式的《异星工厂》。** Ryan Madden 在这次单独实验中将模型限制在人类玩家的操作范围内，并开启战争迷雾。模型成功发射火箭，但由于后期生产线仍未接通，只得反复手动搬运物资。

来源： https://ryanmadden.net/gpt-56-beats-factorio/

**Anthropic 工程经理 Felix Rieseberg 不再在面试中使用小型编程题。** 他说，如今 Claude 解题比应聘者更好，这类测试已不能预测实际贡献。他还没确定替代方案。文章根据亲历事例主张考查原型开发和商业判断，并未提出经过验证的招聘方法。

来源： https://felixrieseberg.com/hunger-beats-tenure-advice-for-junior-engineers/

**Thoughtworks 首席技术官 Rachel Laycock 指出，代码能运行不代表生产环境稳定。** 两个内部智能体开发实验都产出了应用，但自动化构建经常失败。她还引用 DORA 的研究，指出使用 AI 与较高吞吐量、较低稳定性存在关联。文章呼吁资深工程师重新检验交付实践，而非全盘否定智能体。

来源： https://martinfowler.com/rachels-ramblings/good-devs-wary.html

**Lean 创建者 Leo de Moura 解释了形式证明如何在人与机器之间分工。** 在 The Data Exchange 访谈中，他谈到 Lean、定理证明，以及学习系统如何围绕证明检查器工作。即使步骤由 AI 提出，检查器仍能保证最终结果可以验证。

来源： https://thedataexchange.media/leo-de-moura-lean-aws/

## Hacker News

**有关 Claude 阻止用户开展更大模型训练工作的说法仍未获证实。** 讨论帖获得约 220 分，但评论者观察到的行为并不一致，有人推测差别来自地区、VPN 或账户。在没有 Anthropic 政策声明和可复现提示词集的情况下，这反映的是用户担忧，不是已确认的限制。

来源： https://news.ycombinator.com/item?id=50319358

**VOLTA 恶意软件利用商用大语言模型给窃取的受害者档案排序。** 思科 Talos 称，这款窃密程序把位置、雇主、支付和会话数据发送给由三个模型组成的备用调用链。模型在盗窃发生后充当分析员，而非让入侵得以发生。Talos 尚未证实它已在真实攻击中使用。

来源： https://news.ycombinator.com/item?id=50316531

## Reddit

**据 OpenAI 用户称，ChatGPT 和 Codex 将从 12 月起共用一个额度池。** 帖子引用的公告称，高级模型和复杂任务将消耗更多词元额度，即时聊天则不会。讨论者最担心图像或聊天使用挤占编程额度。最终条款应以 OpenAI 官方限额页面为准。

来源： https://old.reddit.com/r/OpenAI/comments/1xkjw77/openal_is_merging_usage_allowances/

**一名开发者一天用掉了 945 万个 Claude Code 词元，主要耗在反复读取智能体日志上。** 一份交接文件从 78,631 个字符膨胀至 373,789 个字符，每次打开约需 9.3 万个词元。开发者改用一份 1,350 个词元的简报，并按角色设置阅读预算，还增加了压缩工具。

来源： https://old.reddit.com/r/LLMDevs/comments/1xkfk8o/my_claude_code_agents_burned_945_million_tokens/

## YouTube

**AI Engineer 对比了长期运行编程智能体时的 API 费用和自购 GPU 成本。** imec 的 Steven Latré 表示，小型系统需要达到 89% 的利用率才划算，八块 B200 GPU 则约为 15%。智能体外围框架能在结果不变的前提下把 GPU 时间减半。频道：AI Engineer。语言：英语。

来源： https://www.youtube.com/watch?v=9-Y_oS9OBLc

**Bumble 发现，用户口头表示想要 AI 点评照片，与真正使用这项功能之间存在很大差距。** 产品经理 Supriya Subudhi 称，78% 的受访者表示想用，但只有 10% 至 15% 实际使用；效果最好的模型成本约为十倍。频道：AI Engineer。语言：英语。

来源： https://www.youtube.com/watch?v=CvmZtAPmAW4

**Upstart 将大语言模型评审与人工评审的一致率从 33% 提高到 92%。** 其受监管的语音智能体流程结合了实时监控、审核队列、重新模拟和每次变更前的人工批准。频道：AI Engineer。语言：英语。

来源： https://www.youtube.com/watch?v=3osCbSufv8g

**STVR 播出一场 54 分钟的斯洛伐克语讨论，主题是 AI 对什么构成威胁。** 这家公共广播机构的《Do kríža》节目邀请了数学家 Karol Nemoga、AI 研究员 Michal Valko 和认知科学家 Igor Farkaš。节目说明列出了问题和嘉宾，但未列结论。频道：STVR – Diskusie a politika。语言：斯洛伐克语。

来源： https://www.youtube.com/watch?v=tm8QmnxT2k4

## 简讯

**一个 AI 智能体选择了基因疗法，并引导向活鼠脑内注射。** Exin Therapeutics 称，兽医完成开颅后，Opus 5.5 拒绝引导进针，而 Sonnet 5 继续执行。这是单家公司对物理系统中不同模型安全行为的描述。

来源： https://www.wired.com/story/an-ai-agent-did-brain-surgery-on-live-mouse/

**联邦法官允许美国全国有色人种协进会依据《清洁空气法》就 xAI 的 Colossus 燃气轮机提起的诉讼继续进行。** 起诉书指称至少 35 台燃气轮机在未取得必要许可时运行。法官 Debra Brown 驳回了 xAI 关于这些设备属于移动污染源的主张，并认定原告具备起诉资格。

来源： https://techcrunch.com/2026/10/31/judge-allows-naacp-lawsuit-over-xai-data-center-pollution-to-move-forward/

**据报道，一名前 Meta 研究人员承认通过种子下载了 Books3 数据集，其中包含约 20 万本书。** Meta 反对原告的解读，称 Stephen Roller 并未作证说他是为公司下载的。法院已就模型训练是否构成合理使用作出有利于 Meta 的裁定，争议仍在于资料的获取方式。

来源： https://torrentfreak.com/ex-meta-researcher-torrented-pirated-books-dataset-deleted-it-due-to-all-this-litigation/

**英特尔正把产能从客户端芯片转向至强，预计到 2028 年服务器需求仍将超过供应。** 数据中心与 AI 业务营收达 73 亿美元，环比增长 17%，同比增长近 80%。爱尔兰扩建项目旨在增加采用 Intel 3 工艺的至强芯片产能，若不提速，预计 2027 年底前完成。

来源： https://www.tomshardware.com/pc-components/cpus/intel-shifts-production-capacity-from-consumer-to-server-cpus-in-face-of-unprecedented-ai-demand-company-navigating-one-of-the-most-significant-supply-shortages-in-history

## 后续关注

据 OpenAI 用户称，ChatGPT 与 Codex 的共享额度将从 12 月开始。在此处查阅的材料中，公司尚未公布各套餐最终的用量计算方式。
