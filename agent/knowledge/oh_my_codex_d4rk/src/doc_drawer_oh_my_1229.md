onfig.json'), JSON.stringify({
        name: 'eta',
        tmux_session: 'omx-team-eta',
      }));

      await writeFile(join(stateDir, 'hud-state.json'), JSON.stringify({
        last_turn_at: new Date(Date.now() - 300_000).toISOString(),
        turn_count: 5,
      }));
      await writeFile(join(stateDir, 'leader-runtime-activity.json'), JSON.stringify({
        last_activity_at: new Date(Date.now() - 5_000).toISOString(),
        last_source: 'team_status',
        last_team_name: 'eta',
      }));