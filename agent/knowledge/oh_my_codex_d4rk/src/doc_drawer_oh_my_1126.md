ator command/i);
    } finally {
      await rm(repo, { recursive: true, force: true });
    }
  });

  it('rejects placeholder evaluator commands and accepts concrete commands', () => {
    assert.equal(isLaunchReadyEvaluatorCommand('TODO replace me'), false);
    assert.equal(isLaunchReadyEvaluatorCommand('node scripts/eval.js'), true);
    assert.equal(isLaunchReadyEvaluatorCommand('bash scripts/eval.sh'), true);
  });