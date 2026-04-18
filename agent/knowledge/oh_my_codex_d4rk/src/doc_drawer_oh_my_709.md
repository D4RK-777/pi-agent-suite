age: string;
}

export interface SkillFrontmatterMetadata {
  name: string;
  description: string;
}

const PROJECT_OMX_GITIGNORE_ENTRY = ".omx/";

function applyScopePathRewritesToAgentsTemplate(
  content: string,
  scope: SetupScope,
): string {
  if (scope !== "project") return content;
  return content.replaceAll("~/.codex", "./.codex");
}

interface PersistedSetupScope {
  scope: SetupScope;
}

interface ResolvedSetupScope {
  scope: SetupScope;
  source: "cli" | "persisted" | "prompt" | "default";
}

const REQUIRED_TEAM_CLI_API_MARKERS = [
  "if (subcommand === 'api')",
  "executeTeamApiOperation",
  "TEAM_API_OPERATIONS",
] as const;