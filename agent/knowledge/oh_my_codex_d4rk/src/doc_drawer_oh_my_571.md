text.match(/(^|[^\w/])#(\d+)\b/);
  return generic ? Number.parseInt(generic[2], 10) : undefined;
}

function resolveNativeSessionName(cwd: string, sessionId: string): string {
  if (process.env.TMUX) {
    try {
      const tmuxSession = execFileSync(
        "tmux",
        ["display-message", "-p", "#S"],
        {
          encoding: "utf-8",
          stdio: ["ignore", "pipe", "ignore"],
          timeout: 2000,
        },
      ).trim();
      if (tmuxSession) return tmuxSession;
    } catch {
      // best effort only
    }
  }
  return buildTmuxSessionName(cwd, sessionId);
}