number;
  exit_code?: number | null;
  stdout?: string;
  stderr?: string;
  parse_error?: string;
}

export interface AutoresearchCandidateArtifact {
  status: AutoresearchCandidateStatus;
  candidate_commit: string | null;
  base_commit: string;
  description: string;
  notes: string[];
  created_at: string;
}

export interface AutoresearchLedgerEntry {
  iteration: number;
  kind: 'baseline' | 'iteration';
  decision: AutoresearchDecisionStatus;
  decision_reason: string;
  candidate_status: AutoresearchCandidateStatus | 'baseline';
  base_commit: string;
  candidate_commit: string | null;
  kept_commit: string;
  keep_policy: AutoresearchKeepPolicy;
  evaluator: AutoresearchEvaluationRecord | null;
  created_at: string;
  notes: string[];
  description: string;
}