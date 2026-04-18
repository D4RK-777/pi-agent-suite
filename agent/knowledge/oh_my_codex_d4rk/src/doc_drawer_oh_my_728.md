if (version[1] !== minimum[1]) return version[1] > minimum[1];
  return version[2] >= minimum[2];
}

function probeInstalledCodexVersion(): string | null {
  const { result } = spawnPlatformCommandSync("codex", ["--version"], {
    encoding: "utf-8",
    stdio: ["pipe", "pipe", "pipe"],
  });
  if (result.error || result.status !== 0) return null;
  const stdout = (result.stdout || "").trim();
  return stdout === "" ? null : stdout;
}

function shouldOmxManageTuiFromCodexVersion(versionOutput: string | null): boolean {
  if (!versionOutput) return true;
  const parsed = parseSemverTriplet(versionOutput);
  if (!parsed) return true;
  return !semverGte(parsed, TUI_OWNED_BY_CODEX_VERSION);
}