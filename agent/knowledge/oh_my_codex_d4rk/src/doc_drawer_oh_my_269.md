findIndex((s: { status: string }) => s.status === 'alias');
    delete broken.skills[idx].canonical;

    assert.throws(
      () => validateCatalogManifest(broken),
      /skills\[\d+\]\.canonical/,
    );
  });

  it('requires canonical for alias/merged agent entries', () => {
    const broken = JSON.parse(JSON.stringify(readSourceManifest()));
    broken.agents.push({
      name: 'tmp-merged-agent',
      category: 'build',
      status: 'merged',
    });

    assert.throws(
      () => validateCatalogManifest(broken),
      /agents\[\d+\]\.canonical/,
    );
  });