toresearchEvaluationRecord | null;
  created_at: string;
  notes: string[];
  description: string;
}

export interface AutoresearchRunManifest {
  schema_version: 1;
  run_id: string;
  run_tag: string;
  mission_dir: string;
  mission_file: string;
  sandbox_file: string;
  repo_root: string;
  worktree_path: string;
  mission_slug: string;
  branch_name: string;
  baseline_commit: string;
  last_kept_commit: string;
  last_kept_score: number | null;
  latest_candidate_commit: string | null;
  results_file: string;
  instructions_file: string;
  manifest_file: string;
  ledger_file: string;
  latest_evaluator_file: string;
  candidate_file: string;
  evaluator: AutoresearchMissionContract['sandbox']['evaluator'];
  keep_policy: AutoresearchKeepPolicy;
  status: AutoresearchRunStatus;