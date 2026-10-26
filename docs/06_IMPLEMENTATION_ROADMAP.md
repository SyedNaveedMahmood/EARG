# Milestone / dependency roadmap

**Principle:** Scientific approval gates govern progression; code completion alone is not approval.

| Milestone | Engineering deliverable | Tests | Human decision |
|---|---|---|---|
| M0: package verification | docs/schema checks, CPU E0 scaffold | `pytest`, package check, freeze policy | Approve definitions |
| M1: model preflight | platform probe, non-network H0 loader plan | no GPU code executed yet | Approve downloads + dependency lock |
| M2: H0 | SD1.5 generator/inpaint isolated workers + memory logger | 12 smoke operations + visuals + logs | GPU fit and canary renderability |
| M3: E1 | family builder, rewriter, pre/mid gates, generator, immutable cache | exact 288 schedule + integration tests | Approve pilot batch |
| M4: shadow gating | 5 policy placements offline on cached E1 image | identical artifact digest across B/C/D/E | Approve measured contrasts |
| M5: E3 | frozen-selection rule + faithful restatement route | exactly 36 additional outputs + semantic adjudication | Causal-claim check |
| M6: E2 | 2×2 inpainting protocol | 144 outputs + unexecuted pair judgments | Optional promotion |
| M7: reporting | family-clustered CIs, uncertainty bounds, tables/figures | recalculation from saved manifests | Decide negative/positive claim |
| M8: E4/E5 | sequence controls and second H0-approved generator | held-out isolation | Optional later work |

## Definition of done for each milestone

1. Source diff reviewed and a git commit exists.
2. All relevant tests genuinely pass and log exact commands.
3. Measured artifacts exist and count matches protocol (or failures are transparently logged).
4. Config/policy/prompt hashes are written and no holdout leakage occurred.
5. An operator has explicitly approved any large batch or new model acquisition.
6. Decision log records promotion or stop, with responsible reviewer and rationale.

## Suggested small-agent structure

- **Lead/Integrator:** owns AGENTS, interfaces, merges, go/no-go and scientific audit.
- **Data/Evaluator agent:** scene graph, labeled datasets, visual-policy oracle, blinded annotator protocol.
- **GPU pipeline agent:** isolated model workers, H0, logging; **only single GPU worker at a time**.
- **Analysis/QA agent:** schemas, invariants, paired statistics, data audits; no exclusive GPU need.

Do not delegate simultaneous changes to shared schema/experiment config without strict interface approval. Split tasks by file boundaries, not by ambiguous research questions.
