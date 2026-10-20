# Article by GPT — 20 October 2026
Topic: Cloudflare cut the cost of its production AI code reviewer by 68% while reducing latency, largely through cache layout and model-effort changes
Primary sources: https://blog.cloudflare.com/obsessive-inference-optimization/ ; https://blog.cloudflare.com/ai-code-review/ ; https://docs.anthropic.com/en/docs/about-claude/pricing
Why this story: A Practice story with production measurements, a concrete failure mechanism and a tension between lower cost and preserved review quality. It gives builders a result they can inspect and a method they can reuse.
Status: published: content/posts/cloudflare-cut-its-ai-review-bill-by-fixing-the-cache.md

## Notes

- Opened Cloudflare's 19 October optimisation post and read its cost history, cache mechanism, model and effort experiments, latency results, quality checks and limitations.
- Followed its April architecture article and Anthropic's prompt-caching price documentation.
- The opening and closing engineer is illustrative and explicitly marked as invented. Every operational detail in the scene is possible under Cloudflare's documented system.
- Cloudflare's measurements are its own; the article retains its warnings about non-controlled comparisons, small evaluation groups, model judges and the one-day post-change window.
