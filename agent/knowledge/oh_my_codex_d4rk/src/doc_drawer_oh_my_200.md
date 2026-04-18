File(missionFile, missionContent, 'utf-8');
  await writeFile(sandboxFile, sandboxContent, 'utf-8');
  await writeFile(join(repo, 'score.txt'), '1\n', 'utf-8');
  await writeFile(join(repo, 'scripts', 'eval.js'), "import { readFileSync } from 'node:fs';\nconst score = Number(readFileSync('score.txt', 'utf-8').trim());\nprocess.stdout.write(JSON.stringify({ pass: true, score }));\n", 'utf-8');
  execFileSync('git', ['add', 'missions/demo/mission.md', 'missions/demo/sandbox.md', 'scripts/eval.js', 'score.txt'], { cwd: repo, stdio: 'ignore' });
  execFileSync('git', ['commit', '-m', 'add autoresearch fixtures'], { cwd: repo, stdio: 'ignore' });
  return {
    missionDir,
    repoRoot: repo,
    missionFile,
    sandboxFile,
    missionRelativeDir: 'missions/demo',
    missionContent,