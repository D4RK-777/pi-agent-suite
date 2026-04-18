escapeTomlBasicString(s: string): string {
  return s.replace(/\\/g, "\\\\").replace(/"/g, '\\"');
}

export function generateStandaloneAgentToml(
  config: GeneratedNativeAgentConfig,
): string {
  const lines = [
    `# oh-my-codex agent: ${config.name}`,
    `name = "${escapeTomlBasicString(config.name)}"`,
    `description = "${escapeTomlBasicString(config.description)}"`,
  ];

  if (config.model) {
    lines.push(`model = "${escapeTomlBasicString(config.model)}"`);
  }
  if (config.reasoningEffort) {
    lines.push(`model_reasoning_effort = "${config.reasoningEffort}"`);
  }
  if (
    typeof config.developerInstructions === "string" &&
    config.developerInstructions.trim().length > 0
  ) {
    const escapedInstructions = escapeTomlMultiline(
      config.developerInstructions,