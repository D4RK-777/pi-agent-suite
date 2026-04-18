wait askYesNoImpl('[omx] Enjoying oh-my-codex? Star it on GitHub? [Y/n] ');
  if (!approved) return;

  const starRepoImpl = deps.starRepoFn ?? starRepo;
  const star = starRepoImpl();
  if (star.ok) {
    const log = deps.logFn ?? console.log;
    log('[omx] Thanks for the star!');
    return;
  }
  const warn = deps.warnFn ?? console.warn;
  warn(`[omx] Could not star repository automatically: ${star.error}`);
}