# Mandatory novelty audit (before positive headline)

This research is **not** starting from an empty field. Existing studies cover multimodal input jailbreaks, image-editing jailbreaks, tool composition and internal generation-stage safety. The narrower candidate novelty is **stage-localized, causally supported guardrail–artifact disagreement with matched input/output semantics and benign rejection**.

## Minimum close comparators (read in full)

1. **OrchJail** — unsafe image outcomes via orchestration of individually benign steps; major risk of overlap.
2. **When the Prompt Becomes Visual / VJA** — visual-centric attacks on image editors and defense.
3. **InGuard** — inner guardrail inside generation pipeline; check if same checkpoint mechanism already studied.
4. **VALOR** — prompt moderation and rewriting for safe image generation.
5. **ConceptGuard** — compositional risk in multimodal visual generation; domain difference alone insufficient.
6. ARC, TISR, MAViQ, HACA, MAMJ, TA-SPA — prior input→language-output comparisons.

Full paper links and citations: `docs/12_REFERENCES.md`.

## Evidence table to fill (NOT pre-answered)

| Comparator | Full text reviewed? | Defended output modality | Attack/edit surface | Instrumented internal guard decision? | Guard placement at matched BRR? | Same causal controls? | Differentiator supported? |
|---|---|---|---|---|---|---|---|
| OrchJail | TODO | images | orchestration | TODO | TODO | TODO | TODO |
| VJA | TODO | images | visual editing | TODO | TODO | TODO | TODO |
| InGuard | TODO | images | denoising guard | TODO | TODO | TODO | TODO |
| VALOR | TODO | images | rewriting | TODO | TODO | TODO | TODO |
| ConceptGuard | TODO | video | multimodal input | TODO | TODO | TODO | TODO |

## Claim policy

If an earlier study has already isolated an equivalent failure through the same guarded intermediate representation and downstream image-output comparison, **do not rename it and call it novel**. Instead: narrow to a new boundary, a causal decomposition, independent benchmark or strong negative replication. Complete comparison with page/section citations, not paper-title impressions.

## Audit questions

- Does a result survive a competent **joint image-text** guard? If not, ordinary screening weakness.
- Is the alleged mismatch a rewrite-introduced change in meaning? If yes, label *semantic drift*.
- Does a guard intentionally lack needed inputs? If yes, report missing-observability baseline, not an emergent bug.
- Is the observed failure present only in toy constructed logic? Then no real-world system vulnerability claim.
- Is the effect new *in mechanism*, not merely better attack success at more compute?
