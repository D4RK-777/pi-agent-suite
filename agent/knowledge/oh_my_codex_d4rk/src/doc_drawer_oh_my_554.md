writeFile(configPath, updated);
  console.log(`Set ${REASONING_KEY}="${mode}" in ${configPath}`);
}

export async function launchWithHud(args: string[]): Promise<void> {
  if (isNativeWindows()) {
    const { result } = spawnPlatformCommandSync("tmux", ["-V"], {
      encoding: "utf-8",
      stdio: ["pipe", "pipe", "pipe"],
    });
    if (result.error) {
      const errno = result.error as NodeJS.ErrnoException;
      const kind = classifySpawnError(errno);
      if (kind === "missing") {
        console.warn(
          "[omx] warning: tmux was not found on native Windows. Continuing without tmux/HUD.\n" +
            "[omx] To enable tmux-backed features, install psmux:\n" +
            "[omx]   winget install psmux\n" +
            "[omx] See: https://github.com/marlocarlo/psmux",