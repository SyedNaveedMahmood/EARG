# Human approval and QA checklist

## Before M0–M1

- [ ] Read proposal and confirm toy-policy rule, population, splits and counts.
- [ ] Verify package schema/configs/tests; clean `git status`.
- [ ] Freeze canary policy version and task-family split manifest SHA.
- [ ] Confirm output folder is not tracked and no secrets are present.

## Before model downloads / H0

- [ ] Record GPU model, 12 GB capacity, driver, PyTorch/CUDA plan.
- [ ] Inspect weight licenses and gated access.
- [ ] Approve expected disk/network use and exact smoke-test limit.
- [ ] Separate subprocesses; one model on GPU at a time.

## H0 pass

- [ ] Six successful benign T2I and six inpainting operations with no OOM.
- [ ] VRAM peaks recorded, 10.5 GiB planning target observed or operator approved smaller headroom.
- [ ] Input artifact and output hashes saved.
- [ ] Canary relation demonstrably renderable and visually judgeable.

## Before E1 large run

- [ ] Exactly 288 scheduled IDs and no duplicate hashes in task specification.
- [ ] Pre/mid full-context safety checks prospective and properly timestamped.
- [ ] Rewriter semantic-fidelity measurement operational.
- [ ] Output judge plus independent human review plan operational.
- [ ] Guard comparisons on cached images implemented and tested.
- [ ] Explicit user approval to spend 288 GPU operations.

## Before paper-level vulnerability claim

- [ ] Reviewer-confirmed final policy violation in actual image-producing system.
- [ ] Strong pair-aware baseline and matched benign-refusal results.
- [ ] Controlled stage-localization intervention.
- [ ] Replication independent of selected discovery cases.
- [ ] Full-text novelty comparison with OrchJail, VJA, InGuard and VALOR.
- [ ] Appropriate disclosure and external-validity statement.
