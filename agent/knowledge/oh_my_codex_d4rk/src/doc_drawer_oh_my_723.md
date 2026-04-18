entsDir: codexAgentsDir(),
    promptsDir: codexPromptsDir(),
    skillsDir: userSkillsDir(),
  };
}

async function readPersistedSetupPreferences(
  projectRoot: string,
): Promise<Partial<PersistedSetupScope> | undefined> {
  const scopePath = getScopeFilePath(projectRoot);
  if (!existsSync(scopePath)) return undefined;
  try {
    const raw = await readFile(scopePath, "utf-8");
    const parsed = JSON.parse(raw) as Partial<PersistedSetupScope>;
    const persisted: Partial<PersistedSetupScope> = {};
    if (parsed && typeof parsed.scope === "string") {
      // Direct match to current scopes
      if (isSetupScope(parsed.scope)) {
        persisted.scope = parsed.scope;
      }
      // Migrate legacy scope values (project-local → project)