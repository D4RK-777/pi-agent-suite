'pane not found' : paneCheck.stderr };
    }
    return { ok: true, target: paneCheck.stdout };
  }

  const paneList = runTmux(['list-panes', '-t', config.target.value, '-F', '#{pane_id} #{pane_active}']);
  if (!paneList.ok) {
    return { ok: false, reason: paneList.stderr };
  }
  const lines = paneList.stdout.split('\n').map(line => line.trim()).filter(Boolean);
  if (lines.length === 0) {
    return { ok: false, reason: 'session has no panes' };
  }
  const active = lines.find(line => line.endsWith(' 1')) || lines[0];
  const paneId = active.split(' ')[0];
  if (!paneId) {
    return { ok: false, reason: 'failed to resolve pane id from session' };
  }
  return { ok: true, target: paneId };
}