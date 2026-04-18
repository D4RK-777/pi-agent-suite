slug: 'onboarding-friction',
        seedInputs: { topic: 'Measure onboarding friction' },
      });

      assert.match(artifacts.draftArtifactPath, /deep-interview-autoresearch-onboarding-friction\.md$/);
      assert.match(artifacts.missionArtifactPath, /autoresearch-onboarding-friction\/mission\.md$/);
      assert.match(artifacts.sandboxArtifactPath, /autoresearch-onboarding-friction\/sandbox\.md$/);
      assert.match(artifacts.resultPath, /autoresearch-onboarding-friction\/result\.json$/);