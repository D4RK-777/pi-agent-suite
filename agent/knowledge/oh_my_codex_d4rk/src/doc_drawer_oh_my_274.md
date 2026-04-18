tsInitOptions {
  dryRun?: boolean;
  force?: boolean;
  verbose?: boolean;
  targetPath?: string;
}

interface AgentsInitSummary {
  updated: number;
  unchanged: number;
  skipped: number;
  backedUp: number;
}

interface ManagedFileDecision {
  action: "updated" | "unchanged" | "skipped";
  reason?: string;
  backedUp: boolean;
}

interface DirectorySnapshot {
  files: string[];
  directories: string[];
}

function createEmptySummary(): AgentsInitSummary {
  return {
    updated: 0,
    unchanged: 0,
    skipped: 0,
    backedUp: 0,
  };
}

function isManagedAgentsInitFile(content: string): boolean {
  return content.includes(MANAGED_MARKER);
}