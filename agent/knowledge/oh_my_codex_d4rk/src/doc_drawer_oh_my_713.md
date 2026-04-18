+/, "")
      : relativePath;
  const backupPath = join(backupContext.backupRoot, safeRelativePath);

  if (!options.dryRun) {
    await mkdir(dirname(backupPath), { recursive: true });
    await copyFile(destinationPath, backupPath);
  }
  if (options.verbose) {
    console.log(`  backup ${destinationPath} -> ${backupPath}`);
  }
  return true;
}

async function filesDiffer(src: string, dst: string): Promise<boolean> {
  if (!existsSync(dst)) return true;
  const [srcContent, dstContent] = await Promise.all([
    readFile(src, "utf-8"),
    readFile(dst, "utf-8"),
  ]);
  return srcContent !== dstContent;
}