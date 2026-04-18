const issueNumber = extractIssueNumber(
    [branch, basename(cwd)].filter(Boolean).join(" "),
  );

  return {
    normalized_event: normalizedEvent,
    session_name: resolveNativeSessionName(cwd, sessionId),
    repo_path: repoPath,
    repo_name: basename(repoPath),
    worktree_path: cwd,
    ...(branch ? { branch } : {}),
    ...(issueNumber !== undefined ? { issue_number: issueNumber } : {}),
    ...extra,
  };
}