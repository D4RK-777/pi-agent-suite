AUTO_UPDATE: '0',
        OMX_NOTIFY_FALLBACK: '0',
        OMX_HOOK_DERIVED_SIGNALS: '0',
      });

      assert.equal(result.status, 0, result.error || result.stderr || result.stdout);
      assert.match(result.stdout, /fake-codex:exec --model gpt-5 say hi /);
      assert.match(result.stdout, /instructions-path:.*\/\.omx\/state\/sessions\/omx-.*\/AGENTS\.md/);
      assert.match(result.stdout, /# User Instructions/);
      assert.match(result.stdout, /# Project Instructions/);
      assert.match(result.stdout, /<!-- OMX:RUNTIME:START -->/);