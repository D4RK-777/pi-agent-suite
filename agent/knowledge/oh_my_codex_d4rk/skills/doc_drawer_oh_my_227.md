---
name: pipeline
description: Configurable pipeline orchestrator for sequencing stages
---

# Pipeline Skill

`$pipeline` is the configurable pipeline orchestrator for OMX. It sequences stages
through a uniform `PipelineStage` interface, with state persistence and resume support.

## Default Autopilot Pipeline

The canonical OMX pipeline sequences:

```
RALPLAN (consensus planning) -> team-exec (Codex CLI workers) -> ralph-verify (architect verification)
```

## Configuration

Pipeline parameters are configurable per run:

| Parameter | Default | Description |
|-----------|---------|-------------|
| `maxRalphIterations` | 10 | Ralph verification iteration ceiling |
| `workerCount` | 2 | Number of Codex CLI team workers |
| `agentType` | `executor` | Agent type for team workers |