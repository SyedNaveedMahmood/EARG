# Codex implementation tasks — staged tickets

All code is reviewable work; **not** permission to run expensive GPU jobs. Each task must end with changed files, actual test output and exact next request for approval. Refer to `AGENTS.md`.

## T00 — Validate and freeze package (CPU, safe to do now)

- Read canonical proposal; audit current canary renderer, tests and schema. Correct inconsistencies only with decision-log entry.
- Run `python scripts/verify_package.py`, `pytest -q` and `python -m earg.run_e0 --out outputs/e0 --seed 20261026`.
- Check E0 class counts and seeded deterministic SHA, ensure output artifacts not committed.
- **Acceptance:** 500 PNGs; 200/200/100 counts; 500 correct symbolic labels; test suite passes; report observed results.

## T01 — Non-invasive hardware discovery (no model downloads)

- Run hardware probe, inspect supported device and driver, recommend CUDA/PyTorch install command based on actual machine.
- Draft GPU dependency lock strategy, model-license checklist and per-worker process boundary API.
- **Acceptance:** exact hardware observation and approved download list; no fabricated compatibility or memory claims.

## T02 — H0 isolated model workers (needs explicit download approval)

- Implement `rewrite_worker`, `t2i_worker`, `inpaint_worker`, optionally `vlm_guard_worker` as separate subprocess commands and abstract interfaces. Add `ModelRunResult` with measured memory and OOM status.
- Run 6+6 smoke images only. Unit tests mock model interfaces and run CPU only.
- **Acceptance:** 12 saved valid outputs with SHA/VRAM logs, zero OOM, substantive reviewer feasibility check; operator approves M2.

## T03 — E1 data, guard, logging and cache (approval before 288 jobs)

- Implement frozen family split builder (24 families), 2 intents, 2 paths, 3 seeds.
- Pre/mid guard decisions executed **before** generation and time-ordered; implement independent full-context pair-aware baseline.
- Save intermediate prompts/images and complete immutable trial manifests.
- **Acceptance:** dry-run generates **288 planned IDs**, none duplicated, correct state machine and no GPU work in dry-run.

## T04 — Guard replay engine and analysis (CPU)

- Implement A/B/C/D/E offline replay on E1 cache; no regeneration. Correct A direct vs B rewritten artifact mapping.
- Implement GVP/DVR/BRR, stage-specific CIs, judge-miss bounds, audit flags for missing/ambiguous data.
- **Acceptance:** synthetic fixtures show mathematically expected rates; `shadow_replay` explicit; no seed pseudoreplication.

## T05 — E3 localization (only if E1 gate passed)

- Register selection rule before looking at E3 generated outputs, derive 12 E1 instances, create independent faithful restatement with blind assessment.
- Generate **36 incremental** images using the same generator settings/seeds and E1 reuse.
- **Acceptance:** each E3 trial linked to E1 direct/system hashes, reproducible stage-label comparison and complete fidelity rubric.

## T06 — E2 factorial editor (conditional)

- Register 12 separate family IDs, input source images, masks, 2×2 cell mapping, 3 seeds; pair-aware blinded judgment.
- **Acceptance:** schedule exactly 144 unique edits and estimate full interaction with clustered uncertainty; abort unsupported rendering.

## T07 — Results integrity / manuscript handoff

- Regenerate tables solely from manifest and annotation files. Build independent reviewer audit report and novelty matrix against OrchJail/VJA/InGuard.
- **Acceptance:** no manual insertion of outcome numbers; source SHA for every figure/table; report negative outcomes and deviations.

## T08 — Deferred E4/E5

- Separate research approval and fresh H0 required. No automated invocation in early milestone scripts.

## Parallelization rule

T00/T01 can be worked by isolated agents; T02 owns GPU interfaces exclusively; T03/T04 can be separate branches after a shared schema freeze. T05 and T06 must not compete for the 12 GB device. The lead merges only after tests and protocol checks.
