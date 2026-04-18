contract.missionContent, 'utf-8');
  await writeFile(sandboxFile, contract.sandboxContent, 'utf-8');

  // Commit materialized mission files so the worktree is clean for
  // assertResetSafeWorktree, which runs immediately after this step.
  try {
    execFileSync('git', ['add', '--', missionFile, sandboxFile], { cwd: worktreePath, stdio: 'ignore',
      windowsHide: true,
    });
    execFileSync('git', ['commit', '-m', `autoresearch: materialize mission ${contract.missionSlug}`], {
      cwd: worktreePath,
      stdio: 'ignore',
    });
  } catch {
    // Non-fatal: if commit fails the reset-safe check will catch it with
    // a clear diagnostic.
  }

  return {
    ...contract,
    missionDir,
    missionFile,
    sandboxFile,
  };
}