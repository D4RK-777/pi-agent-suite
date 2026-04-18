ss.env.OMX_AUTO_UPDATE === '0') return;
  if (!process.stdin.isTTY || !process.stdout.isTTY) return;

  const now = Date.now();
  const state = await readUpdateState(cwd);
  if (!shouldCheckForUpdates(now, state)) return;

  const [current, latest] = await Promise.all([
    updateDependencies.getCurrentVersion(),
    updateDependencies.fetchLatestVersion(),
  ]);

  await writeUpdateState(cwd, {
    last_checked_at: new Date(now).toISOString(),
    last_seen_latest: latest || state?.last_seen_latest,
  });

  if (!current || !latest || !isNewerVersion(current, latest)) return;

  const approved = await updateDependencies.askYesNo(
    `[omx] Update available: v${current} → v${latest}. Update now? [Y/n] `,
  );
  if (!approved) return;