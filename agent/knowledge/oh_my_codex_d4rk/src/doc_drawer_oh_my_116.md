md',
    trimContent(contract.sandbox.body || contract.sandboxContent),
    '```',
  ].join('\n');
}

export async function materializeAutoresearchMissionToWorktree(
  contract: AutoresearchMissionContract,
  worktreePath: string,
): Promise<AutoresearchMissionContract> {
  const missionDir = join(worktreePath, contract.missionRelativeDir);
  const missionFile = join(missionDir, 'mission.md');
  const sandboxFile = join(missionDir, 'sandbox.md');

  await mkdir(missionDir, { recursive: true });
  await writeFile(missionFile, contract.missionContent, 'utf-8');
  await writeFile(sandboxFile, contract.sandboxContent, 'utf-8');