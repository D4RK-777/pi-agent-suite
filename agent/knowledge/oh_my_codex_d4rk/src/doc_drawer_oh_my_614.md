);
    return findHudWatchPaneIds(parseTmuxPaneSnapshot(output), currentPaneId);
  } catch (err) {
    process.stderr.write(`[cli/index] operation failed: ${err}\n`);
    return [];
  }
}

function createHudWatchPane(cwd: string, hudCmd: string): string | null {
  const output = execFileSync(
    "tmux",
    [
      "split-window",
      "-v",
      "-l",
      String(HUD_TMUX_HEIGHT_LINES),
      "-d",
      "-c",
      cwd,
      "-P",
      "-F",
      "#{pane_id}",
      hudCmd,
    ],
    { encoding: "utf-8" },
  );
  return parsePaneIdFromTmuxOutput(output);
}