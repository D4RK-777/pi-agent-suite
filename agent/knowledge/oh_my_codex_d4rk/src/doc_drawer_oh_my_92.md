orktree_path: manifest.worktree_path,
    status: manifest.status,
    updated_at: nowIso(),
  });
}

async function deactivateAutoresearchRun(manifest: AutoresearchRunManifest): Promise<void> {
  const previous = await readActiveRunState(manifest.repo_root);
  await writeActiveRunState(manifest.repo_root, {
    schema_version: 1,
    active: false,
    run_id: previous?.run_id ?? manifest.run_id,
    mission_slug: previous?.mission_slug ?? manifest.mission_slug,
    repo_root: manifest.repo_root,
    worktree_path: previous?.worktree_path ?? manifest.worktree_path,
    status: manifest.status,
    updated_at: nowIso(),
    completed_at: nowIso(),
  });
}

function resultPassValue(value: boolean | undefined): string {
  return value === undefined ? '' : String(value);
}