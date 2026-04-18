return getRootModelName(configTomlContent)
    ?? getMainDefaultModel(options.codexHomeOverride);
}

function resolveStandardModel(options: AgentModelResolutionOptions): string {
  const explicitStandardModel = getEnvConfiguredStandardDefaultModel(
    options.env ?? process.env,
    options.codexHomeOverride,
  );

  if (explicitStandardModel) return explicitStandardModel;
  return getStandardDefaultModel(options.codexHomeOverride);
}

function resolveAgentModel(
  agent: AgentDefinition,
  options: AgentModelResolutionOptions = {},
): string {
  if (agent.name === "executor") {
    return resolveFrontierModel(options);
  }