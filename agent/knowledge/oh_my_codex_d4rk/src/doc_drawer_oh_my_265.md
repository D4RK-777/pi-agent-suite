est(root);
    assert.equal(parsed.schemaVersion, 1);
    assert.ok(parsed.skills.length > 0);
  });

  it('builds public contract with aliases and internalHidden', async () => {
    const contract = toPublicCatalogContract(readCatalogManifest());
    const expected = await readSourceManifestCounts();
    assert.equal(contract.counts.skillCount, expected.skills);
    assert.equal(contract.counts.promptCount, expected.agents);
    assert.ok(contract.aliases.some((a) => a.name === 'swarm' && a.canonical === 'team'));
    assert.ok(contract.internalHidden.includes('worker'));
    assert.ok(contract.coreSkills.includes('autopilot'));
    assert.ok(contract.skills.some((s) => s.name === 'ask-claude' && s.status === 'active'));