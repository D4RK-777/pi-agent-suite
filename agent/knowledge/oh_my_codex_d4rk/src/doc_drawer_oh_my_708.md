ing;
  codexHomeDir: string;
  nativeAgentsDir: string;
  promptsDir: string;
  skillsDir: string;
}

interface SetupCategorySummary {
  updated: number;
  unchanged: number;
  backedUp: number;
  skipped: number;
  removed: number;
}

interface SetupRunSummary {
  prompts: SetupCategorySummary;
  skills: SetupCategorySummary;
  nativeAgents: SetupCategorySummary;
  agentsMd: SetupCategorySummary;
  config: SetupCategorySummary;
}

interface SetupBackupContext {
  backupRoot: string;
  baseRoot: string;
}

interface ManagedConfigResult {
  finalConfig: string;
  omxManagesTui: boolean;
}

interface LegacySkillOverlapNotice {
  shouldWarn: boolean;
  message: string;
}

export interface SkillFrontmatterMetadata {
  name: string;
  description: string;
}