createRalplanStage,
  createTeamExecStage,
  createRalphVerifyStage,
} from './pipeline/index.js';

const config = createAutopilotPipelineConfig('build feature X', {
  stages: [
    createRalplanStage(),
    createTeamExecStage({ workerCount: 3, agentType: 'executor' }),
    createRalphVerifyStage({ maxIterations: 15 }),
  ],
});

const result = await runPipeline(config);
```

## Relationship to Other Modes

- **autopilot**: Autopilot can use pipeline as its execution engine (v0.8+)
- **team**: Pipeline delegates execution to team mode (Codex CLI workers)
- **ralph**: Pipeline delegates verification to ralph (configurable iterations)
- **ralplan**: Pipeline's first stage runs RALPLAN consensus planning