fest['agents'];
  aliases: Array<{ name: string; canonical: string }>;
  internalHidden: string[];
}

export function toPublicCatalogContract(manifest: CatalogManifest): PublicCatalogContract {
  const aliases = manifest.skills
    .filter((s) => (s.status === 'alias' || s.status === 'merged') && typeof s.canonical === 'string')
    .map((s) => ({ name: s.name, canonical: s.canonical! }));
  const internalHidden = manifest.skills
    .filter((s) => s.status === 'internal')
    .map((s) => s.name);