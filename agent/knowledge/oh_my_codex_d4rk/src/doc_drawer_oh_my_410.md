interface CleanupCandidate extends ProcessEntry {
  reason: 'ppid=1' | 'outside-current-session';
}

export interface CleanupResult {
  dryRun: boolean;
  candidates: CleanupCandidate[];
  terminatedCount: number;
  forceKilledCount: number;
  failedPids: number[];
}

export interface CleanupDependencies {
  currentPid?: number;
  listProcesses?: () => ProcessEntry[];
  isPidAlive?: (pid: number) => boolean;
  sendSignal?: (pid: number, signal: NodeJS.Signals) => void;
  sleep?: (ms: number) => Promise<void>;
  now?: () => number;
  writeLine?: (line: string) => void;
}

interface TmpDirectoryEntry {
  name: string;
  isDirectory(): boolean;
}