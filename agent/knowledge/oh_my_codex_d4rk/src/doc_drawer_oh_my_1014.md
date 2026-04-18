ve?.[0] || '').trim();
  const sessionName = (active?.[2] || '').trim();
  if (!paneId) return null;

  return {
    target: { type: 'pane', value: paneId },
    sessionName: sessionName || undefined,
  };
}

function detectInitialTarget(): InitialTargetDetection | null {
  const canonicalPane = resolveCodexPane();
  if (canonicalPane) {
    const pane = runTmux(['display-message', '-p', '-t', canonicalPane, '#{pane_id}']);
    if (pane.ok && pane.stdout) {
      const session = runTmux(['display-message', '-p', '-t', canonicalPane, '#S']);
      return {
        target: { type: 'pane', value: pane.stdout },
        sessionName: session.ok && session.stdout ? session.stdout : undefined,
      };
    }
  }