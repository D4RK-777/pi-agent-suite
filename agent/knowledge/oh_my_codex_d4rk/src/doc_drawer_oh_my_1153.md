,
        'utf-8',
      );
      execFileSync('chmod', ['+x', fakeCodexPath], { stdio: 'ignore' });

      const result = runOmx(repo, ['autoresearch', '--topic', 'Investigate flaky onboarding behavior', '--evaluator', 'node scripts/eval.js', '--slug', 'test-launch'], {
        PATH: `${fakeBin}:${process.env.PATH || ''}`,
        OMX_TEST_REPO_ROOT: repo,
      });
      assert.equal(result.status, 0, result.stderr || result.stdout);