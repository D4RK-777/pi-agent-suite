{
    pass: result.pass,
    ...(result.score === undefined ? {} : { score: result.score }),
  };
}

export async function loadAutoresearchMissionContract(missionDirArg: string): Promise<AutoresearchMissionContract> {
  const missionDir = resolve(missionDirArg);
  if (!existsSync(missionDir)) {
    throw contractError(`mission-dir does not exist: ${missionDir}`);
  }

  const repoRoot = readGit(missionDir, ['rev-parse', '--show-toplevel']);
  ensurePathInside(repoRoot, missionDir);