assert.equal(await processAutoresearchCandidate(worktreeContract, manifest, repo), 'interrupted');

      manifest = await loadAutoresearchRunManifest(repo, runtime.runId);
      await writeFile(join(worktreePath, 'scripts', 'eval.js'), "process.stdout.write(JSON.stringify({ pass: false, score: 0 }));\n", 'utf-8');
      await writeFile(join(worktreePath, 'score.txt'), '0\n', 'utf-8');
      execFileSync('git', ['add', 'scripts/eval.js', 'score.txt'], { cwd: worktreePath, stdio: 'ignore' });
      execFileSync('git', ['commit', '-m', 'make evaluator fail'], { cwd: worktreePath, stdio: 'ignore' });
      const failingCommit = execFileSync('git', ['rev-parse', 'HEAD'], { cwd: worktreePath, encoding: 'utf-8' }).trim();
      await writeFile(runtime.candidateFile, `${JSON.stringify({