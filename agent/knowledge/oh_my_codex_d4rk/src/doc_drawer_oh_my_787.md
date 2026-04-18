in config.toml via mergeConfig
  if (options.verbose) console.log(`  Notify hook: ${hookScript}`);
}

async function verifyTeamCliApiInterop(
  pkgRoot: string,
): Promise<{ ok: true } | { ok: false; message: string }> {
  const teamCliPath = join(pkgRoot, "dist", "cli", "team.js");
  if (!existsSync(teamCliPath)) {
    return { ok: false, message: `missing ${teamCliPath}` };
  }

  try {
    const content = await readFile(teamCliPath, "utf-8");
    const missing = REQUIRED_TEAM_CLI_API_MARKERS.filter(
      (marker) => !content.includes(marker),
    );
    if (missing.length > 0) {
      return {
        ok: false,
        message: `team CLI interop markers missing: ${missing.join(", ")}`,
      };
    }
    return { ok: true };
  } catch {