join(packageRoot, ...segments);
    if (existsSync(fullPath)) return fullPath;
  }
  return null;
}

export function readCatalogManifest(packageRoot: string = getPackageRoot()): CatalogManifest {
  const path = resolveManifestPath(packageRoot);
  if (!path) {
    throw new Error('catalog_manifest_missing');
  }

  if (cachedManifest && cachedPath === path) return cachedManifest;

  const raw = JSON.parse(readFileSync(path, 'utf8')) as unknown;
  const manifest = validateCatalogManifest(raw);
  cachedManifest = manifest;
  cachedPath = path;
  return manifest;
}

export function tryReadCatalogManifest(packageRoot: string = getPackageRoot()): CatalogManifest | null {
  try {
    return readCatalogManifest(packageRoot);
  } catch {
    return null;
  }
}