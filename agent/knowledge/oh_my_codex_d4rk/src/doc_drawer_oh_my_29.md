ure"];
  modelClass: AgentDefinition["modelClass"];
  routingRole: AgentDefinition["routingRole"];
}

function readConfigTomlContent(
  codexHomeOverride?: string,
  provided?: string,
): string {
  if (typeof provided === "string") return provided;
  const configPath = join(codexHomeOverride ?? process.env.CODEX_HOME ?? "", "config.toml");
  if (codexHomeOverride && existsSync(configPath)) {
    return readFileSync(configPath, "utf-8");
  }
  return "";
}

function resolveFrontierModel(options: AgentModelResolutionOptions): string {
  const configTomlContent = readConfigTomlContent(
    options.codexHomeOverride,
    options.configTomlContent,
  );
  return getRootModelName(configTomlContent)
    ?? getMainDefaultModel(options.codexHomeOverride);
}