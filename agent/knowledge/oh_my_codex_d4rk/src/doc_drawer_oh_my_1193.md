ne!.prompts - 2));
    assert.equal(expectations.skillMin, Math.max(1, headline!.skills - 2));
  });

  it('never returns non-positive minimum expectations', () => {
    const expectations = getCatalogExpectations();
    assert.ok(expectations.promptMin >= 1);
    assert.ok(expectations.skillMin >= 1);
  });
});