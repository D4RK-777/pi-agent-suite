;
      } else {
        console.log(`No team state found for ${name}`);
      }
      return;
    }

    const baselineCursor = afterEventId || (await readTeamEvents(name, cwd, { wakeableOnly: true }).then((events) => events.at(-1)?.event_id ?? ''));
    const snapshot = await monitorTeam(name, cwd);
    const immediateEvent = await readTeamEvents(name, cwd, {
      afterEventId: baselineCursor || undefined,
      wakeableOnly: true,
    }).then((events) => events[0]);