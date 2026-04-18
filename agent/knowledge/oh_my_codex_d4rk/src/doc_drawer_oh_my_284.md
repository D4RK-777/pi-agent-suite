upPath), { recursive: true });
    await copyFile(destinationPath, backupPath);
  }
  return true;
}

function resolveTargetDirectories(targetDir: string): Promise<string[]> {
  return readdir(targetDir, { withFileTypes: true }).then((entries) => {
    const childDirs = entries
      .filter((entry) => entry.isDirectory())
      .filter((entry) => !IGNORE_DIRECTORY_NAMES.has(entry.name))
      .map((entry) => join(targetDir, entry.name))
      .sort((a, b) => a.localeCompare(b));
    return [targetDir, ...childDirs];
  });
}