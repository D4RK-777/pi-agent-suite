codex", launchArgs, {
    cwd,
    stdio: "inherit",
    env: codexEnv,
    encoding: "utf-8",
  });

  if (result.error) {
    const errno = result.error as NodeJS.ErrnoException;
    const kind = classifySpawnError(errno);
    if (kind === "missing") {
      console.error(
        "[omx] failed to launch codex: executable not found in PATH",
      );
    } else if (kind === "blocked") {
      console.error(
        `[omx] failed to launch codex: executable is present but blocked in the current environment (${errno.code || "blocked"})`,
      );
    } else {
      console.error(`[omx] failed to launch codex: ${errno.message}`);
    }
    throw result.error;
  }