ed noop limit reached (3)');
      assert.match(manifest.completed_at || '', /^\d{4}-\d{2}-\d{2}T/);

      const ledger = JSON.parse(await readFile(join(logsRoot, runId, 'iteration-ledger.json'), 'utf-8')) as {
        entries: Array<{ decision: string }>;
      };
      assert.deepEqual(ledger.entries.map((entry) => entry.decision), ['baseline', 'noop', 'noop', 'noop']);

      const resumeResult = runOmx(repo, ['autoresearch', '--resume', runId]);
      assert.notEqual(resumeResult.status, 0, resumeResult.stderr || resumeResult.stdout);
      assert.match(`${resumeResult.stderr}\n${resumeResult.stdout}`, /autoresearch_resume_terminal_run/i);
    } finally {
      await rm(repo, { recursive: true, force: true });
      await rm(fakeBin, { recursive: true, force: true });
    }
  });
});