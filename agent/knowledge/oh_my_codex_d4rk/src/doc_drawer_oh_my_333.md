or(result.compileTarget.evaluatorCommand);
  return initAutoresearchMission(result.compileTarget);
}

export async function initAutoresearchMission(opts: InitAutoresearchOptions): Promise<InitAutoresearchResult> {
  const missionsRoot = join(opts.repoRoot, 'missions');
  const missionDir = join(missionsRoot, opts.slug);

  const rel = relative(missionsRoot, missionDir);
  if (!rel || rel.startsWith('..') || resolve(rel) === resolve(missionDir)) {
    throw new Error('Invalid slug: resolves outside missions/ directory.');
  }

  if (existsSync(missionDir)) {
    throw new Error(`Mission directory already exists: ${missionDir}`);
  }

  await mkdir(missionDir, { recursive: true });