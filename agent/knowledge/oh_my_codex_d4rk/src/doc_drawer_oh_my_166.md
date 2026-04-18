d: node scripts/eval.js\n  format: json\n${keepPolicyLine}---\nStay inside the mission boundary.\n`;
  await writeFile(missionFile, missionContent, 'utf-8');
  await writeFile(sandboxFile, sandboxContent, 'utf-8');
  await writeFile(join(repo, 'score.txt'), '1\n', 'utf-8');
  await writeFile(join(repo, 'scripts', 'eval.js'), "process.stdout.write(JSON.stringify({ pass: true, score: 1 }));\n", 'utf-8');
  execFileSync('git', ['add', 'missions/demo/mission.md', 'missions/demo/sandbox.md', 'scripts/eval.js', 'score.txt'], { cwd: repo, stdio: 'ignore' });
  execFileSync('git', ['commit', '-m', 'add autoresearch fixtures'], { cwd: repo, stdio: 'ignore' });
  return {
    missionDir,
    repoRoot: repo,
    missionFile,
    sandboxFile,
    missionRelativeDir: 'missions/demo',