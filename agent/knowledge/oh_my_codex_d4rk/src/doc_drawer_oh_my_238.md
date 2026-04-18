<string, unknown> {
  return typeof value === 'object' && value !== null && !Array.isArray(value);
}

function assertNonEmptyString(value: unknown, field: string): asserts value is string {
  if (typeof value !== 'string' || value.trim() === '') {
    throw new Error(`catalog_manifest_invalid:${field}`);
  }
}

export function validateCatalogManifest(input: unknown): CatalogManifest {
  if (!isObject(input)) throw new Error('catalog_manifest_invalid:root');

  if (typeof input.schemaVersion !== 'number' || !Number.isInteger(input.schemaVersion)) {
    throw new Error('catalog_manifest_invalid:schemaVersion');
  }

  assertNonEmptyString(input.catalogVersion, 'catalogVersion');