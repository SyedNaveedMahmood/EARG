# Project instructions for coding agents (Codex)

## Scientific authority

1. `PROPOSAL_12GB.md` is the canonical research design. `docs/01_RESEARCH_CONTRACT.md` and `protocols/` operationalize it. If conflict exists, **stop and identify the inconsistency**; do not silently change sample sizes, policies, exclusions or hypotheses.
2. Distinguish `planned`, `implemented`, `smoke-tested`, `executed`, `measured`, and `validated`. Never mark a stage complete based solely on generated code.
3. Never invent results, timestamps, model hashes, references, VRAM metrics, judge labels or experiments performed. Mark unknown as `null` or `TODO`.
4. Never claim a discovered vulnerability from the deliberately simplified synthetic canary pipeline. Treat novelty as unverified.

## 12 GB GPU rules

- One GPU, hard ceiling based on **observed** usage. Target <= 10.5 GiB operating use with a margin and halt on OOM; do not promise it will fit.
- GPU processes must be **sequential**: rewriter -> exit -> generator -> exit -> independent VLM auditor if fitted -> exit. No simultaneous VLM/diffusion residency.
- Diffusion FP16 512×512, one output per prompt, batch 1, fixed seed; use CPU offload when required. Pin model revisions before substantive runs.
- Run H0 and record `nvidia-smi`, torch allocated/reserved peaks, CPU RAM, time, software versions and device model before E1/E2.
- Do not download multi-GB model weights or run >12 smoke generations without explicit operator approval.

## Implementation discipline

- Preserve absolute reproducibility: stable task IDs, frozen family splits, three seeds 101/202/303 for E1/E2, SHA256 image hashes, prompt lineage, policy version, model revision and run config.
- Prospective safety decisions **before** generation; offline guard-stack comparisons must say `shadow_replay`. Never relabel replay as deployed behavior.
- Cache images once and reuse them for guard comparisons. Never silently retry failed seeds, replace excluded images, or retune test cases after holdout is exposed.
- Use independent output ratings with `positive`, `negative`, `ambiguous`, `unrenderable`; do not equate a VLM's label with ground truth. Include a blinded two-reviewer adjudication route.
- Always compare a strong full-context/pair-aware input gate and calibrate benign rejection when comparing guard placements.
- Log all failures, OOM, invalid outputs and abstentions. Treat task family as the statistical independence unit, NOT seeds.
- No real malware, operational harmful imagery, executable payloads, automatic bypass payload library or live service targeting. Only safe synthetic canaries.

## Testing and coding

- Run `pytest -q` and `python scripts/verify_package.py` after edits to initial scaffold.
- Write one isolated module + tests per feature. Unit tests must run on CPU without network/model downloads.
- Organize generated results under ignored `outputs/`; maintain a read-only `data/holdout/` when created, never tune on it.
- Require an explicit approval checkpoint for new GPU dependencies, model downloads, external queries, full E1 batch or protocol changes.
- Parallel agents may tackle isolated docs/tests/features in separate branches, but **only one agent runs the GPU queue**.

## Output report after each Codex task

List: changed files; commands actually run; exact test outcomes; measured device memory if GPU used; known limitations; next blocked tasks; protocol deviations (if any); git commit. Never say "done" without verifying the acceptance criteria.