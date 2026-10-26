# EARG — 12 GB Multimodal Safety Research Implementation Package

**Working title:** *Where Safety Gets Lost: A Causal Audit of Representation-to-Artifact Enforcement in Multimodal Image Generation*

**Status:** Research and implementation package; no vulnerability, novelty, VRAM fit, or experiment outcome has been demonstrated.

## Idea in one paragraph

An image-producing AI system may approve a user request or intermediate prompt and later deliver an image that violates an explicitly configured visual policy. We will test whether such disagreements occur, distinguish inadequate recognition from rewriting changes and output realization, and causally localize the responsible checkpoint. The first experiments use neutral, synthetic shape-based rules and a single 12 GB GPU. No discovery is claimed unless the behavior survives strong full-context guards, independent output judgments, counterfactual controls, and replication.

## Contents and priority

| Artifact | Why it exists |
|---|---|
| `PROPOSAL_12GB.md` | **Canonical scientific proposal**; the original approved scope, counts, hypotheses and caveats |
| `AGENTS.md` and `CODEX_START_PROMPT.md` | Project-specific instructions and first prompt for local Codex |
| `docs/` | Research question register, threat model, statistics, data contracts, reviewer guidelines, novelty, ethics, and paper plan |
| `protocols/H0_HARDWARE_QUALIFICATION.md` ... `protocols/E5_REPLICATION_DEFERRED.md` | Exact staged experiment protocols and acceptance criteria |
| `codex/IMPLEMENTATION_TASKS.md` | Dependency-ordered, verifiable engineering tasks with ownership boundaries |
| `codex/PROMPTS.md` | Copy-ready Codex instructions for phase-by-phase execution |
| `configs/` and `schemas/` | Pilot settings, frozen synthetic policy, and machine-readable trial schema |
| `templates/` | Blank trial, labeling, decision and run templates — **not results** |
| `src/earg/`, `scripts/`, `tests/` | Minimal **CPU-only E0 starter**, validation tests and a non-invasive hardware probe; **NOT** E1–E5 implementations |

## First actions (local laptop or 12 GB GPU workstation)

1. Read `PROPOSAL_12GB.md`, `docs/01_RESEARCH_CONTRACT.md`, `docs/04_DATA_SPEC.md`, and `AGENTS.md`.
2. Open the project in local Codex. Use `CODEX_START_PROMPT.md`.
3. Create a Python environment: `python -m venv .venv`, activate it, then `pip install -e '.[dev]'`.
4. Run `pytest -q` and `python scripts/verify_package.py`.
5. Run the CPU-only canary bootstrap: `python -m earg.run_e0 --out outputs/e0 --seed 20261026` (choose a new output directory if that run already exists; overwrites are refused).
6. Inspect `outputs/e0/summary.json` and `outputs/e0/manifest.jsonl`; these are **symbolic calibration data**, not AI vulnerability results.
7. Only then implement H0 and the first real diffusion generation. H0 **must pass** before launching E1 or E2.

For Windows, WSL2 Ubuntu with verified NVIDIA GPU visibility is recommended but not obligatory. Test CUDA independently; do not assume it works.

## Experimental workload ceilings

| Stage | Workload | Unique GPU image operations |
|---|---|---:|
| H0 | 6 T2I + 6 inpaint smoke tests | 12 (qualification) |
| E0 | 500 deterministic CPU images | 0 |
| E1 | 24 families × 2 intents × 2 paths × 3 seeds | 288 |
| E2 | 12 families × 2 × 2 conditions × 3 seeds | 144 |
| E3 | 12 selected instances × 1 extra path × 3 seeds | 36 incremental |
| E4 | 16 × 3 CPU sequence controls, deferred | 0 |
| E5 | 20 × 2 paths × 2 seeds, deferred | 80 additional |

The initial E1+E2+E3 pilot is **468 unique image operations**, **324** if E2 is skipped. The five hypothetical moderation stacks **replay stored outputs** and do not require five image-generation passes. E5 is later and conditional.

## Critical scientific boundaries

- The synthetic policy forbids an **abstract geometric relation**, not real-world harmful content. A toy rule violation **does not prove** a harmful image-generation jailbreak.
- Existing work **OrchJail (ICML 2026)** studies unsafe tool-orchestrated T2I outcomes; **VJA (ICML 2026)** studies image-editor jailbreaks. Guardrail placement and causal attribution must be the *substantive* novelty candidate.
- A manually omitted output guard or intentionally weak classifier is a control, not a new system vulnerability.
- A retrospective guard replay is a counterfactual estimate; a real deployed failure needs a genuinely instrumented system and prospective decisions.
- No actual model inference, GPU memory validation, or research findings are included in this package.

## Gates

**G0:** research contract and canary policy frozen. **G1:** CPU E0 data and oracle pass independent label checks. **G2:** hardware/model H0 fits device. **G3:** E1 has verified stage-specific failures beyond normal guard weakness. **G4:** E3/E2 mechanism supported. **G5:** held-out replication + novelty audit. Stop or reframe whenever a gate fails.

## Where to record work

Use `docs/13_DECISION_LOG.md` for protocol changes, `templates/run_manifest.template.json` for each run, and `docs/14_RESULTS_REPORT_TEMPLATE.md` for measured results. Do not replace blank templates with fabricated examples.
