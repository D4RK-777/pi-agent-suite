`[omx] postLaunch: session archive failed: ${err instanceof Error ? err.message : err}`,
    );
  }

  // 3. Cancel any still-active modes
  try {
    const { readdir, writeFile, readFile } = await import("fs/promises");
    const scopedDirs = [getBaseStateDir(cwd), getStateDir(cwd, sessionId)];
    for (const stateDir of scopedDirs) {
      const files = await readdir(stateDir).catch(() => [] as string[]);
      for (const file of files) {
        if (!file.endsWith("-state.json") || file === "session.json") continue;
        const path = join(stateDir, file);
        const content = await readFile(path, "utf-8");
        const state = JSON.parse(content);
        if (state.active) {
          state.active = false;
          state.completed_at = new Date().toISOString();