ive-assets\] failed to download /i.test(error.message)
    || /fetch failed/i.test(error.message);
}

async function downloadFile(url: string, destinationPath: string): Promise<void> {
  const response = await fetch(url);
  if (!response.ok || !response.body) {
    throw new Error(`[native-assets] failed to download ${url} (${response.status} ${response.statusText})`);
  }
  await mkdir(dirname(destinationPath), { recursive: true });
  await pipeline(Readable.fromWeb(response.body), createWriteStream(destinationPath));
}

async function sha256ForFile(path: string): Promise<string> {
  const hash = createHash('sha256');
  hash.update(await readFile(path));
  return hash.digest('hex');
}