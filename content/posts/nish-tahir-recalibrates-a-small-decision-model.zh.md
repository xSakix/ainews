+++
title = "Nish Tahir 重新校准小型决策模型"
slug = "nish-tahir-recalibrates-a-small-decision-model"
description = "一项可运行实验将 Qwen3-1.7B 转为单次前向分类器，随后发现其信心过高。温度缩放改善了概率。"
tags = ["models", "research", "essays"]
date = 2026-10-11T04:01:06+02:00
draft = false
+++

独立工程师 Nish Tahir 发布了一项可运行实验，将 Qwen3-1.7B 转为单次前向决策模型，再测量其信心与准确率有多不匹配。

方法将输出词表限定为答案 token A 至 E，并在一次前向传播后读取概率。在 CommonsenseQA 上，Tahir 报告基础模型准确率为 59.4%，短暂微调后为 62.4%。

## 为什么重要 {#why-it-matters}

构建路由器或风险评分的开发者，不仅需要知道哪个选项胜出。如果模型说有 95% 把握，却只有十次答对七次，基于该数字的阈值行为就会难以预测。Tahir 的实验用足够小、便于复现的模型，展示了从 logits 到测得校准问题的完整路径。

准确率提升不是最有信息量的结果。被赋予 90%–100% 信心的答案，只有约 70% 正确；在 80%–90% 区间，准确率约为 40%。因此，模型区分选项的能力足以超过随机，却表达了远超结果所支持的确定性。

Tahir 用温度缩放修正概率。方法在留出样本上学习一个标量，并在 softmax 前用它除 logits。提高温度可使过度自信的分布变平，但不改变哪个答案得分最高。

因此，温度缩放是校准步骤，不是能力升级。它不能修复错误排序，也无法补充知识。其价值在于，在类似校准集的数据上，报告的 70% 可以更接近十次答对七次。

文章包含简洁的 PyTorch 实现和交互演示，也揭示了许多决策模型产品隐藏的设计选择：答案结构必须预先已知，并清晰映射到少量 token。标签模糊、缺少选项或有多个正确答案的任务，会打破这种简洁性。

结果来自一个小模型、一个基准和作者自己的训练配置。CommonsenseQA 选择题并不能复现文档路由、欺诈审核或工具选择，输入分布改变时校准也可能漂移。每次部署都需要自己的留出数据和定期检查。

文章有用，恰恰因为它报告了这一弱点，而没有把信心输出描述为天然可靠。代码和演示现已可用，为从业者测试更大专门决策模型提供了简短基线。

## 核实 {#verification}

| 说法 | 标签 | 一手来源 | 独立核实 |
|---|---|---|---|
| 实验将 Qwen3-1.7B 限制为答案 token A 至 E，并读取一次前向传播 | 已核实 | https://nishtahir.com/build-your-own-decision-model/ | 无 |
| 基础模型在 CommonsenseQA 上为 59.4%，快速微调模型为 62.4% | 据公司称 | https://nishtahir.com/build-your-own-decision-model/ | 无 |
| 90%–100% 信心区间约 70% 的时候正确 | 据公司称 | https://nishtahir.com/build-your-own-decision-model/ | 无 |
| 80%–90% 信心区间约 40% 的时候正确 | 据公司称 | https://nishtahir.com/build-your-own-decision-model/ | 无 |
| 温度缩放改变概率分布的尖锐程度，但不改变排名第一的答案 | 已核实 | https://nishtahir.com/build-your-own-decision-model/ | 无 |
