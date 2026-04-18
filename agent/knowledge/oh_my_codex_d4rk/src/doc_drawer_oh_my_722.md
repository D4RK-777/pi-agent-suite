opeFilePath(projectRoot: string): string {
  return join(projectRoot, ".omx", "setup-scope.json");
}

export function resolveScopeDirectories(
  scope: SetupScope,
  projectRoot: string,
): ScopeDirectories {
  if (scope === "project") {
    const codexHomeDir = join(projectRoot, ".codex");
    return {
      codexConfigFile: join(codexHomeDir, "config.toml"),
      codexHomeDir,
      nativeAgentsDir: join(codexHomeDir, "agents"),
      promptsDir: join(codexHomeDir, "prompts"),
      skillsDir: join(codexHomeDir, "skills"),
    };
  }
  return {
    codexConfigFile: codexConfigPath(),
    codexHomeDir: codexHome(),
    nativeAgentsDir: codexAgentsDir(),
    promptsDir: codexPromptsDir(),
    skillsDir: userSkillsDir(),
  };
}