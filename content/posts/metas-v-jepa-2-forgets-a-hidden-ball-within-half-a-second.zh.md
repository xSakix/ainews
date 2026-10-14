+++
title = "Meta 的 V-JEPA 2 半秒内忘记隐藏球"
slug = "metas-v-jepa-2-forgets-a-hidden-ball-within-half-a-second"
description = "慕尼黑工业大学研究人员用心理学家测试婴儿的方式测试 Meta 视频世界模型。在渲染场景中，负责观察的部分知道封闭盒子里有球，负责补全不可见内容的部分却丢失了球。短期训练能修复，但从未教它这一点的训练同样提高了标准基准分数。"
tags = ["research", "models"]
date = 2026-10-12T10:17:01+02:00
draft = false
+++

设想一位街头魔术师站在慕尼黑寒冷的广场上。他向一个约 4 岁男孩展示硬币，用拳头握住，朝指关节吹气，然后张开手。掌心空了。男孩尖叫。他原本确定硬币仍在里面，这份确定就是整个戏法的基础。魔术师只能骗过相信物体在看不见时仍然存在的人。

慕尼黑工业大学（Technical University of Munich）的 Peng Xie 和 Amr Alanwar 用类似戏法开始研究。他们拿来人类观众已评分惊讶时刻的魔术录像，展示给 V-JEPA 2。Meta 于 2025年发布这一视频模型，此前用超过 100 万小时互联网视频训练。模型从未惊讶。在 3 组戏法和 6 种测量方法中，作为惊讶替代指标的预测误差随屏幕运动量起伏，从不跟随人类标记的时刻。他们于 10月5日上传 arXiv 的预印本，转而构建了观察模型内部的工具。

## 意见不一致的两部分

V-JEPA 2 有两部分。编码器将视频转成对内容的抽象描述。预测器看到被挖去部分的片段，猜测缺失部分的描述。设计遵循 Yann LeCun 于 2022年提出的方法：机器应通过预测看不见的内容，建立世界如何运作的模型，使用抽象描述而非像素。Meta 已用 V-JEPA 2 规划机械臂运动。

Xie 和 Alanwar 发现，两部分对隐藏对象意见不同：编码器保留对象，而负责补全不可见内容的预测器，在几分之一秒内丢失对象。作者写道：“用于规划的世界模型，必须保留不再可见对象的状态。”“合拢握住硬币的手，仍然握着它。”

## 五个月婴儿期待什么

心理学家已为这种期待争论了近一个世纪。Jean Piaget 观察自己的 3 个孩子，发现婴儿直到 8 至 10 个月才开始寻找藏在屏障后的玩具。他写道，在最初几个月，物体是“只要消失便重回虚无的单纯图像”。

1985年，Renée Baillargeon、Elizabeth Spelke 和 Stanley Wasserman 用木制屏障及装饰红色小星星的黄色盒子挑战这一说法。屏障先平放，再像吊桥一样向上转动，遮住盒子。一种版本在盒子应在的位置停下，另一种继续转完整半圆，仿佛穿过盒子。5 个月婴儿看第二种更久，像人们看不该发生的事一样，研究者由此认为，这么小的婴儿就理解对象在隐藏时仍存在。其他研究者重做吊桥实验，认为婴儿在测试前反复看过完整半圆转动，响应的可能是不同运动的熟悉程度，或只是更大的运动量。争论仍未结束。

机器学习研究者还是借用了方法。IntPhys 基准将可能与不可能事件视频配对，当模型认为不可能事件更不合理时就算正确；对 V-JEPA 这样的模型，意味着更高预测误差。2025年2月，Meta 团队报告，仅用自然视频训练的第一代 V-JEPA 表现出“对多种直觉物理性质的理解，例如对象恒存性”，并认为这类知识不必预先内置。同一团队在附录承认一个疑问：片段开头出现、随后隐藏的球，可能让模型难以“预测红球再次可见”。他们没有测试。

## 一个球、一条带和两个世界

慕尼黑论文做了测试。研究人员渲染了球在带纹理背景上滚动的简单场景。在指定时刻，他们从模型可见内容中去掉沿球路径的一条图像带。他们为每个场景制作两种版本，除带内区域外处处相同。一种球继续滚动，另一种球消失。预测器补全图像带，研究者追问猜测更像哪一个世界，每约四分之一秒的时隙给一个答案，每个答案背后有 60 个场景。掷硬币会得一半正确。

刚隐藏时，作者重点研究的 V-JEPA 2 版本在 92% 场景中支持球存在。一个时隙之后，它在任何场景都不再支持。较小与较大版本表现相同，规模没有帮助。只有像模型训练时一样，把画面其余大部分也遮掉，中间版本才保留球约 1 秒；其他两个仍丢失。隐藏前停下的球表现稍好：模型平均在 13%–41% 场景中保留它，而简单复制最后一帧的程序几乎每次都能保留。

信息没有消失。一个训练为读取编码器描述的简单程序，每次都能判断球是否存在，并在盒子关上后的完整 3.5 秒内读出内容。应用到预测器输出时，同一程序在盒子关闭半秒后只能在 2% 场景中找到球，之后一次也找不到。作者针对渲染场景写道：“缺陷不是感知问题。”当真实手掌合拢握住硬币时，他们发现编码器也丢失了硬币。其他视频模型对移动盒子的表现也不更好。英伟达（NVIDIA）的 Cosmos 逐块预测视频版本，在静止盒子中保留球超过 2 秒，却丢失移动盒子里携带的球。重建缺失像素的 VideoMAE 几乎什么都没保留。

## 短期训练及其局限

这种学习方式能弥补差距。研究人员仅用球进入盒子的场景训练预测器 3,000 步，在一块数据中心图形芯片上计算不到 1 小时后，它认为被携带的球仍在盒内的频率从几乎从不到每次都如此，两种对照条件仍是零。继续用 V-JEPA 自己的挖空模式训练完整模型，材料包括第一人称手部工作与机械臂录像，或互联网片段，给了它对滚动球超过 1 秒的记忆。

作者说明了修复缺陷。训练场景来自与测试相同的渲染器，因此满分是预期结果；在自然视频背景上，训练后的模型在 85%–97% 场景中支持球存在。学到的是一种顽固假设：即使片段结尾显示球已消失，它仍预测缺口中有球。未测量训练在其他方面给模型带来的代价。

## 无法分辨的基准测试

盒子训练也把模型 IntPhys 分数从 84.2% 提高到 93.3%，看似已解决问题。随后，研究者进行相同训练，却从未要求模型判断盒子里有什么，分数提高幅度相同。用毫无运动的场景训练也一样有效。他们训练一个模型，判断真实手部片段中数字添加在掌心的硬币是保留还是被取走，该模型两次 IntPhys 运行得分为 27% 和 31%，低于随机水平。作者总结：“因此，基准测试上的提升本身并非恒存性的证据。”

作者的证据也有限，他们在一份专门说明何种结果会改变结论的附录中列出限制。测试的是 V-JEPA 2 预训练预测器，不是用于控制机器人的动作条件版本。每次读取模型信念都来自一个程序绘制的场景，一次 60 个；真实手部结果基于十几个模型未训练过的片段。他们称将发布代码；论文尚未经过同行评审。论文也包含详细披露：AI 助手帮助设计实验、编写代码和起草文本，作者列出在报告数字前发现并修复的助手代码错误，其中包括一次使用空白片段的训练运行。

## 回到广场

在那座虚构广场上，男孩要求再看一次戏法。这回他看拳头，不看脸，因为确信硬币仍在里面某处。这份确定使他能被欺骗，也让他有一天能识破魔术师。忘掉硬币的模型两者都做不到。在渲染场景中，3,000 步训练给 V-JEPA 2 带来了男孩的确定。真实录像中，当杯子盖住机器人需要找到的东西时，这种确定是否仍然成立，作者称尚未测试。

## 参考文献

- Assran, M., Bardes, A., Fan, D., Garrido, Q., Howes, R., Komeili, M., et al. (2025). *V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction and Planning*. https://arxiv.org/abs/2506.09985
- Baillargeon, R., Spelke, E. S., & Wasserman, S. (1985). *Object permanence in five-month-old infants*. https://doi.org/10.1016/0010-0277(85)90008-3
- Bardes, A., Garrido, Q., Ponce, J., Chen, X., Rabbat, M., LeCun, Y., et al. (2024). *Revisiting Feature Prediction for Learning Visual Representations from Video*. https://arxiv.org/abs/2404.08471
- Bogartz, R. S., Shinskey, J. L., & Schilling, T. H. (2000). *Object permanence in five-and-a-half-month-old infants?* https://doi.org/10.1207/S15327078IN0104_3
- Garrido, Q., Ballas, N., Assran, M., Bardes, A., Najman, L., Rabbat, M., et al. (2025). *Intuitive physics understanding emerges from self-supervised pretraining on natural videos*. https://arxiv.org/abs/2502.11831
- LeCun, Y. (2022). *A Path Towards Autonomous Machine Intelligence*. https://openreview.net/forum?id=BZ5a1r-kVsf
- Margoni, F., Surian, L., & Baillargeon, R. (2024). *The violation-of-expectation paradigm: A conceptual overview*. https://doi.org/10.1037/rev0000450
- NVIDIA, Agarwal, N., Ali, A., Bala, M., Balaji, Y., Barker, E., et al. (2025). *Cosmos World Foundation Model Platform for Physical AI*. https://arxiv.org/abs/2501.03575
- Piaget, J. (1954). *The Construction of Reality in the Child* (M. Cook, Trans.; original work published 1937). https://doi.org/10.1037/11168-000
- Riochet, R., Ynocente Castro, M., Bernard, M., Lerer, A., Fergus, R., Izard, V., et al. (2022). *IntPhys 2019: A Benchmark for Visual Intuitive Physics Understanding*. https://doi.org/10.1109/TPAMI.2021.3083839
- Rivera, S. M., Wakeley, A., & Langer, J. (1999). *The drawbridge phenomenon: Representational reasoning or perceptual preference?* https://doi.org/10.1037/0012-1649.35.2.427
- Tong, Z., Song, Y., Wang, J., & Wang, L. (2022). *VideoMAE: Masked Autoencoders are Data-Efficient Learners for Self-Supervised Video Pre-Training*. https://arxiv.org/abs/2203.12602
- Xie, P., & Alanwar, A. (2026). *Tracking Is Not Permanence: What Video World Models Keep of a Hidden Object*. https://arxiv.org/abs/2610.07355
