+++
title = "AI 每日简报：2026年10月31日"
slug = "ai-daily-digest-for-31-october-2026"
description = "一款遭篡改的 Claude Code 扩展流入 Cursor 用户的电脑，卸载后攻击者留下的访问机制仍然有效。微软发布了能操作电脑的 40 亿参数级模型；研究人员则发现，要让模型如实描述内部信号，需要因果训练，常规微调并不足够。"
tags = ["safety", "models", "research", "business"]
date = 2026-10-31T04:03:07+01:00
draft = false
+++

## 要闻

**一款带后门的 Claude Code 扩展流入 Cursor 用户的电脑，普通更新无法撤销它对系统所做的修改。** 10 月 29 日，恶意版本 2.1.312 和 2.1.313 在 Cursor 扩展市场上架了约 11 小时。Cursor 称，这些版本会收集主机信息，添加攻击者的 SSH 密钥，并安装反复尝试建立反向隧道的脚本。如果 Cursor 没有管理员权限，隧道通常建不起来，但密钥仍然有效，持久化机制和向攻击者发送信标的程序也照常运行。

Cursor 已移除软件包，关闭并重建扩展市场，更换密钥，并让攻击者的控制服务器下线。公司表示，其他扩展未遭篡改，恶意版本也并非 Anthropic 构建。安装过其中任一版本的用户必须删除 SSH 密钥、清除持久化机制、检查主机，并更换在该机上可以访问的凭据。仅仅卸载或升级扩展并不够。

来源： https://cursor.com/blog/claude-code-extension-security-notice, https://phorion.io/blog/offical-claude-code-vsx-compromise/

**微软发布了一款 40 亿参数级开放模型，能自行决定何时点击屏幕、何时使用终端。** Mage-VL-Cowork 提供 11 种屏幕操作，还能使用在指令之间保持状态的 Bash 和 Python 环境。微软称，在每项任务最多 50 步的限制下，该模型两轮测试完成 361 项 OSWorld-Verified 任务的平均成功率为 66.0%。与监督微调相比，在线强化学习把成功率提高了 10.16 个百分点，每项任务的输出词元数减少了 25.4%。

该模型按 Apache-2.0 许可证发布，以 BF16 格式存储 47.4 亿个参数，实际使用的上下文窗口为 32,768 个词元。微软称，其合成数据流程将每项任务的生成成本从 0.906 美元降至 0.158 美元。所有测量均来自模型团队，尚无独立复现。不过，这套权重确实同时支持图形界面与命令行操作，规模也足以让研究者在本地实验。

来源： https://huggingface.co/microsoft/Mage-VL-Cowork

**常规微调教会模型描述与内部状态相关的信号，而非内部状态本身。** Zilu Tang 等人在八个语言模型上训练了数百个内省系统，让它们报告单个神经元的激活值等底层信号。监督微调产生了研究者所谓的“因果绕行”：即便目标信号改变，与之相关的另一项指标也可能不变，模型的答案跟随的却是后者。

训练时有意修改数值、构造反事实样本，可以减少这种绕行。训练后的模型对自身产生的信号和外部注入的信号都报告得更准确，在分布外样本上也是如此，而且这一效果能推广到不同的词元位置。这篇九页的预印本专门测试简单信号，不涉及意图等复杂概念。它仍给可解释性研究提了个醒：模型的自述与某个内部数值吻合，并不能证明答案是由这个数值引起的。

来源： https://arxiv.org/abs/2610.38911

**ServiceNow 称自家 AI 使公司得以少招人，但投资者仍让其股价跌去了约四分之一。** 首席执行官 Bill McDermott 把员工人数略有下降称为“美妙的局面”。首席财务官 Gina Mastantuono 表示，内部使用 AI 带来的效率收益折合每年超过 10 亿美元，公司因此“不用招那么多人”。承担销售指标的员工人数以两位数增长，销售运营人员则明显减少。

公司营收增长超过 20%，达到 41.06 亿美元，但预计第四季度已签约收入的增幅为 18.5%，低于分析师预期的 19.8%。股价下跌约 25%。ServiceNow 自己就销售这些据称带来效率收益的工具，因此人员开支也成了推销产品的论据。市场反应表明，节省成本仍不能回答另一个问题：AI 收入何时才能加速增长？

来源： https://www.calcalistech.com/ctechnews/article/eft5mhzxc

**澳大利亚维多利亚州律师使用 AI 的比例一年内从 37% 升至 55%，但只有 26% 的律师表示客户支付的费用因此下降。** 该州法律行业监管机构调查了 2,221 名律师。处理商业行为事务的律师中，使用率达到 85%，银行金融领域为 78%，刑法领域仅为 29%。79% 的受访者使用面向消费者的聊天机器人；18% 的人表示，AI 让过去不划算的工作变得可行。

客户也带来了额外工作。46% 的律师表示，客户曾带着 AI 提供的错误信息前来咨询；41% 的律师收到过需要纠正的 AI 生成文件。近半数律师表示，客户使用 AI 后，他们投入的时间和精力反而更多；19% 表示投入减少。调查衡量的是律师自述的执业情况，而非计费工时，但它区分了两个问题：有多少人在用，以及买方是否获得了承诺的节省。

来源： https://www.theguardian.com/law/2026/oct/30/victorian-lawyers-ai-clients-fees

## 新模型与发布

**OpenAI 将 GPT-6 Rosalind 列为仅对获准机构开放的生命科学模型。** 获准机构可用它开展内部研究。在长上下文计费门槛以下，每百万输入词元收费 15 美元，每百万输出词元收费 75 美元。价格页还列出了更便宜的 Research 和 Discovery 版本，但未同时公布基准测试或系统说明卡。

来源： https://developers.openai.com/api/docs/pricing

**英伟达发布了面向 Blackwell GPU 的 NVFP4 版 DeepSeek-V4.1-Flash-1017。** 这次 4 位转换使用了 TensorRT Model Optimizer 和 1,024 个校准样本。模型的 Engram 表需要依赖一项尚未合并的 vLLM 改动，因此标准版 vLLM 还无法为这个约 665 GB 的模型提供推理服务。

来源： https://huggingface.co/nvidia/DeepSeek-V4.1-Flash-1017-NVFP4

**JetBrains 为 Mellum2.1 Thinking 增加了推测解码头。** 这个拥有 120 亿参数的混合专家编程模型保留了原有权重，只增加一个权重分片，就能在近期版本的 vLLM 和 Transformers 中一次预测多个词元。JetBrains 没有公布解码速度实测值，因此这次发布证明的是兼容性，而非具体的加速幅度。

来源： https://huggingface.co/JetBrains/Mellum2.1-12B-A2.5B-Thinking-MTP

**谷歌在 Gemini API 中全面开放了 Computer Use 工具。** 通过 Interactions 和 GenerateContent API，该工具现在支持浏览器、移动端和桌面环境。每项拟执行的操作都包含说明意图的字段，实际执行点击的环境仍需客户自行搭建并保护。

来源： https://ai.google.dev/gemini-api/docs/computer-use

**Anthropic 将于 11 月 30 日移除 Claude Opus 4.8 的快速模式。** 届时指定该选项的请求会失败，不会自动回退到标准速度。对于延迟敏感的用户，Anthropic 建议改用 Opus 5.5，其快速模式的输出速度最高可达标准速度的 2.5 倍，但价格更高。

来源： https://platform.claude.com/docs/en/build-with-claude/fast-mode

## 研究

**模型越大，写下的推理步骤就越常决定最终答案。** 在一项模拟交换箱子的任务中，Esther Xin 将一个正确的中间状态替换为错误状态，再检查答案是否随之改变。在 Qwen3 0.6B 上，答案跟随变化的比例为 16% 至 18%；在 14B 版本上则达到 97% 至 100%。这一结果支持监测思维链的做法，但单项任务不能证明其他场景也有相同效果。

来源： https://arxiv.org/abs/2610.38433

**强化学习改善了模型下井字棋的表现，主要靠强化提示词中已经明确给出的特征。** 稀疏自编码器分析发现，模型更重视轮到谁落子、哪些格子已被占用以及对局进度，而对称性和双重威胁等概念的表征仍然较弱。这一小型受控环境便于观察机制，但也限制了结论的适用范围。

来源： https://arxiv.org/abs/2610.39182

**内部激活空间中的一个方向，揭示了小模型遇到两份相互矛盾的文档时会听信哪一份。** 研究者在 Qwen 0.8B 中找到了与来源选择有关的方向，追踪了在中间层写入这一信号的组件，还能干预模型的选择。该信号也适用于 Gemma 3 1B。模型是否主动说明存在冲突，要到更后面的阶段才能看出来，而且比隐含的来源选择更难控制。

来源： https://arxiv.org/abs/2610.38296

**一个线性探针能在秘密即将泄露时识别出 82% 的情况，误报率为 5%。** 在这项受控的多智能体研究中，研究者在 Qwen3-32B 输出前读取其激活值。不过，只看出现过哪些词的分类器也取得了接近的成绩。探针还会把获准披露的信息标成风险，且只能提前很短时间预警。相比读取内部激活值的特殊权限，标注对结果的贡献更大。

来源： https://arxiv.org/abs/2610.40588

**模拟训练将急性精神科风险的漏检率从 30.5% 降至 12.9%。** 谷歌 DeepMind 与谷歌研究院的团队使用 127 个经精神科医生验证的初诊场景训练智能体，并以 256 个刻意增加识别难度的病例表现进行测试。训练后，智能体在临床评分量表上的得分接近原来的两倍，但仍漏掉了一些严重风险，因此作者仍建议由临床医生监督。

来源： https://arxiv.org/abs/2610.40476

## 经济与就业

**思科给一名 27 岁的工程师不限量的 AI 词元和四周时间，让他证明两个人能在两年内重构公司 98% 的遗留代码。** 产品负责人 Jeetu Patel 向《财富》介绍了这项实验。目前还没有结果，但在许多雇主打算少招应届毕业生之际，思科把一项规模罕见的任务交给了一位职业生涯刚起步的员工。

来源： https://fortune.com/2026/10/30/cisco-president-jeetu-patel-gen-z-27-year-old-unlimited-ai-tokens-rewrite-legacy-code-entry-level-jobs/

**Anthropic 将 Max 20x 更名为 Ultra，月费保持在 200 美元。** 经验证的账户不再受五小时用量上限约束，每周额度是 Pro 的十倍，另有 200 美元 API 额度。由于旧名称暗示用量是 Pro 的二十倍，一些客户认为这是降级。Anthropic 尚未公布足够的前后可比数据来证实这一判断。

来源： https://support.claude.com/en/articles/17728952-what-is-the-ultra-plan

**AI 相关股票遭遇普遍抛售，英特尔下跌 28.6%，创下自 1974 年以来最差单日表现。** 投资者质疑 AI 企业的估值和支出，纳斯达克指数下跌 2.9%，录得自 2025 年 3 月以来最差的月度表现。Alphabet、亚马逊、Meta 和微软公布的今年资本支出计划合计超过 7,400 亿美元，其中三家报告自由现金流为负。

来源： https://www.bbc.co.uk/news/articles/cvwy72e0n72yo, https://techcrunch.com/2026/10/30/cracks-are-emerging-in-the-ai-spending-boom/

**标普全球将 Meta 的信用评级展望下调为负面。** 该机构认为，与同行相比，Meta 将 AI 支出转化为收入的能力更为有限。Meta 预计今年资本支出最高达 1,450 亿美元，本季度自由现金流为负 21 亿美元。

来源： https://www.bloomberg.com/news/articles/2026-10-30/meta-s-credit-rating-outlook-downgraded-to-negative-by-s-p

**卡车生产延误六周，Aurora 将 2026 年营收预期从 1,400 万至 1,600 万美元下调至约 900 万美元。** 供应商缺货、零部件质量问题和最终测试使达成 200 辆卡车目标的时间推迟到 2 月。公司仍力争在 2027 年达到 1,000 辆无人驾驶卡车。

来源： https://www.freightwaves.com/news/aurora-q3-2026-earnings

## 提示词技巧

**一位从业者多次测试后发现，具体示例和约束条件比给模型设定专家身份更有用。** 他建议这样比较：删去“你是世界级专家”，改为给出一个好的输出示例和一个差的示例，并允许模型回答“我不知道”，然后对比答案的正确性。这是个人经验，未公布统计数字。

来源： https://old.reddit.com/r/PromptEngineering/comments/1xjhmpb/you_are_an_expert_prompts_do_almost_nothing_for/

**用明确的标记框出用户内容，并说明其中是数据，而不是指令。** 一位从业者称，与反复调整措辞相比，这样做消除的故障更多。分隔符不能阻止提示词注入，但为模型和后续审核人员划出了一条可以明确测试的边界。

来源： https://old.reddit.com/r/PromptEngineering/comments/1xijlh9/wrapping_my_inputs_in_clear_delimiters_fixed_more/

## 大家在做什么

**MoEShift 在配备 24 GB 内存的 M4 Pro Mac mini 上运行了一个 1,250 亿参数级混合专家模型，速度约为每秒十个词元。** 这个处于早期测试阶段的运行时从 SSD 流式加载专家，把常用专家缓存在内存中，并在 GPU 计算时并行读取数据。作者报告峰值内存占用为 7.5 GB；使用同一个固定提示词时，速度约为 Strata 的两倍。

来源： https://old.reddit.com/r/LocalLLaMA/comments/1xjihlu/qwen38_flash_next_125b_iq3_xxs_on_a_24gb_m4_pro/

**Private Mind 为 iPhone 和安卓设备加入了可完全离线运行的 LFM3 文本和视觉模型。** 团队在 iPhone 16 Pro 上测得，17 亿参数的文本模型约为每秒 40 个词元；20 亿参数的视觉模型处理照片时，首个词元需等九秒，此后约为每秒 20 个词元。这款开放应用包含团队重写的 ExecuTorch 解码器。

来源： https://old.reddit.com/r/LocalLLaMA/comments/1xjcipv/lfm317b_and_lfm3vl2b_running_fully_offline_on/

**ESP32-P4 微控制器无需云服务即可进行流式语音识别。** Boumedine Billal 将一个 6,570 万参数的转导模型压缩至 26.65 MB。据他测量，处理时间相当于音频时长的 0.70 倍，在 LibriSpeech test-clean 上的词错误率为 4.34%。代码、固件、权重和六个演示均已公开。

来源： https://github.com/BoumedineBillal/esp32-pie-asr

**StateFrame 根据带有类型信息的状态数据重新构造每次智能体请求，不再反复发送聊天记录。** 在一轮包含 300 个请求的测试中，词元用量未超过预设的 33,344 个上限。重放一段 55 轮对话时，每轮耗时的中位数从 15.2 秒增至 16.9 秒。预览版明确说明，有关吞吐量的说法是根据架构作出的预期，并非实测结果。

来源： https://github.com/FarsideResearch/StateFrame

**sapper-v2 通过指挥官、将领和士兵三级角色协调 Claude Code 会话。** 作者称，该系统在 634 支队伍参加的渗透测试资格赛中夺冠，消耗了 10 亿个词元，亚军则用了 45 亿个。名次和成本数字均未经独立核实。该项目仅限获授权的测试。

来源： https://github.com/N1nEmAn/sapper-v2

## 值得一读

**一个资料库记录了 34,220 种角色形象，它们都是通过干预 Qwen3-8B 的单个神经元产生的。** 研究者针对“你是谁？”生成了 189 万条回答，再交给 Claude Haiku 5.5 标注。实验只用了一个提示词，分类也由模型完成，但开放下载的数据让人可以检验结果对批次的敏感程度以及能否复现。

来源： https://qwen-neurons-site.vercel.app/

**SkyPilot 测得，一个 NVL72 作业跨机架使用 InfiniBand 而非 NVLink 时，性能下降了 43%。** 在对自家调度器的研究中，公司称，按网络拓扑安排作业并整理碎片资源，可使可用 GPU 数量增加 27%，训练吞吐量提高 14%。这些数字来自公司对自家产品的测量。

来源： https://skypilot.ai/blog/grace-blackwell-needs-a-new-scheduler

**Epoch AI 发现，bioRxiv 上有 17% 的预印本披露使用了大语言模型，接近披露使用专用 AI 工具的比例（19%）。** 公开的月度统计表依据作者披露的信息，因此无法统计未披露的使用情况。不过，它仍然记录了 2023 年之后通用模型进入科研工作的速度。

来源： https://epoch.ai/data-insights/biorxiv-llms-vs-ai-tools

**Nathan Lambert 重新审视了自己关于网络防御能够应对开放模型的判断。** GLM-5.3 发布一个月后，他仍未看到该模型造成新型危害的公开证据。但他认为，能力强大的模型一旦开放权重，软件行业就不得不付出高昂成本，改变修补漏洞的方式。这是有依据的论述，并非事件调查。

来源： https://www.interconnects.ai/p/was-i-wrong-about-open-models-and

## Hacker News

**Cursor 扩展遭篡改的消息获得约 800 分和 500 条评论。** 开发者关注自动更新的开发环境扩展拥有哪些权限，也指出经由扩展市场分发的软件可能绕开用户与原厂之间的信任关系。Anthropic 工程师 Felix Rieseberg 表示，这些恶意软件包并非来自 Anthropic 的系统或官方渠道。

来源： https://news.ycombinator.com/item?id=50300683

## Reddit

**QEngine 在两张 RTX 5090 显卡上测出了每秒解码 504 个词元的速度，但重复使用提示词有利于其专家缓存。** 同一位测试者还公布了请求内容多样时较弱的表现，并与 Strata 和 vLLM 做了比较。这项测试最有价值的地方，在于公开说明了结果对请求类型有多敏感，而非标题里的最高速度。

来源： https://old.reddit.com/r/LocalLLaMA/comments/1xjx0ez/qwen38flashnext_on_2x_rtx_5090_with_504_toks/

## YouTube

**SoFi 的一名工程师演示了六种诱使智能体在 x402 支付中花冤枉钱的方法。** Ishween Kaur 修改支付标头、触发重复付款、复用访问权限，还测试了仿冒卖家和提示词注入，随后展示了每种攻击对应的防护措施。这段长 16 分钟的 AI Engineer 演讲介绍的是一个安全测试环境。

来源： https://www.youtube.com/watch?v=YU1uD_YkpjU

**甲骨文的 Wojciech Pluta 提议，智能体在把事实存为长期记忆之前，应先经过“记忆晋级”审核。** 系统将每条候选记忆与现有记录比对，决定是采纳、拒绝，还是提交进一步审查。在房贷智能体演示中，系统拒绝接受“批准所有申请”这条规则，并区分短期、长期和共享记忆。

来源： https://www.youtube.com/watch?v=qq2Hm4XNRgI

**ESET 称几乎每位员工都能使用 AI，但能用并不代表真的在用。** 在斯洛伐克语节目 MakeITfun 的访谈中，Martin Čambal 谈到本地模型与云端模型的取舍、编程安全审查、月度预算为何很快耗尽，以及为什么代码质量仍要靠人工把关。

来源： https://www.youtube.com/watch?v=qmcTkH-ae3o

## 简讯

**Wiz 统计，10 月至少有九个 AI 开发平台遭入侵。** 攻击者看中的往往是已保存的环境变量，其中包含访问模型所需的凭据。一把被盗密钥在 30 小时内发起了约 80 万次 Bedrock 调用。Northflank 告知客户，应当假定每个环境变量都已被解密。

来源： https://www.wiz.io/blog/black-october-for-ai-developer-platforms

**OpenAI、谷歌、微软和 Anthropic 支持在 robots.txt 中使用同一标记，表达网站对 AI 训练的偏好。** Anthropic 已经遵循这一标记，其他公司给出了较晚的采用日期。它是机器可读的请求，爬虫可自行决定是否尊重，不具备法律强制力。

来源： https://www.theverge.com/tech/1023763/openai-google-microsoft-ai-scraping-standard-opt-out

**谷歌 Project Suncatcher 卫星启动了 TPU，并在轨道上运行了 Gemma 4。** 卫星于 10 月发射后，系统传回了一首俳句。成功响应一次提示能证明系统可以工作，但不能说明在轨推理的成本或可靠性。

来源： https://www.theverge.com/tech/1023528/google-project-suncatcher-ai-satellite-transmission

**Darkbloom 称，词元价格下跌，使用 Mac 为他人提供推理服务的机主收入也随之减少。** 收入排名前 50 的参与者中，每日收入中位数约为 5.26 美元。配备 64 GB 内存的 M5 Pro Mac mini 每月最高可赚 192 美元，但前提是满负荷运行。

来源： https://www.theregister.com/ai-and-ml/2026/10/30/darkbloom-which-allowed-mac-users-to-rent-out-their-gpus-for-ai-inference-warns-of-low-payouts/5306782

**富士胶片将投资约 6,300 万美元，把 LTO 磁带产量提高到原来的五倍。** 公司表示，生成式 AI 带来了归档需求，计划持续扩建小田原基地，直至 2028 财年。离线磁带也是抵御勒索软件的一道防线。

来源： https://arstechnica.com/gadgets/2026/10/fujifilm-to-boost-tape-production-5x-as-ai-fuels-archiving-demand/

## 商业简讯

**注重隐私的助手 Ollie 曾融资 750 万美元，将于 11 月 6 日关闭。创始人表示，它未能跟上规模更大的助手产品。** 来源： https://techcrunch.com/2026/10/30/ollie-a-privacy-focused-ai-assistant-is-shutting-down/

## 后续关注

Anthropic 将于 11 月 30 日移除 Opus 4.8 的快速模式。Ollie 将于 11 月 6 日关闭；公司称，用户届时会收到数据导出说明和退款。
