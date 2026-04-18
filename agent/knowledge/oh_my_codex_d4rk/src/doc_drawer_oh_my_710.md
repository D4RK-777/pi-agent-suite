= [
  "if (subcommand === 'api')",
  "executeTeamApiOperation",
  "TEAM_API_OPERATIONS",
] as const;

const DEFAULT_SETUP_SCOPE: SetupScope = "user";
const LEGACY_SETUP_MODEL = "gpt-5.3-codex";
const DEFAULT_SETUP_MODEL = DEFAULT_FRONTIER_MODEL;
const OBSOLETE_NATIVE_AGENT_FIELD = ["skill", "ref"].join("_");
const TUI_OWNED_BY_CODEX_VERSION = [0, 107, 0] as const;

function createEmptyCategorySummary(): SetupCategorySummary {
  return {
    updated: 0,
    unchanged: 0,
    backedUp: 0,
    skipped: 0,
    removed: 0,
  };
}