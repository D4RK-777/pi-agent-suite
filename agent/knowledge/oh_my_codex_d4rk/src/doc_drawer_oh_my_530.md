upScope(cwd: string): SetupScope | undefined {
  return readPersistedSetupPreferences(cwd)?.scope;
}

export function readPersistedSetupPreferences(
  cwd: string,
): Partial<{ scope: SetupScope }> | undefined {
  const scopePath = join(cwd, ".omx", "setup-scope.json");
  if (!existsSync(scopePath)) return undefined;
  try {
    const parsed = JSON.parse(readFileSync(scopePath, "utf-8")) as Partial<{
      scope: string;
    }>;
    const persisted: Partial<{ scope: SetupScope }> = {};
    if (typeof parsed.scope === "string") {
      if (SETUP_SCOPES.includes(parsed.scope as SetupScope)) {
        persisted.scope = parsed.scope as SetupScope;
      }
      const migrated = LEGACY_SCOPE_MIGRATION_SYNC[parsed.scope];
      if (migrated) persisted.scope = migrated;
    }