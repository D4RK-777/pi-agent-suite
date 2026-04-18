codexAgentsDir } from "../utils/paths.js";

export const EXACT_GPT_5_4_MINI_MODEL = "gpt-5.4-mini";

const POSTURE_OVERLAYS: Record<AgentDefinition["posture"], string> = {
  "frontier-orchestrator": [
    "<posture_overlay>",
    "",
    "You are operating in the frontier-orchestrator posture.",
    "- Prioritize intent classification before implementation.",
    "- Default to delegation and orchestration when specialists exist.",
    "- Treat the first decision as a routing problem: research vs planning vs implementation vs verification.",
    "- Challenge flawed user assumptions concisely before execution when the design is likely to cause avoidable problems.",