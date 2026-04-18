# Runtime Model Metadata Cleanup

## Why

Benchmark runs showed spawned child agents being labeled with legacy model aliases such as `sonnet`, even when OMX was launched under Codex with GPT-5.x reasoning settings.

The prompt/skill layer was already sanitized, but runtime metadata still used historical aliases in `src/agents/definitions.ts`. Those aliases were also used when generating native agent configs, which made legacy labels leak into spawned-agent UX and benchmark output.

## What changed

### 1. Agent runtime metadata
- Replaced `model: haiku|sonnet|opus` with `reasoningEffort: low|medium|high` in `src/agents/definitions.ts`.
- Kept posture and model-class concepts intact.