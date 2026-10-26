# Paper outline (not results)

## Working title

**Where Safety Gets Lost: A Causal Audit of Representation-to-Artifact Enforcement in Multimodal Image Generation**

## Manuscript plan

1. **Introduction:** output-side enforcement risk; exact difference from ARC/TISR and OrchJail/VJA; bounded hypothesis.
2. **Related work:** input-to-text multimodal jailbreaks; image-editing attacks; T2I orchestration; prompt rewriting/guard placement; representation-level defenses.
3. **Threat model:** fixed policy, input, rewriter, intermediate prompt, generator/editor, guards, actual delivery versus replay.
4. **Methods:** canary policy, calibration, guard checkpoints, matched paths, fidelity auditing, independent artifact adjudication.
5. **Research questions:** RQ1–RQ5; H6 optional.
6. **Results:** only verified outcomes — artifact prevalence, DVR/BRR, B/C/D contrasts, fidelity and judge uncertainty, E2 interaction if promoted.
7. **Causal mechanism:** checkpoint swap and rival-explanation eliminations (only if supported).
8. **Replication and limitations:** 12 GB generator limitations, toy external validity, model/architecture transfer, relevant negative results.
9. **Ethics/disclosure:** sanitized visual policy and deployment boundaries.

## Essential figures (to create after experiments)

- Figure 1: pipeline checkpoints and observable representation flow (no results).
- Figure 2: exact canary rule and calibrated near-miss examples.
- Figure 3: DVR versus BRR under A–E guards (only if measured).
- Figure 4: controlled direct / independent-faithful / system rewrite comparisons.
- Figure 5: schematic of supported mechanism *or* most informative negative result.

## Abstract shell

"We investigate whether safety judgments made on intermediate representations of multimodal image-generation pipelines predict the policy status of their delivered images. We introduce [exact evaluated system], [frozen controlled policy], and a stage-aware audit that distinguishes [recognition], [rewrite fidelity], [generation], and [delivery]. Across [measured scope], we find [observed empirical result]. Controlled interventions show [evidence], with [uncertainty/limits]. The study contributes [verified insight]."

**Never fill placeholders by guessing.** Use `docs/14_RESULTS_REPORT_TEMPLATE.md` after experiment evidence exists.
