`.
The HUD renders pipeline phase automatically. Resume is supported from the last incomplete stage.

- **On start**: `state_write({mode: "pipeline", active: true, current_phase: "stage:ralplan"})`
- **On stage transitions**: `state_write({mode: "pipeline", current_phase: "stage:<name>"})`
- **On completion**: `state_write({mode: "pipeline", active: false, current_phase: "complete"})`

## API

```typescript
import {
  runPipeline,
  createAutopilotPipelineConfig,
  createRalplanStage,
  createTeamExecStage,
  createRalphVerifyStage,
} from './pipeline/index.js';