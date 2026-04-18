import { describe, it } from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { join } from 'node:path';
import { summarizeCatalogCounts, validateCatalogManifest } from '../schema.js';

function readSourceManifest(): unknown {
  const path = join(process.cwd(), 'src', 'catalog', 'manifest.json');
  return JSON.parse(readFileSync(path, 'utf8'));
}

describe('catalog schema', () => {
  it('validates repository manifest', () => {
    const parsed = validateCatalogManifest(readSourceManifest());
    assert.equal(parsed.schemaVersion, 1);
    assert.ok(parsed.catalogVersion.length > 0);
    assert.ok(parsed.skills.length > 0);
    assert.ok(parsed.agents.length > 0);
  });