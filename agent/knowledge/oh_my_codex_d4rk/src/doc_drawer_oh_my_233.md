est | null {
  try {
    return readCatalogManifest(packageRoot);
  } catch {
    return null;
  }
}

export function getCatalogCounts(packageRoot: string = getPackageRoot()): CatalogCounts {
  const manifest = readCatalogManifest(packageRoot);
  return summarizeCatalogCounts(manifest);
}

export interface PublicCatalogContract {
  generatedAt: string;
  version: string;
  counts: CatalogCounts;
  coreSkills: string[];
  skills: CatalogManifest['skills'];
  agents: CatalogManifest['agents'];
  aliases: Array<{ name: string; canonical: string }>;
  internalHidden: string[];
}