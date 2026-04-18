(l[0] !== c[0]) return l[0] > c[0];
  if (l[1] !== c[1]) return l[1] > c[1];
  return l[2] > c[2];
}

export function shouldCheckForUpdates(
  nowMs: number,
  state: UpdateState | null,
  intervalMs = CHECK_INTERVAL_MS
): boolean {
  if (!state?.last_checked_at) return true;
  const last = Date.parse(state.last_checked_at);
  if (!Number.isFinite(last)) return true;
  return (nowMs - last) >= intervalMs;
}

function updateStatePath(cwd: string): string {
  return join(cwd, '.omx', 'state', 'update-check.json');
}