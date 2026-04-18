.throws(
      () => validateCatalogManifest(broken),
      /agents\[\d+\]\.canonical/,
    );
  });

  it('summarizes counts', () => {
    const parsed = validateCatalogManifest(readSourceManifest());
    const counts = summarizeCatalogCounts(parsed);
    assert.equal(counts.skillCount, parsed.skills.length);
    assert.equal(counts.promptCount, parsed.agents.length);
    assert.ok(counts.activeSkillCount > 0);
    assert.ok(counts.activeAgentCount > 0);
  });

  it('includes ask-claude and ask-gemini as active built-in skills', () => {
    const parsed = validateCatalogManifest(readSourceManifest());
    const askClaude = parsed.skills.find((skill) => skill.name === 'ask-claude');
    const askGemini = parsed.skills.find((skill) => skill.name === 'ask-gemini');