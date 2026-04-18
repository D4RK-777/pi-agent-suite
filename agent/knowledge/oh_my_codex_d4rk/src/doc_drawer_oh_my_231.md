import { existsSync, readFileSync } from 'fs';
import { join } from 'path';
import { getPackageRoot } from '../utils/package.js';
import { type CatalogManifest, summarizeCatalogCounts, type CatalogCounts, validateCatalogManifest } from './schema.js';

const MANIFEST_CANDIDATE_PATHS = [
  ['templates', 'catalog-manifest.json'],
  ['src', 'catalog', 'manifest.json'],
  ['dist', 'catalog', 'manifest.json'],
] as const;

let cachedManifest: CatalogManifest | null = null;
let cachedPath: string | null = null;

function resolveManifestPath(packageRoot: string): string | null {
  for (const segments of MANIFEST_CANDIDATE_PATHS) {
    const fullPath = join(packageRoot, ...segments);
    if (existsSync(fullPath)) return fullPath;
  }
  return null;
}