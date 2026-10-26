# Package handoff status (as delivered)

**Completed and locally checked in the package-building container:**

- Canonical 12 GB research proposal preserved verbatim in `PROPOSAL_12GB.md`.
- Scientific protocols H0/E0/E1/E2/E3/E4/E5; research contracts, metrics, novelty/ethics guidance, Codex agent instructions and task board authored.
- CPU-only E0 deterministic shape dataset and exact scene-graph oracle implemented.
- The package builder executed its unit tests and a 500-scene CPU calibration run.

**Not done, not simulated, and not represented as completed:**

- NVIDIA CUDA/GPU H0 measurement on the user's actual 12 GB device.
- Downloading/running any VLM, SD1.5, or inpainting weights.
- E1's 288 generated images; E2's 144 edits; E3's 36 extra generations; later E4/E5.
- Human blinded ratings, prospective model-based guard decisions, formal experiment statistics, any real vulnerability finding, or proof of novelty.

**Readiness:** Implementation handoff package, **not** turnkey completed image-generation experiment pipeline. Begin at `CODEX_START_PROMPT.md`; checkpoint approvals in `AGENTS.md` and `checklists/PHASE_GATES.md`.
