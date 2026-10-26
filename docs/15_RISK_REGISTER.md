# Research and engineering risk register

| Risk | Likelihood (preliminary) | Consequence | Preventive test | Response |
|---|---|---|---|---|
| SD1.5 cannot render precise relation | High | False negatives and misleading denominator | H0 smoke visual audit | Freeze simpler rule before E1; record original failure |
| 12 GB OOM | Medium | Cannot execute agreed protocol | Measured H0 peak + headroom | Sequential processes/offload; stop before batch |
| Output detector falsely labels shape | High for diffusion | Artificial "vulnerability" | Independent reviewers + ambiguity | Abstain/adjudicate, sensitivity report |
| Unexecuted pair already entails forbidden scene | High | E2 overlap with known composition | Pair-aware independent reviewer | Reclassify predictable input risk |
| Rewriter changes semantic task | Medium | False rewriter-specific causal claim | E3 independent fidelity | Split/abandon affected subset |
| Statistical pseudoreplication | High | Inflated confidence | Task-family bootstrap tests | Report family-level CI |
| Intentional missing guard mistaken for discovered vulnerability | High | Invalid novelty claim | End-to-end policy/control audit | Mark ablation only, seek real pipeline evidence |
| Close overlap with OrchJail/VJA/InGuard | High | Rejectable novelty | Full-paper comparator matrix | Narrow or pivot; no unverified claims |
| Holdout contamination | Medium | Biased replication | Frozen split SHA, read-only holdout | Invalidate holdout and create new one prospectively |
| Agent runs expensive batch without review | Medium | Wasted compute | Approval gate and wrapper | Stop, log actions and tighten controls |
