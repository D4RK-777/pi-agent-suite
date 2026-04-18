: unknown[] };
  return {
    skills: parsed.skills.length,
    agents: parsed.agents.length,
  };
}

describe('catalog reader/contract', () => {
  it('prefers template manifest path when present', async () => {
    const root = await mkdtemp(join(tmpdir(), 'omx-catalog-'));
    await mkdir(join(root, 'templates'), { recursive: true });
    await writeFile(
      join(root, 'templates', 'catalog-manifest.json'),
      await readSourceManifestRaw(),
    );

    const parsed = readCatalogManifest(root);
    assert.equal(parsed.schemaVersion, 1);
    assert.ok(parsed.skills.length > 0);
  });