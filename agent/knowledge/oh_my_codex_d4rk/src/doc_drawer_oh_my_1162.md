TMUX_PANE: '%42',
      });
      assert.equal(result.status, 0, result.stderr || result.stdout);

      const codexArgs = await readFile(codexLog, 'utf-8');
      const tmuxOutput = await readFile(tmuxLog, 'utf-8');
      assert.match(codexArgs, /\$deep-interview --autoresearch/);
      assert.match(tmuxOutput, /split-window -h -t %42 -d -P -F #\{pane_id\} -c/);

      const missionContent = await readFile(join(repo, 'missions', 'test-launch', 'mission.md'), 'utf-8');
      const sandboxContent = await readFile(join(repo, 'missions', 'test-launch', 'sandbox.md'), 'utf-8');
      assert.match(missionContent, /Investigate flaky onboarding behavior/);
      assert.match(sandboxContent, /command: node scripts\/eval\.js/);
    } finally {