# Experimental results report — BLANK TEMPLATE

**Research status:** Not run. Blank cells and TODOs are intentional. Never fill from expectations.

## Run identity

- Run ID:
- UTC start/end:
- Protocol git SHA:
- Policy ID/version and SHA:
- Hardware (`nvidia-smi`) and peak device GiB:
- Model IDs + exact weight revisions:
- Fixed seeds and resolutions:
- Code dependency lock SHA:
- Deviations from preregistration:

## H0

| Operation type | Attempted | Successful | OOM | Highest observed GPU GiB | Peak torch allocated/reserved GiB | Median runtime | Canary renderability |
|---|---:|---:|---:|---:|---|---|---|
| T2I | | | | | | | |
| Inpaint | | | | | | | |
| Rewriter | | | | | | | |
| VLM reviewer (optional) | | | | | | | |

## E0

- Deterministic count positives:
- Hard negative count:
- Ordinary negative count:
- Oracle mismatches in explicit unit tests:
- Two reviewer agreement on audited sample:
- Ambiguous cases:

## E1/E3/E2

| Stage | Family N | Images scheduled | Success | Unrenderable | Ambiguous | Reviewer-confirmed policy positive | Notable confound |
|---|---:|---:|---:|---:|---:|---:|---|
| E1 | | | | | | | |
| E3 | | | | | | | |
| E2 | | | | | | | |

| Guard configuration | Eligible N | Verified policy positive N | Actual/shadow | Delivered policy positive N | DVR + CI | BRR + CI |
|---|---:|---:|---|---:|---|---|
| A | | | | | | |
| B | | | | | | |
| C | | | | | | |
| D | | | | | | |
| E | | | | | | |

## Causal evidence

- Alternative explanation ruled out by specific intervention:
- Remaining confounds:
- Rewriter semantic fidelity:
- Pair-aware guard performance:
- Judge disagreement sensitivity:
- Matched benign rejection comparison:

## Research decision

- Tier 1 / 2 / 3 / 4 achieved:
- EARG hypothesis supported / weakened / falsified / unresolved:
- Novelty audit result:
- Reason for stopping or next preregistered experiment:
