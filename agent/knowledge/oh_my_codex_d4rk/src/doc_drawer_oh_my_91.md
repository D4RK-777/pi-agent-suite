rchActiveRunState): Promise<void> {
  await writeJsonFile(activeRunStateFile(projectRoot), value);
}

async function assertAutoresearchLockAvailable(projectRoot: string): Promise<void> {
  const state = await readActiveRunState(projectRoot);
  if (state?.active && state.run_id) {
    throw new Error(`autoresearch_active_run_exists:${state.run_id}`);
  }
}

async function activateAutoresearchRun(manifest: AutoresearchRunManifest): Promise<void> {
  await writeActiveRunState(manifest.repo_root, {
    schema_version: 1,
    active: true,
    run_id: manifest.run_id,
    mission_slug: manifest.mission_slug,
    repo_root: manifest.repo_root,
    worktree_path: manifest.worktree_path,
    status: manifest.status,
    updated_at: nowIso(),
  });
}