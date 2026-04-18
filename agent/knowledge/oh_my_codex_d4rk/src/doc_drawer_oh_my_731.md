eturn { scope, source: "prompt" };
  }
  return { scope: DEFAULT_SETUP_SCOPE, source: "default" };
}

function hasGitignoreEntry(content: string, entry: string): boolean {
  return content
    .split(/\r?\n/)
    .map((line) => line.trim())
    .some((line) => line === entry);
}

async function ensureProjectOmxGitignore(
  projectRoot: string,
  backupContext: SetupBackupContext,
  options: Pick<SetupOptions, "dryRun" | "verbose">,
): Promise<"created" | "updated" | "unchanged"> {
  const gitignorePath = join(projectRoot, ".gitignore");
  const destinationExists = existsSync(gitignorePath);
  const existing = destinationExists
    ? await readFile(gitignorePath, "utf-8")
    : "";

  if (hasGitignoreEntry(existing, PROJECT_OMX_GITIGNORE_ENTRY)) {
    return "unchanged";
  }