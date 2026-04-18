import { describe, it } from 'node:test';
import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import { join } from 'node:path';

async function readSource(relativePath: string): Promise<string> {
  return readFile(join(process.cwd(), relativePath), 'utf8');
}

describe('error-handling warning guards', () => {
  it('removes silent shutdown mode-state swallow in team command', async () => {
    const source = await readSource('src/cli/team.ts');
    assert.match(source, /failed to persist team mode shutdown state/);
    assert.ok(!source.includes("completed_at: new Date().toISOString(),\n    }).catch(() => {});"));
  });