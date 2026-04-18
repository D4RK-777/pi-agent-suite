const rootSessionGuardActive = Boolean(
    activeSession && !isSessionStale(activeSession),
  );

  console.log("oh-my-codex AGENTS bootstrap");
  console.log("===========================\n");
  console.log(`Target: ${requestedTarget}`);
  console.log(
    `Scope: target directory + ${Math.max(plannedDirs.length - 1, 0)} direct child director${plannedDirs.length === 2 ? "y" : "ies"}\n`,
  );

  for (let index = 0; index < plannedDirs.length; index += 1) {
    const dir = plannedDirs[index];
    const destinationPath = join(dir, "AGENTS.md");
    const existingContent = existsSync(destinationPath)
      ? await readFile(destinationPath, "utf-8")
      : undefined;
    const isRootTarget = index === 0;
    const relativeDir = relative(cwd, dir).replaceAll("\\", "/") || ".";