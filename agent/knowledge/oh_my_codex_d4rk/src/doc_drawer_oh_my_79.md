act['sandbox']['evaluator'];
  keep_policy: AutoresearchKeepPolicy;
  status: AutoresearchRunStatus;
  stop_reason: string | null;
  iteration: number;
  created_at: string;
  updated_at: string;
  completed_at: string | null;
}

interface AutoresearchActiveRunState {
  schema_version: 1;
  active: boolean;
  run_id: string | null;
  mission_slug: string | null;
  repo_root: string;
  worktree_path: string | null;
  status: AutoresearchRunStatus | 'idle';
  updated_at: string;
  completed_at?: string;
}

interface AutoresearchDecision {
  decision: AutoresearchDecisionStatus;
  decisionReason: string;
  keep: boolean;
  evaluator: AutoresearchEvaluationRecord | null;
  notes: string[];
}