160)}`
      : null,
    recentLedgerSummary: formatAutoresearchInstructionSummary(entries),
  };
}

export async function runAutoresearchEvaluator(
  contract: AutoresearchMissionContract,
  worktreePath: string,
  ledgerFile?: string,
  latestEvaluatorFile?: string,
): Promise<AutoresearchEvaluationRecord> {
  const ran_at = nowIso();
  const result = spawnSync(contract.sandbox.evaluator.command, {
    cwd: worktreePath,
    encoding: 'utf-8',
    shell: true,
    maxBuffer: 1024 * 1024,
      windowsHide: true,
    });
  const stdout = result.stdout?.trim() || '';
  const stderr = result.stderr?.trim() || '';