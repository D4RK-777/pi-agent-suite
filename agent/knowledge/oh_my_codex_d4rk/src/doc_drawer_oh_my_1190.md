te.json'), 'utf-8')) as {
        active: boolean;
      };
      assert.equal(state.active, false);

      const logsRoot = join(repo, '.omx', 'logs', 'autoresearch');
      const [runId] = readdirSync(logsRoot, { withFileTypes: true })
        .filter(d => d.isDirectory())
        .map(d => d.name);
      assert.ok(runId);

      const manifest = JSON.parse(await readFile(join(logsRoot, runId, 'manifest.json'), 'utf-8')) as {
        status: string;
        stop_reason: string | null;
        completed_at: string | null;
      };
      assert.equal(manifest.status, 'stopped');
      assert.equal(manifest.stop_reason, 'repeated noop limit reached (3)');
      assert.match(manifest.completed_at || '', /^\d{4}-\d{2}-\d{2}T/);