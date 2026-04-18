t.status !== 0) return null;
  const value = (result.stdout || '').trim();
  return value || null;
}

function listHudWatchPaneIdsInCurrentWindow(currentPaneId?: string): string[] {
  if (!currentPaneId) return [];
  const result = spawnSync(
    'tmux',
    ['list-panes', '-t', currentPaneId, '-F', '#{pane_id}\t#{pane_current_command}\t#{pane_start_command}'],
    { encoding: 'utf-8' },
  );
  if (result.error || result.status !== 0) return [];
  return (result.stdout || '')
    .split('\n')
    .map((line) => line.trim())
    .filter(Boolean)
    .map((line) => line.split('\t'))
    .filter((parts) => parts.length >= 3)
    .map(([paneId = '', currentCommand = '', startCommand = '']) => ({ paneId, currentCommand, startCommand }))
    .filter((pane) => pane.paneId.startsWith('%'))