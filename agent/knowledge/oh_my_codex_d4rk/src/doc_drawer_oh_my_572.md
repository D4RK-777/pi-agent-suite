;
    } catch {
      // best effort only
    }
  }
  return buildTmuxSessionName(cwd, sessionId);
}

function buildNativeHookBaseContext(
  cwd: string,
  sessionId: string,
  normalizedEvent: "started" | "blocked" | "finished" | "failed",
  extra: Record<string, unknown> = {},
): Record<string, unknown> {
  const repoPath =
    tryReadGitValue(cwd, ["rev-parse", "--show-toplevel"]) || cwd;
  const branch = tryReadGitValue(cwd, ["rev-parse", "--abbrev-ref", "HEAD"]);
  const issueNumber = extractIssueNumber(
    [branch, basename(cwd)].filter(Boolean).join(" "),
  );