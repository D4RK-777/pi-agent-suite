tRoot,
    };
  }
  return {
    backupRoot: join(homedir(), ".omx", "backups", "setup", timestamp),
    baseRoot: homedir(),
  };
}

async function ensureBackup(
  destinationPath: string,
  contentChanged: boolean,
  backupContext: SetupBackupContext,
  options: Pick<SetupOptions, "dryRun" | "verbose">,
): Promise<boolean> {
  if (!contentChanged || !existsSync(destinationPath)) return false;

  const relativePath = relative(backupContext.baseRoot, destinationPath);
  const safeRelativePath =
    relativePath.startsWith("..") || relativePath === ""
      ? destinationPath.replace(/^[/]+/, "")
      : relativePath;
  const backupPath = join(backupContext.backupRoot, safeRelativePath);