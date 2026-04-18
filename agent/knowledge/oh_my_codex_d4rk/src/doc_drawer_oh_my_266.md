ot'));
    assert.ok(contract.skills.some((s) => s.name === 'ask-claude' && s.status === 'active'));
    assert.ok(contract.skills.some((s) => s.name === 'ask-gemini' && s.status === 'active'));
    assert.ok(contract.skills.some((s) => s.name === 'ai-slop-cleaner' && s.status === 'active'));
  });

  it('template manifest can be synced from source manifest', async () => {
    const sourceRaw = await readFile(join(process.cwd(), 'src', 'catalog', 'manifest.json'), 'utf8');
    const targetRaw = await readFile(join(process.cwd(), 'templates', 'catalog-manifest.json'), 'utf8');
    assert.equal(JSON.parse(targetRaw).catalogVersion, JSON.parse(sourceRaw).catalogVersion);
  });
});