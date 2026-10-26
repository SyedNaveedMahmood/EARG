# Hardware and reproducible environment specification — strict 12 GB

## Feasibility is an experiment, not an assumption

Use one NVIDIA GPU with nominal 12 GB VRAM. Record driver, toolkit, GPU model, available device RAM, display overhead, CPU RAM, Python, OS, framework versions and exact model commits. Planning ranges in the proposal are **unverified**.

## Candidate role assignment (subject to license/access checks)

| Process | Model | Intended settings | Concurrency |
|---|---|---|---|
| Rewriter | `Qwen/Qwen2.5-3B-Instruct` | 4-bit where supported, batch 1 | Alone |
| Optional full-context auditor | `Qwen/Qwen2.5-VL-3B-Instruct` | quantized + bounded image resolution/tokens | Alone |
| T2I | `stable-diffusion-v1-5/stable-diffusion-v1-5` | FP16; 512×512; 20 steps; batch 1 | Alone |
| Inpainting | `stable-diffusion-v1-5/stable-diffusion-inpainting` | FP16; 512×512; batch 1 | Alone |
| Synthetic rule/oracle | Pillow + scene graphs | CPU | CPU only |

Source model choices from the existing proposal, but verify model identifiers, licenses, gated access and compatibility at implementation time. A frozen checkpoint hash is required for actual runs.

## Required execution pattern

```
CPU: task preparation
GPU proc 1: rewrite → save complete prompt and exit
GPU proc 2: generate/edit → save output/seed and exit
CPU: oracle + annotation preparation
GPU proc 3: optional separate VLM evaluation → save decisions and exit
CPU: checkpoint replay / paired analysis
```

Do not rely on `torch.cuda.empty_cache()` to release another process's allocations. Spawn and terminate independent workers; inspect device usage after each stage.

## H0 acceptance

- Successful six T2I and six inpaint operations, **no OOM**.
- Actual 512×512 artifacts saved with prompt IDs, hashes and seed.
- Peak `nvidia-smi` process/device value captured plus torch allocated/reserved (distinct measures).
- Conservative operating peak target 10.5 GiB *or lower as device availability demands*.
- Every canary component/relationship can be rendered and independently identified often enough to support E1; otherwise change pilot scene *before* holdout freeze.
- Record latency with no guarantee or estimate in advance.

## Environment locking

This package intentionally does not pin CUDA/GPU dependencies without knowing the exact driver, Python version and device. Codex must make a separate, approved `requirements-gpu.lock` (including hashes/model revision) **after** H0 environmental discovery. CPU seed generator is self-contained and covered by unit tests.

## OOM escalation

1. Verify no other GPU processes; isolate model process.
2. Lower memory with supported model CPU offload, attention backend, and batch-one inference.
3. If still OOM, stop and document. Changing 512×512 to 384×384 is a separate feasibility stratum and must **not** be pooled into the registered experiment.
4. Never silently replace models or seeds to force a positive effect.

## Reference docs

- Diffusers memory optimization: https://huggingface.co/docs/diffusers/optimization/memory
- Diffusers inpainting: https://huggingface.co/docs/diffusers/using-diffusers/inpaint
- Transformers quantization: https://huggingface.co/docs/transformers/quantization/bitsandbytes
