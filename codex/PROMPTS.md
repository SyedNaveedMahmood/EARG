# Copy-ready prompts for sequential Codex implementation

## Prompt A — repository audit and CPU E0

"Read AGENTS.md and PROPOSAL_12GB.md and the T00 contract. Audit the supplied CPU code for the frozen canary rule, check counts/hashes, run every test, and correct implementation bugs without changing the scientific definition. Run the CPU E0 generator, report exact counts and failures, create the first decision-log entry. Do not download weights or run CUDA."

## Prompt B — GPU discovery / H0 approval request

"Implement only T01: use the included non-invasive hardware probe and inspect available CUDA. Propose, but do not execute, an exact dependency/model acquisition plan based on this machine. Define independent subprocess interfaces, a VRAM logger and failure manifest. Do not download weights or generate images. Ask approval only for the next precise prerequisite."

## Prompt C — H0 workers (after approval)

"Implement T02 with SD1.5 T2I + inpainting at 512×512 FP16, batch 1; build standalone worker processes and independent logging. Restrict to six benign T2I and six benign inpainting operations. Record model weight revisions, peak observed GPU GiB, allocated/reserved CUDA GiB, seeds, scheduler, latency and image SHA. Run mocked CPU tests. Do not start E1 until explicit H0 acceptance."

## Prompt D — E1 dry run / cached replay

"Implement T03+T04 **without a GPU batch**: generate exactly 288 E1 immutable trial schedules, prospective pre/mid guard interfaces and offline shadow replay A–E with strict artifact reuse. Test on CPU fixtures, calculate GVP/DVR/BRR correctly, cluster by family, and reject ambiguous/missing labels. Do not claim a real image-producing failure from a toy case. Report which data files and approvals are still needed before E1 execution."

## Prompt E — mechanism and independent review

"After operator-approved E1 and independent artifact annotation, implement E3's frozen 12-case selection and 36 incremental faithful-rewrite operations. Compare the direct/system/faithful routes using matched generator settings and comprehensive semantic-fidelity judgments. Enumerate competing explanations before naming any failure a vulnerability."
