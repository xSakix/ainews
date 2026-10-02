# Desk: Lab releases

Desk name for the header: `Lab releases`
Output file: `reports/YYYY-MM-DD-briefing-releases-<suffix>.md`, where `<suffix>` is your system's suffix (see `prompts/research-run.md`)

## Scope

New models and open weights, technical reports, model cards, notable version updates, and API or platform changes from AI labs — major and minor, in every region. A small lab's open model with a technical report is as much in scope as a frontier launch.

Developer tools and products count when a lab ships them (a coding agent, an SDK, an API feature, a price change). Independent and community projects belong to the builders desk.

## Window

24 hours for announcements from the labs' own channels. Up to 72 hours for a release that surfaced late — smaller labs and non-English labs are often noticed a day or two after upload — provided it appears in no earlier briefing or post. State the release date in the item.

## Labs to check

The list is a guide for breadth, not a limit. Check each region every day.

- **United States and Canada:** OpenAI, Anthropic, Google DeepMind, Meta, xAI, Microsoft (MAI, Phi), NVIDIA (Nemotron), Amazon (Nova), Apple, IBM (Granite), Allen Institute for AI (OLMo, Molmo, Tülu), Cohere, Liquid AI, Nous Research, Arcee, Prime Intellect, Reka, Together AI, Perplexity, Thinking Machines.
- **Europe:** Mistral, Hugging Face (SmolLM and others), Black Forest Labs, Aleph Alpha, Kyutai, H Company, Pleias, LightOn, Poolside, DeepL, Stability AI, Wayve, and public or national models (Swiss AI's Apertus, EuroLLM and OpenEuroLLM, BSC's Salamandra, TildeOpen and others).
- **China:** DeepSeek, Alibaba (Qwen, Wan), Moonshot (Kimi), Zhipu (Z.ai, GLM), MiniMax, ByteDance Seed, Tencent Hunyuan, Baidu ERNIE, StepFun, Xiaomi MiMo, Meituan LongCat, Ant Group (Ling, Ring), Shanghai AI Lab (InternLM, InternVL), OpenBMB (MiniCPM), Kuaishou (Kling), 01.AI, Baichuan, iFlytek.
- **Rest of the world:** Sakana AI and Preferred Networks (Japan), LG AI Research (EXAONE), Naver, Upstage and Kakao (South Korea), Sarvam AI and Krutrim (India), AI21 Labs (Israel), TII (Falcon) and MBZUAI's Institute of Foundation Models (United Arab Emirates), AI Singapore (SEA-LION), Latin American and African model efforts.

## Where to look

- Each lab's own news, blog or research page, and its GitHub organisation's releases.
- Hugging Face: recently created and trending models — `https://huggingface.co/models?sort=trending` or the API `https://huggingface.co/api/models?sort=trendingScore&limit=100` (each entry has `createdAt`); lab organisation pages such as `https://huggingface.co/Qwen` or `https://huggingface.co/deepseek-ai`.
- ModelScope (`https://modelscope.cn/models`) for Chinese releases that reach it first.
- r/LocalLLaMA new posts, which often spot open-weight releases within hours.
- Labs' posts on X, WeChat or Weibo as pointers only: cite the lab's own page, model card or repository.

## What to report

For each item, after the summary, add one line:
`Artefacts: [weights (licence) / API only / technical report / model card / code / none] · Sizes or variants: [...] · Released: [date]`

Report what is checkable: parameter counts, context length, licence, modalities, where it runs, price. Benchmark claims are the lab's own; say so.

## Sections

1. United States
2. Europe
3. China
4. Rest of the world
5. Tools, APIs and platform updates

A quiet region gets one line naming the labs checked, so a gap in coverage is visible.
