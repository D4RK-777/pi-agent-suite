(line: string) => void;
}

interface TmpDirectoryEntry {
  name: string;
  isDirectory(): boolean;
}

export interface TmpCleanupDependencies {
  tmpRoot?: string;
  listTmpEntries?: (tmpRoot: string) => Promise<TmpDirectoryEntry[]>;
  statPath?: (path: string) => Promise<{ mtimeMs: number }>;
  removePath?: (path: string) => Promise<void>;
  now?: () => number;
  writeLine?: (line: string) => void;
}

export interface CleanupCommandDependencies {
  cleanupProcesses?: (args: readonly string[]) => Promise<CleanupResult>;
  cleanupTmpDirectories?: (args: readonly string[]) => Promise<number>;
}

function normalizeCommand(command: string): string {
  return command.replace(/\\+/g, '/').trim();
}