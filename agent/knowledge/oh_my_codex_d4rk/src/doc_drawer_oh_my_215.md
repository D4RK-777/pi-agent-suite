RunManifest(repo, runtime.runId);
      assert.equal(keptManifest.last_kept_commit, improvedCommit);

      await writeFile(join(worktreePath, 'score.txt'), '1\n', 'utf-8');
      execFileSync('git', ['add', 'score.txt'], { cwd: worktreePath, stdio: 'ignore' });
      execFileSync('git', ['commit', '-m', 'worse score'], { cwd: worktreePath, stdio: 'ignore' });
      const worseCommit = execFileSync('git', ['rev-parse', 'HEAD'], { cwd: worktreePath, encoding: 'utf-8' }).trim();
      const beforeDiscardManifest = await loadAutoresearchRunManifest(repo, runtime.runId);
      await writeFile(runtime.candidateFile, `${JSON.stringify({
        status: 'candidate',
        candidate_commit: worseCommit,
        base_commit: beforeDiscardManifest.last_kept_commit,