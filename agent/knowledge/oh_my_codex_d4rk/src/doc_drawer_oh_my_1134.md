tf-8');
      const sandboxContent = await readFile(join(result.missionDir, 'sandbox.md'), 'utf-8');

      assert.equal(result.slug, 'ux-eval');
      assert.match(draftContent, /Launch-ready: yes/);
      assert.match(resultContent, /"launchReady": true/);
      assert.match(missionContent, /Improve evaluator UX/);
      assert.match(sandboxContent, /command: node scripts\/eval\.js/);
      assert.match(sandboxContent, /keep_policy: pass_only/);
    } finally {
      await rm(repo, { recursive: true, force: true });
    }
  });