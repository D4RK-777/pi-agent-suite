on'), JSON.stringify({
        name: 'epsilon',
        tmux_session: 'omx-team-epsilon',
      }));

      // Stale HUD state (leader inactive for 5 minutes)
      await writeFile(join(wd, '.omx', 'state', 'hud-state.json'), JSON.stringify({
        last_turn_at: new Date(Date.now() - 300_000).toISOString(),
        turn_count: 5,
      }));

      const fakeBin = join(wd, 'bin');
      await mkdir(fakeBin, { recursive: true });
      const tmuxPath = join(fakeBin, 'tmux');
      // Fake tmux reports the team session exists
      await writeFile(tmuxPath, '#!/bin/sh\nif [ "$1" = "list-sessions" ]; then echo "omx-team-epsilon"; exit 0; fi\nexit 0\n');
      spawnSync('chmod', ['+x', tmuxPath], { encoding: 'utf-8' });