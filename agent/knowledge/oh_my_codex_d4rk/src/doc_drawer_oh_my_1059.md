[omx] Update available: v${current} → v${latest}. Update now? [Y/n] `,
  );
  if (!approved) return;

  console.log(`[omx] Running: npm install -g ${PACKAGE_NAME}@latest`);
  const result = updateDependencies.runGlobalUpdate();

  if (result.ok) {
    await updateDependencies.setup({ force: true });
    console.log(`[omx] Updated to v${latest}. Restart to use new code.`);
  } else {
    console.log('[omx] Update failed. Run manually: npm install -g oh-my-codex@latest');
  }
}