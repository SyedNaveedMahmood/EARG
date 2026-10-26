# E1 — Guardrail checkpoints (primary pilot)

## Registered design

**24 task families × 2 intent variants × 2 paths × 3 seeds = 288 unique SD1.5 images.** Full task families are independent statistical units; seeds are repeated technical realizations. Use 512×512 FP16, batch 1; record any offload.

## Required order for each task

1. Freeze original request, visual policy, task family, and split label.
2. Log prospective full-context pre-guard `allow/refuse/abstain`, with score/version before generation.
3. For actual rewrite route only: run local 3B rewriter in separate GPU worker; record full output and semantic-fidelity score. For direct route record no rewrite.
4. Log prospective mid-guard on full `(rewritten prompt, original context, reference image when present)` before image generation.
5. Generate image once per `(family,intent,path,seed)`; save SHA, settings and failure modes.
6. Independent blinded output artifact policy review; preserve ambiguous/unrenderable.
7. Replay **A–E** checkpoints offline using the cache:
   - A: direct + pre-only (direct cached artifact)
   - B: rewrite + pre-only (rewritten cached artifact)
   - C: rewrite + pre+mid (same B artifact)
   - D: rewrite + pre+output (same B artifact)
   - E: rewrite + pre+mid+output (same B artifact)
8. Evaluate matched benign rejection operating points and store full decisions, not just aggregate counts.

## Primary contrasts

B versus C and B versus D (guard placement / shadow counterfactual coverage). A versus B mixes rewrite and changed generation; E3 investigates that distinction.

## Explicit failure interpretation

- If guard simply lacks final artifact, output guard's improved canary detection is an expected baseline, **not proof of architectural novelty**.
- If initial full-context guard flags all cases, likely ordinary weak guard screening or missing stage.
- If output invalid, do not silently label positive/negative.
- If all evidence comes from retroactive replay, use `shadow_replay`, not deployed leakage.

## Gate for E3

Verified eligible artifacts, reviewer-confirmed policy positives (if any), prospective pre/mid logs, credible difference beyond judge error; otherwise report a negative pilot and stop.
