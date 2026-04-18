t_path}') || args.repoRoot;
  const existingHudPaneIds = listHudWatchPaneIdsInCurrentWindow(paneId);

  const omxPath = process.argv[1];
  if (!omxPath) return false;
  // Re-enter through the bare compatibility alias so the new pane executes immediately
  // instead of recursively taking the split-pane branch again.
  const launchArgs = ['autoresearch', args.missionDir, ...args.codexArgs];
  const command = [process.execPath, omxPath, ...launchArgs]
    .map((part) => `'${part.replace(/'/g, `'\\''`)}'`)
    .join(' ');

  const split = spawnSync(
    'tmux',
    ['split-window', '-h', '-t', paneId, '-d', '-P', '-F', '#{pane_id}', '-c', currentCwd, command],
    { encoding: 'utf-8' },
  );
  if (split.error || split.status !== 0) {
    return false;
  }