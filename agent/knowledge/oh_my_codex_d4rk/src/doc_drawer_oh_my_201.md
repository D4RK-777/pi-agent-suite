repo,
    missionFile,
    sandboxFile,
    missionRelativeDir: 'missions/demo',
    missionContent,
    sandboxContent,
    sandbox: {
      frontmatter: { evaluator: { command: 'node scripts/eval.js', format: 'json' } },
      evaluator: { command: 'node scripts/eval.js', format: 'json' },
      body: 'Stay inside the mission boundary.',
    },
    missionSlug: 'missions-demo',
  };
}

describe('autoresearch runtime', () => {
  it('builds bootstrap instructions with mission, sandbox, and evaluator contract', async () => {
    const repo = await initRepo();
    try {
      const contract = await makeContract(repo);