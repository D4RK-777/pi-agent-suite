const worktreeContract = await materializeAutoresearchMissionToWorktree(contract, worktreePath);
      const runtime = await prepareAutoresearchRuntime(worktreeContract, repo, worktreePath, { runTag: '20260314T010000Z' });

      await writeFile(join(worktreePath, 'score.txt'), '2\n', 'utf-8');
      execFileSync('git', ['add', 'score.txt'], { cwd: worktreePath, stdio: 'ignore' });
      execFileSync('git', ['commit', '-m', 'improve score'], { cwd: worktreePath, stdio: 'ignore' });
      const improvedCommit = execFileSync('git', ['rev-parse', 'HEAD'], { cwd: worktreePath, encoding: 'utf-8' }).trim();
      const initialManifest = await loadAutoresearchRunManifest(repo, runtime.runId);
      await writeFile(runtime.candidateFile, `${JSON.stringify({
        status: 'candidate',