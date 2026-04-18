import { describe, it } from 'node:test';
import assert from 'node:assert/strict';
import { mkdir, mkdtemp, readFile, writeFile } from 'fs/promises';
import { join } from 'path';
import { tmpdir } from 'os';
import { readCatalogManifest, toPublicCatalogContract } from '../reader.js';

async function readSourceManifestRaw(): Promise<string> {
  return readFile(join(process.cwd(), 'src', 'catalog', 'manifest.json'), 'utf8');
}

async function readSourceManifestCounts(): Promise<{ skills: number; agents: number }> {
  const raw = await readSourceManifestRaw();
  const parsed = JSON.parse(raw) as { skills: unknown[]; agents: unknown[] };
  return {
    skills: parsed.skills.length,
    agents: parsed.agents.length,
  };
}