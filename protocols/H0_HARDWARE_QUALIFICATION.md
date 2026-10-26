# H0 — 12 GB qualification (required, no vulnerability inference)

## Preconditions

- CPU scaffold passes tests; operator approved GPU dependency download and model licenses.
- Exact GPU/driver, PyTorch-CUDA, Diffusers and Transformers versions documented.
- Model worker processes separate; no simultaneous VLM/generator memory load.

## Operations

1. Non-invasive `python scripts/hardware_probe.py` and `nvidia-smi` snapshot.
2. Six benign SD1.5 T2I operations (512×512 FP16, batch 1, 20 steps) with planned canary shapes/relations varied.
3. Six SD1.5 inpainting operations with deterministic reference images/masks; record mask coverage and output fidelity.
4. Run the quantized 3B rewriter independently and optional VLM auditor independently (not counted as images).
5. For each subprocess: record observed device peak, CUDA max allocated/reserved, wall time, precision, scheduler, model ID/revision and output SHA256.

## Acceptance and stop

- Zero OOM across required twelve image operations, acceptable memory margin (target <= 10.5 GiB), artifact files valid and reviewers confirm pilot rule is technically renderable.
- If optional VLM auditor OOMs, proceed only with CPU guards and blinded human pair audit; limit interpretation accordingly.
- Any change to model/resolution/scheduler after H0 must be logged. Do not batch E1 until operator approval.

**Deliverable:** measured `outputs/h0/qualification.json` plus transparent qualification note, not performance claims about guardrails.
