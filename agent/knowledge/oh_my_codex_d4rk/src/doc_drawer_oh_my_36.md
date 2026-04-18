h > 0
  ) {
    const escapedInstructions = escapeTomlMultiline(
      config.developerInstructions,
    );
    lines.push('developer_instructions = """', escapedInstructions, '"""');
  }

  lines.push("");
  return lines.join("\n");
}

/**
 * Generate TOML content for a prompt-backed OMX role agent.
 */
export function generateAgentToml(
  agent: AgentDefinition,
  promptContent: string,
  options: AgentModelResolutionOptions = {},
): string {
  const resolvedModel = resolveAgentModel(agent, options);
  return generateStandaloneAgentToml({
    name: agent.name,
    description: agent.description,
    developerInstructions: composeRoleInstructions(promptContent, agent, resolvedModel),
    model: resolvedModel,
    reasoningEffort: agent.reasoningEffort,
  });
}