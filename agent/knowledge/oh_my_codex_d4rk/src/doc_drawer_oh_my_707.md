del: string,
    targetModel: string,
  ) => Promise<boolean>;
  mcpRegistryCandidates?: string[];
}

/**
 * Legacy scope values that may appear in persisted setup-scope.json files.
 * Both 'project-local' (renamed) and old 'project' (minimal, removed) are
 * migrated to the current 'project' scope on read.
 */
const LEGACY_SCOPE_MIGRATION: Record<string, "project"> = {
  "project-local": "project",
};

export const SETUP_SCOPES = ["user", "project"] as const;
export type SetupScope = (typeof SETUP_SCOPES)[number];

export interface ScopeDirectories {
  codexConfigFile: string;
  codexHomeDir: string;
  nativeAgentsDir: string;
  promptsDir: string;
  skillsDir: string;
}