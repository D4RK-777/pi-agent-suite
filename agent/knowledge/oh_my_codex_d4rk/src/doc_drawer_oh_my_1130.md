/eval\.js/);
    } finally {
      await rm(repo, { recursive: true, force: true });
    }
  });
});

describe('buildAutoresearchDeepInterviewPrompt', () => {
  it('activates deep-interview --autoresearch and includes seed inputs', () => {
    const prompt = buildAutoresearchDeepInterviewPrompt({
      topic: 'Investigate flaky tests',
      evaluatorCommand: 'node scripts/eval.js',
      keepPolicy: 'score_improvement',
      slug: 'flaky-tests',
    });