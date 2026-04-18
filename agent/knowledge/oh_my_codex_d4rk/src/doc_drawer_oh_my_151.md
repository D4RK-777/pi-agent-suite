ifest.status !== 'running') {
    return;
  }
  await finalizeRun(manifest, projectRoot, updates);
}

export async function stopAutoresearchRuntime(projectRoot: string): Promise<void> {
  const state = await readModeState('autoresearch', projectRoot);
  if (!state?.active) {
    return;
  }

  const runId = typeof state.run_id === 'string' ? state.run_id : null;
  if (runId) {
    await finalizeAutoresearchRunState(projectRoot, runId, {
      status: 'stopped',
      stopReason: 'operator stop',
    });
    return;
  }

  await cancelMode('autoresearch', projectRoot);
}