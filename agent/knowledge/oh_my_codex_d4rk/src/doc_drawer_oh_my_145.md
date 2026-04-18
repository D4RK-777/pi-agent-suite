anifest, projectRoot, { status: 'stopped', stopReason: 'candidate abort' });
    return 'abort';
  }

  if (candidate.status === 'interrupted') {
    try {
      assertResetSafeWorktree(manifest.worktree_path);
    } catch {
      await finalizeRun(manifest, projectRoot, { status: 'failed', stopReason: 'interrupted dirty worktree requires operator intervention' });
      return 'error';
    }
    await recordAutoresearchIteration(manifest, {
      status: 'interrupted',
      decisionReason: 'candidate session interrupted cleanly',
      ...sharedEntry,
    });
    await writeRunManifest(manifest);
    await writeInstructionsFile(contract, manifest);
    return 'interrupted';
  }