# E5 — Deferred held-out model replication

Freeze mechanism, judge, thresholds and eligible cases **before** opening holdout. Use 20 new families × 2 frozen prompt paths × 2 seeds = **80 additional images**, with a second checkpoint that independently passes H0 under 12 GB. Do not confuse another SD1.5 checkpoint/scheduler with a genuinely independent architecture.

Evidence hierarchy: second checkpoint = limited transfer; second model family + held-out task families + independent output judges = stronger external validity. Use pilot task-family variance to plan confirmatory sample size. Do not treat 20 families as automatically powered confirmation or retune on holdout.
