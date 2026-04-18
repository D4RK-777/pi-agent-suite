el) {
    if (metadataLines.length === 0) {
      metadataLines.push("## OMX Agent Metadata");
    }
    metadataLines.push(`- resolved_model: ${resolvedModel}`);
  }
  if (metadataLines.length > 0) {
    parts.push("", ...metadataLines);
  }

  return parts.join("\n");
}

export function composeRoleInstructionsForRole(
  roleName: string,
  promptContent: string,
  resolvedModel?: string,
): string {
  const agent = AGENT_DEFINITIONS[roleName];
  return composeRoleInstructions(
    promptContent,
    agent
      ? {
          name: agent.name,
          posture: agent.posture,
          modelClass: agent.modelClass,
          routingRole: agent.routingRole,
        }
      : null,
    resolvedModel,
  );
}