# Ethics, disclosure and safe experiment policy

## Research purpose

Study alignment between declared visual-policy checkpoints and final artifacts, using **abstract shape canaries**. The pilot may use the word "forbidden" only for a synthetic rule; it does **not** create dangerous or malware-bearing images.

## Permitted initial experiments

- Deterministic abstract shape scenes and masks.
- Local, license-compliant generative and editing models on benign synthetic requests.
- Independent policy-review experiments with anonymized/neutral artifacts.
- CPU-reproducible symbolic counterexamples, guard-placement comparisons, and error analysis.

## Out of scope

- Embedding payloads or executables in image files; operational malware instructions; real-world abusive image generation; targeted live attacks on third-party systems; publishing usable bypass recipes; acquiring unauthorized user content.

## Controls

- Study designs must be approved before expanding beyond benign synthetic policy.
- Hosted model evaluations only with explicit access and compliant rates/terms.
- Never confuse synthetic canary violation with real-world content harm or a model-provider policy breach.
- Disclose suspected real vulnerabilities responsibly, with the smallest necessary sanitized reproducer; keep potentially harmful artifacts restricted.
- Record exactly what is public: code, configs, model hashes, sanitized synthetic artifacts, quantitative tables, reviewer guidelines. Restrict anything unsafe or third-party proprietary.

## Reviewer-facing disclosure text (template, fill after running)

"Our initial evaluation uses neutral shape-based policies to isolate representation-to-artifact enforcement effects. These are controlled proxy tasks; we make no claim that a synthetic-rule violation implies real-world harmful image generation. Stronger external validity claims require independent, policy-compliant validation."
