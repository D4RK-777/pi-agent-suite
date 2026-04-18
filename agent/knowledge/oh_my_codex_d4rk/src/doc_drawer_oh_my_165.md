nore' });
  execFileSync('git', ['commit', '-m', 'init'], { cwd, stdio: 'ignore' });
  return cwd;
}

async function makeContract(repo: string, keepPolicy?: 'score_improvement' | 'pass_only'): Promise<AutoresearchMissionContract> {
  const missionDir = join(repo, 'missions', 'demo');
  await mkdir(missionDir, { recursive: true });
  await mkdir(join(repo, 'scripts'), { recursive: true });
  const missionFile = join(missionDir, 'mission.md');
  const sandboxFile = join(missionDir, 'sandbox.md');
  const missionContent = '# Mission\nSolve the task.\n';
  const keepPolicyLine = keepPolicy ? `  keep_policy: ${keepPolicy}\n` : '';
  const sandboxContent = `---\nevaluator:\n  command: node scripts/eval.js\n  format: json\n${keepPolicyLine}---\nStay inside the mission boundary.\n`;