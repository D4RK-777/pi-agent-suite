; exit 1; fi\nexit 0\n',
      );
      spawnSync('chmod', ['+x', tmuxPath], { encoding: 'utf-8' });

      const res = runOmx(wd, ['doctor', '--team'], { PATH: `${fakeBin}:${process.env.PATH || ''}` });
      if (shouldSkipForSpawnPermissions(res.error)) return;
      assert.equal(res.status, 0, res.stderr || res.stdout);
      assert.doesNotMatch(res.stdout, /orphan_tmux_session/);
    } finally {
      await rm(wd, { recursive: true, force: true });
    }
  });
});