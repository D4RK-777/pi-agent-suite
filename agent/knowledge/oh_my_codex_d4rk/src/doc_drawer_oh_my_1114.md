question(): Promise<string> {
      return queue.shift() ?? '';
    },
    close(): void {},
  };
}

describe('initAutoresearchMission', () => {
  it('creates mission.md with correct content', async () => {
    const repo = await initRepo();
    try {
      const result = await initAutoresearchMission({
        topic: 'Improve test coverage for the auth module',
        evaluatorCommand: 'node scripts/eval.js',
        keepPolicy: 'score_improvement',
        slug: 'auth-coverage',
        repoRoot: repo,
      });

      assert.equal(result.slug, 'auth-coverage');
      assert.equal(result.missionDir, join(repo, 'missions', 'auth-coverage'));