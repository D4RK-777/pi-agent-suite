length > 0);
    assert.ok(parsed.skills.length > 0);
    assert.ok(parsed.agents.length > 0);
  });

  it('enforces required core skills as active', () => {
    const broken = JSON.parse(JSON.stringify(readSourceManifest()));
    const idx = broken.skills.findIndex((s: { name: string }) => s.name === 'team');
    broken.skills[idx].status = 'deprecated';
    assert.throws(() => validateCatalogManifest(broken), /missing_core_skill:team/);
  });

  it('requires canonical for alias/merged skill entries', () => {
    const broken = JSON.parse(JSON.stringify(readSourceManifest()));
    const idx = broken.skills.findIndex((s: { status: string }) => s.status === 'alias');
    delete broken.skills[idx].canonical;