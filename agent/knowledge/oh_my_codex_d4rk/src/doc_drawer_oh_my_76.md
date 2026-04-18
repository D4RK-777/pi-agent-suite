pted' | 'error';
export type AutoresearchRunStatus = 'running' | 'stopped' | 'completed' | 'failed';

export interface PreparedAutoresearchRuntime {
  runId: string;
  runTag: string;
  runDir: string;
  instructionsFile: string;
  manifestFile: string;
  ledgerFile: string;
  latestEvaluatorFile: string;
  resultsFile: string;
  stateFile: string;
  candidateFile: string;
  repoRoot: string;
  worktreePath: string;
  taskDescription: string;
}

export interface AutoresearchEvaluationRecord {
  command: string;
  ran_at: string;
  status: 'pass' | 'fail' | 'error';
  pass?: boolean;
  score?: number;
  exit_code?: number | null;
  stdout?: string;
  stderr?: string;
  parse_error?: string;
}