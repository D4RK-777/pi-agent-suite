notes: ['candidate discarded because evaluator score was not better than the kept baseline'],
  };
}

export function buildAutoresearchInstructions(
  contract: AutoresearchMissionContract,
  context: {
    runId: string;
    iteration: number;
    baselineCommit: string;
    lastKeptCommit: string;
    lastKeptScore?: number | null;
    resultsFile: string;
    candidateFile: string;
    keepPolicy: AutoresearchKeepPolicy;
    previousIterationOutcome?: string | null;
    recentLedgerSummary?: AutoresearchInstructionLedgerSummary[];
  },
): string {
  return [
    '# OMX Autoresearch Supervisor Instructions',
    '',
    `Run ID: ${context.runId}`,
    `Mission directory: ${contract.missionDir}`,
    `Mission file: ${contract.missionFile}`,
    `Sandbox file: ${contract.sandboxFile}`,