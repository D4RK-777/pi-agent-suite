evaluator: evaluation,
    created_at: nowIso(),
    notes: ['baseline row is always recorded'],
    description: 'initial baseline evaluation',
  });
  manifest.last_kept_score = evaluation.pass && typeof evaluation.score === 'number' ? evaluation.score : null;
  await writeRunManifest(manifest);
  await writeInstructionsFile(contract, manifest);
  return evaluation;
}

export async function prepareAutoresearchRuntime(
  contract: AutoresearchMissionContract,
  projectRoot: string,
  worktreePath: string,
  options: { runTag?: string } = {},
): Promise<PreparedAutoresearchRuntime> {
  await assertAutoresearchLockAvailable(projectRoot);
  await ensureRuntimeExcludes(worktreePath);
  await ensureAutoresearchWorktreeDependencies(projectRoot, worktreePath);