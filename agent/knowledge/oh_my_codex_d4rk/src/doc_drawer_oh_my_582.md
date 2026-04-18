TmuxToken(`${repoDir}-${dirName}`)
    : sanitizeTmuxToken(dirName);
  let branchToken = "detached";
  const branch = tryReadGitValue(cwd, ["rev-parse", "--abbrev-ref", "HEAD"]);
  if (branch) branchToken = sanitizeTmuxToken(branch);
  const sessionToken = sanitizeTmuxToken(sessionId.replace(/^omx-/, ""));
  const name = `omx-${dirToken}-${branchToken}-${sessionToken}`;
  return name.length > 120 ? name.slice(0, 120) : name;
}

function parsePaneIdFromTmuxOutput(rawOutput: string): string | null {
  const paneId = rawOutput.split("\n")[0]?.trim() || "";
  return paneId.startsWith("%") ? paneId : null;
}