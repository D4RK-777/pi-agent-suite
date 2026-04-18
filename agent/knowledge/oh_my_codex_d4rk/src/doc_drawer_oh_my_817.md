t stdoutIsTTY = deps.stdoutIsTTY ?? process.stdout.isTTY;
  if (!stdinIsTTY || !stdoutIsTTY) return;

  const hasBeenPromptedImpl = deps.hasBeenPromptedFn ?? hasBeenPrompted;
  if (await hasBeenPromptedImpl()) return;

  const isGhInstalledImpl = deps.isGhInstalledFn ?? isGhInstalled;
  if (!isGhInstalledImpl()) return;

  // Mark as prompted before asking so we never prompt again even if interrupted.
  const markPromptedImpl = deps.markPromptedFn ?? markPrompted;
  await markPromptedImpl();

  const askYesNoImpl = deps.askYesNoFn ?? askYesNo;
  const approved = await askYesNoImpl('[omx] Enjoying oh-my-codex? Star it on GitHub? [Y/n] ');
  if (!approved) return;