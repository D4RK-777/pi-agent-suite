rt missing evidence and incomplete work honestly.",
  "",
  "</exact_model_guidance>",
].join("\n");

export interface GeneratedNativeAgentConfig {
  name: string;
  description: string;
  developerInstructions?: string;
  model?: string;
  reasoningEffort?: "low" | "medium" | "high" | "xhigh";
}

interface AgentModelResolutionOptions {
  codexHomeOverride?: string;
  configTomlContent?: string;
  env?: NodeJS.ProcessEnv;
}

interface RoleInstructionMetadata {
  name: string;
  posture: AgentDefinition["posture"];
  modelClass: AgentDefinition["modelClass"];
  routingRole: AgentDefinition["routingRole"];
}