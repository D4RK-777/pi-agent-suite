to extract archive ${archivePath}: ${(result.stderr || result.error?.message || '').trim()}`);
  }
}

async function findExtractedBinaryPath(rootDir: string, binaryPath: string): Promise<string | undefined> {
  const normalizedNeedle = binaryPath.replaceAll('\\', '/');
  const exactCandidate = join(rootDir, binaryPath);
  if (existsSync(exactCandidate)) return exactCandidate;

  const pending = [rootDir];
  while (pending.length > 0) {
    const current = pending.pop()!;
    const entries = await readdir(current, { withFileTypes: true });
    for (const entry of entries) {
      const fullPath = join(current, entry.name);
      if (entry.isDirectory()) {
        pending.push(fullPath);
        continue;
      }