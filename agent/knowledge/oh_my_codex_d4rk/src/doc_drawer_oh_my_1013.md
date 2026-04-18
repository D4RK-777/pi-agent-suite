se, reason: 'failed to resolve pane id from session' };
  }
  return { ok: true, target: paneId };
}

function detectActivePaneFromList(): InitialTargetDetection | null {
  const paneList = runTmux(['list-panes', '-a', '-F', '#{pane_id}\t#{pane_active}\t#{session_name}']);
  if (!paneList.ok || paneList.stdout.trim() === '') return null;

  const rows = paneList.stdout
    .split('\n')
    .map(line => line.trim())
    .filter(Boolean)
    .map(line => line.split('\t'))
    .filter(parts => parts.length >= 3);
  if (rows.length === 0) return null;

  const active = rows.find(parts => parts[1] === '1') || rows[0];
  const paneId = (active?.[0] || '').trim();
  const sessionName = (active?.[2] || '').trim();
  if (!paneId) return null;