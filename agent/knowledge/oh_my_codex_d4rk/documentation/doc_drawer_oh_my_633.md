concurrent-run shape:

```bash
seq 1 5 | xargs -I{} -P5 node bin/omx.js sparkshell git --version
```

**Evidence to capture**
- run count,
- any non-zero exits,
- stderr snapshots,
- whether output format/guidance drifted across runs.

**Failure signal**
- intermittent launch failures,
- inconsistent or truncated guidance text,
- different recovery messaging for the same failure mode without reason.

## Scenario 3: pseudo-fuzz summary corpora

**Why excluded from default CI**
- Corpus design is intentionally adversarial and may evolve faster than stable fixtures.
- Review requires semantic inspection against predeclared must-preserve facts.

**Goal**
- Stress `omx-explore` and `omx-sparkshell` summarization with outputs that bury signal under distractors.