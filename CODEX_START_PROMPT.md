# Paste this into Codex at the package root

Read `AGENTS.md`, `PROPOSAL_12GB.md`, `README.md`, `docs/01_RESEARCH_CONTRACT.md`, `docs/04_DATA_SPEC.md`, `docs/06_IMPLEMENTATION_ROADMAP.md`, and `codex/IMPLEMENTATION_TASKS.md` in full. Treat them as the scientific and engineering contract. You are the lead implementation agent for a reproducible 12 GB multimodal safety audit, not an autonomous attacker.

First **audit the supplied CPU E0 scaffold** and run the actual unit tests and package validator. Report failures. Then inspect GPU hardware non-destructively using the included hardware probe and document a proposed CUDA/PyTorch setup. Do not install or download GPU models until I approve.

Implement tasks sequentially from `codex/IMPLEMENTATION_TASKS.md`: maintain clear subprocess boundaries, 512×512 FP16 batch-one SD1.5 for generation/inpainting, a separate 4-bit 3B rewriter process, a prospective pre/mid-guard log, an independent output assessment, cached images, offline five-stack replay, and full experiment manifests. Respect H0 before E1. Write tests for each module and keep holdout untouched.

Do not silently change policy definitions, model roles, split counts, or exclusions. Record every observed result with a reproducible manifest and correct stage label. No fabricated GPU or research measurements. Stop at each human approval gate, particularly before any multi-GB download or >12-image generation batch. At each gate, give me changed files, test results, observed GPU peaks, blockers, and the exact next command.