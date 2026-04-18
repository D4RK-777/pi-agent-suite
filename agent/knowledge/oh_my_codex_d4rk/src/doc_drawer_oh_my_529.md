ook",
]);

export interface ResolvedCliInvocation {
  command: CliCommand;
  launchArgs: string[];
}

/**
 * Legacy scope values that may appear in persisted setup-scope.json files.
 * Both 'project-local' (renamed) and old 'project' (minimal, removed) are
 * migrated to the current 'project' scope on read.
 */
const LEGACY_SCOPE_MIGRATION_SYNC: Record<string, SetupScope> = {
  "project-local": "project",
};

export function readPersistedSetupScope(cwd: string): SetupScope | undefined {
  return readPersistedSetupPreferences(cwd)?.scope;
}