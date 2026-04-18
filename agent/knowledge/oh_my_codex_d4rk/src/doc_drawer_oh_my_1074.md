session_id: 'session-1',
          started_at: new Date().toISOString(),
          cwd: wd,
          pid: process.pid,
          pid_start_ticks: pidStartTicks,
        }, null, 2),
      );

      await withCwd(wd, async () => {
        await agentsInit({ force: true });
      });

      assert.equal(await readFile(join(wd, 'AGENTS.md'), 'utf-8'), '# unmanaged\n');
      assert.equal(existsSync(join(wd, 'src', 'AGENTS.md')), true);
    } finally {
      await rm(wd, { recursive: true, force: true });
    }
  });