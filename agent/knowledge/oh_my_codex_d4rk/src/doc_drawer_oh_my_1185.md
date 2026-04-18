dbox'],
        { PATH: `${fakeBin}:${process.env.PATH || ''}`, OMX_TEST_REPO_ROOT: repo },
      );

      assert.equal(result.status, 0, result.stderr || result.stdout);
      assert.match(result.stderr, /fake-codex:exec --dangerously-bypass-approvals-and-sandbox -/);
    } finally {
      await rm(repo, { recursive: true, force: true });
      await rm(fakeBin, { recursive: true, force: true });
    }
  });