son: string;
  keep: boolean;
  evaluator: AutoresearchEvaluationRecord | null;
  notes: string[];
}

interface AutoresearchInstructionLedgerSummary {
  iteration: number;
  decision: AutoresearchDecisionStatus;
  reason: string;
  kept_commit: string;
  candidate_commit: string | null;
  evaluator_status: AutoresearchEvaluationRecord['status'] | null;
  evaluator_score: number | null;
  description: string;
}

const AUTORESEARCH_RESULTS_HEADER = 'iteration\tcommit\tpass\tscore\tstatus\tdescription\n';
const AUTORESEARCH_WORKTREE_EXCLUDES = ['results.tsv', 'run.log', 'node_modules', '.omx/'];

function nowIso(): string {
  return new Date().toISOString();
}