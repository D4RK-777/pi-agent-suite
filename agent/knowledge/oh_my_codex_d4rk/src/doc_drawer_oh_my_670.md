nst hash = createHash('sha256');
  hash.update(await readFile(path));
  return hash.digest('hex');
}

async function extractArchive(archivePath: string, destinationDir: string): Promise<void> {
  await mkdir(destinationDir, { recursive: true });
  const ext = extname(archivePath).toLowerCase();
  if (ext === '.zip') {
    const { result } = spawnPlatformCommandSync(
      process.platform === 'win32' ? 'powershell' : 'unzip',
      process.platform === 'win32'
        ? ['-NoLogo', '-NoProfile', '-ExecutionPolicy', 'Bypass', '-Command', `Expand-Archive -LiteralPath '${archivePath.replace(/'/g, "''")}' -DestinationPath '${destinationDir.replace(/'/g, "''")}' -Force`]
        : ['-oq', archivePath, '-d', destinationDir],
      { encoding: 'utf-8' },
    );