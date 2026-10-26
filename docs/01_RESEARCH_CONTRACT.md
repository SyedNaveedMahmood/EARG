# Research contract: questions, hypotheses, interpretations

**Canonical source:** `PROPOSAL_12GB.md`, §§1–4 and 8. This file is an operational index, not a replacement proposal.

## Precise object of study

Audit an **instrumented image-producing pipeline** `x → U(x) → g_pre → R → g_mid → G → g_out → delivery`. A study unit is a semantically specified task family with a fixed policy, matched benign control(s), one or more prompt paths, fixed generator parameters and repeated predeclared seeds.

## Research questions and falsifiable hypotheses

| ID | Question | Candidate prediction | Primary failure interpretation |
|---|---|---|---|
| RQ1/H1 | Do approved representations yield **delivered** rule-violating images? | Actual violation exceeds judge-error and benign-control prevalence in at least one fully instrumented pipeline | Otherwise it may be rendering noise or an incomplete guard |
| RQ2/H2 | Is a rewrite/plan transition causally involved? | A swap to no-rewrite or a faithful independent rewrite changes leak probability with downstream generation held fixed | Otherwise guard weakness or stochastic output |
| RQ3/H3 | Does image+edit composition produce previously unpredicted rule violation? | Cell interaction survives a competent **unexecuted-pair** evaluation and independent output judging | Otherwise a predictable pair-level harm, already known from compositional work |
| RQ4/H4 | Which checkpoint placement helps at **matched benign rejection**? | Guard stacks using final-artifact evidence may outperform early-only stacks in a restricted regime | Otherwise guard comparability invalid |
| RQ5/H5 | Is the stage-specific effect reproducible? | Held-out families and another **distinct generator architecture** support localization | Another SD1.5 checkpoint is not architecture replication |
| RQ6/H6 | Is there unexpected session-wide enforcement failure? | Only meaningful if the system **claims** a history-sensitive safety policy | A frame-only guard predictably misses a sequence rule by construction |

## Outcome labels and evidence ladder

- `positive` means final artifact **satisfies toy forbidden visual relation**; NOT real-world harm.
- `delivered` means the tested **enforcement configuration** allowed actual user-visible output. Distinguish actual delivery from `shadow_replay` delivery.
- `recognized_risk`: independent *prospective* risk assessment before delivery; do not infer from later model explanations.
- Tier 1: mathematically/symbolically possible on CPU. Tier 2: generated/edited image from open pipeline. Tier 3: controlled, causally localized checkpoint effect. Tier 4: held-out independent architecture/policy replication.

## Criteria for stopping rather than overstating

Stop the headline claim if a strong full-context guard catches all leaks at comparable false-positive cost; if rewrite semantic fidelity fails; if output judges disagree on pivotal cases; if the effect relies on deliberately absent protection; or if OrchJail/VJA/InGuard already establish the same mechanism with equivalent causal evidence.

## Scope

Primary: synthetic visual canaries and auditable local generation/editing. Excluded: executable malware in image files, software parser exploits, operational cybercrime content, arbitrary live-model attacks, unsupported claims about commercial systems.
