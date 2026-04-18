{
  return join(omxDir(cwd), 'logs', `tmux-hook-${new Date().toISOString().split('T')[0]}.jsonl`);
}

function parseConfig(raw: unknown): TmuxHookConfig {
  if (!raw || typeof raw !== 'object') {
    throw new Error('tmux-hook config must be a JSON object');
  }
  const parsed = raw as Record<string, unknown>;
  if (parsed.enabled !== true && parsed.enabled !== false) {
    throw new Error('`enabled` must be boolean');
  }
  const target = parsed.target;
  if (!target || typeof target !== 'object') {
    throw new Error('`target` is required');
  }
  const targetObj = target as Record<string, unknown>;
  if (targetObj.type !== 'session' && targetObj.type !== 'pane') {
    throw new Error('`target.type` must be "session" or "pane"');
  }