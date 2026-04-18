ovement',
        seedInputs: { topic: 'Improve onboarding for first-time contributors' },
      });

      assert.match(artifact.path, /\.omx\/specs\/deep-interview-autoresearch-improve-onboarding-for-first-time-contributors\.md$/);
      assert.equal(artifact.launchReady, false);
      assert.match(artifact.content, /## Mission Draft/);
      assert.match(artifact.content, /## Evaluator Draft/);
      assert.match(artifact.content, /## Launch Readiness/);
      assert.match(artifact.content, /## Seed Inputs/);
      assert.match(artifact.content, /## Confirmation Bridge/);
      assert.match(artifact.content, /TODO replace with evaluator command/i);
    } finally {
      await rm(repo, { recursive: true, force: true });
    }
  });