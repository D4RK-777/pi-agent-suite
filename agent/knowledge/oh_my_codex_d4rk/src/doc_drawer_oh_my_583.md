paneId = rawOutput.split("\n")[0]?.trim() || "";
  return paneId.startsWith("%") ? paneId : null;
}

function parseWindowIndexFromTmuxOutput(rawOutput: string): string | null {
  const windowIndex = rawOutput.split("\n")[0]?.trim() || "";
  return /^[0-9]+$/.test(windowIndex) ? windowIndex : null;
}

function detectDetachedSessionWindowIndex(sessionName: string): string | null {
  try {
    const output = execFileSync(
      "tmux",
      ["display-message", "-p", "-t", sessionName, "#{window_index}"],
      { encoding: "utf-8" },
    );
    return parseWindowIndexFromTmuxOutput(output);
  } catch (err) {
    process.stderr.write(`[cli/index] operation failed: ${err}\n`);
    return null;
  }
}