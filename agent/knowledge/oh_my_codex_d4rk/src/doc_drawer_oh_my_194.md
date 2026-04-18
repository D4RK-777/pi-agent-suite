assert.equal(await processAutoresearchCandidate(worktreeContract, manifest, repo), 'discard');

      manifest = await loadAutoresearchRunManifest(repo, runtime.runId);
      await writeFile(join(worktreePath, 'scripts', 'eval.js'), "process.stdout.write('not json');\n", 'utf-8');
      execFileSync('git', ['add', 'scripts/eval.js'], { cwd: worktreePath, stdio: 'ignore' });
      execFileSync('git', ['commit', '-m', 'break evaluator json'], { cwd: worktreePath, stdio: 'ignore' });
      const parseErrorCommit = execFileSync('git', ['rev-parse', 'HEAD'], { cwd: worktreePath, encoding: 'utf-8' }).trim();
      await writeFile(runtime.candidateFile, `${JSON.stringify({
        status: 'candidate',
        candidate_commit: parseErrorCommit,