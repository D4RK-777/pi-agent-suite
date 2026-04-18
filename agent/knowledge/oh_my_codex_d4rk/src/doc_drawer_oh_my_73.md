t = readGit(missionDir, ['rev-parse', '--show-toplevel']);
  ensurePathInside(repoRoot, missionDir);

  const missionFile = join(missionDir, 'mission.md');
  const sandboxFile = join(missionDir, 'sandbox.md');
  if (!existsSync(missionFile)) {
    throw contractError(`mission.md is required inside mission-dir: ${missionFile}`);
  }
  if (!existsSync(sandboxFile)) {
    throw contractError(`sandbox.md is required inside mission-dir: ${sandboxFile}`);
  }

  const missionContent = await readFile(missionFile, 'utf-8');
  const sandboxContent = await readFile(sandboxFile, 'utf-8');
  const sandbox = parseSandboxContract(sandboxContent);
  const missionRelativeDir = relative(repoRoot, missionDir) || basename(missionDir);
  const missionSlug = slugifyMissionName(missionRelativeDir);