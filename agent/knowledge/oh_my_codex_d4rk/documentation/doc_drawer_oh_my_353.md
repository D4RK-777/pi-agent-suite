ract is about **how OMX prompts should behave**.
It is not the same thing as OMX's routing metadata.

- **Behavioral contract:** compact output defaults, automatic follow-through, localized task updates, persistent tool use, and evidence-backed completion.
- **Adjacent but separate routing layer:** role/tier/posture metadata such as `frontier-orchestrator`, `deep-worker`, and `fast-lane` in `src/agents/native-config.ts` and `docs/shared/agent-tiers.md`.

If you are changing prompt prose, use this document first.
If you are changing routing metadata or native config overlays, use the routing docs/tests first.

## The 4 core GPT-5.4 patterns OMX currently enforces

### 1. Compact, information-dense output by default