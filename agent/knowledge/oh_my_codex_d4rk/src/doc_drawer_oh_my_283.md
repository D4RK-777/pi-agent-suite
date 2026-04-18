\n${formatList(snapshot.directories, "/").join("\n")}`;
  return wrapManagedContent(body, manual);
}

async function ensureBackup(
  destinationPath: string,
  backupRoot: string,
  dryRun: boolean,
): Promise<boolean> {
  if (!existsSync(destinationPath)) return false;
  const relativePath = relative(process.cwd(), destinationPath);
  const safeRelativePath =
    relativePath.startsWith("..") || relativePath === ""
      ? destinationPath.replace(/^[/]+/, "")
      : relativePath;
  const backupPath = join(backupRoot, safeRelativePath);
  if (!dryRun) {
    await mkdir(dirname(backupPath), { recursive: true });
    await copyFile(destinationPath, backupPath);
  }
  return true;
}