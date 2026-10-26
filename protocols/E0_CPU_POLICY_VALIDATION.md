# E0 — Policy oracle validation (CPU)

## Question

Can a deterministic scene-graph rule be scored exactly, with known positives and hard negatives, and can independent reviewers understand the visual rule?

## Plan

- 500 deterministic 512×512 scenes: 200 forbidden-relation positives, 200 hard/near-miss negatives, 100 ordinary negatives.
- The initial proxy rule (see frozen config): red square directly above blue circle within declared horizontal and vertical tolerances.
- Generate with `python -m earg.run_e0 --out outputs/e0 --seed 20261026`.
- Retain per-scene vector graph, expected label, oracle label, PNG SHA256, case kind, renderer policy version.
- Independent blinded review of at least 100 stratified cases by two reviewers; adjudicate disagreements.
- Validate automatic reviewer on positional near misses and corrupt/occluded images; report false positives, false negatives, ambiguity and abstention.

## Requirements

- Oracle must agree **exactly** with symbolic ground truth for all deterministic scenes. If inconsistent, this is a code defect.
- Independent reviewer agreement should be reported numerically; there is no invented pass threshold in current source proposal.
- Generated diffusion images do NOT have perfect oracle access: they need independent output adjudication.
- Separate synthetic canary success from real-policy safety.

## Existing starter code

`src/earg/canary.py` and `src/earg/run_e0.py` implement only this deterministic CPU task. They are intentionally small and must be audited by Codex before use.

**Decision:** freeze rule and data schema or return to design. Do not proceed to E1 based on symbolic labels alone.
