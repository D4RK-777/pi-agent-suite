{response.statusText}) from ${url}`);
  }
  return await response.json() as NativeReleaseManifest;
}

function isUnavailableManifestError(error: unknown): boolean {
  if (!(error instanceof Error)) return false;
  return /\[native-assets\] failed to fetch native release manifest/i.test(error.message)
    || /fetch failed/i.test(error.message);
}

function isUnavailableArchiveError(error: unknown): boolean {
  if (!(error instanceof Error)) return false;
  return /\[native-assets\] failed to download /i.test(error.message)
    || /fetch failed/i.test(error.message);
}