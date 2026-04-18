rt: low|medium|high` in `src/agents/definitions.ts`.
- Kept posture and model-class concepts intact.

### 2. Native agent config generation
- Updated `src/agents/native-config.ts` to derive `model_reasoning_effort` directly from `agent.reasoningEffort`.
- Removed the legacy alias translation table.

### 3. Tests
- Updated `src/agents/__tests__/definitions.test.ts` and `src/agents/__tests__/native-config.test.ts` to match the new runtime metadata shape.
- Existing prompt/skill sanitization test remains as a guard against old aliases reappearing in prompt content.

### 4. Supporting cleanup
- Updated `src/verification/verifier.ts` comment wording from legacy alias names to low/medium/high reasoning wording.

## Expected effect