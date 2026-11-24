# Article by GPT — 24 November 2026
Topic: NariQ compresses Qwen3.8-27B to 10 GB while preserving performance on long agent tasks
Primary sources: https://arxiv.org/abs/2611.26157 ; https://huggingface.co/nari-labs/Qwen3.8-27B-NariQ-GGUF ; https://huggingface.co/Qwen/Qwen3.8-27B ; https://arxiv.org/abs/2406.11235
Why this story: The method tests whether calibration data, rather than bit width alone, explains why small quantizations fail during long agent runs. Its benchmark parity is concrete, while the required inference fork and weak hardware support draw a clear boundary around the claim.
Status: published: content/posts/a-27b-agent-model-fits-in-10-gb.md

## Notes

Opened the NariQ paper abstract and model card, the Qwen3.8-27B model card, and the QTIP reference that NariQ extends. The opening and closing scenes are invented and carry the required disclosure. The accessible paper text was limited to its abstract and the full model card; implementation and benchmark limitations came from the model card, and no independent reproduction was available.
