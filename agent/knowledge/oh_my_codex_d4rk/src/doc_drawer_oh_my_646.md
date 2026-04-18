, "--cwd", cwd], {
    cwd,
    stdio: "ignore",
    timeout: 3000,
    env: {
      ...process.env,
      OMX_HOOK_DERIVED_SIGNALS: "1",
    },
  });
}

async function cancelModes(): Promise<void> {
  const { writeFile, readFile } = await import("fs/promises");
  const cwd = process.cwd();
  const nowIso = new Date().toISOString();
  try {
    const refs = await listModeStateFilesWithScopePreference(cwd);
    const states = new Map<
      string,
      {
        path: string;
        scope: "root" | "session";
        state: Record<string, unknown>;
      }
    >();