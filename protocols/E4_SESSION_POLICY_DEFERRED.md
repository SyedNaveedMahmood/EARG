# E4 — Session-wide policy (deferred / CPU-first)

Define a *new*, explicit session policy for **four images whose sequence order matters**, completely separate from E1/E2 per-frame policy. Create 16 symbolic sequences and compare target order, reverse/permuted order and matched random order = **48 CPU sequence evaluations**, zero diffusion inference.

A frame-only gate predictably cannot detect a violation defined only over a sequence. This is a design control, **not a vulnerability discovery**. Only test a real system if it explicitly promises session-level enforcement and after the E1/E3 evidence supports extending the study. Pre-register the history-aware baseline and never conflate a session-policy failure with a frame-policy failure.
