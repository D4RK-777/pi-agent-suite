`tmux exited ${result.status}` };
  }
  return { ok: true, stdout: (result.stdout || '').trim() };
}

function resolveValidateTarget(config: TmuxHookConfig): { ok: true; target: string } | { ok: false; reason: string } {
  if (config.target.type === 'pane') {
    const paneCheck = runTmux(['display-message', '-p', '-t', config.target.value, '#{pane_id}']);
    if (!paneCheck.ok || paneCheck.stdout === '') {
      return { ok: false, reason: paneCheck.ok ? 'pane not found' : paneCheck.stderr };
    }
    return { ok: true, target: paneCheck.stdout };
  }