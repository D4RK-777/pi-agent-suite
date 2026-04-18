=== 'ask-claude');
    const askGemini = parsed.skills.find((skill) => skill.name === 'ask-gemini');

    assert.equal(askClaude?.status, 'active');
    assert.equal(askGemini?.status, 'active');
  });

  it('includes ai-slop-cleaner as an active built-in skill', () => {
    const parsed = validateCatalogManifest(readSourceManifest());
    const aiSlopCleaner = parsed.skills.find((skill) => skill.name === 'ai-slop-cleaner');

    assert.equal(aiSlopCleaner?.category, 'shortcut');
    assert.equal(aiSlopCleaner?.status, 'active');
  });
});