const fallbackEvent = buildDeadWorkerAwaitEvent(name, snapshot);
            return fallbackEvent
              ? { status: 'event' as const, cursor: baselineCursor, event: fallbackEvent }
              : { status: 'timeout' as const, cursor: baselineCursor };
          })
          : await waitForTeamEvent(name, cwd, {
            afterEventId: baselineCursor || undefined,
            timeoutMs,
            pollMs: 100,
            wakeableOnly: true,
          });

    if (wantsJson) {
      console.log(JSON.stringify({
        team_name: sanitizeTeamName(name),
        status: result.status,
        cursor: result.cursor,
        event: result.event ?? null,
      }));
      return;
    }