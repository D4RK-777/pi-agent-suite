d],
    { encoding: 'utf-8' },
  );
  if (split.error || split.status !== 0) {
    return false;
  }

  if (sessionName && process.env.OMX_MOUSE !== '0') {
    enableMouseScrolling(sessionName);
  }
  if (existingHudPaneIds.length === 0) {
    restoreStandaloneHudPane(paneId, currentCwd);
  }
  console.log(`Autoresearch launched in split pane next to interview pane.`);
  return true;
}

async function executeAutoresearchMissionRun(missionDir: string, codexArgs: string[]): Promise<void> {
  const contract = await loadAutoresearchMissionContract(missionDir);
  await assertModeStartAllowed('autoresearch', contract.repoRoot);
  const runTag = buildAutoresearchRunTag();
  const plan = planWorktreeTarget({
    cwd: contract.repoRoot,
    scope: 'autoresearch',