nore' });
  execFileSync('git', ['commit', '-m', 'init'], { cwd, stdio: 'ignore' });
  return cwd;
}

async function makeContract(repo: string): Promise<AutoresearchMissionContract> {
  const missionDir = join(repo, 'missions', 'demo');
  await mkdir(missionDir, { recursive: true });
  await mkdir(join(repo, 'scripts'), { recursive: true });
  const missionFile = join(missionDir, 'mission.md');
  const sandboxFile = join(missionDir, 'sandbox.md');
  const missionContent = '# Mission\nSolve the task.\n';
  const sandboxContent = `---\nevaluator:\n  command: node scripts/eval.js\n  format: json\n---\nStay inside the mission boundary.\n`;
  await writeFile(missionFile, missionContent, 'utf-8');
  await writeFile(sandboxFile, sandboxContent, 'utf-8');