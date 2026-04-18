TMUX_PANE: '%9',
      });
      assert.equal(result.status, 0, result.stderr || result.stdout);

      const tmuxOutput = await readFile(tmuxLog, 'utf-8');
      assert.match(tmuxOutput, /split-window -h -t %9 -d -P -F #\{pane_id\} -c/);
      assert.match(tmuxOutput, /'autoresearch' '\/tmp\/[^']+\/missions\/demo' '--model' 'gpt-5'/);
      assert.doesNotMatch(tmuxOutput, /kill-pane -t %9/);
    } finally {
      await rm(repo, { recursive: true, force: true });
      await rm(fakeBin, { recursive: true, force: true });
    }
  });