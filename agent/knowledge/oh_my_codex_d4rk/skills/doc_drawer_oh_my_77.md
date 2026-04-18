ostgreSQL"
4. Let it run -- avoid interrupting unless truly needed

## Pipeline Orchestrator (v0.8+)

Autopilot can be driven by the configurable pipeline orchestrator (`src/pipeline/`), which
sequences stages through a uniform `PipelineStage` interface:

```
RALPLAN (consensus planning) -> team-exec (Codex CLI workers) -> ralph-verify (architect verification)
```

Pipeline configuration options:

```toml
[omx.autopilot.pipeline]
maxRalphIterations = 10    # Ralph verification iteration ceiling
workerCount = 2            # Number of Codex CLI team workers
agentType = "executor"     # Agent type for team workers
```

The pipeline persists state via `pipeline-state.json` and supports resume from the last
incomplete stage. See `src/pipeline/orchestrator.ts` for the full API.