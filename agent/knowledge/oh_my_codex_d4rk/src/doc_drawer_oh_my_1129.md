.md$/);
      assert.match(artifacts.resultPath, /autoresearch-onboarding-friction\/result\.json$/);

      const resolved = await resolveAutoresearchDeepInterviewResult(repo, { slug: 'onboarding-friction' });
      assert.ok(resolved);
      assert.equal(resolved?.compileTarget.slug, 'onboarding-friction');
      assert.equal(resolved?.compileTarget.keepPolicy, 'pass_only');
      assert.equal(resolved?.launchReady, true);
      assert.match(resolved?.missionContent || '', /Measure onboarding friction/);
      assert.match(resolved?.sandboxContent || '', /command: node scripts\/eval\.js/);
    } finally {
      await rm(repo, { recursive: true, force: true });
    }
  });
});