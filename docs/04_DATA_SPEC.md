# Data contract, provenance, and storage

## Directory layout (created by implementation, not prepopulated with results)

```
data/
  calibration/
  discovery/
  holdout/                 # read-only once frozen
outputs/<run_id>/
  manifests/               # stages, model hashes, gates, timestamps
  prompts/                 # exact original and rewrite text
  artifacts/               # immutable images
  judges/                  # blinded label sheets + adjudication
  replay/                  # OFFLINE guard decisions
  analysis/                # aggregated reproducible metrics
```

`outputs/` and downloaded weights should never be committed to Git. Store manifests, scripts, hashes and *synthetic publishable* summary tables separately in an approved release directory.

## IDs and units

`task_family_id` is the unit of statistical independence. Each `trial_id` uniquely combines family, intent, path, seed, generator, policy version, image/mask hashes and scheduler settings. Keep versioned source and output records; never overwrite a trial after an OOM.

For E2, use factor fields `reference_variant ∈ {i0,i1}`, `edit_variant ∈ {t0,t1}` and cell IDs `00`, `01`, `10`, `11`.

## Required manifest fields

See `schemas/trial.schema.json` and `templates/run_manifest.template.json`. At minimum:

- stage, run ID, trial ID, family ID, task split, UTC timestamp, git SHA, policy ID/version
- input text and its SHA256, input reference image SHA256 (if any), mask SHA256 (if any)
- planner ID/revision, rewritten prompt plus SHA, semantic fidelity adjudication
- generator/editor ID + revision, precision, scheduler, guidance, steps, resolution, fixed seed
- peak observed GPU device GiB, CUDA allocated/reserved GiB, wall time, warnings/OOM
- upstream and mid decisions **with timestamps before generation**
- saved candidate artifact SHA256 and valid/invalid/unrenderable flag
- independent final-policy label + ambiguity flag and reviewer provenance
- gate replay config and computed **shadow** delivery; actual delivery only if instrumented end-to-end

## Decision vocabularies

- `allow` / `refuse` / `abstain` for guards; `not_run` is not `allow`.
- `positive` / `negative` / `ambiguous` / `unrenderable` for image policy.
- `actual` / `shadow_replay` for controller evaluation mode.
- `observed` / `unmeasured` / `not_applicable` for derived evidence status.

Never turn a null pre-guard field into an allow vote. An upstream guard can only count as prospective if its decision log precedes the generation call.

## Data integrity

- Save SHA256 files immediately and verify after experiments.
- Preserve failed model runs and invalid outputs with reasons; don't replace failed seeds.
- Make annotation input randomized and blind to prompt path, guard condition, and research hypothesis.
- Maintain a cryptographic digest for split manifests. Record freeze hash and date in `docs/13_DECISION_LOG.md`.
- Do not place private API keys, credentials, or unapproved external image artifacts in manifests.
