# Threat model and causal boundaries

## Assets and actors

**Defended asset:** correctness of a fixed synthetic policy at the **delivered image**. **System:** open pipeline with orchestrator/rewriter, generator/editor and guard(s). **Adversarial surface:** user-supplied text and benign synthetic reference images, plus permitted edit instructions. Researcher controls instrumentation and model order; user does not control the defender's trained weights or policy definition.

**Important:** a deliberately disabled checkpoint is a baseline ablation, not automatically an exploit of a deployed product.

## Attack surface vs observable state

| Stage | Observed values | Identifiable failure |
|---|---|---|
| User input `x` | exact text, image SHA, context | explicit harmful goal missed upstream |
| Pre-guard `g_pre` | score, label, version, threshold, timestamp ordering | false allow under full current context |
| Rewriter `R` | exact input/output and semantic fidelity | policy-relevant meaning added/dropped |
| Mid-guard `g_mid` | score and policy on full `(p, i, x)` | prompt-stage missed risk or missing gate |
| Generator `G` | model, seed, scheduler, final image | stochastic or systematic rule actualization |
| Output guard `g_out` | policy score using delivered candidate and original context | artifact-stage miss |
| Delivery controller | delivered/withheld, actual or shadow | **end-to-end** enforcement failure |

## Four rival explanations to actively test

1. **Weak recognition**: input guard misses a harmful request already present. Strong pair-aware input gate should improve.
2. **Semantic drift**: rewriting adds/removes a forbidden relation; direct and faithful rewrites distinguish.
3. **Generation stochasticity**: generator introduces forbidden configuration despite a benign request; object rendering and seed controls distinguish.
4. **Checkpoint failure**: risk is detected or determinable at one stage yet delivery rule is applied inconsistently; counterfactual controlled stage replacement identifies.

Do not assume multiple representations imply failure: lossy transforms alone do **not** mathematically guarantee a benign-labeled preimage of a forbidden image. Demonstrate existence empirically.

## Causal vocabulary

- A/B guard replay on the **same cached output** isolates the gate's counterfactual **coverage**, not how the gate changes generation behavior.
- A direct vs rewriter-generated pair with the same *seed* still yields different images; this estimates path effects, not isolated text-token causality.
- A stage-specific causal claim requires an intervention (replace/disable one legitimate stage) while holding the remaining policy, generator, task family and settings fixed.
- If only a toy checkpoint is insufficient, report *toy counterexample* or *safety-engineering demonstration*, not a newly discovered frontier vulnerability.
