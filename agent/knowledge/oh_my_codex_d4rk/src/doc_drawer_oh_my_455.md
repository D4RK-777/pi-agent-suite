utf-8' });
  if (res.error) {
    // tmux binary unavailable or not executable.
    return null;
  }

  if (res.status !== 0) {
    const stderr = (res.stderr || '').toLowerCase();
    // tmux installed but no server/session is running.
    if (stderr.includes('no server running') || stderr.includes('failed to connect to server')) {
      return new Set();
    }
    return null;
  }

  const sessions = (res.stdout || '')
    .split('\n')
    .map((s) => s.trim())
    .filter((s) => s.startsWith('omx-team-'));
  return new Set(sessions);
}