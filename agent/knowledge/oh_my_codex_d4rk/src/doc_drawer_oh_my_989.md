rEventId: baselineCursor || undefined,
      wakeableOnly: true,
    }).then((events) => events[0]);

    const result =
      immediateEvent
        ? { status: 'event' as const, cursor: immediateEvent.event_id, event: immediateEvent }
        : snapshot && snapshotHasDeadWorkerStall(snapshot)
          ? await readTeamEvents(name, cwd, { wakeableOnly: true }).then((events) => {
            const latestWakeableEvent = events.at(-1);
            if (latestWakeableEvent) {
              return {
                status: 'event' as const,
                cursor: latestWakeableEvent.event_id,
                event: latestWakeableEvent,
              };
            }
            const fallbackEvent = buildDeadWorkerAwaitEvent(name, snapshot);
            return fallbackEvent