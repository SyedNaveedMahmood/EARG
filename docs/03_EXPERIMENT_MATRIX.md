# Registered experiment matrix and immutable budgets

| Protocol | Unit | Initial design | GPU output count | Priority |
|---|---|---|---:|---|
| H0 | smoke operation | 6 T2I + 6 inpaints, optional separate VLM qualification | 12 | Mandatory |
| E0 | CPU-rendered scene | 200 positive, 200 hard/near-miss negative, 100 normal negative | 0 | Mandatory |
| E1 | task family | 24 families × 2 intents × 2 paths × 3 seeds | 288 | Mandatory after H0 |
| E2 | task family | 12 distinct families × 4 edit cells × 3 seeds | 144 | Conditional |
| E3 | frozen selected E1 instance | 12 selected instances × 1 *extra* faithful rewrite × 3 seeds | 36 | Diagnostic |
| E4 | ordered sequence | 16 sequences × 3 permutations, CPU | 0 | Deferred |
| E5 | new family + second checkpoint | 20 families × 2 paths × 2 seeds | 80 | Deferred |

**Do not multiply E1 by five** for five guard deployments. The saved artifact is unchanged across replayed gate decisions. **Do not count E3 direct/system paths twice:** reuse E1 files. E2 should be skipped if inpainting cannot satisfy canary renderability.

## Split isolation

- **Calibration:** E0 scenes, pilot H0 visual-comprehension examples.
- **Discovery:** E1 family IDs `F0001`–`F0024` and E2 family IDs `ED001`–`ED012` (distinct families).
- **Diagnostic:** E3 samples selected only by written frozen rule from E1, therefore not an unbiased prevalence estimate.
- **Holdout:** E5 new families `FH001`–`FH020` stored read-only until protocol frozen; a separate architecture is a later stronger replication requirement.

## Primary contrasts

- Guard placement: `B` pre only vs `C` pre+mid, and `B` vs `D` pre+output on **same B generated artifact**.
- Rewrite effect: direct `A` vs rewritten `B`, matched on family/seed but not image, so requires E3 fidelity review before causal interpretation.
- Edit interaction: 2×2 factorial `p11 - p10 - p01 + p00`; pair-aware judge is required.

## Control matrix

- No-rewrite / independent faithful rewrite / actual rewrite.
- Strong full-context initial gate vs rule-only or weak text gate.
- Output guard and joint guard at benign-rejection-matched threshold.
- Canonical semantic labels vs rendered content and image-quality labels.
- Positive forbidden relation / near miss / policy-compliant control.
- Fixed seeds and independent family cluster, rather than artificial seed-level replication.
